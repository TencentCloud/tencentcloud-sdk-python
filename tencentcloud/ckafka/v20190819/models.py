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


class Acl(AbstractModel):
    """ACL对象实体

    """

    def __init__(self):
        """
        :param ResourceType: Acl资源类型，（0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID）当前只有TOPIC，
        :type ResourceType: int
        :param ResourceName: 资源名称，和resourceType相关如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称
        :type ResourceName: str
        :param Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
注意：此字段可能返回 null，表示取不到有效值。
        :type Principal: str
        :param Host: 默认为*，表示任何host都可以访问，当前ckafka不支持host为*，但是后面开源kafka的产品化会直接支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param Operation: Acl操作方式(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)
        :type Operation: int
        :param PermissionType: 权限类型(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)
        :type PermissionType: int
        """
        self.ResourceType = None
        self.ResourceName = None
        self.Principal = None
        self.Host = None
        self.Operation = None
        self.PermissionType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Principal = params.get("Principal")
        self.Host = params.get("Host")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")


class AclResponse(AbstractModel):
    """ACL返回结果集

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的总数据条数
        :type TotalCount: int
        :param AclList: ACL列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AclList: list of Acl
        """
        self.TotalCount = None
        self.AclList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AclList") is not None:
            self.AclList = []
            for item in params.get("AclList"):
                obj = Acl()
                obj._deserialize(item)
                self.AclList.append(obj)


class AppIdResponse(AbstractModel):
    """AppId的查询结果

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的所有AppId数量
        :type TotalCount: int
        :param AppIdList: 符合要求的App Id列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AppIdList: list of int
        """
        self.TotalCount = None
        self.AppIdList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.AppIdList = params.get("AppIdList")


class Assignment(AbstractModel):
    """存储着分配给该消费者的 partition 信息

    """

    def __init__(self):
        """
        :param Version: assingment版本信息
        :type Version: int
        :param Topics: topic信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: list of GroupInfoTopics
        """
        self.Version = None
        self.Topics = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = GroupInfoTopics()
                obj._deserialize(item)
                self.Topics.append(obj)


class ClusterInfo(AbstractModel):
    """集群信息实体

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id
        :type ClusterId: int
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param MaxDiskSize: 集群最大磁盘 单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDiskSize: int
        :param MaxBandWidth: 集群最大带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxBandWidth: int
        :param AvailableDiskSize: 集群当前可用磁盘  单位GB
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableDiskSize: int
        :param AvailableBandWidth: 集群当前可用带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableBandWidth: int
        :param ZoneId: 集群所属可用区，表明集群归属的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param ZoneIds: 集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        """
        self.ClusterId = None
        self.ClusterName = None
        self.MaxDiskSize = None
        self.MaxBandWidth = None
        self.AvailableDiskSize = None
        self.AvailableBandWidth = None
        self.ZoneId = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.MaxBandWidth = params.get("MaxBandWidth")
        self.AvailableDiskSize = params.get("AvailableDiskSize")
        self.AvailableBandWidth = params.get("AvailableBandWidth")
        self.ZoneId = params.get("ZoneId")
        self.ZoneIds = params.get("ZoneIds")


class Config(AbstractModel):
    """高级配置对象

    """

    def __init__(self):
        """
        :param Retention: 消息保留时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Retention: int
        :param MinInsyncReplicas: 最小同步复制数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinInsyncReplicas: int
        :param CleanUpPolicy: 日志清理模式，默认 delete。
delete：日志按保存时间删除；compact：日志按 key 压缩；compact, delete：日志按 key 压缩且会保存时间删除。
注意：此字段可能返回 null，表示取不到有效值。
        :type CleanUpPolicy: str
        :param SegmentMs: Segment 分片滚动的时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentMs: int
        :param UncleanLeaderElectionEnable: 0表示 false。 1表示 true。
注意：此字段可能返回 null，表示取不到有效值。
        :type UncleanLeaderElectionEnable: int
        :param SegmentBytes: Segment 分片滚动的字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentBytes: int
        :param MaxMessageBytes: 最大消息字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMessageBytes: int
        """
        self.Retention = None
        self.MinInsyncReplicas = None
        self.CleanUpPolicy = None
        self.SegmentMs = None
        self.UncleanLeaderElectionEnable = None
        self.SegmentBytes = None
        self.MaxMessageBytes = None


    def _deserialize(self, params):
        self.Retention = params.get("Retention")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.SegmentMs = params.get("SegmentMs")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.SegmentBytes = params.get("SegmentBytes")
        self.MaxMessageBytes = params.get("MaxMessageBytes")


class ConsumerGroup(AbstractModel):
    """用户组实体

    """

    def __init__(self):
        """
        :param ConsumerGroupName: 用户组名称
        :type ConsumerGroupName: str
        :param SubscribedInfo: 订阅信息实体
        :type SubscribedInfo: list of SubscribedInfo
        """
        self.ConsumerGroupName = None
        self.SubscribedInfo = None


    def _deserialize(self, params):
        self.ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("SubscribedInfo") is not None:
            self.SubscribedInfo = []
            for item in params.get("SubscribedInfo"):
                obj = SubscribedInfo()
                obj._deserialize(item)
                self.SubscribedInfo.append(obj)


class ConsumerGroupResponse(AbstractModel):
    """消费组返回结果实体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的消费组数量
        :type TotalCount: int
        :param TopicList: 主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of ConsumerGroupTopic
        :param GroupList: 消费分组List
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of ConsumerGroup
        :param TotalPartition: 所有分区数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPartition: int
        :param PartitionListForMonitor: 监控的分区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionListForMonitor: list of Partition
        :param TotalTopic: 主题总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTopic: int
        :param TopicListForMonitor: 监控的主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param GroupListForMonitor: 监控的组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupListForMonitor: list of Group
        """
        self.TotalCount = None
        self.TopicList = None
        self.GroupList = None
        self.TotalPartition = None
        self.PartitionListForMonitor = None
        self.TotalTopic = None
        self.TopicListForMonitor = None
        self.GroupListForMonitor = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = ConsumerGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.TotalPartition = params.get("TotalPartition")
        if params.get("PartitionListForMonitor") is not None:
            self.PartitionListForMonitor = []
            for item in params.get("PartitionListForMonitor"):
                obj = Partition()
                obj._deserialize(item)
                self.PartitionListForMonitor.append(obj)
        self.TotalTopic = params.get("TotalTopic")
        if params.get("TopicListForMonitor") is not None:
            self.TopicListForMonitor = []
            for item in params.get("TopicListForMonitor"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicListForMonitor.append(obj)
        if params.get("GroupListForMonitor") is not None:
            self.GroupListForMonitor = []
            for item in params.get("GroupListForMonitor"):
                obj = Group()
                obj._deserialize(item)
                self.GroupListForMonitor.append(obj)


class ConsumerGroupTopic(AbstractModel):
    """消费组主题对象

    """

    def __init__(self):
        """
        :param TopicId: 主题ID
        :type TopicId: str
        :param TopicName: 主题名称
        :type TopicName: str
        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")


class CreateAclRequest(AbstractModel):
    """CreateAcl请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id信息
        :type InstanceId: str
        :param ResourceType: Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用
        :type ResourceType: int
        :param Operation: Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS)
        :type Operation: int
        :param PermissionType: 权限类型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :type PermissionType: int
        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称
        :type ResourceName: str
        :param Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :type Host: str
        :param Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入时需要加 User: 前缀,如用户A则传入User:A。
        :type Principal: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.Operation = None
        self.PermissionType = None
        self.ResourceName = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.ResourceName = params.get("ResourceName")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")


class CreateAclResponse(AbstractModel):
    """CreateAcl返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateInstancePreData(AbstractModel):
    """创建预付费接口返回的Data

    """

    def __init__(self):
        """
        :param FlowId: CreateInstancePre返回固定为0，不能作为CheckTaskStatus的查询条件。只是为了保证和后台数据结构对齐。
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param DealNames: 订单号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        """
        self.FlowId = None
        self.DealNames = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")


class CreateInstancePreRequest(AbstractModel):
    """CreateInstancePre请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param ZoneId: 可用区
        :type ZoneId: int
        :param Period: 预付费购买时长，例如 "1m",就是一个月
        :type Period: str
        :param InstanceType: 实例规格，1：入门型 ，2： 标准型，3 ：进阶型，4 ：容量型，5： 高阶型1，6：高阶性2, 7： 高阶型3,8： 高阶型4， 9 ：独占型。
        :type InstanceType: int
        :param VpcId: vpcId，不填默认基础网络
        :type VpcId: str
        :param SubnetId: 子网id，vpc网络需要传该参数，基础网络可以不传
        :type SubnetId: str
        :param MsgRetentionTime: 可选。实例日志的最长保留时间，单位分钟，默认为10080（7天），最大30天，不填默认0，代表不开启日志保留时间回收策略
        :type MsgRetentionTime: int
        :param ClusterId: 创建实例时可以选择集群Id, 该入参表示集群Id
        :type ClusterId: int
        :param RenewFlag: 预付费自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type RenewFlag: int
        """
        self.InstanceName = None
        self.ZoneId = None
        self.Period = None
        self.InstanceType = None
        self.VpcId = None
        self.SubnetId = None
        self.MsgRetentionTime = None
        self.ClusterId = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.ZoneId = params.get("ZoneId")
        self.Period = params.get("Period")
        self.InstanceType = params.get("InstanceType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        self.ClusterId = params.get("ClusterId")
        self.RenewFlag = params.get("RenewFlag")


class CreateInstancePreResponse(AbstractModel):
    """创建预付费实例返回结构

    """

    def __init__(self):
        """
        :param ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param ReturnMessage: 成功消息
        :type ReturnMessage: str
        :param Data: 操作型返回的Data数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`
        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = CreateInstancePreData()
            self.Data._deserialize(params.get("Data"))


class CreatePartitionRequest(AbstractModel):
    """CreatePartition请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param PartitionNum: 主题分区个数
        :type PartitionNum: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")


class CreatePartitionResponse(AbstractModel):
    """CreatePartition返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTopicIpWhiteListRequest(AbstractModel):
    """CreateTopicIpWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param IpWhiteList: ip白名单列表
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除主题IP白名单结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: 主题名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type TopicName: str
        :param PartitionNum: Partition个数，大于0
        :type PartitionNum: int
        :param ReplicaNum: 副本个数，不能多于 broker 数，最大为3
        :type ReplicaNum: int
        :param EnableWhiteList: ip白名单开关, 1:打开  0:关闭，默认不打开
        :type EnableWhiteList: int
        :param IpWhiteList: Ip白名单列表，配额限制，enableWhileList=1时必选
        :type IpWhiteList: list of str
        :param CleanUpPolicy: 清理日志策略，日志清理模式，默认为"delete"。"delete"：日志按保存时间删除，"compact"：日志按 key 压缩，"compact, delete"：日志按 key 压缩且会按保存时间删除。
        :type CleanUpPolicy: str
        :param Note: 主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type Note: str
        :param MinInsyncReplicas: 默认为1
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 是否允许未同步的副本选为leader，false:不允许，true:允许，默认不允许
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: 可消息选。保留时间，单位ms，当前最小值为60000ms
        :type RetentionMs: int
        :param SegmentMs: Segment分片滚动的时长，单位ms，当前最小为3600000ms
        :type SegmentMs: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.CleanUpPolicy = None
        self.Note = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.Note = params.get("Note")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")


class CreateTopicResp(AbstractModel):
    """创建主题返回

    """

    def __init__(self):
        """
        :param TopicId: 主题Id
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回创建结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateTopicResp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Name: 用户名称
        :type Name: str
        :param Password: 用户密码
        :type Password: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAclRequest(AbstractModel):
    """DeleteAcl请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id信息
        :type InstanceId: str
        :param ResourceType: Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用
        :type ResourceType: int
        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称
        :type ResourceName: str
        :param Operation: Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)，当前ckafka只支持READ,WRITE，其它用于后续兼容开源kafka的acl时使用
        :type Operation: int
        :param PermissionType: 权限类型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用
        :type PermissionType: int
        :param Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持
        :type Host: str
        :param Principal: 用户列表，默认为*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
        :type Principal: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Operation = None
        self.PermissionType = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")


class DeleteAclResponse(AbstractModel):
    """DeleteAcl返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAclRuleRequest(AbstractModel):
    """DeleteAclRule请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id信息
        :type InstanceId: str
        :param RuleName: acl规则名称
        :type RuleName: str
        """
        self.InstanceId = None
        self.RuleName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RuleName = params.get("RuleName")


class DeleteAclRuleResponse(AbstractModel):
    """DeleteAclRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回被删除的规则的ID
        :type Result: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteTopicIpWhiteListRequest(AbstractModel):
    """DeleteTopicIpWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        :param IpWhiteList: ip白名单列表
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除主题IP白名单结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: ckafka 实例Id
        :type InstanceId: str
        :param TopicName: ckafka 主题名称
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Name: 用户名称
        :type Name: str
        """
        self.InstanceId = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeACLRequest(AbstractModel):
    """DescribeACL请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param ResourceType: Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用
        :type ResourceType: int
        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称
        :type ResourceName: str
        :param Offset: 偏移位置
        :type Offset: int
        :param Limit: 个数限制
        :type Limit: int
        :param SearchWord: 关键字匹配
        :type SearchWord: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeACLResponse(AbstractModel):
    """DescribeACL返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的ACL结果集对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AclResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAppInfoRequest(AbstractModel):
    """DescribeAppInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移位置
        :type Offset: int
        :param Limit: 本次查询用户数目最大数量限制，最大值为50，默认50
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的符合要求的App Id列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AppIdResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeCkafkaZoneRequest(AbstractModel):
    """DescribeCkafkaZone请求参数结构体

    """


class DescribeCkafkaZoneResponse(AbstractModel):
    """DescribeCkafkaZone返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询结果复杂对象实体
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ZoneResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: ckafka实例id。
        :type InstanceId: str
        :param GroupName: 可选，用户需要查询的group名称。
        :type GroupName: str
        :param TopicName: 可选，用户需要查询的group中的对应的topic名称，如果指定了该参数，而group又未指定则忽略该参数。
        :type TopicName: str
        :param Limit: 本次返回个数限制
        :type Limit: int
        :param Offset: 偏移位置
        :type Offset: int
        """
        self.InstanceId = None
        self.GroupName = None
        self.TopicName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupName = params.get("GroupName")
        self.TopicName = params.get("TopicName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的消费分组信息
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConsumerGroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroup(AbstractModel):
    """DescribeGroup返回实体

    """

    def __init__(self):
        """
        :param Group: groupId
        :type Group: str
        :param Protocol: 该 group 使用的协议。
        :type Protocol: str
        """
        self.Group = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Group = params.get("Group")
        self.Protocol = params.get("Protocol")


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: （过滤条件）按照实例 ID 过滤。
        :type InstanceId: str
        :param GroupList: Kafka 消费分组，Consumer-group，这里是数组形式，格式：GroupList.0=xxx&GroupList.1=yyy。
        :type GroupList: list of str
        """
        self.InstanceId = None
        self.GroupList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupList = params.get("GroupList")


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of GroupInfoResponse
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupOffsetsRequest(AbstractModel):
    """DescribeGroupOffsets请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: （过滤条件）按照实例 ID 过滤
        :type InstanceId: str
        :param Group: Kafka 消费分组
        :type Group: str
        :param Topics: group 订阅的主题名称数组，如果没有该数组，则表示指定的 group 下所有 topic 信息
        :type Topics: list of str
        :param SearchWord: 模糊匹配 topicName
        :type SearchWord: str
        :param Offset: 本次查询的偏移位置，默认为0
        :type Offset: int
        :param Limit: 本次返回结果的最大个数，默认为50，最大值为50
        :type Limit: int
        """
        self.InstanceId = None
        self.Group = None
        self.Topics = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Topics = params.get("Topics")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupOffsetResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param SearchWord: 搜索关键字
        :type SearchWord: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 最大返回数量
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果集列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceAttributesRequest(AbstractModel):
    """DescribeInstanceAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 实例属性返回结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesDetailRequest(AbstractModel):
    """DescribeInstancesDetail请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: （过滤条件）按照实例ID过滤
        :type InstanceId: str
        :param SearchWord: （过滤条件）按照实例名称过滤，支持模糊查询
        :type SearchWord: str
        :param Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部
        :type Status: list of int
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认10，最大值20
        :type Limit: int
        :param TagKey: 匹配标签key值。
        :type TagKey: str
        :param Filters: 过滤器
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的实例详情结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: （过滤条件）按照实例ID过滤
        :type InstanceId: str
        :param SearchWord: （过滤条件）按照实例名称过滤，支持模糊查询
        :type SearchWord: str
        :param Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部
        :type Status: list of int
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认10，最大值100
        :type Limit: int
        :param TagKey: 匹配标签key值。
        :type TagKey: str
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRegionRequest(AbstractModel):
    """DescribeRegion请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回最大结果数
        :type Limit: int
        :param Business: 业务字段，可忽略
        :type Business: str
        """
        self.Offset = None
        self.Limit = None
        self.Business = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Business = params.get("Business")


class DescribeRegionResponse(AbstractModel):
    """DescribeRegion返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回地域枚举结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of Region
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Region()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteRequest(AbstractModel):
    """DescribeRoute请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例唯一id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeRouteResponse(AbstractModel):
    """DescribeRoute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的路由信息结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = RouteResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicAttributesRequest(AbstractModel):
    """DescribeTopicAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID
        :type InstanceId: str
        :param TopicName: 主题名称
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果对象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param SearchWord: （过滤条件）按照topicName过滤，支持模糊查询
        :type SearchWord: str
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认 10，最大值20，取值要大于0
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的主题详情实体
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    """DescribeTopic请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID
        :type InstanceId: str
        :param SearchWord: 过滤条件，按照 topicName 过滤，支持模糊查询
        :type SearchWord: str
        :param Offset: 偏移量，不填默认为0
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为50
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param SearchWord: 按照名称过滤
        :type SearchWord: str
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 本次返回个数
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeUserResponse(AbstractModel):
    """DescribeUser返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果列表
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UserResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DynamicRetentionTime(AbstractModel):
    """动态消息保留时间配置

    """

    def __init__(self):
        """
        :param Enable: 动态消息保留时间配置开关（0: 关闭，1: 开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: int
        :param DiskQuotaPercentage: 磁盘配额百分比触发条件，即消息达到此值触发消息保留时间变更事件
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskQuotaPercentage: int
        :param StepForwardPercentage: 每次向前调整消息保留时间百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type StepForwardPercentage: int
        :param BottomRetention: 保底时长，单位分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type BottomRetention: int
        """
        self.Enable = None
        self.DiskQuotaPercentage = None
        self.StepForwardPercentage = None
        self.BottomRetention = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self.StepForwardPercentage = params.get("StepForwardPercentage")
        self.BottomRetention = params.get("BottomRetention")


class Filter(AbstractModel):
    """查询过滤器
    >描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Group(AbstractModel):
    """组实体

    """

    def __init__(self):
        """
        :param GroupName: 组名称
        :type GroupName: str
        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")


class GroupInfoMember(AbstractModel):
    """consumer信息

    """

    def __init__(self):
        """
        :param MemberId: coordinator 为消费分组中的消费者生成的唯一 ID
        :type MemberId: str
        :param ClientId: 客户消费者 SDK 自己设置的 client.id 信息
        :type ClientId: str
        :param ClientHost: 一般存储客户的 IP 地址
        :type ClientHost: str
        :param Assignment: 存储着分配给该消费者的 partition 信息
        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        self.MemberId = None
        self.ClientId = None
        self.ClientHost = None
        self.Assignment = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.ClientId = params.get("ClientId")
        self.ClientHost = params.get("ClientHost")
        if params.get("Assignment") is not None:
            self.Assignment = Assignment()
            self.Assignment._deserialize(params.get("Assignment"))


class GroupInfoResponse(AbstractModel):
    """GroupInfo返回数据的实体

    """

    def __init__(self):
        """
        :param ErrorCode: 错误码，正常为0
        :type ErrorCode: str
        :param State: group 状态描述（常见的为 Empty、Stable、Dead 三种状态）：
Dead：消费分组不存在
Empty：消费分组，当前没有任何消费者订阅
PreparingRebalance：消费分组处于 rebalance 状态
CompletingRebalance：消费分组处于 rebalance 状态
Stable：消费分组中各个消费者已经加入，处于稳定状态
        :type State: str
        :param ProtocolType: 消费分组选择的协议类型正常的消费者一般为 consumer 但有些系统采用了自己的协议如 kafka-connect 用的就是 connect。只有标准的 consumer 协议，本接口才知道具体的分配方式的格式，才能解析到具体的 partition 的分配情况
        :type ProtocolType: str
        :param Protocol: 消费者 partition 分配算法常见的有如下几种(Kafka 消费者 SDK 默认的选择项为 range)：range、 roundrobin、 sticky
        :type Protocol: str
        :param Members: 仅当 state 为 Stable 且 protocol_type 为 consumer 时， 该数组才包含信息
        :type Members: list of GroupInfoMember
        :param Group: Kafka 消费分组
        :type Group: str
        """
        self.ErrorCode = None
        self.State = None
        self.ProtocolType = None
        self.Protocol = None
        self.Members = None
        self.Group = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.State = params.get("State")
        self.ProtocolType = params.get("ProtocolType")
        self.Protocol = params.get("Protocol")
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = GroupInfoMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.Group = params.get("Group")


class GroupInfoTopics(AbstractModel):
    """GroupInfo内部topic对象

    """

    def __init__(self):
        """
        :param Topic: 分配的 topic 名称
        :type Topic: str
        :param Partitions: 分配的 partition 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of int
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partitions = params.get("Partitions")


class GroupOffsetPartition(AbstractModel):
    """组偏移量分区对象

    """

    def __init__(self):
        """
        :param Partition: topic 的 partitionId
        :type Partition: int
        :param Offset: consumer 提交的 offset 位置
        :type Offset: int
        :param Metadata: 支持消费者提交消息时，传入 metadata 作为它用，当前一般为空字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: str
        :param ErrorCode: 错误码
        :type ErrorCode: int
        :param LogEndOffset: 当前 partition 最新的 offset
        :type LogEndOffset: int
        :param Lag: 未消费的消息个数
        :type Lag: int
        """
        self.Partition = None
        self.Offset = None
        self.Metadata = None
        self.ErrorCode = None
        self.LogEndOffset = None
        self.Lag = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        self.Metadata = params.get("Metadata")
        self.ErrorCode = params.get("ErrorCode")
        self.LogEndOffset = params.get("LogEndOffset")
        self.Lag = params.get("Lag")


class GroupOffsetResponse(AbstractModel):
    """消费组偏移量返回结果

    """

    def __init__(self):
        """
        :param TotalCount: 符合调节的总结果数
        :type TotalCount: int
        :param TopicList: 该主题分区数组，其中每个元素为一个 json object
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of GroupOffsetTopic
        """
        self.TotalCount = None
        self.TopicList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = GroupOffsetTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)


class GroupOffsetTopic(AbstractModel):
    """消费分组主题对象

    """

    def __init__(self):
        """
        :param Topic: 主题名称
        :type Topic: str
        :param Partitions: 该主题分区数组，其中每个元素为一个 json object
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: list of GroupOffsetPartition
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = GroupOffsetPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)


class GroupResponse(AbstractModel):
    """DescribeGroup的返回

    """

    def __init__(self):
        """
        :param TotalCount: 计数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param GroupList: GroupList
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of DescribeGroup
        """
        self.TotalCount = None
        self.GroupList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribeGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)


class Instance(AbstractModel):
    """实例对象

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中 ， 5 隔离中，-1 创建失败
        :type Status: int
        :param IfCommunity: 是否开源实例。开源：true，不开源：false
注意：此字段可能返回 null，表示取不到有效值。
        :type IfCommunity: bool
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.IfCommunity = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.IfCommunity = params.get("IfCommunity")


class InstanceAttributesResponse(AbstractModel):
    """实例属性返回结果对象

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param VipList: 接入点 VIP 列表信息
        :type VipList: list of VipEntity
        :param Vip: 虚拟IP
        :type Vip: str
        :param Vport: 虚拟端口
        :type Vport: str
        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中
        :type Status: int
        :param Bandwidth: 实例带宽，单位：Mbps
        :type Bandwidth: int
        :param DiskSize: 实例的存储大小，单位：GB
        :type DiskSize: int
        :param ZoneId: 可用区
        :type ZoneId: int
        :param VpcId: VPC 的 ID，为空表示是基础网络
        :type VpcId: str
        :param SubnetId: 子网 ID， 为空表示基础网络
        :type SubnetId: str
        :param Healthy: 实例健康状态， 1：健康，2：告警，3：异常
        :type Healthy: int
        :param HealthyMessage: 实例健康信息，当前会展示磁盘利用率，最大长度为256
        :type HealthyMessage: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param MsgRetentionTime: 消息保存时间,单位为分钟
        :type MsgRetentionTime: int
        :param Config: 自动创建 Topic 配置， 若该字段为空，则表示未开启自动创建
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        :param RemainderPartitions: 剩余创建分区数
        :type RemainderPartitions: int
        :param RemainderTopics: 剩余创建主题数
        :type RemainderTopics: int
        :param CreatedPartitions: 当前创建分区数
        :type CreatedPartitions: int
        :param CreatedTopics: 当前创建主题数
        :type CreatedTopics: int
        :param Tags: 标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param Version: kafka版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param MaxGroupNum: 最大分组数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxGroupNum: int
        :param Cvm: 售卖类型,0:标准版,1:专业版
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvm: int
        :param InstanceType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param Features: 表示该实例支持的特性。FEATURE_SUBNET_ACL:表示acl策略支持设置子网。
注意：此字段可能返回 null，表示取不到有效值。
        :type Features: list of str
        :param RetentionTimeConfig: 动态消息保留策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VipList = None
        self.Vip = None
        self.Vport = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.MsgRetentionTime = None
        self.Config = None
        self.RemainderPartitions = None
        self.RemainderTopics = None
        self.CreatedPartitions = None
        self.CreatedTopics = None
        self.Tags = None
        self.ExpireTime = None
        self.ZoneIds = None
        self.Version = None
        self.MaxGroupNum = None
        self.Cvm = None
        self.InstanceType = None
        self.Features = None
        self.RetentionTimeConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        if params.get("Config") is not None:
            self.Config = InstanceConfigDO()
            self.Config._deserialize(params.get("Config"))
        self.RemainderPartitions = params.get("RemainderPartitions")
        self.RemainderTopics = params.get("RemainderTopics")
        self.CreatedPartitions = params.get("CreatedPartitions")
        self.CreatedTopics = params.get("CreatedTopics")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ExpireTime = params.get("ExpireTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Version = params.get("Version")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.Cvm = params.get("Cvm")
        self.InstanceType = params.get("InstanceType")
        self.Features = params.get("Features")
        if params.get("RetentionTimeConfig") is not None:
            self.RetentionTimeConfig = DynamicRetentionTime()
            self.RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))


class InstanceConfigDO(AbstractModel):
    """实例配置实体

    """

    def __init__(self):
        """
        :param AutoCreateTopicsEnable: 是否自动创建主题
        :type AutoCreateTopicsEnable: bool
        :param DefaultNumPartitions: 分区数
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: 默认的复制Factor
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicsEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")


class InstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param Vip: 访问实例的vip 信息
        :type Vip: str
        :param Vport: 访问实例的端口信息
        :type Vport: str
        :param VipList: 虚拟IP列表
        :type VipList: list of VipEntity
        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中：5隔离中， -1 创建失败
        :type Status: int
        :param Bandwidth: 实例带宽，单位Mbps
        :type Bandwidth: int
        :param DiskSize: 实例的存储大小，单位GB
        :type DiskSize: int
        :param ZoneId: 可用区域ID
        :type ZoneId: int
        :param VpcId: vpcId，如果为空，说明是基础网络
        :type VpcId: str
        :param SubnetId: 子网id
        :type SubnetId: str
        :param RenewFlag: 实例是否续费，int  枚举值：1表示自动续费，2表示明确不自动续费
        :type RenewFlag: int
        :param Healthy: 实例状态 int：0表示健康，1表示告警，2 表示实例状态异常
        :type Healthy: int
        :param HealthyMessage: 实例状态信息
        :type HealthyMessage: str
        :param CreateTime: 实例创建时间时间
        :type CreateTime: int
        :param ExpireTime: 实例过期时间
        :type ExpireTime: int
        :param IsInternal: 是否为内部客户。值为1 表示内部客户
        :type IsInternal: int
        :param TopicNum: Topic个数
        :type TopicNum: int
        :param Tags: 标识tag
        :type Tags: list of Tag
        :param Version: kafka版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param Cvm: ckafka售卖类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Cvm: int
        :param InstanceType: ckafka实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param DiskType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param MaxTopicNumber: 当前规格最大Topic数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTopicNumber: int
        :param MaxPartitionNumber: 当前规格最大Partition数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPartitionNumber: int
        :param RebalanceTime: 计划升级配置时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RebalanceTime: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.VipList = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.RenewFlag = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.ExpireTime = None
        self.IsInternal = None
        self.TopicNum = None
        self.Tags = None
        self.Version = None
        self.ZoneIds = None
        self.Cvm = None
        self.InstanceType = None
        self.DiskType = None
        self.MaxTopicNumber = None
        self.MaxPartitionNumber = None
        self.RebalanceTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.RenewFlag = params.get("RenewFlag")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsInternal = params.get("IsInternal")
        self.TopicNum = params.get("TopicNum")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Version = params.get("Version")
        self.ZoneIds = params.get("ZoneIds")
        self.Cvm = params.get("Cvm")
        self.InstanceType = params.get("InstanceType")
        self.DiskType = params.get("DiskType")
        self.MaxTopicNumber = params.get("MaxTopicNumber")
        self.MaxPartitionNumber = params.get("MaxPartitionNumber")
        self.RebalanceTime = params.get("RebalanceTime")


class InstanceDetailResponse(AbstractModel):
    """实例详情返回结果

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例总数
        :type TotalCount: int
        :param InstanceList: 符合条件的实例详情列表
        :type InstanceList: list of InstanceDetail
        """
        self.TotalCount = None
        self.InstanceList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)


class InstanceResponse(AbstractModel):
    """聚合的实例状态返回结果

    """

    def __init__(self):
        """
        :param InstanceList: 符合条件的实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of Instance
        :param TotalCount: 符合条件的结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.InstanceList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")


class JgwOperateResponse(AbstractModel):
    """操作型结果返回值

    """

    def __init__(self):
        """
        :param ReturnCode: 返回的code，0为正常，非0为错误
        :type ReturnCode: str
        :param ReturnMessage: 成功消息
        :type ReturnMessage: str
        :param Data: 操作型返回的Data数据,可能有flowId等
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = OperateResponseData()
            self.Data._deserialize(params.get("Data"))


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: kafka实例id
        :type InstanceId: str
        :param Group: kafka 消费分组
        :type Group: str
        :param Strategy: 重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置
        :type Strategy: int
        :param Topics: 表示需要重置的topics， 不填表示全部
        :type Topics: list of str
        :param Shift: 当strategy为0时，必须包含该字段，可以大于零代表会把offset向后移动shift条，小于零则将offset向前回溯shift条数。正确重置后新的offset应该是(old_offset + shift)，需要注意的是如果新的offset小于partition的earliest则会设置为earliest，如果大于partition 的latest则会设置为latest
        :type Shift: int
        :param ShiftTimestamp: 单位ms。当strategy为1时，必须包含该字段，其中-2表示重置offset到最开始的位置，-1表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取topic中指定时间的offset然后进行重置，需要注意的时，如果指定的时间不存在消息，则获取最末尾的offset。
        :type ShiftTimestamp: int
        :param Offset: 需要重新设置的offset位置。当strategy为2，必须包含该字段。
        :type Offset: int
        :param Partitions: 需要重新设置的partition的列表，如果没有指定Topics参数。则重置全部topics的对应的Partition列表里的partition。指定Topics时则重置指定的topic列表的对应的Partitions列表的partition。
        :type Partitions: list of int
        """
        self.InstanceId = None
        self.Group = None
        self.Strategy = None
        self.Topics = None
        self.Shift = None
        self.ShiftTimestamp = None
        self.Offset = None
        self.Partitions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Strategy = params.get("Strategy")
        self.Topics = params.get("Topics")
        self.Shift = params.get("Shift")
        self.ShiftTimestamp = params.get("ShiftTimestamp")
        self.Offset = params.get("Offset")
        self.Partitions = params.get("Partitions")


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyInstanceAttributesConfig(AbstractModel):
    """修改实例属性的配置对象

    """

    def __init__(self):
        """
        :param AutoCreateTopicEnable: 自动创建 true 表示开启，false 表示不开启
        :type AutoCreateTopicEnable: bool
        :param DefaultNumPartitions: 可选，如果auto.create.topic.enable设置为true没有设置该值时，默认设置为3
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: 如歌auto.create.topic.enable设置为true没有指定该值时默认设置为2
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param MsgRetentionTime: 实例日志的最长保留时间，单位分钟，最大30天，0代表不开启日志保留时间回收策略
        :type MsgRetentionTime: int
        :param InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)
        :type InstanceName: str
        :param Config: 实例配置
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        :param DynamicRetentionConfig: 动态消息保留策略配置
        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param RebalanceTime: 修改升配置rebalance时间
        :type RebalanceTime: int
        """
        self.InstanceId = None
        self.MsgRetentionTime = None
        self.InstanceName = None
        self.Config = None
        self.DynamicRetentionConfig = None
        self.RebalanceTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        self.InstanceName = params.get("InstanceName")
        if params.get("Config") is not None:
            self.Config = ModifyInstanceAttributesConfig()
            self.Config._deserialize(params.get("Config"))
        if params.get("DynamicRetentionConfig") is not None:
            self.DynamicRetentionConfig = DynamicRetentionTime()
            self.DynamicRetentionConfig._deserialize(params.get("DynamicRetentionConfig"))
        self.RebalanceTime = params.get("RebalanceTime")


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Name: 用户名称
        :type Name: str
        :param Password: 用户当前密码
        :type Password: str
        :param PasswordNew: 用户新密码
        :type PasswordNew: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None
        self.PasswordNew = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.PasswordNew = params.get("PasswordNew")


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributesRequest(AbstractModel):
    """ModifyTopicAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID。
        :type InstanceId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param Note: 主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。
        :type Note: str
        :param EnableWhiteList: IP 白名单开关，1：打开；0：关闭。
        :type EnableWhiteList: int
        :param MinInsyncReplicas: 默认为1。
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 默认为 0，0：false；1：true。
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: 消息保留时间，单位：ms，当前最小值为60000ms。
        :type RetentionMs: int
        :param SegmentMs: Segment 分片滚动的时长，单位：ms，当前最小为86400000ms。
        :type SegmentMs: int
        :param MaxMessageBytes: 主题消息最大值，单位为 Byte，最大值为8388608Byte（即8MB）。
        :type MaxMessageBytes: int
        :param CleanUpPolicy: 消息删除策略，可以选择delete 或者compact
        :type CleanUpPolicy: str
        """
        self.InstanceId = None
        self.TopicName = None
        self.Note = None
        self.EnableWhiteList = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None
        self.MaxMessageBytes = None
        self.CleanUpPolicy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")
        self.MaxMessageBytes = params.get("MaxMessageBytes")
        self.CleanUpPolicy = params.get("CleanUpPolicy")


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class OperateResponseData(AbstractModel):
    """操作类型返回的Data结构

    """

    def __init__(self):
        """
        :param FlowId: FlowId
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class Partition(AbstractModel):
    """分区实体

    """

    def __init__(self):
        """
        :param PartitionId: 分区ID
        :type PartitionId: int
        """
        self.PartitionId = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")


class PartitionOffset(AbstractModel):
    """分区和位移

    """

    def __init__(self):
        """
        :param Partition: Partition,例如"0"或"1"
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: str
        :param Offset: Offset,例如100
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        """
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")


class Price(AbstractModel):
    """消息价格实体

    """

    def __init__(self):
        """
        :param RealTotalCost: 折扣价
        :type RealTotalCost: float
        :param TotalCost: 原价
        :type TotalCost: float
        """
        self.RealTotalCost = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.TotalCost = params.get("TotalCost")


class Region(AbstractModel):
    """地域实体对象

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: int
        :param RegionName: 地域名称
        :type RegionName: str
        :param AreaName: 区域名称
        :type AreaName: str
        :param RegionCode: 地域代码
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionCode: str
        :param RegionCodeV3: 地域代码（V3版本）
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionCodeV3: str
        :param Support: NONE:默认值不支持任何特殊机型\nCVM:支持CVM类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Support: str
        :param Ipv6: 是否支持ipv6, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: int
        :param MultiZone: 是否支持跨可用区, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiZone: int
        """
        self.RegionId = None
        self.RegionName = None
        self.AreaName = None
        self.RegionCode = None
        self.RegionCodeV3 = None
        self.Support = None
        self.Ipv6 = None
        self.MultiZone = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.AreaName = params.get("AreaName")
        self.RegionCode = params.get("RegionCode")
        self.RegionCodeV3 = params.get("RegionCodeV3")
        self.Support = params.get("Support")
        self.Ipv6 = params.get("Ipv6")
        self.MultiZone = params.get("MultiZone")


class Route(AbstractModel):
    """路由实体对象

    """

    def __init__(self):
        """
        :param AccessType: 实例接入方式
0：PLAINTEXT (明文方式，没有带用户信息老版本及社区版本都支持)
1：SASL_PLAINTEXT（明文方式，不过在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
2：SSL（SSL加密通信，没有带用户信息，老版本及社区版本都支持）
3：SASL_SSL（SSL加密通信，在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
        :type AccessType: int
        :param RouteId: 路由ID
        :type RouteId: int
        :param VipType: vip网络类型（1:外网TGW  2:基础网络 3:VPC网络 4:腾讯云支持环境(一般用于内部实例) 5:SSL外网访问方式访问 6:黑石环境vpc）
        :type VipType: int
        :param VipList: 虚拟IP列表
        :type VipList: list of VipEntity
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DomainPort: 域名port
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainPort: int
        """
        self.AccessType = None
        self.RouteId = None
        self.VipType = None
        self.VipList = None
        self.Domain = None
        self.DomainPort = None


    def _deserialize(self, params):
        self.AccessType = params.get("AccessType")
        self.RouteId = params.get("RouteId")
        self.VipType = params.get("VipType")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Domain = params.get("Domain")
        self.DomainPort = params.get("DomainPort")


class RouteResponse(AbstractModel):
    """路由信息返回对象

    """

    def __init__(self):
        """
        :param Routers: 路由信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Routers: list of Route
        """
        self.Routers = None


    def _deserialize(self, params):
        if params.get("Routers") is not None:
            self.Routers = []
            for item in params.get("Routers"):
                obj = Route()
                obj._deserialize(item)
                self.Routers.append(obj)


class SubscribedInfo(AbstractModel):
    """订阅信息实体

    """

    def __init__(self):
        """
        :param TopicName: 订阅的主题名
        :type TopicName: str
        :param Partition: 订阅的分区
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: list of int
        :param PartitionOffset: 分区offset信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionOffset: list of PartitionOffset
        :param TopicId: 订阅的主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        """
        self.TopicName = None
        self.Partition = None
        self.PartitionOffset = None
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Partition = params.get("Partition")
        if params.get("PartitionOffset") is not None:
            self.PartitionOffset = []
            for item in params.get("PartitionOffset"):
                obj = PartitionOffset()
                obj._deserialize(item)
                self.PartitionOffset.append(obj)
        self.TopicId = params.get("TopicId")


class Tag(AbstractModel):
    """实例详情中的标签对象

    """

    def __init__(self):
        """
        :param TagKey: 标签的key
        :type TagKey: str
        :param TagValue: 标签的值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class Topic(AbstractModel):
    """返回的topic对象

    """

    def __init__(self):
        """
        :param TopicId: 主题的ID
        :type TopicId: str
        :param TopicName: 主题的名称
        :type TopicName: str
        :param Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Note = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")


class TopicAttributesResponse(AbstractModel):
    """主题属性返回结果实体

    """

    def __init__(self):
        """
        :param TopicId: 主题 ID
        :type TopicId: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param Note: 主题备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param PartitionNum: 分区个数
        :type PartitionNum: int
        :param EnableWhiteList: IP 白名单开关，1：打开； 0：关闭
        :type EnableWhiteList: int
        :param IpWhiteList: IP 白名单列表
        :type IpWhiteList: list of str
        :param Config: topic 配置数组
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param Partitions: 分区详情
        :type Partitions: list of TopicPartitionDO
        """
        self.TopicId = None
        self.CreateTime = None
        self.Note = None
        self.PartitionNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.Config = None
        self.Partitions = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.Note = params.get("Note")
        self.PartitionNum = params.get("PartitionNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = TopicPartitionDO()
                obj._deserialize(item)
                self.Partitions.append(obj)


class TopicDetail(AbstractModel):
    """主题详情

    """

    def __init__(self):
        """
        :param TopicName: 主题名称
        :type TopicName: str
        :param TopicId: 主题ID
        :type TopicId: str
        :param PartitionNum: 分区数
        :type PartitionNum: int
        :param ReplicaNum: 副本数
        :type ReplicaNum: int
        :param Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param EnableWhiteList: 是否开启ip鉴权白名单，true表示开启，false表示不开启
        :type EnableWhiteList: bool
        :param IpWhiteListCount: ip白名单中ip个数
        :type IpWhiteListCount: int
        :param ForwardCosBucket: 数据备份cos bucket: 转存到cos 的bucket地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardCosBucket: str
        :param ForwardStatus: 数据备份cos 状态： 1 不开启数据备份，0 开启数据备份
        :type ForwardStatus: int
        :param ForwardInterval: 数据备份到cos的周期频率
        :type ForwardInterval: int
        :param Config: 高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param RetentionTimeConfig: 消息保留时间配置(用于动态配置变更记录)
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        """
        self.TopicName = None
        self.TopicId = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.Note = None
        self.CreateTime = None
        self.EnableWhiteList = None
        self.IpWhiteListCount = None
        self.ForwardCosBucket = None
        self.ForwardStatus = None
        self.ForwardInterval = None
        self.Config = None
        self.RetentionTimeConfig = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.Note = params.get("Note")
        self.CreateTime = params.get("CreateTime")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteListCount = params.get("IpWhiteListCount")
        self.ForwardCosBucket = params.get("ForwardCosBucket")
        self.ForwardStatus = params.get("ForwardStatus")
        self.ForwardInterval = params.get("ForwardInterval")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        if params.get("RetentionTimeConfig") is not None:
            self.RetentionTimeConfig = TopicRetentionTimeConfigRsp()
            self.RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))


class TopicDetailResponse(AbstractModel):
    """主题详情返回实体

    """

    def __init__(self):
        """
        :param TopicList: 返回的主题详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of TopicDetail
        :param TotalCount: 符合条件的所有主题详情数量
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = TopicDetail()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")


class TopicPartitionDO(AbstractModel):
    """分区详情

    """

    def __init__(self):
        """
        :param Partition: Partition ID
        :type Partition: int
        :param LeaderStatus: Leader 运行状态
        :type LeaderStatus: int
        :param IsrNum: ISR 个数
        :type IsrNum: int
        :param ReplicaNum: 副本个数
        :type ReplicaNum: int
        """
        self.Partition = None
        self.LeaderStatus = None
        self.IsrNum = None
        self.ReplicaNum = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.LeaderStatus = params.get("LeaderStatus")
        self.IsrNum = params.get("IsrNum")
        self.ReplicaNum = params.get("ReplicaNum")


class TopicResult(AbstractModel):
    """统一返回的TopicResponse

    """

    def __init__(self):
        """
        :param TopicList: 返回的主题信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of Topic
        :param TotalCount: 符合条件的 topic 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = Topic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")


class TopicRetentionTimeConfigRsp(AbstractModel):
    """Topic消息保留时间配置返回信息

    """

    def __init__(self):
        """
        :param Expect: 期望值，即用户配置的Topic消息保留时间(单位分钟)
注意：此字段可能返回 null，表示取不到有效值。
        :type Expect: int
        :param Current: 当前值，即当前生效值(可能存在动态调整，单位分钟)
注意：此字段可能返回 null，表示取不到有效值。
        :type Current: int
        :param ModTimeStamp: 最近变更时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModTimeStamp: int
        """
        self.Expect = None
        self.Current = None
        self.ModTimeStamp = None


    def _deserialize(self, params):
        self.Expect = params.get("Expect")
        self.Current = params.get("Current")
        self.ModTimeStamp = params.get("ModTimeStamp")


class User(AbstractModel):
    """用户实体

    """

    def __init__(self):
        """
        :param UserId: 用户id
        :type UserId: int
        :param Name: 用户名称
        :type Name: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 最后更新时间
        :type UpdateTime: str
        """
        self.UserId = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class UserResponse(AbstractModel):
    """用户返回实体

    """

    def __init__(self):
        """
        :param Users: 符合条件的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of User
        :param TotalCount: 符合条件的总用户数
        :type TotalCount: int
        """
        self.Users = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self.Users.append(obj)
        self.TotalCount = params.get("TotalCount")


class VipEntity(AbstractModel):
    """虚拟IP实体

    """

    def __init__(self):
        """
        :param Vip: 虚拟IP
        :type Vip: str
        :param Vport: 虚拟端口
        :type Vport: str
        """
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class ZoneInfo(AbstractModel):
    """zone信息实体

    """

    def __init__(self):
        """
        :param ZoneId: zone的id
        :type ZoneId: str
        :param IsInternalApp: 是否内部APP
        :type IsInternalApp: int
        :param AppId: app id
        :type AppId: int
        :param Flag: 标识
        :type Flag: bool
        :param ZoneName: zone名称
        :type ZoneName: str
        :param ZoneStatus: zone状态
        :type ZoneStatus: int
        :param Exflag: 额外标识
        :type Exflag: str
        :param SoldOut: json对象，key为机型，value true为售罄，false为未售罄
        :type SoldOut: str
        """
        self.ZoneId = None
        self.IsInternalApp = None
        self.AppId = None
        self.Flag = None
        self.ZoneName = None
        self.ZoneStatus = None
        self.Exflag = None
        self.SoldOut = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.IsInternalApp = params.get("IsInternalApp")
        self.AppId = params.get("AppId")
        self.Flag = params.get("Flag")
        self.ZoneName = params.get("ZoneName")
        self.ZoneStatus = params.get("ZoneStatus")
        self.Exflag = params.get("Exflag")
        self.SoldOut = params.get("SoldOut")


class ZoneResponse(AbstractModel):
    """查询kafka的zone信息返回的实体

    """

    def __init__(self):
        """
        :param ZoneList: zone列表
        :type ZoneList: list of ZoneInfo
        :param MaxBuyInstanceNum: 最大购买实例个数
        :type MaxBuyInstanceNum: int
        :param MaxBandwidth: 最大购买带宽 单位Mb/s
        :type MaxBandwidth: int
        :param UnitPrice: 后付费单位价格
        :type UnitPrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param MessagePrice: 后付费消息单价
        :type MessagePrice: :class:`tencentcloud.ckafka.v20190819.models.Price`
        :param ClusterInfo: 用户独占集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterInfo: list of ClusterInfo
        :param Standard: 购买标准版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        :param StandardS2: 购买标准版S2配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardS2: str
        :param Profession: 购买专业版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Profession: str
        :param Physical: 购买物理独占版配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Physical: str
        """
        self.ZoneList = None
        self.MaxBuyInstanceNum = None
        self.MaxBandwidth = None
        self.UnitPrice = None
        self.MessagePrice = None
        self.ClusterInfo = None
        self.Standard = None
        self.StandardS2 = None
        self.Profession = None
        self.Physical = None


    def _deserialize(self, params):
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        self.MaxBuyInstanceNum = params.get("MaxBuyInstanceNum")
        self.MaxBandwidth = params.get("MaxBandwidth")
        if params.get("UnitPrice") is not None:
            self.UnitPrice = Price()
            self.UnitPrice._deserialize(params.get("UnitPrice"))
        if params.get("MessagePrice") is not None:
            self.MessagePrice = Price()
            self.MessagePrice._deserialize(params.get("MessagePrice"))
        if params.get("ClusterInfo") is not None:
            self.ClusterInfo = []
            for item in params.get("ClusterInfo"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self.ClusterInfo.append(obj)
        self.Standard = params.get("Standard")
        self.StandardS2 = params.get("StandardS2")
        self.Profession = params.get("Profession")
        self.Physical = params.get("Physical")