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


class AssignProjectRequest(AbstractModel):
    """AssignProject请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceIds: list of str\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        """
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
        


class AssignProjectResponse(AbstractModel):
    """AssignProject返回参数结构体

    """

    def __init__(self):
        """
        :param FlowIds: 返回的异步任务ID列表\n        :type FlowIds: list of int non-negative\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.RequestId = params.get("RequestId")


class BackupDownloadTask(AbstractModel):
    """备份下载任务

    """

    def __init__(self):
        """
        :param CreateTime: 任务创建时间\n        :type CreateTime: str\n        :param BackupName: 备份文件名\n        :type BackupName: str\n        :param ReplicaSetId: 分片名称\n        :type ReplicaSetId: str\n        :param BackupSize: 备份数据大小，单位为字节\n        :type BackupSize: int\n        :param Status: 任务状态。0-等待执行，1-正在下载，2-下载完成，3-下载失败，4-等待重试\n        :type Status: int\n        :param Percent: 任务进度百分比\n        :type Percent: int\n        :param TimeSpend: 耗时，单位为秒\n        :type TimeSpend: int\n        :param Url: 备份数据下载链接\n        :type Url: str\n        """
        self.CreateTime = None
        self.BackupName = None
        self.ReplicaSetId = None
        self.BackupSize = None
        self.Status = None
        self.Percent = None
        self.TimeSpend = None
        self.Url = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.BackupName = params.get("BackupName")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.BackupSize = params.get("BackupSize")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.TimeSpend = params.get("TimeSpend")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadTaskStatus(AbstractModel):
    """创建备份下载任务结果

    """

    def __init__(self):
        """
        :param ReplicaSetId: 分片名\n        :type ReplicaSetId: str\n        :param Status: 任务当前状态。0-等待执行，1-正在下载，2-下载完成，3-下载失败，4-等待重试\n        :type Status: int\n        """
        self.ReplicaSetId = None
        self.Status = None


    def _deserialize(self, params):
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFile(AbstractModel):
    """备份文件存储信息

    """

    def __init__(self):
        """
        :param ReplicateSetId: 备份文件所属的副本集/分片ID\n        :type ReplicateSetId: str\n        :param File: 备份文件保存路径\n        :type File: str\n        """
        self.ReplicateSetId = None
        self.File = None


    def _deserialize(self, params):
        self.ReplicateSetId = params.get("ReplicateSetId")
        self.File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupInfo(AbstractModel):
    """备份信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param BackupType: 备份方式，0-自动备份，1-手动备份\n        :type BackupType: int\n        :param BackupName: 备份名称\n        :type BackupName: str\n        :param BackupDesc: 备份备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupDesc: str\n        :param BackupSize: 备份文件大小，单位KB
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupSize: int\n        :param StartTime: 备份开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTime: str\n        :param EndTime: 备份结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        :param Status: 备份状态，1-备份中，2-备份成功\n        :type Status: int\n        :param BackupMethod: 备份方法，0-逻辑备份，1-物理备份\n        :type BackupMethod: int\n        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupName = None
        self.BackupDesc = None
        self.BackupSize = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.BackupMethod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupName = params.get("BackupName")
        self.BackupDesc = params.get("BackupDesc")
        self.BackupSize = params.get("BackupSize")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.BackupMethod = params.get("BackupMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientConnection(AbstractModel):
    """客户端连接信息，包括客户端IP和连接数

    """

    def __init__(self):
        """
        :param IP: 连接的客户端IP\n        :type IP: str\n        :param Count: 对应客户端IP的连接数\n        :type Count: int\n        """
        self.IP = None
        self.Count = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDBInstanceRequest(AbstractModel):
    """CreateBackupDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param BackupMethod: 0-逻辑备份，1-物理备份\n        :type BackupMethod: int\n        :param BackupRemark: 备份备注\n        :type BackupRemark: str\n        """
        self.InstanceId = None
        self.BackupMethod = None
        self.BackupRemark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupRemark = params.get("BackupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDBInstanceResponse(AbstractModel):
    """CreateBackupDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 查询备份流程的状态\n        :type AsyncRequestId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateBackupDownloadTaskRequest(AbstractModel):
    """CreateBackupDownloadTask请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param BackupName: 要下载的备份文件名，可通过DescribeDBBackups接口获取\n        :type BackupName: str\n        :param BackupSets: 下载备份的分片列表\n        :type BackupSets: list of ReplicaSetInfo\n        """
        self.InstanceId = None
        self.BackupName = None
        self.BackupSets = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        if params.get("BackupSets") is not None:
            self.BackupSets = []
            for item in params.get("BackupSets"):
                obj = ReplicaSetInfo()
                obj._deserialize(item)
                self.BackupSets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupDownloadTaskResponse(AbstractModel):
    """CreateBackupDownloadTask返回参数结构体

    """

    def __init__(self):
        """
        :param Tasks: 下载任务状态\n        :type Tasks: list of BackupDownloadTaskStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = BackupDownloadTaskStatus()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param Memory: 实例内存大小，单位：GB\n        :type Memory: int\n        :param Volume: 实例硬盘大小，单位：GB\n        :type Volume: int\n        :param ReplicateSetNum: 副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数\n        :type ReplicateSetNum: int\n        :param NodeNum: 每个副本集内节点个数，当前副本集节点数固定为3，分片从节点数可选，具体参照查询云数据库的售卖规格返回参数\n        :type NodeNum: int\n        :param MongoVersion: 版本号，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本\n        :type MongoVersion: str\n        :param MachineCode: 机器类型，HIO：高IO型；HIO10G：高IO万兆\n        :type MachineCode: str\n        :param GoodsNum: 实例数量，最小值1，最大值为10\n        :type GoodsNum: int\n        :param Zone: 可用区信息，格式如：ap-guangzhou-2\n        :type Zone: str\n        :param ClusterType: 实例类型，REPLSET-副本集，SHARD-分片集群\n        :type ClusterType: str\n        :param VpcId: 私有网络ID，如果不设置该参数则默认选择基础网络\n        :type VpcId: str\n        :param SubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填\n        :type SubnetId: str\n        :param Password: 实例密码，不设置该参数则默认密码规则为 实例ID+"@"+主账户uin。举例实例id为cmgo-higv73ed，uin为100000001，则默认密码为"cmgo-higv73ed@100000001"。密码必须是8-16位字符，且至少包含字母、数字和字符 !@#%^*() 中的两种\n        :type Password: str\n        :param ProjectId: 项目ID，不设置为默认项目\n        :type ProjectId: int\n        :param Tags: 实例标签信息\n        :type Tags: list of TagInfo\n        :param Clone: 1:正式实例,2:临时实例,3:只读实例，4：灾备实例\n        :type Clone: int\n        :param Father: 父实例Id，当Clone为3或者4时，这个必须填\n        :type Father: str\n        :param SecurityGroup: 安全组\n        :type SecurityGroup: list of str\n        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.NodeNum = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.ClusterType = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ProjectId = None
        self.Tags = None
        self.Clone = None
        self.Father = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.NodeNum = params.get("NodeNum")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Clone = params.get("Clone")
        self.Father = params.get("Father")
        self.SecurityGroup = params.get("SecurityGroup")
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
        """
        :param DealId: 订单ID\n        :type DealId: str\n        :param InstanceIds: 创建的实例ID列表\n        :type InstanceIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param NodeNum: 每个副本集内节点个数，当前副本集节点数固定为3，分片从节点数可选，具体参照查询云数据库的售卖规格返回参数\n        :type NodeNum: int\n        :param Memory: 实例内存大小，单位：GB\n        :type Memory: int\n        :param Volume: 实例硬盘大小，单位：GB\n        :type Volume: int\n        :param MongoVersion: 版本号，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本，MONGO_40_WT：MongoDB 4.0 WiredTiger存储引擎版本\n        :type MongoVersion: str\n        :param GoodsNum: 实例数量, 最小值1，最大值为10\n        :type GoodsNum: int\n        :param Zone: 实例所属区域名称，格式如：ap-guangzhou-2\n        :type Zone: str\n        :param Period: 实例时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]\n        :type Period: int\n        :param MachineCode: 机器类型，HIO：高IO型；HIO10G：高IO万兆型；STDS5：标准型\n        :type MachineCode: str\n        :param ClusterType: 实例类型，REPLSET-副本集，SHARD-分片集群，STANDALONE-单节点\n        :type ClusterType: str\n        :param ReplicateSetNum: 副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数；若为单节点实例，该参数设置为0\n        :type ReplicateSetNum: int\n        :param ProjectId: 项目ID，不设置为默认项目\n        :type ProjectId: int\n        :param VpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 查询私有网络列表\n        :type VpcId: str\n        :param SubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 查询子网列表\n        :type SubnetId: str\n        :param Password: 实例密码，不设置该参数则默认密码规则为 实例ID+"@"+主账户uin。举例实例id为cmgo-higv73ed，uin为100000001，则默认密码为"cmgo-higv73ed@100000001"。密码必须是8-16位字符，且至少包含字母、数字和字符 !@#%^*() 中的两种\n        :type Password: str\n        :param Tags: 实例标签信息\n        :type Tags: list of TagInfo\n        :param AutoRenewFlag: 自动续费标记，可选值为：0 - 不自动续费；1 - 自动续费。默认为不自动续费\n        :type AutoRenewFlag: int\n        :param AutoVoucher: 是否自动选择代金券，可选值为：1 - 是；0 - 否； 默认为0\n        :type AutoVoucher: int\n        :param Clone: 1:正式实例,2:临时实例,3:只读实例，4：灾备实例\n        :type Clone: int\n        :param Father: 若是只读，灾备实例，Father必须填写，即主实例ID\n        :type Father: str\n        :param SecurityGroup: 安全组\n        :type SecurityGroup: list of str\n        """
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.GoodsNum = None
        self.Zone = None
        self.Period = None
        self.MachineCode = None
        self.ClusterType = None
        self.ReplicateSetNum = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.Tags = None
        self.AutoRenewFlag = None
        self.AutoVoucher = None
        self.Clone = None
        self.Father = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.Period = params.get("Period")
        self.MachineCode = params.get("MachineCode")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoVoucher = params.get("AutoVoucher")
        self.Clone = params.get("Clone")
        self.Father = params.get("Father")
        self.SecurityGroup = params.get("SecurityGroup")
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
        :param DealId: 订单ID\n        :type DealId: str\n        :param InstanceIds: 创建的实例ID列表\n        :type InstanceIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CurrentOp(AbstractModel):
    """云数据库实例当前操作

    """

    def __init__(self):
        """
        :param OpId: 操作序号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OpId: int\n        :param Ns: 操作所在的命名空间，形式如db.collection
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ns: str\n        :param Query: 操作执行语句
注意：此字段可能返回 null，表示取不到有效值。\n        :type Query: str\n        :param Op: 操作类型，可能的取值：aggregate、count、delete、distinct、find、findAndModify、getMore、insert、mapReduce、update和command
注意：此字段可能返回 null，表示取不到有效值。\n        :type Op: str\n        :param ReplicaSetName: 操作所在的分片名称\n        :type ReplicaSetName: str\n        :param State: 筛选条件，节点状态，可能的取值为：Primary、Secondary
注意：此字段可能返回 null，表示取不到有效值。\n        :type State: str\n        :param Operation: 操作详细信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Operation: str\n        :param NodeName: 操作所在的节点名称\n        :type NodeName: str\n        :param MicrosecsRunning: 操作已执行时间（ms）
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicrosecsRunning: int\n        """
        self.OpId = None
        self.Ns = None
        self.Query = None
        self.Op = None
        self.ReplicaSetName = None
        self.State = None
        self.Operation = None
        self.NodeName = None
        self.MicrosecsRunning = None


    def _deserialize(self, params):
        self.OpId = params.get("OpId")
        self.Ns = params.get("Ns")
        self.Query = params.get("Query")
        self.Op = params.get("Op")
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.State = params.get("State")
        self.Operation = params.get("Operation")
        self.NodeName = params.get("NodeName")
        self.MicrosecsRunning = params.get("MicrosecsRunning")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstanceInfo(AbstractModel):
    """实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Region: 地域信息\n        :type Region: str\n        """
        self.InstanceId = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBInstancePrice(AbstractModel):
    """数据库实例价格

    """

    def __init__(self):
        """
        :param UnitPrice: 单价
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnitPrice: float\n        :param OriginalPrice: 原价\n        :type OriginalPrice: float\n        :param DiscountPrice: 折扣加\n        :type DiscountPrice: float\n        """
        self.UnitPrice = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步请求Id，涉及到异步流程的接口返回，如CreateBackupDBInstance\n        :type AsyncRequestId: str\n        """
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
        """
        :param Status: 状态\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeBackupAccessRequest(AbstractModel):
    """DescribeBackupAccess请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param BackupName: 需要获取下载授权的备份文件名\n        :type BackupName: str\n        """
        self.InstanceId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupAccessResponse(AbstractModel):
    """DescribeBackupAccess返回参数结构体

    """

    def __init__(self):
        """
        :param Region: 实例所属地域\n        :type Region: str\n        :param Bucket: 备份文件所在存储桶\n        :type Bucket: str\n        :param Files: 备份文件的存储信息\n        :type Files: list of BackupFile\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Region = None
        self.Bucket = None
        self.Files = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = BackupFile()
                obj._deserialize(item)
                self.Files.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupDownloadTaskRequest(AbstractModel):
    """DescribeBackupDownloadTask请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param BackupName: 备份文件名，用来过滤指定文件的下载任务\n        :type BackupName: str\n        :param StartTime: 指定要查询任务的时间范围，StartTime指定开始时间，不填默认不限制开始时间\n        :type StartTime: str\n        :param EndTime: 指定要查询任务的时间范围，EndTime指定结束时间，不填默认不限制结束时间\n        :type EndTime: str\n        :param Limit: 此次查询返回的条数，取值范围为1-100，默认为20\n        :type Limit: int\n        :param Offset: 指定此次查询返回的页数，默认为0\n        :type Offset: int\n        :param OrderBy: 排序字段，取值为createTime，finishTime两种，默认为createTime\n        :type OrderBy: str\n        :param OrderByType: 排序方式，取值为asc，desc两种，默认desc\n        :type OrderByType: str\n        :param Status: 根据任务状态过滤。0-等待执行，1-正在下载，2-下载完成，3-下载失败，4-等待重试。不填默认返回所有类型\n        :type Status: list of int\n        """
        self.InstanceId = None
        self.BackupName = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadTaskResponse(AbstractModel):
    """DescribeBackupDownloadTask返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 满足查询条件的所有条数\n        :type TotalCount: int\n        :param Tasks: 下载任务列表\n        :type Tasks: list of BackupDownloadTask\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = BackupDownloadTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param Limit: 查询返回记录条数，默认为10000。\n        :type Limit: int\n        :param Offset: 偏移量，默认值为0。\n        :type Offset: int\n        """
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
        


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections返回参数结构体

    """

    def __init__(self):
        """
        :param Clients: 客户端连接信息，包括客户端IP和对应IP的连接数量。\n        :type Clients: list of ClientConnection\n        :param TotalCount: 满足条件的记录总条数，可用于分页查询。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Clients = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self.Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self.Clients.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCurrentOpRequest(AbstractModel):
    """DescribeCurrentOp请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param Ns: 筛选条件，操作所属的命名空间namespace，格式为db.collection\n        :type Ns: str\n        :param MillisecondRunning: 筛选条件，操作已经执行的时间（单位：毫秒），结果将返回超过设置时间的操作，默认值为0，取值范围为[0, 3600000]\n        :type MillisecondRunning: int\n        :param Op: 筛选条件，操作类型，可能的取值：none，update，insert，query，command，getmore，remove和killcursors\n        :type Op: str\n        :param ReplicaSetName: 筛选条件，分片名称\n        :type ReplicaSetName: str\n        :param State: 筛选条件，节点状态，可能的取值为：primary
secondary\n        :type State: str\n        :param Limit: 单次请求返回的数量，默认值为100，取值范围为[0,100]\n        :type Limit: int\n        :param Offset: 偏移量，默认值为0，取值范围为[0,10000]\n        :type Offset: int\n        :param OrderBy: 返回结果集排序的字段，目前支持："MicrosecsRunning"/"microsecsrunning"，默认为升序排序\n        :type OrderBy: str\n        :param OrderByType: 返回结果集排序方式，可能的取值："ASC"/"asc"或"DESC"/"desc"\n        :type OrderByType: str\n        """
        self.InstanceId = None
        self.Ns = None
        self.MillisecondRunning = None
        self.Op = None
        self.ReplicaSetName = None
        self.State = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ns = params.get("Ns")
        self.MillisecondRunning = params.get("MillisecondRunning")
        self.Op = params.get("Op")
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.State = params.get("State")
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
        


class DescribeCurrentOpResponse(AbstractModel):
    """DescribeCurrentOp返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的操作总数\n        :type TotalCount: int\n        :param CurrentOps: 当前操作列表\n        :type CurrentOps: list of CurrentOp\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.CurrentOps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CurrentOps") is not None:
            self.CurrentOps = []
            for item in params.get("CurrentOps"):
                obj = CurrentOp()
                obj._deserialize(item)
                self.CurrentOps.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param BackupMethod: 备份方式，当前支持：0-逻辑备份，1-物理备份，2-所有备份。默认为逻辑备份。\n        :type BackupMethod: int\n        :param Limit: 分页大小，最大值为100，不设置默认查询所有。\n        :type Limit: int\n        :param Offset: 分页偏移量，最小值为0，默认值为0。\n        :type Offset: int\n        """
        self.InstanceId = None
        self.BackupMethod = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
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
        :param BackupList: 备份列表\n        :type BackupList: list of BackupInfo\n        :param TotalCount: 备份总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BackupList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceDealRequest(AbstractModel):
    """DescribeDBInstanceDeal请求参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID，通过CreateDBInstance等接口返回\n        :type DealId: str\n        """
        self.DealId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceDealResponse(AbstractModel):
    """DescribeDBInstanceDeal返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 订单状态，1：未支付，2：已支付，3：发货中，4：发货成功，5：发货失败，6：退款，7：订单关闭，8：超时未支付关闭。\n        :type Status: int\n        :param OriginalPrice: 订单原价。\n        :type OriginalPrice: float\n        :param DiscountPrice: 订单折扣价格。\n        :type DiscountPrice: float\n        :param Action: 订单行为，purchase：新购，renew：续费，upgrade：升配，downgrade：降配，refund：退货退款。\n        :type Action: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.Action = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.Action = params.get("Action")
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceIds: list of str\n        :param InstanceType: 实例类型，取值范围：0-所有实例,1-正式实例，2-临时实例, 3-只读实例，-1-正式实例+只读+灾备实例\n        :type InstanceType: int\n        :param ClusterType: 集群类型，取值范围：0-副本集实例，1-分片实例，-1-所有实例\n        :type ClusterType: int\n        :param Status: 实例状态，取值范围：0-待初始化，1-流程执行中，2-实例有效，-2-已隔离（包年包月实例），-3-已隔离（按量计费实例）\n        :type Status: list of int\n        :param VpcId: 私有网络的ID，基础网络则不传该参数\n        :type VpcId: str\n        :param SubnetId: 私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId\n        :type SubnetId: str\n        :param PayMode: 付费类型，取值范围：0-按量计费，1-包年包月，-1-按量计费+包年包月\n        :type PayMode: int\n        :param Limit: 单次请求返回的数量，最小值为1，最大值为100，默认值为20\n        :type Limit: int\n        :param Offset: 偏移量，默认值为0\n        :type Offset: int\n        :param OrderBy: 返回结果集排序的字段，目前支持："ProjectId", "InstanceName", "CreateTime"，默认为升序排序\n        :type OrderBy: str\n        :param OrderByType: 返回结果集排序方式，目前支持："ASC"或者"DESC"\n        :type OrderByType: str\n        :param ProjectIds: 项目 ID\n        :type ProjectIds: list of int non-negative\n        :param SearchKey: 搜索关键词，支持实例ID、实例名称、完整IP\n        :type SearchKey: str\n        :param Tags: Tag信息\n        :type Tags: :class:`tencentcloud.mongodb.v20190725.models.TagInfo`\n        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ClusterType = None
        self.Status = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.ProjectIds = None
        self.SearchKey = None
        self.Tags = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ClusterType = params.get("ClusterType")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")
        if params.get("Tags") is not None:
            self.Tags = TagInfo()
            self.Tags._deserialize(params.get("Tags"))
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
        :param TotalCount: 符合查询条件的实例总数\n        :type TotalCount: int\n        :param InstanceDetails: 实例详细信息列表\n        :type InstanceDetails: list of InstanceDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupResponse(AbstractModel):
    """DescribeSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Groups: 实例绑定的安全组\n        :type Groups: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeSlowLogPatternsRequest(AbstractModel):
    """DescribeSlowLogPatterns请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param StartTime: 慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。\n        :type StartTime: str\n        :param EndTime: 慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。\n        :type EndTime: str\n        :param SlowMS: 慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。\n        :type SlowMS: int\n        :param Offset: 偏移量，最小值为0，最大值为10000，默认值为0。\n        :type Offset: int\n        :param Limit: 分页大小，最小值为1，最大值为100，默认值为20。\n        :type Limit: int\n        :param Format: 慢日志返回格式，可设置为json，不传默认返回原生慢日志格式。\n        :type Format: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None
        self.Format = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogPatternsResponse(AbstractModel):
    """DescribeSlowLogPatterns返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 慢日志统计信息总数\n        :type Count: int\n        :param SlowLogPatterns: 慢日志统计信息\n        :type SlowLogPatterns: list of SlowLogPattern\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Count = None
        self.SlowLogPatterns = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("SlowLogPatterns") is not None:
            self.SlowLogPatterns = []
            for item in params.get("SlowLogPatterns"):
                obj = SlowLogPattern()
                obj._deserialize(item)
                self.SlowLogPatterns.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param StartTime: 慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。\n        :type StartTime: str\n        :param EndTime: 慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。\n        :type EndTime: str\n        :param SlowMS: 慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。\n        :type SlowMS: int\n        :param Offset: 偏移量，最小值为0，最大值为10000，默认值为0。\n        :type Offset: int\n        :param Limit: 分页大小，最小值为1，最大值为100，默认值为20。\n        :type Limit: int\n        :param Format: 慢日志返回格式，可设置为json，不传默认返回原生慢日志格式。\n        :type Format: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None
        self.Format = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Format = params.get("Format")
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
        """
        :param Count: 慢日志总数\n        :type Count: int\n        :param SlowLogs: 慢日志详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type SlowLogs: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Count = None
        self.SlowLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.SlowLogs = params.get("SlowLogs")
        self.RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    """DescribeSpecInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 待查询可用区\n        :type Zone: str\n        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpecInfoResponse(AbstractModel):
    """DescribeSpecInfo返回参数结构体

    """

    def __init__(self):
        """
        :param SpecInfoList: 实例售卖规格信息列表\n        :type SpecInfoList: list of SpecificationInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class FlushInstanceRouterConfigRequest(AbstractModel):
    """FlushInstanceRouterConfig请求参数结构体

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
        


class FlushInstanceRouterConfigResponse(AbstractModel):
    """FlushInstanceRouterConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InquirePriceCreateDBInstancesRequest(AbstractModel):
    """InquirePriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 实例所属区域名称，格式如：ap-guangzhou-2\n        :type Zone: str\n        :param NodeNum: 每个副本集内节点个数，当前副本集节点数固定为3，分片从节点数可选，具体参照查询云数据库的售卖规格返回参数\n        :type NodeNum: int\n        :param Memory: 实例内存大小，单位：GB\n        :type Memory: int\n        :param Volume: 实例硬盘大小，单位：GB\n        :type Volume: int\n        :param MongoVersion: 版本号，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本，MONGO_40_WT：MongoDB 4.0 WiredTiger存储引擎版本\n        :type MongoVersion: str\n        :param MachineCode: 机器类型，HIO：高IO型；HIO10G：高IO万兆型；STDS5：标准型\n        :type MachineCode: str\n        :param GoodsNum: 实例数量, 最小值1，最大值为10\n        :type GoodsNum: int\n        :param Period: 实例时长，单位：月，可选值包括[1,2,3,4,5,6,7,8,9,10,11,12,24,36]\n        :type Period: int\n        :param ClusterType: 实例类型，REPLSET-副本集，SHARD-分片集群，STANDALONE-单节点\n        :type ClusterType: str\n        :param ReplicateSetNum: 副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数；若为单节点实例，该参数设置为0\n        :type ReplicateSetNum: int\n        """
        self.Zone = None
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Period = None
        self.ClusterType = None
        self.ReplicateSetNum = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDBInstancesResponse(AbstractModel):
    """InquirePriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格\n        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquirePriceModifyDBInstanceSpecRequest(AbstractModel):
    """InquirePriceModifyDBInstanceSpec请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同。\n        :type InstanceId: str\n        :param Memory: 变更配置后实例内存大小，单位：GB。\n        :type Memory: int\n        :param Volume: 变更配置后实例磁盘大小，单位：GB。\n        :type Volume: int\n        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceModifyDBInstanceSpecResponse(AbstractModel):
    """InquirePriceModifyDBInstanceSpec返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格。\n        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquirePriceRenewDBInstancesRequest(AbstractModel):
    """InquirePriceRenewDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同，接口单次最多只支持5个实例进行操作。\n        :type InstanceIds: list of str\n        :param InstanceChargePrepaid: 预付费模式（即包年包月）相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。\n        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`\n        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewDBInstancesResponse(AbstractModel):
    """InquirePriceRenewDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格\n        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        """
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。默认为1。
（InquirePriceRenewDBInstances，RenewDBInstances调用时必填）\n        :type Period: int\n        :param RenewFlag: 自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
（InquirePriceRenewDBInstances，RenewDBInstances调用时必填）\n        :type RenewFlag: str\n        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param PayMode: 付费类型，可能的返回值：1-包年包月；0-按量计费\n        :type PayMode: int\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param ClusterType: 集群类型，可能的返回值：0-副本集实例，1-分片实例，\n        :type ClusterType: int\n        :param Region: 地域信息\n        :type Region: str\n        :param Zone: 可用区信息\n        :type Zone: str\n        :param NetType: 网络类型，可能的返回值：0-基础网络，1-私有网络\n        :type NetType: int\n        :param VpcId: 私有网络的ID\n        :type VpcId: str\n        :param SubnetId: 私有网络的子网ID\n        :type SubnetId: str\n        :param Status: 实例状态，可能的返回值：0-待初始化，1-流程处理中，2-运行中，-2-实例已过期\n        :type Status: int\n        :param Vip: 实例IP\n        :type Vip: str\n        :param Vport: 端口号\n        :type Vport: int\n        :param CreateTime: 实例创建时间\n        :type CreateTime: str\n        :param DeadLine: 实例到期时间\n        :type DeadLine: str\n        :param MongoVersion: 实例版本信息\n        :type MongoVersion: str\n        :param Memory: 实例内存规格，单位为MB\n        :type Memory: int\n        :param Volume: 实例磁盘规格，单位为MB\n        :type Volume: int\n        :param CpuNum: 实例CPU核心数\n        :type CpuNum: int\n        :param MachineType: 实例机器类型\n        :type MachineType: str\n        :param SecondaryNum: 实例从节点数\n        :type SecondaryNum: int\n        :param ReplicationSetNum: 实例分片数\n        :type ReplicationSetNum: int\n        :param AutoRenewFlag: 实例自动续费标志，可能的返回值：0-手动续费，1-自动续费，2-确认不续费\n        :type AutoRenewFlag: int\n        :param UsedVolume: 已用容量，单位MB\n        :type UsedVolume: int\n        :param MaintenanceStart: 维护窗口起始时间\n        :type MaintenanceStart: str\n        :param MaintenanceEnd: 维护窗口结束时间\n        :type MaintenanceEnd: str\n        :param ReplicaSets: 分片信息\n        :type ReplicaSets: list of ShardInfo\n        :param ReadonlyInstances: 只读实例信息\n        :type ReadonlyInstances: list of DBInstanceInfo\n        :param StandbyInstances: 灾备实例信息\n        :type StandbyInstances: list of DBInstanceInfo\n        :param CloneInstances: 临时实例信息\n        :type CloneInstances: list of DBInstanceInfo\n        :param RelatedInstance: 关联实例信息，对于正式实例，该字段表示它的临时实例信息；对于临时实例，则表示它的正式实例信息;如果为只读/灾备实例,则表示他的主实例信息\n        :type RelatedInstance: :class:`tencentcloud.mongodb.v20190725.models.DBInstanceInfo`\n        :param Tags: 实例标签信息集合\n        :type Tags: list of TagInfo\n        :param InstanceVer: 实例版本标记\n        :type InstanceVer: int\n        :param ClusterVer: 实例版本标记\n        :type ClusterVer: int\n        :param Protocol: 协议信息，可能的返回值：1-mongodb，2-dynamodb\n        :type Protocol: int\n        :param InstanceType: 实例类型，可能的返回值，1-正式实例，2-临时实例，3-只读实例，4-灾备实例\n        :type InstanceType: int\n        :param InstanceStatusDesc: 实例状态描述\n        :type InstanceStatusDesc: str\n        :param RealInstanceId: 实例对应的物理实例id，回档并替换过的实例有不同的InstanceId和RealInstanceId，从barad获取监控数据等场景下需要用物理id获取\n        :type RealInstanceId: str\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.PayMode = None
        self.ProjectId = None
        self.ClusterType = None
        self.Region = None
        self.Zone = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.DeadLine = None
        self.MongoVersion = None
        self.Memory = None
        self.Volume = None
        self.CpuNum = None
        self.MachineType = None
        self.SecondaryNum = None
        self.ReplicationSetNum = None
        self.AutoRenewFlag = None
        self.UsedVolume = None
        self.MaintenanceStart = None
        self.MaintenanceEnd = None
        self.ReplicaSets = None
        self.ReadonlyInstances = None
        self.StandbyInstances = None
        self.CloneInstances = None
        self.RelatedInstance = None
        self.Tags = None
        self.InstanceVer = None
        self.ClusterVer = None
        self.Protocol = None
        self.InstanceType = None
        self.InstanceStatusDesc = None
        self.RealInstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        self.ProjectId = params.get("ProjectId")
        self.ClusterType = params.get("ClusterType")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.DeadLine = params.get("DeadLine")
        self.MongoVersion = params.get("MongoVersion")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.CpuNum = params.get("CpuNum")
        self.MachineType = params.get("MachineType")
        self.SecondaryNum = params.get("SecondaryNum")
        self.ReplicationSetNum = params.get("ReplicationSetNum")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.UsedVolume = params.get("UsedVolume")
        self.MaintenanceStart = params.get("MaintenanceStart")
        self.MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self.ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self.ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self.StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self.CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self.RelatedInstance = DBInstanceInfo()
            self.RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceVer = params.get("InstanceVer")
        self.ClusterVer = params.get("ClusterVer")
        self.Protocol = params.get("Protocol")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.RealInstanceId = params.get("RealInstanceId")
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
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        """
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
        """
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。\n        :type AsyncRequestId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class KillOpsRequest(AbstractModel):
    """KillOps请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param Operations: 待终止的操作\n        :type Operations: list of Operation\n        """
        self.InstanceId = None
        self.Operations = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self.Operations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillOpsResponse(AbstractModel):
    """KillOps返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param Memory: 实例配置变更后的内存大小，单位：GB。内存和磁盘必须同时升配或同时降配\n        :type Memory: int\n        :param Volume: 实例配置变更后的硬盘大小，单位：GB。内存和磁盘必须同时升配或同时降配。降配时，新的磁盘参数必须大于已用磁盘容量的1.2倍\n        :type Volume: int\n        :param OplogSize: 实例配置变更后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%\n        :type OplogSize: int\n        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSpecResponse(AbstractModel):
    """ModifyDBInstanceSpec返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID\n        :type DealId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class OfflineIsolatedDBInstanceRequest(AbstractModel):
    """OfflineIsolatedDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineIsolatedDBInstanceResponse(AbstractModel):
    """OfflineIsolatedDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。\n        :type AsyncRequestId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class Operation(AbstractModel):
    """需要终止的操作

    """

    def __init__(self):
        """
        :param ReplicaSetName: 操作所在的分片名\n        :type ReplicaSetName: str\n        :param NodeName: 操作所在的节点名\n        :type NodeName: str\n        :param OpId: 操作序号\n        :type OpId: int\n        """
        self.ReplicaSetName = None
        self.NodeName = None
        self.OpId = None


    def _deserialize(self, params):
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.NodeName = params.get("NodeName")
        self.OpId = params.get("OpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceRequest(AbstractModel):
    """RenameInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param NewName: 实例名称\n        :type NewName: str\n        """
        self.InstanceId = None
        self.NewName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewName = params.get("NewName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenameInstanceResponse(AbstractModel):
    """RenameInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewDBInstancesRequest(AbstractModel):
    """RenewDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 一个或多个待操作的实例ID。可通过DescribeInstances接口返回值中的InstanceId获取。每次请求批量实例的上限为100。\n        :type InstanceIds: list of str\n        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。包年包月实例该参数为必传参数。\n        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`\n        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDBInstancesResponse(AbstractModel):
    """RenewDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplicaSetInfo(AbstractModel):
    """分片信息

    """

    def __init__(self):
        """
        :param ReplicaSetId: 分片名称\n        :type ReplicaSetId: str\n        """
        self.ReplicaSetId = None


    def _deserialize(self, params):
        self.ReplicaSetId = params.get("ReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDBInstancePasswordRequest(AbstractModel):
    """ResetDBInstancePassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param UserName: 实例账号名\n        :type UserName: str\n        :param Password: 新密码\n        :type Password: str\n        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDBInstancePasswordResponse(AbstractModel):
    """ResetDBInstancePassword返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步请求Id，用户查询该流程的运行状态\n        :type AsyncRequestId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组信息

    """

    def __init__(self):
        """
        :param ProjectId: 所属项目id\n        :type ProjectId: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param Inbound: 入站规则\n        :type Inbound: list of SecurityGroupBound\n        :param Outbound: 出站规则\n        :type Outbound: list of SecurityGroupBound\n        :param SecurityGroupId: 安全组id\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: 安全组备注\n        :type SecurityGroupRemark: str\n        """
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
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
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
        


class SecurityGroupBound(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        """
        :param Action: 执行规则。ACCEPT或DROP\n        :type Action: str\n        :param CidrIp: ip段。\n        :type CidrIp: str\n        :param PortRange: 端口范围\n        :type PortRange: str\n        :param IpProtocol: 传输层协议。tcp，udp或ALL\n        :type IpProtocol: str\n        :param Id: 安全组id代表的地址集合\n        :type Id: str\n        :param AddressModule: 地址组id代表的地址集合\n        :type AddressModule: str\n        :param ServiceModule: 服务组id代表的协议和端口集合\n        :type ServiceModule: str\n        :param Desc: 描述\n        :type Desc: str\n        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Id = None
        self.AddressModule = None
        self.ServiceModule = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Id = params.get("Id")
        self.AddressModule = params.get("AddressModule")
        self.ServiceModule = params.get("ServiceModule")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardInfo(AbstractModel):
    """实例分片详情

    """

    def __init__(self):
        """
        :param UsedVolume: 分片已使用容量\n        :type UsedVolume: float\n        :param ReplicaSetId: 分片ID\n        :type ReplicaSetId: str\n        :param ReplicaSetName: 分片名\n        :type ReplicaSetName: str\n        :param Memory: 分片内存规格，单位为MB\n        :type Memory: int\n        :param Volume: 分片磁盘规格，单位为MB\n        :type Volume: int\n        :param OplogSize: 分片Oplog大小，单位为MB\n        :type OplogSize: int\n        :param SecondaryNum: 分片从节点数\n        :type SecondaryNum: int\n        :param RealReplicaSetId: 分片物理id\n        :type RealReplicaSetId: str\n        """
        self.UsedVolume = None
        self.ReplicaSetId = None
        self.ReplicaSetName = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.SecondaryNum = None
        self.RealReplicaSetId = None


    def _deserialize(self, params):
        self.UsedVolume = params.get("UsedVolume")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.SecondaryNum = params.get("SecondaryNum")
        self.RealReplicaSetId = params.get("RealReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowLogPattern(AbstractModel):
    """用于描述MongoDB数据库慢日志统计信息

    """

    def __init__(self):
        """
        :param Pattern: 慢日志模式\n        :type Pattern: str\n        :param MaxTime: 最大执行时间\n        :type MaxTime: int\n        :param AverageTime: 平均执行时间\n        :type AverageTime: int\n        :param Total: 该模式慢日志条数\n        :type Total: int\n        """
        self.Pattern = None
        self.MaxTime = None
        self.AverageTime = None
        self.Total = None


    def _deserialize(self, params):
        self.Pattern = params.get("Pattern")
        self.MaxTime = params.get("MaxTime")
        self.AverageTime = params.get("AverageTime")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecItem(AbstractModel):
    """mongodb售卖规格

    """

    def __init__(self):
        """
        :param SpecCode: 规格信息标识\n        :type SpecCode: str\n        :param Status: 规格有效标志，取值：0-停止售卖，1-开放售卖\n        :type Status: int\n        :param Cpu: 计算资源规格，单位为CPU核心数\n        :type Cpu: int\n        :param Memory: 内存规格，单位为MB\n        :type Memory: int\n        :param DefaultStorage: 默认磁盘规格，单位MB\n        :type DefaultStorage: int\n        :param MaxStorage: 最大磁盘规格，单位MB\n        :type MaxStorage: int\n        :param MinStorage: 最小磁盘规格，单位MB\n        :type MinStorage: int\n        :param Qps: 可承载qps信息\n        :type Qps: int\n        :param Conns: 连接数限制\n        :type Conns: int\n        :param MongoVersionCode: 实例mongodb版本信息\n        :type MongoVersionCode: str\n        :param MongoVersionValue: 实例mongodb版本号\n        :type MongoVersionValue: int\n        :param Version: 实例mongodb版本号（短）\n        :type Version: str\n        :param EngineName: 存储引擎\n        :type EngineName: str\n        :param ClusterType: 集群类型，取值：1-分片集群，0-副本集集群\n        :type ClusterType: int\n        :param MinNodeNum: 最小副本集从节点数\n        :type MinNodeNum: int\n        :param MaxNodeNum: 最大副本集从节点数\n        :type MaxNodeNum: int\n        :param MinReplicateSetNum: 最小分片数\n        :type MinReplicateSetNum: int\n        :param MaxReplicateSetNum: 最大分片数\n        :type MaxReplicateSetNum: int\n        :param MinReplicateSetNodeNum: 最小分片从节点数\n        :type MinReplicateSetNodeNum: int\n        :param MaxReplicateSetNodeNum: 最大分片从节点数\n        :type MaxReplicateSetNodeNum: int\n        :param MachineType: 机器类型，取值：0-HIO，4-HIO10G\n        :type MachineType: str\n        """
        self.SpecCode = None
        self.Status = None
        self.Cpu = None
        self.Memory = None
        self.DefaultStorage = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Conns = None
        self.MongoVersionCode = None
        self.MongoVersionValue = None
        self.Version = None
        self.EngineName = None
        self.ClusterType = None
        self.MinNodeNum = None
        self.MaxNodeNum = None
        self.MinReplicateSetNum = None
        self.MaxReplicateSetNum = None
        self.MinReplicateSetNodeNum = None
        self.MaxReplicateSetNodeNum = None
        self.MachineType = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Status = params.get("Status")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.DefaultStorage = params.get("DefaultStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Conns = params.get("Conns")
        self.MongoVersionCode = params.get("MongoVersionCode")
        self.MongoVersionValue = params.get("MongoVersionValue")
        self.Version = params.get("Version")
        self.EngineName = params.get("EngineName")
        self.ClusterType = params.get("ClusterType")
        self.MinNodeNum = params.get("MinNodeNum")
        self.MaxNodeNum = params.get("MaxNodeNum")
        self.MinReplicateSetNum = params.get("MinReplicateSetNum")
        self.MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self.MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self.MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificationInfo(AbstractModel):
    """实例规格信息

    """

    def __init__(self):
        """
        :param Region: 地域信息\n        :type Region: str\n        :param Zone: 可用区信息\n        :type Zone: str\n        :param SpecItems: 售卖规格信息\n        :type SpecItems: list of SpecItem\n        """
        self.Region = None
        self.Zone = None
        self.SpecItems = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self.SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self.SpecItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """实例标签信息

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
        