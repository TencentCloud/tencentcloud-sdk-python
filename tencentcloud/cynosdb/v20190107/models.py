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


class Account(AbstractModel):
    """数据库账号信息

    """

    def __init__(self):
        """
        :param AccountName: 数据库账号名
        :type AccountName: str
        :param Description: 数据库账号描述
        :type Description: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Host: 主机
        :type Host: str
        """
        self.AccountName = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Host = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddInstancesRequest(AbstractModel):
    """AddInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Cpu: Cpu核数
        :type Cpu: int
        :param Memory: 内存
        :type Memory: int
        :param ReadOnlyCount: 新增只读实例数
        :type ReadOnlyCount: int
        :param InstanceGrpId: 实例组ID，在已有RO组中新增实例时使用，不传则新增RO组
        :type InstanceGrpId: str
        :param VpcId: 所属VPC网络ID
        :type VpcId: str
        :param SubnetId: 所属子网ID
        :type SubnetId: str
        :param Port: 新增RO组时使用的Port
        :type Port: int
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param OrderSource: 订单来源
        :type OrderSource: str
        """
        self.ClusterId = None
        self.Cpu = None
        self.Memory = None
        self.ReadOnlyCount = None
        self.InstanceGrpId = None
        self.VpcId = None
        self.SubnetId = None
        self.Port = None
        self.InstanceName = None
        self.AutoVoucher = None
        self.DbType = None
        self.OrderSource = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.ReadOnlyCount = params.get("ReadOnlyCount")
        self.InstanceGrpId = params.get("InstanceGrpId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Port = params.get("Port")
        self.InstanceName = params.get("InstanceName")
        self.AutoVoucher = params.get("AutoVoucher")
        self.DbType = params.get("DbType")
        self.OrderSource = params.get("OrderSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddInstancesResponse(AbstractModel):
    """AddInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 冻结流水，一次开通一个冻结流水。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param DealNames: 后付费订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param ResourceIds: 发货资源id列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.DealNames = None
        self.ResourceIds = None
        self.BigDealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.DealNames = params.get("DealNames")
        self.ResourceIds = params.get("ResourceIds")
        self.BigDealIds = params.get("BigDealIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Addr(AbstractModel):
    """数据库地址

    """

    def __init__(self):
        """
        :param IP: IP
        :type IP: str
        :param Port: 端口
        :type Port: int
        """
        self.IP = None
        self.Port = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BackupFileInfo(AbstractModel):
    """备份文件信息

    """

    def __init__(self):
        """
        :param SnapshotId: 快照文件ID，用于回滚
        :type SnapshotId: int
        :param FileName: 快照文件名
        :type FileName: str
        :param FileSize: 快照文件大小
        :type FileSize: int
        :param StartTime: 快照备份开始时间
        :type StartTime: str
        :param FinishTime: 快照备份完成时间
        :type FinishTime: str
        :param BackupType: 备份类型：snapshot，快照备份；timepoint，时间点备份
        :type BackupType: str
        :param BackupMethod: 备份方式：auto，自动备份；manual，手动备份
        :type BackupMethod: str
        :param BackupStatus: 备份文件状态：success：备份成功；fail：备份失败；creating：备份文件创建中；deleting：备份文件删除中
        :type BackupStatus: str
        :param SnapshotTime: 备份文件时间
        :type SnapshotTime: str
        """
        self.SnapshotId = None
        self.FileName = None
        self.FileSize = None
        self.StartTime = None
        self.FinishTime = None
        self.BackupType = None
        self.BackupMethod = None
        self.BackupStatus = None
        self.SnapshotTime = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.StartTime = params.get("StartTime")
        self.FinishTime = params.get("FinishTime")
        self.BackupType = params.get("BackupType")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupStatus = params.get("BackupStatus")
        self.SnapshotTime = params.get("SnapshotTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BillingResourceInfo(AbstractModel):
    """计费资源信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterInstanceDetail(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param InstanceType: 引擎类型
        :type InstanceType: str
        :param InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param InstanceStatusDesc: 实例状态描述
        :type InstanceStatusDesc: str
        :param InstanceCpu: cpu核数
        :type InstanceCpu: int
        :param InstanceMemory: 内存
        :type InstanceMemory: int
        :param InstanceStorage: 硬盘
        :type InstanceStorage: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceType = None
        self.InstanceStatus = None
        self.InstanceStatusDesc = None
        self.InstanceCpu = None
        self.InstanceMemory = None
        self.InstanceStorage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatus = params.get("InstanceStatus")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.InstanceCpu = params.get("InstanceCpu")
        self.InstanceMemory = params.get("InstanceMemory")
        self.InstanceStorage = params.get("InstanceStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClustersRequest(AbstractModel):
    """CreateClusters请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区
        :type Zone: str
        :param VpcId: 所属VPC网络ID
        :type VpcId: str
        :param SubnetId: 所属子网ID
        :type SubnetId: str
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param DbVersion: 数据库版本，取值范围: 
<li> MYSQL可选值：5.7 </li>
        :type DbVersion: str
        :param ProjectId: 所属项目ID
        :type ProjectId: int
        :param Cpu: 普通实例Cpu核数
        :type Cpu: int
        :param Memory: 普通实例内存
        :type Memory: int
        :param Storage: 存储
        :type Storage: int
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param AdminPassword: 账号密码(8-64个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()~）中的两种)
        :type AdminPassword: str
        :param Port: 端口，默认5432
        :type Port: int
        :param PayMode: 计费模式，按量计费：0，包年包月：1。默认按量计费。
        :type PayMode: int
        :param Count: 购买个数，目前只支持传1（不传默认为1）
        :type Count: int
        :param RollbackStrategy: 回档类型：
noneRollback：不回档；
snapRollback，快照回档；
timeRollback，时间点回档
        :type RollbackStrategy: str
        :param RollbackId: 快照回档，表示snapshotId；时间点回档，表示queryId，为0，表示需要判断时间点是否有效
        :type RollbackId: int
        :param OriginalClusterId: 回档时，传入源集群ID，用于查找源poolId
        :type OriginalClusterId: str
        :param ExpectTime: 时间点回档，指定时间；快照回档，快照时间
        :type ExpectTime: str
        :param ExpectTimeThresh: 时间点回档，指定时间允许范围
        :type ExpectTimeThresh: int
        :param StorageLimit: 普通实例存储上限，单位GB
        :type StorageLimit: int
        :param InstanceCount: 实例数量
        :type InstanceCount: int
        :param TimeSpan: 包年包月购买时长
        :type TimeSpan: int
        :param TimeUnit: 包年包月购买时长单位
        :type TimeUnit: str
        :param AutoRenewFlag: 包年包月购买是否自动续费
        :type AutoRenewFlag: int
        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param HaCount: 实例数量（该参数已不再使用，只做存量兼容处理）
        :type HaCount: int
        :param OrderSource: 订单来源
        :type OrderSource: str
        :param ResourceTags: 集群创建需要绑定的tag数组信息
        :type ResourceTags: list of Tag
        :param DbMode: Db类型
当DbType为MYSQL时可选(默认NORMAL)：
<li>NORMAL</li>
<li>SERVERLESS</li>
        :type DbMode: str
        :param MinCpu: 当DbMode为SEVERLESS时必填
cpu最小值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MinCpu: float
        :param MaxCpu: 当DbMode为SEVERLESS时必填：
cpu最大值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MaxCpu: float
        :param AutoPause: 当DbMode为SEVERLESS时，指定集群是否自动暂停，可选范围
<li>yes</li>
<li>no</li>
默认值:yes
        :type AutoPause: str
        :param AutoPauseDelay: 当DbMode为SEVERLESS时，指定集群自动暂停的延迟，单位秒，可选范围[600,691200]
默认值:600
        :type AutoPauseDelay: int
        """
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.DbType = None
        self.DbVersion = None
        self.ProjectId = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.ClusterName = None
        self.AdminPassword = None
        self.Port = None
        self.PayMode = None
        self.Count = None
        self.RollbackStrategy = None
        self.RollbackId = None
        self.OriginalClusterId = None
        self.ExpectTime = None
        self.ExpectTimeThresh = None
        self.StorageLimit = None
        self.InstanceCount = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.AutoRenewFlag = None
        self.AutoVoucher = None
        self.HaCount = None
        self.OrderSource = None
        self.ResourceTags = None
        self.DbMode = None
        self.MinCpu = None
        self.MaxCpu = None
        self.AutoPause = None
        self.AutoPauseDelay = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.ProjectId = params.get("ProjectId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ClusterName = params.get("ClusterName")
        self.AdminPassword = params.get("AdminPassword")
        self.Port = params.get("Port")
        self.PayMode = params.get("PayMode")
        self.Count = params.get("Count")
        self.RollbackStrategy = params.get("RollbackStrategy")
        self.RollbackId = params.get("RollbackId")
        self.OriginalClusterId = params.get("OriginalClusterId")
        self.ExpectTime = params.get("ExpectTime")
        self.ExpectTimeThresh = params.get("ExpectTimeThresh")
        self.StorageLimit = params.get("StorageLimit")
        self.InstanceCount = params.get("InstanceCount")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoVoucher = params.get("AutoVoucher")
        self.HaCount = params.get("HaCount")
        self.OrderSource = params.get("OrderSource")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DbMode = params.get("DbMode")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.AutoPause = params.get("AutoPause")
        self.AutoPauseDelay = params.get("AutoPauseDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClustersResponse(AbstractModel):
    """CreateClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param ResourceIds: 资源ID列表（异步发货可能无法返回该字段, 强烈建议使用dealNames字段查询接口DescribeResourcesByDealName获取异步发货的资源ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param ClusterIds: 集群ID列表（异步发货可能不返回该字段, 强烈建议使用dealNames查询接口DescribeResourcesByDealName获取异步发货的集群ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIds: list of str
        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.DealNames = None
        self.ResourceIds = None
        self.ClusterIds = None
        self.BigDealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.DealNames = params.get("DealNames")
        self.ResourceIds = params.get("ResourceIds")
        self.ClusterIds = params.get("ClusterIds")
        self.BigDealIds = params.get("BigDealIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CynosdbCluster(AbstractModel):
    """集群信息

    """

    def __init__(self):
        """
        :param Status: 集群状态
        :type Status: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Zone: 可用区
        :type Zone: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Region: 地域
        :type Region: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceNum: 实例数
        :type InstanceNum: int
        :param Uin: 用户uin
        :type Uin: str
        :param DbType: 引擎类型
        :type DbType: str
        :param AppId: 用户appid
        :type AppId: int
        :param StatusDesc: 集群状态描述
        :type StatusDesc: str
        :param CreateTime: 集群创建时间
        :type CreateTime: str
        :param PayMode: 付费模式。0-按量计费，1-包年包月
        :type PayMode: int
        :param PeriodEndTime: 截止时间
        :type PeriodEndTime: str
        :param Vip: 集群读写vip
        :type Vip: str
        :param Vport: 集群读写vport
        :type Vport: int
        :param ProjectID: 项目id
        :type ProjectID: int
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param CynosVersion: cynos内核版本
        :type CynosVersion: str
        :param StorageLimit: 存储容量
        :type StorageLimit: int
        :param RenewFlag: 续费标志
        :type RenewFlag: int
        :param ProcessingTask: 正在处理的任务
        :type ProcessingTask: str
        :param Tasks: 集群的任务数组
        :type Tasks: list of ObjectTask
        :param ResourceTags: 集群绑定的tag数组
        :type ResourceTags: list of Tag
        :param DbMode: Db类型(NORMAL, SERVERLESS)
        :type DbMode: str
        :param ServerlessStatus: 当Db类型为SERVERLESS时，serverless集群状态，可选值:
resume
pause
        :type ServerlessStatus: str
        """
        self.Status = None
        self.UpdateTime = None
        self.Zone = None
        self.ClusterName = None
        self.Region = None
        self.DbVersion = None
        self.ClusterId = None
        self.InstanceNum = None
        self.Uin = None
        self.DbType = None
        self.AppId = None
        self.StatusDesc = None
        self.CreateTime = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.Vip = None
        self.Vport = None
        self.ProjectID = None
        self.VpcId = None
        self.SubnetId = None
        self.CynosVersion = None
        self.StorageLimit = None
        self.RenewFlag = None
        self.ProcessingTask = None
        self.Tasks = None
        self.ResourceTags = None
        self.DbMode = None
        self.ServerlessStatus = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.UpdateTime = params.get("UpdateTime")
        self.Zone = params.get("Zone")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.DbVersion = params.get("DbVersion")
        self.ClusterId = params.get("ClusterId")
        self.InstanceNum = params.get("InstanceNum")
        self.Uin = params.get("Uin")
        self.DbType = params.get("DbType")
        self.AppId = params.get("AppId")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.ProjectID = params.get("ProjectID")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CynosVersion = params.get("CynosVersion")
        self.StorageLimit = params.get("StorageLimit")
        self.RenewFlag = params.get("RenewFlag")
        self.ProcessingTask = params.get("ProcessingTask")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DbMode = params.get("DbMode")
        self.ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CynosdbClusterDetail(AbstractModel):
    """集群详情详细信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Region: 地域
        :type Region: str
        :param Status: 状态
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        :param VpcName: VPC名称
        :type VpcName: str
        :param VpcId: vpc唯一id
        :type VpcId: str
        :param SubnetName: 子网名称
        :type SubnetName: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Charset: 字符集
        :type Charset: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param DbType: 数据库类型
        :type DbType: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param UsedStorage: 使用容量
        :type UsedStorage: int
        :param RoAddr: 读写分离Vport
        :type RoAddr: list of Addr
        :param InstanceSet: 实例信息
        :type InstanceSet: list of ClusterInstanceDetail
        :param PayMode: 付费模式
        :type PayMode: int
        :param PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param Vip: vip地址
        :type Vip: str
        :param Vport: vport端口
        :type Vport: int
        :param ProjectID: 项目id
        :type ProjectID: int
        :param Zone: 可用区
        :type Zone: str
        :param ResourceTags: 实例绑定的tag数组信息
        :type ResourceTags: list of Tag
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.Status = None
        self.StatusDesc = None
        self.VpcName = None
        self.VpcId = None
        self.SubnetName = None
        self.SubnetId = None
        self.Charset = None
        self.CreateTime = None
        self.DbType = None
        self.DbVersion = None
        self.UsedStorage = None
        self.RoAddr = None
        self.InstanceSet = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.Vip = None
        self.Vport = None
        self.ProjectID = None
        self.Zone = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.SubnetId = params.get("SubnetId")
        self.Charset = params.get("Charset")
        self.CreateTime = params.get("CreateTime")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.UsedStorage = params.get("UsedStorage")
        if params.get("RoAddr") is not None:
            self.RoAddr = []
            for item in params.get("RoAddr"):
                obj = Addr()
                obj._deserialize(item)
                self.RoAddr.append(obj)
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ClusterInstanceDetail()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.ProjectID = params.get("ProjectID")
        self.Zone = params.get("Zone")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CynosdbInstance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        """
        :param Uin: 用户Uin
        :type Uin: str
        :param AppId: 用户AppId
        :type AppId: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param Status: 实例状态
        :type Status: str
        :param StatusDesc: 实例状态中文描述
        :type StatusDesc: str
        :param DbType: 数据库类型
        :type DbType: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param Cpu: Cpu，单位：核
        :type Cpu: int
        :param Memory: 内存，单位：GB
        :type Memory: int
        :param Storage: 存储量，单位：GB
        :type Storage: int
        :param InstanceType: 实例类型
        :type InstanceType: str
        :param InstanceRole: 实例当前角色
        :type InstanceRole: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param VpcId: VPC网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Vip: 实例内网IP
        :type Vip: str
        :param Vport: 实例内网端口
        :type Vport: int
        :param PayMode: 付费模式
        :type PayMode: int
        :param PeriodEndTime: 实例过期时间
        :type PeriodEndTime: str
        :param DestroyDeadlineText: 销毁期限
        :type DestroyDeadlineText: str
        :param IsolateTime: 隔离时间
        :type IsolateTime: str
        :param NetType: 网络类型
        :type NetType: int
        :param WanDomain: 外网域名
        :type WanDomain: str
        :param WanIP: 外网IP
        :type WanIP: str
        :param WanPort: 外网端口
        :type WanPort: int
        :param WanStatus: 外网状态
        :type WanStatus: str
        :param DestroyTime: 实例销毁时间
        :type DestroyTime: str
        :param CynosVersion: Cynos内核版本
        :type CynosVersion: str
        :param ProcessingTask: 正在处理的任务
        :type ProcessingTask: str
        :param RenewFlag: 续费标志
        :type RenewFlag: int
        :param MinCpu: serverless实例cpu下限
        :type MinCpu: float
        :param MaxCpu: serverless实例cpu上限
        :type MaxCpu: float
        :param ServerlessStatus: serverless实例状态, 可选值：
resume
pause
        :type ServerlessStatus: str
        """
        self.Uin = None
        self.AppId = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.StatusDesc = None
        self.DbType = None
        self.DbVersion = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.InstanceType = None
        self.InstanceRole = None
        self.UpdateTime = None
        self.CreateTime = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vport = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.DestroyDeadlineText = None
        self.IsolateTime = None
        self.NetType = None
        self.WanDomain = None
        self.WanIP = None
        self.WanPort = None
        self.WanStatus = None
        self.DestroyTime = None
        self.CynosVersion = None
        self.ProcessingTask = None
        self.RenewFlag = None
        self.MinCpu = None
        self.MaxCpu = None
        self.ServerlessStatus = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceType = params.get("InstanceType")
        self.InstanceRole = params.get("InstanceRole")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.DestroyDeadlineText = params.get("DestroyDeadlineText")
        self.IsolateTime = params.get("IsolateTime")
        self.NetType = params.get("NetType")
        self.WanDomain = params.get("WanDomain")
        self.WanIP = params.get("WanIP")
        self.WanPort = params.get("WanPort")
        self.WanStatus = params.get("WanStatus")
        self.DestroyTime = params.get("DestroyTime")
        self.CynosVersion = params.get("CynosVersion")
        self.ProcessingTask = params.get("ProcessingTask")
        self.RenewFlag = params.get("RenewFlag")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CynosdbInstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        """
        :param Uin: 用户Uin
        :type Uin: str
        :param AppId: 用户AppId
        :type AppId: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param Status: 实例状态
        :type Status: str
        :param StatusDesc: 实例状态中文描述
        :type StatusDesc: str
        :param DbType: 数据库类型
        :type DbType: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param Cpu: Cpu，单位：核
        :type Cpu: int
        :param Memory: 内存，单位：GB
        :type Memory: int
        :param Storage: 存储量，单位：GB
        :type Storage: int
        :param InstanceType: 实例类型
        :type InstanceType: str
        :param InstanceRole: 实例当前角色
        :type InstanceRole: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PayMode: 付费模式
        :type PayMode: int
        :param PeriodEndTime: 实例过期时间
        :type PeriodEndTime: str
        :param NetType: 网络类型
        :type NetType: int
        :param VpcId: VPC网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Vip: 实例内网IP
        :type Vip: str
        :param Vport: 实例内网端口
        :type Vport: int
        :param WanDomain: 实例外网域名
        :type WanDomain: str
        :param Charset: 字符集
        :type Charset: str
        :param CynosVersion: Cynos内核版本
        :type CynosVersion: str
        :param RenewFlag: 续费标志
        :type RenewFlag: int
        """
        self.Uin = None
        self.AppId = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.StatusDesc = None
        self.DbType = None
        self.DbVersion = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.InstanceType = None
        self.InstanceRole = None
        self.UpdateTime = None
        self.CreateTime = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.Charset = None
        self.CynosVersion = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceType = params.get("InstanceType")
        self.InstanceRole = params.get("InstanceRole")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.Charset = params.get("Charset")
        self.CynosVersion = params.get("CynosVersion")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CynosdbInstanceGrp(AbstractModel):
    """实例组信息

    """

    def __init__(self):
        """
        :param AppId: appId
        :type AppId: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param DeletedTime: 删除时间
        :type DeletedTime: str
        :param InstanceGrpId: 实例组ID
        :type InstanceGrpId: str
        :param Status: 状态
        :type Status: str
        :param Type: 实例组类型。ha-ha组；ro-只读组
        :type Type: str
        :param UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param Vip: 内网IP
        :type Vip: str
        :param Vport: 内网端口
        :type Vport: int
        :param WanDomain: 外网域名
        :type WanDomain: str
        :param WanIP: 外网ip
        :type WanIP: str
        :param WanPort: 外网端口
        :type WanPort: int
        :param WanStatus: 外网状态
        :type WanStatus: str
        :param InstanceSet: 实例组包含实例信息
        :type InstanceSet: list of CynosdbInstance
        """
        self.AppId = None
        self.ClusterId = None
        self.CreatedTime = None
        self.DeletedTime = None
        self.InstanceGrpId = None
        self.Status = None
        self.Type = None
        self.UpdatedTime = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanIP = None
        self.WanPort = None
        self.WanStatus = None
        self.InstanceSet = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.CreatedTime = params.get("CreatedTime")
        self.DeletedTime = params.get("DeletedTime")
        self.InstanceGrpId = params.get("InstanceGrpId")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanIP = params.get("WanIP")
        self.WanPort = params.get("WanPort")
        self.WanStatus = params.get("WanStatus")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
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
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AccountNames: 需要过滤的账户列表
        :type AccountNames: list of str
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        """
        self.ClusterId = None
        self.AccountNames = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AccountNames = params.get("AccountNames")
        self.DbType = params.get("DbType")
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
        :param AccountSet: 数据库账号列表
        :type AccountSet: list of Account
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountSet") is not None:
            self.AccountSet = []
            for item in params.get("AccountSet"):
                obj = Account()
                obj._deserialize(item)
                self.AccountSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeBeg: int
        :param BackupTimeEnd: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeEnd: int
        :param ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800
        :type ReserveDuration: int
        :param BackupFreq: 备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupFreq: list of str
        :param BackupType: 备份方式，logic-逻辑备份，snapshot-快照备份
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupTimeBeg = None
        self.BackupTimeEnd = None
        self.ReserveDuration = None
        self.BackupFreq = None
        self.BackupType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupTimeBeg = params.get("BackupTimeBeg")
        self.BackupTimeEnd = params.get("BackupTimeEnd")
        self.ReserveDuration = params.get("ReserveDuration")
        self.BackupFreq = params.get("BackupFreq")
        self.BackupType = params.get("BackupType")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupListRequest(AbstractModel):
    """DescribeBackupList请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Limit: 备份文件列表偏移
        :type Limit: int
        :param Offset: 备份文件列表起始
        :type Offset: int
        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBackupListResponse(AbstractModel):
    """DescribeBackupList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总共备份文件个数
        :type TotalCount: int
        :param BackupList: 备份文件列表
        :type BackupList: list of BackupFileInfo
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
                obj = BackupFileInfo()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Detail: 集群详细信息
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbClusterDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterInstanceGrpsRequest(AbstractModel):
    """DescribeClusterInstanceGrps请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterInstanceGrpsResponse(AbstractModel):
    """DescribeClusterInstanceGrps返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例组个数
        :type TotalCount: int
        :param InstanceGrpInfoList: 实例组列表
        :type InstanceGrpInfoList: list of CynosdbInstanceGrp
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceGrpInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceGrpInfoList") is not None:
            self.InstanceGrpInfoList = []
            for item in params.get("InstanceGrpInfoList"):
                obj = CynosdbInstanceGrp()
                obj._deserialize(item)
                self.InstanceGrpInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        """
        :param DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”
        :type DbType: str
        :param Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        """
        self.DbType = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Filters = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群数
        :type TotalCount: int
        :param ClusterSet: 集群列表
        :type ClusterSet: list of CynosdbCluster
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self.ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = CynosdbCluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
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
        :param InstanceId: 实例组ID
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
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Groups: 安全组信息
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
        


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail请求参数结构体

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
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Detail: 实例详情
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbInstanceDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstanceSpecsRequest(AbstractModel):
    """DescribeInstanceSpecs请求参数结构体

    """

    def __init__(self):
        """
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        """
        self.DbType = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstanceSpecsResponse(AbstractModel):
    """DescribeInstanceSpecs返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceSpecSet: 规格信息
        :type InstanceSpecSet: list of InstanceSpec
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSpecSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSpecSet") is not None:
            self.InstanceSpecSet = []
            for item in params.get("InstanceSpecSet"):
                obj = InstanceSpec()
                obj._deserialize(item)
                self.InstanceSpecSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        :param DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”
        :type DbType: str
        :param Status: 实例状态
        :type Status: str
        :param InstanceIds: 实例id列表
        :type InstanceIds: list of str
        """
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Filters = None
        self.DbType = None
        self.Status = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DbType = params.get("DbType")
        self.Status = params.get("Status")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例个数
        :type TotalCount: int
        :param InstanceSet: 实例列表
        :type InstanceSet: list of CynosdbInstance
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
                obj = CynosdbInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMaintainPeriodRequest(AbstractModel):
    """DescribeMaintainPeriod请求参数结构体

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
        


class DescribeMaintainPeriodResponse(AbstractModel):
    """DescribeMaintainPeriod返回参数结构体

    """

    def __init__(self):
        """
        :param MaintainWeekDays: 维护week days
        :type MaintainWeekDays: list of str
        :param MaintainStartTime: 维护开始时间，单位秒
        :type MaintainStartTime: int
        :param MaintainDuration: 维护时长，单位秒
        :type MaintainDuration: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaintainWeekDays = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
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
        :param ProjectId: 项目ID
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Groups: 安全组详情
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
        


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName请求参数结构体

    """

    def __init__(self):
        """
        :param DealName: 计费订单id
        :type DealName: str
        """
        self.DealName = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName返回参数结构体

    """

    def __init__(self):
        """
        :param BillingResourceInfos: 计费资源id信息数组
        :type BillingResourceInfos: list of BillingResourceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BillingResourceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BillingResourceInfos") is not None:
            self.BillingResourceInfos = []
            for item in params.get("BillingResourceInfos"):
                obj = BillingResourceInfo()
                obj._deserialize(item)
                self.BillingResourceInfos.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRollbackTimeRangeRequest(AbstractModel):
    """DescribeRollbackTimeRange请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRollbackTimeRangeResponse(AbstractModel):
    """DescribeRollbackTimeRange返回参数结构体

    """

    def __init__(self):
        """
        :param TimeRangeStart: 有效回归时间范围开始时间点
        :type TimeRangeStart: str
        :param TimeRangeEnd: 有效回归时间范围结束时间点
        :type TimeRangeEnd: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRollbackTimeValidityRequest(AbstractModel):
    """DescribeRollbackTimeValidity请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ExpectTime: 期望回滚的时间点
        :type ExpectTime: str
        :param ExpectTimeThresh: 回滚时间点的允许误差范围
        :type ExpectTimeThresh: int
        """
        self.ClusterId = None
        self.ExpectTime = None
        self.ExpectTimeThresh = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ExpectTime = params.get("ExpectTime")
        self.ExpectTimeThresh = params.get("ExpectTimeThresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRollbackTimeValidityResponse(AbstractModel):
    """DescribeRollbackTimeValidity返回参数结构体

    """

    def __init__(self):
        """
        :param PoolId: 存储poolID
        :type PoolId: int
        :param QueryId: 回滚任务ID，后续按该时间点回滚时，需要传入
        :type QueryId: int
        :param Status: 时间点是否有效：pass，检测通过；fail，检测失败
        :type Status: str
        :param SuggestTime: 建议时间点，在Status为fail时，该值才有效
        :type SuggestTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PoolId = None
        self.QueryId = None
        self.Status = None
        self.SuggestTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PoolId = params.get("PoolId")
        self.QueryId = params.get("QueryId")
        self.Status = params.get("Status")
        self.SuggestTime = params.get("SuggestTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceSpec(AbstractModel):
    """实例可售卖规格详细信息，创建实例时Cpu/Memory确定实例规格，存储可选大小为[MinStorageSize,MaxStorageSize]

    """

    def __init__(self):
        """
        :param Cpu: 实例CPU，单位：核
        :type Cpu: int
        :param Memory: 实例内存，单位：GB
        :type Memory: int
        :param MaxStorageSize: 实例最大可用存储，单位：GB
        :type MaxStorageSize: int
        :param MinStorageSize: 实例最小可用存储，单位：GB
        :type MinStorageSize: int
        """
        self.Cpu = None
        self.Memory = None
        self.MaxStorageSize = None
        self.MinStorageSize = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorageSize = params.get("MaxStorageSize")
        self.MinStorageSize = params.get("MinStorageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        """
        self.ClusterId = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param DealNames: 退款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IsolateInstanceRequest(AbstractModel):
    """IsolateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 实例ID数组
        :type InstanceIdList: list of str
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IsolateInstanceResponse(AbstractModel):
    """IsolateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流id
        :type FlowId: int
        :param DealNames: 隔离实例的订单id（预付费实例）
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeBeg: int
        :param BackupTimeEnd: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeEnd: int
        :param ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800
        :type ReserveDuration: int
        :param BackupFreq: 备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份
        :type BackupFreq: list of str
        :param BackupType: 备份方式，logic-逻辑备份，snapshot-快照备份
        :type BackupType: str
        """
        self.ClusterId = None
        self.BackupTimeBeg = None
        self.BackupTimeEnd = None
        self.ReserveDuration = None
        self.BackupFreq = None
        self.BackupType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupTimeBeg = params.get("BackupTimeBeg")
        self.BackupTimeEnd = params.get("BackupTimeEnd")
        self.ReserveDuration = params.get("ReserveDuration")
        self.BackupFreq = params.get("BackupFreq")
        self.BackupType = params.get("BackupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回参数结构体

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
        :param InstanceId: 实例组ID
        :type InstanceId: str
        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组Id组成的数组。
        :type SecurityGroupIds: list of str
        :param Zone: 可用区
        :type Zone: str
        """
        self.InstanceId = None
        self.SecurityGroupIds = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.Zone = params.get("Zone")
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
        


class ModifyMaintainPeriodConfigRequest(AbstractModel):
    """ModifyMaintainPeriodConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param MaintainStartTime: 维护开始时间，单位为秒，如3:00为10800
        :type MaintainStartTime: int
        :param MaintainDuration: 维护持续时间，单位为秒，如1小时为3600
        :type MaintainDuration: int
        :param MaintainWeekDays: 每周维护日期
        :type MaintainWeekDays: list of str
        """
        self.InstanceId = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.MaintainWeekDays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMaintainPeriodConfigResponse(AbstractModel):
    """ModifyMaintainPeriodConfig返回参数结构体

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
        


class ObjectTask(AbstractModel):
    """任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务自增ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param TaskStatus: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param ObjectId: 任务ID（集群ID|实例组ID|实例ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectId: str
        :param ObjectType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectType: str
        """
        self.TaskId = None
        self.TaskType = None
        self.TaskStatus = None
        self.ObjectId = None
        self.ObjectType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.TaskStatus = params.get("TaskStatus")
        self.ObjectId = params.get("ObjectId")
        self.ObjectType = params.get("ObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OfflineClusterRequest(AbstractModel):
    """OfflineCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OfflineClusterResponse(AbstractModel):
    """OfflineCluster返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OfflineInstanceRequest(AbstractModel):
    """OfflineInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 实例ID数组
        :type InstanceIdList: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OfflineInstanceResponse(AbstractModel):
    """OfflineInstance返回参数结构体

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PolicyRule(AbstractModel):
    """安全组规则

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
        :param ServiceModule: 协议端口ID或者协议端口组ID。
        :type ServiceModule: str
        :param AddressModule: IP地址ID或者ID地址组ID。
        :type AddressModule: str
        :param Id: id
        :type Id: str
        :param Desc: 描述
        :type Desc: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.ServiceModule = None
        self.AddressModule = None
        self.Id = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.ServiceModule = params.get("ServiceModule")
        self.AddressModule = params.get("AddressModule")
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryFilter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        """
        :param Names: 搜索字段，目前支持："InstanceId", "ProjectId", "InstanceName", "Vip"
        :type Names: list of str
        :param Values: 搜索字符串
        :type Values: list of str
        :param ExactMatch: 是否精确匹配
        :type ExactMatch: bool
        :param Name: 搜索字段
        :type Name: str
        """
        self.Names = None
        self.Values = None
        self.ExactMatch = None
        self.Name = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        self.Name = params.get("Name")
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
        :param Inbound: 入站规则
        :type Inbound: list of PolicyRule
        :param Outbound: 出站规则
        :type Outbound: list of PolicyRule
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
                obj = PolicyRule()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetRenewFlagRequest(AbstractModel):
    """SetRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceIds: 需操作的实例ID
        :type ResourceIds: list of str
        :param AutoRenewFlag: 自动续费标志位
        :type AutoRenewFlag: int
        """
        self.ResourceIds = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetRenewFlagResponse(AbstractModel):
    """SetRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 操作成功实例数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Tag(AbstractModel):
    """集群绑定的标签信息，包含标签键TagKey和标签值TagValue

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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Cpu: 数据库CPU
        :type Cpu: int
        :param Memory: 数据库内存
        :type Memory: int
        :param UpgradeType: 升级类型：upgradeImmediate，upgradeInMaintain
        :type UpgradeType: str
        :param StorageLimit: 存储上限，为0表示使用标准配置
        :type StorageLimit: int
        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        """
        self.InstanceId = None
        self.Cpu = None
        self.Memory = None
        self.UpgradeType = None
        self.StorageLimit = None
        self.AutoVoucher = None
        self.DbType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.UpgradeType = params.get("UpgradeType")
        self.StorageLimit = params.get("StorageLimit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param DealNames: 订单号
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.BigDealIds = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.BigDealIds = params.get("BigDealIds")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        