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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddShardConfig(AbstractModel):
    """升级实例 -- 新增分片类型

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BriefNodeInfo(AbstractModel):
    """描述分片DB节点信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloneAccountRequest(AbstractModel):
    """CloneAccount请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloneAccountResponse(AbstractModel):
    """CloneAccount返回参数结构体

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param UserName: AccountName
        :type UserName: str
        :param Host: 可以登录的主机，与mysql 账号的 host 格式一致，可以支持通配符，例如 %，10.%，10.20.%。
        :type Host: str
        :param Password: 账号密码，由字母、数字或常见符号组成，不能包含分号、单引号和双引号，长度为6~32位。
        :type Password: str
        :param ReadOnly: 是否创建为只读账号，0：否， 1：该账号的sql请求优先选择备机执行，备机不可用时选择主机执行，2：优先选择备机执行，备机不可用时操作失败，3：只从备机读取。
        :type ReadOnly: int
        :param Description: 账号备注，可以包含中文、英文字符、常见符号和数字，长度为0~256字符
        :type Description: str
        :param DelayThresh: 如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :type DelayThresh: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDCDBInstanceRequest(AbstractModel):
    """CreateDCDBInstance请求参数结构体

    """

    def __init__(self):
        """
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
        :param DbVersionId: 数据库引擎版本，当前可选：8.0.18，10.1.9，5.7.17。
8.0.18 - MySQL 8.0.18；
10.1.9 - Mariadb 10.1.9；
5.7.17 - Percona 5.7.17。
如果不填的话，默认为5.7.17，表示Percona 5.7.17。
        :type DbVersionId: str
        :param AutoVoucher: 是否自动使用代金券进行支付，默认不使用。
        :type AutoVoucher: bool
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param SecurityGroupId: 安全组id
        :type SecurityGroupId: str
        :param InstanceName: 实例名称， 可以通过该字段自主的设置实例的名字
        :type InstanceName: str
        :param Ipv6Flag: 是否支持IPv6
        :type Ipv6Flag: int
        :param ResourceTags: 标签键值对数组
        :type ResourceTags: list of ResourceTag
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDCDBInstanceResponse(AbstractModel):
    """CreateDCDBInstance返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param DelayThresh: 如果备机延迟超过本参数设置值，系统将认为备机发生故障
建议该参数值大于10。当ReadOnly选择1、2时该参数生效。
        :type DelayThresh: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DCDBInstanceInfo(AbstractModel):
    """分布式数据库实例信息

    """

    def __init__(self):
        """
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
        :param Status: 状态
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DCDBShardInfo(AbstractModel):
    """描述分布式数据库分片信息。

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Database(AbstractModel):
    """数据库信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DatabaseFunction(AbstractModel):
    """数据库函数信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DatabaseProcedure(AbstractModel):
    """数据库存储过程信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DatabaseTable(AbstractModel):
    """数据库表信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DatabaseView(AbstractModel):
    """数据库视图信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Deal(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param DealName: 订单号
        :type DealName: str
        :param OwnerUin: 所属账号
        :type OwnerUin: str
        :param Count: 商品数量
        :type Count: int
        :param FlowId: 关联的流程 Id，可用于查询流程执行状态
        :type FlowId: int
        :param InstanceIds: 只有创建实例的订单会填充该字段，表示该订单创建的实例的 ID。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Groups: 安全组详情。
        :type Groups: list of SecurityGroup
        :param VIP: 实例VIP
注意：此字段可能返回 null，表示取不到有效值。
        :type VIP: str
        :param VPort: 实例端口
注意：此字段可能返回 null，表示取不到有效值。
        :type VPort: int
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBSyncModeRequest(AbstractModel):
    """DescribeDBSyncMode请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDBSyncModeResponse(AbstractModel):
    """DescribeDBSyncMode返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBInstanceNodeInfoRequest(AbstractModel):
    """DescribeDCDBInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBInstanceNodeInfoResponse(AbstractModel):
    """DescribeDCDBInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBInstancesRequest(AbstractModel):
    """DescribeDCDBInstances请求参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBInstancesResponse(AbstractModel):
    """DescribeDCDBInstances返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBPriceRequest(AbstractModel):
    """DescribeDCDBPrice请求参数结构体

    """

    def __init__(self):
        """
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
        """
        self.Zone = None
        self.Count = None
        self.Period = None
        self.ShardNodeCount = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardCount = None
        self.Paymode = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Count = params.get("Count")
        self.Period = params.get("Period")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardCount = params.get("ShardCount")
        self.Paymode = params.get("Paymode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBPriceResponse(AbstractModel):
    """DescribeDCDBPrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBRenewalPriceRequest(AbstractModel):
    """DescribeDCDBRenewalPrice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。
        :type InstanceId: str
        :param Period: 续费时长，单位：月。不传则默认为1个月。
        :type Period: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBRenewalPriceResponse(AbstractModel):
    """DescribeDCDBRenewalPrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBSaleInfoRequest(AbstractModel):
    """DescribeDCDBSaleInfo请求参数结构体

    """


class DescribeDCDBSaleInfoResponse(AbstractModel):
    """DescribeDCDBSaleInfo返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBShardsRequest(AbstractModel):
    """DescribeDCDBShards请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBShardsResponse(AbstractModel):
    """DescribeDCDBShards返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBUpgradePriceRequest(AbstractModel):
    """DescribeDCDBUpgradePrice请求参数结构体

    """

    def __init__(self):
        """
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
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDCDBUpgradePriceResponse(AbstractModel):
    """DescribeDCDBUpgradePrice返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价，单位：分
        :type OriginalPrice: int
        :param Price: 实际价格，单位：分。受折扣等影响，可能和原价不同。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDatabaseObjectsRequest(AbstractModel):
    """DescribeDatabaseObjects请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    """DescribeDatabaseObjects返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDatabaseTableRequest(AbstractModel):
    """DescribeDatabaseTable请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDatabaseTableResponse(AbstractModel):
    """DescribeDatabaseTable返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的订单数量。
        :type TotalCount: list of int
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeShardSpecRequest(AbstractModel):
    """DescribeShardSpec请求参数结构体

    """


class DescribeShardSpecResponse(AbstractModel):
    """DescribeShardSpec返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSqlLogsRequest(AbstractModel):
    """DescribeSqlLogs请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSqlLogsResponse(AbstractModel):
    """DescribeSqlLogs返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUserTasksRequest(AbstractModel):
    """DescribeUserTasks请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUserTasksResponse(AbstractModel):
    """DescribeUserTasks返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExpandShardConfig(AbstractModel):
    """升级实例 -- 扩容分片类型

    """

    def __init__(self):
        """
        :param ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param ShardMemory: 分片内存大小，单位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片存储大小，单位 GB
        :type ShardStorage: int
        """
        self.ShardInstanceIds = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FlushBinlogRequest(AbstractModel):
    """FlushBinlog请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FlushBinlogResponse(AbstractModel):
    """FlushBinlog返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param UserName: 登录用户名。
        :type UserName: str
        :param Host: 用户允许的访问 host，用户名+host唯一确定一个账号。
        :type Host: str
        :param DbName: 数据库名。如果为 \*，表示查询全局权限（即 \*.\*），此时忽略 Type 和 Object 参数
        :type DbName: str
        :param Privileges: 全局权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES 
库权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER 
表/视图权限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER 
存储过程/函数权限： ALTER ROUTINE，EXECUTE 
字段权限： INSERT，REFERENCES，SELECT，UPDATE
        :type Privileges: list of str
        :param Type: 类型,可以填入 table 、 view 、 proc 、 func 和 \*。当 DbName 为具体数据库名，Type为 \* 时，表示设置该数据库权限（即db.\*），此时忽略 Object 参数
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InitDCDBInstancesRequest(AbstractModel):
    """InitDCDBInstances请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InitDCDBInstancesResponse(AbstractModel):
    """InitDCDBInstances返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class KillSessionRequest(AbstractModel):
    """KillSession请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class KillSessionResponse(AbstractModel):
    """KillSession返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBSyncModeRequest(AbstractModel):
    """ModifyDBSyncMode请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDBSyncModeResponse(AbstractModel):
    """ModifyDBSyncMode返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
注意：此字段可能返回 null，表示取不到有效值。
        :type SetValue: str
        :param Default: 系统默认值
        :type Default: str
        :param Constraint: 参数限制
        :type Constraint: :class:`tencentcloud.dcdb.v20180411.models.ParamConstraint`
        :param HaveSetValue: 是否有设置过值，false:没有设置过值，true:有设置过值。
        :type HaveSetValue: bool
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Project(AbstractModel):
    """项目信息描述

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RenewDCDBInstanceRequest(AbstractModel):
    """RenewDCDBInstance请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RenewDCDBInstanceResponse(AbstractModel):
    """RenewDCDBInstance返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceTag(AbstractModel):
    """标签对象，包含tagKey & tagValue

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SecurityGroupBound(AbstractModel):
    """安全出入口规则

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT 或者 DROP
        :type Action: str
        :param CidrIp: 来源 IP 或 IP 段，例如192.168.0.0/16
        :type CidrIp: str
        :param PortRange: 端口
        :type PortRange: str
        :param IpProtocol: 网络协议，支持 UDP、TCP 等
        :type IpProtocol: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ShardInfo(AbstractModel):
    """分片信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ShardZoneChooseInfo(AbstractModel):
    """分片节点可用区选择

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SpecConfig(AbstractModel):
    """按机型分类的规格配置

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SpecConfigInfo(AbstractModel):
    """实例可售卖规格详细信息，创建实例和扩容实例时 NodeCount、Memory 确定售卖规格，硬盘大小可用区间为[MinStorage,MaxStorage]

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SplitShardConfig(AbstractModel):
    """升级实例 -- 切分分片类型

    """

    def __init__(self):
        """
        :param ShardInstanceIds: 分片ID数组
        :type ShardInstanceIds: list of str
        :param SplitRate: 数据切分比例
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SqlLogItem(AbstractModel):
    """描述一条sql日志的详细信息。

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TableColumn(AbstractModel):
    """数据库列信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeDCDBInstanceRequest(AbstractModel):
    """UpgradeDCDBInstance请求参数结构体

    """

    def __init__(self):
        """
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
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None
        self.AutoVoucher = None
        self.VoucherIds = None


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeDCDBInstanceResponse(AbstractModel):
    """UpgradeDCDBInstance返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UserTaskInfo(AbstractModel):
    """用户任务信息

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        