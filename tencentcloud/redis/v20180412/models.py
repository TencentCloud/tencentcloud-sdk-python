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


class ClearInstanceRequest(AbstractModel):
    """ClearInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Password: redis的实例密码
        :type Password: str
        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")


class ClearInstanceResponse(AbstractModel):
    """ClearInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务Id
        :type TaskId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 实例所属的可用区id
        :type ZoneId: int
        :param TypeId: 实例类型：2 – 主从版，5-单机版
        :type TypeId: int
        :param MemSize: 实例容量，单位MB， 取值大小以 查询售卖规格接口返回的规格为准
        :type MemSize: int
        :param GoodsNum: 实例数量，单次购买实例数量以 查询售卖规格接口返回的规格为准
        :type GoodsNum: int
        :param Period: 购买时长，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param Password: 实例密码，密码规则：1.长度为8-16个字符；2:至少包含字母、数字和字符!@^*()中的两种
        :type Password: str
        :param BillingMode: 付费方式:0-按量计费，1-包年包月。
        :type BillingMode: int
        :param VpcId: 私有网络ID，如果不传则默认选择基础网络，请使用私有网络列表 查询
        :type VpcId: str
        :param SubnetId: 基础网络下， subnetId无效； vpc子网下，取值以查询查询子网列表
        :type SubnetId: str
        :param ProjectId: 项目id，取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准
        :type ProjectId: int
        :param AutoRenew: 自动续费表示。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费
        :type AutoRenew: int
        :param SecurityGroupIdList: 安全组id数组
        :type SecurityGroupIdList: list of str
        :param VPort: 用户自定义的端口 不填则默认为6379
        :type VPort: int
        """
        self.ZoneId = None
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.Password = None
        self.BillingMode = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AutoRenew = None
        self.SecurityGroupIdList = None
        self.VPort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.Password = params.get("Password")
        self.BillingMode = params.get("BillingMode")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenew = params.get("AutoRenew")
        self.SecurityGroupIdList = params.get("SecurityGroupIdList")
        self.VPort = params.get("VPort")


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 交易的Id
        :type DealId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeAutoBackupConfigResponse(AbstractModel):
    """DescribeAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param AutoBackupType: 备份类型。自动备份类型： 1 “定时回档”
        :type AutoBackupType: int
        :param WeekDays: Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param TimePeriod: 时间段。
        :type TimePeriod: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class DescribeInstanceBackupsRequest(AbstractModel):
    """DescribeInstanceBackups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param Limit: 实例列表大小
        :type Limit: int
        :param Offset: 偏移量，取Limit整数倍
        :type Offset: int
        :param BeginTime: 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type BeginTime: str
        :param EndTime: 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type EndTime: str
        :param Status: 1：备份在流程中，2：备份正常，3：备份转RDB文件处理中，4：已完成RDB转换，-1：备份已过期，-2：备份已删除。
        :type Status: list of str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")


class DescribeInstanceBackupsResponse(AbstractModel):
    """DescribeInstanceBackups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 备份总数
        :type TotalCount: int
        :param BackupSet: 实例的备份数组
        :type BackupSet: list of RedisBackupSet
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self.BackupSet = []
            for item in params.get("BackupSet"):
                obj = RedisBackupSet()
                obj._deserialize(item)
                self.BackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 实例列表大小
        :type Limit: int
        :param Offset: 偏移量，取Limit整数倍
        :type Offset: int
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param OrderBy: 枚举范围： projectId,createtime,instancename,type,curDeadline
        :type OrderBy: str
        :param OrderType: 1倒序，0顺序，默认倒序
        :type OrderType: int
        :param VpcIds: 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络
        :type VpcIds: list of str
        :param SubnetIds: 子网ID数组，数组下标从0开始
        :type SubnetIds: list of str
        :param ProjectIds: 项目ID 组成的数组，数组下标从0开始
        :type ProjectIds: list of int
        :param SearchKey: 查找实例的ID。
        :type SearchKey: str
        :param RegionIds: 查询的Region的列表。
        :type RegionIds: list of int
        :param InstanceName: 实例名称
        :type InstanceName: str
        """
        self.Limit = None
        self.Offset = None
        self.InstanceId = None
        self.OrderBy = None
        self.OrderType = None
        self.VpcIds = None
        self.SubnetIds = None
        self.ProjectIds = None
        self.SearchKey = None
        self.RegionIds = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstanceId = params.get("InstanceId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.VpcIds = params.get("VpcIds")
        self.SubnetIds = params.get("SubnetIds")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")
        self.RegionIds = params.get("RegionIds")
        self.InstanceName = params.get("InstanceName")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例数
        :type TotalCount: int
        :param InstanceSet: 实例详细信息列表
        :type InstanceSet: list of InstanceSet
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceSet()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class InstanceSet(AbstractModel):
    """实例详细信息列表

    """

    def __init__(self):
        """
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param InstanceId: 实例串号
        :type InstanceId: str
        :param Appid: appid
        :type Appid: int
        :param ProjectId: 项目id
        :type ProjectId: int
        :param RegionId: 地域id 1--广州 4--上海 5-- 香港 6--多伦多 7--上海金融 8--北京 9-- 新加坡 11--深圳金融 15--美西（硅谷）
        :type RegionId: int
        :param ZoneId: 区域id
        :type ZoneId: int
        :param VpcId: vpc网络id
        :type VpcId: int
        :param SubnetId: vpc网络下子网id
        :type SubnetId: int
        :param Status: 实例当前状态，0：待初始化；1：实例在流程中；2：实例运行中；-2：实例已隔离
        :type Status: int
        :param WanIp: 实例vip
        :type WanIp: str
        :param Port: 实例端口号
        :type Port: int
        :param Createtime: 实例创建时间
        :type Createtime: str
        :param Size: 实例容量大小，单位：MB
        :type Size: float
        :param SizeUsed: 实例当前已使用容量，单位：MB
        :type SizeUsed: float
        :param Type: 实例类型，1：集群版；2：主从版
        :type Type: int
        :param AutoRenewFlag: 实例是否设置自动续费标识，1：设置自动续费；0：未设置自动续费
        :type AutoRenewFlag: int
        :param DeadlineTime: 实例到期时间
        :type DeadlineTime: str
        """
        self.InstanceName = None
        self.InstanceId = None
        self.Appid = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.WanIp = None
        self.Port = None
        self.Createtime = None
        self.Size = None
        self.SizeUsed = None
        self.Type = None
        self.AutoRenewFlag = None
        self.DeadlineTime = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.Appid = params.get("Appid")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.WanIp = params.get("WanIp")
        self.Port = params.get("Port")
        self.Createtime = params.get("Createtime")
        self.Size = params.get("Size")
        self.SizeUsed = params.get("SizeUsed")
        self.Type = params.get("Type")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeadlineTime = params.get("DeadlineTime")


class ManualBackupInstanceRequest(AbstractModel):
    """ManualBackupInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的实例ID，可通过 DescribeInstance接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param Remark: 备份的备注信息
        :type Remark: str
        """
        self.InstanceId = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Remark = params.get("Remark")


class ManualBackupInstanceResponse(AbstractModel):
    """ManualBackupInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModfiyInstancePasswordRequest(AbstractModel):
    """ModfiyInstancePassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param OldPassword: 实例旧密码
        :type OldPassword: str
        :param Password: 实例新密码
        :type Password: str
        """
        self.InstanceId = None
        self.OldPassword = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldPassword = params.get("OldPassword")
        self.Password = params.get("Password")


class ModfiyInstancePasswordResponse(AbstractModel):
    """ModfiyInstancePassword返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param WeekDays: 日期 Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday
        :type WeekDays: list of str
        :param TimePeriod: 时间段 00:00-01:00, 01:00-02:00...... 23:00-00:00
        :type TimePeriod: str
        :param AutoBackupType: 自动备份类型： 1 “定时回档”
        :type AutoBackupType: int
        """
        self.InstanceId = None
        self.WeekDays = None
        self.TimePeriod = None
        self.AutoBackupType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.AutoBackupType = params.get("AutoBackupType")


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param AutoBackupType: 自动备份类型： 1 “定时回档”
        :type AutoBackupType: int
        :param WeekDays: 日期Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param TimePeriod: 时间段 00:00-01:00, 01:00-02:00...... 23:00-00:00
        :type TimePeriod: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class RedisBackupSet(AbstractModel):
    """实例的备份数组

    """

    def __init__(self):
        """
        :param StartTime: 开始备份的时间
        :type StartTime: str
        :param BackupId: 备份ID
        :type BackupId: str
        :param BackupType: 备份类型。 manualBackupInstance：用户发起的手动备份； systemBackupInstance：凌晨系统发起的备份
        :type BackupType: str
        :param Status: 备份状态。  1:"备份被其它流程锁定";  2:"备份正常，没有被任何流程锁定";  -1:"备份已过期"； 3:"备份正在被导出";  4:"备份导出成功"
        :type Status: int
        :param Remark: 备份的备注信息
        :type Remark: str
        :param Locked: 备份是否被锁定，0：未被锁定；1：已被锁定
        :type Locked: int
        """
        self.StartTime = None
        self.BackupId = None
        self.BackupType = None
        self.Status = None
        self.Remark = None
        self.Locked = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.BackupId = params.get("BackupId")
        self.BackupType = params.get("BackupType")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.Locked = params.get("Locked")


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Period: 购买时长，单位：月
        :type Period: int
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.Period = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.InstanceId = params.get("InstanceId")


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 交易Id
        :type DealId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体

    """

    def __init__(self):
        """
        :param Password: 重置的密码
        :type Password: str
        :param InstanceId: Redis实例ID
        :type InstanceId: str
        """
        self.Password = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.InstanceId = params.get("InstanceId")


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 升级的实例Id
        :type InstanceId: str
        :param MemSize: 规格 单位 MB
        :type MemSize: int
        """
        self.InstanceId = None
        self.MemSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MemSize = params.get("MemSize")


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")