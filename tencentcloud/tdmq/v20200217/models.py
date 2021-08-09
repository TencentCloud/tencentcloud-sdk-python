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


class AcknowledgeMessageRequest(AbstractModel):
    """AcknowledgeMessage请求参数结构体

    """

    def __init__(self):
        """
        :param MessageId: 用作标识消息的唯一的ID（可从 receiveMessage 的返回值中获得）\n        :type MessageId: str\n        :param AckTopic: Topic 名字（可从 receiveMessage 的返回值中获得）这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default\n        :type AckTopic: str\n        :param SubName: 订阅者的名字，可以从receiveMessage的返回值中获取到。这里尽量与receiveMessage中的订阅者保持一致，否则没办法正确ack 接收回来的消息。\n        :type SubName: str\n        """
        self.MessageId = None
        self.AckTopic = None
        self.SubName = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.AckTopic = params.get("AckTopic")
        self.SubName = params.get("SubName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcknowledgeMessageResponse(AbstractModel):
    """AcknowledgeMessage返回参数结构体

    """

    def __init__(self):
        """
        :param ErrorMsg: 如果为“”，则说明没有错误返回
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class BindCluster(AbstractModel):
    """用户专享集群信息

    """

    def __init__(self):
        """
        :param ClusterName: 物理集群的名称\n        :type ClusterName: str\n        """
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BundleSetOpt(AbstractModel):
    """运营端命名空间bundle实体

    """


class ClearCmqQueueRequest(AbstractModel):
    """ClearCmqQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearCmqQueueResponse(AbstractModel):
    """ClearCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearCmqSubscriptionFilterTagsRequest(AbstractModel):
    """ClearCmqSubscriptionFilterTags请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearCmqSubscriptionFilterTagsResponse(AbstractModel):
    """ClearCmqSubscriptionFilterTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """集群信息集合

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id。\n        :type ClusterId: str\n        :param ClusterName: 集群名称。\n        :type ClusterName: str\n        :param Remark: 说明信息。\n        :type Remark: str\n        :param EndPointNum: 接入点数量\n        :type EndPointNum: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param Healthy: 集群是否健康，1表示健康，0表示异常\n        :type Healthy: int\n        :param HealthyInfo: 集群健康信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthyInfo: str\n        :param Status: 集群状态，0:创建中，1:正常，2:删除中，3:已删除，5:创建失败，6: 删除失败\n        :type Status: int\n        :param MaxNamespaceNum: 最大命名空间数量\n        :type MaxNamespaceNum: int\n        :param MaxTopicNum: 最大Topic数量\n        :type MaxTopicNum: int\n        :param MaxQps: 最大QPS\n        :type MaxQps: int\n        :param MessageRetentionTime: 消息保留时间\n        :type MessageRetentionTime: int\n        :param MaxStorageCapacity: 最大存储容量\n        :type MaxStorageCapacity: int\n        :param Version: 集群版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: str\n        :param PublicEndPoint: 公网访问接入点
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicEndPoint: str\n        :param VpcEndPoint: VPC访问接入点
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcEndPoint: str\n        :param NamespaceNum: 命名空间数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceNum: int\n        """
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
        self.Version = None
        self.PublicEndPoint = None
        self.VpcEndPoint = None
        self.NamespaceNum = None


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
        self.Version = params.get("Version")
        self.PublicEndPoint = params.get("PublicEndPoint")
        self.VpcEndPoint = params.get("VpcEndPoint")
        self.NamespaceNum = params.get("NamespaceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqDeadLetterPolicy(AbstractModel):
    """cmq DeadLetterPolicy

    """

    def __init__(self):
        """
        :param DeadLetterQueue: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeadLetterQueue: str\n        :param Policy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Policy: int\n        :param MaxTimeToLive: 最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxTimeToLive: int\n        :param MaxReceiveCount: 最大接收次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxReceiveCount: int\n        """
        self.DeadLetterQueue = None
        self.Policy = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None


    def _deserialize(self, params):
        self.DeadLetterQueue = params.get("DeadLetterQueue")
        self.Policy = params.get("Policy")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqDeadLetterSource(AbstractModel):
    """Cmq DeadLetterSource

    """

    def __init__(self):
        """
        :param QueueId: 消息队列ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueueId: str\n        :param QueueName: 消息队列名字。
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueueName: str\n        """
        self.QueueId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqQueue(AbstractModel):
    """cmq 批量queue属性信息

    """

    def __init__(self):
        """
        :param QueueId: 消息队列ID。\n        :type QueueId: str\n        :param QueueName: 消息队列名字。\n        :type QueueName: str\n        :param Qps: 每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Qps: int\n        :param Bps: 带宽限制。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bps: int\n        :param MaxDelaySeconds: 飞行消息最大保留时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxDelaySeconds: int\n        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PollingWaitSeconds: int\n        :param MsgRetentionSeconds: 消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRetentionSeconds: int\n        :param VisibilityTimeout: 消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: 消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxMsgSize: int\n        :param RewindSeconds: 回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RewindSeconds: int\n        :param CreateTime: 队列的创建时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param LastModifyTime: 最后一次修改队列属性的时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTime: int\n        :param ActiveMsgNum: 在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActiveMsgNum: int\n        :param InactiveMsgNum: 在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InactiveMsgNum: int\n        :param DelayMsgNum: 延迟消息数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DelayMsgNum: int\n        :param RewindMsgNum: 已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RewindMsgNum: int\n        :param MinMsgTime: 消息最小未消费时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinMsgTime: int\n        :param Transaction: 事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Transaction: bool\n        :param DeadLetterSource: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeadLetterSource: list of CmqDeadLetterSource\n        :param DeadLetterPolicy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeadLetterPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqDeadLetterPolicy`\n        :param TransactionPolicy: 事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqTransactionPolicy`\n        :param CreateUin: 创建者Uin。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUin: int\n        :param Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Trace: bool\n        :param TenantId: 租户id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TenantId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqSubscription(AbstractModel):
    """cmq订阅返回参数

    """

    def __init__(self):
        """
        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubscriptionName: str\n        :param SubscriptionId: 订阅 ID。订阅 ID 在拉取监控数据时会用到。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubscriptionId: str\n        :param TopicOwner: 订阅拥有者的 APPID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicOwner: int\n        :param MsgCount: 该订阅待投递的消息数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgCount: int\n        :param LastModifyTime: 最后一次修改订阅属性的时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTime: int\n        :param CreateTime: 订阅的创建时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param BindingKey: 表示订阅接收消息的过滤策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindingKey: list of str\n        :param Endpoint: 接收通知的 endpoint，根据协议 protocol 区分：对于 HTTP，endpoint 必须以http://开头，host 可以是域名或 IP；对于 queue，则填 queueName。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Endpoint: str\n        :param FilterTags: 描述用户创建订阅时选择的过滤策略：
filterType = 1表示用户使用 filterTag 标签过滤
filterType = 2表示用户使用 bindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterTags: list of str\n        :param Protocol: 订阅的协议，目前支持两种协议：HTTP、queue。使用 HTTP 协议，用户需自己搭建接受消息的 Web Server。使用 queue，消息会自动推送到 CMQ queue，用户可以并发地拉取消息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param NotifyStrategy: 向 endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值有：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始 1s，后面是 2s，4s，8s...由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotifyStrategy: str\n        :param NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 protocol 是 queue，则取值必须为 SIMPLIFIED。如果 protocol 是 HTTP，两个值均可以，默认值是 JSON。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotifyContentFormat: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqTopic(AbstractModel):
    """cmq topic返回信息展示字段

    """

    def __init__(self):
        """
        :param TopicId: 主题的 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicId: str\n        :param TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicName: str\n        :param MsgRetentionSeconds: 消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRetentionSeconds: int\n        :param MaxMsgSize: 消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为65536。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxMsgSize: int\n        :param Qps: 每秒钟发布消息的条数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Qps: int\n        :param FilterType: 描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterType: int\n        :param CreateTime: 主题的创建时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param LastModifyTime: 最后一次修改主题属性的时间。返回 Unix 时间戳，精确到毫秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTime: int\n        :param MsgCount: 当前该主题中消息数目（消息堆积数）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgCount: int\n        :param CreateUin: 创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUin: int\n        :param Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Trace: bool\n        :param TenantId: 租户id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TenantId: str\n        :param NamespaceName: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqTransactionPolicy(AbstractModel):
    """cmq TransactionPolicy

    """

    def __init__(self):
        """
        :param FirstQueryInterval: 第一次回查时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: 最大查询次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxQueryCount: int\n        """
        self.FirstQueryInterval = None
        self.MaxQueryCount = None


    def _deserialize(self, params):
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Connection(AbstractModel):
    """生产者连接实例

    """

    def __init__(self):
        """
        :param Address: 生产者地址。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Address: str\n        :param Partitions: 主题分区。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partitions: int\n        :param ClientVersion: 生产者版本。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientVersion: str\n        :param ProducerName: 生产者名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProducerName: str\n        :param ProducerId: 生产者ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProducerId: str\n        :param AverageMsgSize: 消息平均大小(byte)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AverageMsgSize: str\n        :param MsgThroughputIn: 生成速率(byte/秒)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgThroughputIn: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Consumer(AbstractModel):
    """消费者

    """

    def __init__(self):
        """
        :param ConnectedSince: 消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConnectedSince: str\n        :param ConsumerAddr: 消费者地址。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerAddr: str\n        :param ConsumerName: 消费者名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerName: str\n        :param ClientVersion: 消费者版本。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientVersion: str\n        """
        self.ConnectedSince = None
        self.ConsumerAddr = None
        self.ConsumerName = None
        self.ClientVersion = None


    def _deserialize(self, params):
        self.ConnectedSince = params.get("ConnectedSince")
        self.ConsumerAddr = params.get("ConsumerAddr")
        self.ConsumerName = params.get("ConsumerName")
        self.ClientVersion = params.get("ClientVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumersSchedule(AbstractModel):
    """消费进度详情

    """

    def __init__(self):
        """
        :param Partitions: 当前分区id。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partitions: int\n        :param NumberOfEntries: 消息数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NumberOfEntries: int\n        :param MsgBacklog: 消息积压数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgBacklog: int\n        :param MsgRateOut: 消费者每秒分发消息的数量之和。\n        :type MsgRateOut: str\n        :param MsgThroughputOut: 消费者每秒消息的byte。\n        :type MsgThroughputOut: str\n        :param MsgRateExpired: 超时丢弃比例。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRateExpired: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterName: 集群名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。\n        :type ClusterName: str\n        :param BindClusterId: 用户专享物理集群ID，如果不传，则默认在公共集群上创建用户集群资源。\n        :type BindClusterId: int\n        :param Remark: 说明，128个字符以内。\n        :type Remark: str\n        :param Tags: 集群的标签列表\n        :type Tags: list of Tag\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。\n        :type PollingWaitSeconds: int\n        :param VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。\n        :type MsgRetentionSeconds: int\n        :param RewindSeconds: 队列是否开启回溯消息能力，该参数取值范围0-msgRetentionSeconds,即最大的回溯时间为消息在队列中的保留周期，0表示不开启。\n        :type RewindSeconds: int\n        :param Transaction: 1 表示事务队列，0 表示普通队列\n        :type Transaction: int\n        :param FirstQueryInterval: 第一次回查间隔\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: 最大回查次数\n        :type MaxQueryCount: int\n        :param DeadLetterQueueName: 死信队列名称\n        :type DeadLetterQueueName: str\n        :param Policy: 死信策略。0为消息被多次消费未删除，1为Time-To-Live过期\n        :type Policy: int\n        :param MaxReceiveCount: 最大接收次数 1-1000\n        :type MaxReceiveCount: int\n        :param MaxTimeToLive: policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds\n        :type MaxTimeToLive: int\n        :param Trace: 是否开启消息轨迹追踪，当不设置字段时，默认为不开启，该字段为true表示开启，为false表示不开启\n        :type Trace: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqQueueResponse(AbstractModel):
    """CreateCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param QueueId: 创建成功的queueId\n        :type QueueId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        :param Protocol: 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。\n        :type Protocol: str\n        :param Endpoint: 接收通知的Endpoint，根据协议Protocol区分：对于http，Endpoint必须以“`http://`”开头，host可以是域名或IP；对于Queue，则填QueueName。 请注意，目前推送服务不能推送到私有网络中，因此Endpoint填写为私有网络域名或地址将接收不到推送的消息，目前支持推送到公网和基础网络。\n        :type Endpoint: str\n        :param NotifyStrategy: 向Endpoint推送消息出现错误时，CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s...由于Topic消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是EXPONENTIAL_DECAY_RETRY。\n        :type NotifyStrategy: str\n        :param FilterTag: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。\n        :type FilterTag: list of str\n        :param BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。\n        :type BindingKey: list of str\n        :param NotifyContentFormat: 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，则取值必须为SIMPLIFIED。如果Protocol是http，两个值均可以，默认值是JSON。\n        :type NotifyContentFormat: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqSubscribeResponse(AbstractModel):
    """CreateCmqSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionId: 订阅id\n        :type SubscriptionId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。\n        :type MaxMsgSize: int\n        :param FilterType: 用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略，默认值为标签匹配策略。\n        :type FilterType: int\n        :param MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。\n        :type MsgRetentionSeconds: int\n        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。\n        :type Trace: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqTopicResponse(AbstractModel):
    """CreateCmqTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 主题id\n        :type TopicId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。\n        :type EnvironmentId: str\n        :param MsgTTL: 未消费消息过期时间，单位：秒，最小60，最大1296000，（15天）。\n        :type MsgTTL: int\n        :param Remark: 说明，128个字符以内。\n        :type Remark: str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param MsgTTL: 未消费消息过期时间，单位：秒。\n        :type MsgTTL: int\n        :param Remark: 说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称。\n        :type TopicName: str\n        :param SubscriptionName: 订阅者名称，不支持中字以及除了短线和下划线外的特殊字符且不超过150个字符。\n        :type SubscriptionName: str\n        :param IsIdempotent: 是否幂等创建，若否不允许创建同名的订阅关系。\n        :type IsIdempotent: bool\n        :param Remark: 备注，128个字符以内。\n        :type Remark: str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        :param AutoCreatePolicyTopic: 是否自动创建死信和重试主题，True 表示创建，False表示不创建，默认自动创建死信和重试主题。\n        :type AutoCreatePolicyTopic: bool\n        :param PostFixPattern: 指定死信和重试主题名称规范，LEGACY表示历史命名规则，COMMUNITY表示Pulsar社区命名规范\n        :type PostFixPattern: str\n        """
        self.EnvironmentId = None
        self.TopicName = None
        self.SubscriptionName = None
        self.IsIdempotent = None
        self.Remark = None
        self.ClusterId = None
        self.AutoCreatePolicyTopic = None
        self.PostFixPattern = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.IsIdempotent = params.get("IsIdempotent")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        self.AutoCreatePolicyTopic = params.get("AutoCreatePolicyTopic")
        self.PostFixPattern = params.get("PostFixPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscriptionResponse(AbstractModel):
    """CreateSubscription返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。\n        :type TopicName: str\n        :param Partitions: 0：非分区topic，无分区；非0：具体分区topic的分区数，最大不允许超过128。\n        :type Partitions: int\n        :param TopicType: 0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列。\n        :type TopicType: int\n        :param Remark: 备注，128字符以内。\n        :type Remark: str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名。\n        :type TopicName: str\n        :param Partitions: 0：非分区topic，无分区；非0：具体分区topic的分区数。\n        :type Partitions: int\n        :param Remark: 备注，128字符以内。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param TopicType: 0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列；
5 ：事务消息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicType: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ClusterId: 集群Id，传入需要删除的集群Id。\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群的ID\n        :type ClusterId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCmqQueueResponse(AbstractModel):
    """DeleteCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCmqSubscribeRequest(AbstractModel):
    """DeleteCmqSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCmqSubscribeResponse(AbstractModel):
    """DeleteCmqSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCmqTopicRequest(AbstractModel):
    """DeleteCmqTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type TopicName: str\n        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCmqTopicResponse(AbstractModel):
    """DeleteCmqTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEnvironmentsRequest(AbstractModel):
    """DeleteEnvironments请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentIds: 环境（命名空间）数组，每次最多删除20个。\n        :type EnvironmentIds: list of str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
        self.EnvironmentIds = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentsResponse(AbstractModel):
    """DeleteEnvironments返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentIds: 成功删除的环境（命名空间）数组。\n        :type EnvironmentIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SubscriptionTopicSets: 订阅关系集合，每次最多删除20个。\n        :type SubscriptionTopicSets: list of SubscriptionTopic\n        :param ClusterId: pulsar集群Id。\n        :type ClusterId: str\n        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubscriptionsResponse(AbstractModel):
    """DeleteSubscriptions返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionTopicSets: 成功删除的订阅关系数组。\n        :type SubscriptionTopicSets: list of SubscriptionTopic\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TopicSets: 主题集合，每次最多删除20个。\n        :type TopicSets: list of TopicRecord\n        :param ClusterId: pulsar集群Id。\n        :type ClusterId: str\n        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicsResponse(AbstractModel):
    """DeleteTopics返回参数结构体

    """

    def __init__(self):
        """
        :param TopicSets: 被删除的主题数组。\n        :type TopicSets: list of TopicRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TotalCount: 专享集群的数量\n        :type TotalCount: int\n        :param ClusterSet: 专享集群的列表\n        :type ClusterSet: list of BindCluster\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 起始下标，不填默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为20。\n        :type Limit: int\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
        self.Offset = None
        self.Limit = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindVpcsResponse(AbstractModel):
    """DescribeBindVpcs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录数。\n        :type TotalCount: int\n        :param VpcSets: Vpc集合。\n        :type VpcSets: list of VpcBindRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ClusterId: 集群的ID\n        :type ClusterId: str\n        """
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
        :param ClusterSet: 集群的详细信息\n        :type ClusterSet: :class:`tencentcloud.tdmq.v20200217.models.Cluster`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 起始下标，不填默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为20。\n        :type Limit: int\n        """
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
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群列表数量\n        :type TotalCount: int\n        :param ClusterSet: 集群信息列表\n        :type ClusterSet: list of Cluster\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param DeadLetterQueueName: 死信队列名称\n        :type DeadLetterQueueName: str\n        :param Limit: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。\n        :type Limit: int\n        :param Offset: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Offset: int\n        :param SourceQueueName: 根据SourceQueueName过滤\n        :type SourceQueueName: str\n        """
        self.DeadLetterQueueName = None
        self.Limit = None
        self.Offset = None
        self.SourceQueueName = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceQueueName = params.get("SourceQueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeCmqDeadLetterSourceQueues返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 满足本次条件的队列个数\n        :type TotalCount: int\n        :param QueueSet: 死信队列源队列\n        :type QueueSet: list of CmqDeadLetterSource\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param QueueName: 精确匹配QueueName\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqQueueDetailResponse(AbstractModel):
    """DescribeCmqQueueDetail返回参数结构体

    """

    def __init__(self):
        """
        :param QueueDescribe: 队列详情列表。\n        :type QueueDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqQueue`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0\n        :type Offset: int\n        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Limit: int\n        :param QueueName: 根据QueueName进行过滤\n        :type QueueName: str\n        """
        self.Offset = None
        self.Limit = None
        self.QueueName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqQueuesResponse(AbstractModel):
    """DescribeCmqQueues返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 数量\n        :type TotalCount: int\n        :param QueueList: 队列列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueueList: list of CmqQueue\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param Offset: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0\n        :type Offset: int\n        :param Limit: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Limit: int\n        :param SubscriptionName: 根据SubscriptionName进行模糊搜索\n        :type SubscriptionName: str\n        """
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqSubscriptionDetailResponse(AbstractModel):
    """DescribeCmqSubscriptionDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数\n        :type TotalCount: int\n        :param SubscriptionSet: Subscription属性集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubscriptionSet: list of CmqSubscription\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TopicName: 精确匹配TopicName。\n        :type TopicName: str\n        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqTopicDetailResponse(AbstractModel):
    """DescribeCmqTopicDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TopicDescribe: 主题详情\n        :type TopicDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqTopic`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0\n        :type Offset: int\n        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Limit: int\n        :param TopicName: 根据TopicName进行模糊搜索\n        :type TopicName: str\n        """
        self.Offset = None
        self.Limit = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqTopicsResponse(AbstractModel):
    """DescribeCmqTopics返回参数结构体

    """

    def __init__(self):
        """
        :param TopicList: 主题列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicList: list of CmqTopic\n        :param TotalCount: 全量主题数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
        self.EnvironmentId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentAttributesResponse(AbstractModel):
    """DescribeEnvironmentAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000（15天）。\n        :type MsgTTL: int\n        :param RateInByte: 消费速率限制，单位：byte/秒，0：不限速。\n        :type RateInByte: int\n        :param RateInSize: 消费速率限制，单位：个数/秒，0：不限速。\n        :type RateInSize: int\n        :param RetentionHours: 已消费消息保存策略，单位：小时，0：消费完马上删除。\n        :type RetentionHours: int\n        :param RetentionSize: 已消费消息保存策略，单位：G，0：消费完马上删除。\n        :type RetentionSize: int\n        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param Replicas: 副本数。\n        :type Replicas: int\n        :param Remark: 备注。\n        :type Remark: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param Offset: 起始下标，不填默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为20。\n        :type Limit: int\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        :param RoleName: 角色名称\n        :type RoleName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentRolesResponse(AbstractModel):
    """DescribeEnvironmentRoles返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录数。\n        :type TotalCount: int\n        :param EnvironmentRoleSets: 命名空间角色集合。\n        :type EnvironmentRoleSets: list of EnvironmentRole\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 命名空间名称，模糊搜索。\n        :type EnvironmentId: str\n        :param Offset: 起始下标，不填默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为20。\n        :type Limit: int\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        :param Filters: * EnvironmentId
按照名称空间进行过滤，精确查询。
类型：String
必选：否\n        :type Filters: list of Filter\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 命名空间记录数。\n        :type TotalCount: int\n        :param EnvironmentSet: 命名空间集合数组。\n        :type EnvironmentSet: list of Environment\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeNamespaceBundlesOptRequest(AbstractModel):
    """DescribeNamespaceBundlesOpt请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterName: 物理集群名\n        :type ClusterName: str\n        :param TenantId: 虚拟集群（租户）ID\n        :type TenantId: str\n        :param NamespaceName: 命名空间名\n        :type NamespaceName: str\n        :param NeedMetrics: 是否需要监控指标，若传false，则不需要传Limit和Offset分页参数\n        :type NeedMetrics: bool\n        :param Limit: 查询限制条数\n        :type Limit: int\n        :param Offset: 查询偏移量\n        :type Offset: int\n        """
        self.ClusterName = None
        self.TenantId = None
        self.NamespaceName = None
        self.NeedMetrics = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.TenantId = params.get("TenantId")
        self.NamespaceName = params.get("NamespaceName")
        self.NeedMetrics = params.get("NeedMetrics")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespaceBundlesOptResponse(AbstractModel):
    """DescribeNamespaceBundlesOpt返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录条数\n        :type TotalCount: int\n        :param BundleSet: bundle列表\n        :type BundleSet: list of BundleSetOpt\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.BundleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BundleSet") is not None:
            self.BundleSet = []
            for item in params.get("BundleSet"):
                obj = BundleSetOpt()
                obj._deserialize(item)
                self.BundleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNodeHealthOptRequest(AbstractModel):
    """DescribeNodeHealthOpt请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 节点实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodeHealthOptResponse(AbstractModel):
    """DescribeNodeHealthOpt返回参数结构体

    """

    def __init__(self):
        """
        :param NodeState: 0-异常；1-正常\n        :type NodeState: int\n        :param LatestHealthCheckTime: 最近一次健康检查的时间\n        :type LatestHealthCheckTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NodeState = None
        self.LatestHealthCheckTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeState = params.get("NodeState")
        self.LatestHealthCheckTime = params.get("LatestHealthCheckTime")
        self.RequestId = params.get("RequestId")


class DescribeProducersRequest(AbstractModel):
    """DescribeProducers请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名。\n        :type TopicName: str\n        :param Offset: 起始下标，不填默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为20。\n        :type Limit: int\n        :param ProducerName: 生产者名称，模糊匹配。\n        :type ProducerName: str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProducersResponse(AbstractModel):
    """DescribeProducers返回参数结构体

    """

    def __init__(self):
        """
        :param ProducerSets: 生产者集合数组。\n        :type ProducerSets: list of Producer\n        :param TotalCount: 记录总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称。\n        :type TopicName: str\n        :param Offset: 起始下标，不填默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为20。\n        :type Limit: int\n        :param SubscriptionName: 订阅者名称，模糊匹配。\n        :type SubscriptionName: str\n        :param Filters: 数据过滤条件。\n        :type Filters: list of FilterSubscription\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionsResponse(AbstractModel):
    """DescribeSubscriptions返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionSets: 订阅者集合数组。\n        :type SubscriptionSets: list of Subscription\n        :param TotalCount: 数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名模糊匹配。\n        :type TopicName: str\n        :param Offset: 起始下标，不填默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，不填则默认为10，最大值为20。\n        :type Limit: int\n        :param TopicType: topic类型描述：
0：普通消息；
1：全局顺序消息；
2：局部顺序消息；
3：重试队列；
4：死信队列；
5：事务消息。\n        :type TopicType: int\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        :param Filters: * TopicName
按照主题名字查询，精确查询。
类型：String
必选：否\n        :type Filters: list of Filter\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics返回参数结构体

    """

    def __init__(self):
        """
        :param TopicSets: 主题集合数组。\n        :type TopicSets: list of Topic\n        :param TotalCount: 主题数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 命名空间名称\n        :type EnvironmentId: str\n        :param Remark: 说明\n        :type Remark: str\n        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000（15天）\n        :type MsgTTL: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 最近修改时间\n        :type UpdateTime: str\n        :param NamespaceId: 命名空间ID\n        :type NamespaceId: str\n        :param NamespaceName: 命名空间名称\n        :type NamespaceName: str\n        :param TopicNum: Topic数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicNum: int\n        """
        self.EnvironmentId = None
        self.Remark = None
        self.MsgTTL = None
        self.CreateTime = None
        self.UpdateTime = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.TopicNum = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Remark = params.get("Remark")
        self.MsgTTL = params.get("MsgTTL")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.TopicNum = params.get("TopicNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentRole(AbstractModel):
    """环境角色集合

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）。\n        :type EnvironmentId: str\n        :param RoleName: 角色名称。\n        :type RoleName: str\n        :param Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。\n        :type Permissions: list of str\n        :param RoleDescribe: 角色描述。\n        :type RoleDescribe: str\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间。\n        :type UpdateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤参数

    """

    def __init__(self):
        """
        :param Name: 过滤参数的名字\n        :type Name: str\n        :param Values: 数值\n        :type Values: list of str\n        """
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
        


class FilterSubscription(AbstractModel):
    """过滤订阅列表

    """

    def __init__(self):
        """
        :param ConsumerHasCount: 是否仅展示包含真实消费者的订阅。\n        :type ConsumerHasCount: bool\n        :param ConsumerHasBacklog: 是否仅展示消息堆积的订阅。\n        :type ConsumerHasBacklog: bool\n        :param ConsumerHasExpired: 是否仅展示存在消息超期丢弃的订阅。\n        :type ConsumerHasExpired: bool\n        :param SubscriptionNames: 按照订阅名过滤，精确查询。\n        :type SubscriptionNames: list of str\n        """
        self.ConsumerHasCount = None
        self.ConsumerHasBacklog = None
        self.ConsumerHasExpired = None
        self.SubscriptionNames = None


    def _deserialize(self, params):
        self.ConsumerHasCount = params.get("ConsumerHasCount")
        self.ConsumerHasBacklog = params.get("ConsumerHasBacklog")
        self.ConsumerHasExpired = params.get("ConsumerHasExpired")
        self.SubscriptionNames = params.get("SubscriptionNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterRequest(AbstractModel):
    """ModifyCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: Pulsar 集群的ID，需要更新的集群Id。\n        :type ClusterId: str\n        :param ClusterName: 更新后的集群名称。\n        :type ClusterName: str\n        :param Remark: 说明信息。\n        :type Remark: str\n        """
        self.ClusterId = None
        self.ClusterName = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterResponse(AbstractModel):
    """ModifyCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。\n        :type PollingWaitSeconds: int\n        :param VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。\n        :type MsgRetentionSeconds: int\n        :param RewindSeconds: 消息最长回溯时间，取值范围0-msgRetentionSeconds，消息的最大回溯之间为消息在队列中的保存周期，0表示不开启消息回溯。\n        :type RewindSeconds: int\n        :param FirstQueryInterval: 第一次查询时间\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: 最大查询次数\n        :type MaxQueryCount: int\n        :param DeadLetterQueueName: 死信队列名称\n        :type DeadLetterQueueName: str\n        :param MaxTimeToLive: MaxTimeToLivepolicy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds\n        :type MaxTimeToLive: int\n        :param MaxReceiveCount: 最大接收次数\n        :type MaxReceiveCount: int\n        :param Policy: 死信队列策略\n        :type Policy: int\n        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。\n        :type Trace: bool\n        :param Transaction: 是否开启事务，1开启，0不开启\n        :type Transaction: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCmqQueueAttributeResponse(AbstractModel):
    """ModifyCmqQueueAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCmqSubscriptionAttributeRequest(AbstractModel):
    """ModifyCmqSubscriptionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        :param NotifyStrategy: 向 Endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值如下：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息。
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s···由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。\n        :type NotifyStrategy: str\n        :param NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 Protocol 是 queue，则取值必须为 SIMPLIFIED。如果 Protocol 是 HTTP，两个值均可以，默认值是 JSON。\n        :type NotifyContentFormat: str\n        :param FilterTags: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。\n        :type FilterTags: list of str\n        :param BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。\n        :type BindingKey: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCmqSubscriptionAttributeResponse(AbstractModel):
    """ModifyCmqSubscriptionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCmqTopicAttributeRequest(AbstractModel):
    """ModifyCmqTopicAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type TopicName: str\n        :param MaxMsgSize: 消息最大长度。取值范围1024 - 65536 Byte（即1 - 64K），默认值65536。\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。\n        :type MsgRetentionSeconds: int\n        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。\n        :type Trace: bool\n        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCmqTopicAttributeResponse(AbstractModel):
    """ModifyCmqTopicAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEnvironmentAttributesRequest(AbstractModel):
    """ModifyEnvironmentAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 命名空间名称。\n        :type EnvironmentId: str\n        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000。\n        :type MsgTTL: int\n        :param Remark: 备注，字符串最长不超过128。\n        :type Remark: str\n        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentAttributesResponse(AbstractModel):
    """ModifyEnvironmentAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 命名空间名称。\n        :type EnvironmentId: str\n        :param MsgTTL: 未消费消息过期时间，单位：秒。\n        :type MsgTTL: int\n        :param Remark: 备注，字符串最长不超过128。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NamespaceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名。\n        :type TopicName: str\n        :param Partitions: 分区数，必须大于或者等于原分区数，若想维持原分区数请输入原数目，修改分区数仅对非全局顺序消息起效果，不允许超过128个分区。\n        :type Partitions: int\n        :param Remark: 备注，128字符以内。\n        :type Remark: str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Partitions: 分区数\n        :type Partitions: int\n        :param Remark: 备注，128字符以内。\n        :type Remark: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type AverageMsgSize: str\n        :param ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerCount: str\n        :param LastConfirmedEntry: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastConfirmedEntry: str\n        :param LastLedgerCreatedTimestamp: 最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastLedgerCreatedTimestamp: str\n        :param MsgRateIn: 本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRateIn: str\n        :param MsgRateOut: 本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRateOut: str\n        :param MsgThroughputIn: 本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgThroughputIn: str\n        :param MsgThroughputOut: 本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgThroughputOut: str\n        :param NumberOfEntries: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NumberOfEntries: str\n        :param Partitions: 子分区id。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partitions: int\n        :param ProducerCount: 生产者数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProducerCount: str\n        :param TotalSize: 以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalSize: str\n        :param TopicType: topic类型描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Producer(AbstractModel):
    """生产者

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称。\n        :type TopicName: str\n        :param CountConnect: 连接数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CountConnect: int\n        :param ConnectionSets: 连接集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConnectionSets: list of Connection\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCmqMsgRequest(AbstractModel):
    """PublishCmqMsg请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名\n        :type TopicName: str\n        :param MsgContent: 消息内容\n        :type MsgContent: str\n        :param MsgTag: 消息标签\n        :type MsgTag: list of str\n        """
        self.TopicName = None
        self.MsgContent = None
        self.MsgTag = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MsgContent = params.get("MsgContent")
        self.MsgTag = params.get("MsgTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCmqMsgResponse(AbstractModel):
    """PublishCmqMsg返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true表示发送成功\n        :type Result: bool\n        :param MsgId: 消息id\n        :type MsgId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.MsgId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.MsgId = params.get("MsgId")
        self.RequestId = params.get("RequestId")


class ReceiveMessageRequest(AbstractModel):
    """ReceiveMessage请求参数结构体

    """

    def __init__(self):
        """
        :param Topic: 接收消息的topic的名字, 这里尽量需要使用topic的全路径，如果不指定，即：tenant/namespace/topic。默认使用的是：public/default\n        :type Topic: str\n        :param SubscriptionName: 订阅者的名字\n        :type SubscriptionName: str\n        :param ReceiverQueueSize: 默认值为1000，consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率\n        :type ReceiverQueueSize: int\n        :param SubInitialPosition: 默认值为：Latest。用作判定consumer初始接收消息的位置，可选参数为：Earliest, Latest\n        :type SubInitialPosition: str\n        """
        self.Topic = None
        self.SubscriptionName = None
        self.ReceiverQueueSize = None
        self.SubInitialPosition = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.SubscriptionName = params.get("SubscriptionName")
        self.ReceiverQueueSize = params.get("ReceiverQueueSize")
        self.SubInitialPosition = params.get("SubInitialPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveMessageResponse(AbstractModel):
    """ReceiveMessage返回参数结构体

    """

    def __init__(self):
        """
        :param MessageID: 用作标识消息的唯一主键\n        :type MessageID: str\n        :param MessagePayload: 接收消息的内容\n        :type MessagePayload: str\n        :param AckTopic: 提供给 Ack 接口，用来Ack哪一个topic中的消息\n        :type AckTopic: str\n        :param ErrorMsg: 返回的错误信息，如果为空，说明没有错误
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMsg: str\n        :param SubName: 返回订阅者的名字，用来创建 ack consumer时使用
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MessageID = None
        self.MessagePayload = None
        self.AckTopic = None
        self.ErrorMsg = None
        self.SubName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageID = params.get("MessageID")
        self.MessagePayload = params.get("MessagePayload")
        self.AckTopic = params.get("AckTopic")
        self.ErrorMsg = params.get("ErrorMsg")
        self.SubName = params.get("SubName")
        self.RequestId = params.get("RequestId")


class ResetMsgSubOffsetByTimestampRequest(AbstractModel):
    """ResetMsgSubOffsetByTimestamp请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 命名空间名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称。\n        :type TopicName: str\n        :param Subscription: 订阅者名称。\n        :type Subscription: str\n        :param ToTimestamp: 时间戳，精确到毫秒。\n        :type ToTimestamp: int\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetMsgSubOffsetByTimestampResponse(AbstractModel):
    """ResetMsgSubOffsetByTimestamp返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        :param StartConsumeTime: 设定该时间，则（Batch）receiveMessage接口，会按照生产消息的先后顺序消费该时间戳以后的消息。\n        :type StartConsumeTime: int\n        """
        self.QueueName = None
        self.StartConsumeTime = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.StartConsumeTime = params.get("StartConsumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindCmqQueueResponse(AbstractModel):
    """RewindCmqQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendBatchMessagesRequest(AbstractModel):
    """SendBatchMessages请求参数结构体

    """

    def __init__(self):
        """
        :param Topic: 消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default\n        :type Topic: str\n        :param Payload: 需要发送消息的内容\n        :type Payload: str\n        :param StringToken: String 类型的 token，可以不填，系统会自动获取\n        :type StringToken: str\n        :param ProducerName: producer 的名字，要求全局是唯一的，如果不设置，系统会自动生成\n        :type ProducerName: str\n        :param SendTimeout: 单位：s。消息发送的超时时间。默认值为：30s\n        :type SendTimeout: int\n        :param MaxPendingMessages: 内存中允许缓存的生产消息的最大数量，默认值：1000条\n        :type MaxPendingMessages: int\n        :param BatchingMaxMessages: 每一个batch中消息的最大数量，默认值：1000条/batch\n        :type BatchingMaxMessages: int\n        :param BatchingMaxPublishDelay: 每一个batch最大等待的时间，超过这个时间，不管是否达到指定的batch中消息的数量和大小，都会将该batch发送出去，默认：10ms\n        :type BatchingMaxPublishDelay: int\n        :param BatchingMaxBytes: 每一个batch中最大允许的消息的大小，默认：128KB\n        :type BatchingMaxBytes: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesResponse(AbstractModel):
    """SendBatchMessages返回参数结构体

    """

    def __init__(self):
        """
        :param MessageId: 消息的唯一标识
注意：此字段可能返回 null，表示取不到有效值。\n        :type MessageId: str\n        :param ErrorMsg: 错误消息，返回为 ""，代表没有错误
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param QueueName: 队列名\n        :type QueueName: str\n        :param MsgContent: 消息内容\n        :type MsgContent: str\n        :param DelaySeconds: 延迟时间\n        :type DelaySeconds: int\n        """
        self.QueueName = None
        self.MsgContent = None
        self.DelaySeconds = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MsgContent = params.get("MsgContent")
        self.DelaySeconds = params.get("DelaySeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCmqMsgResponse(AbstractModel):
    """SendCmqMsg返回参数结构体

    """

    def __init__(self):
        """
        :param Result: true表示发送成功\n        :type Result: bool\n        :param MsgId: 消息id\n        :type MsgId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Topic: 消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default\n        :type Topic: str\n        :param Payload: 要发送的消息的内容\n        :type Payload: str\n        :param StringToken: Token 是用来做鉴权使用的，可以不填，系统会自动获取\n        :type StringToken: str\n        :param ProducerName: 设置 producer 的名字，要求全局唯一，用户不配置，系统会随机生成\n        :type ProducerName: str\n        :param SendTimeout: 设置消息发送的超时时间，默认为30s\n        :type SendTimeout: int\n        :param MaxPendingMessages: 内存中缓存的最大的生产消息的数量，默认为1000条\n        :type MaxPendingMessages: int\n        """
        self.Topic = None
        self.Payload = None
        self.StringToken = None
        self.ProducerName = None
        self.SendTimeout = None
        self.MaxPendingMessages = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.StringToken = params.get("StringToken")
        self.ProducerName = params.get("ProducerName")
        self.SendTimeout = params.get("SendTimeout")
        self.MaxPendingMessages = params.get("MaxPendingMessages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessagesResponse(AbstractModel):
    """SendMessages返回参数结构体

    """

    def __init__(self):
        """
        :param MessageId: 消息的messageID, 是全局唯一的，用来标识消息的元数据信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type MessageId: str\n        :param ErrorMsg: 返回的错误消息，如果返回为 “”，说明没有错误
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MessageId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class SendMsgRequest(AbstractModel):
    """SendMsg请求参数结构体

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称，如果是分区topic需要指定具体分区，如果没有指定则默认发到0分区，例如：my_topic-partition-0。\n        :type TopicName: str\n        :param MsgContent: 消息内容，不能为空且大小不得大于5242880个byte。\n        :type MsgContent: str\n        :param ClusterId: Pulsar 集群的ID\n        :type ClusterId: str\n        """
        self.EnvironmentId = None
        self.TopicName = None
        self.MsgContent = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.MsgContent = params.get("MsgContent")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMsgResponse(AbstractModel):
    """SendMsg返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """订阅者

    """

    def __init__(self):
        """
        :param TopicName: 主题名称。\n        :type TopicName: str\n        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param ConnectedSince: 消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConnectedSince: str\n        :param ConsumerAddr: 消费者地址。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerAddr: str\n        :param ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerCount: str\n        :param ConsumerName: 消费者名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerName: str\n        :param MsgBacklog: 堆积的消息数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgBacklog: str\n        :param MsgRateExpired: 于TTL，此订阅下没有被发送而是被丢弃的比例。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRateExpired: str\n        :param MsgRateOut: 消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRateOut: str\n        :param MsgThroughputOut: 消费者每秒消息的byte。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgThroughputOut: str\n        :param SubscriptionName: 订阅名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubscriptionName: str\n        :param ConsumerSets: 消费者集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerSets: list of Consumer\n        :param IsOnline: 是否在线。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsOnline: bool\n        :param ConsumersScheduleSets: 消费进度集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumersScheduleSets: list of ConsumersSchedule\n        :param Remark: 备注。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscriptionTopic(AbstractModel):
    """订阅关系

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名称。\n        :type SubscriptionName: str\n        """
        self.EnvironmentId = None
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签的key/value的类型

    """

    def __init__(self):
        """
        :param TagKey: 标签的key的值\n        :type TagKey: str\n        :param TagValue: 标签的Value的值\n        :type TagValue: str\n        """
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
    """主题实例

    """

    def __init__(self):
        """
        :param AverageMsgSize: 最后一次间隔内发布消息的平均byte大小。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AverageMsgSize: str\n        :param ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerCount: str\n        :param LastConfirmedEntry: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastConfirmedEntry: str\n        :param LastLedgerCreatedTimestamp: 最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastLedgerCreatedTimestamp: str\n        :param MsgRateIn: 本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRateIn: str\n        :param MsgRateOut: 本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRateOut: str\n        :param MsgThroughputIn: 本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgThroughputIn: str\n        :param MsgThroughputOut: 本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgThroughputOut: str\n        :param NumberOfEntries: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NumberOfEntries: str\n        :param Partitions: 分区数<=0：topic下无子分区。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Partitions: int\n        :param ProducerCount: 生产者数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProducerCount: str\n        :param TotalSize: 以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalSize: str\n        :param SubTopicSets: 分区topic里面的子分区。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubTopicSets: list of PartitionsTopic\n        :param TopicType: topic类型描述：
0：普通消息；
1：全局顺序消息；
2：局部顺序消息；
3：重试队列；
4：死信队列；
5：事务消息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicType: int\n        :param EnvironmentId: 环境（命名空间）名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicName: str\n        :param Remark: 说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param ProducerLimit: 生产者上限。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProducerLimit: str\n        :param ConsumerLimit: 消费者上限。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConsumerLimit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRecord(AbstractModel):
    """主题关键信息

    """

    def __init__(self):
        """
        :param EnvironmentId: 环境（命名空间）名称。\n        :type EnvironmentId: str\n        :param TopicName: 主题名称。\n        :type TopicName: str\n        """
        self.EnvironmentId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCmqDeadLetterRequest(AbstractModel):
    """UnbindCmqDeadLetter请求参数结构体

    """

    def __init__(self):
        """
        :param SourceQueueName: 死信策略源队列名称，调用本接口会清空该队列的死信队列策略。\n        :type SourceQueueName: str\n        """
        self.SourceQueueName = None


    def _deserialize(self, params):
        self.SourceQueueName = params.get("SourceQueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCmqDeadLetterResponse(AbstractModel):
    """UnbindCmqDeadLetter返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VpcBindRecord(AbstractModel):
    """vcp绑定记录

    """

    def __init__(self):
        """
        :param UniqueVpcId: 租户Vpc Id\n        :type UniqueVpcId: str\n        :param UniqueSubnetId: 租户Vpc子网Id\n        :type UniqueSubnetId: str\n        :param RouterId: 路由Id\n        :type RouterId: str\n        :param Ip: Vpc的Id\n        :type Ip: str\n        :param Port: Vpc的Port\n        :type Port: int\n        :param Remark: 说明，128个字符以内
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        