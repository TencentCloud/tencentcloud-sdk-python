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


class CreateRabbitMQServerlessBindingRequest(AbstractModel):
    """CreateRabbitMQServerlessBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _Source: 源exchange
        :type Source: str
        :param _DestinationType: 目标类型,取值queue或exchange
        :type DestinationType: str
        :param _Destination: 目标队列或者交换机
        :type Destination: str
        :param _RoutingKey: 绑定key
        :type RoutingKey: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Source = None
        self._DestinationType = None
        self._Destination = None
        self._RoutingKey = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Source(self):
        """源exchange
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def DestinationType(self):
        """目标类型,取值queue或exchange
        :rtype: str
        """
        return self._DestinationType

    @DestinationType.setter
    def DestinationType(self, DestinationType):
        self._DestinationType = DestinationType

    @property
    def Destination(self):
        """目标队列或者交换机
        :rtype: str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def RoutingKey(self):
        """绑定key
        :rtype: str
        """
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Source = params.get("Source")
        self._DestinationType = params.get("DestinationType")
        self._Destination = params.get("Destination")
        self._RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessBindingResponse(AbstractModel):
    """CreateRabbitMQServerlessBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 队列名称
        :type InstanceId: str
        :param _VirtualHost: vhost参数
        :type VirtualHost: str
        :param _BindingId: 路由关系Id
        :type BindingId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._BindingId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """队列名称
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def BindingId(self):
        """路由关系Id
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._BindingId = params.get("BindingId")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessExchangeRequest(AbstractModel):
    """CreateRabbitMQServerlessExchange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: VHost参数
        :type VirtualHost: str
        :param _ExchangeName: exchange 名称
        :type ExchangeName: str
        :param _ExchangeType: exchange 类型, 支持 "fanout","direct","topic","headers"
        :type ExchangeType: str
        :param _Remark: exchange 备注
        :type Remark: str
        :param _Durable: 是否为持久化 exchange, 当集群重启时,将会清除所有该字段为"false"的 exchange
        :type Durable: bool
        :param _AutoDelete: 是否自动删除该 exchange, 如果为 "true", 当解绑所有当前 exchange 上的路由关系时, 该 exchange 将会被自动删除
        :type AutoDelete: bool
        :param _Internal: 是否为内部 exchange, 如果为 "true", 则无法直接投递消息到该 exchange, 需要在路由设置中通过其他 exchange 进行转发
        :type Internal: bool
        :param _AlternateExchange: 替代 exchange, 如果消息无法发送到当前 exchange, 就会发送到该替代 exchange
        :type AlternateExchange: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None
        self._ExchangeType = None
        self._Remark = None
        self._Durable = None
        self._AutoDelete = None
        self._Internal = None
        self._AlternateExchange = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """VHost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        """exchange 名称
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def ExchangeType(self):
        """exchange 类型, 支持 "fanout","direct","topic","headers"
        :rtype: str
        """
        return self._ExchangeType

    @ExchangeType.setter
    def ExchangeType(self, ExchangeType):
        self._ExchangeType = ExchangeType

    @property
    def Remark(self):
        """exchange 备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Durable(self):
        """是否为持久化 exchange, 当集群重启时,将会清除所有该字段为"false"的 exchange
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        """是否自动删除该 exchange, 如果为 "true", 当解绑所有当前 exchange 上的路由关系时, 该 exchange 将会被自动删除
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Internal(self):
        """是否为内部 exchange, 如果为 "true", 则无法直接投递消息到该 exchange, 需要在路由设置中通过其他 exchange 进行转发
        :rtype: bool
        """
        return self._Internal

    @Internal.setter
    def Internal(self, Internal):
        self._Internal = Internal

    @property
    def AlternateExchange(self):
        """替代 exchange, 如果消息无法发送到当前 exchange, 就会发送到该替代 exchange
        :rtype: str
        """
        return self._AlternateExchange

    @AlternateExchange.setter
    def AlternateExchange(self, AlternateExchange):
        self._AlternateExchange = AlternateExchange


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        self._ExchangeType = params.get("ExchangeType")
        self._Remark = params.get("Remark")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Internal = params.get("Internal")
        self._AlternateExchange = params.get("AlternateExchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessExchangeResponse(AbstractModel):
    """CreateRabbitMQServerlessExchange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange 名称
        :type ExchangeName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExchangeName = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        """exchange 名称
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExchangeName = params.get("ExchangeName")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessQueueRequest(AbstractModel):
    """CreateRabbitMQServerlessQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: VHost参数
        :type VirtualHost: str
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _QueueType: 只支持 classic
        :type QueueType: str
        :param _Durable: 持久标记,classic类型必传,quorum类型无需传入固定为true
        :type Durable: bool
        :param _AutoDelete: 自动清除,classic类型必传,quorum类型无需传入固定为false
        :type AutoDelete: bool
        :param _Remark: 备注
        :type Remark: str
        :param _MessageTTL: MessageTTL参数,classic类型专用
        :type MessageTTL: int
        :param _AutoExpire: AutoExpire参数，单位为 ms，队列在指定时间内没有被使用，将会被删除
        :type AutoExpire: int
        :param _MaxLength: MaxLength参数。队列可以容纳的最大条数。若超出上限，将根据 overview behavior 处理
        :type MaxLength: int
        :param _MaxLengthBytes: MaxLengthBytes参数。若超出上限，将根据 overview behavior 处理。
        :type MaxLengthBytes: int
        :param _DeliveryLimit: DeliveryLimit参数,quorum类型专用
        :type DeliveryLimit: int
        :param _OverflowBehaviour: OverflowBehaviour参数,取值为drop-head, reject-publish或reject-publish-dlx
        :type OverflowBehaviour: str
        :param _DeadLetterExchange: DeadLetterExchange参数。可将过期或被拒绝的消息投往指定的死信 exchange。
        :type DeadLetterExchange: str
        :param _DeadLetterRoutingKey: DeadLetterRoutingKey参数。只能包含字母、数字、"."、"-"，"@"，"_"
        :type DeadLetterRoutingKey: str
        :param _SingleActiveConsumer: SingleActiveConsumer参数。若开启，需确保每次有且只有一个消费者从队列中消费
        :type SingleActiveConsumer: bool
        :param _MaximumPriority: MaximumPriority参数,classic类型专用
        :type MaximumPriority: int
        :param _LazyMode: LazyMode参数,classic类型专用
        :type LazyMode: bool
        :param _MasterLocator: MasterLocator参数,classic类型专用,取值为min-masters,client-local或random
        :type MasterLocator: str
        :param _MaxInMemoryLength: MaxInMemoryLength参数，quorum类型专用。quorum 队列的内存中最大消息数量
        :type MaxInMemoryLength: int
        :param _MaxInMemoryBytes: MaxInMemoryBytes参数，quorum类型专用。quorum 队列的内存中最大数总消息大小
        :type MaxInMemoryBytes: int
        :param _Node: Node参数，非必填，指定创建 queue 所在节点
        :type Node: str
        :param _DeadLetterStrategy: 仲裁队列死信一致性策略，at-most-once、at-least-once，默认是at-most-once
        :type DeadLetterStrategy: str
        :param _QueueLeaderLocator: 仲裁队列的领导者选举策略，client-local、balanced，默认是client-local
        :type QueueLeaderLocator: str
        :param _QuorumInitialGroupSize: 仲裁队列的初始副本组大小，默认3
        :type QuorumInitialGroupSize: int
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._QueueType = None
        self._Durable = None
        self._AutoDelete = None
        self._Remark = None
        self._MessageTTL = None
        self._AutoExpire = None
        self._MaxLength = None
        self._MaxLengthBytes = None
        self._DeliveryLimit = None
        self._OverflowBehaviour = None
        self._DeadLetterExchange = None
        self._DeadLetterRoutingKey = None
        self._SingleActiveConsumer = None
        self._MaximumPriority = None
        self._LazyMode = None
        self._MasterLocator = None
        self._MaxInMemoryLength = None
        self._MaxInMemoryBytes = None
        self._Node = None
        self._DeadLetterStrategy = None
        self._QueueLeaderLocator = None
        self._QuorumInitialGroupSize = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """VHost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def QueueType(self):
        """只支持 classic
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def Durable(self):
        """持久标记,classic类型必传,quorum类型无需传入固定为true
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        """自动清除,classic类型必传,quorum类型无需传入固定为false
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageTTL(self):
        """MessageTTL参数,classic类型专用
        :rtype: int
        """
        return self._MessageTTL

    @MessageTTL.setter
    def MessageTTL(self, MessageTTL):
        self._MessageTTL = MessageTTL

    @property
    def AutoExpire(self):
        """AutoExpire参数，单位为 ms，队列在指定时间内没有被使用，将会被删除
        :rtype: int
        """
        return self._AutoExpire

    @AutoExpire.setter
    def AutoExpire(self, AutoExpire):
        self._AutoExpire = AutoExpire

    @property
    def MaxLength(self):
        """MaxLength参数。队列可以容纳的最大条数。若超出上限，将根据 overview behavior 处理
        :rtype: int
        """
        return self._MaxLength

    @MaxLength.setter
    def MaxLength(self, MaxLength):
        self._MaxLength = MaxLength

    @property
    def MaxLengthBytes(self):
        """MaxLengthBytes参数。若超出上限，将根据 overview behavior 处理。
        :rtype: int
        """
        return self._MaxLengthBytes

    @MaxLengthBytes.setter
    def MaxLengthBytes(self, MaxLengthBytes):
        self._MaxLengthBytes = MaxLengthBytes

    @property
    def DeliveryLimit(self):
        """DeliveryLimit参数,quorum类型专用
        :rtype: int
        """
        return self._DeliveryLimit

    @DeliveryLimit.setter
    def DeliveryLimit(self, DeliveryLimit):
        self._DeliveryLimit = DeliveryLimit

    @property
    def OverflowBehaviour(self):
        """OverflowBehaviour参数,取值为drop-head, reject-publish或reject-publish-dlx
        :rtype: str
        """
        return self._OverflowBehaviour

    @OverflowBehaviour.setter
    def OverflowBehaviour(self, OverflowBehaviour):
        self._OverflowBehaviour = OverflowBehaviour

    @property
    def DeadLetterExchange(self):
        """DeadLetterExchange参数。可将过期或被拒绝的消息投往指定的死信 exchange。
        :rtype: str
        """
        return self._DeadLetterExchange

    @DeadLetterExchange.setter
    def DeadLetterExchange(self, DeadLetterExchange):
        self._DeadLetterExchange = DeadLetterExchange

    @property
    def DeadLetterRoutingKey(self):
        """DeadLetterRoutingKey参数。只能包含字母、数字、"."、"-"，"@"，"_"
        :rtype: str
        """
        return self._DeadLetterRoutingKey

    @DeadLetterRoutingKey.setter
    def DeadLetterRoutingKey(self, DeadLetterRoutingKey):
        self._DeadLetterRoutingKey = DeadLetterRoutingKey

    @property
    def SingleActiveConsumer(self):
        """SingleActiveConsumer参数。若开启，需确保每次有且只有一个消费者从队列中消费
        :rtype: bool
        """
        return self._SingleActiveConsumer

    @SingleActiveConsumer.setter
    def SingleActiveConsumer(self, SingleActiveConsumer):
        self._SingleActiveConsumer = SingleActiveConsumer

    @property
    def MaximumPriority(self):
        """MaximumPriority参数,classic类型专用
        :rtype: int
        """
        return self._MaximumPriority

    @MaximumPriority.setter
    def MaximumPriority(self, MaximumPriority):
        self._MaximumPriority = MaximumPriority

    @property
    def LazyMode(self):
        """LazyMode参数,classic类型专用
        :rtype: bool
        """
        return self._LazyMode

    @LazyMode.setter
    def LazyMode(self, LazyMode):
        self._LazyMode = LazyMode

    @property
    def MasterLocator(self):
        """MasterLocator参数,classic类型专用,取值为min-masters,client-local或random
        :rtype: str
        """
        return self._MasterLocator

    @MasterLocator.setter
    def MasterLocator(self, MasterLocator):
        self._MasterLocator = MasterLocator

    @property
    def MaxInMemoryLength(self):
        """MaxInMemoryLength参数，quorum类型专用。quorum 队列的内存中最大消息数量
        :rtype: int
        """
        return self._MaxInMemoryLength

    @MaxInMemoryLength.setter
    def MaxInMemoryLength(self, MaxInMemoryLength):
        self._MaxInMemoryLength = MaxInMemoryLength

    @property
    def MaxInMemoryBytes(self):
        """MaxInMemoryBytes参数，quorum类型专用。quorum 队列的内存中最大数总消息大小
        :rtype: int
        """
        return self._MaxInMemoryBytes

    @MaxInMemoryBytes.setter
    def MaxInMemoryBytes(self, MaxInMemoryBytes):
        self._MaxInMemoryBytes = MaxInMemoryBytes

    @property
    def Node(self):
        """Node参数，非必填，指定创建 queue 所在节点
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def DeadLetterStrategy(self):
        """仲裁队列死信一致性策略，at-most-once、at-least-once，默认是at-most-once
        :rtype: str
        """
        return self._DeadLetterStrategy

    @DeadLetterStrategy.setter
    def DeadLetterStrategy(self, DeadLetterStrategy):
        self._DeadLetterStrategy = DeadLetterStrategy

    @property
    def QueueLeaderLocator(self):
        """仲裁队列的领导者选举策略，client-local、balanced，默认是client-local
        :rtype: str
        """
        return self._QueueLeaderLocator

    @QueueLeaderLocator.setter
    def QueueLeaderLocator(self, QueueLeaderLocator):
        self._QueueLeaderLocator = QueueLeaderLocator

    @property
    def QuorumInitialGroupSize(self):
        """仲裁队列的初始副本组大小，默认3
        :rtype: int
        """
        return self._QuorumInitialGroupSize

    @QuorumInitialGroupSize.setter
    def QuorumInitialGroupSize(self, QuorumInitialGroupSize):
        self._QuorumInitialGroupSize = QuorumInitialGroupSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._QueueType = params.get("QueueType")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Remark = params.get("Remark")
        self._MessageTTL = params.get("MessageTTL")
        self._AutoExpire = params.get("AutoExpire")
        self._MaxLength = params.get("MaxLength")
        self._MaxLengthBytes = params.get("MaxLengthBytes")
        self._DeliveryLimit = params.get("DeliveryLimit")
        self._OverflowBehaviour = params.get("OverflowBehaviour")
        self._DeadLetterExchange = params.get("DeadLetterExchange")
        self._DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        self._SingleActiveConsumer = params.get("SingleActiveConsumer")
        self._MaximumPriority = params.get("MaximumPriority")
        self._LazyMode = params.get("LazyMode")
        self._MasterLocator = params.get("MasterLocator")
        self._MaxInMemoryLength = params.get("MaxInMemoryLength")
        self._MaxInMemoryBytes = params.get("MaxInMemoryBytes")
        self._Node = params.get("Node")
        self._DeadLetterStrategy = params.get("DeadLetterStrategy")
        self._QueueLeaderLocator = params.get("QueueLeaderLocator")
        self._QuorumInitialGroupSize = params.get("QuorumInitialGroupSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessQueueResponse(AbstractModel):
    """CreateRabbitMQServerlessQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueName = None
        self._RequestId = None

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessUserRequest(AbstractModel):
    """CreateRabbitMQServerlessUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，登录时使用
        :type User: str
        :param _Password: 密码，登录时使用
        :type Password: str
        :param _Description: 描述
        :type Description: str
        :param _Tags: serverless 实例该字段无效
        :type Tags: list of str
        :param _MaxConnections: 该用户的最大连接数，不填写则不限制
        :type MaxConnections: int
        :param _MaxChannels: 该用户的最大channel数，不填写则不限制
        :type MaxChannels: int
        """
        self._InstanceId = None
        self._User = None
        self._Password = None
        self._Description = None
        self._Tags = None
        self._MaxConnections = None
        self._MaxChannels = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名，登录时使用
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """密码，登录时使用
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        """serverless 实例该字段无效
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MaxConnections(self):
        """该用户的最大连接数，不填写则不限制
        :rtype: int
        """
        return self._MaxConnections

    @MaxConnections.setter
    def MaxConnections(self, MaxConnections):
        self._MaxConnections = MaxConnections

    @property
    def MaxChannels(self):
        """该用户的最大channel数，不填写则不限制
        :rtype: int
        """
        return self._MaxChannels

    @MaxChannels.setter
    def MaxChannels(self, MaxChannels):
        self._MaxChannels = MaxChannels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._MaxConnections = params.get("MaxConnections")
        self._MaxChannels = params.get("MaxChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessUserResponse(AbstractModel):
    """CreateRabbitMQServerlessUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _User: 用户名，登录时使用
        :type User: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._User = None
        self._RequestId = None

    @property
    def User(self):
        """用户名，登录时使用
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._User = params.get("User")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQServerlessVirtualHostRequest(AbstractModel):
    """CreateRabbitMQServerlessVirtualHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _VirtualHost: vhost名称
        :type VirtualHost: str
        :param _Description: 描述信息
        :type Description: str
        :param _TraceFlag: 消息轨迹开关,true打开,false关闭,默认关闭
        :type TraceFlag: bool
        :param _MirrorQueuePolicyFlag: 是否创建镜像队列策略，默认值 true
        :type MirrorQueuePolicyFlag: bool
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Description = None
        self._TraceFlag = None
        self._MirrorQueuePolicyFlag = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost名称
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Description(self):
        """描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceFlag(self):
        """消息轨迹开关,true打开,false关闭,默认关闭
        :rtype: bool
        """
        return self._TraceFlag

    @TraceFlag.setter
    def TraceFlag(self, TraceFlag):
        self._TraceFlag = TraceFlag

    @property
    def MirrorQueuePolicyFlag(self):
        """是否创建镜像队列策略，默认值 true
        :rtype: bool
        """
        return self._MirrorQueuePolicyFlag

    @MirrorQueuePolicyFlag.setter
    def MirrorQueuePolicyFlag(self, MirrorQueuePolicyFlag):
        self._MirrorQueuePolicyFlag = MirrorQueuePolicyFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Description = params.get("Description")
        self._TraceFlag = params.get("TraceFlag")
        self._MirrorQueuePolicyFlag = params.get("MirrorQueuePolicyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQServerlessVirtualHostResponse(AbstractModel):
    """CreateRabbitMQServerlessVirtualHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VirtualHost: vhost名称
        :type VirtualHost: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VirtualHost = None
        self._RequestId = None

    @property
    def VirtualHost(self):
        """vhost名称
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VirtualHost = params.get("VirtualHost")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessBindingRequest(AbstractModel):
    """DeleteRabbitMQServerlessBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _BindingId: 路由关系Id
        :type BindingId: int
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._BindingId = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def BindingId(self):
        """路由关系Id
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._BindingId = params.get("BindingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessBindingResponse(AbstractModel):
    """DeleteRabbitMQServerlessBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 队列名称
        :type InstanceId: str
        :param _VirtualHost: vhost参数
        :type VirtualHost: str
        :param _BindingId: 路由关系Id
        :type BindingId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._BindingId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """队列名称
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def BindingId(self):
        """路由关系Id
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._BindingId = params.get("BindingId")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessExchangeRequest(AbstractModel):
    """DeleteRabbitMQServerlessExchange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 id
        :type InstanceId: str
        :param _VirtualHost: vhost 参数
        :type VirtualHost: str
        :param _ExchangeName: exchange 名称
        :type ExchangeName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None

    @property
    def InstanceId(self):
        """实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost 参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        """exchange 名称
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessExchangeResponse(AbstractModel):
    """DeleteRabbitMQServerlessExchange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange 名称
        :type ExchangeName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExchangeName = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        """exchange 名称
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExchangeName = params.get("ExchangeName")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessPermissionRequest(AbstractModel):
    """DeleteRabbitMQServerlessPermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，登录时使用
        :type User: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名，登录时使用
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessPermissionResponse(AbstractModel):
    """DeleteRabbitMQServerlessPermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessQueueRequest(AbstractModel):
    """DeleteRabbitMQServerlessQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _QueueName: 队列名称
        :type QueueName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessQueueResponse(AbstractModel):
    """DeleteRabbitMQServerlessQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueName = None
        self._RequestId = None

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessUserRequest(AbstractModel):
    """DeleteRabbitMQServerlessUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，登录时使用
        :type User: str
        """
        self._InstanceId = None
        self._User = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名，登录时使用
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessUserResponse(AbstractModel):
    """DeleteRabbitMQServerlessUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQServerlessVirtualHostRequest(AbstractModel):
    """DeleteRabbitMQServerlessVirtualHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        """
        self._InstanceId = None
        self._VirtualHost = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQServerlessVirtualHostResponse(AbstractModel):
    """DeleteRabbitMQServerlessVirtualHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessBindingsRequest(AbstractModel):
    """DescribeRabbitMQServerlessBindings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _Offset: 分页offset
        :type Offset: int
        :param _Limit: 分页limit
        :type Limit: int
        :param _SearchWord: 搜索关键词，根据源exchange名称/目标资源名称/绑定key进行模糊搜索
        :type SearchWord: str
        :param _SourceExchange: 根据源Exchange精准搜索过滤
        :type SourceExchange: str
        :param _QueueName: 根据目标QueueName精准搜索过滤，和DestinationExchange过滤不可同时设置
        :type QueueName: str
        :param _DestinationExchange: 根据目标Exchange精准搜索过滤，和QueueName过滤不可同时设置
        :type DestinationExchange: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._SourceExchange = None
        self._QueueName = None
        self._DestinationExchange = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        """分页offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """搜索关键词，根据源exchange名称/目标资源名称/绑定key进行模糊搜索
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def SourceExchange(self):
        """根据源Exchange精准搜索过滤
        :rtype: str
        """
        return self._SourceExchange

    @SourceExchange.setter
    def SourceExchange(self, SourceExchange):
        self._SourceExchange = SourceExchange

    @property
    def QueueName(self):
        """根据目标QueueName精准搜索过滤，和DestinationExchange过滤不可同时设置
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def DestinationExchange(self):
        """根据目标Exchange精准搜索过滤，和QueueName过滤不可同时设置
        :rtype: str
        """
        return self._DestinationExchange

    @DestinationExchange.setter
    def DestinationExchange(self, DestinationExchange):
        self._DestinationExchange = DestinationExchange


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        self._SourceExchange = params.get("SourceExchange")
        self._QueueName = params.get("QueueName")
        self._DestinationExchange = params.get("DestinationExchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessBindingsResponse(AbstractModel):
    """DescribeRabbitMQServerlessBindings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindingInfoList: 路由关系列表
        :type BindingInfoList: list of RabbitMQBindingListInfo
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindingInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BindingInfoList(self):
        """路由关系列表
        :rtype: list of RabbitMQBindingListInfo
        """
        return self._BindingInfoList

    @BindingInfoList.setter
    def BindingInfoList(self, BindingInfoList):
        self._BindingInfoList = BindingInfoList

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BindingInfoList") is not None:
            self._BindingInfoList = []
            for item in params.get("BindingInfoList"):
                obj = RabbitMQBindingListInfo()
                obj._deserialize(item)
                self._BindingInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessConnectionRequest(AbstractModel):
    """DescribeRabbitMQServerlessConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id	
        :type InstanceId: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        """
        self._InstanceId = None
        self._VirtualHost = None

    @property
    def InstanceId(self):
        """集群实例Id	
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessConnectionResponse(AbstractModel):
    """DescribeRabbitMQServerlessConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回连接数量
        :type TotalCount: int
        :param _Connections: 连接详情列表
        :type Connections: list of RabbitMQConnection
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Connections = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回连接数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Connections(self):
        """连接详情列表
        :rtype: list of RabbitMQConnection
        """
        return self._Connections

    @Connections.setter
    def Connections(self, Connections):
        self._Connections = Connections

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Connections") is not None:
            self._Connections = []
            for item in params.get("Connections"):
                obj = RabbitMQConnection()
                obj._deserialize(item)
                self._Connections.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessConsumersRequest(AbstractModel):
    """DescribeRabbitMQServerlessConsumers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _QueueName: 队列名
        :type QueueName: str
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Offset: 分页Offset
        :type Offset: int
        :param _SearchWord: 搜索关键词
        :type SearchWord: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._Limit = None
        self._Offset = None
        self._SearchWord = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        """队列名
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Limit(self):
        """分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SearchWord(self):
        """搜索关键词
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessConsumersResponse(AbstractModel):
    """DescribeRabbitMQServerlessConsumers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsumerInfoList: 消费者列表信息
        :type ConsumerInfoList: list of RabbitMQConsumersListInfo
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConsumerInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConsumerInfoList(self):
        """消费者列表信息
        :rtype: list of RabbitMQConsumersListInfo
        """
        return self._ConsumerInfoList

    @ConsumerInfoList.setter
    def ConsumerInfoList(self, ConsumerInfoList):
        self._ConsumerInfoList = ConsumerInfoList

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConsumerInfoList") is not None:
            self._ConsumerInfoList = []
            for item in params.get("ConsumerInfoList"):
                obj = RabbitMQConsumersListInfo()
                obj._deserialize(item)
                self._ConsumerInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessExchangeDetailRequest(AbstractModel):
    """DescribeRabbitMQServerlessExchangeDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 id
        :type InstanceId: str
        :param _VirtualHost: vhost 参数
        :type VirtualHost: str
        :param _ExchangeName: exchange 名称
        :type ExchangeName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None

    @property
    def InstanceId(self):
        """实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost 参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        """exchange 名称
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessExchangeDetailResponse(AbstractModel):
    """DescribeRabbitMQServerlessExchangeDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange 名
        :type ExchangeName: str
        :param _Remark: 备注说明
        :type Remark: str
        :param _Durable: 是否为持久化 exchange, 当集群重启时, 将会清除所有该字段为 "false" 的 exchange
        :type Durable: bool
        :param _AutoDelete: 是否自动删除该 exchange, 如果为 "true", 当解绑所有当前 exchange 上的路由关系时, 该 exchange 将会被自动删除
        :type AutoDelete: bool
        :param _Internal: 是否为内部 exchange, 如果为 "true", 则无法直接投递消息到该 exchange, 需要在路由设置中通过其他 exchange 进行转发
        :type Internal: bool
        :param _AlternateExchange: 替代 exchange, 如果消息没有匹配当前 exchange 绑定的所有 queue 或 exchange, 就会发送到该替代 exchange
        :type AlternateExchange: str
        :param _ExchangeType: exchange 类型, 支持 "fanout","direct","topic","headers"
        :type ExchangeType: str
        :param _VirtualHost: VHost参数
        :type VirtualHost: str
        :param _ExchangeCreator: exchange 创建者, "system":"系统创建", "user":"用户创建"
        :type ExchangeCreator: str
        :param _Arguments: 扩展参数 key-value 字符串
        :type Arguments: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExchangeName = None
        self._Remark = None
        self._Durable = None
        self._AutoDelete = None
        self._Internal = None
        self._AlternateExchange = None
        self._ExchangeType = None
        self._VirtualHost = None
        self._ExchangeCreator = None
        self._Arguments = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        """exchange 名
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def Remark(self):
        """备注说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Durable(self):
        """是否为持久化 exchange, 当集群重启时, 将会清除所有该字段为 "false" 的 exchange
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        """是否自动删除该 exchange, 如果为 "true", 当解绑所有当前 exchange 上的路由关系时, 该 exchange 将会被自动删除
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Internal(self):
        """是否为内部 exchange, 如果为 "true", 则无法直接投递消息到该 exchange, 需要在路由设置中通过其他 exchange 进行转发
        :rtype: bool
        """
        return self._Internal

    @Internal.setter
    def Internal(self, Internal):
        self._Internal = Internal

    @property
    def AlternateExchange(self):
        """替代 exchange, 如果消息没有匹配当前 exchange 绑定的所有 queue 或 exchange, 就会发送到该替代 exchange
        :rtype: str
        """
        return self._AlternateExchange

    @AlternateExchange.setter
    def AlternateExchange(self, AlternateExchange):
        self._AlternateExchange = AlternateExchange

    @property
    def ExchangeType(self):
        """exchange 类型, 支持 "fanout","direct","topic","headers"
        :rtype: str
        """
        return self._ExchangeType

    @ExchangeType.setter
    def ExchangeType(self, ExchangeType):
        self._ExchangeType = ExchangeType

    @property
    def VirtualHost(self):
        """VHost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeCreator(self):
        """exchange 创建者, "system":"系统创建", "user":"用户创建"
        :rtype: str
        """
        return self._ExchangeCreator

    @ExchangeCreator.setter
    def ExchangeCreator(self, ExchangeCreator):
        self._ExchangeCreator = ExchangeCreator

    @property
    def Arguments(self):
        """扩展参数 key-value 字符串
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExchangeName = params.get("ExchangeName")
        self._Remark = params.get("Remark")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Internal = params.get("Internal")
        self._AlternateExchange = params.get("AlternateExchange")
        self._ExchangeType = params.get("ExchangeType")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeCreator = params.get("ExchangeCreator")
        self._Arguments = params.get("Arguments")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessExchangesRequest(AbstractModel):
    """DescribeRabbitMQServerlessExchanges请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 id
        :type InstanceId: str
        :param _VirtualHost: vhost 参数
        :type VirtualHost: str
        :param _Offset: 分页 offset
        :type Offset: int
        :param _Limit: 分页 limit
        :type Limit: int
        :param _SearchWord: 搜索关键词, 支持模糊匹配 
        :type SearchWord: str
        :param _ExchangeTypeFilters: 筛选 exchange 类型, 数组中每个元素为选中的过滤类型
        :type ExchangeTypeFilters: list of str
        :param _ExchangeCreatorFilters: 筛选 exchange 创建来源,  "system":"系统创建", "user":"用户创建"
        :type ExchangeCreatorFilters: list of str
        :param _ExchangeName: exchange 名称，用于精确匹配
        :type ExchangeName: str
        :param _SortElement: 排序依据的字段：
MessageRateInOut - 生产消费速率之和；
MessageRateIn - 生产速率；
MessageRateOut - 消费速率；
        :type SortElement: str
        :param _SortOrder: 排序顺序，ascend 或 descend
        :type SortOrder: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._ExchangeTypeFilters = None
        self._ExchangeCreatorFilters = None
        self._ExchangeName = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        """实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost 参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        """分页 offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页 limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """搜索关键词, 支持模糊匹配 
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def ExchangeTypeFilters(self):
        """筛选 exchange 类型, 数组中每个元素为选中的过滤类型
        :rtype: list of str
        """
        return self._ExchangeTypeFilters

    @ExchangeTypeFilters.setter
    def ExchangeTypeFilters(self, ExchangeTypeFilters):
        self._ExchangeTypeFilters = ExchangeTypeFilters

    @property
    def ExchangeCreatorFilters(self):
        """筛选 exchange 创建来源,  "system":"系统创建", "user":"用户创建"
        :rtype: list of str
        """
        return self._ExchangeCreatorFilters

    @ExchangeCreatorFilters.setter
    def ExchangeCreatorFilters(self, ExchangeCreatorFilters):
        self._ExchangeCreatorFilters = ExchangeCreatorFilters

    @property
    def ExchangeName(self):
        """exchange 名称，用于精确匹配
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def SortElement(self):
        """排序依据的字段：
MessageRateInOut - 生产消费速率之和；
MessageRateIn - 生产速率；
MessageRateOut - 消费速率；
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        """排序顺序，ascend 或 descend
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        self._ExchangeTypeFilters = params.get("ExchangeTypeFilters")
        self._ExchangeCreatorFilters = params.get("ExchangeCreatorFilters")
        self._ExchangeName = params.get("ExchangeName")
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessExchangesResponse(AbstractModel):
    """DescribeRabbitMQServerlessExchanges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExchangeInfoList: 交换机列表
        :type ExchangeInfoList: list of RabbitMQExchangeListInfo
        :param _TotalCount: 交换机总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExchangeInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ExchangeInfoList(self):
        """交换机列表
        :rtype: list of RabbitMQExchangeListInfo
        """
        return self._ExchangeInfoList

    @ExchangeInfoList.setter
    def ExchangeInfoList(self, ExchangeInfoList):
        self._ExchangeInfoList = ExchangeInfoList

    @property
    def TotalCount(self):
        """交换机总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ExchangeInfoList") is not None:
            self._ExchangeInfoList = []
            for item in params.get("ExchangeInfoList"):
                obj = RabbitMQExchangeListInfo()
                obj._deserialize(item)
                self._ExchangeInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessInstanceRequest(AbstractModel):
    """DescribeRabbitMQServerlessInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessInstanceResponse(AbstractModel):
    """DescribeRabbitMQServerlessInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: 集群信息
        :type ClusterInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterInfo`
        :param _ClusterSpecInfo: 集群规格信息
        :type ClusterSpecInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterSpecInfo`
        :param _VirtualHostQuota: vhost配额信息
        :type VirtualHostQuota: :class:`tencentcloud.trabbit.v20230418.models.VirtualHostQuota`
        :param _ExchangeQuota: exchange配额信息
        :type ExchangeQuota: :class:`tencentcloud.trabbit.v20230418.models.ExchangeQuota`
        :param _QueueQuota: queue配额信息
        :type QueueQuota: :class:`tencentcloud.trabbit.v20230418.models.QueueQuota`
        :param _ClusterNetInfo: 网络信息
        :type ClusterNetInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessAccessInfo`
        :param _ClusterWhiteListInfo: 公网白名单信息
        :type ClusterWhiteListInfo: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessWhiteListInfo`
        :param _UserQuota: user配额信息
        :type UserQuota: :class:`tencentcloud.trabbit.v20230418.models.UserQuota`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._ClusterSpecInfo = None
        self._VirtualHostQuota = None
        self._ExchangeQuota = None
        self._QueueQuota = None
        self._ClusterNetInfo = None
        self._ClusterWhiteListInfo = None
        self._UserQuota = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        """集群信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterInfo`
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def ClusterSpecInfo(self):
        """集群规格信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQClusterSpecInfo`
        """
        return self._ClusterSpecInfo

    @ClusterSpecInfo.setter
    def ClusterSpecInfo(self, ClusterSpecInfo):
        self._ClusterSpecInfo = ClusterSpecInfo

    @property
    def VirtualHostQuota(self):
        """vhost配额信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.VirtualHostQuota`
        """
        return self._VirtualHostQuota

    @VirtualHostQuota.setter
    def VirtualHostQuota(self, VirtualHostQuota):
        self._VirtualHostQuota = VirtualHostQuota

    @property
    def ExchangeQuota(self):
        """exchange配额信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.ExchangeQuota`
        """
        return self._ExchangeQuota

    @ExchangeQuota.setter
    def ExchangeQuota(self, ExchangeQuota):
        self._ExchangeQuota = ExchangeQuota

    @property
    def QueueQuota(self):
        """queue配额信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.QueueQuota`
        """
        return self._QueueQuota

    @QueueQuota.setter
    def QueueQuota(self, QueueQuota):
        self._QueueQuota = QueueQuota

    @property
    def ClusterNetInfo(self):
        """网络信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessAccessInfo`
        """
        return self._ClusterNetInfo

    @ClusterNetInfo.setter
    def ClusterNetInfo(self, ClusterNetInfo):
        self._ClusterNetInfo = ClusterNetInfo

    @property
    def ClusterWhiteListInfo(self):
        """公网白名单信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQServerlessWhiteListInfo`
        """
        return self._ClusterWhiteListInfo

    @ClusterWhiteListInfo.setter
    def ClusterWhiteListInfo(self, ClusterWhiteListInfo):
        self._ClusterWhiteListInfo = ClusterWhiteListInfo

    @property
    def UserQuota(self):
        """user配额信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.UserQuota`
        """
        return self._UserQuota

    @UserQuota.setter
    def UserQuota(self, UserQuota):
        self._UserQuota = UserQuota

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterInfo") is not None:
            self._ClusterInfo = RabbitMQClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("ClusterSpecInfo") is not None:
            self._ClusterSpecInfo = RabbitMQClusterSpecInfo()
            self._ClusterSpecInfo._deserialize(params.get("ClusterSpecInfo"))
        if params.get("VirtualHostQuota") is not None:
            self._VirtualHostQuota = VirtualHostQuota()
            self._VirtualHostQuota._deserialize(params.get("VirtualHostQuota"))
        if params.get("ExchangeQuota") is not None:
            self._ExchangeQuota = ExchangeQuota()
            self._ExchangeQuota._deserialize(params.get("ExchangeQuota"))
        if params.get("QueueQuota") is not None:
            self._QueueQuota = QueueQuota()
            self._QueueQuota._deserialize(params.get("QueueQuota"))
        if params.get("ClusterNetInfo") is not None:
            self._ClusterNetInfo = RabbitMQServerlessAccessInfo()
            self._ClusterNetInfo._deserialize(params.get("ClusterNetInfo"))
        if params.get("ClusterWhiteListInfo") is not None:
            self._ClusterWhiteListInfo = RabbitMQServerlessWhiteListInfo()
            self._ClusterWhiteListInfo._deserialize(params.get("ClusterWhiteListInfo"))
        if params.get("UserQuota") is not None:
            self._UserQuota = UserQuota()
            self._UserQuota._deserialize(params.get("UserQuota"))
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessPermissionRequest(AbstractModel):
    """DescribeRabbitMQServerlessPermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例id
        :type InstanceId: str
        :param _User: 用户名，用于查询过滤，不传则查询全部
        :type User: str
        :param _VirtualHost: vhost名，用于查询过滤，不传则查询全部
        :type VirtualHost: str
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Limit: 分页Limit
        :type Limit: int
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """集群实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名，用于查询过滤，不传则查询全部
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        """vhost名，用于查询过滤，不传则查询全部
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        """分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessPermissionResponse(AbstractModel):
    """DescribeRabbitMQServerlessPermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回权限数量
        :type TotalCount: int
        :param _RabbitMQPermissionList: 权限详情列表
        :type RabbitMQPermissionList: list of RabbitMQPermission
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RabbitMQPermissionList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回权限数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RabbitMQPermissionList(self):
        """权限详情列表
        :rtype: list of RabbitMQPermission
        """
        return self._RabbitMQPermissionList

    @RabbitMQPermissionList.setter
    def RabbitMQPermissionList(self, RabbitMQPermissionList):
        self._RabbitMQPermissionList = RabbitMQPermissionList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RabbitMQPermissionList") is not None:
            self._RabbitMQPermissionList = []
            for item in params.get("RabbitMQPermissionList"):
                obj = RabbitMQPermission()
                obj._deserialize(item)
                self._RabbitMQPermissionList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessQueueDetailRequest(AbstractModel):
    """DescribeRabbitMQServerlessQueueDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _QueueName: 队列名称
        :type QueueName: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessQueueDetailResponse(AbstractModel):
    """DescribeRabbitMQServerlessQueueDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _QueueType: 队列类型,取值classic或quorum
        :type QueueType: str
        :param _Consumers: 在线消费者数量
        :type Consumers: int
        :param _Durable: 持久标记
        :type Durable: bool
        :param _AutoDelete: 自动清除
        :type AutoDelete: bool
        :param _Remark: 备注
        :type Remark: str
        :param _MessageTTL: MessageTTL参数,classic类型专用
        :type MessageTTL: int
        :param _AutoExpire: AutoExpire参数
        :type AutoExpire: int
        :param _MaxLength: MaxLength参数
        :type MaxLength: int
        :param _MaxLengthBytes: MaxLengthBytes参数
        :type MaxLengthBytes: int
        :param _DeliveryLimit: DeliveryLimit参数,quorum类型专用
        :type DeliveryLimit: int
        :param _OverflowBehaviour: OverflowBehaviour参数,取值为drop-head, reject-publish或reject-publish-dlx
        :type OverflowBehaviour: str
        :param _DeadLetterExchange: DeadLetterExchange参数
        :type DeadLetterExchange: str
        :param _DeadLetterRoutingKey: DeadLetterRoutingKey参数
        :type DeadLetterRoutingKey: str
        :param _SingleActiveConsumer: SingleActiveConsumer参数
        :type SingleActiveConsumer: bool
        :param _MaximumPriority: MaximumPriority参数,classic类型专用
        :type MaximumPriority: int
        :param _LazyMode: LazyMode参数,classic类型专用
        :type LazyMode: bool
        :param _MasterLocator: MasterLocator参数,classic类型专用
        :type MasterLocator: str
        :param _MaxInMemoryLength: MaxInMemoryLength参数,quorum类型专用
        :type MaxInMemoryLength: int
        :param _MaxInMemoryBytes: MaxInMemoryBytes参数,quorum类型专用
        :type MaxInMemoryBytes: int
        :param _CreateTime: 创建时间戳,单位秒
        :type CreateTime: int
        :param _Node: 节点
        :type Node: str
        :param _DeadLetterStrategy: 仲裁队列死信一致性策略
        :type DeadLetterStrategy: str
        :param _QueueLeaderLocator: 仲裁队列的领导者选举策略
        :type QueueLeaderLocator: str
        :param _QuorumInitialGroupSize: 仲裁队列的初始副本组大小
        :type QuorumInitialGroupSize: int
        :param _Exclusive: 是否为独占队列
        :type Exclusive: bool
        :param _Policy: 生效的策略名
        :type Policy: str
        :param _Arguments: 扩展参数 key-value
        :type Arguments: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._QueueType = None
        self._Consumers = None
        self._Durable = None
        self._AutoDelete = None
        self._Remark = None
        self._MessageTTL = None
        self._AutoExpire = None
        self._MaxLength = None
        self._MaxLengthBytes = None
        self._DeliveryLimit = None
        self._OverflowBehaviour = None
        self._DeadLetterExchange = None
        self._DeadLetterRoutingKey = None
        self._SingleActiveConsumer = None
        self._MaximumPriority = None
        self._LazyMode = None
        self._MasterLocator = None
        self._MaxInMemoryLength = None
        self._MaxInMemoryBytes = None
        self._CreateTime = None
        self._Node = None
        self._DeadLetterStrategy = None
        self._QueueLeaderLocator = None
        self._QuorumInitialGroupSize = None
        self._Exclusive = None
        self._Policy = None
        self._Arguments = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def QueueType(self):
        """队列类型,取值classic或quorum
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def Consumers(self):
        """在线消费者数量
        :rtype: int
        """
        return self._Consumers

    @Consumers.setter
    def Consumers(self, Consumers):
        self._Consumers = Consumers

    @property
    def Durable(self):
        """持久标记
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        """自动清除
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageTTL(self):
        """MessageTTL参数,classic类型专用
        :rtype: int
        """
        return self._MessageTTL

    @MessageTTL.setter
    def MessageTTL(self, MessageTTL):
        self._MessageTTL = MessageTTL

    @property
    def AutoExpire(self):
        """AutoExpire参数
        :rtype: int
        """
        return self._AutoExpire

    @AutoExpire.setter
    def AutoExpire(self, AutoExpire):
        self._AutoExpire = AutoExpire

    @property
    def MaxLength(self):
        """MaxLength参数
        :rtype: int
        """
        return self._MaxLength

    @MaxLength.setter
    def MaxLength(self, MaxLength):
        self._MaxLength = MaxLength

    @property
    def MaxLengthBytes(self):
        """MaxLengthBytes参数
        :rtype: int
        """
        return self._MaxLengthBytes

    @MaxLengthBytes.setter
    def MaxLengthBytes(self, MaxLengthBytes):
        self._MaxLengthBytes = MaxLengthBytes

    @property
    def DeliveryLimit(self):
        """DeliveryLimit参数,quorum类型专用
        :rtype: int
        """
        return self._DeliveryLimit

    @DeliveryLimit.setter
    def DeliveryLimit(self, DeliveryLimit):
        self._DeliveryLimit = DeliveryLimit

    @property
    def OverflowBehaviour(self):
        """OverflowBehaviour参数,取值为drop-head, reject-publish或reject-publish-dlx
        :rtype: str
        """
        return self._OverflowBehaviour

    @OverflowBehaviour.setter
    def OverflowBehaviour(self, OverflowBehaviour):
        self._OverflowBehaviour = OverflowBehaviour

    @property
    def DeadLetterExchange(self):
        """DeadLetterExchange参数
        :rtype: str
        """
        return self._DeadLetterExchange

    @DeadLetterExchange.setter
    def DeadLetterExchange(self, DeadLetterExchange):
        self._DeadLetterExchange = DeadLetterExchange

    @property
    def DeadLetterRoutingKey(self):
        """DeadLetterRoutingKey参数
        :rtype: str
        """
        return self._DeadLetterRoutingKey

    @DeadLetterRoutingKey.setter
    def DeadLetterRoutingKey(self, DeadLetterRoutingKey):
        self._DeadLetterRoutingKey = DeadLetterRoutingKey

    @property
    def SingleActiveConsumer(self):
        """SingleActiveConsumer参数
        :rtype: bool
        """
        return self._SingleActiveConsumer

    @SingleActiveConsumer.setter
    def SingleActiveConsumer(self, SingleActiveConsumer):
        self._SingleActiveConsumer = SingleActiveConsumer

    @property
    def MaximumPriority(self):
        """MaximumPriority参数,classic类型专用
        :rtype: int
        """
        return self._MaximumPriority

    @MaximumPriority.setter
    def MaximumPriority(self, MaximumPriority):
        self._MaximumPriority = MaximumPriority

    @property
    def LazyMode(self):
        """LazyMode参数,classic类型专用
        :rtype: bool
        """
        return self._LazyMode

    @LazyMode.setter
    def LazyMode(self, LazyMode):
        self._LazyMode = LazyMode

    @property
    def MasterLocator(self):
        """MasterLocator参数,classic类型专用
        :rtype: str
        """
        return self._MasterLocator

    @MasterLocator.setter
    def MasterLocator(self, MasterLocator):
        self._MasterLocator = MasterLocator

    @property
    def MaxInMemoryLength(self):
        """MaxInMemoryLength参数,quorum类型专用
        :rtype: int
        """
        return self._MaxInMemoryLength

    @MaxInMemoryLength.setter
    def MaxInMemoryLength(self, MaxInMemoryLength):
        self._MaxInMemoryLength = MaxInMemoryLength

    @property
    def MaxInMemoryBytes(self):
        """MaxInMemoryBytes参数,quorum类型专用
        :rtype: int
        """
        return self._MaxInMemoryBytes

    @MaxInMemoryBytes.setter
    def MaxInMemoryBytes(self, MaxInMemoryBytes):
        self._MaxInMemoryBytes = MaxInMemoryBytes

    @property
    def CreateTime(self):
        """创建时间戳,单位秒
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Node(self):
        """节点
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def DeadLetterStrategy(self):
        """仲裁队列死信一致性策略
        :rtype: str
        """
        return self._DeadLetterStrategy

    @DeadLetterStrategy.setter
    def DeadLetterStrategy(self, DeadLetterStrategy):
        self._DeadLetterStrategy = DeadLetterStrategy

    @property
    def QueueLeaderLocator(self):
        """仲裁队列的领导者选举策略
        :rtype: str
        """
        return self._QueueLeaderLocator

    @QueueLeaderLocator.setter
    def QueueLeaderLocator(self, QueueLeaderLocator):
        self._QueueLeaderLocator = QueueLeaderLocator

    @property
    def QuorumInitialGroupSize(self):
        """仲裁队列的初始副本组大小
        :rtype: int
        """
        return self._QuorumInitialGroupSize

    @QuorumInitialGroupSize.setter
    def QuorumInitialGroupSize(self, QuorumInitialGroupSize):
        self._QuorumInitialGroupSize = QuorumInitialGroupSize

    @property
    def Exclusive(self):
        """是否为独占队列
        :rtype: bool
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive

    @property
    def Policy(self):
        """生效的策略名
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Arguments(self):
        """扩展参数 key-value
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._QueueType = params.get("QueueType")
        self._Consumers = params.get("Consumers")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Remark = params.get("Remark")
        self._MessageTTL = params.get("MessageTTL")
        self._AutoExpire = params.get("AutoExpire")
        self._MaxLength = params.get("MaxLength")
        self._MaxLengthBytes = params.get("MaxLengthBytes")
        self._DeliveryLimit = params.get("DeliveryLimit")
        self._OverflowBehaviour = params.get("OverflowBehaviour")
        self._DeadLetterExchange = params.get("DeadLetterExchange")
        self._DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        self._SingleActiveConsumer = params.get("SingleActiveConsumer")
        self._MaximumPriority = params.get("MaximumPriority")
        self._LazyMode = params.get("LazyMode")
        self._MasterLocator = params.get("MasterLocator")
        self._MaxInMemoryLength = params.get("MaxInMemoryLength")
        self._MaxInMemoryBytes = params.get("MaxInMemoryBytes")
        self._CreateTime = params.get("CreateTime")
        self._Node = params.get("Node")
        self._DeadLetterStrategy = params.get("DeadLetterStrategy")
        self._QueueLeaderLocator = params.get("QueueLeaderLocator")
        self._QuorumInitialGroupSize = params.get("QuorumInitialGroupSize")
        self._Exclusive = params.get("Exclusive")
        self._Policy = params.get("Policy")
        self._Arguments = params.get("Arguments")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessQueuesRequest(AbstractModel):
    """DescribeRabbitMQServerlessQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Limit: 分页Limit
        :type Limit: int
        :param _SearchWord: 搜索关键词
        :type SearchWord: str
        :param _QueueType: 队列类型筛选，不填或 "all"：classic 和 quorum 队列；"classic"：筛选 classic 队列；"quorum"：筛选 quorum 队列
        :type QueueType: str
        :param _SortElement: 排序依据的字段：
ConsumerNumber - 在线消费者数量；
MessageHeapCount - 消息堆积数；
MessageRateInOut - 生产消费速率之和；
MessageRateIn - 生产速率；
MessageRateOut - 消费速率；
        :type SortElement: str
        :param _SortOrder: 排序顺序，ascend 或 descend
        :type SortOrder: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._QueueType = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        """分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """搜索关键词
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def QueueType(self):
        """队列类型筛选，不填或 "all"：classic 和 quorum 队列；"classic"：筛选 classic 队列；"quorum"：筛选 quorum 队列
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def SortElement(self):
        """排序依据的字段：
ConsumerNumber - 在线消费者数量；
MessageHeapCount - 消息堆积数；
MessageRateInOut - 生产消费速率之和；
MessageRateIn - 生产速率；
MessageRateOut - 消费速率；
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        """排序顺序，ascend 或 descend
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        self._QueueType = params.get("QueueType")
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessQueuesResponse(AbstractModel):
    """DescribeRabbitMQServerlessQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueInfoList: 队列列表信息
        :type QueueInfoList: list of RabbitMQQueueListInfo
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def QueueInfoList(self):
        """队列列表信息
        :rtype: list of RabbitMQQueueListInfo
        """
        return self._QueueInfoList

    @QueueInfoList.setter
    def QueueInfoList(self, QueueInfoList):
        self._QueueInfoList = QueueInfoList

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QueueInfoList") is not None:
            self._QueueInfoList = []
            for item in params.get("QueueInfoList"):
                obj = RabbitMQQueueListInfo()
                obj._deserialize(item)
                self._QueueInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessUserRequest(AbstractModel):
    """DescribeRabbitMQServerlessUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _SearchUser: 用户名检索，支持前缀匹配，后缀匹配
        :type SearchUser: str
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Limit: 分页Limit
        :type Limit: int
        :param _User: 用户名，精确查询
        :type User: str
        :param _Tags: 用户标签，根据标签过滤列表
        :type Tags: list of str
        """
        self._InstanceId = None
        self._SearchUser = None
        self._Offset = None
        self._Limit = None
        self._User = None
        self._Tags = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SearchUser(self):
        """用户名检索，支持前缀匹配，后缀匹配
        :rtype: str
        """
        return self._SearchUser

    @SearchUser.setter
    def SearchUser(self, SearchUser):
        self._SearchUser = SearchUser

    @property
    def Offset(self):
        """分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def User(self):
        """用户名，精确查询
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Tags(self):
        """用户标签，根据标签过滤列表
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SearchUser = params.get("SearchUser")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._User = params.get("User")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessUserResponse(AbstractModel):
    """DescribeRabbitMQServerlessUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的User数量
        :type TotalCount: int
        :param _RabbitMQUserList: 当前已创建的RabbitMQ用户列表
        :type RabbitMQUserList: list of RabbitMQUser
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RabbitMQUserList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的User数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RabbitMQUserList(self):
        """当前已创建的RabbitMQ用户列表
        :rtype: list of RabbitMQUser
        """
        return self._RabbitMQUserList

    @RabbitMQUserList.setter
    def RabbitMQUserList(self, RabbitMQUserList):
        self._RabbitMQUserList = RabbitMQUserList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RabbitMQUserList") is not None:
            self._RabbitMQUserList = []
            for item in params.get("RabbitMQUserList"):
                obj = RabbitMQUser()
                obj._deserialize(item)
                self._RabbitMQUserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQServerlessVirtualHostRequest(AbstractModel):
    """DescribeRabbitMQServerlessVirtualHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _VirtualHost: vhost名,不传则查询全部
        :type VirtualHost: str
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Filters: search-virtual-host：vhost名称模糊查询，之前前缀和后缀匹配
        :type Filters: :class:`tencentcloud.trabbit.v20230418.models.Filter`
        :param _SortElement: 排序依据的字段：
MessageHeapCount - 消息堆积数；
MessageRateInOut - 生产消费速率之和；
MessageRateIn - 生产速率；
MessageRateOut - 消费速率；
        :type SortElement: str
        :param _SortOrder: 排序顺序，ascend 或 descend
        :type SortOrder: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost名,不传则查询全部
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Offset(self):
        """分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """search-virtual-host：vhost名称模糊查询，之前前缀和后缀匹配
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.Filter`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortElement(self):
        """排序依据的字段：
MessageHeapCount - 消息堆积数；
MessageRateInOut - 生产消费速率之和；
MessageRateIn - 生产速率；
MessageRateOut - 消费速率；
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        """排序顺序，ascend 或 descend
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = Filter()
            self._Filters._deserialize(params.get("Filters"))
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQServerlessVirtualHostResponse(AbstractModel):
    """DescribeRabbitMQServerlessVirtualHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回vhost数量
        :type TotalCount: int
        :param _VirtualHostList: vhost详情列表
        :type VirtualHostList: list of RabbitMQVirtualHostInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VirtualHostList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回vhost数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VirtualHostList(self):
        """vhost详情列表
        :rtype: list of RabbitMQVirtualHostInfo
        """
        return self._VirtualHostList

    @VirtualHostList.setter
    def VirtualHostList(self, VirtualHostList):
        self._VirtualHostList = VirtualHostList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VirtualHostList") is not None:
            self._VirtualHostList = []
            for item in params.get("VirtualHostList"):
                obj = RabbitMQVirtualHostInfo()
                obj._deserialize(item)
                self._VirtualHostList.append(obj)
        self._RequestId = params.get("RequestId")


class ExchangeQuota(AbstractModel):
    """exchange使用配额信息

    """

    def __init__(self):
        r"""
        :param _MaxExchange: 可创建最大exchange数
        :type MaxExchange: int
        :param _UsedExchange: 已创建exchange数
        :type UsedExchange: int
        """
        self._MaxExchange = None
        self._UsedExchange = None

    @property
    def MaxExchange(self):
        """可创建最大exchange数
        :rtype: int
        """
        return self._MaxExchange

    @MaxExchange.setter
    def MaxExchange(self, MaxExchange):
        self._MaxExchange = MaxExchange

    @property
    def UsedExchange(self):
        """已创建exchange数
        :rtype: int
        """
        return self._UsedExchange

    @UsedExchange.setter
    def UsedExchange(self, UsedExchange):
        self._UsedExchange = UsedExchange


    def _deserialize(self, params):
        self._MaxExchange = params.get("MaxExchange")
        self._UsedExchange = params.get("UsedExchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤参数

    """

    def __init__(self):
        r"""
        :param _Name: 过滤参数的名字
        :type Name: str
        :param _Values: 数值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """过滤参数的名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """数值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRabbitMQServerlessInstancesRequest(AbstractModel):
    """ListRabbitMQServerlessInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Limit: 翻页大小
        :type Limit: int
        :param _Offset: 翻页的起始索引值
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """翻页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """翻页的起始索引值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRabbitMQServerlessInstancesResponse(AbstractModel):
    """ListRabbitMQServerlessInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 实例列表
        :type Instances: list of RabbitMQServerlessInstance
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        """实例列表
        :rtype: list of RabbitMQServerlessInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RabbitMQServerlessInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessExchangeRequest(AbstractModel):
    """ModifyRabbitMQServerlessExchange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 id
        :type InstanceId: str
        :param _VirtualHost: vhost 参数
        :type VirtualHost: str
        :param _ExchangeName: exchange 名称
        :type ExchangeName: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._ExchangeName = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例 id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost 参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeName(self):
        """exchange 名称
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeName = params.get("ExchangeName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessExchangeResponse(AbstractModel):
    """ModifyRabbitMQServerlessExchange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange 名称
        :type ExchangeName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExchangeName = None
        self._RequestId = None

    @property
    def ExchangeName(self):
        """exchange 名称
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExchangeName = params.get("ExchangeName")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessInstanceRequest(AbstractModel):
    """ModifyRabbitMQServerlessInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ClusterName: 集群名
        :type ClusterName: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _TraceFlag: 是否开启trace
        :type TraceFlag: bool
        """
        self._InstanceId = None
        self._ClusterName = None
        self._Remark = None
        self._TraceFlag = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterName(self):
        """集群名
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TraceFlag(self):
        """是否开启trace
        :rtype: bool
        """
        return self._TraceFlag

    @TraceFlag.setter
    def TraceFlag(self, TraceFlag):
        self._TraceFlag = TraceFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._TraceFlag = params.get("TraceFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessInstanceResponse(AbstractModel):
    """ModifyRabbitMQServerlessInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessPermissionRequest(AbstractModel):
    """ModifyRabbitMQServerlessPermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，权限关联的用户
        :type User: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        :param _ConfigRegexp: 权限类型，declare相关操作，该用户可操作该vhost下的资源名称正则表达式
        :type ConfigRegexp: str
        :param _WriteRegexp: 权限类型，消息写入相关操作，该用户可操作该vhost下的资源名称正则表达式
        :type WriteRegexp: str
        :param _ReadRegexp: 权限类型，消息读取相关操作，该用户可操作该vhost下的资源名称正则表达式
        :type ReadRegexp: str
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None
        self._ConfigRegexp = None
        self._WriteRegexp = None
        self._ReadRegexp = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名，权限关联的用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ConfigRegexp(self):
        """权限类型，declare相关操作，该用户可操作该vhost下的资源名称正则表达式
        :rtype: str
        """
        return self._ConfigRegexp

    @ConfigRegexp.setter
    def ConfigRegexp(self, ConfigRegexp):
        self._ConfigRegexp = ConfigRegexp

    @property
    def WriteRegexp(self):
        """权限类型，消息写入相关操作，该用户可操作该vhost下的资源名称正则表达式
        :rtype: str
        """
        return self._WriteRegexp

    @WriteRegexp.setter
    def WriteRegexp(self, WriteRegexp):
        self._WriteRegexp = WriteRegexp

    @property
    def ReadRegexp(self):
        """权限类型，消息读取相关操作，该用户可操作该vhost下的资源名称正则表达式
        :rtype: str
        """
        return self._ReadRegexp

    @ReadRegexp.setter
    def ReadRegexp(self, ReadRegexp):
        self._ReadRegexp = ReadRegexp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        self._ConfigRegexp = params.get("ConfigRegexp")
        self._WriteRegexp = params.get("WriteRegexp")
        self._ReadRegexp = params.get("ReadRegexp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessPermissionResponse(AbstractModel):
    """ModifyRabbitMQServerlessPermission返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessQueueRequest(AbstractModel):
    """ModifyRabbitMQServerlessQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _Remark: 新修改的备注
        :type Remark: str
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._QueueName = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Remark(self):
        """新修改的备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._QueueName = params.get("QueueName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessQueueResponse(AbstractModel):
    """ModifyRabbitMQServerlessQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueName = None
        self._RequestId = None

    @property
    def QueueName(self):
        """队列名称
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessUserRequest(AbstractModel):
    """ModifyRabbitMQServerlessUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名
        :type User: str
        :param _Password: 密码
        :type Password: str
        :param _Description: 描述，不传则不修改
        :type Description: str
        :param _Tags: 用户标签，用于决定改用户访问RabbitMQ Management的权限范围，不传则不修改
        :type Tags: list of str
        :param _MaxConnections: 该用户的最大连接数，不传则不修改
        :type MaxConnections: int
        :param _MaxChannels: 该用户的最大channel数，不传则不修改
        :type MaxChannels: int
        """
        self._InstanceId = None
        self._User = None
        self._Password = None
        self._Description = None
        self._Tags = None
        self._MaxConnections = None
        self._MaxChannels = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        """描述，不传则不修改
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        """用户标签，用于决定改用户访问RabbitMQ Management的权限范围，不传则不修改
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MaxConnections(self):
        """该用户的最大连接数，不传则不修改
        :rtype: int
        """
        return self._MaxConnections

    @MaxConnections.setter
    def MaxConnections(self, MaxConnections):
        self._MaxConnections = MaxConnections

    @property
    def MaxChannels(self):
        """该用户的最大channel数，不传则不修改
        :rtype: int
        """
        return self._MaxChannels

    @MaxChannels.setter
    def MaxChannels(self, MaxChannels):
        self._MaxChannels = MaxChannels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._MaxConnections = params.get("MaxConnections")
        self._MaxChannels = params.get("MaxChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessUserResponse(AbstractModel):
    """ModifyRabbitMQServerlessUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQServerlessVirtualHostRequest(AbstractModel):
    """ModifyRabbitMQServerlessVirtualHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        :param _Description: vhost描述信息
        :type Description: str
        :param _TraceFlag: 消息轨迹开关,true打开,false关闭
        :type TraceFlag: bool
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Description = None
        self._TraceFlag = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Description(self):
        """vhost描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceFlag(self):
        """消息轨迹开关,true打开,false关闭
        :rtype: bool
        """
        return self._TraceFlag

    @TraceFlag.setter
    def TraceFlag(self, TraceFlag):
        self._TraceFlag = TraceFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Description = params.get("Description")
        self._TraceFlag = params.get("TraceFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQServerlessVirtualHostResponse(AbstractModel):
    """ModifyRabbitMQServerlessVirtualHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class QueueQuota(AbstractModel):
    """queue使用配额信息

    """

    def __init__(self):
        r"""
        :param _MaxQueue: 可创建最大Queue数
        :type MaxQueue: int
        :param _UsedQueue: 已创建Queue数
        :type UsedQueue: int
        """
        self._MaxQueue = None
        self._UsedQueue = None

    @property
    def MaxQueue(self):
        """可创建最大Queue数
        :rtype: int
        """
        return self._MaxQueue

    @MaxQueue.setter
    def MaxQueue(self, MaxQueue):
        self._MaxQueue = MaxQueue

    @property
    def UsedQueue(self):
        """已创建Queue数
        :rtype: int
        """
        return self._UsedQueue

    @UsedQueue.setter
    def UsedQueue(self, UsedQueue):
        self._UsedQueue = UsedQueue


    def _deserialize(self, params):
        self._MaxQueue = params.get("MaxQueue")
        self._UsedQueue = params.get("UsedQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQBindingListInfo(AbstractModel):
    """Rabbitmq路由关系列表成员

    """

    def __init__(self):
        r"""
        :param _BindingId: 路由关系id
        :type BindingId: int
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _Source: 源exchange名称
        :type Source: str
        :param _DestinationType: 目标类型,queue或exchange
        :type DestinationType: str
        :param _Destination: 目标资源名称
        :type Destination: str
        :param _RoutingKey: 绑定key
        :type RoutingKey: str
        :param _SourceExchangeType: 源exchange类型
        :type SourceExchangeType: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._BindingId = None
        self._VirtualHost = None
        self._Source = None
        self._DestinationType = None
        self._Destination = None
        self._RoutingKey = None
        self._SourceExchangeType = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def BindingId(self):
        """路由关系id
        :rtype: int
        """
        return self._BindingId

    @BindingId.setter
    def BindingId(self, BindingId):
        self._BindingId = BindingId

    @property
    def VirtualHost(self):
        """Vhost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Source(self):
        """源exchange名称
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def DestinationType(self):
        """目标类型,queue或exchange
        :rtype: str
        """
        return self._DestinationType

    @DestinationType.setter
    def DestinationType(self, DestinationType):
        self._DestinationType = DestinationType

    @property
    def Destination(self):
        """目标资源名称
        :rtype: str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def RoutingKey(self):
        """绑定key
        :rtype: str
        """
        return self._RoutingKey

    @RoutingKey.setter
    def RoutingKey(self, RoutingKey):
        self._RoutingKey = RoutingKey

    @property
    def SourceExchangeType(self):
        """源exchange类型
        :rtype: str
        """
        return self._SourceExchangeType

    @SourceExchangeType.setter
    def SourceExchangeType(self, SourceExchangeType):
        self._SourceExchangeType = SourceExchangeType

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._BindingId = params.get("BindingId")
        self._VirtualHost = params.get("VirtualHost")
        self._Source = params.get("Source")
        self._DestinationType = params.get("DestinationType")
        self._Destination = params.get("Destination")
        self._RoutingKey = params.get("RoutingKey")
        self._SourceExchangeType = params.get("SourceExchangeType")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQClusterInfo(AbstractModel):
    """RabbiteMQ集群基本信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _Region: 地域信息
        :type Region: str
        :param _CreateTime: 创建时间，毫秒为单位
        :type CreateTime: int
        :param _Remark: 集群说明信息
        :type Remark: str
        :param _Vpcs: VPC及网络信息
        :type Vpcs: list of VpcEndpointInfo
        :param _ZoneIds: 可用区信息
        :type ZoneIds: list of int
        :param _VirtualHostNumber: 虚拟主机数量
        :type VirtualHostNumber: int
        :param _QueueNumber: 队列数量
        :type QueueNumber: int
        :param _MessagePublishRate: 每秒生产消息数 单位：条/秒
        :type MessagePublishRate: float
        :param _MessageStackNumber: 堆积消息数 单位：条
        :type MessageStackNumber: int
        :param _ExpireTime: 过期时间
        :type ExpireTime: int
        :param _ChannelNumber: Channel数量
        :type ChannelNumber: int
        :param _ConnectionNumber: Connection数量
        :type ConnectionNumber: int
        :param _ConsumerNumber: Consumer数量
        :type ConsumerNumber: int
        :param _ExchangeNumber: Exchang数量
        :type ExchangeNumber: int
        :param _ExceptionInformation: 集群异常信息
        :type ExceptionInformation: str
        :param _ClusterStatus: 实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败
        :type ClusterStatus: int
        :param _AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type AutoRenewFlag: int
        :param _MirrorQueuePolicyFlag: 是否开启镜像队列策略。1表示开启，0表示没开启。
        :type MirrorQueuePolicyFlag: int
        :param _MessageConsumeRate: 每秒消费消息数 单位：条/秒
        :type MessageConsumeRate: float
        :param _ClusterVersion: 集群版本信息
        :type ClusterVersion: str
        :param _PayMode: 计费模式，0-后付费，1-预付费
        :type PayMode: int
        :param _InstanceType: 集群类型
        :type InstanceType: int
        :param _MessageRetainTime: 消息保留时间，单位小时
        :type MessageRetainTime: int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._CreateTime = None
        self._Remark = None
        self._Vpcs = None
        self._ZoneIds = None
        self._VirtualHostNumber = None
        self._QueueNumber = None
        self._MessagePublishRate = None
        self._MessageStackNumber = None
        self._ExpireTime = None
        self._ChannelNumber = None
        self._ConnectionNumber = None
        self._ConsumerNumber = None
        self._ExchangeNumber = None
        self._ExceptionInformation = None
        self._ClusterStatus = None
        self._AutoRenewFlag = None
        self._MirrorQueuePolicyFlag = None
        self._MessageConsumeRate = None
        self._ClusterVersion = None
        self._PayMode = None
        self._InstanceType = None
        self._MessageRetainTime = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        """地域信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CreateTime(self):
        """创建时间，毫秒为单位
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        """集群说明信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Vpcs(self):
        """VPC及网络信息
        :rtype: list of VpcEndpointInfo
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def ZoneIds(self):
        """可用区信息
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def VirtualHostNumber(self):
        """虚拟主机数量
        :rtype: int
        """
        return self._VirtualHostNumber

    @VirtualHostNumber.setter
    def VirtualHostNumber(self, VirtualHostNumber):
        self._VirtualHostNumber = VirtualHostNumber

    @property
    def QueueNumber(self):
        """队列数量
        :rtype: int
        """
        return self._QueueNumber

    @QueueNumber.setter
    def QueueNumber(self, QueueNumber):
        self._QueueNumber = QueueNumber

    @property
    def MessagePublishRate(self):
        """每秒生产消息数 单位：条/秒
        :rtype: float
        """
        return self._MessagePublishRate

    @MessagePublishRate.setter
    def MessagePublishRate(self, MessagePublishRate):
        self._MessagePublishRate = MessagePublishRate

    @property
    def MessageStackNumber(self):
        """堆积消息数 单位：条
        :rtype: int
        """
        return self._MessageStackNumber

    @MessageStackNumber.setter
    def MessageStackNumber(self, MessageStackNumber):
        self._MessageStackNumber = MessageStackNumber

    @property
    def ExpireTime(self):
        """过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ChannelNumber(self):
        """Channel数量
        :rtype: int
        """
        return self._ChannelNumber

    @ChannelNumber.setter
    def ChannelNumber(self, ChannelNumber):
        self._ChannelNumber = ChannelNumber

    @property
    def ConnectionNumber(self):
        """Connection数量
        :rtype: int
        """
        return self._ConnectionNumber

    @ConnectionNumber.setter
    def ConnectionNumber(self, ConnectionNumber):
        self._ConnectionNumber = ConnectionNumber

    @property
    def ConsumerNumber(self):
        """Consumer数量
        :rtype: int
        """
        return self._ConsumerNumber

    @ConsumerNumber.setter
    def ConsumerNumber(self, ConsumerNumber):
        self._ConsumerNumber = ConsumerNumber

    @property
    def ExchangeNumber(self):
        """Exchang数量
        :rtype: int
        """
        return self._ExchangeNumber

    @ExchangeNumber.setter
    def ExchangeNumber(self, ExchangeNumber):
        self._ExchangeNumber = ExchangeNumber

    @property
    def ExceptionInformation(self):
        """集群异常信息
        :rtype: str
        """
        return self._ExceptionInformation

    @ExceptionInformation.setter
    def ExceptionInformation(self, ExceptionInformation):
        self._ExceptionInformation = ExceptionInformation

    @property
    def ClusterStatus(self):
        """实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败
        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def AutoRenewFlag(self):
        """自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def MirrorQueuePolicyFlag(self):
        """是否开启镜像队列策略。1表示开启，0表示没开启。
        :rtype: int
        """
        return self._MirrorQueuePolicyFlag

    @MirrorQueuePolicyFlag.setter
    def MirrorQueuePolicyFlag(self, MirrorQueuePolicyFlag):
        self._MirrorQueuePolicyFlag = MirrorQueuePolicyFlag

    @property
    def MessageConsumeRate(self):
        """每秒消费消息数 单位：条/秒
        :rtype: float
        """
        return self._MessageConsumeRate

    @MessageConsumeRate.setter
    def MessageConsumeRate(self, MessageConsumeRate):
        self._MessageConsumeRate = MessageConsumeRate

    @property
    def ClusterVersion(self):
        """集群版本信息
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def PayMode(self):
        """计费模式，0-后付费，1-预付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def InstanceType(self):
        """集群类型
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def MessageRetainTime(self):
        """消息保留时间，单位小时
        :rtype: int
        """
        return self._MessageRetainTime

    @MessageRetainTime.setter
    def MessageRetainTime(self, MessageRetainTime):
        self._MessageRetainTime = MessageRetainTime


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcEndpointInfo()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        self._ZoneIds = params.get("ZoneIds")
        self._VirtualHostNumber = params.get("VirtualHostNumber")
        self._QueueNumber = params.get("QueueNumber")
        self._MessagePublishRate = params.get("MessagePublishRate")
        self._MessageStackNumber = params.get("MessageStackNumber")
        self._ExpireTime = params.get("ExpireTime")
        self._ChannelNumber = params.get("ChannelNumber")
        self._ConnectionNumber = params.get("ConnectionNumber")
        self._ConsumerNumber = params.get("ConsumerNumber")
        self._ExchangeNumber = params.get("ExchangeNumber")
        self._ExceptionInformation = params.get("ExceptionInformation")
        self._ClusterStatus = params.get("ClusterStatus")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._MirrorQueuePolicyFlag = params.get("MirrorQueuePolicyFlag")
        self._MessageConsumeRate = params.get("MessageConsumeRate")
        self._ClusterVersion = params.get("ClusterVersion")
        self._PayMode = params.get("PayMode")
        self._InstanceType = params.get("InstanceType")
        self._MessageRetainTime = params.get("MessageRetainTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQClusterSpecInfo(AbstractModel):
    """RabbitMQ集群规格信息

    """

    def __init__(self):
        r"""
        :param _SpecName: 集群规格名称
        :type SpecName: str
        :param _MaxTps: 峰值tps
        :type MaxTps: int
        :param _MaxQueueNum: 最大队列数
        :type MaxQueueNum: int
        :param _MaxExchangeNum: 最大交换机数
        :type MaxExchangeNum: int
        :param _MaxVhostNum: 最大vhost数
        :type MaxVhostNum: int
        :param _MaxConnNum: 最大连接数
        :type MaxConnNum: int
        :param _MaxUserNum: 最大用户数
        :type MaxUserNum: int
        :param _MaxBandWidth: 峰值带宽，已废弃
        :type MaxBandWidth: int
        :param _PublicNetworkTps: 公网带宽，已废弃
        :type PublicNetworkTps: int
        :param _Features: 实例对应的功能列表，true表示支持，false 表示不支持
        :type Features: str
        """
        self._SpecName = None
        self._MaxTps = None
        self._MaxQueueNum = None
        self._MaxExchangeNum = None
        self._MaxVhostNum = None
        self._MaxConnNum = None
        self._MaxUserNum = None
        self._MaxBandWidth = None
        self._PublicNetworkTps = None
        self._Features = None

    @property
    def SpecName(self):
        """集群规格名称
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def MaxTps(self):
        """峰值tps
        :rtype: int
        """
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxQueueNum(self):
        """最大队列数
        :rtype: int
        """
        return self._MaxQueueNum

    @MaxQueueNum.setter
    def MaxQueueNum(self, MaxQueueNum):
        self._MaxQueueNum = MaxQueueNum

    @property
    def MaxExchangeNum(self):
        """最大交换机数
        :rtype: int
        """
        return self._MaxExchangeNum

    @MaxExchangeNum.setter
    def MaxExchangeNum(self, MaxExchangeNum):
        self._MaxExchangeNum = MaxExchangeNum

    @property
    def MaxVhostNum(self):
        """最大vhost数
        :rtype: int
        """
        return self._MaxVhostNum

    @MaxVhostNum.setter
    def MaxVhostNum(self, MaxVhostNum):
        self._MaxVhostNum = MaxVhostNum

    @property
    def MaxConnNum(self):
        """最大连接数
        :rtype: int
        """
        return self._MaxConnNum

    @MaxConnNum.setter
    def MaxConnNum(self, MaxConnNum):
        self._MaxConnNum = MaxConnNum

    @property
    def MaxUserNum(self):
        """最大用户数
        :rtype: int
        """
        return self._MaxUserNum

    @MaxUserNum.setter
    def MaxUserNum(self, MaxUserNum):
        self._MaxUserNum = MaxUserNum

    @property
    def MaxBandWidth(self):
        """峰值带宽，已废弃
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def PublicNetworkTps(self):
        """公网带宽，已废弃
        :rtype: int
        """
        return self._PublicNetworkTps

    @PublicNetworkTps.setter
    def PublicNetworkTps(self, PublicNetworkTps):
        self._PublicNetworkTps = PublicNetworkTps

    @property
    def Features(self):
        """实例对应的功能列表，true表示支持，false 表示不支持
        :rtype: str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._MaxTps = params.get("MaxTps")
        self._MaxQueueNum = params.get("MaxQueueNum")
        self._MaxExchangeNum = params.get("MaxExchangeNum")
        self._MaxVhostNum = params.get("MaxVhostNum")
        self._MaxConnNum = params.get("MaxConnNum")
        self._MaxUserNum = params.get("MaxUserNum")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._PublicNetworkTps = params.get("PublicNetworkTps")
        self._Features = params.get("Features")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQConnection(AbstractModel):
    """RabbitMQ连接详情

    """

    def __init__(self):
        r"""
        :param _ConnectionName: 连接名称
        :type ConnectionName: str
        :param _PeerHost: 客户端ip
        :type PeerHost: str
        :param _State: 连接状态，包括 starting、tuning、opening、running、flow、blocking、blocked、closing 和 closed
        :type State: str
        :param _User: 连接使用用户
        :type User: str
        :param _SSL: 是否开启ssl
        :type SSL: bool
        :param _Protocol: 连接协议
        :type Protocol: str
        :param _Channels: 连接下的channel数
        :type Channels: int
        """
        self._ConnectionName = None
        self._PeerHost = None
        self._State = None
        self._User = None
        self._SSL = None
        self._Protocol = None
        self._Channels = None

    @property
    def ConnectionName(self):
        """连接名称
        :rtype: str
        """
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName

    @property
    def PeerHost(self):
        """客户端ip
        :rtype: str
        """
        return self._PeerHost

    @PeerHost.setter
    def PeerHost(self, PeerHost):
        self._PeerHost = PeerHost

    @property
    def State(self):
        """连接状态，包括 starting、tuning、opening、running、flow、blocking、blocked、closing 和 closed
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def User(self):
        """连接使用用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def SSL(self):
        """是否开启ssl
        :rtype: bool
        """
        return self._SSL

    @SSL.setter
    def SSL(self, SSL):
        self._SSL = SSL

    @property
    def Protocol(self):
        """连接协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Channels(self):
        """连接下的channel数
        :rtype: int
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels


    def _deserialize(self, params):
        self._ConnectionName = params.get("ConnectionName")
        self._PeerHost = params.get("PeerHost")
        self._State = params.get("State")
        self._User = params.get("User")
        self._SSL = params.get("SSL")
        self._Protocol = params.get("Protocol")
        self._Channels = params.get("Channels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQConsumersListInfo(AbstractModel):
    """队列消费者列表信息

    """

    def __init__(self):
        r"""
        :param _ClientIp: 客户端Ip
        :type ClientIp: str
        :param _ConsumerTag: 消费者Tag
        :type ConsumerTag: str
        """
        self._ClientIp = None
        self._ConsumerTag = None

    @property
    def ClientIp(self):
        """客户端Ip
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def ConsumerTag(self):
        """消费者Tag
        :rtype: str
        """
        return self._ConsumerTag

    @ConsumerTag.setter
    def ConsumerTag(self, ConsumerTag):
        self._ConsumerTag = ConsumerTag


    def _deserialize(self, params):
        self._ClientIp = params.get("ClientIp")
        self._ConsumerTag = params.get("ConsumerTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQExchangeListInfo(AbstractModel):
    """RabbitMQ exchange列表成员信息

    """

    def __init__(self):
        r"""
        :param _ExchangeName: exchange 名
        :type ExchangeName: str
        :param _Remark: 备注说明
        :type Remark: str
        :param _ExchangeType: exchange 类型, 支持 "fanout","direct","topic","headers"
        :type ExchangeType: str
        :param _VirtualHost: VHost参数
        :type VirtualHost: str
        :param _ExchangeCreator: exchange 创建者, "system":"系统创建", "user":"用户创建"
        :type ExchangeCreator: str
        :param _CreateTimeStamp: exchange 创建时间
        :type CreateTimeStamp: str
        :param _ModTimeStamp: exchange 修改时间
        :type ModTimeStamp: str
        :param _MessageRateIn: 输入消息速率
        :type MessageRateIn: float
        :param _MessageRateOut: 输出消息速率
        :type MessageRateOut: float
        :param _Durable: 是否为持久化交换机，true 为持久化，false 为非持久化
        :type Durable: bool
        :param _AutoDelete: 是否为自动删除交换机，true 为自动删除，false 为非自动删除
        :type AutoDelete: bool
        :param _Internal: 是否为内部交换机，true 为内部交换机
        :type Internal: bool
        :param _InstanceId: 交换机所属实例 ID
        :type InstanceId: str
        :param _Policy: 生效的策略名称
        :type Policy: str
        :param _Arguments: 扩展参数 key-value 对象
        :type Arguments: str
        :param _MessagesDelayed: 未调度的延时消息数量
        :type MessagesDelayed: int
        """
        self._ExchangeName = None
        self._Remark = None
        self._ExchangeType = None
        self._VirtualHost = None
        self._ExchangeCreator = None
        self._CreateTimeStamp = None
        self._ModTimeStamp = None
        self._MessageRateIn = None
        self._MessageRateOut = None
        self._Durable = None
        self._AutoDelete = None
        self._Internal = None
        self._InstanceId = None
        self._Policy = None
        self._Arguments = None
        self._MessagesDelayed = None

    @property
    def ExchangeName(self):
        """exchange 名
        :rtype: str
        """
        return self._ExchangeName

    @ExchangeName.setter
    def ExchangeName(self, ExchangeName):
        self._ExchangeName = ExchangeName

    @property
    def Remark(self):
        """备注说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ExchangeType(self):
        """exchange 类型, 支持 "fanout","direct","topic","headers"
        :rtype: str
        """
        return self._ExchangeType

    @ExchangeType.setter
    def ExchangeType(self, ExchangeType):
        self._ExchangeType = ExchangeType

    @property
    def VirtualHost(self):
        """VHost参数
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ExchangeCreator(self):
        """exchange 创建者, "system":"系统创建", "user":"用户创建"
        :rtype: str
        """
        return self._ExchangeCreator

    @ExchangeCreator.setter
    def ExchangeCreator(self, ExchangeCreator):
        self._ExchangeCreator = ExchangeCreator

    @property
    def CreateTimeStamp(self):
        """exchange 创建时间
        :rtype: str
        """
        return self._CreateTimeStamp

    @CreateTimeStamp.setter
    def CreateTimeStamp(self, CreateTimeStamp):
        self._CreateTimeStamp = CreateTimeStamp

    @property
    def ModTimeStamp(self):
        """exchange 修改时间
        :rtype: str
        """
        return self._ModTimeStamp

    @ModTimeStamp.setter
    def ModTimeStamp(self, ModTimeStamp):
        self._ModTimeStamp = ModTimeStamp

    @property
    def MessageRateIn(self):
        """输入消息速率
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        """输出消息速率
        :rtype: float
        """
        return self._MessageRateOut

    @MessageRateOut.setter
    def MessageRateOut(self, MessageRateOut):
        self._MessageRateOut = MessageRateOut

    @property
    def Durable(self):
        """是否为持久化交换机，true 为持久化，false 为非持久化
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        """是否为自动删除交换机，true 为自动删除，false 为非自动删除
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Internal(self):
        """是否为内部交换机，true 为内部交换机
        :rtype: bool
        """
        return self._Internal

    @Internal.setter
    def Internal(self, Internal):
        self._Internal = Internal

    @property
    def InstanceId(self):
        """交换机所属实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Policy(self):
        """生效的策略名称
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Arguments(self):
        """扩展参数 key-value 对象
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def MessagesDelayed(self):
        """未调度的延时消息数量
        :rtype: int
        """
        return self._MessagesDelayed

    @MessagesDelayed.setter
    def MessagesDelayed(self, MessagesDelayed):
        self._MessagesDelayed = MessagesDelayed


    def _deserialize(self, params):
        self._ExchangeName = params.get("ExchangeName")
        self._Remark = params.get("Remark")
        self._ExchangeType = params.get("ExchangeType")
        self._VirtualHost = params.get("VirtualHost")
        self._ExchangeCreator = params.get("ExchangeCreator")
        self._CreateTimeStamp = params.get("CreateTimeStamp")
        self._ModTimeStamp = params.get("ModTimeStamp")
        self._MessageRateIn = params.get("MessageRateIn")
        self._MessageRateOut = params.get("MessageRateOut")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._Internal = params.get("Internal")
        self._InstanceId = params.get("InstanceId")
        self._Policy = params.get("Policy")
        self._Arguments = params.get("Arguments")
        self._MessagesDelayed = params.get("MessagesDelayed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQPermission(AbstractModel):
    """RabbitMQ权限详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，权限关联的用户
        :type User: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        :param _ConfigRegexp: 权限类型，declare相关操作，该用户可操作该vhost下的资源名称正则表达式
        :type ConfigRegexp: str
        :param _WriteRegexp: 权限类型，消息写入相关操作，该用户可操作该vhost下的资源名称正则表达式
        :type WriteRegexp: str
        :param _ReadRegexp: 权限类型，消息读取相关操作，该用户可操作该vhost下的资源名称正则表达式
        :type ReadRegexp: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._User = None
        self._VirtualHost = None
        self._ConfigRegexp = None
        self._WriteRegexp = None
        self._ReadRegexp = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名，权限关联的用户
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def VirtualHost(self):
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def ConfigRegexp(self):
        """权限类型，declare相关操作，该用户可操作该vhost下的资源名称正则表达式
        :rtype: str
        """
        return self._ConfigRegexp

    @ConfigRegexp.setter
    def ConfigRegexp(self, ConfigRegexp):
        self._ConfigRegexp = ConfigRegexp

    @property
    def WriteRegexp(self):
        """权限类型，消息写入相关操作，该用户可操作该vhost下的资源名称正则表达式
        :rtype: str
        """
        return self._WriteRegexp

    @WriteRegexp.setter
    def WriteRegexp(self, WriteRegexp):
        self._WriteRegexp = WriteRegexp

    @property
    def ReadRegexp(self):
        """权限类型，消息读取相关操作，该用户可操作该vhost下的资源名称正则表达式
        :rtype: str
        """
        return self._ReadRegexp

    @ReadRegexp.setter
    def ReadRegexp(self, ReadRegexp):
        self._ReadRegexp = ReadRegexp

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._VirtualHost = params.get("VirtualHost")
        self._ConfigRegexp = params.get("ConfigRegexp")
        self._WriteRegexp = params.get("WriteRegexp")
        self._ReadRegexp = params.get("ReadRegexp")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQQueueListConsumerDetailInfo(AbstractModel):
    """RabbitMQ队列列表消费者信息

    """

    def __init__(self):
        r"""
        :param _ConsumersNumber: 消费者数量
        :type ConsumersNumber: int
        """
        self._ConsumersNumber = None

    @property
    def ConsumersNumber(self):
        """消费者数量
        :rtype: int
        """
        return self._ConsumersNumber

    @ConsumersNumber.setter
    def ConsumersNumber(self, ConsumersNumber):
        self._ConsumersNumber = ConsumersNumber


    def _deserialize(self, params):
        self._ConsumersNumber = params.get("ConsumersNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQQueueListInfo(AbstractModel):
    """RabbitMQ队列列表成员信息

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名
        :type QueueName: str
        :param _Remark: 备注说明
        :type Remark: str
        :param _ConsumerDetail: 消费者信息
        :type ConsumerDetail: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQQueueListConsumerDetailInfo`
        :param _QueueType: 队列类型，取值 "classic"，"quorum"
        :type QueueType: str
        :param _MessageHeapCount: 消息堆积数
        :type MessageHeapCount: int
        :param _MessageRateIn: 消息生产速率，每秒
        :type MessageRateIn: float
        :param _MessageRateOut: 消息消费速率，每秒
        :type MessageRateOut: float
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _Durable: 队列是否持久化，true 为持久化，false 为非持久化
        :type Durable: bool
        :param _AutoDelete: 队列是否为自动删除队列，true 为自动删除，false 为非自动删除
        :type AutoDelete: bool
        :param _InstanceId: 队列所属实例 ID
        :type InstanceId: str
        :param _VirtualHost: 队列所属虚拟主机名称
        :type VirtualHost: str
        :param _Node: 队列所在主节点名称
        :type Node: str
        :param _Policy: 生效的策略名称
        :type Policy: str
        :param _Arguments: 扩展参数 key-value 对象
        :type Arguments: str
        :param _Exclusive: 是否独占队列
        :type Exclusive: bool
        """
        self._QueueName = None
        self._Remark = None
        self._ConsumerDetail = None
        self._QueueType = None
        self._MessageHeapCount = None
        self._MessageRateIn = None
        self._MessageRateOut = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Durable = None
        self._AutoDelete = None
        self._InstanceId = None
        self._VirtualHost = None
        self._Node = None
        self._Policy = None
        self._Arguments = None
        self._Exclusive = None

    @property
    def QueueName(self):
        """队列名
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Remark(self):
        """备注说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsumerDetail(self):
        """消费者信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQQueueListConsumerDetailInfo`
        """
        return self._ConsumerDetail

    @ConsumerDetail.setter
    def ConsumerDetail(self, ConsumerDetail):
        self._ConsumerDetail = ConsumerDetail

    @property
    def QueueType(self):
        """队列类型，取值 "classic"，"quorum"
        :rtype: str
        """
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def MessageHeapCount(self):
        """消息堆积数
        :rtype: int
        """
        return self._MessageHeapCount

    @MessageHeapCount.setter
    def MessageHeapCount(self, MessageHeapCount):
        self._MessageHeapCount = MessageHeapCount

    @property
    def MessageRateIn(self):
        """消息生产速率，每秒
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        """消息消费速率，每秒
        :rtype: float
        """
        return self._MessageRateOut

    @MessageRateOut.setter
    def MessageRateOut(self, MessageRateOut):
        self._MessageRateOut = MessageRateOut

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Durable(self):
        """队列是否持久化，true 为持久化，false 为非持久化
        :rtype: bool
        """
        return self._Durable

    @Durable.setter
    def Durable(self, Durable):
        self._Durable = Durable

    @property
    def AutoDelete(self):
        """队列是否为自动删除队列，true 为自动删除，false 为非自动删除
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def InstanceId(self):
        """队列所属实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """队列所属虚拟主机名称
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Node(self):
        """队列所在主节点名称
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def Policy(self):
        """生效的策略名称
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Arguments(self):
        """扩展参数 key-value 对象
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments

    @property
    def Exclusive(self):
        """是否独占队列
        :rtype: bool
        """
        return self._Exclusive

    @Exclusive.setter
    def Exclusive(self, Exclusive):
        self._Exclusive = Exclusive


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._Remark = params.get("Remark")
        if params.get("ConsumerDetail") is not None:
            self._ConsumerDetail = RabbitMQQueueListConsumerDetailInfo()
            self._ConsumerDetail._deserialize(params.get("ConsumerDetail"))
        self._QueueType = params.get("QueueType")
        self._MessageHeapCount = params.get("MessageHeapCount")
        self._MessageRateIn = params.get("MessageRateIn")
        self._MessageRateOut = params.get("MessageRateOut")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Durable = params.get("Durable")
        self._AutoDelete = params.get("AutoDelete")
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Node = params.get("Node")
        self._Policy = params.get("Policy")
        self._Arguments = params.get("Arguments")
        self._Exclusive = params.get("Exclusive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessAccessInfo(AbstractModel):
    """公网访问信息

    """

    def __init__(self):
        r"""
        :param _PublicAccessEndpoint: 公网域名
        :type PublicAccessEndpoint: str
        :param _PublicDataStreamStatus: 公网状态
        :type PublicDataStreamStatus: str
        """
        self._PublicAccessEndpoint = None
        self._PublicDataStreamStatus = None

    @property
    def PublicAccessEndpoint(self):
        """公网域名
        :rtype: str
        """
        return self._PublicAccessEndpoint

    @PublicAccessEndpoint.setter
    def PublicAccessEndpoint(self, PublicAccessEndpoint):
        self._PublicAccessEndpoint = PublicAccessEndpoint

    @property
    def PublicDataStreamStatus(self):
        """公网状态
        :rtype: str
        """
        return self._PublicDataStreamStatus

    @PublicDataStreamStatus.setter
    def PublicDataStreamStatus(self, PublicDataStreamStatus):
        self._PublicDataStreamStatus = PublicDataStreamStatus


    def _deserialize(self, params):
        self._PublicAccessEndpoint = params.get("PublicAccessEndpoint")
        self._PublicDataStreamStatus = params.get("PublicDataStreamStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessEndpoint(AbstractModel):
    """接入点

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
        :type VpcId: str
        :param _SubnetId: subnet id
        :type SubnetId: str
        :param _VpcEndpoint: 接入地址
        :type VpcEndpoint: str
        :param _VpcDataStreamEndpointStatus: 接入地址状态
        :type VpcDataStreamEndpointStatus: str
        :param _PublicNetwork: 是否是公网
        :type PublicNetwork: bool
        :param _AccessStrategy: 访问策略
        :type AccessStrategy: str
        :param _Bandwidth: 带宽
        :type Bandwidth: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._VpcEndpoint = None
        self._VpcDataStreamEndpointStatus = None
        self._PublicNetwork = None
        self._AccessStrategy = None
        self._Bandwidth = None

    @property
    def VpcId(self):
        """vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """subnet id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcEndpoint(self):
        """接入地址
        :rtype: str
        """
        return self._VpcEndpoint

    @VpcEndpoint.setter
    def VpcEndpoint(self, VpcEndpoint):
        self._VpcEndpoint = VpcEndpoint

    @property
    def VpcDataStreamEndpointStatus(self):
        """接入地址状态
        :rtype: str
        """
        return self._VpcDataStreamEndpointStatus

    @VpcDataStreamEndpointStatus.setter
    def VpcDataStreamEndpointStatus(self, VpcDataStreamEndpointStatus):
        self._VpcDataStreamEndpointStatus = VpcDataStreamEndpointStatus

    @property
    def PublicNetwork(self):
        """是否是公网
        :rtype: bool
        """
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork

    @property
    def AccessStrategy(self):
        """访问策略
        :rtype: str
        """
        return self._AccessStrategy

    @AccessStrategy.setter
    def AccessStrategy(self, AccessStrategy):
        self._AccessStrategy = AccessStrategy

    @property
    def Bandwidth(self):
        """带宽
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VpcEndpoint = params.get("VpcEndpoint")
        self._VpcDataStreamEndpointStatus = params.get("VpcDataStreamEndpointStatus")
        self._PublicNetwork = params.get("PublicNetwork")
        self._AccessStrategy = params.get("AccessStrategy")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessInstance(AbstractModel):
    """rabbitmq serverless 实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceVersion: 实例版本号
        :type InstanceVersion: str
        :param _Status: 实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败
        :type Status: int
        :param _MaxTps: TPS
        :type MaxTps: int
        :param _MaxBandWidth: 带宽
        :type MaxBandWidth: int
        :param _ExpireTime: 集群过期时间
        :type ExpireTime: int
        :param _AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type AutoRenewFlag: int
        :param _PayMode: 0-后付费，1-预付费
        :type PayMode: int
        :param _Remark: 备注
        :type Remark: str
        :param _SpecName: 集群规格
        :type SpecName: str
        :param _ExceptionInformation: 异常信息
        :type ExceptionInformation: str
        :param _PublicAccessEndpoint: 公网接入点
        :type PublicAccessEndpoint: str
        :param _Vpcs: 私有网络接入点
        :type Vpcs: list of RabbitMQServerlessEndpoint
        :param _ClusterStatus: 实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败

        :type ClusterStatus: int
        :param _InstanceType: 集群类型：1
        :type InstanceType: int
        :param _CreateTime: 过期时间
        :type CreateTime: int
        :param _NodeCount: 为了兼容托管版，固定值 0
        :type NodeCount: int
        :param _MaxStorage: 为了兼容托管版，固定值 0
        :type MaxStorage: int
        :param _IsolatedTime: 隔离时间
        :type IsolatedTime: int
        :param _ServerlessExt: Serverless 扩展字段
        :type ServerlessExt: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None
        self._ExceptionInformation = None
        self._PublicAccessEndpoint = None
        self._Vpcs = None
        self._ClusterStatus = None
        self._InstanceType = None
        self._CreateTime = None
        self._NodeCount = None
        self._MaxStorage = None
        self._IsolatedTime = None
        self._ServerlessExt = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceVersion(self):
        """实例版本号
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        """实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaxTps(self):
        """TPS
        :rtype: int
        """
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxBandWidth(self):
        """带宽
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def ExpireTime(self):
        """集群过期时间
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        """自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PayMode(self):
        """0-后付费，1-预付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        """集群规格
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def ExceptionInformation(self):
        """异常信息
        :rtype: str
        """
        return self._ExceptionInformation

    @ExceptionInformation.setter
    def ExceptionInformation(self, ExceptionInformation):
        self._ExceptionInformation = ExceptionInformation

    @property
    def PublicAccessEndpoint(self):
        """公网接入点
        :rtype: str
        """
        return self._PublicAccessEndpoint

    @PublicAccessEndpoint.setter
    def PublicAccessEndpoint(self, PublicAccessEndpoint):
        self._PublicAccessEndpoint = PublicAccessEndpoint

    @property
    def Vpcs(self):
        """私有网络接入点
        :rtype: list of RabbitMQServerlessEndpoint
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def ClusterStatus(self):
        """实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败

        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def InstanceType(self):
        """集群类型：1
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def CreateTime(self):
        """过期时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def NodeCount(self):
        """为了兼容托管版，固定值 0
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def MaxStorage(self):
        """为了兼容托管版，固定值 0
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def IsolatedTime(self):
        """隔离时间
        :rtype: int
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def ServerlessExt(self):
        """Serverless 扩展字段
        :rtype: str
        """
        return self._ServerlessExt

    @ServerlessExt.setter
    def ServerlessExt(self, ServerlessExt):
        self._ServerlessExt = ServerlessExt


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        self._ExceptionInformation = params.get("ExceptionInformation")
        self._PublicAccessEndpoint = params.get("PublicAccessEndpoint")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = RabbitMQServerlessEndpoint()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        self._ClusterStatus = params.get("ClusterStatus")
        self._InstanceType = params.get("InstanceType")
        self._CreateTime = params.get("CreateTime")
        self._NodeCount = params.get("NodeCount")
        self._MaxStorage = params.get("MaxStorage")
        self._IsolatedTime = params.get("IsolatedTime")
        self._ServerlessExt = params.get("ServerlessExt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQServerlessWhiteListInfo(AbstractModel):
    """公网白名单信息

    """

    def __init__(self):
        r"""
        :param _PublicDataStreamWhiteList: 公网数据流白名单
        :type PublicDataStreamWhiteList: str
        :param _PublicDataStreamWhiteListStatus: 公网数据流白名单状态
        :type PublicDataStreamWhiteListStatus: str
        """
        self._PublicDataStreamWhiteList = None
        self._PublicDataStreamWhiteListStatus = None

    @property
    def PublicDataStreamWhiteList(self):
        """公网数据流白名单
        :rtype: str
        """
        return self._PublicDataStreamWhiteList

    @PublicDataStreamWhiteList.setter
    def PublicDataStreamWhiteList(self, PublicDataStreamWhiteList):
        self._PublicDataStreamWhiteList = PublicDataStreamWhiteList

    @property
    def PublicDataStreamWhiteListStatus(self):
        """公网数据流白名单状态
        :rtype: str
        """
        return self._PublicDataStreamWhiteListStatus

    @PublicDataStreamWhiteListStatus.setter
    def PublicDataStreamWhiteListStatus(self, PublicDataStreamWhiteListStatus):
        self._PublicDataStreamWhiteListStatus = PublicDataStreamWhiteListStatus


    def _deserialize(self, params):
        self._PublicDataStreamWhiteList = params.get("PublicDataStreamWhiteList")
        self._PublicDataStreamWhiteListStatus = params.get("PublicDataStreamWhiteListStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQUser(AbstractModel):
    """RabbitMQ用户实体详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，登录时使用
        :type User: str
        :param _Password: 密码，登录时使用
        :type Password: str
        :param _Description: 用户描述
        :type Description: str
        :param _Tags: 用户标签，用于决定改用户访问RabbitMQ Management的权限范围
        :type Tags: list of str
        :param _CreateTime: 用户创建时间
        :type CreateTime: str
        :param _ModifyTime: 用户最后修改时间
        :type ModifyTime: str
        :param _Type: 用户类型，System：系统创建，User：用户创建
        :type Type: str
        :param _MaxConnections: 该用户所能允许的最大连接数
        :type MaxConnections: int
        :param _MaxChannels: 该用户所能允许的最大通道数
        :type MaxChannels: int
        """
        self._InstanceId = None
        self._User = None
        self._Password = None
        self._Description = None
        self._Tags = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Type = None
        self._MaxConnections = None
        self._MaxChannels = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def User(self):
        """用户名，登录时使用
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """密码，登录时使用
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        """用户描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        """用户标签，用于决定改用户访问RabbitMQ Management的权限范围
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        """用户创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """用户最后修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Type(self):
        """用户类型，System：系统创建，User：用户创建
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MaxConnections(self):
        """该用户所能允许的最大连接数
        :rtype: int
        """
        return self._MaxConnections

    @MaxConnections.setter
    def MaxConnections(self, MaxConnections):
        self._MaxConnections = MaxConnections

    @property
    def MaxChannels(self):
        """该用户所能允许的最大通道数
        :rtype: int
        """
        return self._MaxChannels

    @MaxChannels.setter
    def MaxChannels(self, MaxChannels):
        self._MaxChannels = MaxChannels


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Type = params.get("Type")
        self._MaxConnections = params.get("MaxConnections")
        self._MaxChannels = params.get("MaxChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQVirtualHostInfo(AbstractModel):
    """RabbitMQ的vhost详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        :param _Description: vhost描述信息
        :type Description: str
        :param _Tags: vhost标签
        :type Tags: list of str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _VirtualHostStatistics: vhost概览统计信息
        :type VirtualHostStatistics: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQVirtualHostStatistics`
        :param _Status: vhost状态，与原生控制台对应，有running、partial、stopped、unknown
        :type Status: str
        :param _MessageHeapCount: 消息堆积数
        :type MessageHeapCount: int
        :param _MessageRateIn: 输入消息速率
        :type MessageRateIn: float
        :param _MessageRateOut: 输出消息速率
        :type MessageRateOut: float
        :param _MirrorQueuePolicyFlag: 是否存在镜像队列策略，true 为存在，false 为不存
        :type MirrorQueuePolicyFlag: bool
        """
        self._InstanceId = None
        self._VirtualHost = None
        self._Description = None
        self._Tags = None
        self._CreateTime = None
        self._ModifyTime = None
        self._VirtualHostStatistics = None
        self._Status = None
        self._MessageHeapCount = None
        self._MessageRateIn = None
        self._MessageRateOut = None
        self._MirrorQueuePolicyFlag = None

    @property
    def InstanceId(self):
        """集群实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def VirtualHost(self):
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

    @property
    def Description(self):
        """vhost描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        """vhost标签
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def VirtualHostStatistics(self):
        """vhost概览统计信息
        :rtype: :class:`tencentcloud.trabbit.v20230418.models.RabbitMQVirtualHostStatistics`
        """
        return self._VirtualHostStatistics

    @VirtualHostStatistics.setter
    def VirtualHostStatistics(self, VirtualHostStatistics):
        self._VirtualHostStatistics = VirtualHostStatistics

    @property
    def Status(self):
        """vhost状态，与原生控制台对应，有running、partial、stopped、unknown
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MessageHeapCount(self):
        """消息堆积数
        :rtype: int
        """
        return self._MessageHeapCount

    @MessageHeapCount.setter
    def MessageHeapCount(self, MessageHeapCount):
        self._MessageHeapCount = MessageHeapCount

    @property
    def MessageRateIn(self):
        """输入消息速率
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        """输出消息速率
        :rtype: float
        """
        return self._MessageRateOut

    @MessageRateOut.setter
    def MessageRateOut(self, MessageRateOut):
        self._MessageRateOut = MessageRateOut

    @property
    def MirrorQueuePolicyFlag(self):
        """是否存在镜像队列策略，true 为存在，false 为不存
        :rtype: bool
        """
        return self._MirrorQueuePolicyFlag

    @MirrorQueuePolicyFlag.setter
    def MirrorQueuePolicyFlag(self, MirrorQueuePolicyFlag):
        self._MirrorQueuePolicyFlag = MirrorQueuePolicyFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VirtualHost = params.get("VirtualHost")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("VirtualHostStatistics") is not None:
            self._VirtualHostStatistics = RabbitMQVirtualHostStatistics()
            self._VirtualHostStatistics._deserialize(params.get("VirtualHostStatistics"))
        self._Status = params.get("Status")
        self._MessageHeapCount = params.get("MessageHeapCount")
        self._MessageRateIn = params.get("MessageRateIn")
        self._MessageRateOut = params.get("MessageRateOut")
        self._MirrorQueuePolicyFlag = params.get("MirrorQueuePolicyFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQVirtualHostStatistics(AbstractModel):
    """vhost概览统计信息

    """

    def __init__(self):
        r"""
        :param _CurrentQueues: 当前vhost的queue数量
        :type CurrentQueues: int
        :param _CurrentExchanges: 当前vhost的exchange数量
        :type CurrentExchanges: int
        :param _CurrentConnections: 当前vhost的连接数量
        :type CurrentConnections: int
        :param _CurrentChannels: 当前vhost的channel数量
        :type CurrentChannels: int
        :param _CurrentUsers: 当前vhost的用户数量
        :type CurrentUsers: int
        """
        self._CurrentQueues = None
        self._CurrentExchanges = None
        self._CurrentConnections = None
        self._CurrentChannels = None
        self._CurrentUsers = None

    @property
    def CurrentQueues(self):
        """当前vhost的queue数量
        :rtype: int
        """
        return self._CurrentQueues

    @CurrentQueues.setter
    def CurrentQueues(self, CurrentQueues):
        self._CurrentQueues = CurrentQueues

    @property
    def CurrentExchanges(self):
        """当前vhost的exchange数量
        :rtype: int
        """
        return self._CurrentExchanges

    @CurrentExchanges.setter
    def CurrentExchanges(self, CurrentExchanges):
        self._CurrentExchanges = CurrentExchanges

    @property
    def CurrentConnections(self):
        """当前vhost的连接数量
        :rtype: int
        """
        return self._CurrentConnections

    @CurrentConnections.setter
    def CurrentConnections(self, CurrentConnections):
        self._CurrentConnections = CurrentConnections

    @property
    def CurrentChannels(self):
        """当前vhost的channel数量
        :rtype: int
        """
        return self._CurrentChannels

    @CurrentChannels.setter
    def CurrentChannels(self, CurrentChannels):
        self._CurrentChannels = CurrentChannels

    @property
    def CurrentUsers(self):
        """当前vhost的用户数量
        :rtype: int
        """
        return self._CurrentUsers

    @CurrentUsers.setter
    def CurrentUsers(self, CurrentUsers):
        self._CurrentUsers = CurrentUsers


    def _deserialize(self, params):
        self._CurrentQueues = params.get("CurrentQueues")
        self._CurrentExchanges = params.get("CurrentExchanges")
        self._CurrentConnections = params.get("CurrentConnections")
        self._CurrentChannels = params.get("CurrentChannels")
        self._CurrentUsers = params.get("CurrentUsers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserQuota(AbstractModel):
    """用户数配额

    """

    def __init__(self):
        r"""
        :param _MaxUser: 最大用户数
        :type MaxUser: int
        :param _UsedUser: 已用用户数
        :type UsedUser: int
        """
        self._MaxUser = None
        self._UsedUser = None

    @property
    def MaxUser(self):
        """最大用户数
        :rtype: int
        """
        return self._MaxUser

    @MaxUser.setter
    def MaxUser(self, MaxUser):
        self._MaxUser = MaxUser

    @property
    def UsedUser(self):
        """已用用户数
        :rtype: int
        """
        return self._UsedUser

    @UsedUser.setter
    def UsedUser(self, UsedUser):
        self._UsedUser = UsedUser


    def _deserialize(self, params):
        self._MaxUser = params.get("MaxUser")
        self._UsedUser = params.get("UsedUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualHostQuota(AbstractModel):
    """虚拟主机配额

    """

    def __init__(self):
        r"""
        :param _MaxVirtualHost: 最大虚拟主机数
        :type MaxVirtualHost: int
        :param _UsedVirtualHost: 已经使用的虚拟主机数
        :type UsedVirtualHost: int
        """
        self._MaxVirtualHost = None
        self._UsedVirtualHost = None

    @property
    def MaxVirtualHost(self):
        """最大虚拟主机数
        :rtype: int
        """
        return self._MaxVirtualHost

    @MaxVirtualHost.setter
    def MaxVirtualHost(self, MaxVirtualHost):
        self._MaxVirtualHost = MaxVirtualHost

    @property
    def UsedVirtualHost(self):
        """已经使用的虚拟主机数
        :rtype: int
        """
        return self._UsedVirtualHost

    @UsedVirtualHost.setter
    def UsedVirtualHost(self, UsedVirtualHost):
        self._UsedVirtualHost = UsedVirtualHost


    def _deserialize(self, params):
        self._MaxVirtualHost = params.get("MaxVirtualHost")
        self._UsedVirtualHost = params.get("UsedVirtualHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcEndpointInfo(AbstractModel):
    """VPC接入点信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc的id
        :type VpcId: str
        :param _SubnetId: 子网id
        :type SubnetId: str
        :param _VpcEndpoint: vpc接入点信息
        :type VpcEndpoint: str
        :param _VpcDataStreamEndpointStatus: vpc接入点状态
OFF/ON/CREATING/DELETING
        :type VpcDataStreamEndpointStatus: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._VpcEndpoint = None
        self._VpcDataStreamEndpointStatus = None

    @property
    def VpcId(self):
        """vpc的id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcEndpoint(self):
        """vpc接入点信息
        :rtype: str
        """
        return self._VpcEndpoint

    @VpcEndpoint.setter
    def VpcEndpoint(self, VpcEndpoint):
        self._VpcEndpoint = VpcEndpoint

    @property
    def VpcDataStreamEndpointStatus(self):
        """vpc接入点状态
OFF/ON/CREATING/DELETING
        :rtype: str
        """
        return self._VpcDataStreamEndpointStatus

    @VpcDataStreamEndpointStatus.setter
    def VpcDataStreamEndpointStatus(self, VpcDataStreamEndpointStatus):
        self._VpcDataStreamEndpointStatus = VpcDataStreamEndpointStatus


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VpcEndpoint = params.get("VpcEndpoint")
        self._VpcDataStreamEndpointStatus = params.get("VpcDataStreamEndpointStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        