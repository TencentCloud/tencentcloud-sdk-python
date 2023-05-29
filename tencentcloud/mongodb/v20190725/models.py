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
        r"""
        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceIds: list of str
        :param ProjectId: 项目ID，用户已创建项目的唯一ID,非自定义
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
        


class AssignProjectResponse(AbstractModel):
    """AssignProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowIds: 返回的异步任务ID列表
        :type FlowIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.RequestId = params.get("RequestId")


class Auth(AbstractModel):
    """用户权限

    """

    def __init__(self):
        r"""
        :param Mask: 当前账号具有的权限信息。<ul><li>0：无权限。</li><li>1：只读。</li><li>2：只写。</li><li>3：读写。</li></ul>
        :type Mask: int
        :param NameSpace: 指具有当前账号权限的数据库名。
<ul><li>* ：表示所有数据库。</li><li>db.name：表示特定name的数据库。</li></ul>
        :type NameSpace: str
        """
        self.Mask = None
        self.NameSpace = None


    def _deserialize(self, params):
        self.Mask = params.get("Mask")
        self.NameSpace = params.get("NameSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupDownloadTask(AbstractModel):
    """备份下载任务

    """

    def __init__(self):
        r"""
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param BackupName: 备份文件名
        :type BackupName: str
        :param ReplicaSetId: 分片名称
        :type ReplicaSetId: str
        :param BackupSize: 备份数据大小，单位为字节
        :type BackupSize: int
        :param Status: 任务状态。0-等待执行，1-正在下载，2-下载完成，3-下载失败，4-等待重试
        :type Status: int
        :param Percent: 任务进度百分比
        :type Percent: int
        :param TimeSpend: 耗时，单位为秒
        :type TimeSpend: int
        :param Url: 备份数据下载链接
        :type Url: str
        :param BackupMethod: 备份文件备份类型，0-逻辑备份，1-物理备份
        :type BackupMethod: int
        :param BackupDesc: 发起备份时指定的备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupDesc: str
        """
        self.CreateTime = None
        self.BackupName = None
        self.ReplicaSetId = None
        self.BackupSize = None
        self.Status = None
        self.Percent = None
        self.TimeSpend = None
        self.Url = None
        self.BackupMethod = None
        self.BackupDesc = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.BackupName = params.get("BackupName")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.BackupSize = params.get("BackupSize")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.TimeSpend = params.get("TimeSpend")
        self.Url = params.get("Url")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupDesc = params.get("BackupDesc")
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
        r"""
        :param ReplicaSetId: 分片名
        :type ReplicaSetId: str
        :param Status: 任务当前状态。0-等待执行，1-正在下载，2-下载完成，3-下载失败，4-等待重试
        :type Status: int
        """
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
        


class BackupInfo(AbstractModel):
    """备份信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param BackupType: 备份方式，0-自动备份，1-手动备份
        :type BackupType: int
        :param BackupName: 备份名称
        :type BackupName: str
        :param BackupDesc: 备份备注
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupDesc: str
        :param BackupSize: 备份文件大小，单位KB
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSize: int
        :param StartTime: 备份开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 备份结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Status: 备份状态，1-备份中，2-备份成功
        :type Status: int
        :param BackupMethod: 备份方法，0-逻辑备份，1-物理备份
        :type BackupMethod: int
        """
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
        r"""
        :param IP: 连接的客户端IP
        :type IP: str
        :param Count: 对应客户端IP的连接数
        :type Count: int
        :param InternalService: 是否为内部ip
        :type InternalService: bool
        """
        self.IP = None
        self.Count = None
        self.InternalService = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Count = params.get("Count")
        self.InternalService = params.get("InternalService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountUserRequest(AbstractModel):
    """CreateAccountUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。
        :type InstanceId: str
        :param UserName: 新账号名称。其格式要求如下：<ul><li>字符范围[1,32]。</li><li>可输入[A,Z]、[a,z]、[1,9]范围的字符以及下划线“_”与短划线“-”。</li></ul>
        :type UserName: str
        :param Password: 新账号密码。密码复杂度要求如下：<ul><li>字符长度范围[8,32]。</li><li>至少包含字母、数字和特殊字符（叹号“!”、at"@"、井号“#”、百分号“%”、插入符“^”、星号“*”、小括号“()”、下划线“_”）中的两种。</li></ul>
        :type Password: str
        :param MongoUserPassword: mongouser 账号对应的密码。mongouser 为系统默认账号，即为创建实例时，设置的密码。
        :type MongoUserPassword: str
        :param UserDesc: 账号备注信息。
        :type UserDesc: str
        :param AuthRole: 账号的读写权限信息。
        :type AuthRole: list of Auth
        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None
        self.MongoUserPassword = None
        self.UserDesc = None
        self.AuthRole = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.MongoUserPassword = params.get("MongoUserPassword")
        self.UserDesc = params.get("UserDesc")
        if params.get("AuthRole") is not None:
            self.AuthRole = []
            for item in params.get("AuthRole"):
                obj = Auth()
                obj._deserialize(item)
                self.AuthRole.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountUserResponse(AbstractModel):
    """CreateAccountUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 创建任务ID。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateBackupDBInstanceRequest(AbstractModel):
    """CreateBackupDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。
        :type InstanceId: str
        :param BackupMethod: 设置备份方式。
- 0：逻辑备份。
- 1：物理备份。
        :type BackupMethod: int
        :param BackupRemark: 备份备注信息。
        :type BackupRemark: str
        """
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
        r"""
        :param AsyncRequestId: 查询备份流程的状态。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateBackupDownloadTaskRequest(AbstractModel):
    """CreateBackupDownloadTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param BackupName: 要下载的备份文件名，可通过DescribeDBBackups接口获取。
        :type BackupName: str
        :param BackupSets: 指定要下载的副本集的节点名称 或 分片集群的分片名称列表。
如副本集cmgo-p8vnipr5，示例(固定取值)：BackupSets.0=cmgo-p8vnipr5_0，可下载全量数据。
如分片集群cmgo-p8vnipr5，示例：BackupSets.0=cmgo-p8vnipr5_0&BackupSets.1=cmgo-p8vnipr5_1，即下载分片0和分片1的数据，分片集群如需全量下载，请按示例方式传入全部分片名称。
        :type BackupSets: list of ReplicaSetInfo
        """
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
        r"""
        :param Tasks: 下载任务状态
        :type Tasks: list of BackupDownloadTaskStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Memory: 实例内存大小，单位：GB。
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB。
        :type Volume: int
        :param ReplicateSetNum: 指副本集数量。
- 创建副本集实例，该参数只能为1。
- 创建分片实例，指分片的数量。具体售卖规格，请通过接口 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567) 获取。
        :type ReplicateSetNum: int
        :param NodeNum: 指每个副本集内节点个数。具体售卖规格，请通过接口 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567) 获取。
        :type NodeNum: int
        :param MongoVersion: 指版本信息。具体售卖规格，请通过接口 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567) 获取。
- MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本。
- MONGO_40_WT：MongoDB 4.0 WiredTiger存储引擎版本。
- MONGO_42_WT：MongoDB 4.2 WiredTiger存储引擎版本。
- MONGO_44_WT：MongoDB 4.4 WiredTiger存储引擎版本。
        :type MongoVersion: str
        :param MachineCode: 机器类型。
- HIO：高IO型。
- HIO10G：高IO万兆。
        :type MachineCode: str
        :param GoodsNum: 实例数量，最小值1，最大值为10。
        :type GoodsNum: int
        :param Zone: 可用区信息，输入格式如：ap-guangzhou-2。
- 具体信息，请通过接口 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567) 获取。
- 该参数为主可用区，如果多可用区部署，Zone必须是AvailabilityZoneList中的一个。
        :type Zone: str
        :param ClusterType: 实例架构类型。
- REPLSET：副本集。
- SHARD：分片集群。
        :type ClusterType: str
        :param VpcId: 私有网络ID。如果不设置该参数，则默认选择基础网络。
        :type VpcId: str
        :param SubnetId: 私有网络下的子网 ID，如果配置参数 VpcId，则 SubnetId必须配置。
        :type SubnetId: str
        :param Password: 实例密码。自定义密码长度为8-32个字符，至少包含字母、数字和字符（!@#%^*()_）中的两种。
        :type Password: str
        :param ProjectId: 项目ID。若不设置该参数，则为默认项目。
        :type ProjectId: int
        :param Tags: 实例标签信息。
        :type Tags: list of TagInfo
        :param Clone: 实例类型。
- 1：正式实例。
- 3：只读实例。
- 4：灾备实例。
        :type Clone: int
        :param Father: 父实例 ID。当参数**Clone**为3或者4时，即实例为只读或灾备实例时，该参数必须配置。
        :type Father: str
        :param SecurityGroup: 安全组。
        :type SecurityGroup: list of str
        :param RestoreTime: 克隆实例回档时间。
- 若为克隆实例，则必须配置该参数。输入格式示例：2021-08-13 16:30:00。
- 回档时间范围：仅能回档7天内时间点的数据。
        :type RestoreTime: str
        :param InstanceName: 实例名称。仅支持长度为60个字符的中文、英文、数字、下划线_、分隔符- 。
        :type InstanceName: str
        :param AvailabilityZoneList: 多可用区部署的节点列表。具体信息，请通过接口 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567)获取。
- 多可用区部署节点只能部署在3个不同可用区。不支持将集群的大多数节点部署在同一个可用区。例如：3节点集群不支持2个节点部署在同一个区。
- 不支持4.2及以上版本。
- 不支持只读灾备实例。
- 不能选择基础网络。
        :type AvailabilityZoneList: list of str
        :param MongosCpu: Mongos CPU 核数。
- 购买MongoDB 3.6 WiredTiger存储引擎版本以上的分片集群时，可选择性配置该参数。
- 若不配置该参数，则根据Mongod节点规格默认适配 Mongos 规格，默认规格免费。
        :type MongosCpu: int
        :param MongosMemory: Mongos 内存大小。
- 购买MongoDB 3.6 WiredTiger存储引擎版本以上的分片集群时，可选择性配置该参数。
- 若不配置该参数，则根据Mongod节点规格默认适配 Mongos 规格，默认规格免费。
        :type MongosMemory: int
        :param MongosNodeNum: Mongos 数量。
- 购买MongoDB 3.6 WiredTiger存储引擎版本以上的分片集群时，可选择性配置该参数。
- 若不配置该参数，则根据Mongod节点规格默认适配 Mongos 规格，默认规格免费。
        :type MongosNodeNum: int
        :param ReadonlyNodeNum: 只读节点数量，最大不超过7个。
        :type ReadonlyNodeNum: int
        :param ReadonlyNodeAvailabilityZoneList: 指只读节点所属可用区。跨可用区部署实例，参数**ReadonlyNodeNum**不为**0**时，必须配置该参数。
        :type ReadonlyNodeAvailabilityZoneList: list of str
        :param HiddenZone: Hidden节点所属可用区。跨可用区部署实例，必须配置该参数。
        :type HiddenZone: str
        """
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
        self.RestoreTime = None
        self.InstanceName = None
        self.AvailabilityZoneList = None
        self.MongosCpu = None
        self.MongosMemory = None
        self.MongosNodeNum = None
        self.ReadonlyNodeNum = None
        self.ReadonlyNodeAvailabilityZoneList = None
        self.HiddenZone = None


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
        self.RestoreTime = params.get("RestoreTime")
        self.InstanceName = params.get("InstanceName")
        self.AvailabilityZoneList = params.get("AvailabilityZoneList")
        self.MongosCpu = params.get("MongosCpu")
        self.MongosMemory = params.get("MongosMemory")
        self.MongosNodeNum = params.get("MongosNodeNum")
        self.ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        self.ReadonlyNodeAvailabilityZoneList = params.get("ReadonlyNodeAvailabilityZoneList")
        self.HiddenZone = params.get("HiddenZone")
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
        r"""
        :param DealId: 订单ID。
        :type DealId: str
        :param InstanceIds: 创建的实例ID列表。
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


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeNum: 每个副本集内节点个数，具体参照查询云数据库的售卖规格返回参数
        :type NodeNum: int
        :param Memory: 实例内存大小，单位：GB
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB
        :type Volume: int
        :param MongoVersion: 版本号，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。参数与版本对应关系是MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本，MONGO_40_WT：MongoDB 4.0 WiredTiger存储引擎版本，MONGO_42_WT：MongoDB 4.2 WiredTiger存储引擎版本
        :type MongoVersion: str
        :param GoodsNum: 实例数量, 最小值1，最大值为10
        :type GoodsNum: int
        :param Zone: 实例所属区域名称，格式如：ap-guangzhou-2。注：此参数填写的是主可用区，如果选择多可用区部署，Zone必须是AvailabilityZoneList中的一个
        :type Zone: str
        :param Period: 实例时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param MachineCode: 机器类型，HIO：高IO型；HIO10G：高IO万兆型；STDS5：标准型
        :type MachineCode: str
        :param ClusterType: 实例类型，REPLSET-副本集，SHARD-分片集群，STANDALONE-单节点
        :type ClusterType: str
        :param ReplicateSetNum: 副本集个数，创建副本集实例时，该参数必须设置为1；创建分片实例时，具体参照查询云数据库的售卖规格返回参数；若为单节点实例，该参数设置为0
        :type ReplicateSetNum: int
        :param ProjectId: 项目ID，不设置为默认项目
        :type ProjectId: int
        :param VpcId: 私有网络 ID，如果不传则默认选择基础网络，请使用 查询私有网络列表
        :type VpcId: str
        :param SubnetId: 私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 查询子网列表
        :type SubnetId: str
        :param Password: 实例密码，不设置该参数则默认密码规则为 实例ID+"@"+主账户uin。举例实例id为cmgo-higv73ed，uin为100000001，则默认密码为"cmgo-higv73ed@100000001"。 自定义密码格式为8-32个字符长度，至少包含字母、数字和字符（!@#%^*()_）中的两种
        :type Password: str
        :param Tags: 实例标签信息
        :type Tags: list of TagInfo
        :param AutoRenewFlag: 自动续费标记，可选值为：0 - 不自动续费；1 - 自动续费。默认为不自动续费
        :type AutoRenewFlag: int
        :param AutoVoucher: 是否自动选择代金券，可选值为：1 - 是；0 - 否； 默认为0
        :type AutoVoucher: int
        :param Clone: 1:正式实例,2:临时实例,3:只读实例,4:灾备实例,5:克隆实例
        :type Clone: int
        :param Father: 若是只读，灾备实例或克隆实例，Father必须填写，即主实例ID
        :type Father: str
        :param SecurityGroup: 安全组
        :type SecurityGroup: list of str
        :param RestoreTime: 克隆实例回档时间。若是克隆实例，则必须填写，格式：2021-08-13 16:30:00。注：只能回档7天内的时间点
        :type RestoreTime: str
        :param InstanceName: 实例名称。注：名称只支持长度为60个字符的中文、英文、数字、下划线_、分隔符-
        :type InstanceName: str
        :param AvailabilityZoneList: 多可用区部署的节点列表，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。注：1、多可用区部署节点只能部署在3个不同可用区；2、为了保障跨可用区切换，不支持将集群的大多数节点部署在同一个可用区（如3节点集群不支持2个节点部署在同一个区）；3、不支持4.2及以上版本；4、不支持只读灾备实例；5、不能选择基础网络
        :type AvailabilityZoneList: list of str
        :param MongosCpu: mongos cpu数量，购买MongoDB 4.2 WiredTiger存储引擎版本的分片集群时必须填写，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果
        :type MongosCpu: int
        :param MongosMemory: mongos 内存大小，购买MongoDB 4.2 WiredTiger存储引擎版本的分片集群时必须填写，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果
        :type MongosMemory: int
        :param MongosNodeNum: mongos 数量，购买MongoDB 4.2 WiredTiger存储引擎版本的分片集群时必须填写，具体支持的售卖版本请参照查询云数据库的售卖规格（DescribeSpecInfo）返回结果。注：为了保障高可用，最低需要购买3个mongos，上限为32个
        :type MongosNodeNum: int
        :param ReadonlyNodeNum: 只读节点数量，最大不超过7个
        :type ReadonlyNodeNum: int
        :param ReadonlyNodeAvailabilityZoneList: 只读节点部署可用区
        :type ReadonlyNodeAvailabilityZoneList: list of str
        :param HiddenZone: Hidden节点所在的可用区，跨可用区实例必传
        :type HiddenZone: str
        """
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
        self.RestoreTime = None
        self.InstanceName = None
        self.AvailabilityZoneList = None
        self.MongosCpu = None
        self.MongosMemory = None
        self.MongosNodeNum = None
        self.ReadonlyNodeNum = None
        self.ReadonlyNodeAvailabilityZoneList = None
        self.HiddenZone = None


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
        self.RestoreTime = params.get("RestoreTime")
        self.InstanceName = params.get("InstanceName")
        self.AvailabilityZoneList = params.get("AvailabilityZoneList")
        self.MongosCpu = params.get("MongosCpu")
        self.MongosMemory = params.get("MongosMemory")
        self.MongosNodeNum = params.get("MongosNodeNum")
        self.ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        self.ReadonlyNodeAvailabilityZoneList = params.get("ReadonlyNodeAvailabilityZoneList")
        self.HiddenZone = params.get("HiddenZone")
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
        r"""
        :param DealId: 订单ID
        :type DealId: str
        :param InstanceIds: 创建的实例ID列表
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


class CurrentOp(AbstractModel):
    """云数据库实例当前操作

    """

    def __init__(self):
        r"""
        :param OpId: 操作序号
注意：此字段可能返回 null，表示取不到有效值。
        :type OpId: int
        :param Ns: 操作所在的命名空间，形式如db.collection
注意：此字段可能返回 null，表示取不到有效值。
        :type Ns: str
        :param Query: 操作执行语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Query: str
        :param Op: 操作类型，可能的取值：aggregate、count、delete、distinct、find、findAndModify、getMore、insert、mapReduce、update和command
注意：此字段可能返回 null，表示取不到有效值。
        :type Op: str
        :param ReplicaSetName: 操作所在的分片名称
        :type ReplicaSetName: str
        :param State: 筛选条件，节点状态，可能的取值为：Primary、Secondary
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param Operation: 操作详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param NodeName: 操作所在的节点名称
        :type NodeName: str
        :param MicrosecsRunning: 操作已执行时间（ms）
注意：此字段可能返回 null，表示取不到有效值。
        :type MicrosecsRunning: int
        """
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
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Region: 地域信息
        :type Region: str
        """
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
        r"""
        :param UnitPrice: 单价
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param OriginalPrice: 原价
        :type OriginalPrice: float
        :param DiscountPrice: 折扣加
        :type DiscountPrice: float
        """
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
        


class DeleteAccountUserRequest(AbstractModel):
    """DeleteAccountUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 指定待删除账号的实例 ID。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。

        :type InstanceId: str
        :param UserName: 配置待删除的账号名。
        :type UserName: str
        :param MongoUserPassword: 配置 mongouser 对应的密码。mongouser为系统默认账号，输入其对应的密码。
        :type MongoUserPassword: str
        """
        self.InstanceId = None
        self.UserName = None
        self.MongoUserPassword = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.MongoUserPassword = params.get("MongoUserPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountUserResponse(AbstractModel):
    """DeleteAccountUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 账户删除任务ID。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DescribeAccountUsersRequest(AbstractModel):
    """DescribeAccountUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 指定待获取账号的实例ID。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。
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
        


class DescribeAccountUsersResponse(AbstractModel):
    """DescribeAccountUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Users: 实例账号列表。
        :type Users: list of UserInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步请求Id，涉及到异步流程的接口返回，如CreateBackupDBInstance
        :type AsyncRequestId: str
        """
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
        r"""
        :param Status: 状态。返回参数有：initial-初始化、running-运行中、paused-任务执行失败，已暂停、undoed-任务执行失败，已回滚、failed-任务执行失败, 已终止、success-成功
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeBackupDownloadTaskRequest(AbstractModel):
    """DescribeBackupDownloadTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param BackupName: 备份文件名，用来过滤指定文件的下载任务
        :type BackupName: str
        :param StartTime: 指定查询时间范围内的任务，StartTime指定开始时间，不填默认不限制开始时间
        :type StartTime: str
        :param EndTime: 指定查询时间范围内的任务，EndTime指定截止时间，不填默认不限制截止时间
        :type EndTime: str
        :param Limit: 此次查询返回的条数，取值范围为1-100，默认为20
        :type Limit: int
        :param Offset: 指定此次查询返回的页数，默认为0
        :type Offset: int
        :param OrderBy: 排序字段，取值为createTime，finishTime两种，默认为createTime
        :type OrderBy: str
        :param OrderByType: 排序方式，取值为asc，desc两种，默认desc
        :type OrderByType: str
        :param Status: 根据任务状态过滤。0-等待执行，1-正在下载，2-下载完成，3-下载失败，4-等待重试。不填默认返回所有类型
        :type Status: list of int
        """
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
        r"""
        :param TotalCount: 满足查询条件的所有条数
        :type TotalCount: int
        :param Tasks: 下载任务列表
        :type Tasks: list of BackupDownloadTask
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
                obj = BackupDownloadTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 指定待查询的实例ID，例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。

        :type InstanceId: str
        :param Limit: 单次请求返回的数量。最小值为1，最大值为1000，默认值为1000。
        :type Limit: int
        :param Offset: 偏移量，默认值为0。Offset=Limit*(页码-1)。
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
        


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param Clients: 客户端连接信息，包括客户端 IP 和对应 IP 的连接数量。
        :type Clients: list of ClientConnection
        :param TotalCount: 满足条件的记录总条数，可用于分页查询。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param Ns: 筛选条件，操作所属的命名空间namespace，格式为db.collection
        :type Ns: str
        :param MillisecondRunning: 筛选条件，操作已经执行的时间（单位：毫秒），结果将返回超过设置时间的操作，默认值为0，取值范围为[0, 3600000]
        :type MillisecondRunning: int
        :param Op: 筛选条件，操作类型，可能的取值：none，update，insert，query，command，getmore，remove和killcursors
        :type Op: str
        :param ReplicaSetName: 筛选条件，分片名称
        :type ReplicaSetName: str
        :param State: 筛选条件，节点状态，可能的取值为：primary
secondary
        :type State: str
        :param Limit: 单次请求返回的数量，默认值为100，取值范围为[0,100]
        :type Limit: int
        :param Offset: 偏移量，默认值为0，取值范围为[0,10000]
        :type Offset: int
        :param OrderBy: 返回结果集排序的字段，目前支持："MicrosecsRunning"/"microsecsrunning"，默认为升序排序
        :type OrderBy: str
        :param OrderByType: 返回结果集排序方式，可能的取值："ASC"/"asc"或"DESC"/"desc"
        :type OrderByType: str
        """
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
        r"""
        :param TotalCount: 符合查询条件的操作总数
        :type TotalCount: int
        :param CurrentOps: 当前操作列表
        :type CurrentOps: list of CurrentOp
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param BackupMethod: 备份方式，当前支持：0-逻辑备份，1-物理备份，2-所有备份。默认为逻辑备份。
        :type BackupMethod: int
        :param Limit: 分页大小，最大值为100，不设置默认查询所有。
        :type Limit: int
        :param Offset: 分页偏移量，最小值为0，默认值为0。
        :type Offset: int
        """
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
        r"""
        :param BackupList: 备份列表
        :type BackupList: list of BackupInfo
        :param TotalCount: 备份总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param DealId: 订单ID，通过CreateDBInstance等接口返回
        :type DealId: str
        """
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
        r"""
        :param Status: 订单状态，1：未支付，2：已支付，3：发货中，4：发货成功，5：发货失败，6：退款，7：订单关闭，8：超时未支付关闭。
        :type Status: int
        :param OriginalPrice: 订单原价。
        :type OriginalPrice: float
        :param DiscountPrice: 订单折扣价格。
        :type DiscountPrice: float
        :param Action: 订单行为，purchase：新购，renew：续费，upgrade：升配，downgrade：降配，refund：退货退款。
        :type Action: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeDBInstanceNodePropertyRequest(AbstractModel):
    """DescribeDBInstanceNodeProperty请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param NodeIds: 节点ID。
        :type NodeIds: list of str
        :param Roles: 节点角色。可选值包括：
<ul><li>PRIMARY：主节点。</li><li>SECONDARY：从节点。</li><li>READONLY：只读节点。</li><li>ARBITER：仲裁节点。</li></ul>
        :type Roles: list of str
        :param OnlyHidden: 该参数指定节点是否为Hidden节点，默认为false。
        :type OnlyHidden: bool
        :param Priority: 该参数指定选举新主节点的优先级。其取值范围为[0,100]，数值越高，优先级越高。
        :type Priority: int
        :param Votes: 该参数指定节点投票权。
<ul><li>1：具有投票权。</li><li>0：无投票权。</li></ul>
        :type Votes: int
        :param Tags: 节点标签。
        :type Tags: list of NodeTag
        """
        self.InstanceId = None
        self.NodeIds = None
        self.Roles = None
        self.OnlyHidden = None
        self.Priority = None
        self.Votes = None
        self.Tags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeIds = params.get("NodeIds")
        self.Roles = params.get("Roles")
        self.OnlyHidden = params.get("OnlyHidden")
        self.Priority = params.get("Priority")
        self.Votes = params.get("Votes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = NodeTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBInstanceNodePropertyResponse(AbstractModel):
    """DescribeDBInstanceNodeProperty返回参数结构体

    """

    def __init__(self):
        r"""
        :param Mongos: Mongos节点属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mongos: list of NodeProperty
        :param ReplicateSets: 副本集节点信息。
        :type ReplicateSets: list of ReplicateSetInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Mongos = None
        self.ReplicateSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Mongos") is not None:
            self.Mongos = []
            for item in params.get("Mongos"):
                obj = NodeProperty()
                obj._deserialize(item)
                self.Mongos.append(obj)
        if params.get("ReplicateSets") is not None:
            self.ReplicateSets = []
            for item in params.get("ReplicateSets"):
                obj = ReplicateSetInfo()
                obj._deserialize(item)
                self.ReplicateSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例 ID 列表。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。
        :type InstanceIds: list of str
        :param InstanceType: 实例类型。取值范围如下：<ul><li>0：所有实例。</li><li>1：正式实例。</li><li>2：临时实例。</li><li>3：只读实例。</li><li>-1：正式实例、只读、灾备实例。</li></ul>
        :type InstanceType: int
        :param ClusterType: 集群类型，取值范围如下：<ul><li>0：副本集实例。</li><li>1：分片实例。</li><li>-1：所有实例。</li></ul>
        :type ClusterType: int
        :param Status: 实例状态，取值范围如下所示：<ul><li>0：待初始化。</li><li>1：流程执行中。</li><li>2：实例有效。</li><li>-2：已隔离（包年包月实例）。</li><li>-3：已隔离（按量计费实例）。</li></ul>
        :type Status: list of int
        :param VpcId: 私有网络的 ID。
- 基础网络则无需配置该参数。
- 请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表中，单击私有网络名称，在**私有网络**页面获取其 ID。
        :type VpcId: str
        :param SubnetId: 私有网络的子网ID。
- 基础网络则无需配置该参数。
- 请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表中，单击私有网络名称，在**私有网络**页面获取其子网 ID。
        :type SubnetId: str
        :param PayMode: 付费类型，取值范围如下：<ul><li>0：查询按量计费实例。</li><li>1：查询包年包月实例。</li><li>-1：查询按量计费与包年包月实例。</li></ul>
        :type PayMode: int
        :param Limit: 单次请求返回的数量。默认值为20，取值范围为[1,100]。
        :type Limit: int
        :param Offset: 偏移量，默认值为0。
        :type Offset: int
        :param OrderBy: 配置返回结果排序依据的字段。目前支持依据"ProjectId"、"InstanceName"、"CreateTime"排序。
        :type OrderBy: str
        :param OrderByType: 配置返回结果的排序方式。
- ASC：升序。
- DESC：降序。
        :type OrderByType: str
        :param ProjectIds: 项目 ID。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)，在右上角的账户信息下拉菜单中，选择项目管理查询项目。
        :type ProjectIds: list of int non-negative
        :param SearchKey: 配置查询搜索的关键词。支持配置为实例ID、实例名称或者内网 IP 地址。
        :type SearchKey: str
        :param Tags: 标签信息，包含标签键与标签值。
        :type Tags: list of TagInfo
        """
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
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
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
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param InstanceDetails: 实例详细信息列表。
        :type InstanceDetails: list of InstanceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 指定待查询参数列表的实例ID。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。
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
        :param InstanceEnumParam: 参数值为枚举类型参数集合。
        :type InstanceEnumParam: list of InstanceEnumParam
        :param InstanceIntegerParam: 参数值为 Integer 类型参数集合。
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param InstanceTextParam: 参数值为 Text 类型的参数集合。
        :type InstanceTextParam: list of InstanceTextParam
        :param InstanceMultiParam: 参数值为混合类型的参数集合。
        :type InstanceMultiParam: list of InstanceMultiParam
        :param TotalCount: 当前实例支持修改的参数个数统计 如0
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceEnumParam = None
        self.InstanceIntegerParam = None
        self.InstanceTextParam = None
        self.InstanceMultiParam = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
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
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupRequest(AbstractModel):
    """DescribeSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。例如：cmgo-p8vn****。
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
        


class DescribeSecurityGroupResponse(AbstractModel):
    """DescribeSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Groups: 实例绑定的安全组信息。
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


class DescribeSlowLogPatternsRequest(AbstractModel):
    """DescribeSlowLogPatterns请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param StartTime: 慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :type StartTime: str
        :param EndTime: 慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :type EndTime: str
        :param SlowMS: 慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。
        :type SlowMS: int
        :param Offset: 偏移量，最小值为0，最大值为10000，默认值为0。
        :type Offset: int
        :param Limit: 分页大小，最小值为1，最大值为100，默认值为20。
        :type Limit: int
        :param Format: 慢日志返回格式，可设置为json，不传默认返回原生慢日志格式。
        :type Format: str
        """
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
        r"""
        :param Count: 慢日志统计信息总数
        :type Count: int
        :param SlowLogPatterns: 慢日志统计信息
        :type SlowLogPatterns: list of SlowLogPattern
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param StartTime: 慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :type StartTime: str
        :param EndTime: 慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。
        :type EndTime: str
        :param SlowMS: 慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。
        :type SlowMS: int
        :param Offset: 偏移量，最小值为0，最大值为10000，默认值为0。
        :type Offset: int
        :param Limit: 分页大小，最小值为1，最大值为100，默认值为20。
        :type Limit: int
        :param Format: 慢日志返回格式。默认返回原生慢日志格式，4.4及以上版本可设置为json。
        :type Format: str
        """
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
        r"""
        :param Count: 慢日志总数
        :type Count: int
        :param SlowLogs: 慢日志详情
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowLogs: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Zone: 待查询可用区
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
        


class DescribeSpecInfoResponse(AbstractModel):
    """DescribeSpecInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpecInfoList: 实例售卖规格信息列表
        :type SpecInfoList: list of SpecificationInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        


class FlushInstanceRouterConfigResponse(AbstractModel):
    """FlushInstanceRouterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InquirePriceCreateDBInstancesRequest(AbstractModel):
    """InquirePriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 实例所属区域及可用区信息。格式：ap-guangzhou-2。
        :type Zone: str
        :param NodeNum: 每个分片的主从节点数量。<br>取值范围：请通过接口<a href="https://cloud.tencent.com/document/product/240/38567">DescribeSpecInfo</a>查询，其返回的数据结构SpecItems中的参数MinNodeNum与MaxNodeNum分别对应其最小值与最大值。</li></ul>
        :type NodeNum: int
        :param Memory: 实例内存大小。<ul><li>单位：GB。</li><li>取值范围：请通过接口<a href="https://cloud.tencent.com/document/product/240/38567">DescribeSpecInfo</a>查询，其返回的数据结构SpecItems中的参数CPU与Memory分别对应CPU核数与内存规格。</li></ul>
        :type Memory: int
        :param Volume: 实例硬盘大小。<ul><li>单位：GB。</li><li>取值范围：请通过接口<a href="https://cloud.tencent.com/document/product/240/38567">DescribeSpecInfo</a>查询，其返回的数据结构SpecItems中的参数MinStorage与MaxStorage分别对应其最小磁盘规格与最大磁盘规格。</br>
        :type Volume: int
        :param MongoVersion: 实例版本信息。<ul><li>具体支持的版本，请通过接口<a href="https://cloud.tencent.com/document/product/240/38567">DescribeSpecInfo</a>查询，其返回的数据结构SpecItems中的参数MongoVersionCode为实例所支持的版本信息。</li><li>版本信息与版本号对应关系如下：<ul><li>MONGO_3_WT：MongoDB 3.2 WiredTiger存储引擎版本。</li><li>MONGO_3_ROCKS：MongoDB 3.2 RocksDB存储引擎版本。</li><li>MONGO_36_WT：MongoDB 3.6 WiredTiger存储引擎版本。</li><li>MONGO_40_WT：MongoDB 4.0 WiredTiger存储引擎版本。</li><li>MONGO_42_WT：MongoDB 4.2 WiredTiger存储引擎版本。</li><li>MONGO_44_WT：MongoDB 4.4 WiredTiger存储引擎版本。</li></ul>
        :type MongoVersion: str
        :param MachineCode: 机器类型。<ul><li>HIO：高IO型。</li><li>HIO10G：高IO万兆型。</li></ul>
        :type MachineCode: str
        :param GoodsNum: 实例数量，取值范围为[1,10]。
        :type GoodsNum: int
        :param ClusterType: 实例类型。<ul><li>REPLSET：副本集。</li><li>SHARD：分片集群。</li><li>STANDALONE：单节点。</li></ul>
        :type ClusterType: str
        :param ReplicateSetNum: 副本集个数。<ul><li>创建副本集实例时，该参数固定设置为1。</li><li>创建分片集群时，指分片数量，请通过接口<a href="https://cloud.tencent.com/document/product/240/38567">DescribeSpecInfo</a>查询，其返回的数据结构SpecItems中的参数MinReplicateSetNum与MaxReplicateSetNum分别对应其最小值与最大值。</li><li>若为单节点实例，该参数固定设置为0。</li></ul>
        :type ReplicateSetNum: int
        :param Period: 选择包年包月计费模式时，您需要设定购买实例的时长。即<b>InstanceChargeType</b>设定为<b>PREPAID</b>时，该参数必须配置。<ul><li>单位：月。</li><li>可选值包括[1,2,3,4,5,6,7,8,9,10,11,12,24,36]。</li></ul>
        :type Period: int
        :param InstanceChargeType: 实例付费方式。<ul><li>PREPAID：包年包月计费。</li><li>POSTPAID_BY_HOUR：按量计费。</li></ul>
        :type InstanceChargeType: str
        :param MongosCpu: 分片实例询价必填参数，指 Mongos CPU核数，取值范围为[1,16]。
        :type MongosCpu: int
        :param MongosMemory: 分片实例询价必填参数，指 Mongos 内存，取值范围为[2,32]，单位：GB。
        :type MongosMemory: int
        :param MongosNum: 分片实例询价必填参数，指 Mongos 个数，取值范围为[3,32]。
        :type MongosNum: int
        :param ConfigServerCpu: 分片实例询价必填参数，指 ConfigServer CPU核数，取值为1，单位：GB。
        :type ConfigServerCpu: int
        :param ConfigServerMemory: 分片实例询价必填参数，指 ConfigServer 内存大小，取值为2，单位：GB。
        :type ConfigServerMemory: int
        :param ConfigServerVolume: 分片实例询价必填参数，指 ConfigServer 磁盘大小，取值为 20，单位：GB。
        :type ConfigServerVolume: int
        """
        self.Zone = None
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.ClusterType = None
        self.ReplicateSetNum = None
        self.Period = None
        self.InstanceChargeType = None
        self.MongosCpu = None
        self.MongosMemory = None
        self.MongosNum = None
        self.ConfigServerCpu = None
        self.ConfigServerMemory = None
        self.ConfigServerVolume = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.Period = params.get("Period")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.MongosCpu = params.get("MongosCpu")
        self.MongosMemory = params.get("MongosMemory")
        self.MongosNum = params.get("MongosNum")
        self.ConfigServerCpu = params.get("ConfigServerCpu")
        self.ConfigServerMemory = params.get("ConfigServerMemory")
        self.ConfigServerVolume = params.get("ConfigServerVolume")
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
        r"""
        :param Price: 价格
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 实例 ID，格式如：cmgo-p8vn****。与云数据库控制台页面中显示的实例ID相同。
        :type InstanceId: str
        :param Memory: 变更配置后实例内存大小，单位：GB。
        :type Memory: int
        :param Volume: 变更配置后实例磁盘大小，单位：GB。
        :type Volume: int
        :param NodeNum: 实例节点数。默认为不变更节点数，暂不支持变更。
        :type NodeNum: int
        :param ReplicateSetNum: 实例分片数。默认为不变更分片数，暂不支持变更。
        :type ReplicateSetNum: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.NodeNum = None
        self.ReplicateSetNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.NodeNum = params.get("NodeNum")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
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
        r"""
        :param Price: 价格。
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceIds: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同，接口单次最多只支持5个实例进行操作。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 预付费模式（即包年包月）相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
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
        r"""
        :param Price: 价格
        :type Price: :class:`tencentcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。默认为1。
（InquirePriceRenewDBInstances，RenewDBInstances调用时必填）
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
（InquirePriceRenewDBInstances，RenewDBInstances调用时必填）
        :type RenewFlag: str
        """
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
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param PayMode: 付费类型，可能的返回值：1-包年包月；0-按量计费
        :type PayMode: int
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param ClusterType: 集群类型，可能的返回值：0-副本集实例，1-分片实例。
        :type ClusterType: int
        :param Region: 地域信息。
        :type Region: str
        :param Zone: 可用区信息。
        :type Zone: str
        :param NetType: 网络类型，可能的返回值：0-基础网络，1-私有网络
        :type NetType: int
        :param VpcId: 私有网络的ID。
        :type VpcId: str
        :param SubnetId: 私有网络的子网ID。
        :type SubnetId: str
        :param Status: 实例状态，可能的返回值：0-待初始化，1-流程处理中，2-运行中，-2-实例已过期。
        :type Status: int
        :param Vip: 实例IP。
        :type Vip: str
        :param Vport: 端口号。
        :type Vport: int
        :param CreateTime: 实例创建时间。
        :type CreateTime: str
        :param DeadLine: 实例到期时间。
        :type DeadLine: str
        :param MongoVersion: 实例版本信息。
        :type MongoVersion: str
        :param Memory: 实例内存规格，单位为MB。
        :type Memory: int
        :param Volume: 实例磁盘规格，单位为MB。
        :type Volume: int
        :param CpuNum: 实例CPU核心数。
        :type CpuNum: int
        :param MachineType: 实例机器类型。
        :type MachineType: str
        :param SecondaryNum: 实例从节点数。
        :type SecondaryNum: int
        :param ReplicationSetNum: 实例分片数。
        :type ReplicationSetNum: int
        :param AutoRenewFlag: 实例自动续费标志，可能的返回值：0-手动续费，1-自动续费，2-确认不续费。
        :type AutoRenewFlag: int
        :param UsedVolume: 已用容量，单位MB。
        :type UsedVolume: int
        :param MaintenanceStart: 维护窗口起始时间。
        :type MaintenanceStart: str
        :param MaintenanceEnd: 维护窗口结束时间。
        :type MaintenanceEnd: str
        :param ReplicaSets: 分片信息。
        :type ReplicaSets: list of ShardInfo
        :param ReadonlyInstances: 只读实例信息。
        :type ReadonlyInstances: list of DBInstanceInfo
        :param StandbyInstances: 灾备实例信息。
        :type StandbyInstances: list of DBInstanceInfo
        :param CloneInstances: 临时实例信息。
        :type CloneInstances: list of DBInstanceInfo
        :param RelatedInstance: 关联实例信息，对于正式实例，该字段表示它的临时实例信息；对于临时实例，则表示它的正式实例信息;如果为只读/灾备实例,则表示他的主实例信息。
        :type RelatedInstance: :class:`tencentcloud.mongodb.v20190725.models.DBInstanceInfo`
        :param Tags: 实例标签信息集合。
        :type Tags: list of TagInfo
        :param InstanceVer: 实例版本标记。
        :type InstanceVer: int
        :param ClusterVer: 实例版本标记。
        :type ClusterVer: int
        :param Protocol: 协议信息，可能的返回值：1-mongodb，2-dynamodb。
        :type Protocol: int
        :param InstanceType: 实例类型，可能的返回值，1-正式实例，2-临时实例，3-只读实例，4-灾备实例
        :type InstanceType: int
        :param InstanceStatusDesc: 实例状态描述
        :type InstanceStatusDesc: str
        :param RealInstanceId: 实例对应的物理实例id，回档并替换过的实例有不同的InstanceId和RealInstanceId，从barad获取监控数据等场景下需要用物理id获取
        :type RealInstanceId: str
        :param MongosNodeNum: mongos节点个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MongosNodeNum: int
        :param MongosMemory: mongos节点内存。
注意：此字段可能返回 null，表示取不到有效值。
        :type MongosMemory: int
        :param MongosCpuNum: mongos节点CPU核数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MongosCpuNum: int
        :param ConfigServerNodeNum: Config Server节点个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigServerNodeNum: int
        :param ConfigServerMemory: Config Server节点内存。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigServerMemory: int
        :param ConfigServerVolume: Config Server节点磁盘大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigServerVolume: int
        :param ConfigServerCpuNum: Config Server节点CPU核数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigServerCpuNum: int
        :param ReadonlyNodeNum: readonly节点个数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadonlyNodeNum: int
        """
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
        self.MongosNodeNum = None
        self.MongosMemory = None
        self.MongosCpuNum = None
        self.ConfigServerNodeNum = None
        self.ConfigServerMemory = None
        self.ConfigServerVolume = None
        self.ConfigServerCpuNum = None
        self.ReadonlyNodeNum = None


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
        self.MongosNodeNum = params.get("MongosNodeNum")
        self.MongosMemory = params.get("MongosMemory")
        self.MongosCpuNum = params.get("MongosCpuNum")
        self.ConfigServerNodeNum = params.get("ConfigServerNodeNum")
        self.ConfigServerMemory = params.get("ConfigServerMemory")
        self.ConfigServerVolume = params.get("ConfigServerVolume")
        self.ConfigServerCpuNum = params.get("ConfigServerCpuNum")
        self.ReadonlyNodeNum = params.get("ReadonlyNodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    """实例可修改参数枚举类型集合。

    """

    def __init__(self):
        r"""
        :param CurrentValue: 参数当前值。
        :type CurrentValue: str
        :param DefaultValue: 参数默认值。
        :type DefaultValue: str
        :param EnumValue: 枚举值，所有支持的值。
        :type EnumValue: list of str
        :param NeedRestart: 参数修改之后是否需要重启生效。
- 1：需要重启后生效。
- 0：无需重启，设置成功即可生效。
        :type NeedRestart: str
        :param ParamName: 参数名称。
        :type ParamName: str
        :param Tips: 参数说明。
        :type Tips: list of str
        :param ValueType: 参数值类型说明。
        :type ValueType: str
        :param Status: 是否为运行中参数值。
- 1：运行中参数值。
- 0：非运行中参数值。
        :type Status: int
        """
        self.CurrentValue = None
        self.DefaultValue = None
        self.EnumValue = None
        self.NeedRestart = None
        self.ParamName = None
        self.Tips = None
        self.ValueType = None
        self.Status = None


    def _deserialize(self, params):
        self.CurrentValue = params.get("CurrentValue")
        self.DefaultValue = params.get("DefaultValue")
        self.EnumValue = params.get("EnumValue")
        self.NeedRestart = params.get("NeedRestart")
        self.ParamName = params.get("ParamName")
        self.Tips = params.get("Tips")
        self.ValueType = params.get("ValueType")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    """实例可修改参数 Integer 类型集合。

    """

    def __init__(self):
        r"""
        :param CurrentValue: 参数当前值。
        :type CurrentValue: str
        :param DefaultValue: 参数默认值。
        :type DefaultValue: str
        :param Max: 参数最大值。
        :type Max: str
        :param Min: 最小值。
        :type Min: str
        :param NeedRestart: 参数修改之后是否需要重启生效。
- 1:需要重启后生效。
- 0：无需重启，设置成功即可生效。
        :type NeedRestart: str
        :param ParamName: 参数名称。
        :type ParamName: str
        :param Tips: 参数说明。
        :type Tips: list of str
        :param ValueType: 参数类型。
        :type ValueType: str
        :param Status: 是否为运行中参数值。
- 1：运行中参数值。
- 0：非运行中参数值。
        :type Status: int
        :param Unit: 冗余字段，可忽略。
        :type Unit: str
        """
        self.CurrentValue = None
        self.DefaultValue = None
        self.Max = None
        self.Min = None
        self.NeedRestart = None
        self.ParamName = None
        self.Tips = None
        self.ValueType = None
        self.Status = None
        self.Unit = None


    def _deserialize(self, params):
        self.CurrentValue = params.get("CurrentValue")
        self.DefaultValue = params.get("DefaultValue")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.NeedRestart = params.get("NeedRestart")
        self.ParamName = params.get("ParamName")
        self.Tips = params.get("Tips")
        self.ValueType = params.get("ValueType")
        self.Status = params.get("Status")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMultiParam(AbstractModel):
    """实例可修改参数Multi类型集合。

    """

    def __init__(self):
        r"""
        :param CurrentValue: 参数当前值。
        :type CurrentValue: str
        :param DefaultValue: 参数默认值。
        :type DefaultValue: str
        :param EnumValue: 参考值范围。
        :type EnumValue: list of str
        :param NeedRestart: 参数修改后是否需要重启才会生效。
- 1：需要重启后生效。
- 0：无需重启，设置成功即可生效。
        :type NeedRestart: str
        :param ParamName: 参数名称。
        :type ParamName: str
        :param Status: 是否为运行中参数值。
- 1：运行中参数值。
- 0：非运行中参数值。
        :type Status: int
        :param Tips: 参数说明。
        :type Tips: list of str
        :param ValueType: 当前值的类型描述，默认为multi。
        :type ValueType: str
        """
        self.CurrentValue = None
        self.DefaultValue = None
        self.EnumValue = None
        self.NeedRestart = None
        self.ParamName = None
        self.Status = None
        self.Tips = None
        self.ValueType = None


    def _deserialize(self, params):
        self.CurrentValue = params.get("CurrentValue")
        self.DefaultValue = params.get("DefaultValue")
        self.EnumValue = params.get("EnumValue")
        self.NeedRestart = params.get("NeedRestart")
        self.ParamName = params.get("ParamName")
        self.Status = params.get("Status")
        self.Tips = params.get("Tips")
        self.ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTextParam(AbstractModel):
    """实例可修改参数为 Text 类型的参数集合。

    """

    def __init__(self):
        r"""
        :param CurrentValue: 参数当前值。
        :type CurrentValue: str
        :param DefaultValue: 参数默认值。
        :type DefaultValue: str
        :param NeedRestart: 修改参数值之后是否需要重启。
        :type NeedRestart: str
        :param ParamName: 参数名称。
        :type ParamName: str
        :param TextValue: Text 类型参数对应的值。
        :type TextValue: str
        :param Tips: 参数说明。
        :type Tips: list of str
        :param ValueType: 参数值类型说明。
        :type ValueType: str
        :param Status: 是否为运行中的参数值。
- 1：运行中参数值。
- 0：非运行中参数值。
        :type Status: str
        """
        self.CurrentValue = None
        self.DefaultValue = None
        self.NeedRestart = None
        self.ParamName = None
        self.TextValue = None
        self.Tips = None
        self.ValueType = None
        self.Status = None


    def _deserialize(self, params):
        self.CurrentValue = params.get("CurrentValue")
        self.DefaultValue = params.get("DefaultValue")
        self.NeedRestart = params.get("NeedRestart")
        self.ParamName = params.get("ParamName")
        self.TextValue = params.get("TextValue")
        self.Tips = params.get("Tips")
        self.ValueType = params.get("ValueType")
        self.Status = params.get("Status")
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
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
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
        


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class KillOpsRequest(AbstractModel):
    """KillOps请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param Operations: 待终止的操作
        :type Operations: list of Operation
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNetworkAddressRequest(AbstractModel):
    """ModifyDBInstanceNetworkAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param OldIpExpiredTime: 原IP保留时长，单位为分钟；原IP会在约定时间后释放，在释放前原IP和新IP均可访问；0表示立即回收原IP
        :type OldIpExpiredTime: int
        :param NewUniqVpcId: 切换后IP地址的归属私有网络统一ID，若为基础网络，该字段为空
        :type NewUniqVpcId: str
        :param NewUniqSubnetId: 切换后IP地址的归属子网统一ID，若为基础网络，该字段为空
        :type NewUniqSubnetId: str
        :param NetworkAddresses: 待修改IP信息
        :type NetworkAddresses: list of ModifyNetworkAddress
        """
        self.InstanceId = None
        self.OldIpExpiredTime = None
        self.NewUniqVpcId = None
        self.NewUniqSubnetId = None
        self.NetworkAddresses = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldIpExpiredTime = params.get("OldIpExpiredTime")
        self.NewUniqVpcId = params.get("NewUniqVpcId")
        self.NewUniqSubnetId = params.get("NewUniqSubnetId")
        if params.get("NetworkAddresses") is not None:
            self.NetworkAddresses = []
            for item in params.get("NetworkAddresses"):
                obj = ModifyNetworkAddress()
                obj._deserialize(item)
                self.NetworkAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceNetworkAddressResponse(AbstractModel):
    """ModifyDBInstanceNetworkAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID。例如：cmgo-7pje****。
        :type InstanceId: str
        :param SecurityGroupIds: 目标安全组 ID。请通过接口[DescribeSecurityGroup](https://cloud.tencent.com/document/product/240/55675)查看具体的安全组 ID。
        :type SecurityGroupIds: list of str
        """
        self.InstanceId = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param Memory: 实例配置变更后的内存大小，单位：GB。内存和磁盘必须同时升配或同时降配
        :type Memory: int
        :param Volume: 实例配置变更后的硬盘大小，单位：GB。内存和磁盘必须同时升配或同时降配。降配时，新的磁盘参数必须大于已用磁盘容量的1.2倍
        :type Volume: int
        :param OplogSize: 实例配置变更后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :type OplogSize: int
        :param NodeNum: 实例变更后的节点数，取值范围具体参照查询云数据库的售卖规格返回参数。默认为不变更节点数
        :type NodeNum: int
        :param ReplicateSetNum: 实例变更后的分片数，取值范围具体参照查询云数据库的售卖规格返回参数。只能增加不能减少，默认为不变更分片数
        :type ReplicateSetNum: int
        :param InMaintenance: 实例配置变更的切换时间，参数为：0(默认)、1。0-调整完成时，1-维护时间内。注：调整节点数和分片数不支持在【维护时间内】变更。
        :type InMaintenance: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.NodeNum = None
        self.ReplicateSetNum = None
        self.InMaintenance = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.NodeNum = params.get("NodeNum")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.InMaintenance = params.get("InMaintenance")
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
        r"""
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ModifyNetworkAddress(AbstractModel):
    """修改数据库地址

    """

    def __init__(self):
        r"""
        :param NewIPAddress: 新IP地址。
        :type NewIPAddress: str
        :param OldIpAddress: 原IP地址。
        :type OldIpAddress: str
        """
        self.NewIPAddress = None
        self.OldIpAddress = None


    def _deserialize(self, params):
        self.NewIPAddress = params.get("NewIPAddress")
        self.OldIpAddress = params.get("OldIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeProperty(AbstractModel):
    """节点属性

    """

    def __init__(self):
        r"""
        :param Zone: 节点所在的可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param NodeName: 节点名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param Address: 节点访问地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Role: 角色。
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param Hidden: 是否为Hidden节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Hidden: bool
        :param Status: 节点状态，包括：ORMAL/STARTUP/RECOVERING/STARTUP2/UNKNOWN/DOWN/ROLLBACK/REMOVED等。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param SlaveDelay: 主从延迟，单位秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveDelay: int
        :param Priority: 节点优先级。
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param Votes: 节点投票权。
注意：此字段可能返回 null，表示取不到有效值。
        :type Votes: int
        :param Tags: 节点标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of NodeTag
        :param ReplicateSetId: 副本集Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicateSetId: str
        """
        self.Zone = None
        self.NodeName = None
        self.Address = None
        self.Role = None
        self.Hidden = None
        self.Status = None
        self.SlaveDelay = None
        self.Priority = None
        self.Votes = None
        self.Tags = None
        self.ReplicateSetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeName = params.get("NodeName")
        self.Address = params.get("Address")
        self.Role = params.get("Role")
        self.Hidden = params.get("Hidden")
        self.Status = params.get("Status")
        self.SlaveDelay = params.get("SlaveDelay")
        self.Priority = params.get("Priority")
        self.Votes = params.get("Votes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = NodeTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ReplicateSetId = params.get("ReplicateSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeTag(AbstractModel):
    """节点Tag

    """

    def __init__(self):
        r"""
        :param TagKey: 节点Tag key
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 节点Tag Value
注意：此字段可能返回 null，表示取不到有效值。
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
        


class OfflineIsolatedDBInstanceRequest(AbstractModel):
    """OfflineIsolatedDBInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
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
        


class OfflineIsolatedDBInstanceResponse(AbstractModel):
    """OfflineIsolatedDBInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步任务的请求 ID，可使用此 ID 查询异步任务的执行结果。
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class Operation(AbstractModel):
    """需要终止的操作

    """

    def __init__(self):
        r"""
        :param ReplicaSetName: 操作所在的分片名
        :type ReplicaSetName: str
        :param NodeName: 操作所在的节点名
        :type NodeName: str
        :param OpId: 操作序号
        :type OpId: int
        """
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
        r"""
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同
        :type InstanceId: str
        :param NewName: 自定义实例名称，名称只支持长度为60个字符的中文、英文、数字、下划线_、分隔符 -
        :type NewName: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewDBInstancesRequest(AbstractModel):
    """RenewDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 一个或多个待操作的实例ID。可通过DescribeInstances接口返回值中的InstanceId获取。每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的续费时长、是否设置自动续费等属性。包年包月实例该参数为必传参数。
        :type InstanceChargePrepaid: :class:`tencentcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplicaSetInfo(AbstractModel):
    """分片信息

    """

    def __init__(self):
        r"""
        :param ReplicaSetId: 副本集ID
        :type ReplicaSetId: str
        """
        self.ReplicaSetId = None


    def _deserialize(self, params):
        self.ReplicaSetId = params.get("ReplicaSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicateSetInfo(AbstractModel):
    """副本集信息

    """

    def __init__(self):
        r"""
        :param Nodes: 节点属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Nodes: list of NodeProperty
        """
        self.Nodes = None


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = NodeProperty()
                obj._deserialize(item)
                self.Nodes.append(obj)
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
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param UserName: 实例账号名
        :type UserName: str
        :param Password: 新密码，新密码长度不能少于8位
        :type Password: str
        """
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
        r"""
        :param AsyncRequestId: 异步请求Id，用户查询该流程的运行状态
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组信息

    """

    def __init__(self):
        r"""
        :param ProjectId: 所属项目id
        :type ProjectId: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Inbound: 入站规则
        :type Inbound: list of SecurityGroupBound
        :param Outbound: 出站规则
        :type Outbound: list of SecurityGroupBound
        :param SecurityGroupId: 安全组id
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
        r"""
        :param Action: 执行规则。ACCEPT或DROP
        :type Action: str
        :param CidrIp: ip段。
        :type CidrIp: str
        :param PortRange: 端口范围
        :type PortRange: str
        :param IpProtocol: 传输层协议。tcp，udp或ALL
        :type IpProtocol: str
        :param Id: 安全组id代表的地址集合
        :type Id: str
        :param AddressModule: 地址组id代表的地址集合
        :type AddressModule: str
        :param ServiceModule: 服务组id代表的协议和端口集合
        :type ServiceModule: str
        :param Desc: 描述
        :type Desc: str
        """
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
        


class SetAccountUserPrivilegeRequest(AbstractModel):
    """SetAccountUserPrivilege请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 指定待设置账号的实例ID。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。
        :type InstanceId: str
        :param UserName: 设置账号名称。
        :type UserName: str
        :param AuthRole: 设置权限信息。
        :type AuthRole: list of Auth
        """
        self.InstanceId = None
        self.UserName = None
        self.AuthRole = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        if params.get("AuthRole") is not None:
            self.AuthRole = []
            for item in params.get("AuthRole"):
                obj = Auth()
                obj._deserialize(item)
                self.AuthRole.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAccountUserPrivilegeResponse(AbstractModel):
    """SetAccountUserPrivilege返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务ID。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ShardInfo(AbstractModel):
    """实例分片详情

    """

    def __init__(self):
        r"""
        :param UsedVolume: 分片已使用容量
        :type UsedVolume: float
        :param ReplicaSetId: 分片ID
        :type ReplicaSetId: str
        :param ReplicaSetName: 分片名
        :type ReplicaSetName: str
        :param Memory: 分片内存规格，单位为MB
        :type Memory: int
        :param Volume: 分片磁盘规格，单位为MB
        :type Volume: int
        :param OplogSize: 分片Oplog大小，单位为MB
        :type OplogSize: int
        :param SecondaryNum: 分片从节点数
        :type SecondaryNum: int
        :param RealReplicaSetId: 分片物理id
        :type RealReplicaSetId: str
        """
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
        r"""
        :param Pattern: 慢日志模式
        :type Pattern: str
        :param MaxTime: 最大执行时间
        :type MaxTime: int
        :param AverageTime: 平均执行时间
        :type AverageTime: int
        :param Total: 该模式慢日志条数
        :type Total: int
        """
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
        r"""
        :param SpecCode: 规格信息标识
        :type SpecCode: str
        :param Status: 规格有效标志，取值：0-停止售卖，1-开放售卖
        :type Status: int
        :param Cpu: 计算资源规格，单位为CPU核心数
        :type Cpu: int
        :param Memory: 内存规格，单位为MB
        :type Memory: int
        :param DefaultStorage: 默认磁盘规格，单位MB
        :type DefaultStorage: int
        :param MaxStorage: 最大磁盘规格，单位MB
        :type MaxStorage: int
        :param MinStorage: 最小磁盘规格，单位MB
        :type MinStorage: int
        :param Qps: 可承载qps信息
        :type Qps: int
        :param Conns: 连接数限制
        :type Conns: int
        :param MongoVersionCode: 实例mongodb版本信息
        :type MongoVersionCode: str
        :param MongoVersionValue: 实例mongodb版本号
        :type MongoVersionValue: int
        :param Version: 实例mongodb版本号（短）
        :type Version: str
        :param EngineName: 存储引擎
        :type EngineName: str
        :param ClusterType: 集群类型，取值：1-分片集群，0-副本集集群
        :type ClusterType: int
        :param MinNodeNum: 最小副本集从节点数
        :type MinNodeNum: int
        :param MaxNodeNum: 最大副本集从节点数
        :type MaxNodeNum: int
        :param MinReplicateSetNum: 最小分片数
        :type MinReplicateSetNum: int
        :param MaxReplicateSetNum: 最大分片数
        :type MaxReplicateSetNum: int
        :param MinReplicateSetNodeNum: 最小分片从节点数
        :type MinReplicateSetNodeNum: int
        :param MaxReplicateSetNodeNum: 最大分片从节点数
        :type MaxReplicateSetNodeNum: int
        :param MachineType: 机器类型，取值：0-HIO，4-HIO10G
        :type MachineType: str
        """
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
        r"""
        :param Region: 地域信息
        :type Region: str
        :param Zone: 可用区信息
        :type Zone: str
        :param SpecItems: 售卖规格信息
        :type SpecItems: list of SpecItem
        :param SupportMultiAZ: 是否支持跨可用区部署 1-支持，0-不支持
        :type SupportMultiAZ: int
        """
        self.Region = None
        self.Zone = None
        self.SpecItems = None
        self.SupportMultiAZ = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self.SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self.SpecItems.append(obj)
        self.SupportMultiAZ = params.get("SupportMultiAZ")
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
        


class TerminateDBInstancesRequest(AbstractModel):
    """TerminateDBInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 指定预隔离实例ID。格式如：cmgo-p8vnipr5。
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
        


class TerminateDBInstancesResponse(AbstractModel):
    """TerminateDBInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserInfo(AbstractModel):
    """账户基本信息

    """

    def __init__(self):
        r"""
        :param UserName: 账号名。
        :type UserName: str
        :param AuthRole: 账号权限详情。
        :type AuthRole: list of Auth
        :param CreateTime: 账号创建时间。
        :type CreateTime: str
        :param UpdateTime: 账号更新时间。
        :type UpdateTime: str
        :param UserDesc: 备注信息。
        :type UserDesc: str
        """
        self.UserName = None
        self.AuthRole = None
        self.CreateTime = None
        self.UpdateTime = None
        self.UserDesc = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        if params.get("AuthRole") is not None:
            self.AuthRole = []
            for item in params.get("AuthRole"):
                obj = Auth()
                obj._deserialize(item)
                self.AuthRole.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.UserDesc = params.get("UserDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        