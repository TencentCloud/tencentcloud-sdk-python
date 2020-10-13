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


class Connection(AbstractModel):
    """生产者连接实例

    """

    def __init__(self):
        """
        :param Address: 生产者地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Partitions: 主题分区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param ClientVersion: 生产者版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientVersion: str
        :param ProducerName: 生产者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerName: str
        :param ProducerId: 生产者ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerId: str
        :param AverageMsgSize: 消息平均大小(byte)。
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageMsgSize: str
        :param MsgThroughputIn: 生成速率(byte/秒)。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: str
        """
        self.Address = None
        self.Partitions = None
        self.ClientVersion = None
        self.ProducerName = None
        self.ProducerId = None
        self.AverageMsgSize = None
        self.MsgThroughputIn = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Partitions = params.get("Partitions")
        self.ClientVersion = params.get("ClientVersion")
        self.ProducerName = params.get("ProducerName")
        self.ProducerId = params.get("ProducerId")
        self.AverageMsgSize = params.get("AverageMsgSize")
        self.MsgThroughputIn = params.get("MsgThroughputIn")


class Consumer(AbstractModel):
    """消费者

    """

    def __init__(self):
        """
        :param ConnectedSince: 消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectedSince: str
        :param ConsumerAddr: 消费者地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerAddr: str
        :param ConsumerName: 消费者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerName: str
        :param ClientVersion: 消费者版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientVersion: str
        """
        self.ConnectedSince = None
        self.ConsumerAddr = None
        self.ConsumerName = None
        self.ClientVersion = None


    def _deserialize(self, params):
        self.ConnectedSince = params.get("ConnectedSince")
        self.ConsumerAddr = params.get("ConsumerAddr")
        self.ConsumerName = params.get("ConsumerName")
        self.ClientVersion = params.get("ClientVersion")


class ConsumersSchedule(AbstractModel):
    """消费进度详情

    """

    def __init__(self):
        """
        :param Partitions: 当前分区id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param NumberOfEntries: 消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfEntries: int
        :param MsgBacklog: 消息积压数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgBacklog: int
        :param MsgRateOut: 消费者每秒分发消息的数量之和。
        :type MsgRateOut: str
        :param MsgThroughputOut: 消费者每秒消息的byte。
        :type MsgThroughputOut: str
        :param MsgRateExpired: 超时丢弃比例。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateExpired: str
        """
        self.Partitions = None
        self.NumberOfEntries = None
        self.MsgBacklog = None
        self.MsgRateOut = None
        self.MsgThroughputOut = None
        self.MsgRateExpired = None


    def _deserialize(self, params):
        self.Partitions = params.get("Partitions")
        self.NumberOfEntries = params.get("NumberOfEntries")
        self.MsgBacklog = params.get("MsgBacklog")
        self.MsgRateOut = params.get("MsgRateOut")
        self.MsgThroughputOut = params.get("MsgThroughputOut")
        self.MsgRateExpired = params.get("MsgRateExpired")


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒，最小60，最大1296000，（15天）。
        :type MsgTTL: int
        :param Remark: 说明，128个字符以内。
        :type Remark: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒。
        :type MsgTTL: int
        :param Remark: 说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class CreateSubscriptionRequest(AbstractModel):
    """CreateSubscription请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param SubscriptionName: 订阅者名称，不支持中字以及除了短线和下划线外的特殊字符且不超过150个字符。
        :type SubscriptionName: str
        :param IsIdempotent: 是否幂等创建，若否不允许创建同名的订阅关系。
        :type IsIdempotent: bool
        :param Remark: 备注，128个字符以内。
        :type Remark: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.SubscriptionName = None
        self.IsIdempotent = None
        self.Remark = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.IsIdempotent = params.get("IsIdempotent")
        self.Remark = params.get("Remark")


class CreateSubscriptionResponse(AbstractModel):
    """CreateSubscription返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名，不支持中字以及除了短线和下划线外的特殊字符且不超过32个字符。
        :type TopicName: str
        :param Partitions: 0：非分区topic，无分区；非0：具体分区topic的分区数，最大不允许超过128。
        :type Partitions: int
        :param TopicType: 0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列；
5 ：事务消息。
        :type TopicType: int
        :param Remark: 备注，128字符以内。
        :type Remark: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.TopicType = None
        self.Remark = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.TopicType = params.get("TopicType")
        self.Remark = params.get("Remark")


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名。
        :type TopicName: str
        :param Partitions: 0：非分区topic，无分区；非0：具体分区topic的分区数。
        :type Partitions: int
        :param Remark: 备注，128字符以内。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param TopicType: 0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列；
5 ：事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.Remark = None
        self.TopicType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.TopicType = params.get("TopicType")
        self.RequestId = params.get("RequestId")


class DeleteEnvironmentsRequest(AbstractModel):
    """DeleteEnvironments请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentIds: 环境（命名空间）数组，每次最多删除20个。
        :type EnvironmentIds: list of str
        """
        self.EnvironmentIds = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")


class DeleteEnvironmentsResponse(AbstractModel):
    """DeleteEnvironments返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentIds: 成功删除的环境（命名空间）数组。
        :type EnvironmentIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvironmentIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")
        self.RequestId = params.get("RequestId")


class DeleteSubscriptionsRequest(AbstractModel):
    """DeleteSubscriptions请求参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionTopicSets: 订阅关系集合，每次最多删除20个。
        :type SubscriptionTopicSets: list of SubscriptionTopic
        """
        self.SubscriptionTopicSets = None


    def _deserialize(self, params):
        if params.get("SubscriptionTopicSets") is not None:
            self.SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self.SubscriptionTopicSets.append(obj)


class DeleteSubscriptionsResponse(AbstractModel):
    """DeleteSubscriptions返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionTopicSets: 成功删除的订阅关系数组。
        :type SubscriptionTopicSets: list of SubscriptionTopic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubscriptionTopicSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubscriptionTopicSets") is not None:
            self.SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self.SubscriptionTopicSets.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTopicsRequest(AbstractModel):
    """DeleteTopics请求参数结构体

    """

    def __init__(self):
        """
        :param TopicSets: 主题集合，每次最多删除20个。
        :type TopicSets: list of TopicRecord
        """
        self.TopicSets = None


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self.TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self.TopicSets.append(obj)


class DeleteTopicsResponse(AbstractModel):
    """DeleteTopics返回参数结构体

    """

    def __init__(self):
        """
        :param TopicSets: 被删除的主题数组。
        :type TopicSets: list of TopicRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self.TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self.TopicSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentAttributesRequest(AbstractModel):
    """DescribeEnvironmentAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        """
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")


class DescribeEnvironmentAttributesResponse(AbstractModel):
    """DescribeEnvironmentAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000（15天）。
        :type MsgTTL: int
        :param RateInByte: 消费速率限制，单位：byte/秒，0：不限速。
        :type RateInByte: int
        :param RateInSize: 消费速率限制，单位：个数/秒，0：不限速。
        :type RateInSize: int
        :param RetentionHours: 已消费消息保存策略，单位：小时，0：消费完马上删除。
        :type RetentionHours: int
        :param RetentionSize: 已消费消息保存策略，单位：G，0：消费完马上删除。
        :type RetentionSize: int
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param Replicas: 副本数。
        :type Replicas: int
        :param Remark: 备注。
        :type Remark: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MsgTTL = None
        self.RateInByte = None
        self.RateInSize = None
        self.RetentionHours = None
        self.RetentionSize = None
        self.EnvironmentId = None
        self.Replicas = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MsgTTL = params.get("MsgTTL")
        self.RateInByte = params.get("RateInByte")
        self.RateInSize = params.get("RateInSize")
        self.RetentionHours = params.get("RetentionHours")
        self.RetentionSize = params.get("RetentionSize")
        self.EnvironmentId = params.get("EnvironmentId")
        self.Replicas = params.get("Replicas")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentRolesRequest(AbstractModel):
    """DescribeEnvironmentRoles请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）
        :type EnvironmentId: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        """
        self.EnvironmentId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeEnvironmentRolesResponse(AbstractModel):
    """DescribeEnvironmentRoles返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录数。
        :type TotalCount: int
        :param EnvironmentRoleSets: 环境角色集合。
        :type EnvironmentRoleSets: list of EnvironmentRole
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EnvironmentRoleSets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentRoleSets") is not None:
            self.EnvironmentRoleSets = []
            for item in params.get("EnvironmentRoleSets"):
                obj = EnvironmentRole()
                obj._deserialize(item)
                self.EnvironmentRoleSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称，模糊搜索。
        :type EnvironmentId: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        """
        self.EnvironmentId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 环境（命名空间）记录数。
        :type TotalCount: int
        :param EnvironmentSet: 环境（命名空间）集合数组。
        :type EnvironmentSet: list of Environment
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EnvironmentSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentSet") is not None:
            self.EnvironmentSet = []
            for item in params.get("EnvironmentSet"):
                obj = Environment()
                obj._deserialize(item)
                self.EnvironmentSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProducersRequest(AbstractModel):
    """DescribeProducers请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名。
        :type TopicName: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param ProducerName: 生产者名称，模糊匹配。
        :type ProducerName: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.ProducerName = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProducerName = params.get("ProducerName")


class DescribeProducersResponse(AbstractModel):
    """DescribeProducers返回参数结构体

    """

    def __init__(self):
        """
        :param ProducerSets: 生产者集合数组。
        :type ProducerSets: list of Producer
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProducerSets = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProducerSets") is not None:
            self.ProducerSets = []
            for item in params.get("ProducerSets"):
                obj = Producer()
                obj._deserialize(item)
                self.ProducerSets.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSubscriptionsRequest(AbstractModel):
    """DescribeSubscriptions请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param SubscriptionName: 订阅者名称，模糊匹配。
        :type SubscriptionName: str
        :param Filters: 数据过滤条件。
        :type Filters: list of FilterSubscription
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.SubscriptionName = None
        self.Filters = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubscriptionName = params.get("SubscriptionName")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = FilterSubscription()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeSubscriptionsResponse(AbstractModel):
    """DescribeSubscriptions返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionSets: 订阅者集合数组。
        :type SubscriptionSets: list of Subscription
        :param TotalCount: 数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubscriptionSets = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubscriptionSets") is not None:
            self.SubscriptionSets = []
            for item in params.get("SubscriptionSets"):
                obj = Subscription()
                obj._deserialize(item)
                self.SubscriptionSets.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名模糊匹配。
        :type TopicName: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param TopicType: topic类型描述：
0：普通消息；
1：全局顺序消息；
2：局部顺序消息；
3：重试队列；
4：死信队列；
5：事务消息。
        :type TopicType: int
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.TopicType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TopicType = params.get("TopicType")


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics返回参数结构体

    """

    def __init__(self):
        """
        :param TopicSets: 主题集合数组。
        :type TopicSets: list of Topic
        :param TotalCount: 主题数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicSets = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self.TopicSets = []
            for item in params.get("TopicSets"):
                obj = Topic()
                obj._deserialize(item)
                self.TopicSets.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """环境信息

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称
        :type EnvironmentId: str
        :param Remark: 说明
        :type Remark: str
        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000（15天）
        :type MsgTTL: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 最近修改时间
        :type UpdateTime: str
        """
        self.EnvironmentId = None
        self.Remark = None
        self.MsgTTL = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Remark = params.get("Remark")
        self.MsgTTL = params.get("MsgTTL")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class EnvironmentRole(AbstractModel):
    """环境角色集合

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）。
        :type EnvironmentId: str
        :param RoleName: 角色名称。
        :type RoleName: str
        :param Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param RoleDescribe: 角色描述。
        :type RoleDescribe: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self.EnvironmentId = None
        self.RoleName = None
        self.Permissions = None
        self.RoleDescribe = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.RoleName = params.get("RoleName")
        self.Permissions = params.get("Permissions")
        self.RoleDescribe = params.get("RoleDescribe")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class FilterSubscription(AbstractModel):
    """过滤订阅列表

    """

    def __init__(self):
        """
        :param ConsumerHasCount: 是否仅展示包含真实消费者的订阅。
        :type ConsumerHasCount: bool
        :param ConsumerHasBacklog: 是否仅展示消息堆积的订阅。
        :type ConsumerHasBacklog: bool
        :param ConsumerHasExpired: 是否仅展示存在消息超期丢弃的订阅。
        :type ConsumerHasExpired: bool
        """
        self.ConsumerHasCount = None
        self.ConsumerHasBacklog = None
        self.ConsumerHasExpired = None


    def _deserialize(self, params):
        self.ConsumerHasCount = params.get("ConsumerHasCount")
        self.ConsumerHasBacklog = params.get("ConsumerHasBacklog")
        self.ConsumerHasExpired = params.get("ConsumerHasExpired")


class ModifyEnvironmentAttributesRequest(AbstractModel):
    """ModifyEnvironmentAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000。
        :type MsgTTL: int
        :param Remark: 备注，字符串最长不超过128。
        :type Remark: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")


class ModifyEnvironmentAttributesResponse(AbstractModel):
    """ModifyEnvironmentAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒。
        :type MsgTTL: int
        :param Remark: 备注，字符串最长不超过128。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名。
        :type TopicName: str
        :param Partitions: 分区数，必须大于或者等于原分区数，若想维持原分区数请输入原数目，修改分区数仅对非全局顺序消息起效果，不允许超过128个分区。
        :type Partitions: int
        :param Remark: 备注，128字符以内。
        :type Remark: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.Remark = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Partitions: 分区数
        :type Partitions: int
        :param Remark: 备注，128字符以内。
        :type Remark: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Partitions = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class PartitionsTopic(AbstractModel):
    """分区topic

    """

    def __init__(self):
        """
        :param AverageMsgSize: 最后一次间隔内发布消息的平均byte大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageMsgSize: str
        :param ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerCount: str
        :param LastConfirmedEntry: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastConfirmedEntry: str
        :param LastLedgerCreatedTimestamp: 最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLedgerCreatedTimestamp: str
        :param MsgRateIn: 本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: str
        :param MsgRateOut: 本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateOut: str
        :param MsgThroughputIn: 本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: str
        :param MsgThroughputOut: 本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputOut: str
        :param NumberOfEntries: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfEntries: str
        :param Partitions: 子分区id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param ProducerCount: 生产者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerCount: str
        :param TotalSize: 以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: str
        :param TopicType: topic类型描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicType: int
        """
        self.AverageMsgSize = None
        self.ConsumerCount = None
        self.LastConfirmedEntry = None
        self.LastLedgerCreatedTimestamp = None
        self.MsgRateIn = None
        self.MsgRateOut = None
        self.MsgThroughputIn = None
        self.MsgThroughputOut = None
        self.NumberOfEntries = None
        self.Partitions = None
        self.ProducerCount = None
        self.TotalSize = None
        self.TopicType = None


    def _deserialize(self, params):
        self.AverageMsgSize = params.get("AverageMsgSize")
        self.ConsumerCount = params.get("ConsumerCount")
        self.LastConfirmedEntry = params.get("LastConfirmedEntry")
        self.LastLedgerCreatedTimestamp = params.get("LastLedgerCreatedTimestamp")
        self.MsgRateIn = params.get("MsgRateIn")
        self.MsgRateOut = params.get("MsgRateOut")
        self.MsgThroughputIn = params.get("MsgThroughputIn")
        self.MsgThroughputOut = params.get("MsgThroughputOut")
        self.NumberOfEntries = params.get("NumberOfEntries")
        self.Partitions = params.get("Partitions")
        self.ProducerCount = params.get("ProducerCount")
        self.TotalSize = params.get("TotalSize")
        self.TopicType = params.get("TopicType")


class Producer(AbstractModel):
    """生产者

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param CountConnect: 连接数。
注意：此字段可能返回 null，表示取不到有效值。
        :type CountConnect: int
        :param ConnectionSets: 连接集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionSets: list of Connection
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.CountConnect = None
        self.ConnectionSets = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.CountConnect = params.get("CountConnect")
        if params.get("ConnectionSets") is not None:
            self.ConnectionSets = []
            for item in params.get("ConnectionSets"):
                obj = Connection()
                obj._deserialize(item)
                self.ConnectionSets.append(obj)


class ResetMsgSubOffsetByTimestampRequest(AbstractModel):
    """ResetMsgSubOffsetByTimestamp请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param Subscription: 订阅者名称。
        :type Subscription: str
        :param ToTimestamp: 时间戳，精确到毫秒。
        :type ToTimestamp: int
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Subscription = None
        self.ToTimestamp = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Subscription = params.get("Subscription")
        self.ToTimestamp = params.get("ToTimestamp")


class ResetMsgSubOffsetByTimestampResponse(AbstractModel):
    """ResetMsgSubOffsetByTimestamp返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """订阅者

    """

    def __init__(self):
        """
        :param TopicName: 主题名称。
        :type TopicName: str
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param ConnectedSince: 消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectedSince: str
        :param ConsumerAddr: 消费者地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerAddr: str
        :param ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerCount: str
        :param ConsumerName: 消费者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerName: str
        :param MsgBacklog: 堆积的消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgBacklog: str
        :param MsgRateExpired: 于TTL，此订阅下没有被发送而是被丢弃的比例。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateExpired: str
        :param MsgRateOut: 消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateOut: str
        :param MsgThroughputOut: 消费者每秒消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputOut: str
        :param SubscriptionName: 订阅名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionName: str
        :param ConsumerSets: 消费者集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerSets: list of Consumer
        :param IsOnline: 是否在线。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOnline: bool
        :param ConsumersScheduleSets: 消费进度集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumersScheduleSets: list of ConsumersSchedule
        :param Remark: 备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.TopicName = None
        self.EnvironmentId = None
        self.ConnectedSince = None
        self.ConsumerAddr = None
        self.ConsumerCount = None
        self.ConsumerName = None
        self.MsgBacklog = None
        self.MsgRateExpired = None
        self.MsgRateOut = None
        self.MsgThroughputOut = None
        self.SubscriptionName = None
        self.ConsumerSets = None
        self.IsOnline = None
        self.ConsumersScheduleSets = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.EnvironmentId = params.get("EnvironmentId")
        self.ConnectedSince = params.get("ConnectedSince")
        self.ConsumerAddr = params.get("ConsumerAddr")
        self.ConsumerCount = params.get("ConsumerCount")
        self.ConsumerName = params.get("ConsumerName")
        self.MsgBacklog = params.get("MsgBacklog")
        self.MsgRateExpired = params.get("MsgRateExpired")
        self.MsgRateOut = params.get("MsgRateOut")
        self.MsgThroughputOut = params.get("MsgThroughputOut")
        self.SubscriptionName = params.get("SubscriptionName")
        if params.get("ConsumerSets") is not None:
            self.ConsumerSets = []
            for item in params.get("ConsumerSets"):
                obj = Consumer()
                obj._deserialize(item)
                self.ConsumerSets.append(obj)
        self.IsOnline = params.get("IsOnline")
        if params.get("ConsumersScheduleSets") is not None:
            self.ConsumersScheduleSets = []
            for item in params.get("ConsumersScheduleSets"):
                obj = ConsumersSchedule()
                obj._deserialize(item)
                self.ConsumersScheduleSets.append(obj)
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class SubscriptionTopic(AbstractModel):
    """订阅关系

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param SubscriptionName: 订阅名称。
        :type SubscriptionName: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")


class Topic(AbstractModel):
    """主题实例

    """

    def __init__(self):
        """
        :param AverageMsgSize: 最后一次间隔内发布消息的平均byte大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageMsgSize: str
        :param ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerCount: str
        :param LastConfirmedEntry: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastConfirmedEntry: str
        :param LastLedgerCreatedTimestamp: 最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLedgerCreatedTimestamp: str
        :param MsgRateIn: 本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: str
        :param MsgRateOut: 本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateOut: str
        :param MsgThroughputIn: 本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: str
        :param MsgThroughputOut: 本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputOut: str
        :param NumberOfEntries: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfEntries: str
        :param Partitions: 分区数<=0：topic下无子分区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param ProducerCount: 生产者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerCount: str
        :param TotalSize: 以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: str
        :param SubTopicSets: 分区topic里面的子分区。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubTopicSets: list of PartitionsTopic
        :param TopicType: topic类型描述：
0：普通消息；
1：全局顺序消息；
2：局部顺序消息；
3：重试队列；
4：死信队列；
5：事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicType: int
        :param EnvironmentId: 环境（命名空间）名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param Remark: 说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.AverageMsgSize = None
        self.ConsumerCount = None
        self.LastConfirmedEntry = None
        self.LastLedgerCreatedTimestamp = None
        self.MsgRateIn = None
        self.MsgRateOut = None
        self.MsgThroughputIn = None
        self.MsgThroughputOut = None
        self.NumberOfEntries = None
        self.Partitions = None
        self.ProducerCount = None
        self.TotalSize = None
        self.SubTopicSets = None
        self.TopicType = None
        self.EnvironmentId = None
        self.TopicName = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.AverageMsgSize = params.get("AverageMsgSize")
        self.ConsumerCount = params.get("ConsumerCount")
        self.LastConfirmedEntry = params.get("LastConfirmedEntry")
        self.LastLedgerCreatedTimestamp = params.get("LastLedgerCreatedTimestamp")
        self.MsgRateIn = params.get("MsgRateIn")
        self.MsgRateOut = params.get("MsgRateOut")
        self.MsgThroughputIn = params.get("MsgThroughputIn")
        self.MsgThroughputOut = params.get("MsgThroughputOut")
        self.NumberOfEntries = params.get("NumberOfEntries")
        self.Partitions = params.get("Partitions")
        self.ProducerCount = params.get("ProducerCount")
        self.TotalSize = params.get("TotalSize")
        if params.get("SubTopicSets") is not None:
            self.SubTopicSets = []
            for item in params.get("SubTopicSets"):
                obj = PartitionsTopic()
                obj._deserialize(item)
                self.SubTopicSets.append(obj)
        self.TopicType = params.get("TopicType")
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class TopicRecord(AbstractModel):
    """主题关键信息

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        """
        self.EnvironmentId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")