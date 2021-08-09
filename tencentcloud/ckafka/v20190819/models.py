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


class Acl(AbstractModel):
    """ACL对象实体

    """

    def __init__(self):
        """
        :param ResourceType: Acl资源类型，（0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID）当前只有TOPIC，\n        :type ResourceType: int\n        :param ResourceName: 资源名称，和resourceType相关如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称\n        :type ResourceName: str\n        :param Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户
注意：此字段可能返回 null，表示取不到有效值。\n        :type Principal: str\n        :param Host: 默认为*，表示任何host都可以访问，当前ckafka不支持host为*，但是后面开源kafka的产品化会直接支持
注意：此字段可能返回 null，表示取不到有效值。\n        :type Host: str\n        :param Operation: Acl操作方式(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)\n        :type Operation: int\n        :param PermissionType: 权限类型(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)\n        :type PermissionType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclResponse(AbstractModel):
    """ACL返回结果集

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的总数据条数\n        :type TotalCount: int\n        :param AclList: ACL列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type AclList: list of Acl\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppIdResponse(AbstractModel):
    """AppId的查询结果

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的所有AppId数量\n        :type TotalCount: int\n        :param AppIdList: 符合要求的App Id列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppIdList: list of int\n        """
        self.TotalCount = None
        self.AppIdList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.AppIdList = params.get("AppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Assignment(AbstractModel):
    """存储着分配给该消费者的 partition 信息

    """

    def __init__(self):
        """
        :param Version: assingment版本信息\n        :type Version: int\n        :param Topics: topic信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Topics: list of GroupInfoTopics\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInfo(AbstractModel):
    """集群信息实体

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id\n        :type ClusterId: int\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param MaxDiskSize: 集群最大磁盘 单位GB
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxDiskSize: int\n        :param MaxBandWidth: 集群最大带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxBandWidth: int\n        :param AvailableDiskSize: 集群当前可用磁盘  单位GB
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvailableDiskSize: int\n        :param AvailableBandWidth: 集群当前可用带宽 单位MB/s
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvailableBandWidth: int\n        :param ZoneId: 集群所属可用区，表明集群归属的可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneId: int\n        :param ZoneIds: 集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneIds: list of int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """高级配置对象

    """

    def __init__(self):
        """
        :param Retention: 消息保留时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type Retention: int\n        :param MinInsyncReplicas: 最小同步复制数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinInsyncReplicas: int\n        :param CleanUpPolicy: 日志清理模式，默认 delete。
delete：日志按保存时间删除；compact：日志按 key 压缩；compact, delete：日志按 key 压缩且会保存时间删除。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CleanUpPolicy: str\n        :param SegmentMs: Segment 分片滚动的时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentMs: int\n        :param UncleanLeaderElectionEnable: 0表示 false。 1表示 true。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UncleanLeaderElectionEnable: int\n        :param SegmentBytes: Segment 分片滚动的字节数
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegmentBytes: int\n        :param MaxMessageBytes: 最大消息字节数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxMessageBytes: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroup(AbstractModel):
    """用户组实体

    """

    def __init__(self):
        """
        :param ConsumerGroupName: 用户组名称\n        :type ConsumerGroupName: str\n        :param SubscribedInfo: 订阅信息实体\n        :type SubscribedInfo: list of SubscribedInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupResponse(AbstractModel):
    """消费组返回结果实体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的消费组数量\n        :type TotalCount: int\n        :param TopicList: 主题列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicList: list of ConsumerGroupTopic\n        :param GroupList: 消费分组List
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupList: list of ConsumerGroup\n        :param TotalPartition: 所有分区数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalPartition: int\n        :param PartitionListForMonitor: 监控的分区列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PartitionListForMonitor: list of Partition\n        :param TotalTopic: 主题总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalTopic: int\n        :param TopicListForMonitor: 监控的主题列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicListForMonitor: list of ConsumerGroupTopic\n        :param GroupListForMonitor: 监控的组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupListForMonitor: list of Group\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupTopic(AbstractModel):
    """消费组主题对象

    """

    def __init__(self):
        """
        :param TopicId: 主题ID\n        :type TopicId: str\n        :param TopicName: 主题名称\n        :type TopicName: str\n        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerRecord(AbstractModel):
    """消息记录

    """

    def __init__(self):
        """
        :param Topic: 主题名\n        :type Topic: str\n        :param Partition: 分区id\n        :type Partition: int\n        :param Offset: 位点\n        :type Offset: int\n        :param Key: 消息key
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Value: 消息value
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param Timestamp: 消息时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type Timestamp: int\n        """
        self.Topic = None
        self.Partition = None
        self.Offset = None
        self.Key = None
        self.Value = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclRequest(AbstractModel):
    """CreateAcl请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id信息\n        :type InstanceId: str\n        :param ResourceType: Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用\n        :type ResourceType: int\n        :param Operation: Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS)\n        :type Operation: int\n        :param PermissionType: 权限类型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用\n        :type PermissionType: int\n        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称\n        :type ResourceName: str\n        :param Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持\n        :type Host: str\n        :param Principal: 用户列表，默认为User:*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户。传入时需要加 User: 前缀,如用户A则传入User:A。\n        :type Principal: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclResponse(AbstractModel):
    """CreateAcl返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowId: int\n        :param DealNames: 订单号列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type DealNames: list of str\n        :param InstanceId: 实例Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        """
        self.FlowId = None
        self.DealNames = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreRequest(AbstractModel):
    """CreateInstancePre请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)\n        :type InstanceName: str\n        :param ZoneId: 可用区\n        :type ZoneId: int\n        :param Period: 预付费购买时长，例如 "1m",就是一个月\n        :type Period: str\n        :param InstanceType: 实例规格，1：入门型 ，2： 标准型，3 ：进阶型，4 ：容量型，5： 高阶型1，6：高阶性2, 7： 高阶型3,8： 高阶型4， 9 ：独占型。\n        :type InstanceType: int\n        :param VpcId: vpcId，不填默认基础网络\n        :type VpcId: str\n        :param SubnetId: 子网id，vpc网络需要传该参数，基础网络可以不传\n        :type SubnetId: str\n        :param MsgRetentionTime: 可选。实例日志的最长保留时间，单位分钟，默认为10080（7天），最大30天，不填默认0，代表不开启日志保留时间回收策略\n        :type MsgRetentionTime: int\n        :param ClusterId: 创建实例时可以选择集群Id, 该入参表示集群Id\n        :type ClusterId: int\n        :param RenewFlag: 预付费自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)\n        :type RenewFlag: int\n        :param KafkaVersion: 支持指定版本Kafka版本（0.10.2/1.1.1/2.4.2） 。指定专业版参数specificationsType=pro\n        :type KafkaVersion: str\n        :param SpecificationsType: 专业版必须填写 （专业版：profession、标准版：standard） 默认是standard。专业版填profession\n        :type SpecificationsType: str\n        :param DiskSize: 磁盘大小,专业版不填写默认最小磁盘,填写后根据磁盘带宽分区数弹性计算\n        :type DiskSize: int\n        :param BandWidth: 带宽,专业版不填写默认最小带宽,填写后根据磁盘带宽分区数弹性计算\n        :type BandWidth: int\n        :param Partition: 分区大小,专业版不填写默认最小分区数,填写后根据磁盘带宽分区数弹性计算\n        :type Partition: int\n        :param Tags: 标签\n        :type Tags: list of Tag\n        :param DiskType: 磁盘类型（ssd填写CLOUD_SSD，sata填写CLOUD_BASIC）\n        :type DiskType: str\n        """
        self.InstanceName = None
        self.ZoneId = None
        self.Period = None
        self.InstanceType = None
        self.VpcId = None
        self.SubnetId = None
        self.MsgRetentionTime = None
        self.ClusterId = None
        self.RenewFlag = None
        self.KafkaVersion = None
        self.SpecificationsType = None
        self.DiskSize = None
        self.BandWidth = None
        self.Partition = None
        self.Tags = None
        self.DiskType = None


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
        self.KafkaVersion = params.get("KafkaVersion")
        self.SpecificationsType = params.get("SpecificationsType")
        self.DiskSize = params.get("DiskSize")
        self.BandWidth = params.get("BandWidth")
        self.Partition = params.get("Partition")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancePreResponse(AbstractModel):
    """创建预付费实例返回结构

    """

    def __init__(self):
        """
        :param ReturnCode: 返回的code，0为正常，非0为错误\n        :type ReturnCode: str\n        :param ReturnMessage: 成功消息\n        :type ReturnMessage: str\n        :param Data: 操作型返回的Data数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreData`\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param TopicName: 主题名称\n        :type TopicName: str\n        :param PartitionNum: 主题分区个数\n        :type PartitionNum: int\n        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePartitionResponse(AbstractModel):
    """CreatePartition返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果集\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param TopicName: 主题名称\n        :type TopicName: str\n        :param IpWhiteList: ip白名单列表\n        :type IpWhiteList: list of str\n        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除主题IP白名单结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param TopicName: 主题名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)\n        :type TopicName: str\n        :param PartitionNum: Partition个数，大于0\n        :type PartitionNum: int\n        :param ReplicaNum: 副本个数，不能多于 broker 数，最大为3\n        :type ReplicaNum: int\n        :param EnableWhiteList: ip白名单开关, 1:打开  0:关闭，默认不打开\n        :type EnableWhiteList: int\n        :param IpWhiteList: Ip白名单列表，配额限制，enableWhileList=1时必选\n        :type IpWhiteList: list of str\n        :param CleanUpPolicy: 清理日志策略，日志清理模式，默认为"delete"。"delete"：日志按保存时间删除，"compact"：日志按 key 压缩，"compact, delete"：日志按 key 压缩且会按保存时间删除。\n        :type CleanUpPolicy: str\n        :param Note: 主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)\n        :type Note: str\n        :param MinInsyncReplicas: 默认为1\n        :type MinInsyncReplicas: int\n        :param UncleanLeaderElectionEnable: 是否允许未同步的副本选为leader，false:不允许，true:允许，默认不允许\n        :type UncleanLeaderElectionEnable: int\n        :param RetentionMs: 可消息选。保留时间，单位ms，当前最小值为60000ms\n        :type RetentionMs: int\n        :param SegmentMs: Segment分片滚动的时长，单位ms，当前最小为3600000ms\n        :type SegmentMs: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResp(AbstractModel):
    """创建主题返回

    """

    def __init__(self):
        """
        :param TopicId: 主题Id\n        :type TopicId: str\n        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回创建结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Name: 用户名称\n        :type Name: str\n        :param Password: 用户密码\n        :type Password: str\n        """
        self.InstanceId = None
        self.Name = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例id信息\n        :type InstanceId: str\n        :param ResourceType: Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用\n        :type ResourceType: int\n        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称\n        :type ResourceName: str\n        :param Operation: Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)，当前ckafka只支持READ,WRITE，其它用于后续兼容开源kafka的acl时使用\n        :type Operation: int\n        :param PermissionType: 权限类型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用\n        :type PermissionType: int\n        :param Host: 默认为\*，表示任何host都可以访问，当前ckafka不支持host为\*，但是后面开源kafka的产品化会直接支持\n        :type Host: str\n        :param Principal: 用户列表，默认为*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户\n        :type Principal: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclResponse(AbstractModel):
    """DeleteAcl返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例id信息\n        :type InstanceId: str\n        :param RuleName: acl规则名称\n        :type RuleName: str\n        """
        self.InstanceId = None
        self.RuleName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclRuleResponse(AbstractModel):
    """DeleteAclRule返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回被删除的规则的ID\n        :type Result: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param TopicName: 主题名称\n        :type TopicName: str\n        :param IpWhiteList: ip白名单列表\n        :type IpWhiteList: list of str\n        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 删除主题IP白名单结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: ckafka 实例Id\n        :type InstanceId: str\n        :param TopicName: ckafka 主题名称\n        :type TopicName: str\n        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果集\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Name: 用户名称\n        :type Name: str\n        """
        self.InstanceId = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param ResourceType: Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用\n        :type ResourceType: int\n        :param ResourceName: 资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称\n        :type ResourceName: str\n        :param Offset: 偏移位置\n        :type Offset: int\n        :param Limit: 个数限制\n        :type Limit: int\n        :param SearchWord: 关键字匹配\n        :type SearchWord: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeACLResponse(AbstractModel):
    """DescribeACL返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的ACL结果集对象\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移位置\n        :type Offset: int\n        :param Limit: 本次查询用户数目最大数量限制，最大值为50，默认50\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的符合要求的App Id列表\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Result: 查询结果复杂对象实体\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: ckafka实例id。\n        :type InstanceId: str\n        :param GroupName: 可选，用户需要查询的group名称。\n        :type GroupName: str\n        :param TopicName: 可选，用户需要查询的group中的对应的topic名称，如果指定了该参数，而group又未指定则忽略该参数。\n        :type TopicName: str\n        :param Limit: 本次返回个数限制\n        :type Limit: int\n        :param Offset: 偏移位置\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的消费分组信息\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Group: groupId\n        :type Group: str\n        :param Protocol: 该 group 使用的协议。\n        :type Protocol: str\n        """
        self.Group = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Group = params.get("Group")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: （过滤条件）按照实例 ID 过滤。\n        :type InstanceId: str\n        :param GroupList: Kafka 消费分组，Consumer-group，这里是数组形式，格式：GroupList.0=xxx&GroupList.1=yyy。\n        :type GroupList: list of str\n        """
        self.InstanceId = None
        self.GroupList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupList = params.get("GroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: list of GroupInfoResponse\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: （过滤条件）按照实例 ID 过滤\n        :type InstanceId: str\n        :param Group: Kafka 消费分组\n        :type Group: str\n        :param Topics: group 订阅的主题名称数组，如果没有该数组，则表示指定的 group 下所有 topic 信息\n        :type Topics: list of str\n        :param SearchWord: 模糊匹配 topicName\n        :type SearchWord: str\n        :param Offset: 本次查询的偏移位置，默认为0\n        :type Offset: int\n        :param Limit: 本次返回结果的最大个数，默认为50，最大值为50\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果对象\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param SearchWord: 搜索关键字\n        :type SearchWord: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 最大返回数量\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果集列表\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例id\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 实例属性返回结果对象\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: （过滤条件）按照实例ID过滤\n        :type InstanceId: str\n        :param SearchWord: （过滤条件）按照实例名称过滤，支持模糊查询\n        :type SearchWord: str\n        :param Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部\n        :type Status: list of int\n        :param Offset: 偏移量，不填默认为0\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认10，最大值20\n        :type Limit: int\n        :param TagKey: 匹配标签key值。\n        :type TagKey: str\n        :param Filters: 过滤器\n        :type Filters: list of Filter\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的实例详情结果对象\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: （过滤条件）按照实例ID过滤\n        :type InstanceId: str\n        :param SearchWord: （过滤条件）按照实例名称过滤，支持模糊查询\n        :type SearchWord: str\n        :param Status: （过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部\n        :type Status: list of int\n        :param Offset: 偏移量，不填默认为0\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认10，最大值100\n        :type Limit: int\n        :param TagKey: 匹配标签key值。\n        :type TagKey: str\n        """
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
        :param Result: 返回的结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回最大结果数\n        :type Limit: int\n        :param Business: 业务字段，可忽略\n        :type Business: str\n        """
        self.Offset = None
        self.Limit = None
        self.Business = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionResponse(AbstractModel):
    """DescribeRegion返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回地域枚举结果列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: list of Region\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例唯一id\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteResponse(AbstractModel):
    """DescribeRoute返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的路由信息结果集\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例 ID\n        :type InstanceId: str\n        :param TopicName: 主题名称\n        :type TopicName: str\n        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果对象\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param SearchWord: （过滤条件）按照topicName过滤，支持模糊查询\n        :type SearchWord: str\n        :param Offset: 偏移量，不填默认为0\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认 10，最大值20，取值要大于0\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的主题详情实体\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例 ID\n        :type InstanceId: str\n        :param SearchWord: 过滤条件，按照 topicName 过滤，支持模糊查询\n        :type SearchWord: str\n        :param Offset: 偏移量，不填默认为0\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为50\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回的结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param SearchWord: 按照名称过滤\n        :type SearchWord: str\n        :param Offset: 偏移\n        :type Offset: int\n        :param Limit: 本次返回个数\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果列表\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Enable: int\n        :param DiskQuotaPercentage: 磁盘配额百分比触发条件，即消息达到此值触发消息保留时间变更事件
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskQuotaPercentage: int\n        :param StepForwardPercentage: 每次向前调整消息保留时间百分比
注意：此字段可能返回 null，表示取不到有效值。\n        :type StepForwardPercentage: int\n        :param BottomRetention: 保底时长，单位分钟
注意：此字段可能返回 null，表示取不到有效值。\n        :type BottomRetention: int\n        """
        self.Enable = None
        self.DiskQuotaPercentage = None
        self.StepForwardPercentage = None
        self.BottomRetention = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self.StepForwardPercentage = params.get("StepForwardPercentage")
        self.BottomRetention = params.get("BottomRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageByOffsetRequest(AbstractModel):
    """FetchMessageByOffset请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Topic: 主题名\n        :type Topic: str\n        :param Partition: 分区id\n        :type Partition: int\n        :param Offset: 位点信息\n        :type Offset: int\n        """
        self.InstanceId = None
        self.Topic = None
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Topic = params.get("Topic")
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FetchMessageByOffsetResponse(AbstractModel):
    """FetchMessageByOffset返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerRecord`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConsumerRecord()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询过滤器
    >描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段。\n        :type Name: str\n        :param Values: 字段的过滤值。\n        :type Values: list of str\n        """
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
        


class Group(AbstractModel):
    """组实体

    """

    def __init__(self):
        """
        :param GroupName: 组名称\n        :type GroupName: str\n        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoMember(AbstractModel):
    """consumer信息

    """

    def __init__(self):
        """
        :param MemberId: coordinator 为消费分组中的消费者生成的唯一 ID\n        :type MemberId: str\n        :param ClientId: 客户消费者 SDK 自己设置的 client.id 信息\n        :type ClientId: str\n        :param ClientHost: 一般存储客户的 IP 地址\n        :type ClientHost: str\n        :param Assignment: 存储着分配给该消费者的 partition 信息\n        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoResponse(AbstractModel):
    """GroupInfo返回数据的实体

    """

    def __init__(self):
        """
        :param ErrorCode: 错误码，正常为0\n        :type ErrorCode: str\n        :param State: group 状态描述（常见的为 Empty、Stable、Dead 三种状态）：
Dead：消费分组不存在
Empty：消费分组，当前没有任何消费者订阅
PreparingRebalance：消费分组处于 rebalance 状态
CompletingRebalance：消费分组处于 rebalance 状态
Stable：消费分组中各个消费者已经加入，处于稳定状态\n        :type State: str\n        :param ProtocolType: 消费分组选择的协议类型正常的消费者一般为 consumer 但有些系统采用了自己的协议如 kafka-connect 用的就是 connect。只有标准的 consumer 协议，本接口才知道具体的分配方式的格式，才能解析到具体的 partition 的分配情况\n        :type ProtocolType: str\n        :param Protocol: 消费者 partition 分配算法常见的有如下几种(Kafka 消费者 SDK 默认的选择项为 range)：range、 roundrobin、 sticky\n        :type Protocol: str\n        :param Members: 仅当 state 为 Stable 且 protocol_type 为 consumer 时， 该数组才包含信息\n        :type Members: list of GroupInfoMember\n        :param Group: Kafka 消费分组\n        :type Group: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoTopics(AbstractModel):
    """GroupInfo内部topic对象

    """

    def __init__(self):
        """
        :param Topic: 分配的 topic 名称\n        :type Topic: str\n        :param Partitions: 分配的 partition 信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partitions: list of int\n        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetPartition(AbstractModel):
    """组偏移量分区对象

    """

    def __init__(self):
        """
        :param Partition: topic 的 partitionId\n        :type Partition: int\n        :param Offset: consumer 提交的 offset 位置\n        :type Offset: int\n        :param Metadata: 支持消费者提交消息时，传入 metadata 作为它用，当前一般为空字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type Metadata: str\n        :param ErrorCode: 错误码\n        :type ErrorCode: int\n        :param LogEndOffset: 当前 partition 最新的 offset\n        :type LogEndOffset: int\n        :param Lag: 未消费的消息个数\n        :type Lag: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetResponse(AbstractModel):
    """消费组偏移量返回结果

    """

    def __init__(self):
        """
        :param TotalCount: 符合调节的总结果数\n        :type TotalCount: int\n        :param TopicList: 该主题分区数组，其中每个元素为一个 json object
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicList: list of GroupOffsetTopic\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetTopic(AbstractModel):
    """消费分组主题对象

    """

    def __init__(self):
        """
        :param Topic: 主题名称\n        :type Topic: str\n        :param Partitions: 该主题分区数组，其中每个元素为一个 json object
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partitions: list of GroupOffsetPartition\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupResponse(AbstractModel):
    """DescribeGroup的返回

    """

    def __init__(self):
        """
        :param TotalCount: 计数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param GroupList: GroupList
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupList: list of DescribeGroup\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """实例对象

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中 ， 5 隔离中，-1 创建失败\n        :type Status: int\n        :param IfCommunity: 是否开源实例。开源：true，不开源：false
注意：此字段可能返回 null，表示取不到有效值。\n        :type IfCommunity: bool\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.IfCommunity = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.IfCommunity = params.get("IfCommunity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAttributesResponse(AbstractModel):
    """实例属性返回结果对象

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param VipList: 接入点 VIP 列表信息\n        :type VipList: list of VipEntity\n        :param Vip: 虚拟IP\n        :type Vip: str\n        :param Vport: 虚拟端口\n        :type Vport: str\n        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中\n        :type Status: int\n        :param Bandwidth: 实例带宽，单位：Mbps\n        :type Bandwidth: int\n        :param DiskSize: 实例的存储大小，单位：GB\n        :type DiskSize: int\n        :param ZoneId: 可用区\n        :type ZoneId: int\n        :param VpcId: VPC 的 ID，为空表示是基础网络\n        :type VpcId: str\n        :param SubnetId: 子网 ID， 为空表示基础网络\n        :type SubnetId: str\n        :param Healthy: 实例健康状态， 1：健康，2：告警，3：异常\n        :type Healthy: int\n        :param HealthyMessage: 实例健康信息，当前会展示磁盘利用率，最大长度为256\n        :type HealthyMessage: str\n        :param CreateTime: 创建时间\n        :type CreateTime: int\n        :param MsgRetentionTime: 消息保存时间,单位为分钟\n        :type MsgRetentionTime: int\n        :param Config: 自动创建 Topic 配置， 若该字段为空，则表示未开启自动创建\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`\n        :param RemainderPartitions: 剩余创建分区数\n        :type RemainderPartitions: int\n        :param RemainderTopics: 剩余创建主题数\n        :type RemainderTopics: int\n        :param CreatedPartitions: 当前创建分区数\n        :type CreatedPartitions: int\n        :param CreatedTopics: 当前创建主题数\n        :type CreatedTopics: int\n        :param Tags: 标签数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: int\n        :param ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneIds: list of int\n        :param Version: kafka版本信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: str\n        :param MaxGroupNum: 最大分组数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxGroupNum: int\n        :param Cvm: 售卖类型,0:标准版,1:专业版
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cvm: int\n        :param InstanceType: 类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param Features: 表示该实例支持的特性。FEATURE_SUBNET_ACL:表示acl策略支持设置子网。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Features: list of str\n        :param RetentionTimeConfig: 动态消息保留策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigDO(AbstractModel):
    """实例配置实体

    """

    def __init__(self):
        """
        :param AutoCreateTopicsEnable: 是否自动创建主题\n        :type AutoCreateTopicsEnable: bool\n        :param DefaultNumPartitions: 分区数\n        :type DefaultNumPartitions: int\n        :param DefaultReplicationFactor: 默认的复制Factor\n        :type DefaultReplicationFactor: int\n        """
        self.AutoCreateTopicsEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")
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
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param Vip: 访问实例的vip 信息\n        :type Vip: str\n        :param Vport: 访问实例的端口信息\n        :type Vport: str\n        :param VipList: 虚拟IP列表\n        :type VipList: list of VipEntity\n        :param Status: 实例的状态。0：创建中，1：运行中，2：删除中：5隔离中， -1 创建失败\n        :type Status: int\n        :param Bandwidth: 实例带宽，单位Mbps\n        :type Bandwidth: int\n        :param DiskSize: 实例的存储大小，单位GB\n        :type DiskSize: int\n        :param ZoneId: 可用区域ID\n        :type ZoneId: int\n        :param VpcId: vpcId，如果为空，说明是基础网络\n        :type VpcId: str\n        :param SubnetId: 子网id\n        :type SubnetId: str\n        :param RenewFlag: 实例是否续费，int  枚举值：1表示自动续费，2表示明确不自动续费\n        :type RenewFlag: int\n        :param Healthy: 实例状态 int：0表示健康，1表示告警，2 表示实例状态异常\n        :type Healthy: int\n        :param HealthyMessage: 实例状态信息\n        :type HealthyMessage: str\n        :param CreateTime: 实例创建时间时间\n        :type CreateTime: int\n        :param ExpireTime: 实例过期时间\n        :type ExpireTime: int\n        :param IsInternal: 是否为内部客户。值为1 表示内部客户\n        :type IsInternal: int\n        :param TopicNum: Topic个数\n        :type TopicNum: int\n        :param Tags: 标识tag\n        :type Tags: list of Tag\n        :param Version: kafka版本信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: str\n        :param ZoneIds: 跨可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneIds: list of int\n        :param Cvm: ckafka售卖类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cvm: int\n        :param InstanceType: ckafka实例类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param DiskType: 磁盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskType: str\n        :param MaxTopicNumber: 当前规格最大Topic数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxTopicNumber: int\n        :param MaxPartitionNumber: 当前规格最大Partition数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxPartitionNumber: int\n        :param RebalanceTime: 计划升级配置时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type RebalanceTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetailResponse(AbstractModel):
    """实例详情返回结果

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例总数\n        :type TotalCount: int\n        :param InstanceList: 符合条件的实例详情列表\n        :type InstanceList: list of InstanceDetail\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceResponse(AbstractModel):
    """聚合的实例状态返回结果

    """

    def __init__(self):
        """
        :param InstanceList: 符合条件的实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceList: list of Instance\n        :param TotalCount: 符合条件的结果总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JgwOperateResponse(AbstractModel):
    """操作型结果返回值

    """

    def __init__(self):
        """
        :param ReturnCode: 返回的code，0为正常，非0为错误\n        :type ReturnCode: str\n        :param ReturnMessage: 成功消息\n        :type ReturnMessage: str\n        :param Data: 操作型返回的Data数据,可能有flowId等
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`\n        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = OperateResponseData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: kafka实例id\n        :type InstanceId: str\n        :param Group: kafka 消费分组\n        :type Group: str\n        :param Strategy: 重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置\n        :type Strategy: int\n        :param Topics: 表示需要重置的topics， 不填表示全部\n        :type Topics: list of str\n        :param Shift: 当strategy为0时，必须包含该字段，可以大于零代表会把offset向后移动shift条，小于零则将offset向前回溯shift条数。正确重置后新的offset应该是(old_offset + shift)，需要注意的是如果新的offset小于partition的earliest则会设置为earliest，如果大于partition 的latest则会设置为latest\n        :type Shift: int\n        :param ShiftTimestamp: 单位ms。当strategy为1时，必须包含该字段，其中-2表示重置offset到最开始的位置，-1表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取topic中指定时间的offset然后进行重置，需要注意的时，如果指定的时间不存在消息，则获取最末尾的offset。\n        :type ShiftTimestamp: int\n        :param Offset: 需要重新设置的offset位置。当strategy为2，必须包含该字段。\n        :type Offset: int\n        :param Partitions: 需要重新设置的partition的列表，如果没有指定Topics参数。则重置全部topics的对应的Partition列表里的partition。指定Topics时则重置指定的topic列表的对应的Partitions列表的partition。\n        :type Partitions: list of int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AutoCreateTopicEnable: 自动创建 true 表示开启，false 表示不开启\n        :type AutoCreateTopicEnable: bool\n        :param DefaultNumPartitions: 可选，如果auto.create.topic.enable设置为true没有设置该值时，默认设置为3\n        :type DefaultNumPartitions: int\n        :param DefaultReplicationFactor: 如歌auto.create.topic.enable设置为true没有指定该值时默认设置为2\n        :type DefaultReplicationFactor: int\n        """
        self.AutoCreateTopicEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param MsgRetentionTime: 实例日志的最长保留时间，单位分钟，最大30天，0代表不开启日志保留时间回收策略\n        :type MsgRetentionTime: int\n        :param InstanceName: 实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)\n        :type InstanceName: str\n        :param Config: 实例配置\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`\n        :param DynamicRetentionConfig: 动态消息保留策略配置\n        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`\n        :param RebalanceTime: 修改升配置rebalance时间\n        :type RebalanceTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Name: 用户名称\n        :type Name: str\n        :param Password: 用户当前密码\n        :type Password: str\n        :param PasswordNew: 用户新密码\n        :type PasswordNew: str\n        """
        self.InstanceId = None
        self.Name = None
        self.Password = None
        self.PasswordNew = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.PasswordNew = params.get("PasswordNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param InstanceId: 实例 ID。\n        :type InstanceId: str\n        :param TopicName: 主题名称。\n        :type TopicName: str\n        :param Note: 主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。\n        :type Note: str\n        :param EnableWhiteList: IP 白名单开关，1：打开；0：关闭。\n        :type EnableWhiteList: int\n        :param MinInsyncReplicas: 默认为1。\n        :type MinInsyncReplicas: int\n        :param UncleanLeaderElectionEnable: 默认为 0，0：false；1：true。\n        :type UncleanLeaderElectionEnable: int\n        :param RetentionMs: 消息保留时间，单位：ms，当前最小值为60000ms。\n        :type RetentionMs: int\n        :param SegmentMs: Segment 分片滚动的时长，单位：ms，当前最小为86400000ms。\n        :type SegmentMs: int\n        :param MaxMessageBytes: 主题消息最大值，单位为 Byte，最大值为8388608Byte（即8MB）。\n        :type MaxMessageBytes: int\n        :param CleanUpPolicy: 消息删除策略，可以选择delete 或者compact\n        :type CleanUpPolicy: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果集\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type FlowId: int\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partition(AbstractModel):
    """分区实体

    """

    def __init__(self):
        """
        :param PartitionId: 分区ID\n        :type PartitionId: int\n        """
        self.PartitionId = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionOffset(AbstractModel):
    """分区和位移

    """

    def __init__(self):
        """
        :param Partition: Partition,例如"0"或"1"
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partition: str\n        :param Offset: Offset,例如100
注意：此字段可能返回 null，表示取不到有效值。\n        :type Offset: int\n        """
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """消息价格实体

    """

    def __init__(self):
        """
        :param RealTotalCost: 折扣价\n        :type RealTotalCost: float\n        :param TotalCost: 原价\n        :type TotalCost: float\n        """
        self.RealTotalCost = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """地域实体对象

    """

    def __init__(self):
        """
        :param RegionId: 地域ID\n        :type RegionId: int\n        :param RegionName: 地域名称\n        :type RegionName: str\n        :param AreaName: 区域名称\n        :type AreaName: str\n        :param RegionCode: 地域代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionCode: str\n        :param RegionCodeV3: 地域代码（V3版本）
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionCodeV3: str\n        :param Support: NONE:默认值不支持任何特殊机型\nCVM:支持CVM类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Support: str\n        :param Ipv6: 是否支持ipv6, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6: int\n        :param MultiZone: 是否支持跨可用区, 0：表示不支持，1：表示支持
注意：此字段可能返回 null，表示取不到有效值。\n        :type MultiZone: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Route(AbstractModel):
    """路由实体对象

    """

    def __init__(self):
        """
        :param AccessType: 实例接入方式
0：PLAINTEXT (明文方式，没有带用户信息老版本及社区版本都支持)
1：SASL_PLAINTEXT（明文方式，不过在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）
2：SSL（SSL加密通信，没有带用户信息，老版本及社区版本都支持）
3：SASL_SSL（SSL加密通信，在数据开始时，会通过SASL方式登录鉴权，仅社区版本支持）\n        :type AccessType: int\n        :param RouteId: 路由ID\n        :type RouteId: int\n        :param VipType: vip网络类型（1:外网TGW  2:基础网络 3:VPC网络 4:腾讯云支持环境(一般用于内部实例) 5:SSL外网访问方式访问 6:黑石环境vpc）\n        :type VipType: int\n        :param VipList: 虚拟IP列表\n        :type VipList: list of VipEntity\n        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param DomainPort: 域名port
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainPort: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteResponse(AbstractModel):
    """路由信息返回对象

    """

    def __init__(self):
        """
        :param Routers: 路由信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Routers: list of Route\n        """
        self.Routers = None


    def _deserialize(self, params):
        if params.get("Routers") is not None:
            self.Routers = []
            for item in params.get("Routers"):
                obj = Route()
                obj._deserialize(item)
                self.Routers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribedInfo(AbstractModel):
    """订阅信息实体

    """

    def __init__(self):
        """
        :param TopicName: 订阅的主题名\n        :type TopicName: str\n        :param Partition: 订阅的分区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partition: list of int\n        :param PartitionOffset: 分区offset信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PartitionOffset: list of PartitionOffset\n        :param TopicId: 订阅的主题ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """实例详情中的标签对象

    """

    def __init__(self):
        """
        :param TagKey: 标签的key\n        :type TagKey: str\n        :param TagValue: 标签的值\n        :type TagValue: str\n        """
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
        


class Topic(AbstractModel):
    """返回的topic对象

    """

    def __init__(self):
        """
        :param TopicId: 主题的ID\n        :type TopicId: str\n        :param TopicName: 主题的名称\n        :type TopicName: str\n        :param Note: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Note: str\n        """
        self.TopicId = None
        self.TopicName = None
        self.Note = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicAttributesResponse(AbstractModel):
    """主题属性返回结果实体

    """

    def __init__(self):
        """
        :param TopicId: 主题 ID\n        :type TopicId: str\n        :param CreateTime: 创建时间\n        :type CreateTime: int\n        :param Note: 主题备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Note: str\n        :param PartitionNum: 分区个数\n        :type PartitionNum: int\n        :param EnableWhiteList: IP 白名单开关，1：打开； 0：关闭\n        :type EnableWhiteList: int\n        :param IpWhiteList: IP 白名单列表\n        :type IpWhiteList: list of str\n        :param Config: topic 配置数组\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`\n        :param Partitions: 分区详情\n        :type Partitions: list of TopicPartitionDO\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetail(AbstractModel):
    """主题详情

    """

    def __init__(self):
        """
        :param TopicName: 主题名称\n        :type TopicName: str\n        :param TopicId: 主题ID\n        :type TopicId: str\n        :param PartitionNum: 分区数\n        :type PartitionNum: int\n        :param ReplicaNum: 副本数\n        :type ReplicaNum: int\n        :param Note: 备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Note: str\n        :param CreateTime: 创建时间\n        :type CreateTime: int\n        :param EnableWhiteList: 是否开启ip鉴权白名单，true表示开启，false表示不开启\n        :type EnableWhiteList: bool\n        :param IpWhiteListCount: ip白名单中ip个数\n        :type IpWhiteListCount: int\n        :param ForwardCosBucket: 数据备份cos bucket: 转存到cos 的bucket地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForwardCosBucket: str\n        :param ForwardStatus: 数据备份cos 状态： 1 不开启数据备份，0 开启数据备份\n        :type ForwardStatus: int\n        :param ForwardInterval: 数据备份到cos的周期频率\n        :type ForwardInterval: int\n        :param Config: 高级配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`\n        :param RetentionTimeConfig: 消息保留时间配置(用于动态配置变更记录)
注意：此字段可能返回 null，表示取不到有效值。\n        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetailResponse(AbstractModel):
    """主题详情返回实体

    """

    def __init__(self):
        """
        :param TopicList: 返回的主题详情列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicList: list of TopicDetail\n        :param TotalCount: 符合条件的所有主题详情数量\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicPartitionDO(AbstractModel):
    """分区详情

    """

    def __init__(self):
        """
        :param Partition: Partition ID\n        :type Partition: int\n        :param LeaderStatus: Leader 运行状态\n        :type LeaderStatus: int\n        :param IsrNum: ISR 个数\n        :type IsrNum: int\n        :param ReplicaNum: 副本个数\n        :type ReplicaNum: int\n        """
        self.Partition = None
        self.LeaderStatus = None
        self.IsrNum = None
        self.ReplicaNum = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.LeaderStatus = params.get("LeaderStatus")
        self.IsrNum = params.get("IsrNum")
        self.ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicResult(AbstractModel):
    """统一返回的TopicResponse

    """

    def __init__(self):
        """
        :param TopicList: 返回的主题信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicList: list of Topic\n        :param TotalCount: 符合条件的 topic 数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRetentionTimeConfigRsp(AbstractModel):
    """Topic消息保留时间配置返回信息

    """

    def __init__(self):
        """
        :param Expect: 期望值，即用户配置的Topic消息保留时间(单位分钟)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Expect: int\n        :param Current: 当前值，即当前生效值(可能存在动态调整，单位分钟)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Current: int\n        :param ModTimeStamp: 最近变更时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModTimeStamp: int\n        """
        self.Expect = None
        self.Current = None
        self.ModTimeStamp = None


    def _deserialize(self, params):
        self.Expect = params.get("Expect")
        self.Current = params.get("Current")
        self.ModTimeStamp = params.get("ModTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户实体

    """

    def __init__(self):
        """
        :param UserId: 用户id\n        :type UserId: int\n        :param Name: 用户名称\n        :type Name: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 最后更新时间\n        :type UpdateTime: str\n        """
        self.UserId = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserResponse(AbstractModel):
    """用户返回实体

    """

    def __init__(self):
        """
        :param Users: 符合条件的用户列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Users: list of User\n        :param TotalCount: 符合条件的总用户数\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VipEntity(AbstractModel):
    """虚拟IP实体

    """

    def __init__(self):
        """
        :param Vip: 虚拟IP\n        :type Vip: str\n        :param Vport: 虚拟端口\n        :type Vport: str\n        """
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """zone信息实体

    """

    def __init__(self):
        """
        :param ZoneId: zone的id\n        :type ZoneId: str\n        :param IsInternalApp: 是否内部APP\n        :type IsInternalApp: int\n        :param AppId: app id\n        :type AppId: int\n        :param Flag: 标识\n        :type Flag: bool\n        :param ZoneName: zone名称\n        :type ZoneName: str\n        :param ZoneStatus: zone状态\n        :type ZoneStatus: int\n        :param Exflag: 额外标识\n        :type Exflag: str\n        :param SoldOut: json对象，key为机型，value true为售罄，false为未售罄\n        :type SoldOut: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResponse(AbstractModel):
    """查询kafka的zone信息返回的实体

    """

    def __init__(self):
        """
        :param ZoneList: zone列表\n        :type ZoneList: list of ZoneInfo\n        :param MaxBuyInstanceNum: 最大购买实例个数\n        :type MaxBuyInstanceNum: int\n        :param MaxBandwidth: 最大购买带宽 单位Mb/s\n        :type MaxBandwidth: int\n        :param UnitPrice: 后付费单位价格\n        :type UnitPrice: :class:`tencentcloud.ckafka.v20190819.models.Price`\n        :param MessagePrice: 后付费消息单价\n        :type MessagePrice: :class:`tencentcloud.ckafka.v20190819.models.Price`\n        :param ClusterInfo: 用户独占集群信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterInfo: list of ClusterInfo\n        :param Standard: 购买标准版配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Standard: str\n        :param StandardS2: 购买标准版S2配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type StandardS2: str\n        :param Profession: 购买专业版配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Profession: str\n        :param Physical: 购买物理独占版配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Physical: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        