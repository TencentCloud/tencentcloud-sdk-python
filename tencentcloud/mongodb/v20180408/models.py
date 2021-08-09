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
        


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param Memory: 实例内存大小，单位：GB\n        :type Memory: int\n        :param Volume: 实例硬盘大小，单位：GB\n        :type Volume: int\n        :param ReplicateSetNum: 副本集个数，1为单副本集实例，大于1为分片集群实例，最大不超过10\n        :type ReplicateSetNum: int\n        :param SecondaryNum: 每个副本集内从节点个数，目前只支持从节点数为2\n        :type SecondaryNum: int\n        :param EngineVersion: MongoDB引擎版本，值包括MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT\n        :type EngineVersion: str\n        :param Machine: 实例类型，GIO：高IO版；TGIO：高IO万兆\n        :type Machine: str\n        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为10\n        :type GoodsNum: int\n        :param Zone: 可用区信息，格式如：ap-guangzhou-2\n        :type Zone: str\n        :param InstanceRole: 实例角色，支持值包括：MASTER-表示主实例，DR-表示灾备实例，RO-表示只读实例\n        :type InstanceRole: str\n        :param InstanceType: 实例类型，REPLSET-副本集，SHARD-分片集群\n        :type InstanceType: str\n        :param Encrypt: 数据是否加密，当且仅当引擎版本为MONGO_3_ROCKS，可以选择加密\n        :type Encrypt: int\n        :param VpcId: 私有网络ID，如果不传则默认选择基础网络\n        :type VpcId: str\n        :param SubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填\n        :type SubnetId: str\n        :param ProjectId: 项目ID，不填为默认项目\n        :type ProjectId: int\n        :param SecurityGroup: 安全组参数\n        :type SecurityGroup: list of str\n        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.SecondaryNum = None
        self.EngineVersion = None
        self.Machine = None
        self.GoodsNum = None
        self.Zone = None
        self.InstanceRole = None
        self.InstanceType = None
        self.Encrypt = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.SecondaryNum = params.get("SecondaryNum")
        self.EngineVersion = params.get("EngineVersion")
        self.Machine = params.get("Machine")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.InstanceRole = params.get("InstanceRole")
        self.InstanceType = params.get("InstanceType")
        self.Encrypt = params.get("Encrypt")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
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
        :param SecondaryNum: 每个副本集内从节点个数\n        :type SecondaryNum: int\n        :param Memory: 实例内存大小，单位：GB\n        :type Memory: int\n        :param Volume: 实例硬盘大小，单位：GB\n        :type Volume: int\n        :param MongoVersion: 版本号，当前支持 MONGO_3_WT、MONGO_3_ROCKS、MONGO_36_WT\n        :type MongoVersion: str\n        :param MachineCode: 机器类型，GIO：高IO版；TGIO：高IO万兆\n        :type MachineCode: str\n        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为10\n        :type GoodsNum: int\n        :param Zone: 实例所属区域名称，格式如：ap-guangzhou-2\n        :type Zone: str\n        :param TimeSpan: 时长，购买月数\n        :type TimeSpan: int\n        :param Password: 实例密码\n        :type Password: str\n        :param ProjectId: 项目ID，不填为默认项目\n        :type ProjectId: int\n        :param SecurityGroup: 安全组参数\n        :type SecurityGroup: list of str\n        :param UniqVpcId: 私有网络ID，如果不传则默认选择基础网络\n        :type UniqVpcId: str\n        :param UniqSubnetId: 私有网络下的子网ID，如果设置了 VpcId，则 SubnetId必填\n        :type UniqSubnetId: str\n        """
        self.SecondaryNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.TimeSpan = None
        self.Password = None
        self.ProjectId = None
        self.SecurityGroup = None
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.SecondaryNum = params.get("SecondaryNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.TimeSpan = params.get("TimeSpan")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroup = params.get("SecurityGroup")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
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


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections请求参数结构体

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
        


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections返回参数结构体

    """

    def __init__(self):
        """
        :param Clients: 客户端连接信息，包括客户端IP和对应IP的连接数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Clients: list of ClientConnection\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Clients = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self.Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self.Clients.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceIds: list of str\n        :param InstanceType: 实例类型，取值范围：0-所有实例,1-正式实例，2-临时实例, 3-只读实例，-1-正式实例+只读+灾备实例\n        :type InstanceType: int\n        :param ClusterType: 集群类型，取值范围：0-副本集实例，1-分片实例，-1-所有实例\n        :type ClusterType: int\n        :param Status: 实例状态，取值范围：0-待初始化，1-流程执行中，2-实例有效，-2-实例已过期\n        :type Status: list of int\n        :param VpcId: 私有网络的ID，基础网络则不传该参数\n        :type VpcId: str\n        :param SubnetId: 私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId\n        :type SubnetId: str\n        :param PayMode: 付费类型，取值范围：0-按量计费，1-包年包月，-1-按量计费+包年包月\n        :type PayMode: int\n        :param Limit: 单次请求返回的数量，最小值为1，最大值为100，默认值为20\n        :type Limit: int\n        :param Offset: 偏移量，默认值为0\n        :type Offset: int\n        :param OrderBy: 返回结果集排序的字段，目前支持："ProjectId", "InstanceName", "CreateTime"，默认为升序排序\n        :type OrderBy: str\n        :param OrderByType: 返回结果集排序方式，目前支持："ASC"或者"DESC"\n        :type OrderByType: str\n        """
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
        :param TotalCount: 符合查询条件的实例总数\n        :type TotalCount: int\n        :param InstanceDetails: 实例详细信息\n        :type InstanceDetails: list of MongoDBInstanceDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = MongoDBInstanceDetail()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param StartTime: 慢日志起始时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。\n        :type StartTime: str\n        :param EndTime: 慢日志终止时间，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查询起止时间间隔不能超过24小时，只允许查询最近7天内慢日志。\n        :type EndTime: str\n        :param SlowMS: 慢日志执行时间阈值，返回执行时间超过该阈值的慢日志，单位为毫秒(ms)，最小为100毫秒。\n        :type SlowMS: int\n        :param Offset: 偏移量，最小值为0，最大值为10000，默认值为0。\n        :type Offset: int\n        :param Limit: 分页大小，最小值为1，最大值为100，默认值为20。\n        :type Limit: int\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    """DescribeSlowLog返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的慢查询日志总数。\n        :type TotalCount: int\n        :param SlowLogList: 符合查询条件的慢查询日志详情。\n        :type SlowLogList: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SlowLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.SlowLogList = params.get("SlowLogList")
        self.RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    """DescribeSpecInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 可用区\n        :type Zone: str\n        """
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


class MongoDBInstance(AbstractModel):
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
        


class MongoDBInstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param PayMode: 付费类型，可能的返回值：1-包年包月；0-按量计费\n        :type PayMode: int\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param ClusterType: 集群类型，可能的返回值：0-副本集实例，1-分片实例，\n        :type ClusterType: int\n        :param Region: 地域信息\n        :type Region: str\n        :param Zone: 可用区信息\n        :type Zone: str\n        :param NetType: 网络类型，可能的返回值：0-基础网络，1-私有网络\n        :type NetType: int\n        :param VpcId: 私有网络的ID\n        :type VpcId: str\n        :param SubnetId: 私有网络的子网ID\n        :type SubnetId: str\n        :param Status: 实例状态，可能的返回值：0-待初始化，1-流程处理中，2-运行中，-2-实例已过期\n        :type Status: int\n        :param Vip: 实例IP\n        :type Vip: str\n        :param Vport: 端口号\n        :type Vport: int\n        :param CreateTime: 实例创建时间\n        :type CreateTime: str\n        :param DeadLine: 实例到期时间\n        :type DeadLine: str\n        :param MongoVersion: 实例版本信息\n        :type MongoVersion: str\n        :param Memory: 实例内存规格，单位为MB\n        :type Memory: int\n        :param Volume: 实例磁盘规格，单位为MB\n        :type Volume: int\n        :param CpuNum: 实例CPU核心数\n        :type CpuNum: int\n        :param MachineType: 实例机器类型\n        :type MachineType: str\n        :param SecondaryNum: 实例从节点数\n        :type SecondaryNum: int\n        :param ReplicationSetNum: 实例分片数\n        :type ReplicationSetNum: int\n        :param AutoRenewFlag: 实例自动续费标志，可能的返回值：0-手动续费，1-自动续费，2-确认不续费\n        :type AutoRenewFlag: int\n        :param UsedVolume: 已用容量，单位MB\n        :type UsedVolume: int\n        :param MaintenanceStart: 维护窗口起始时间\n        :type MaintenanceStart: str\n        :param MaintenanceEnd: 维护窗口结束时间\n        :type MaintenanceEnd: str\n        :param ReplicaSets: 分片信息\n        :type ReplicaSets: list of MongodbShardInfo\n        :param ReadonlyInstances: 只读实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReadonlyInstances: list of MongoDBInstance\n        :param StandbyInstances: 灾备实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type StandbyInstances: list of MongoDBInstance\n        :param CloneInstances: 临时实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type CloneInstances: list of MongoDBInstance\n        :param RelatedInstance: 关联实例信息，对于正式实例，该字段表示它的临时实例信息；对于临时实例，则表示它的正式实例信息;如果为只读/灾备实例,则表示他的主实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelatedInstance: :class:`tencentcloud.mongodb.v20180408.models.MongoDBInstance`\n        :param Tags: 实例标签信息集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of TagInfo\n        :param InstanceVer: 实例标记\n        :type InstanceVer: int\n        :param ClusterVer: 实例标记\n        :type ClusterVer: int\n        :param Protocol: 协议信息，可能的返回值：1-mongodb，2-dynamodb\n        :type Protocol: int\n        :param InstanceType: 实例类型，可能的返回值，1-正式实例，2-临时实例，3-只读实例，4-灾备实例\n        :type InstanceType: int\n        :param InstanceStatusDesc: 实例状态描述\n        :type InstanceStatusDesc: str\n        :param RealInstanceId: 实例对应的物理实例ID，回档并替换过的实例有不同的InstanceId和RealInstanceId，从barad获取监控数据等场景下需要用物理id获取\n        :type RealInstanceId: str\n        """
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
                obj = MongodbShardInfo()
                obj._deserialize(item)
                self.ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self.ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self.ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self.StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self.StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self.CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = MongoDBInstance()
                obj._deserialize(item)
                self.CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self.RelatedInstance = MongoDBInstance()
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
        


class MongodbShardInfo(AbstractModel):
    """实例分片详情

    """

    def __init__(self):
        """
        :param UsedVolume: 分片已使用容量\n        :type UsedVolume: float\n        :param ReplicaSetId: 分片ID\n        :type ReplicaSetId: str\n        :param ReplicaSetName: 分片名\n        :type ReplicaSetName: str\n        :param Memory: 分片内存规格，单位为MB\n        :type Memory: int\n        :param Volume: 分片磁盘规格，单位为MB\n        :type Volume: int\n        :param OplogSize: 分片Oplog大小，单位为MB\n        :type OplogSize: int\n        :param SecondaryNum: 分片从节点数\n        :type SecondaryNum: int\n        :param RealReplicaSetId: 分片物理ID\n        :type RealReplicaSetId: str\n        """
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


class SetAutoRenewRequest(AbstractModel):
    """SetAutoRenew请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceIds: list of str\n        :param AutoRenewFlag: 续费选项，取值范围：0-手动续费，1-自动续费，2-确认不续费\n        :type AutoRenewFlag: int\n        """
        self.InstanceIds = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoRenewResponse(AbstractModel):
    """SetAutoRenew返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetPasswordRequest(AbstractModel):
    """SetPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param UserName: 实例账户名称\n        :type UserName: str\n        :param Password: 实例新密码，至少包含字母、数字和字符（!@#%^*()）中的两种，长度为8-16个字符\n        :type Password: str\n        """
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
        


class SetPasswordResponse(AbstractModel):
    """SetPassword返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 返回的异步任务ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SpecItem(AbstractModel):
    """mongodb售卖规格

    """

    def __init__(self):
        """
        :param SpecCode: 规格信息标识\n        :type SpecCode: str\n        :param Status: 规格有效标志，取值：0-停止售卖，1-开放售卖\n        :type Status: int\n        :param MachineType: 机器类型，取值：0-HIO，4-HIO10G\n        :type MachineType: str\n        :param Cpu: cpu核心数\n        :type Cpu: int\n        :param Memory: 内存规格，单位为MB\n        :type Memory: int\n        :param DefaultStorage: 默认磁盘规格，单位MB\n        :type DefaultStorage: int\n        :param MaxStorage: 最大磁盘规格，单位MB\n        :type MaxStorage: int\n        :param MinStorage: 最小磁盘规格，单位MB\n        :type MinStorage: int\n        :param Qps: 可承载qps信息\n        :type Qps: int\n        :param Conns: 连接数限制\n        :type Conns: int\n        :param MongoVersionCode: 实例mongodb版本信息\n        :type MongoVersionCode: str\n        :param MongoVersionValue: 实例mongodb版本号\n        :type MongoVersionValue: int\n        :param Version: 实例mongodb版本号（短）\n        :type Version: str\n        :param EngineName: 存储引擎\n        :type EngineName: str\n        :param ClusterType: 集群类型，取值：1-分片集群，0-副本集集群\n        :type ClusterType: int\n        :param MinNodeNum: 最小副本集从节点数\n        :type MinNodeNum: int\n        :param MaxNodeNum: 最大副本集从节点数\n        :type MaxNodeNum: int\n        :param MinReplicateSetNum: 最小分片数\n        :type MinReplicateSetNum: int\n        :param MaxReplicateSetNum: 最大分片数\n        :type MaxReplicateSetNum: int\n        :param MinReplicateSetNodeNum: 最小分片从节点数\n        :type MinReplicateSetNodeNum: int\n        :param MaxReplicateSetNodeNum: 最大分片从节点数\n        :type MaxReplicateSetNodeNum: int\n        """
        self.SpecCode = None
        self.Status = None
        self.MachineType = None
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


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Status = params.get("Status")
        self.MachineType = params.get("MachineType")
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
        :param TagKey: 标签Key值\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
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
        


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance请求参数结构体

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
        


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 订单ID，表示注销实例成功\n        :type AsyncRequestId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceHourRequest(AbstractModel):
    """UpgradeDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5\n        :type InstanceId: str\n        :param Memory: 升级后的内存大小，单位：GB\n        :type Memory: int\n        :param Volume: 升级后的硬盘大小，单位：GB\n        :type Volume: int\n        :param OplogSize: 升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%\n        :type OplogSize: int\n        """
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
        


class UpgradeDBInstanceHourResponse(AbstractModel):
    """UpgradeDBInstanceHour返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID\n        :type DealId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        :param Memory: 升级后的内存大小，单位：GB\n        :type Memory: int\n        :param Volume: 升级后的硬盘大小，单位：GB\n        :type Volume: int\n        :param OplogSize: 升级后oplog的大小，单位：GB，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%\n        :type OplogSize: int\n        """
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
        


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID\n        :type DealId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")