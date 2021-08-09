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
        :param AccountName: 数据库账号名\n        :type AccountName: str\n        :param Description: 数据库账号描述\n        :type Description: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param Host: 主机\n        :type Host: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesRequest(AbstractModel):
    """AddInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param Cpu: Cpu核数\n        :type Cpu: int\n        :param Memory: 内存\n        :type Memory: int\n        :param ReadOnlyCount: 新增只读实例数\n        :type ReadOnlyCount: int\n        :param InstanceGrpId: 实例组ID，在已有RO组中新增实例时使用，不传则新增RO组\n        :type InstanceGrpId: str\n        :param VpcId: 所属VPC网络ID\n        :type VpcId: str\n        :param SubnetId: 所属子网ID\n        :type SubnetId: str\n        :param Port: 新增RO组时使用的Port\n        :type Port: int\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0\n        :type AutoVoucher: int\n        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        :param OrderSource: 订单来源\n        :type OrderSource: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesResponse(AbstractModel):
    """AddInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 冻结流水，一次开通一个冻结流水。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranId: str\n        :param DealNames: 后付费订单号。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealNames: list of str\n        :param ResourceIds: 发货资源id列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceIds: list of str\n        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BigDealIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class Addr(AbstractModel):
    """数据库地址

    """

    def __init__(self):
        """
        :param IP: IP\n        :type IP: str\n        :param Port: 端口\n        :type Port: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFileInfo(AbstractModel):
    """备份文件信息

    """

    def __init__(self):
        """
        :param SnapshotId: 快照文件ID，用于回滚\n        :type SnapshotId: int\n        :param FileName: 快照文件名\n        :type FileName: str\n        :param FileSize: 快照文件大小\n        :type FileSize: int\n        :param StartTime: 快照备份开始时间\n        :type StartTime: str\n        :param FinishTime: 快照备份完成时间\n        :type FinishTime: str\n        :param BackupType: 备份类型：snapshot，快照备份；timepoint，时间点备份\n        :type BackupType: str\n        :param BackupMethod: 备份方式：auto，自动备份；manual，手动备份\n        :type BackupMethod: str\n        :param BackupStatus: 备份文件状态：success：备份成功；fail：备份失败；creating：备份文件创建中；deleting：备份文件删除中\n        :type BackupStatus: str\n        :param SnapshotTime: 备份文件时间\n        :type SnapshotTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingResourceInfo(AbstractModel):
    """计费资源信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIds: 实例ID列表\n        :type InstanceIds: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInstanceDetail(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param InstanceType: 引擎类型\n        :type InstanceType: str\n        :param InstanceStatus: 实例状态\n        :type InstanceStatus: str\n        :param InstanceStatusDesc: 实例状态描述\n        :type InstanceStatusDesc: str\n        :param InstanceCpu: cpu核数\n        :type InstanceCpu: int\n        :param InstanceMemory: 内存\n        :type InstanceMemory: int\n        :param InstanceStorage: 硬盘\n        :type InstanceStorage: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClustersRequest(AbstractModel):
    """CreateClusters请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区\n        :type Zone: str\n        :param VpcId: 所属VPC网络ID\n        :type VpcId: str\n        :param SubnetId: 所属子网ID\n        :type SubnetId: str\n        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        :param DbVersion: 数据库版本，取值范围: 
<li> MYSQL可选值：5.7 </li>\n        :type DbVersion: str\n        :param ProjectId: 所属项目ID\n        :type ProjectId: int\n        :param Cpu: 普通实例Cpu核数\n        :type Cpu: int\n        :param Memory: 普通实例内存,单位G\n        :type Memory: int\n        :param Storage: 存储大小，单位G\n        :type Storage: int\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param AdminPassword: 账号密码(8-64个字符，包含大小写英文字母、数字和符号~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/中的任意三种)\n        :type AdminPassword: str\n        :param Port: 端口，默认5432\n        :type Port: int\n        :param PayMode: 计费模式，按量计费：0，包年包月：1。默认按量计费。\n        :type PayMode: int\n        :param Count: 购买个数，目前只支持传1（不传默认为1）\n        :type Count: int\n        :param RollbackStrategy: 回档类型：
noneRollback：不回档；
snapRollback，快照回档；
timeRollback，时间点回档\n        :type RollbackStrategy: str\n        :param RollbackId: 快照回档，表示snapshotId；时间点回档，表示queryId，为0，表示需要判断时间点是否有效\n        :type RollbackId: int\n        :param OriginalClusterId: 回档时，传入源集群ID，用于查找源poolId\n        :type OriginalClusterId: str\n        :param ExpectTime: 时间点回档，指定时间；快照回档，快照时间\n        :type ExpectTime: str\n        :param ExpectTimeThresh: 时间点回档，指定时间允许范围\n        :type ExpectTimeThresh: int\n        :param StorageLimit: 普通实例存储上限，单位GB
当DbType为MYSQL，且存储计费模式为预付费时，该参数需不大于cpu与memory对应存储规格上限\n        :type StorageLimit: int\n        :param InstanceCount: 实例数量\n        :type InstanceCount: int\n        :param TimeSpan: 包年包月购买时长\n        :type TimeSpan: int\n        :param TimeUnit: 包年包月购买时长单位\n        :type TimeUnit: str\n        :param AutoRenewFlag: 包年包月购买是否自动续费\n        :type AutoRenewFlag: int\n        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0\n        :type AutoVoucher: int\n        :param HaCount: 实例数量（该参数已不再使用，只做存量兼容处理）\n        :type HaCount: int\n        :param OrderSource: 订单来源\n        :type OrderSource: str\n        :param ResourceTags: 集群创建需要绑定的tag数组信息\n        :type ResourceTags: list of Tag\n        :param DbMode: Db类型
当DbType为MYSQL时可选(默认NORMAL)：
<li>NORMAL</li>
<li>SERVERLESS</li>\n        :type DbMode: str\n        :param MinCpu: 当DbMode为SEVERLESS时必填
cpu最小值，可选范围参考DescribeServerlessInstanceSpecs接口返回\n        :type MinCpu: float\n        :param MaxCpu: 当DbMode为SEVERLESS时必填：
cpu最大值，可选范围参考DescribeServerlessInstanceSpecs接口返回\n        :type MaxCpu: float\n        :param AutoPause: 当DbMode为SEVERLESS时，指定集群是否自动暂停，可选范围
<li>yes</li>
<li>no</li>
默认值:yes\n        :type AutoPause: str\n        :param AutoPauseDelay: 当DbMode为SEVERLESS时，指定集群自动暂停的延迟，单位秒，可选范围[600,691200]
默认值:600\n        :type AutoPauseDelay: int\n        :param StoragePayMode: 集群存储计费模式，按量计费：0，包年包月：1。默认按量计费
当DbType为MYSQL时，在集群计算计费模式为后付费（包括DbMode为SERVERLESS）时，存储计费模式仅可为按量计费
回档与克隆均不支持包年包月存储\n        :type StoragePayMode: int\n        """
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
        self.StoragePayMode = None


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
        self.StoragePayMode = params.get("StoragePayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClustersResponse(AbstractModel):
    """CreateClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranId: str\n        :param DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealNames: list of str\n        :param ResourceIds: 资源ID列表（异步发货可能无法返回该字段, 强烈建议使用dealNames字段查询接口DescribeResourcesByDealName获取异步发货的资源ID）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceIds: list of str\n        :param ClusterIds: 集群ID列表（异步发货可能不返回该字段, 强烈建议使用dealNames查询接口DescribeResourcesByDealName获取异步发货的集群ID）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterIds: list of str\n        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BigDealIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class CynosdbCluster(AbstractModel):
    """集群信息

    """

    def __init__(self):
        """
        :param Status: 集群状态\n        :type Status: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param Zone: 可用区\n        :type Zone: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param Region: 地域\n        :type Region: str\n        :param DbVersion: 数据库版本\n        :type DbVersion: str\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceNum: 实例数\n        :type InstanceNum: int\n        :param Uin: 用户uin\n        :type Uin: str\n        :param DbType: 引擎类型\n        :type DbType: str\n        :param AppId: 用户appid\n        :type AppId: int\n        :param StatusDesc: 集群状态描述\n        :type StatusDesc: str\n        :param CreateTime: 集群创建时间\n        :type CreateTime: str\n        :param PayMode: 付费模式。0-按量计费，1-包年包月\n        :type PayMode: int\n        :param PeriodEndTime: 截止时间\n        :type PeriodEndTime: str\n        :param Vip: 集群读写vip\n        :type Vip: str\n        :param Vport: 集群读写vport\n        :type Vport: int\n        :param ProjectID: 项目id\n        :type ProjectID: int\n        :param VpcId: 私有网络ID\n        :type VpcId: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param CynosVersion: cynos内核版本\n        :type CynosVersion: str\n        :param StorageLimit: 存储容量\n        :type StorageLimit: int\n        :param RenewFlag: 续费标志\n        :type RenewFlag: int\n        :param ProcessingTask: 正在处理的任务\n        :type ProcessingTask: str\n        :param Tasks: 集群的任务数组\n        :type Tasks: list of ObjectTask\n        :param ResourceTags: 集群绑定的tag数组\n        :type ResourceTags: list of Tag\n        :param DbMode: Db类型(NORMAL, SERVERLESS)\n        :type DbMode: str\n        :param ServerlessStatus: 当Db类型为SERVERLESS时，serverless集群状态，可选值:
resume
pause\n        :type ServerlessStatus: str\n        :param Storage: 集群预付费存储值大小\n        :type Storage: int\n        :param StorageId: 集群存储为预付费时的存储ID，用于预付费存储变配\n        :type StorageId: str\n        :param StoragePayMode: 集群存储付费模式。0-按量计费，1-包年包月\n        :type StoragePayMode: int\n        :param MinStorageSize: 集群计算规格对应的最小存储值\n        :type MinStorageSize: int\n        :param MaxStorageSize: 集群计算规格对应的最大存储值\n        :type MaxStorageSize: int\n        """
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
        self.Storage = None
        self.StorageId = None
        self.StoragePayMode = None
        self.MinStorageSize = None
        self.MaxStorageSize = None


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
        self.Storage = params.get("Storage")
        self.StorageId = params.get("StorageId")
        self.StoragePayMode = params.get("StoragePayMode")
        self.MinStorageSize = params.get("MinStorageSize")
        self.MaxStorageSize = params.get("MaxStorageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbClusterDetail(AbstractModel):
    """集群详情详细信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param Region: 地域\n        :type Region: str\n        :param Status: 状态\n        :type Status: str\n        :param StatusDesc: 状态描述\n        :type StatusDesc: str\n        :param VpcName: VPC名称\n        :type VpcName: str\n        :param VpcId: vpc唯一id\n        :type VpcId: str\n        :param SubnetName: 子网名称\n        :type SubnetName: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param Charset: 字符集\n        :type Charset: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param DbType: 数据库类型\n        :type DbType: str\n        :param DbVersion: 数据库版本\n        :type DbVersion: str\n        :param UsedStorage: 使用容量\n        :type UsedStorage: int\n        :param RoAddr: 读写分离Vport\n        :type RoAddr: list of Addr\n        :param InstanceSet: 实例信息\n        :type InstanceSet: list of ClusterInstanceDetail\n        :param PayMode: 付费模式\n        :type PayMode: int\n        :param PeriodEndTime: 到期时间\n        :type PeriodEndTime: str\n        :param Vip: vip地址\n        :type Vip: str\n        :param Vport: vport端口\n        :type Vport: int\n        :param ProjectID: 项目id\n        :type ProjectID: int\n        :param Zone: 可用区\n        :type Zone: str\n        :param ResourceTags: 实例绑定的tag数组信息\n        :type ResourceTags: list of Tag\n        :param ServerlessStatus: 当Db类型为SERVERLESS时，serverless集群状态，可选值:
resume
resuming
pause
pausing\n        :type ServerlessStatus: str\n        """
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
        self.ServerlessStatus = None


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
        self.ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        """
        :param Uin: 用户Uin\n        :type Uin: str\n        :param AppId: 用户AppId\n        :type AppId: int\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param Region: 地域\n        :type Region: str\n        :param Zone: 可用区\n        :type Zone: str\n        :param Status: 实例状态\n        :type Status: str\n        :param StatusDesc: 实例状态中文描述\n        :type StatusDesc: str\n        :param DbType: 数据库类型\n        :type DbType: str\n        :param DbVersion: 数据库版本\n        :type DbVersion: str\n        :param Cpu: Cpu，单位：核\n        :type Cpu: int\n        :param Memory: 内存，单位：GB\n        :type Memory: int\n        :param Storage: 存储量，单位：GB\n        :type Storage: int\n        :param InstanceType: 实例类型\n        :type InstanceType: str\n        :param InstanceRole: 实例当前角色\n        :type InstanceRole: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param VpcId: VPC网络ID\n        :type VpcId: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param Vip: 实例内网IP\n        :type Vip: str\n        :param Vport: 实例内网端口\n        :type Vport: int\n        :param PayMode: 付费模式\n        :type PayMode: int\n        :param PeriodEndTime: 实例过期时间\n        :type PeriodEndTime: str\n        :param DestroyDeadlineText: 销毁期限\n        :type DestroyDeadlineText: str\n        :param IsolateTime: 隔离时间\n        :type IsolateTime: str\n        :param NetType: 网络类型\n        :type NetType: int\n        :param WanDomain: 外网域名\n        :type WanDomain: str\n        :param WanIP: 外网IP\n        :type WanIP: str\n        :param WanPort: 外网端口\n        :type WanPort: int\n        :param WanStatus: 外网状态\n        :type WanStatus: str\n        :param DestroyTime: 实例销毁时间\n        :type DestroyTime: str\n        :param CynosVersion: Cynos内核版本\n        :type CynosVersion: str\n        :param ProcessingTask: 正在处理的任务\n        :type ProcessingTask: str\n        :param RenewFlag: 续费标志\n        :type RenewFlag: int\n        :param MinCpu: serverless实例cpu下限\n        :type MinCpu: float\n        :param MaxCpu: serverless实例cpu上限\n        :type MaxCpu: float\n        :param ServerlessStatus: serverless实例状态, 可选值：
resume
pause\n        :type ServerlessStatus: str\n        :param StoragePayMode: 存储付费类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type StoragePayMode: int\n        :param StorageId: 预付费存储Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type StorageId: str\n        """
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
        self.StoragePayMode = None
        self.StorageId = None


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
        self.StoragePayMode = params.get("StoragePayMode")
        self.StorageId = params.get("StorageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        """
        :param Uin: 用户Uin\n        :type Uin: str\n        :param AppId: 用户AppId\n        :type AppId: int\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param Region: 地域\n        :type Region: str\n        :param Zone: 可用区\n        :type Zone: str\n        :param Status: 实例状态\n        :type Status: str\n        :param StatusDesc: 实例状态中文描述\n        :type StatusDesc: str\n        :param DbType: 数据库类型\n        :type DbType: str\n        :param DbVersion: 数据库版本\n        :type DbVersion: str\n        :param Cpu: Cpu，单位：核\n        :type Cpu: int\n        :param Memory: 内存，单位：GB\n        :type Memory: int\n        :param Storage: 存储量，单位：GB\n        :type Storage: int\n        :param InstanceType: 实例类型\n        :type InstanceType: str\n        :param InstanceRole: 实例当前角色\n        :type InstanceRole: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param PayMode: 付费模式\n        :type PayMode: int\n        :param PeriodEndTime: 实例过期时间\n        :type PeriodEndTime: str\n        :param NetType: 网络类型\n        :type NetType: int\n        :param VpcId: VPC网络ID\n        :type VpcId: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param Vip: 实例内网IP\n        :type Vip: str\n        :param Vport: 实例内网端口\n        :type Vport: int\n        :param WanDomain: 实例外网域名\n        :type WanDomain: str\n        :param Charset: 字符集\n        :type Charset: str\n        :param CynosVersion: Cynos内核版本\n        :type CynosVersion: str\n        :param RenewFlag: 续费标志\n        :type RenewFlag: int\n        :param MinCpu: serverless实例cpu下限\n        :type MinCpu: float\n        :param MaxCpu: serverless实例cpu上限\n        :type MaxCpu: float\n        :param ServerlessStatus: serverless实例状态, 可能值：
resume
pause\n        :type ServerlessStatus: str\n        """
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
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceGrp(AbstractModel):
    """实例组信息

    """

    def __init__(self):
        """
        :param AppId: appId\n        :type AppId: int\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param CreatedTime: 创建时间\n        :type CreatedTime: str\n        :param DeletedTime: 删除时间\n        :type DeletedTime: str\n        :param InstanceGrpId: 实例组ID\n        :type InstanceGrpId: str\n        :param Status: 状态\n        :type Status: str\n        :param Type: 实例组类型。ha-ha组；ro-只读组\n        :type Type: str\n        :param UpdatedTime: 更新时间\n        :type UpdatedTime: str\n        :param Vip: 内网IP\n        :type Vip: str\n        :param Vport: 内网端口\n        :type Vport: int\n        :param WanDomain: 外网域名\n        :type WanDomain: str\n        :param WanIP: 外网ip\n        :type WanIP: str\n        :param WanPort: 外网端口\n        :type WanPort: int\n        :param WanStatus: 外网状态\n        :type WanStatus: str\n        :param InstanceSet: 实例组包含实例信息\n        :type InstanceSet: list of CynosdbInstance\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param AccountNames: 需要过滤的账户列表\n        :type AccountNames: list of str\n        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param AccountSet: 数据库账号列表\n        :type AccountSet: list of Account\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
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
        """
        :param BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200\n        :type BackupTimeBeg: int\n        :param BackupTimeEnd: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200\n        :type BackupTimeEnd: int\n        :param ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800\n        :type ReserveDuration: int\n        :param BackupFreq: 备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupFreq: list of str\n        :param BackupType: 备份方式，logic-逻辑备份，snapshot-快照备份
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeBackupListRequest(AbstractModel):
    """DescribeBackupList请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param Limit: 备份文件列表偏移\n        :type Limit: int\n        :param Offset: 备份文件列表起始\n        :type Offset: int\n        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupListResponse(AbstractModel):
    """DescribeBackupList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总共备份文件个数\n        :type TotalCount: int\n        :param BackupList: 备份文件列表\n        :type BackupList: list of BackupFileInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Detail: 集群详细信息\n        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbClusterDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeClusterInstanceGrpsRequest(AbstractModel):
    """DescribeClusterInstanceGrps请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstanceGrpsResponse(AbstractModel):
    """DescribeClusterInstanceGrps返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例组个数\n        :type TotalCount: int\n        :param InstanceGrpInfoList: 实例组列表\n        :type InstanceGrpInfoList: list of CynosdbInstanceGrp\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        """
        :param DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”\n        :type DbType: str\n        :param Limit: 返回数量，默认为 20，最大值为 100\n        :type Limit: int\n        :param Offset: 记录偏移量，默认值为0\n        :type Offset: int\n        :param OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>\n        :type OrderBy: str\n        :param OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>\n        :type OrderByType: str\n        :param Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。\n        :type Filters: list of QueryFilter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群数\n        :type TotalCount: int\n        :param ClusterSet: 集群列表\n        :type ClusterSet: list of CynosdbCluster\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例组ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
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
        :param Groups: 安全组信息\n        :type Groups: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail请求参数结构体

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
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Detail: 实例详情\n        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbInstanceDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceSpecsRequest(AbstractModel):
    """DescribeInstanceSpecs请求参数结构体

    """

    def __init__(self):
        """
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        """
        self.DbType = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSpecsResponse(AbstractModel):
    """DescribeInstanceSpecs返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceSpecSet: 规格信息\n        :type InstanceSpecSet: list of InstanceSpec\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为 20，最大值为 100\n        :type Limit: int\n        :param Offset: 记录偏移量，默认值为0\n        :type Offset: int\n        :param OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>\n        :type OrderBy: str\n        :param OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>\n        :type OrderByType: str\n        :param Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。\n        :type Filters: list of QueryFilter\n        :param DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”\n        :type DbType: str\n        :param Status: 实例状态\n        :type Status: str\n        :param InstanceIds: 实例id列表\n        :type InstanceIds: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例个数\n        :type TotalCount: int\n        :param InstanceSet: 实例列表\n        :type InstanceSet: list of CynosdbInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeMaintainPeriodRequest(AbstractModel):
    """DescribeMaintainPeriod请求参数结构体

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
        


class DescribeMaintainPeriodResponse(AbstractModel):
    """DescribeMaintainPeriod返回参数结构体

    """

    def __init__(self):
        """
        :param MaintainWeekDays: 维护week days\n        :type MaintainWeekDays: list of str\n        :param MaintainStartTime: 维护开始时间，单位秒\n        :type MaintainStartTime: int\n        :param MaintainDuration: 维护时长，单位秒\n        :type MaintainDuration: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MaintainWeekDays = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: int\n        """
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
        """
        :param Groups: 安全组详情\n        :type Groups: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName请求参数结构体

    """

    def __init__(self):
        """
        :param DealName: 计费订单id（如果计费还没回调业务发货，可能出现错误码InvalidParameterValue.DealNameNotFound，这种情况需要业务重试DescribeResourcesByDealName接口直到成功）\n        :type DealName: str\n        """
        self.DealName = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName返回参数结构体

    """

    def __init__(self):
        """
        :param BillingResourceInfos: 计费资源id信息数组\n        :type BillingResourceInfos: list of BillingResourceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeRollbackTimeRangeRequest(AbstractModel):
    """DescribeRollbackTimeRange请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeRangeResponse(AbstractModel):
    """DescribeRollbackTimeRange返回参数结构体

    """

    def __init__(self):
        """
        :param TimeRangeStart: 有效回归时间范围开始时间点\n        :type TimeRangeStart: str\n        :param TimeRangeEnd: 有效回归时间范围结束时间点\n        :type TimeRangeEnd: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeValidityRequest(AbstractModel):
    """DescribeRollbackTimeValidity请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ExpectTime: 期望回滚的时间点\n        :type ExpectTime: str\n        :param ExpectTimeThresh: 回滚时间点的允许误差范围\n        :type ExpectTimeThresh: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeValidityResponse(AbstractModel):
    """DescribeRollbackTimeValidity返回参数结构体

    """

    def __init__(self):
        """
        :param PoolId: 存储poolID\n        :type PoolId: int\n        :param QueryId: 回滚任务ID，后续按该时间点回滚时，需要传入\n        :type QueryId: int\n        :param Status: 时间点是否有效：pass，检测通过；fail，检测失败\n        :type Status: str\n        :param SuggestTime: 建议时间点，在Status为fail时，该值才有效\n        :type SuggestTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class InstanceSpec(AbstractModel):
    """实例可售卖规格详细信息，创建实例时Cpu/Memory确定实例规格，存储可选大小为[MinStorageSize,MaxStorageSize]

    """

    def __init__(self):
        """
        :param Cpu: 实例CPU，单位：核\n        :type Cpu: int\n        :param Memory: 实例内存，单位：GB\n        :type Memory: int\n        :param MaxStorageSize: 实例最大可用存储，单位：GB\n        :type MaxStorageSize: int\n        :param MinStorageSize: 实例最小可用存储，单位：GB\n        :type MinStorageSize: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowId: int\n        :param DealNames: 退款订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealNames: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class IsolateInstanceRequest(AbstractModel):
    """IsolateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIdList: 实例ID数组\n        :type InstanceIdList: list of str\n        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstanceResponse(AbstractModel):
    """IsolateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流id\n        :type FlowId: int\n        :param DealNames: 隔离实例的订单id（预付费实例）
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealNames: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200\n        :type BackupTimeBeg: int\n        :param BackupTimeEnd: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200\n        :type BackupTimeEnd: int\n        :param ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800\n        :type ReserveDuration: int\n        :param BackupFreq: 备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份\n        :type BackupFreq: list of str\n        :param BackupType: 备份方式，logic-逻辑备份，snapshot-快照备份\n        :type BackupType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例组ID\n        :type InstanceId: str\n        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组Id组成的数组。\n        :type SecurityGroupIds: list of str\n        :param Zone: 可用区\n        :type Zone: str\n        """
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


class ModifyMaintainPeriodConfigRequest(AbstractModel):
    """ModifyMaintainPeriodConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param MaintainStartTime: 维护开始时间，单位为秒，如3:00为10800\n        :type MaintainStartTime: int\n        :param MaintainDuration: 维护持续时间，单位为秒，如1小时为3600\n        :type MaintainDuration: int\n        :param MaintainWeekDays: 每周维护日期\n        :type MaintainWeekDays: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintainPeriodConfigResponse(AbstractModel):
    """ModifyMaintainPeriodConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ObjectTask(AbstractModel):
    """任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务自增ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        :param TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskType: str\n        :param TaskStatus: 任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskStatus: str\n        :param ObjectId: 任务ID（集群ID|实例组ID|实例ID）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ObjectId: str\n        :param ObjectType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type ObjectType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterRequest(AbstractModel):
    """OfflineCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterResponse(AbstractModel):
    """OfflineCluster返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class OfflineInstanceRequest(AbstractModel):
    """OfflineInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIdList: 实例ID数组\n        :type InstanceIdList: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineInstanceResponse(AbstractModel):
    """OfflineInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务流ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class PolicyRule(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT或者DROP\n        :type Action: str\n        :param CidrIp: 来源Ip或Ip段，例如192.168.0.0/16\n        :type CidrIp: str\n        :param PortRange: 端口\n        :type PortRange: str\n        :param IpProtocol: 网络协议，支持udp、tcp等\n        :type IpProtocol: str\n        :param ServiceModule: 协议端口ID或者协议端口组ID。\n        :type ServiceModule: str\n        :param AddressModule: IP地址ID或者ID地址组ID。\n        :type AddressModule: str\n        :param Id: id\n        :type Id: str\n        :param Desc: 描述\n        :type Desc: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        """
        :param Names: 搜索字段，目前支持："InstanceId", "ProjectId", "InstanceName", "Vip"\n        :type Names: list of str\n        :param Values: 搜索字符串\n        :type Values: list of str\n        :param ExactMatch: 是否精确匹配\n        :type ExactMatch: bool\n        :param Name: 搜索字段\n        :type Name: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss\n        :type CreateTime: str\n        :param Inbound: 入站规则\n        :type Inbound: list of PolicyRule\n        :param Outbound: 出站规则\n        :type Outbound: list of PolicyRule\n        :param SecurityGroupId: 安全组ID\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: 安全组备注\n        :type SecurityGroupRemark: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagRequest(AbstractModel):
    """SetRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceIds: 需操作的实例ID\n        :type ResourceIds: list of str\n        :param AutoRenewFlag: 自动续费标志位\n        :type AutoRenewFlag: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagResponse(AbstractModel):
    """SetRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 操作成功实例数\n        :type Count: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """集群绑定的标签信息，包含标签键TagKey和标签值TagValue

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
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
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Cpu: 数据库CPU\n        :type Cpu: int\n        :param Memory: 数据库内存\n        :type Memory: int\n        :param UpgradeType: 升级类型：upgradeImmediate，upgradeInMaintain\n        :type UpgradeType: str\n        :param StorageLimit: 存储上限，为0表示使用标准配置\n        :type StorageLimit: int\n        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0\n        :type AutoVoucher: int\n        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>\n        :type DbType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranId: str\n        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type BigDealIds: list of str\n        :param DealNames: 订单号\n        :type DealNames: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TranId = None
        self.BigDealIds = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.BigDealIds = params.get("BigDealIds")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")