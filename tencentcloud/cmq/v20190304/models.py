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


class ClearQueueRequest(AbstractModel):
    """ClearQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearQueueResponse(AbstractModel):
    """ClearQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ClearSubscriptionFilterTagsRequest(AbstractModel):
    """ClearSubscriptionFilterTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        """
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearSubscriptionFilterTagsResponse(AbstractModel):
    """ClearSubscriptionFilterTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateQueueRequest(AbstractModel):
    """CreateQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param _MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :type VisibilityTimeout: int
        :param _MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: 队列是否开启回溯消息能力，该参数取值范围0-msgRetentionSeconds,即最大的回溯时间为消息在队列中的保留周期，0表示不开启。
        :type RewindSeconds: int
        :param _Transaction: 1 表示事务队列，0 表示普通队列
        :type Transaction: int
        :param _FirstQueryInterval: 第一次回查间隔
        :type FirstQueryInterval: int
        :param _MaxQueryCount: 最大回查次数
        :type MaxQueryCount: int
        :param _DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param _Policy: 死信策略。0为消息被多次消费未删除，1为Time-To-Live过期
        :type Policy: int
        :param _MaxReceiveCount: 最大接收次数 1-1000
        :type MaxReceiveCount: int
        :param _MaxTimeToLive: policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds
        :type MaxTimeToLive: int
        :param _Trace: 是否开启消息轨迹追踪，当不设置字段时，默认为不开启，该字段为true表示开启，为false表示不开启
        :type Trace: bool
        """
        self._QueueName = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._VisibilityTimeout = None
        self._MaxMsgSize = None
        self._MsgRetentionSeconds = None
        self._RewindSeconds = None
        self._Transaction = None
        self._FirstQueryInterval = None
        self._MaxQueryCount = None
        self._DeadLetterQueueName = None
        self._Policy = None
        self._MaxReceiveCount = None
        self._MaxTimeToLive = None
        self._Trace = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MaxMsgHeapNum(self):
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def VisibilityTimeout(self):
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def RewindSeconds(self):
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def FirstQueryInterval(self):
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxReceiveCount(self):
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount

    @property
    def MaxTimeToLive(self):
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._RewindSeconds = params.get("RewindSeconds")
        self._Transaction = params.get("Transaction")
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        self._MaxQueryCount = params.get("MaxQueryCount")
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._Policy = params.get("Policy")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQueueResponse(AbstractModel):
    """CreateQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueId: 创建成功的queueId
        :type QueueId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueId = None
        self._RequestId = None

    @property
    def QueueId(self):
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        :param _Protocol: 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。
        :type Protocol: str
        :param _Endpoint: 接收通知的Endpoint，根据协议Protocol区分：对于http，Endpoint必须以“`http://`”开头，host可以是域名或IP；对于Queue，则填QueueName。 请注意，目前推送服务不能推送到私有网络中，因此Endpoint填写为私有网络域名或地址将接收不到推送的消息，目前支持推送到公网和基础网络。
        :type Endpoint: str
        :param _NotifyStrategy: 向Endpoint推送消息出现错误时，CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s...由于Topic消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是EXPONENTIAL_DECAY_RETRY。
        :type NotifyStrategy: str
        :param _FilterTag: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。
        :type FilterTag: list of str
        :param _BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。
        :type BindingKey: list of str
        :param _NotifyContentFormat: 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，则取值必须为SIMPLIFIED。如果Protocol是http，两个值均可以，默认值是JSON。
        :type NotifyContentFormat: str
        """
        self._TopicName = None
        self._SubscriptionName = None
        self._Protocol = None
        self._Endpoint = None
        self._NotifyStrategy = None
        self._FilterTag = None
        self._BindingKey = None
        self._NotifyContentFormat = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def NotifyStrategy(self):
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def FilterTag(self):
        return self._FilterTag

    @FilterTag.setter
    def FilterTag(self, FilterTag):
        self._FilterTag = FilterTag

    @property
    def BindingKey(self):
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey

    @property
    def NotifyContentFormat(self):
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        self._Protocol = params.get("Protocol")
        self._Endpoint = params.get("Endpoint")
        self._NotifyStrategy = params.get("NotifyStrategy")
        self._FilterTag = params.get("FilterTag")
        self._BindingKey = params.get("BindingKey")
        self._NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscriptionId: SubscriptionId
        :type SubscriptionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscriptionId = None
        self._RequestId = None

    @property
    def SubscriptionId(self):
        return self._SubscriptionId

    @SubscriptionId.setter
    def SubscriptionId(self, SubscriptionId):
        self._SubscriptionId = SubscriptionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscriptionId = params.get("SubscriptionId")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param _FilterType: 用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略，默认值为标签匹配策略。
        :type FilterType: int
        :param _MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。
        :type MsgRetentionSeconds: int
        :param _Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        """
        self._TopicName = None
        self._MaxMsgSize = None
        self._FilterType = None
        self._MsgRetentionSeconds = None
        self._Trace = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._FilterType = params.get("FilterType")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: TopicName
        :type TopicId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class DeadLetterPolicy(AbstractModel):
    """死信队列策略

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueue: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterQueue: str
        :param _DeadLetterQueueName: 死信队列名字。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterQueueName: str
        :param _MaxTimeToLive: 最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTimeToLive: int
        :param _Policy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: int
        :param _MaxReceiveCount: 最大接收次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReceiveCount: int
        """
        self._DeadLetterQueue = None
        self._DeadLetterQueueName = None
        self._MaxTimeToLive = None
        self._Policy = None
        self._MaxReceiveCount = None

    @property
    def DeadLetterQueue(self):
        return self._DeadLetterQueue

    @DeadLetterQueue.setter
    def DeadLetterQueue(self, DeadLetterQueue):
        self._DeadLetterQueue = DeadLetterQueue

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def MaxTimeToLive(self):
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxReceiveCount(self):
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount


    def _deserialize(self, params):
        self._DeadLetterQueue = params.get("DeadLetterQueue")
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._Policy = params.get("Policy")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeadLetterSource(AbstractModel):
    """死信源队列信息

    """

    def __init__(self):
        r"""
        :param _QueueId: 消息队列ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueId: str
        :param _QueueName: 消息队列名字。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        """
        self._QueueId = None
        self._QueueName = None

    @property
    def QueueId(self):
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSubscribeRequest(AbstractModel):
    """DeleteSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        """
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubscribeResponse(AbstractModel):
    """DeleteSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        """
        self._TopicName = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeDeadLetterSourceQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param _Limit: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。
        :type Limit: int
        :param _Offset: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Offset: int
        :param _Filters: 过滤死信队列源队列名称，目前仅支持SourceQueueName过滤
        :type Filters: list of Filter
        """
        self._DeadLetterQueueName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeDeadLetterSourceQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足本次条件的队列个数
        :type TotalCount: int
        :param _QueueSet: 死信队列源队列
        :type QueueSet: list of DeadLetterSource
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueueSet(self):
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self._QueueSet = []
            for item in params.get("QueueSet"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQueueDetailRequest(AbstractModel):
    """DescribeQueueDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param _Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _Filters: 筛选参数，目前支持QueueName筛选，且仅支持一个关键字
        :type Filters: list of Filter
        :param _TagKey: 标签搜索
        :type TagKey: str
        :param _QueueName: 精确匹配QueueName
        :type QueueName: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagKey = None
        self._QueueName = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TagKey = params.get("TagKey")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueueDetailResponse(AbstractModel):
    """DescribeQueueDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总队列数。
        :type TotalCount: int
        :param _QueueSet: 队列详情列表。
        :type QueueSet: list of QueueSet
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueueSet(self):
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self._QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueSet()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscriptionDetailRequest(AbstractModel):
    """DescribeSubscriptionDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _Offset: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param _Limit: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _Filters: 筛选参数，目前只支持SubscriptionName，且仅支持一个关键字。
        :type Filters: list of Filter
        """
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionDetailResponse(AbstractModel):
    """DescribeSubscriptionDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _SubscriptionSet: Subscription属性集合
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionSet: list of Subscription
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SubscriptionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SubscriptionSet(self):
        return self._SubscriptionSet

    @SubscriptionSet.setter
    def SubscriptionSet(self, SubscriptionSet):
        self._SubscriptionSet = SubscriptionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SubscriptionSet") is not None:
            self._SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = Subscription()
                obj._deserialize(item)
                self._SubscriptionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。
        :type Offset: int
        :param _Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _Filters: 目前只支持过滤TopicName ， 且只能填一个过滤值。
        :type Filters: list of Filter
        :param _TagKey: 标签匹配。
        :type TagKey: str
        :param _TopicName: 精确匹配TopicName。
        :type TopicName: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagKey = None
        self._TopicName = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TagKey = params.get("TagKey")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 主题列表总数。
        :type TotalCount: int
        :param _TopicSet: 主题详情列表。
        :type TopicSet: list of TopicSet
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TopicSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicSet(self):
        return self._TopicSet

    @TopicSet.setter
    def TopicSet(self, TopicSet):
        self._TopicSet = TopicSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicSet") is not None:
            self._TopicSet = []
            for item in params.get("TopicSet"):
                obj = TopicSet()
                obj._deserialize(item)
                self._TopicSet.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """过滤参数

    """

    def __init__(self):
        r"""
        :param _Values: 数值
        :type Values: list of str
        :param _Name: 过滤参数的名字
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeRequest(AbstractModel):
    """ModifyQueueAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param _MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :type VisibilityTimeout: int
        :param _MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: 消息最长回溯时间，取值范围0-msgRetentionSeconds，消息的最大回溯之间为消息在队列中的保存周期，0表示不开启消息回溯。
        :type RewindSeconds: int
        :param _FirstQueryInterval: 第一次查询时间
        :type FirstQueryInterval: int
        :param _MaxQueryCount: 最大查询次数
        :type MaxQueryCount: int
        :param _DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param _MaxTimeToLive: MaxTimeToLivepolicy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds
        :type MaxTimeToLive: int
        :param _MaxReceiveCount: 最大接收次数
        :type MaxReceiveCount: int
        :param _Policy: 死信队列策略
        :type Policy: int
        :param _Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        """
        self._QueueName = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._VisibilityTimeout = None
        self._MaxMsgSize = None
        self._MsgRetentionSeconds = None
        self._RewindSeconds = None
        self._FirstQueryInterval = None
        self._MaxQueryCount = None
        self._DeadLetterQueueName = None
        self._MaxTimeToLive = None
        self._MaxReceiveCount = None
        self._Policy = None
        self._Trace = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MaxMsgHeapNum(self):
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def VisibilityTimeout(self):
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def RewindSeconds(self):
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def FirstQueryInterval(self):
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def MaxTimeToLive(self):
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def MaxReceiveCount(self):
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._RewindSeconds = params.get("RewindSeconds")
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        self._MaxQueryCount = params.get("MaxQueryCount")
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        self._Policy = params.get("Policy")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeResponse(AbstractModel):
    """ModifyQueueAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscriptionAttributeRequest(AbstractModel):
    """ModifySubscriptionAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        :param _NotifyStrategy: 向 Endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值如下：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息。
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s···由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
        :type NotifyStrategy: str
        :param _NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 Protocol 是 queue，则取值必须为 SIMPLIFIED。如果 Protocol 是 HTTP，两个值均可以，默认值是 JSON。
        :type NotifyContentFormat: str
        :param _FilterTags: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。
        :type FilterTags: list of str
        :param _BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。
        :type BindingKey: list of str
        """
        self._TopicName = None
        self._SubscriptionName = None
        self._NotifyStrategy = None
        self._NotifyContentFormat = None
        self._FilterTags = None
        self._BindingKey = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def NotifyStrategy(self):
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def NotifyContentFormat(self):
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat

    @property
    def FilterTags(self):
        return self._FilterTags

    @FilterTags.setter
    def FilterTags(self, FilterTags):
        self._FilterTags = FilterTags

    @property
    def BindingKey(self):
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        self._NotifyStrategy = params.get("NotifyStrategy")
        self._NotifyContentFormat = params.get("NotifyContentFormat")
        self._FilterTags = params.get("FilterTags")
        self._BindingKey = params.get("BindingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscriptionAttributeResponse(AbstractModel):
    """ModifySubscriptionAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTopicAttributeRequest(AbstractModel):
    """ModifyTopicAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        :param _MaxMsgSize: 消息最大长度。取值范围1024 - 65536 Byte（即1 - 64K），默认值65536。
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。
        :type MsgRetentionSeconds: int
        :param _Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        """
        self._TopicName = None
        self._MaxMsgSize = None
        self._MsgRetentionSeconds = None
        self._Trace = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributeResponse(AbstractModel):
    """ModifyTopicAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class QueueSet(AbstractModel):
    """批量queue属性信息

    """

    def __init__(self):
        r"""
        :param _QueueId: 消息队列ID。
        :type QueueId: str
        :param _RewindSeconds: 回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
注意：此字段可能返回 null，表示取不到有效值。
        :type RewindSeconds: int
        :param _CreateUin: 创建者Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param _LastModifyTime: 最后一次修改队列属性的时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param _VisibilityTimeout: 消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
注意：此字段可能返回 null，表示取不到有效值。
        :type VisibilityTimeout: int
        :param _QueueName: 消息队列名字。
        :type QueueName: str
        :param _Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
        :param _Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _RewindMsgNum: 已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type RewindMsgNum: int
        :param _MaxDelaySeconds: 飞行消息最大保留时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDelaySeconds: int
        :param _TransactionPolicy: 事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        :param _MsgRetentionSeconds: 消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param _DelayMsgNum: 延迟消息数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayMsgNum: int
        :param _MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: 消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
注意：此字段可能返回 null，表示取不到有效值。
        :type PollingWaitSeconds: int
        :param _Bps: 带宽限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bps: int
        :param _InactiveMsgNum: 在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。
        :type InactiveMsgNum: int
        :param _DeadLetterPolicy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        :param _ActiveMsgNum: 在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveMsgNum: int
        :param _MaxMsgSize: 消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param _MinMsgTime: 消息最小未消费时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type MinMsgTime: int
        :param _DeadLetterSource: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterSource: list of DeadLetterSource
        :param _Transaction: 事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Transaction: bool
        :param _Qps: 每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        :param _CreateTime: 队列的创建时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _Migrate: 是否迁移到新版本。0 表示仅同步元数据，1 表示迁移中，2 表示已经迁移完毕，3 表示回切状态，曾经迁移过，4 未迁移。
注意：此字段可能返回 null，表示取不到有效值。
        :type Migrate: int
        """
        self._QueueId = None
        self._RewindSeconds = None
        self._CreateUin = None
        self._LastModifyTime = None
        self._VisibilityTimeout = None
        self._QueueName = None
        self._Trace = None
        self._Tags = None
        self._RewindMsgNum = None
        self._MaxDelaySeconds = None
        self._TransactionPolicy = None
        self._MsgRetentionSeconds = None
        self._DelayMsgNum = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._Bps = None
        self._InactiveMsgNum = None
        self._DeadLetterPolicy = None
        self._ActiveMsgNum = None
        self._MaxMsgSize = None
        self._MinMsgTime = None
        self._DeadLetterSource = None
        self._Transaction = None
        self._Qps = None
        self._CreateTime = None
        self._Migrate = None

    @property
    def QueueId(self):
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def RewindSeconds(self):
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def LastModifyTime(self):
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def VisibilityTimeout(self):
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RewindMsgNum(self):
        return self._RewindMsgNum

    @RewindMsgNum.setter
    def RewindMsgNum(self, RewindMsgNum):
        self._RewindMsgNum = RewindMsgNum

    @property
    def MaxDelaySeconds(self):
        return self._MaxDelaySeconds

    @MaxDelaySeconds.setter
    def MaxDelaySeconds(self, MaxDelaySeconds):
        self._MaxDelaySeconds = MaxDelaySeconds

    @property
    def TransactionPolicy(self):
        return self._TransactionPolicy

    @TransactionPolicy.setter
    def TransactionPolicy(self, TransactionPolicy):
        self._TransactionPolicy = TransactionPolicy

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def DelayMsgNum(self):
        return self._DelayMsgNum

    @DelayMsgNum.setter
    def DelayMsgNum(self, DelayMsgNum):
        self._DelayMsgNum = DelayMsgNum

    @property
    def MaxMsgHeapNum(self):
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def Bps(self):
        return self._Bps

    @Bps.setter
    def Bps(self, Bps):
        self._Bps = Bps

    @property
    def InactiveMsgNum(self):
        return self._InactiveMsgNum

    @InactiveMsgNum.setter
    def InactiveMsgNum(self, InactiveMsgNum):
        self._InactiveMsgNum = InactiveMsgNum

    @property
    def DeadLetterPolicy(self):
        return self._DeadLetterPolicy

    @DeadLetterPolicy.setter
    def DeadLetterPolicy(self, DeadLetterPolicy):
        self._DeadLetterPolicy = DeadLetterPolicy

    @property
    def ActiveMsgNum(self):
        return self._ActiveMsgNum

    @ActiveMsgNum.setter
    def ActiveMsgNum(self, ActiveMsgNum):
        self._ActiveMsgNum = ActiveMsgNum

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MinMsgTime(self):
        return self._MinMsgTime

    @MinMsgTime.setter
    def MinMsgTime(self, MinMsgTime):
        self._MinMsgTime = MinMsgTime

    @property
    def DeadLetterSource(self):
        return self._DeadLetterSource

    @DeadLetterSource.setter
    def DeadLetterSource(self, DeadLetterSource):
        self._DeadLetterSource = DeadLetterSource

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Migrate(self):
        return self._Migrate

    @Migrate.setter
    def Migrate(self, Migrate):
        self._Migrate = Migrate


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._RewindSeconds = params.get("RewindSeconds")
        self._CreateUin = params.get("CreateUin")
        self._LastModifyTime = params.get("LastModifyTime")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._QueueName = params.get("QueueName")
        self._Trace = params.get("Trace")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RewindMsgNum = params.get("RewindMsgNum")
        self._MaxDelaySeconds = params.get("MaxDelaySeconds")
        if params.get("TransactionPolicy") is not None:
            self._TransactionPolicy = TransactionPolicy()
            self._TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._DelayMsgNum = params.get("DelayMsgNum")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._Bps = params.get("Bps")
        self._InactiveMsgNum = params.get("InactiveMsgNum")
        if params.get("DeadLetterPolicy") is not None:
            self._DeadLetterPolicy = DeadLetterPolicy()
            self._DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        self._ActiveMsgNum = params.get("ActiveMsgNum")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._MinMsgTime = params.get("MinMsgTime")
        if params.get("DeadLetterSource") is not None:
            self._DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self._DeadLetterSource.append(obj)
        self._Transaction = params.get("Transaction")
        self._Qps = params.get("Qps")
        self._CreateTime = params.get("CreateTime")
        self._Migrate = params.get("Migrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueRequest(AbstractModel):
    """RewindQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param _StartConsumeTime: 设定该时间，则（Batch）receiveMessage接口，会按照生产消息的先后顺序消费该时间戳以后的消息。
        :type StartConsumeTime: int
        """
        self._QueueName = None
        self._StartConsumeTime = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def StartConsumeTime(self):
        return self._StartConsumeTime

    @StartConsumeTime.setter
    def StartConsumeTime(self, StartConsumeTime):
        self._StartConsumeTime = StartConsumeTime


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._StartConsumeTime = params.get("StartConsumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueResponse(AbstractModel):
    """RewindQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """订阅返回参数

    """

    def __init__(self):
        r"""
        :param _SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionName: str
        :param _SubscriptionId: 订阅 ID。订阅 ID 在拉取监控数据时会用到。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionId: str
        :param _TopicOwner: 订阅拥有者的 APPID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicOwner: int
        :param _MsgCount: 该订阅待投递的消息数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param _LastModifyTime: 最后一次修改订阅属性的时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param _CreateTime: 订阅的创建时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _BindingKey: 表示订阅接收消息的过滤策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingKey: list of str
        :param _Endpoint: 接收通知的 endpoint，根据协议 protocol 区分：对于 HTTP，endpoint 必须以http://开头，host 可以是域名或 IP；对于 queue，则填 queueName。
注意：此字段可能返回 null，表示取不到有效值。
        :type Endpoint: str
        :param _FilterTags: 描述用户创建订阅时选择的过滤策略：
filterType = 1表示用户使用 filterTag 标签过滤
filterType = 2表示用户使用 bindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterTags: list of str
        :param _Protocol: 订阅的协议，目前支持两种协议：HTTP、queue。使用 HTTP 协议，用户需自己搭建接受消息的 Web Server。使用 queue，消息会自动推送到 CMQ queue，用户可以并发地拉取消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _NotifyStrategy: 向 endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值有：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始 1s，后面是 2s，4s，8s...由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyStrategy: str
        :param _NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 protocol 是 queue，则取值必须为 SIMPLIFIED。如果 protocol 是 HTTP，两个值均可以，默认值是 JSON。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyContentFormat: str
        """
        self._SubscriptionName = None
        self._SubscriptionId = None
        self._TopicOwner = None
        self._MsgCount = None
        self._LastModifyTime = None
        self._CreateTime = None
        self._BindingKey = None
        self._Endpoint = None
        self._FilterTags = None
        self._Protocol = None
        self._NotifyStrategy = None
        self._NotifyContentFormat = None

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def SubscriptionId(self):
        return self._SubscriptionId

    @SubscriptionId.setter
    def SubscriptionId(self, SubscriptionId):
        self._SubscriptionId = SubscriptionId

    @property
    def TopicOwner(self):
        return self._TopicOwner

    @TopicOwner.setter
    def TopicOwner(self, TopicOwner):
        self._TopicOwner = TopicOwner

    @property
    def MsgCount(self):
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def LastModifyTime(self):
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BindingKey(self):
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def FilterTags(self):
        return self._FilterTags

    @FilterTags.setter
    def FilterTags(self, FilterTags):
        self._FilterTags = FilterTags

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NotifyStrategy(self):
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def NotifyContentFormat(self):
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat


    def _deserialize(self, params):
        self._SubscriptionName = params.get("SubscriptionName")
        self._SubscriptionId = params.get("SubscriptionId")
        self._TopicOwner = params.get("TopicOwner")
        self._MsgCount = params.get("MsgCount")
        self._LastModifyTime = params.get("LastModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._BindingKey = params.get("BindingKey")
        self._Endpoint = params.get("Endpoint")
        self._FilterTags = params.get("FilterTags")
        self._Protocol = params.get("Protocol")
        self._NotifyStrategy = params.get("NotifyStrategy")
        self._NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签Key
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicSet(AbstractModel):
    """topic返回信息展示字段

    """

    def __init__(self):
        r"""
        :param _MsgCount: 当前该主题中消息数目（消息堆积数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param _TopicId: 主题的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _MaxMsgSize: 消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为65536。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param _Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
        :param _Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _CreateUin: 创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param _FilterType: 描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: int
        :param _TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _LastModifyTime: 最后一次修改主题属性的时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param _MsgRetentionSeconds: 消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param _Qps: 每秒钟发布消息的条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        :param _CreateTime: 主题的创建时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _Migrate: 是否迁移到新版本。0 表示未迁移，1 表示迁移中，2 表示已经迁移完毕，3 表示回切状态，曾经迁移过，4 未知状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type Migrate: int
        """
        self._MsgCount = None
        self._TopicId = None
        self._MaxMsgSize = None
        self._Trace = None
        self._Tags = None
        self._CreateUin = None
        self._FilterType = None
        self._TopicName = None
        self._LastModifyTime = None
        self._MsgRetentionSeconds = None
        self._Qps = None
        self._CreateTime = None
        self._Migrate = None

    @property
    def MsgCount(self):
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def LastModifyTime(self):
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Migrate(self):
        return self._Migrate

    @Migrate.setter
    def Migrate(self, Migrate):
        self._Migrate = Migrate


    def _deserialize(self, params):
        self._MsgCount = params.get("MsgCount")
        self._TopicId = params.get("TopicId")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._Trace = params.get("Trace")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateUin = params.get("CreateUin")
        self._FilterType = params.get("FilterType")
        self._TopicName = params.get("TopicName")
        self._LastModifyTime = params.get("LastModifyTime")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._Qps = params.get("Qps")
        self._CreateTime = params.get("CreateTime")
        self._Migrate = params.get("Migrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionPolicy(AbstractModel):
    """事务消息策略

    """

    def __init__(self):
        r"""
        :param _MaxQueryCount: 最大查询次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxQueryCount: int
        :param _FirstQueryInterval: 第一次回查时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstQueryInterval: int
        """
        self._MaxQueryCount = None
        self._FirstQueryInterval = None

    @property
    def MaxQueryCount(self):
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def FirstQueryInterval(self):
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval


    def _deserialize(self, params):
        self._MaxQueryCount = params.get("MaxQueryCount")
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterRequest(AbstractModel):
    """UnbindDeadLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 死信策略源队列名称，调用本接口会清空该队列的死信队列策略。
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterResponse(AbstractModel):
    """UnbindDeadLetter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")