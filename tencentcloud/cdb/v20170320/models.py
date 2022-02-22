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


class Account(AbstractModel):
    """数据库账号信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountInfo(AbstractModel):
    """账号详细信息

    """

    def __init__(self):
        r"""
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
        :param CreateTime: 该值已废弃
        :type CreateTime: str
        :param MaxUserConnections: 用户最大可用实例连接数
        :type MaxUserConnections: int
        """
        self.Notes = None
        self.Host = None
        self.User = None
        self.ModifyTime = None
        self.ModifyPasswordTime = None
        self.CreateTime = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        self.Notes = params.get("Notes")
        self.Host = params.get("Host")
        self.User = params.get("User")
        self.ModifyTime = params.get("ModifyTime")
        self.ModifyPasswordTime = params.get("ModifyPasswordTime")
        self.CreateTime = params.get("CreateTime")
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowRequest(AbstractModel):
    """AddTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Monday: 星期一的可维护时间段，其中每一个时间段的格式形如：10:00-12:00；起始时间按半个小时对齐；最短半个小时，最长三个小时；可设置多个时间段。 一周中应至少设置一天的时间窗。下同。
        :type Monday: list of str
        :param Tuesday: 星期二的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Tuesday: list of str
        :param Wednesday: 星期三的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Wednesday: list of str
        :param Thursday: 星期四的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Thursday: list of str
        :param Friday: 星期五的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Friday: list of str
        :param Saturday: 星期六的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Saturday: list of str
        :param Sunday: 星期日的可维护时间窗口。 一周中应至少设置一天的时间窗。
        :type Sunday: list of str
        """
        self.InstanceId = None
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTimeWindowResponse(AbstractModel):
    """AddTimeWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Address(AbstractModel):
    """地址

    """

    def __init__(self):
        r"""
        :param Vip: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param VPort: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type VPort: int
        :param UniqVpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param UniqSubnet: 私有网络子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnet: str
        :param Desc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        """
        self.Vip = None
        self.VPort = None
        self.UniqVpcId = None
        self.UniqSubnet = None
        self.Desc = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.VPort = params.get("VPort")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnet = params.get("UniqSubnet")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCDBProxyRequest(AbstractModel):
    """ApplyCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 主实例唯一标识ID
        :type InstanceId: str
        :param UniqVpcId: 私有网络ID
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络子网ID
        :type UniqSubnetId: str
        :param ProxyCount: 代理组节点个数
        :type ProxyCount: int
        :param Cpu: cpu核数
        :type Cpu: int
        :param Mem: 内存
        :type Mem: int
        :param SecurityGroup: 安全组
        :type SecurityGroup: list of str
        :param Desc: 描述说明
        :type Desc: str
        """
        self.InstanceId = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ProxyCount = None
        self.Cpu = None
        self.Mem = None
        self.SecurityGroup = None
        self.Desc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ProxyCount = params.get("ProxyCount")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.SecurityGroup = params.get("SecurityGroup")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCDBProxyResponse(AbstractModel):
    """ApplyCDBProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步处理ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityGroupId: 安全组 ID。
        :type SecurityGroupId: str
        :param InstanceIds: 实例 ID 列表，一个或者多个实例 ID 组成的数组。
        :type InstanceIds: list of str
        :param ForReadonlyInstance: 当传入只读实例ID时，默认操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True
        :type ForReadonlyInstance: bool
        """
        self.SecurityGroupId = None
        self.InstanceIds = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuditFilter(AbstractModel):
    """审计规则过滤条件

    """

    def __init__(self):
        r"""
        :param Type: 过滤条件参数名称。目前支持：
SrcIp – 客户端 IP；
User – 数据库账户；
DB – 数据库名称；
        :type Type: str
        :param Compare: 过滤条件匹配类型。目前支持：
INC – 包含；
EXC – 不包含；
EQ – 等于；
NEQ – 不等于；
        :type Compare: str
        :param Value: 过滤条件匹配值。
        :type Value: str
        """
        self.Type = None
        self.Compare = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Compare = params.get("Compare")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFile(AbstractModel):
    """审计日志文件

    """

    def __init__(self):
        r"""
        :param FileName: 审计日志文件名称
        :type FileName: str
        :param CreateTime: 审计日志文件创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param Status: 文件状态值。可能返回的值为：
"creating" - 生成中;
"failed" - 创建失败;
"success" - 已生成;
        :type Status: str
        :param FileSize: 文件大小，单位为 KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param DownloadUrl: 审计日志下载地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param ErrMsg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        """
        self.FileName = None
        self.CreateTime = None
        self.Status = None
        self.FileSize = None
        self.DownloadUrl = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.FileSize = params.get("FileSize")
        self.DownloadUrl = params.get("DownloadUrl")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFilter(AbstractModel):
    """审计日志过滤条件。查询审计日志时，用户过滤返回的审计日志。

    """

    def __init__(self):
        r"""
        :param Host: 客户端地址。
        :type Host: list of str
        :param User: 用户名。
        :type User: list of str
        :param DBName: 数据库名称。
        :type DBName: list of str
        :param TableName: 表名称。
        :type TableName: list of str
        :param PolicyName: 审计策略名称。
        :type PolicyName: list of str
        :param Sql: SQL 语句。支持模糊匹配。
        :type Sql: str
        :param SqlType: SQL 类型。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlType: str
        :param ExecTime: 执行时间。单位为：ms。表示筛选执行时间大于该值的审计日志。
        :type ExecTime: int
        :param AffectRows: 影响行数。表示筛选影响行数大于该值的审计日志。
        :type AffectRows: int
        :param SqlTypes: SQL 类型。支持多个类型同时查询。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlTypes: list of str
        :param Sqls: SQL 语句。支持传递多个sql语句。
        :type Sqls: list of str
        """
        self.Host = None
        self.User = None
        self.DBName = None
        self.TableName = None
        self.PolicyName = None
        self.Sql = None
        self.SqlType = None
        self.ExecTime = None
        self.AffectRows = None
        self.SqlTypes = None
        self.Sqls = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.User = params.get("User")
        self.DBName = params.get("DBName")
        self.TableName = params.get("TableName")
        self.PolicyName = params.get("PolicyName")
        self.Sql = params.get("Sql")
        self.SqlType = params.get("SqlType")
        self.ExecTime = params.get("ExecTime")
        self.AffectRows = params.get("AffectRows")
        self.SqlTypes = params.get("SqlTypes")
        self.Sqls = params.get("Sqls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditPolicy(AbstractModel):
    """审计策略

    """

    def __init__(self):
        r"""
        :param PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param Status: 审计策略的状态。可能返回的值为：
"creating" - 创建中;
"running" - 运行中;
"paused" - 暂停中;
"failed" - 创建失败。
        :type Status: str
        :param InstanceId: 数据库实例 ID。
        :type InstanceId: str
        :param CreateTime: 审计策略创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param ModifyTime: 审计策略最后修改时间。格式为 : "2019-03-20 17:09:13"。
        :type ModifyTime: str
        :param PolicyName: 审计策略名称。
        :type PolicyName: str
        :param RuleId: 审计规则 ID。
        :type RuleId: str
        :param RuleName: 审计规则名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        """
        self.PolicyId = None
        self.Status = None
        self.InstanceId = None
        self.CreateTime = None
        self.ModifyTime = None
        self.PolicyName = None
        self.RuleId = None
        self.RuleName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.Status = params.get("Status")
        self.InstanceId = params.get("InstanceId")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.PolicyName = params.get("PolicyName")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRule(AbstractModel):
    """审计规则

    """

    def __init__(self):
        r"""
        :param RuleId: 审计规则 Id。
        :type RuleId: str
        :param CreateTime: 审计规则创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param ModifyTime: 审计规则最后修改时间。格式为 : "2019-03-20 17:09:13"。
        :type ModifyTime: str
        :param RuleName: 审计规则名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param Description: 审计规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param RuleFilters: 审计规则过滤条件。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleFilters: list of AuditFilter
        :param AuditAll: 是否开启全审计。
        :type AuditAll: bool
        """
        self.RuleId = None
        self.CreateTime = None
        self.ModifyTime = None
        self.RuleName = None
        self.Description = None
        self.RuleFilters = None
        self.AuditAll = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.RuleName = params.get("RuleName")
        self.Description = params.get("Description")
        if params.get("RuleFilters") is not None:
            self.RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = AuditFilter()
                obj._deserialize(item)
                self.RuleFilters.append(obj)
        self.AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupConfig(AbstractModel):
    """ECDB第二个从库的配置信息，只有ECDB实例才有这个字段

    """

    def __init__(self):
        r"""
        :param ReplicationMode: 第二个从库复制方式，可能的返回值：async-异步，semisync-半同步
        :type ReplicationMode: str
        :param Zone: 第二个从库可用区的正式名称，如ap-shanghai-1
        :type Zone: str
        :param Vip: 第二个从库内网IP地址
        :type Vip: str
        :param Vport: 第二个从库访问端口
        :type Vport: int
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    """备份详细信息

    """

    def __init__(self):
        r"""
        :param Name: 备份文件名
        :type Name: str
        :param Size: 备份文件大小，单位：Byte
        :type Size: int
        :param Date: 备份快照时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 下载地址
        :type IntranetUrl: str
        :param InternetUrl: 下载地址
        :type InternetUrl: str
        :param Type: 日志具体类型。可能的值有 "logical": 逻辑冷备， "physical": 物理冷备。
        :type Type: str
        :param BackupId: 备份子任务的ID，删除备份文件时使用
        :type BackupId: int
        :param Status: 备份任务状态。可能的值有 "SUCCESS": 备份成功， "FAILED": 备份失败， "RUNNING": 备份进行中。
        :type Status: str
        :param FinishTime: 备份任务的完成时间
        :type FinishTime: str
        :param Creator: （该值将废弃，不建议使用）备份的创建者，可能的值：SYSTEM - 系统创建，Uin - 发起者Uin值。
        :type Creator: str
        :param StartTime: 备份任务的开始时间
        :type StartTime: str
        :param Method: 备份方法。可能的值有 "full": 全量备份， "partial": 部分备份。
        :type Method: str
        :param Way: 备份方式。可能的值有 "manual": 手动备份， "automatic": 自动备份。
        :type Way: str
        :param ManualBackupName: 手动备份别名
        :type ManualBackupName: str
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
        self.StartTime = None
        self.Method = None
        self.Way = None
        self.ManualBackupName = None


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
        self.StartTime = params.get("StartTime")
        self.Method = params.get("Method")
        self.Way = params.get("Way")
        self.ManualBackupName = params.get("ManualBackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupItem(AbstractModel):
    """创建备份时，指定需要备份的库表信息

    """

    def __init__(self):
        r"""
        :param Db: 需要备份的库名
        :type Db: str
        :param Table: 需要备份的表名。 如果传该参数，表示备份该库中的指定表。如果不传该参数则备份该db库
        :type Table: str
        """
        self.Db = None
        self.Table = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupLimitVpcItem(AbstractModel):
    """备份文件限制下载来源VPC设置项

    """

    def __init__(self):
        r"""
        :param Region: 限制下载来源的地域。目前仅支持当前地域。
        :type Region: str
        :param VpcList: 限制下载的vpc列表。
        :type VpcList: list of str
        """
        self.Region = None
        self.VpcList = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.VpcList = params.get("VpcList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupSummaryItem(AbstractModel):
    """实例备份统计项

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param AutoBackupCount: 该实例自动数据备份的个数。
        :type AutoBackupCount: int
        :param AutoBackupVolume: 该实例自动数据备份的容量。
        :type AutoBackupVolume: int
        :param ManualBackupCount: 该实例手动数据备份的个数。
        :type ManualBackupCount: int
        :param ManualBackupVolume: 该实例手动数据备份的容量。
        :type ManualBackupVolume: int
        :param DataBackupCount: 该实例总的数据备份（包含自动备份和手动备份）个数。
        :type DataBackupCount: int
        :param DataBackupVolume: 该实例总的数据备份容量。
        :type DataBackupVolume: int
        :param BinlogBackupCount: 该实例日志备份的个数。
        :type BinlogBackupCount: int
        :param BinlogBackupVolume: 该实例日志备份的容量。
        :type BinlogBackupVolume: int
        :param BackupVolume: 该实例的总备份（包含数据备份和日志备份）占用容量。
        :type BackupVolume: int
        """
        self.InstanceId = None
        self.AutoBackupCount = None
        self.AutoBackupVolume = None
        self.ManualBackupCount = None
        self.ManualBackupVolume = None
        self.DataBackupCount = None
        self.DataBackupVolume = None
        self.BinlogBackupCount = None
        self.BinlogBackupVolume = None
        self.BackupVolume = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoBackupCount = params.get("AutoBackupCount")
        self.AutoBackupVolume = params.get("AutoBackupVolume")
        self.ManualBackupCount = params.get("ManualBackupCount")
        self.ManualBackupVolume = params.get("ManualBackupVolume")
        self.DataBackupCount = params.get("DataBackupCount")
        self.DataBackupVolume = params.get("DataBackupVolume")
        self.BinlogBackupCount = params.get("BinlogBackupCount")
        self.BinlogBackupVolume = params.get("BinlogBackupVolume")
        self.BackupVolume = params.get("BackupVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadRequest(AbstractModel):
    """BalanceRoGroupLoad请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoGroupId: RO 组的 ID，格式如：cdbrg-c1nl9rpv。
        :type RoGroupId: str
        """
        self.RoGroupId = None


    def _deserialize(self, params):
        self.RoGroupId = params.get("RoGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BalanceRoGroupLoadResponse(AbstractModel):
    """BalanceRoGroupLoad返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BaseGroupInfo(AbstractModel):
    """proxy代理组信息

    """

    def __init__(self):
        r"""
        :param ProxyGroupId: 代理组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyGroupId: str
        :param NodeCount: 代理节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeCount: int
        :param Status: 状态：发货中（init）运行中（online）下线中（offline）销毁中（destroy）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param OpenRW: 是否开启读写分离
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenRW: bool
        :param CurrentProxyVersion: 当前代理版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentProxyVersion: str
        :param SupportUpgradeProxyVersion: 支持升级版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportUpgradeProxyVersion: str
        """
        self.ProxyGroupId = None
        self.NodeCount = None
        self.Status = None
        self.Region = None
        self.Zone = None
        self.OpenRW = None
        self.CurrentProxyVersion = None
        self.SupportUpgradeProxyVersion = None


    def _deserialize(self, params):
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.NodeCount = params.get("NodeCount")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.OpenRW = params.get("OpenRW")
        self.CurrentProxyVersion = params.get("CurrentProxyVersion")
        self.SupportUpgradeProxyVersion = params.get("SupportUpgradeProxyVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogInfo(AbstractModel):
    """二进制日志信息

    """

    def __init__(self):
        r"""
        :param Name: binlog 日志备份文件名
        :type Name: str
        :param Size: 备份文件大小，单位：Byte
        :type Size: int
        :param Date: 文件存储时间，时间格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 下载地址
        :type IntranetUrl: str
        :param InternetUrl: 下载地址
        :type InternetUrl: str
        :param Type: 日志具体类型，可能的值有：binlog - 二进制日志
        :type Type: str
        :param BinlogStartTime: binlog 文件起始时间
        :type BinlogStartTime: str
        :param BinlogFinishTime: binlog 文件截止时间
        :type BinlogFinishTime: str
        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None
        self.BinlogStartTime = None
        self.BinlogFinishTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")
        self.BinlogStartTime = params.get("BinlogStartTime")
        self.BinlogFinishTime = params.get("BinlogFinishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneItem(AbstractModel):
    """克隆任务记录。

    """

    def __init__(self):
        r"""
        :param SrcInstanceId: 克隆任务的源实例Id。
        :type SrcInstanceId: str
        :param DstInstanceId: 克隆任务的新产生实例Id。
        :type DstInstanceId: str
        :param CloneJobId: 克隆任务对应的任务列表Id。
        :type CloneJobId: int
        :param RollbackStrategy: 克隆实例使用的策略， 包括以下类型：  timepoint:指定时间点回档，  backupset: 指定备份文件回档。
        :type RollbackStrategy: str
        :param RollbackTargetTime: 克隆实例回档的时间点。
        :type RollbackTargetTime: str
        :param StartTime: 任务开始时间。
        :type StartTime: str
        :param EndTime: 任务结束时间。
        :type EndTime: str
        :param TaskStatus: 任务状态，包括以下状态：initial,running,wait_complete,success,failed
        :type TaskStatus: str
        """
        self.SrcInstanceId = None
        self.DstInstanceId = None
        self.CloneJobId = None
        self.RollbackStrategy = None
        self.RollbackTargetTime = None
        self.StartTime = None
        self.EndTime = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.SrcInstanceId = params.get("SrcInstanceId")
        self.DstInstanceId = params.get("DstInstanceId")
        self.CloneJobId = params.get("CloneJobId")
        self.RollbackStrategy = params.get("RollbackStrategy")
        self.RollbackTargetTime = params.get("RollbackTargetTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCDBProxyRequest(AbstractModel):
    """CloseCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param OnlyCloseRW: 是否只关闭读写分离，取值："true" | "false"
        :type OnlyCloseRW: bool
        """
        self.InstanceId = None
        self.ProxyGroupId = None
        self.OnlyCloseRW = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.OnlyCloseRW = params.get("OnlyCloseRW")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCDBProxyResponse(AbstractModel):
    """CloseCDBProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CloseWanServiceRequest(AbstractModel):
    """CloseWanService请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWanServiceResponse(AbstractModel):
    """CloseWanService返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonTimeWindow(AbstractModel):
    """通用时间窗

    """

    def __init__(self):
        r"""
        :param Monday: 周一的时间窗，格式如： 02:00-06:00
        :type Monday: str
        :param Tuesday: 周二的时间窗，格式如： 02:00-06:00
        :type Tuesday: str
        :param Wednesday: 周三的时间窗，格式如： 02:00-06:00
        :type Wednesday: str
        :param Thursday: 周四的时间窗，格式如： 02:00-06:00
        :type Thursday: str
        :param Friday: 周五的时间窗，格式如： 02:00-06:00
        :type Friday: str
        :param Saturday: 周六的时间窗，格式如： 02:00-06:00
        :type Saturday: str
        :param Sunday: 周日的时间窗，格式如： 02:00-06:00
        :type Sunday: str
        """
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None


    def _deserialize(self, params):
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionPoolInfo(AbstractModel):
    """连接池信息

    """

    def __init__(self):
        r"""
        :param ConnectionPool: 是否开启了连接池
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPool: bool
        :param ConnectionPoolType: 连接池类型：SessionConnectionPool（会话级别连接池）
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolType: str
        :param PoolConnectionTimeOut: 连接池保持阈值：单位（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolConnectionTimeOut: int
        """
        self.ConnectionPool = None
        self.ConnectionPoolType = None
        self.PoolConnectionTimeOut = None


    def _deserialize(self, params):
        self.ConnectionPool = params.get("ConnectionPool")
        self.ConnectionPoolType = params.get("ConnectionPoolType")
        self.PoolConnectionTimeOut = params.get("PoolConnectionTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Accounts: 云数据库账号。
        :type Accounts: list of Account
        :param Password: 新账户的密码。
        :type Password: str
        :param Description: 备注信息。
        :type Description: str
        :param MaxUserConnections: 新账户最大可用连接数，默认值为10240，最大可设置值为10240。
        :type MaxUserConnections: int
        """
        self.InstanceId = None
        self.Accounts = None
        self.Password = None
        self.Description = None
        self.MaxUserConnections = None


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
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateAuditLogFileRequest(AbstractModel):
    """CreateAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param StartTime: 开始时间，格式为："2017-07-12 10:29:20"。
        :type StartTime: str
        :param EndTime: 结束时间，格式为："2017-07-12 10:29:20"。
        :type EndTime: str
        :param Order: 排序方式。支持值包括："ASC" - 升序，"DESC" - 降序。
        :type Order: str
        :param OrderBy: 排序字段。支持值包括：
"timestamp" - 时间戳；
"affectRows" - 影响行数；
"execTime" - 执行时间。
        :type OrderBy: str
        :param Filter: 过滤条件。可按设置的过滤条件过滤日志。
        :type Filter: :class:`tencentcloud.cdb.v20170320.models.AuditLogFilter`
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = AuditLogFilter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditLogFileResponse(AbstractModel):
    """CreateAuditLogFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileName: 审计日志文件名称。
        :type FileName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.RequestId = params.get("RequestId")


class CreateAuditPolicyRequest(AbstractModel):
    """CreateAuditPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 审计策略名称。
        :type Name: str
        :param RuleId: 审计规则 ID。
        :type RuleId: str
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param LogExpireDay: 审计日志保存时长。支持值包括：
7 - 一周
30 - 一个月；
180 - 六个月；
365 - 一年；
1095 - 三年；
1825 - 五年；
实例首次开通审计策略时，可传该值，用于设置存储日志保存天数，默认为 30 天。若实例已存在审计策略，则此参数无效，可使用 更改审计服务配置 接口修改日志存储时长。
        :type LogExpireDay: int
        """
        self.Name = None
        self.RuleId = None
        self.InstanceId = None
        self.LogExpireDay = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RuleId = params.get("RuleId")
        self.InstanceId = params.get("InstanceId")
        self.LogExpireDay = params.get("LogExpireDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditPolicyResponse(AbstractModel):
    """CreateAuditPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateAuditRuleRequest(AbstractModel):
    """CreateAuditRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 审计规则名称。
        :type RuleName: str
        :param Description: 审计规则描述。
        :type Description: str
        :param RuleFilters: 审计规则过滤条件。若设置了过滤条件，则不会开启全审计。
        :type RuleFilters: list of AuditFilter
        :param AuditAll: 是否开启全审计。支持值包括：false – 不开启全审计，true – 开启全审计。用户未设置审计规则过滤条件时，默认开启全审计。
        :type AuditAll: bool
        """
        self.RuleName = None
        self.Description = None
        self.RuleFilters = None
        self.AuditAll = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Description = params.get("Description")
        if params.get("RuleFilters") is not None:
            self.RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = AuditFilter()
                obj._deserialize(item)
                self.RuleFilters.append(obj)
        self.AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRuleResponse(AbstractModel):
    """CreateAuditRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 审计规则 ID。
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param BackupMethod: 目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备。
        :type BackupMethod: str
        :param BackupDBTableList: 需要备份的库表信息，如果不设置该参数，则默认整实例备份。在 BackupMethod=logical 逻辑备份中才可设置该参数。指定的库表必须存在，否则可能导致备份失败。
例：如果需要备份 db1 库的 tb1、tb2 表 和 db2 库。则该参数设置为 [{"Db": "db1", "Table": "tb1"}, {"Db": "db1", "Table": "tb2"}, {"Db": "db2"} ]。
        :type BackupDBTableList: list of BackupItem
        :param ManualBackupName: 手动备份别名
        :type ManualBackupName: str
        """
        self.InstanceId = None
        self.BackupMethod = None
        self.BackupDBTableList = None
        self.ManualBackupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
        if params.get("BackupDBTableList") is not None:
            self.BackupDBTableList = []
            for item in params.get("BackupDBTableList"):
                obj = BackupItem()
                obj._deserialize(item)
                self.BackupDBTableList.append(obj)
        self.ManualBackupName = params.get("ManualBackupName")
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
        r"""
        :param BackupId: 备份任务 ID。
        :type BackupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupId = params.get("BackupId")
        self.RequestId = params.get("RequestId")


class CreateCloneInstanceRequest(AbstractModel):
    """CreateCloneInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 克隆源实例Id。
        :type InstanceId: str
        :param SpecifiedRollbackTime: 如果需要克隆实例回档到指定时间，则指定该值。时间格式为： yyyy-mm-dd hh:mm:ss 。
        :type SpecifiedRollbackTime: str
        :param SpecifiedBackupId: 如果需要克隆实例回档到指定备份的时间点，则指定该值为物理备份的Id。请使用 [查询数据备份文件列表](/document/api/236/15842) 。
        :type SpecifiedBackupId: int
        :param UniqVpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 [查询子网列表](/document/api/215/15784)。
        :type UniqSubnetId: str
        :param Memory: 实例内存大小，单位：MB，需要不低于克隆源实例，默认和源实例相同。
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB，需要不低于克隆源实例，默认和源实例相同。
        :type Volume: int
        :param InstanceName: 新产生的克隆实例名称。
        :type InstanceName: str
        :param SecurityGroup: 安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。
        :type SecurityGroup: list of str
        :param ResourceTags: 实例标签信息。
        :type ResourceTags: list of TagInfo
        :param Cpu: 实例Cpu核数，需要不低于克隆源实例，默认和源实例相同。
        :type Cpu: int
        :param ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。
        :type ProtectMode: int
        :param DeployMode: 多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区。
        :type DeployMode: int
        :param SlaveZone: 新产生的克隆实例备库 1 的可用区信息，默认同源实例 Zone 的值。
        :type SlaveZone: str
        :param BackupZone: 备库 2 的可用区信息，默认为空，克隆强同步主实例时可指定该参数。
        :type BackupZone: str
        :param DeviceType: 克隆实例类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例。 不指定则默认为通用型。
        :type DeviceType: str
        :param InstanceNodes: 新克隆实例节点数。如果需要克隆出三节点实例， 请将该值设置为3 或指定 BackupZone 参数。如果需要克隆出两节点实例，请将该值设置为2。默认克隆出两节点实例。
        :type InstanceNodes: int
        :param DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param DryRun: 是否只预检此次请求。true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制等。如果检查不通过，则返回对应错误码；如果检查通过，则返回RequestId.默认为false：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
        :param CageId: 金融围拢 ID 。
        :type CageId: str
        """
        self.InstanceId = None
        self.SpecifiedRollbackTime = None
        self.SpecifiedBackupId = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.Memory = None
        self.Volume = None
        self.InstanceName = None
        self.SecurityGroup = None
        self.ResourceTags = None
        self.Cpu = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.BackupZone = None
        self.DeviceType = None
        self.InstanceNodes = None
        self.DeployGroupId = None
        self.DryRun = None
        self.CageId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpecifiedRollbackTime = params.get("SpecifiedRollbackTime")
        self.SpecifiedBackupId = params.get("SpecifiedBackupId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroup = params.get("SecurityGroup")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.Cpu = params.get("Cpu")
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")
        self.DeviceType = params.get("DeviceType")
        self.InstanceNodes = params.get("InstanceNodes")
        self.DeployGroupId = params.get("DeployGroupId")
        self.DryRun = params.get("DryRun")
        self.CageId = params.get("CageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloneInstanceResponse(AbstractModel):
    """CreateCloneInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBImportJobRequest(AbstractModel):
    """CreateDBImportJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param User: 云数据库的用户名。
        :type User: str
        :param FileName: 文件名称。该文件是指用户已上传到腾讯云的文件，仅支持.sql文件。
        :type FileName: str
        :param Password: 云数据库实例 User 账号的密码。
        :type Password: str
        :param DbName: 导入的目标数据库名，不传表示不指定数据库。
        :type DbName: str
        :param CosUrl: 腾讯云COS文件链接。 用户需要指定 FileName 或者 CosUrl 其中一个。 COS文件需要是 .sql 文件。
        :type CosUrl: str
        """
        self.InstanceId = None
        self.User = None
        self.FileName = None
        self.Password = None
        self.DbName = None
        self.CosUrl = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.FileName = params.get("FileName")
        self.Password = params.get("Password")
        self.DbName = params.get("DbName")
        self.CosUrl = params.get("CosUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBImportJobResponse(AbstractModel):
    """CreateDBImportJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param GoodsNum: 实例数量，默认值为 1，最小值 1，最大值为 100。
        :type GoodsNum: int
        :param Memory: 实例内存大小，单位：MB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的内存规格。
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的硬盘范围。
        :type Volume: int
        :param EngineVersion: MySQL 版本，值包括：5.5、5.6 、5.7 、8.0，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的实例版本。
        :type EngineVersion: str
        :param UniqVpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/document/api/215/15784)。
        :type UniqSubnetId: str
        :param ProjectId: 项目 ID，不填为默认项目。请使用 [查询项目列表](https://cloud.tencent.com/document/product/378/4400) 接口获取项目 ID。
        :type ProjectId: int
        :param Zone: 可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的可用区。
        :type Zone: str
        :param MasterInstanceId: 实例 ID，购买只读实例或者灾备实例时必填，该字段表示只读实例或者灾备实例的主实例 ID，请使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询云数据库实例 ID。
        :type MasterInstanceId: str
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。
        :type InstanceRole: str
        :param MasterRegion: 主实例的可用区信息，购买灾备实例时必填。
        :type MasterRegion: str
        :param Port: 自定义端口，端口支持范围：[ 1024-65535 ] 。
        :type Port: int
        :param Password: 设置 root 帐号密码，密码规则：8 - 64 个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type Password: str
        :param ParamList: 参数列表，参数格式如 ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过 [查询默认的可设置参数列表](https://cloud.tencent.com/document/api/236/32662) 查询支持设置的参数。
        :type ParamList: list of ParamInfo
        :param ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type ProtectMode: int
        :param DeployMode: 多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type DeployMode: int
        :param SlaveZone: 备库 1 的可用区信息，默认为 Zone 的值，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type SlaveZone: str
        :param BackupZone: 备库 2 的可用区信息，默认为空，购买三节点主实例时可指定该参数。
        :type BackupZone: str
        :param SecurityGroup: 安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。
        :type SecurityGroup: list of str
        :param RoGroup: 只读实例信息。购买只读实例时，该参数必传。
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param AutoRenewFlag: 购买按量计费实例该字段无意义。
        :type AutoRenewFlag: int
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param ResourceTags: 实例标签信息。
        :type ResourceTags: list of TagInfo
        :param DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间在当天内唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param ParamTemplateId: 参数模板id。
        :type ParamTemplateId: int
        :param AlarmPolicyList: 告警策略id数组。
        :type AlarmPolicyList: list of int
        :param InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要购买三节点实例， 请将该值设置为3 或指定 BackupZone 参数。当购买主实例，且未指定该参数和 BackupZone 参数时，该值默认是 2， 即购买两节点实例。
        :type InstanceNodes: int
        :param Cpu: 实例cpu核数， 如果不传将根据memory指定的内存值自动填充对应的cpu值。
        :type Cpu: int
        :param AutoSyncFlag: 是否自动发起灾备同步功能。该参数仅对购买灾备实例生效。 可选值为：0 - 不自动发起灾备同步；1 - 自动发起灾备同步。该值默认为0。
        :type AutoSyncFlag: int
        :param CageId: 金融围拢 ID 。
        :type CageId: str
        :param ParamTemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模板，"HIGH_PERFORMANCE" - 高性能模板。
        :type ParamTemplateType: str
        :param AlarmPolicyIdList: 告警策略名数组，例如:["policy-uyoee9wg"]，AlarmPolicyList不为空时该参数无效。
        :type AlarmPolicyIdList: list of str
        :param DryRun: 是否只预检此次请求。true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制等。如果检查不通过，则返回对应错误码；如果检查通过，则返回RequestId.默认为false：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
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
        self.ResourceTags = None
        self.DeployGroupId = None
        self.ClientToken = None
        self.DeviceType = None
        self.ParamTemplateId = None
        self.AlarmPolicyList = None
        self.InstanceNodes = None
        self.Cpu = None
        self.AutoSyncFlag = None
        self.CageId = None
        self.ParamTemplateType = None
        self.AlarmPolicyIdList = None
        self.DryRun = None


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
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DeployGroupId = params.get("DeployGroupId")
        self.ClientToken = params.get("ClientToken")
        self.DeviceType = params.get("DeviceType")
        self.ParamTemplateId = params.get("ParamTemplateId")
        self.AlarmPolicyList = params.get("AlarmPolicyList")
        self.InstanceNodes = params.get("InstanceNodes")
        self.Cpu = params.get("Cpu")
        self.AutoSyncFlag = params.get("AutoSyncFlag")
        self.CageId = params.get("CageId")
        self.ParamTemplateType = params.get("ParamTemplateType")
        self.AlarmPolicyIdList = params.get("AlarmPolicyIdList")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealIds: 短订单 ID。
        :type DealIds: list of str
        :param InstanceIds: 实例 ID 列表。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param Memory: 实例内存大小，单位：MB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的内存规格。
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的硬盘范围。
        :type Volume: int
        :param Period: 实例时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type Period: int
        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为100。
        :type GoodsNum: int
        :param Zone: 可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的可用区。
        :type Zone: str
        :param UniqVpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 [查询子网列表](/document/api/215/15784)。
        :type UniqSubnetId: str
        :param ProjectId: 项目 ID，不填为默认项目。请使用 [查询项目列表](https://cloud.tencent.com/document/product/378/4400) 接口获取项目 ID。购买只读实例和灾备实例时，项目 ID 默认和主实例保持一致。
        :type ProjectId: int
        :param Port: 自定义端口，端口支持范围：[ 1024-65535 ]。
        :type Port: int
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。
        :type InstanceRole: str
        :param MasterInstanceId: 实例 ID，购买只读实例时必填，该字段表示只读实例的主实例ID，请使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询云数据库实例 ID。
        :type MasterInstanceId: str
        :param EngineVersion: MySQL 版本，值包括：5.5、5.6 和 5.7，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的实例版本。
        :type EngineVersion: str
        :param Password: 设置 root 帐号密码，密码规则：8 - 64 个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。
        :type Password: str
        :param ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。
        :type ProtectMode: int
        :param DeployMode: 多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区。
        :type DeployMode: int
        :param SlaveZone: 备库 1 的可用区信息，默认为 Zone 的值。
        :type SlaveZone: str
        :param ParamList: 参数列表，参数格式如 ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过 [查询默认的可设置参数列表](https://cloud.tencent.com/document/api/236/32662) 查询支持设置的参数。
        :type ParamList: list of ParamInfo
        :param BackupZone: 备库 2 的可用区信息，默认为空，购买三节点主实例时可指定该参数。
        :type BackupZone: str
        :param AutoRenewFlag: 自动续费标记，可选值为：0 - 不自动续费；1 - 自动续费。
        :type AutoRenewFlag: int
        :param MasterRegion: 主实例地域信息，购买灾备实例时，该字段必填。
        :type MasterRegion: str
        :param SecurityGroup: 安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。
        :type SecurityGroup: list of str
        :param RoGroup: 只读实例参数。购买只读实例时，该参数必传。
        :type RoGroup: :class:`tencentcloud.cdb.v20170320.models.RoGroup`
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param ResourceTags: 实例标签信息。
        :type ResourceTags: list of TagInfo
        :param DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间在当天内唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param ParamTemplateId: 参数模板id。
        :type ParamTemplateId: int
        :param AlarmPolicyList: 告警策略id数组。
        :type AlarmPolicyList: list of int
        :param InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要购买三节点实例， 请将该值设置为3 或指定 BackupZone 参数。当购买主实例，且未指定该参数和 BackupZone 参数时，该值默认是 2， 即购买两节点实例。
        :type InstanceNodes: int
        :param Cpu: 实例cpu核数， 如果不传将根据memory指定的内存值自动填充对应的cpu值。
        :type Cpu: int
        :param AutoSyncFlag: 是否自动发起灾备同步功能。该参数仅对购买灾备实例生效。 可选值为：0 - 不自动发起灾备同步；1 - 自动发起灾备同步。该值默认为0。
        :type AutoSyncFlag: int
        :param CageId: 金融围拢 ID。
        :type CageId: str
        :param ParamTemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模板，"HIGH_PERFORMANCE" - 高性能模板。
        :type ParamTemplateType: str
        :param AlarmPolicyIdList: 告警策略名数组，例如:["policy-uyoee9wg"]，AlarmPolicyList不为空时该参数无效。
        :type AlarmPolicyIdList: list of str
        :param DryRun: 是否只预检此次请求。true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制等。如果检查不通过，则返回对应错误码；如果检查通过，则返回RequestId.默认为false：发送正常请求，通过检查后直接创建实例。
        :type DryRun: bool
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
        self.ResourceTags = None
        self.DeployGroupId = None
        self.ClientToken = None
        self.DeviceType = None
        self.ParamTemplateId = None
        self.AlarmPolicyList = None
        self.InstanceNodes = None
        self.Cpu = None
        self.AutoSyncFlag = None
        self.CageId = None
        self.ParamTemplateType = None
        self.AlarmPolicyIdList = None
        self.DryRun = None


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
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DeployGroupId = params.get("DeployGroupId")
        self.ClientToken = params.get("ClientToken")
        self.DeviceType = params.get("DeviceType")
        self.ParamTemplateId = params.get("ParamTemplateId")
        self.AlarmPolicyList = params.get("AlarmPolicyList")
        self.InstanceNodes = params.get("InstanceNodes")
        self.Cpu = params.get("Cpu")
        self.AutoSyncFlag = params.get("AutoSyncFlag")
        self.CageId = params.get("CageId")
        self.ParamTemplateType = params.get("ParamTemplateType")
        self.AlarmPolicyIdList = params.get("AlarmPolicyIdList")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealIds: 短订单 ID。
        :type DealIds: list of str
        :param InstanceIds: 实例 ID 列表。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDeployGroupRequest(AbstractModel):
    """CreateDeployGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployGroupName: 置放群组名称，最长不能超过60个字符。
        :type DeployGroupName: str
        :param Description: 置放群组描述，最长不能超过200个字符。
        :type Description: str
        :param Affinity: 置放群组的亲和性策略，目前仅支持取值为1，策略1表示同台物理机上限制实例的个数。
        :type Affinity: list of int
        :param LimitNum: 置放群组亲和性策略1中同台物理机上实例的限制个数。
        :type LimitNum: int
        :param DevClass: 置放群组机型属性，可选参数：SH12+SH02、TS85。
        :type DevClass: list of str
        """
        self.DeployGroupName = None
        self.Description = None
        self.Affinity = None
        self.LimitNum = None
        self.DevClass = None


    def _deserialize(self, params):
        self.DeployGroupName = params.get("DeployGroupName")
        self.Description = params.get("Description")
        self.Affinity = params.get("Affinity")
        self.LimitNum = params.get("LimitNum")
        self.DevClass = params.get("DevClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeployGroupResponse(AbstractModel):
    """CreateDeployGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeployGroupId: 置放群组ID。
        :type DeployGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeployGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 参数模板名称。
        :type Name: str
        :param Description: 参数模板描述。
        :type Description: str
        :param EngineVersion: MySQL 版本号。
        :type EngineVersion: str
        :param TemplateId: 源参数模板 ID。
        :type TemplateId: int
        :param ParamList: 参数列表。
        :type ParamList: list of Parameter
        :param TemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模版，"HIGH_PERFORMANCE" - 高性能模版。
        :type TemplateType: str
        """
        self.Name = None
        self.Description = None
        self.EngineVersion = None
        self.TemplateId = None
        self.ParamList = None
        self.TemplateType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.EngineVersion = params.get("EngineVersion")
        self.TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.TemplateType = params.get("TemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板 ID。
        :type TemplateId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateRoInstanceIpRequest(AbstractModel):
    """CreateRoInstanceIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 只读实例ID，格式如：cdbro-3i70uj0k，与云数据库控制台页面中显示的只读实例ID相同。
        :type InstanceId: str
        :param UniqSubnetId: 子网描述符，例如：subnet-1typ0s7d。
        :type UniqSubnetId: str
        :param UniqVpcId: vpc描述符，例如：vpc-a23yt67j,如果传了该字段则UniqSubnetId必传
        :type UniqVpcId: str
        """
        self.InstanceId = None
        self.UniqSubnetId = None
        self.UniqVpcId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoInstanceIpResponse(AbstractModel):
    """CreateRoInstanceIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoVpcId: 只读实例的私有网络的ID。
        :type RoVpcId: int
        :param RoSubnetId: 只读实例的子网ID。
        :type RoSubnetId: int
        :param RoVip: 只读实例的内网IP地址。
        :type RoVip: str
        :param RoVport: 只读实例的内网端口号。
        :type RoVport: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoVpcId = None
        self.RoSubnetId = None
        self.RoVip = None
        self.RoVport = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoVpcId = params.get("RoVpcId")
        self.RoSubnetId = params.get("RoSubnetId")
        self.RoVip = params.get("RoVip")
        self.RoVport = params.get("RoVport")
        self.RequestId = params.get("RequestId")


class CustomConfig(AbstractModel):
    """proxy配置

    """

    def __init__(self):
        r"""
        :param Device: 设备
注意：此字段可能返回 null，表示取不到有效值。
        :type Device: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param DeviceType: 设备类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param Memory: 内存
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param Cpu: 核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        """
        self.Device = None
        self.Type = None
        self.DeviceType = None
        self.Memory = None
        self.Cpu = None


    def _deserialize(self, params):
        self.Device = params.get("Device")
        self.Type = params.get("Type")
        self.DeviceType = params.get("DeviceType")
        self.Memory = params.get("Memory")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBSwitchInfo(AbstractModel):
    """云数据库切换记录

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseName(AbstractModel):
    """数据库表名

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库表名
        :type DatabaseName: str
        """
        self.DatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivilege(AbstractModel):
    """数据库权限

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasesWithCharacterLists(AbstractModel):
    """数据库名以及字符集

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库名
        :type DatabaseName: str
        :param CharacterSet: 字符集类型
        :type CharacterSet: str
        """
        self.DatabaseName = None
        self.CharacterSet = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.CharacterSet = params.get("CharacterSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class DeleteAuditLogFileRequest(AbstractModel):
    """DeleteAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileName: 审计日志文件名称。
        :type FileName: str
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self.FileName = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditLogFileResponse(AbstractModel):
    """DeleteAuditLogFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAuditPolicyRequest(AbstractModel):
    """DeleteAuditPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        """
        self.PolicyId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditPolicyResponse(AbstractModel):
    """DeleteAuditPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAuditRuleRequest(AbstractModel):
    """DeleteAuditRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 审计规则 ID。
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditRuleResponse(AbstractModel):
    """DeleteAuditRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param BackupId: 备份任务 ID。该任务 ID 为 [创建云数据库备份](https://cloud.tencent.com/document/api/236/15844) 接口返回的任务 ID。
        :type BackupId: int
        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeployGroupsRequest(AbstractModel):
    """DeleteDeployGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployGroupIds: 要删除的置放群组 ID 列表。
        :type DeployGroupIds: list of str
        """
        self.DeployGroupIds = None


    def _deserialize(self, params):
        self.DeployGroupIds = params.get("DeployGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeployGroupsResponse(AbstractModel):
    """DeleteDeployGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTimeWindowRequest(AbstractModel):
    """DeleteTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTimeWindowResponse(AbstractModel):
    """DeleteTimeWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeployGroupInfo(AbstractModel):
    """置放群组信息

    """

    def __init__(self):
        r"""
        :param DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param DeployGroupName: 置放群组名称。
        :type DeployGroupName: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param Quota: 置放群组实例配额，表示一个置放群组中可容纳的最大实例数目。
        :type Quota: int
        :param Affinity: 置放群组亲和性策略，目前仅支持策略1，即在物理机纬度打散实例的分布。
注意：此字段可能返回 null，表示取不到有效值。
        :type Affinity: str
        :param LimitNum: 置放群组亲和性策略1中，同台物理机上同个置放群组实例的限制个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitNum: int
        :param Description: 置放群组详细信息。
        :type Description: str
        :param DevClass: 置放群组物理机型属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type DevClass: str
        """
        self.DeployGroupId = None
        self.DeployGroupName = None
        self.CreateTime = None
        self.Quota = None
        self.Affinity = None
        self.LimitNum = None
        self.Description = None
        self.DevClass = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.DeployGroupName = params.get("DeployGroupName")
        self.CreateTime = params.get("CreateTime")
        self.Quota = params.get("Quota")
        self.Affinity = params.get("Affinity")
        self.LimitNum = params.get("LimitNum")
        self.Description = params.get("Description")
        self.DevClass = params.get("DevClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param GlobalPrivileges: 全局权限数组。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 数据库权限数组。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: 数据库中的表权限数组。
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: 数据库表中的列权限数组。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param AccountRegexp: 匹配账号名的正则表达式，规则同 MySQL 官网。
        :type AccountRegexp: str
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.AccountRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AccountRegexp = params.get("AccountRegexp")
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
        r"""
        :param TotalCount: 符合查询条件的账号数量。
        :type TotalCount: int
        :param Items: 符合查询条件的账号详细信息。
        :type Items: list of AccountInfo
        :param MaxUserConnections: 用户可设置实例最大连接数。
        :type MaxUserConnections: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.MaxUserConnections = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.MaxUserConnections = params.get("MaxUserConnections")
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID。
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 任务执行结果。可能的取值：INITIAL - 初始化，RUNNING - 运行中，SUCCESS - 执行成功，FAILED - 执行失败，KILLED - 已终止，REMOVED - 已删除，PAUSED - 终止中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Info: 任务执行信息描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DescribeAuditConfigRequest(AbstractModel):
    """DescribeAuditConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditConfigResponse(AbstractModel):
    """DescribeAuditConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogExpireDay: 审计日志保存时长。目前支持的值包括：[0，7，30，180，365，1095，1825]。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogExpireDay: int
        :param LogType: 审计日志存储类型。目前支持的值包括："storage" - 存储型。
        :type LogType: str
        :param IsClosing: 是否正在关闭审计。目前支持的值包括："false"-否，"true"-是
        :type IsClosing: str
        :param CreateTime: 审计服务开通时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogExpireDay = None
        self.LogType = None
        self.IsClosing = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogExpireDay = params.get("LogExpireDay")
        self.LogType = params.get("LogType")
        self.IsClosing = params.get("IsClosing")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DescribeAuditLogFilesRequest(AbstractModel):
    """DescribeAuditLogFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param Offset: 分页偏移量。
        :type Offset: int
        :param FileName: 审计日志文件名。
        :type FileName: str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.FileName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogFilesResponse(AbstractModel):
    """DescribeAuditLogFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的审计日志文件个数。
        :type TotalCount: int
        :param Items: 审计日志文件详情。
        :type Items: list of AuditLogFile
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = AuditLogFile()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAuditPoliciesRequest(AbstractModel):
    """DescribeAuditPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param PolicyId: 审计策略 ID。
        :type PolicyId: str
        :param PolicyName: 审计策略名称。支持按审计策略名称进行模糊匹配查询。
        :type PolicyName: str
        :param Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param Offset: 分页偏移量。
        :type Offset: int
        :param RuleId: 审计规则 ID。可使用该审计规则 ID 查询到其关联的审计策略。
注意，参数 RuleId，InstanceId，PolicyId，PolicyName 必须至少传一个。
        :type RuleId: str
        """
        self.InstanceId = None
        self.PolicyId = None
        self.PolicyName = None
        self.Limit = None
        self.Offset = None
        self.RuleId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditPoliciesResponse(AbstractModel):
    """DescribeAuditPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的审计策略个数。
        :type TotalCount: int
        :param Items: 审计策略详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = AuditPolicy()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAuditRulesRequest(AbstractModel):
    """DescribeAuditRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 审计规则 ID。
        :type RuleId: str
        :param RuleName: 审计规则名称。支持按审计规则名称进行模糊匹配查询。
        :type RuleName: str
        :param Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param Offset: 分页偏移量。
        :type Offset: int
        """
        self.RuleId = None
        self.RuleName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRulesResponse(AbstractModel):
    """DescribeAuditRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的审计规则个数。
        :type TotalCount: int
        :param Items: 审计规则详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = AuditRule()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param StartTimeMin: 自动备份开始的最早时间点，单位为时刻。例如，2 - 凌晨 2:00。（该字段已废弃，建议使用 BackupTimeWindow 字段）
        :type StartTimeMin: int
        :param StartTimeMax: 自动备份开始的最晚时间点，单位为时刻。例如，6 - 凌晨 6:00。（该字段已废弃，建议使用 BackupTimeWindow 字段）
        :type StartTimeMax: int
        :param BackupExpireDays: 备份文件保留时间，单位为天。
        :type BackupExpireDays: int
        :param BackupMethod: 备份方式，可能的值为：physical - 物理备份，logical - 逻辑备份。
        :type BackupMethod: str
        :param BinlogExpireDays: Binlog 文件保留时间，单位为天。
        :type BinlogExpireDays: int
        :param BackupTimeWindow: 实例自动备份的时间窗。
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StartTimeMin = None
        self.StartTimeMax = None
        self.BackupExpireDays = None
        self.BackupMethod = None
        self.BinlogExpireDays = None
        self.BackupTimeWindow = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTimeMin = params.get("StartTimeMin")
        self.StartTimeMax = params.get("StartTimeMax")
        self.BackupExpireDays = params.get("BackupExpireDays")
        self.BackupMethod = params.get("BackupMethod")
        self.BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self.BackupTimeWindow = CommonTimeWindow()
            self.BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        self.RequestId = params.get("RequestId")


class DescribeBackupDatabasesRequest(AbstractModel):
    """DescribeBackupDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDatabasesResponse(AbstractModel):
    """DescribeBackupDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的数据个数。
        :type TotalCount: int
        :param Items: 符合查询条件的数据库数组。
        :type Items: list of DatabaseName
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeBackupDownloadRestrictionRequest(AbstractModel):
    """DescribeBackupDownloadRestriction请求参数结构体

    """


class DescribeBackupDownloadRestrictionResponse(AbstractModel):
    """DescribeBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param LimitType: NoLimit 不限制,内外网都可以下载； LimitOnlyIntranet 仅内网可下载； Customize 用户自定义vpc:ip可下载。 只有该值为 Customize 时， LimitVpc 和 LimitIp 才有意义。
        :type LimitType: str
        :param VpcComparisonSymbol: 该参数仅支持 In， 表示 LimitVpc 指定的vpc可以下载。
        :type VpcComparisonSymbol: str
        :param IpComparisonSymbol: In: 指定的ip可以下载； NotIn: 指定的ip不可以下载。
        :type IpComparisonSymbol: str
        :param LimitVpc: 限制下载的vpc设置。
        :type LimitVpc: list of BackupLimitVpcItem
        :param LimitIp: 限制下载的ip设置。
        :type LimitIp: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LimitType = None
        self.VpcComparisonSymbol = None
        self.IpComparisonSymbol = None
        self.LimitVpc = None
        self.LimitIp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LimitType = params.get("LimitType")
        self.VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self.IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self.LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self.LimitVpc.append(obj)
        self.LimitIp = params.get("LimitIp")
        self.RequestId = params.get("RequestId")


class DescribeBackupOverviewRequest(AbstractModel):
    """DescribeBackupOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupOverviewResponse(AbstractModel):
    """DescribeBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param BackupCount: 用户在当前地域备份的总个数（包含数据备份和日志备份）。
        :type BackupCount: int
        :param BackupVolume: 用户在当前地域备份的总容量
        :type BackupVolume: int
        :param BillingVolume: 用户在当前地域备份的计费容量，即超出赠送容量的部分。
        :type BillingVolume: int
        :param FreeVolume: 用户在当前地域获得的赠送备份容量。
        :type FreeVolume: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupCount = None
        self.BackupVolume = None
        self.BillingVolume = None
        self.FreeVolume = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupCount = params.get("BackupCount")
        self.BackupVolume = params.get("BackupVolume")
        self.BillingVolume = params.get("BillingVolume")
        self.FreeVolume = params.get("FreeVolume")
        self.RequestId = params.get("RequestId")


class DescribeBackupSummariesRequest(AbstractModel):
    """DescribeBackupSummaries请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        :param Offset: 分页查询数据的偏移量，默认为0。
        :type Offset: int
        :param Limit: 分页查询数据的条目限制，默认值为20。最小值为1，最大值为100。
        :type Limit: int
        :param OrderBy: 指定按某一项排序，可选值包括： BackupVolume: 备份容量， DataBackupVolume: 数据备份容量， BinlogBackupVolume: 日志备份容量， AutoBackupVolume: 自动备份容量， ManualBackupVolume: 手动备份容量。默认按照BackupVolume排序。
        :type OrderBy: str
        :param OrderDirection: 指定排序方向，可选值包括： ASC: 正序， DESC: 逆序。默认值为 ASC。
        :type OrderDirection: str
        """
        self.Product = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupSummariesResponse(AbstractModel):
    """DescribeBackupSummaries返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 实例备份统计条目。
        :type Items: list of BackupSummaryItem
        :param TotalCount: 实例备份统计总条目数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = BackupSummaryItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBackupTablesRequest(AbstractModel):
    """DescribeBackupTables请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupTablesResponse(AbstractModel):
    """DescribeBackupTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的数据个数。
        :type TotalCount: int
        :param Items: 符合条件的数据表数组。
        :type Items: list of TableName
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
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
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 符合查询条件的备份信息详情。
        :type Items: list of BackupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeBinlogBackupOverviewRequest(AbstractModel):
    """DescribeBinlogBackupOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogBackupOverviewResponse(AbstractModel):
    """DescribeBinlogBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param BinlogBackupVolume: 总的日志备份容量（单位为字节）。
        :type BinlogBackupVolume: int
        :param BinlogBackupCount: 总的日志备份个数。
        :type BinlogBackupCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BinlogBackupVolume = None
        self.BinlogBackupCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BinlogBackupVolume = params.get("BinlogBackupVolume")
        self.BinlogBackupCount = params.get("BinlogBackupCount")
        self.RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的日志文件总数。
        :type TotalCount: int
        :param Items: 符合查询条件的二进制日志文件详情。
        :type Items: list of BinlogInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeCDBProxyRequest(AbstractModel):
    """DescribeCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProxyGroupId: 代理ID
        :type ProxyGroupId: str
        """
        self.InstanceId = None
        self.ProxyGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCDBProxyResponse(AbstractModel):
    """DescribeCDBProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param BaseGroup: 代理组基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseGroup: :class:`tencentcloud.cdb.v20170320.models.BaseGroupInfo`
        :param Address: 代理组地址信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: :class:`tencentcloud.cdb.v20170320.models.Address`
        :param ProxyNode: 代理组节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNode: :class:`tencentcloud.cdb.v20170320.models.ProxyNodeInfo`
        :param RWInstInfo: 读写分析信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInfo`
        :param ConnectionPoolInfo: 连接池信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolInfo: :class:`tencentcloud.cdb.v20170320.models.ConnectionPoolInfo`
        :param Count: 代理数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param ProxyGroup: 代理信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyGroup: list of ProxyGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaseGroup = None
        self.Address = None
        self.ProxyNode = None
        self.RWInstInfo = None
        self.ConnectionPoolInfo = None
        self.Count = None
        self.ProxyGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BaseGroup") is not None:
            self.BaseGroup = BaseGroupInfo()
            self.BaseGroup._deserialize(params.get("BaseGroup"))
        if params.get("Address") is not None:
            self.Address = Address()
            self.Address._deserialize(params.get("Address"))
        if params.get("ProxyNode") is not None:
            self.ProxyNode = ProxyNodeInfo()
            self.ProxyNode._deserialize(params.get("ProxyNode"))
        if params.get("RWInstInfo") is not None:
            self.RWInstInfo = RWInfo()
            self.RWInstInfo._deserialize(params.get("RWInstInfo"))
        if params.get("ConnectionPoolInfo") is not None:
            self.ConnectionPoolInfo = ConnectionPoolInfo()
            self.ConnectionPoolInfo._deserialize(params.get("ConnectionPoolInfo"))
        self.Count = params.get("Count")
        if params.get("ProxyGroup") is not None:
            self.ProxyGroup = []
            for item in params.get("ProxyGroup"):
                obj = ProxyGroup()
                obj._deserialize(item)
                self.ProxyGroup.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloneListRequest(AbstractModel):
    """DescribeCloneList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 查询指定源实例的克隆任务列表。
        :type InstanceId: str
        :param Offset: 分页查询时的偏移量，默认值为0。
        :type Offset: int
        :param Limit: 分页查询时的每页条目数，默认值为20。
        :type Limit: int
        """
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
        


class DescribeCloneListResponse(AbstractModel):
    """DescribeCloneList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 满足条件的条目数。
        :type TotalCount: int
        :param Items: 克隆任务列表。
        :type Items: list of CloneItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = CloneItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBImportRecordsRequest(AbstractModel):
    """DescribeDBImportRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param StartTime: 开始时间，时间格式如：2016-01-01 00:00:01。
        :type StartTime: str
        :param EndTime: 结束时间，时间格式如：2016-01-01 23:59:59。
        :type EndTime: str
        :param Offset: 分页参数，偏移量，默认值为0。
        :type Offset: int
        :param Limit: 分页参数，单次请求返回的数量，默认值为20，最小值为1，最大值为100。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBImportRecordsResponse(AbstractModel):
    """DescribeDBImportRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的导入任务操作日志总数。
        :type TotalCount: int
        :param Items: 返回的导入操作记录列表。
        :type Items: list of ImportRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceCharsetResponse(AbstractModel):
    """DescribeDBInstanceCharset返回参数结构体

    """

    def __init__(self):
        r"""
        :param Charset: 实例的默认字符集，如 "latin1"，"utf8" 等。
        :type Charset: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceConfigResponse(AbstractModel):
    """DescribeDBInstanceConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProtectMode: 主实例数据保护方式，可能的返回值：0 - 异步复制方式，1 - 半同步复制方式，2 - 强同步复制方式。
        :type ProtectMode: int
        :param DeployMode: 主实例部署方式，可能的返回值：0 - 单可用部署，1 - 多可用区部署。
        :type DeployMode: int
        :param Zone: 实例可用区信息，格式如 "ap-shanghai-1"。
        :type Zone: str
        :param SlaveConfig: 备库的配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveConfig: :class:`tencentcloud.cdb.v20170320.models.SlaveConfig`
        :param BackupConfig: 强同步实例第二备库的配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupConfig: :class:`tencentcloud.cdb.v20170320.models.BackupConfig`
        :param Switched: 是否切换备库。
        :type Switched: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProtectMode = None
        self.DeployMode = None
        self.Zone = None
        self.SlaveConfig = None
        self.BackupConfig = None
        self.Switched = None
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
        self.Switched = params.get("Switched")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceGTIDRequest(AbstractModel):
    """DescribeDBInstanceGTID请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceGTIDResponse(AbstractModel):
    """DescribeDBInstanceGTID返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsGTIDOpen: GTID 是否开通的标记，可能的取值为：0 - 未开通，1 - 已开通。
        :type IsGTIDOpen: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsGTIDOpen = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsGTIDOpen = params.get("IsGTIDOpen")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceInfoRequest(AbstractModel):
    """DescribeDBInstanceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceInfoResponse(AbstractModel):
    """DescribeDBInstanceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param Encryption: 是否开通加密，YES 已开通，NO 未开通。
        :type Encryption: str
        :param KeyId: 加密使用的密钥 ID 。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param KeyRegion: 密钥所在地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyRegion: str
        :param DefaultKmsRegion: 当前 CDB 后端服务使用的 KMS 服务的默认地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultKmsRegion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Encryption = None
        self.KeyId = None
        self.KeyRegion = None
        self.DefaultKmsRegion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Encryption = params.get("Encryption")
        self.KeyId = params.get("KeyId")
        self.KeyRegion = params.get("KeyRegion")
        self.DefaultKmsRegion = params.get("DefaultKmsRegion")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceRebootTimeRequest(AbstractModel):
    """DescribeDBInstanceRebootTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceRebootTimeResponse(AbstractModel):
    """DescribeDBInstanceRebootTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 返回的参数信息。
        :type Items: list of InstanceRebootTime
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param ProjectId: 项目 ID，可使用 [查询项目列表](https://cloud.tencent.com/document/product/378/4400) 接口查询项目 ID。
        :type ProjectId: int
        :param InstanceTypes: 实例类型，可取值：1 - 主实例，2 - 灾备实例，3 - 只读实例。
        :type InstanceTypes: list of int non-negative
        :param Vips: 实例的内网 IP 地址。
        :type Vips: list of str
        :param Status: 实例状态，可取值：<br>0 - 创建中<br>1 - 运行中<br>4 - 正在进行隔离操作<br>5 - 隔离中（可在回收站恢复开机）
        :type Status: list of int non-negative
        :param Offset: 偏移量，默认值为 0。
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为 20，最大值为 2000。
        :type Limit: int
        :param SecurityGroupId: 安全组 ID。当使用安全组 ID 为过滤条件时，需指定 WithSecurityGroup 参数为 1。
        :type SecurityGroupId: str
        :param PayTypes: 付费类型，可取值：0 - 包年包月，1 - 小时计费。
        :type PayTypes: list of int non-negative
        :param InstanceNames: 实例名称。
        :type InstanceNames: list of str
        :param TaskStatus: 实例任务状态，可能取值：<br>0 - 没有任务<br>1 - 升级中<br>2 - 数据导入中<br>3 - 开放Slave中<br>4 - 外网访问开通中<br>5 - 批量操作执行中<br>6 - 回档中<br>7 - 外网访问关闭中<br>8 - 密码修改中<br>9 - 实例名修改中<br>10 - 重启中<br>12 - 自建迁移中<br>13 - 删除库表中<br>14 - 灾备实例创建同步中<br>15 - 升级待切换<br>16 - 升级切换中<br>17 - 升级切换完成<br>19 - 参数设置待执行
        :type TaskStatus: list of int non-negative
        :param EngineVersions: 实例数据库引擎版本，可能取值：5.1、5.5、5.6 和 5.7。
        :type EngineVersions: list of str
        :param VpcIds: 私有网络的 ID。
        :type VpcIds: list of int non-negative
        :param ZoneIds: 可用区的 ID。
        :type ZoneIds: list of int non-negative
        :param SubnetIds: 子网 ID。
        :type SubnetIds: list of int non-negative
        :param CdbErrors: 是否锁定标记。
        :type CdbErrors: list of int
        :param OrderBy: 返回结果集排序的字段，目前支持："InstanceId"，"InstanceName"，"CreateTime"，"DeadlineTime"。
        :type OrderBy: str
        :param OrderDirection: 返回结果集排序方式，目前支持："ASC" 或者 "DESC"。
        :type OrderDirection: str
        :param WithSecurityGroup: 是否以安全组 ID 为过滤条件。
        :type WithSecurityGroup: int
        :param WithExCluster: 是否包含独享集群详细信息，可取值：0 - 不包含，1 - 包含。
        :type WithExCluster: int
        :param ExClusterId: 独享集群 ID。
        :type ExClusterId: str
        :param InstanceIds: 实例 ID。
        :type InstanceIds: list of str
        :param InitFlag: 初始化标记，可取值：0 - 未初始化，1 - 初始化。
        :type InitFlag: int
        :param WithDr: 是否包含灾备关系对应的实例，可取值：0 - 不包含，1 - 包含。默认取值为1。如果拉取主实例，则灾备关系的数据在DrInfo字段中， 如果拉取灾备实例， 则灾备关系的数据在MasterInfo字段中。灾备关系中只包含部分基本的数据，详细的数据需要自行调接口拉取。
        :type WithDr: int
        :param WithRo: 是否包含只读实例，可取值：0 - 不包含，1 - 包含。默认取值为1。
        :type WithRo: int
        :param WithMaster: 是否包含主实例，可取值：0 - 不包含，1 - 包含。默认取值为1。
        :type WithMaster: int
        :param DeployGroupIds: 置放群组ID列表。
        :type DeployGroupIds: list of str
        :param TagKeysForSearch: 是否以标签键为过滤条件。
        :type TagKeysForSearch: list of str
        :param CageIds: 金融围拢 ID 。
        :type CageIds: list of str
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
        self.DeployGroupIds = None
        self.TagKeysForSearch = None
        self.CageIds = None


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
        self.DeployGroupIds = params.get("DeployGroupIds")
        self.TagKeysForSearch = params.get("TagKeysForSearch")
        self.CageIds = params.get("CageIds")
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
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 实例详细信息。
        :type Items: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param Period: 实例时长，单位：月，最小值 1，最大值为 36；查询按量计费价格时，该字段无效。
        :type Period: int
        :param Zone: 可用区信息，格式如 "ap-guangzhou-2"。具体能设置的值请通过 <a href="https://cloud.tencent.com/document/api/236/17229">DescribeDBZoneConfig</a> 接口查询。InstanceId为空时该参数为必填项。
        :type Zone: str
        :param GoodsNum: 实例数量，默认值为 1，最小值 1，最大值为 100。InstanceId为空时该参数为必填项。
        :type GoodsNum: int
        :param Memory: 实例内存大小，单位：MB。InstanceId为空时该参数为必填项。
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB。InstanceId为空时该参数为必填项。
        :type Volume: int
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，ro - 表示只读实例，dr - 表示灾备实例。InstanceId为空时该参数为必填项。
        :type InstanceRole: str
        :param PayType: 付费类型，支持值包括：PRE_PAID - 包年包月，HOUR_PAID - 按量计费。InstanceId为空时该参数为必填项。
        :type PayType: str
        :param ProtectMode: 数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。
        :type ProtectMode: int
        :param DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要询价三节点实例， 请将该值设置为3。其余主实例该值默认为2。
        :type InstanceNodes: int
        :param Cpu: 询价实例的CPU核心数目，单位：核，为保证传入 CPU 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可售卖的核心数目，当未指定该值时，将按照 Memory 大小补全一个默认值。
        :type Cpu: int
        :param InstanceId: 续费询价实例ID。如需查询实例续费价格，填写InstanceId和Period即可。
        :type InstanceId: str
        """
        self.Period = None
        self.Zone = None
        self.GoodsNum = None
        self.Memory = None
        self.Volume = None
        self.InstanceRole = None
        self.PayType = None
        self.ProtectMode = None
        self.DeviceType = None
        self.InstanceNodes = None
        self.Cpu = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.Zone = params.get("Zone")
        self.GoodsNum = params.get("GoodsNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.InstanceRole = params.get("InstanceRole")
        self.PayType = params.get("PayType")
        self.ProtectMode = params.get("ProtectMode")
        self.DeviceType = params.get("DeviceType")
        self.InstanceNodes = params.get("InstanceNodes")
        self.Cpu = params.get("Cpu")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPriceResponse(AbstractModel):
    """DescribeDBPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 实例价格，单位：分（人民币）。
        :type Price: int
        :param OriginalPrice: 实例原价，单位：分（人民币）。
        :type OriginalPrice: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param ForReadonlyInstance: 该值默认为False，表示当传入只读实例ID时，查询操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True。
        :type ForReadonlyInstance: bool
        """
        self.InstanceId = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
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
        r"""
        :param Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Offset: 分页偏移量。
        :type Offset: int
        :param Limit: 分页大小，默认值为 50，最小值为 1，最大值为 2000。
        :type Limit: int
        """
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
        


class DescribeDBSwitchRecordsResponse(AbstractModel):
    """DescribeDBSwitchRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例切换记录的总数。
        :type TotalCount: int
        :param Items: 实例切换记录详情。
        :type Items: list of DBSwitchInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param TotalCount: 可售卖地域配置数量
        :type TotalCount: int
        :param Items: 可售卖地域配置详情
        :type Items: list of RegionSellConf
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeDataBackupOverviewRequest(AbstractModel):
    """DescribeDataBackupOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 需要查询的云数据库产品类型，目前仅支持 "mysql"。
        :type Product: str
        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataBackupOverviewResponse(AbstractModel):
    """DescribeDataBackupOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataBackupVolume: 当前地域的数据备份总容量（包含自动备份和手动备份，单位为字节）。
        :type DataBackupVolume: int
        :param DataBackupCount: 当前地域的数据备份总个数。
        :type DataBackupCount: int
        :param AutoBackupVolume: 当前地域的自动备份总容量。
        :type AutoBackupVolume: int
        :param AutoBackupCount: 当前地域的自动备份总个数。
        :type AutoBackupCount: int
        :param ManualBackupVolume: 当前地域的手动备份总容量。
        :type ManualBackupVolume: int
        :param ManualBackupCount: 当前地域的手动备份总个数。
        :type ManualBackupCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataBackupVolume = None
        self.DataBackupCount = None
        self.AutoBackupVolume = None
        self.AutoBackupCount = None
        self.ManualBackupVolume = None
        self.ManualBackupCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataBackupVolume = params.get("DataBackupVolume")
        self.DataBackupCount = params.get("DataBackupCount")
        self.AutoBackupVolume = params.get("AutoBackupVolume")
        self.AutoBackupCount = params.get("AutoBackupCount")
        self.ManualBackupVolume = params.get("ManualBackupVolume")
        self.ManualBackupCount = params.get("ManualBackupCount")
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值为0。
        :type Offset: int
        :param Limit: 单次请求数量，默认值为20，最小值为1，最大值为100。
        :type Limit: int
        :param DatabaseRegexp: 匹配数据库库名的正则表达式。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 返回的实例信息。
        :type Items: list of str
        :param DatabaseList: 数据库名以及字符集
        :type DatabaseList: list of DatabasesWithCharacterLists
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.DatabaseList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        if params.get("DatabaseList") is not None:
            self.DatabaseList = []
            for item in params.get("DatabaseList"):
                obj = DatabasesWithCharacterLists()
                obj._deserialize(item)
                self.DatabaseList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDefaultParamsRequest(AbstractModel):
    """DescribeDefaultParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param EngineVersion: mysql版本，目前支持 ["5.1", "5.5", "5.6", "5.7"]。
        :type EngineVersion: str
        :param TemplateType: 默认参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模版，"HIGH_PERFORMANCE" - 高性能模版。
        :type TemplateType: str
        """
        self.EngineVersion = None
        self.TemplateType = None


    def _deserialize(self, params):
        self.EngineVersion = params.get("EngineVersion")
        self.TemplateType = params.get("TemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultParamsResponse(AbstractModel):
    """DescribeDefaultParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 参数个数。
        :type TotalCount: int
        :param Items: 参数详情。
        :type Items: list of ParameterDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeDeployGroupListRequest(AbstractModel):
    """DescribeDeployGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param DeployGroupName: 置放群组名称。
        :type DeployGroupName: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.DeployGroupId = None
        self.DeployGroupName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.DeployGroupName = params.get("DeployGroupName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployGroupListResponse(AbstractModel):
    """DescribeDeployGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 符合条件的记录总数。
        :type Total: int
        :param Items: 返回列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DeployGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DeployGroupInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceMonitorInfoRequest(AbstractModel):
    """DescribeDeviceMonitorInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Count: 返回当天最近Count个5分钟粒度的监控数据。最小值1，最大值288，不传该参数默认返回当天所有5分钟粒度监控数据。
        :type Count: int
        """
        self.InstanceId = None
        self.Count = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceMonitorInfoResponse(AbstractModel):
    """DescribeDeviceMonitorInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Cpu: 实例CPU监控数据
        :type Cpu: :class:`tencentcloud.cdb.v20170320.models.DeviceCpuInfo`
        :param Mem: 实例内存监控数据
        :type Mem: :class:`tencentcloud.cdb.v20170320.models.DeviceMemInfo`
        :param Net: 实例网络监控数据
        :type Net: :class:`tencentcloud.cdb.v20170320.models.DeviceNetInfo`
        :param Disk: 实例磁盘监控数据
        :type Disk: :class:`tencentcloud.cdb.v20170320.models.DeviceDiskInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Cpu = None
        self.Mem = None
        self.Net = None
        self.Disk = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cpu") is not None:
            self.Cpu = DeviceCpuInfo()
            self.Cpu._deserialize(params.get("Cpu"))
        if params.get("Mem") is not None:
            self.Mem = DeviceMemInfo()
            self.Mem._deserialize(params.get("Mem"))
        if params.get("Net") is not None:
            self.Net = DeviceNetInfo()
            self.Net._deserialize(params.get("Net"))
        if params.get("Disk") is not None:
            self.Disk = DeviceDiskInfo()
            self.Disk._deserialize(params.get("Disk"))
        self.RequestId = params.get("RequestId")


class DescribeErrorLogDataRequest(AbstractModel):
    """DescribeErrorLogData请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间戳。
        :type StartTime: int
        :param EndTime: 结束时间戳。
        :type EndTime: int
        :param KeyWords: 要匹配的关键字列表，最多支持15个关键字。
        :type KeyWords: list of str
        :param Limit: 分页的返回数量，默认为100，最大为400。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param InstType: 仅在实例为主实例或者灾备实例时生效，可选值：slave，代表拉取从机的日志。
        :type InstType: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.KeyWords = None
        self.Limit = None
        self.Offset = None
        self.InstType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.KeyWords = params.get("KeyWords")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorLogDataResponse(AbstractModel):
    """DescribeErrorLogData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param Items: 返回的记录。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ErrlogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = ErrlogItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param Offset: 分页偏移量。
        :type Offset: int
        :param Limit: 分页大小。
        :type Limit: int
        """
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
        r"""
        :param TotalCount: 符合条件的记录数。
        :type TotalCount: int
        :param Items: 参数修改记录。
        :type Items: list of ParamRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = ParamRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
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
        r"""
        :param TotalCount: 实例的参数总数。
        :type TotalCount: int
        :param Items: 参数详情。
        :type Items: list of ParameterDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeLocalBinlogConfigRequest(AbstractModel):
    """DescribeLocalBinlogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLocalBinlogConfigResponse(AbstractModel):
    """DescribeLocalBinlogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param LocalBinlogConfig: 实例binlog保留策略。
        :type LocalBinlogConfig: :class:`tencentcloud.cdb.v20170320.models.LocalBinlogConfig`
        :param LocalBinlogConfigDefault: 该地域默认binlog保留策略。
        :type LocalBinlogConfigDefault: :class:`tencentcloud.cdb.v20170320.models.LocalBinlogConfigDefault`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LocalBinlogConfig = None
        self.LocalBinlogConfigDefault = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LocalBinlogConfig") is not None:
            self.LocalBinlogConfig = LocalBinlogConfig()
            self.LocalBinlogConfig._deserialize(params.get("LocalBinlogConfig"))
        if params.get("LocalBinlogConfigDefault") is not None:
            self.LocalBinlogConfigDefault = LocalBinlogConfigDefault()
            self.LocalBinlogConfigDefault._deserialize(params.get("LocalBinlogConfigDefault"))
        self.RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板 ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateInfoResponse(AbstractModel):
    """DescribeParamTemplateInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板 ID。
        :type TemplateId: int
        :param Name: 参数模板名称。
        :type Name: str
        :param EngineVersion: 参数模板对应实例版本
        :type EngineVersion: str
        :param TotalCount: 参数模板中的参数数量
        :type TotalCount: int
        :param Items: 参数详情
        :type Items: list of ParameterDetail
        :param Description: 参数模板描述
        :type Description: str
        :param TemplateType: 参数模板类型。支持值包括："HIGH_STABILITY" - 高稳定模版，"HIGH_PERFORMANCE" - 高性能模版。
        :type TemplateType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.Name = None
        self.EngineVersion = None
        self.TotalCount = None
        self.Items = None
        self.Description = None
        self.TemplateType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.EngineVersion = params.get("EngineVersion")
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Description = params.get("Description")
        self.TemplateType = params.get("TemplateType")
        self.RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param EngineVersions: 引擎版本，缺省则查询所有
        :type EngineVersions: list of str
        """
        self.EngineVersions = None


    def _deserialize(self, params):
        self.EngineVersions = params.get("EngineVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 该用户的参数模板数量。
        :type TotalCount: int
        :param Items: 参数模板详情。
        :type Items: list of ParamTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID。
        :type ProjectId: int
        """
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
        r"""
        :param Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param TotalCount: 安全组规则数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProxyConnectionPoolConfRequest(AbstractModel):
    """DescribeProxyConnectionPoolConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Offset: 分页查询偏移量
        :type Offset: int
        :param Limit: 分页查询限制
        :type Limit: int
        """
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
        


class DescribeProxyConnectionPoolConfResponse(AbstractModel):
    """DescribeProxyConnectionPoolConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 配置规格数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param PoolConf: 连接池配置规格
注意：此字段可能返回 null，表示取不到有效值。
        :type PoolConf: :class:`tencentcloud.cdb.v20170320.models.PoolConf`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.PoolConf = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("PoolConf") is not None:
            self.PoolConf = PoolConf()
            self.PoolConf._deserialize(params.get("PoolConf"))
        self.RequestId = params.get("RequestId")


class DescribeProxyCustomConfRequest(AbstractModel):
    """DescribeProxyCustomConf请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Offset: 分页
        :type Offset: int
        :param Limit: 限制
        :type Limit: int
        """
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
        


class DescribeProxyCustomConfResponse(AbstractModel):
    """DescribeProxyCustomConf返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 代理配置数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param CustomConf: 代理配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomConf: :class:`tencentcloud.cdb.v20170320.models.CustomConfig`
        :param WeightRule: 权重限制
注意：此字段可能返回 null，表示取不到有效值。
        :type WeightRule: :class:`tencentcloud.cdb.v20170320.models.Rule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.CustomConf = None
        self.WeightRule = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("CustomConf") is not None:
            self.CustomConf = CustomConfig()
            self.CustomConf._deserialize(params.get("CustomConf"))
        if params.get("WeightRule") is not None:
            self.WeightRule = Rule()
            self.WeightRule._deserialize(params.get("WeightRule"))
        self.RequestId = params.get("RequestId")


class DescribeRoGroupsRequest(AbstractModel):
    """DescribeRoGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoGroupsResponse(AbstractModel):
    """DescribeRoGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoGroups: RO组信息数组，一个实例可关联多个RO组。
        :type RoGroups: list of RoGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoGroups") is not None:
            self.RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self.RoGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoMinScaleRequest(AbstractModel):
    """DescribeRoMinScale请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoInstanceId: 只读实例ID，格式如：cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，该参数与MasterInstanceId参数不能同时为空。
        :type RoInstanceId: str
        :param MasterInstanceId: 主实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，该参数与RoInstanceId参数不能同时为空。注意，当传入参数包含RoInstanceId时，返回值为只读实例升级时的最小规格；当传入参数只包含MasterInstanceId时，返回值为只读实例购买时的最小规格。
        :type MasterInstanceId: str
        """
        self.RoInstanceId = None
        self.MasterInstanceId = None


    def _deserialize(self, params):
        self.RoInstanceId = params.get("RoInstanceId")
        self.MasterInstanceId = params.get("MasterInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoMinScaleResponse(AbstractModel):
    """DescribeRoMinScale返回参数结构体

    """

    def __init__(self):
        r"""
        :param Memory: 内存规格大小, 单位为：MB。
        :type Memory: int
        :param Volume: 磁盘规格大小, 单位为：GB。
        :type Volume: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Memory = None
        self.Volume = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.RequestId = params.get("RequestId")


class DescribeRollbackRangeTimeRequest(AbstractModel):
    """DescribeRollbackRangeTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表，单个实例 ID 的格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackRangeTimeResponse(AbstractModel):
    """DescribeRollbackRangeTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 返回的参数信息。
        :type Items: list of InstanceRollbackRangeTime
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeRollbackTaskDetailRequest(AbstractModel):
    """DescribeRollbackTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872)。
        :type InstanceId: str
        :param AsyncRequestId: 异步任务 ID。
        :type AsyncRequestId: str
        :param Limit: 分页参数，每次请求返回的记录数。默认值为 20，最大值为 100。
        :type Limit: int
        :param Offset: 分页偏移量。默认为 0。
        :type Offset: int
        """
        self.InstanceId = None
        self.AsyncRequestId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTaskDetailResponse(AbstractModel):
    """DescribeRollbackTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param Items: 回档任务详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of RollbackTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = RollbackTask()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogDataRequest(AbstractModel):
    """DescribeSlowLogData请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param StartTime: 开始时间戳。
        :type StartTime: int
        :param EndTime: 结束时间戳。
        :type EndTime: int
        :param UserHosts: 客户端 Host 列表。
        :type UserHosts: list of str
        :param UserNames: 客户端 用户名 列表。
        :type UserNames: list of str
        :param DataBases: 访问的 数据库 列表。
        :type DataBases: list of str
        :param SortBy: 排序字段。当前支持：Timestamp,QueryTime,LockTime,RowsExamined,RowsSent 。
        :type SortBy: str
        :param OrderBy: 升序还是降序排列。当前支持：ASC,DESC 。
        :type OrderBy: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 一次性返回的记录数量，默认为100，最大为400。
        :type Limit: int
        :param InstType: 仅在实例为主实例或者灾备实例时生效，可选值：slave，代表拉取从机的日志。
        :type InstType: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.UserHosts = None
        self.UserNames = None
        self.DataBases = None
        self.SortBy = None
        self.OrderBy = None
        self.Offset = None
        self.Limit = None
        self.InstType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserHosts = params.get("UserHosts")
        self.UserNames = params.get("UserNames")
        self.DataBases = params.get("DataBases")
        self.SortBy = params.get("SortBy")
        self.OrderBy = params.get("OrderBy")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstType = params.get("InstType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogDataResponse(AbstractModel):
    """DescribeSlowLogData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param Items: 查询到的记录。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SlowLogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = SlowLogItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Offset: 偏移量，默认值为0，最小值为0。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的慢查询日志总数。
        :type TotalCount: int
        :param Items: 符合查询条件的慢查询日志详情。
        :type Items: list of SlowLogInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeSupportedPrivilegesRequest(AbstractModel):
    """DescribeSupportedPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportedPrivilegesResponse(AbstractModel):
    """DescribeSupportedPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param GlobalSupportedPrivileges: 实例支持的全局权限。
        :type GlobalSupportedPrivileges: list of str
        :param DatabaseSupportedPrivileges: 实例支持的数据库权限。
        :type DatabaseSupportedPrivileges: list of str
        :param TableSupportedPrivileges: 实例支持的数据库表权限。
        :type TableSupportedPrivileges: list of str
        :param ColumnSupportedPrivileges: 实例支持的数据库列权限。
        :type ColumnSupportedPrivileges: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GlobalSupportedPrivileges = None
        self.DatabaseSupportedPrivileges = None
        self.TableSupportedPrivileges = None
        self.ColumnSupportedPrivileges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GlobalSupportedPrivileges = params.get("GlobalSupportedPrivileges")
        self.DatabaseSupportedPrivileges = params.get("DatabaseSupportedPrivileges")
        self.TableSupportedPrivileges = params.get("TableSupportedPrivileges")
        self.ColumnSupportedPrivileges = params.get("ColumnSupportedPrivileges")
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Database: 数据库的名称。
        :type Database: str
        :param Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最大值为2000。
        :type Limit: int
        :param TableRegexp: 匹配数据库表名的正则表达式，规则同 MySQL 官网
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的数据库表总数。
        :type TotalCount: int
        :param Items: 返回的数据库表信息。
        :type Items: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeTagsOfInstanceIdsRequest(AbstractModel):
    """DescribeTagsOfInstanceIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例列表。
        :type InstanceIds: list of str
        :param Offset: 分页偏移量。
        :type Offset: int
        :param Limit: 分页大小。
        :type Limit: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsOfInstanceIdsResponse(AbstractModel):
    """DescribeTagsOfInstanceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页偏移量。
        :type Offset: int
        :param Limit: 分页大小。
        :type Limit: int
        :param Rows: 实例标签信息。
        :type Rows: list of TagsInfoOfInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfInstance()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param AsyncRequestId: 异步任务请求 ID，执行云数据库相关操作返回的 AsyncRequestId。
        :type AsyncRequestId: str
        :param TaskTypes: 任务类型，不传值则查询所有任务类型，支持的值包括：
1 - 数据库回档；
2 - SQL操作；
3 - 数据导入；
5 - 参数设置；
6 - 初始化云数据库实例；
7 - 重启云数据库实例；
8 - 开启云数据库实例GTID；
9 - 只读实例升级；
10 - 数据库批量回档；
11 - 主实例升级；
12 - 删除云数据库库表；
13 - 灾备实例提升为主。
        :type TaskTypes: list of int
        :param TaskStatus: 任务状态，不传值则查询所有任务状态，支持的值包括：
-1 - 未定义；
0 - 初始化；
1 - 运行中；
2 - 执行成功；
3 - 执行失败；
4 - 已终止；
5 - 已删除；
6 - 已暂停。
        :type TaskStatus: list of int
        :param StartTimeBegin: 第一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01。
        :type StartTimeBegin: str
        :param StartTimeEnd: 最后一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01。
        :type StartTimeEnd: str
        :param Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最大值为100。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 返回的实例任务信息。
        :type Items: list of TaskDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = TaskDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimeWindowRequest(AbstractModel):
    """DescribeTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimeWindowResponse(AbstractModel):
    """DescribeTimeWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Monday: 星期一的可维护时间列表。
        :type Monday: list of str
        :param Tuesday: 星期二的可维护时间列表。
        :type Tuesday: list of str
        :param Wednesday: 星期三的可维护时间列表。
        :type Wednesday: list of str
        :param Thursday: 星期四的可维护时间列表。
        :type Thursday: list of str
        :param Friday: 星期五的可维护时间列表。
        :type Friday: list of str
        :param Saturday: 星期六的可维护时间列表。
        :type Saturday: list of str
        :param Sunday: 星期日的可维护时间列表。
        :type Sunday: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")
        self.RequestId = params.get("RequestId")


class DescribeUploadedFilesRequest(AbstractModel):
    """DescribeUploadedFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Path: 文件路径。该字段应填用户主账号的OwnerUin信息。
        :type Path: str
        :param Offset: 记录偏移量，默认值为0。
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20。
        :type Limit: int
        """
        self.Path = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadedFilesResponse(AbstractModel):
    """DescribeUploadedFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的SQL文件总数。
        :type TotalCount: int
        :param Items: 返回的SQL文件列表。
        :type Items: list of SqlFileInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = SqlFileInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceCpuInfo(AbstractModel):
    """CPU负载

    """

    def __init__(self):
        r"""
        :param Rate: 实例CPU平均使用率
        :type Rate: list of DeviceCpuRateInfo
        :param Load: 实例CPU监控数据
        :type Load: list of int
        """
        self.Rate = None
        self.Load = None


    def _deserialize(self, params):
        if params.get("Rate") is not None:
            self.Rate = []
            for item in params.get("Rate"):
                obj = DeviceCpuRateInfo()
                obj._deserialize(item)
                self.Rate.append(obj)
        self.Load = params.get("Load")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceCpuRateInfo(AbstractModel):
    """实例CPU平均使用率

    """

    def __init__(self):
        r"""
        :param CpuCore: Cpu核编号
        :type CpuCore: int
        :param Rate: Cpu使用率
        :type Rate: list of int
        """
        self.CpuCore = None
        self.Rate = None


    def _deserialize(self, params):
        self.CpuCore = params.get("CpuCore")
        self.Rate = params.get("Rate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDiskInfo(AbstractModel):
    """实例磁盘监控数据

    """

    def __init__(self):
        r"""
        :param IoRatioPerSec: 平均每秒有百分之几的时间用于IO操作
        :type IoRatioPerSec: list of int
        :param IoWaitTime: 平均每次设备I/O操作的等待时间*100，单位为毫秒。例如：该值为201，表示平均每次I/O操作等待时间为：201/100=2.1毫秒
        :type IoWaitTime: list of int
        :param Read: 磁盘平均每秒完成的读操作次数总和*100。例如：该值为2002，表示磁盘平均每秒完成读操作为：2002/100=20.2次
        :type Read: list of int
        :param Write: 磁盘平均每秒完成的写操作次数总和*100。例如：该值为30001，表示磁盘平均每秒完成写操作为：30001/100=300.01次
        :type Write: list of int
        :param CapacityRatio: 磁盘空间容量，每两个一组，第一个为已使用容量，第二个为磁盘总容量
        :type CapacityRatio: list of int
        """
        self.IoRatioPerSec = None
        self.IoWaitTime = None
        self.Read = None
        self.Write = None
        self.CapacityRatio = None


    def _deserialize(self, params):
        self.IoRatioPerSec = params.get("IoRatioPerSec")
        self.IoWaitTime = params.get("IoWaitTime")
        self.Read = params.get("Read")
        self.Write = params.get("Write")
        self.CapacityRatio = params.get("CapacityRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceMemInfo(AbstractModel):
    """实例所在物理机内存监控信息

    """

    def __init__(self):
        r"""
        :param Total: 总内存大小。free命令中Mem:一行total的值,单位：KB
        :type Total: list of int
        :param Used: 已使用内存。free命令中Mem:一行used的值,单位：KB
        :type Used: list of int
        """
        self.Total = None
        self.Used = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceNetInfo(AbstractModel):
    """实例所在物理机网络监控信息

    """

    def __init__(self):
        r"""
        :param Conn: tcp连接数
        :type Conn: list of int
        :param PackageIn: 网卡入包量，单位：个/秒
        :type PackageIn: list of int
        :param PackageOut: 网卡出包量，单位：个/秒
        :type PackageOut: list of int
        :param FlowIn: 入流量，单位：kbps
        :type FlowIn: list of int
        :param FlowOut: 出流量，单位：kbps
        :type FlowOut: list of int
        """
        self.Conn = None
        self.PackageIn = None
        self.PackageOut = None
        self.FlowIn = None
        self.FlowOut = None


    def _deserialize(self, params):
        self.Conn = params.get("Conn")
        self.PackageIn = params.get("PackageIn")
        self.PackageOut = params.get("PackageOut")
        self.FlowIn = params.get("FlowIn")
        self.FlowOut = params.get("FlowOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityGroupId: 安全组 ID。
        :type SecurityGroupId: str
        :param InstanceIds: 实例 ID 列表，一个或者多个实例 ID 组成的数组。
        :type InstanceIds: list of str
        :param ForReadonlyInstance: 当传入只读实例ID时，默认操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True
        :type ForReadonlyInstance: bool
        """
        self.SecurityGroupId = None
        self.InstanceIds = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DrInfo(AbstractModel):
    """灾备实例信息

    """

    def __init__(self):
        r"""
        :param Status: 灾备实例状态
        :type Status: int
        :param Zone: 可用区信息
        :type Zone: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Region: 地域信息
        :type Region: str
        :param SyncStatus: 实例同步状态。可能的返回值为：
0 - 灾备未同步；
1 - 灾备同步中；
2 - 灾备同步成功；
3 - 灾备同步失败；
4 - 灾备同步修复中。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrlogItem(AbstractModel):
    """结构化的错误日志详情

    """

    def __init__(self):
        r"""
        :param Timestamp: 错误发生时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param Content: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self.Timestamp = None
        self.Content = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportRecord(AbstractModel):
    """导入任务记录

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inbound(AbstractModel):
    """安全组入站规则

    """

    def __init__(self):
        r"""
        :param Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param CidrIp: 来源 IP 或 IP 段，例如192.168.0.0/16
        :type CidrIp: str
        :param PortRange: 端口
        :type PortRange: str
        :param IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        :param Dir: 规则限定的方向，进站规则为 INPUT
        :type Dir: str
        :param Desc: 规则描述
        :type Desc: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Dir = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Dir = params.get("Dir")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestIds: 异步任务的请求ID数组，可使用此ID查询异步任务的执行结果
        :type AsyncRequestIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstancesRequest(AbstractModel):
    """InquiryPriceUpgradeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param Memory: 升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的内存规格。
        :type Memory: int
        :param Volume: 升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的硬盘范围。
        :type Volume: int
        :param Cpu: 升级后的核心数目，单位：核，为保证传入 CPU 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的核心数目，当未指定该值时，将按照 Memory 大小补全一个默认值。
        :type Cpu: int
        :param ProtectMode: 数据复制方式，支持值包括：0 - 异步复制，1 - 半同步复制，2 - 强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type ProtectMode: int
        :param DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。 不指定则默认为通用型实例。
        :type DeviceType: str
        :param InstanceNodes: 实例节点数。对于 RO 和 基础版实例， 该值默认为1。 如果需要询价三节点实例， 请将该值设置为3。其余主实例该值默认为2。
        :type InstanceNodes: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.Cpu = None
        self.ProtectMode = None
        self.DeviceType = None
        self.InstanceNodes = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.Cpu = params.get("Cpu")
        self.ProtectMode = params.get("ProtectMode")
        self.DeviceType = params.get("DeviceType")
        self.InstanceNodes = params.get("InstanceNodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeInstancesResponse(AbstractModel):
    """InquiryPriceUpgradeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Price: 实例价格，单位：分（人民币）。
        :type Price: int
        :param OriginalPrice: 实例原价，单位：分（人民币）。
        :type OriginalPrice: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.OriginalPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.OriginalPrice = params.get("OriginalPrice")
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param WanStatus: 外网状态，可能的返回值为：0-未开通外网；1-已开通外网；2-已关闭外网
        :type WanStatus: int
        :param Zone: 可用区信息
        :type Zone: str
        :param InitFlag: 初始化标志，可能的返回值为：0-未初始化；1-已初始化
        :type InitFlag: int
        :param RoVipInfo: 只读vip信息。单独开通只读实例访问的只读实例才有该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type RoVipInfo: :class:`tencentcloud.cdb.v20170320.models.RoVipInfo`
        :param Memory: 内存容量，单位为 MB
        :type Memory: int
        :param Status: 实例状态，可能的返回值：0-创建中；1-运行中；4-隔离中；5-已隔离
        :type Status: int
        :param VpcId: 私有网络 ID，例如：51102
        :type VpcId: int
        :param SlaveInfo: 备机信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveInfo: :class:`tencentcloud.cdb.v20170320.models.SlaveInfo`
        :param InstanceId: 实例 ID
        :type InstanceId: str
        :param Volume: 硬盘容量，单位为 GB
        :type Volume: int
        :param AutoRenew: 自动续费标志，可能的返回值：0-未开通自动续费；1-已开通自动续费；2-已关闭自动续费
        :type AutoRenew: int
        :param ProtectMode: 数据复制方式。0 - 异步复制；1 - 半同步复制；2 - 强同步复制
        :type ProtectMode: int
        :param RoGroups: 只读组详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RoGroups: list of RoGroup
        :param SubnetId: 子网 ID，例如：2333
        :type SubnetId: int
        :param InstanceType: 实例类型，可能的返回值：1-主实例；2-灾备实例；3-只读实例
        :type InstanceType: int
        :param ProjectId: 项目 ID
        :type ProjectId: int
        :param Region: 地域信息
        :type Region: str
        :param DeadlineTime: 实例到期时间
        :type DeadlineTime: str
        :param DeployMode: 可用区部署方式。可能的值为：0 - 单可用区；1 - 多可用区
        :type DeployMode: int
        :param TaskStatus: 实例任务状态。0 - 没有任务 ,1 - 升级中,2 - 数据导入中,3 - 开放Slave中,4 - 外网访问开通中,5 - 批量操作执行中,6 - 回档中,7 - 外网访问关闭中,8 - 密码修改中,9 - 实例名修改中,10 - 重启中,12 - 自建迁移中,13 - 删除库表中,14 - 灾备实例创建同步中,15 - 升级待切换,16 - 升级切换中,17 - 升级切换完成
        :type TaskStatus: int
        :param MasterInfo: 主实例详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterInfo: :class:`tencentcloud.cdb.v20170320.models.MasterInfo`
        :param DeviceType: 实例类型
        :type DeviceType: str
        :param EngineVersion: 内核版本
        :type EngineVersion: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param DrInfo: 灾备实例详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DrInfo: list of DrInfo
        :param WanDomain: 外网域名
        :type WanDomain: str
        :param WanPort: 外网端口号
        :type WanPort: int
        :param PayType: 付费类型，可能的返回值：0-包年包月；1-按量计费
        :type PayType: int
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param Vip: 实例 IP
        :type Vip: str
        :param Vport: 端口号
        :type Vport: int
        :param CdbError: 是否锁定标记
        :type CdbError: int
        :param UniqVpcId: 私有网络描述符，例如：“vpc-5v8wn9mg”
        :type UniqVpcId: str
        :param UniqSubnetId: 子网描述符，例如：“subnet-1typ0s7d”
        :type UniqSubnetId: str
        :param PhysicalId: 物理 ID
        :type PhysicalId: str
        :param Cpu: 核心数
        :type Cpu: int
        :param Qps: 每秒查询数量
        :type Qps: int
        :param ZoneName: 可用区中文名称
        :type ZoneName: str
        :param DeviceClass: 物理机型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param DeployGroupId: 置放群组 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployGroupId: str
        :param ZoneId: 可用区 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param InstanceNodes: 节点数
        :type InstanceNodes: int
        :param TagList: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of TagInfoItem
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
        self.PhysicalId = None
        self.Cpu = None
        self.Qps = None
        self.ZoneName = None
        self.DeviceClass = None
        self.DeployGroupId = None
        self.ZoneId = None
        self.InstanceNodes = None
        self.TagList = None


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
        self.PhysicalId = params.get("PhysicalId")
        self.Cpu = params.get("Cpu")
        self.Qps = params.get("Qps")
        self.ZoneName = params.get("ZoneName")
        self.DeviceClass = params.get("DeviceClass")
        self.DeployGroupId = params.get("DeployGroupId")
        self.ZoneId = params.get("ZoneId")
        self.InstanceNodes = params.get("InstanceNodes")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfoItem()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRebootTime(AbstractModel):
    """实例预期重启时间

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRollbackRangeTime(AbstractModel):
    """实例可回档时间范围

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。(该返回字段目前已废弃，可以通过 DescribeDBInstances 接口查询实例的隔离状态)
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class LocalBinlogConfig(AbstractModel):
    """本地binlog保留配置

    """

    def __init__(self):
        r"""
        :param SaveHours: 本地binlog保留时长，可取值范围：[72,168]。
        :type SaveHours: int
        :param MaxUsage: 本地binlog空间使用率，可取值范围：[30,50]。
        :type MaxUsage: int
        """
        self.SaveHours = None
        self.MaxUsage = None


    def _deserialize(self, params):
        self.SaveHours = params.get("SaveHours")
        self.MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalBinlogConfigDefault(AbstractModel):
    """本地binlog保留策略默认配置。

    """

    def __init__(self):
        r"""
        :param SaveHours: 本地binlog保留时长，可取值范围：[72,168]。
        :type SaveHours: int
        :param MaxUsage: 本地binlog空间使用率，可取值范围：[30,50]。
        :type MaxUsage: int
        """
        self.SaveHours = None
        self.MaxUsage = None


    def _deserialize(self, params):
        self.SaveHours = params.get("SaveHours")
        self.MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MasterInfo(AbstractModel):
    """主实例信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountHostRequest(AbstractModel):
    """ModifyAccountHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param User: 账户的名称
        :type User: str
        :param Host: 账户的旧主机
        :type Host: str
        :param NewHost: 账户的新主机
        :type NewHost: str
        """
        self.InstanceId = None
        self.User = None
        self.Host = None
        self.NewHost = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.Host = params.get("Host")
        self.NewHost = params.get("NewHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountHostResponse(AbstractModel):
    """ModifyAccountHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountMaxUserConnectionsRequest(AbstractModel):
    """ModifyAccountMaxUserConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param Accounts: 云数据库账号。
        :type Accounts: list of Account
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param MaxUserConnections: 设置账户最大可用连接数，最大可设置值为10240。
        :type MaxUserConnections: int
        """
        self.Accounts = None
        self.InstanceId = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountMaxUserConnectionsResponse(AbstractModel):
    """ModifyAccountMaxUserConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param NewPassword: 数据库账号的新密码。密码应至少包含字母、数字和字符（_+-&=!@#$%^*()）中的两种，长度为8-64个字符。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPasswordResponse(AbstractModel):
    """ModifyAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Accounts: 数据库的账号，包括用户名和域名。
        :type Accounts: list of Account
        :param GlobalPrivileges: 全局权限。其中，GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER","CREATE USER","RELOAD","REPLICATION CLIENT","REPLICATION SLAVE","UPDATE"。
注意，不传该参数表示清除该权限。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 数据库的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示清除该权限。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: 数据库中表的权限。Privileges 权限的可选值为：权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示清除该权限。
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: 数据库表中列的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，不传该参数表示清除该权限。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param ModifyAction: 该参数不为空时，为批量修改权限。可选值为：grant，revoke。
        :type ModifyAction: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.ModifyAction = None


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
        self.ModifyAction = params.get("ModifyAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAuditConfigRequest(AbstractModel):
    """ModifyAuditConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param LogExpireDay: 审计日志保存时长。支持值包括：
7 - 一周
30 - 一个月；
180 - 六个月；
365 - 一年；
1095 - 三年；
1825 - 五年；
        :type LogExpireDay: int
        :param CloseAudit: 是否关闭审计服务。可选值：true - 关闭审计服务；false - 不关闭审计服务。默认值为 false。
当关闭审计服务时，会删除用户的审计日志和文件，并删除该实例的所有审计策略。
CloseAudit、LogExpireDay必须至少提供一个，如果两个都提供则按照CloseAudit优先的逻辑处理。
        :type CloseAudit: bool
        """
        self.InstanceId = None
        self.LogExpireDay = None
        self.CloseAudit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogExpireDay = params.get("LogExpireDay")
        self.CloseAudit = params.get("CloseAudit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditConfigResponse(AbstractModel):
    """ModifyAuditConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAuditRuleRequest(AbstractModel):
    """ModifyAuditRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 审计规则 ID。
        :type RuleId: str
        :param RuleName: 审计规则名称。
        :type RuleName: str
        :param Description: 审计规则描述。
        :type Description: str
        :param RuleFilters: 审计规则过滤条件。若设置了过滤条件，则不会开启全审计。
        :type RuleFilters: list of AuditFilter
        :param AuditAll: 是否开启全审计。支持值包括：false – 不开启全审计，true – 开启全审计。用户未设置审计规则过滤条件时，默认开启全审计。
        :type AuditAll: bool
        """
        self.RuleId = None
        self.RuleName = None
        self.Description = None
        self.RuleFilters = None
        self.AuditAll = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Description = params.get("Description")
        if params.get("RuleFilters") is not None:
            self.RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = AuditFilter()
                obj._deserialize(item)
                self.RuleFilters.append(obj)
        self.AuditAll = params.get("AuditAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditRuleResponse(AbstractModel):
    """ModifyAuditRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        :param AutoRenew: 自动续费标记，可取值的有：0 - 不自动续费，1 - 自动续费。
        :type AutoRenew: int
        """
        self.InstanceIds = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param ExpireDays: 备份文件的保留时间，单位为天。最小值为7天，最大值为732天。
        :type ExpireDays: int
        :param StartTime: (将废弃，建议使用 BackupTimeWindow 参数) 备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 00:00-12:00，02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。
        :type StartTime: str
        :param BackupMethod: 自动备份方式，仅支持：physical - 物理冷备
        :type BackupMethod: str
        :param BinlogExpireDays: binlog的保留时间，单位为天。最小值为7天，最大值为732天。该值的设置不能大于备份文件的保留时间。
        :type BinlogExpireDays: int
        :param BackupTimeWindow: 备份时间窗，比如要设置每周二和周日 10:00-14:00之间备份，该参数如下：{"Monday": "", "Tuesday": "10:00-14:00", "Wednesday": "", "Thursday": "", "Friday": "", "Saturday": "", "Sunday": "10:00-14:00"}    （注：可以设置一周的某几天备份，但是每天的备份时间需要设置为相同的时间段。 如果设置了该字段，将忽略StartTime字段的设置）
        :type BackupTimeWindow: :class:`tencentcloud.cdb.v20170320.models.CommonTimeWindow`
        """
        self.InstanceId = None
        self.ExpireDays = None
        self.StartTime = None
        self.BackupMethod = None
        self.BinlogExpireDays = None
        self.BackupTimeWindow = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ExpireDays = params.get("ExpireDays")
        self.StartTime = params.get("StartTime")
        self.BackupMethod = params.get("BackupMethod")
        self.BinlogExpireDays = params.get("BinlogExpireDays")
        if params.get("BackupTimeWindow") is not None:
            self.BackupTimeWindow = CommonTimeWindow()
            self.BackupTimeWindow._deserialize(params.get("BackupTimeWindow"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupDownloadRestrictionRequest(AbstractModel):
    """ModifyBackupDownloadRestriction请求参数结构体

    """

    def __init__(self):
        r"""
        :param LimitType: NoLimit 不限制,内外网都可以下载； LimitOnlyIntranet 仅内网可下载； Customize 用户自定义vpc:ip可下载。 只有该值为 Customize 时，才可以设置 LimitVpc 和 LimitIp 。
        :type LimitType: str
        :param VpcComparisonSymbol: 该参数仅支持 In， 表示 LimitVpc 指定的vpc可以下载。默认为In。
        :type VpcComparisonSymbol: str
        :param IpComparisonSymbol: In: 指定的ip可以下载； NotIn: 指定的ip不可以下载。 默认为In。
        :type IpComparisonSymbol: str
        :param LimitVpc: 限制下载的vpc设置。
        :type LimitVpc: list of BackupLimitVpcItem
        :param LimitIp: 限制下载的ip设置
        :type LimitIp: list of str
        """
        self.LimitType = None
        self.VpcComparisonSymbol = None
        self.IpComparisonSymbol = None
        self.LimitVpc = None
        self.LimitIp = None


    def _deserialize(self, params):
        self.LimitType = params.get("LimitType")
        self.VpcComparisonSymbol = params.get("VpcComparisonSymbol")
        self.IpComparisonSymbol = params.get("IpComparisonSymbol")
        if params.get("LimitVpc") is not None:
            self.LimitVpc = []
            for item in params.get("LimitVpc"):
                obj = BackupLimitVpcItem()
                obj._deserialize(item)
                self.LimitVpc.append(obj)
        self.LimitIp = params.get("LimitIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupDownloadRestrictionResponse(AbstractModel):
    """ModifyBackupDownloadRestriction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCDBProxyConnectionPoolRequest(AbstractModel):
    """ModifyCDBProxyConnectionPool请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyGroupId: 数据库代理ID
        :type ProxyGroupId: str
        :param OpenConnectionPool: 是否开启连接池，true：开启连接池；
                             false：关闭连接池。
        :type OpenConnectionPool: bool
        :param ConnectionPoolType: 连接池类型，
通过DescribeProxyConnectionPoolConf获取连接池类型值
        :type ConnectionPoolType: str
        :param PoolConnectionTimeOut: 连接保留阈值：单位（秒）
        :type PoolConnectionTimeOut: int
        """
        self.ProxyGroupId = None
        self.OpenConnectionPool = None
        self.ConnectionPoolType = None
        self.PoolConnectionTimeOut = None


    def _deserialize(self, params):
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.OpenConnectionPool = params.get("OpenConnectionPool")
        self.ConnectionPoolType = params.get("ConnectionPoolType")
        self.PoolConnectionTimeOut = params.get("PoolConnectionTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCDBProxyConnectionPoolResponse(AbstractModel):
    """ModifyCDBProxyConnectionPool返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步处理ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyCDBProxyDescRequest(AbstractModel):
    """ModifyCDBProxyDesc请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProxyGroupId: 数据库代理ID
        :type ProxyGroupId: str
        :param Desc: 数据库代理描述
        :type Desc: str
        """
        self.InstanceId = None
        self.ProxyGroupId = None
        self.Desc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCDBProxyDescResponse(AbstractModel):
    """ModifyCDBProxyDesc返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCDBProxyRequest(AbstractModel):
    """ModifyCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyGroupId: 数据库代理组唯一ID
        :type ProxyGroupId: str
        :param IsKickout: 是否开始延迟剔除，取值："true" | "false"
        :type IsKickout: bool
        :param MinCount: 最少保留数
        :type MinCount: int
        :param MaxDelay: 延迟剔除的阈值；如果IsKickOut="true", 该字段必填
        :type MaxDelay: int
        :param WeightMode: 读写权重分配模式；系统自动分配："system"， 自定义："custom"
        :type WeightMode: str
        :param RoWeightValues: 实例只读权重
        :type RoWeightValues: :class:`tencentcloud.cdb.v20170320.models.RoWeight`
        :param FailOver: 是否开启故障转移，代理出现故障后，连接地址将路由到主实例，取值："true" | "false"
        :type FailOver: bool
        :param AutoAddRo: 是否自动添加只读实例，取值："true" | "false"
        :type AutoAddRo: bool
        """
        self.ProxyGroupId = None
        self.IsKickout = None
        self.MinCount = None
        self.MaxDelay = None
        self.WeightMode = None
        self.RoWeightValues = None
        self.FailOver = None
        self.AutoAddRo = None


    def _deserialize(self, params):
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.IsKickout = params.get("IsKickout")
        self.MinCount = params.get("MinCount")
        self.MaxDelay = params.get("MaxDelay")
        self.WeightMode = params.get("WeightMode")
        if params.get("RoWeightValues") is not None:
            self.RoWeightValues = RoWeight()
            self.RoWeightValues._deserialize(params.get("RoWeightValues"))
        self.FailOver = params.get("FailOver")
        self.AutoAddRo = params.get("AutoAddRo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCDBProxyResponse(AbstractModel):
    """ModifyCDBProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCDBProxyVipVPortRequest(AbstractModel):
    """ModifyCDBProxyVipVPort请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        :param UniqVpcId: 私有网络ID
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络子网ID
        :type UniqSubnetId: str
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: int
        :param ReleaseDuration: 旧IP回收时间 单位小时
        :type ReleaseDuration: int
        """
        self.ProxyGroupId = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.DstIp = None
        self.DstPort = None
        self.ReleaseDuration = None


    def _deserialize(self, params):
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCDBProxyVipVPortResponse(AbstractModel):
    """ModifyCDBProxyVipVPort返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param InstanceName: 修改后的实例名称。
        :type InstanceName: str
        """
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
        r"""
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
        r"""
        :param InstanceIds: 实例 ID 数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        :param NewProjectId: 项目的 ID。
        :type NewProjectId: int
        """
        self.InstanceIds = None
        self.NewProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewProjectId = params.get("NewProjectId")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param SecurityGroupIds: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        :param ForReadonlyInstance: 当传入只读实例ID时，默认操作的是对应只读组的安全组。如果需要操作只读实例ID的安全组， 需要将该入参置为True
        :type ForReadonlyInstance: bool
        """
        self.InstanceId = None
        self.SecurityGroupIds = None
        self.ForReadonlyInstance = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.ForReadonlyInstance = params.get("ForReadonlyInstance")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceVipVportRequest(AbstractModel):
    """ModifyDBInstanceVipVport请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param DstIp: 目标 IP。该参数和 DstPort 参数，两者必传一个。
        :type DstIp: str
        :param DstPort: 目标端口，支持范围为：[1024-65535]。该参数和 DstIp 参数，两者必传一个。
        :type DstPort: int
        :param UniqVpcId: 私有网络统一 ID。
        :type UniqVpcId: str
        :param UniqSubnetId: 子网统一 ID。
        :type UniqSubnetId: str
        :param ReleaseDuration: 进行基础网络转 VPC 网络和 VPC 网络下的子网变更时，原网络中旧IP的回收时间，单位为小时，取值范围为0-168，默认值为24小时。
        :type ReleaseDuration: int
        """
        self.InstanceId = None
        self.DstIp = None
        self.DstPort = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ReleaseDuration = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ReleaseDuration = params.get("ReleaseDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceVipVportResponse(AbstractModel):
    """ModifyDBInstanceVipVport返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务ID。(该返回字段目前已废弃)
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceIds: 实例短 ID 列表。
        :type InstanceIds: list of str
        :param ParamList: 要修改的参数列表。每一个元素是 Name 和 CurrentValue 的组合。Name 是参数名，CurrentValue 是要修改成的值。
        :type ParamList: list of Parameter
        :param TemplateId: 模板id，ParamList和TemplateId必须至少传其中之一
        :type TemplateId: int
        :param WaitSwitch: 执行参数调整任务的方式，默认为 0。支持值包括：0 - 立刻执行，1 - 时间窗执行；当该值为 1 时，每次只能传一个实例（InstanceIds数量为1）
        :type WaitSwitch: int
        """
        self.InstanceIds = None
        self.ParamList = None
        self.TemplateId = None
        self.WaitSwitch = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.TemplateId = params.get("TemplateId")
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
        r"""
        :param AsyncRequestId: 异步任务 ID，可用于查询任务进度。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceTagRequest(AbstractModel):
    """ModifyInstanceTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param ReplaceTags: 要增加或修改的标签。
        :type ReplaceTags: list of TagInfo
        :param DeleteTags: 要删除的标签。
        :type DeleteTags: list of TagInfo
        """
        self.InstanceId = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceTagResponse(AbstractModel):
    """ModifyInstanceTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLocalBinlogConfigRequest(AbstractModel):
    """ModifyLocalBinlogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param SaveHours: 本地binlog保留时长，可取值范围：[72,168]。
        :type SaveHours: int
        :param MaxUsage: 本地binlog空间使用率，可取值范围：[30,50]。
        :type MaxUsage: int
        """
        self.InstanceId = None
        self.SaveHours = None
        self.MaxUsage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SaveHours = params.get("SaveHours")
        self.MaxUsage = params.get("MaxUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLocalBinlogConfigResponse(AbstractModel):
    """ModifyLocalBinlogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNameOrDescByDpIdRequest(AbstractModel):
    """ModifyNameOrDescByDpId请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployGroupId: 置放群组 ID。
        :type DeployGroupId: str
        :param DeployGroupName: 置放群组名称，最长不能超过60个字符。置放群组名和置放群组描述不能都为空。
        :type DeployGroupName: str
        :param Description: 置放群组描述，最长不能超过200个字符。置放群组名和置放群组描述不能都为空。
        :type Description: str
        """
        self.DeployGroupId = None
        self.DeployGroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.DeployGroupId = params.get("DeployGroupId")
        self.DeployGroupName = params.get("DeployGroupName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNameOrDescByDpIdResponse(AbstractModel):
    """ModifyNameOrDescByDpId返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param Name: 模板名称。
        :type Name: str
        :param Description: 模板描述。
        :type Description: str
        :param ParamList: 参数列表。
        :type ParamList: list of Parameter
        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.ParamList = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoGroupInfoRequest(AbstractModel):
    """ModifyRoGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoGroupId: RO 组的 ID。
        :type RoGroupId: str
        :param RoGroupInfo: RO 组的详细信息。
        :type RoGroupInfo: :class:`tencentcloud.cdb.v20170320.models.RoGroupAttr`
        :param RoWeightValues: RO 组内实例的权重。若修改 RO 组的权重模式为用户自定义模式（custom），则必须设置该参数，且需要设置每个 RO 实例的权重值。
        :type RoWeightValues: list of RoWeightValue
        :param IsBalanceRoLoad: 是否重新均衡 RO 组内的 RO 实例的负载。支持值包括：1 - 重新均衡负载；0 - 不重新均衡负载。默认值为 0。注意，设置为重新均衡负载时，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库。
        :type IsBalanceRoLoad: int
        :param ReplicationDelayTime: 废弃参数，无意义。
        :type ReplicationDelayTime: int
        """
        self.RoGroupId = None
        self.RoGroupInfo = None
        self.RoWeightValues = None
        self.IsBalanceRoLoad = None
        self.ReplicationDelayTime = None


    def _deserialize(self, params):
        self.RoGroupId = params.get("RoGroupId")
        if params.get("RoGroupInfo") is not None:
            self.RoGroupInfo = RoGroupAttr()
            self.RoGroupInfo._deserialize(params.get("RoGroupInfo"))
        if params.get("RoWeightValues") is not None:
            self.RoWeightValues = []
            for item in params.get("RoWeightValues"):
                obj = RoWeightValue()
                obj._deserialize(item)
                self.RoWeightValues.append(obj)
        self.IsBalanceRoLoad = params.get("IsBalanceRoLoad")
        self.ReplicationDelayTime = params.get("ReplicationDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoGroupInfoResponse(AbstractModel):
    """ModifyRoGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyTimeWindowRequest(AbstractModel):
    """ModifyTimeWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param TimeRanges: 修改后的可维护时间段，其中每一个时间段的格式形如：10:00-12:00；起止时间按半个小时对齐；最短半个小时，最长三个小时；最多设置两个时间段；起止时间范围为：[00:00, 24:00]。
        :type TimeRanges: list of str
        :param Weekdays: 指定修改哪一天的客户时间段，可能的取值为：monday，tuesday，wednesday，thursday，friday，saturday，sunday。如果不指定该值或者为空，则默认一周七天都修改。
        :type Weekdays: list of str
        """
        self.InstanceId = None
        self.TimeRanges = None
        self.Weekdays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeRanges = params.get("TimeRanges")
        self.Weekdays = params.get("Weekdays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTimeWindowResponse(AbstractModel):
    """ModifyTimeWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineIsolatedInstancesRequest(AbstractModel):
    """OfflineIsolatedInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedInstancesResponse(AbstractModel):
    """OfflineIsolatedInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OpenDBInstanceGTIDRequest(AbstractModel):
    """OpenDBInstanceGTID请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBInstanceGTIDResponse(AbstractModel):
    """OpenDBInstanceGTID返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWanServiceResponse(AbstractModel):
    """OpenWanService返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param CidrIp: 目的 IP 或 IP 段，例如172.16.0.0/12
        :type CidrIp: str
        :param PortRange: 端口或者端口范围
        :type PortRange: str
        :param IpProtocol: 网络协议，支持 UDP、TCP等
        :type IpProtocol: str
        :param Dir: 规则限定的方向，进站规则为 OUTPUT
        :type Dir: str
        :param Desc: 规则描述
        :type Desc: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Dir = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Dir = params.get("Dir")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamInfo(AbstractModel):
    """实例参数信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamRecord(AbstractModel):
    """参数修改记录

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ParamName: 参数名称
        :type ParamName: str
        :param OldValue: 参数修改前的值
        :type OldValue: str
        :param NewValue: 参数修改后的值
        :type NewValue: str
        :param IsSucess: 参数是否修改成功
        :type IsSucess: bool
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.InstanceId = None
        self.ParamName = None
        self.OldValue = None
        self.NewValue = None
        self.IsSucess = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ParamName = params.get("ParamName")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")
        self.IsSucess = params.get("IsSucess")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateInfo(AbstractModel):
    """参数模板信息

    """

    def __init__(self):
        r"""
        :param TemplateId: 参数模板ID
        :type TemplateId: int
        :param Name: 参数模板名称
        :type Name: str
        :param Description: 参数模板描述
        :type Description: str
        :param EngineVersion: 实例引擎版本
        :type EngineVersion: str
        :param TemplateType: 参数模板类型
        :type TemplateType: str
        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.EngineVersion = None
        self.TemplateType = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.EngineVersion = params.get("EngineVersion")
        self.TemplateType = params.get("TemplateType")
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
        r"""
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
        r"""
        :param Name: 参数名称
        :type Name: str
        :param ParamType: 参数类型：integer，enum，float，string，func
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
        :param MaxFunc: 参数是公式类型时，该字段有效，表示公式类型最大值
        :type MaxFunc: str
        :param MinFunc: 参数是公式类型时，该字段有效，表示公式类型最小值
        :type MinFunc: str
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
        self.MaxFunc = None
        self.MinFunc = None


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
        self.MaxFunc = params.get("MaxFunc")
        self.MinFunc = params.get("MinFunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoolConf(AbstractModel):
    """数据库代理连接池规格配置

    """

    def __init__(self):
        r"""
        :param ConnectionPoolType: 连接池类型：SessionConnectionPool（会话级别连接池
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolType: str
        :param MaxPoolConnectionTimeOut: 最大可保持连接阈值：单位（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPoolConnectionTimeOut: int
        :param MinPoolConnectionTimeOut: 最小可保持连接阈值：单位（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MinPoolConnectionTimeOut: int
        """
        self.ConnectionPoolType = None
        self.MaxPoolConnectionTimeOut = None
        self.MinPoolConnectionTimeOut = None


    def _deserialize(self, params):
        self.ConnectionPoolType = params.get("ConnectionPoolType")
        self.MaxPoolConnectionTimeOut = params.get("MaxPoolConnectionTimeOut")
        self.MinPoolConnectionTimeOut = params.get("MinPoolConnectionTimeOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroup(AbstractModel):
    """数据代理组信息

    """

    def __init__(self):
        r"""
        :param BaseGroup: 代理基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseGroup: :class:`tencentcloud.cdb.v20170320.models.BaseGroupInfo`
        :param Address: 代理地址信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: list of Address
        :param ConnectionPoolInfo: 代理连接池信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolInfo: :class:`tencentcloud.cdb.v20170320.models.ConnectionPoolInfo`
        :param ProxyNode: 代理节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNode: list of ProxyNodeInfo
        :param RWInstInfo: 代理路由信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInfo`
        """
        self.BaseGroup = None
        self.Address = None
        self.ConnectionPoolInfo = None
        self.ProxyNode = None
        self.RWInstInfo = None


    def _deserialize(self, params):
        if params.get("BaseGroup") is not None:
            self.BaseGroup = BaseGroupInfo()
            self.BaseGroup._deserialize(params.get("BaseGroup"))
        if params.get("Address") is not None:
            self.Address = []
            for item in params.get("Address"):
                obj = Address()
                obj._deserialize(item)
                self.Address.append(obj)
        if params.get("ConnectionPoolInfo") is not None:
            self.ConnectionPoolInfo = ConnectionPoolInfo()
            self.ConnectionPoolInfo._deserialize(params.get("ConnectionPoolInfo"))
        if params.get("ProxyNode") is not None:
            self.ProxyNode = []
            for item in params.get("ProxyNode"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self.ProxyNode.append(obj)
        if params.get("RWInstInfo") is not None:
            self.RWInstInfo = RWInfo()
            self.RWInstInfo._deserialize(params.get("RWInstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroups(AbstractModel):
    """数据代理组信息

    """

    def __init__(self):
        r"""
        :param BaseGroup: 代理基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseGroup: :class:`tencentcloud.cdb.v20170320.models.BaseGroupInfo`
        :param Address: 代理地址信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: list of Address
        :param ConnectionPoolInfo: 代理连接池信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionPoolInfo: :class:`tencentcloud.cdb.v20170320.models.ConnectionPoolInfo`
        :param ProxyNode: 代理节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNode: list of ProxyNodeInfo
        :param RWInstInfo: 代理路由信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInfos`
        """
        self.BaseGroup = None
        self.Address = None
        self.ConnectionPoolInfo = None
        self.ProxyNode = None
        self.RWInstInfo = None


    def _deserialize(self, params):
        if params.get("BaseGroup") is not None:
            self.BaseGroup = BaseGroupInfo()
            self.BaseGroup._deserialize(params.get("BaseGroup"))
        if params.get("Address") is not None:
            self.Address = []
            for item in params.get("Address"):
                obj = Address()
                obj._deserialize(item)
                self.Address.append(obj)
        if params.get("ConnectionPoolInfo") is not None:
            self.ConnectionPoolInfo = ConnectionPoolInfo()
            self.ConnectionPoolInfo._deserialize(params.get("ConnectionPoolInfo"))
        if params.get("ProxyNode") is not None:
            self.ProxyNode = []
            for item in params.get("ProxyNode"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self.ProxyNode.append(obj)
        if params.get("RWInstInfo") is not None:
            self.RWInstInfo = RWInfos()
            self.RWInstInfo._deserialize(params.get("RWInstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeInfo(AbstractModel):
    """代理节点信息

    """

    def __init__(self):
        r"""
        :param ProxyNodeId: 代理节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNodeId: str
        :param ProxyNodeConnections: 节点当前连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNodeConnections: int
        :param ProxyNodeCpu: cup
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNodeCpu: int
        :param ProxyNodeMem: 内存
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyNodeMem: int
        :param ProxyStatus: 节点状态：
init（申请中）
online（运行中）
offline（离线中）
destroy（已销毁）
recovering（故障恢复中）
error（节点故障）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyStatus: str
        """
        self.ProxyNodeId = None
        self.ProxyNodeConnections = None
        self.ProxyNodeCpu = None
        self.ProxyNodeMem = None
        self.ProxyStatus = None


    def _deserialize(self, params):
        self.ProxyNodeId = params.get("ProxyNodeId")
        self.ProxyNodeConnections = params.get("ProxyNodeConnections")
        self.ProxyNodeCpu = params.get("ProxyNodeCpu")
        self.ProxyNodeMem = params.get("ProxyNodeMem")
        self.ProxyStatus = params.get("ProxyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCDBProxyRequest(AbstractModel):
    """QueryCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProxyGroupId: 代理ID
        :type ProxyGroupId: str
        """
        self.InstanceId = None
        self.ProxyGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCDBProxyResponse(AbstractModel):
    """QueryCDBProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 代理数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param ProxyGroup: 代理信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyGroup: list of ProxyGroups
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.ProxyGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("ProxyGroup") is not None:
            self.ProxyGroup = []
            for item in params.get("ProxyGroup"):
                obj = ProxyGroups()
                obj._deserialize(item)
                self.ProxyGroup.append(obj)
        self.RequestId = params.get("RequestId")


class RWInfo(AbstractModel):
    """proxy读写分离信息

    """

    def __init__(self):
        r"""
        :param InstCount: 代理实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InstCount: int
        :param WeightMode: 权重分配模式；
系统自动分配："system"， 自定义："custom"
注意：此字段可能返回 null，表示取不到有效值。
        :type WeightMode: str
        :param IsKickOut: 是否开启延迟剔除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsKickOut: bool
        :param MinCount: 最小保留数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinCount: int
        :param MaxDelay: 延迟剔除阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDelay: int
        :param FailOver: 是否开启故障转移
注意：此字段可能返回 null，表示取不到有效值。
        :type FailOver: bool
        :param AutoAddRo: 是否自动添加RO
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoAddRo: bool
        :param RWInstInfo: 代理实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RWInstInfo: :class:`tencentcloud.cdb.v20170320.models.RWInstanceInfo`
        """
        self.InstCount = None
        self.WeightMode = None
        self.IsKickOut = None
        self.MinCount = None
        self.MaxDelay = None
        self.FailOver = None
        self.AutoAddRo = None
        self.RWInstInfo = None


    def _deserialize(self, params):
        self.InstCount = params.get("InstCount")
        self.WeightMode = params.get("WeightMode")
        self.IsKickOut = params.get("IsKickOut")
        self.MinCount = params.get("MinCount")
        self.MaxDelay = params.get("MaxDelay")
        self.FailOver = params.get("FailOver")
        self.AutoAddRo = params.get("AutoAddRo")
        if params.get("RWInstInfo") is not None:
            self.RWInstInfo = RWInstanceInfo()
            self.RWInstInfo._deserialize(params.get("RWInstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RWInfos(AbstractModel):
    """proxy读写分离信息

    """

    def __init__(self):
        r"""
        :param InstCount: 代理实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InstCount: int
        :param WeightMode: 权重分配模式；
系统自动分配："system"， 自定义："custom"
注意：此字段可能返回 null，表示取不到有效值。
        :type WeightMode: str
        :param IsKickOut: 是否开启延迟剔除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsKickOut: bool
        :param MinCount: 最小保留数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinCount: int
        :param MaxDelay: 延迟剔除阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDelay: int
        :param FailOver: 是否开启故障转移
注意：此字段可能返回 null，表示取不到有效值。
        :type FailOver: bool
        :param AutoAddRo: 是否自动添加RO
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoAddRo: bool
        :param RWInstInfo: 代理实例信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RWInstInfo: list of RWInstanceInfo
        """
        self.InstCount = None
        self.WeightMode = None
        self.IsKickOut = None
        self.MinCount = None
        self.MaxDelay = None
        self.FailOver = None
        self.AutoAddRo = None
        self.RWInstInfo = None


    def _deserialize(self, params):
        self.InstCount = params.get("InstCount")
        self.WeightMode = params.get("WeightMode")
        self.IsKickOut = params.get("IsKickOut")
        self.MinCount = params.get("MinCount")
        self.MaxDelay = params.get("MaxDelay")
        self.FailOver = params.get("FailOver")
        self.AutoAddRo = params.get("AutoAddRo")
        if params.get("RWInstInfo") is not None:
            self.RWInstInfo = []
            for item in params.get("RWInstInfo"):
                obj = RWInstanceInfo()
                obj._deserialize(item)
                self.RWInstInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RWInstanceInfo(AbstractModel):
    """代理实例信息

    """


class RegionSellConf(AbstractModel):
    """地域售卖配置

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIsolatedDBInstancesRequest(AbstractModel):
    """ReleaseIsolatedDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 数组，单个实例 ID 格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIsolatedDBInstancesResponse(AbstractModel):
    """ReleaseIsolatedDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 解隔离操作的结果集。
        :type Items: list of ReleaseResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ReleaseResult()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class ReleaseResult(AbstractModel):
    """解隔离任务结果

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Code: 实例解隔离操作的结果值。返回值为0表示成功。
        :type Code: int
        :param Message: 实例解隔离操作的错误信息。
        :type Message: str
        """
        self.InstanceId = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeRequest(AbstractModel):
    """ReloadBalanceProxyNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyGroupId: 代理组ID
        :type ProxyGroupId: str
        """
        self.ProxyGroupId = None


    def _deserialize(self, params):
        self.ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReloadBalanceProxyNodeResponse(AbstractModel):
    """ReloadBalanceProxyNode返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param InstanceId: 待续费的实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872)。
        :type InstanceId: str
        :param TimeSpan: 续费时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。
        :type TimeSpan: int
        :param ModifyPayType: 如果需要将按量计费实例续费为包年包月的实例，该入参的值需要指定为 "PREPAID" 。
        :type ModifyPayType: str
        """
        self.InstanceId = None
        self.TimeSpan = None
        self.ModifyPayType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeSpan = params.get("TimeSpan")
        self.ModifyPayType = params.get("ModifyPayType")
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
        r"""
        :param DealId: 订单 ID。
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesResponse(AbstractModel):
    """RestartDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param RoGroupMode: 只读组模式，可选值为：alone-系统自动分配只读组；allinone-新建只读组；join-使用现有只读组。
        :type RoGroupMode: str
        :param RoGroupId: 只读组 ID。
        :type RoGroupId: str
        :param RoGroupName: 只读组名称。
        :type RoGroupName: str
        :param RoOfflineDelay: 是否启用延迟超限剔除功能，启用该功能后，只读实例与主实例的延迟超过延迟阈值，只读实例将被隔离。可选值：1-启用；0-不启用。
        :type RoOfflineDelay: int
        :param RoMaxDelayTime: 延迟阈值。
        :type RoMaxDelayTime: int
        :param MinRoInGroup: 最少实例保留个数，若购买只读实例数量小于设置数量将不做剔除。
        :type MinRoInGroup: int
        :param WeightMode: 读写权重分配模式，可选值：system-系统自动分配；custom-自定义。
        :type WeightMode: str
        :param Weight: 权重值。
        :type Weight: int
        :param RoInstances: 只读组中的只读实例详情。
        :type RoInstances: list of RoInstanceInfo
        :param Vip: 只读组的内网 IP。
        :type Vip: str
        :param Vport: 只读组的内网端口号。
        :type Vport: int
        :param UniqVpcId: 私有网络 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param UniqSubnetId: 子网 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param RoGroupRegion: 只读组所在的地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoGroupRegion: str
        :param RoGroupZone: 只读组所在的可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoGroupZone: str
        :param DelayReplicationTime: 延迟复制时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayReplicationTime: int
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
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.RoGroupRegion = None
        self.RoGroupZone = None
        self.DelayReplicationTime = None


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
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.RoGroupRegion = params.get("RoGroupRegion")
        self.RoGroupZone = params.get("RoGroupZone")
        self.DelayReplicationTime = params.get("DelayReplicationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoGroupAttr(AbstractModel):
    """RO 组的配置信息

    """

    def __init__(self):
        r"""
        :param RoGroupName: RO 组名称。
        :type RoGroupName: str
        :param RoMaxDelayTime: RO 实例最大延迟阈值。单位为秒，最小值为 1。注意，RO 组必须设置了开启实例延迟剔除策略，该值才有效。
        :type RoMaxDelayTime: int
        :param RoOfflineDelay: 是否开启实例延迟剔除。支持的值包括：1 - 开启；0 - 不开启。注意，若设置开启实例延迟剔除，则必须设置延迟阈值（RoMaxDelayTime）参数。
        :type RoOfflineDelay: int
        :param MinRoInGroup: 最少保留实例数。可设置为小于或等于该 RO 组下 RO 实例个数的任意值。注意，若设置值大于 RO 实例数量将不做剔除；若设置为 0，所有实例延迟超限都会被剔除。
        :type MinRoInGroup: int
        :param WeightMode: 权重模式。支持值包括："system" - 系统自动分配； "custom" - 用户自定义设置。注意，若设置 "custom" 模式，则必须设置 RO 实例权重配置（RoWeightValues）参数。
        :type WeightMode: str
        :param ReplicationDelayTime: 延迟复制时间。
        :type ReplicationDelayTime: int
        """
        self.RoGroupName = None
        self.RoMaxDelayTime = None
        self.RoOfflineDelay = None
        self.MinRoInGroup = None
        self.WeightMode = None
        self.ReplicationDelayTime = None


    def _deserialize(self, params):
        self.RoGroupName = params.get("RoGroupName")
        self.RoMaxDelayTime = params.get("RoMaxDelayTime")
        self.RoOfflineDelay = params.get("RoOfflineDelay")
        self.MinRoInGroup = params.get("MinRoInGroup")
        self.WeightMode = params.get("WeightMode")
        self.ReplicationDelayTime = params.get("ReplicationDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoInstanceInfo(AbstractModel):
    """RO实例的详细信息

    """

    def __init__(self):
        r"""
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
        :param EngineVersion: RO实例数据库引擎版本，可能返回值：5.1、5.5、5.6、5.7、8.0
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoVipInfo(AbstractModel):
    """只读vip信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoWeight(AbstractModel):
    """实例权重

    """


class RoWeightValue(AbstractModel):
    """RO 实例的权重值

    """

    def __init__(self):
        r"""
        :param InstanceId: RO 实例 ID。
        :type InstanceId: str
        :param Weight: 权重值。取值范围为 [0, 100]。
        :type Weight: int
        """
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackDBName(AbstractModel):
    """用于回档的数据库名

    """

    def __init__(self):
        r"""
        :param DatabaseName: 回档前的原数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param NewDatabaseName: 回档后的新数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewDatabaseName: str
        """
        self.DatabaseName = None
        self.NewDatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.NewDatabaseName = params.get("NewDatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackInstancesInfo(AbstractModel):
    """用于回档的实例详情

    """

    def __init__(self):
        r"""
        :param InstanceId: 云数据库实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Strategy: 回档策略。可选值为：table、db、full；默认值为full。table - 极速回档模式，仅导入所选中表级别的备份和binlog，如有跨表操作，且关联表未被同时选中，将会导致回档失败，该模式下参数Databases必须为空；db - 快速模式，仅导入所选中库级别的备份和binlog，如有跨库操作，且关联库未被同时选中，将会导致回档失败；full - 普通回档模式，将导入整个实例的备份和binlog，速度较慢。
        :type Strategy: str
        :param RollbackTime: 数据库回档时间，时间格式为：yyyy-mm-dd hh:mm:ss
        :type RollbackTime: str
        :param Databases: 待回档的数据库信息，表示整库回档
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of RollbackDBName
        :param Tables: 待回档的数据库表信息，表示按表回档
注意：此字段可能返回 null，表示取不到有效值。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTableName(AbstractModel):
    """用于回档的数据库表名

    """

    def __init__(self):
        r"""
        :param TableName: 回档前的原数据库表名
注意：此字段可能返回 null，表示取不到有效值。
        :type TableName: str
        :param NewTableName: 回档后的新数据库表名
注意：此字段可能返回 null，表示取不到有效值。
        :type NewTableName: str
        """
        self.TableName = None
        self.NewTableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTables(AbstractModel):
    """用于回档的数据库表详情

    """

    def __init__(self):
        r"""
        :param Database: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param Table: 数据库表详情
注意：此字段可能返回 null，表示取不到有效值。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTask(AbstractModel):
    """回档任务详情

    """

    def __init__(self):
        r"""
        :param Info: 任务执行信息描述。
        :type Info: str
        :param Status: 任务执行结果。可能的取值：INITIAL - 初始化，RUNNING - 运行中，SUCCESS - 执行成功，FAILED - 执行失败，KILLED - 已终止，REMOVED - 已删除，PAUSED - 终止中。
        :type Status: str
        :param Progress: 任务执行进度。取值范围为[0, 100]。
        :type Progress: int
        :param StartTime: 任务开始时间。
        :type StartTime: str
        :param EndTime: 任务结束时间。
        :type EndTime: str
        :param Detail: 回档任务详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of RollbackInstancesInfo
        """
        self.Info = None
        self.Status = None
        self.Progress = None
        self.StartTime = None
        self.EndTime = None
        self.Detail = None


    def _deserialize(self, params):
        self.Info = params.get("Info")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self.Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTimeRange(AbstractModel):
    """可回档时间范围

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """权重分配规则

    """

    def __init__(self):
        r"""
        :param LessThan: 划分上限
注意：此字段可能返回 null，表示取不到有效值。
        :type LessThan: int
        :param Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        """
        self.LessThan = None
        self.Weight = None


    def _deserialize(self, params):
        self.LessThan = params.get("LessThan")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SellConfig(AbstractModel):
    """售卖配置详情

    """

    def __init__(self):
        r"""
        :param Device: 设备类型（废弃）
        :type Device: str
        :param Type: 售卖规格描述（废弃）
        :type Type: str
        :param CdbType: 实例类型（废弃）
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
        :param Status: 状态值，0 表示该规格对外售卖
        :type Status: int
        :param Tag: 标签值（废弃）
        :type Tag: int
        :param DeviceType: 实例类型，可能的取值范围有：UNIVERSAL (通用型), EXCLUSIVE (独享型), BASIC (基础型)
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceType: str
        :param DeviceTypeName: 实例类型描述，可能的取值范围有：通用型， 独享型， 基础型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceTypeName: str
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
        self.Tag = None
        self.DeviceType = None
        self.DeviceTypeName = None


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
        self.Tag = params.get("Tag")
        self.DeviceType = params.get("DeviceType")
        self.DeviceTypeName = params.get("DeviceTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SellType(AbstractModel):
    """售卖实例类型

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveConfig(AbstractModel):
    """从库的配置信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInfo(AbstractModel):
    """备机信息

    """

    def __init__(self):
        r"""
        :param First: 第一备机信息
        :type First: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        :param Second: 第二备机信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Second: :class:`tencentcloud.cdb.v20170320.models.SlaveInstanceInfo`
        """
        self.First = None
        self.Second = None


    def _deserialize(self, params):
        if params.get("First") is not None:
            self.First = SlaveInstanceInfo()
            self.First._deserialize(params.get("First"))
        if params.get("Second") is not None:
            self.Second = SlaveInstanceInfo()
            self.Second._deserialize(params.get("Second"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlaveInstanceInfo(AbstractModel):
    """备机信息

    """

    def __init__(self):
        r"""
        :param Vport: 端口号
        :type Vport: int
        :param Region: 地域信息
        :type Region: str
        :param Vip: 虚拟 IP 信息
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogInfo(AbstractModel):
    """慢查询日志详情

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogItem(AbstractModel):
    """结构化的慢日志详情

    """

    def __init__(self):
        r"""
        :param Timestamp: Sql的执行时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param QueryTime: Sql的执行时长（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryTime: float
        :param SqlText: Sql语句。
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlText: str
        :param UserHost: 客户端地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserHost: str
        :param UserName: 用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param Database: 数据库名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param LockTime: 锁时长（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type LockTime: float
        :param RowsExamined: 扫描行数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RowsExamined: int
        :param RowsSent: 结果集行数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RowsSent: int
        :param SqlTemplate: Sql模板。
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlTemplate: str
        :param Md5: Sql语句的md5。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        """
        self.Timestamp = None
        self.QueryTime = None
        self.SqlText = None
        self.UserHost = None
        self.UserName = None
        self.Database = None
        self.LockTime = None
        self.RowsExamined = None
        self.RowsSent = None
        self.SqlTemplate = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.QueryTime = params.get("QueryTime")
        self.SqlText = params.get("SqlText")
        self.UserHost = params.get("UserHost")
        self.UserName = params.get("UserName")
        self.Database = params.get("Database")
        self.LockTime = params.get("LockTime")
        self.RowsExamined = params.get("RowsExamined")
        self.RowsSent = params.get("RowsSent")
        self.SqlTemplate = params.get("SqlTemplate")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SqlFileInfo(AbstractModel):
    """sql文件信息

    """

    def __init__(self):
        r"""
        :param UploadTime: 上传时间
        :type UploadTime: str
        :param UploadInfo: 上传进度
        :type UploadInfo: :class:`tencentcloud.cdb.v20170320.models.UploadInfo`
        :param FileName: 文件名
        :type FileName: str
        :param FileSize: 文件大小，单位为Bytes
        :type FileSize: int
        :param IsUploadFinished: 上传是否完成标志，可选值：0 - 未完成，1 - 已完成
        :type IsUploadFinished: int
        :param FileId: 文件ID
        :type FileId: str
        """
        self.UploadTime = None
        self.UploadInfo = None
        self.FileName = None
        self.FileSize = None
        self.IsUploadFinished = None
        self.FileId = None


    def _deserialize(self, params):
        self.UploadTime = params.get("UploadTime")
        if params.get("UploadInfo") is not None:
            self.UploadInfo = UploadInfo()
            self.UploadInfo._deserialize(params.get("UploadInfo"))
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.IsUploadFinished = params.get("IsUploadFinished")
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackRequest(AbstractModel):
    """StartBatchRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 用于回档的实例详情信息。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartBatchRollbackResponse(AbstractModel):
    """StartBatchRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StartReplicationRequest(AbstractModel):
    """StartReplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。仅支持只读实例。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartReplicationResponse(AbstractModel):
    """StartReplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param AsyncRequestId: 异步任务的请求 ID。
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDBImportJobResponse(AbstractModel):
    """StopDBImportJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopReplicationRequest(AbstractModel):
    """StopReplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。仅支持只读实例。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopReplicationResponse(AbstractModel):
    """StopReplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StopRollbackRequest(AbstractModel):
    """StopRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 撤销回档任务对应的实例Id。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRollbackResponse(AbstractModel):
    """StopRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 执行请求的异步任务ID
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchCDBProxyRequest(AbstractModel):
    """SwitchCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProxyGroupId: 数据库代理ID
        :type ProxyGroupId: str
        """
        self.InstanceId = None
        self.ProxyGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchCDBProxyResponse(AbstractModel):
    """SwitchCDBProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchDBInstanceMasterSlaveRequest(AbstractModel):
    """SwitchDBInstanceMasterSlave请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param DstSlave: 目标从实例。可选值："first" - 第一备机；"second" - 第二备机。默认值为 "first"，仅多可用区实例支持设置为 "second"。
        :type DstSlave: str
        :param ForceSwitch: 是否强制切换。默认为 False。注意，若设置强制切换为 True，实例存在丢失数据的风险，请谨慎使用。
        :type ForceSwitch: bool
        :param WaitSwitch: 是否时间窗内切换。默认为 False，即不在时间窗内切换。注意，如果设置了 ForceSwitch 参数为 True，则该参数不生效。
        :type WaitSwitch: bool
        """
        self.InstanceId = None
        self.DstSlave = None
        self.ForceSwitch = None
        self.WaitSwitch = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DstSlave = params.get("DstSlave")
        self.ForceSwitch = params.get("ForceSwitch")
        self.WaitSwitch = params.get("WaitSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceMasterSlaveResponse(AbstractModel):
    """SwitchDBInstanceMasterSlave返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务 ID。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchDrInstanceToMasterRequest(AbstractModel):
    """SwitchDrInstanceToMaster请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 灾备实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDrInstanceToMasterResponse(AbstractModel):
    """SwitchDrInstanceToMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SwitchForUpgradeRequest(AbstractModel):
    """SwitchForUpgrade请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchForUpgradeResponse(AbstractModel):
    """SwitchForUpgrade返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TableName(AbstractModel):
    """表名

    """

    def __init__(self):
        r"""
        :param TableName: 表名
        :type TableName: str
        """
        self.TableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TablePrivilege(AbstractModel):
    """数据库表权限

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: list of str
        """
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
        


class TagInfoItem(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
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
        


class TagInfoUnit(AbstractModel):
    """tag信息单元

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
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
        


class TagsInfoOfInstance(AbstractModel):
    """实例的标签信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Tags: 标签信息
        :type Tags: list of TagInfoUnit
        """
        self.InstanceId = None
        self.Tags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetail(AbstractModel):
    """实例任务详情

    """

    def __init__(self):
        r"""
        :param Code: 错误码。
        :type Code: int
        :param Message: 错误信息。
        :type Message: str
        :param JobId: 实例任务 ID。
        :type JobId: int
        :param Progress: 实例任务进度。
        :type Progress: int
        :param TaskStatus: 实例任务状态，可能的值包括：
"UNDEFINED" - 未定义；
"INITIAL" - 初始化；
"RUNNING" - 运行中；
"SUCCEED" - 执行成功；
"FAILED" - 执行失败；
"KILLED" - 已终止；
"REMOVED" - 已删除；
"PAUSED" - 已暂停。
"WAITING" - 等待中（可撤销）
        :type TaskStatus: str
        :param TaskType: 实例任务类型，可能的值包括：
"ROLLBACK" - 数据库回档；
"SQL OPERATION" - SQL操作；
"IMPORT DATA" - 数据导入；
"MODIFY PARAM" - 参数设置；
"INITIAL" - 初始化云数据库实例；
"REBOOT" - 重启云数据库实例；
"OPEN GTID" - 开启云数据库实例GTID；
"UPGRADE RO" - 只读实例升级；
"BATCH ROLLBACK" - 数据库批量回档；
"UPGRADE MASTER" - 主实例升级；
"DROP TABLES" - 删除云数据库库表；
"SWITCH DR TO MASTER" - 灾备实例提升为主。
        :type TaskType: str
        :param StartTime: 实例任务开始时间。
        :type StartTime: str
        :param EndTime: 实例任务结束时间。
        :type EndTime: str
        :param InstanceIds: 任务关联的实例 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param AsyncRequestId: 异步任务的请求 ID。
        :type AsyncRequestId: str
        """
        self.Code = None
        self.Message = None
        self.JobId = None
        self.Progress = None
        self.TaskStatus = None
        self.TaskType = None
        self.StartTime = None
        self.EndTime = None
        self.InstanceIds = None
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskType = params.get("TaskType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceIds = params.get("InstanceIds")
        self.AsyncRequestId = params.get("AsyncRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeCDBProxyRequest(AbstractModel):
    """UpgradeCDBProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProxyGroupId: 数据库代理ID
        :type ProxyGroupId: str
        :param ProxyCount: 代理节点个数
        :type ProxyCount: int
        :param Cpu: 代理节点核数
        :type Cpu: int
        :param Mem: 代理节点内存大小
        :type Mem: int
        :param ReloadBalance: 重新负载均衡：auto（自动），manual（手动）
        :type ReloadBalance: str
        :param UpgradeTime: 升级时间 nowTime（升级完成时）timeWindow（实例维护时间）
        :type UpgradeTime: str
        """
        self.InstanceId = None
        self.ProxyGroupId = None
        self.ProxyCount = None
        self.Cpu = None
        self.Mem = None
        self.ReloadBalance = None
        self.UpgradeTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.ProxyCount = params.get("ProxyCount")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.ReloadBalance = params.get("ReloadBalance")
        self.UpgradeTime = params.get("UpgradeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeCDBProxyResponse(AbstractModel):
    """UpgradeCDBProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步处理ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeCDBProxyVersionRequest(AbstractModel):
    """UpgradeCDBProxyVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ProxyGroupId: 数据库代理ID
        :type ProxyGroupId: str
        :param SrcProxyVersion: 数据库代理当前版本
        :type SrcProxyVersion: str
        :param DstProxyVersion: 数据库代理升级版本
        :type DstProxyVersion: str
        :param UpgradeTime: 升级时间 ：nowTime（升级完成时）timeWindow（实例维护时间）
        :type UpgradeTime: str
        """
        self.InstanceId = None
        self.ProxyGroupId = None
        self.SrcProxyVersion = None
        self.DstProxyVersion = None
        self.UpgradeTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ProxyGroupId = params.get("ProxyGroupId")
        self.SrcProxyVersion = params.get("SrcProxyVersion")
        self.DstProxyVersion = params.get("DstProxyVersion")
        self.UpgradeTime = params.get("UpgradeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeCDBProxyVersionResponse(AbstractModel):
    """UpgradeCDBProxyVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步处理ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param EngineVersion: 主实例数据库引擎版本，支持值包括：5.6 和 5.7。
        :type EngineVersion: str
        :param WaitSwitch: 切换访问新实例的方式，默认为 0。支持值包括：0 - 立刻切换，1 - 时间窗切换；当该值为 1 时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口 [切换访问新实例](https://cloud.tencent.com/document/product/236/15864) 触发该流程。
        :type WaitSwitch: int
        :param UpgradeSubversion: 是否是内核子版本升级，支持的值：1 - 升级内核子版本；0 - 升级数据库引擎版本。
        :type UpgradeSubversion: int
        :param MaxDelayTime: 延迟阈值。取值范围1~10
        :type MaxDelayTime: int
        """
        self.InstanceId = None
        self.EngineVersion = None
        self.WaitSwitch = None
        self.UpgradeSubversion = None
        self.MaxDelayTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")
        self.UpgradeSubversion = params.get("UpgradeSubversion")
        self.MaxDelayTime = params.get("MaxDelayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDBInstanceEngineVersionResponse(AbstractModel):
    """UpgradeDBInstanceEngineVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务 ID，可使用 [查询异步任务的执行结果](https://cloud.tencent.com/document/api/236/20410) 获取其执行情况。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceId: str
        :param Memory: 升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的内存规格。
        :type Memory: int
        :param Volume: 升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的硬盘范围。
        :type Volume: int
        :param ProtectMode: 数据复制方式，支持值包括：0 - 异步复制，1 - 半同步复制，2 - 强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type ProtectMode: int
        :param DeployMode: 部署模式，默认为 0，支持值包括：0 - 单可用区部署，1 - 多可用区部署，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type DeployMode: int
        :param SlaveZone: 备库1的可用区信息，默认和实例的 Zone 参数一致，升级主实例为多可用区部署时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。可通过 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口查询支持的可用区。
        :type SlaveZone: str
        :param EngineVersion: 主实例数据库引擎版本，支持值包括：5.5、5.6 和 5.7。
        :type EngineVersion: str
        :param WaitSwitch: 切换访问新实例的方式，默认为 0。支持值包括：0 - 立刻切换，1 - 时间窗切换；当该值为 1 时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口 [切换访问新实例](https://cloud.tencent.com/document/product/236/15864) 触发该流程。
        :type WaitSwitch: int
        :param BackupZone: 备库 2 的可用区信息，默认为空，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。
        :type BackupZone: str
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。
        :type InstanceRole: str
        :param DeviceType: 实例隔离类型。支持值包括： "UNIVERSAL" - 通用型实例， "EXCLUSIVE" - 独享型实例， "BASIC" - 基础版实例。
        :type DeviceType: str
        :param Cpu: 升级后的实例cpu核数， 如果不传将根据 Memory 指定的内存值自动填充对应的cpu值。
        :type Cpu: int
        :param FastUpgrade: 是否极速变配。0-普通升级，1-极速变配。选择极速变配会根据资源状况校验是否可以进行极速变配，满足条件则进行极速变配，不满足条件会返回报错信息。
        :type FastUpgrade: int
        :param MaxDelayTime: 延迟阈值。取值范围1~10，默认值为10。
        :type MaxDelayTime: int
        :param CrossCluster: 是否跨区迁移。0-普通迁移，1-跨区迁移，默认值为0。该值为1时支持变更实例主节点可用区。
        :type CrossCluster: int
        :param ZoneId: 主节点可用区，该值仅在跨区迁移时生效。仅支持同地域下的可用区进行迁移。
        :type ZoneId: str
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
        self.DeviceType = None
        self.Cpu = None
        self.FastUpgrade = None
        self.MaxDelayTime = None
        self.CrossCluster = None
        self.ZoneId = None


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
        self.DeviceType = params.get("DeviceType")
        self.Cpu = params.get("Cpu")
        self.FastUpgrade = params.get("FastUpgrade")
        self.MaxDelayTime = params.get("MaxDelayTime")
        self.CrossCluster = params.get("CrossCluster")
        self.ZoneId = params.get("ZoneId")
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
        r"""
        :param DealIds: 订单 ID。
        :type DealIds: list of str
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UploadInfo(AbstractModel):
    """文件上传描述

    """

    def __init__(self):
        r"""
        :param AllSliceNum: 文件所有分片数
        :type AllSliceNum: int
        :param CompleteNum: 已完成分片数
        :type CompleteNum: int
        """
        self.AllSliceNum = None
        self.CompleteNum = None


    def _deserialize(self, params):
        self.AllSliceNum = params.get("AllSliceNum")
        self.CompleteNum = params.get("CompleteNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyRootAccountRequest(AbstractModel):
    """VerifyRootAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Password: 实例 ROOT 账号的密码。
        :type Password: str
        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyRootAccountResponse(AbstractModel):
    """VerifyRootAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSellConf(AbstractModel):
    """可用区售卖配置

    """

    def __init__(self):
        r"""
        :param Status: 可用区状态。可能的返回值为：1-上线；3-停售；4-不展示
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
        :param DrZone: 可支持的灾备可用区信息
        :type DrZone: list of str
        :param IsSupportRemoteRo: 是否支持跨可用区只读
        :type IsSupportRemoteRo: bool
        :param RemoteRoZone: 可支持的跨可用区只读区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoteRoZone: list of str
        :param ExClusterStatus: 独享型可用区状态。可能的返回值为：1-上线；3-停售；4-不展示
        :type ExClusterStatus: int
        :param ExClusterRemoteRoZone: 独享型可支持的跨可用区只读区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExClusterRemoteRoZone: list of str
        :param ExClusterZoneConf: 独享型多可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExClusterZoneConf: :class:`tencentcloud.cdb.v20170320.models.ZoneConf`
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
        self.DrZone = None
        self.IsSupportRemoteRo = None
        self.RemoteRoZone = None
        self.ExClusterStatus = None
        self.ExClusterRemoteRoZone = None
        self.ExClusterZoneConf = None


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
        self.DrZone = params.get("DrZone")
        self.IsSupportRemoteRo = params.get("IsSupportRemoteRo")
        self.RemoteRoZone = params.get("RemoteRoZone")
        self.ExClusterStatus = params.get("ExClusterStatus")
        self.ExClusterRemoteRoZone = params.get("ExClusterRemoteRoZone")
        if params.get("ExClusterZoneConf") is not None:
            self.ExClusterZoneConf = ZoneConf()
            self.ExClusterZoneConf._deserialize(params.get("ExClusterZoneConf"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        