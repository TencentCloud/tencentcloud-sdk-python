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


class Account(AbstractModel):
    """数据库账号信息

    """

    def __init__(self):
        """
        :param User: 新账户的名称
        :type User: str
        :param Host: 新账户的域名
        :type Host: str
        """
        self.User = None
        self.Host = None


    def _deserialize(self, params):
        self.User = params.get("User")
        self.Host = params.get("Host")


class AccountInfo(AbstractModel):
    """账号详细信息

    """

    def __init__(self):
        """
        :param Notes: 账号备注信息
        :type Notes: str
        :param Host: 账号的域名
        :type Host: str
        :param User: 账号的名称
        :type User: str
        :param ModifyTime: 账号信息修改时间
        :type ModifyTime: str
        :param ModifyPasswordTime: 修改密码的时间
        :type ModifyPasswordTime: str
        :param CreateTime: 账号的创建时间
        :type CreateTime: str
        """
        self.Notes = None
        self.Host = None
        self.User = None
        self.ModifyTime = None
        self.ModifyPasswordTime = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Notes = params.get("Notes")
        self.Host = params.get("Host")
        self.User = params.get("User")
        self.ModifyTime = params.get("ModifyTime")
        self.ModifyPasswordTime = params.get("ModifyPasswordTime")
        self.CreateTime = params.get("CreateTime")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组Id。
        :type SecurityGroupId: str
        :param InstanceIds: 实例ID列表，一个或者多个实例Id组成的数组。
        :type InstanceIds: list of str
        """
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BackupConfig(AbstractModel):
    """ECDB第二个从库的配置信息，只有ECDB实例才有这个字段

    """

    def __init__(self):
        """
        :param ReplicationMode: 第二个从库复制方式，可能的返回值：async-异步，semisync-半同步
        :type ReplicationMode: str
        :param Zone: 第二个从库可用区的正式名称，如ap-shanghai-1
        :type Zone: str
        :param Vip: 第二个从库内网IP地址
        :type Vip: str
        :param Vport: 第二个从库访问端口
        :type Vport: str
        """
        self.ReplicationMode = None
        self.Zone = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.ReplicationMode = params.get("ReplicationMode")
        self.Zone = params.get("Zone")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class BackupInfo(AbstractModel):
    """备份详细信息

    """

    def __init__(self):
        """
        :param Name: 备份文件名
        :type Name: str
        :param Size: 备份文件大小，单位：Byte
        :type Size: int
        :param Date: 备份快照时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 内网下载地址
        :type IntranetUrl: str
        :param InternetUrl: 外网下载地址
        :type InternetUrl: str
        :param Type: 日志具体类型，可能的值有：logic - 逻辑冷备，physical - 物理冷备
        :type Type: str
        :param BackupId: 备份子任务的ID，删除备份文件时使用
        :type BackupId: int
        :param Status: 备份任务状态
        :type Status: str
        :param FinishTime: 备份任务的完成时间
        :type FinishTime: str
        :param Creator: 备份的创建者，可能的值：SYSTEM - 系统创建，Uin - 发起者Uin值
        :type Creator: str
        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None
        self.BackupId = None
        self.Status = None
        self.FinishTime = None
        self.Creator = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")
        self.BackupId = params.get("BackupId")
        self.Status = params.get("Status")
        self.FinishTime = params.get("FinishTime")
        self.Creator = params.get("Creator")


class BinlogInfo(AbstractModel):
    """二进制日志信息

    """

    def __init__(self):
        """
        :param Name: 备份文件名
        :type Name: str
        :param Size: 备份文件大小，单位：Byte
        :type Size: int
        :param Date: 备份快照时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 内网下载地址
        :type IntranetUrl: str
        :param InternetUrl: 外网下载地址
        :type InternetUrl: str
        :param Type: 日志具体类型，可能的值有：binlog - 二进制日志
        :type Type: str
        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")


class CloseWanServiceRequest(AbstractModel):
    """CloseWanService请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class CloseWanServiceResponse(AbstractModel):
    """CloseWanService返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """列权限信息

    """

    def __init__(self):
        """
        :param Database: 数据库名
        :type Database: str
        :param Table: 数据库表名
        :type Table: str
        :param Column: 数据库列名
        :type Column: str
        :param Privileges: 权限信息
        :type Privileges: list of str
        """
        self.Database = None
        self.Table = None
        self.Column = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Column = params.get("Column")
        self.Privileges = params.get("Privileges")


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Accounts: 云数据库账号。
        :type Accounts: list of Account
        :param Password: 新账户的密码。
        :type Password: str
        :param Description: 备注信息。
        :type Description: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.Password = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Password = params.get("Password")
        self.Description = params.get("Description")


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param BackupMethod: 目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备。
        :type BackupMethod: str
        """
        self.InstanceId = None
        self.BackupMethod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        """
        :param BackupId: 备份任务ID。
        :type BackupId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.BackupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupId = params.get("BackupId")
        self.RequestId = params.get("RequestId")


class CreateDBImportJobRequest(AbstractModel):
    """CreateDBImportJob请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例的ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param FileName: 文件名称。
        :type FileName: str
        :param User: 云数据库的用户名。
        :type User: str
        :param Password: 云数据库实例User账号的密码。
        :type Password: str
        :param DbName: 导入的目标数据库名，不传表示不指定数据库。
        :type DbName: str
        """
        self.InstanceId = None
        self.FileName = None
        self.User = None
        self.Password = None
        self.DbName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FileName = params.get("FileName")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.DbName = params.get("DbName")


class CreateDBImportJobResponse(AbstractModel):
    """CreateDBImportJob返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为100
        :type GoodsNum: int
        :param Memory: 实例内存大小，单位：MB，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的内存规格
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的硬盘范围
        :type Volume: int
        :param EngineVersion: MySQL版本，值包括：5.5、5.6和5.7，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的实例版本
        :type EngineVersion: str
        :param UniqVpcId: 私有网络ID，如果不传则默认选择基础网络，请使用[查询私有网络列表](/document/api/215/15778)
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络下的子网ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/document/api/215/15784)
        :type UniqSubnetId: str
        :param ProjectId: 项目ID，不填为默认项目。请使用[查询项目列表](https://cloud.tencent.com/document/product/378/4400)接口获取项目ID
        :type ProjectId: int
        :param Zone: 可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的可用区
        :type Zone: str
        :param MasterInstanceId: 实例ID，购买只读实例或者灾备实例时必填，该字段表示只读实例或者灾备实例的主实例ID，请使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询云数据库实例ID
        :type MasterInstanceId: str
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例
        :type InstanceRole: str
        :param MasterRegion: 主实例的可用区信息，购买灾备实例时必填
        :type MasterRegion: str
        :param Port: 自定义端口，端口支持范围：[ 1024-65535 ]
        :type Port: int
        :param Password: 设置root帐号密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type Password: str
        :param ParamList: 参数列表，参数格式如ParamList.0.Name=auto_increment_increment&ParamList.0.Value=1。可通过[查询参数列表](/document/product/236/6369)查询支持设置的参数
        :type ParamList: list of ParamInfo
        :param ProtectMode: 数据复制方式，默认为0，支持值包括：0-表示异步复制，1-表示半同步复制，2-表示强同步复制，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type ProtectMode: int
        :param DeployMode: 多可用区域，默认为0，支持值包括：0-表示单可用区，1-表示多可用区，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type DeployMode: int
        :param SlaveZone: 备库1的可用区ID，默认为zoneId的值，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type SlaveZone: str
        :param BackupZone: 备库2的可用区ID，默认为0，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type BackupZone: str
        :param SecurityGroup: 安全组参数，可使用[查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850)接口查询某个项目的安全组详情
        :type SecurityGroup: list of str
        :param RoGroup: 只读实例信息
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param AutoRenewFlag: 自动续费标记，值为0或1。购买按量计费实例该字段无意义
        :type AutoRenewFlag: int
        :param InstanceName: 实例名称
        :type InstanceName: str
        """
        self.GoodsNum = None
        self.Memory = None
        self.Volume = None
        self.EngineVersion = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ProjectId = None
        self.Zone = None
        self.MasterInstanceId = None
        self.InstanceRole = None
        self.MasterRegion = None
        self.Port = None
        self.Password = None
        self.ParamList = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.BackupZone = None
        self.SecurityGroup = None
        self.RoGroup = None
        self.AutoRenewFlag = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.EngineVersion = params.get("EngineVersion")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Zone = params.get("Zone")
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.MasterRegion = params.get("MasterRegion")
        self.Port = params.get("Port")
        self.Password = params.get("Password")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")
        self.SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self.RoGroup = RoGroup()
            self.RoGroup._deserialize(params.get("RoGroup"))
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.InstanceName = params.get("InstanceName")


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 短订单ID
        :type DealIds: list of str
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Memory: 实例内存大小，单位：MB，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的内存规格
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的硬盘范围
        :type Volume: int
        :param Period: 实例时长，单位：月，可选值包括[1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为100
        :type GoodsNum: int
        :param Zone: 可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的可用区
        :type Zone: str
        :param UniqVpcId: 私有网络ID，如果不传则默认选择基础网络，请使用[查询私有网络列表](/document/api/215/15778)
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络下的子网ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/document/api/215/15784)
        :type UniqSubnetId: str
        :param ProjectId: 项目ID，不填为默认项目。请使用[查询项目列表](https://cloud.tencent.com/document/product/378/4400)接口获取项目ID
        :type ProjectId: int
        :param Port: 自定义端口，端口支持范围：[ 1024-65535 ]
        :type Port: int
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例
        :type InstanceRole: str
        :param MasterInstanceId: 实例ID，购买只读实例时必填，该字段表示只读实例的主实例ID，请使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询云数据库实例ID
        :type MasterInstanceId: str
        :param EngineVersion: MySQL版本，值包括：5.5、5.6和5.7，请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口获取可创建的实例版本
        :type EngineVersion: str
        :param Password: 设置root帐号密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type Password: str
        :param ProtectMode: 数据复制方式，默认为0，支持值包括：0-表示异步复制，1-表示半同步复制，2-表示强同步复制
        :type ProtectMode: int
        :param DeployMode: 多可用区域，默认为0，支持值包括：0-表示单可用区，1-表示多可用区
        :type DeployMode: int
        :param SlaveZone: 备库1的可用区信息，默认为zone的值
        :type SlaveZone: str
        :param ParamList: 参数列表，参数格式如ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过[查询参数列表](/document/product/236/6369)查询支持设置的参数
        :type ParamList: list of ParamInfo
        :param BackupZone: 备库2的可用区ID，默认为0，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type BackupZone: str
        :param AutoRenewFlag: 自动续费标记，可选值为：0-不自动续费；1-自动续费
        :type AutoRenewFlag: int
        :param MasterRegion: 主实例地域信息，购买灾备实例时，该字段必填
        :type MasterRegion: str
        :param SecurityGroup: 安全组参数，可使用[查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850)接口查询某个项目的安全组详情
        :type SecurityGroup: list of str
        :param RoGroup: 只读实例参数
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param InstanceName: 实例名称
        :type InstanceName: str
        """
        self.Memory = None
        self.Volume = None
        self.Period = None
        self.GoodsNum = None
        self.Zone = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ProjectId = None
        self.Port = None
        self.InstanceRole = None
        self.MasterInstanceId = None
        self.EngineVersion = None
        self.Password = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.ParamList = None
        self.BackupZone = None
        self.AutoRenewFlag = None
        self.MasterRegion = None
        self.SecurityGroup = None
        self.RoGroup = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.Period = params.get("Period")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Port = params.get("Port")
        self.InstanceRole = params.get("InstanceRole")
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.EngineVersion = params.get("EngineVersion")
        self.Password = params.get("Password")
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.BackupZone = params.get("BackupZone")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.MasterRegion = params.get("MasterRegion")
        self.SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self.RoGroup = RoGroup()
            self.RoGroup._deserialize(params.get("RoGroup"))
        self.InstanceName = params.get("InstanceName")


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 短订单ID
        :type DealIds: list of str
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DBSwitchInfo(AbstractModel):
    """云数据库切换记录

    """

    def __init__(self):
        """
        :param SwitchTime: 切换时间，格式为：2017-09-03 01:34:31
        :type SwitchTime: str
        :param SwitchType: 切换类型，可能的返回值为：TRANSFER - 数据迁移；MASTER2SLAVE - 主备切换；RECOVERY - 主从恢复
        :type SwitchType: str
        """
        self.SwitchTime = None
        self.SwitchType = None


    def _deserialize(self, params):
        self.SwitchTime = params.get("SwitchTime")
        self.SwitchType = params.get("SwitchType")


class DatabaseName(AbstractModel):
    """数据库表名

    """

    def __init__(self):
        """
        :param DatabaseName: 数据库表名
        :type DatabaseName: str
        """
        self.DatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")


class DatabasePrivilege(AbstractModel):
    """数据库权限

    """

    def __init__(self):
        """
        :param Privileges: 权限信息
        :type Privileges: list of str
        :param Database: 数据库名
        :type Database: str
        """
        self.Privileges = None
        self.Database = None


    def _deserialize(self, params):
        self.Privileges = params.get("Privileges")
        self.Database = params.get("Database")


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Accounts: 云数据库账号。
        :type Accounts: list of Account
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param BackupId: 备份任务ID。该任务ID为[创建云数据库备份](https://cloud.tencent.com/document/api/236/15844)接口返回的任务ID。
        :type BackupId: int
        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param User: 数据库的账号名称。
        :type User: str
        :param Host: 数据库的账号域名。
        :type Host: str
        """
        self.InstanceId = None
        self.User = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.Host = params.get("Host")


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param GlobalPrivileges: 全局权限数组。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 数据库权限数组。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: 数据库中的表权限数组。
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: 数据库表中的列权限数组。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self.ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self.ColumnPrivileges.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的账号数量。
        :type TotalCount: int
        :param Items: 符合查询条件的账号详细信息。
        :type Items: list of AccountInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID。
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务执行结果。可能的取值：INITIAL - 初始化，RUNNING - 运行中，SUCCESS - 执行成功，FAILED - 执行失败，KILLED - 已终止，REMOVED - 已删除，PAUSED - 终止中。
        :type Status: str
        :param Info: 任务执行信息描述。
        :type Info: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例短实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param StartTimeMin: 备份开始的最早时间点，单位为时刻。例如，2 - 凌晨2:00
        :type StartTimeMin: int
        :param StartTimeMax: 备份开始的最晚时间点，单位为时刻。例如，6 - 凌晨6:00
        :type StartTimeMax: int
        :param BackupExpireDays: 备份过期时间，单位为天
        :type BackupExpireDays: int
        :param BackupMethod: 备份方式，可能的值为：physical - 物理备份，logical - 逻辑备份
        :type BackupMethod: str
        :param BinlogExpireDays: Binlog过期时间，单位为天
        :type BinlogExpireDays: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.StartTimeMin = None
        self.StartTimeMax = None
        self.BackupExpireDays = None
        self.BackupMethod = None
        self.BinlogExpireDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTimeMin = params.get("StartTimeMin")
        self.StartTimeMax = params.get("StartTimeMax")
        self.BackupExpireDays = params.get("BackupExpireDays")
        self.BackupMethod = params.get("BackupMethod")
        self.BinlogExpireDays = params.get("BinlogExpireDays")
        self.RequestId = params.get("RequestId")


class DescribeBackupDatabasesRequest(AbstractModel):
    """DescribeBackupDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param StartTime: 开始时间，格式为：2017-07-12 10:29:20。
        :type StartTime: str
        :param SearchDatabase: 要查询的数据库名前缀。
        :type SearchDatabase: str
        :param Offset: 分页偏移量。
        :type Offset: int
        :param Limit: 分页大小，最小值为1，最大值为2000。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.SearchDatabase = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.SearchDatabase = params.get("SearchDatabase")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBackupDatabasesResponse(AbstractModel):
    """DescribeBackupDatabases返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的数据个数
        :type TotalCount: int
        :param Items: 符合查询条件的数据库数组
        :type Items: list of DatabaseName
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DatabaseName()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupTablesRequest(AbstractModel):
    """DescribeBackupTables请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param StartTime: 开始时间，格式为：2017-07-12 10:29:20。
        :type StartTime: str
        :param DatabaseName: 指定的数据库名。
        :type DatabaseName: str
        :param SearchTable: 要查询的数据表名前缀。
        :type SearchTable: str
        :param Offset: 分页偏移。
        :type Offset: int
        :param Limit: 分页大小，最小值为1，最大值为2000。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.DatabaseName = None
        self.SearchTable = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.DatabaseName = params.get("DatabaseName")
        self.SearchTable = params.get("SearchTable")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBackupTablesResponse(AbstractModel):
    """DescribeBackupTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的数据个数。
        :type TotalCount: int
        :param Items: 符合条件的数据表数组。
        :type Items: list of TableName
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = TableName()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值为0。
        :type Offset: int
        :param Limit: 分页大小，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param Items: 符合查询条件的备份信息详情
        :type Items: list of BackupInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值为0。
        :type Offset: int
        :param Limit: 分页大小，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的日志文件总数
        :type TotalCount: int
        :param Items: 符合查询条件的二进制日志文件详情
        :type Items: list of BinlogInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = BinlogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBImportRecordsRequest(AbstractModel):
    """DescribeDBImportRecords请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param StartTime: 开始时间，时间格式如：2016-01-01 00:00:01。
        :type StartTime: str
        :param EndTime: 结束时间，时间格式如：2016-01-01 23:59:59。
        :type EndTime: str
        :param Offset: 分页参数 , 偏移量 , 默认值为0。
        :type Offset: int
        :param Limit: 分页参数 , 单次请求返回的数量 , 默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDBImportRecordsResponse(AbstractModel):
    """DescribeDBImportRecords返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的导入任务操作日志总数。
        :type TotalCount: int
        :param Items: 返回的导入操作记录列表。
        :type Items: list of ImportRecord
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ImportRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceCharsetRequest(AbstractModel):
    """DescribeDBInstanceCharset请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBInstanceCharsetResponse(AbstractModel):
    """DescribeDBInstanceCharset返回参数结构体

    """

    def __init__(self):
        """
        :param Charset: 实例的默认字符集，如"latin1", "utf8"等。
        :type Charset: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Charset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Charset = params.get("Charset")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceConfigRequest(AbstractModel):
    """DescribeDBInstanceConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBInstanceConfigResponse(AbstractModel):
    """DescribeDBInstanceConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ProtectMode: 主库数据保护方式，主实例属性，可能的返回值：0-异步复制方式，1-半同步复制方式，2-强同步复制方式。
        :type ProtectMode: int
        :param DeployMode: 主库部署方式，主实例属性，可能的返回值：0-单可用部署，1-多可用区部署。
        :type DeployMode: int
        :param Zone: 主库可用区的正式名称，如ap-shanghai-1。
        :type Zone: str
        :param SlaveConfig: 从库的配置信息。
        :type SlaveConfig: :class:`tencentcloud.cdb.v20170320.models.SlaveConfig`
        :param BackupConfig: ECDB第二个从库的配置信息，只有ECDB实例才有这个字段。
        :type BackupConfig: :class:`tencentcloud.cdb.v20170320.models.BackupConfig`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ProtectMode = None
        self.DeployMode = None
        self.Zone = None
        self.SlaveConfig = None
        self.BackupConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.Zone = params.get("Zone")
        if params.get("SlaveConfig") is not None:
            self.SlaveConfig = SlaveConfig()
            self.SlaveConfig._deserialize(params.get("SlaveConfig"))
        if params.get("BackupConfig") is not None:
            self.BackupConfig = BackupConfig()
            self.BackupConfig._deserialize(params.get("BackupConfig"))
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceGTIDRequest(AbstractModel):
    """DescribeDBInstanceGTID请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBInstanceGTIDResponse(AbstractModel):
    """DescribeDBInstanceGTID返回参数结构体

    """

    def __init__(self):
        """
        :param IsGTIDOpen: GTID是否开通的标记：0-未开通，1-已开通。
        :type IsGTIDOpen: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.IsGTIDOpen = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsGTIDOpen = params.get("IsGTIDOpen")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceRebootTimeRequest(AbstractModel):
    """DescribeDBInstanceRebootTime请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例的ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeDBInstanceRebootTimeResponse(AbstractModel):
    """DescribeDBInstanceRebootTime返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 返回的参数信息。
        :type Items: list of InstanceRebootTime
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceRebootTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID，可使用[查询项目列表](https://cloud.tencent.com/document/product/378/4400)接口查询项目ID
        :type ProjectId: int
        :param InstanceTypes: 实例类型，可取值：1-主实例，2-灾备实例，3-只读实例
        :type InstanceTypes: list of int non-negative
        :param Vips: 实例的内网IP地址
        :type Vips: list of str
        :param Status: 实例状态，可取值：0-创建中，1-运行中，4-隔离中，5-已隔离
        :type Status: list of int non-negative
        :param Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最大值为2000
        :type Limit: int
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param PayTypes: 付费类型，可取值：0-包年包月，1-小时计费
        :type PayTypes: list of int non-negative
        :param InstanceNames: 实例名称
        :type InstanceNames: list of str
        :param TaskStatus: 实例任务状态，可能取值：<br>0-没有任务<br>1-升级中<br>2-数据导入中<br>3-开放Slave中<br>4-外网访问开通中<br>5-批量操作执行中<br>6-回档中<br>7-外网访问关闭中<br>8-密码修改中<br>9-实例名修改中<br>10-重启中<br>12-自建迁移中<br>13-删除库表中<br>14-灾备实例创建同步中
        :type TaskStatus: list of int non-negative
        :param EngineVersions: 实例数据库引擎版本，可能取值：5.1、5.5、5.6和5.7
        :type EngineVersions: list of str
        :param VpcIds: 私有网络的ID
        :type VpcIds: list of int non-negative
        :param ZoneIds: 可用区的ID
        :type ZoneIds: list of int non-negative
        :param SubnetIds: 子网ID
        :type SubnetIds: list of int non-negative
        :param CdbErrors: 是否锁定标记
        :type CdbErrors: list of int
        :param OrderBy: 排序的字段，目前支持："InstanceId", "InstanceName", "CreateTime", "DeadlineTime"
        :type OrderBy: str
        :param OrderDirection: 排序方式，目前支持："ASC"或者"DESC"
        :type OrderDirection: str
        :param WithSecurityGroup: 是否包含安全组信息，可取值：0-不包含，1-包含
        :type WithSecurityGroup: int
        :param WithExCluster: 是否包含独享集群信息，可取值：0-不包含，1-包含
        :type WithExCluster: int
        :param ExClusterId: 独享集群ID
        :type ExClusterId: str
        :param InstanceIds: 实例ID
        :type InstanceIds: list of str
        :param InitFlag: 初始化标记，可取值：0-未初始化，1-初始化
        :type InitFlag: int
        :param WithDr: 是否包含灾备实例，可取值：0-不包含，1-包含
        :type WithDr: int
        :param WithRo: 是否包含只读实例，可取值：0-不包含，1-包含
        :type WithRo: int
        :param WithMaster: 是否包含主实例，可取值：0-不包含，1-包含
        :type WithMaster: int
        """
        self.ProjectId = None
        self.InstanceTypes = None
        self.Vips = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.SecurityGroupId = None
        self.PayTypes = None
        self.InstanceNames = None
        self.TaskStatus = None
        self.EngineVersions = None
        self.VpcIds = None
        self.ZoneIds = None
        self.SubnetIds = None
        self.CdbErrors = None
        self.OrderBy = None
        self.OrderDirection = None
        self.WithSecurityGroup = None
        self.WithExCluster = None
        self.ExClusterId = None
        self.InstanceIds = None
        self.InitFlag = None
        self.WithDr = None
        self.WithRo = None
        self.WithMaster = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.Vips = params.get("Vips")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.PayTypes = params.get("PayTypes")
        self.InstanceNames = params.get("InstanceNames")
        self.TaskStatus = params.get("TaskStatus")
        self.EngineVersions = params.get("EngineVersions")
        self.VpcIds = params.get("VpcIds")
        self.ZoneIds = params.get("ZoneIds")
        self.SubnetIds = params.get("SubnetIds")
        self.CdbErrors = params.get("CdbErrors")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        self.WithSecurityGroup = params.get("WithSecurityGroup")
        self.WithExCluster = params.get("WithExCluster")
        self.ExClusterId = params.get("ExClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InitFlag = params.get("InitFlag")
        self.WithDr = params.get("WithDr")
        self.WithRo = params.get("WithRo")
        self.WithMaster = params.get("WithMaster")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param Items: 实例详细信息
        :type Items: list of InstanceInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBPriceRequest(AbstractModel):
    """DescribeDBPrice请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区信息，格式如"ap-guangzhou-1"
        :type Zone: str
        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为100
        :type GoodsNum: int
        :param Memory: 实例内存大小，单位：MB
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param PayType: 付费类型，支持值包括：PRE_PAID - 包年包月，HOUR_PAID - 按量计费
        :type PayType: str
        :param Period: 实例时长，单位：月，最小值1，最大值为36；查询按量计费价格时，该字段无效
        :type Period: int
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master-表示主实例，ro-表示只读实例，dr-表示灾备实例
        :type InstanceRole: str
        :param ProtectMode: 数据复制方式，默认为0，支持值包括：0-表示异步复制，1-表示半同步复制，2-表示强同步复制
        :type ProtectMode: int
        """
        self.Zone = None
        self.GoodsNum = None
        self.Memory = None
        self.Volume = None
        self.PayType = None
        self.Period = None
        self.InstanceRole = None
        self.ProtectMode = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.GoodsNum = params.get("GoodsNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.PayType = params.get("PayType")
        self.Period = params.get("Period")
        self.InstanceRole = params.get("InstanceRole")
        self.ProtectMode = params.get("ProtectMode")


class DescribeDBPriceResponse(AbstractModel):
    """DescribeDBPrice返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 实例价格，单位：分（人民币）
        :type Price: int
        :param OriginalPrice: 实例原价，单位：分（人民币）
        :type OriginalPrice: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.OriginalPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.OriginalPrice = params.get("OriginalPrice")
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
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
        :param Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSwitchRecordsRequest(AbstractModel):
    """DescribeDBSwitchRecords请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Offset: 分页偏移量。
        :type Offset: int
        :param Limit: 分页大小，默认值为50，最小值为1，最大值为2000。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDBSwitchRecordsResponse(AbstractModel):
    """DescribeDBSwitchRecords返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例切换记录的总数。
        :type TotalCount: int
        :param Items: 实例切换记录详情。
        :type Items: list of DBSwitchInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DBSwitchInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBZoneConfigRequest(AbstractModel):
    """DescribeDBZoneConfig请求参数结构体

    """


class DescribeDBZoneConfigResponse(AbstractModel):
    """DescribeDBZoneConfig返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 可售卖地域配置数量
        :type TotalCount: int
        :param Items: 可售卖地域配置详情
        :type Items: list of RegionSellConf
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = RegionSellConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值为0。
        :type Offset: int
        :param Limit: 单次请求数量，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param DatabaseRegexp: 匹配数据库库名的正则表达式，规则同MySQL官网
        :type DatabaseRegexp: str
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.DatabaseRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DatabaseRegexp = params.get("DatabaseRegexp")


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 返回的实例信息。
        :type Items: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例的参数总数
        :type TotalCount: int
        :param Items: 参数详情
        :type Items: list of ParameterDetail
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackRangeTimeRequest(AbstractModel):
    """DescribeRollbackRangeTime请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表，单个实例Id的格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeRollbackRangeTimeResponse(AbstractModel):
    """DescribeRollbackRangeTime返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 返回的参数信息。
        :type Items: list of InstanceRollbackRangeTime
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceRollbackRangeTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值为0。
        :type Offset: int
        :param Limit: 分页大小，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的慢查询日志总数
        :type TotalCount: int
        :param Items: 符合查询条件的慢查询日志详情
        :type Items: list of SlowLogInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SlowLogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Database: 数据库的名称。
        :type Database: str
        :param Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最大值为2000。
        :type Limit: int
        :param TableRegexp: 匹配数据库表名的正则表达式，规则同MySQL官网
        :type TableRegexp: str
        """
        self.InstanceId = None
        self.Database = None
        self.Offset = None
        self.Limit = None
        self.TableRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Database = params.get("Database")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TableRegexp = params.get("TableRegexp")


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的数据库表总数。
        :type TotalCount: int
        :param Items: 返回的数据库表信息。
        :type Items: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param AsyncRequestId: 异步任务请求ID，执行 CDB 相关操作返回的 AsyncRequestId
        :type AsyncRequestId: str
        :param TaskTypes: 任务类型，不传值则查询所有任务类型，可能的值：1-数据库回档；2-SQL操作；3-数据导入；5-参数设置；6-初始化；7-重启；8-开启GTID；9-只读实例升级；10-数据库批量回档；11-主实例升级；12-删除库表；13-切换为主实例；
        :type TaskTypes: list of int
        :param TaskStatus: 任务状态，不传值则查询所有任务状态，可能的值：-1-未定义；0-初始化; 1-运行中；2-执行成功；3-执行失败；4-已终止；5-已删除；6-已暂停；
        :type TaskStatus: list of int
        :param StartTimeBegin: 第一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01
        :type StartTimeBegin: str
        :param StartTimeEnd: 最后一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01
        :type StartTimeEnd: str
        :param Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最大值为100
        :type Limit: int
        """
        self.InstanceId = None
        self.AsyncRequestId = None
        self.TaskTypes = None
        self.TaskStatus = None
        self.StartTimeBegin = None
        self.StartTimeEnd = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.TaskTypes = params.get("TaskTypes")
        self.TaskStatus = params.get("TaskStatus")
        self.StartTimeBegin = params.get("StartTimeBegin")
        self.StartTimeEnd = params.get("StartTimeEnd")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param Items: 返回的实例任务信息
        :type Items: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组Id。
        :type SecurityGroupId: str
        :param InstanceIds: 实例ID列表，一个或者多个实例Id组成的数组。
        :type InstanceIds: list of str
        """
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DrInfo(AbstractModel):
    """灾备实例信息

    """

    def __init__(self):
        """
        :param Status: 灾备实例状态
        :type Status: int
        :param Zone: 可用区信息
        :type Zone: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Region: 地域信息
        :type Region: str
        :param SyncStatus: 实例同步状态
        :type SyncStatus: int
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param InstanceType: 实例类型
        :type InstanceType: int
        """
        self.Status = None
        self.Zone = None
        self.InstanceId = None
        self.Region = None
        self.SyncStatus = None
        self.InstanceName = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.SyncStatus = params.get("SyncStatus")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")


class First(AbstractModel):
    """第一备机信息

    """

    def __init__(self):
        """
        :param Vport: 端口号
        :type Vport: int
        :param Region: 地域信息
        :type Region: str
        :param Vip: 虚拟Ip信息
        :type Vip: str
        :param Zone: 可用区信息
        :type Zone: str
        """
        self.Vport = None
        self.Region = None
        self.Vip = None
        self.Zone = None


    def _deserialize(self, params):
        self.Vport = params.get("Vport")
        self.Region = params.get("Region")
        self.Vip = params.get("Vip")
        self.Zone = params.get("Zone")


class ImportRecord(AbstractModel):
    """导入任务记录

    """

    def __init__(self):
        """
        :param Status: 状态值
        :type Status: int
        :param Code: 状态值
        :type Code: int
        :param CostTime: 执行时间
        :type CostTime: int
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param WorkId: 后端任务ID
        :type WorkId: str
        :param FileName: 导入文件名
        :type FileName: str
        :param Process: 执行进度
        :type Process: int
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param FileSize: 文件大小
        :type FileSize: str
        :param Message: 任务执行信息
        :type Message: str
        :param JobId: 任务ID
        :type JobId: int
        :param DbName: 导入库表名
        :type DbName: str
        :param AsyncRequestId: 异步任务的请求ID
        :type AsyncRequestId: str
        """
        self.Status = None
        self.Code = None
        self.CostTime = None
        self.InstanceId = None
        self.WorkId = None
        self.FileName = None
        self.Process = None
        self.CreateTime = None
        self.FileSize = None
        self.Message = None
        self.JobId = None
        self.DbName = None
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.CostTime = params.get("CostTime")
        self.InstanceId = params.get("InstanceId")
        self.WorkId = params.get("WorkId")
        self.FileName = params.get("FileName")
        self.Process = params.get("Process")
        self.CreateTime = params.get("CreateTime")
        self.FileSize = params.get("FileSize")
        self.Message = params.get("Message")
        self.JobId = params.get("JobId")
        self.DbName = params.get("DbName")
        self.AsyncRequestId = params.get("AsyncRequestId")


class Inbound(AbstractModel):
    """安全组入站规则

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT或者DROP
        :type Action: str
        :param CidrIp: 来源Ip或Ip段，例如192.168.0.0/16
        :type CidrIp: str
        :param PortRange: 端口
        :type PortRange: str
        :param IpProtocol: 网络协议，支持udp、tcp等
        :type IpProtocol: str
        :param Dir: 规则限定的方向，进站规则为INPUT
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


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        :param NewPassword: 实例新的密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：!@#$%^*()）中的两种。
        :type NewPassword: str
        :param Parameters: 实例的参数列表，目前支持设置“character_set_server”、“lower_case_table_names”参数。其中，“character_set_server”参数可选值为["utf8","latin1","gbk","utf8mb4"]；“lower_case_table_names”可选值为[“0”,“1”]。
        :type Parameters: list of ParamInfo
        :param Vport: 实例的端口，取值范围为[1024, 65535]
        :type Vport: int
        """
        self.InstanceIds = None
        self.NewPassword = None
        self.Parameters = None
        self.Vport = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewPassword = params.get("NewPassword")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.Parameters.append(obj)
        self.Vport = params.get("Vport")


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestIds: 异步任务的请求ID数组，可使用此ID查询异步任务的执行结果
        :type AsyncRequestIds: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        """
        :param WanStatus: 外网状态
        :type WanStatus: int
        :param Zone: 可用区信息
        :type Zone: str
        :param InitFlag: 初始化标志
        :type InitFlag: int
        :param RoVipInfo: 只读vip信息
        :type RoVipInfo: :class:`tencentcloud.cdb.v20170320.models.RoVipInfo`
        :param Memory: 内存容量
        :type Memory: int
        :param Status: 实例状态
        :type Status: int
        :param VpcId: 私有网络ID
        :type VpcId: int
        :param SlaveInfo: 备机信息
        :type SlaveInfo: :class:`tencentcloud.cdb.v20170320.models.SlaveInfo`
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Volume: 硬盘容量
        :type Volume: int
        :param AutoRenew: 自动续费标志
        :type AutoRenew: int
        :param ProtectMode: 数据复制方式
        :type ProtectMode: int
        :param RoGroups: 只读组信息
        :type RoGroups: list of RoGroup
        :param SubnetId: 子网ID
        :type SubnetId: int
        :param InstanceType: 实例类型
        :type InstanceType: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域信息
        :type Region: str
        :param DeadlineTime: 到期时间
        :type DeadlineTime: str
        :param DeployMode: 可用区部署方式
        :type DeployMode: int
        :param TaskStatus: 实例任务状态
        :type TaskStatus: int
        :param MasterInfo: 主实例信息
        :type MasterInfo: :class:`tencentcloud.cdb.v20170320.models.MasterInfo`
        :param DeviceType: 实例售卖机型
        :type DeviceType: str
        :param EngineVersion: 内核版本
        :type EngineVersion: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param DrInfo: 灾备实例信息
        :type DrInfo: list of DrInfo
        :param WanDomain: 外网域名
        :type WanDomain: str
        :param WanPort: 外网端口号
        :type WanPort: int
        :param PayType: 付费类型
        :type PayType: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Vip: 实例IP
        :type Vip: str
        :param Vport: 端口号
        :type Vport: int
        :param CdbError: 实例状态
        :type CdbError: int
        :param UniqVpcId: 私有网络描述符
        :type UniqVpcId: str
        :param UniqSubnetId: 子网描述符
        :type UniqSubnetId: str
        """
        self.WanStatus = None
        self.Zone = None
        self.InitFlag = None
        self.RoVipInfo = None
        self.Memory = None
        self.Status = None
        self.VpcId = None
        self.SlaveInfo = None
        self.InstanceId = None
        self.Volume = None
        self.AutoRenew = None
        self.ProtectMode = None
        self.RoGroups = None
        self.SubnetId = None
        self.InstanceType = None
        self.ProjectId = None
        self.Region = None
        self.DeadlineTime = None
        self.DeployMode = None
        self.TaskStatus = None
        self.MasterInfo = None
        self.DeviceType = None
        self.EngineVersion = None
        self.InstanceName = None
        self.DrInfo = None
        self.WanDomain = None
        self.WanPort = None
        self.PayType = None
        self.CreateTime = None
        self.Vip = None
        self.Vport = None
        self.CdbError = None
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.WanStatus = params.get("WanStatus")
        self.Zone = params.get("Zone")
        self.InitFlag = params.get("InitFlag")
        if params.get("RoVipInfo") is not None:
            self.RoVipInfo = RoVipInfo()
            self.RoVipInfo._deserialize(params.get("RoVipInfo"))
        self.Memory = params.get("Memory")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        if params.get("SlaveInfo") is not None:
            self.SlaveInfo = SlaveInfo()
            self.SlaveInfo._deserialize(params.get("SlaveInfo"))
        self.InstanceId = params.get("InstanceId")
        self.Volume = params.get("Volume")
        self.AutoRenew = params.get("AutoRenew")
        self.ProtectMode = params.get("ProtectMode")
        if params.get("RoGroups") is not None:
            self.RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self.RoGroups.append(obj)
        self.SubnetId = params.get("SubnetId")
        self.InstanceType = params.get("InstanceType")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.DeadlineTime = params.get("DeadlineTime")
        self.DeployMode = params.get("DeployMode")
        self.TaskStatus = params.get("TaskStatus")
        if params.get("MasterInfo") is not None:
            self.MasterInfo = MasterInfo()
            self.MasterInfo._deserialize(params.get("MasterInfo"))
        self.DeviceType = params.get("DeviceType")
        self.EngineVersion = params.get("EngineVersion")
        self.InstanceName = params.get("InstanceName")
        if params.get("DrInfo") is not None:
            self.DrInfo = []
            for item in params.get("DrInfo"):
                obj = DrInfo()
                obj._deserialize(item)
                self.DrInfo.append(obj)
        self.WanDomain = params.get("WanDomain")
        self.WanPort = params.get("WanPort")
        self.PayType = params.get("PayType")
        self.CreateTime = params.get("CreateTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CdbError = params.get("CdbError")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")


class InstanceRebootTime(AbstractModel):
    """实例预期重启时间

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param TimeInSeconds: 预期重启时间
        :type TimeInSeconds: int
        """
        self.InstanceId = None
        self.TimeInSeconds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeInSeconds = params.get("TimeInSeconds")


class InstanceRollbackRangeTime(AbstractModel):
    """实例可回档时间范围

    """

    def __init__(self):
        """
        :param Code: 查询数据库错误码
        :type Code: int
        :param Message: 查询数据库错误信息
        :type Message: str
        :param InstanceId: 实例ID列表，单个实例Id的格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param Times: 可回档时间范围
        :type Times: list of RollbackTimeRange
        """
        self.Code = None
        self.Message = None
        self.InstanceId = None
        self.Times = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.InstanceId = params.get("InstanceId")
        if params.get("Times") is not None:
            self.Times = []
            for item in params.get("Times"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self.Times.append(obj)


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class MasterInfo(AbstractModel):
    """主实例信息

    """

    def __init__(self):
        """
        :param Region: 地域信息
        :type Region: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param ZoneId: 可用区ID
        :type ZoneId: int
        :param Zone: 可用区信息
        :type Zone: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ResourceId: 实例长ID
        :type ResourceId: str
        :param Status: 实例状态
        :type Status: int
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param InstanceType: 实例类型
        :type InstanceType: int
        :param TaskStatus: 任务状态
        :type TaskStatus: int
        :param Memory: 内存容量
        :type Memory: int
        :param Volume: 硬盘容量
        :type Volume: int
        :param DeviceType: 实例机型
        :type DeviceType: str
        :param Qps: 每秒查询数
        :type Qps: int
        :param VpcId: 私有网络ID
        :type VpcId: int
        :param SubnetId: 子网ID
        :type SubnetId: int
        :param ExClusterId: 独享集群ID
        :type ExClusterId: str
        :param ExClusterName: 独享集群名称
        :type ExClusterName: str
        """
        self.Region = None
        self.RegionId = None
        self.ZoneId = None
        self.Zone = None
        self.InstanceId = None
        self.ResourceId = None
        self.Status = None
        self.InstanceName = None
        self.InstanceType = None
        self.TaskStatus = None
        self.Memory = None
        self.Volume = None
        self.DeviceType = None
        self.Qps = None
        self.VpcId = None
        self.SubnetId = None
        self.ExClusterId = None
        self.ExClusterName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.ResourceId = params.get("ResourceId")
        self.Status = params.get("Status")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")
        self.TaskStatus = params.get("TaskStatus")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.DeviceType = params.get("DeviceType")
        self.Qps = params.get("Qps")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ExClusterId = params.get("ExClusterId")
        self.ExClusterName = params.get("ExClusterName")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Accounts: 云数据库账号。
        :type Accounts: list of Account
        :param Description: 数据库账号的备注信息。
        :type Description: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Description = params.get("Description")


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPasswordRequest(AbstractModel):
    """ModifyAccountPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param NewPassword: 数据库账号的新密码。
        :type NewPassword: str
        :param Accounts: 云数据库账号。
        :type Accounts: list of Account
        """
        self.InstanceId = None
        self.NewPassword = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewPassword = params.get("NewPassword")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ModifyAccountPasswordResponse(AbstractModel):
    """ModifyAccountPassword返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Accounts: 数据库的账号，包括用户名和域名。
        :type Accounts: list of Account
        :param GlobalPrivileges: 全局权限。其中，GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 数据库的权限。Privileges权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: 数据库中表的权限。Privileges权限的可选值为：权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: 数据库表中列的权限。Privileges权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
        :type ColumnPrivileges: list of ColumnPrivilege
        """
        self.InstanceId = None
        self.Accounts = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self.ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self.ColumnPrivileges.append(obj)


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例的ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceIds: list of str
        :param AutoRenew: 自动续费标记，可取值的有：0-不自动续费，1-自动续费。
        :type AutoRenew: int
        """
        self.InstanceIds = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.AutoRenew = params.get("AutoRenew")


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param ExpireDays: 备份过期时间，单位为天，最小值为7天，最大值为732天。
        :type ExpireDays: int
        :param StartTime: 备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。
        :type StartTime: str
        :param BackupMethod: 目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备；默认备份方法为 逻辑冷备。
        :type BackupMethod: str
        """
        self.InstanceId = None
        self.ExpireDays = None
        self.StartTime = None
        self.BackupMethod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ExpireDays = params.get("ExpireDays")
        self.StartTime = params.get("StartTime")
        self.BackupMethod = params.get("BackupMethod")


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param InstanceName: 实例名称。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param InstanceIds: 实例ID数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        :param NewProjectId: 项目的ID。
        :type NewProjectId: int
        """
        self.InstanceIds = None
        self.NewProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewProjectId = params.get("NewProjectId")


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组Id组成的数组。
        :type SecurityGroupIds: list of str
        """
        self.InstanceId = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceVipVportRequest(AbstractModel):
    """ModifyDBInstanceVipVport请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param DstIp: 目标IP。该参数和DstPort参数，两者必传一个。
        :type DstIp: str
        :param DstPort: 目标端口，支持范围为：[1024-65535]。该参数和DstIp参数，两者必传一个。
        :type DstPort: int
        :param UniqVpcId: 私有网络统一ID。
        :type UniqVpcId: str
        :param UniqSubnetId: 子网统一ID。
        :type UniqSubnetId: str
        """
        self.InstanceId = None
        self.DstIp = None
        self.DstPort = None
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")


class ModifyDBInstanceVipVportResponse(AbstractModel):
    """ModifyDBInstanceVipVport返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务ID，可使用[查询任务列表](https://cloud.tencent.com/document/api/236/8010)获取其执行情况。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例短Id列表。
        :type InstanceIds: list of str
        :param ParamList: 要修改的参数列表。每一个元素是name和currentValue的组合。name是参数名，currentValue是要修改成的值。
        :type ParamList: list of Parameter
        """
        self.InstanceIds = None
        self.ParamList = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务Id，可用于查询任务进度。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class OpenDBInstanceGTIDRequest(AbstractModel):
    """OpenDBInstanceGTID请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OpenDBInstanceGTIDResponse(AbstractModel):
    """OpenDBInstanceGTID返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class OpenWanServiceRequest(AbstractModel):
    """OpenWanService请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OpenWanServiceResponse(AbstractModel):
    """OpenWanService返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """安全组出站规则

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT或者DROP
        :type Action: str
        :param CidrIp: 目的Ip或Ip段，例如172.16.0.0/12
        :type CidrIp: str
        :param PortRange: 端口或者端口范围
        :type PortRange: str
        :param IpProtocol: 网络协议，支持udp、tcp等
        :type IpProtocol: str
        :param Dir: 规则限定的方向，进站规则为OUTPUT
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


class ParamInfo(AbstractModel):
    """实例参数信息

    """

    def __init__(self):
        """
        :param Name: 参数名
        :type Name: str
        :param Value: 参数值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class Parameter(AbstractModel):
    """数据库实例参数

    """

    def __init__(self):
        """
        :param Name: 参数名称
        :type Name: str
        :param CurrentValue: 参数值
        :type CurrentValue: str
        """
        self.Name = None
        self.CurrentValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CurrentValue = params.get("CurrentValue")


class ParameterDetail(AbstractModel):
    """实例参数的详细描述

    """

    def __init__(self):
        """
        :param Name: 参数名称
        :type Name: str
        :param ParamType: 参数类型
        :type ParamType: str
        :param Default: 参数默认值
        :type Default: str
        :param Description: 参数描述
        :type Description: str
        :param CurrentValue: 参数当前值
        :type CurrentValue: str
        :param NeedReboot: 修改参数后，是否需要重启数据库以使参数生效。可能的值包括：0-不需要重启；1-需要重启
        :type NeedReboot: int
        :param Max: 参数允许的最大值
        :type Max: int
        :param Min: 参数允许的最小值
        :type Min: int
        :param EnumValue: 参数的可选枚举值。如果为非枚举参数，则为空
        :type EnumValue: list of str
        """
        self.Name = None
        self.ParamType = None
        self.Default = None
        self.Description = None
        self.CurrentValue = None
        self.NeedReboot = None
        self.Max = None
        self.Min = None
        self.EnumValue = None


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


class RegionSellConf(AbstractModel):
    """地域售卖配置

    """

    def __init__(self):
        """
        :param RegionName: 地域中文名称
        :type RegionName: str
        :param Area: 所属大区
        :type Area: str
        :param IsDefaultRegion: 是否为默认地域
        :type IsDefaultRegion: int
        :param Region: 地域名称
        :type Region: str
        :param ZonesConf: 可用区售卖配置
        :type ZonesConf: list of ZoneSellConf
        """
        self.RegionName = None
        self.Area = None
        self.IsDefaultRegion = None
        self.Region = None
        self.ZonesConf = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.Area = params.get("Area")
        self.IsDefaultRegion = params.get("IsDefaultRegion")
        self.Region = params.get("Region")
        if params.get("ZonesConf") is not None:
            self.ZonesConf = []
            for item in params.get("ZonesConf"):
                obj = ZoneSellConf()
                obj._deserialize(item)
                self.ZonesConf.append(obj)


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class RestartDBInstancesResponse(AbstractModel):
    """RestartDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class RoGroup(AbstractModel):
    """只读组参数

    """

    def __init__(self):
        """
        :param RoGroupMode: 只读组模式，可选值为：alone-系统自动分配只读组；allinone-新建只读组；join-使用现有只读组
        :type RoGroupMode: str
        :param RoGroupId: 只读组ID
        :type RoGroupId: str
        :param RoGroupName: 只读组名称
        :type RoGroupName: str
        :param RoOfflineDelay: 是否启用延迟超限剔除功能，启用该功能后，只读实例与主实例的延迟超过延迟阈值值，只读实例将被隔离。可选值：1-启用；0-不启用
        :type RoOfflineDelay: int
        :param RoMaxDelayTime: 延迟阀值
        :type RoMaxDelayTime: int
        :param MinRoInGroup: 最少实例保留个数，若购买只读实例数量小于设置数量将不做剔除
        :type MinRoInGroup: int
        :param WeightMode: 读写权重分配模式，可选值：system-系统自动分配；custom-自定义
        :type WeightMode: str
        :param Weight: 权重值
        :type Weight: int
        :param RoInstances: 只读组中的只读实例详情
        :type RoInstances: list of RoInstanceInfo
        :param Vip: 只读组的内网IP
        :type Vip: str
        :param Vport: 只读组的内网端口号
        :type Vport: int
        """
        self.RoGroupMode = None
        self.RoGroupId = None
        self.RoGroupName = None
        self.RoOfflineDelay = None
        self.RoMaxDelayTime = None
        self.MinRoInGroup = None
        self.WeightMode = None
        self.Weight = None
        self.RoInstances = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.RoGroupMode = params.get("RoGroupMode")
        self.RoGroupId = params.get("RoGroupId")
        self.RoGroupName = params.get("RoGroupName")
        self.RoOfflineDelay = params.get("RoOfflineDelay")
        self.RoMaxDelayTime = params.get("RoMaxDelayTime")
        self.MinRoInGroup = params.get("MinRoInGroup")
        self.WeightMode = params.get("WeightMode")
        self.Weight = params.get("Weight")
        if params.get("RoInstances") is not None:
            self.RoInstances = []
            for item in params.get("RoInstances"):
                obj = RoInstanceInfo()
                obj._deserialize(item)
                self.RoInstances.append(obj)
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class RoInstanceInfo(AbstractModel):
    """RO实例的详细信息

    """

    def __init__(self):
        """
        :param MasterInstanceId: RO组对应的主实例的ID
        :type MasterInstanceId: str
        :param RoStatus: RO实例在RO组内的状态，可能的值：online-在线，offline-下线
        :type RoStatus: str
        :param OfflineTime: RO实例在RO组内上一次下线的时间
        :type OfflineTime: str
        :param Weight: RO实例在RO组内的权重
        :type Weight: int
        :param Region: RO实例所在区域名称，如ap-shanghai
        :type Region: str
        :param Zone: RO可用区的正式名称，如ap-shanghai-1
        :type Zone: str
        :param InstanceId: RO实例ID，格式如：cdbro-c1nl9rpv
        :type InstanceId: str
        :param Status: RO实例状态，可能返回值：0-创建中，1-运行中，4-删除中
        :type Status: int
        :param InstanceType: 实例类型，可能返回值：1-主实例，2-灾备实例，3-只读实例
        :type InstanceType: int
        :param InstanceName: RO实例名称
        :type InstanceName: str
        :param HourFeeStatus: 按量计费状态，可能的取值：1-正常，2-欠费
        :type HourFeeStatus: int
        :param TaskStatus: RO实例任务状态，可能返回值：<br>0-没有任务<br>1-升级中<br>2-数据导入中<br>3-开放Slave中<br>4-外网访问开通中<br>5-批量操作执行中<br>6-回档中<br>7-外网访问关闭中<br>8-密码修改中<br>9-实例名修改中<br>10-重启中<br>12-自建迁移中<br>13-删除库表中<br>14-灾备实例创建同步中
        :type TaskStatus: int
        :param Memory: RO实例内存大小，单位：MB
        :type Memory: int
        :param Volume: RO实例硬盘大小，单位：GB
        :type Volume: int
        :param Qps: 每次查询数量
        :type Qps: int
        :param Vip: RO实例的内网IP地址
        :type Vip: str
        :param Vport: RO实例访问端口
        :type Vport: int
        :param VpcId: RO实例所在私有网络ID
        :type VpcId: int
        :param SubnetId: RO实例所在私有网络子网ID
        :type SubnetId: int
        :param DeviceType: RO实例规格描述，目前可取值 CUSTOM
        :type DeviceType: str
        :param EngineVersion: RO实例数据库引擎版本，可能返回值：5.1、5.5、5.6和5.7
        :type EngineVersion: str
        :param DeadlineTime: RO实例到期时间，时间格式：yyyy-mm-dd hh:mm:ss，如实例为按量计费模式，则此字段值为0000-00-00 00:00:00
        :type DeadlineTime: str
        :param PayType: RO实例计费类型，可能返回值：0-包年包月，1-按量计费，2-后付费月结
        :type PayType: int
        """
        self.MasterInstanceId = None
        self.RoStatus = None
        self.OfflineTime = None
        self.Weight = None
        self.Region = None
        self.Zone = None
        self.InstanceId = None
        self.Status = None
        self.InstanceType = None
        self.InstanceName = None
        self.HourFeeStatus = None
        self.TaskStatus = None
        self.Memory = None
        self.Volume = None
        self.Qps = None
        self.Vip = None
        self.Vport = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceType = None
        self.EngineVersion = None
        self.DeadlineTime = None
        self.PayType = None


    def _deserialize(self, params):
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.RoStatus = params.get("RoStatus")
        self.OfflineTime = params.get("OfflineTime")
        self.Weight = params.get("Weight")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.InstanceType = params.get("InstanceType")
        self.InstanceName = params.get("InstanceName")
        self.HourFeeStatus = params.get("HourFeeStatus")
        self.TaskStatus = params.get("TaskStatus")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.Qps = params.get("Qps")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceType = params.get("DeviceType")
        self.EngineVersion = params.get("EngineVersion")
        self.DeadlineTime = params.get("DeadlineTime")
        self.PayType = params.get("PayType")


class RoVipInfo(AbstractModel):
    """只读vip信息

    """

    def __init__(self):
        """
        :param RoVipStatus: 只读vip状态
        :type RoVipStatus: int
        :param RoSubnetId: 只读vip的子网
        :type RoSubnetId: int
        :param RoVpcId: 只读vip的私有网络
        :type RoVpcId: int
        :param RoVport: 只读vip的端口号
        :type RoVport: int
        :param RoVip: 只读vip
        :type RoVip: str
        """
        self.RoVipStatus = None
        self.RoSubnetId = None
        self.RoVpcId = None
        self.RoVport = None
        self.RoVip = None


    def _deserialize(self, params):
        self.RoVipStatus = params.get("RoVipStatus")
        self.RoSubnetId = params.get("RoSubnetId")
        self.RoVpcId = params.get("RoVpcId")
        self.RoVport = params.get("RoVport")
        self.RoVip = params.get("RoVip")


class RollbackDBName(AbstractModel):
    """用于回档的数据库名

    """

    def __init__(self):
        """
        :param DatabaseName: 回档前的原数据库名
        :type DatabaseName: str
        :param NewDatabaseName: 回档后的新数据库名
        :type NewDatabaseName: str
        """
        self.DatabaseName = None
        self.NewDatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.NewDatabaseName = params.get("NewDatabaseName")


class RollbackInstancesInfo(AbstractModel):
    """用于回档的实例详情

    """

    def __init__(self):
        """
        :param InstanceId: 云数据库实例ID
        :type InstanceId: str
        :param Strategy: 回档策略。可选值为：table、db、full；默认值为full。table - 急速回档模式，仅导入所选中表级别的备份和binlog，如有跨表操作，且关联表未被同时选中，将会导致回档失败，该模式下参数Databases必须为空；db - 快速模式，仅导入所选中库级别的备份和binlog，如有跨库操作，且关联库未被同时选中，将会导致回档失败；full - 普通回档模式，将导入整个实例的备份和binlog，速度较慢。
        :type Strategy: str
        :param RollbackTime: 数据库回档时间，时间格式为：yyyy-mm-dd hh:mm:ss
        :type RollbackTime: str
        :param Databases: 待回档的数据库信息，表示整库回档
        :type Databases: list of RollbackDBName
        :param Tables: 待回档的数据库表信息，表示按表回档
        :type Tables: list of RollbackTables
        """
        self.InstanceId = None
        self.Strategy = None
        self.RollbackTime = None
        self.Databases = None
        self.Tables = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Strategy = params.get("Strategy")
        self.RollbackTime = params.get("RollbackTime")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = RollbackDBName()
                obj._deserialize(item)
                self.Databases.append(obj)
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = RollbackTables()
                obj._deserialize(item)
                self.Tables.append(obj)


class RollbackTableName(AbstractModel):
    """用于回档的数据库表名

    """

    def __init__(self):
        """
        :param TableName: 回档前的原数据库表名
        :type TableName: str
        :param NewTableName: 回档后的新数据库表名
        :type NewTableName: str
        """
        self.TableName = None
        self.NewTableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")


class RollbackTables(AbstractModel):
    """用于回档的数据库表详情

    """

    def __init__(self):
        """
        :param Database: 数据库名
        :type Database: str
        :param Table: 数据库表详情
        :type Table: list of RollbackTableName
        """
        self.Database = None
        self.Table = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        if params.get("Table") is not None:
            self.Table = []
            for item in params.get("Table"):
                obj = RollbackTableName()
                obj._deserialize(item)
                self.Table.append(obj)


class RollbackTimeRange(AbstractModel):
    """可回档时间范围

    """

    def __init__(self):
        """
        :param Begin: 实例可回档开始时间，时间格式：2016-10-29 01:06:04
        :type Begin: str
        :param End: 实例可回档结束时间，时间格式：2016-11-02 11:44:47
        :type End: str
        """
        self.Begin = None
        self.End = None


    def _deserialize(self, params):
        self.Begin = params.get("Begin")
        self.End = params.get("End")


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param Inbound: 入站规则
        :type Inbound: list of Inbound
        :param Outbound: 出站规则
        :type Outbound: list of Outbound
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        """
        self.ProjectId = None
        self.CreateTime = None
        self.Inbound = None
        self.Outbound = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self.Outbound.append(obj)
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")


class SellConfig(AbstractModel):
    """售卖配置详情

    """

    def __init__(self):
        """
        :param Device: 设备类型
        :type Device: str
        :param Type: 售卖规格描述
        :type Type: str
        :param CdbType: 实例类型
        :type CdbType: str
        :param Memory: 内存大小，单位为MB
        :type Memory: int
        :param Cpu: CPU核心数
        :type Cpu: int
        :param VolumeMin: 磁盘最小规格，单位为GB
        :type VolumeMin: int
        :param VolumeMax: 磁盘最大规格，单位为GB
        :type VolumeMax: int
        :param VolumeStep: 磁盘步长，单位为GB
        :type VolumeStep: int
        :param Connection: 链接数
        :type Connection: int
        :param Qps: 每秒查询数量
        :type Qps: int
        :param Iops: 每秒IO数量
        :type Iops: int
        :param Info: 应用场景描述
        :type Info: str
        :param Status: 状态值
        :type Status: int
        """
        self.Device = None
        self.Type = None
        self.CdbType = None
        self.Memory = None
        self.Cpu = None
        self.VolumeMin = None
        self.VolumeMax = None
        self.VolumeStep = None
        self.Connection = None
        self.Qps = None
        self.Iops = None
        self.Info = None
        self.Status = None


    def _deserialize(self, params):
        self.Device = params.get("Device")
        self.Type = params.get("Type")
        self.CdbType = params.get("CdbType")
        self.Memory = params.get("Memory")
        self.Cpu = params.get("Cpu")
        self.VolumeMin = params.get("VolumeMin")
        self.VolumeMax = params.get("VolumeMax")
        self.VolumeStep = params.get("VolumeStep")
        self.Connection = params.get("Connection")
        self.Qps = params.get("Qps")
        self.Iops = params.get("Iops")
        self.Info = params.get("Info")
        self.Status = params.get("Status")


class SellType(AbstractModel):
    """售卖实例类型

    """

    def __init__(self):
        """
        :param TypeName: 售卖实例名称
        :type TypeName: str
        :param EngineVersion: 内核版本号
        :type EngineVersion: list of str
        :param Configs: 售卖规格详细配置
        :type Configs: list of SellConfig
        """
        self.TypeName = None
        self.EngineVersion = None
        self.Configs = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.EngineVersion = params.get("EngineVersion")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = SellConfig()
                obj._deserialize(item)
                self.Configs.append(obj)


class SlaveConfig(AbstractModel):
    """从库的配置信息

    """

    def __init__(self):
        """
        :param ReplicationMode: 从库复制方式，可能的返回值：aysnc-异步，semisync-半同步
        :type ReplicationMode: str
        :param Zone: 从库可用区的正式名称，如ap-shanghai-1
        :type Zone: str
        """
        self.ReplicationMode = None
        self.Zone = None


    def _deserialize(self, params):
        self.ReplicationMode = params.get("ReplicationMode")
        self.Zone = params.get("Zone")


class SlaveInfo(AbstractModel):
    """备机信息

    """

    def __init__(self):
        """
        :param First: 第一备机信息
        :type First: :class:`tencentcloud.cdb.v20170320.models.First`
        :param Second: 第二备机信息
        :type Second: :class:`tencentcloud.cdb.v20170320.models.First`
        """
        self.First = None
        self.Second = None


    def _deserialize(self, params):
        if params.get("First") is not None:
            self.First = First()
            self.First._deserialize(params.get("First"))
        if params.get("Second") is not None:
            self.Second = First()
            self.Second._deserialize(params.get("Second"))


class SlowLogInfo(AbstractModel):
    """慢查询日志详情

    """

    def __init__(self):
        """
        :param Name: 备份文件名
        :type Name: str
        :param Size: 备份文件大小，单位：Byte
        :type Size: int
        :param Date: 备份快照时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 内网下载地址
        :type IntranetUrl: str
        :param InternetUrl: 外网下载地址
        :type InternetUrl: str
        :param Type: 日志具体类型，可能的值：slowlog - 慢日志
        :type Type: str
        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")


class StartBatchRollbackRequest(AbstractModel):
    """StartBatchRollback请求参数结构体

    """

    def __init__(self):
        """
        :param Instances: 用于回档的实例详情信息
        :type Instances: list of RollbackInstancesInfo
        """
        self.Instances = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self.Instances.append(obj)


class StartBatchRollbackResponse(AbstractModel):
    """StartBatchRollback返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StopDBImportJobRequest(AbstractModel):
    """StopDBImportJob请求参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID。
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")


class StopDBImportJobResponse(AbstractModel):
    """StopDBImportJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchForUpgradeRequest(AbstractModel):
    """SwitchForUpgrade请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class SwitchForUpgradeResponse(AbstractModel):
    """SwitchForUpgrade返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TableName(AbstractModel):
    """表名

    """

    def __init__(self):
        """
        :param TableName: 表名
        :type TableName: str
        """
        self.TableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")


class TablePrivilege(AbstractModel):
    """数据库表权限

    """

    def __init__(self):
        """
        :param Database: 数据库名
        :type Database: str
        :param Table: 数据库表名
        :type Table: str
        :param Privileges: 权限信息
        :type Privileges: list of str
        """
        self.Database = None
        self.Table = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Privileges = params.get("Privileges")


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param EngineVersion: 主实例数据库引擎版本，支持值包括：5.6和5.7
        :type EngineVersion: str
        :param WaitSwitch: 切换访问新实例的方式，默认为0，升级主实例时，可指定该参数，升级只读实例或者灾备实例时指定该参数无意义，支持值包括：0-立刻切换，1-时间窗切换；当该值为1时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口[切换访问新实例](https://cloud.tencent.com/document/api/403/4392)触发该流程
        :type WaitSwitch: int
        """
        self.InstanceId = None
        self.EngineVersion = None
        self.WaitSwitch = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")


class UpgradeDBInstanceEngineVersionResponse(AbstractModel):
    """UpgradeDBInstanceEngineVersion返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务ID，可使用[查询任务列表](https://cloud.tencent.com/document/api/236/8010)获取其执行情况
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Memory: 升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可升级的内存规格
        :type Memory: int
        :param Volume: 升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可升级的硬盘范围
        :type Volume: int
        :param ProtectMode: 数据复制方式，支持值包括：0-异步复制，1-半同步复制，2-强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义
        :type ProtectMode: int
        :param DeployMode: 部署模式，默认为0，支持值包括：0-单可用区部署，1-多可用区部署，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义
        :type DeployMode: int
        :param SlaveZone: 备库1的可用区信息，默认为实例的Zone，升级主实例为多可用区部署时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。可通过<a href='/document/product/236/6921' title='查询云数据库可售卖规格'>查询云数据库可售卖规格</a>查询支持的可用区
        :type SlaveZone: str
        :param EngineVersion: 主实例数据库引擎版本，支持值包括：5.5、5.6和5.7
        :type EngineVersion: str
        :param WaitSwitch: 切换访问新实例的方式，默认为0，升级主实例时，可指定该参数，升级只读实例或者灾备实例时指定该参数无意义，支持值包括：0-立刻切换，1-时间窗切换；当该值为1时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口[切换访问新实例](https://cloud.tencent.com/document/api/403/4392)触发该流程
        :type WaitSwitch: int
        :param BackupZone: 备库2的可用区ID，默认为0，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义
        :type BackupZone: str
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例
        :type InstanceRole: str
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.EngineVersion = None
        self.WaitSwitch = None
        self.BackupZone = None
        self.InstanceRole = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")
        self.BackupZone = params.get("BackupZone")
        self.InstanceRole = params.get("InstanceRole")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 订单ID，用于调用云API相关接口，如[获取订单信息](https://cloud.tencent.com/document/api/403/4392)
        :type DealIds: list of str
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class VerifyRootAccountRequest(AbstractModel):
    """VerifyRootAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Password: 实例ROOT账号的密码。
        :type Password: str
        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")


class VerifyRootAccountResponse(AbstractModel):
    """VerifyRootAccount返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ZoneConf(AbstractModel):
    """多可用区信息

    """

    def __init__(self):
        """
        :param DeployMode: 可用区部署方式，可能的值为：0-单可用区；1-多可用区
        :type DeployMode: list of int
        :param MasterZone: 主实例所在的可用区
        :type MasterZone: list of str
        :param SlaveZone: 实例为多可用区部署时，备库1所在的可用区
        :type SlaveZone: list of str
        :param BackupZone: 实例为多可用区部署时，备库2所在的可用区
        :type BackupZone: list of str
        """
        self.DeployMode = None
        self.MasterZone = None
        self.SlaveZone = None
        self.BackupZone = None


    def _deserialize(self, params):
        self.DeployMode = params.get("DeployMode")
        self.MasterZone = params.get("MasterZone")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")


class ZoneSellConf(AbstractModel):
    """可用区售卖配置

    """

    def __init__(self):
        """
        :param Status: 可用区状态。可能的返回值为：0-未上线；1-上线；2-开放；3-停售；4-不展示
        :type Status: int
        :param ZoneName: 可用区中文名称
        :type ZoneName: str
        :param IsCustom: 实例类型是否为自定义类型
        :type IsCustom: bool
        :param IsSupportDr: 是否支持灾备
        :type IsSupportDr: bool
        :param IsSupportVpc: 是否支持私有网络
        :type IsSupportVpc: bool
        :param HourInstanceSaleMaxNum: 小时计费实例最大售卖数量
        :type HourInstanceSaleMaxNum: int
        :param IsDefaultZone: 是否为默认可用区
        :type IsDefaultZone: bool
        :param IsBm: 是否为黑石区
        :type IsBm: bool
        :param PayType: 支持的付费类型。可能的返回值为：0-包年包月；1-小时计费；2-后付费
        :type PayType: list of str
        :param ProtectMode: 数据复制类型。0-异步复制；1-半同步复制；2-强同步复制
        :type ProtectMode: list of str
        :param Zone: 可用区名称
        :type Zone: str
        :param SellType: 售卖实例类型数组
        :type SellType: list of SellType
        :param ZoneConf: 多可用区信息
        :type ZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`
        """
        self.Status = None
        self.ZoneName = None
        self.IsCustom = None
        self.IsSupportDr = None
        self.IsSupportVpc = None
        self.HourInstanceSaleMaxNum = None
        self.IsDefaultZone = None
        self.IsBm = None
        self.PayType = None
        self.ProtectMode = None
        self.Zone = None
        self.SellType = None
        self.ZoneConf = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ZoneName = params.get("ZoneName")
        self.IsCustom = params.get("IsCustom")
        self.IsSupportDr = params.get("IsSupportDr")
        self.IsSupportVpc = params.get("IsSupportVpc")
        self.HourInstanceSaleMaxNum = params.get("HourInstanceSaleMaxNum")
        self.IsDefaultZone = params.get("IsDefaultZone")
        self.IsBm = params.get("IsBm")
        self.PayType = params.get("PayType")
        self.ProtectMode = params.get("ProtectMode")
        self.Zone = params.get("Zone")
        if params.get("SellType") is not None:
            self.SellType = []
            for item in params.get("SellType"):
                obj = SellType()
                obj._deserialize(item)
                self.SellType.append(obj)
        if params.get("ZoneConf") is not None:
            self.ZoneConf = ZoneConf()
            self.ZoneConf._deserialize(params.get("ZoneConf"))