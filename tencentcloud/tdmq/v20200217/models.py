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


class BindCluster(AbstractModel):
    """用户专享集群信息

    """

    def __init__(self):
        """
        :param ClusterName: 物理集群的名称
        :type ClusterName: str
        """
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")


class ClearCmqQueueRequest(AbstractModel):
    """ClearCmqQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class ClearCmqQueueResponse(AbstractModel):
    """ClearCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearCmqSubscriptionFilterTagsRequest(AbstractModel):
    """ClearCmqSubscriptionFilterTags请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")


class ClearCmqSubscriptionFilterTagsResponse(AbstractModel):
    """ClearCmqSubscriptionFilterTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """集群信息集合

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id。
        :type ClusterId: str
        :param ClusterName: 集群名称。
        :type ClusterName: str
        :param Remark: 说明信息。
        :type Remark: str
        :param EndPointNum: 接入点数量
        :type EndPointNum: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Healthy: 集群是否健康，1表示健康，0表示异常
        :type Healthy: int
        :param HealthyInfo: 集群健康信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthyInfo: str
        :param Status: 集群状态，0:创建中，1:正常，2:删除中，3:已删除，5:创建失败，6: 删除失败
        :type Status: int
        :param MaxNamespaceNum: 最大命名空间数量
        :type MaxNamespaceNum: int
        :param MaxTopicNum: 最大Topic数量
        :type MaxTopicNum: int
        :param MaxQps: 最大QPS
        :type MaxQps: int
        :param MessageRetentionTime: 消息保留时间
        :type MessageRetentionTime: int
        :param MaxStorageCapacity: 最大存储容量
        :type MaxStorageCapacity: int
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Remark = None
        self.EndPointNum = None
        self.CreateTime = None
        self.Healthy = None
        self.HealthyInfo = None
        self.Status = None
        self.MaxNamespaceNum = None
        self.MaxTopicNum = None
        self.MaxQps = None
        self.MessageRetentionTime = None
        self.MaxStorageCapacity = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Remark = params.get("Remark")
        self.EndPointNum = params.get("EndPointNum")
        self.CreateTime = params.get("CreateTime")
        self.Healthy = params.get("Healthy")
        self.HealthyInfo = params.get("HealthyInfo")
        self.Status = params.get("Status")
        self.MaxNamespaceNum = params.get("MaxNamespaceNum")
        self.MaxTopicNum = params.get("MaxTopicNum")
        self.MaxQps = params.get("MaxQps")
        self.MessageRetentionTime = params.get("MessageRetentionTime")
        self.MaxStorageCapacity = params.get("MaxStorageCapacity")


class CmqDeadLetterPolicy(AbstractModel):
    """cmq DeadLetterPolicy

    """

    def __init__(self):
        """
        :param DeadLetterQueue: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterQueue: str
        :param Policy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: int
        :param MaxTimeToLive: 最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTimeToLive: int
        :param MaxReceiveCount: 最大接收次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReceiveCount: int
        """
        self.DeadLetterQueue = None
        self.Policy = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None


    def _deserialize(self, params):
        self.DeadLetterQueue = params.get("DeadLetterQueue")
        self.Policy = params.get("Policy")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")


class CmqDeadLetterSource(AbstractModel):
    """Cmq DeadLetterSource

    """

    def __init__(self):
        """
        :param QueueId: 消息队列ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueId: str
        :param QueueName: 消息队列名字。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        """
        self.QueueId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")


class CmqQueue(AbstractModel):
    """cmq 批量queue属性信息

    """

    def __init__(self):
        """
        :param QueueId: 消息队列ID。
        :type QueueId: str
        :param QueueName: 消息队列名字。
        :type QueueName: str
        :param Qps: 每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        :param Bps: 带宽限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bps: int
        :param MaxDelaySeconds: 飞行消息最大保留时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDelaySeconds: int
        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
注意：此字段可能返回 null，表示取不到有效值。
        :type PollingWaitSeconds: int
        :param MsgRetentionSeconds: 消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param VisibilityTimeout: 消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
注意：此字段可能返回 null，表示取不到有效值。
        :type VisibilityTimeout: int
        :param MaxMsgSize: 消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param RewindSeconds: 回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
注意：此字段可能返回 null，表示取不到有效值。
        :type RewindSeconds: int
        :param CreateTime: 队列的创建时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LastModifyTime: 最后一次修改队列属性的时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param ActiveMsgNum: 在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveMsgNum: int
        :param InactiveMsgNum: 在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。
        :type InactiveMsgNum: int
        :param DelayMsgNum: 延迟消息数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayMsgNum: int
        :param RewindMsgNum: 已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type RewindMsgNum: int
        :param MinMsgTime: 消息最小未消费时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type MinMsgTime: int
        :param Transaction: 事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Transaction: bool
        :param DeadLetterSource: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterSource: list of CmqDeadLetterSource
        :param DeadLetterPolicy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqDeadLetterPolicy`
        :param TransactionPolicy: 事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqTransactionPolicy`
        :param CreateUin: 创建者Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
        :param TenantId: 租户id
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        """
        self.QueueId = None
        self.QueueName = None
        self.Qps = None
        self.Bps = None
        self.MaxDelaySeconds = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.MsgRetentionSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.RewindSeconds = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.ActiveMsgNum = None
        self.InactiveMsgNum = None
        self.DelayMsgNum = None
        self.RewindMsgNum = None
        self.MinMsgTime = None
        self.Transaction = None
        self.DeadLetterSource = None
        self.DeadLetterPolicy = None
        self.TransactionPolicy = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None
        self.TenantId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")
        self.Qps = params.get("Qps")
        self.Bps = params.get("Bps")
        self.MaxDelaySeconds = params.get("MaxDelaySeconds")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.RewindSeconds = params.get("RewindSeconds")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.ActiveMsgNum = params.get("ActiveMsgNum")
        self.InactiveMsgNum = params.get("InactiveMsgNum")
        self.DelayMsgNum = params.get("DelayMsgNum")
        self.RewindMsgNum = params.get("RewindMsgNum")
        self.MinMsgTime = params.get("MinMsgTime")
        self.Transaction = params.get("Transaction")
        if params.get("DeadLetterSource") is not None:
            self.DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = CmqDeadLetterSource()
                obj._deserialize(item)
                self.DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self.DeadLetterPolicy = CmqDeadLetterPolicy()
            self.DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self.TransactionPolicy = CmqTransactionPolicy()
            self.TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")
        self.TenantId = params.get("TenantId")
        self.NamespaceName = params.get("NamespaceName")


class CmqSubscription(AbstractModel):
    """cmq订阅返回参数

    """

    def __init__(self):
        """
        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionName: str
        :param SubscriptionId: 订阅 ID。订阅 ID 在拉取监控数据时会用到。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionId: str
        :param TopicOwner: 订阅拥有者的 APPID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicOwner: int
        :param MsgCount: 该订阅待投递的消息数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param LastModifyTime: 最后一次修改订阅属性的时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param CreateTime: 订阅的创建时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param BindingKey: 表示订阅接收消息的过滤策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingKey: list of str
        :param Endpoint: 接收通知的 endpoint，根据协议 protocol 区分：对于 HTTP，endpoint 必须以http://开头，host 可以是域名或 IP；对于 queue，则填 queueName。
注意：此字段可能返回 null，表示取不到有效值。
        :type Endpoint: str
        :param FilterTags: 描述用户创建订阅时选择的过滤策略：
filterType = 1表示用户使用 filterTag 标签过滤
filterType = 2表示用户使用 bindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterTags: list of str
        :param Protocol: 订阅的协议，目前支持两种协议：HTTP、queue。使用 HTTP 协议，用户需自己搭建接受消息的 Web Server。使用 queue，消息会自动推送到 CMQ queue，用户可以并发地拉取消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param NotifyStrategy: 向 endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值有：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始 1s，后面是 2s，4s，8s...由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyStrategy: str
        :param NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 protocol 是 queue，则取值必须为 SIMPLIFIED。如果 protocol 是 HTTP，两个值均可以，默认值是 JSON。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyContentFormat: str
        """
        self.SubscriptionName = None
        self.SubscriptionId = None
        self.TopicOwner = None
        self.MsgCount = None
        self.LastModifyTime = None
        self.CreateTime = None
        self.BindingKey = None
        self.Endpoint = None
        self.FilterTags = None
        self.Protocol = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.SubscriptionName = params.get("SubscriptionName")
        self.SubscriptionId = params.get("SubscriptionId")
        self.TopicOwner = params.get("TopicOwner")
        self.MsgCount = params.get("MsgCount")
        self.LastModifyTime = params.get("LastModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.BindingKey = params.get("BindingKey")
        self.Endpoint = params.get("Endpoint")
        self.FilterTags = params.get("FilterTags")
        self.Protocol = params.get("Protocol")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")


class CmqTopic(AbstractModel):
    """cmq topic返回信息展示字段

    """

    def __init__(self):
        """
        :param TopicId: 主题的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param MsgRetentionSeconds: 消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param MaxMsgSize: 消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为65536。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param Qps: 每秒钟发布消息的条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        :param FilterType: 描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: int
        :param CreateTime: 主题的创建时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LastModifyTime: 最后一次修改主题属性的时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param MsgCount: 当前该主题中消息数目（消息堆积数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param CreateUin: 创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
        :param TenantId: 租户id
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantId: str
        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        """
        self.TopicId = None
        self.TopicName = None
        self.MsgRetentionSeconds = None
        self.MaxMsgSize = None
        self.Qps = None
        self.FilterType = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.MsgCount = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None
        self.TenantId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.Qps = params.get("Qps")
        self.FilterType = params.get("FilterType")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.MsgCount = params.get("MsgCount")
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")
        self.TenantId = params.get("TenantId")
        self.NamespaceName = params.get("NamespaceName")


class CmqTransactionPolicy(AbstractModel):
    """cmq TransactionPolicy

    """

    def __init__(self):
        """
        :param FirstQueryInterval: 第一次回查时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstQueryInterval: int
        :param MaxQueryCount: 最大查询次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxQueryCount: int
        """
        self.FirstQueryInterval = None
        self.MaxQueryCount = None


    def _deserialize(self, params):
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")


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


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterName: 集群名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。
        :type ClusterName: str
        :param BindClusterId: 用户专享物理集群ID，如果不传，则默认在公共集群上创建用户集群资源。
        :type BindClusterId: int
        :param Remark: 说明，128个字符以内。
        :type Remark: str
        :param Tags: 集群的标签列表
        :type Tags: list of Tag
        """
        self.ClusterName = None
        self.BindClusterId = None
        self.Remark = None
        self.Tags = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.BindClusterId = params.get("BindClusterId")
        self.Remark = params.get("Remark")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateCmqQueueRequest(AbstractModel):
    """CreateCmqQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :type PollingWaitSeconds: int
        :param VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :type VisibilityTimeout: int
        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。
        :type MsgRetentionSeconds: int
        :param RewindSeconds: 队列是否开启回溯消息能力，该参数取值范围0-msgRetentionSeconds,即最大的回溯时间为消息在队列中的保留周期，0表示不开启。
        :type RewindSeconds: int
        :param Transaction: 1 表示事务队列，0 表示普通队列
        :type Transaction: int
        :param FirstQueryInterval: 第一次回查间隔
        :type FirstQueryInterval: int
        :param MaxQueryCount: 最大回查次数
        :type MaxQueryCount: int
        :param DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param Policy: 死信策略。0为消息被多次消费未删除，1为Time-To-Live过期
        :type Policy: int
        :param MaxReceiveCount: 最大接收次数 1-1000
        :type MaxReceiveCount: int
        :param MaxTimeToLive: policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds
        :type MaxTimeToLive: int
        :param Trace: 是否开启消息轨迹追踪，当不设置字段时，默认为不开启，该字段为true表示开启，为false表示不开启
        :type Trace: bool
        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.Transaction = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.Policy = None
        self.MaxReceiveCount = None
        self.MaxTimeToLive = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.Transaction = params.get("Transaction")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Policy = params.get("Policy")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.Trace = params.get("Trace")


class CreateCmqQueueResponse(AbstractModel):
    """CreateCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param QueueId: 创建成功的queueId
        :type QueueId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QueueId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.RequestId = params.get("RequestId")


class CreateCmqSubscribeRequest(AbstractModel):
    """CreateCmqSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        :param Protocol: 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。
        :type Protocol: str
        :param Endpoint: 接收通知的Endpoint，根据协议Protocol区分：对于http，Endpoint必须以“`http://`”开头，host可以是域名或IP；对于Queue，则填QueueName。 请注意，目前推送服务不能推送到私有网络中，因此Endpoint填写为私有网络域名或地址将接收不到推送的消息，目前支持推送到公网和基础网络。
        :type Endpoint: str
        :param NotifyStrategy: 向Endpoint推送消息出现错误时，CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s...由于Topic消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是EXPONENTIAL_DECAY_RETRY。
        :type NotifyStrategy: str
        :param FilterTag: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。
        :type FilterTag: list of str
        :param BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。
        :type BindingKey: list of str
        :param NotifyContentFormat: 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，则取值必须为SIMPLIFIED。如果Protocol是http，两个值均可以，默认值是JSON。
        :type NotifyContentFormat: str
        """
        self.TopicName = None
        self.SubscriptionName = None
        self.Protocol = None
        self.Endpoint = None
        self.NotifyStrategy = None
        self.FilterTag = None
        self.BindingKey = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.Protocol = params.get("Protocol")
        self.Endpoint = params.get("Endpoint")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.FilterTag = params.get("FilterTag")
        self.BindingKey = params.get("BindingKey")
        self.NotifyContentFormat = params.get("NotifyContentFormat")


class CreateCmqSubscribeResponse(AbstractModel):
    """CreateCmqSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionId: 订阅id
        :type SubscriptionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubscriptionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscriptionId = params.get("SubscriptionId")
        self.RequestId = params.get("RequestId")


class CreateCmqTopicRequest(AbstractModel):
    """CreateCmqTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param FilterType: 用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略，默认值为标签匹配策略。
        :type FilterType: int
        :param MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。
        :type MsgRetentionSeconds: int
        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.FilterType = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.FilterType = params.get("FilterType")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")


class CreateCmqTopicResponse(AbstractModel):
    """CreateCmqTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 主题id
        :type TopicId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


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
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")


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
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.NamespaceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.NamespaceId = params.get("NamespaceId")
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
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param AutoCreatePolicyTopic: 是否自动创建死信和重试主题，True 表示创建，False表示不创建，默认自动创建死信和重试主题。
        :type AutoCreatePolicyTopic: bool
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.SubscriptionName = None
        self.IsIdempotent = None
        self.Remark = None
        self.ClusterId = None
        self.AutoCreatePolicyTopic = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.IsIdempotent = params.get("IsIdempotent")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        self.AutoCreatePolicyTopic = params.get("AutoCreatePolicyTopic")


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
        :param TopicName: 主题名，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
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
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.TopicType = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.TopicType = params.get("TopicType")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")


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


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id，传入需要删除的集群Id。
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群的ID
        :type ClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class DeleteCmqQueueRequest(AbstractModel):
    """DeleteCmqQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class DeleteCmqQueueResponse(AbstractModel):
    """DeleteCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCmqSubscribeRequest(AbstractModel):
    """DeleteCmqSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")


class DeleteCmqSubscribeResponse(AbstractModel):
    """DeleteCmqSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCmqTopicRequest(AbstractModel):
    """DeleteCmqTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")


class DeleteCmqTopicResponse(AbstractModel):
    """DeleteCmqTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEnvironmentsRequest(AbstractModel):
    """DeleteEnvironments请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentIds: 环境（命名空间）数组，每次最多删除20个。
        :type EnvironmentIds: list of str
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentIds = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")
        self.ClusterId = params.get("ClusterId")


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
        :param ClusterId: pulsar集群Id。
        :type ClusterId: str
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        """
        self.SubscriptionTopicSets = None
        self.ClusterId = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        if params.get("SubscriptionTopicSets") is not None:
            self.SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self.SubscriptionTopicSets.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.EnvironmentId = params.get("EnvironmentId")


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
        :param ClusterId: pulsar集群Id。
        :type ClusterId: str
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        """
        self.TopicSets = None
        self.ClusterId = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self.TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self.TopicSets.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.EnvironmentId = params.get("EnvironmentId")


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


class DescribeBindClustersRequest(AbstractModel):
    """DescribeBindClusters请求参数结构体

    """


class DescribeBindClustersResponse(AbstractModel):
    """DescribeBindClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 专享集群的数量
        :type TotalCount: int
        :param ClusterSet: 专享集群的列表
        :type ClusterSet: list of BindCluster
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
                obj = BindCluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBindVpcsRequest(AbstractModel):
    """DescribeBindVpcs请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.Offset = None
        self.Limit = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")


class DescribeBindVpcsResponse(AbstractModel):
    """DescribeBindVpcs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录数。
        :type TotalCount: int
        :param VpcSets: Vpc集合。
        :type VpcSets: list of VpcBindRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcSets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcSets") is not None:
            self.VpcSets = []
            for item in params.get("VpcSets"):
                obj = VpcBindRecord()
                obj._deserialize(item)
                self.VpcSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群的ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterSet: 集群的详细信息
        :type ClusterSet: :class:`tencentcloud.tdmq.v20200217.models.Cluster`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterSet") is not None:
            self.ClusterSet = Cluster()
            self.ClusterSet._deserialize(params.get("ClusterSet"))
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群列表数量
        :type TotalCount: int
        :param ClusterSet: 集群信息列表
        :type ClusterSet: list of Cluster
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
                obj = Cluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCmqDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeCmqDeadLetterSourceQueues请求参数结构体

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param Limit: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。
        :type Limit: int
        :param Offset: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Offset: int
        :param SourceQueueName: 根据SourceQueueName过滤
        :type SourceQueueName: str
        """
        self.DeadLetterQueueName = None
        self.Limit = None
        self.Offset = None
        self.SourceQueueName = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceQueueName = params.get("SourceQueueName")


class DescribeCmqDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeCmqDeadLetterSourceQueues返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 满足本次条件的队列个数
        :type TotalCount: int
        :param QueueSet: 死信队列源队列
        :type QueueSet: list of CmqDeadLetterSource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = CmqDeadLetterSource()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCmqQueueDetailRequest(AbstractModel):
    """DescribeCmqQueueDetail请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 精确匹配QueueName
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class DescribeCmqQueueDetailResponse(AbstractModel):
    """DescribeCmqQueueDetail返回参数结构体

    """

    def __init__(self):
        """
        :param QueueDescribe: 队列详情列表。
        :type QueueDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqQueue`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QueueDescribe = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QueueDescribe") is not None:
            self.QueueDescribe = CmqQueue()
            self.QueueDescribe._deserialize(params.get("QueueDescribe"))
        self.RequestId = params.get("RequestId")


class DescribeCmqQueuesRequest(AbstractModel):
    """DescribeCmqQueues请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param QueueName: 根据QueueName进行过滤
        :type QueueName: str
        """
        self.Offset = None
        self.Limit = None
        self.QueueName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.QueueName = params.get("QueueName")


class DescribeCmqQueuesResponse(AbstractModel):
    """DescribeCmqQueues返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 数量
        :type TotalCount: int
        :param QueueList: 队列列表
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueList: list of CmqQueue
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.QueueList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueList") is not None:
            self.QueueList = []
            for item in params.get("QueueList"):
                obj = CmqQueue()
                obj._deserialize(item)
                self.QueueList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCmqSubscriptionDetailRequest(AbstractModel):
    """DescribeCmqSubscriptionDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param Offset: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param Limit: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param SubscriptionName: 根据SubscriptionName进行模糊搜索
        :type SubscriptionName: str
        """
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubscriptionName = params.get("SubscriptionName")


class DescribeCmqSubscriptionDetailResponse(AbstractModel):
    """DescribeCmqSubscriptionDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param SubscriptionSet: Subscription属性集合
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionSet: list of CmqSubscription
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SubscriptionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubscriptionSet") is not None:
            self.SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = CmqSubscription()
                obj._deserialize(item)
                self.SubscriptionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCmqTopicDetailRequest(AbstractModel):
    """DescribeCmqTopicDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 精确匹配TopicName。
        :type TopicName: str
        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")


class DescribeCmqTopicDetailResponse(AbstractModel):
    """DescribeCmqTopicDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TopicDescribe: 主题详情
        :type TopicDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqTopic`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicDescribe = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicDescribe") is not None:
            self.TopicDescribe = CmqTopic()
            self.TopicDescribe._deserialize(params.get("TopicDescribe"))
        self.RequestId = params.get("RequestId")


class DescribeCmqTopicsRequest(AbstractModel):
    """DescribeCmqTopics请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param TopicName: 根据TopicName进行模糊搜索
        :type TopicName: str
        """
        self.Offset = None
        self.Limit = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TopicName = params.get("TopicName")


class DescribeCmqTopicsResponse(AbstractModel):
    """DescribeCmqTopics返回参数结构体

    """

    def __init__(self):
        """
        :param TopicList: 主题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of CmqTopic
        :param TotalCount: 全量主题数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = CmqTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentAttributesRequest(AbstractModel):
    """DescribeEnvironmentAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterId = params.get("ClusterId")


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
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param RoleName: 角色名称
        :type RoleName: str
        """
        self.EnvironmentId = None
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.RoleName = params.get("RoleName")


class DescribeEnvironmentRolesResponse(AbstractModel):
    """DescribeEnvironmentRoles返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录数。
        :type TotalCount: int
        :param EnvironmentRoleSets: 命名空间角色集合。
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
        :param EnvironmentId: 命名空间名称，模糊搜索。
        :type EnvironmentId: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param Filters: * EnvironmentId
按照名称空间进行过滤，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self.EnvironmentId = None
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.Filters = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 命名空间记录数。
        :type TotalCount: int
        :param EnvironmentSet: 命名空间集合数组。
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
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.ProducerName = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProducerName = params.get("ProducerName")
        self.ClusterId = params.get("ClusterId")


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
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.SubscriptionName = None
        self.Filters = None
        self.ClusterId = None


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
        self.ClusterId = params.get("ClusterId")


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
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param Filters: * TopicName
按照主题名字查询，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.TopicType = None
        self.ClusterId = None
        self.Filters = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TopicType = params.get("TopicType")
        self.ClusterId = params.get("ClusterId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


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
    """命名空间信息

    """

    def __init__(self):
        """
        :param EnvironmentId: 命名空间名称
        :type EnvironmentId: str
        :param Remark: 说明
        :type Remark: str
        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000（15天）
        :type MsgTTL: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 最近修改时间
        :type UpdateTime: str
        :param NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param NamespaceName: 命名空间名称
        :type NamespaceName: str
        """
        self.EnvironmentId = None
        self.Remark = None
        self.MsgTTL = None
        self.CreateTime = None
        self.UpdateTime = None
        self.NamespaceId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Remark = params.get("Remark")
        self.MsgTTL = params.get("MsgTTL")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")


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


class Filter(AbstractModel):
    """过滤参数

    """

    def __init__(self):
        """
        :param Name: 过滤参数的名字
        :type Name: str
        :param Values: 数值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


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
        :param SubscriptionNames: 按照订阅名过滤，精确查询。
        :type SubscriptionNames: list of str
        """
        self.ConsumerHasCount = None
        self.ConsumerHasBacklog = None
        self.ConsumerHasExpired = None
        self.SubscriptionNames = None


    def _deserialize(self, params):
        self.ConsumerHasCount = params.get("ConsumerHasCount")
        self.ConsumerHasBacklog = params.get("ConsumerHasBacklog")
        self.ConsumerHasExpired = params.get("ConsumerHasExpired")
        self.SubscriptionNames = params.get("SubscriptionNames")


class ModifyClusterRequest(AbstractModel):
    """ModifyCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: Pulsar 集群的ID，需要更新的集群Id。
        :type ClusterId: str
        :param ClusterName: 更新后的集群名称。
        :type ClusterName: str
        :param Remark: 说明信息。
        :type Remark: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Remark = params.get("Remark")


class ModifyClusterResponse(AbstractModel):
    """ModifyCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class ModifyCmqQueueAttributeRequest(AbstractModel):
    """ModifyCmqQueueAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :type PollingWaitSeconds: int
        :param VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :type VisibilityTimeout: int
        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。
        :type MsgRetentionSeconds: int
        :param RewindSeconds: 消息最长回溯时间，取值范围0-msgRetentionSeconds，消息的最大回溯之间为消息在队列中的保存周期，0表示不开启消息回溯。
        :type RewindSeconds: int
        :param FirstQueryInterval: 第一次查询时间
        :type FirstQueryInterval: int
        :param MaxQueryCount: 最大查询次数
        :type MaxQueryCount: int
        :param DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param MaxTimeToLive: MaxTimeToLivepolicy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds
        :type MaxTimeToLive: int
        :param MaxReceiveCount: 最大接收次数
        :type MaxReceiveCount: int
        :param Policy: 死信队列策略
        :type Policy: int
        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        :param Transaction: 是否开启事务，1开启，0不开启
        :type Transaction: int
        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None
        self.Policy = None
        self.Trace = None
        self.Transaction = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.Policy = params.get("Policy")
        self.Trace = params.get("Trace")
        self.Transaction = params.get("Transaction")


class ModifyCmqQueueAttributeResponse(AbstractModel):
    """ModifyCmqQueueAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCmqSubscriptionAttributeRequest(AbstractModel):
    """ModifyCmqSubscriptionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        :param NotifyStrategy: 向 Endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值如下：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息。
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s···由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
        :type NotifyStrategy: str
        :param NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 Protocol 是 queue，则取值必须为 SIMPLIFIED。如果 Protocol 是 HTTP，两个值均可以，默认值是 JSON。
        :type NotifyContentFormat: str
        :param FilterTags: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。
        :type FilterTags: list of str
        :param BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。
        :type BindingKey: list of str
        """
        self.TopicName = None
        self.SubscriptionName = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None
        self.FilterTags = None
        self.BindingKey = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        self.FilterTags = params.get("FilterTags")
        self.BindingKey = params.get("BindingKey")


class ModifyCmqSubscriptionAttributeResponse(AbstractModel):
    """ModifyCmqSubscriptionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCmqTopicAttributeRequest(AbstractModel):
    """ModifyCmqTopicAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        :param MaxMsgSize: 消息最大长度。取值范围1024 - 65536 Byte（即1 - 64K），默认值65536。
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。
        :type MsgRetentionSeconds: int
        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")


class ModifyCmqTopicAttributeResponse(AbstractModel):
    """ModifyCmqTopicAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEnvironmentAttributesRequest(AbstractModel):
    """ModifyEnvironmentAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 命名空间名称。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000。
        :type MsgTTL: int
        :param Remark: 备注，字符串最长不超过128。
        :type Remark: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")


class ModifyEnvironmentAttributesResponse(AbstractModel):
    """ModifyEnvironmentAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 命名空间名称。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒。
        :type MsgTTL: int
        :param Remark: 备注，字符串最长不超过128。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.NamespaceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.NamespaceId = params.get("NamespaceId")
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
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")


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


class PublishCmqMsgRequest(AbstractModel):
    """PublishCmqMsg请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名
        :type TopicName: str
        :param MsgContent: 消息内容
        :type MsgContent: str
        :param MsgTag: 消息标签
        :type MsgTag: list of str
        """
        self.TopicName = None
        self.MsgContent = None
        self.MsgTag = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MsgContent = params.get("MsgContent")
        self.MsgTag = params.get("MsgTag")


class PublishCmqMsgResponse(AbstractModel):
    """PublishCmqMsg返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true表示发送成功
        :type Result: bool
        :param MsgId: 消息id
        :type MsgId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.MsgId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.MsgId = params.get("MsgId")
        self.RequestId = params.get("RequestId")


class ResetMsgSubOffsetByTimestampRequest(AbstractModel):
    """ResetMsgSubOffsetByTimestamp请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 命名空间名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称。
        :type TopicName: str
        :param Subscription: 订阅者名称。
        :type Subscription: str
        :param ToTimestamp: 时间戳，精确到毫秒。
        :type ToTimestamp: int
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Subscription = None
        self.ToTimestamp = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Subscription = params.get("Subscription")
        self.ToTimestamp = params.get("ToTimestamp")
        self.ClusterId = params.get("ClusterId")


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


class RewindCmqQueueRequest(AbstractModel):
    """RewindCmqQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param StartConsumeTime: 设定该时间，则（Batch）receiveMessage接口，会按照生产消息的先后顺序消费该时间戳以后的消息。
        :type StartConsumeTime: int
        """
        self.QueueName = None
        self.StartConsumeTime = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.StartConsumeTime = params.get("StartConsumeTime")


class RewindCmqQueueResponse(AbstractModel):
    """RewindCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendBatchMessagesRequest(AbstractModel):
    """SendBatchMessages请求参数结构体

    """

    def __init__(self):
        """
        :param Topic: Topic name
        :type Topic: str
        :param Payload: 需要发送消息的内容
        :type Payload: str
        :param StringToken: String 类型的 token，用来校验客户端和服务端之间的连接
        :type StringToken: str
        :param ProducerName: producer 的名字，要求全局是唯一的，如果不设置，系统会自动生成
        :type ProducerName: str
        :param SendTimeout: 单位：s。消息发送的超时时间。默认值为：30s
        :type SendTimeout: int
        :param MaxPendingMessages: 内存中允许缓存的生产消息的最大数量，默认值：1000条
        :type MaxPendingMessages: int
        :param BatchingMaxMessages: 每一个batch中消息的最大数量，默认值：1000条/batch
        :type BatchingMaxMessages: int
        :param BatchingMaxPublishDelay: 每一个batch最大等待的时间，超过这个时间，不管是否达到指定的batch中消息的数量和大小，都会将该batch发送出去，默认：10ms
        :type BatchingMaxPublishDelay: int
        :param BatchingMaxBytes: 每一个batch中最大允许的消息的大小，默认：128KB
        :type BatchingMaxBytes: int
        """
        self.Topic = None
        self.Payload = None
        self.StringToken = None
        self.ProducerName = None
        self.SendTimeout = None
        self.MaxPendingMessages = None
        self.BatchingMaxMessages = None
        self.BatchingMaxPublishDelay = None
        self.BatchingMaxBytes = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.StringToken = params.get("StringToken")
        self.ProducerName = params.get("ProducerName")
        self.SendTimeout = params.get("SendTimeout")
        self.MaxPendingMessages = params.get("MaxPendingMessages")
        self.BatchingMaxMessages = params.get("BatchingMaxMessages")
        self.BatchingMaxPublishDelay = params.get("BatchingMaxPublishDelay")
        self.BatchingMaxBytes = params.get("BatchingMaxBytes")


class SendBatchMessagesResponse(AbstractModel):
    """SendBatchMessages返回参数结构体

    """

    def __init__(self):
        """
        :param MessageId: 消息的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: str
        :param ErrorMsg: 错误消息，返回为 ""，代表没有错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MessageId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class SendCmqMsgRequest(AbstractModel):
    """SendCmqMsg请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名
        :type QueueName: str
        :param MsgContent: 消息内容
        :type MsgContent: str
        :param DelaySeconds: 延迟时间
        :type DelaySeconds: int
        """
        self.QueueName = None
        self.MsgContent = None
        self.DelaySeconds = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MsgContent = params.get("MsgContent")
        self.DelaySeconds = params.get("DelaySeconds")


class SendCmqMsgResponse(AbstractModel):
    """SendCmqMsg返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true表示发送成功
        :type Result: bool
        :param MsgId: 消息id
        :type MsgId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.MsgId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.MsgId = params.get("MsgId")
        self.RequestId = params.get("RequestId")


class SendMessagesRequest(AbstractModel):
    """SendMessages请求参数结构体

    """

    def __init__(self):
        """
        :param StringToken: Token 是用来做鉴权使用的
        :type StringToken: str
        :param Topic: 消息要发送的topic的名字
        :type Topic: str
        :param Payload: 要发送的消息的内容
        :type Payload: str
        :param ProducerName: 设置 producer 的名字，要求全局唯一，用户不配置，系统会随机生成
        :type ProducerName: str
        :param SendTimeout: 设置消息发送的超时时间，默认为30s
        :type SendTimeout: int
        :param MaxPendingMessages: 内存中缓存的最大的生产消息的数量，默认为1000条
        :type MaxPendingMessages: int
        """
        self.StringToken = None
        self.Topic = None
        self.Payload = None
        self.ProducerName = None
        self.SendTimeout = None
        self.MaxPendingMessages = None


    def _deserialize(self, params):
        self.StringToken = params.get("StringToken")
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.ProducerName = params.get("ProducerName")
        self.SendTimeout = params.get("SendTimeout")
        self.MaxPendingMessages = params.get("MaxPendingMessages")


class SendMessagesResponse(AbstractModel):
    """SendMessages返回参数结构体

    """

    def __init__(self):
        """
        :param MessageId: 消息的messageID, 是全局唯一的，用来标识消息的元数据信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: str
        :param ErrorMsg: 返回的错误消息，如果返回为 “”，说明没有错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MessageId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.ErrorMsg = params.get("ErrorMsg")
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


class Tag(AbstractModel):
    """标签的key/value的类型

    """

    def __init__(self):
        """
        :param TagKey: 标签的key的值
        :type TagKey: str
        :param TagValue: 标签的Value的值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


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
        :param ProducerLimit: 生产者上限。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerLimit: str
        :param ConsumerLimit: 消费者上限。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLimit: str
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
        self.ProducerLimit = None
        self.ConsumerLimit = None


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
        self.ProducerLimit = params.get("ProducerLimit")
        self.ConsumerLimit = params.get("ConsumerLimit")


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


class UnbindCmqDeadLetterRequest(AbstractModel):
    """UnbindCmqDeadLetter请求参数结构体

    """

    def __init__(self):
        """
        :param SourceQueueName: 死信策略源队列名称，调用本接口会清空该队列的死信队列策略。
        :type SourceQueueName: str
        """
        self.SourceQueueName = None


    def _deserialize(self, params):
        self.SourceQueueName = params.get("SourceQueueName")


class UnbindCmqDeadLetterResponse(AbstractModel):
    """UnbindCmqDeadLetter返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VpcBindRecord(AbstractModel):
    """vcp绑定记录

    """

    def __init__(self):
        """
        :param UniqueVpcId: 租户Vpc Id
        :type UniqueVpcId: str
        :param UniqueSubnetId: 租户Vpc子网Id
        :type UniqueSubnetId: str
        :param RouterId: 路由Id
        :type RouterId: str
        :param Ip: Vpc的Id
        :type Ip: str
        :param Port: Vpc的Port
        :type Port: int
        :param Remark: 说明，128个字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.RouterId = None
        self.Ip = None
        self.Port = None
        self.Remark = None


    def _deserialize(self, params):
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.RouterId = params.get("RouterId")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Remark = params.get("Remark")