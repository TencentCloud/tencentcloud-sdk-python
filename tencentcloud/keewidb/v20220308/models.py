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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param SecurityGroupId: 要绑定的安全组 ID，类似sg-efil7***。
        :type SecurityGroupId: str
        :param InstanceIds: 实例 ID，格式如：kee-c1nl9***，支持指定多个实例。
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


class BackupInfo(AbstractModel):
    """实例的备份信息

    """

    def __init__(self):
        r"""
        :param StartTime: 备份开始时间。
        :type StartTime: str
        :param BackupId: 备份 ID。
        :type BackupId: str
        :param BackupType: 备份类型。<ul><li>1：手动备份，指根据业务运维排障需求，立即执行备份任务的操作。</li> <li>0：自动备份，指根据自动备份策略定时自动发起的备份任务。</li></ul>
        :type BackupType: str
        :param Remark: 备份的备注信息.
        :type Remark: str
        :param Status: 备份状态。  <ul><li>1：备份任务被其它流程锁定。</li><li>2：备份正常，没有被任何流程锁定。</li> <li>-1：备份已过期。</li><li>3：备份正在被导出。</li> <li>4：备份导出成功。</li></ul>
        :type Status: int
        :param Locked: 备份是否被锁定。<ul><li>0：未被锁定。</li><li>1：已被锁定。</li></ul>
        :type Locked: int
        """
        self.StartTime = None
        self.BackupId = None
        self.BackupType = None
        self.Remark = None
        self.Status = None
        self.Locked = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.BackupId = params.get("BackupId")
        self.BackupType = params.get("BackupType")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        self.Locked = params.get("Locked")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogInfo(AbstractModel):
    """实例增量备份信息

    """

    def __init__(self):
        r"""
        :param StartTime: 备份开始时间。
        :type StartTime: str
        :param EndTime: 备份结束时间。
        :type EndTime: str
        :param BackupId: 备份 ID。
        :type BackupId: str
        :param Filename: 备份文件名。
        :type Filename: str
        :param FileSize: 备份文件大小，单位：Byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        """
        self.StartTime = None
        self.EndTime = None
        self.BackupId = None
        self.Filename = None
        self.FileSize = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.BackupId = params.get("BackupId")
        self.Filename = params.get("Filename")
        self.FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceMasterRequest(AbstractModel):
    """ChangeInstanceMaster请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param NodeId: 副本节点 ID。
        :type NodeId: str
        """
        self.InstanceId = None
        self.NodeId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeInstanceMasterResponse(AbstractModel):
    """ChangeInstanceMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 异步任务 ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CleanUpInstanceRequest(AbstractModel):
    """CleanUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
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
        


class CleanUpInstanceResponse(AbstractModel):
    """CleanUpInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ClearInstanceRequest(AbstractModel):
    """ClearInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubhg****。
        :type InstanceId: str
        :param Password: 实例访问密码。
实例为免密访问，则无需设置该参数。
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
        


class ClearInstanceResponse(AbstractModel):
    """ClearInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateBackupManuallyRequest(AbstractModel):
    """CreateBackupManually请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待操作的实例 ID，可通过 DescribeInstance接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param Remark: 本次备份的备注信息。
        :type Remark: str
        :param StorageDays: 备份文件保存天数。0代表指定默认保留时间
        :type StorageDays: int
        """
        self.InstanceId = None
        self.Remark = None
        self.StorageDays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Remark = params.get("Remark")
        self.StorageDays = params.get("StorageDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupManuallyResponse(AbstractModel):
    """CreateBackupManually返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
        :param TypeId: 产品版本。
14：当前仅支持混合存储版。
        :type TypeId: int
        :param UniqVpcId: 私有网络唯一ID。
请登录控制台在私有网络列表查询，如：vpc-azlk3***。
        :type UniqVpcId: str
        :param UniqSubnetId: 私有网络所属子网唯一ID。
请登录控制台在私有网络列表查询，如：subnet-8abje***。
        :type UniqSubnetId: str
        :param BillingMode: 计费模式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :type BillingMode: int
        :param GoodsNum: 实例数量，单次最大购买数量以查询产品售卖规格返回的数量为准。
        :type GoodsNum: int
        :param Period: 选择包年包月计费模式（BillingMode 设置为1）时，您需要选择购买实例的时长。单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。按量计费（BillingMode 设置为0）实例该参数设置为1即可。
        :type Period: int
        :param ShardNum: 分片数量，支持选择3、5、6、8、9、10、12、15、16、18、20、21、24、25、27、30、32、33、35、36、39、40、42、45、48、50、51、54、55、56、57、60、63、64分片。
        :type ShardNum: int
        :param ReplicasNum: 副本数。当前仅支持设置1个副本节点，即每一个分片仅包含1个主节点与1个副本节点，数据主从实时热备。
        :type ReplicasNum: int
        :param MachineCpu: 计算cpu核心数。
        :type MachineCpu: int
        :param MachineMemory: 实例内存容量，单位：GB。
KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。
        :type MachineMemory: int
        :param ZoneId: 实例所属的可用区ID。<ul><li>具体取值，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106)获取。</li><li>参数<b>ZoneId</b>和<b>ZoneName</b>至少配置其中一个。</li></u>
        :type ZoneId: int
        :param ZoneName: 实例所属的可用区名称。<ul><li>具体取值，请参见[地域和可用区](https://cloud.tencent.com/document/product/239/4106)获取。</li><li>参数<b>ZoneId</b>和<b>ZoneName</b>至少配置其中一个。</li></u>
        :type ZoneName: str
        :param InstanceName: 创建实例的名称。
仅支持长度小于60的中文、英文或者数字，短划线"-"、下划线"_"。
        :type InstanceName: str
        :param NoAuth: 指明创建的实例是否需要支持免密访问。<ul><li>true：免密实例。</li><li>false：非免密实例，默认为非免密实例。此时，需要设置访问密码。</li></ul>
        :type NoAuth: bool
        :param Password: 实例访问密码。<ul><li>当参数<b>NoAuth</b>为<b>true</b>时，Password为无需设置，否则Password为必填参数。</li>
<li>密码复杂度要求：<ul><li>8-30个字符。</li><li>至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种。</li><li>不能以"/"开头。</li></ul></li></ul>
        :type Password: str
        :param VPort: 自定义端口。默认为6379，范围[1024,65535]。
        :type VPort: int
        :param AutoRenew: 包年包月计费的续费模式。<ul><li>0：默认状态，指手动续费。</li><li>1：自动续费。</li><li>2：到期不再续费。</ul>
        :type AutoRenew: int
        :param SecurityGroupIdList: 给实例设置安全组 ID 数组。
        :type SecurityGroupIdList: list of str
        :param ResourceTags: 给实例绑定标签。
        :type ResourceTags: list of ResourceTag
        :param MemSize: 混合存储版，单分片持久化内存容量，单位：GB。
KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。
        :type MemSize: int
        :param DiskSize: 每个分片硬盘的容量。单位：GB。
每一缓存分片容量，对应的磁盘容量范围不同。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。
        :type DiskSize: int
        :param ProjectId: 项目id，取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准。
        :type ProjectId: int
        """
        self.TypeId = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.BillingMode = None
        self.GoodsNum = None
        self.Period = None
        self.ShardNum = None
        self.ReplicasNum = None
        self.MachineCpu = None
        self.MachineMemory = None
        self.ZoneId = None
        self.ZoneName = None
        self.InstanceName = None
        self.NoAuth = None
        self.Password = None
        self.VPort = None
        self.AutoRenew = None
        self.SecurityGroupIdList = None
        self.ResourceTags = None
        self.MemSize = None
        self.DiskSize = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.BillingMode = params.get("BillingMode")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.ShardNum = params.get("ShardNum")
        self.ReplicasNum = params.get("ReplicasNum")
        self.MachineCpu = params.get("MachineCpu")
        self.MachineMemory = params.get("MachineMemory")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.InstanceName = params.get("InstanceName")
        self.NoAuth = params.get("NoAuth")
        self.Password = params.get("Password")
        self.VPort = params.get("VPort")
        self.AutoRenew = params.get("AutoRenew")
        self.SecurityGroupIdList = params.get("SecurityGroupIdList")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.MemSize = params.get("MemSize")
        self.DiskSize = params.get("DiskSize")
        self.ProjectId = params.get("ProjectId")
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
        r"""
        :param DealId: 交易 ID。
        :type DealId: str
        :param InstanceIds: 实例 ID 。
        :type InstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
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
        


class DescribeAutoBackupConfigResponse(AbstractModel):
    """DescribeAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param WeekDays: 自动备份的周期。包括：Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param TimePeriod: 自动备份时间段。
        :type TimePeriod: str
        :param BackupStorageDays: 全量备份文件保存天数。
        :type BackupStorageDays: int
        :param BinlogStorageDays: 增量备份文件保存天数。
        :type BinlogStorageDays: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WeekDays = None
        self.TimePeriod = None
        self.BackupStorageDays = None
        self.BinlogStorageDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.BackupStorageDays = params.get("BackupStorageDays")
        self.BinlogStorageDays = params.get("BinlogStorageDays")
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param InstanceId: 实例ID，格式如：kee-c1nl9***。
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
        :param Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param VIP: 安全组生效内网地址。
        :type VIP: str
        :param VPort: 安全组生效内网端口。
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


class DescribeInstanceBackupsRequest(AbstractModel):
    """DescribeInstanceBackups请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。
        :type InstanceId: str
        :param Limit: 每页输出的备份列表大小，即每页输出的备份文件的数量，默认值20，取值范围为[1,100]。
        :type Limit: int
        :param Offset: 备份列表分页偏移量，取Limit整数倍。
计算公式为offset=limit*(页码-1)。例如 limit=10，第1页offset就为0，第2页offset就为10，依次类推。
        :type Offset: int
        :param BeginTime: 查询备份文件的开始时间，格式如：2017-02-08 16:46:34。查询实例在 [BeginTime, EndTime] 时间段内的备份列表。
        :type BeginTime: str
        :param EndTime: 查询备份文件的结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内的备份列表。
        :type EndTime: str
        :param Status: 备份任务状态。<ul><li>1：备份在流程中。</li><li>2：备份正常。</li><li>3：备份转RDB文件处理中。</li><li>4：已完成RDB转换。</li><li>-1：备份已过期。</li><li>-2：备份已删除。</li></ul>
        :type Status: list of int
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceBackupsResponse(AbstractModel):
    """DescribeInstanceBackups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 备份文件总数。
        :type TotalCount: int
        :param BackupSet: 废弃字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSet: list of BinlogInfo
        :param BackupRecord: 实例备份信息列表。
        :type BackupRecord: list of BackupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupSet = None
        self.BackupRecord = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self.BackupSet = []
            for item in params.get("BackupSet"):
                obj = BinlogInfo()
                obj._deserialize(item)
                self.BackupSet.append(obj)
        if params.get("BackupRecord") is not None:
            self.BackupRecord = []
            for item in params.get("BackupRecord"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.BackupRecord.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceBinlogsRequest(AbstractModel):
    """DescribeInstanceBinlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Limit: 每页输出备份列表大小，默认大小20。
        :type Limit: int
        :param Offset: 分页偏移量，取Limit整数倍。
        :type Offset: int
        :param BeginTime: 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type BeginTime: str
        :param EndTime: 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type EndTime: str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceBinlogsResponse(AbstractModel):
    """DescribeInstanceBinlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 备份总数
        :type TotalCount: int
        :param BackupSet: 实例的备份信息数组
        :type BackupSet: list of BinlogInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = BinlogInfo()
                obj._deserialize(item)
                self.BackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceDealDetailRequest(AbstractModel):
    """DescribeInstanceDealDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param DealIds: 订单交易ID数组，即 [CreateInstances](https://cloud.tencent.com/document/api/1520/86207) 的输出参数DealId。
        :type DealIds: list of str
        """
        self.DealIds = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailResponse(AbstractModel):
    """DescribeInstanceDealDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealDetails: 订单详细信息
        :type DealDetails: list of TradeDealDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DealDetails") is not None:
            self.DealDetails = []
            for item in params.get("DealDetails"):
                obj = TradeDealDetail()
                obj._deserialize(item)
                self.DealDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param Limit: 每页输出的节点信息大小。默认为 20。
        :type Limit: int
        :param Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
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
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyCount: Proxy 节点数量。
        :type ProxyCount: int
        :param Proxy: Proxy 节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Proxy: list of ProxyNodeInfo
        :param RedisCount: Redis 节点数量。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
        :type RedisCount: int
        :param Redis: Redis 节点信息。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Redis: list of RedisNodeInfo
        :param TendisCount: Tendis 节点数量。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
        :type TendisCount: int
        :param Tendis: Tendis 节点信息。该参数仅为产品兼容性而保留，并不具有实际意义，可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tendis: list of InstanceNodeInfo
        :param KeeWiDBCount: KeewiDB 节点数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeeWiDBCount: int
        :param KeeWiDB: KeewiDB 节点信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeeWiDB: list of InstanceNodeInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyCount = None
        self.Proxy = None
        self.RedisCount = None
        self.Redis = None
        self.TendisCount = None
        self.Tendis = None
        self.KeeWiDBCount = None
        self.KeeWiDB = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyCount = params.get("ProxyCount")
        if params.get("Proxy") is not None:
            self.Proxy = []
            for item in params.get("Proxy"):
                obj = ProxyNodeInfo()
                obj._deserialize(item)
                self.Proxy.append(obj)
        self.RedisCount = params.get("RedisCount")
        if params.get("Redis") is not None:
            self.Redis = []
            for item in params.get("Redis"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self.Redis.append(obj)
        self.TendisCount = params.get("TendisCount")
        if params.get("Tendis") is not None:
            self.Tendis = []
            for item in params.get("Tendis"):
                obj = InstanceNodeInfo()
                obj._deserialize(item)
                self.Tendis.append(obj)
        self.KeeWiDBCount = params.get("KeeWiDBCount")
        if params.get("KeeWiDB") is not None:
            self.KeeWiDB = []
            for item in params.get("KeeWiDB"):
                obj = InstanceNodeInfo()
                obj._deserialize(item)
                self.KeeWiDB.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param Limit: 每页输出的参数列表大小。默认为 20，最多输出100条。
        :type Limit: int
        :param Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
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
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 修改历史记录总数。
        :type TotalCount: int
        :param InstanceParamHistory: 修改历史记录信息。
        :type InstanceParamHistory: list of InstanceParamHistory
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceParamHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceParamHistory") is not None:
            self.InstanceParamHistory = []
            for item in params.get("InstanceParamHistory"):
                obj = InstanceParamHistory()
                obj._deserialize(item)
                self.InstanceParamHistory.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
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
        :param TotalCount: 实例参数总数量。
        :type TotalCount: int
        :param InstanceEnumParam: 实例枚举类型参数数组。
        :type InstanceEnumParam: list of InstanceEnumParam
        :param InstanceIntegerParam: 实例整型参数数组。
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param InstanceTextParam: 实例字符型参数数组。
        :type InstanceTextParam: list of InstanceTextParam
        :param InstanceMultiParam: 实例多选项型参数数组。
        :type InstanceMultiParam: list of InstanceMultiParam
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceEnumParam = None
        self.InstanceIntegerParam = None
        self.InstanceTextParam = None
        self.InstanceMultiParam = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceEnumParam") is not None:
            self.InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self.InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self.InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self.InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self.InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self.InstanceTextParam.append(obj)
        if params.get("InstanceMultiParam") is not None:
            self.InstanceMultiParam = []
            for item in params.get("InstanceMultiParam"):
                obj = InstanceMultiParam()
                obj._deserialize(item)
                self.InstanceMultiParam.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceReplicasRequest(AbstractModel):
    """DescribeInstanceReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
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
        


class DescribeInstanceReplicasResponse(AbstractModel):
    """DescribeInstanceReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例所有节点数量，包括主节点、副本节点。
        :type TotalCount: int
        :param ReplicaGroups: 实例节点信息。
        :type ReplicaGroups: list of ReplicaGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReplicaGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReplicaGroups") is not None:
            self.ReplicaGroups = []
            for item in params.get("ReplicaGroups"):
                obj = ReplicaGroup()
                obj._deserialize(item)
                self.ReplicaGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 每页输出的实例列表的大小，即每页输出的实例数量，默认值20，取值范围为[1,1000]。
        :type Limit: int
        :param Offset: 分页偏移量，取Limit整数倍。
计算公式为offset=limit*(页码-1)。例如 limit=10，第1页offset就为0，第2页offset就为10，依次类推。
        :type Offset: int
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param OrderBy: 排序依据。枚举范围如下所示。 <ul><li>projectId：实例按照项目ID排序。</li><li>createtime：实例按照创建时间排序。</li><li>instancename：实例按照实例名称排序。</li><li>type：实例按照类型排序。</li><li>curDeadline：实例按照到期时间排序。</li></ul>
        :type OrderBy: str
        :param OrderType: 排序方式。<ul><li>1：倒序。默认为倒序。</li><li>0：顺序。</li></ul>
        :type OrderType: int
        :param VpcIds: 私有网络ID数组。数组下标从0开始，如果不传则默认选择基础网络，如：47525
        :type VpcIds: list of str
        :param SubnetIds: 子网ID数组，数组下标从0开始，如：56854
        :type SubnetIds: list of str
        :param ProjectIds: 项目ID 组成的数组，数组下标从0开始
        :type ProjectIds: list of int
        :param SearchKey: 查找关键字，可输入实例的ID或者实例名称。
        :type SearchKey: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param UniqVpcIds: 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：vpc-sad23jfdfk
        :type UniqVpcIds: list of str
        :param UniqSubnetIds: 子网ID数组，数组下标从0开始，如：subnet-fdj24n34j2
        :type UniqSubnetIds: list of str
        :param Status: 实例状态。<ul><li>0：待初始化。</li><li>1：流程中。</li><li>2：运行中。</li><li>-2：已隔离。</li><li>-3：待删除。</li></ul>
        :type Status: list of int
        :param AutoRenew: 包年包月计费的续费模式。<ul><li>0：默认状态，指手动续费。</li><li>1：自动续费。</li><li>2：到期不再续费。</ul>
        :type AutoRenew: list of int
        :param BillingMode: 计费模式。<ul><li>postpaid：按量计费。</li><li>prepaid：包年包月。</li></ul>
        :type BillingMode: str
        :param Type: 实例类型。<ul><li>13：标准版。</li><li>14：集群版。</li></ul>
        :type Type: int
        :param SearchKeys: 搜索关键词：支持实例 ID、实例名称、私有网络IP地址。
        :type SearchKeys: list of str
        :param TypeList: 内部参数，用户可忽略。
        :type TypeList: list of int
        :param MonitorVersion: 内部参数，用户可忽略。
        :type MonitorVersion: str
        :param InstanceTags: 根据标签的 Key 和 Value 筛选资源。该参数不配置或者数组设置为空值，则不根据标签进行过滤。
        :type InstanceTags: :class:`tencentcloud.keewidb.v20220308.models.InstanceTagInfo`
        :param TagKeys: 根据标签的 Key 筛选资源，该参数不配置或者数组设置为空值，则不根据标签Key进行过滤。
        :type TagKeys: list of str
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
        self.InstanceName = None
        self.UniqVpcIds = None
        self.UniqSubnetIds = None
        self.Status = None
        self.AutoRenew = None
        self.BillingMode = None
        self.Type = None
        self.SearchKeys = None
        self.TypeList = None
        self.MonitorVersion = None
        self.InstanceTags = None
        self.TagKeys = None


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
        self.InstanceName = params.get("InstanceName")
        self.UniqVpcIds = params.get("UniqVpcIds")
        self.UniqSubnetIds = params.get("UniqSubnetIds")
        self.Status = params.get("Status")
        self.AutoRenew = params.get("AutoRenew")
        self.BillingMode = params.get("BillingMode")
        self.Type = params.get("Type")
        self.SearchKeys = params.get("SearchKeys")
        self.TypeList = params.get("TypeList")
        self.MonitorVersion = params.get("MonitorVersion")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = InstanceTagInfo()
            self.InstanceTags._deserialize(params.get("InstanceTags"))
        self.TagKeys = params.get("TagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例数
        :type TotalCount: int
        :param InstanceSet: 实例详细信息列表
        :type InstanceSet: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaintenanceWindowRequest(AbstractModel):
    """DescribeMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubhg***。
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
        


class DescribeMaintenanceWindowResponse(AbstractModel):
    """DescribeMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 维护时间窗起始时间，如：03:00。
        :type StartTime: str
        :param EndTime: 维护时间窗结束时间，如：06:00。
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo请求参数结构体

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionSet: 地域售卖信息
        :type RegionSet: list of RegionConf
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionConf()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称。该产品固定为 keewidb。
        :type Product: str
        :param ProjectId: 项目 ID。
登录 [账号中心](https://console.cloud.tencent.com/developer)，在<b>项目管理</b>中可获取项目 ID。
        :type ProjectId: int
        :param Offset: 分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param Limit: 每页安全组的数量限制。默认为 20，最多输出100条。
        :type Limit: int
        :param SearchKey: 搜索关键词，支持根据安全组 ID 或者安全组名称搜索。
        :type SearchKey: str
        """
        self.Product = None
        self.ProjectId = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.ProjectId = params.get("ProjectId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
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
        :param Groups: 安全组规则。
        :type Groups: list of SecurityGroup
        :param Total: 符合条件的安全组总数量。
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


class DescribeProxySlowLogRequest(AbstractModel):
    """DescribeProxySlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubhgouj
        :type InstanceId: str
        :param BeginTime: 开始时间。
        :type BeginTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MinQueryTime: 慢查询平均执行时间阈值。<ul><li>单位：毫秒。</li><li>取值范围：10、20、30、40、50。</li></ul>
        :type MinQueryTime: int
        :param Limit: 每个页面大小，即每个页面输出慢日志的数量。取值范围为：10、20、30、40、50，默认为 20。
        :type Limit: int
        :param Offset: 页面偏移量，取Limit整数倍，计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self.InstanceId = None
        self.BeginTime = None
        self.EndTime = None
        self.MinQueryTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.MinQueryTime = params.get("MinQueryTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySlowLogResponse(AbstractModel):
    """DescribeProxySlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 慢查询总数。
        :type TotalCount: int
        :param InstanceProxySlowLogDetail: 慢查询详情。
        :type InstanceProxySlowLogDetail: list of InstanceProxySlowlogDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceProxySlowLogDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceProxySlowLogDetail") is not None:
            self.InstanceProxySlowLogDetail = []
            for item in params.get("InstanceProxySlowLogDetail"):
                obj = InstanceProxySlowlogDetail()
                obj._deserialize(item)
                self.InstanceProxySlowLogDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 任务状态。<ul><li>preparing：待执行。</li><li>running：执行中。</li><li>succeed：成功。</li><li>failed：失败。</li><li>error：执行出错。</li></ul>
        :type Status: str
        :param StartTime: 任务开始时间。
        :type StartTime: str
        :param TaskType: 任务类型。
        :type TaskType: str
        :param InstanceId: 实例的ID。
        :type InstanceId: str
        :param TaskMessage: 任务信息，错误时显示错误信息。执行中与成功则为空值。
        :type TaskMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.StartTime = None
        self.TaskType = None
        self.InstanceId = None
        self.TaskMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.InstanceId = params.get("InstanceId")
        self.TaskMessage = params.get("TaskMessage")
        self.RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param Limit: 每页输出的任务列表大小。默认为 20，最多输出100条。
        :type Limit: int
        :param Offset: Offset：分页偏移量，取Limit整数倍。计算公式：offset=limit*(页码-1)。
        :type Offset: int
        :param ProjectIds: 项目ID。
        :type ProjectIds: list of int
        :param TaskTypes: 任务类型。可设置为：FLOW_CREATE、FLOW_SETPWD、FLOW_CLOSE等。
        :type TaskTypes: list of str
        :param BeginTime: 起始时间。
        :type BeginTime: str
        :param EndTime: 终止时间。
        :type EndTime: str
        :param TaskStatus: 任务状态。
        :type TaskStatus: list of int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Limit = None
        self.Offset = None
        self.ProjectIds = None
        self.TaskTypes = None
        self.BeginTime = None
        self.EndTime = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProjectIds = params.get("ProjectIds")
        self.TaskTypes = params.get("TaskTypes")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 任务总数。
        :type TotalCount: int
        :param Tasks: 任务详细信息列表。
        :type Tasks: list of TaskInfoDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfoDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTendisSlowLogRequest(AbstractModel):
    """DescribeTendisSlowLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param BeginTime: 开始时间。
        :type BeginTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MinQueryTime: 慢查询平均执行时间阈值。<ul><li>单位：毫秒。</li><li>取值范围：10、20、30、40、50。</li></ul>
        :type MinQueryTime: int
        :param Limit: 每个页面大小，即每个页面输出慢日志的数量。取值范围为：10、20、30、40、50。默认为 20。
        :type Limit: int
        :param Offset: 页面偏移量，取Limit整数倍，计算公式：offset=limit*(页码-1)。
        :type Offset: int
        """
        self.InstanceId = None
        self.BeginTime = None
        self.EndTime = None
        self.MinQueryTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.MinQueryTime = params.get("MinQueryTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTendisSlowLogResponse(AbstractModel):
    """DescribeTendisSlowLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param TendisSlowLogDetail: 慢查询详情。
        :type TendisSlowLogDetail: list of TendisSlowLogDetail
        :param TotalCount: 慢查询总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TendisSlowLogDetail = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TendisSlowLogDetail") is not None:
            self.TendisSlowLogDetail = []
            for item in params.get("TendisSlowLogDetail"):
                obj = TendisSlowLogDetail()
                obj._deserialize(item)
                self.TendisSlowLogDetail.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DestroyPostpaidInstanceRequest(AbstractModel):
    """DestroyPostpaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
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
        


class DestroyPostpaidInstanceResponse(AbstractModel):
    """DestroyPostpaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DestroyPrepaidInstanceRequest(AbstractModel):
    """DestroyPrepaidInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
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
        


class DestroyPrepaidInstanceResponse(AbstractModel):
    """DestroyPrepaidInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealId: 交易ID。
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param SecurityGroupId: 要绑定的安全组 ID，类似sg-efil****。
        :type SecurityGroupId: str
        :param InstanceIds: 实例 ID，格式如：kee-c1nl****，支持指定多个实例。
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


class Inbound(AbstractModel):
    """安全组入站规则

    """

    def __init__(self):
        r"""
        :param Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param Desc: 描述。
        :type Desc: str
        :param IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param PortRange: 端口。
        :type PortRange: str
        :param ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self.Action = None
        self.AddressModule = None
        self.CidrIp = None
        self.Desc = None
        self.IpProtocol = None
        self.PortRange = None
        self.ServiceModule = None
        self.Id = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.AddressModule = params.get("AddressModule")
        self.CidrIp = params.get("CidrIp")
        self.Desc = params.get("Desc")
        self.IpProtocol = params.get("IpProtocol")
        self.PortRange = params.get("PortRange")
        self.ServiceModule = params.get("ServiceModule")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    """实例枚举类型参数描述

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名
        :type ParamName: str
        :param ValueType: 参数类型：enum
        :type ValueType: str
        :param NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param DefaultValue: 参数默认值
        :type DefaultValue: str
        :param CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param Tips: 参数说明
        :type Tips: str
        :param EnumValue: 参数可取值
        :type EnumValue: list of str
        :param Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.EnumValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.EnumValue = params.get("EnumValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        r"""
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Appid: 用户的Appid。
        :type Appid: int
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        :param RegionId: 地域ID。<ul><li>1：广州。</li><li>4：上海。</li><li>8：北京。</li></ul>
        :type RegionId: int
        :param ZoneId: 可用区 ID。
        :type ZoneId: int
        :param VpcId: VPC 网络 ID， 如：75101。该参数当前暂保留，可忽略。
        :type VpcId: int
        :param Status: 实例当前状态。<ul><li>0：待初始化。</li><li>1：实例在流程中。</li><li>2：实例运行中。</li><li>-2：实例已隔离。</li><li>-3：实例待删除。</li></ul>
        :type Status: int
        :param SubnetId: VPC 网络下子网 ID， 如：46315。该参数当前暂保留，可忽略。
        :type SubnetId: int
        :param WanIp: 实例 VIP。
        :type WanIp: str
        :param Port: 实例端口号。
        :type Port: int
        :param Createtime: 实例创建时间。
        :type Createtime: str
        :param Size: 实例持久内存总容量大小，单位：MB。
        :type Size: float
        :param Type: 实例类型。<ul><li>13：标准版。</li><li>14：集群版。</li></ul>
        :type Type: int
        :param AutoRenewFlag: 实例是否设置自动续费标识。<ul><li>1：设置自动续费。</li><li>0：未设置自动续费。</li></ul>
        :type AutoRenewFlag: int
        :param DeadlineTime: 实例到期时间。
        :type DeadlineTime: str
        :param Engine: 存储引擎。
        :type Engine: str
        :param ProductType: 产品类型。<ul><li>standalone ：标准版。</li><li>cluster ：集群版。</li></ul>
        :type ProductType: str
        :param UniqVpcId: VPC 网络 ID， 如：vpc-fk33jsf4****。
        :type UniqVpcId: str
        :param UniqSubnetId: VPC 网络下子网 ID，如：subnet-fd3j6l3****。
        :type UniqSubnetId: str
        :param BillingMode: 计费模式。<ul><li>0：按量计费。</li><li>1：包年包月。</li></ul>
        :type BillingMode: int
        :param InstanceTitle: 实例运行状态描述：如”实例运行中“。
        :type InstanceTitle: str
        :param OfflineTime: 计划下线时间。
        :type OfflineTime: str
        :param SubStatus: 流程中的实例，返回子状态。
        :type SubStatus: int
        :param Tags: 反亲和性标签
        :type Tags: list of str
        :param RedisShardSize: 分片大小。
        :type RedisShardSize: int
        :param RedisShardNum: 分片数量。
        :type RedisShardNum: int
        :param RedisReplicasNum: 副本数量。
        :type RedisReplicasNum: int
        :param PriceId: 计费 ID。
        :type PriceId: int
        :param CloseTime: 隔离时间。
        :type CloseTime: str
        :param SlaveReadWeight: 从节点读取权重。
        :type SlaveReadWeight: int
        :param InstanceTags: 实例关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTags: list of InstanceTagInfo
        :param ProjectName: 项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param NoAuth: 是否为免密实例；<ul><li>true：免密实例。</li><li>false：非免密实例。</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type NoAuth: bool
        :param ClientLimit: 客户端连接数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimit: int
        :param DtsStatus: DTS状态（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DtsStatus: int
        :param NetLimit: 分片带宽上限，单位 MB。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetLimit: int
        :param PasswordFree: 免密实例标识（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PasswordFree: int
        :param ReadOnly: 实例只读标识（内部参数，用户可忽略）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: int
        :param Vip6: 内部参数，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip6: str
        :param RemainBandwidthDuration: 内部参数，用户可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainBandwidthDuration: str
        :param DiskSize: 实例的磁盘容量大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param MonitorVersion: 监控版本。<ul><li>1m：分钟粒度监控。</li><li>5s：5秒粒度监控。</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type MonitorVersion: str
        :param ClientLimitMin: 客户端最大连接数可设置的最小值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimitMin: int
        :param ClientLimitMax: 客户端最大连接数可设置的最大值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientLimitMax: int
        :param NodeSet: 实例的节点详细信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of NodeInfo
        :param Region: 实例所在的地域信息，比如ap-guangzhou。
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param MachineMemory: 实例内存容量，单位：GB。KeeWiDB 内存容量
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineMemory: int
        :param DiskShardSize: 单分片磁盘大小，单位：MB
        :type DiskShardSize: int
        :param DiskShardNum: 3
        :type DiskShardNum: int
        :param DiskReplicasNum: 1
        :type DiskReplicasNum: int
        """
        self.InstanceName = None
        self.InstanceId = None
        self.Appid = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.Status = None
        self.SubnetId = None
        self.WanIp = None
        self.Port = None
        self.Createtime = None
        self.Size = None
        self.Type = None
        self.AutoRenewFlag = None
        self.DeadlineTime = None
        self.Engine = None
        self.ProductType = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.BillingMode = None
        self.InstanceTitle = None
        self.OfflineTime = None
        self.SubStatus = None
        self.Tags = None
        self.RedisShardSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.PriceId = None
        self.CloseTime = None
        self.SlaveReadWeight = None
        self.InstanceTags = None
        self.ProjectName = None
        self.NoAuth = None
        self.ClientLimit = None
        self.DtsStatus = None
        self.NetLimit = None
        self.PasswordFree = None
        self.ReadOnly = None
        self.Vip6 = None
        self.RemainBandwidthDuration = None
        self.DiskSize = None
        self.MonitorVersion = None
        self.ClientLimitMin = None
        self.ClientLimitMax = None
        self.NodeSet = None
        self.Region = None
        self.MachineMemory = None
        self.DiskShardSize = None
        self.DiskShardNum = None
        self.DiskReplicasNum = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.Appid = params.get("Appid")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.WanIp = params.get("WanIp")
        self.Port = params.get("Port")
        self.Createtime = params.get("Createtime")
        self.Size = params.get("Size")
        self.Type = params.get("Type")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Engine = params.get("Engine")
        self.ProductType = params.get("ProductType")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.BillingMode = params.get("BillingMode")
        self.InstanceTitle = params.get("InstanceTitle")
        self.OfflineTime = params.get("OfflineTime")
        self.SubStatus = params.get("SubStatus")
        self.Tags = params.get("Tags")
        self.RedisShardSize = params.get("RedisShardSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.PriceId = params.get("PriceId")
        self.CloseTime = params.get("CloseTime")
        self.SlaveReadWeight = params.get("SlaveReadWeight")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.ProjectName = params.get("ProjectName")
        self.NoAuth = params.get("NoAuth")
        self.ClientLimit = params.get("ClientLimit")
        self.DtsStatus = params.get("DtsStatus")
        self.NetLimit = params.get("NetLimit")
        self.PasswordFree = params.get("PasswordFree")
        self.ReadOnly = params.get("ReadOnly")
        self.Vip6 = params.get("Vip6")
        self.RemainBandwidthDuration = params.get("RemainBandwidthDuration")
        self.DiskSize = params.get("DiskSize")
        self.MonitorVersion = params.get("MonitorVersion")
        self.ClientLimitMin = params.get("ClientLimitMin")
        self.ClientLimitMax = params.get("ClientLimitMax")
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.Region = params.get("Region")
        self.MachineMemory = params.get("MachineMemory")
        self.DiskShardSize = params.get("DiskShardSize")
        self.DiskShardNum = params.get("DiskShardNum")
        self.DiskReplicasNum = params.get("DiskReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    """实例整型参数描述

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名
        :type ParamName: str
        :param ValueType: 参数类型：integer
        :type ValueType: str
        :param NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param DefaultValue: 参数默认值
        :type DefaultValue: str
        :param CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param Tips: 参数说明
        :type Tips: str
        :param Min: 参数最小值
        :type Min: str
        :param Max: 参数最大值
        :type Max: str
        :param Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        :param Unit: 参数单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.Min = None
        self.Max = None
        self.Status = None
        self.Unit = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.Status = params.get("Status")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMultiParam(AbstractModel):
    """实例多选项类型参数描述

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名
        :type ParamName: str
        :param ValueType: 参数类型：multi
        :type ValueType: str
        :param NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param DefaultValue: 参数默认值
        :type DefaultValue: str
        :param CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param Tips: 参数说明
        :type Tips: str
        :param EnumValue: 参数说明
        :type EnumValue: list of str
        :param Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.EnumValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.EnumValue = params.get("EnumValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNodeInfo(AbstractModel):
    """实例节点信息

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID
        :type NodeId: str
        :param NodeRole: 节点角色
        :type NodeRole: str
        """
        self.NodeId = None
        self.NodeRole = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeRole = params.get("NodeRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParam(AbstractModel):
    """实例参数

    """

    def __init__(self):
        r"""
        :param Key: 设置参数的名字
        :type Key: str
        :param Value: 设置参数的值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParamHistory(AbstractModel):
    """实例参数修改历史

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名称
        :type ParamName: str
        :param PreValue: 修改前值
        :type PreValue: str
        :param NewValue: 修改后值
        :type NewValue: str
        :param Status: 状态：1-参数配置修改中；2-参数配置修改成功；3-参数配置修改失败
        :type Status: int
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.ParamName = None
        self.PreValue = None
        self.NewValue = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.PreValue = params.get("PreValue")
        self.NewValue = params.get("NewValue")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceProxySlowlogDetail(AbstractModel):
    """代理慢查询详情

    """

    def __init__(self):
        r"""
        :param Duration: 慢查询耗时
        :type Duration: int
        :param Client: 客户端地址
        :type Client: str
        :param Command: 命令
        :type Command: str
        :param CommandLine: 详细命令行信息
        :type CommandLine: str
        :param ExecuteTime: 执行时间
        :type ExecuteTime: str
        """
        self.Duration = None
        self.Client = None
        self.Command = None
        self.CommandLine = None
        self.ExecuteTime = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.Client = params.get("Client")
        self.Command = params.get("Command")
        self.CommandLine = params.get("CommandLine")
        self.ExecuteTime = params.get("ExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    """实例标签信息

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
        


class InstanceTextParam(AbstractModel):
    """实例字符型参数描述

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名
        :type ParamName: str
        :param ValueType: 参数类型：text
        :type ValueType: str
        :param NeedRestart: 修改后是否需要重启：true，false
        :type NeedRestart: str
        :param DefaultValue: 参数默认值
        :type DefaultValue: str
        :param CurrentValue: 当前运行参数值
        :type CurrentValue: str
        :param Tips: 参数说明
        :type Tips: str
        :param TextValue: 参数可取值
        :type TextValue: list of str
        :param Status: 参数状态, 1: 修改中， 2：修改完成
        :type Status: int
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.TextValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.TextValue = params.get("TextValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeeWiDBNode(AbstractModel):
    """KeeWiDB节点的运行信息

    """

    def __init__(self):
        r"""
        :param NodeId: 节点的序列ID。
        :type NodeId: str
        :param Status: 节点的状态。
        :type Status: str
        :param Role: 节点角色。
        :type Role: str
        """
        self.NodeId = None
        self.Status = None
        self.Role = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Status = params.get("Status")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param WeekDays: 备份周期。可设置为 Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday，该参数暂不支持修改、
        :type WeekDays: list of str
        :param TimePeriod: 备份任务执行时间段。
可设置的格式为一个整点到下一个整点。例如：00:00-01:00、01:00-02:00、21:00-22:00、23:00-00:00等。
        :type TimePeriod: str
        """
        self.InstanceId = None
        self.WeekDays = None
        self.TimePeriod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param BackupStorageDays: 增量备份文件保存天数。
        :type BackupStorageDays: int
        :param BinlogStorageDays: 全量备份文件保存天数。
        :type BinlogStorageDays: int
        :param TimePeriod: 备份时间段。
        :type TimePeriod: str
        :param WeekDays: 备份周期。Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupStorageDays = None
        self.BinlogStorageDays = None
        self.TimePeriod = None
        self.WeekDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupStorageDays = params.get("BackupStorageDays")
        self.BinlogStorageDays = params.get("BinlogStorageDays")
        self.TimePeriod = params.get("TimePeriod")
        self.WeekDays = params.get("WeekDays")
        self.RequestId = params.get("RequestId")


class ModifyConnectionConfigRequest(AbstractModel):
    """ModifyConnectionConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param Bandwidth: 单分片附加带宽，取值范围[0,512]，单位：MB。
<ul><li>开启副本只读时，实例总带宽  = 单分片附加带宽 * 分片数 + 标准带宽 * 分片数 * Max ([只读副本数量, 1])，标准架构的分片数 = 1。</li><li>没有开启副本只读时，实例总带宽 = 单分片附加带宽 * 分片数 + 标准带宽 * 分片数，标准架构的分片数 = 1。</li></ul>
        :type Bandwidth: int
        :param ClientLimit: 单分片的总连接数。
<ul>默认为10000，整个实例的最大连接数为单个分片的最大连接数 x 分片数量。标准架构分片数量为1。
<li>关闭副本只读：每个分片的最大连接数的取值范围为[10000,40000]。</li><li>开启副本只读：每个分片的最大连接数的取值范围为 [10000,10000 x (副本数 + 3)]。</li></ul>
        :type ClientLimit: int
        """
        self.InstanceId = None
        self.Bandwidth = None
        self.ClientLimit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Bandwidth = params.get("Bandwidth")
        self.ClientLimit = params.get("ClientLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConnectionConfigResponse(AbstractModel):
    """ModifyConnectionConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 数据库引擎名称：keewidb。
        :type Product: str
        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组 ID 组成的数组。
        :type SecurityGroupIds: list of str
        :param InstanceId: 实例ID，格式如：kee-c1nl****。
        :type InstanceId: str
        """
        self.Product = None
        self.SecurityGroupIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceId = params.get("InstanceId")
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


class ModifyInstanceParamsRequest(AbstractModel):
    """ModifyInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param InstanceParams: 实例修改的参数列表。
        :type InstanceParams: list of InstanceParam
        """
        self.InstanceId = None
        self.InstanceParams = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self.InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self.InstanceParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamsResponse(AbstractModel):
    """ModifyInstanceParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param Changed: 修改是否成功。<ul><li>true：修改成功。</li><li>false：修改失败。</li></ul>
        :type Changed: bool
        :param TaskId: 任务 ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Changed = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Changed = params.get("Changed")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operation: 修改实例操作。<ul><li>rename：表示实例重命名。</li><li>modifyProject：修改实例所属项目。</li><li>modifyAutoRenew：修改实例续费模式。</li></ul>
        :type Operation: str
        :param InstanceIds: 实例 ID 数组。
        :type InstanceIds: list of str
        :param InstanceNames: 实例的新名称。
        :type InstanceNames: list of str
        :param ProjectId: 实例新的项目 ID。
        :type ProjectId: int
        :param AutoRenews: 包年包月计费的续费模式。<b>InstanceIds</b>数组和<b>AutoRenews</b>数组中的修改值对应。<ul><li>0：默认状态，指手动续费。</li><li>1：自动续费。</li><li>2：到期不再续费。</ul>
        :type AutoRenews: list of int
        """
        self.Operation = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.ProjectId = None
        self.AutoRenews = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenews = params.get("AutoRenews")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMaintenanceWindowRequest(AbstractModel):
    """ModifyMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param StartTime: 维护时间窗起始时间，如：03:00。
        :type StartTime: str
        :param EndTime: 维护时间窗结束时间，如：06:00。
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceWindowResponse(AbstractModel):
    """ModifyMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 执行结果。<ul><li>success：修改成功。 </li> <li>failed：修改失败。</li></ul>
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    """ModifyNetworkConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID，如：kee-6ubh****。
        :type InstanceId: str
        :param Operation: 操作类型。<ul><li>changeVip：修改实例私有网络。</li><li>changeVpc：修改实例私有网络所属子网。</li><li>changeBaseToVpc：基础网络转为私有网络。</li></ul>
        :type Operation: str
        :param Vip: 修改后的 VIP 地址。
当参数<b>Operation</b>为<b>changeVip</b>时，需设置实例修改后的 VIP 地址。该参数不配置，则自动分配。
        :type Vip: str
        :param VpcId: 修改后的私有网络 ID。
当参数<b>Operation</b>为<b>changeVip</b>或者为<b>changeBaseToVpc</b>时，务必设置实例修改后的私有网络 ID。
        :type VpcId: str
        :param SubnetId: 修改后的所属子网 ID。
当参数<b>Operation</b>为<b>changeVpc</b>或者为<b>changeBaseToVpc</b>时，务必设置实例修改后的子网 ID。
        :type SubnetId: str
        :param Recycle: 原 VIP 保留时长。
单位：天。取值范围：0、1、2、3、7、15。
        :type Recycle: int
        """
        self.InstanceId = None
        self.Operation = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.Recycle = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Operation = params.get("Operation")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Recycle = params.get("Recycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkConfigResponse(AbstractModel):
    """ModifyNetworkConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 执行状态。<ul><li>true：执行成功。</li><li>false：执行失败。</li></ul>
        :type Status: bool
        :param SubnetId: 修改后的子网 ID。
        :type SubnetId: str
        :param VpcId: 修改后的私有网络 ID。
        :type VpcId: str
        :param Vip: 修改后的 VIP 地址。
        :type Vip: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.SubnetId = None
        self.VpcId = None
        self.Vip = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Vip = params.get("Vip")
        self.RequestId = params.get("RequestId")


class NodeInfo(AbstractModel):
    """描述实例的主节点或者副本节点信息

    """

    def __init__(self):
        r"""
        :param NodeType: 节点类型，0 为主节点，1 为副本节点
        :type NodeType: int
        :param NodeId: 主节点或者副本节点的ID，创建时不需要传递此参数。
        :type NodeId: int
        :param ZoneId: 主节点或者副本节点的可用区ID
        :type ZoneId: int
        :param ZoneName: 主节点或者副本节点的可用区名称
        :type ZoneName: str
        """
        self.NodeType = None
        self.NodeId = None
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.NodeId = params.get("NodeId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Outbound(AbstractModel):
    """安全组出站规则

    """

    def __init__(self):
        r"""
        :param Action: 策略，ACCEPT或者DROP。
        :type Action: str
        :param AddressModule: 地址组id代表的地址集合。
        :type AddressModule: str
        :param CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。
        :type CidrIp: str
        :param Desc: 描述。
        :type Desc: str
        :param IpProtocol: 网络协议，支持udp、tcp等。
        :type IpProtocol: str
        :param PortRange: 端口。
        :type PortRange: str
        :param ServiceModule: 服务组id代表的协议和端口集合。
        :type ServiceModule: str
        :param Id: 安全组id代表的地址集合。
        :type Id: str
        """
        self.Action = None
        self.AddressModule = None
        self.CidrIp = None
        self.Desc = None
        self.IpProtocol = None
        self.PortRange = None
        self.ServiceModule = None
        self.Id = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.AddressModule = params.get("AddressModule")
        self.CidrIp = params.get("CidrIp")
        self.Desc = params.get("Desc")
        self.IpProtocol = params.get("IpProtocol")
        self.PortRange = params.get("PortRange")
        self.ServiceModule = params.get("ServiceModule")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductConf(AbstractModel):
    """产品规格信息

    """

    def __init__(self):
        r"""
        :param Type: 产品类型，13-KeewiDB标准架构，14-KeewiDB集群架构
        :type Type: int
        :param TypeName: KeewiDB标准架构，KeewiDB集群架构
        :type TypeName: str
        :param MinBuyNum: 购买时的最小数量
        :type MinBuyNum: int
        :param MaxBuyNum: 购买时的最大数量
        :type MaxBuyNum: int
        :param Saleout: 产品是否售罄
        :type Saleout: bool
        :param Engine: 产品引擎，keewidb
        :type Engine: str
        :param Version: 兼容版本，Redis-2.8，Redis-3.2，Redis-4.0
        :type Version: str
        :param ReplicaNum: 副本数量
        :type ReplicaNum: list of str
        :param PayMode: 支持的计费模式，1-包年包月，0-按量计费
        :type PayMode: str
        """
        self.Type = None
        self.TypeName = None
        self.MinBuyNum = None
        self.MaxBuyNum = None
        self.Saleout = None
        self.Engine = None
        self.Version = None
        self.ReplicaNum = None
        self.PayMode = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        self.MinBuyNum = params.get("MinBuyNum")
        self.MaxBuyNum = params.get("MaxBuyNum")
        self.Saleout = params.get("Saleout")
        self.Engine = params.get("Engine")
        self.Version = params.get("Version")
        self.ReplicaNum = params.get("ReplicaNum")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodeInfo(AbstractModel):
    """Proxy节点信息

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodeInfo(AbstractModel):
    """Redis节点信息

    """

    def __init__(self):
        r"""
        :param NodeId: 节点ID
        :type NodeId: str
        :param NodeRole: 节点角色
        :type NodeRole: str
        :param ClusterId: 分片ID
        :type ClusterId: int
        :param ZoneId: 可用区ID
        :type ZoneId: int
        """
        self.NodeId = None
        self.NodeRole = None
        self.ClusterId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeRole = params.get("NodeRole")
        self.ClusterId = params.get("ClusterId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionConf(AbstractModel):
    """地域售卖信息

    """

    def __init__(self):
        r"""
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名称
        :type RegionName: str
        :param RegionShortName: 地域简称
        :type RegionShortName: str
        :param Area: 地域所在大区名称
        :type Area: str
        :param ZoneSet: 可用区信息
        :type ZoneSet: list of ZoneCapacityConf
        """
        self.RegionId = None
        self.RegionName = None
        self.RegionShortName = None
        self.Area = None
        self.ZoneSet = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RegionShortName = params.get("RegionShortName")
        self.Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Period: 购买时长。单位：月。取值为 [1,2,3,4,5,6,7,8,9,10,11,12,24,36,48,60]。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealId: 交易 ID。
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ReplicaGroup(AbstractModel):
    """实例副本组信息

    """

    def __init__(self):
        r"""
        :param GroupId: 节点 ID。
        :type GroupId: int
        :param GroupName: 节点组的名称，主节点为空。
        :type GroupName: str
        :param ZoneId: 节点的可用区ID，比如ap-guangzhou-1。
        :type ZoneId: str
        :param Role: 节点组角色。<ul><li>master：为主节点。</li><li>replica：为副本节点。</li></ul>
        :type Role: str
        :param KeeWiDBNodes: 节点组节点列表。
        :type KeeWiDBNodes: list of KeeWiDBNode
        """
        self.GroupId = None
        self.GroupName = None
        self.ZoneId = None
        self.Role = None
        self.KeeWiDBNodes = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ZoneId = params.get("ZoneId")
        self.Role = params.get("Role")
        if params.get("KeeWiDBNodes") is not None:
            self.KeeWiDBNodes = []
            for item in params.get("KeeWiDBNodes"):
                obj = KeeWiDBNode()
                obj._deserialize(item)
                self.KeeWiDBNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param Password: 设置新密码。<ul><li>当参数<b>NoAuth</b>设置为<b>true</b>，切换为免密实例时，可不设置该参数。</li><li>密码复杂度要求：<ul><li>长度8 - 30位, 推荐使用12位以上的密码。</li><li>不能以"/"开头。</li>
<li>至少包含以下两项：<ul><li>小写字母a - z</li><li>大写字母A - Z</li><li>数字0 - 9</li><li>()~!@#$%^&*-+=_|{}[]:;<>,.?/</li></ul></li></ul></li></ul>
        :type Password: str
        :param NoAuth: 标识实例是否切换免密认证。<ul><li>false：由免密码认证方式切换为密码认证实例。默认为false。</li><li>true：由密码认证方式切换为免密码认证的方式。</li></ul>
        :type NoAuth: bool
        """
        self.InstanceId = None
        self.Password = None
        self.NoAuth = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        self.NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID。
<b>说明：</b>修改密码时的任务ID，如果切换免密访问或者非免密码实例，则无需关注此返回值。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """实例绑定标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签 Key。
        :type TagKey: str
        :param TagValue: 标签 Value。
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
    """安全组规则

    """

    def __init__(self):
        r"""
        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss。
        :type CreateTime: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param SecurityGroupId: 安全组ID。
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全组名称。
        :type SecurityGroupName: str
        :param SecurityGroupRemark: 安全组备注。
        :type SecurityGroupRemark: str
        :param Outbound: 出站规则。
        :type Outbound: list of Outbound
        :param Inbound: 入站规则。
        :type Inbound: list of Inbound
        """
        self.CreateTime = None
        self.ProjectId = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.Outbound = None
        self.Inbound = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self.Outbound.append(obj)
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartUpInstanceRequest(AbstractModel):
    """StartUpInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
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
        


class StartUpInstanceResponse(AbstractModel):
    """StartUpInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TaskInfoDetail(AbstractModel):
    """任务信息详情

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param InstanceId: 实例Id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param Progress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Progress: float
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Result: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: int
        :param OperatorUin: 操作者用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUin: str
        """
        self.TaskId = None
        self.StartTime = None
        self.TaskType = None
        self.InstanceName = None
        self.InstanceId = None
        self.ProjectId = None
        self.Progress = None
        self.EndTime = None
        self.Result = None
        self.OperatorUin = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.ProjectId = params.get("ProjectId")
        self.Progress = params.get("Progress")
        self.EndTime = params.get("EndTime")
        self.Result = params.get("Result")
        self.OperatorUin = params.get("OperatorUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisSlowLogDetail(AbstractModel):
    """实例慢查询详情

    """

    def __init__(self):
        r"""
        :param ExecuteTime: 执行时间
        :type ExecuteTime: str
        :param Duration: 慢查询耗时（毫秒）
        :type Duration: int
        :param Command: 命令
        :type Command: str
        :param CommandLine: 详细命令行信息
        :type CommandLine: str
        :param Node: 节点ID
        :type Node: str
        """
        self.ExecuteTime = None
        self.Duration = None
        self.Command = None
        self.CommandLine = None
        self.Node = None


    def _deserialize(self, params):
        self.ExecuteTime = params.get("ExecuteTime")
        self.Duration = params.get("Duration")
        self.Command = params.get("Command")
        self.CommandLine = params.get("CommandLine")
        self.Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeDealDetail(AbstractModel):
    """订单交易信息

    """

    def __init__(self):
        r"""
        :param DealId: 订单号ID，调用云API时使用此ID	
        :type DealId: str
        :param DealName: 长订单ID，反馈订单问题给官方客服使用此ID	
        :type DealName: str
        :param ZoneId: 可用区id
        :type ZoneId: int
        :param GoodsNum: 订单关联的实例数
        :type GoodsNum: int
        :param Creater: 创建用户uin
        :type Creater: str
        :param CreatTime: 订单创建时间
        :type CreatTime: str
        :param OverdueTime: 订单超时时间
        :type OverdueTime: str
        :param EndTime: 订单完成时间
        :type EndTime: str
        :param Status: 订单状态 1：未支付 2:已支付，未发货 3:发货中 4:发货成功 5:发货失败 6:已退款 7:已关闭订单 8:订单过期 9:订单已失效 10:产品已失效 11:代付拒绝 12:支付中
        :type Status: int
        :param Description: 订单状态描述
        :type Description: str
        :param Price: 订单实际总价，单位：分
        :type Price: float
        :param InstanceIds: 实例ID
        :type InstanceIds: list of str
        """
        self.DealId = None
        self.DealName = None
        self.ZoneId = None
        self.GoodsNum = None
        self.Creater = None
        self.CreatTime = None
        self.OverdueTime = None
        self.EndTime = None
        self.Status = None
        self.Description = None
        self.Price = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.ZoneId = params.get("ZoneId")
        self.GoodsNum = params.get("GoodsNum")
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.OverdueTime = params.get("OverdueTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Price = params.get("Price")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param MemSize: 配置变更后，每个分片持久化内存容量，单位：GB。
<ul><li>KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type MemSize: int
        :param MachineCpu: CPU 核数。
        :type MachineCpu: int
        :param MachineMemory: 实例内存容量，单位：GB。
<ul><li>KeeWiDB 内存容量<b>MachineMemory</b>与持久内存容量<b>MemSize</b>为固定搭配，即2GB内存，固定分配8GB的持久内存，不可选择。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type MachineMemory: int
        :param ShardNum: 配置变更后，分片数量。
<ul><li>增加后分片的数量务必为增加之前数量的整数倍。分片数量支持选择3、5、6、8、9、10、12、15、16、18、20、21、24、25、27、30、32、33、35、36、39、40、42、45、48、50、51、54、55、56、57、60、63、64分片。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type ShardNum: int
        :param DiskSize: 配置变更后，每个分片硬盘的容量。单位：GB。
<ul><li>每一缓存分片容量，对应的磁盘容量范围不同。具体信息，请参见[产品规格](https://cloud.tencent.com/document/product/1520/80808)。</li><li>变更实例内存、持久化内存与磁盘、变更实例的分片数量，每次只能变更一项。</li></ul>
        :type DiskSize: int
        """
        self.InstanceId = None
        self.MemSize = None
        self.MachineCpu = None
        self.MachineMemory = None
        self.ShardNum = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MemSize = params.get("MemSize")
        self.MachineCpu = params.get("MachineCpu")
        self.MachineMemory = params.get("MachineMemory")
        self.ShardNum = params.get("ShardNum")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealId: 交易ID。
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ZoneCapacityConf(AbstractModel):
    """可用区内产品售卖信息

    """

    def __init__(self):
        r"""
        :param ZoneId: 可用区ID
        :type ZoneId: str
        :param ZoneName: 可用区名称
        :type ZoneName: str
        :param IsSaleout: 可用区是否售罄
        :type IsSaleout: bool
        :param IsDefault: 是否为默认可用区
        :type IsDefault: bool
        :param NetWorkType: 网络类型：basenet -- 基础网络；vpcnet -- VPC网络
        :type NetWorkType: list of str
        :param ProductSet: 产品规格等信息
        :type ProductSet: list of ProductConf
        :param OldZoneId: Int类型可用区ID
        :type OldZoneId: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.IsSaleout = None
        self.IsDefault = None
        self.NetWorkType = None
        self.ProductSet = None
        self.OldZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.IsSaleout = params.get("IsSaleout")
        self.IsDefault = params.get("IsDefault")
        self.NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self.ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self.ProductSet.append(obj)
        self.OldZoneId = params.get("OldZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        