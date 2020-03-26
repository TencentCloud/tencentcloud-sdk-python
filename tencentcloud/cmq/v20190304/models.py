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


class ClearQueueRequest(AbstractModel):
    """ClearQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class ClearQueueResponse(AbstractModel):
    """ClearQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearSubscriptionFilterTagsRequest(AbstractModel):
    """ClearSubscriptionFilterTags请求参数结构体

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


class ClearSubscriptionFilterTagsResponse(AbstractModel):
    """ClearSubscriptionFilterTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateQueueRequest(AbstractModel):
    """CreateQueue请求参数结构体

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


class CreateQueueResponse(AbstractModel):
    """CreateQueue返回参数结构体

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


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe请求参数结构体

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


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionId: SubscriptionId
        :type SubscriptionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubscriptionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscriptionId = params.get("SubscriptionId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param FilterType: 用于指定主题的消息匹配策略。
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


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: TopicName
        :type TopicId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class DeadLetterPolicy(AbstractModel):
    """DeadLetterPolicy

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: DeadLetterQueueName
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterQueueName: str
        :param DeadLetterQueue: DeadLetterQueue
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterQueue: str
        :param Policy: Policy
注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: int
        :param MaxTimeToLive: MaxTimeToLive
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTimeToLive: int
        :param MaxReceiveCount: MaxReceiveCount
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReceiveCount: int
        """
        self.DeadLetterQueueName = None
        self.DeadLetterQueue = None
        self.Policy = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.DeadLetterQueue = params.get("DeadLetterQueue")
        self.Policy = params.get("Policy")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")


class DeadLetterSource(AbstractModel):
    """DeadLetterSource

    """

    def __init__(self):
        """
        :param QueueId: QueueId
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueId: str
        :param QueueName: QueueName
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        """
        self.QueueId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubscribeRequest(AbstractModel):
    """DeleteSubscribe请求参数结构体

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


class DeleteSubscribeResponse(AbstractModel):
    """DeleteSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeDeadLetterSourceQueues请求参数结构体

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param Limit: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。
        :type Limit: int
        :param Offset: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Offset: int
        :param Filters: 过滤死信队列源队列名称，目前仅支持SourceQueueName过滤
        :type Filters: list of Filter
        """
        self.DeadLetterQueueName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeDeadLetterSourceQueues返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 满足本次条件的队列个数
        :type TotalCount: int
        :param QueueSet: 死信队列源队列
        :type QueueSet: list of DeadLetterSource
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
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQueueDetailRequest(AbstractModel):
    """DescribeQueueDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param Filters: 筛选参数，目前支持QueueName筛选，且仅支持一个关键字
        :type Filters: list of Filter
        :param TagKey: 标签搜索
        :type TagKey: str
        :param QueueName: 精确匹配QueueName
        :type QueueName: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.QueueName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.QueueName = params.get("QueueName")


class DescribeQueueDetailResponse(AbstractModel):
    """DescribeQueueDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: queue总数量
        :type TotalCount: int
        :param QueueSet: queue列表
        :type QueueSet: list of QueueSet
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
                obj = QueueSet()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscriptionDetailRequest(AbstractModel):
    """DescribeSubscriptionDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param Offset: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param Limit: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param Filters: 筛选参数，目前只支持SubscriptionName，且仅支持一个关键字。
        :type Filters: list of Filter
        """
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeSubscriptionDetailResponse(AbstractModel):
    """DescribeSubscriptionDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param SubscriptionSet: Subscription属性集合
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionSet: list of Subscription
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
                obj = Subscription()
                obj._deserialize(item)
                self.SubscriptionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。
        :type Offset: int
        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param Filters: 目前只支持过滤TopicName ， 且只能填一个过滤值
        :type Filters: list of Filter
        :param TagKey: 标签匹配
        :type TagKey: str
        :param TopicName: 精确匹配TopicName
        :type TopicName: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.TopicName = params.get("TopicName")


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: TotalCount
        :type TotalCount: int
        :param TopicSet: TopicSet
        :type TopicSet: list of TopicSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TopicSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicSet") is not None:
            self.TopicSet = []
            for item in params.get("TopicSet"):
                obj = TopicSet()
                obj._deserialize(item)
                self.TopicSet.append(obj)
        self.RequestId = params.get("RequestId")


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


class ModifyQueueAttributeRequest(AbstractModel):
    """ModifyQueueAttribute请求参数结构体

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


class ModifyQueueAttributeResponse(AbstractModel):
    """ModifyQueueAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscriptionAttributeRequest(AbstractModel):
    """ModifySubscriptionAttribute请求参数结构体

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


class ModifySubscriptionAttributeResponse(AbstractModel):
    """ModifySubscriptionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributeRequest(AbstractModel):
    """ModifyTopicAttribute请求参数结构体

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


class ModifyTopicAttributeResponse(AbstractModel):
    """ModifyTopicAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QueueSet(AbstractModel):
    """批量queue属性信息

    """

    def __init__(self):
        """
        :param QueueId: QueueId
        :type QueueId: str
        :param QueueName: QueueName
        :type QueueName: str
        :param Qps: Qps
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        :param Bps: Bps
注意：此字段可能返回 null，表示取不到有效值。
        :type Bps: int
        :param MaxDelaySeconds: MaxDelaySeconds
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDelaySeconds: int
        :param MaxMsgHeapNum: MaxMsgHeapNum
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: PollingWaitSeconds
注意：此字段可能返回 null，表示取不到有效值。
        :type PollingWaitSeconds: int
        :param MsgRetentionSeconds: MsgRetentionSeconds
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param VisibilityTimeout: VisibilityTimeout
注意：此字段可能返回 null，表示取不到有效值。
        :type VisibilityTimeout: int
        :param MaxMsgSize: MaxMsgSize
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param RewindSeconds: RewindSeconds
注意：此字段可能返回 null，表示取不到有效值。
        :type RewindSeconds: int
        :param CreateTime: CreateTime
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LastModifyTime: LastModifyTime
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param ActiveMsgNum: ActiveMsgNum
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveMsgNum: int
        :param InactiveMsgNum: InactiveMsgNum
注意：此字段可能返回 null，表示取不到有效值。
        :type InactiveMsgNum: int
        :param DelayMsgNum: DelayMsgNum
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayMsgNum: int
        :param RewindMsgNum: RewindMsgNum
注意：此字段可能返回 null，表示取不到有效值。
        :type RewindMsgNum: int
        :param MinMsgTime: MinMsgTime
注意：此字段可能返回 null，表示取不到有效值。
        :type MinMsgTime: int
        :param Transaction: Transaction
注意：此字段可能返回 null，表示取不到有效值。
        :type Transaction: bool
        :param DeadLetterSource: DeadLetterSource
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterSource: list of DeadLetterSource
        :param DeadLetterPolicy: DeadLetterPolicy
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        :param TransactionPolicy: TransactionPolicy
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        :param CreateUin: 创建者uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Trace: 消息轨迹表示，true表示开启，false表示不开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
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
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self.DeadLetterPolicy = DeadLetterPolicy()
            self.DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self.TransactionPolicy = TransactionPolicy()
            self.TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")


class RewindQueueRequest(AbstractModel):
    """RewindQueue请求参数结构体

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


class RewindQueueResponse(AbstractModel):
    """RewindQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """订阅返回参数

    """

    def __init__(self):
        """
        :param SubscriptionName: SubscriptionName
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionName: str
        :param SubscriptionId: SubscriptionId
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionId: str
        :param TopicOwner: TopicOwner
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicOwner: int
        :param MsgCount: MsgCount
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param LastModifyTime: LastModifyTime
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param CreateTime: CreateTime
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param BindingKey: BindingKey
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingKey: list of str
        :param Endpoint: Endpoint
注意：此字段可能返回 null，表示取不到有效值。
        :type Endpoint: str
        :param FilterTags: FilterTags
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterTags: list of str
        :param Protocol: Protocol
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param NotifyStrategy: NotifyStrategy
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyStrategy: str
        :param NotifyContentFormat: NotifyContentFormat
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


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param TagKey: 标签Key
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TopicSet(AbstractModel):
    """topic返回信息展示字段

    """

    def __init__(self):
        """
        :param TopicId: TopicId
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param TopicName: TopicName
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param MsgRetentionSeconds: MsgRetentionSeconds
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param MaxMsgSize: MaxMsgSize
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param Qps: Qps
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        :param FilterType: FilterType
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: int
        :param CreateTime: CreateTime
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LastModifyTime: LastModifyTime
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param MsgCount: MsgCount
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param CreateUin: CreateUin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param Tags: Tags
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Trace: 主题是否开启消息轨迹，true表示开启，false表示不开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
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


class TransactionPolicy(AbstractModel):
    """TransactionPolicy

    """

    def __init__(self):
        """
        :param FirstQueryInterval: FirstQueryInterval
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstQueryInterval: int
        :param MaxQueryCount: MaxQueryCount
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxQueryCount: int
        """
        self.FirstQueryInterval = None
        self.MaxQueryCount = None


    def _deserialize(self, params):
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")


class UnbindDeadLetterRequest(AbstractModel):
    """UnbindDeadLetter请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 死信策略源队列名称，调用本接口会清空该队列的死信队列策略。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class UnbindDeadLetterResponse(AbstractModel):
    """UnbindDeadLetter返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")