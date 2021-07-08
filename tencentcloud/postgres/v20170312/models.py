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


class AccountInfo(AbstractModel):
    """账户信息

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param UserName: 帐号
        :type UserName: str
        :param Remark: 帐号备注
        :type Remark: str
        :param Status: 帐号状态。 1-创建中，2-正常，3-修改中，4-密码重置中，-1-删除中
        :type Status: int
        :param CreateTime: 帐号创建时间
        :type CreateTime: str
        :param UpdateTime: 帐号最后一次更新时间
        :type UpdateTime: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupRequest(AbstractModel):
    """AddDBInstanceToReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        """
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDBInstanceToReadOnlyGroupResponse(AbstractModel):
    """AddDBInstanceToReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        """
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


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-6r233v55
        :type DBInstanceId: str
        :param IsIpv6: 是否关闭Ipv6外网，1：是，0：否
        :type IsIpv6: int
        """
        self.DBInstanceId = None
        self.IsIpv6 = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.IsIpv6 = params.get("IsIpv6")
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


class CloseServerlessDBExtranetAccessRequest(AbstractModel):
    """CloseServerlessDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例唯一标识符
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
        :type DBInstanceName: str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseServerlessDBExtranetAccessResponse(AbstractModel):
    """CloseServerlessDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param DBVersion: PostgreSQL内核版本，目前支持以下版本：9.3.5、9.5.4、10.4、11.8、12.4 。
        :type DBVersion: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 一次性购买的实例数量。取值1-100
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID。
        :type SubnetId: str
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费；
        :type AutoRenewFlag: int
        :param ActivityId: 活动ID
        :type ActivityId: int
        :param Name: 实例名(后续支持)
        :type Name: str
        :param NeedSupportIpv6: 是否需要支持Ipv6，1：是，0：否
        :type NeedSupportIpv6: int
        :param TagList: 实例需要绑定的Tag信息，默认为空
        :type TagList: list of Tag
        :param SecurityGroupIds: 安全组id
        :type SecurityGroupIds: list of str
        """
        self.SpecCode = None
        self.DBVersion = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Zone = None
        self.ProjectId = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.AutoRenewFlag = None
        self.ActivityId = None
        self.Name = None
        self.NeedSupportIpv6 = None
        self.TagList = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.DBVersion = params.get("DBVersion")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ActivityId = params.get("ActivityId")
        self.Name = params.get("Name")
        self.NeedSupportIpv6 = params.get("NeedSupportIpv6")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.SecurityGroupIds = params.get("SecurityGroupIds")
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
        :param DealNames: 订单号列表。每个实例对应一个订单号。
        :type DealNames: list of str
        :param BillId: 冻结流水号
        :type BillId: str
        :param DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.BillId = None
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.BillId = params.get("BillId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体

    """

    def __init__(self):
        """
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param DBVersion: PostgreSQL内核版本，目前支持：9.3.5、9.5.4、10.4、11.8、12.4五种版本。
        :type DBVersion: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 一次性购买的实例数量。取值1-10。
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param Charset: 实例字符集，目前只支持：UTF8、LATIN1。
        :type Charset: str
        :param AdminName: 实例根账号用户名。
        :type AdminName: str
        :param AdminPassword: 实例根账号用户名对应的密码。
        :type AdminPassword: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 已配置的私有网络中的子网ID。
        :type SubnetId: str
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费。
        :type AutoRenewFlag: int
        :param ActivityId: 活动ID。
        :type ActivityId: int
        :param Name: 实例名。
        :type Name: str
        :param NeedSupportIpv6: 是否需要支持Ipv6，1：是，0：否（默认）。
        :type NeedSupportIpv6: int
        :param TagList: 实例需要绑定的Tag信息，默认为空。
        :type TagList: list of Tag
        :param SecurityGroupIds: 安全组ID。
        :type SecurityGroupIds: list of str
        """
        self.SpecCode = None
        self.DBVersion = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Zone = None
        self.Charset = None
        self.AdminName = None
        self.AdminPassword = None
        self.ProjectId = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.AutoRenewFlag = None
        self.ActivityId = None
        self.Name = None
        self.NeedSupportIpv6 = None
        self.TagList = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.DBVersion = params.get("DBVersion")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Zone = params.get("Zone")
        self.Charset = params.get("Charset")
        self.AdminName = params.get("AdminName")
        self.AdminPassword = params.get("AdminPassword")
        self.ProjectId = params.get("ProjectId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ActivityId = params.get("ActivityId")
        self.Name = params.get("Name")
        self.NeedSupportIpv6 = params.get("NeedSupportIpv6")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 订单号列表。每个实例对应一个订单号。
        :type DealNames: list of str
        :param BillId: 冻结流水号。
        :type BillId: str
        :param DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值。
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.BillId = None
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.BillId = params.get("BillId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateReadOnlyDBInstanceRequest(AbstractModel):
    """CreateReadOnlyDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param SpecCode: 售卖规格ID。该参数可以通过调用DescribeProductConfig的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param DBVersion: PostgreSQL内核版本，目前强制和主实例保持一致
        :type DBVersion: str
        :param Storage: 实例容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 一次性购买的实例数量。取值1-100
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值，按量计费模式下该参数传1。
        :type Period: int
        :param MasterDBInstanceId: 只读实例的主实例ID
        :type MasterDBInstanceId: str
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param InstanceChargeType: 实例计费类型。目前支持：PREPAID（预付费，即包年包月），POSTPAID_BY_HOUR（后付费，即按量计费）。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自动使用代金券。1（是），0（否），默认不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券。
        :type VoucherIds: list of str
        :param AutoRenewFlag: 续费标记：0-正常续费（默认）；1-自动续费；
        :type AutoRenewFlag: int
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID。
        :type SubnetId: str
        :param ActivityId: 优惠活动ID
        :type ActivityId: int
        :param Name: 实例名(后续支持)
        :type Name: str
        :param NeedSupportIpv6: 是否需要支持Ipv6，1：是，0：否
        :type NeedSupportIpv6: int
        :param ReadOnlyGroupId: 只读组ID。
        :type ReadOnlyGroupId: str
        :param TagList: 实例需要绑定的Tag信息，默认为空
        :type TagList: :class:`tencentcloud.postgres.v20170312.models.Tag`
        :param SecurityGroupIds: 安全组id
        :type SecurityGroupIds: list of str
        """
        self.SpecCode = None
        self.DBVersion = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.MasterDBInstanceId = None
        self.Zone = None
        self.ProjectId = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.AutoRenewFlag = None
        self.VpcId = None
        self.SubnetId = None
        self.ActivityId = None
        self.Name = None
        self.NeedSupportIpv6 = None
        self.ReadOnlyGroupId = None
        self.TagList = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.DBVersion = params.get("DBVersion")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ActivityId = params.get("ActivityId")
        self.Name = params.get("Name")
        self.NeedSupportIpv6 = params.get("NeedSupportIpv6")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        if params.get("TagList") is not None:
            self.TagList = Tag()
            self.TagList._deserialize(params.get("TagList"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyDBInstanceResponse(AbstractModel):
    """CreateReadOnlyDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 订单号列表。每个实例对应一个订单号
        :type DealNames: list of str
        :param BillId: 冻结流水号
        :type BillId: str
        :param DBInstanceIdSet: 创建成功的实例ID集合，只在后付费情景下有返回值
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.BillId = None
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.BillId = params.get("BillId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateReadOnlyGroupRequest(AbstractModel):
    """CreateReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param MasterDBInstanceId: 主实例ID
        :type MasterDBInstanceId: str
        :param Name: 只读组名称
        :type Name: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param ReplayLagEliminate: 延迟时间大小开关：0关、1开
        :type ReplayLagEliminate: int
        :param ReplayLatencyEliminate: 延迟空间大小开关： 0关、1开
        :type ReplayLatencyEliminate: int
        :param MaxReplayLag: 延迟时间大小阈值，单位ms
        :type MaxReplayLag: int
        :param MaxReplayLatency: 延迟空间大小阈值，单位MB
        :type MaxReplayLatency: int
        :param MinDelayEliminateReserve: 延迟剔除最小保留实例数
        :type MinDelayEliminateReserve: int
        :param SecurityGroupIds: 安全组id
        :type SecurityGroupIds: list of str
        """
        self.MasterDBInstanceId = None
        self.Name = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.ReplayLagEliminate = None
        self.ReplayLatencyEliminate = None
        self.MaxReplayLag = None
        self.MaxReplayLatency = None
        self.MinDelayEliminateReserve = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ReplayLagEliminate = params.get("ReplayLagEliminate")
        self.ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self.MaxReplayLag = params.get("MaxReplayLag")
        self.MaxReplayLatency = params.get("MaxReplayLatency")
        self.MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReadOnlyGroupResponse(AbstractModel):
    """CreateReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReadOnlyGroupId = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateServerlessDBInstanceRequest(AbstractModel):
    """CreateServerlessDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区ID。公测阶段仅支持ap-shanghai-2、ap-beijing-1,ap-guangzhou-2.
        :type Zone: str
        :param DBInstanceName: DB实例名称，同一个账号下该值必须唯一。
        :type DBInstanceName: str
        :param DBVersion: PostgreSQL内核版本，目前只支持：10.4。
        :type DBVersion: str
        :param DBCharset: PostgreSQL数据库字符集，目前支持UTF8。
        :type DBCharset: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param VpcId: 私有网络ID。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID。
        :type SubnetId: str
        :param TagList: 实例需要绑定的标签数组信息
        :type TagList: list of Tag
        """
        self.Zone = None
        self.DBInstanceName = None
        self.DBVersion = None
        self.DBCharset = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.TagList = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBVersion = params.get("DBVersion")
        self.DBCharset = params.get("DBCharset")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerlessDBInstanceResponse(AbstractModel):
    """CreateServerlessDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，该ID全局唯一，如：postgres-xxxxx
        :type DBInstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.RequestId = params.get("RequestId")


class DBBackup(AbstractModel):
    """数据库备份信息

    """

    def __init__(self):
        """
        :param Id: 备份文件唯一标识
        :type Id: int
        :param StartTime: 文件生成的开始时间
        :type StartTime: str
        :param EndTime: 文件生成的结束时间
        :type EndTime: str
        :param Size: 文件大小(K)
        :type Size: int
        :param Strategy: 策略（0-实例备份；1-多库备份）
        :type Strategy: int
        :param Way: 类型（0-定时）
        :type Way: int
        :param Type: 备份方式（1-完整）
        :type Type: int
        :param Status: 状态（1-创建中；2-成功；3-失败）
        :type Status: int
        :param DbList: DB列表
        :type DbList: list of str
        :param InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Strategy = None
        self.Way = None
        self.Type = None
        self.Status = None
        self.DbList = None
        self.InternalAddr = None
        self.ExternalAddr = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Strategy = params.get("Strategy")
        self.Way = params.get("Way")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.DbList = params.get("DbList")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstance(AbstractModel):
    """描述实例的详细信息

    """

    def __init__(self):
        """
        :param Region: 实例所属地域，如: ap-guangzhou，对应RegionSet的Region字段
        :type Region: str
        :param Zone: 实例所属可用区， 如：ap-guangzhou-3，对应ZoneSet的Zone字段
        :type Zone: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
        :type DBInstanceName: str
        :param DBInstanceStatus: 实例状态，分别为：applying（申请中）、init(待初始化)、initing(初始化中)、running(运行中)、limited run（受限运行）、isolated（已隔离）、recycling（回收中）、recycled（已回收）、job running（任务执行中）、offline（下线）、migrating（迁移中）、expanding（扩容中）、readonly（只读）、restarting（重启中）
        :type DBInstanceStatus: str
        :param DBInstanceMemory: 实例分配的内存大小，单位：GB
        :type DBInstanceMemory: int
        :param DBInstanceStorage: 实例分配的存储空间大小，单位：GB
        :type DBInstanceStorage: int
        :param DBInstanceCpu: 实例分配的CPU数量，单位：个
        :type DBInstanceCpu: int
        :param DBInstanceClass: 售卖规格ID
        :type DBInstanceClass: str
        :param DBInstanceType: 实例类型，类型有：1、primary（主实例）；2、readonly（只读实例）；3、guard（灾备实例）；4、temp（临时实例）
        :type DBInstanceType: str
        :param DBInstanceVersion: 实例版本，目前只支持standard（双机高可用版, 一主一从）
        :type DBInstanceVersion: str
        :param DBCharset: 实例DB字符集
        :type DBCharset: str
        :param DBVersion: PostgreSQL内核版本
        :type DBVersion: str
        :param CreateTime: 实例创建时间
        :type CreateTime: str
        :param UpdateTime: 实例执行最后一次更新的时间
        :type UpdateTime: str
        :param ExpireTime: 实例到期时间
        :type ExpireTime: str
        :param IsolatedTime: 实例隔离时间
        :type IsolatedTime: str
        :param PayType: 计费模式，1、prepaid（包年包月,预付费）；2、postpaid（按量计费，后付费）
        :type PayType: str
        :param AutoRenew: 是否自动续费，1：自动续费，0：不自动续费
        :type AutoRenew: int
        :param DBInstanceNetInfo: 实例网络连接信息
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param Type: 机器类型
        :type Type: str
        :param AppId: 用户的AppId
        :type AppId: int
        :param Uid: 实例的Uid
        :type Uid: int
        :param SupportIpv6: 实例是否支持Ipv6，1：支持，0：不支持
        :type SupportIpv6: int
        :param TagList: 实例绑定的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        :param MasterDBInstanceId: 主实例信息，仅在实例为只读实例时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterDBInstanceId: str
        :param ReadOnlyInstanceNum: 只读实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyInstanceNum: int
        :param StatusInReadonlyGroup: 只读实例在只读组中的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInReadonlyGroup: str
        :param OfflineTime: 下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        """
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.DBInstanceMemory = None
        self.DBInstanceStorage = None
        self.DBInstanceCpu = None
        self.DBInstanceClass = None
        self.DBInstanceType = None
        self.DBInstanceVersion = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.PayType = None
        self.AutoRenew = None
        self.DBInstanceNetInfo = None
        self.Type = None
        self.AppId = None
        self.Uid = None
        self.SupportIpv6 = None
        self.TagList = None
        self.MasterDBInstanceId = None
        self.ReadOnlyInstanceNum = None
        self.StatusInReadonlyGroup = None
        self.OfflineTime = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.DBInstanceMemory = params.get("DBInstanceMemory")
        self.DBInstanceStorage = params.get("DBInstanceStorage")
        self.DBInstanceCpu = params.get("DBInstanceCpu")
        self.DBInstanceClass = params.get("DBInstanceClass")
        self.DBInstanceType = params.get("DBInstanceType")
        self.DBInstanceVersion = params.get("DBInstanceVersion")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.PayType = params.get("PayType")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        self.Type = params.get("Type")
        self.AppId = params.get("AppId")
        self.Uid = params.get("Uid")
        self.SupportIpv6 = params.get("SupportIpv6")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.ReadOnlyInstanceNum = params.get("ReadOnlyInstanceNum")
        self.StatusInReadonlyGroup = params.get("StatusInReadonlyGroup")
        self.OfflineTime = params.get("OfflineTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstanceNetInfo(AbstractModel):
    """描述实例的网络连接信息。

    """

    def __init__(self):
        """
        :param Address: DNS域名
        :type Address: str
        :param Ip: IP地址
        :type Ip: str
        :param Port: 连接Port地址
        :type Port: int
        :param NetType: 网络类型，1、inner（基础网络内网地址）；2、private（私有网络内网地址）；3、public（基础网络或私有网络的外网地址）；
        :type NetType: str
        :param Status: 网络连接状态
        :type Status: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.NetType = None
        self.Status = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.NetType = params.get("NetType")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupRequest(AbstractModel):
    """DeleteReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 待删除只读组ID
        :type ReadOnlyGroupId: str
        """
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReadOnlyGroupResponse(AbstractModel):
    """DeleteReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteServerlessDBInstanceRequest(AbstractModel):
    """DeleteServerlessDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceName: DB实例名称，实例名和实例ID必须至少传一个，如果同时存在，将只以实例ID为准。
        :type DBInstanceName: str
        :param DBInstanceId: DB实例ID，实例名和实例ID必须至少传一个，如果同时存在，将只以实例ID为准。
        :type DBInstanceId: str
        """
        self.DBInstanceName = None
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServerlessDBInstanceResponse(AbstractModel):
    """DeleteServerlessDBInstance返回参数结构体

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
        :param DBInstanceId: 实例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param Limit: 分页返回，每页最大返回数目，默认20，取值范围为1-100
        :type Limit: int
        :param Offset: 分页返回，返回第几页的用户数据。页码从0开始计数
        :type Offset: int
        :param OrderBy: 返回数据按照创建时间或者用户名排序。取值只能为createTime或者name。createTime-按照创建时间排序；name-按照用户名排序
        :type OrderBy: str
        :param OrderByType: 返回结果是升序还是降序。取值只能为desc或者asc。desc-降序；asc-升序
        :type OrderByType: str
        """
        self.DBInstanceId = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
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
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 本次调用接口共返回了多少条数据。
        :type TotalCount: int
        :param Details: 帐号列表详细信息。
        :type Details: list of AccountInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param Type: 备份方式（1-全量）。目前只支持全量，取值为1。
        :type Type: int
        :param StartTime: 查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param Limit: 备份列表分页返回，每页返回数量，默认为 20，最小为1，最大值为 100。（当该参数不传或者传0时按默认值处理）
        :type Limit: int
        :param Offset: 返回结果中的第几页，从第0页开始。默认为0。
        :type Offset: int
        """
        self.DBInstanceId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Type = params.get("Type")
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
        


class DescribeDBBackupsResponse(AbstractModel):
    """DescribeDBBackups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回备份列表中备份文件的个数
        :type TotalCount: int
        :param BackupList: 备份列表
        :type BackupList: list of DBBackup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = DBBackup()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBErrlogsRequest(AbstractModel):
    """DescribeDBErrlogs请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-5bq3wfjd
        :type DBInstanceId: str
        :param StartTime: 查询起始时间，形如2018-01-01 00:00:00，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-01-01 00:00:00
        :type EndTime: str
        :param DatabaseName: 数据库名字
        :type DatabaseName: str
        :param SearchKeys: 搜索关键字
        :type SearchKeys: list of str
        :param Limit: 分页返回，每页返回的最大数量。取值为1-100
        :type Limit: int
        :param Offset: 分页返回，返回第几页的数据，从第0页开始计数
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.SearchKeys = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.SearchKeys = params.get("SearchKeys")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBErrlogsResponse(AbstractModel):
    """DescribeDBErrlogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 本次调用返回了多少条数据
        :type TotalCount: int
        :param Details: 错误日志列表
        :type Details: list of ErrLogDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ErrLogDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceAttributeRequest(AbstractModel):
    """DescribeDBInstanceAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceAttributeResponse(AbstractModel):
    """DescribeDBInstanceAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param DBInstance: 实例详细信息。
        :type DBInstance: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBInstance = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DBInstance") is not None:
            self.DBInstance = DBInstance()
            self.DBInstance._deserialize(params.get("DBInstance"))
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 按照一个或者多个过滤条件进行查询，目前支持的过滤条件有：
db-instance-id：按照实例ID过滤，类型为string
db-instance-name：按照实例名过滤，类型为string
db-project-id：按照项目ID过滤，类型为integer
db-pay-mode：按照付费模式过滤，类型为string
db-tag-key：按照标签键过滤，类型为string
        :type Filters: list of Filter
        :param Limit: 每页显示数量，取值范围为1-100，默认为返回10条。
        :type Limit: int
        :param OrderBy: 排序指标，如实例名、创建时间等，支持DBInstanceId,CreateTime,Name,EndTime
        :type OrderBy: str
        :param Offset: 页码偏移量，从0开始。
        :type Offset: int
        :param OrderByType: 排序方式，包括升序：asc、降序：desc。
        :type OrderByType: str
        """
        self.Filters = None
        self.Limit = None
        self.OrderBy = None
        self.Offset = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.Offset = params.get("Offset")
        self.OrderByType = params.get("OrderByType")
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
        :param TotalCount: 查询到的实例数量。
        :type TotalCount: int
        :param DBInstanceSet: 实例详细信息集合。
        :type DBInstanceSet: list of DBInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self.DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = DBInstance()
                obj._deserialize(item)
                self.DBInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSlowlogsRequest(AbstractModel):
    """DescribeDBSlowlogs请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param StartTime: 查询起始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param DatabaseName: 数据库名字
        :type DatabaseName: str
        :param OrderBy: 按照何种指标排序，取值为sum_calls或者sum_cost_time。sum_calls-总调用次数；sum_cost_time-总的花费时间
        :type OrderBy: str
        :param OrderByType: 排序规则。desc-降序；asc-升序
        :type OrderByType: str
        :param Limit: 分页返回结果，每页最大返回数量，取值为1-100，默认20
        :type Limit: int
        :param Offset: 分页返回结果，返回结果的第几页，从0开始计数
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.OrderBy = None
        self.OrderByType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSlowlogsResponse(AbstractModel):
    """DescribeDBSlowlogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 本次返回多少条数据
        :type TotalCount: int
        :param Detail: 慢查询日志详情
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.SlowlogDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self.Detail = SlowlogDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeDBXlogsRequest(AbstractModel):
    """DescribeDBXlogs请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param StartTime: 查询开始时间，形如2018-06-10 17:06:38，起始时间不得小于7天以前
        :type StartTime: str
        :param EndTime: 查询结束时间，形如2018-06-10 17:06:38
        :type EndTime: str
        :param Offset: 分页返回，表示返回第几页的条目。从第0页开始计数。
        :type Offset: int
        :param Limit: 分页返回，表示每页有多少条目。取值为1-100。
        :type Limit: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
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
        


class DescribeDBXlogsResponse(AbstractModel):
    """DescribeDBXlogs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 表示此次返回结果有多少条数据。
        :type TotalCount: int
        :param XlogList: Xlog列表
        :type XlogList: list of Xlog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.XlogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("XlogList") is not None:
            self.XlogList = []
            for item in params.get("XlogList"):
                obj = Xlog()
                obj._deserialize(item)
                self.XlogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
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
        :param Items: 数据库信息
        :type Items: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders请求参数结构体

    """

    def __init__(self):
        """
        :param DealNames: 订单名集合
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
        """
        :param TotalCount: 订单数量
        :type TotalCount: int
        :param Deals: 订单数组
        :type Deals: list of PgDeal
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
                obj = PgDeal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区名称
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
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
        :param SpecInfoList: 售卖规格列表。
        :type SpecInfoList: list of SpecInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReadOnlyGroupsRequest(AbstractModel):
    """DescribeReadOnlyGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件，必须传入主实例ID进行过滤，否则返回值将为空，过滤参数为：db-master-instance-id
        :type Filters: list of Filter
        :param PageSize: 查询每一页的条数，默认为10
        :type PageSize: int
        :param PageNumber: 查询的页码，默认为1
        :type PageNumber: int
        :param OrderBy: 查询排序依据，目前支持:ROGroupId,CreateTime,Name
        :type OrderBy: str
        :param OrderByType: 查询排序依据类型，目前支持:desc,asc
        :type OrderByType: str
        """
        self.Filters = None
        self.PageSize = None
        self.PageNumber = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReadOnlyGroupsResponse(AbstractModel):
    """DescribeReadOnlyGroups返回参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupList: 只读组列表
        :type ReadOnlyGroupList: list of ReadOnlyGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReadOnlyGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReadOnlyGroupList") is not None:
            self.ReadOnlyGroupList = []
            for item in params.get("ReadOnlyGroupList"):
                obj = ReadOnlyGroup()
                obj._deserialize(item)
                self.ReadOnlyGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param RegionSet: 地域信息集合。
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


class DescribeServerlessDBInstancesRequest(AbstractModel):
    """DescribeServerlessDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filter: 查询条件
        :type Filter: list of Filter
        :param Limit: 查询个数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param OrderBy: 排序指标，目前支持实例创建时间CreateTime
        :type OrderBy: str
        :param OrderByType: 排序方式，包括升序、降序
        :type OrderByType: str
        """
        self.Filter = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)
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
        


class DescribeServerlessDBInstancesResponse(AbstractModel):
    """DescribeServerlessDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询结果数
        :type TotalCount: int
        :param DBInstanceSet: 查询结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceSet: list of ServerlessDBInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self.DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = ServerlessDBInstance()
                obj._deserialize(item)
                self.DBInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的结果数量。
        :type TotalCount: int
        :param ZoneSet: 可用区信息集合。
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


class DestroyDBInstanceRequest(AbstractModel):
    """DestroyDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 待下线实例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDBInstanceResponse(AbstractModel):
    """DestroyDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisIsolateDBInstancesRequest(AbstractModel):
    """DisIsolateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 资源ID列表
        :type DBInstanceIdSet: list of str
        :param Period: 包年包月实例解隔离时购买时常 以月为单位
        :type Period: int
        :param AutoVoucher: 是否使用代金券：true-使用,false-不使用，默认不使用
        :type AutoVoucher: bool
        :param VoucherIds: 代金券id列表
        :type VoucherIds: list of str
        """
        self.DBInstanceIdSet = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisIsolateDBInstancesResponse(AbstractModel):
    """DisIsolateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ErrLogDetail(AbstractModel):
    """错误日志详情

    """

    def __init__(self):
        """
        :param UserName: 用户名
        :type UserName: str
        :param Database: 数据库名字
        :type Database: str
        :param ErrTime: 错误发生时间
        :type ErrTime: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        """
        self.UserName = None
        self.Database = None
        self.ErrTime = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Database = params.get("Database")
        self.ErrTime = params.get("ErrTime")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称等
    * 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    * 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
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
        """
        :param DBInstanceIdSet: 实例ID集合。
        :type DBInstanceIdSet: list of str
        :param AdminName: 实例根账号用户名。
        :type AdminName: str
        :param AdminPassword: 实例根账号用户名对应的密码。
        :type AdminPassword: str
        :param Charset: 实例字符集，目前只支持：UTF8、LATIN1。
        :type Charset: str
        """
        self.DBInstanceIdSet = None
        self.AdminName = None
        self.AdminPassword = None
        self.Charset = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AdminName = params.get("AdminName")
        self.AdminPassword = params.get("AdminPassword")
        self.Charset = params.get("Charset")
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
        :param DBInstanceIdSet: 实例ID集合。
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区ID。该参数可以通过调用 DescribeZones 接口的返回值中的Zone字段来获取。
        :type Zone: str
        :param SpecCode: 规格ID。该参数可以通过调用DescribeProductConfig接口的返回值中的SpecCode字段来获取。
        :type SpecCode: str
        :param Storage: 存储容量大小，单位：GB。
        :type Storage: int
        :param InstanceCount: 实例数量。目前最大数量不超过100，如需一次性创建更多实例，请联系客服支持。
        :type InstanceCount: int
        :param Period: 购买时长，单位：月。目前只支持1,2,3,4,5,6,7,8,9,10,11,12,24,36这些值。
        :type Period: int
        :param Pid: 计费ID。该参数可以通过调用DescribeProductConfig接口的返回值中的Pid字段来获取。
        :type Pid: int
        :param InstanceChargeType: 实例计费类型。目前只支持：PREPAID（预付费，即包年包月）。
        :type InstanceChargeType: str
        """
        self.Zone = None
        self.SpecCode = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Pid = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Pid = params.get("Pid")
        self.InstanceChargeType = params.get("InstanceChargeType")
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
        :param OriginalPrice: 原始价格，单位：分
        :type OriginalPrice: int
        :param Price: 折后价格，单位：分
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
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param Period: 续费周期，按月计算，最大不超过48
        :type Period: int
        """
        self.DBInstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Period = params.get("Period")
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
        :param OriginalPrice: 总费用，打折前的。比如24650表示246.5元
        :type OriginalPrice: int
        :param Price: 实际需要付款金额。比如24650表示246.5元
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
        :param Storage: 实例的磁盘大小，单位GB
        :type Storage: int
        :param Memory: 实例的内存大小，单位GB
        :type Memory: int
        :param DBInstanceId: 实例ID，形如postgres-hez4fh0v
        :type DBInstanceId: str
        :param InstanceChargeType: 实例计费类型，预付费或者后付费。PREPAID-预付费。目前只支持预付费。
        :type InstanceChargeType: str
        """
        self.Storage = None
        self.Memory = None
        self.DBInstanceId = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Storage = params.get("Storage")
        self.Memory = params.get("Memory")
        self.DBInstanceId = params.get("DBInstanceId")
        self.InstanceChargeType = params.get("InstanceChargeType")
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
        :param OriginalPrice: 总费用，打折前的
        :type OriginalPrice: int
        :param Price: 实际需要付款金额
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


class IsolateDBInstancesRequest(AbstractModel):
    """IsolateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 实例ID集合
        :type DBInstanceIdSet: list of str
        """
        self.DBInstanceIdSet = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateDBInstancesResponse(AbstractModel):
    """IsolateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: 实例用户名
        :type UserName: str
        :param Remark: 用户UserName对应的新备注
        :type Remark: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
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
        :param DBInstanceId: 数据库实例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param InstanceName: 新的数据库实例名字
        :type InstanceName: str
        """
        self.DBInstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceReadOnlyGroupRequest(AbstractModel):
    """ModifyDBInstanceReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 当前实例所在只读组ID
        :type ReadOnlyGroupId: str
        :param NewReadOnlyGroupId: 实例修改的目标只读组ID
        :type NewReadOnlyGroupId: str
        """
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None
        self.NewReadOnlyGroupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.NewReadOnlyGroupId = params.get("NewReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceReadOnlyGroupResponse(AbstractModel):
    """ModifyDBInstanceReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        """
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


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: postgresql实例ID数组
        :type DBInstanceIdSet: list of str
        :param ProjectId: postgresql实例所属新项目的ID
        :type ProjectId: str
        """
        self.DBInstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
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
        :param Count: 转移项目成功的实例个数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class ModifyReadOnlyGroupConfigRequest(AbstractModel):
    """ModifyReadOnlyGroupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名称
        :type ReadOnlyGroupName: str
        :param ReplayLagEliminate: 延迟时间配置开关：0关、1开
        :type ReplayLagEliminate: int
        :param ReplayLatencyEliminate: 延迟日志大小配置开关：0关、1开
        :type ReplayLatencyEliminate: int
        :param MaxReplayLatency: 延迟日志大小阈值，单位MB
        :type MaxReplayLatency: int
        :param MaxReplayLag: 延迟时间大小阈值，单位ms
        :type MaxReplayLag: int
        :param Rebalance: 自动负载均衡开关：0关、1开
        :type Rebalance: int
        :param MinDelayEliminateReserve: 延迟剔除最小保留实例数
        :type MinDelayEliminateReserve: int
        """
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.ReplayLagEliminate = None
        self.ReplayLatencyEliminate = None
        self.MaxReplayLatency = None
        self.MaxReplayLag = None
        self.Rebalance = None
        self.MinDelayEliminateReserve = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.ReplayLagEliminate = params.get("ReplayLagEliminate")
        self.ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self.MaxReplayLatency = params.get("MaxReplayLatency")
        self.MaxReplayLag = params.get("MaxReplayLag")
        self.Rebalance = params.get("Rebalance")
        self.MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyReadOnlyGroupConfigResponse(AbstractModel):
    """ModifyReadOnlyGroupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NormalQueryItem(AbstractModel):
    """单条SlowQuery信息

    """

    def __init__(self):
        """
        :param UserName: 用户名
        :type UserName: str
        :param Calls: 调用次数
        :type Calls: int
        :param CallsGrids: 粒度点
        :type CallsGrids: list of int
        :param CostTime: 花费总时间
        :type CostTime: float
        :param Rows: 影响的行数
        :type Rows: int
        :param MinCostTime: 花费最小时间
        :type MinCostTime: float
        :param MaxCostTime: 花费最大时间
        :type MaxCostTime: float
        :param FirstTime: 最早一条慢SQL时间
        :type FirstTime: str
        :param LastTime: 最晚一条慢SQL时间
        :type LastTime: str
        :param SharedReadBlks: 读共享内存块数
        :type SharedReadBlks: int
        :param SharedWriteBlks: 写共享内存块数
        :type SharedWriteBlks: int
        :param ReadCostTime: 读io总耗时
        :type ReadCostTime: int
        :param WriteCostTime: 写io总耗时
        :type WriteCostTime: int
        :param DatabaseName: 数据库名字
        :type DatabaseName: str
        :param NormalQuery: 脱敏后的慢SQL
        :type NormalQuery: str
        """
        self.UserName = None
        self.Calls = None
        self.CallsGrids = None
        self.CostTime = None
        self.Rows = None
        self.MinCostTime = None
        self.MaxCostTime = None
        self.FirstTime = None
        self.LastTime = None
        self.SharedReadBlks = None
        self.SharedWriteBlks = None
        self.ReadCostTime = None
        self.WriteCostTime = None
        self.DatabaseName = None
        self.NormalQuery = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Calls = params.get("Calls")
        self.CallsGrids = params.get("CallsGrids")
        self.CostTime = params.get("CostTime")
        self.Rows = params.get("Rows")
        self.MinCostTime = params.get("MinCostTime")
        self.MaxCostTime = params.get("MaxCostTime")
        self.FirstTime = params.get("FirstTime")
        self.LastTime = params.get("LastTime")
        self.SharedReadBlks = params.get("SharedReadBlks")
        self.SharedWriteBlks = params.get("SharedWriteBlks")
        self.ReadCostTime = params.get("ReadCostTime")
        self.WriteCostTime = params.get("WriteCostTime")
        self.DatabaseName = params.get("DatabaseName")
        self.NormalQuery = params.get("NormalQuery")
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
        :param DBInstanceId: 实例ID，形如postgres-hez4fh0v
        :type DBInstanceId: str
        :param IsIpv6: 是否开通Ipv6外网，1：是，0：否
        :type IsIpv6: int
        """
        self.DBInstanceId = None
        self.IsIpv6 = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.IsIpv6 = params.get("IsIpv6")
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


class OpenServerlessDBExtranetAccessRequest(AbstractModel):
    """OpenServerlessDBExtranetAccess请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例的唯一标识符
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
        :type DBInstanceName: str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenServerlessDBExtranetAccessResponse(AbstractModel):
    """OpenServerlessDBExtranetAccess返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PgDeal(AbstractModel):
    """订单详情

    """

    def __init__(self):
        """
        :param DealName: 订单名
        :type DealName: str
        :param OwnerUin: 所属用户
        :type OwnerUin: str
        :param Count: 订单涉及多少个实例
        :type Count: int
        :param PayMode: 付费模式。1-预付费；0-后付费
        :type PayMode: int
        :param FlowId: 异步任务流程ID
        :type FlowId: int
        :param DBInstanceIdSet: 实例ID数组
        :type DBInstanceIdSet: list of str
        """
        self.DealName = None
        self.OwnerUin = None
        self.Count = None
        self.PayMode = None
        self.FlowId = None
        self.DBInstanceIdSet = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Count = params.get("Count")
        self.PayMode = params.get("PayMode")
        self.FlowId = params.get("FlowId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReadOnlyGroup(AbstractModel):
    """只读组信息

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyGroupId: str
        :param ReadOnlyGroupName: 只读组名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnlyGroupName: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param MasterDBInstanceId: 主实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterDBInstanceId: str
        :param MinDelayEliminateReserve: 最小保留实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinDelayEliminateReserve: int
        :param MaxReplayLatency: 延迟空间大小阈值
        :type MaxReplayLatency: int
        :param ReplayLatencyEliminate: 延迟大小开关
        :type ReplayLatencyEliminate: int
        :param MaxReplayLag: 延迟时间大小阈值
        :type MaxReplayLag: float
        :param ReplayLagEliminate: 延迟时间开关
        :type ReplayLagEliminate: int
        :param VpcId: 虚拟网络id
        :type VpcId: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Region: 地域id
        :type Region: str
        :param Zone: 地区id
        :type Zone: str
        :param Status: 状态
        :type Status: str
        :param ReadOnlyDBInstanceList: 实例详细信息
        :type ReadOnlyDBInstanceList: list of DBInstance
        :param Rebalance: 自动负载均衡开关
        :type Rebalance: int
        :param DBInstanceNetInfo: 网络信息
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        """
        self.ReadOnlyGroupId = None
        self.ReadOnlyGroupName = None
        self.ProjectId = None
        self.MasterDBInstanceId = None
        self.MinDelayEliminateReserve = None
        self.MaxReplayLatency = None
        self.ReplayLatencyEliminate = None
        self.MaxReplayLag = None
        self.ReplayLagEliminate = None
        self.VpcId = None
        self.SubnetId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.ReadOnlyDBInstanceList = None
        self.Rebalance = None
        self.DBInstanceNetInfo = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        self.ReadOnlyGroupName = params.get("ReadOnlyGroupName")
        self.ProjectId = params.get("ProjectId")
        self.MasterDBInstanceId = params.get("MasterDBInstanceId")
        self.MinDelayEliminateReserve = params.get("MinDelayEliminateReserve")
        self.MaxReplayLatency = params.get("MaxReplayLatency")
        self.ReplayLatencyEliminate = params.get("ReplayLatencyEliminate")
        self.MaxReplayLag = params.get("MaxReplayLag")
        self.ReplayLagEliminate = params.get("ReplayLagEliminate")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        if params.get("ReadOnlyDBInstanceList") is not None:
            self.ReadOnlyDBInstanceList = []
            for item in params.get("ReadOnlyDBInstanceList"):
                obj = DBInstance()
                obj._deserialize(item)
                self.ReadOnlyDBInstanceList.append(obj)
        self.Rebalance = params.get("Rebalance")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupRequest(AbstractModel):
    """RebalanceReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        """
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebalanceReadOnlyGroupResponse(AbstractModel):
    """RebalanceReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """描述地域的编码和状态等信息

    """

    def __init__(self):
        """
        :param Region: 该地域对应的英文名称
        :type Region: str
        :param RegionName: 该地域对应的中文名称
        :type RegionName: str
        :param RegionId: 该地域对应的数字编号
        :type RegionId: int
        :param RegionState: 可用状态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :type RegionState: str
        :param SupportInternational: 该地域是否支持国际站售卖，0：不支持，1：支持
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportInternational: int
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None
        self.SupportInternational = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")
        self.SupportInternational = params.get("SupportInternational")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupRequest(AbstractModel):
    """RemoveDBInstanceFromReadOnlyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID
        :type DBInstanceId: str
        :param ReadOnlyGroupId: 只读组ID
        :type ReadOnlyGroupId: str
        """
        self.DBInstanceId = None
        self.ReadOnlyGroupId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.ReadOnlyGroupId = params.get("ReadOnlyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveDBInstanceFromReadOnlyGroupResponse(AbstractModel):
    """RemoveDBInstanceFromReadOnlyGroup返回参数结构体

    """

    def __init__(self):
        """
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


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param Period: 续费多少个月
        :type Period: int
        :param AutoVoucher: 是否自动使用代金券,1是,0否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券
        :type VoucherIds: list of str
        """
        self.DBInstanceId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealName: 订单名
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
        :param DBInstanceId: 实例ID，形如postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: 实例账户名
        :type UserName: str
        :param Password: UserName账户对应的新密码
        :type Password: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例ID，形如postgres-6r233v55
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
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
        :param FlowId: 异步流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ServerlessDBAccount(AbstractModel):
    """serverless账号描述

    """

    def __init__(self):
        """
        :param DBUser: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type DBUser: str
        :param DBPassword: 密码
注意：此字段可能返回 null，表示取不到有效值。
        :type DBPassword: str
        :param DBConnLimit: 连接数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type DBConnLimit: int
        """
        self.DBUser = None
        self.DBPassword = None
        self.DBConnLimit = None


    def _deserialize(self, params):
        self.DBUser = params.get("DBUser")
        self.DBPassword = params.get("DBPassword")
        self.DBConnLimit = params.get("DBConnLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBInstance(AbstractModel):
    """serverless实例描述

    """

    def __init__(self):
        """
        :param DBInstanceId: 实例id，唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceId: str
        :param DBInstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceName: str
        :param DBInstanceStatus: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceStatus: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param VpcId: 私有网络Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param DBCharset: 字符集
注意：此字段可能返回 null，表示取不到有效值。
        :type DBCharset: str
        :param DBVersion: 数据库版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DBVersion: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param DBInstanceNetInfo: 实例网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBInstanceNetInfo: list of ServerlessDBInstanceNetInfo
        :param DBAccountSet: 实例账户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBAccountSet: list of ServerlessDBAccount
        :param DBDatabaseList: 实例下的db信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DBDatabaseList: list of str
        :param TagList: 实例绑定的标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        """
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.DBInstanceNetInfo = None
        self.DBAccountSet = None
        self.DBDatabaseList = None
        self.TagList = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = ServerlessDBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        if params.get("DBAccountSet") is not None:
            self.DBAccountSet = []
            for item in params.get("DBAccountSet"):
                obj = ServerlessDBAccount()
                obj._deserialize(item)
                self.DBAccountSet.append(obj)
        self.DBDatabaseList = params.get("DBDatabaseList")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self.TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerlessDBInstanceNetInfo(AbstractModel):
    """serverless实例网络信息描述

    """

    def __init__(self):
        """
        :param Address: 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Ip: ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Port: 端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param NetType: 网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.Status = None
        self.NetType = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagRequest(AbstractModel):
    """SetAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 实例ID数组
        :type DBInstanceIdSet: list of str
        :param AutoRenewFlag: 续费标记。0-正常续费；1-自动续费；2-到期不续费
        :type AutoRenewFlag: int
        """
        self.DBInstanceIdSet = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewFlagResponse(AbstractModel):
    """SetAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 设置成功的实例个数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class SlowlogDetail(AbstractModel):
    """慢查询详情

    """

    def __init__(self):
        """
        :param TotalTime: 花费总时间
        :type TotalTime: float
        :param TotalCalls: 调用总次数
        :type TotalCalls: int
        :param NormalQueries: 脱敏后的慢SQL列表
        :type NormalQueries: list of NormalQueryItem
        """
        self.TotalTime = None
        self.TotalCalls = None
        self.NormalQueries = None


    def _deserialize(self, params):
        self.TotalTime = params.get("TotalTime")
        self.TotalCalls = params.get("TotalCalls")
        if params.get("NormalQueries") is not None:
            self.NormalQueries = []
            for item in params.get("NormalQueries"):
                obj = NormalQueryItem()
                obj._deserialize(item)
                self.NormalQueries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecInfo(AbstractModel):
    """描述某个地域下某个可用区的可售卖规格详细信息。

    """

    def __init__(self):
        """
        :param Region: 地域英文编码，对应RegionSet的Region字段
        :type Region: str
        :param Zone: 区域英文编码，对应ZoneSet的Zone字段
        :type Zone: str
        :param SpecItemInfoList: 规格详细信息列表
        :type SpecItemInfoList: list of SpecItemInfo
        """
        self.Region = None
        self.Zone = None
        self.SpecItemInfoList = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItemInfoList") is not None:
            self.SpecItemInfoList = []
            for item in params.get("SpecItemInfoList"):
                obj = SpecItemInfo()
                obj._deserialize(item)
                self.SpecItemInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItemInfo(AbstractModel):
    """描述一种规格的信息

    """

    def __init__(self):
        """
        :param SpecCode: 规格ID
        :type SpecCode: str
        :param Version: PostgreSQL的内核版本编号
        :type Version: str
        :param VersionName: 内核编号对应的完整版本名称
        :type VersionName: str
        :param Cpu: CPU核数
        :type Cpu: int
        :param Memory: 内存大小，单位：MB
        :type Memory: int
        :param MaxStorage: 该规格所支持最大存储容量，单位：GB
        :type MaxStorage: int
        :param MinStorage: 该规格所支持最小存储容量，单位：GB
        :type MinStorage: int
        :param Qps: 该规格的预估QPS
        :type Qps: int
        :param Pid: 该规格对应的计费ID
        :type Pid: int
        :param Type: 机器类型
        :type Type: str
        """
        self.SpecCode = None
        self.Version = None
        self.VersionName = None
        self.Cpu = None
        self.Memory = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Pid = None
        self.Type = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """实例绑定的标签信息，包含标签键TagKey和标签值TagValue

    """

    def __init__(self):
        """
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
        


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Memory: 升级后的实例内存大小，单位GB
        :type Memory: int
        :param Storage: 升级后的实例磁盘大小，单位GB
        :type Storage: int
        :param DBInstanceId: 实例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param AutoVoucher: 是否自动使用代金券,1是,0否，默认不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID列表，目前仅支持指定一张代金券
        :type VoucherIds: list of str
        :param ActivityId: 活动ID
        :type ActivityId: int
        """
        self.Memory = None
        self.Storage = None
        self.DBInstanceId = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.DBInstanceId = params.get("DBInstanceId")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.ActivityId = params.get("ActivityId")
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
        :param DealName: 交易名字。
        :type DealName: str
        :param BillId: 冻结流水号
        :type BillId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.BillId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.BillId = params.get("BillId")
        self.RequestId = params.get("RequestId")


class Xlog(AbstractModel):
    """数据库Xlog信息

    """

    def __init__(self):
        """
        :param Id: 备份文件唯一标识
        :type Id: int
        :param StartTime: 文件生成的开始时间
        :type StartTime: str
        :param EndTime: 文件生成的结束时间
        :type EndTime: str
        :param InternalAddr: 内网下载地址
        :type InternalAddr: str
        :param ExternalAddr: 外网下载地址
        :type ExternalAddr: str
        :param Size: 备份文件大小
        :type Size: int
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Size = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """描述可用区的编码和状态信息

    """

    def __init__(self):
        """
        :param Zone: 该可用区的英文名称
        :type Zone: str
        :param ZoneName: 该可用区的中文名称
        :type ZoneName: str
        :param ZoneId: 该可用区对应的数字编号
        :type ZoneId: int
        :param ZoneState: 可用状态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :type ZoneState: str
        :param ZoneSupportIpv6: 该可用区是否支持Ipv6
        :type ZoneSupportIpv6: int
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None
        self.ZoneSupportIpv6 = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")
        self.ZoneSupportIpv6 = params.get("ZoneSupportIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        