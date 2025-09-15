# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class DeadLetterPolicy(AbstractModel):
    r"""死信队列策略

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueue: 死信队列。
        :type DeadLetterQueue: str
        :param _DeadLetterQueueName: 死信队列名字。
        :type DeadLetterQueueName: str
        :param _MaxTimeToLive: 最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
        :type MaxTimeToLive: int
        :param _Policy: 死信队列策略。
        :type Policy: int
        :param _MaxReceiveCount: 最大接收次数。
        :type MaxReceiveCount: int
        """
        self._DeadLetterQueue = None
        self._DeadLetterQueueName = None
        self._MaxTimeToLive = None
        self._Policy = None
        self._MaxReceiveCount = None

    @property
    def DeadLetterQueue(self):
        r"""死信队列。
        :rtype: str
        """
        return self._DeadLetterQueue

    @DeadLetterQueue.setter
    def DeadLetterQueue(self, DeadLetterQueue):
        self._DeadLetterQueue = DeadLetterQueue

    @property
    def DeadLetterQueueName(self):
        r"""死信队列名字。
        :rtype: str
        """
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def MaxTimeToLive(self):
        r"""最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
        :rtype: int
        """
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def Policy(self):
        r"""死信队列策略。
        :rtype: int
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxReceiveCount(self):
        r"""最大接收次数。
        :rtype: int
        """
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
    r"""死信源队列信息

    """

    def __init__(self):
        r"""
        :param _QueueId: 消息队列ID。
        :type QueueId: str
        :param _QueueName: 消息队列名字。
        :type QueueName: str
        """
        self._QueueId = None
        self._QueueName = None

    @property
    def QueueId(self):
        r"""消息队列ID。
        :rtype: str
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        r"""消息队列名字。
        :rtype: str
        """
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
        


class DescribeQueueDetailRequest(AbstractModel):
    r"""DescribeQueueDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签搜索
        :type TagKey: str
        :param _Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _QueueName: 精确匹配QueueName
        :type QueueName: str
        :param _Filters: 筛选参数，目前支持QueueName筛选，且仅支持一个关键字
        :type Filters: list of Filter
        :param _Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        """
        self._TagKey = None
        self._Limit = None
        self._QueueName = None
        self._Filters = None
        self._Offset = None

    @property
    def TagKey(self):
        r"""标签搜索
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Limit(self):
        r"""分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QueueName(self):
        r"""精确匹配QueueName
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Filters(self):
        r"""筛选参数，目前支持QueueName筛选，且仅支持一个关键字
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._Limit = params.get("Limit")
        self._QueueName = params.get("QueueName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueueDetailResponse(AbstractModel):
    r"""DescribeQueueDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总队列数。
        :type TotalCount: int
        :param _QueueSet: 队列详情列表。
        :type QueueSet: list of QueueSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总队列数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueueSet(self):
        r"""队列详情列表。
        :rtype: list of QueueSet
        """
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class DescribeTopicDetailRequest(AbstractModel):
    r"""DescribeTopicDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签匹配。
        :type TagKey: str
        :param _Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _TopicName: 精确匹配TopicName。
        :type TopicName: str
        :param _Filters: 目前只支持过滤TopicName ， 且只能填一个过滤值。
        :type Filters: list of Filter
        :param _Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。
        :type Offset: int
        """
        self._TagKey = None
        self._Limit = None
        self._TopicName = None
        self._Filters = None
        self._Offset = None

    @property
    def TagKey(self):
        r"""标签匹配。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Limit(self):
        r"""分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TopicName(self):
        r"""精确匹配TopicName。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Filters(self):
        r"""目前只支持过滤TopicName ， 且只能填一个过滤值。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._Limit = params.get("Limit")
        self._TopicName = params.get("TopicName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    r"""DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 主题列表总数。
        :type TotalCount: int
        :param _TopicSet: 主题详情列表。
        :type TopicSet: list of TopicSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TopicSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""主题列表总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicSet(self):
        r"""主题详情列表。
        :rtype: list of TopicSet
        """
        return self._TopicSet

    @TopicSet.setter
    def TopicSet(self, TopicSet):
        self._TopicSet = TopicSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""过滤参数

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
        r"""数值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        r"""过滤参数的名字
        :rtype: str
        """
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
        


class QueueSet(AbstractModel):
    r"""批量queue属性信息

    """

    def __init__(self):
        r"""
        :param _QueueId: 消息队列ID。
        :type QueueId: str
        :param _RewindSeconds: 回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
        :type RewindSeconds: int
        :param _CreateUin: 创建者Uin。
        :type CreateUin: int
        :param _LastModifyTime: 最后一次修改队列属性的时间。返回 Unix 时间戳，精确到秒。
        :type LastModifyTime: int
        :param _VisibilityTimeout: 消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
        :type VisibilityTimeout: int
        :param _QueueName: 消息队列名字。
        :type QueueName: str
        :param _Trace: 消息轨迹。true表示开启，false表示不开启。
        :type Trace: bool
        :param _Tags: 关联的标签。
        :type Tags: list of Tag
        :param _RewindMsgNum: 已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
        :type RewindMsgNum: int
        :param _MaxDelaySeconds: 飞行消息最大保留时间。
        :type MaxDelaySeconds: int
        :param _TransactionPolicy: 事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        :param _MsgRetentionSeconds: 消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
        :type MsgRetentionSeconds: int
        :param _DelayMsgNum: 延迟消息数。
        :type DelayMsgNum: int
        :param _MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: 消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
        :type PollingWaitSeconds: int
        :param _Bps: 带宽限制。
        :type Bps: int
        :param _InactiveMsgNum: 在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
        :type InactiveMsgNum: int
        :param _DeadLetterPolicy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        :param _ActiveMsgNum: 在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
        :type ActiveMsgNum: int
        :param _MaxMsgSize: 消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
        :type MaxMsgSize: int
        :param _MinMsgTime: 消息最小未消费时间，单位为秒。
        :type MinMsgTime: int
        :param _DeadLetterSource: 死信队列。
        :type DeadLetterSource: list of DeadLetterSource
        :param _Transaction: 事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Transaction: bool
        :param _Qps: 每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
        :type Qps: int
        :param _CreateTime: 队列的创建时间。返回 Unix 时间戳，精确到秒。
        :type CreateTime: int
        :param _Migrate: 是否迁移到新版本。0 表示仅同步元数据，1 表示迁移中，2 表示已经迁移完毕，3 表示回切状态，曾经迁移过，4 未迁移。
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
        r"""消息队列ID。
        :rtype: str
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def RewindSeconds(self):
        r"""回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
        :rtype: int
        """
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def CreateUin(self):
        r"""创建者Uin。
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def LastModifyTime(self):
        r"""最后一次修改队列属性的时间。返回 Unix 时间戳，精确到秒。
        :rtype: int
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def VisibilityTimeout(self):
        r"""消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
        :rtype: int
        """
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def QueueName(self):
        r"""消息队列名字。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Trace(self):
        r"""消息轨迹。true表示开启，false表示不开启。
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def Tags(self):
        r"""关联的标签。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RewindMsgNum(self):
        r"""已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
        :rtype: int
        """
        return self._RewindMsgNum

    @RewindMsgNum.setter
    def RewindMsgNum(self, RewindMsgNum):
        self._RewindMsgNum = RewindMsgNum

    @property
    def MaxDelaySeconds(self):
        r"""飞行消息最大保留时间。
        :rtype: int
        """
        return self._MaxDelaySeconds

    @MaxDelaySeconds.setter
    def MaxDelaySeconds(self, MaxDelaySeconds):
        self._MaxDelaySeconds = MaxDelaySeconds

    @property
    def TransactionPolicy(self):
        r"""事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        """
        return self._TransactionPolicy

    @TransactionPolicy.setter
    def TransactionPolicy(self, TransactionPolicy):
        self._TransactionPolicy = TransactionPolicy

    @property
    def MsgRetentionSeconds(self):
        r"""消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def DelayMsgNum(self):
        r"""延迟消息数。
        :rtype: int
        """
        return self._DelayMsgNum

    @DelayMsgNum.setter
    def DelayMsgNum(self, DelayMsgNum):
        self._DelayMsgNum = DelayMsgNum

    @property
    def MaxMsgHeapNum(self):
        r"""最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :rtype: int
        """
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        r"""消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
        :rtype: int
        """
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def Bps(self):
        r"""带宽限制。
        :rtype: int
        """
        return self._Bps

    @Bps.setter
    def Bps(self, Bps):
        self._Bps = Bps

    @property
    def InactiveMsgNum(self):
        r"""在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
        :rtype: int
        """
        return self._InactiveMsgNum

    @InactiveMsgNum.setter
    def InactiveMsgNum(self, InactiveMsgNum):
        self._InactiveMsgNum = InactiveMsgNum

    @property
    def DeadLetterPolicy(self):
        r"""死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        """
        return self._DeadLetterPolicy

    @DeadLetterPolicy.setter
    def DeadLetterPolicy(self, DeadLetterPolicy):
        self._DeadLetterPolicy = DeadLetterPolicy

    @property
    def ActiveMsgNum(self):
        r"""在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
        :rtype: int
        """
        return self._ActiveMsgNum

    @ActiveMsgNum.setter
    def ActiveMsgNum(self, ActiveMsgNum):
        self._ActiveMsgNum = ActiveMsgNum

    @property
    def MaxMsgSize(self):
        r"""消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MinMsgTime(self):
        r"""消息最小未消费时间，单位为秒。
        :rtype: int
        """
        return self._MinMsgTime

    @MinMsgTime.setter
    def MinMsgTime(self, MinMsgTime):
        self._MinMsgTime = MinMsgTime

    @property
    def DeadLetterSource(self):
        r"""死信队列。
        :rtype: list of DeadLetterSource
        """
        return self._DeadLetterSource

    @DeadLetterSource.setter
    def DeadLetterSource(self, DeadLetterSource):
        self._DeadLetterSource = DeadLetterSource

    @property
    def Transaction(self):
        r"""事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def Qps(self):
        r"""每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def CreateTime(self):
        r"""队列的创建时间。返回 Unix 时间戳，精确到秒。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Migrate(self):
        r"""是否迁移到新版本。0 表示仅同步元数据，1 表示迁移中，2 表示已经迁移完毕，3 表示回切状态，曾经迁移过，4 未迁移。
        :rtype: int
        """
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
        


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签Key
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签Key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
        :rtype: str
        """
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
    r"""topic返回信息展示字段

    """

    def __init__(self):
        r"""
        :param _MsgCount: 当前该主题中消息数目（消息堆积数）。
        :type MsgCount: int
        :param _TopicId: 主题的 ID。
        :type TopicId: str
        :param _MaxMsgSize: 消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为65536。
        :type MaxMsgSize: int
        :param _Trace: 消息轨迹。true表示开启，false表示不开启。
        :type Trace: bool
        :param _Tags: 关联的标签。
        :type Tags: list of Tag
        :param _CreateUin: 创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
        :type CreateUin: int
        :param _FilterType: 描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
        :type FilterType: int
        :param _TopicName: 主题名称。
        :type TopicName: str
        :param _LastModifyTime: 最后一次修改主题属性的时间。返回 Unix 时间戳，精确到秒。
        :type LastModifyTime: int
        :param _MsgRetentionSeconds: 消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
        :type MsgRetentionSeconds: int
        :param _Qps: 每秒钟发布消息的条数。
        :type Qps: int
        :param _CreateTime: 主题的创建时间。返回 Unix 时间戳，精确到秒。
        :type CreateTime: int
        :param _Migrate: 是否迁移到新版本。0 表示未迁移，1 表示迁移中，2 表示已经迁移完毕，3 表示回切状态，曾经迁移过，4 未知状态。
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
        r"""当前该主题中消息数目（消息堆积数）。
        :rtype: int
        """
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def TopicId(self):
        r"""主题的 ID。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def MaxMsgSize(self):
        r"""消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为65536。
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def Trace(self):
        r"""消息轨迹。true表示开启，false表示不开启。
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def Tags(self):
        r"""关联的标签。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateUin(self):
        r"""创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def FilterType(self):
        r"""描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def TopicName(self):
        r"""主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def LastModifyTime(self):
        r"""最后一次修改主题属性的时间。返回 Unix 时间戳，精确到秒。
        :rtype: int
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def MsgRetentionSeconds(self):
        r"""消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Qps(self):
        r"""每秒钟发布消息的条数。
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def CreateTime(self):
        r"""主题的创建时间。返回 Unix 时间戳，精确到秒。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Migrate(self):
        r"""是否迁移到新版本。0 表示未迁移，1 表示迁移中，2 表示已经迁移完毕，3 表示回切状态，曾经迁移过，4 未知状态。
        :rtype: int
        """
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
    r"""事务消息策略

    """

    def __init__(self):
        r"""
        :param _MaxQueryCount: 最大查询次数。
        :type MaxQueryCount: int
        :param _FirstQueryInterval: 第一次回查时间。
        :type FirstQueryInterval: int
        """
        self._MaxQueryCount = None
        self._FirstQueryInterval = None

    @property
    def MaxQueryCount(self):
        r"""最大查询次数。
        :rtype: int
        """
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def FirstQueryInterval(self):
        r"""第一次回查时间。
        :rtype: int
        """
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
        