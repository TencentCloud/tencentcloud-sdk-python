# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待关闭外网访问的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务Id，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ConstraintRange(AbstractModel):
    """约束类型值的范围

    """

    def __init__(self):
        """
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


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param SrcUserName: 源用户名
        :type SrcUserName: str
        :param SrcHost: 源用户允许的访问 host
        :type SrcHost: str
        :param SrcReadOnly: 源账号的 ReadOnly 属性
        :type SrcReadOnly: str
        :param DstUserName: 目的用户名
        :type DstUserName: str
        :param DstHost: 目的用户允许的访问 host
        :type DstHost: str
        :param DstReadOnly: 目的账号的 ReadOnly 属性
        :type DstReadOnly: str
        """
        self.InstanceId = None
        self.SrcUserName = None
        self.SrcHost = None
        self.SrcReadOnly = None
        self.DstUserName = None
        self.DstHost = None
        self.DstReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUserName = params.get("SrcUserName")
        self.SrcHost = params.get("SrcHost")
        self.SrcReadOnly = params.get("SrcReadOnly")
        self.DstUserName = params.get("DstUserName")
        self.DstHost = params.get("DstHost")
        self.DstReadOnly = params.get("DstReadOnly")


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UserName: 登录用户名，由字幕、数字、下划线和连字符组成，长度为1~32位。
        :type UserName: str
        :param Host: 可以登录的主机，与mysql 账号的 host 格式一致，可以支持通配符，例如 %，10.%，10.20.%。
        :type Host: str
        :param Password: 账号密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。
        :type Password: str
        :param ReadOnly: 是否创建为只读账号，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败。
        :type ReadOnly: int
        :param Description: 账号备注，可以包含中文、英文字符、常见符号和数字，长度为0~256字符
        :type Description: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None
        self.ReadOnly = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        self.ReadOnly = params.get("ReadOnly")
        self.Description = params.get("Description")


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id，透传入参。
        :type InstanceId: str
        :param UserName: 用户名，透传入参。
        :type UserName: str
        :param Host: 允许访问的 host，透传入参。
        :type Host: str
        :param ReadOnly: 透传入参。
        :type ReadOnly: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zones: 实例节点可用区分布，最多可填两个可用区。当分片规格为一主两从时，其中两个节点在第一个可用区。
        :type Zones: list of str
        :param NodeCount: 节点个数大小，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。
        :type NodeCount: int
        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。
        :type Memory: int
        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。
        :type Storage: int
        :param Period: 欲购买的时长，单位：月。
        :type Period: int
        :param Count: 欲购买的数量，默认查询购买1个实例的价格。
        :type Count: int
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param VpcId: 虚拟私有网络 ID，不传或传 0 表示创建为基础网络
        :type VpcId: str
        :param SubnetId: 虚拟私有网络子网 ID，VpcId 不为0时必填
        :type SubnetId: str
        :param ProjectId: 项目 ID，可以通过查看项目列表获取，不传则关联到默认项目
        :type ProjectId: int
        :param DbVersionId: 数据库引擎版本，当前可选：10.0.10，10.1.9，5.7.17
        :type DbVersionId: str
        """
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


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param InstanceIds: 订单对应的实例 ID 列表，如果此处没有返回实例 ID，可以通过订单查询接口获取。还可通过实例查询接口查询实例是否创建完成。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """云数据库账号信息

    """

    def __init__(self):
        """
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
        """
        self.UserName = None
        self.Host = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ReadOnly = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ReadOnly = params.get("ReadOnly")


class DBBackupTimeConfig(AbstractModel):
    """云数据库实例备份时间配置信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例 Id
        :type InstanceId: str
        :param StartBackupTime: 每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00
        :type StartBackupTime: str
        :param EndBackupTime: 每天备份执行的区间的结束时间，格式 mm:ss，形如 23:00
        :type EndBackupTime: str
        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")


class DBInstance(AbstractModel):
    """描述云数据库实例的详细信息。

    """

    def __init__(self):
        """
        :param InstanceId: 实例 Id，唯一标识一个 TDSQL 实例
        :type InstanceId: str
        :param InstanceName: 实例名称，用户可修改
        :type InstanceName: str
        :param AppId: 实例所属应用 Id
        :type AppId: int
        :param ProjectId: 实例所属项目 Id
        :type ProjectId: int
        :param Region: 实例所在地域名称，如 ap-shanghai
        :type Region: str
        :param Zone: 实例所在可用区名称，如 ap-shanghai-1
        :type Zone: str
        :param VpcId: 私有网络 Id，基础网络时为 0
        :type VpcId: int
        :param SubnetId: 子网 Id，基础网络时为 0
        :type SubnetId: int
        :param Status: 实例状态：0 创建中，1 流程处理中， 2 运行中，3 实例未初始化，-1 实例已隔离，-2 实例已删除
        :type Status: int
        :param Vip: 内网 IP 地址
        :type Vip: str
        :param Vport: 内网端口
        :type Vport: int
        :param WanDomain: 外网访问的域名，公网可解析
        :type WanDomain: str
        :param WanVip: 外网 IP 地址，公网可访问
        :type WanVip: str
        :param WanPort: 外网端口
        :type WanPort: int
        :param CreateTime: 实例创建时间，格式为 2006-01-02 15:04:05
        :type CreateTime: str
        :param UpdateTime: 实例最后更新时间，格式为 2006-01-02 15:04:05
        :type UpdateTime: str
        :param AutoRenewFlag: 自动续费标志：0 否，1 是
        :type AutoRenewFlag: int
        :param Pid: 产品类型 Id
        :type Pid: int
        :param PeriodEndTime: 实例到期时间，格式为 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param Uin: 实例所属账号
        :type Uin: str
        :param TdsqlVersion: TDSQL 版本信息，如 10.1.9
        :type TdsqlVersion: str
        :param Memory: 实例内存大小，单位 GB
        :type Memory: int
        :param Storage: 实例存储大小，单位 GB
        :type Storage: int
        """
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
        self.Pid = None
        self.PeriodEndTime = None
        self.Uin = None
        self.TdsqlVersion = None
        self.Memory = None
        self.Storage = None


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
        self.Pid = params.get("Pid")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Uin = params.get("Uin")
        self.TdsqlVersion = params.get("TdsqlVersion")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")


class DBParamValue(AbstractModel):
    """云数据库参数信息。

    """

    def __init__(self):
        """
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


class Deal(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param DealName: 订单号
        :type DealName: str
        :param OwnerUin: 所属账号
        :type OwnerUin: str
        :param Quantity: 商品数量
        :type Quantity: int
        :param FlowId: 关联的流程 Id，可用于查询流程执行状态
        :type FlowId: int
        :param InstanceIds: 只有创建实例的订单会填充该字段，表示该订单创建的实例的 ID。
        :type InstanceIds: list of str
        """
        self.DealName = None
        self.OwnerUin = None
        self.Quantity = None
        self.FlowId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Quantity = params.get("Quantity")
        self.FlowId = params.get("FlowId")
        self.InstanceIds = params.get("InstanceIds")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
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


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

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
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UserName: 登录用户名。
        :type UserName: str
        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param Type: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示查询该数据库权限（即db.\*），此时忽略 Object 参数
        :type Type: str
        :param Object: 具体的 Type 的名称，比如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
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


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Privileges: 权限列表。
        :type Privileges: list of str
        :param UserName: 数据库账号用户名
        :type UserName: str
        :param Host: 数据库账号Host
        :type Host: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        """
        :param InstanceId: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，透传入参。
        :type InstanceId: str
        :param Users: 实例用户列表。
        :type Users: list of DBAccount
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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


class DescribeBackupTimeRequest(AbstractModel):
    """DescribeBackupTime请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeBackupTimeResponse(AbstractModel):
    """DescribeBackupTime返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的配置数量
        :type TotalCount: int
        :param Items: 实例备份时间配置信息
        :type Items: :class:`tencentcloud.mariadb.v20170312.models.DBBackupTimeConfig`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = DBBackupTimeConfig()
            self.Items._deserialize(params.get("Items"))
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceSpecsRequest(AbstractModel):
    """DescribeDBInstanceSpecs请求参数结构体

    """


class DescribeDBInstanceSpecsResponse(AbstractModel):
    """DescribeDBInstanceSpecs返回参数结构体

    """

    def __init__(self):
        """
        :param Specs: 按机型分类的可售卖规格列表
        :type Specs: list of InstanceSpec
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param InstanceIds: 按照一个或者多个实例 ID 查询。实例 ID 形如：tdsql-ow728lmc。每次请求的实例的上限为100。
        :type InstanceIds: list of str
        :param SearchName: 搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。
        :type SearchName: str
        :param SearchKey: 搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\n'）分割。
        :type SearchKey: str
        :param ProjectIds: 按项目 ID 查询
        :type ProjectIds: list of int
        :param IsFilterVpc: 是否根据 VPC 网络来搜索，0 为否，1 为是
        :type IsFilterVpc: int
        :param VpcId: 私有网络 ID， IsFilterVpc 为 1 时有效
        :type VpcId: int
        :param SubnetId: 私有网络的子网 ID， IsFilterVpc 为 1 时有效
        :type SubnetId: int
        :param OrderBy: 排序字段， projectId， createtime， instancename 三者之一
        :type OrderBy: str
        :param OrderByType: 排序类型， desc 或者 asc
        :type OrderByType: str
        :param Offset: 偏移量，默认为 0
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param OriginSerialIds: 按 OriginSerialId 查询
        :type OriginSerialIds: list of str
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
        self.OriginSerialIds = None


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


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量
        :type TotalCount: list of int non-negative
        :param Instances: 实例详细信息列表
        :type Instances: list of DBInstance
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
                obj = DBInstance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Type: 请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。
        :type Type: int
        """
        self.InstanceId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Type: 请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。
        :type Type: int
        :param Total: 请求日志总数
        :type Total: int
        :param Files: 包含uri、length、mtime（修改时间）等信息
        :type Files: list of LogFileInfo
        :param Vpcprefix: 如果是VPC网络的实例，做用本前缀加上URI为下载地址
        :type Vpcprefix: str
        :param Normalprefix: 如果是普通网络的实例，做用本前缀加上URI为下载地址
        :type Normalprefix: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Type = None
        self.Total = None
        self.Files = None
        self.Vpcprefix = None
        self.Normalprefix = None
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
        self.Vpcprefix = params.get("Vpcprefix")
        self.Normalprefix = params.get("Normalprefix")
        self.RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Params: 请求DB的当前参数值
        :type Params: list of ParamDesc
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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


class DescribeDBPerformanceDetailsRequest(AbstractModel):
    """DescribeDBPerformanceDetails请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 开始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 结束日期，格式yyyy-mm-dd
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDBPerformanceDetailsResponse(AbstractModel):
    """DescribeDBPerformanceDetails返回参数结构体

    """

    def __init__(self):
        """
        :param Master: 主节点性能监控数据
        :type Master: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param Slave1: 备机1性能监控数据
        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param Slave2: 备机2性能监控数据，如果实例是一主一从，则没有该字段
        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 开始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 结束日期，格式yyyy-mm-dd
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDBPerformanceResponse(AbstractModel):
    """DescribeDBPerformance返回参数结构体

    """

    def __init__(self):
        """
        :param LongQuery: 慢查询数
        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SelectTotal: 查询操作数SELECT
        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param UpdateTotal: 更新操作数UPDATE
        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param InsertTotal: 插入操作数INSERT
        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DeleteTotal: 删除操作数DELETE
        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemHitRate: 缓存命中率
        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DiskIops: 磁盘每秒IO次数
        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param ConnActive: 活跃连接数
        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param IsMasterSwitched: 是否发生主备切换，1为发生，0否
        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SlaveDelay: 主备延迟
        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 开始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 结束日期，格式yyyy-mm-dd
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDBResourceUsageDetailsResponse(AbstractModel):
    """DescribeDBResourceUsageDetails返回参数结构体

    """

    def __init__(self):
        """
        :param Master: 主节点资源使用情况监控数据
        :type Master: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param Slave1: 备机1资源使用情况监控数据
        :type Slave1: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param Slave2: 备机2资源使用情况监控数据
        :type Slave2: :class:`tencentcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 开始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 结束日期，格式yyyy-mm-dd
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDBResourceUsageResponse(AbstractModel):
    """DescribeDBResourceUsage返回参数结构体

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: binlog日志磁盘可用空间,单位GB
        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DataDiskAvailable: 磁盘可用空间,单位GB
        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param CpuUsageRate: CPU利用率
        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemAvailable: 内存可用空间,单位GB
        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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


class DescribeDBSlowLogsRequest(AbstractModel):
    """DescribeDBSlowLogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Offset: 从结果的第几条数据开始返回
        :type Offset: int
        :param Limit: 返回的结果条数
        :type Limit: int
        :param StartTime: 查询的起始时间，形如2016-07-23 14:55:20
        :type StartTime: str
        :param EndTime: 查询的结束时间，形如2016-08-22 14:55:20
        :type EndTime: str
        :param Db: 要查询的具体数据库名称
        :type Db: str
        :param OrderBy: 排序指标，取值为query_time_sum或者query_count
        :type OrderBy: str
        :param OrderByType: 排序类型，desc或者asc
        :type OrderByType: str
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None
        self.Db = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Db = params.get("Db")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 慢查询日志数据
        :type Data: list of SlowLogData
        :param LockTimeSum: 所有语句锁时间总和
        :type LockTimeSum: str
        :param QueryCount: 所有语句查询总次数
        :type QueryCount: str
        :param Total: 总记录数
        :type Total: str
        :param QueryTimeSum: 所有语句查询时间总和
        :type QueryTimeSum: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步请求接口返回的任务流程号。
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 流程状态，0：成功，1：失败，2：运行中
        :type Status: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeLogFileRetentionPeriodRequest(AbstractModel):
    """DescribeLogFileRetentionPeriod请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeLogFileRetentionPeriodResponse(AbstractModel):
    """DescribeLogFileRetentionPeriod返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Days: 日志备份天数
        :type Days: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param DealNames: 待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。
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
        :param TotalCount: 返回的订单数量。
        :type TotalCount: list of int
        :param Deals: 订单信息列表。
        :type Deals: list of Deal
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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


class DescribePriceRequest(AbstractModel):
    """DescribePrice请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 欲新购实例的可用区ID。
        :type Zone: str
        :param NodeCount: 实例节点个数，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。
        :type NodeCount: int
        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。
        :type Memory: int
        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。
        :type Storage: int
        :param Period: 欲购买的时长，单位：月。
        :type Period: int
        :param Count: 欲购买的数量，默认查询购买1个实例的价格。
        :type Count: int
        """
        self.Zone = None
        self.NodeCount = None
        self.Memory = None
        self.Storage = None
        self.Period = None
        self.Count = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Period = params.get("Period")
        self.Count = params.get("Count")


class DescribePriceResponse(AbstractModel):
    """DescribePrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
        :type Price: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeRenewalPriceRequest(AbstractModel):
    """DescribeRenewalPrice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待续费的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Period: 续费时长，单位：月。不传则默认为1个月。
        :type Period: int
        """
        self.InstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")


class DescribeRenewalPriceResponse(AbstractModel):
    """DescribeRenewalPrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
        :type Price: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param RegionList: 可售卖地域信息列表
        :type RegionList: list of RegionInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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


class DescribeUpgradePriceRequest(AbstractModel):
    """DescribeUpgradePrice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待升级的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。
        :type Memory: int
        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。
        :type Storage: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")


class DescribeUpgradePriceResponse(AbstractModel):
    """DescribeUpgradePrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
        :type Price: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UserName: 登录用户名。
        :type UserName: str
        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param DbName: 数据库名。如果为 \*，表示设置全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param Type: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示设置该数据库权限（即db.\*），此时忽略 Object 参数
        :type Type: str
        :param Object: 具体的 Type 的名称，比如 Type 为 table 时就是具体的表名。DbName 和 Type 都为具体名称，则 Object 表示具体对象名，不能为 \* 或者为空
        :type Object: str
        :param ColName: 当 Type=table 时，ColName 为 \* 表示对表授权，如果为具体字段名，表示对字段授权
        :type ColName: str
        :param Privileges: 全局权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES 
库权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER 
表/视图权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER 
存储过程/函数权限： ALTER ROUTINE，EXECUTE 
字段权限： INSERT，REFERENCES，SELECT，UPDATE
        :type Privileges: list of str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Type = None
        self.Object = None
        self.ColName = None
        self.Privileges = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")
        self.Privileges = params.get("Privileges")


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待初始化的实例Id列表，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceIds: list of str
        :param Params: 参数列表。本接口的可选值为：character_set_server（字符集，必传），lower_case_table_names（表名大小写敏感，必传），innodb_page_size（innodb数据页，默认16K），sync_mode（同步模式：0 - 异步； 1 - 强同步；2 - 强同步可退化。默认为强同步）。
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


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务Id，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param InstanceIds: 透传入参。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param Machine: 设备型号
        :type Machine: str
        :param SpecInfos: 该机型对应的可售卖规格列表
        :type SpecInfos: list of SpecConfigInfo
        """
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


class LogFileInfo(AbstractModel):
    """拉取的日志信息

    """

    def __init__(self):
        """
        :param Mtime: Log最后修改时间
        :type Mtime: int
        :param Length: 文件长度
        :type Length: int
        :param Uri: 下载Log时用到的统一资源标识符
        :type Uri: int
        """
        self.Mtime = None
        self.Length = None
        self.Uri = None


    def _deserialize(self, params):
        self.Mtime = params.get("Mtime")
        self.Length = params.get("Length")
        self.Uri = params.get("Uri")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
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


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupTimeRequest(AbstractModel):
    """ModifyBackupTime请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param StartBackupTime: 每天备份执行的区间的开始时间，格式 mm:ss，形如 22:00
        :type StartBackupTime: str
        :param EndBackupTime: 每天备份执行的区间的结束时间，格式 mm:ss，形如 23:59
        :type EndBackupTime: str
        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")


class ModifyBackupTimeResponse(AbstractModel):
    """ModifyBackupTime返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 设置的状态，0 表示成功
        :type Status: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param InstanceId: 待修改的实例 ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param InstanceName: 新的实例名称。允许的字符为字母、数字、下划线、连字符和中文。
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


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待修改的实例ID列表。实例 ID 形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceIds: list of str
        :param ProjectId: 要分配的项目 ID，可以通过 DescribeProjects 查询项目列表接口获取。
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
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


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Config: 参数修改结果
        :type Config: list of ParamModifyResult
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Config") is not None:
            self.Config = []
            for item in params.get("Config"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self.Config.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyLogFileRetentionPeriodRequest(AbstractModel):
    """ModifyLogFileRetentionPeriod请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Days: 保存的天数,不能超过30
        :type Days: int
        """
        self.InstanceId = None
        self.Days = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")


class ModifyLogFileRetentionPeriodResponse(AbstractModel):
    """ModifyLogFileRetentionPeriod返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
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
        :param StartTime: 起始时间，形如 2018-03-24 23:59:59
        :type StartTime: str
        :param EndTime: 结束时间，形如 2018-03-24 23:59:59
        :type EndTime: str
        :param Data: 监控数据
        :type Data: list of float
        """
        self.StartTime = None
        self.EndTime = None
        self.Data = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")


class MonitorIntData(AbstractModel):
    """整形监控数据

    """

    def __init__(self):
        """
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Data: 监控数据
        :type Data: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Data = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待开放外网访问的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 异步任务Id，可通过 DescribeFlow 查询任务状态。
        :type FlowId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        """
        :param Type: 约束类型,如枚举enum，区间section
        :type Type: str
        :param Enum: 约束类型为enum时的可选值列表
        :type Enum: str
        :param Range: 约束类型为section时的范围
        :type Range: :class:`tencentcloud.mariadb.v20170312.models.ConstraintRange`
        """
        self.Type = None
        self.Enum = None
        self.Range = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Enum = params.get("Enum")
        if params.get("Range") is not None:
            self.Range = ConstraintRange()
            self.Range._deserialize(params.get("Range"))


class ParamDesc(AbstractModel):
    """DB参数描述

    """

    def __init__(self):
        """
        :param Param: 参数名字
        :type Param: str
        :param Value: 当前参数值
        :type Value: str
        :param SetValue: 设置过的值，参数生效后，该值和value一样。未设置过就不返回该字段。
        :type SetValue: str
        :param Default: 系统默认值
        :type Default: str
        :param Constraint: 参数限制
        :type Constraint: :class:`tencentcloud.mariadb.v20170312.models.ParamConstraint`
        """
        self.Param = None
        self.Value = None
        self.SetValue = None
        self.Default = None
        self.Constraint = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        self.SetValue = params.get("SetValue")
        self.Default = params.get("Default")
        if params.get("Constraint") is not None:
            self.Constraint = ParamConstraint()
            self.Constraint._deserialize(params.get("Constraint"))


class ParamModifyResult(AbstractModel):
    """修改参数结果

    """

    def __init__(self):
        """
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


class PerformanceMonitorSet(AbstractModel):
    """DB性能监控指标集合

    """

    def __init__(self):
        """
        :param UpdateTotal: 更新操作数UPDATE
        :type UpdateTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DiskIops: 磁盘每秒IO次数
        :type DiskIops: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param ConnActive: 活跃连接数
        :type ConnActive: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemHitRate: 缓存命中率
        :type MemHitRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SlaveDelay: 主备延迟
        :type SlaveDelay: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param SelectTotal: 查询操作数SELECT
        :type SelectTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param LongQuery: 慢查询数
        :type LongQuery: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DeleteTotal: 删除操作数DELETE
        :type DeleteTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param InsertTotal: 插入操作数INSERT
        :type InsertTotal: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param IsMasterSwitched: 是否发生主备切换，1为发生，0否
        :type IsMasterSwitched: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        """
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


class RegionInfo(AbstractModel):
    """售卖可用区信息

    """

    def __init__(self):
        """
        :param Region: 地域英文ID
        :type Region: str
        :param RegionId: 地域数字ID
        :type RegionId: int
        :param RegionName: 地域中文名
        :type RegionName: str
        :param ZoneList: 可用区列表
        :type ZoneList: list of ZonesInfo
        :param AvailableChoice: 可选择的主可用区和从可用区
        :type AvailableChoice: list of ZoneChooseInfo
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
                obj = ZoneChooseInfo()
                obj._deserialize(item)
                self.AvailableChoice.append(obj)


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待续费的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
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


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param InstanceId: 实例 ID，形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
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


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceUsageMonitorSet(AbstractModel):
    """DB资源使用情况监控指标集合

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: binlog日志磁盘可用空间,单位GB
        :type BinlogDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param CpuUsageRate: CPU利用率
        :type CpuUsageRate: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param MemAvailable: 内存可用空间,单位GB
        :type MemAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorData`
        :param DataDiskAvailable: 磁盘可用空间,单位GB
        :type DataDiskAvailable: :class:`tencentcloud.mariadb.v20170312.models.MonitorIntData`
        """
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
            self.DataDiskAvailable = MonitorIntData()
            self.DataDiskAvailable._deserialize(params.get("DataDiskAvailable"))


class SlowLogData(AbstractModel):
    """慢查询条目信息

    """

    def __init__(self):
        """
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
        :param TsMax: 首次执行时间
        :type TsMax: str
        :param TsMin: 最后执行时间
        :type TsMin: str
        :param User: 帐号
        :type User: str
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


class SpecConfigInfo(AbstractModel):
    """实例可售卖规格详细信息，创建实例和扩容实例时 Pid+MemSize 唯一确定一种售卖规格，磁盘大小可用区间为[MinDataDisk,MaxDataDisk]

    """

    def __init__(self):
        """
        :param Machine: 设备型号
        :type Machine: str
        :param Memory: 内存大小，单位 GB
        :type Memory: int
        :param MinStorage: 数据盘规格最小值，单位 GB
        :type MinStorage: int
        :param MaxStorage: 数据盘规格最大值，单位 GB
        :type MaxStorage: int
        :param SuitInfo: 推荐的使用场景
        :type SuitInfo: str
        :param Qps: 最大 Qps 值
        :type Qps: int
        :param Pid: 产品类型 Id
        :type Pid: int
        :param NodeCount: 节点个数，2 表示一主一从，3 表示一主二从
        :type NodeCount: int
        """
        self.Machine = None
        self.Memory = None
        self.MinStorage = None
        self.MaxStorage = None
        self.SuitInfo = None
        self.Qps = None
        self.Pid = None
        self.NodeCount = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        self.Memory = params.get("Memory")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.SuitInfo = params.get("SuitInfo")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")
        self.NodeCount = params.get("NodeCount")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待升级的实例ID。形如：tdsql-ow728lmc，可以通过 DescribeDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Memory: 内存大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得。
        :type Memory: int
        :param Storage: 存储空间大小，单位：GB，可以通过 DescribeDBInstanceSpecs
 查询实例规格获得不同内存大小对应的磁盘规格下限和上限。
        :type Storage: int
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: str
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
        :param DealName: 长订单号。可以据此调用 DescribeOrders
 查询订单详细信息，或在支付失败时调用用户账号相关接口进行支付。
        :type DealName: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ZoneChooseInfo(AbstractModel):
    """分片节点可用区选择

    """

    def __init__(self):
        """
        :param MasterZone: 主可用区
        :type MasterZone: :class:`tencentcloud.mariadb.v20170312.models.ZonesInfo`
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


class ZonesInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        """
        :param Zone: 可用区英文ID
        :type Zone: str
        :param ZoneId: 可用区数字ID
        :type ZoneId: int
        :param ZoneName: 可用区中文名
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")