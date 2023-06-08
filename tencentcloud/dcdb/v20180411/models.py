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
        :param User: 账户的名称
        :type User: str
        :param Host: 账户的域名
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
        


class ActiveHourDCDBInstanceRequest(AbstractModel):
    """ActiveHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 待升级的实例ID列表。形如：["dcdbt-ow728lmc"]，可以通过 DescribeDCDBInstances 查询实例详情获得。
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
        


class ActiveHourDCDBInstanceResponse(AbstractModel):
    """ActiveHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessInstanceIds: 解隔离成功的实例id列表
        :type SuccessInstanceIds: list of str
        :param FailedInstanceIds: 解隔离失败的实例id列表
        :type FailedInstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessInstanceIds = None
        self.FailedInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessInstanceIds = params.get("SuccessInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.RequestId = params.get("RequestId")


class AddShardConfig(AbstractModel):
    """升级实例 -- 新增分片类型

    """

    def __init__(self):
        r"""
        :param ShardCount: 新增分片的数量
        :type ShardCount: int
        :param ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self.ShardCount = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardCount = params.get("ShardCount")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
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
        r"""
        :param Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param SecurityGroupId: 要绑定的安全组ID，类似sg-efil73jd。
        :type SecurityGroupId: str
        :param InstanceIds: 被绑定的实例ID，类似tdsqlshard-lesecurk，支持指定多个实例。
        :type InstanceIds: list of str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BriefNodeInfo(AbstractModel):
    """描述分片DB节点信息

    """

    def __init__(self):
        r"""
        :param NodeId: DB节点ID
        :type NodeId: str
        :param Role: DB节点角色，取值为master或者slave
        :type Role: str
        :param ShardId: 节点所属分片的分片ID
        :type ShardId: str
        """
        self.NodeId = None
        self.Role = None
        self.ShardId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Role = params.get("Role")
        self.ShardId = params.get("ShardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDcnJobRequest(AbstractModel):
    """CancelDcnJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 灾备实例ID
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
        


class CancelDcnJobResponse(AbstractModel):
    """CancelDcnJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloneAccountRequest(AbstractModel):
    """CloneAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param SrcUser: 源用户账户名
        :type SrcUser: str
        :param SrcHost: 源用户HOST
        :type SrcHost: str
        :param DstUser: 目的用户账户名
        :type DstUser: str
        :param DstHost: 目的用户HOST
        :type DstHost: str
        :param DstDesc: 目的用户账户描述
        :type DstDesc: str
        """
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
        r"""
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


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待关闭外网访问的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Ipv6Flag: 是否IPv6，默认0
        :type Ipv6Flag: int
        """
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
        r"""
        :param FlowId: 异步任务ID，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
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
        


class ConfigValue(AbstractModel):
    """配置信息。包含配置项Config，配置值Value

    """

    def __init__(self):
        r"""
        :param Config: 配置项的名称，支持填写max_user_connections
        :type Config: str
        :param Value: 配置值
        :type Value: str
        """
        self.Config = None
        self.Value = None


    def _deserialize(self, params):
        self.Config = params.get("Config")
        self.Value = params.get("Value")
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
        r"""
        :param Min: 约束类型为section时的最小值
        :type Min: str
        :param Max: 约束类型为section时的最大值
        :type Max: str
        """
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
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param SrcUserName: 源用户名
        :type SrcUserName: str
        :param SrcHost: 源用户允许的访问 host
        :type SrcHost: str
        :param DstUserName: 目的用户名
        :type DstUserName: str
        :param DstHost: 目的用户允许的访问 host
        :type DstHost: str
        :param SrcReadOnly: 源账号的 ReadOnly 属性
        :type SrcReadOnly: str
        :param DstReadOnly: 目的账号的 ReadOnly 属性
        :type DstReadOnly: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UserName: AccountName
        :type UserName: str
        :param Host: 可以登录的主机，与mysql 账号的 host 格式一致，可以支持通配符，例如 %，10.%，10.20.%。
        :type Host: str
        :param Password: 账号密码，密码需要 8-32 个字符，不能以 '/' 开头，并且必须包含小写字母、大写字母、数字和符号()~!@#$%^&*-+=_|{}[]:<>,.?/。
        :type Password: str
        :param ReadOnly: 是否创建为只读账号，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败，3：只从备机读取。
        :type ReadOnly: int
        :param Description: 账号备注，可以包含中文、英文字符、常见符号和数字，长度为0~256字符
        :type Description: str
        :param DelayThresh: 如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :type DelayThresh: int
        :param SlaveConst: 针对只读账号，设置策略是否固定备机，0：不固定备机，即备机不满足条件与客户端不断开连接，Proxy选择其他可用备机，1：备机不满足条件断开连接，确保一个连接固定备机。
        :type SlaveConst: int
        :param MaxUserConnections: 用户最大连接数限制参数。不传或者传0表示为不限制，对应max_user_connections参数，目前10.1内核版本不支持设置。
        :type MaxUserConnections: int
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None
        self.ReadOnly = None
        self.Description = None
        self.DelayThresh = None
        self.SlaveConst = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        self.ReadOnly = params.get("ReadOnly")
        self.Description = params.get("Description")
        self.DelayThresh = params.get("DelayThresh")
        self.SlaveConst = params.get("SlaveConst")
        self.MaxUserConnections = params.get("MaxUserConnections")
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
        r"""
        :param InstanceId: 实例ID，透传入参。
        :type InstanceId: str
        :param UserName: 用户名，透传入参。
        :type UserName: str
        :param Host: 允许访问的 host，透传入参。
        :type Host: str
        :param ReadOnly: 透传入参。
        :type ReadOnly: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class CreateDCDBInstanceRequest(AbstractModel):
    """CreateDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zones: 分片节点可用区分布，最多可填两个可用区。当分片规格为一主两从时，其中两个节点在第一个可用区。
注意当前可售卖的可用区需要通过DescribeDCDBSaleInfo接口拉取。
        :type Zones: list of str
        :param Period: 欲购买的时长，单位：月。
        :type Period: int
        :param ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param ShardNodeCount: 单个分片节点个数，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        :param Count: 欲购买实例的数量
        :type Count: int
        :param ProjectId: 项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :type ProjectId: int
        :param VpcId: 虚拟私有网络 ID，不传或传空表示创建为基础网络
        :type VpcId: str
        :param SubnetId: 虚拟私有网络子网 ID，VpcId不为空时必填
        :type SubnetId: str
        :param DbVersionId: 数据库引擎版本，当前可选：8.0，5.7，10.1，10.0。
        :type DbVersionId: str
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param SecurityGroupId: 安全组id
        :type SecurityGroupId: str
        :param InstanceName: 实例名称， 可以通过该字段自主的设置实例的名字
        :type InstanceName: str
        :param Ipv6Flag: 是否支持IPv6，0:不支持，1:支持
        :type Ipv6Flag: int
        :param ResourceTags: 标签键值对数组
        :type ResourceTags: list of ResourceTag
        :param InitParams: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :type InitParams: list of DBParamValue
        :param DcnRegion: DCN源地域
        :type DcnRegion: str
        :param DcnInstanceId: DCN源实例ID
        :type DcnInstanceId: str
        :param AutoRenewFlag: 自动续费标记，0:默认状态(用户未设置，即初始状态即手动续费，用户开通了预付费不停服特权也会进行自动续费)， 1:自动续费，2:明确不自动续费(用户设置)。若业务无续费概念或无需自动续费，需要设置为0
        :type AutoRenewFlag: int
        :param SecurityGroupIds: 安全组ids，安全组可以传数组形式，兼容之前SecurityGroupId参数
        :type SecurityGroupIds: list of str
        """
        self.Zones = None
        self.Period = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardNodeCount = None
        self.ShardCount = None
        self.Count = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DbVersionId = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.SecurityGroupId = None
        self.InstanceName = None
        self.Ipv6Flag = None
        self.ResourceTags = None
        self.InitParams = None
        self.DcnRegion = None
        self.DcnInstanceId = None
        self.AutoRenewFlag = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.Period = params.get("Period")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardCount = params.get("ShardCount")
        self.Count = params.get("Count")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DbVersionId = params.get("DbVersionId")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceName = params.get("InstanceName")
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
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDCDBInstanceResponse(AbstractModel):
    """CreateDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param InstanceIds: 订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDedicatedClusterDCDBInstanceRequest(AbstractModel):
    """CreateDedicatedClusterDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param GoodsNum: 分配实例个数
        :type GoodsNum: int
        :param ShardNum: 分片数量
        :type ShardNum: int
        :param ShardMemory: 分片內存大小, 单位GB
        :type ShardMemory: int
        :param ShardStorage: 分片磁盘大小, 单位GB
        :type ShardStorage: int
        :param ClusterId: 独享集群集群uuid
        :type ClusterId: str
        :param Zone: （废弃）可用区
        :type Zone: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Cpu: （废弃）cpu大小，单位：核
        :type Cpu: int
        :param VpcId: 网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param ShardMachine: （废弃）分片机型
        :type ShardMachine: str
        :param ShardNodeNum: 分片的节点个数
        :type ShardNodeNum: int
        :param ShardNodeCpu: （废弃）节点cpu核数，单位：1/100核
        :type ShardNodeCpu: int
        :param ShardNodeMemory: （废弃）节点內存大小，单位：GB
        :type ShardNodeMemory: int
        :param ShardNodeStorage: （废弃）节点磁盘大小，单位：GB
        :type ShardNodeStorage: int
        :param DbVersionId: db版本
        :type DbVersionId: str
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param DcnInstanceId: DCN源实例ID
        :type DcnInstanceId: str
        :param DcnRegion: DCN源实例地域名
        :type DcnRegion: str
        :param InstanceName: 自定义实例名称
        :type InstanceName: str
        :param ResourceTags: 标签
        :type ResourceTags: list of ResourceTag
        :param Ipv6Flag: 支持IPv6标志：1 支持， 0 不支持
        :type Ipv6Flag: int
        :param Pid: （废弃）Pid，可通过获取独享集群售卖配置接口得到
        :type Pid: int
        :param InitParams: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :type InitParams: list of DBParamValue
        :param MasterHostId: 指定主节点uuid，不填随机分配
        :type MasterHostId: str
        :param SlaveHostIds: 指定从节点uuid，不填随机分配
        :type SlaveHostIds: list of str
        :param RollbackInstanceId: 需要回档的源实例ID
        :type RollbackInstanceId: str
        :param RollbackTime: 回档时间
        :type RollbackTime: str
        """
        self.GoodsNum = None
        self.ShardNum = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ClusterId = None
        self.Zone = None
        self.ProjectId = None
        self.Cpu = None
        self.VpcId = None
        self.SubnetId = None
        self.ShardMachine = None
        self.ShardNodeNum = None
        self.ShardNodeCpu = None
        self.ShardNodeMemory = None
        self.ShardNodeStorage = None
        self.DbVersionId = None
        self.SecurityGroupId = None
        self.DcnInstanceId = None
        self.DcnRegion = None
        self.InstanceName = None
        self.ResourceTags = None
        self.Ipv6Flag = None
        self.Pid = None
        self.InitParams = None
        self.MasterHostId = None
        self.SlaveHostIds = None
        self.RollbackInstanceId = None
        self.RollbackTime = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.ShardNum = params.get("ShardNum")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ClusterId = params.get("ClusterId")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.Cpu = params.get("Cpu")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ShardMachine = params.get("ShardMachine")
        self.ShardNodeNum = params.get("ShardNodeNum")
        self.ShardNodeCpu = params.get("ShardNodeCpu")
        self.ShardNodeMemory = params.get("ShardNodeMemory")
        self.ShardNodeStorage = params.get("ShardNodeStorage")
        self.DbVersionId = params.get("DbVersionId")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.DcnInstanceId = params.get("DcnInstanceId")
        self.DcnRegion = params.get("DcnRegion")
        self.InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.Ipv6Flag = params.get("Ipv6Flag")
        self.Pid = params.get("Pid")
        if params.get("InitParams") is not None:
            self.InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.InitParams.append(obj)
        self.MasterHostId = params.get("MasterHostId")
        self.SlaveHostIds = params.get("SlaveHostIds")
        self.RollbackInstanceId = params.get("RollbackInstanceId")
        self.RollbackTime = params.get("RollbackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDedicatedClusterDCDBInstanceResponse(AbstractModel):
    """CreateDedicatedClusterDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 分配资源ID数组
        :type InstanceIds: list of str
        :param FlowId: 流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIds = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateHourDCDBInstanceRequest(AbstractModel):
    """CreateHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param ShardNodeCount: 单个分片节点个数，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        :param Count: 欲购买实例的数量
        :type Count: int
        :param ProjectId: 项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :type ProjectId: int
        :param VpcId: 虚拟私有网络 ID，不传或传空表示创建为基础网络
        :type VpcId: str
        :param SubnetId: 虚拟私有网络子网 ID，VpcId不为空时必填
        :type SubnetId: str
        :param ShardCpu: 分片cpu大小，单位：核，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardCpu: int
        :param DbVersionId: 数据库引擎版本，当前可选：8.0，5.7，10.1，10.0。
        :type DbVersionId: str
        :param Zones: 分片节点可用区分布，最多可填两个可用区。当分片规格为一主两从时，其中两个节点在第一个可用区。
        :type Zones: list of str
        :param SecurityGroupId: 安全组id
        :type SecurityGroupId: str
        :param InstanceName: 实例名称， 可以通过该字段自主的设置实例的名字
        :type InstanceName: str
        :param Ipv6Flag: 是否支持IPv6，0:不支持，1:支持
        :type Ipv6Flag: int
        :param ResourceTags: 标签键值对数组
        :type ResourceTags: list of ResourceTag
        :param DcnRegion: DCN源地域
        :type DcnRegion: str
        :param DcnInstanceId: DCN源实例ID
        :type DcnInstanceId: str
        :param InitParams: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步可退化）。
        :type InitParams: list of DBParamValue
        :param RollbackInstanceId: 需要回档的源实例ID
        :type RollbackInstanceId: str
        :param RollbackTime: 回档时间，例如“2021-11-22 00:00:00”
        :type RollbackTime: str
        :param SecurityGroupIds: 安全组ids，安全组可以传数组形式，兼容之前SecurityGroupId参数
        :type SecurityGroupIds: list of str
        """
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardNodeCount = None
        self.ShardCount = None
        self.Count = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.ShardCpu = None
        self.DbVersionId = None
        self.Zones = None
        self.SecurityGroupId = None
        self.InstanceName = None
        self.Ipv6Flag = None
        self.ResourceTags = None
        self.DcnRegion = None
        self.DcnInstanceId = None
        self.InitParams = None
        self.RollbackInstanceId = None
        self.RollbackTime = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardCount = params.get("ShardCount")
        self.Count = params.get("Count")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ShardCpu = params.get("ShardCpu")
        self.DbVersionId = params.get("DbVersionId")
        self.Zones = params.get("Zones")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceName = params.get("InstanceName")
        self.Ipv6Flag = params.get("Ipv6Flag")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DcnRegion = params.get("DcnRegion")
        self.DcnInstanceId = params.get("DcnInstanceId")
        if params.get("InitParams") is not None:
            self.InitParams = []
            for item in params.get("InitParams"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.InitParams.append(obj)
        self.RollbackInstanceId = params.get("RollbackInstanceId")
        self.RollbackTime = params.get("RollbackTime")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHourDCDBInstanceResponse(AbstractModel):
    """CreateHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
        :type InstanceIds: list of str
        :param FlowId: 流程id，可以根据流程id查询创建进度
        :type FlowId: int
        :param DealName: 订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIds = None
        self.FlowId = None
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.FlowId = params.get("FlowId")
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class CreateTmpDCDBInstanceRequest(AbstractModel):
    """CreateTmpDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 回档实例的ID
        :type InstanceId: str
        :param RollbackTime: 回档时间点
        :type RollbackTime: str
        """
        self.InstanceId = None
        self.RollbackTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RollbackTime = params.get("RollbackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTmpDCDBInstanceResponse(AbstractModel):
    """CreateTmpDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
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


class DBAccount(AbstractModel):
    """云数据库账号信息

    """

    def __init__(self):
        r"""
        :param UserName: 用户名
        :type UserName: str
        :param Host: 用户可以从哪台主机登录（对应 MySQL 用户的 host 字段，UserName + Host 唯一标识一个用户，IP形式，IP段以%结尾；支持填入%；为空默认等于%）
        :type Host: str
        :param Description: 用户备注信息
        :type Description: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 最后更新时间
        :type UpdateTime: str
        :param ReadOnly: 只读标记，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败。
        :type ReadOnly: int
        :param DelayThresh: 如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :type DelayThresh: int
        :param SlaveConst: 针对只读账号，设置策略是否固定备机，0：不固定备机，即备机不满足条件与客户端不断开连接，Proxy选择其他可用备机，1：备机不满足条件断开连接，确保一个连接固定备机。
        :type SlaveConst: int
        :param MaxUserConnections: 用户最大连接数，0代表无限制	
        :type MaxUserConnections: int
        """
        self.UserName = None
        self.Host = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ReadOnly = None
        self.DelayThresh = None
        self.SlaveConst = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ReadOnly = params.get("ReadOnly")
        self.DelayThresh = params.get("DelayThresh")
        self.SlaveConst = params.get("SlaveConst")
        self.MaxUserConnections = params.get("MaxUserConnections")
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
        r"""
        :param Param: 参数名称
        :type Param: str
        :param Value: 参数值
        :type Value: str
        """
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
        


class DCDBInstanceInfo(AbstractModel):
    """分布式数据库实例信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param AppId: 应用ID
        :type AppId: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param VpcId: VPC数字ID
        :type VpcId: int
        :param SubnetId: Subnet数字ID
        :type SubnetId: int
        :param StatusDesc: 状态中文描述
        :type StatusDesc: str
        :param Status: 实例状态：0 创建中，1 流程处理中， 2 运行中，3 实例未初始化，-1 实例已隔离，4 实例初始化中，5 实例删除中，6 实例重启中，7 数据迁移中
        :type Status: int
        :param Vip: 内网IP
        :type Vip: str
        :param Vport: 内网端口
        :type Vport: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param AutoRenewFlag: 自动续费标志
        :type AutoRenewFlag: int
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param Storage: 存储大小，单位 GB
        :type Storage: int
        :param ShardCount: 分片个数
        :type ShardCount: int
        :param PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param IsolatedTimestamp: 隔离时间
        :type IsolatedTimestamp: str
        :param Uin: 账号ID
        :type Uin: str
        :param ShardDetail: 分片详情
        :type ShardDetail: list of ShardInfo
        :param NodeCount: 节点数，2 为一主一从， 3 为一主二从
        :type NodeCount: int
        :param IsTmp: 临时实例标记，0 为非临时实例
        :type IsTmp: int
        :param ExclusterId: 独享集群ID，为空表示非独享集群实例
        :type ExclusterId: str
        :param UniqueVpcId: 字符串型的私有网络ID
        :type UniqueVpcId: str
        :param UniqueSubnetId: 字符串型的私有网络子网ID
        :type UniqueSubnetId: str
        :param Id: 数字实例ID（过时字段，请勿依赖该值）
        :type Id: int
        :param WanDomain: 外网访问的域名，公网可解析
        :type WanDomain: str
        :param WanVip: 外网 IP 地址，公网可访问
        :type WanVip: str
        :param WanPort: 外网端口
        :type WanPort: int
        :param Pid: 产品类型 ID（过时字段，请勿依赖该值）
        :type Pid: int
        :param UpdateTime: 实例最后更新时间，格式为 2006-01-02 15:04:05
        :type UpdateTime: str
        :param DbEngine: 数据库引擎
        :type DbEngine: str
        :param DbVersion: 数据库引擎版本
        :type DbVersion: str
        :param Paymode: 付费模式
        :type Paymode: str
        :param Locker: 实例处于异步任务状态时，表示异步任务流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Locker: int
        :param WanStatus: 外网状态，0-未开通；1-已开通；2-关闭；3-开通中
        :type WanStatus: int
        :param IsAuditSupported: 该实例是否支持审计。1-支持；0-不支持
        :type IsAuditSupported: int
        :param Cpu: Cpu核数
        :type Cpu: int
        :param Ipv6Flag: 实例IPv6标志
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6Flag: int
        :param Vipv6: 内网IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type Vipv6: str
        :param WanVipv6: 外网IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type WanVipv6: str
        :param WanPortIpv6: 外网IPv6端口
注意：此字段可能返回 null，表示取不到有效值。
        :type WanPortIpv6: int
        :param WanStatusIpv6: 外网IPv6状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WanStatusIpv6: int
        :param DcnFlag: DCN标志，0-无，1-主实例，2-灾备实例
注意：此字段可能返回 null，表示取不到有效值。
        :type DcnFlag: int
        :param DcnStatus: DCN状态，0-无，1-创建中，2-同步中，3-已断开
注意：此字段可能返回 null，表示取不到有效值。
        :type DcnStatus: int
        :param DcnDstNum: DCN灾备实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type DcnDstNum: int
        :param InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: int
        :param ResourceTags: 实例标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of ResourceTag
        :param DbVersionId: 数据库引擎版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DbVersionId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.StatusDesc = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.AutoRenewFlag = None
        self.Memory = None
        self.Storage = None
        self.ShardCount = None
        self.PeriodEndTime = None
        self.IsolatedTimestamp = None
        self.Uin = None
        self.ShardDetail = None
        self.NodeCount = None
        self.IsTmp = None
        self.ExclusterId = None
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.Id = None
        self.WanDomain = None
        self.WanVip = None
        self.WanPort = None
        self.Pid = None
        self.UpdateTime = None
        self.DbEngine = None
        self.DbVersion = None
        self.Paymode = None
        self.Locker = None
        self.WanStatus = None
        self.IsAuditSupported = None
        self.Cpu = None
        self.Ipv6Flag = None
        self.Vipv6 = None
        self.WanVipv6 = None
        self.WanPortIpv6 = None
        self.WanStatusIpv6 = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.DcnDstNum = None
        self.InstanceType = None
        self.ResourceTags = None
        self.DbVersionId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.StatusDesc = params.get("StatusDesc")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardCount = params.get("ShardCount")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.IsolatedTimestamp = params.get("IsolatedTimestamp")
        self.Uin = params.get("Uin")
        if params.get("ShardDetail") is not None:
            self.ShardDetail = []
            for item in params.get("ShardDetail"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ShardDetail.append(obj)
        self.NodeCount = params.get("NodeCount")
        self.IsTmp = params.get("IsTmp")
        self.ExclusterId = params.get("ExclusterId")
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.Id = params.get("Id")
        self.WanDomain = params.get("WanDomain")
        self.WanVip = params.get("WanVip")
        self.WanPort = params.get("WanPort")
        self.Pid = params.get("Pid")
        self.UpdateTime = params.get("UpdateTime")
        self.DbEngine = params.get("DbEngine")
        self.DbVersion = params.get("DbVersion")
        self.Paymode = params.get("Paymode")
        self.Locker = params.get("Locker")
        self.WanStatus = params.get("WanStatus")
        self.IsAuditSupported = params.get("IsAuditSupported")
        self.Cpu = params.get("Cpu")
        self.Ipv6Flag = params.get("Ipv6Flag")
        self.Vipv6 = params.get("Vipv6")
        self.WanVipv6 = params.get("WanVipv6")
        self.WanPortIpv6 = params.get("WanPortIpv6")
        self.WanStatusIpv6 = params.get("WanStatusIpv6")
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.DcnDstNum = params.get("DcnDstNum")
        self.InstanceType = params.get("InstanceType")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DbVersionId = params.get("DbVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCDBShardInfo(AbstractModel):
    """描述分布式数据库分片信息。

    """

    def __init__(self):
        r"""
        :param InstanceId: 所属实例Id
        :type InstanceId: str
        :param ShardSerialId: 分片SQL透传Id，用于将sql透传到指定分片执行
        :type ShardSerialId: str
        :param ShardInstanceId: 全局唯一的分片Id
        :type ShardInstanceId: str
        :param Status: 状态：0 创建中，1 流程处理中， 2 运行中，3 分片未初始化
        :type Status: int
        :param StatusDesc: 状态中文描述
        :type StatusDesc: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param VpcId: 字符串格式的私有网络Id
        :type VpcId: str
        :param SubnetId: 字符串格式的私有网络子网Id
        :type SubnetId: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param Storage: 存储大小，单位 GB
        :type Storage: int
        :param PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param NodeCount: 节点数，2 为一主一从， 3 为一主二从
        :type NodeCount: int
        :param StorageUsage: 存储使用率，单位为 %
        :type StorageUsage: float
        :param MemoryUsage: 内存使用率，单位为 %
        :type MemoryUsage: float
        :param ShardId: 数字分片Id（过时字段，请勿依赖该值）
        :type ShardId: int
        :param Pid: 产品ProductID
        :type Pid: int
        :param ProxyVersion: Proxy版本
        :type ProxyVersion: str
        :param Paymode: 付费模型
注意：此字段可能返回 null，表示取不到有效值。
        :type Paymode: str
        :param ShardMasterZone: 分片的主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardMasterZone: str
        :param ShardSlaveZones: 分片的从可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ShardSlaveZones: list of str
        :param Cpu: CPU核数
        :type Cpu: int
        :param Range: 分片ShardKey的范围（总共64个哈希值），例如： 0-31，32-63
        :type Range: str
        """
        self.InstanceId = None
        self.ShardSerialId = None
        self.ShardInstanceId = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.PeriodEndTime = None
        self.NodeCount = None
        self.StorageUsage = None
        self.MemoryUsage = None
        self.ShardId = None
        self.Pid = None
        self.ProxyVersion = None
        self.Paymode = None
        self.ShardMasterZone = None
        self.ShardSlaveZones = None
        self.Cpu = None
        self.Range = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardSerialId = params.get("ShardSerialId")
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.NodeCount = params.get("NodeCount")
        self.StorageUsage = params.get("StorageUsage")
        self.MemoryUsage = params.get("MemoryUsage")
        self.ShardId = params.get("ShardId")
        self.Pid = params.get("Pid")
        self.ProxyVersion = params.get("ProxyVersion")
        self.Paymode = params.get("Paymode")
        self.ShardMasterZone = params.get("ShardMasterZone")
        self.ShardSlaveZones = params.get("ShardSlaveZones")
        self.Cpu = params.get("Cpu")
        self.Range = params.get("Range")
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
        r"""
        :param DbName: 数据库名称
        :type DbName: str
        """
        self.DbName = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseFunction(AbstractModel):
    """数据库函数信息

    """

    def __init__(self):
        r"""
        :param Func: 函数名称
        :type Func: str
        """
        self.Func = None


    def _deserialize(self, params):
        self.Func = params.get("Func")
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
        


class DatabaseProcedure(AbstractModel):
    """数据库存储过程信息

    """

    def __init__(self):
        r"""
        :param Proc: 存储过程名称
        :type Proc: str
        """
        self.Proc = None


    def _deserialize(self, params):
        self.Proc = params.get("Proc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTable(AbstractModel):
    """数据库表信息

    """

    def __init__(self):
        r"""
        :param Table: 表名
        :type Table: str
        """
        self.Table = None


    def _deserialize(self, params):
        self.Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseView(AbstractModel):
    """数据库视图信息

    """

    def __init__(self):
        r"""
        :param View: 视图名称
        :type View: str
        """
        self.View = None


    def _deserialize(self, params):
        self.View = params.get("View")
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
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Region: 实例地域
        :type Region: str
        :param Zone: 实例可用区
        :type Zone: str
        :param Vip: 实例IP地址
        :type Vip: str
        :param Vipv6: 实例IPv6地址
        :type Vipv6: str
        :param Vport: 实例端口
        :type Vport: int
        :param Status: 实例状态
        :type Status: int
        :param StatusDesc: 实例状态描述
        :type StatusDesc: str
        :param DcnFlag: 实例DCN标志，1-主，2-备
        :type DcnFlag: int
        :param DcnStatus: 实例DCN状态，0-无，1-创建中，2-同步中，3-已断开
        :type DcnStatus: int
        :param Cpu: 实例CPU核数
        :type Cpu: int
        :param Memory: 实例内存大小，单位 GB
        :type Memory: int
        :param Storage: 实例存储大小，单位 GB
        :type Storage: int
        :param PayMode: 付费模式
        :type PayMode: int
        :param CreateTime: 实例创建时间，格式为 2006-01-02 15:04:05
        :type CreateTime: str
        :param PeriodEndTime: 实例到期时间，格式为 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
        :type InstanceType: int
        :param EncryptStatus: 是否开启了 kms
        :type EncryptStatus: int
        """
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
        self.EncryptStatus = None


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
        self.EncryptStatus = params.get("EncryptStatus")
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
        r"""
        :param DealName: 订单号
        :type DealName: str
        :param OwnerUin: 所属账号
        :type OwnerUin: str
        :param Count: 商品数量
        :type Count: int
        :param FlowId: 关联的流程 Id，可用于查询流程执行状态
        :type FlowId: int
        :param InstanceIds: 只有创建实例且已完成发货的订单会填充该字段，表示该订单创建的实例的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param PayMode: 付费模式，0后付费/1预付费
        :type PayMode: int
        """
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
        r"""
        :param InstanceId: 实例ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UserName: 用户名
        :type UserName: str
        :param Host: 用户允许的访问 host
        :type Host: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param UserName: 登录用户名。
        :type UserName: str
        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param Type: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示查询该数据库权限（即db.\*），此时忽略 Object 参数
        :type Type: str
        :param Object: 具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :type Object: str
        :param ColName: 当 Type=table 时，ColName 为 \* 表示查询表的权限，如果为具体字段名，表示查询对应字段的权限
        :type ColName: str
        """
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
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Privileges: 权限列表。
        :type Privileges: list of str
        :param UserName: 数据库账号用户名
        :type UserName: str
        :param Host: 数据库账号Host
        :type Host: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 实例ID，形如：dcdbt-ow728lmc。
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
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，透传入参。
        :type InstanceId: str
        :param Users: 实例用户列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of DBAccount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeBackupFilesRequest(AbstractModel):
    """DescribeBackupFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 按实例ID查询
        :type InstanceId: str
        :param ShardId: 按分片ID查询
        :type ShardId: str
        :param BackupType: 备份类型，Data:数据备份，Binlog:Binlog备份，Errlog:错误日志，Slowlog:慢日志
        :type BackupType: str
        :param StartTime: 按开始时间查询
        :type StartTime: str
        :param EndTime: 按结束时间查询
        :type EndTime: str
        :param Limit: 分页参数
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param OrderBy: 排序参数，可选值：Time,Size
        :type OrderBy: str
        :param OrderType: 排序参数，可选值：DESC,ASC
        :type OrderType: str
        """
        self.InstanceId = None
        self.ShardId = None
        self.BackupType = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardId = params.get("ShardId")
        self.BackupType = params.get("BackupType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupFilesResponse(AbstractModel):
    """DescribeBackupFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param Files: 备份文件列表
        :type Files: list of InstanceBackupFileItem
        :param TotalCount: 总条目数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Files = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = InstanceBackupFileItem()
                obj._deserialize(item)
                self.Files.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDBEncryptAttributesRequest(AbstractModel):
    """DescribeDBEncryptAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id，形如：tdsqlshard-ow728lmc。
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
        


class DescribeDBEncryptAttributesResponse(AbstractModel):
    """DescribeDBEncryptAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param EncryptStatus: 是否启用加密，1-已开启；0-未开启。
        :type EncryptStatus: int
        :param CipherText: DEK密钥
        :type CipherText: str
        :param ExpireDate: DEK密钥过期日期。
        :type ExpireDate: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EncryptStatus = None
        self.CipherText = None
        self.ExpireDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EncryptStatus = params.get("EncryptStatus")
        self.CipherText = params.get("CipherText")
        self.ExpireDate = params.get("ExpireDate")
        self.RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param ShardId: 分片 ID，形如：shard-7noic7tv
        :type ShardId: str
        :param Type: 请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。
        :type Type: int
        """
        self.InstanceId = None
        self.ShardId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardId = params.get("ShardId")
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
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param Type: 请求日志类型。1-binlog，2-冷备，3-errlog，4-slowlog。
        :type Type: int
        :param Total: 请求日志总数
        :type Total: int
        :param Files: 日志文件列表
        :type Files: list of LogFileInfo
        :param VpcPrefix: 如果是VPC网络的实例，做用本前缀加上URI为下载地址
        :type VpcPrefix: str
        :param NormalPrefix: 如果是普通网络的实例，做用本前缀加上URI为下载地址
        :type NormalPrefix: str
        :param ShardId: 分片 ID，形如：shard-7noic7tv
        :type ShardId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Type = None
        self.Total = None
        self.Files = None
        self.VpcPrefix = None
        self.NormalPrefix = None
        self.ShardId = None
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
        self.ShardId = params.get("ShardId")
        self.RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
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
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param Params: 请求DB的当前参数值
        :type Params: list of ParamDesc
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param InstanceId: 实例ID。
        :type InstanceId: str
        """
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
        r"""
        :param Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param VIP: 实例VIP
注意：此字段可能返回 null，表示取不到有效值。
        :type VIP: str
        :param VPort: 实例端口
注意：此字段可能返回 null，表示取不到有效值。
        :type VPort: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-hw0qj6m1
        :type InstanceId: str
        :param Offset: 从结果的第几条数据开始返回
        :type Offset: int
        :param Limit: 返回的结果条数
        :type Limit: int
        :param StartTime: 查询的起始时间，形如2016-07-23 14:55:20
        :type StartTime: str
        :param ShardId: 实例的分片ID，形如shard-53ima8ln
        :type ShardId: str
        :param EndTime: 查询的结束时间，形如2016-08-22 14:55:20。如果不填，那么查询结束时间就是当前时间
        :type EndTime: str
        :param Db: 要查询的具体数据库名称
        :type Db: str
        :param OrderBy: 排序指标，取值为query_time_sum或者query_count。不填默认按照query_time_sum排序
        :type OrderBy: str
        :param OrderByType: 排序类型，desc（降序）或者asc（升序）。不填默认desc排序
        :type OrderByType: str
        :param Slave: 是否查询从机的慢查询，0-主机; 1-从机。不填默认查询主机慢查询
        :type Slave: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.ShardId = None
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
        self.ShardId = params.get("ShardId")
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
        r"""
        :param LockTimeSum: 所有语句锁时间总和
        :type LockTimeSum: float
        :param QueryCount: 所有语句查询总次数
        :type QueryCount: int
        :param Total: 总记录数
        :type Total: int
        :param QueryTimeSum: 所有语句查询时间总和
        :type QueryTimeSum: float
        :param Data: 慢查询日志数据
        :type Data: list of SlowLogData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LockTimeSum = None
        self.QueryCount = None
        self.Total = None
        self.QueryTimeSum = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LockTimeSum = params.get("LockTimeSum")
        self.QueryCount = params.get("QueryCount")
        self.Total = params.get("Total")
        self.QueryTimeSum = params.get("QueryTimeSum")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SlowLogData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSyncModeRequest(AbstractModel):
    """DescribeDBSyncMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待修改同步模式的实例ID。形如：dcdbt-ow728lmc。
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
        


class DescribeDBSyncModeResponse(AbstractModel):
    """DescribeDBSyncMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param SyncMode: 同步模式：0 异步，1 强同步， 2 强同步可退化
        :type SyncMode: int
        :param IsModifying: 是否有修改流程在执行中：1 是， 0 否。
        :type IsModifying: int
        :param CurrentSyncMode: 当前复制方式，0 异步，1 同步
        :type CurrentSyncMode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SyncMode = None
        self.IsModifying = None
        self.CurrentSyncMode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SyncMode = params.get("SyncMode")
        self.IsModifying = params.get("IsModifying")
        self.CurrentSyncMode = params.get("CurrentSyncMode")
        self.RequestId = params.get("RequestId")


class DescribeDCDBInstanceDetailRequest(AbstractModel):
    """DescribeDCDBInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，形如dcdbt-7oaxtcb7
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
        


class DescribeDCDBInstanceDetailResponse(AbstractModel):
    """DescribeDCDBInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，形如dcdbt-7oaxtcb7
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Status: 实例状态。0-实例创建中；1-异步任务处理中；2-运行中；3-实例未初始化；-1-实例已隔离
        :type Status: int
        :param StatusDesc: 实例目前运行状态描述
        :type StatusDesc: str
        :param Vip: 实例内网IP地址
        :type Vip: str
        :param Vport: 实例内网端口
        :type Vport: int
        :param NodeCount: 实例节点数。值为2时表示一主一从，值为3时表示一主二从
        :type NodeCount: int
        :param Region: 实例所在地域名称，形如ap-guangzhou
        :type Region: str
        :param VpcId: 实例私有网络ID，形如vpc-r9jr0de3
        :type VpcId: str
        :param SubnetId: 实例私有网络子网ID，形如subnet-6rqs61o2
        :type SubnetId: str
        :param WanStatus: 外网状态，0-未开通；1-已开通；2-关闭；3-开通中；4-关闭中
        :type WanStatus: int
        :param WanDomain: 外网访问的域名，公网可解析
        :type WanDomain: str
        :param WanVip: 外网IP地址，公网可访问
        :type WanVip: str
        :param WanPort: 外网访问端口
        :type WanPort: int
        :param ProjectId: 实例所属项目ID
        :type ProjectId: int
        :param AutoRenewFlag: 实例自动续费标志。0-正常续费；1-自动续费；2-到期不续费
        :type AutoRenewFlag: int
        :param ExclusterId: 独享集群ID
        :type ExclusterId: str
        :param PayMode: 付费模式。prepaid-预付费；postpaid-按量计费
        :type PayMode: str
        :param CreateTime: 实例创建时间，格式为 2006-01-02 15:04:05
        :type CreateTime: str
        :param PeriodEndTime: 实例到期时间，格式为 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param DbVersion: 数据库版本信息
        :type DbVersion: str
        :param IsAuditSupported: 实例是否支持审计。0-不支持；1-支持
        :type IsAuditSupported: int
        :param IsEncryptSupported: 实例是否支持数据加密。0-不支持；1-支持
        :type IsEncryptSupported: int
        :param Machine: 实例母机机器型号
        :type Machine: str
        :param Memory: 实例内存大小，单位 GB，各个分片的内存大小的和
        :type Memory: int
        :param Storage: 实例磁盘存储大小，单位 GB，各个分片的磁盘大小的和
        :type Storage: int
        :param StorageUsage: 实例存储空间使用率，计算方式为：各个分片已经使用的磁盘大小的和/各个分片的磁盘大小的和。
        :type StorageUsage: float
        :param LogStorage: 日志存储空间大小，单位GB
        :type LogStorage: int
        :param Pid: 产品类型ID
        :type Pid: int
        :param MasterZone: 主DB可用区
        :type MasterZone: str
        :param SlaveZones: 从DB可用区
        :type SlaveZones: list of str
        :param Shards: 分片信息
        :type Shards: list of ShardBriefInfo
        :param Vip6: 内网IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip6: str
        :param Cpu: 实例Cpu核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Qps: 实例QPS
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        :param DbEngine: DB引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type DbEngine: str
        :param Ipv6Flag: 是否支持IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6Flag: int
        :param WanVipv6: 外网IPv6地址，公网可访问
注意：此字段可能返回 null，表示取不到有效值。
        :type WanVipv6: str
        :param WanStatusIpv6: 外网状态，0-未开通；1-已开通；2-关闭；3-开通中；4-关闭中
注意：此字段可能返回 null，表示取不到有效值。
        :type WanStatusIpv6: int
        :param WanPortIpv6: 外网IPv6端口
注意：此字段可能返回 null，表示取不到有效值。
        :type WanPortIpv6: int
        :param ResourceTags: 标签信息
        :type ResourceTags: list of ResourceTag
        :param DcnFlag: DCN标志，0-无，1-主实例，2-灾备实例
注意：此字段可能返回 null，表示取不到有效值。
        :type DcnFlag: int
        :param DcnStatus: DCN状态，0-无，1-创建中，2-同步中，3-已断开
注意：此字段可能返回 null，表示取不到有效值。
        :type DcnStatus: int
        :param DcnDstNum: DCN灾备实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type DcnDstNum: int
        :param InstanceType: 1： 主实例（独享型）, 2: 主实例, 3： 灾备实例, 4： 灾备实例（独享型）
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: int
        :param IsMaxUserConnectionsSupported: 实例是否支持设置用户连接数限制，内核为10.1暂不支持。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMaxUserConnectionsSupported: bool
        :param DbVersionId: 对外显示的数据库版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DbVersionId: str
        :param EncryptStatus: 加密状态, 0-未开启，1-已开启
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptStatus: int
        :param ExclusterType: 独享集群类型，0:公有云, 1:金融围笼, 2:CDC集群
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusterType: int
        :param RsAccessStrategy: VPC就近访问
注意：此字段可能返回 null，表示取不到有效值。
        :type RsAccessStrategy: int
        :param ReservedNetResources: 尚未回收的网络资源
        :type ReservedNetResources: list of ReservedNetResource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.StatusDesc = None
        self.Vip = None
        self.Vport = None
        self.NodeCount = None
        self.Region = None
        self.VpcId = None
        self.SubnetId = None
        self.WanStatus = None
        self.WanDomain = None
        self.WanVip = None
        self.WanPort = None
        self.ProjectId = None
        self.AutoRenewFlag = None
        self.ExclusterId = None
        self.PayMode = None
        self.CreateTime = None
        self.PeriodEndTime = None
        self.DbVersion = None
        self.IsAuditSupported = None
        self.IsEncryptSupported = None
        self.Machine = None
        self.Memory = None
        self.Storage = None
        self.StorageUsage = None
        self.LogStorage = None
        self.Pid = None
        self.MasterZone = None
        self.SlaveZones = None
        self.Shards = None
        self.Vip6 = None
        self.Cpu = None
        self.Qps = None
        self.DbEngine = None
        self.Ipv6Flag = None
        self.WanVipv6 = None
        self.WanStatusIpv6 = None
        self.WanPortIpv6 = None
        self.ResourceTags = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.DcnDstNum = None
        self.InstanceType = None
        self.IsMaxUserConnectionsSupported = None
        self.DbVersionId = None
        self.EncryptStatus = None
        self.ExclusterType = None
        self.RsAccessStrategy = None
        self.ReservedNetResources = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.NodeCount = params.get("NodeCount")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.WanStatus = params.get("WanStatus")
        self.WanDomain = params.get("WanDomain")
        self.WanVip = params.get("WanVip")
        self.WanPort = params.get("WanPort")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ExclusterId = params.get("ExclusterId")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.DbVersion = params.get("DbVersion")
        self.IsAuditSupported = params.get("IsAuditSupported")
        self.IsEncryptSupported = params.get("IsEncryptSupported")
        self.Machine = params.get("Machine")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.StorageUsage = params.get("StorageUsage")
        self.LogStorage = params.get("LogStorage")
        self.Pid = params.get("Pid")
        self.MasterZone = params.get("MasterZone")
        self.SlaveZones = params.get("SlaveZones")
        if params.get("Shards") is not None:
            self.Shards = []
            for item in params.get("Shards"):
                obj = ShardBriefInfo()
                obj._deserialize(item)
                self.Shards.append(obj)
        self.Vip6 = params.get("Vip6")
        self.Cpu = params.get("Cpu")
        self.Qps = params.get("Qps")
        self.DbEngine = params.get("DbEngine")
        self.Ipv6Flag = params.get("Ipv6Flag")
        self.WanVipv6 = params.get("WanVipv6")
        self.WanStatusIpv6 = params.get("WanStatusIpv6")
        self.WanPortIpv6 = params.get("WanPortIpv6")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.DcnDstNum = params.get("DcnDstNum")
        self.InstanceType = params.get("InstanceType")
        self.IsMaxUserConnectionsSupported = params.get("IsMaxUserConnectionsSupported")
        self.DbVersionId = params.get("DbVersionId")
        self.EncryptStatus = params.get("EncryptStatus")
        self.ExclusterType = params.get("ExclusterType")
        self.RsAccessStrategy = params.get("RsAccessStrategy")
        if params.get("ReservedNetResources") is not None:
            self.ReservedNetResources = []
            for item in params.get("ReservedNetResources"):
                obj = ReservedNetResource()
                obj._deserialize(item)
                self.ReservedNetResources.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBInstanceNodeInfoRequest(AbstractModel):
    """DescribeDCDBInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Limit: 单次最多返回多少条，取值范围为(0-100]，默认为100
        :type Limit: int
        :param Offset: 返回数据的偏移值，默认为0
        :type Offset: int
        """
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
        


class DescribeDCDBInstanceNodeInfoResponse(AbstractModel):
    """DescribeDCDBInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 节点总个数
        :type TotalCount: int
        :param NodesInfo: 节点信息
        :type NodesInfo: list of BriefNodeInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NodesInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NodesInfo") is not None:
            self.NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = BriefNodeInfo()
                obj._deserialize(item)
                self.NodesInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBInstancesRequest(AbstractModel):
    """DescribeDCDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 按照一个或者多个实例 ID 查询。实例 ID 形如：dcdbt-2t4cf98d
        :type InstanceIds: list of str
        :param SearchName: 搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。
        :type SearchName: str
        :param SearchKey: 搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\n'）分割。
        :type SearchKey: str
        :param ProjectIds: 按项目 ID 查询
        :type ProjectIds: list of int
        :param IsFilterVpc: 是否根据 VPC 网络来搜索
        :type IsFilterVpc: bool
        :param VpcId: 私有网络 ID， IsFilterVpc 为 1 时有效
        :type VpcId: str
        :param SubnetId: 私有网络的子网 ID， IsFilterVpc 为 1 时有效
        :type SubnetId: str
        :param OrderBy: 排序字段， projectId， createtime， instancename 三者之一
        :type OrderBy: str
        :param OrderByType: 排序类型， desc 或者 asc
        :type OrderByType: str
        :param Offset: 偏移量，默认为 0
        :type Offset: int
        :param Limit: 返回数量，默认为 10，最大值为 100。
        :type Limit: int
        :param ExclusterType: 1非独享集群，2独享集群， 0全部
        :type ExclusterType: int
        :param IsFilterExcluster: 标识是否使用ExclusterType字段, false不使用，true使用
        :type IsFilterExcluster: bool
        :param ExclusterIds: 独享集群ID
        :type ExclusterIds: list of str
        :param TagKeys: 按标签key查询
        :type TagKeys: list of str
        :param FilterInstanceType: 实例类型过滤，1-独享实例，2-主实例，3-灾备实例，多个按逗号分隔
        :type FilterInstanceType: str
        :param Status: 按实例状态筛选
        :type Status: list of int
        :param ExcludeStatus: 排除实例状态
        :type ExcludeStatus: list of int
        """
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
        self.ExclusterType = None
        self.IsFilterExcluster = None
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
        self.ExclusterType = params.get("ExclusterType")
        self.IsFilterExcluster = params.get("IsFilterExcluster")
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
        


class DescribeDCDBInstancesResponse(AbstractModel):
    """DescribeDCDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的实例数量
        :type TotalCount: int
        :param Instances: 实例详细信息列表
        :type Instances: list of DCDBInstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DCDBInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBPriceRequest(AbstractModel):
    """DescribeDCDBPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 欲新购实例的可用区ID。
        :type Zone: str
        :param Count: 欲购买实例的数量，目前支持购买1-10个实例
        :type Count: int
        :param Period: 欲购买的时长，单位：月。
        :type Period: int
        :param ShardNodeCount: 单个分片节点个数大小，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardNodeCount: int
        :param ShardMemory: 分片内存大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardMemory: int
        :param ShardStorage: 分片存储空间大小，单位：GB，可以通过 DescribeShardSpec
 查询实例规格获得。
        :type ShardStorage: int
        :param ShardCount: 实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。
        :type ShardCount: int
        :param Paymode: 付费类型。postpaid：按量付费   prepaid：预付费
        :type Paymode: str
        :param AmountUnit: 价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :type AmountUnit: str
        """
        self.Zone = None
        self.Count = None
        self.Period = None
        self.ShardNodeCount = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardCount = None
        self.Paymode = None
        self.AmountUnit = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Count = params.get("Count")
        self.Period = params.get("Period")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardCount = params.get("ShardCount")
        self.Paymode = params.get("Paymode")
        self.AmountUnit = params.get("AmountUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBPriceResponse(AbstractModel):
    """DescribeDCDBPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginalPrice: 原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :type OriginalPrice: int
        :param Price: 实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
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


class DescribeDCDBRenewalPriceRequest(AbstractModel):
    """DescribeDCDBRenewalPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Period: 续费时长，单位：月。不传则默认为1个月。
        :type Period: int
        :param AmountUnit: 价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :type AmountUnit: str
        """
        self.InstanceId = None
        self.Period = None
        self.AmountUnit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.AmountUnit = params.get("AmountUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBRenewalPriceResponse(AbstractModel):
    """DescribeDCDBRenewalPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginalPrice: 原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :type OriginalPrice: int
        :param Price: 实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
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


class DescribeDCDBSaleInfoRequest(AbstractModel):
    """DescribeDCDBSaleInfo请求参数结构体

    """


class DescribeDCDBSaleInfoResponse(AbstractModel):
    """DescribeDCDBSaleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionList: 可售卖地域信息列表
        :type RegionList: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeDCDBShardsRequest(AbstractModel):
    """DescribeDCDBShards请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param ShardInstanceIds: 分片ID列表。
        :type ShardInstanceIds: list of str
        :param Offset: 偏移量，默认为 0
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param OrderBy: 排序字段， 目前仅支持 createtime
        :type OrderBy: str
        :param OrderByType: 排序类型， desc 或者 asc
        :type OrderByType: str
        """
        self.InstanceId = None
        self.ShardInstanceIds = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBShardsResponse(AbstractModel):
    """DescribeDCDBShards返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的分片数量
        :type TotalCount: int
        :param Shards: 分片信息列表
        :type Shards: list of DCDBShardInfo
        :param DcnFlag: 灾备标志，0-无，1-主实例，2-灾备实例
注意：此字段可能返回 null，表示取不到有效值。
        :type DcnFlag: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Shards = None
        self.DcnFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Shards") is not None:
            self.Shards = []
            for item in params.get("Shards"):
                obj = DCDBShardInfo()
                obj._deserialize(item)
                self.Shards.append(obj)
        self.DcnFlag = params.get("DcnFlag")
        self.RequestId = params.get("RequestId")


class DescribeDCDBUpgradePriceRequest(AbstractModel):
    """DescribeDCDBUpgradePrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param AmountUnit: 价格金额单位，不传默认单位为分，取值：  
* pent：分
* microPent：微分
        :type AmountUnit: str
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None
        self.AmountUnit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self.AmountUnit = params.get("AmountUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBUpgradePriceResponse(AbstractModel):
    """DescribeDCDBUpgradePrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginalPrice: 原价  
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站为人民币，国际站为美元
        :type OriginalPrice: int
        :param Price: 实际价格，受折扣等影响，可能和原价不同
* 单位：默认为分，若请求参数带有AmountUnit，参考AmountUnit描述
* 币种：国内站人民币，国际站美元
        :type Price: int
        :param Formula: 变配明细计算公式
        :type Formula: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.Formula = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.Formula = params.get("Formula")
        self.RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    """DescribeDatabaseObjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param DbName: 数据库名称，通过 DescribeDatabases 接口获取。
        :type DbName: str
        """
        self.InstanceId = None
        self.DbName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    """DescribeDatabaseObjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 透传入参。
        :type InstanceId: str
        :param DbName: 数据库名称。
        :type DbName: str
        :param Tables: 表列表。
        :type Tables: list of DatabaseTable
        :param Views: 视图列表。
        :type Views: list of DatabaseView
        :param Procs: 存储过程列表。
        :type Procs: list of DatabaseProcedure
        :param Funcs: 函数列表。
        :type Funcs: list of DatabaseFunction
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Tables = None
        self.Views = None
        self.Procs = None
        self.Funcs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self.Tables.append(obj)
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self.Views.append(obj)
        if params.get("Procs") is not None:
            self.Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self.Procs.append(obj)
        if params.get("Funcs") is not None:
            self.Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self.Funcs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabaseTableRequest(AbstractModel):
    """DescribeDatabaseTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param DbName: 数据库名称，通过 DescribeDatabases 接口获取。
        :type DbName: str
        :param Table: 表名称，通过 DescribeDatabaseObjects 接口获取。
        :type Table: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Table = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        self.Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseTableResponse(AbstractModel):
    """DescribeDatabaseTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例名称。
        :type InstanceId: str
        :param DbName: 数据库名称。
        :type DbName: str
        :param Table: 表名称。
        :type Table: str
        :param Cols: 列信息。
        :type Cols: list of TableColumn
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Table = None
        self.Cols = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        self.Table = params.get("Table")
        if params.get("Cols") is not None:
            self.Cols = []
            for item in params.get("Cols"):
                obj = TableColumn()
                obj._deserialize(item)
                self.Cols.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow7t8lmc。
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
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param Databases: 该实例上的数据库列表。
        :type Databases: list of Database
        :param InstanceId: 透传入参。
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 实例ID
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
        


class DescribeDcnDetailResponse(AbstractModel):
    """DescribeDcnDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param DcnDetails: DCN同步详情
        :type DcnDetails: list of DcnDetailItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeFileDownloadUrlRequest(AbstractModel):
    """DescribeFileDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ShardId: 实例分片ID
        :type ShardId: str
        :param FilePath: 不带签名的文件路径
        :type FilePath: str
        """
        self.InstanceId = None
        self.ShardId = None
        self.FilePath = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardId = params.get("ShardId")
        self.FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileDownloadUrlResponse(AbstractModel):
    """DescribeFileDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param PreSignedUrl: 带签名的下载连接
        :type PreSignedUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PreSignedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedUrl = params.get("PreSignedUrl")
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步请求接口返回的任务流程号。
        :type FlowId: int
        """
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
        r"""
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


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        r"""
        :param DealNames: 待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。
        :type DealNames: list of str
        """
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
        r"""
        :param TotalCount: 返回的订单数量。
        :type TotalCount: int
        :param Deals: 订单信息列表。
        :type Deals: list of Deal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        """
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
        r"""
        :param Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param Total: 安全组个数。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param Projects: 项目列表
        :type Projects: list of Project
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Projects = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShardSpecRequest(AbstractModel):
    """DescribeShardSpec请求参数结构体

    """


class DescribeShardSpecResponse(AbstractModel):
    """DescribeShardSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpecConfig: 按机型分类的可售卖规格列表
        :type SpecConfig: list of SpecConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpecConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecConfig") is not None:
            self.SpecConfig = []
            for item in params.get("SpecConfig"):
                obj = SpecConfig()
                obj._deserialize(item)
                self.SpecConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSqlLogsRequest(AbstractModel):
    """DescribeSqlLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Offset: SQL日志偏移。
        :type Offset: int
        :param Limit: 拉取数量（0-10000，为0时拉取总数信息）。
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
        


class DescribeSqlLogsResponse(AbstractModel):
    """DescribeSqlLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 当前消息队列中的sql日志条目数。
        :type TotalCount: int
        :param StartOffset: 消息队列中的sql日志起始偏移。
        :type StartOffset: int
        :param EndOffset: 消息队列中的sql日志结束偏移。
        :type EndOffset: int
        :param Offset: 返回的第一条sql日志的偏移。
        :type Offset: int
        :param Count: 返回的sql日志数量。
        :type Count: int
        :param SqlItems: Sql日志列表。
        :type SqlItems: list of SqlLogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeUserTasksRequest(AbstractModel):
    """DescribeUserTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Statuses: 任务的状态列表。0-任务启动中；1-任务运行中；2-任务成功；3-任务失败
        :type Statuses: list of int
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param FlowTypes: 任务类型列表，当前支持的任务类型有：0-回档任务；1-创建实例任务；2-扩容任务；3-迁移任务；4-删除实例任务；5-重启任务
        :type FlowTypes: list of int
        :param StartTime: 任务的创建时间
        :type StartTime: str
        :param EndTime: 任务的结束时间
        :type EndTime: str
        :param UTaskIds: 任务ID的数组
        :type UTaskIds: list of int
        :param Limit: 每次最多返回多少条任务，取值范围为(0,100]，不传的话默认值为20
        :type Limit: int
        :param Offset: 返回任务默认是按照创建时间降序排列，从偏移值Offset处开始返回
        :type Offset: int
        """
        self.Statuses = None
        self.InstanceIds = None
        self.FlowTypes = None
        self.StartTime = None
        self.EndTime = None
        self.UTaskIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Statuses = params.get("Statuses")
        self.InstanceIds = params.get("InstanceIds")
        self.FlowTypes = params.get("FlowTypes")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UTaskIds = params.get("UTaskIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserTasksResponse(AbstractModel):
    """DescribeUserTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 任务总数
        :type TotalCount: int
        :param FlowSet: 任务列表
        :type FlowSet: list of UserTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.FlowSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("FlowSet") is not None:
            self.FlowSet = []
            for item in params.get("FlowSet"):
                obj = UserTaskInfo()
                obj._deserialize(item)
                self.FlowSet.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyDCDBInstanceRequest(AbstractModel):
    """DestroyDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
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
        


class DestroyDCDBInstanceResponse(AbstractModel):
    """DestroyDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，与入参InstanceId一致。
        :type InstanceId: str
        :param FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/557/56485)。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DestroyHourDCDBInstanceRequest(AbstractModel):
    """DestroyHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
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
        


class DestroyHourDCDBInstanceResponse(AbstractModel):
    """DestroyHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/557/56485)。
        :type FlowId: int
        :param InstanceId: 实例 ID，与入参InstanceId一致。
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param SecurityGroupId: 安全组Id。
        :type SecurityGroupId: str
        :param InstanceIds: 实例ID列表，一个或者多个实例Id组成的数组。
        :type InstanceIds: list of str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExpandShardConfig(AbstractModel):
    """升级实例 -- 扩容分片类型

    """

    def __init__(self):
        r"""
        :param ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        :param ShardNodeCount: 分片节点数
        :type ShardNodeCount: int
        """
        self.ShardInstanceIds = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardNodeCount = None


    def _deserialize(self, params):
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardNodeCount = params.get("ShardNodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlushBinlogRequest(AbstractModel):
    """FlushBinlog请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
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
        


class FlushBinlogResponse(AbstractModel):
    """FlushBinlog返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param UserName: 登录用户名。
        :type UserName: str
        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param Privileges: 全局权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES，REPLICATION CLIENT，REPLICATION SLAVE
库权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER 
表权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER  
字段权限： INSERT，REFERENCES，SELECT，UPDATE
        :type Privileges: list of str
        :param Type: 类型,可以填入 table 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示设置该数据库权限（即db.\*），此时忽略 Object 参数
        :type Type: str
        :param Object: 具体的 Type 的名称，例如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :type Object: str
        :param ColName: 当 Type=table 时，ColName 为 \* 表示对表授权，如果为具体字段名，表示对字段授权
        :type ColName: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDCDBInstancesRequest(AbstractModel):
    """InitDCDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 待初始化的实例ID列表，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceIds: list of str
        :param Params: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传，0 - 敏感；1-不敏感），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步）。
        :type Params: list of DBParamValue
        """
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
        


class InitDCDBInstancesResponse(AbstractModel):
    """InitDCDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowIds: 异步任务ID，可通过 DescribeFlow 查询任务状态。
        :type FlowIds: list of int non-negative
        :param InstanceIds: 透传入参。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class InstanceBackupFileItem(AbstractModel):
    """实例备份文件信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param InstanceStatus: 实例状态
        :type InstanceStatus: int
        :param ShardId: 分片ID
        :type ShardId: str
        :param FilePath: 文件路径
        :type FilePath: str
        :param FileName: 文件名
        :type FileName: str
        :param FileSize: 文件大小
        :type FileSize: int
        :param BackupType: 备份类型，Data:数据备份，Binlog:Binlog备份，Errlog:错误日志，Slowlog:慢日志
        :type BackupType: str
        :param ManualBackup: 手动备份，0:否，1:是
        :type ManualBackup: int
        :param StartTime: 备份开始时间
        :type StartTime: str
        :param EndTime: 备份结束时间
        :type EndTime: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceStatus = None
        self.ShardId = None
        self.FilePath = None
        self.FileName = None
        self.FileSize = None
        self.BackupType = None
        self.ManualBackup = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceStatus = params.get("InstanceStatus")
        self.ShardId = params.get("ShardId")
        self.FilePath = params.get("FilePath")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.BackupType = params.get("BackupType")
        self.ManualBackup = params.get("ManualBackup")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDCDBInstanceRequest(AbstractModel):
    """IsolateDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID，格式如：tdsqlshard-avw0207d，与云数据库控制台页面中显示的实例 ID 相同，可使用 查询实例列表 接口获取，其值为输出参数中字段 InstanceId 的值。
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
        


class IsolateDCDBInstanceResponse(AbstractModel):
    """IsolateDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessInstanceIds: 隔离成功实例ID列表。
        :type SuccessInstanceIds: list of str
        :param FailedInstanceIds: 隔离失败实例ID列表。
        :type FailedInstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessInstanceIds = None
        self.FailedInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessInstanceIds = params.get("SuccessInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.RequestId = params.get("RequestId")


class IsolateDedicatedDBInstanceRequest(AbstractModel):
    """IsolateDedicatedDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 Id，形如：dcdbt-ow728lmc。
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
        


class IsolateDedicatedDBInstanceResponse(AbstractModel):
    """IsolateDedicatedDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IsolateHourDCDBInstanceRequest(AbstractModel):
    """IsolateHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 待升级的实例ID列表。形如：["dcdbt-ow728lmc"]，可以通过 DescribeDCDBInstances 查询实例详情获得。
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
        


class IsolateHourDCDBInstanceResponse(AbstractModel):
    """IsolateHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessInstanceIds: 隔离成功的实例id列表
        :type SuccessInstanceIds: list of str
        :param FailedInstanceIds: 隔离失败的实例id列表
        :type FailedInstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessInstanceIds = None
        self.FailedInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessInstanceIds = params.get("SuccessInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.RequestId = params.get("RequestId")


class KillSessionRequest(AbstractModel):
    """KillSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param SessionId: 会话ID列表
        :type SessionId: list of int
        :param ShardId: 分片ID，与ShardSerialId设置一个
        :type ShardId: str
        :param ShardSerialId: 分片序列ID，与ShardId设置一个
        :type ShardSerialId: str
        """
        self.InstanceId = None
        self.SessionId = None
        self.ShardId = None
        self.ShardSerialId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SessionId = params.get("SessionId")
        self.ShardId = params.get("ShardId")
        self.ShardSerialId = params.get("ShardSerialId")
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
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """拉取的日志信息

    """

    def __init__(self):
        r"""
        :param Mtime: Log最后修改时间
        :type Mtime: int
        :param Length: 文件长度
        :type Length: int
        :param Uri: 下载Log时用到的统一资源标识符
        :type Uri: str
        :param FileName: 文件名
        :type FileName: str
        """
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
        


class ModifyAccountConfigRequest(AbstractModel):
    """ModifyAccountConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：tdsqlshard-kpkvq5oj，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param UserName: 账号的名称
        :type UserName: str
        :param Host: 账号的域名
        :type Host: str
        :param Configs: 配置列表，每一个元素是Config和Value的组合
        :type Configs: list of ConfigValue
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Configs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = ConfigValue()
                obj._deserialize(item)
                self.Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountConfigResponse(AbstractModel):
    """ModifyAccountConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param UserName: 登录用户名。
        :type UserName: str
        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param Description: 新的账号备注，长度 0~256。
        :type Description: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：tdsql-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param Accounts: 数据库的账号，包括用户名和域名。
        :type Accounts: list of Account
        :param GlobalPrivileges: 全局权限。其中，GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，该字段传空数组。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 数据库的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: 数据库中表的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: 数据库表中列的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param ViewPrivileges: 数据库视图的权限。Privileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组。
        :type ViewPrivileges: list of ViewPrivileges
        """
        self.InstanceId = None
        self.Accounts = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.ViewPrivileges = None


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
        :param FlowId: 异步任务的请求 ID，可使用此 ID [查询异步任务的执行结果](https://cloud.tencent.com/document/product/237/16177)。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDBEncryptAttributesRequest(AbstractModel):
    """ModifyDBEncryptAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id，形如：tdsqlshard-ow728lmc。
        :type InstanceId: str
        :param EncryptEnabled: 是否启用数据加密，开启后暂不支持关闭。本接口的可选值为：1-开启数据加密。
        :type EncryptEnabled: int
        """
        self.InstanceId = None
        self.EncryptEnabled = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EncryptEnabled = params.get("EncryptEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBEncryptAttributesResponse(AbstractModel):
    """ModifyDBEncryptAttributes返回参数结构体

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
        :param InstanceId: 实例ID，形如tdsql-hdaprz0v
        :type InstanceId: str
        :param InstanceName: 实例名称
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
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称，本接口取值：dcdb。
        :type Product: str
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param SecurityGroupIds: 要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 待修改的实例ID列表。实例 ID 形如：dcdbt-ow728lmc。
        :type InstanceIds: list of str
        :param ProjectId: 要分配的项目 ID，可以通过 DescribeProjects 查询项目列表接口获取。
        :type ProjectId: int
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param Params: 参数列表，每一个元素是Param和Value的组合
        :type Params: list of DBParamValue
        """
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
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param Result: 各参数修改结果
        :type Result: list of ParamModifyResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class ModifyDBSyncModeRequest(AbstractModel):
    """ModifyDBSyncMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待修改同步模式的实例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param SyncMode: 同步模式：0 异步，1 强同步， 2 强同步可退化
        :type SyncMode: int
        """
        self.InstanceId = None
        self.SyncMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSyncModeResponse(AbstractModel):
    """ModifyDBSyncMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务Id，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceNetworkRequest(AbstractModel):
    """ModifyInstanceNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param VpcId: 希望转到的VPC网络的VpcId
        :type VpcId: str
        :param SubnetId: 希望转到的VPC网络的子网ID
        :type SubnetId: str
        :param Vip: 如果需要指定VIP，填上该字段
        :type Vip: str
        :param Vipv6: 如果需要指定VIPv6，填上该字段
        :type Vipv6: str
        :param VipReleaseDelay: VIP保留时长，单位小时，取值范围（0~168），0表示立即释放，有一分钟释放延迟。不传此参数，默认24小时释放VIP。
        :type VipReleaseDelay: int
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vipv6 = None
        self.VipReleaseDelay = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vipv6 = params.get("Vipv6")
        self.VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNetworkResponse(AbstractModel):
    """ModifyInstanceNetwork返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务ID，根据此FlowId通过DescribeFlow接口查询任务进行状态
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceVipRequest(AbstractModel):
    """ModifyInstanceVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Vip: 实例VIP
        :type Vip: str
        :param Ipv6Flag: IPv6标志
        :type Ipv6Flag: int
        :param VipReleaseDelay: VIP保留时长，单位小时，取值范围（0~168），0表示立即释放，有一分钟释放延迟。不传此参数，默认24小时释放VIP。
        :type VipReleaseDelay: int
        """
        self.InstanceId = None
        self.Vip = None
        self.Ipv6Flag = None
        self.VipReleaseDelay = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Vip = params.get("Vip")
        self.Ipv6Flag = params.get("Ipv6Flag")
        self.VipReleaseDelay = params.get("VipReleaseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVipResponse(AbstractModel):
    """ModifyInstanceVip返回参数结构体

    """

    def __init__(self):
        r"""
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


class ModifyInstanceVportRequest(AbstractModel):
    """ModifyInstanceVport请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Vport: 实例VPORT
        :type Vport: int
        """
        self.InstanceId = None
        self.Vport = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceVportResponse(AbstractModel):
    """ModifyInstanceVport返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRealServerAccessStrategyRequest(AbstractModel):
    """ModifyRealServerAccessStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，格式如：tdsqlshard-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。
        :type InstanceId: str
        :param RsAccessStrategy: RS就近模式, 0-无策略, 1-可用区就近访问。
        :type RsAccessStrategy: int
        """
        self.InstanceId = None
        self.RsAccessStrategy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RsAccessStrategy = params.get("RsAccessStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRealServerAccessStrategyResponse(AbstractModel):
    """ModifyRealServerAccessStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NodeInfo(AbstractModel):
    """描述DB节点信息

    """

    def __init__(self):
        r"""
        :param NodeId: DB节点ID
        :type NodeId: str
        :param Role: DB节点角色，取值为master或者slave
        :type Role: str
        """
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
        r"""
        :param InstanceId: 待开放外网访问的实例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param Ipv6Flag: 是否IPv6，默认0
        :type Ipv6Flag: int
        """
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
        r"""
        :param FlowId: 异步任务ID，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ParamConstraint(AbstractModel):
    """参数约束

    """

    def __init__(self):
        r"""
        :param Type: 约束类型,如枚举enum，区间section
        :type Type: str
        :param Enum: 约束类型为enum时的可选值列表
        :type Enum: str
        :param Range: 约束类型为section时的范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: :class:`tencentcloud.dcdb.v20180411.models.ConstraintRange`
        :param String: 约束类型为string时的可选值列表
        :type String: str
        """
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
        r"""
        :param Param: 参数名字
        :type Param: str
        :param Value: 当前参数值
        :type Value: str
        :param SetValue: 设置过的值，参数生效后，该值和value一样。未设置过就不返回该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type SetValue: str
        :param Default: 系统默认值
        :type Default: str
        :param Constraint: 参数限制
        :type Constraint: :class:`tencentcloud.dcdb.v20180411.models.ParamConstraint`
        :param HaveSetValue: 是否有设置过值，false:没有设置过值，true:有设置过值。
        :type HaveSetValue: bool
        :param NeedRestart: 是否需要重启生效，false:不需要重启，
true:需要重启
        :type NeedRestart: bool
        """
        self.Param = None
        self.Value = None
        self.SetValue = None
        self.Default = None
        self.Constraint = None
        self.HaveSetValue = None
        self.NeedRestart = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        self.SetValue = params.get("SetValue")
        self.Default = params.get("Default")
        if params.get("Constraint") is not None:
            self.Constraint = ParamConstraint()
            self.Constraint._deserialize(params.get("Constraint"))
        self.HaveSetValue = params.get("HaveSetValue")
        self.NeedRestart = params.get("NeedRestart")
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
        r"""
        :param Param: 修改参数名字
        :type Param: str
        :param Code: 参数修改结果。0表示修改成功；-1表示修改失败；-2表示该参数值非法
        :type Code: int
        """
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
        


class Project(AbstractModel):
    """项目信息描述

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param OwnerUin: 资源拥有者（主账号）uin
        :type OwnerUin: int
        :param AppId: 应用Id
        :type AppId: int
        :param Name: 项目名称
        :type Name: str
        :param CreatorUin: 创建者uin
        :type CreatorUin: int
        :param SrcPlat: 来源平台
        :type SrcPlat: str
        :param SrcAppId: 来源AppId
        :type SrcAppId: int
        :param Status: 项目状态,0正常，-1关闭。默认项目为3
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param IsDefault: 是否默认项目，1 是，0 不是
        :type IsDefault: int
        :param Info: 描述信息
        :type Info: str
        """
        self.ProjectId = None
        self.OwnerUin = None
        self.AppId = None
        self.Name = None
        self.CreatorUin = None
        self.SrcPlat = None
        self.SrcAppId = None
        self.Status = None
        self.CreateTime = None
        self.IsDefault = None
        self.Info = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.CreatorUin = params.get("CreatorUin")
        self.SrcPlat = params.get("SrcPlat")
        self.SrcAppId = params.get("SrcAppId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.IsDefault = params.get("IsDefault")
        self.Info = params.get("Info")
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
        r"""
        :param Region: 地域英文ID
        :type Region: str
        :param RegionId: 地域数字ID
        :type RegionId: int
        :param RegionName: 地域中文名
        :type RegionName: str
        :param ZoneList: 可用区列表
        :type ZoneList: list of ZonesInfo
        :param AvailableChoice: 可选择的主可用区和从可用区
        :type AvailableChoice: list of ShardZoneChooseInfo
        """
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
                obj = ShardZoneChooseInfo()
                obj._deserialize(item)
                self.AvailableChoice.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDCDBInstanceRequest(AbstractModel):
    """RenewDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Period: 续费时长，单位：月。
        :type Period: int
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDCDBInstanceResponse(AbstractModel):
    """RenewDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ReservedNetResource(AbstractModel):
    """保留的网络资源信息

    """

    def __init__(self):
        r"""
        :param VpcId: 私有网络
        :type VpcId: str
        :param SubnetId: 子网
        :type SubnetId: str
        :param Vip: VpcId,SubnetId下保留的内网ip
        :type Vip: str
        :param Vports: Vip下的端口
        :type Vports: list of int
        :param RecycleTime: Vip的回收时间	
        :type RecycleTime: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vports = None
        self.RecycleTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vports = params.get("Vports")
        self.RecycleTime = params.get("RecycleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param UserName: 登录用户名。
        :type UserName: str
        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param Password: 新密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。
        :type Password: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """标签对象，包含tagKey & tagValue

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键key
        :type TagKey: str
        :param TagValue: 标签值value
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
        


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        :param Inbound: 入站规则
        :type Inbound: list of SecurityGroupBound
        :param Outbound: 出站规则
        :type Outbound: list of SecurityGroupBound
        """
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
        r"""
        :param CidrIp: 来源 IP 或 IP 段，例如192.168.0.0/16
        :type CidrIp: str
        :param Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param PortRange: 端口
        :type PortRange: str
        :param IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        """
        self.CidrIp = None
        self.Action = None
        self.PortRange = None
        self.IpProtocol = None


    def _deserialize(self, params):
        self.CidrIp = params.get("CidrIp")
        self.Action = params.get("Action")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardBriefInfo(AbstractModel):
    """DCDB分片信息

    """

    def __init__(self):
        r"""
        :param ShardSerialId: 分片SerialId
        :type ShardSerialId: str
        :param ShardInstanceId: 分片ID，形如shard-7vg1o339
        :type ShardInstanceId: str
        :param Status: 分片运行状态
        :type Status: int
        :param StatusDesc: 分片运行状态描述
        :type StatusDesc: str
        :param CreateTime: 分片创建时间
        :type CreateTime: str
        :param Memory: 分片内存大小，单位GB
        :type Memory: int
        :param Storage: 分片磁盘大小，单位GB
        :type Storage: int
        :param LogDisk: 分片日志磁盘空间大小，单位GB
        :type LogDisk: int
        :param NodeCount: 分片节点个数
        :type NodeCount: int
        :param StorageUsage: 分片磁盘空间使用率
        :type StorageUsage: float
        :param ProxyVersion: 分片Proxy版本信息
        :type ProxyVersion: str
        :param ShardMasterZone: 分片主DB可用区
        :type ShardMasterZone: str
        :param ShardSlaveZones: 分片从DB可用区
        :type ShardSlaveZones: list of str
        :param Cpu: 分片Cpu核数
        :type Cpu: int
        :param NodesInfo: DB节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodesInfo: list of NodeInfo
        """
        self.ShardSerialId = None
        self.ShardInstanceId = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.Memory = None
        self.Storage = None
        self.LogDisk = None
        self.NodeCount = None
        self.StorageUsage = None
        self.ProxyVersion = None
        self.ShardMasterZone = None
        self.ShardSlaveZones = None
        self.Cpu = None
        self.NodesInfo = None


    def _deserialize(self, params):
        self.ShardSerialId = params.get("ShardSerialId")
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.LogDisk = params.get("LogDisk")
        self.NodeCount = params.get("NodeCount")
        self.StorageUsage = params.get("StorageUsage")
        self.ProxyVersion = params.get("ProxyVersion")
        self.ShardMasterZone = params.get("ShardMasterZone")
        self.ShardSlaveZones = params.get("ShardSlaveZones")
        self.Cpu = params.get("Cpu")
        if params.get("NodesInfo") is not None:
            self.NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodesInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardInfo(AbstractModel):
    """分片信息

    """

    def __init__(self):
        r"""
        :param ShardInstanceId: 分片ID
        :type ShardInstanceId: str
        :param ShardSerialId: 分片Set ID
        :type ShardSerialId: str
        :param Status: 状态：0 创建中，1 流程处理中， 2 运行中，3 分片未初始化，-2 分片已删除
        :type Status: int
        :param Createtime: 创建时间
        :type Createtime: str
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param Storage: 存储大小，单位 GB
        :type Storage: int
        :param ShardId: 分片数字ID
        :type ShardId: int
        :param NodeCount: 节点数，2 为一主一从， 3 为一主二从
        :type NodeCount: int
        :param Pid: 产品类型 Id（过时字段，请勿依赖该值）
        :type Pid: int
        :param Cpu: Cpu核数
        :type Cpu: int
        """
        self.ShardInstanceId = None
        self.ShardSerialId = None
        self.Status = None
        self.Createtime = None
        self.Memory = None
        self.Storage = None
        self.ShardId = None
        self.NodeCount = None
        self.Pid = None
        self.Cpu = None


    def _deserialize(self, params):
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.ShardSerialId = params.get("ShardSerialId")
        self.Status = params.get("Status")
        self.Createtime = params.get("Createtime")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardId = params.get("ShardId")
        self.NodeCount = params.get("NodeCount")
        self.Pid = params.get("Pid")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardZoneChooseInfo(AbstractModel):
    """分片节点可用区选择

    """

    def __init__(self):
        r"""
        :param MasterZone: 主可用区
        :type MasterZone: :class:`tencentcloud.dcdb.v20180411.models.ZonesInfo`
        :param SlaveZones: 可选的从可用区
        :type SlaveZones: list of ZonesInfo
        """
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
        


class SlowLogData(AbstractModel):
    """慢查询条目信息

    """

    def __init__(self):
        r"""
        :param CheckSum: 语句校验和，用于查询详情
        :type CheckSum: str
        :param Db: 数据库名称
        :type Db: str
        :param FingerPrint: 抽象的SQL语句
        :type FingerPrint: str
        :param LockTimeAvg: 平均的锁时间
        :type LockTimeAvg: str
        :param LockTimeMax: 最大锁时间
        :type LockTimeMax: str
        :param LockTimeMin: 最小锁时间
        :type LockTimeMin: str
        :param LockTimeSum: 锁时间总和
        :type LockTimeSum: str
        :param QueryCount: 查询次数
        :type QueryCount: str
        :param QueryTimeAvg: 平均查询时间
        :type QueryTimeAvg: str
        :param QueryTimeMax: 最大查询时间
        :type QueryTimeMax: str
        :param QueryTimeMin: 最小查询时间
        :type QueryTimeMin: str
        :param QueryTimeSum: 查询时间总和
        :type QueryTimeSum: str
        :param RowsExaminedSum: 扫描行数
        :type RowsExaminedSum: str
        :param RowsSentSum: 发送行数
        :type RowsSentSum: str
        :param TsMax: 最后执行时间
        :type TsMax: str
        :param TsMin: 首次执行时间
        :type TsMin: str
        :param User: 帐号
        :type User: str
        :param ExampleSql: 样例Sql
注意：此字段可能返回 null，表示取不到有效值。
        :type ExampleSql: str
        :param Host: 账户的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        """
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
        self.Host = None


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
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecConfig(AbstractModel):
    """按机型分类的规格配置

    """

    def __init__(self):
        r"""
        :param Machine: 规格机型
        :type Machine: str
        :param SpecConfigInfos: 规格列表
        :type SpecConfigInfos: list of SpecConfigInfo
        """
        self.Machine = None
        self.SpecConfigInfos = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        if params.get("SpecConfigInfos") is not None:
            self.SpecConfigInfos = []
            for item in params.get("SpecConfigInfos"):
                obj = SpecConfigInfo()
                obj._deserialize(item)
                self.SpecConfigInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecConfigInfo(AbstractModel):
    """实例可售卖规格详细信息，创建实例和扩容实例时 NodeCount、Memory 确定售卖规格，硬盘大小可用区间为[MinStorage,MaxStorage]

    """

    def __init__(self):
        r"""
        :param NodeCount: 节点个数，2 表示一主一从，3 表示一主二从
        :type NodeCount: int
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param MinStorage: 数据盘规格最小值，单位 GB
        :type MinStorage: int
        :param MaxStorage: 数据盘规格最大值，单位 GB
        :type MaxStorage: int
        :param SuitInfo: 推荐的使用场景
        :type SuitInfo: str
        :param Pid: 产品类型 Id
        :type Pid: int
        :param Qps: 最大 Qps 值
        :type Qps: int
        :param Cpu: CPU核数
        :type Cpu: int
        """
        self.NodeCount = None
        self.Memory = None
        self.MinStorage = None
        self.MaxStorage = None
        self.SuitInfo = None
        self.Pid = None
        self.Qps = None
        self.Cpu = None


    def _deserialize(self, params):
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.SuitInfo = params.get("SuitInfo")
        self.Pid = params.get("Pid")
        self.Qps = params.get("Qps")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitShardConfig(AbstractModel):
    """升级实例 -- 切分分片类型

    """

    def __init__(self):
        r"""
        :param ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param SplitRate: 数据切分比例，固定50%
        :type SplitRate: int
        :param ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self.ShardInstanceIds = None
        self.SplitRate = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.SplitRate = params.get("SplitRate")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
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
        r"""
        :param Offset: 本条日志在消息队列中的偏移量。
        :type Offset: int
        :param User: 执行本条sql的用户。
        :type User: str
        :param Client: 执行本条sql的客户端IP+端口。
        :type Client: str
        :param DbName: 数据库名称。
        :type DbName: str
        :param Sql: 执行的sql语句。
        :type Sql: str
        :param SelectRowNum: 返回的数据行数。
        :type SelectRowNum: int
        :param AffectRowNum: 影响行数。
        :type AffectRowNum: int
        :param Timestamp: Sql执行时间戳。
        :type Timestamp: int
        :param TimeCostMs: Sql耗时，单位为毫秒。
        :type TimeCostMs: int
        :param ResultCode: Sql返回码，0为成功。
        :type ResultCode: int
        """
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
        


class SwitchDBInstanceHARequest(AbstractModel):
    """SwitchDBInstanceHA请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id，形如 tdsql-ow728lmc。
        :type InstanceId: str
        :param Zone: 切换的目标区域，会自动选择该可用区中延迟最低的节点。
        :type Zone: str
        """
        self.InstanceId = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDBInstanceHAResponse(AbstractModel):
    """SwitchDBInstanceHA返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步流程Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class TableColumn(AbstractModel):
    """数据库列信息

    """

    def __init__(self):
        r"""
        :param Col: 列名称
        :type Col: str
        :param Type: 列类型
        :type Type: str
        """
        self.Col = None
        self.Type = None


    def _deserialize(self, params):
        self.Col = params.get("Col")
        self.Type = params.get("Type")
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
        


class TerminateDedicatedDBInstanceRequest(AbstractModel):
    """TerminateDedicatedDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 Id，形如：dcdbt-ow728lmc。
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
        


class TerminateDedicatedDBInstanceResponse(AbstractModel):
    """TerminateDedicatedDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步流程Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class UpgradeDCDBInstanceRequest(AbstractModel):
    """UpgradeDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param Zones: 变更部署时指定的新可用区列表，第1个为主可用区，其余为从可用区
        :type Zones: list of str
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.Zones = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDCDBInstanceResponse(AbstractModel):
    """UpgradeDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class UpgradeDedicatedDCDBInstanceRequest(AbstractModel):
    """UpgradeDedicatedDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param UpgradeType: 升级类型，取值为ADD，SPLIT和EXPAND。ADD-添加分片；SPLIT-切分某个分片；EXPAND-垂直扩容某个分片
        :type UpgradeType: str
        :param InstanceId: 实例ID，形如 dcdbt-mlfjm74h
        :type InstanceId: str
        :param AddShardConfig: 当UpgradeType取值为ADD时，添加分片的配置参数
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 当UpgradeType取值为EXPAND时，垂直扩容分片的配置参数
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 当UpgradeType取值为SPLIT时，切分分片的配置参数
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param SwitchAutoRetry: 错过切换时间窗口时，是否自动重试一次，0-否，1-是
        :type SwitchAutoRetry: int
        :param SwitchStartTime: 切换时间窗口开始时间
        :type SwitchStartTime: str
        :param SwitchEndTime: 切换时间窗口结束时间
        :type SwitchEndTime: str
        """
        self.UpgradeType = None
        self.InstanceId = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None
        self.SwitchAutoRetry = None
        self.SwitchStartTime = None
        self.SwitchEndTime = None


    def _deserialize(self, params):
        self.UpgradeType = params.get("UpgradeType")
        self.InstanceId = params.get("InstanceId")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self.SwitchAutoRetry = params.get("SwitchAutoRetry")
        self.SwitchStartTime = params.get("SwitchStartTime")
        self.SwitchEndTime = params.get("SwitchEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDedicatedDCDBInstanceResponse(AbstractModel):
    """UpgradeDedicatedDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
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


class UpgradeHourDCDBInstanceRequest(AbstractModel):
    """UpgradeHourDCDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UpgradeType: 升级类型，取值范围: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升级实例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>
        :type UpgradeType: str
        :param AddShardConfig: 新增分片配置，当UpgradeType为ADD时生效。
        :type AddShardConfig: :class:`tencentcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 扩容分片配置，当UpgradeType为EXPAND时生效。
        :type ExpandShardConfig: :class:`tencentcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 切分分片配置，当UpgradeType为SPLIT时生效。
        :type SplitShardConfig: :class:`tencentcloud.dcdb.v20180411.models.SplitShardConfig`
        :param SwitchStartTime: 切换开始时间，格式如: "2019-12-12 07:00:00"。开始时间必须在当前时间一个小时以后，3天以内。
        :type SwitchStartTime: str
        :param SwitchEndTime: 切换结束时间,  格式如: "2019-12-12 07:15:00"，结束时间必须大于开始时间。
        :type SwitchEndTime: str
        :param SwitchAutoRetry: 是否自动重试。 0：不自动重试  1：自动重试
        :type SwitchAutoRetry: int
        :param Zones: 变更部署时指定的新可用区列表，第1个为主可用区，其余为从可用区
        :type Zones: list of str
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None
        self.SwitchStartTime = None
        self.SwitchEndTime = None
        self.SwitchAutoRetry = None
        self.Zones = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self.SwitchStartTime = params.get("SwitchStartTime")
        self.SwitchEndTime = params.get("SwitchEndTime")
        self.SwitchAutoRetry = params.get("SwitchAutoRetry")
        self.Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeHourDCDBInstanceResponse(AbstractModel):
    """UpgradeHourDCDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserTaskInfo(AbstractModel):
    """用户任务信息

    """

    def __init__(self):
        r"""
        :param Id: 任务ID
        :type Id: int
        :param AppId: 用户账户ID
        :type AppId: int
        :param Status: 任务状态，0-任务初始化中；1-任务运行中；2-任务成功；3-任务失败
        :type Status: int
        :param UserTaskType: 任务类型，0-实例回档；1-实例创建；2-实例扩容；3-实例迁移；4-实例删除；5-实例重启
        :type UserTaskType: int
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param EndTime: 任务结束时间
        :type EndTime: str
        :param ErrMsg: 任务错误信息
        :type ErrMsg: str
        :param InputData: 客户端参数
        :type InputData: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param RegionId: 地域ID
        :type RegionId: int
        """
        self.Id = None
        self.AppId = None
        self.Status = None
        self.UserTaskType = None
        self.CreateTime = None
        self.EndTime = None
        self.ErrMsg = None
        self.InputData = None
        self.InstanceId = None
        self.InstanceName = None
        self.RegionId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.AppId = params.get("AppId")
        self.Status = params.get("Status")
        self.UserTaskType = params.get("UserTaskType")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        self.ErrMsg = params.get("ErrMsg")
        self.InputData = params.get("InputData")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewPrivileges(AbstractModel):
    """视图权限信息

    """

    def __init__(self):
        r"""
        :param Database: 数据库名
        :type Database: str
        :param View: 数据库视图名
        :type View: str
        :param Privileges: 权限信息
        :type Privileges: list of str
        """
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
        


class ZonesInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区英文ID
        :type Zone: str
        :param ZoneId: 可用区数字ID
        :type ZoneId: int
        :param ZoneName: 可用区中文名
        :type ZoneName: str
        :param OnSale: 是否在售
        :type OnSale: bool
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneName = None
        self.OnSale = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OnSale = params.get("OnSale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        