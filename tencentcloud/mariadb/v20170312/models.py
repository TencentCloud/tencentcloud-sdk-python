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
        """
        :param User: 账户的名称\n        :type User: str\n        :param Host: 账户的域名\n        :type Host: str\n        """
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
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称，本接口取值：mariadb。\n        :type Product: str\n        :param SecurityGroupId: 要绑定的安全组ID，类似sg-efil73jd。\n        :type SecurityGroupId: str\n        :param InstanceIds: 被绑定的实例ID，类似tdsql-lesecurk，支持指定多个实例。\n        :type InstanceIds: list of str\n        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
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


class CancelDcnJobRequest(AbstractModel):
    """CancelDcnJob请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 灾备实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobResponse(AbstractModel):
    """CancelDcnJob返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloneAccountRequest(AbstractModel):
    """CloneAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param SrcUser: 源用户账户名\n        :type SrcUser: str\n        :param SrcHost: 源用户HOST\n        :type SrcHost: str\n        :param DstUser: 目的用户账户名\n        :type DstUser: str\n        :param DstHost: 目的用户HOST\n        :type DstHost: str\n        :param DstDesc: 目的用户账户描述\n        :type DstDesc: str\n        """
        self.InstanceId = None
        self.SrcUser = None
        self.SrcHost = None
        self.DstUser = None
        self.DstHost = None
        self.DstDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUser = params.get("SrcUser")
        self.SrcHost = params.get("SrcHost")
        self.DstUser = params.get("DstUser")
        self.DstHost = params.get("DstHost")
        self.DstDesc = params.get("DstDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneAccountResponse(AbstractModel):
    """CloneAccount返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务流程ID。\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待关闭外网访问的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param Ipv6Flag: 是否IPv6，默认0\n        :type Ipv6Flag: int\n        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务ID，可通过 DescribeFlow 查询任务状态。\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """列权限信息

    """

    def __init__(self):
        """
        :param Database: 数据库名\n        :type Database: str\n        :param Table: 数据库表名\n        :type Table: str\n        :param Column: 数据库列名\n        :type Column: str\n        :param Privileges: 权限信息\n        :type Privileges: list of str\n        """
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
        


class ConstraintRange(AbstractModel):
    """约束类型值的范围

    """

    def __init__(self):
        """
        :param Min: 约束类型为section时的最小值\n        :type Min: str\n        :param Max: 约束类型为section时的最大值\n        :type Max: str\n        """
        self.Min = None
        self.Max = None


    def _deserialize(self, params):
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param SrcUserName: 源用户名\n        :type SrcUserName: str\n        :param SrcHost: 源用户允许的访问 host\n        :type SrcHost: str\n        :param DstUserName: 目的用户名\n        :type DstUserName: str\n        :param DstHost: 目的用户允许的访问 host\n        :type DstHost: str\n        :param SrcReadOnly: 源账号的 ReadOnly 属性\n        :type SrcReadOnly: str\n        :param DstReadOnly: 目的账号的 ReadOnly 属性\n        :type DstReadOnly: str\n        """
        self.InstanceId = None
        self.SrcUserName = None
        self.SrcHost = None
        self.DstUserName = None
        self.DstHost = None
        self.SrcReadOnly = None
        self.DstReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUserName = params.get("SrcUserName")
        self.SrcHost = params.get("SrcHost")
        self.DstUserName = params.get("DstUserName")
        self.DstHost = params.get("DstHost")
        self.SrcReadOnly = params.get("SrcReadOnly")
        self.DstReadOnly = params.get("DstReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param UserName: 登录用户名，由字母、数字、下划线和连字符组成，长度为1~32位。\n        :type UserName: str\n        :param Host: 可以登录的主机，与mysql 账号的 host 格式一致，可以支持通配符，例如 %，10.%，10.20.%。\n        :type Host: str\n        :param Password: 账号密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。\n        :type Password: str\n        :param ReadOnly: 是否创建为只读账号，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败。\n        :type ReadOnly: int\n        :param Description: 账号备注，可以包含中文、英文字符、常见符号和数字，长度为0~256字符\n        :type Description: str\n        :param DelayThresh: 根据传入时间判断备机不可用\n        :type DelayThresh: int\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None
        self.ReadOnly = None
        self.Description = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        self.ReadOnly = params.get("ReadOnly")
        self.Description = params.get("Description")
        self.DelayThresh = params.get("DelayThresh")
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
        :param InstanceId: 实例ID，透传入参。\n        :type InstanceId: str\n        :param UserName: 用户名，透传入参。\n        :type UserName: str\n        :param Host: 允许访问的 host，透传入参。\n        :type Host: str\n        :param ReadOnly: 透传入参。\n        :type ReadOnly: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.ReadOnly = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.ReadOnly = params.get("ReadOnly")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zones: 实例节点可用区分布，最多可填两个可用区。当分片规格为一主两从时，其中两个节点在第一个可用区。\n        :type Zones: list of str\n        :param NodeCount: 节点个数大小，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。\n        :type NodeCount: int\n        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。\n        :type Memory: int\n        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。\n        :type Storage: int\n        :param Period: 欲购买的时长，单位：月。\n        :type Period: int\n        :param Count: 欲购买的数量，默认查询购买1个实例的价格。\n        :type Count: int\n        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。\n        :type AutoVoucher: bool\n        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。\n        :type VoucherIds: list of str\n        :param VpcId: 虚拟私有网络 ID，不传表示创建为基础网络\n        :type VpcId: str\n        :param SubnetId: 虚拟私有网络子网 ID，VpcId 不为空时必填\n        :type SubnetId: str\n        :param ProjectId: 项目 ID，可以通过查看项目列表获取，不传则关联到默认项目\n        :type ProjectId: int\n        :param DbVersionId: 数据库引擎版本，当前可选：8.0.18，10.1.9，5.7.17。如果不传的话，默认为 Percona 5.7.17。\n        :type DbVersionId: str\n        :param InstanceName: 实例名称， 可以通过该字段自主的设置实例的名字\n        :type InstanceName: str\n        :param SecurityGroupIds: 安全组ID列表\n        :type SecurityGroupIds: list of str\n        :param AutoRenewFlag: 自动续费标志，1:自动续费，2:不自动续费\n        :type AutoRenewFlag: int\n        :param Ipv6Flag: 是否支持IPv6\n        :type Ipv6Flag: int\n        :param ResourceTags: 标签键值对数组\n        :type ResourceTags: list of ResourceTag\n        :param InitParams: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。\n        :type InitParams: list of DBParamValue\n        :param DcnRegion: DCN源地域\n        :type DcnRegion: str\n        :param DcnInstanceId: DCN源实例ID\n        :type DcnInstanceId: str\n        """
        self.Zones = None
        self.NodeCount = None
        self.Memory = None
        self.Storage = None
        self.Period = None
        self.Count = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.DbVersionId = None
        self.InstanceName = None
        self.SecurityGroupIds = None
        self.AutoRenewFlag = None
        self.Ipv6Flag = None
        self.ResourceTags = None
        self.InitParams = None
        self.DcnRegion = None
        self.DcnInstanceId = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Period = params.get("Period")
        self.Count = params.get("Count")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.DbVersionId = params.get("DbVersionId")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        if params.get("InitParams") is not None:
            self.InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.InitParams.append(obj)
        self.DcnRegion = params.get("DcnRegion")
        self.DcnInstanceId = params.get("DcnInstanceId")
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
        """
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。\n        :type DealName: str\n        :param InstanceIds: 订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealName = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateTmpInstancesRequest(AbstractModel):
    """CreateTmpInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 回档实例的ID列表，形如：tdsql-ow728lmc。\n        :type InstanceIds: list of str\n        :param RollbackTime: 回档时间点\n        :type RollbackTime: str\n        """
        self.InstanceIds = None
        self.RollbackTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.RollbackTime = params.get("RollbackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTmpInstancesResponse(AbstractModel):
    """CreateTmpInstances返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务流程ID。\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """云数据库账号信息

    """

    def __init__(self):
        """
        :param UserName: 用户名\n        :type UserName: str\n        :param Host: 用户可以从哪台主机登录（对应 MySQL 用户的 host 字段，UserName + Host 唯一标识一个用户，IP形式，IP段以%结尾；支持填入%；为空默认等于%）\n        :type Host: str\n        :param Description: 用户备注信息\n        :type Description: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 最后更新时间\n        :type UpdateTime: str\n        :param ReadOnly: 只读标记，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败。\n        :type ReadOnly: int\n        :param DelayThresh: 该字段对只读帐号有意义，表示选择主备延迟小于该值的备机
注意：此字段可能返回 null，表示取不到有效值。\n        :type DelayThresh: int\n        """
        self.UserName = None
        self.Host = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ReadOnly = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ReadOnly = params.get("ReadOnly")
        self.DelayThresh = params.get("DelayThresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBBackupTimeConfig(AbstractModel):
    """云数据库实例备份时间配置信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID\n        :type InstanceId: str\n        :param StartBackupTime: 每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00\n        :type StartBackupTime: str\n        :param EndBackupTime: 每天备份执行的区间的结束时间，格式 mm:ss，形如 23:00\n        :type EndBackupTime: str\n        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """描述云数据库实例的详细信息。

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，唯一标识一个 TDSQL 实例\n        :type InstanceId: str\n        :param InstanceName: 实例名称，用户可修改\n        :type InstanceName: str\n        :param AppId: 实例所属应用 ID\n        :type AppId: int\n        :param ProjectId: 实例所属项目 ID\n        :type ProjectId: int\n        :param Region: 实例所在地域名称，如 ap-shanghai\n        :type Region: str\n        :param Zone: 实例所在可用区名称，如 ap-shanghai-1\n        :type Zone: str\n        :param VpcId: 私有网络 ID，基础网络时为 0\n        :type VpcId: int\n        :param SubnetId: 子网 ID，基础网络时为 0\n        :type SubnetId: int\n        :param Status: 实例状态：0 创建中，1 流程处理中， 2 运行中，3 实例未初始化，-1 实例已隔离，4 实例初始化中，5 实例删除中，6 实例重启中，7 数据迁移中\n        :type Status: int\n        :param Vip: 内网 IP 地址\n        :type Vip: str\n        :param Vport: 内网端口\n        :type Vport: int\n        :param WanDomain: 外网访问的域名，公网可解析\n        :type WanDomain: str\n        :param WanVip: 外网 IP 地址，公网可访问\n        :type WanVip: str\n        :param WanPort: 外网端口\n        :type WanPort: int\n        :param CreateTime: 实例创建时间，格式为 2006-01-02 15:04:05\n        :type CreateTime: str\n        :param UpdateTime: 实例最后更新时间，格式为 2006-01-02 15:04:05\n        :type UpdateTime: str\n        :param AutoRenewFlag: 自动续费标志：0 否，1 是\n        :type AutoRenewFlag: int\n        :param PeriodEndTime: 实例到期时间，格式为 2006-01-02 15:04:05\n        :type PeriodEndTime: str\n        :param Uin: 实例所属账号\n        :type Uin: str\n        :param TdsqlVersion: TDSQL 版本信息\n        :type TdsqlVersion: str\n        :param Memory: 实例内存大小，单位 GB\n        :type Memory: int\n        :param Storage: 实例存储大小，单位 GB\n        :type Storage: int\n        :param UniqueVpcId: 字符串型的私有网络ID\n        :type UniqueVpcId: str\n        :param UniqueSubnetId: 字符串型的私有网络子网ID\n        :type UniqueSubnetId: str\n        :param OriginSerialId: 原始实例ID（过时字段，请勿依赖该值）\n        :type OriginSerialId: str\n        :param NodeCount: 节点数，2为一主一从，3为一主二从\n        :type NodeCount: int\n        :param IsTmp: 是否临时实例，0为否，非0为是\n        :type IsTmp: int\n        :param ExclusterId: 独享集群ID，为空表示为普通实例\n        :type ExclusterId: str\n        :param Id: 数字实例ID（过时字段，请勿依赖该值）\n        :type Id: int\n        :param Pid: 产品类型 ID\n        :type Pid: int\n        :param Qps: 最大 Qps 值\n        :type Qps: int\n        :param Paymode: 付费模式
注意：此字段可能返回 null，表示取不到有效值。\n        :type Paymode: str\n        :param Locker: 实例处于异步任务时的异步任务流程ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Locker: int\n        :param StatusDesc: 实例目前运行状态描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusDesc: str\n        :param WanStatus: 外网状态，0-未开通；1-已开通；2-关闭；3-开通中\n        :type WanStatus: int\n        :param IsAuditSupported: 该实例是否支持审计。1-支持；0-不支持\n        :type IsAuditSupported: int\n        :param Machine: 机器型号\n        :type Machine: str\n        :param IsEncryptSupported: 是否支持数据加密。1-支持；0-不支持\n        :type IsEncryptSupported: int\n        :param Cpu: 实例CPU核数\n        :type Cpu: int\n        :param Ipv6Flag: 实例IPv6标志
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6Flag: int\n        :param Vipv6: 内网IPv6
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vipv6: str\n        :param WanVipv6: 外网IPv6
注意：此字段可能返回 null，表示取不到有效值。\n        :type WanVipv6: str\n        :param WanPortIpv6: 外网IPv6端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type WanPortIpv6: int\n        :param WanStatusIpv6: 外网IPv6状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type WanStatusIpv6: int\n        :param DbEngine: 数据库引擎
注意：此字段可能返回 null，表示取不到有效值。\n        :type DbEngine: str\n        :param DbVersion: 数据库版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type DbVersion: str\n        :param DcnFlag: DCN标志，0-无，1-主实例，2-灾备实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type DcnFlag: int\n        :param DcnStatus: DCN状态，0-无，1-创建中，2-同步中，3-已断开
注意：此字段可能返回 null，表示取不到有效值。\n        :type DcnStatus: int\n        :param DcnDstNum: DCN灾备实例数
注意：此字段可能返回 null，表示取不到有效值。\n        :type DcnDstNum: int\n        :param InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: int\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanVip = None
        self.WanPort = None
        self.CreateTime = None
        self.UpdateTime = None
        self.AutoRenewFlag = None
        self.PeriodEndTime = None
        self.Uin = None
        self.TdsqlVersion = None
        self.Memory = None
        self.Storage = None
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.OriginSerialId = None
        self.NodeCount = None
        self.IsTmp = None
        self.ExclusterId = None
        self.Id = None
        self.Pid = None
        self.Qps = None
        self.Paymode = None
        self.Locker = None
        self.StatusDesc = None
        self.WanStatus = None
        self.IsAuditSupported = None
        self.Machine = None
        self.IsEncryptSupported = None
        self.Cpu = None
        self.Ipv6Flag = None
        self.Vipv6 = None
        self.WanVipv6 = None
        self.WanPortIpv6 = None
        self.WanStatusIpv6 = None
        self.DbEngine = None
        self.DbVersion = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.DcnDstNum = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanVip = params.get("WanVip")
        self.WanPort = params.get("WanPort")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Uin = params.get("Uin")
        self.TdsqlVersion = params.get("TdsqlVersion")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.OriginSerialId = params.get("OriginSerialId")
        self.NodeCount = params.get("NodeCount")
        self.IsTmp = params.get("IsTmp")
        self.ExclusterId = params.get("ExclusterId")
        self.Id = params.get("Id")
        self.Pid = params.get("Pid")
        self.Qps = params.get("Qps")
        self.Paymode = params.get("Paymode")
        self.Locker = params.get("Locker")
        self.StatusDesc = params.get("StatusDesc")
        self.WanStatus = params.get("WanStatus")
        self.IsAuditSupported = params.get("IsAuditSupported")
        self.Machine = params.get("Machine")
        self.IsEncryptSupported = params.get("IsEncryptSupported")
        self.Cpu = params.get("Cpu")
        self.Ipv6Flag = params.get("Ipv6Flag")
        self.Vipv6 = params.get("Vipv6")
        self.WanVipv6 = params.get("WanVipv6")
        self.WanPortIpv6 = params.get("WanPortIpv6")
        self.WanStatusIpv6 = params.get("WanStatusIpv6")
        self.DbEngine = params.get("DbEngine")
        self.DbVersion = params.get("DbVersion")
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.DcnDstNum = params.get("DcnDstNum")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBParamValue(AbstractModel):
    """云数据库参数信息。

    """

    def __init__(self):
        """
        :param Param: 参数名称\n        :type Param: str\n        :param Value: 参数值\n        :type Value: str\n        """
        self.Param = None
        self.Value = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        """
        :param DbName: 数据库名称\n        :type DbName: str\n        """
        self.DbName = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
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
        """
        :param Privileges: 权限信息\n        :type Privileges: list of str\n        :param Database: 数据库名\n        :type Database: str\n        """
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
        


class DcnDetailItem(AbstractModel):
    """DCN详情条目

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param Region: 实例地域\n        :type Region: str\n        :param Zone: 实例可用区\n        :type Zone: str\n        :param Vip: 实例IP地址\n        :type Vip: str\n        :param Vipv6: 实例IPv6地址\n        :type Vipv6: str\n        :param Vport: 实例端口\n        :type Vport: int\n        :param Status: 实例状态\n        :type Status: int\n        :param StatusDesc: 实例状态描述\n        :type StatusDesc: str\n        :param DcnFlag: 实例DCN标志，1-主，2-备\n        :type DcnFlag: int\n        :param DcnStatus: 实例DCN状态，0-无，1-创建中，2-同步中，3-已断开\n        :type DcnStatus: int\n        :param Cpu: 实例CPU核数\n        :type Cpu: int\n        :param Memory: 实例内存大小，单位 GB\n        :type Memory: int\n        :param Storage: 实例存储大小，单位 GB\n        :type Storage: int\n        :param PayMode: 付费模式\n        :type PayMode: int\n        :param CreateTime: 实例创建时间，格式为 2006-01-02 15:04:05\n        :type CreateTime: str\n        :param PeriodEndTime: 实例到期时间，格式为 2006-01-02 15:04:05\n        :type PeriodEndTime: str\n        :param InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）\n        :type InstanceType: int\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.Vip = None
        self.Vipv6 = None
        self.Vport = None
        self.Status = None
        self.StatusDesc = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.PayMode = None
        self.CreateTime = None
        self.PeriodEndTime = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Vip = params.get("Vip")
        self.Vipv6 = params.get("Vipv6")
        self.Vport = params.get("Vport")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Deal(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param DealName: 订单号\n        :type DealName: str\n        :param OwnerUin: 所属账号\n        :type OwnerUin: str\n        :param Count: 商品数量\n        :type Count: int\n        :param FlowId: 关联的流程 Id，可用于查询流程执行状态\n        :type FlowId: int\n        :param InstanceIds: 只有创建实例的订单会填充该字段，表示该订单创建的实例的 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceIds: list of str\n        :param PayMode: 付费模式，0后付费/1预付费\n        :type PayMode: int\n        """
        self.DealName = None
        self.OwnerUin = None
        self.Count = None
        self.FlowId = None
        self.InstanceIds = None
        self.PayMode = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Count = params.get("Count")
        self.FlowId = params.get("FlowId")
        self.InstanceIds = params.get("InstanceIds")
        self.PayMode = params.get("PayMode")
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
        :param InstanceId: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param UserName: 用户名\n        :type UserName: str\n        :param Host: 用户允许的访问 host\n        :type Host: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param UserName: 登录用户名。\n        :type UserName: str\n        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。\n        :type Host: str\n        :param DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数\n        :type DbName: str\n        :param Type: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示查询该数据库权限（即db.\*），此时忽略 Object 参数\n        :type Type: str\n        :param Object: 具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空\n        :type Object: str\n        :param ColName: 当 Type=table 时，ColName 为 \* 表示查询表的权限，如果为具体字段名，表示查询对应字段的权限\n        :type ColName: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")
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
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Privileges: 权限列表。\n        :type Privileges: list of str\n        :param UserName: 数据库账号用户名\n        :type UserName: str\n        :param Host: 数据库账号Host\n        :type Host: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.Privileges = None
        self.UserName = None
        self.Host = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Privileges = params.get("Privileges")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        :param InstanceId: 实例ID，透传入参。\n        :type InstanceId: str\n        :param Users: 实例用户列表。\n        :type Users: list of DBAccount\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = DBAccount()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupTimeRequest(AbstractModel):
    """DescribeBackupTime请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupTimeResponse(AbstractModel):
    """DescribeBackupTime返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的配置数量\n        :type TotalCount: int\n        :param Items: 实例备份时间配置信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Items: list of DBBackupTimeConfig\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = DBBackupTimeConfig()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceSpecsRequest(AbstractModel):
    """DescribeDBInstanceSpecs请求参数结构体

    """


class DescribeDBInstanceSpecsResponse(AbstractModel):
    """DescribeDBInstanceSpecs返回参数结构体

    """

    def __init__(self):
        """
        :param Specs: 按机型分类的可售卖规格列表\n        :type Specs: list of InstanceSpec\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Specs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Specs") is not None:
            self.Specs = []
            for item in params.get("Specs"):
                obj = InstanceSpec()
                obj._deserialize(item)
                self.Specs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 按照一个或者多个实例 ID 查询。实例 ID 形如：tdsql-ow728lmc。每次请求的实例的上限为100。\n        :type InstanceIds: list of str\n        :param SearchName: 搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。\n        :type SearchName: str\n        :param SearchKey: 搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\n'）分割。\n        :type SearchKey: str\n        :param ProjectIds: 按项目 ID 查询\n        :type ProjectIds: list of int\n        :param IsFilterVpc: 是否根据 VPC 网络来搜索\n        :type IsFilterVpc: bool\n        :param VpcId: 私有网络 ID， IsFilterVpc 为 1 时有效\n        :type VpcId: str\n        :param SubnetId: 私有网络的子网 ID， IsFilterVpc 为 1 时有效\n        :type SubnetId: str\n        :param OrderBy: 排序字段， projectId， createtime， instancename 三者之一\n        :type OrderBy: str\n        :param OrderByType: 排序类型， desc 或者 asc\n        :type OrderByType: str\n        :param Offset: 偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param OriginSerialIds: 按 OriginSerialId 查询\n        :type OriginSerialIds: list of str\n        :param IsFilterExcluster: 标识是否使用ExclusterType字段, false不使用，true使用\n        :type IsFilterExcluster: bool\n        :param ExclusterType: 实例所属独享集群类型。取值范围：1-非独享集群，2-独享集群， 0-全部\n        :type ExclusterType: int\n        :param ExclusterIds: 按独享集群ID过滤实例，独享集群ID形如dbdc-4ih6uct9\n        :type ExclusterIds: list of str\n        :param TagKeys: 按标签key查询\n        :type TagKeys: list of str\n        :param FilterInstanceType: 实例类型过滤，1-独享实例，2-主实例，3-灾备实例，多个按逗号分隔\n        :type FilterInstanceType: str\n        :param Status: 按照实例状态进行筛选\n        :type Status: list of int\n        :param ExcludeStatus: 排除实例状态\n        :type ExcludeStatus: list of int\n        """
        self.InstanceIds = None
        self.SearchName = None
        self.SearchKey = None
        self.ProjectIds = None
        self.IsFilterVpc = None
        self.VpcId = None
        self.SubnetId = None
        self.OrderBy = None
        self.OrderByType = None
        self.Offset = None
        self.Limit = None
        self.OriginSerialIds = None
        self.IsFilterExcluster = None
        self.ExclusterType = None
        self.ExclusterIds = None
        self.TagKeys = None
        self.FilterInstanceType = None
        self.Status = None
        self.ExcludeStatus = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SearchName = params.get("SearchName")
        self.SearchKey = params.get("SearchKey")
        self.ProjectIds = params.get("ProjectIds")
        self.IsFilterVpc = params.get("IsFilterVpc")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OriginSerialIds = params.get("OriginSerialIds")
        self.IsFilterExcluster = params.get("IsFilterExcluster")
        self.ExclusterType = params.get("ExclusterType")
        self.ExclusterIds = params.get("ExclusterIds")
        self.TagKeys = params.get("TagKeys")
        self.FilterInstanceType = params.get("FilterInstanceType")
        self.Status = params.get("Status")
        self.ExcludeStatus = params.get("ExcludeStatus")
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
        :param TotalCount: 符合条件的实例数量\n        :type TotalCount: int\n        :param Instances: 实例详细信息列表\n        :type Instances: list of DBInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DBInstance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Type: 请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。\n        :type Type: int\n        """
        self.InstanceId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Type: 请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。\n        :type Type: int\n        :param Total: 请求日志总数\n        :type Total: int\n        :param Files: 包含uri、length、mtime（修改时间）等信息\n        :type Files: list of LogFileInfo\n        :param VpcPrefix: 如果是VPC网络的实例，做用本前缀加上URI为下载地址\n        :type VpcPrefix: str\n        :param NormalPrefix: 如果是普通网络的实例，做用本前缀加上URI为下载地址\n        :type NormalPrefix: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.Type = None
        self.Total = None
        self.Files = None
        self.VpcPrefix = None
        self.NormalPrefix = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.Total = params.get("Total")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = LogFileInfo()
                obj._deserialize(item)
                self.Files.append(obj)
        self.VpcPrefix = params.get("VpcPrefix")
        self.NormalPrefix = params.get("NormalPrefix")
        self.RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Params: 请求DB的当前参数值\n        :type Params: list of ParamDesc\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.Params = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self.Params.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBPerformanceDetailsRequest(AbstractModel):
    """DescribeDBPerformanceDetails请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param StartTime: 开始日期，格式yyyy-mm-dd\n        :type StartTime: str\n        :param EndTime: 结束日期，格式yyyy-mm-dd\n        :type EndTime: str\n        :param MetricName: 拉取的指标名，支持的值为：long_query,select_total,update_total,insert_total,delete_total,mem_hit_rate,disk_iops,conn_active,is_master_switched,slave_delay\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPerformanceDetailsResponse(AbstractModel):
    """DescribeDBPerformanceDetails返回参数结构体

    """

    def __init__(self):
        """
        :param Master: 主节点性能监控数据\n        :type Master: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`\n        :param Slave1: 备机1性能监控数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`\n        :param Slave2: 备机2性能监控数据，如果实例是一主一从，则没有该字段
注意：此字段可能返回 null，表示取不到有效值。\n        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Master = None
        self.Slave1 = None
        self.Slave2 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Master") is not None:
            self.Master = PerformanceMonitorSet()
            self.Master._deserialize(params.get("Master"))
        if params.get("Slave1") is not None:
            self.Slave1 = PerformanceMonitorSet()
            self.Slave1._deserialize(params.get("Slave1"))
        if params.get("Slave2") is not None:
            self.Slave2 = PerformanceMonitorSet()
            self.Slave2._deserialize(params.get("Slave2"))
        self.RequestId = params.get("RequestId")


class DescribeDBPerformanceRequest(AbstractModel):
    """DescribeDBPerformance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param StartTime: 开始日期，格式yyyy-mm-dd\n        :type StartTime: str\n        :param EndTime: 结束日期，格式yyyy-mm-dd\n        :type EndTime: str\n        :param MetricName: 拉取的指标名，支持的值为：long_query,select_total,update_total,insert_total,delete_total,mem_hit_rate,disk_iops,conn_active,is_master_switched,slave_delay\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBPerformanceResponse(AbstractModel):
    """DescribeDBPerformance返回参数结构体

    """

    def __init__(self):
        """
        :param LongQuery: 慢查询数\n        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SelectTotal: 查询操作数SELECT\n        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param UpdateTotal: 更新操作数UPDATE\n        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param InsertTotal: 插入操作数INSERT\n        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DeleteTotal: 删除操作数DELETE\n        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemHitRate: 缓存命中率\n        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DiskIops: 磁盘每秒IO次数\n        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param ConnActive: 活跃连接数\n        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param IsMasterSwitched: 是否发生主备切换，1为发生，0否\n        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SlaveDelay: 主备延迟\n        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LongQuery = None
        self.SelectTotal = None
        self.UpdateTotal = None
        self.InsertTotal = None
        self.DeleteTotal = None
        self.MemHitRate = None
        self.DiskIops = None
        self.ConnActive = None
        self.IsMasterSwitched = None
        self.SlaveDelay = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LongQuery") is not None:
            self.LongQuery = MonitorData()
            self.LongQuery._deserialize(params.get("LongQuery"))
        if params.get("SelectTotal") is not None:
            self.SelectTotal = MonitorData()
            self.SelectTotal._deserialize(params.get("SelectTotal"))
        if params.get("UpdateTotal") is not None:
            self.UpdateTotal = MonitorData()
            self.UpdateTotal._deserialize(params.get("UpdateTotal"))
        if params.get("InsertTotal") is not None:
            self.InsertTotal = MonitorData()
            self.InsertTotal._deserialize(params.get("InsertTotal"))
        if params.get("DeleteTotal") is not None:
            self.DeleteTotal = MonitorData()
            self.DeleteTotal._deserialize(params.get("DeleteTotal"))
        if params.get("MemHitRate") is not None:
            self.MemHitRate = MonitorData()
            self.MemHitRate._deserialize(params.get("MemHitRate"))
        if params.get("DiskIops") is not None:
            self.DiskIops = MonitorData()
            self.DiskIops._deserialize(params.get("DiskIops"))
        if params.get("ConnActive") is not None:
            self.ConnActive = MonitorData()
            self.ConnActive._deserialize(params.get("ConnActive"))
        if params.get("IsMasterSwitched") is not None:
            self.IsMasterSwitched = MonitorData()
            self.IsMasterSwitched._deserialize(params.get("IsMasterSwitched"))
        if params.get("SlaveDelay") is not None:
            self.SlaveDelay = MonitorData()
            self.SlaveDelay._deserialize(params.get("SlaveDelay"))
        self.RequestId = params.get("RequestId")


class DescribeDBResourceUsageDetailsRequest(AbstractModel):
    """DescribeDBResourceUsageDetails请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param StartTime: 开始日期，格式yyyy-mm-dd\n        :type StartTime: str\n        :param EndTime: 结束日期，格式yyyy-mm-dd\n        :type EndTime: str\n        :param MetricName: 拉取的指标名称，支持的值为：data_disk_available,binlog_disk_available,mem_available,cpu_usage_rate\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBResourceUsageDetailsResponse(AbstractModel):
    """DescribeDBResourceUsageDetails返回参数结构体

    """

    def __init__(self):
        """
        :param Master: 主节点资源使用情况监控数据\n        :type Master: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`\n        :param Slave1: 备机1资源使用情况监控数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`\n        :param Slave2: 备机2资源使用情况监控数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Master = None
        self.Slave1 = None
        self.Slave2 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Master") is not None:
            self.Master = ResourceUsageMonitorSet()
            self.Master._deserialize(params.get("Master"))
        if params.get("Slave1") is not None:
            self.Slave1 = ResourceUsageMonitorSet()
            self.Slave1._deserialize(params.get("Slave1"))
        if params.get("Slave2") is not None:
            self.Slave2 = ResourceUsageMonitorSet()
            self.Slave2._deserialize(params.get("Slave2"))
        self.RequestId = params.get("RequestId")


class DescribeDBResourceUsageRequest(AbstractModel):
    """DescribeDBResourceUsage请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param StartTime: 开始日期，格式yyyy-mm-dd\n        :type StartTime: str\n        :param EndTime: 结束日期，格式yyyy-mm-dd\n        :type EndTime: str\n        :param MetricName: 拉取的指标名称，支持的值为：data_disk_available,binlog_disk_available,mem_available,cpu_usage_rate\n        :type MetricName: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBResourceUsageResponse(AbstractModel):
    """DescribeDBResourceUsage返回参数结构体

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: binlog日志磁盘可用空间,单位GB\n        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DataDiskAvailable: 磁盘可用空间,单位GB\n        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param CpuUsageRate: CPU利用率\n        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemAvailable: 内存可用空间,单位GB\n        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BinlogDiskAvailable = None
        self.DataDiskAvailable = None
        self.CpuUsageRate = None
        self.MemAvailable = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BinlogDiskAvailable") is not None:
            self.BinlogDiskAvailable = MonitorData()
            self.BinlogDiskAvailable._deserialize(params.get("BinlogDiskAvailable"))
        if params.get("DataDiskAvailable") is not None:
            self.DataDiskAvailable = MonitorData()
            self.DataDiskAvailable._deserialize(params.get("DataDiskAvailable"))
        if params.get("CpuUsageRate") is not None:
            self.CpuUsageRate = MonitorData()
            self.CpuUsageRate._deserialize(params.get("CpuUsageRate"))
        if params.get("MemAvailable") is not None:
            self.MemAvailable = MonitorData()
            self.MemAvailable._deserialize(params.get("MemAvailable"))
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称，本接口取值：mariadb。\n        :type Product: str\n        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        """
        self.Product = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
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
        :param Groups: 安全组详情。\n        :type Groups: list of SecurityGroup\n        :param VIP: 实例VIP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VIP: str\n        :param VPort: 实例端口。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VPort: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Groups = None
        self.VIP = None
        self.VPort = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.VIP = params.get("VIP")
        self.VPort = params.get("VPort")
        self.RequestId = params.get("RequestId")


class DescribeDBSlowLogsRequest(AbstractModel):
    """DescribeDBSlowLogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Offset: 从结果的第几条数据开始返回\n        :type Offset: int\n        :param Limit: 返回的结果条数\n        :type Limit: int\n        :param StartTime: 查询的起始时间，形如2016-07-23 14:55:20\n        :type StartTime: str\n        :param EndTime: 查询的结束时间，形如2016-08-22 14:55:20\n        :type EndTime: str\n        :param Db: 要查询的具体数据库名称\n        :type Db: str\n        :param OrderBy: 排序指标，取值为query_time_sum或者query_count\n        :type OrderBy: str\n        :param OrderByType: 排序类型，desc或者asc\n        :type OrderByType: str\n        :param Slave: 是否查询从机的慢查询，0-主机; 1-从机\n        :type Slave: int\n        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None
        self.Db = None
        self.OrderBy = None
        self.OrderByType = None
        self.Slave = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Db = params.get("Db")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Slave = params.get("Slave")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 慢查询日志数据\n        :type Data: list of SlowLogData\n        :param LockTimeSum: 所有语句锁时间总和\n        :type LockTimeSum: float\n        :param QueryCount: 所有语句查询总次数\n        :type QueryCount: int\n        :param Total: 总记录数\n        :type Total: int\n        :param QueryTimeSum: 所有语句查询时间总和\n        :type QueryTimeSum: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.LockTimeSum = None
        self.QueryCount = None
        self.Total = None
        self.QueryTimeSum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SlowLogData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.LockTimeSum = params.get("LockTimeSum")
        self.QueryCount = params.get("QueryCount")
        self.Total = params.get("Total")
        self.QueryTimeSum = params.get("QueryTimeSum")
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        """
        :param Databases: 该实例上的数据库列表。\n        :type Databases: list of Database\n        :param InstanceId: 透传入参。\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Databases = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DescribeDcnDetailRequest(AbstractModel):
    """DescribeDcnDetail请求参数结构体

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
        


class DescribeDcnDetailResponse(AbstractModel):
    """DescribeDcnDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DcnDetails: DCN同步详情\n        :type DcnDetails: list of DcnDetailItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DcnDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DcnDetails") is not None:
            self.DcnDetails = []
            for item in params.get("DcnDetails"):
                obj = DcnDetailItem()
                obj._deserialize(item)
                self.DcnDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步请求接口返回的任务流程号。\n        :type FlowId: int\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 流程状态，0：成功，1：失败，2：运行中\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如tdsql-6ltok4u9\n        :type InstanceId: str\n        :param Limit: 一次最多返回多少条数据。默认为无穷大，返回符合要求的所有数据\n        :type Limit: int\n        :param Offset: 返回数据的偏移量，默认为0\n        :type Offset: int\n        """
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
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 节点总个数\n        :type TotalCount: int\n        :param NodesInfo: 节点信息\n        :type NodesInfo: list of NodeInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.NodesInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NodesInfo") is not None:
            self.NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodesInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogFileRetentionPeriodRequest(AbstractModel):
    """DescribeLogFileRetentionPeriod请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogFileRetentionPeriodResponse(AbstractModel):
    """DescribeLogFileRetentionPeriod返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Days: 日志备份天数\n        :type Days: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.Days = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。\n        :type DealNames: list of str\n        """
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
        :param TotalCount: 返回的订单数量。\n        :type TotalCount: list of int\n        :param Deals: 订单信息列表。\n        :type Deals: list of Deal\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Deals = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePriceRequest(AbstractModel):
    """DescribePrice请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 欲新购实例的可用区ID。\n        :type Zone: str\n        :param NodeCount: 实例节点个数，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。\n        :type NodeCount: int\n        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。\n        :type Memory: int\n        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。\n        :type Storage: int\n        :param Period: 欲购买的时长，单位：月。\n        :type Period: int\n        :param Count: 欲购买的数量，默认查询购买1个实例的价格。\n        :type Count: int\n        :param Paymode: 付费类型。postpaid：按量付费   prepaid：预付费\n        :type Paymode: str\n        """
        self.Zone = None
        self.NodeCount = None
        self.Memory = None
        self.Storage = None
        self.Period = None
        self.Count = None
        self.Paymode = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Period = params.get("Period")
        self.Count = params.get("Count")
        self.Paymode = params.get("Paymode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePriceResponse(AbstractModel):
    """DescribePrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分\n        :type OriginalPrice: int\n        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。\n        :type Price: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称，本接口取值：mariadb。\n        :type Product: str\n        :param ProjectId: 项目ID。\n        :type ProjectId: int\n        """
        self.Product = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
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
        :param Groups: 安全组详情。\n        :type Groups: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeRenewalPriceRequest(AbstractModel):
    """DescribeRenewalPrice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待续费的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param Period: 续费时长，单位：月。不传则默认为1个月。\n        :type Period: int\n        """
        self.InstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRenewalPriceResponse(AbstractModel):
    """DescribeRenewalPrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分\n        :type OriginalPrice: int\n        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。\n        :type Price: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeSaleInfoRequest(AbstractModel):
    """DescribeSaleInfo请求参数结构体

    """


class DescribeSaleInfoResponse(AbstractModel):
    """DescribeSaleInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RegionList: 可售卖地域信息列表\n        :type RegionList: list of RegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSqlLogsRequest(AbstractModel):
    """DescribeSqlLogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param Offset: SQL日志偏移。\n        :type Offset: int\n        :param Limit: 拉取数量（0-10000，为0时拉取总数信息）。\n        :type Limit: int\n        """
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
        


class DescribeSqlLogsResponse(AbstractModel):
    """DescribeSqlLogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 当前消息队列中的sql日志条目数。\n        :type TotalCount: int\n        :param StartOffset: 消息队列中的sql日志起始偏移。\n        :type StartOffset: int\n        :param EndOffset: 消息队列中的sql日志结束偏移。\n        :type EndOffset: int\n        :param Offset: 返回的第一条sql日志的偏移。\n        :type Offset: int\n        :param Count: 返回的sql日志数量。\n        :type Count: int\n        :param SqlItems: Sql日志列表。\n        :type SqlItems: list of SqlLogItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.StartOffset = None
        self.EndOffset = None
        self.Offset = None
        self.Count = None
        self.SqlItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.StartOffset = params.get("StartOffset")
        self.EndOffset = params.get("EndOffset")
        self.Offset = params.get("Offset")
        self.Count = params.get("Count")
        if params.get("SqlItems") is not None:
            self.SqlItems = []
            for item in params.get("SqlItems"):
                obj = SqlLogItem()
                obj._deserialize(item)
                self.SqlItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUpgradePriceRequest(AbstractModel):
    """DescribeUpgradePrice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待升级的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。\n        :type Memory: int\n        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。\n        :type Storage: int\n        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpgradePriceResponse(AbstractModel):
    """DescribeUpgradePrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分\n        :type OriginalPrice: int\n        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。\n        :type Price: int\n        :param Formula: 变配明细计算公式\n        :type Formula: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OriginalPrice = None
        self.Price = None
        self.Formula = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.Formula = params.get("Formula")
        self.RequestId = params.get("RequestId")


class DestroyHourDBInstanceRequest(AbstractModel):
    """DestroyHourDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，格式如：tdsql-avw0207d，与云数据库控制台页面中显示的实例 ID 相同。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyHourDBInstanceResponse(AbstractModel):
    """DestroyHourDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/237/16177)。\n        :type FlowId: int\n        :param InstanceId: 实例 ID，与入参InstanceId一致。\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称，本接口取值：mariadb。\n        :type Product: str\n        :param SecurityGroupId: 安全组Id。\n        :type SecurityGroupId: str\n        :param InstanceIds: 实例ID列表，一个或者多个实例Id组成的数组。\n        :type InstanceIds: list of str\n        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
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


class FlushBinlogRequest(AbstractModel):
    """FlushBinlog请求参数结构体

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
        


class FlushBinlogResponse(AbstractModel):
    """FlushBinlog返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FunctionPrivilege(AbstractModel):
    """函数权限信息

    """

    def __init__(self):
        """
        :param Database: 数据库名\n        :type Database: str\n        :param FunctionName: 数据库函数名\n        :type FunctionName: str\n        :param Privileges: 权限信息\n        :type Privileges: list of str\n        """
        self.Database = None
        self.FunctionName = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.FunctionName = params.get("FunctionName")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param UserName: 登录用户名。\n        :type UserName: str\n        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。\n        :type Host: str\n        :param DbName: 数据库名。如果为 \*，表示设置全局权限（即 \*.\*），此时忽略 Type 和 Object 参数。当DbName不为\*时，需要传入参 Type。\n        :type DbName: str\n        :param Privileges: 全局权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES 
库权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER 
表/视图权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER 
存储过程/函数权限： ALTER ROUTINE，EXECUTE 
字段权限： INSERT，REFERENCES，SELECT，UPDATE\n        :type Privileges: list of str\n        :param Type: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示设置该数据库权限（即db.\*），此时忽略 Object 参数\n        :type Type: str\n        :param Object: 具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空\n        :type Object: str\n        :param ColName: 当 Type=table 时，ColName 为 \* 表示对表授权，如果为具体字段名，表示对字段授权\n        :type ColName: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Privileges = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Privileges = params.get("Privileges")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待初始化的实例ID列表，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceIds: list of str\n        :param Params: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步）。\n        :type Params: list of DBParamValue\n        """
        self.InstanceIds = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)
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
        """
        :param FlowId: 异步任务ID，可通过 DescribeFlow 查询任务状态。\n        :type FlowId: int\n        :param InstanceIds: 透传入参。\n        :type InstanceIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class InstanceSpec(AbstractModel):
    """按机型归类的实例可售卖规格信息

    """

    def __init__(self):
        """
        :param Machine: 设备型号\n        :type Machine: str\n        :param SpecInfos: 该机型对应的可售卖规格列表\n        :type SpecInfos: list of SpecConfigInfo\n        """
        self.Machine = None
        self.SpecInfos = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        if params.get("SpecInfos") is not None:
            self.SpecInfos = []
            for item in params.get("SpecInfos"):
                obj = SpecConfigInfo()
                obj._deserialize(item)
                self.SpecInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillSessionRequest(AbstractModel):
    """KillSession请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param SessionId: 会话ID列表\n        :type SessionId: list of int\n        """
        self.InstanceId = None
        self.SessionId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillSessionResponse(AbstractModel):
    """KillSession返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """拉取的日志信息

    """

    def __init__(self):
        """
        :param Mtime: Log最后修改时间\n        :type Mtime: int\n        :param Length: 文件长度\n        :type Length: int\n        :param Uri: 下载Log时用到的统一资源标识符\n        :type Uri: str\n        :param FileName: 文件名\n        :type FileName: str\n        """
        self.Mtime = None
        self.Length = None
        self.Uri = None
        self.FileName = None


    def _deserialize(self, params):
        self.Mtime = params.get("Mtime")
        self.Length = params.get("Length")
        self.Uri = params.get("Uri")
        self.FileName = params.get("FileName")
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
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param UserName: 登录用户名。\n        :type UserName: str\n        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。\n        :type Host: str\n        :param Description: 新的账号备注，长度 0~256。\n        :type Description: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，格式如：tdsql-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。\n        :type InstanceId: str\n        :param Accounts: 数据库的账号，包括用户名和域名。\n        :type Accounts: list of Account\n        :param GlobalPrivileges: 全局权限。其中，GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，该字段传空数组。\n        :type GlobalPrivileges: list of str\n        :param DatabasePrivileges: 数据库的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。\n        :type DatabasePrivileges: list of DatabasePrivilege\n        :param TablePrivileges: 数据库中表的权限。Privileges 权限的可选值为：权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。\n        :type TablePrivileges: list of TablePrivilege\n        :param ColumnPrivileges: 数据库表中列的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。\n        :type ColumnPrivileges: list of ColumnPrivilege\n        :param ViewPrivileges: 数据库视图的权限。Privileges 权限的可选值为：权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。\n        :type ViewPrivileges: list of ViewPrivileges\n        :param FunctionPrivileges: 数据库函数的权限。Privileges 权限的可选值为：权限的可选值为："ALTER ROUTINE"，"EXECUTE"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。\n        :type FunctionPrivileges: list of FunctionPrivilege\n        :param ProcedurePrivileges: 数据库存储过程的权限。Privileges 权限的可选值为：权限的可选值为："ALTER ROUTINE"，"EXECUTE"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。\n        :type ProcedurePrivileges: list of ProcedurePrivilege\n        """
        self.InstanceId = None
        self.Accounts = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.ViewPrivileges = None
        self.FunctionPrivileges = None
        self.ProcedurePrivileges = None


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
        if params.get("ViewPrivileges") is not None:
            self.ViewPrivileges = []
            for item in params.get("ViewPrivileges"):
                obj = ViewPrivileges()
                obj._deserialize(item)
                self.ViewPrivileges.append(obj)
        if params.get("FunctionPrivileges") is not None:
            self.FunctionPrivileges = []
            for item in params.get("FunctionPrivileges"):
                obj = FunctionPrivilege()
                obj._deserialize(item)
                self.FunctionPrivileges.append(obj)
        if params.get("ProcedurePrivileges") is not None:
            self.ProcedurePrivileges = []
            for item in params.get("ProcedurePrivileges"):
                obj = ProcedurePrivilege()
                obj._deserialize(item)
                self.ProcedurePrivileges.append(obj)
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
        """
        :param FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/237/16177)。\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyBackupTimeRequest(AbstractModel):
    """ModifyBackupTime请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param StartBackupTime: 每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00\n        :type StartBackupTime: str\n        :param EndBackupTime: 每天备份执行的区间的结束时间，格式 mm:ss，形如 23:59\n        :type EndBackupTime: str\n        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupTimeResponse(AbstractModel):
    """ModifyBackupTime返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 设置的状态，0 表示成功\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待修改的实例 ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param InstanceName: 新的实例名称。允许的字符为字母、数字、下划线、连字符和中文。\n        :type InstanceName: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称，本接口取值：mariadb。\n        :type Product: str\n        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param SecurityGroupIds: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组\n        :type SecurityGroupIds: list of str\n        """
        self.Product = None
        self.InstanceId = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
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


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待修改的实例ID列表。实例 ID 形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceIds: list of str\n        :param ProjectId: 要分配的项目 ID，可以通过 DescribeProjects 查询项目列表接口获取。\n        :type ProjectId: int\n        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Params: 参数列表，每一个元素是Param和Value的组合\n        :type Params: list of DBParamValue\n        """
        self.InstanceId = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Result: 参数修改结果\n        :type Result: list of ParamModifyResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyLogFileRetentionPeriodRequest(AbstractModel):
    """ModifyLogFileRetentionPeriod请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param Days: 保存的天数,不能超过30\n        :type Days: int\n        """
        self.InstanceId = None
        self.Days = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogFileRetentionPeriodResponse(AbstractModel):
    """ModifyLogFileRetentionPeriod返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class MonitorData(AbstractModel):
    """监控数据

    """

    def __init__(self):
        """
        :param StartTime: 起始时间，形如 2018-03-24 23:59:59\n        :type StartTime: str\n        :param EndTime: 结束时间，形如 2018-03-24 23:59:59\n        :type EndTime: str\n        :param Data: 监控数据\n        :type Data: list of float\n        """
        self.StartTime = None
        self.EndTime = None
        self.Data = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """描述实例的各个DB节点信息

    """

    def __init__(self):
        """
        :param NodeId: DB节点ID\n        :type NodeId: str\n        :param Role: DB节点角色，取值为master或者slave\n        :type Role: str\n        """
        self.NodeId = None
        self.Role = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待开放外网访问的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param Ipv6Flag: 是否IPv6，默认0\n        :type Ipv6Flag: int\n        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务ID，可通过 DescribeFlow 查询任务状态。\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ParamConstraint(AbstractModel):
    """参数约束

    """

    def __init__(self):
        """
        :param Type: 约束类型,如枚举enum，区间section\n        :type Type: str\n        :param Enum: 约束类型为enum时的可选值列表\n        :type Enum: str\n        :param Range: 约束类型为section时的范围
注意：此字段可能返回 null，表示取不到有效值。\n        :type Range: :class:`tencentcloud.mariadb.v20170312.models.ConstraintRange`\n        :param String: 约束类型为string时的可选值列表\n        :type String: str\n        """
        self.Type = None
        self.Enum = None
        self.Range = None
        self.String = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Enum = params.get("Enum")
        if params.get("Range") is not None:
            self.Range = ConstraintRange()
            self.Range._deserialize(params.get("Range"))
        self.String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    """DB参数描述

    """

    def __init__(self):
        """
        :param Param: 参数名字\n        :type Param: str\n        :param Value: 当前参数值\n        :type Value: str\n        :param SetValue: 设置过的值，参数生效后，该值和value一样。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SetValue: str\n        :param Default: 系统默认值\n        :type Default: str\n        :param Constraint: 参数限制\n        :type Constraint: :class:`tencentcloud.mariadb.v20170312.models.ParamConstraint`\n        :param HaveSetValue: 是否有设置过值，false:没有设置过值，true:有设置过值。\n        :type HaveSetValue: bool\n        """
        self.Param = None
        self.Value = None
        self.SetValue = None
        self.Default = None
        self.Constraint = None
        self.HaveSetValue = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        self.SetValue = params.get("SetValue")
        self.Default = params.get("Default")
        if params.get("Constraint") is not None:
            self.Constraint = ParamConstraint()
            self.Constraint._deserialize(params.get("Constraint"))
        self.HaveSetValue = params.get("HaveSetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamModifyResult(AbstractModel):
    """修改参数结果

    """

    def __init__(self):
        """
        :param Param: 修改参数名字\n        :type Param: str\n        :param Code: 参数修改结果。0表示修改成功；-1表示修改失败；-2表示该参数值非法\n        :type Code: int\n        """
        self.Param = None
        self.Code = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PerformanceMonitorSet(AbstractModel):
    """DB性能监控指标集合

    """

    def __init__(self):
        """
        :param UpdateTotal: 更新操作数UPDATE\n        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DiskIops: 磁盘每秒IO次数\n        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param ConnActive: 活跃连接数\n        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemHitRate: 缓存命中率\n        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SlaveDelay: 主备延迟\n        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param SelectTotal: 查询操作数SELECT\n        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param LongQuery: 慢查询数\n        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DeleteTotal: 删除操作数DELETE\n        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param InsertTotal: 插入操作数INSERT\n        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param IsMasterSwitched: 是否发生主备切换，1为发生，0否\n        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        """
        self.UpdateTotal = None
        self.DiskIops = None
        self.ConnActive = None
        self.MemHitRate = None
        self.SlaveDelay = None
        self.SelectTotal = None
        self.LongQuery = None
        self.DeleteTotal = None
        self.InsertTotal = None
        self.IsMasterSwitched = None


    def _deserialize(self, params):
        if params.get("UpdateTotal") is not None:
            self.UpdateTotal = MonitorData()
            self.UpdateTotal._deserialize(params.get("UpdateTotal"))
        if params.get("DiskIops") is not None:
            self.DiskIops = MonitorData()
            self.DiskIops._deserialize(params.get("DiskIops"))
        if params.get("ConnActive") is not None:
            self.ConnActive = MonitorData()
            self.ConnActive._deserialize(params.get("ConnActive"))
        if params.get("MemHitRate") is not None:
            self.MemHitRate = MonitorData()
            self.MemHitRate._deserialize(params.get("MemHitRate"))
        if params.get("SlaveDelay") is not None:
            self.SlaveDelay = MonitorData()
            self.SlaveDelay._deserialize(params.get("SlaveDelay"))
        if params.get("SelectTotal") is not None:
            self.SelectTotal = MonitorData()
            self.SelectTotal._deserialize(params.get("SelectTotal"))
        if params.get("LongQuery") is not None:
            self.LongQuery = MonitorData()
            self.LongQuery._deserialize(params.get("LongQuery"))
        if params.get("DeleteTotal") is not None:
            self.DeleteTotal = MonitorData()
            self.DeleteTotal._deserialize(params.get("DeleteTotal"))
        if params.get("InsertTotal") is not None:
            self.InsertTotal = MonitorData()
            self.InsertTotal._deserialize(params.get("InsertTotal"))
        if params.get("IsMasterSwitched") is not None:
            self.IsMasterSwitched = MonitorData()
            self.IsMasterSwitched._deserialize(params.get("IsMasterSwitched"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcedurePrivilege(AbstractModel):
    """存储过程权限信息

    """

    def __init__(self):
        """
        :param Database: 数据库名\n        :type Database: str\n        :param Procedure: 数据库存储过程名\n        :type Procedure: str\n        :param Privileges: 权限信息\n        :type Privileges: list of str\n        """
        self.Database = None
        self.Procedure = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Procedure = params.get("Procedure")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """售卖可用区信息

    """

    def __init__(self):
        """
        :param Region: 地域英文ID\n        :type Region: str\n        :param RegionId: 地域数字ID\n        :type RegionId: int\n        :param RegionName: 地域中文名\n        :type RegionName: str\n        :param ZoneList: 可用区列表\n        :type ZoneList: list of ZonesInfo\n        :param AvailableChoice: 可选择的主可用区和从可用区\n        :type AvailableChoice: list of ZoneChooseInfo\n        """
        self.Region = None
        self.RegionId = None
        self.RegionName = None
        self.ZoneList = None
        self.AvailableChoice = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        if params.get("AvailableChoice") is not None:
            self.AvailableChoice = []
            for item in params.get("AvailableChoice"):
                obj = ZoneChooseInfo()
                obj._deserialize(item)
                self.AvailableChoice.append(obj)
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
        :param InstanceId: 待续费的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param Period: 续费时长，单位：月。\n        :type Period: int\n        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。\n        :type AutoVoucher: bool\n        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。\n        :type VoucherIds: list of str\n        """
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
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。\n        :type DealName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param UserName: 登录用户名。\n        :type UserName: str\n        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。\n        :type Host: str\n        :param Password: 新密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。\n        :type Password: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """标签对象，包含tagKey & tagValue

    """

    def __init__(self):
        """
        :param TagKey: 标签键key\n        :type TagKey: str\n        :param TagValue: 标签值value\n        :type TagValue: str\n        """
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
        


class ResourceUsageMonitorSet(AbstractModel):
    """DB资源使用情况监控指标集合

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: binlog日志磁盘可用空间,单位GB\n        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param CpuUsageRate: CPU利用率\n        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param MemAvailable: 内存可用空间,单位GB\n        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        :param DataDiskAvailable: 磁盘可用空间,单位GB\n        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`\n        """
        self.BinlogDiskAvailable = None
        self.CpuUsageRate = None
        self.MemAvailable = None
        self.DataDiskAvailable = None


    def _deserialize(self, params):
        if params.get("BinlogDiskAvailable") is not None:
            self.BinlogDiskAvailable = MonitorData()
            self.BinlogDiskAvailable._deserialize(params.get("BinlogDiskAvailable"))
        if params.get("CpuUsageRate") is not None:
            self.CpuUsageRate = MonitorData()
            self.CpuUsageRate._deserialize(params.get("CpuUsageRate"))
        if params.get("MemAvailable") is not None:
            self.MemAvailable = MonitorData()
            self.MemAvailable._deserialize(params.get("MemAvailable"))
        if params.get("DataDiskAvailable") is not None:
            self.DataDiskAvailable = MonitorData()
            self.DataDiskAvailable._deserialize(params.get("DataDiskAvailable"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID的数组\n        :type InstanceIds: list of str\n        :param RestartTime: 重启时间\n        :type RestartTime: str\n        """
        self.InstanceIds = None
        self.RestartTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.RestartTime = params.get("RestartTime")
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
        """
        :param FlowId: 异步任务ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss\n        :type CreateTime: str\n        :param SecurityGroupId: 安全组ID\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: 安全组备注\n        :type SecurityGroupRemark: str\n        :param Inbound: 入站规则\n        :type Inbound: list of SecurityGroupBound\n        :param Outbound: 出站规则\n        :type Outbound: list of SecurityGroupBound\n        """
        self.ProjectId = None
        self.CreateTime = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.Inbound = None
        self.Outbound = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Outbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    """安全出入口规则

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT 或者 DROP\n        :type Action: str\n        :param CidrIp: 来源 IP 或 IP 段，例如192.168.0.0/16\n        :type CidrIp: str\n        :param PortRange: 端口\n        :type PortRange: str\n        :param IpProtocol: 网络协议，支持 UDP、TCP 等\n        :type IpProtocol: str\n        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogData(AbstractModel):
    """慢查询条目信息

    """

    def __init__(self):
        """
        :param CheckSum: 语句校验和，用于查询详情\n        :type CheckSum: str\n        :param Db: 数据库名称\n        :type Db: str\n        :param FingerPrint: 抽象的SQL语句\n        :type FingerPrint: str\n        :param LockTimeAvg: 平均的锁时间\n        :type LockTimeAvg: str\n        :param LockTimeMax: 最大锁时间\n        :type LockTimeMax: str\n        :param LockTimeMin: 最小锁时间\n        :type LockTimeMin: str\n        :param LockTimeSum: 锁时间总和\n        :type LockTimeSum: str\n        :param QueryCount: 查询次数\n        :type QueryCount: str\n        :param QueryTimeAvg: 平均查询时间\n        :type QueryTimeAvg: str\n        :param QueryTimeMax: 最大查询时间\n        :type QueryTimeMax: str\n        :param QueryTimeMin: 最小查询时间\n        :type QueryTimeMin: str\n        :param QueryTimeSum: 查询时间总和\n        :type QueryTimeSum: str\n        :param RowsExaminedSum: 扫描行数\n        :type RowsExaminedSum: str\n        :param RowsSentSum: 发送行数\n        :type RowsSentSum: str\n        :param TsMax: 最后执行时间\n        :type TsMax: str\n        :param TsMin: 首次执行时间\n        :type TsMin: str\n        :param User: 帐号\n        :type User: str\n        :param ExampleSql: 样例Sql
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExampleSql: str\n        """
        self.CheckSum = None
        self.Db = None
        self.FingerPrint = None
        self.LockTimeAvg = None
        self.LockTimeMax = None
        self.LockTimeMin = None
        self.LockTimeSum = None
        self.QueryCount = None
        self.QueryTimeAvg = None
        self.QueryTimeMax = None
        self.QueryTimeMin = None
        self.QueryTimeSum = None
        self.RowsExaminedSum = None
        self.RowsSentSum = None
        self.TsMax = None
        self.TsMin = None
        self.User = None
        self.ExampleSql = None


    def _deserialize(self, params):
        self.CheckSum = params.get("CheckSum")
        self.Db = params.get("Db")
        self.FingerPrint = params.get("FingerPrint")
        self.LockTimeAvg = params.get("LockTimeAvg")
        self.LockTimeMax = params.get("LockTimeMax")
        self.LockTimeMin = params.get("LockTimeMin")
        self.LockTimeSum = params.get("LockTimeSum")
        self.QueryCount = params.get("QueryCount")
        self.QueryTimeAvg = params.get("QueryTimeAvg")
        self.QueryTimeMax = params.get("QueryTimeMax")
        self.QueryTimeMin = params.get("QueryTimeMin")
        self.QueryTimeSum = params.get("QueryTimeSum")
        self.RowsExaminedSum = params.get("RowsExaminedSum")
        self.RowsSentSum = params.get("RowsSentSum")
        self.TsMax = params.get("TsMax")
        self.TsMin = params.get("TsMin")
        self.User = params.get("User")
        self.ExampleSql = params.get("ExampleSql")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecConfigInfo(AbstractModel):
    """实例可售卖规格详细信息，创建实例和扩容实例时 Pid+MemSize 唯一确定一种售卖规格，磁盘大小可用区间为[MinDataDisk,MaxDataDisk]

    """

    def __init__(self):
        """
        :param Machine: 设备型号\n        :type Machine: str\n        :param Memory: 内存大小，单位 GB\n        :type Memory: int\n        :param MinStorage: 数据盘规格最小值，单位 GB\n        :type MinStorage: int\n        :param MaxStorage: 数据盘规格最大值，单位 GB\n        :type MaxStorage: int\n        :param SuitInfo: 推荐的使用场景\n        :type SuitInfo: str\n        :param Qps: 最大 Qps 值\n        :type Qps: int\n        :param Pid: 产品类型 Id\n        :type Pid: int\n        :param NodeCount: 节点个数，2 表示一主一从，3 表示一主二从\n        :type NodeCount: int\n        :param Cpu: Cpu核数\n        :type Cpu: int\n        """
        self.Machine = None
        self.Memory = None
        self.MinStorage = None
        self.MaxStorage = None
        self.SuitInfo = None
        self.Qps = None
        self.Pid = None
        self.NodeCount = None
        self.Cpu = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        self.Memory = params.get("Memory")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.SuitInfo = params.get("SuitInfo")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")
        self.NodeCount = params.get("NodeCount")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SqlLogItem(AbstractModel):
    """描述一条sql日志的详细信息。

    """

    def __init__(self):
        """
        :param Offset: 本条日志在消息队列中的偏移量。\n        :type Offset: int\n        :param User: 执行本条sql的用户。\n        :type User: str\n        :param Client: 执行本条sql的客户端IP+端口。\n        :type Client: str\n        :param DbName: 数据库名称。\n        :type DbName: str\n        :param Sql: 执行的sql语句。\n        :type Sql: str\n        :param SelectRowNum: 返回的数据行数。\n        :type SelectRowNum: int\n        :param AffectRowNum: 影响行数。\n        :type AffectRowNum: int\n        :param Timestamp: Sql执行时间戳。\n        :type Timestamp: int\n        :param TimeCostMs: Sql耗时，单位为毫秒。\n        :type TimeCostMs: int\n        :param ResultCode: Sql返回码，0为成功。\n        :type ResultCode: int\n        """
        self.Offset = None
        self.User = None
        self.Client = None
        self.DbName = None
        self.Sql = None
        self.SelectRowNum = None
        self.AffectRowNum = None
        self.Timestamp = None
        self.TimeCostMs = None
        self.ResultCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.User = params.get("User")
        self.Client = params.get("Client")
        self.DbName = params.get("DbName")
        self.Sql = params.get("Sql")
        self.SelectRowNum = params.get("SelectRowNum")
        self.AffectRowNum = params.get("AffectRowNum")
        self.Timestamp = params.get("Timestamp")
        self.TimeCostMs = params.get("TimeCostMs")
        self.ResultCode = params.get("ResultCode")
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
        """
        :param Database: 数据库名\n        :type Database: str\n        :param Table: 数据库表名\n        :type Table: str\n        :param Privileges: 权限信息\n        :type Privileges: list of str\n        """
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
        


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待升级的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。\n        :type InstanceId: str\n        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。\n        :type Memory: int\n        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。\n        :type Storage: int\n        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。\n        :type AutoVoucher: bool\n        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。\n        :type VoucherIds: list of str\n        """
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
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。\n        :type DealName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ViewPrivileges(AbstractModel):
    """视图权限信息

    """

    def __init__(self):
        """
        :param Database: 数据库名\n        :type Database: str\n        :param View: 数据库视图名\n        :type View: str\n        :param Privileges: 权限信息\n        :type Privileges: list of str\n        """
        self.Database = None
        self.View = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.View = params.get("View")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneChooseInfo(AbstractModel):
    """分片节点可用区选择

    """

    def __init__(self):
        """
        :param MasterZone: 主可用区\n        :type MasterZone: :class:`tencentcloud.mariadb.v20170312.models.ZonesInfo`\n        :param SlaveZones: 可选的从可用区\n        :type SlaveZones: list of ZonesInfo\n        """
        self.MasterZone = None
        self.SlaveZones = None


    def _deserialize(self, params):
        if params.get("MasterZone") is not None:
            self.MasterZone = ZonesInfo()
            self.MasterZone._deserialize(params.get("MasterZone"))
        if params.get("SlaveZones") is not None:
            self.SlaveZones = []
            for item in params.get("SlaveZones"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self.SlaveZones.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZonesInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        """
        :param Zone: 可用区英文ID\n        :type Zone: str\n        :param ZoneId: 可用区数字ID\n        :type ZoneId: int\n        :param ZoneName: 可用区中文名\n        :type ZoneName: str\n        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        