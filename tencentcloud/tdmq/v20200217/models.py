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


class AMQPClusterConfig(AbstractModel):
    """AMQP集群配置

    """

    def __init__(self):
        r"""
        :param _MaxTpsPerVHost: 单Vhost TPS上限
        :type MaxTpsPerVHost: int
        :param _MaxConnNumPerVHost: 单Vhost客户端连接数上限
        :type MaxConnNumPerVHost: int
        :param _MaxVHostNum: 最大Vhost数量
        :type MaxVHostNum: int
        :param _MaxExchangeNum: 最大exchange数量
        :type MaxExchangeNum: int
        :param _MaxQueueNum: 最大Queue数量
        :type MaxQueueNum: int
        :param _MaxRetentionTime: 消息最大保留时间，以毫秒为单位
        :type MaxRetentionTime: int
        :param _UsedVHostNum: 已使用Vhost数量
        :type UsedVHostNum: int
        :param _UsedExchangeNum: 已使用exchange数量
        :type UsedExchangeNum: int
        :param _UsedQueueNum: 已使用queue数量
        :type UsedQueueNum: int
        """
        self._MaxTpsPerVHost = None
        self._MaxConnNumPerVHost = None
        self._MaxVHostNum = None
        self._MaxExchangeNum = None
        self._MaxQueueNum = None
        self._MaxRetentionTime = None
        self._UsedVHostNum = None
        self._UsedExchangeNum = None
        self._UsedQueueNum = None

    @property
    def MaxTpsPerVHost(self):
        """单Vhost TPS上限
        :rtype: int
        """
        return self._MaxTpsPerVHost

    @MaxTpsPerVHost.setter
    def MaxTpsPerVHost(self, MaxTpsPerVHost):
        self._MaxTpsPerVHost = MaxTpsPerVHost

    @property
    def MaxConnNumPerVHost(self):
        """单Vhost客户端连接数上限
        :rtype: int
        """
        return self._MaxConnNumPerVHost

    @MaxConnNumPerVHost.setter
    def MaxConnNumPerVHost(self, MaxConnNumPerVHost):
        self._MaxConnNumPerVHost = MaxConnNumPerVHost

    @property
    def MaxVHostNum(self):
        """最大Vhost数量
        :rtype: int
        """
        return self._MaxVHostNum

    @MaxVHostNum.setter
    def MaxVHostNum(self, MaxVHostNum):
        self._MaxVHostNum = MaxVHostNum

    @property
    def MaxExchangeNum(self):
        """最大exchange数量
        :rtype: int
        """
        return self._MaxExchangeNum

    @MaxExchangeNum.setter
    def MaxExchangeNum(self, MaxExchangeNum):
        self._MaxExchangeNum = MaxExchangeNum

    @property
    def MaxQueueNum(self):
        """最大Queue数量
        :rtype: int
        """
        return self._MaxQueueNum

    @MaxQueueNum.setter
    def MaxQueueNum(self, MaxQueueNum):
        self._MaxQueueNum = MaxQueueNum

    @property
    def MaxRetentionTime(self):
        """消息最大保留时间，以毫秒为单位
        :rtype: int
        """
        return self._MaxRetentionTime

    @MaxRetentionTime.setter
    def MaxRetentionTime(self, MaxRetentionTime):
        self._MaxRetentionTime = MaxRetentionTime

    @property
    def UsedVHostNum(self):
        """已使用Vhost数量
        :rtype: int
        """
        return self._UsedVHostNum

    @UsedVHostNum.setter
    def UsedVHostNum(self, UsedVHostNum):
        self._UsedVHostNum = UsedVHostNum

    @property
    def UsedExchangeNum(self):
        """已使用exchange数量
        :rtype: int
        """
        return self._UsedExchangeNum

    @UsedExchangeNum.setter
    def UsedExchangeNum(self, UsedExchangeNum):
        self._UsedExchangeNum = UsedExchangeNum

    @property
    def UsedQueueNum(self):
        """已使用queue数量
        :rtype: int
        """
        return self._UsedQueueNum

    @UsedQueueNum.setter
    def UsedQueueNum(self, UsedQueueNum):
        self._UsedQueueNum = UsedQueueNum


    def _deserialize(self, params):
        self._MaxTpsPerVHost = params.get("MaxTpsPerVHost")
        self._MaxConnNumPerVHost = params.get("MaxConnNumPerVHost")
        self._MaxVHostNum = params.get("MaxVHostNum")
        self._MaxExchangeNum = params.get("MaxExchangeNum")
        self._MaxQueueNum = params.get("MaxQueueNum")
        self._MaxRetentionTime = params.get("MaxRetentionTime")
        self._UsedVHostNum = params.get("UsedVHostNum")
        self._UsedExchangeNum = params.get("UsedExchangeNum")
        self._UsedQueueNum = params.get("UsedQueueNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPClusterDetail(AbstractModel):
    """租户AMQP集群详细信息

    """

    def __init__(self):
        r"""
        :param _Info: 集群基本信息
        :type Info: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterInfo`
        :param _Config: 集群配置信息
        :type Config: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterConfig`
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :type Status: int
        """
        self._Info = None
        self._Config = None
        self._Tags = None
        self._Status = None

    @property
    def Info(self):
        """集群基本信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Config(self):
        """集群配置信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        """集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = AMQPClusterInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("Config") is not None:
            self._Config = AMQPClusterConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPClusterInfo(AbstractModel):
    """AMQP集群基本信息

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
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _PublicEndPoint: 公网接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicEndPoint: str
        :param _VpcEndPoint: VPC接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcEndPoint: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._CreateTime = None
        self._Remark = None
        self._PublicEndPoint = None
        self._VpcEndPoint = None

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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicEndPoint(self):
        """公网接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicEndPoint

    @PublicEndPoint.setter
    def PublicEndPoint(self, PublicEndPoint):
        self._PublicEndPoint = PublicEndPoint

    @property
    def VpcEndPoint(self):
        """VPC接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcEndPoint

    @VpcEndPoint.setter
    def VpcEndPoint(self, VpcEndPoint):
        self._VpcEndPoint = VpcEndPoint


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        self._PublicEndPoint = params.get("PublicEndPoint")
        self._VpcEndPoint = params.get("VpcEndPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcknowledgeMessageRequest(AbstractModel):
    """AcknowledgeMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageId: 用作标识消息的唯一的ID（可从 receiveMessage 的返回值中获得）
        :type MessageId: str
        :param _AckTopic: Topic 名字（可从 receiveMessage 的返回值中获得）这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :type AckTopic: str
        :param _SubName: 订阅者的名字，可以从receiveMessage的返回值中获取到。这里尽量与receiveMessage中的订阅者保持一致，否则没办法正确ack 接收回来的消息。
        :type SubName: str
        """
        self._MessageId = None
        self._AckTopic = None
        self._SubName = None

    @property
    def MessageId(self):
        """用作标识消息的唯一的ID（可从 receiveMessage 的返回值中获得）
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def AckTopic(self):
        """Topic 名字（可从 receiveMessage 的返回值中获得）这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :rtype: str
        """
        return self._AckTopic

    @AckTopic.setter
    def AckTopic(self, AckTopic):
        self._AckTopic = AckTopic

    @property
    def SubName(self):
        """订阅者的名字，可以从receiveMessage的返回值中获取到。这里尽量与receiveMessage中的订阅者保持一致，否则没办法正确ack 接收回来的消息。
        :rtype: str
        """
        return self._SubName

    @SubName.setter
    def SubName(self, SubName):
        self._SubName = SubName


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._AckTopic = params.get("AckTopic")
        self._SubName = params.get("SubName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcknowledgeMessageResponse(AbstractModel):
    """AcknowledgeMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 如果为""，则说明没有错误返回，否则返回具体的错误信息。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        """如果为""，则说明没有错误返回，否则返回具体的错误信息。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class BindCluster(AbstractModel):
    """用户专享集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterName: 物理集群的名称
        :type ClusterName: str
        """
        self._ClusterName = None

    @property
    def ClusterName(self):
        """物理集群的名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearCmqQueueRequest(AbstractModel):
    """ClearCmqQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一账号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        """队列名字，在单个地域同一账号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
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
        


class ClearCmqQueueResponse(AbstractModel):
    """ClearCmqQueue返回参数结构体

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


class ClearCmqSubscriptionFilterTagsRequest(AbstractModel):
    """ClearCmqSubscriptionFilterTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        """
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def TopicName(self):
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        """订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
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
        


class ClearCmqSubscriptionFilterTagsResponse(AbstractModel):
    """ClearCmqSubscriptionFilterTags返回参数结构体

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


class ClientSubscriptionInfo(AbstractModel):
    """客户端订阅详情，可用于辅助判断哪些客户端订阅关系不一致

    """

    def __init__(self):
        r"""
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _ClientAddr: 客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientAddr: str
        :param _Topic: 订阅主题
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: str
        :param _SubString: 订阅表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type SubString: str
        :param _ExpressionType: 订阅方式
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpressionType: str
        """
        self._ClientId = None
        self._ClientAddr = None
        self._Topic = None
        self._SubString = None
        self._ExpressionType = None

    @property
    def ClientId(self):
        """客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientAddr(self):
        """客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def Topic(self):
        """订阅主题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def SubString(self):
        """订阅表达式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubString

    @SubString.setter
    def SubString(self, SubString):
        self._SubString = SubString

    @property
    def ExpressionType(self):
        """订阅方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpressionType

    @ExpressionType.setter
    def ExpressionType(self, ExpressionType):
        self._ExpressionType = ExpressionType


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._ClientAddr = params.get("ClientAddr")
        self._Topic = params.get("Topic")
        self._SubString = params.get("SubString")
        self._ExpressionType = params.get("ExpressionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cluster(AbstractModel):
    """集群信息集合

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id。
        :type ClusterId: str
        :param _ClusterName: 集群名称。
        :type ClusterName: str
        :param _Remark: 说明信息。
        :type Remark: str
        :param _EndPointNum: 接入点数量
        :type EndPointNum: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Healthy: 集群是否健康，1表示健康，0表示异常
        :type Healthy: int
        :param _HealthyInfo: 集群健康信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthyInfo: str
        :param _Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :type Status: int
        :param _MaxNamespaceNum: 最大命名空间数量
        :type MaxNamespaceNum: int
        :param _MaxTopicNum: 最大Topic数量
        :type MaxTopicNum: int
        :param _MaxQps: 最大QPS
        :type MaxQps: int
        :param _MessageRetentionTime: 最大消息保留时间，秒为单位
        :type MessageRetentionTime: int
        :param _MaxStorageCapacity: 最大存储容量
        :type MaxStorageCapacity: int
        :param _Version: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _PublicEndPoint: 公网访问接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicEndPoint: str
        :param _VpcEndPoint: VPC访问接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcEndPoint: str
        :param _NamespaceNum: 命名空间数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceNum: int
        :param _UsedStorageBudget: 已使用存储限制，MB为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedStorageBudget: int
        :param _MaxPublishRateInMessages: 最大生产消息速率，以条数为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPublishRateInMessages: int
        :param _MaxDispatchRateInMessages: 最大推送消息速率，以条数为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDispatchRateInMessages: int
        :param _MaxPublishRateInBytes: 最大生产消息速率，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPublishRateInBytes: int
        :param _MaxDispatchRateInBytes: 最大推送消息速率，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDispatchRateInBytes: int
        :param _TopicNum: 已创建主题数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNum: int
        :param _MaxMessageDelayInSeconds: 最长消息延时，以秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMessageDelayInSeconds: int
        :param _PublicAccessEnabled: 是否开启公网访问，不填时默认开启
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccessEnabled: bool
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _PayMode: 计费模式：
0: 按量计费
1: 包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _ProjectName: 项目名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _UpgradeProInstance: 是否支持升级专业版实例
        :type UpgradeProInstance: bool
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None
        self._EndPointNum = None
        self._CreateTime = None
        self._Healthy = None
        self._HealthyInfo = None
        self._Status = None
        self._MaxNamespaceNum = None
        self._MaxTopicNum = None
        self._MaxQps = None
        self._MessageRetentionTime = None
        self._MaxStorageCapacity = None
        self._Version = None
        self._PublicEndPoint = None
        self._VpcEndPoint = None
        self._NamespaceNum = None
        self._UsedStorageBudget = None
        self._MaxPublishRateInMessages = None
        self._MaxDispatchRateInMessages = None
        self._MaxPublishRateInBytes = None
        self._MaxDispatchRateInBytes = None
        self._TopicNum = None
        self._MaxMessageDelayInSeconds = None
        self._PublicAccessEnabled = None
        self._Tags = None
        self._PayMode = None
        self._ProjectId = None
        self._ProjectName = None
        self._UpgradeProInstance = None

    @property
    def ClusterId(self):
        """集群Id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """集群名称。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        """说明信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def EndPointNum(self):
        """接入点数量
        :rtype: int
        """
        return self._EndPointNum

    @EndPointNum.setter
    def EndPointNum(self, EndPointNum):
        self._EndPointNum = EndPointNum

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
    def Healthy(self):
        """集群是否健康，1表示健康，0表示异常
        :rtype: int
        """
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyInfo(self):
        """集群健康信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HealthyInfo

    @HealthyInfo.setter
    def HealthyInfo(self, HealthyInfo):
        self._HealthyInfo = HealthyInfo

    @property
    def Status(self):
        """集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaxNamespaceNum(self):
        """最大命名空间数量
        :rtype: int
        """
        return self._MaxNamespaceNum

    @MaxNamespaceNum.setter
    def MaxNamespaceNum(self, MaxNamespaceNum):
        self._MaxNamespaceNum = MaxNamespaceNum

    @property
    def MaxTopicNum(self):
        """最大Topic数量
        :rtype: int
        """
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def MaxQps(self):
        """最大QPS
        :rtype: int
        """
        return self._MaxQps

    @MaxQps.setter
    def MaxQps(self, MaxQps):
        self._MaxQps = MaxQps

    @property
    def MessageRetentionTime(self):
        """最大消息保留时间，秒为单位
        :rtype: int
        """
        return self._MessageRetentionTime

    @MessageRetentionTime.setter
    def MessageRetentionTime(self, MessageRetentionTime):
        self._MessageRetentionTime = MessageRetentionTime

    @property
    def MaxStorageCapacity(self):
        """最大存储容量
        :rtype: int
        """
        return self._MaxStorageCapacity

    @MaxStorageCapacity.setter
    def MaxStorageCapacity(self, MaxStorageCapacity):
        self._MaxStorageCapacity = MaxStorageCapacity

    @property
    def Version(self):
        """集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def PublicEndPoint(self):
        """公网访问接入点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicEndPoint

    @PublicEndPoint.setter
    def PublicEndPoint(self, PublicEndPoint):
        self._PublicEndPoint = PublicEndPoint

    @property
    def VpcEndPoint(self):
        """VPC访问接入点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcEndPoint

    @VpcEndPoint.setter
    def VpcEndPoint(self, VpcEndPoint):
        self._VpcEndPoint = VpcEndPoint

    @property
    def NamespaceNum(self):
        """命名空间数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NamespaceNum

    @NamespaceNum.setter
    def NamespaceNum(self, NamespaceNum):
        self._NamespaceNum = NamespaceNum

    @property
    def UsedStorageBudget(self):
        """已使用存储限制，MB为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UsedStorageBudget

    @UsedStorageBudget.setter
    def UsedStorageBudget(self, UsedStorageBudget):
        self._UsedStorageBudget = UsedStorageBudget

    @property
    def MaxPublishRateInMessages(self):
        """最大生产消息速率，以条数为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxPublishRateInMessages

    @MaxPublishRateInMessages.setter
    def MaxPublishRateInMessages(self, MaxPublishRateInMessages):
        self._MaxPublishRateInMessages = MaxPublishRateInMessages

    @property
    def MaxDispatchRateInMessages(self):
        """最大推送消息速率，以条数为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxDispatchRateInMessages

    @MaxDispatchRateInMessages.setter
    def MaxDispatchRateInMessages(self, MaxDispatchRateInMessages):
        self._MaxDispatchRateInMessages = MaxDispatchRateInMessages

    @property
    def MaxPublishRateInBytes(self):
        """最大生产消息速率，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxPublishRateInBytes

    @MaxPublishRateInBytes.setter
    def MaxPublishRateInBytes(self, MaxPublishRateInBytes):
        self._MaxPublishRateInBytes = MaxPublishRateInBytes

    @property
    def MaxDispatchRateInBytes(self):
        """最大推送消息速率，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxDispatchRateInBytes

    @MaxDispatchRateInBytes.setter
    def MaxDispatchRateInBytes(self, MaxDispatchRateInBytes):
        self._MaxDispatchRateInBytes = MaxDispatchRateInBytes

    @property
    def TopicNum(self):
        """已创建主题数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def MaxMessageDelayInSeconds(self):
        """最长消息延时，以秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxMessageDelayInSeconds

    @MaxMessageDelayInSeconds.setter
    def MaxMessageDelayInSeconds(self, MaxMessageDelayInSeconds):
        self._MaxMessageDelayInSeconds = MaxMessageDelayInSeconds

    @property
    def PublicAccessEnabled(self):
        """是否开启公网访问，不填时默认开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PayMode(self):
        """计费模式：
0: 按量计费
1: 包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ProjectId(self):
        """项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """项目名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def UpgradeProInstance(self):
        """是否支持升级专业版实例
        :rtype: bool
        """
        return self._UpgradeProInstance

    @UpgradeProInstance.setter
    def UpgradeProInstance(self, UpgradeProInstance):
        self._UpgradeProInstance = UpgradeProInstance


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._EndPointNum = params.get("EndPointNum")
        self._CreateTime = params.get("CreateTime")
        self._Healthy = params.get("Healthy")
        self._HealthyInfo = params.get("HealthyInfo")
        self._Status = params.get("Status")
        self._MaxNamespaceNum = params.get("MaxNamespaceNum")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._MaxQps = params.get("MaxQps")
        self._MessageRetentionTime = params.get("MessageRetentionTime")
        self._MaxStorageCapacity = params.get("MaxStorageCapacity")
        self._Version = params.get("Version")
        self._PublicEndPoint = params.get("PublicEndPoint")
        self._VpcEndPoint = params.get("VpcEndPoint")
        self._NamespaceNum = params.get("NamespaceNum")
        self._UsedStorageBudget = params.get("UsedStorageBudget")
        self._MaxPublishRateInMessages = params.get("MaxPublishRateInMessages")
        self._MaxDispatchRateInMessages = params.get("MaxDispatchRateInMessages")
        self._MaxPublishRateInBytes = params.get("MaxPublishRateInBytes")
        self._MaxDispatchRateInBytes = params.get("MaxDispatchRateInBytes")
        self._TopicNum = params.get("TopicNum")
        self._MaxMessageDelayInSeconds = params.get("MaxMessageDelayInSeconds")
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PayMode = params.get("PayMode")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._UpgradeProInstance = params.get("UpgradeProInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqDeadLetterPolicy(AbstractModel):
    """cmq DeadLetterPolicy

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueue: 死信队列。
        :type DeadLetterQueue: str
        :param _Policy: 死信队列策略。0:最大接收次数;1:最大未消费时间
        :type Policy: int
        :param _MaxTimeToLive: 最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
        :type MaxTimeToLive: int
        :param _MaxReceiveCount: 最大接收次数。Policy为0时必选，范围在1到1000。
        :type MaxReceiveCount: int
        """
        self._DeadLetterQueue = None
        self._Policy = None
        self._MaxTimeToLive = None
        self._MaxReceiveCount = None

    @property
    def DeadLetterQueue(self):
        """死信队列。
        :rtype: str
        """
        return self._DeadLetterQueue

    @DeadLetterQueue.setter
    def DeadLetterQueue(self, DeadLetterQueue):
        self._DeadLetterQueue = DeadLetterQueue

    @property
    def Policy(self):
        """死信队列策略。0:最大接收次数;1:最大未消费时间
        :rtype: int
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxTimeToLive(self):
        """最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
        :rtype: int
        """
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def MaxReceiveCount(self):
        """最大接收次数。Policy为0时必选，范围在1到1000。
        :rtype: int
        """
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount


    def _deserialize(self, params):
        self._DeadLetterQueue = params.get("DeadLetterQueue")
        self._Policy = params.get("Policy")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqDeadLetterSource(AbstractModel):
    """Cmq DeadLetterSource

    """

    def __init__(self):
        r"""
        :param _QueueId: 消息队列ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueId: str
        :param _QueueName: 消息队列名字。
        :type QueueName: str
        """
        self._QueueId = None
        self._QueueName = None

    @property
    def QueueId(self):
        """消息队列ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        """消息队列名字。
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
        


class CmqQueue(AbstractModel):
    """cmq 批量queue属性信息

    """

    def __init__(self):
        r"""
        :param _QueueId: 消息队列ID。
        :type QueueId: str
        :param _QueueName: 消息队列名字。
        :type QueueName: str
        :param _Qps: 每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
        :type Qps: int
        :param _Bps: 带宽限制。
        :type Bps: int
        :param _MaxDelaySeconds: 飞行消息最大保留时间，需要小于消息保留周期。
        :type MaxDelaySeconds: int
        :param _MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: 消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
        :type PollingWaitSeconds: int
        :param _MsgRetentionSeconds: 消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
        :type MsgRetentionSeconds: int
        :param _VisibilityTimeout: 消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
        :type VisibilityTimeout: int
        :param _MaxMsgSize: 消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
        :type MaxMsgSize: int
        :param _RewindSeconds: 回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
        :type RewindSeconds: int
        :param _CreateTime: 队列的创建时间。返回 Unix 时间戳，精确到毫秒。
        :type CreateTime: int
        :param _LastModifyTime: 最后一次修改队列属性的时间。返回 Unix 时间戳，精确到毫秒。
        :type LastModifyTime: int
        :param _ActiveMsgNum: 在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
        :type ActiveMsgNum: int
        :param _InactiveMsgNum: 在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
        :type InactiveMsgNum: int
        :param _DelayMsgNum: 延迟消息数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DelayMsgNum: int
        :param _RewindMsgNum: 已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type RewindMsgNum: int
        :param _MinMsgTime: 消息最小未消费时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type MinMsgTime: int
        :param _Transaction: 事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Transaction: bool
        :param _DeadLetterSource: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterSource: list of CmqDeadLetterSource
        :param _DeadLetterPolicy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqDeadLetterPolicy`
        :param _TransactionPolicy: 事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqTransactionPolicy`
        :param _CreateUin: 创建者Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param _Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
        :param _TenantId: 租户id
        :type TenantId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :type Status: int
        :param _MaxUnackedMsgNum: 最大未确认消息数量
        :type MaxUnackedMsgNum: int
        :param _MaxMsgBacklogSize: 最大消息堆积大小（字节）
        :type MaxMsgBacklogSize: int
        :param _RetentionSizeInMB: 队列可回溯存储空间，取值范围1024MB - 10240MB，0表示不开启
        :type RetentionSizeInMB: int
        """
        self._QueueId = None
        self._QueueName = None
        self._Qps = None
        self._Bps = None
        self._MaxDelaySeconds = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._MsgRetentionSeconds = None
        self._VisibilityTimeout = None
        self._MaxMsgSize = None
        self._RewindSeconds = None
        self._CreateTime = None
        self._LastModifyTime = None
        self._ActiveMsgNum = None
        self._InactiveMsgNum = None
        self._DelayMsgNum = None
        self._RewindMsgNum = None
        self._MinMsgTime = None
        self._Transaction = None
        self._DeadLetterSource = None
        self._DeadLetterPolicy = None
        self._TransactionPolicy = None
        self._CreateUin = None
        self._Tags = None
        self._Trace = None
        self._TenantId = None
        self._NamespaceName = None
        self._Status = None
        self._MaxUnackedMsgNum = None
        self._MaxMsgBacklogSize = None
        self._RetentionSizeInMB = None

    @property
    def QueueId(self):
        """消息队列ID。
        :rtype: str
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        """消息队列名字。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Qps(self):
        """每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Bps(self):
        """带宽限制。
        :rtype: int
        """
        return self._Bps

    @Bps.setter
    def Bps(self, Bps):
        self._Bps = Bps

    @property
    def MaxDelaySeconds(self):
        """飞行消息最大保留时间，需要小于消息保留周期。
        :rtype: int
        """
        return self._MaxDelaySeconds

    @MaxDelaySeconds.setter
    def MaxDelaySeconds(self, MaxDelaySeconds):
        self._MaxDelaySeconds = MaxDelaySeconds

    @property
    def MaxMsgHeapNum(self):
        """最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :rtype: int
        """
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        """消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
        :rtype: int
        """
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def MsgRetentionSeconds(self):
        """消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def VisibilityTimeout(self):
        """消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
        :rtype: int
        """
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        """消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def RewindSeconds(self):
        """回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
        :rtype: int
        """
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def CreateTime(self):
        """队列的创建时间。返回 Unix 时间戳，精确到毫秒。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastModifyTime(self):
        """最后一次修改队列属性的时间。返回 Unix 时间戳，精确到毫秒。
        :rtype: int
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def ActiveMsgNum(self):
        """在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
        :rtype: int
        """
        return self._ActiveMsgNum

    @ActiveMsgNum.setter
    def ActiveMsgNum(self, ActiveMsgNum):
        self._ActiveMsgNum = ActiveMsgNum

    @property
    def InactiveMsgNum(self):
        """在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
        :rtype: int
        """
        return self._InactiveMsgNum

    @InactiveMsgNum.setter
    def InactiveMsgNum(self, InactiveMsgNum):
        self._InactiveMsgNum = InactiveMsgNum

    @property
    def DelayMsgNum(self):
        """延迟消息数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DelayMsgNum

    @DelayMsgNum.setter
    def DelayMsgNum(self, DelayMsgNum):
        self._DelayMsgNum = DelayMsgNum

    @property
    def RewindMsgNum(self):
        """已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RewindMsgNum

    @RewindMsgNum.setter
    def RewindMsgNum(self, RewindMsgNum):
        self._RewindMsgNum = RewindMsgNum

    @property
    def MinMsgTime(self):
        """消息最小未消费时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinMsgTime

    @MinMsgTime.setter
    def MinMsgTime(self, MinMsgTime):
        self._MinMsgTime = MinMsgTime

    @property
    def Transaction(self):
        """事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def DeadLetterSource(self):
        """死信队列。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CmqDeadLetterSource
        """
        return self._DeadLetterSource

    @DeadLetterSource.setter
    def DeadLetterSource(self, DeadLetterSource):
        self._DeadLetterSource = DeadLetterSource

    @property
    def DeadLetterPolicy(self):
        """死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CmqDeadLetterPolicy`
        """
        return self._DeadLetterPolicy

    @DeadLetterPolicy.setter
    def DeadLetterPolicy(self, DeadLetterPolicy):
        self._DeadLetterPolicy = DeadLetterPolicy

    @property
    def TransactionPolicy(self):
        """事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CmqTransactionPolicy`
        """
        return self._TransactionPolicy

    @TransactionPolicy.setter
    def TransactionPolicy(self, TransactionPolicy):
        self._TransactionPolicy = TransactionPolicy

    @property
    def CreateUin(self):
        """创建者Uin。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Tags(self):
        """关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Trace(self):
        """消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def TenantId(self):
        """租户id
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def NamespaceName(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Status(self):
        """集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaxUnackedMsgNum(self):
        """最大未确认消息数量
        :rtype: int
        """
        return self._MaxUnackedMsgNum

    @MaxUnackedMsgNum.setter
    def MaxUnackedMsgNum(self, MaxUnackedMsgNum):
        self._MaxUnackedMsgNum = MaxUnackedMsgNum

    @property
    def MaxMsgBacklogSize(self):
        """最大消息堆积大小（字节）
        :rtype: int
        """
        return self._MaxMsgBacklogSize

    @MaxMsgBacklogSize.setter
    def MaxMsgBacklogSize(self, MaxMsgBacklogSize):
        self._MaxMsgBacklogSize = MaxMsgBacklogSize

    @property
    def RetentionSizeInMB(self):
        """队列可回溯存储空间，取值范围1024MB - 10240MB，0表示不开启
        :rtype: int
        """
        return self._RetentionSizeInMB

    @RetentionSizeInMB.setter
    def RetentionSizeInMB(self, RetentionSizeInMB):
        self._RetentionSizeInMB = RetentionSizeInMB


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._QueueName = params.get("QueueName")
        self._Qps = params.get("Qps")
        self._Bps = params.get("Bps")
        self._MaxDelaySeconds = params.get("MaxDelaySeconds")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._RewindSeconds = params.get("RewindSeconds")
        self._CreateTime = params.get("CreateTime")
        self._LastModifyTime = params.get("LastModifyTime")
        self._ActiveMsgNum = params.get("ActiveMsgNum")
        self._InactiveMsgNum = params.get("InactiveMsgNum")
        self._DelayMsgNum = params.get("DelayMsgNum")
        self._RewindMsgNum = params.get("RewindMsgNum")
        self._MinMsgTime = params.get("MinMsgTime")
        self._Transaction = params.get("Transaction")
        if params.get("DeadLetterSource") is not None:
            self._DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = CmqDeadLetterSource()
                obj._deserialize(item)
                self._DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self._DeadLetterPolicy = CmqDeadLetterPolicy()
            self._DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self._TransactionPolicy = CmqTransactionPolicy()
            self._TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self._CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Trace = params.get("Trace")
        self._TenantId = params.get("TenantId")
        self._NamespaceName = params.get("NamespaceName")
        self._Status = params.get("Status")
        self._MaxUnackedMsgNum = params.get("MaxUnackedMsgNum")
        self._MaxMsgBacklogSize = params.get("MaxMsgBacklogSize")
        self._RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqSubscription(AbstractModel):
    """cmq订阅返回参数

    """

    def __init__(self):
        r"""
        :param _SubscriptionName: 订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        :param _SubscriptionId: 订阅 ID。订阅 ID 在拉取监控数据时会用到。
        :type SubscriptionId: str
        :param _TopicOwner: 订阅拥有者的 APPID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicOwner: int
        :param _MsgCount: 该订阅待投递的消息数。
        :type MsgCount: int
        :param _LastModifyTime: 最后一次修改订阅属性的时间。返回 Unix 时间戳，精确到毫秒。
        :type LastModifyTime: int
        :param _CreateTime: 订阅的创建时间。返回 Unix 时间戳，精确到毫秒。
        :type CreateTime: int
        :param _BindingKey: 表示订阅接收消息的过滤策略。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingKey: list of str
        :param _Endpoint: 接收通知的 endpoint，根据协议 protocol 区分：对于 HTTP，endpoint 必须以http://开头，host 可以是域名或 IP；对于 queue，则填 queueName。
        :type Endpoint: str
        :param _FilterTags: 描述用户创建订阅时选择的过滤策略：
filterType = 1表示用户使用 filterTag 标签过滤
filterType = 2表示用户使用 bindingKey 过滤。
        :type FilterTags: list of str
        :param _Protocol: 订阅的协议，目前支持两种协议：HTTP、queue。使用 HTTP 协议，用户需自己搭建接受消息的 Web Server。使用 queue，消息会自动推送到 CMQ queue，用户可以并发地拉取消息。
        :type Protocol: str
        :param _NotifyStrategy: 向 endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值有：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始 1s，后面是 2s，4s，8s...由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
        :type NotifyStrategy: str
        :param _NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 protocol 是 queue，则取值必须为 SIMPLIFIED。如果 protocol 是 HTTP，两个值均可以，默认值是 JSON。
        :type NotifyContentFormat: str
        :param _TopicName: 订阅所属的主题名称
        :type TopicName: str
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
        self._TopicName = None

    @property
    def SubscriptionName(self):
        """订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def SubscriptionId(self):
        """订阅 ID。订阅 ID 在拉取监控数据时会用到。
        :rtype: str
        """
        return self._SubscriptionId

    @SubscriptionId.setter
    def SubscriptionId(self, SubscriptionId):
        self._SubscriptionId = SubscriptionId

    @property
    def TopicOwner(self):
        """订阅拥有者的 APPID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicOwner

    @TopicOwner.setter
    def TopicOwner(self, TopicOwner):
        self._TopicOwner = TopicOwner

    @property
    def MsgCount(self):
        """该订阅待投递的消息数。
        :rtype: int
        """
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def LastModifyTime(self):
        """最后一次修改订阅属性的时间。返回 Unix 时间戳，精确到毫秒。
        :rtype: int
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def CreateTime(self):
        """订阅的创建时间。返回 Unix 时间戳，精确到毫秒。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BindingKey(self):
        """表示订阅接收消息的过滤策略。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey

    @property
    def Endpoint(self):
        """接收通知的 endpoint，根据协议 protocol 区分：对于 HTTP，endpoint 必须以http://开头，host 可以是域名或 IP；对于 queue，则填 queueName。
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def FilterTags(self):
        """描述用户创建订阅时选择的过滤策略：
filterType = 1表示用户使用 filterTag 标签过滤
filterType = 2表示用户使用 bindingKey 过滤。
        :rtype: list of str
        """
        return self._FilterTags

    @FilterTags.setter
    def FilterTags(self, FilterTags):
        self._FilterTags = FilterTags

    @property
    def Protocol(self):
        """订阅的协议，目前支持两种协议：HTTP、queue。使用 HTTP 协议，用户需自己搭建接受消息的 Web Server。使用 queue，消息会自动推送到 CMQ queue，用户可以并发地拉取消息。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NotifyStrategy(self):
        """向 endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值有：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始 1s，后面是 2s，4s，8s...由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
        :rtype: str
        """
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def NotifyContentFormat(self):
        """推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 protocol 是 queue，则取值必须为 SIMPLIFIED。如果 protocol 是 HTTP，两个值均可以，默认值是 JSON。
        :rtype: str
        """
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat

    @property
    def TopicName(self):
        """订阅所属的主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


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
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqTopic(AbstractModel):
    """cmq topic返回信息展示字段

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题的 ID。
        :type TopicId: str
        :param _TopicName: 主题名称。
        :type TopicName: str
        :param _MsgRetentionSeconds: 消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
        :type MsgRetentionSeconds: int
        :param _MaxMsgSize: 消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为1048576。
        :type MaxMsgSize: int
        :param _Qps: 每秒钟发布消息的条数。
        :type Qps: int
        :param _FilterType: 描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
        :type FilterType: int
        :param _CreateTime: 主题的创建时间。返回 Unix 时间戳，精确到毫秒。
        :type CreateTime: int
        :param _LastModifyTime: 最后一次修改主题属性的时间。返回 Unix 时间戳，精确到毫秒。
        :type LastModifyTime: int
        :param _MsgCount: 当前该主题中消息数目（消息堆积数）。
        :type MsgCount: int
        :param _CreateUin: 创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param _Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type Trace: bool
        :param _TenantId: 租户id
        :type TenantId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :type Status: int
        :param _BrokerType: 0表示pulsar，1表示rocketmq
        :type BrokerType: int
        :param _SubscriptionCount: 订阅数量
        :type SubscriptionCount: int
        """
        self._TopicId = None
        self._TopicName = None
        self._MsgRetentionSeconds = None
        self._MaxMsgSize = None
        self._Qps = None
        self._FilterType = None
        self._CreateTime = None
        self._LastModifyTime = None
        self._MsgCount = None
        self._CreateUin = None
        self._Tags = None
        self._Trace = None
        self._TenantId = None
        self._NamespaceName = None
        self._Status = None
        self._BrokerType = None
        self._SubscriptionCount = None

    @property
    def TopicId(self):
        """主题的 ID。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgRetentionSeconds(self):
        """消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def MaxMsgSize(self):
        """消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为1048576。
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def Qps(self):
        """每秒钟发布消息的条数。
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def FilterType(self):
        """描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def CreateTime(self):
        """主题的创建时间。返回 Unix 时间戳，精确到毫秒。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastModifyTime(self):
        """最后一次修改主题属性的时间。返回 Unix 时间戳，精确到毫秒。
        :rtype: int
        """
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def MsgCount(self):
        """当前该主题中消息数目（消息堆积数）。
        :rtype: int
        """
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def CreateUin(self):
        """创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Tags(self):
        """关联的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Trace(self):
        """消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def TenantId(self):
        """租户id
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def NamespaceName(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Status(self):
        """集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BrokerType(self):
        """0表示pulsar，1表示rocketmq
        :rtype: int
        """
        return self._BrokerType

    @BrokerType.setter
    def BrokerType(self, BrokerType):
        self._BrokerType = BrokerType

    @property
    def SubscriptionCount(self):
        """订阅数量
        :rtype: int
        """
        return self._SubscriptionCount

    @SubscriptionCount.setter
    def SubscriptionCount(self, SubscriptionCount):
        self._SubscriptionCount = SubscriptionCount


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._Qps = params.get("Qps")
        self._FilterType = params.get("FilterType")
        self._CreateTime = params.get("CreateTime")
        self._LastModifyTime = params.get("LastModifyTime")
        self._MsgCount = params.get("MsgCount")
        self._CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Trace = params.get("Trace")
        self._TenantId = params.get("TenantId")
        self._NamespaceName = params.get("NamespaceName")
        self._Status = params.get("Status")
        self._BrokerType = params.get("BrokerType")
        self._SubscriptionCount = params.get("SubscriptionCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqTransactionPolicy(AbstractModel):
    """cmq TransactionPolicy

    """

    def __init__(self):
        r"""
        :param _FirstQueryInterval: 第一次回查时间。
        :type FirstQueryInterval: int
        :param _MaxQueryCount: 最大查询次数。
        :type MaxQueryCount: int
        """
        self._FirstQueryInterval = None
        self._MaxQueryCount = None

    @property
    def FirstQueryInterval(self):
        """第一次回查时间。
        :rtype: int
        """
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        """最大查询次数。
        :rtype: int
        """
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount


    def _deserialize(self, params):
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        self._MaxQueryCount = params.get("MaxQueryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Consumer(AbstractModel):
    """消费者

    """

    def __init__(self):
        r"""
        :param _ConnectedSince: 消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectedSince: str
        :param _ConsumerAddr: 消费者地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerAddr: str
        :param _ConsumerName: 消费者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerName: str
        :param _ClientVersion: 消费者版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientVersion: str
        :param _Partition: 消费者连接的主题分区号
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: int
        """
        self._ConnectedSince = None
        self._ConsumerAddr = None
        self._ConsumerName = None
        self._ClientVersion = None
        self._Partition = None

    @property
    def ConnectedSince(self):
        """消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConnectedSince

    @ConnectedSince.setter
    def ConnectedSince(self, ConnectedSince):
        self._ConnectedSince = ConnectedSince

    @property
    def ConsumerAddr(self):
        """消费者地址。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerAddr

    @ConsumerAddr.setter
    def ConsumerAddr(self, ConsumerAddr):
        self._ConsumerAddr = ConsumerAddr

    @property
    def ConsumerName(self):
        """消费者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerName

    @ConsumerName.setter
    def ConsumerName(self, ConsumerName):
        self._ConsumerName = ConsumerName

    @property
    def ClientVersion(self):
        """消费者版本。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientVersion

    @ClientVersion.setter
    def ClientVersion(self, ClientVersion):
        self._ClientVersion = ClientVersion

    @property
    def Partition(self):
        """消费者连接的主题分区号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._ConnectedSince = params.get("ConnectedSince")
        self._ConsumerAddr = params.get("ConsumerAddr")
        self._ConsumerName = params.get("ConsumerName")
        self._ClientVersion = params.get("ClientVersion")
        self._Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerLog(AbstractModel):
    """消费日志

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息ID。
        :type MsgId: str
        :param _ConsumerGroup: 消费组。
        :type ConsumerGroup: str
        :param _ConsumerName: 消费者名称。
        :type ConsumerName: str
        :param _ConsumeTime: 消费时间。
        :type ConsumeTime: str
        :param _ConsumerAddr: 消费者客户端地址。
        :type ConsumerAddr: str
        :param _ConsumeUseTime: 消费耗时（毫秒）。
        :type ConsumeUseTime: int
        :param _Status: 消费状态。
        :type Status: str
        """
        self._MsgId = None
        self._ConsumerGroup = None
        self._ConsumerName = None
        self._ConsumeTime = None
        self._ConsumerAddr = None
        self._ConsumeUseTime = None
        self._Status = None

    @property
    def MsgId(self):
        """消息ID。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ConsumerGroup(self):
        """消费组。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def ConsumerName(self):
        """消费者名称。
        :rtype: str
        """
        return self._ConsumerName

    @ConsumerName.setter
    def ConsumerName(self, ConsumerName):
        self._ConsumerName = ConsumerName

    @property
    def ConsumeTime(self):
        """消费时间。
        :rtype: str
        """
        return self._ConsumeTime

    @ConsumeTime.setter
    def ConsumeTime(self, ConsumeTime):
        self._ConsumeTime = ConsumeTime

    @property
    def ConsumerAddr(self):
        """消费者客户端地址。
        :rtype: str
        """
        return self._ConsumerAddr

    @ConsumerAddr.setter
    def ConsumerAddr(self, ConsumerAddr):
        self._ConsumerAddr = ConsumerAddr

    @property
    def ConsumeUseTime(self):
        """消费耗时（毫秒）。
        :rtype: int
        """
        return self._ConsumeUseTime

    @ConsumeUseTime.setter
    def ConsumeUseTime(self, ConsumeUseTime):
        self._ConsumeUseTime = ConsumeUseTime

    @property
    def Status(self):
        """消费状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._ConsumerName = params.get("ConsumerName")
        self._ConsumeTime = params.get("ConsumeTime")
        self._ConsumerAddr = params.get("ConsumerAddr")
        self._ConsumeUseTime = params.get("ConsumeUseTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerLogs(AbstractModel):
    """消费信息

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ConsumerLogSets: 消费日志。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLogSets: list of ConsumerLog
        """
        self._TotalCount = None
        self._ConsumerLogSets = None

    @property
    def TotalCount(self):
        """记录数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConsumerLogSets(self):
        """消费日志。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConsumerLog
        """
        return self._ConsumerLogSets

    @ConsumerLogSets.setter
    def ConsumerLogSets(self, ConsumerLogSets):
        self._ConsumerLogSets = ConsumerLogSets


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConsumerLogSets") is not None:
            self._ConsumerLogSets = []
            for item in params.get("ConsumerLogSets"):
                obj = ConsumerLog()
                obj._deserialize(item)
                self._ConsumerLogSets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerStats(AbstractModel):
    """消费详情

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _BrokerName: 所属Broker
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerName: str
        :param _QueueId: 队列编号
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueId: int
        :param _ConsumerClientId: 消费者ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerClientId: str
        :param _ConsumerOffset: 消费位点
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerOffset: int
        :param _BrokerOffset: 服务端位点
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerOffset: int
        :param _DiffTotal: 消息堆积条数
注意：此字段可能返回 null，表示取不到有效值。
        :type DiffTotal: int
        :param _LastTimestamp: 最近消费时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTimestamp: int
        """
        self._TopicName = None
        self._BrokerName = None
        self._QueueId = None
        self._ConsumerClientId = None
        self._ConsumerOffset = None
        self._BrokerOffset = None
        self._DiffTotal = None
        self._LastTimestamp = None

    @property
    def TopicName(self):
        """主题名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def BrokerName(self):
        """所属Broker
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BrokerName

    @BrokerName.setter
    def BrokerName(self, BrokerName):
        self._BrokerName = BrokerName

    @property
    def QueueId(self):
        """队列编号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def ConsumerClientId(self):
        """消费者ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerClientId

    @ConsumerClientId.setter
    def ConsumerClientId(self, ConsumerClientId):
        self._ConsumerClientId = ConsumerClientId

    @property
    def ConsumerOffset(self):
        """消费位点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConsumerOffset

    @ConsumerOffset.setter
    def ConsumerOffset(self, ConsumerOffset):
        self._ConsumerOffset = ConsumerOffset

    @property
    def BrokerOffset(self):
        """服务端位点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BrokerOffset

    @BrokerOffset.setter
    def BrokerOffset(self, BrokerOffset):
        self._BrokerOffset = BrokerOffset

    @property
    def DiffTotal(self):
        """消息堆积条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DiffTotal

    @DiffTotal.setter
    def DiffTotal(self, DiffTotal):
        self._DiffTotal = DiffTotal

    @property
    def LastTimestamp(self):
        """最近消费时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastTimestamp

    @LastTimestamp.setter
    def LastTimestamp(self, LastTimestamp):
        self._LastTimestamp = LastTimestamp


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._BrokerName = params.get("BrokerName")
        self._QueueId = params.get("QueueId")
        self._ConsumerClientId = params.get("ConsumerClientId")
        self._ConsumerOffset = params.get("ConsumerOffset")
        self._BrokerOffset = params.get("BrokerOffset")
        self._DiffTotal = params.get("DiffTotal")
        self._LastTimestamp = params.get("LastTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumersSchedule(AbstractModel):
    """消费进度详情

    """

    def __init__(self):
        r"""
        :param _Partitions: 当前分区id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param _NumberOfEntries: 消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfEntries: int
        :param _MsgBacklog: 消息积压数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgBacklog: int
        :param _MsgRateOut: 消费者每秒分发消息的数量之和。
        :type MsgRateOut: str
        :param _MsgThroughputOut: 消费者每秒消息的byte。
        :type MsgThroughputOut: str
        :param _MsgRateExpired: 超时丢弃比例。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateExpired: str
        """
        self._Partitions = None
        self._NumberOfEntries = None
        self._MsgBacklog = None
        self._MsgRateOut = None
        self._MsgThroughputOut = None
        self._MsgRateExpired = None

    @property
    def Partitions(self):
        """当前分区id。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def NumberOfEntries(self):
        """消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NumberOfEntries

    @NumberOfEntries.setter
    def NumberOfEntries(self, NumberOfEntries):
        self._NumberOfEntries = NumberOfEntries

    @property
    def MsgBacklog(self):
        """消息积压数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MsgBacklog

    @MsgBacklog.setter
    def MsgBacklog(self, MsgBacklog):
        self._MsgBacklog = MsgBacklog

    @property
    def MsgRateOut(self):
        """消费者每秒分发消息的数量之和。
        :rtype: str
        """
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputOut(self):
        """消费者每秒消息的byte。
        :rtype: str
        """
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def MsgRateExpired(self):
        """超时丢弃比例。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgRateExpired

    @MsgRateExpired.setter
    def MsgRateExpired(self, MsgRateExpired):
        self._MsgRateExpired = MsgRateExpired


    def _deserialize(self, params):
        self._Partitions = params.get("Partitions")
        self._NumberOfEntries = params.get("NumberOfEntries")
        self._MsgBacklog = params.get("MsgBacklog")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._MsgRateExpired = params.get("MsgRateExpired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterName: 集群名称，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
        :type ClusterName: str
        :param _BindClusterId: 用户专享物理集群ID，如果不传，则默认在公共集群上创建用户集群资源。
        :type BindClusterId: int
        :param _Remark: 说明，128个字符以内。
        :type Remark: str
        :param _Tags: 集群的标签列表(已废弃)
        :type Tags: list of Tag
        :param _PublicAccessEnabled: 是否开启公网访问，不填时默认开启
        :type PublicAccessEnabled: bool
        """
        self._ClusterName = None
        self._BindClusterId = None
        self._Remark = None
        self._Tags = None
        self._PublicAccessEnabled = None

    @property
    def ClusterName(self):
        """集群名称，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def BindClusterId(self):
        """用户专享物理集群ID，如果不传，则默认在公共集群上创建用户集群资源。
        :rtype: int
        """
        return self._BindClusterId

    @BindClusterId.setter
    def BindClusterId(self, BindClusterId):
        self._BindClusterId = BindClusterId

    @property
    def Remark(self):
        """说明，128个字符以内。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Tags(self):
        """集群的标签列表(已废弃)
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PublicAccessEnabled(self):
        """是否开启公网访问，不填时默认开启
        :rtype: bool
        """
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        self._BindClusterId = params.get("BindClusterId")
        self._Remark = params.get("Remark")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateCmqQueueRequest(AbstractModel):
    """CreateCmqQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一账号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param _MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :type VisibilityTimeout: int
        :param _MaxMsgSize: 消息最大长度。取值范围 1024-1048576 Byte（即1-1024K），默认值 1048576。
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: 消息最长未确认时间。取值范围 30-43200 秒（30秒~12小时），默认值 3600 (1 小时)。
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: 队列是否开启回溯消息能力，该参数取值范围0-1296000，0表示不开启。
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
        :param _Tags: 标签数组
        :type Tags: list of Tag
        :param _RetentionSizeInMB: 队列可回溯存储空间：若开启消息回溯，取值范围：10240MB - 512000MB，若不开启消息回溯，取值：0
        :type RetentionSizeInMB: int
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
        self._Tags = None
        self._RetentionSizeInMB = None

    @property
    def QueueName(self):
        """队列名字，在单个地域同一账号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MaxMsgHeapNum(self):
        """最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :rtype: int
        """
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        """消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :rtype: int
        """
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def VisibilityTimeout(self):
        """消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :rtype: int
        """
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        """消息最大长度。取值范围 1024-1048576 Byte（即1-1024K），默认值 1048576。
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        """消息最长未确认时间。取值范围 30-43200 秒（30秒~12小时），默认值 3600 (1 小时)。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def RewindSeconds(self):
        """队列是否开启回溯消息能力，该参数取值范围0-1296000，0表示不开启。
        :rtype: int
        """
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def Transaction(self):
        """1 表示事务队列，0 表示普通队列
        :rtype: int
        """
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def FirstQueryInterval(self):
        """第一次回查间隔
        :rtype: int
        """
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        """最大回查次数
        :rtype: int
        """
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def DeadLetterQueueName(self):
        """死信队列名称
        :rtype: str
        """
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def Policy(self):
        """死信策略。0为消息被多次消费未删除，1为Time-To-Live过期
        :rtype: int
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxReceiveCount(self):
        """最大接收次数 1-1000
        :rtype: int
        """
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount

    @property
    def MaxTimeToLive(self):
        """policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds
        :rtype: int
        """
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def Trace(self):
        """是否开启消息轨迹追踪，当不设置字段时，默认为不开启，该字段为true表示开启，为false表示不开启
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def Tags(self):
        """标签数组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RetentionSizeInMB(self):
        """队列可回溯存储空间：若开启消息回溯，取值范围：10240MB - 512000MB，若不开启消息回溯，取值：0
        :rtype: int
        """
        return self._RetentionSizeInMB

    @RetentionSizeInMB.setter
    def RetentionSizeInMB(self, RetentionSizeInMB):
        self._RetentionSizeInMB = RetentionSizeInMB


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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqQueueResponse(AbstractModel):
    """CreateCmqQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueId: 创建成功的queueId
        :type QueueId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueId = None
        self._RequestId = None

    @property
    def QueueId(self):
        """创建成功的queueId
        :rtype: str
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

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
        self._QueueId = params.get("QueueId")
        self._RequestId = params.get("RequestId")


class CreateCmqSubscribeRequest(AbstractModel):
    """CreateCmqSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
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
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        """订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def Protocol(self):
        """订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Endpoint(self):
        """接收通知的Endpoint，根据协议Protocol区分：对于http，Endpoint必须以“`http://`”开头，host可以是域名或IP；对于Queue，则填QueueName。 请注意，目前推送服务不能推送到私有网络中，因此Endpoint填写为私有网络域名或地址将接收不到推送的消息，目前支持推送到公网和基础网络。
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def NotifyStrategy(self):
        """向Endpoint推送消息出现错误时，CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s...由于Topic消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是EXPONENTIAL_DECAY_RETRY。
        :rtype: str
        """
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def FilterTag(self):
        """消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。
        :rtype: list of str
        """
        return self._FilterTag

    @FilterTag.setter
    def FilterTag(self, FilterTag):
        self._FilterTag = FilterTag

    @property
    def BindingKey(self):
        """BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。
        :rtype: list of str
        """
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey

    @property
    def NotifyContentFormat(self):
        """推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，则取值必须为SIMPLIFIED。如果Protocol是http，两个值均可以，默认值是JSON。
        :rtype: str
        """
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
        


class CreateCmqSubscribeResponse(AbstractModel):
    """CreateCmqSubscribe返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscriptionId: 订阅id
        :type SubscriptionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscriptionId = None
        self._RequestId = None

    @property
    def SubscriptionId(self):
        """订阅id
        :rtype: str
        """
        return self._SubscriptionId

    @SubscriptionId.setter
    def SubscriptionId(self, SubscriptionId):
        self._SubscriptionId = SubscriptionId

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
        self._SubscriptionId = params.get("SubscriptionId")
        self._RequestId = params.get("RequestId")


class CreateCmqTopicRequest(AbstractModel):
    """CreateCmqTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :type MaxMsgSize: int
        :param _FilterType: 用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略，默认值为标签匹配策略。
        :type FilterType: int
        :param _MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。
        :type MsgRetentionSeconds: int
        :param _Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        :param _Tags: 标签数组
        :type Tags: list of Tag
        """
        self._TopicName = None
        self._MaxMsgSize = None
        self._FilterType = None
        self._MsgRetentionSeconds = None
        self._Trace = None
        self._Tags = None

    @property
    def TopicName(self):
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MaxMsgSize(self):
        """消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def FilterType(self):
        """用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略，默认值为标签匹配策略。
        :rtype: int
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def MsgRetentionSeconds(self):
        """消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Trace(self):
        """是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def Tags(self):
        """标签数组
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._FilterType = params.get("FilterType")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._Trace = params.get("Trace")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqTopicResponse(AbstractModel):
    """CreateCmqTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题id
        :type TopicId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        """主题id
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

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
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。
        :type EnvironmentId: str
        :param _MsgTTL: 未消费消息过期时间，单位：秒，取值范围：60秒~15天。
        :type MsgTTL: int
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _Remark: 说明，128个字符以内。
        :type Remark: str
        :param _RetentionPolicy: 消息保留策略
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        :param _AutoSubscriptionCreation: 是否开启自动创建订阅
        :type AutoSubscriptionCreation: bool
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._ClusterId = None
        self._Remark = None
        self._RetentionPolicy = None
        self._AutoSubscriptionCreation = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒，取值范围：60秒~15天。
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        """说明，128个字符以内。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RetentionPolicy(self):
        """消息保留策略
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        return self._RetentionPolicy

    @RetentionPolicy.setter
    def RetentionPolicy(self, RetentionPolicy):
        self._RetentionPolicy = RetentionPolicy

    @property
    def AutoSubscriptionCreation(self):
        """是否开启自动创建订阅
        :rtype: bool
        """
        return self._AutoSubscriptionCreation

    @AutoSubscriptionCreation.setter
    def AutoSubscriptionCreation(self, AutoSubscriptionCreation):
        self._AutoSubscriptionCreation = AutoSubscriptionCreation


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        if params.get("RetentionPolicy") is not None:
            self._RetentionPolicy = RetentionPolicy()
            self._RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        self._AutoSubscriptionCreation = params.get("AutoSubscriptionCreation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _MsgTTL: 未消费消息过期时间，单位：秒。
        :type MsgTTL: int
        :param _Remark: 说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._Remark = None
        self._NamespaceId = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒。
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def Remark(self):
        """说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def NamespaceId(self):
        """命名空间ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

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
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._Remark = params.get("Remark")
        self._NamespaceId = params.get("NamespaceId")
        self._RequestId = params.get("RequestId")


class CreateEnvironmentRoleRequest(AbstractModel):
    """CreateEnvironmentRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _RoleName: 角色名称。
        :type RoleName: str
        :param _Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param _ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        """角色名称。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        """授权项，最多只能包含produce、consume两项的非空字符串数组。
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def ClusterId(self):
        """必填字段，集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRoleResponse(AbstractModel):
    """CreateEnvironmentRole返回参数结构体

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


class CreateProClusterRequest(AbstractModel):
    """CreateProCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneIds: 多可用区部署选择三个可用区，示例[200002,200003,200004]

单可用区部署选择一个可用区，示例[200002]
        :type ZoneIds: list of int
        :param _ProductName: 集群规格代号
参考 [专业集群规格](https://cloud.tencent.com/document/product/1179/83705)
        :type ProductName: str
        :param _StorageSize: 存储规格
参考 [专业集群规格](https://cloud.tencent.com/document/product/1179/83705)
        :type StorageSize: int
        :param _AutoRenewFlag: 1: true，开启自动按月续费

0: false，关闭自动按月续费
        :type AutoRenewFlag: int
        :param _TimeSpan: 购买时长，取值范围：1～50
        :type TimeSpan: int
        :param _ClusterName: 集群名称，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
        :type ClusterName: str
        :param _AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param _Vpc: vpc网络标签
        :type Vpc: :class:`tencentcloud.tdmq.v20200217.models.VpcInfo`
        :param _Tags: 集群的标签列表(已废弃)
        :type Tags: list of Tag
        """
        self._ZoneIds = None
        self._ProductName = None
        self._StorageSize = None
        self._AutoRenewFlag = None
        self._TimeSpan = None
        self._ClusterName = None
        self._AutoVoucher = None
        self._Vpc = None
        self._Tags = None

    @property
    def ZoneIds(self):
        """多可用区部署选择三个可用区，示例[200002,200003,200004]

单可用区部署选择一个可用区，示例[200002]
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def ProductName(self):
        """集群规格代号
参考 [专业集群规格](https://cloud.tencent.com/document/product/1179/83705)
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def StorageSize(self):
        """存储规格
参考 [专业集群规格](https://cloud.tencent.com/document/product/1179/83705)
        :rtype: int
        """
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def AutoRenewFlag(self):
        """1: true，开启自动按月续费

0: false，关闭自动按月续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def TimeSpan(self):
        """购买时长，取值范围：1～50
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ClusterName(self):
        """集群名称，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AutoVoucher(self):
        """是否自动选择代金券 1是 0否 默认为0
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def Vpc(self):
        """vpc网络标签
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.VpcInfo`
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def Tags(self):
        """集群的标签列表(已废弃)
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ZoneIds = params.get("ZoneIds")
        self._ProductName = params.get("ProductName")
        self._StorageSize = params.get("StorageSize")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._ClusterName = params.get("ClusterName")
        self._AutoVoucher = params.get("AutoVoucher")
        if params.get("Vpc") is not None:
            self._Vpc = VpcInfo()
            self._Vpc._deserialize(params.get("Vpc"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProClusterResponse(AbstractModel):
    """CreateProCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 子订单号
        :type DealName: str
        :param _BigDealId: 订单号
        :type BigDealId: str
        :param _ClusterId: 集群Id
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._BigDealId = None
        self._ClusterId = None
        self._ClusterName = None
        self._RequestId = None

    @property
    def DealName(self):
        """子订单号
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def BigDealId(self):
        """订单号
        :rtype: str
        """
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId

    @property
    def ClusterId(self):
        """集群Id
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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DealName = params.get("DealName")
        self._BigDealId = params.get("BigDealId")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQBindingRequest(AbstractModel):
    """CreateRabbitMQBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost名称
        :type VirtualHost: str
        :param _Source: 源exchange
        :type Source: str
        :param _DestinationType: 目标类型,取值queue或exchange
        :type DestinationType: str
        :param _Destination: 目标
        :type Destination: str
        :param _RoutingKey: 路由键
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
        """Vhost名称
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
        """目标
        :rtype: str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def RoutingKey(self):
        """路由键
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
        


class CreateRabbitMQBindingResponse(AbstractModel):
    """CreateRabbitMQBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称
        :type InstanceId: str
        :param _VirtualHost: vhost名称
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
        """实例名称
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


class CreateRabbitMQUserRequest(AbstractModel):
    """CreateRabbitMQUser请求参数结构体

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
        :param _Tags: 用户标签，用于决定改用户访问RabbitMQ Management的权限范围
management：普通控制台用户，monitoring：管理型控制台用户，其他值：非控制台用户
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
        """用户标签，用于决定改用户访问RabbitMQ Management的权限范围
management：普通控制台用户，monitoring：管理型控制台用户，其他值：非控制台用户
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
        


class CreateRabbitMQUserResponse(AbstractModel):
    """CreateRabbitMQUser返回参数结构体

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


class CreateRabbitMQVipInstanceRequest(AbstractModel):
    """CreateRabbitMQVipInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneIds: 可用区
        :type ZoneIds: list of int
        :param _VpcId: 私有网络VpcId
        :type VpcId: str
        :param _SubnetId: 私有网络SubnetId
        :type SubnetId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _NodeSpec: 节点规格,基础型rabbit-vip-basic-1,标准型rabbit-vip-basic-2,高阶1型rabbit-vip-basic-3,高阶2型rabbit-vip-basic-4。不传默认为基础型
        :type NodeSpec: str
        :param _NodeNum: 节点数量,多可用区最少为3节点。不传默认单可用区为1,多可用区为3
        :type NodeNum: int
        :param _StorageSize: 单节点存储规格,不传默认为200G
        :type StorageSize: int
        :param _EnableCreateDefaultHaMirrorQueue: 镜像队列,不传默认为false
        :type EnableCreateDefaultHaMirrorQueue: bool
        :param _AutoRenewFlag: 预付费使用。自动续费,不传默认为true
        :type AutoRenewFlag: bool
        :param _TimeSpan: 购买时长,不传默认为1(月)
        :type TimeSpan: int
        :param _PayMode: 付费方式，0 为后付费，即按量计费；1 为预付费，即包年包月。默认包年包月
        :type PayMode: int
        :param _ClusterVersion: 集群版本，不传默认为 3.8.30，可选值为 3.8.30 和 3.11.8
        :type ClusterVersion: str
        :param _IsIntl: 是否国际站请求，默认 false
        :type IsIntl: bool
        :param _ResourceTags: 资源标签列表
        :type ResourceTags: list of Tag
        :param _Bandwidth: 公网带宽大小，单位 M
        :type Bandwidth: int
        :param _EnablePublicAccess: 是否打开公网接入，不传默认为false
        :type EnablePublicAccess: bool
        """
        self._ZoneIds = None
        self._VpcId = None
        self._SubnetId = None
        self._ClusterName = None
        self._NodeSpec = None
        self._NodeNum = None
        self._StorageSize = None
        self._EnableCreateDefaultHaMirrorQueue = None
        self._AutoRenewFlag = None
        self._TimeSpan = None
        self._PayMode = None
        self._ClusterVersion = None
        self._IsIntl = None
        self._ResourceTags = None
        self._Bandwidth = None
        self._EnablePublicAccess = None

    @property
    def ZoneIds(self):
        """可用区
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def VpcId(self):
        """私有网络VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络SubnetId
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

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
    def NodeSpec(self):
        """节点规格,基础型rabbit-vip-basic-1,标准型rabbit-vip-basic-2,高阶1型rabbit-vip-basic-3,高阶2型rabbit-vip-basic-4。不传默认为基础型
        :rtype: str
        """
        return self._NodeSpec

    @NodeSpec.setter
    def NodeSpec(self, NodeSpec):
        self._NodeSpec = NodeSpec

    @property
    def NodeNum(self):
        """节点数量,多可用区最少为3节点。不传默认单可用区为1,多可用区为3
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def StorageSize(self):
        """单节点存储规格,不传默认为200G
        :rtype: int
        """
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def EnableCreateDefaultHaMirrorQueue(self):
        """镜像队列,不传默认为false
        :rtype: bool
        """
        return self._EnableCreateDefaultHaMirrorQueue

    @EnableCreateDefaultHaMirrorQueue.setter
    def EnableCreateDefaultHaMirrorQueue(self, EnableCreateDefaultHaMirrorQueue):
        self._EnableCreateDefaultHaMirrorQueue = EnableCreateDefaultHaMirrorQueue

    @property
    def AutoRenewFlag(self):
        """预付费使用。自动续费,不传默认为true
        :rtype: bool
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def TimeSpan(self):
        """购买时长,不传默认为1(月)
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PayMode(self):
        """付费方式，0 为后付费，即按量计费；1 为预付费，即包年包月。默认包年包月
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ClusterVersion(self):
        """集群版本，不传默认为 3.8.30，可选值为 3.8.30 和 3.11.8
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def IsIntl(self):
        """是否国际站请求，默认 false
        :rtype: bool
        """
        return self._IsIntl

    @IsIntl.setter
    def IsIntl(self, IsIntl):
        self._IsIntl = IsIntl

    @property
    def ResourceTags(self):
        """资源标签列表
        :rtype: list of Tag
        """
        return self._ResourceTags

    @ResourceTags.setter
    def ResourceTags(self, ResourceTags):
        self._ResourceTags = ResourceTags

    @property
    def Bandwidth(self):
        """公网带宽大小，单位 M
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def EnablePublicAccess(self):
        """是否打开公网接入，不传默认为false
        :rtype: bool
        """
        return self._EnablePublicAccess

    @EnablePublicAccess.setter
    def EnablePublicAccess(self, EnablePublicAccess):
        self._EnablePublicAccess = EnablePublicAccess


    def _deserialize(self, params):
        self._ZoneIds = params.get("ZoneIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ClusterName = params.get("ClusterName")
        self._NodeSpec = params.get("NodeSpec")
        self._NodeNum = params.get("NodeNum")
        self._StorageSize = params.get("StorageSize")
        self._EnableCreateDefaultHaMirrorQueue = params.get("EnableCreateDefaultHaMirrorQueue")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._PayMode = params.get("PayMode")
        self._ClusterVersion = params.get("ClusterVersion")
        self._IsIntl = params.get("IsIntl")
        if params.get("ResourceTags") is not None:
            self._ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ResourceTags.append(obj)
        self._Bandwidth = params.get("Bandwidth")
        self._EnablePublicAccess = params.get("EnablePublicAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQVipInstanceResponse(AbstractModel):
    """CreateRabbitMQVipInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 订单号Id
        :type TranId: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def TranId(self):
        """订单号Id
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateRabbitMQVirtualHostRequest(AbstractModel):
    """CreateRabbitMQVirtualHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        :param _Description: 描述
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
        """vhost名
        :rtype: str
        """
        return self._VirtualHost

    @VirtualHost.setter
    def VirtualHost(self, VirtualHost):
        self._VirtualHost = VirtualHost

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
        


class CreateRabbitMQVirtualHostResponse(AbstractModel):
    """CreateRabbitMQVirtualHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VirtualHost = None
        self._RequestId = None

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


class CreateRocketMQClusterRequest(AbstractModel):
    """CreateRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 集群名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type Name: str
        :param _Remark: 集群描述，128个字符以内
        :type Remark: str
        """
        self._Name = None
        self._Remark = None

    @property
    def Name(self):
        """集群名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """集群描述，128个字符以内
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQClusterResponse(AbstractModel):
    """CreateRocketMQCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateRocketMQEnvironmentRoleRequest(AbstractModel):
    """CreateRocketMQEnvironmentRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间
        :type EnvironmentId: str
        :param _RoleName: 角色名称。
        :type RoleName: str
        :param _Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param _ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        :param _DetailedPerms: Topic&Group维度权限配置
        :type DetailedPerms: list of DetailedRolePerm
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._ClusterId = None
        self._DetailedPerms = None

    @property
    def EnvironmentId(self):
        """命名空间
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        """角色名称。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        """授权项，最多只能包含produce、consume两项的非空字符串数组。
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def ClusterId(self):
        """必填字段，集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DetailedPerms(self):
        """Topic&Group维度权限配置
        :rtype: list of DetailedRolePerm
        """
        return self._DetailedPerms

    @DetailedPerms.setter
    def DetailedPerms(self, DetailedPerms):
        self._DetailedPerms = DetailedPerms


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._ClusterId = params.get("ClusterId")
        if params.get("DetailedPerms") is not None:
            self._DetailedPerms = []
            for item in params.get("DetailedPerms"):
                obj = DetailedRolePerm()
                obj._deserialize(item)
                self._DetailedPerms.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQEnvironmentRoleResponse(AbstractModel):
    """CreateRocketMQEnvironmentRole返回参数结构体

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


class CreateRocketMQGroupRequest(AbstractModel):
    """CreateRocketMQGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: Group名称，8~64个字符
        :type GroupId: str
        :param _Namespaces: 命名空间，目前只支持单个命名空间
        :type Namespaces: list of str
        :param _ReadEnable: 是否开启消费
        :type ReadEnable: bool
        :param _BroadcastEnable: 是否开启广播消费
        :type BroadcastEnable: bool
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Remark: 说明信息，最长128个字符
        :type Remark: str
        :param _GroupType: Group类型（TCP/HTTP）
        :type GroupType: str
        :param _RetryMaxTimes: Group最大重试次数
        :type RetryMaxTimes: int
        """
        self._GroupId = None
        self._Namespaces = None
        self._ReadEnable = None
        self._BroadcastEnable = None
        self._ClusterId = None
        self._Remark = None
        self._GroupType = None
        self._RetryMaxTimes = None

    @property
    def GroupId(self):
        """Group名称，8~64个字符
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Namespaces(self):
        """命名空间，目前只支持单个命名空间
        :rtype: list of str
        """
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def ReadEnable(self):
        """是否开启消费
        :rtype: bool
        """
        return self._ReadEnable

    @ReadEnable.setter
    def ReadEnable(self, ReadEnable):
        self._ReadEnable = ReadEnable

    @property
    def BroadcastEnable(self):
        """是否开启广播消费
        :rtype: bool
        """
        return self._BroadcastEnable

    @BroadcastEnable.setter
    def BroadcastEnable(self, BroadcastEnable):
        self._BroadcastEnable = BroadcastEnable

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
    def Remark(self):
        """说明信息，最长128个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def GroupType(self):
        """Group类型（TCP/HTTP）
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def RetryMaxTimes(self):
        """Group最大重试次数
        :rtype: int
        """
        return self._RetryMaxTimes

    @RetryMaxTimes.setter
    def RetryMaxTimes(self, RetryMaxTimes):
        self._RetryMaxTimes = RetryMaxTimes


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Namespaces = params.get("Namespaces")
        self._ReadEnable = params.get("ReadEnable")
        self._BroadcastEnable = params.get("BroadcastEnable")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._GroupType = params.get("GroupType")
        self._RetryMaxTimes = params.get("RetryMaxTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQGroupResponse(AbstractModel):
    """CreateRocketMQGroup返回参数结构体

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


class CreateRocketMQNamespaceRequest(AbstractModel):
    """CreateRocketMQNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type NamespaceId: str
        :param _Ttl: 已废弃
        :type Ttl: int
        :param _RetentionTime: 已废弃
        :type RetentionTime: int
        :param _Remark: 说明，最大128个字符
        :type Remark: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Ttl = None
        self._RetentionTime = None
        self._Remark = None

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
    def NamespaceId(self):
        """命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Ttl(self):
        """已废弃
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def RetentionTime(self):
        """已废弃
        :rtype: int
        """
        return self._RetentionTime

    @RetentionTime.setter
    def RetentionTime(self, RetentionTime):
        self._RetentionTime = RetentionTime

    @property
    def Remark(self):
        """说明，最大128个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Ttl = params.get("Ttl")
        self._RetentionTime = params.get("RetentionTime")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQNamespaceResponse(AbstractModel):
    """CreateRocketMQNamespace返回参数结构体

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


class CreateRocketMQRoleRequest(AbstractModel):
    """CreateRocketMQRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :type RoleName: str
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        :param _Remark: 备注说明，长度必须大等于0且小等于128。
        :type Remark: str
        :param _PermType: 角色授权类型（集群：Cluster; 主题或消费组：TopicAndGroup）
        :type PermType: str
        """
        self._RoleName = None
        self._ClusterId = None
        self._Remark = None
        self._PermType = None

    @property
    def RoleName(self):
        """角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        """备注说明，长度必须大等于0且小等于128。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PermType(self):
        """角色授权类型（集群：Cluster; 主题或消费组：TopicAndGroup）
        :rtype: str
        """
        return self._PermType

    @PermType.setter
    def PermType(self, PermType):
        self._PermType = PermType


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._PermType = params.get("PermType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQRoleResponse(AbstractModel):
    """CreateRocketMQRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _Token: 角色token
        :type Token: str
        :param _Remark: 备注说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleName = None
        self._Token = None
        self._Remark = None
        self._RequestId = None

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Token(self):
        """角色token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Remark(self):
        """备注说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

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
        self._RoleName = params.get("RoleName")
        self._Token = params.get("Token")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class CreateRocketMQTopicRequest(AbstractModel):
    """CreateRocketMQTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: 主题名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type Topic: str
        :param _Namespaces: 主题所在的命名空间，目前支持在单个命名空间下创建主题
        :type Namespaces: list of str
        :param _Type: 主题类型，可选值为Normal, GlobalOrder, PartitionedOrder, Transaction, DelayScheduled。Transaction仅在专享版支持。
        :type Type: str
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Remark: 主题说明，最大128个字符
        :type Remark: str
        :param _PartitionNum: 分区数，全局顺序无效
        :type PartitionNum: int
        """
        self._Topic = None
        self._Namespaces = None
        self._Type = None
        self._ClusterId = None
        self._Remark = None
        self._PartitionNum = None

    @property
    def Topic(self):
        """主题名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Namespaces(self):
        """主题所在的命名空间，目前支持在单个命名空间下创建主题
        :rtype: list of str
        """
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def Type(self):
        """主题类型，可选值为Normal, GlobalOrder, PartitionedOrder, Transaction, DelayScheduled。Transaction仅在专享版支持。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def Remark(self):
        """主题说明，最大128个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PartitionNum(self):
        """分区数，全局顺序无效
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Namespaces = params.get("Namespaces")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQTopicResponse(AbstractModel):
    """CreateRocketMQTopic返回参数结构体

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


class CreateRocketMQVipInstanceRequest(AbstractModel):
    """CreateRocketMQVipInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 实例名称
        :type Name: str
        :param _Spec: 集群规格，支持规格有 1.通用型:rocket-vip-basic-0; 2.基础型:rocket-vip-basic-1; 3.标准型:rocket-vip-basic-2; 4.高阶Ⅰ型:rocket-vip-basic-3; 5.高阶Ⅱ型:rocket-vip-basic-4
        :type Spec: str
        :param _NodeCount: 节点数量，最小2，最大20
        :type NodeCount: int
        :param _StorageSize: 单节点存储空间，GB为单位，最低200GB
        :type StorageSize: int
        :param _ZoneIds: 节点部署的区域ID列表，如广州一区，则是100001，具体可查询腾讯云官网
        :type ZoneIds: list of str
        :param _VpcInfo: VPC信息
        :type VpcInfo: :class:`tencentcloud.tdmq.v20200217.models.VpcInfo`
        :param _TimeSpan: 购买时长，月为单位
        :type TimeSpan: int
        :param _SupportsMigrateToCloud: 是否用于迁移上云，默认为false
        :type SupportsMigrateToCloud: bool
        :param _EnablePublic: 是否开启公网
        :type EnablePublic: bool
        :param _Bandwidth: 公网带宽，在开启公网情况下为必传字段
        :type Bandwidth: int
        :param _IpRules: 公网白名单
        :type IpRules: list of PublicAccessRule
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._Name = None
        self._Spec = None
        self._NodeCount = None
        self._StorageSize = None
        self._ZoneIds = None
        self._VpcInfo = None
        self._TimeSpan = None
        self._SupportsMigrateToCloud = None
        self._EnablePublic = None
        self._Bandwidth = None
        self._IpRules = None
        self._Tags = None

    @property
    def Name(self):
        """实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Spec(self):
        """集群规格，支持规格有 1.通用型:rocket-vip-basic-0; 2.基础型:rocket-vip-basic-1; 3.标准型:rocket-vip-basic-2; 4.高阶Ⅰ型:rocket-vip-basic-3; 5.高阶Ⅱ型:rocket-vip-basic-4
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def NodeCount(self):
        """节点数量，最小2，最大20
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def StorageSize(self):
        """单节点存储空间，GB为单位，最低200GB
        :rtype: int
        """
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def ZoneIds(self):
        """节点部署的区域ID列表，如广州一区，则是100001，具体可查询腾讯云官网
        :rtype: list of str
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def VpcInfo(self):
        """VPC信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.VpcInfo`
        """
        return self._VpcInfo

    @VpcInfo.setter
    def VpcInfo(self, VpcInfo):
        self._VpcInfo = VpcInfo

    @property
    def TimeSpan(self):
        """购买时长，月为单位
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def SupportsMigrateToCloud(self):
        """是否用于迁移上云，默认为false
        :rtype: bool
        """
        return self._SupportsMigrateToCloud

    @SupportsMigrateToCloud.setter
    def SupportsMigrateToCloud(self, SupportsMigrateToCloud):
        self._SupportsMigrateToCloud = SupportsMigrateToCloud

    @property
    def EnablePublic(self):
        """是否开启公网
        :rtype: bool
        """
        return self._EnablePublic

    @EnablePublic.setter
    def EnablePublic(self, EnablePublic):
        self._EnablePublic = EnablePublic

    @property
    def Bandwidth(self):
        """公网带宽，在开启公网情况下为必传字段
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        """公网白名单
        :rtype: list of PublicAccessRule
        """
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Spec = params.get("Spec")
        self._NodeCount = params.get("NodeCount")
        self._StorageSize = params.get("StorageSize")
        self._ZoneIds = params.get("ZoneIds")
        if params.get("VpcInfo") is not None:
            self._VpcInfo = VpcInfo()
            self._VpcInfo._deserialize(params.get("VpcInfo"))
        self._TimeSpan = params.get("TimeSpan")
        self._SupportsMigrateToCloud = params.get("SupportsMigrateToCloud")
        self._EnablePublic = params.get("EnablePublic")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("IpRules") is not None:
            self._IpRules = []
            for item in params.get("IpRules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._IpRules.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQVipInstanceResponse(AbstractModel):
    """CreateRocketMQVipInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :type RoleName: str
        :param _Remark: 备注说明，长度必须大等于0且小等于128。
        :type Remark: str
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        """
        self._RoleName = None
        self._Remark = None
        self._ClusterId = None

    @property
    def RoleName(self):
        """角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Remark(self):
        """备注说明，长度必须大等于0且小等于128。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Remark = params.get("Remark")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _Token: 角色token
        :type Token: str
        :param _Remark: 备注说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _EnvironmentRoleSets: 批量绑定名字空间
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentRoleSets: list of EnvironmentRoleSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleName = None
        self._Token = None
        self._Remark = None
        self._EnvironmentRoleSets = None
        self._RequestId = None

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Token(self):
        """角色token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Remark(self):
        """备注说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def EnvironmentRoleSets(self):
        """批量绑定名字空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EnvironmentRoleSet
        """
        return self._EnvironmentRoleSets

    @EnvironmentRoleSets.setter
    def EnvironmentRoleSets(self, EnvironmentRoleSets):
        self._EnvironmentRoleSets = EnvironmentRoleSets

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
        self._RoleName = params.get("RoleName")
        self._Token = params.get("Token")
        self._Remark = params.get("Remark")
        if params.get("EnvironmentRoleSets") is not None:
            self._EnvironmentRoleSets = []
            for item in params.get("EnvironmentRoleSets"):
                obj = EnvironmentRoleSet()
                obj._deserialize(item)
                self._EnvironmentRoleSets.append(obj)
        self._RequestId = params.get("RequestId")


class CreateSubscriptionRequest(AbstractModel):
    """CreateSubscription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名称。
        :type TopicName: str
        :param _SubscriptionName: 订阅者名称，不超过128个字符。
        :type SubscriptionName: str
        :param _IsIdempotent: 是否幂等创建，若否不允许创建同名的订阅关系。
        :type IsIdempotent: bool
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _Remark: 备注，128个字符以内。
        :type Remark: str
        :param _AutoCreatePolicyTopic: 是否自动创建死信和重试主题，True 表示创建，False表示不创建，默认自动创建死信和重试主题。
        :type AutoCreatePolicyTopic: bool
        :param _PostFixPattern: 指定死信和重试主题名称规范，LEGACY表示历史命名规则，COMMUNITY表示Pulsar社区命名规范
        :type PostFixPattern: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._SubscriptionName = None
        self._IsIdempotent = None
        self._ClusterId = None
        self._Remark = None
        self._AutoCreatePolicyTopic = None
        self._PostFixPattern = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        """订阅者名称，不超过128个字符。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def IsIdempotent(self):
        """是否幂等创建，若否不允许创建同名的订阅关系。
        :rtype: bool
        """
        return self._IsIdempotent

    @IsIdempotent.setter
    def IsIdempotent(self, IsIdempotent):
        self._IsIdempotent = IsIdempotent

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        """备注，128个字符以内。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def AutoCreatePolicyTopic(self):
        """是否自动创建死信和重试主题，True 表示创建，False表示不创建，默认自动创建死信和重试主题。
        :rtype: bool
        """
        return self._AutoCreatePolicyTopic

    @AutoCreatePolicyTopic.setter
    def AutoCreatePolicyTopic(self, AutoCreatePolicyTopic):
        self._AutoCreatePolicyTopic = AutoCreatePolicyTopic

    @property
    def PostFixPattern(self):
        """指定死信和重试主题名称规范，LEGACY表示历史命名规则，COMMUNITY表示Pulsar社区命名规范
        :rtype: str
        """
        return self._PostFixPattern

    @PostFixPattern.setter
    def PostFixPattern(self, PostFixPattern):
        self._PostFixPattern = PostFixPattern


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        self._IsIdempotent = params.get("IsIdempotent")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._AutoCreatePolicyTopic = params.get("AutoCreatePolicyTopic")
        self._PostFixPattern = params.get("PostFixPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscriptionResponse(AbstractModel):
    """CreateSubscription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建结果。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """创建结果。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
        :type TopicName: str
        :param _Partitions: 入参为1，即是创建非分区topic，无分区；入参大于1，表示分区topic的分区数，最大不允许超过32。
        :type Partitions: int
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _Remark: 备注，128字符以内。
        :type Remark: str
        :param _TopicType: 该入参将逐步弃用，可切换至PulsarTopicType参数
0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列。
        :type TopicType: int
        :param _PulsarTopicType: Pulsar 主题类型
0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
        :type PulsarTopicType: int
        :param _MsgTTL: 未消费消息过期时间，单位：秒，取值范围：60秒~15天。
        :type MsgTTL: int
        :param _UnackPolicy: 不传默认是原生策略，DefaultPolicy表示当订阅下达到最大未确认消息数 5000 时，服务端将不再向当前订阅下的所有消费者推送消息，DynamicPolicy表示动态调整订阅下的最大未确认消息数，具体配额是在 5000 和消费者数量*20之间取最大值。每个消费者默认最大 unack 消息数为 20，超过该限制时仅影响该消费者，不影响其他消费者。
        :type UnackPolicy: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Partitions = None
        self._ClusterId = None
        self._Remark = None
        self._TopicType = None
        self._PulsarTopicType = None
        self._MsgTTL = None
        self._UnackPolicy = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partitions(self):
        """入参为1，即是创建非分区topic，无分区；入参大于1，表示分区topic的分区数，最大不允许超过32。
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        """备注，128字符以内。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicType(self):
        """该入参将逐步弃用，可切换至PulsarTopicType参数
0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列。
        :rtype: int
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def PulsarTopicType(self):
        """Pulsar 主题类型
0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
        :rtype: int
        """
        return self._PulsarTopicType

    @PulsarTopicType.setter
    def PulsarTopicType(self, PulsarTopicType):
        self._PulsarTopicType = PulsarTopicType

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒，取值范围：60秒~15天。
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def UnackPolicy(self):
        """不传默认是原生策略，DefaultPolicy表示当订阅下达到最大未确认消息数 5000 时，服务端将不再向当前订阅下的所有消费者推送消息，DynamicPolicy表示动态调整订阅下的最大未确认消息数，具体配额是在 5000 和消费者数量*20之间取最大值。每个消费者默认最大 unack 消息数为 20，超过该限制时仅影响该消费者，不影响其他消费者。
        :rtype: str
        """
        return self._UnackPolicy

    @UnackPolicy.setter
    def UnackPolicy(self, UnackPolicy):
        self._UnackPolicy = UnackPolicy


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Partitions = params.get("Partitions")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._TopicType = params.get("TopicType")
        self._PulsarTopicType = params.get("PulsarTopicType")
        self._MsgTTL = params.get("MsgTTL")
        self._UnackPolicy = params.get("UnackPolicy")
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
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名。
        :type TopicName: str
        :param _Partitions: 0或1：非分区topic，无分区；大于1：具体分区topic的分区数。（存量非分区主题返回0，增量非分区主题返回1）
        :type Partitions: int
        :param _Remark: 备注，128字符以内。
        :type Remark: str
        :param _TopicType: 0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列；
        :type TopicType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Partitions = None
        self._Remark = None
        self._TopicType = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partitions(self):
        """0或1：非分区topic，无分区；大于1：具体分区topic的分区数。（存量非分区主题返回0，增量非分区主题返回1）
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Remark(self):
        """备注，128字符以内。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicType(self):
        """0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列；
        :rtype: int
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

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
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        self._TopicType = params.get("TopicType")
        self._RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id，传入需要删除的集群Id。
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群Id，传入需要删除的集群Id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群的ID
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        """集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class DeleteCmqQueueRequest(AbstractModel):
    """DeleteCmqQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一账号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        """队列名字，在单个地域同一账号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
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
        


class DeleteCmqQueueResponse(AbstractModel):
    """DeleteCmqQueue返回参数结构体

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


class DeleteCmqSubscribeRequest(AbstractModel):
    """DeleteCmqSubscribe请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type SubscriptionName: str
        """
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def TopicName(self):
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        """订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
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
        


class DeleteCmqSubscribeResponse(AbstractModel):
    """DeleteCmqSubscribe返回参数结构体

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


class DeleteCmqTopicRequest(AbstractModel):
    """DeleteCmqTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        """
        self._TopicName = None

    @property
    def TopicName(self):
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
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
        


class DeleteCmqTopicResponse(AbstractModel):
    """DeleteCmqTopic返回参数结构体

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


class DeleteEnvironmentRolesRequest(AbstractModel):
    """DeleteEnvironmentRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _RoleNames: 角色名称数组。
        :type RoleNames: list of str
        :param _ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._RoleNames = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleNames(self):
        """角色名称数组。
        :rtype: list of str
        """
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

    @property
    def ClusterId(self):
        """必填字段，集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleNames = params.get("RoleNames")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRolesResponse(AbstractModel):
    """DeleteEnvironmentRoles返回参数结构体

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


class DeleteEnvironmentsRequest(AbstractModel):
    """DeleteEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentIds: 环境（命名空间）数组，每次最多删除20个。
        :type EnvironmentIds: list of str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentIds = None
        self._ClusterId = None

    @property
    def EnvironmentIds(self):
        """环境（命名空间）数组，每次最多删除20个。
        :rtype: list of str
        """
        return self._EnvironmentIds

    @EnvironmentIds.setter
    def EnvironmentIds(self, EnvironmentIds):
        self._EnvironmentIds = EnvironmentIds

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentIds = params.get("EnvironmentIds")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentsResponse(AbstractModel):
    """DeleteEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentIds: 成功删除的环境（命名空间）数组。
        :type EnvironmentIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvironmentIds = None
        self._RequestId = None

    @property
    def EnvironmentIds(self):
        """成功删除的环境（命名空间）数组。
        :rtype: list of str
        """
        return self._EnvironmentIds

    @EnvironmentIds.setter
    def EnvironmentIds(self, EnvironmentIds):
        self._EnvironmentIds = EnvironmentIds

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
        self._EnvironmentIds = params.get("EnvironmentIds")
        self._RequestId = params.get("RequestId")


class DeleteProClusterRequest(AbstractModel):
    """DeleteProCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProClusterResponse(AbstractModel):
    """DeleteProCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DealName: 退还实例订单号
        :type DealName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DealName = None
        self._RequestId = None

    @property
    def DealName(self):
        """退还实例订单号
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQBindingRequest(AbstractModel):
    """DeleteRabbitMQBinding请求参数结构体

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
        


class DeleteRabbitMQBindingResponse(AbstractModel):
    """DeleteRabbitMQBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称
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
        """实例名称
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


class DeleteRabbitMQPermissionRequest(AbstractModel):
    """DeleteRabbitMQPermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，登录时使用
        :type User: str
        :param _VirtualHost: vhost名称
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
        """vhost名称
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
        


class DeleteRabbitMQPermissionResponse(AbstractModel):
    """DeleteRabbitMQPermission返回参数结构体

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


class DeleteRabbitMQUserRequest(AbstractModel):
    """DeleteRabbitMQUser请求参数结构体

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
        


class DeleteRabbitMQUserResponse(AbstractModel):
    """DeleteRabbitMQUser返回参数结构体

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


class DeleteRabbitMQVipInstanceRequest(AbstractModel):
    """DeleteRabbitMQVipInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _IsIntl: 是否国际站请求，默认 false
        :type IsIntl: bool
        """
        self._InstanceId = None
        self._IsIntl = None

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
    def IsIntl(self):
        """是否国际站请求，默认 false
        :rtype: bool
        """
        return self._IsIntl

    @IsIntl.setter
    def IsIntl(self, IsIntl):
        self._IsIntl = IsIntl


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IsIntl = params.get("IsIntl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRabbitMQVipInstanceResponse(AbstractModel):
    """DeleteRabbitMQVipInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranId: 订单号Id
        :type TranId: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranId = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def TranId(self):
        """订单号Id
        :rtype: str
        """
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class DeleteRabbitMQVirtualHostRequest(AbstractModel):
    """DeleteRabbitMQVirtualHost请求参数结构体

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
        


class DeleteRabbitMQVirtualHostResponse(AbstractModel):
    """DeleteRabbitMQVirtualHost返回参数结构体

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


class DeleteRocketMQClusterRequest(AbstractModel):
    """DeleteRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 待删除的集群Id。
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """待删除的集群Id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQClusterResponse(AbstractModel):
    """DeleteRocketMQCluster返回参数结构体

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


class DeleteRocketMQEnvironmentRolesRequest(AbstractModel):
    """DeleteRocketMQEnvironmentRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _RoleNames: 角色名称数组。
        :type RoleNames: list of str
        :param _ClusterId: 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._RoleNames = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleNames(self):
        """角色名称数组。
        :rtype: list of str
        """
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

    @property
    def ClusterId(self):
        """集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleNames = params.get("RoleNames")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQEnvironmentRolesResponse(AbstractModel):
    """DeleteRocketMQEnvironmentRoles返回参数结构体

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


class DeleteRocketMQGroupRequest(AbstractModel):
    """DeleteRocketMQGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _GroupId: 消费组名称
        :type GroupId: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        """消费组名称
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQGroupResponse(AbstractModel):
    """DeleteRocketMQGroup返回参数结构体

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


class DeleteRocketMQNamespaceRequest(AbstractModel):
    """DeleteRocketMQNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        """
        self._ClusterId = None
        self._NamespaceId = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQNamespaceResponse(AbstractModel):
    """DeleteRocketMQNamespace返回参数结构体

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


class DeleteRocketMQRolesRequest(AbstractModel):
    """DeleteRocketMQRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleNames: 角色名称数组。
        :type RoleNames: list of str
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        """
        self._RoleNames = None
        self._ClusterId = None

    @property
    def RoleNames(self):
        """角色名称数组。
        :rtype: list of str
        """
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._RoleNames = params.get("RoleNames")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQRolesResponse(AbstractModel):
    """DeleteRocketMQRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleNames: 成功删除的角色名称数组。
        :type RoleNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleNames = None
        self._RequestId = None

    @property
    def RoleNames(self):
        """成功删除的角色名称数组。
        :rtype: list of str
        """
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

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
        self._RoleNames = params.get("RoleNames")
        self._RequestId = params.get("RequestId")


class DeleteRocketMQTopicRequest(AbstractModel):
    """DeleteRocketMQTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _Topic: 主题名称
        :type Topic: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Topic = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQTopicResponse(AbstractModel):
    """DeleteRocketMQTopic返回参数结构体

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


class DeleteRocketMQVipInstanceRequest(AbstractModel):
    """DeleteRocketMQVipInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 实例的集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """实例的集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQVipInstanceResponse(AbstractModel):
    """DeleteRocketMQVipInstance返回参数结构体

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


class DeleteRolesRequest(AbstractModel):
    """DeleteRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleNames: 角色名称数组。
        :type RoleNames: list of str
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        """
        self._RoleNames = None
        self._ClusterId = None

    @property
    def RoleNames(self):
        """角色名称数组。
        :rtype: list of str
        """
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._RoleNames = params.get("RoleNames")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolesResponse(AbstractModel):
    """DeleteRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleNames: 成功删除的角色名称数组。
        :type RoleNames: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleNames = None
        self._RequestId = None

    @property
    def RoleNames(self):
        """成功删除的角色名称数组。
        :rtype: list of str
        """
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

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
        self._RoleNames = params.get("RoleNames")
        self._RequestId = params.get("RequestId")


class DeleteSubscriptionsRequest(AbstractModel):
    """DeleteSubscriptions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscriptionTopicSets: 订阅关系集合，每次最多删除20个。
        :type SubscriptionTopicSets: list of SubscriptionTopic
        :param _ClusterId: pulsar集群Id。
        :type ClusterId: str
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _Force: 是否强制删除，默认为false
        :type Force: bool
        """
        self._SubscriptionTopicSets = None
        self._ClusterId = None
        self._EnvironmentId = None
        self._Force = None

    @property
    def SubscriptionTopicSets(self):
        """订阅关系集合，每次最多删除20个。
        :rtype: list of SubscriptionTopic
        """
        return self._SubscriptionTopicSets

    @SubscriptionTopicSets.setter
    def SubscriptionTopicSets(self, SubscriptionTopicSets):
        self._SubscriptionTopicSets = SubscriptionTopicSets

    @property
    def ClusterId(self):
        """pulsar集群Id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Force(self):
        """是否强制删除，默认为false
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        if params.get("SubscriptionTopicSets") is not None:
            self._SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self._SubscriptionTopicSets.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubscriptionsResponse(AbstractModel):
    """DeleteSubscriptions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscriptionTopicSets: 成功删除的订阅关系数组。
        :type SubscriptionTopicSets: list of SubscriptionTopic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscriptionTopicSets = None
        self._RequestId = None

    @property
    def SubscriptionTopicSets(self):
        """成功删除的订阅关系数组。
        :rtype: list of SubscriptionTopic
        """
        return self._SubscriptionTopicSets

    @SubscriptionTopicSets.setter
    def SubscriptionTopicSets(self, SubscriptionTopicSets):
        self._SubscriptionTopicSets = SubscriptionTopicSets

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
        if params.get("SubscriptionTopicSets") is not None:
            self._SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self._SubscriptionTopicSets.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTopicsRequest(AbstractModel):
    """DeleteTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicSets: 主题集合，每次最多删除20个。
        :type TopicSets: list of TopicRecord
        :param _ClusterId: pulsar集群Id。
        :type ClusterId: str
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _Force: 是否强制删除，默认为false
        :type Force: bool
        """
        self._TopicSets = None
        self._ClusterId = None
        self._EnvironmentId = None
        self._Force = None

    @property
    def TopicSets(self):
        """主题集合，每次最多删除20个。
        :rtype: list of TopicRecord
        """
        return self._TopicSets

    @TopicSets.setter
    def TopicSets(self, TopicSets):
        self._TopicSets = TopicSets

    @property
    def ClusterId(self):
        """pulsar集群Id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Force(self):
        """是否强制删除，默认为false
        :rtype: bool
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self._TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self._TopicSets.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicsResponse(AbstractModel):
    """DeleteTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicSets: 被删除的主题数组。
        :type TopicSets: list of TopicRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicSets = None
        self._RequestId = None

    @property
    def TopicSets(self):
        """被删除的主题数组。
        :rtype: list of TopicRecord
        """
        return self._TopicSets

    @TopicSets.setter
    def TopicSets(self, TopicSets):
        self._TopicSets = TopicSets

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
        if params.get("TopicSets") is not None:
            self._TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self._TopicSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAMQPClustersRequest(AbstractModel):
    """DescribeAMQPClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _IdKeyword: 按照集群ID关键字搜索
        :type IdKeyword: str
        :param _NameKeyword: 按照集群名称关键字搜索
        :type NameKeyword: str
        :param _ClusterIdList: 集群ID列表过滤
        :type ClusterIdList: list of str
        :param _IsTagFilter: 标签过滤查找时，需要设置为true
        :type IsTagFilter: bool
        :param _Filters: 过滤器。目前支持按标签过滤。
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._IdKeyword = None
        self._NameKeyword = None
        self._ClusterIdList = None
        self._IsTagFilter = None
        self._Filters = None

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IdKeyword(self):
        """按照集群ID关键字搜索
        :rtype: str
        """
        return self._IdKeyword

    @IdKeyword.setter
    def IdKeyword(self, IdKeyword):
        self._IdKeyword = IdKeyword

    @property
    def NameKeyword(self):
        """按照集群名称关键字搜索
        :rtype: str
        """
        return self._NameKeyword

    @NameKeyword.setter
    def NameKeyword(self, NameKeyword):
        self._NameKeyword = NameKeyword

    @property
    def ClusterIdList(self):
        """集群ID列表过滤
        :rtype: list of str
        """
        return self._ClusterIdList

    @ClusterIdList.setter
    def ClusterIdList(self, ClusterIdList):
        self._ClusterIdList = ClusterIdList

    @property
    def IsTagFilter(self):
        """标签过滤查找时，需要设置为true
        :rtype: bool
        """
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        """过滤器。目前支持按标签过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IdKeyword = params.get("IdKeyword")
        self._NameKeyword = params.get("NameKeyword")
        self._ClusterIdList = params.get("ClusterIdList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeAMQPClustersResponse(AbstractModel):
    """DescribeAMQPClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterList: 集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of AMQPClusterDetail
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterList(self):
        """集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AMQPClusterDetail
        """
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def TotalCount(self):
        """总条数
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
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = AMQPClusterDetail()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAllTenantsRequest(AbstractModel):
    """DescribeAllTenants请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询限制条数
        :type Limit: int
        :param _ClusterName: 物理集群名称
        :type ClusterName: str
        :param _TenantId: 虚拟集群ID
        :type TenantId: str
        :param _TenantName: 虚拟集群名称
        :type TenantName: str
        :param _Types: 协议类型数组
        :type Types: list of str
        :param _SortBy: 排序字段名，支持createTime，updateTime
        :type SortBy: str
        :param _SortOrder: 升序排列ASC，降序排列DESC
        :type SortOrder: str
        """
        self._Offset = None
        self._Limit = None
        self._ClusterName = None
        self._TenantId = None
        self._TenantName = None
        self._Types = None
        self._SortBy = None
        self._SortOrder = None

    @property
    def Offset(self):
        """查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ClusterName(self):
        """物理集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TenantId(self):
        """虚拟集群ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def TenantName(self):
        """虚拟集群名称
        :rtype: str
        """
        return self._TenantName

    @TenantName.setter
    def TenantName(self, TenantName):
        self._TenantName = TenantName

    @property
    def Types(self):
        """协议类型数组
        :rtype: list of str
        """
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types

    @property
    def SortBy(self):
        """排序字段名，支持createTime，updateTime
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def SortOrder(self):
        """升序排列ASC，降序排列DESC
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterName = params.get("ClusterName")
        self._TenantId = params.get("TenantId")
        self._TenantName = params.get("TenantName")
        self._Types = params.get("Types")
        self._SortBy = params.get("SortBy")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllTenantsResponse(AbstractModel):
    """DescribeAllTenants返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Tenants: 虚拟集群列表
        :type Tenants: list of InternalTenant
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tenants = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tenants(self):
        """虚拟集群列表
        :rtype: list of InternalTenant
        """
        return self._Tenants

    @Tenants.setter
    def Tenants(self, Tenants):
        self._Tenants = Tenants

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
        if params.get("Tenants") is not None:
            self._Tenants = []
            for item in params.get("Tenants"):
                obj = InternalTenant()
                obj._deserialize(item)
                self._Tenants.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBindClustersRequest(AbstractModel):
    """DescribeBindClusters请求参数结构体

    """


class DescribeBindClustersResponse(AbstractModel):
    """DescribeBindClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 专享集群的数量
        :type TotalCount: int
        :param _ClusterSet: 专享集群的列表
        :type ClusterSet: list of BindCluster
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """专享集群的数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        """专享集群的列表
        :rtype: list of BindCluster
        """
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

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
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = BindCluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBindVpcsRequest(AbstractModel):
    """DescribeBindVpcs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._Offset = None
        self._Limit = None
        self._ClusterId = None

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindVpcsResponse(AbstractModel):
    """DescribeBindVpcs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数。
        :type TotalCount: int
        :param _VpcSets: Vpc集合。
        :type VpcSets: list of VpcBindRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSets(self):
        """Vpc集合。
        :rtype: list of VpcBindRecord
        """
        return self._VpcSets

    @VpcSets.setter
    def VpcSets(self, VpcSets):
        self._VpcSets = VpcSets

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
        if params.get("VpcSets") is not None:
            self._VpcSets = []
            for item in params.get("VpcSets"):
                obj = VpcBindRecord()
                obj._deserialize(item)
                self._VpcSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群的ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterSet: 集群的详细信息
        :type ClusterSet: :class:`tencentcloud.tdmq.v20200217.models.Cluster`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterSet = None
        self._RequestId = None

    @property
    def ClusterSet(self):
        """集群的详细信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.Cluster`
        """
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

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
        if params.get("ClusterSet") is not None:
            self._ClusterSet = Cluster()
            self._ClusterSet._deserialize(params.get("ClusterSet"))
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _ClusterIdList: 集群ID列表过滤
        :type ClusterIdList: list of str
        :param _IsTagFilter: 是否标签过滤
        :type IsTagFilter: bool
        :param _Filters: 过滤器。目前支持按标签过滤。
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._ClusterIdList = None
        self._IsTagFilter = None
        self._Filters = None

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ClusterIdList(self):
        """集群ID列表过滤
        :rtype: list of str
        """
        return self._ClusterIdList

    @ClusterIdList.setter
    def ClusterIdList(self, ClusterIdList):
        self._ClusterIdList = ClusterIdList

    @property
    def IsTagFilter(self):
        """是否标签过滤
        :rtype: bool
        """
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        """过滤器。目前支持按标签过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterIdList = params.get("ClusterIdList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群列表数量
        :type TotalCount: int
        :param _ClusterSet: 集群信息列表
        :type ClusterSet: list of Cluster
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """集群列表数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        """集群信息列表
        :rtype: list of Cluster
        """
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

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
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCmqQueueDetailRequest(AbstractModel):
    """DescribeCmqQueueDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 精确匹配QueueName
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        """精确匹配QueueName
        :rtype: str
        """
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
        


class DescribeCmqQueueDetailResponse(AbstractModel):
    """DescribeCmqQueueDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueDescribe: 队列详情列表。
        :type QueueDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqQueue`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueDescribe = None
        self._RequestId = None

    @property
    def QueueDescribe(self):
        """队列详情列表。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CmqQueue`
        """
        return self._QueueDescribe

    @QueueDescribe.setter
    def QueueDescribe(self, QueueDescribe):
        self._QueueDescribe = QueueDescribe

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
        if params.get("QueueDescribe") is not None:
            self._QueueDescribe = CmqQueue()
            self._QueueDescribe._deserialize(params.get("QueueDescribe"))
        self._RequestId = params.get("RequestId")


class DescribeCmqQueuesRequest(AbstractModel):
    """DescribeCmqQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param _Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _QueueName: 根据QueueName进行过滤
        :type QueueName: str
        :param _QueueNameList: CMQ 队列名称列表过滤
        :type QueueNameList: list of str
        :param _IsTagFilter: 标签过滤查找时，需要设置为 true
        :type IsTagFilter: bool
        :param _Filters: 过滤器。目前支持按标签过滤，标签的Name需要加前缀“tag:”，例如：tag:负责人、tag:环境、tag:业务
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._QueueName = None
        self._QueueNameList = None
        self._IsTagFilter = None
        self._Filters = None

    @property
    def Offset(self):
        """分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QueueName(self):
        """根据QueueName进行过滤
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def QueueNameList(self):
        """CMQ 队列名称列表过滤
        :rtype: list of str
        """
        return self._QueueNameList

    @QueueNameList.setter
    def QueueNameList(self, QueueNameList):
        self._QueueNameList = QueueNameList

    @property
    def IsTagFilter(self):
        """标签过滤查找时，需要设置为 true
        :rtype: bool
        """
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        """过滤器。目前支持按标签过滤，标签的Name需要加前缀“tag:”，例如：tag:负责人、tag:环境、tag:业务
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._QueueName = params.get("QueueName")
        self._QueueNameList = params.get("QueueNameList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeCmqQueuesResponse(AbstractModel):
    """DescribeCmqQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _QueueList: 队列列表
        :type QueueList: list of CmqQueue
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueList = None
        self._RequestId = None

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
    def QueueList(self):
        """队列列表
        :rtype: list of CmqQueue
        """
        return self._QueueList

    @QueueList.setter
    def QueueList(self, QueueList):
        self._QueueList = QueueList

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
        if params.get("QueueList") is not None:
            self._QueueList = []
            for item in params.get("QueueList"):
                obj = CmqQueue()
                obj._deserialize(item)
                self._QueueList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCmqSubscriptionDetailRequest(AbstractModel):
    """DescribeCmqSubscriptionDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _Offset: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param _Limit: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _SubscriptionName: 根据SubscriptionName进行模糊搜索
        :type SubscriptionName: str
        :param _QueueName: 队列名称，订阅绑定的endpoint
        :type QueueName: str
        :param _QueryType: 查询类型。取值：（1）topic；（2）queue。
默认值是topic。如果 queryType 是 topic，则查询主题下的订阅列表；如果 queryType 是 queue，则查询队列绑定的订阅列表。
        :type QueryType: str
        """
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._SubscriptionName = None
        self._QueueName = None
        self._QueryType = None

    @property
    def TopicName(self):
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        """分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SubscriptionName(self):
        """根据SubscriptionName进行模糊搜索
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def QueueName(self):
        """队列名称，订阅绑定的endpoint
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def QueryType(self):
        """查询类型。取值：（1）topic；（2）queue。
默认值是topic。如果 queryType 是 topic，则查询主题下的订阅列表；如果 queryType 是 queue，则查询队列绑定的订阅列表。
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SubscriptionName = params.get("SubscriptionName")
        self._QueueName = params.get("QueueName")
        self._QueryType = params.get("QueryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqSubscriptionDetailResponse(AbstractModel):
    """DescribeCmqSubscriptionDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _SubscriptionSet: Subscription属性集合
        :type SubscriptionSet: list of CmqSubscription
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SubscriptionSet = None
        self._RequestId = None

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
    def SubscriptionSet(self):
        """Subscription属性集合
        :rtype: list of CmqSubscription
        """
        return self._SubscriptionSet

    @SubscriptionSet.setter
    def SubscriptionSet(self, SubscriptionSet):
        self._SubscriptionSet = SubscriptionSet

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
        if params.get("SubscriptionSet") is not None:
            self._SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = CmqSubscription()
                obj._deserialize(item)
                self._SubscriptionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCmqTopicDetailRequest(AbstractModel):
    """DescribeCmqTopicDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 精确匹配TopicName。
        :type TopicName: str
        """
        self._TopicName = None

    @property
    def TopicName(self):
        """精确匹配TopicName。
        :rtype: str
        """
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
        


class DescribeCmqTopicDetailResponse(AbstractModel):
    """DescribeCmqTopicDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicDescribe: 主题详情
        :type TopicDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqTopic`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicDescribe = None
        self._RequestId = None

    @property
    def TopicDescribe(self):
        """主题详情
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CmqTopic`
        """
        return self._TopicDescribe

    @TopicDescribe.setter
    def TopicDescribe(self, TopicDescribe):
        self._TopicDescribe = TopicDescribe

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
        if params.get("TopicDescribe") is not None:
            self._TopicDescribe = CmqTopic()
            self._TopicDescribe._deserialize(params.get("TopicDescribe"))
        self._RequestId = params.get("RequestId")


class DescribeCmqTopicsRequest(AbstractModel):
    """DescribeCmqTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param _Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param _TopicName: 根据TopicName进行模糊搜索
        :type TopicName: str
        :param _TopicNameList: CMQ 主题名称列表过滤
        :type TopicNameList: list of str
        :param _IsTagFilter: 标签过滤查找时，需要设置为 true
        :type IsTagFilter: bool
        :param _Filters: 过滤器。目前支持按标签过滤，标签的Name需要加前缀“tag:”，例如：tag:负责人、tag:环境、tag:业务
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._TopicName = None
        self._TopicNameList = None
        self._IsTagFilter = None
        self._Filters = None

    @property
    def Offset(self):
        """分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TopicName(self):
        """根据TopicName进行模糊搜索
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicNameList(self):
        """CMQ 主题名称列表过滤
        :rtype: list of str
        """
        return self._TopicNameList

    @TopicNameList.setter
    def TopicNameList(self, TopicNameList):
        self._TopicNameList = TopicNameList

    @property
    def IsTagFilter(self):
        """标签过滤查找时，需要设置为 true
        :rtype: bool
        """
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        """过滤器。目前支持按标签过滤，标签的Name需要加前缀“tag:”，例如：tag:负责人、tag:环境、tag:业务
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TopicName = params.get("TopicName")
        self._TopicNameList = params.get("TopicNameList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeCmqTopicsResponse(AbstractModel):
    """DescribeCmqTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicList: 主题列表
        :type TopicList: list of CmqTopic
        :param _TotalCount: 全量主题数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TopicList(self):
        """主题列表
        :rtype: list of CmqTopic
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        """全量主题数量
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
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = CmqTopic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentAttributesRequest(AbstractModel):
    """DescribeEnvironmentAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentAttributesResponse(AbstractModel):
    """DescribeEnvironmentAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MsgTTL: 未消费消息过期时间，单位：秒，最大1296000（15天）。
        :type MsgTTL: int
        :param _RateInByte: 消费速率限制，单位：byte/秒，0：不限速。
        :type RateInByte: int
        :param _RateInSize: 消费速率限制，单位：个数/秒，0：不限速。
        :type RateInSize: int
        :param _RetentionHours: 已消费消息保存策略，单位：小时，0：消费完马上删除。
        :type RetentionHours: int
        :param _RetentionSize: 已消费消息保存策略，单位：G，0：消费完马上删除。
        :type RetentionSize: int
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _Replicas: 副本数。
        :type Replicas: int
        :param _Remark: 备注。
        :type Remark: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MsgTTL = None
        self._RateInByte = None
        self._RateInSize = None
        self._RetentionHours = None
        self._RetentionSize = None
        self._EnvironmentId = None
        self._Replicas = None
        self._Remark = None
        self._RequestId = None

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒，最大1296000（15天）。
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def RateInByte(self):
        """消费速率限制，单位：byte/秒，0：不限速。
        :rtype: int
        """
        return self._RateInByte

    @RateInByte.setter
    def RateInByte(self, RateInByte):
        self._RateInByte = RateInByte

    @property
    def RateInSize(self):
        """消费速率限制，单位：个数/秒，0：不限速。
        :rtype: int
        """
        return self._RateInSize

    @RateInSize.setter
    def RateInSize(self, RateInSize):
        self._RateInSize = RateInSize

    @property
    def RetentionHours(self):
        """已消费消息保存策略，单位：小时，0：消费完马上删除。
        :rtype: int
        """
        return self._RetentionHours

    @RetentionHours.setter
    def RetentionHours(self, RetentionHours):
        self._RetentionHours = RetentionHours

    @property
    def RetentionSize(self):
        """已消费消息保存策略，单位：G，0：消费完马上删除。
        :rtype: int
        """
        return self._RetentionSize

    @RetentionSize.setter
    def RetentionSize(self, RetentionSize):
        self._RetentionSize = RetentionSize

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Replicas(self):
        """副本数。
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Remark(self):
        """备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

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
        self._MsgTTL = params.get("MsgTTL")
        self._RateInByte = params.get("RateInByte")
        self._RateInSize = params.get("RateInSize")
        self._RetentionHours = params.get("RetentionHours")
        self._RetentionSize = params.get("RetentionSize")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Replicas = params.get("Replicas")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentRolesRequest(AbstractModel):
    """DescribeEnvironmentRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 必填字段，环境（命名空间）名称。
        :type EnvironmentId: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _ClusterId: 必填字段，Pulsar 集群的ID
        :type ClusterId: str
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _Filters: * RoleName
按照角色名进行过滤，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self._EnvironmentId = None
        self._Offset = None
        self._Limit = None
        self._ClusterId = None
        self._RoleName = None
        self._Filters = None

    @property
    def EnvironmentId(self):
        """必填字段，环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ClusterId(self):
        """必填字段，Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Filters(self):
        """* RoleName
按照角色名进行过滤，精确查询。
类型：String
必选：否
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
        self._RoleName = params.get("RoleName")
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
        


class DescribeEnvironmentRolesResponse(AbstractModel):
    """DescribeEnvironmentRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数。
        :type TotalCount: int
        :param _EnvironmentRoleSets: 命名空间角色集合。
        :type EnvironmentRoleSets: list of EnvironmentRole
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EnvironmentRoleSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentRoleSets(self):
        """命名空间角色集合。
        :rtype: list of EnvironmentRole
        """
        return self._EnvironmentRoleSets

    @EnvironmentRoleSets.setter
    def EnvironmentRoleSets(self, EnvironmentRoleSets):
        self._EnvironmentRoleSets = EnvironmentRoleSets

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
        if params.get("EnvironmentRoleSets") is not None:
            self._EnvironmentRoleSets = []
            for item in params.get("EnvironmentRoleSets"):
                obj = EnvironmentRole()
                obj._deserialize(item)
                self._EnvironmentRoleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _EnvironmentId: 命名空间名称，模糊搜索。
        :type EnvironmentId: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _Filters: * EnvironmentId
按照名称空间进行过滤，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self._ClusterId = None
        self._EnvironmentId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """命名空间名称，模糊搜索。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """* EnvironmentId
按照名称空间进行过滤，精确查询。
类型：String
必选：否
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
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
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 命名空间记录数。
        :type TotalCount: int
        :param _EnvironmentSet: 命名空间集合数组。
        :type EnvironmentSet: list of Environment
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EnvironmentSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """命名空间记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentSet(self):
        """命名空间集合数组。
        :rtype: list of Environment
        """
        return self._EnvironmentSet

    @EnvironmentSet.setter
    def EnvironmentSet(self, EnvironmentSet):
        self._EnvironmentSet = EnvironmentSet

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
        if params.get("EnvironmentSet") is not None:
            self._EnvironmentSet = []
            for item in params.get("EnvironmentSet"):
                obj = Environment()
                obj._deserialize(item)
                self._EnvironmentSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMqMsgTraceRequest(AbstractModel):
    """DescribeMqMsgTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Protocol: pulsar、rocketmq、rabbitmq、cmq
        :type Protocol: str
        :param _MsgId: 消息id
        :type MsgId: str
        :param _ClusterId: 集群id，cmq为空
        :type ClusterId: str
        :param _EnvironmentId: 命名空间，cmq为空
        :type EnvironmentId: str
        :param _TopicName: 主题，cmq为空，rocketmq查询死信时值为groupId
        :type TopicName: str
        :param _QueueName: cmq必填，其他协议填空
        :type QueueName: str
        :param _GroupName: 消费组、订阅
        :type GroupName: str
        :param _QueryDlqMsg: 查询死信时该值为true，只对Rocketmq有效
        :type QueryDlqMsg: bool
        """
        self._Protocol = None
        self._MsgId = None
        self._ClusterId = None
        self._EnvironmentId = None
        self._TopicName = None
        self._QueueName = None
        self._GroupName = None
        self._QueryDlqMsg = None

    @property
    def Protocol(self):
        """pulsar、rocketmq、rabbitmq、cmq
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ClusterId(self):
        """集群id，cmq为空
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """命名空间，cmq为空
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题，cmq为空，rocketmq查询死信时值为groupId
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def QueueName(self):
        """cmq必填，其他协议填空
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def GroupName(self):
        """消费组、订阅
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def QueryDlqMsg(self):
        """查询死信时该值为true，只对Rocketmq有效
        :rtype: bool
        """
        return self._QueryDlqMsg

    @QueryDlqMsg.setter
    def QueryDlqMsg(self, QueryDlqMsg):
        self._QueryDlqMsg = QueryDlqMsg


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._MsgId = params.get("MsgId")
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._QueueName = params.get("QueueName")
        self._GroupName = params.get("GroupName")
        self._QueryDlqMsg = params.get("QueryDlqMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMqMsgTraceResponse(AbstractModel):
    """DescribeMqMsgTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 消息内容
        :type Result: list of TraceResult
        :param _ShowTopicName: 消息轨迹页展示的topic名称
        :type ShowTopicName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._ShowTopicName = None
        self._RequestId = None

    @property
    def Result(self):
        """消息内容
        :rtype: list of TraceResult
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ShowTopicName(self):
        """消息轨迹页展示的topic名称
        :rtype: str
        """
        return self._ShowTopicName

    @ShowTopicName.setter
    def ShowTopicName(self, ShowTopicName):
        self._ShowTopicName = ShowTopicName

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = TraceResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._ShowTopicName = params.get("ShowTopicName")
        self._RequestId = params.get("RequestId")


class DescribeMsgRequest(AbstractModel):
    """DescribeMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _MsgId: 消息ID。
        :type MsgId: str
        :param _TopicName: 主题名。
        :type TopicName: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._MsgId = None
        self._TopicName = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgId(self):
        """消息ID。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def TopicName(self):
        """主题名。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgId = params.get("MsgId")
        self._TopicName = params.get("TopicName")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMsgResponse(AbstractModel):
    """DescribeMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Properties: 消息属性。
        :type Properties: str
        :param _Body: 消息体。
        :type Body: str
        :param _BatchId: 批次ID。
        :type BatchId: str
        :param _ProduceTime: 生产时间。
        :type ProduceTime: str
        :param _MsgId: 消息ID。
        :type MsgId: str
        :param _ProducerName: 生产者名称。
        :type ProducerName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Properties = None
        self._Body = None
        self._BatchId = None
        self._ProduceTime = None
        self._MsgId = None
        self._ProducerName = None
        self._RequestId = None

    @property
    def Properties(self):
        """消息属性。
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def Body(self):
        """消息体。
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def BatchId(self):
        """批次ID。
        :rtype: str
        """
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def ProduceTime(self):
        """生产时间。
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def MsgId(self):
        """消息ID。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ProducerName(self):
        """生产者名称。
        :rtype: str
        """
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

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
        self._Properties = params.get("Properties")
        self._Body = params.get("Body")
        self._BatchId = params.get("BatchId")
        self._ProduceTime = params.get("ProduceTime")
        self._MsgId = params.get("MsgId")
        self._ProducerName = params.get("ProducerName")
        self._RequestId = params.get("RequestId")


class DescribeMsgTraceRequest(AbstractModel):
    """DescribeMsgTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）。
        :type EnvironmentId: str
        :param _MsgId: 消息ID。
        :type MsgId: str
        :param _ProduceTime: 消息生产时间。
        :type ProduceTime: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _SubscriptionName: 消费组名称模糊匹配。
        :type SubscriptionName: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._MsgId = None
        self._ProduceTime = None
        self._Offset = None
        self._Limit = None
        self._SubscriptionName = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgId(self):
        """消息ID。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ProduceTime(self):
        """消息生产时间。
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SubscriptionName(self):
        """消费组名称模糊匹配。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgId = params.get("MsgId")
        self._ProduceTime = params.get("ProduceTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SubscriptionName = params.get("SubscriptionName")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMsgTraceResponse(AbstractModel):
    """DescribeMsgTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProducerLog: 生产信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerLog: :class:`tencentcloud.tdmq.v20200217.models.ProducerLog`
        :param _ServerLog: 服务方信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerLog: :class:`tencentcloud.tdmq.v20200217.models.ServerLog`
        :param _ConsumerLogs: 消费信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLogs: :class:`tencentcloud.tdmq.v20200217.models.ConsumerLogs`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProducerLog = None
        self._ServerLog = None
        self._ConsumerLogs = None
        self._RequestId = None

    @property
    def ProducerLog(self):
        """生产信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ProducerLog`
        """
        return self._ProducerLog

    @ProducerLog.setter
    def ProducerLog(self, ProducerLog):
        self._ProducerLog = ProducerLog

    @property
    def ServerLog(self):
        """服务方信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ServerLog`
        """
        return self._ServerLog

    @ServerLog.setter
    def ServerLog(self, ServerLog):
        self._ServerLog = ServerLog

    @property
    def ConsumerLogs(self):
        """消费信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ConsumerLogs`
        """
        return self._ConsumerLogs

    @ConsumerLogs.setter
    def ConsumerLogs(self, ConsumerLogs):
        self._ConsumerLogs = ConsumerLogs

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
        if params.get("ProducerLog") is not None:
            self._ProducerLog = ProducerLog()
            self._ProducerLog._deserialize(params.get("ProducerLog"))
        if params.get("ServerLog") is not None:
            self._ServerLog = ServerLog()
            self._ServerLog._deserialize(params.get("ServerLog"))
        if params.get("ConsumerLogs") is not None:
            self._ConsumerLogs = ConsumerLogs()
            self._ConsumerLogs._deserialize(params.get("ConsumerLogs"))
        self._RequestId = params.get("RequestId")


class DescribeNamespaceBundlesOptRequest(AbstractModel):
    """DescribeNamespaceBundlesOpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterName: 物理集群名
        :type ClusterName: str
        :param _TenantId: 虚拟集群（租户）ID
        :type TenantId: str
        :param _NamespaceName: 命名空间名
        :type NamespaceName: str
        :param _NeedMetrics: 是否需要监控指标，若传false，则不需要传Limit和Offset分页参数
        :type NeedMetrics: bool
        :param _Limit: 查询限制条数
        :type Limit: int
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Bundle: 过滤的 bundle
        :type Bundle: str
        :param _OwnerBroker: bundle 所属的 broker IP 地址，支持模糊查询
        :type OwnerBroker: str
        """
        self._ClusterName = None
        self._TenantId = None
        self._NamespaceName = None
        self._NeedMetrics = None
        self._Limit = None
        self._Offset = None
        self._Bundle = None
        self._OwnerBroker = None

    @property
    def ClusterName(self):
        """物理集群名
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TenantId(self):
        """虚拟集群（租户）ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def NamespaceName(self):
        """命名空间名
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def NeedMetrics(self):
        """是否需要监控指标，若传false，则不需要传Limit和Offset分页参数
        :rtype: bool
        """
        return self._NeedMetrics

    @NeedMetrics.setter
    def NeedMetrics(self, NeedMetrics):
        self._NeedMetrics = NeedMetrics

    @property
    def Limit(self):
        """查询限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Bundle(self):
        """过滤的 bundle
        :rtype: str
        """
        return self._Bundle

    @Bundle.setter
    def Bundle(self, Bundle):
        self._Bundle = Bundle

    @property
    def OwnerBroker(self):
        """bundle 所属的 broker IP 地址，支持模糊查询
        :rtype: str
        """
        return self._OwnerBroker

    @OwnerBroker.setter
    def OwnerBroker(self, OwnerBroker):
        self._OwnerBroker = OwnerBroker


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        self._TenantId = params.get("TenantId")
        self._NamespaceName = params.get("NamespaceName")
        self._NeedMetrics = params.get("NeedMetrics")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Bundle = params.get("Bundle")
        self._OwnerBroker = params.get("OwnerBroker")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespaceBundlesOptResponse(AbstractModel):
    """DescribeNamespaceBundlesOpt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """记录条数
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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNodeHealthOptRequest(AbstractModel):
    """DescribeNodeHealthOpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 节点实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """节点实例ID
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
        


class DescribeNodeHealthOptResponse(AbstractModel):
    """DescribeNodeHealthOpt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeState: 0-异常；1-正常
        :type NodeState: int
        :param _LatestHealthCheckTime: 最近一次健康检查的时间
        :type LatestHealthCheckTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeState = None
        self._LatestHealthCheckTime = None
        self._RequestId = None

    @property
    def NodeState(self):
        """0-异常；1-正常
        :rtype: int
        """
        return self._NodeState

    @NodeState.setter
    def NodeState(self, NodeState):
        self._NodeState = NodeState

    @property
    def LatestHealthCheckTime(self):
        """最近一次健康检查的时间
        :rtype: str
        """
        return self._LatestHealthCheckTime

    @LatestHealthCheckTime.setter
    def LatestHealthCheckTime(self, LatestHealthCheckTime):
        self._LatestHealthCheckTime = LatestHealthCheckTime

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
        self._NodeState = params.get("NodeState")
        self._LatestHealthCheckTime = params.get("LatestHealthCheckTime")
        self._RequestId = params.get("RequestId")


class DescribePublisherSummaryRequest(AbstractModel):
    """DescribePublisherSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _Topic: 主题名称
        :type Topic: str
        """
        self._ClusterId = None
        self._Namespace = None
        self._Topic = None

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
    def Namespace(self):
        """命名空间名称
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublisherSummaryResponse(AbstractModel):
    """DescribePublisherSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MsgRateIn: 生产速率（条/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: float
        :param _MsgThroughputIn: 生产速率（字节/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: float
        :param _PublisherCount: 生产者数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PublisherCount: int
        :param _StorageSize: 消息存储大小，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MsgRateIn = None
        self._MsgThroughputIn = None
        self._PublisherCount = None
        self._StorageSize = None
        self._RequestId = None

    @property
    def MsgRateIn(self):
        """生产速率（条/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgThroughputIn(self):
        """生产速率（字节/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def PublisherCount(self):
        """生产者数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PublisherCount

    @PublisherCount.setter
    def PublisherCount(self, PublisherCount):
        self._PublisherCount = PublisherCount

    @property
    def StorageSize(self):
        """消息存储大小，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

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
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._PublisherCount = params.get("PublisherCount")
        self._StorageSize = params.get("StorageSize")
        self._RequestId = params.get("RequestId")


class DescribePublishersRequest(AbstractModel):
    """DescribePublishers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Filters: 参数过滤器，支持ProducerName，Address字段
        :type Filters: list of Filter
        :param _Offset: 查询偏移量，默认为0
        :type Offset: int
        :param _Limit: 查询条数，默认为20
        :type Limit: int
        :param _Sort: 排序器
        :type Sort: :class:`tencentcloud.tdmq.v20200217.models.Sort`
        """
        self._ClusterId = None
        self._Namespace = None
        self._Topic = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Sort = None

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
    def Namespace(self):
        """命名空间名称
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Filters(self):
        """参数过滤器，支持ProducerName，Address字段
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """查询偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询条数，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Sort(self):
        """排序器
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._Topic = params.get("Topic")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublishersResponse(AbstractModel):
    """DescribePublishers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Publishers: 生产者信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Publishers: list of Publisher
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Publishers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Publishers(self):
        """生产者信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Publisher
        """
        return self._Publishers

    @Publishers.setter
    def Publishers(self, Publishers):
        self._Publishers = Publishers

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
        if params.get("Publishers") is not None:
            self._Publishers = []
            for item in params.get("Publishers"):
                obj = Publisher()
                obj._deserialize(item)
                self._Publishers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePulsarProInstanceDetailRequest(AbstractModel):
    """DescribePulsarProInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePulsarProInstanceDetailResponse(AbstractModel):
    """DescribePulsarProInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: 集群信息
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.PulsarProClusterInfo`
        :param _NetworkAccessPointInfos: 集群网络接入点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAccessPointInfos: list of PulsarNetworkAccessPointInfo
        :param _ClusterSpecInfo: 集群规格信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterSpecInfo: :class:`tencentcloud.tdmq.v20200217.models.PulsarProClusterSpecInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._NetworkAccessPointInfos = None
        self._ClusterSpecInfo = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        """集群信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.PulsarProClusterInfo`
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def NetworkAccessPointInfos(self):
        """集群网络接入点信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PulsarNetworkAccessPointInfo
        """
        return self._NetworkAccessPointInfos

    @NetworkAccessPointInfos.setter
    def NetworkAccessPointInfos(self, NetworkAccessPointInfos):
        self._NetworkAccessPointInfos = NetworkAccessPointInfos

    @property
    def ClusterSpecInfo(self):
        """集群规格信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.PulsarProClusterSpecInfo`
        """
        return self._ClusterSpecInfo

    @ClusterSpecInfo.setter
    def ClusterSpecInfo(self, ClusterSpecInfo):
        self._ClusterSpecInfo = ClusterSpecInfo

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
            self._ClusterInfo = PulsarProClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("NetworkAccessPointInfos") is not None:
            self._NetworkAccessPointInfos = []
            for item in params.get("NetworkAccessPointInfos"):
                obj = PulsarNetworkAccessPointInfo()
                obj._deserialize(item)
                self._NetworkAccessPointInfos.append(obj)
        if params.get("ClusterSpecInfo") is not None:
            self._ClusterSpecInfo = PulsarProClusterSpecInfo()
            self._ClusterSpecInfo._deserialize(params.get("ClusterSpecInfo"))
        self._RequestId = params.get("RequestId")


class DescribePulsarProInstancesRequest(AbstractModel):
    """DescribePulsarProInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件过滤器
        :type Filters: list of Filter
        :param _Limit: 查询数目上限，默认20
        :type Limit: int
        :param _Offset: 查询起始位置
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        """查询条件过滤器
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """查询数目上限，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询起始位置
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
        


class DescribePulsarProInstancesResponse(AbstractModel):
    """DescribePulsarProInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 未分页的总数目
        :type TotalCount: int
        :param _Instances: 实例信息列表
        :type Instances: list of PulsarProInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """未分页的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """实例信息列表
        :rtype: list of PulsarProInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = PulsarProInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQBindingsRequest(AbstractModel):
    """DescribeRabbitMQBindings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _VirtualHost: Vhost名称
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
        """Vhost名称
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
        


class DescribeRabbitMQBindingsResponse(AbstractModel):
    """DescribeRabbitMQBindings返回参数结构体

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


class DescribeRabbitMQExchangesRequest(AbstractModel):
    """DescribeRabbitMQExchanges请求参数结构体

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
        


class DescribeRabbitMQExchangesResponse(AbstractModel):
    """DescribeRabbitMQExchanges返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExchangeInfoList: 策略列表信息
        :type ExchangeInfoList: list of RabbitMQExchangeListInfo
        :param _TotalCount: 策略结果总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExchangeInfoList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ExchangeInfoList(self):
        """策略列表信息
        :rtype: list of RabbitMQExchangeListInfo
        """
        return self._ExchangeInfoList

    @ExchangeInfoList.setter
    def ExchangeInfoList(self, ExchangeInfoList):
        self._ExchangeInfoList = ExchangeInfoList

    @property
    def TotalCount(self):
        """策略结果总数
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


class DescribeRabbitMQNodeListRequest(AbstractModel):
    """DescribeRabbitMQNodeList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: rabbitmq集群ID
        :type InstanceId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 一页限制
        :type Limit: int
        :param _NodeName: 模糊搜索节点名字
        :type NodeName: str
        :param _Filters: 过滤参数的名字和数值
现在只有一个nodeStatus
running/down
数组类型，兼容后续添加过滤参数

        :type Filters: list of Filter
        :param _SortElement: 按指定元素排序，现在只有2个
cpuUsage/diskUsage
        :type SortElement: str
        :param _SortOrder: 升序/降序
ascend/descend
        :type SortOrder: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._NodeName = None
        self._Filters = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        """rabbitmq集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NodeName(self):
        """模糊搜索节点名字
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Filters(self):
        """过滤参数的名字和数值
现在只有一个nodeStatus
running/down
数组类型，兼容后续添加过滤参数

        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortElement(self):
        """按指定元素排序，现在只有2个
cpuUsage/diskUsage
        :rtype: str
        """
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        """升序/降序
ascend/descend
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NodeName = params.get("NodeName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQNodeListResponse(AbstractModel):
    """DescribeRabbitMQNodeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群列表数量
        :type TotalCount: int
        :param _NodeList: 集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of RabbitMQPrivateNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """集群列表数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeList(self):
        """集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RabbitMQPrivateNode
        """
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

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
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = RabbitMQPrivateNode()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQPermissionRequest(AbstractModel):
    """DescribeRabbitMQPermission请求参数结构体

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
        


class DescribeRabbitMQPermissionResponse(AbstractModel):
    """DescribeRabbitMQPermission返回参数结构体

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


class DescribeRabbitMQQueueDetailRequest(AbstractModel):
    """DescribeRabbitMQQueueDetail请求参数结构体

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
        


class DescribeRabbitMQQueueDetailResponse(AbstractModel):
    """DescribeRabbitMQQueueDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称
        :type InstanceId: str
        :param _VirtualHost: Vhost参数
        :type VirtualHost: str
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _QueueType: 队列类型,取值classic或quorum
        :type QueueType: str
        :param _Consumers: 在线消费者数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Consumers: int
        :param _Durable: 持久标记
        :type Durable: bool
        :param _AutoDelete: 自动清除
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoDelete: bool
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _MessageTTL: MessageTTL参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageTTL: int
        :param _AutoExpire: AutoExpire参数
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoExpire: int
        :param _MaxLength: MaxLength参数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxLength: int
        :param _MaxLengthBytes: MaxLengthBytes参数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxLengthBytes: int
        :param _DeliveryLimit: DeliveryLimit参数,quorum类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliveryLimit: int
        :param _OverflowBehaviour: OverflowBehaviour参数,取值为drop-head, reject-publish或reject-publish-dlx
注意：此字段可能返回 null，表示取不到有效值。
        :type OverflowBehaviour: str
        :param _DeadLetterExchange: DeadLetterExchange参数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterExchange: str
        :param _DeadLetterRoutingKey: DeadLetterRoutingKey参数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterRoutingKey: str
        :param _SingleActiveConsumer: SingleActiveConsumer参数
注意：此字段可能返回 null，表示取不到有效值。
        :type SingleActiveConsumer: bool
        :param _MaximumPriority: MaximumPriority参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :type MaximumPriority: int
        :param _LazyMode: LazyMode参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :type LazyMode: bool
        :param _MasterLocator: MasterLocator参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterLocator: str
        :param _MaxInMemoryLength: MaxInMemoryLength参数,quorum类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxInMemoryLength: int
        :param _MaxInMemoryBytes: MaxInMemoryBytes参数,quorum类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxInMemoryBytes: int
        :param _CreateTime: 创建时间戳,单位秒
        :type CreateTime: int
        :param _Node: 节点
注意：此字段可能返回 null，表示取不到有效值。
        :type Node: str
        :param _DeadLetterStrategy: 仲裁队列死信一致性策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterStrategy: str
        :param _QueueLeaderLocator: 仲裁队列的领导者选举策略
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueLeaderLocator: str
        :param _QuorumInitialGroupSize: 仲裁队列的初始副本组大小
注意：此字段可能返回 null，表示取不到有效值。
        :type QuorumInitialGroupSize: int
        :param _Exclusive: 是否为独占队列
        :type Exclusive: bool
        :param _Policy: 生效的策略名
注意：此字段可能返回 null，表示取不到有效值。
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
        """实例名称
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoDelete

    @AutoDelete.setter
    def AutoDelete(self, AutoDelete):
        self._AutoDelete = AutoDelete

    @property
    def Remark(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageTTL(self):
        """MessageTTL参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MessageTTL

    @MessageTTL.setter
    def MessageTTL(self, MessageTTL):
        self._MessageTTL = MessageTTL

    @property
    def AutoExpire(self):
        """AutoExpire参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AutoExpire

    @AutoExpire.setter
    def AutoExpire(self, AutoExpire):
        self._AutoExpire = AutoExpire

    @property
    def MaxLength(self):
        """MaxLength参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxLength

    @MaxLength.setter
    def MaxLength(self, MaxLength):
        self._MaxLength = MaxLength

    @property
    def MaxLengthBytes(self):
        """MaxLengthBytes参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxLengthBytes

    @MaxLengthBytes.setter
    def MaxLengthBytes(self, MaxLengthBytes):
        self._MaxLengthBytes = MaxLengthBytes

    @property
    def DeliveryLimit(self):
        """DeliveryLimit参数,quorum类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeliveryLimit

    @DeliveryLimit.setter
    def DeliveryLimit(self, DeliveryLimit):
        self._DeliveryLimit = DeliveryLimit

    @property
    def OverflowBehaviour(self):
        """OverflowBehaviour参数,取值为drop-head, reject-publish或reject-publish-dlx
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OverflowBehaviour

    @OverflowBehaviour.setter
    def OverflowBehaviour(self, OverflowBehaviour):
        self._OverflowBehaviour = OverflowBehaviour

    @property
    def DeadLetterExchange(self):
        """DeadLetterExchange参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeadLetterExchange

    @DeadLetterExchange.setter
    def DeadLetterExchange(self, DeadLetterExchange):
        self._DeadLetterExchange = DeadLetterExchange

    @property
    def DeadLetterRoutingKey(self):
        """DeadLetterRoutingKey参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeadLetterRoutingKey

    @DeadLetterRoutingKey.setter
    def DeadLetterRoutingKey(self, DeadLetterRoutingKey):
        self._DeadLetterRoutingKey = DeadLetterRoutingKey

    @property
    def SingleActiveConsumer(self):
        """SingleActiveConsumer参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SingleActiveConsumer

    @SingleActiveConsumer.setter
    def SingleActiveConsumer(self, SingleActiveConsumer):
        self._SingleActiveConsumer = SingleActiveConsumer

    @property
    def MaximumPriority(self):
        """MaximumPriority参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaximumPriority

    @MaximumPriority.setter
    def MaximumPriority(self, MaximumPriority):
        self._MaximumPriority = MaximumPriority

    @property
    def LazyMode(self):
        """LazyMode参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._LazyMode

    @LazyMode.setter
    def LazyMode(self, LazyMode):
        self._LazyMode = LazyMode

    @property
    def MasterLocator(self):
        """MasterLocator参数,classic类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MasterLocator

    @MasterLocator.setter
    def MasterLocator(self, MasterLocator):
        self._MasterLocator = MasterLocator

    @property
    def MaxInMemoryLength(self):
        """MaxInMemoryLength参数,quorum类型专用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxInMemoryLength

    @MaxInMemoryLength.setter
    def MaxInMemoryLength(self, MaxInMemoryLength):
        self._MaxInMemoryLength = MaxInMemoryLength

    @property
    def MaxInMemoryBytes(self):
        """MaxInMemoryBytes参数,quorum类型专用
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Node

    @Node.setter
    def Node(self, Node):
        self._Node = Node

    @property
    def DeadLetterStrategy(self):
        """仲裁队列死信一致性策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeadLetterStrategy

    @DeadLetterStrategy.setter
    def DeadLetterStrategy(self, DeadLetterStrategy):
        self._DeadLetterStrategy = DeadLetterStrategy

    @property
    def QueueLeaderLocator(self):
        """仲裁队列的领导者选举策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QueueLeaderLocator

    @QueueLeaderLocator.setter
    def QueueLeaderLocator(self, QueueLeaderLocator):
        self._QueueLeaderLocator = QueueLeaderLocator

    @property
    def QuorumInitialGroupSize(self):
        """仲裁队列的初始副本组大小
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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


class DescribeRabbitMQQueuesRequest(AbstractModel):
    """DescribeRabbitMQQueues请求参数结构体

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
        


class DescribeRabbitMQQueuesResponse(AbstractModel):
    """DescribeRabbitMQQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueInfoList: 列表信息
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
        """列表信息
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


class DescribeRabbitMQUserRequest(AbstractModel):
    """DescribeRabbitMQUser请求参数结构体

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
        


class DescribeRabbitMQUserResponse(AbstractModel):
    """DescribeRabbitMQUser返回参数结构体

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


class DescribeRabbitMQVipInstanceRequest(AbstractModel):
    """DescribeRabbitMQVipInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQVipInstanceResponse(AbstractModel):
    """DescribeRabbitMQVipInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: 集群信息
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterInfo`
        :param _ClusterSpecInfo: 集群规格信息
        :type ClusterSpecInfo: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterSpecInfo`
        :param _ClusterNetInfo: 集群访问
        :type ClusterNetInfo: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterAccessInfo`
        :param _ClusterWhiteListInfo: 集群白名单
        :type ClusterWhiteListInfo: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterWhiteListInfo`
        :param _VirtualHostQuota: vhost配额信息
        :type VirtualHostQuota: :class:`tencentcloud.tdmq.v20200217.models.VirtualHostQuota`
        :param _ExchangeQuota: exchange配额信息
        :type ExchangeQuota: :class:`tencentcloud.tdmq.v20200217.models.ExchangeQuota`
        :param _QueueQuota: queue配额信息
        :type QueueQuota: :class:`tencentcloud.tdmq.v20200217.models.QueueQuota`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._ClusterSpecInfo = None
        self._ClusterNetInfo = None
        self._ClusterWhiteListInfo = None
        self._VirtualHostQuota = None
        self._ExchangeQuota = None
        self._QueueQuota = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        """集群信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterInfo`
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def ClusterSpecInfo(self):
        """集群规格信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterSpecInfo`
        """
        return self._ClusterSpecInfo

    @ClusterSpecInfo.setter
    def ClusterSpecInfo(self, ClusterSpecInfo):
        self._ClusterSpecInfo = ClusterSpecInfo

    @property
    def ClusterNetInfo(self):
        """集群访问
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterAccessInfo`
        """
        return self._ClusterNetInfo

    @ClusterNetInfo.setter
    def ClusterNetInfo(self, ClusterNetInfo):
        self._ClusterNetInfo = ClusterNetInfo

    @property
    def ClusterWhiteListInfo(self):
        """集群白名单
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQClusterWhiteListInfo`
        """
        return self._ClusterWhiteListInfo

    @ClusterWhiteListInfo.setter
    def ClusterWhiteListInfo(self, ClusterWhiteListInfo):
        self._ClusterWhiteListInfo = ClusterWhiteListInfo

    @property
    def VirtualHostQuota(self):
        """vhost配额信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.VirtualHostQuota`
        """
        return self._VirtualHostQuota

    @VirtualHostQuota.setter
    def VirtualHostQuota(self, VirtualHostQuota):
        self._VirtualHostQuota = VirtualHostQuota

    @property
    def ExchangeQuota(self):
        """exchange配额信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ExchangeQuota`
        """
        return self._ExchangeQuota

    @ExchangeQuota.setter
    def ExchangeQuota(self, ExchangeQuota):
        self._ExchangeQuota = ExchangeQuota

    @property
    def QueueQuota(self):
        """queue配额信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.QueueQuota`
        """
        return self._QueueQuota

    @QueueQuota.setter
    def QueueQuota(self, QueueQuota):
        self._QueueQuota = QueueQuota

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
        if params.get("ClusterNetInfo") is not None:
            self._ClusterNetInfo = RabbitMQClusterAccessInfo()
            self._ClusterNetInfo._deserialize(params.get("ClusterNetInfo"))
        if params.get("ClusterWhiteListInfo") is not None:
            self._ClusterWhiteListInfo = RabbitMQClusterWhiteListInfo()
            self._ClusterWhiteListInfo._deserialize(params.get("ClusterWhiteListInfo"))
        if params.get("VirtualHostQuota") is not None:
            self._VirtualHostQuota = VirtualHostQuota()
            self._VirtualHostQuota._deserialize(params.get("VirtualHostQuota"))
        if params.get("ExchangeQuota") is not None:
            self._ExchangeQuota = ExchangeQuota()
            self._ExchangeQuota._deserialize(params.get("ExchangeQuota"))
        if params.get("QueueQuota") is not None:
            self._QueueQuota = QueueQuota()
            self._QueueQuota._deserialize(params.get("QueueQuota"))
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQVipInstancesRequest(AbstractModel):
    """DescribeRabbitMQVipInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件过滤器
        :type Filters: list of Filter
        :param _Limit: 查询数目上限，默认20
        :type Limit: int
        :param _Offset: 查询起始位置
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        """查询条件过滤器
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """查询数目上限，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询起始位置
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
        


class DescribeRabbitMQVipInstancesResponse(AbstractModel):
    """DescribeRabbitMQVipInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 未分页的总数目
        :type TotalCount: int
        :param _Instances: 实例信息列表
        :type Instances: list of RabbitMQVipInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """未分页的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """实例信息列表
        :rtype: list of RabbitMQVipInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RabbitMQVipInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQVirtualHostRequest(AbstractModel):
    """DescribeRabbitMQVirtualHost请求参数结构体

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
        :type Filters: :class:`tencentcloud.tdmq.v20200217.models.Filter`
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
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.Filter`
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
        


class DescribeRabbitMQVirtualHostResponse(AbstractModel):
    """DescribeRabbitMQVirtualHost返回参数结构体

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


class DescribeRocketMQClusterRequest(AbstractModel):
    """DescribeRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQClusterResponse(AbstractModel):
    """DescribeRocketMQCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: 集群信息
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param _ClusterConfig: 集群配置
        :type ClusterConfig: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        :param _ClusterStats: 集群最近使用量，即将废弃，请使用腾讯云可观测平台获取相关数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStats: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterRecentStats`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._ClusterConfig = None
        self._ClusterStats = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        """集群信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def ClusterConfig(self):
        """集群配置
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        """
        return self._ClusterConfig

    @ClusterConfig.setter
    def ClusterConfig(self, ClusterConfig):
        self._ClusterConfig = ClusterConfig

    @property
    def ClusterStats(self):
        """集群最近使用量，即将废弃，请使用腾讯云可观测平台获取相关数据。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterRecentStats`
        """
        return self._ClusterStats

    @ClusterStats.setter
    def ClusterStats(self, ClusterStats):
        self._ClusterStats = ClusterStats

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
            self._ClusterInfo = RocketMQClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("ClusterConfig") is not None:
            self._ClusterConfig = RocketMQClusterConfig()
            self._ClusterConfig._deserialize(params.get("ClusterConfig"))
        if params.get("ClusterStats") is not None:
            self._ClusterStats = RocketMQClusterRecentStats()
            self._ClusterStats._deserialize(params.get("ClusterStats"))
        self._RequestId = params.get("RequestId")


class DescribeRocketMQClustersRequest(AbstractModel):
    """DescribeRocketMQClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _IdKeyword: 按照集群ID关键字搜索
        :type IdKeyword: str
        :param _NameKeyword: 按照集群名称关键字搜索
        :type NameKeyword: str
        :param _ClusterIdList: 集群ID列表过滤
        :type ClusterIdList: list of str
        :param _IsTagFilter: 标签过滤查找时，需要设置为true
        :type IsTagFilter: bool
        :param _Filters: 过滤器。目前支持标签过滤。
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._IdKeyword = None
        self._NameKeyword = None
        self._ClusterIdList = None
        self._IsTagFilter = None
        self._Filters = None

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IdKeyword(self):
        """按照集群ID关键字搜索
        :rtype: str
        """
        return self._IdKeyword

    @IdKeyword.setter
    def IdKeyword(self, IdKeyword):
        self._IdKeyword = IdKeyword

    @property
    def NameKeyword(self):
        """按照集群名称关键字搜索
        :rtype: str
        """
        return self._NameKeyword

    @NameKeyword.setter
    def NameKeyword(self, NameKeyword):
        self._NameKeyword = NameKeyword

    @property
    def ClusterIdList(self):
        """集群ID列表过滤
        :rtype: list of str
        """
        return self._ClusterIdList

    @ClusterIdList.setter
    def ClusterIdList(self, ClusterIdList):
        self._ClusterIdList = ClusterIdList

    @property
    def IsTagFilter(self):
        """标签过滤查找时，需要设置为true
        :rtype: bool
        """
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        """过滤器。目前支持标签过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IdKeyword = params.get("IdKeyword")
        self._NameKeyword = params.get("NameKeyword")
        self._ClusterIdList = params.get("ClusterIdList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeRocketMQClustersResponse(AbstractModel):
    """DescribeRocketMQClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterList: 集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of RocketMQClusterDetail
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterList(self):
        """集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQClusterDetail
        """
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def TotalCount(self):
        """总条数
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
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = RocketMQClusterDetail()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQConsumeStatsRequest(AbstractModel):
    """DescribeRocketMQConsumeStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 实例ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间
        :type NamespaceId: str
        :param _ConsumerGroup: 消费组
        :type ConsumerGroup: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._ConsumerGroup = None

    @property
    def ClusterId(self):
        """实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        """命名空间
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ConsumerGroup(self):
        """消费组
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQConsumeStatsResponse(AbstractModel):
    """DescribeRocketMQConsumeStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsumerStatsList: 消费详情列表
        :type ConsumerStatsList: list of ConsumerStats
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConsumerStatsList = None
        self._RequestId = None

    @property
    def ConsumerStatsList(self):
        """消费详情列表
        :rtype: list of ConsumerStats
        """
        return self._ConsumerStatsList

    @ConsumerStatsList.setter
    def ConsumerStatsList(self, ConsumerStatsList):
        self._ConsumerStatsList = ConsumerStatsList

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
        if params.get("ConsumerStatsList") is not None:
            self._ConsumerStatsList = []
            for item in params.get("ConsumerStatsList"):
                obj = ConsumerStats()
                obj._deserialize(item)
                self._ConsumerStatsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQConsumerConnectionDetailRequest(AbstractModel):
    """DescribeRocketMQConsumerConnectionDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _GroupId: 消费组名称
        :type GroupId: str
        :param _ClientId: 消费端实例ID
        :type ClientId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _FilterType: 按主题类型过滤查询结果，可选择Normal, GlobalOrder, PartitionedOrder, Retry, Transaction, DeadLetter
        :type FilterType: list of str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._ClientId = None
        self._Offset = None
        self._Limit = None
        self._FilterType = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        """消费组名称
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ClientId(self):
        """消费端实例ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterType(self):
        """按主题类型过滤查询结果，可选择Normal, GlobalOrder, PartitionedOrder, Retry, Transaction, DeadLetter
        :rtype: list of str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._ClientId = params.get("ClientId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQConsumerConnectionDetailResponse(AbstractModel):
    """DescribeRocketMQConsumerConnectionDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Details: 消费端主题信息列表
        :type Details: list of RocketMQConsumerTopic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Details(self):
        """消费端主题信息列表
        :rtype: list of RocketMQConsumerTopic
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = RocketMQConsumerTopic()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQConsumerConnectionsRequest(AbstractModel):
    """DescribeRocketMQConsumerConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _GroupId: 消费组ID
        :type GroupId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _SortedBy: 对查询结果排序，此为排序字段，目前支持Accumulative（消息堆积量）
        :type SortedBy: str
        :param _SortOrder: 查询结果排序规则，ASC为升序，DESC为降序
        :type SortOrder: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._Offset = None
        self._Limit = None
        self._SortedBy = None
        self._SortOrder = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        """消费组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortedBy(self):
        """对查询结果排序，此为排序字段，目前支持Accumulative（消息堆积量）
        :rtype: str
        """
        return self._SortedBy

    @SortedBy.setter
    def SortedBy(self, SortedBy):
        self._SortedBy = SortedBy

    @property
    def SortOrder(self):
        """查询结果排序规则，ASC为升序，DESC为降序
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortedBy = params.get("SortedBy")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQConsumerConnectionsResponse(AbstractModel):
    """DescribeRocketMQConsumerConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _Connections: 在线消费者信息
        :type Connections: list of RocketMQConsumerConnection
        :param _GroupDetail: 订阅组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupDetail: :class:`tencentcloud.tdmq.v20200217.models.RocketMQGroup`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Connections = None
        self._GroupDetail = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Connections(self):
        """在线消费者信息
        :rtype: list of RocketMQConsumerConnection
        """
        return self._Connections

    @Connections.setter
    def Connections(self, Connections):
        self._Connections = Connections

    @property
    def GroupDetail(self):
        """订阅组信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQGroup`
        """
        return self._GroupDetail

    @GroupDetail.setter
    def GroupDetail(self, GroupDetail):
        self._GroupDetail = GroupDetail

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
                obj = RocketMQConsumerConnection()
                obj._deserialize(item)
                self._Connections.append(obj)
        if params.get("GroupDetail") is not None:
            self._GroupDetail = RocketMQGroup()
            self._GroupDetail._deserialize(params.get("GroupDetail"))
        self._RequestId = params.get("RequestId")


class DescribeRocketMQEnvironmentRolesRequest(AbstractModel):
    """DescribeRocketMQEnvironmentRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 必填字段，RocketMQ集群的ID
        :type ClusterId: str
        :param _EnvironmentId: 命名空间
        :type EnvironmentId: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _Filters: RoleName按照角色名进行过滤，精确查询。类型：String必选：否
        :type Filters: list of Filter
        """
        self._ClusterId = None
        self._EnvironmentId = None
        self._Offset = None
        self._Limit = None
        self._RoleName = None
        self._Filters = None

    @property
    def ClusterId(self):
        """必填字段，RocketMQ集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """命名空间
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Filters(self):
        """RoleName按照角色名进行过滤，精确查询。类型：String必选：否
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._RoleName = params.get("RoleName")
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
        


class DescribeRocketMQEnvironmentRolesResponse(AbstractModel):
    """DescribeRocketMQEnvironmentRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数。
        :type TotalCount: int
        :param _EnvironmentRoleSets: 命名空间角色集合。
        :type EnvironmentRoleSets: list of EnvironmentRole
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EnvironmentRoleSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentRoleSets(self):
        """命名空间角色集合。
        :rtype: list of EnvironmentRole
        """
        return self._EnvironmentRoleSets

    @EnvironmentRoleSets.setter
    def EnvironmentRoleSets(self, EnvironmentRoleSets):
        self._EnvironmentRoleSets = EnvironmentRoleSets

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
        if params.get("EnvironmentRoleSets") is not None:
            self._EnvironmentRoleSets = []
            for item in params.get("EnvironmentRoleSets"):
                obj = EnvironmentRole()
                obj._deserialize(item)
                self._EnvironmentRoleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQGroupsRequest(AbstractModel):
    """DescribeRocketMQGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间
        :type NamespaceId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制条数
        :type Limit: int
        :param _FilterTopic: 主题名称，输入此参数可查询该主题下所有的订阅组
        :type FilterTopic: str
        :param _FilterGroup: 按消费组名称查询消费组，支持模糊查询
        :type FilterGroup: str
        :param _SortedBy: 按照指定字段排序，可选值为tps，accumulative
        :type SortedBy: str
        :param _SortOrder: 按升序或降序排列，可选值为asc，desc
        :type SortOrder: str
        :param _FilterOneGroup: 订阅组名称，指定此参数后将只返回该订阅组信息
        :type FilterOneGroup: str
        :param _Types: group类型
        :type Types: list of str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Offset = None
        self._Limit = None
        self._FilterTopic = None
        self._FilterGroup = None
        self._SortedBy = None
        self._SortOrder = None
        self._FilterOneGroup = None
        self._Types = None

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
    def NamespaceId(self):
        """命名空间
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterTopic(self):
        """主题名称，输入此参数可查询该主题下所有的订阅组
        :rtype: str
        """
        return self._FilterTopic

    @FilterTopic.setter
    def FilterTopic(self, FilterTopic):
        self._FilterTopic = FilterTopic

    @property
    def FilterGroup(self):
        """按消费组名称查询消费组，支持模糊查询
        :rtype: str
        """
        return self._FilterGroup

    @FilterGroup.setter
    def FilterGroup(self, FilterGroup):
        self._FilterGroup = FilterGroup

    @property
    def SortedBy(self):
        """按照指定字段排序，可选值为tps，accumulative
        :rtype: str
        """
        return self._SortedBy

    @SortedBy.setter
    def SortedBy(self, SortedBy):
        self._SortedBy = SortedBy

    @property
    def SortOrder(self):
        """按升序或降序排列，可选值为asc，desc
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def FilterOneGroup(self):
        """订阅组名称，指定此参数后将只返回该订阅组信息
        :rtype: str
        """
        return self._FilterOneGroup

    @FilterOneGroup.setter
    def FilterOneGroup(self, FilterOneGroup):
        self._FilterOneGroup = FilterOneGroup

    @property
    def Types(self):
        """group类型
        :rtype: list of str
        """
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterTopic = params.get("FilterTopic")
        self._FilterGroup = params.get("FilterGroup")
        self._SortedBy = params.get("SortedBy")
        self._SortOrder = params.get("SortOrder")
        self._FilterOneGroup = params.get("FilterOneGroup")
        self._Types = params.get("Types")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQGroupsResponse(AbstractModel):
    """DescribeRocketMQGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Groups: 订阅组列表
        :type Groups: list of RocketMQGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        """订阅组列表
        :rtype: list of RocketMQGroup
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = RocketMQGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQMigratingTopicListRequest(AbstractModel):
    """DescribeRocketMQMigratingTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 迁移任务名称
        :type TaskId: str
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Filters: 查询过滤器，支持topicname、MigrationStatus查询
        :type Filters: list of Filter
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def TaskId(self):
        """迁移任务名称
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """查询过滤器，支持topicname、MigrationStatus查询
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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
        


class DescribeRocketMQMigratingTopicListResponse(AbstractModel):
    """DescribeRocketMQMigratingTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _MigrateTopics: 迁移topic列表
        :type MigrateTopics: list of MigrateTopic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MigrateTopics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrateTopics(self):
        """迁移topic列表
        :rtype: list of MigrateTopic
        """
        return self._MigrateTopics

    @MigrateTopics.setter
    def MigrateTopics(self, MigrateTopics):
        self._MigrateTopics = MigrateTopics

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
        if params.get("MigrateTopics") is not None:
            self._MigrateTopics = []
            for item in params.get("MigrateTopics"):
                obj = MigrateTopic()
                obj._deserialize(item)
                self._MigrateTopics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQMsgRequest(AbstractModel):
    """DescribeRocketMQMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _EnvironmentId: 命名空间
        :type EnvironmentId: str
        :param _TopicName: 主题，查询死信时传groupId
        :type TopicName: str
        :param _MsgId: 消息id
        :type MsgId: str
        :param _PulsarMsgId: pulsar消息id
        :type PulsarMsgId: str
        :param _QueryDlqMsg: 查询死信时该值为true，只对Rocketmq有效
        :type QueryDlqMsg: bool
        :param _QueryDeadLetterMessage: 查询死信时该值为true，只对Rocketmq有效
        :type QueryDeadLetterMessage: bool
        :param _Offset: 分页Offset
        :type Offset: int
        :param _Limit: 分页Limit
        :type Limit: int
        :param _FilterTrackGroup: 根据消费组名称过滤消费详情
        :type FilterTrackGroup: str
        """
        self._ClusterId = None
        self._EnvironmentId = None
        self._TopicName = None
        self._MsgId = None
        self._PulsarMsgId = None
        self._QueryDlqMsg = None
        self._QueryDeadLetterMessage = None
        self._Offset = None
        self._Limit = None
        self._FilterTrackGroup = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """命名空间
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题，查询死信时传groupId
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def PulsarMsgId(self):
        """pulsar消息id
        :rtype: str
        """
        return self._PulsarMsgId

    @PulsarMsgId.setter
    def PulsarMsgId(self, PulsarMsgId):
        self._PulsarMsgId = PulsarMsgId

    @property
    def QueryDlqMsg(self):
        warnings.warn("parameter `QueryDlqMsg` is deprecated", DeprecationWarning) 

        """查询死信时该值为true，只对Rocketmq有效
        :rtype: bool
        """
        return self._QueryDlqMsg

    @QueryDlqMsg.setter
    def QueryDlqMsg(self, QueryDlqMsg):
        warnings.warn("parameter `QueryDlqMsg` is deprecated", DeprecationWarning) 

        self._QueryDlqMsg = QueryDlqMsg

    @property
    def QueryDeadLetterMessage(self):
        """查询死信时该值为true，只对Rocketmq有效
        :rtype: bool
        """
        return self._QueryDeadLetterMessage

    @QueryDeadLetterMessage.setter
    def QueryDeadLetterMessage(self, QueryDeadLetterMessage):
        self._QueryDeadLetterMessage = QueryDeadLetterMessage

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
    def FilterTrackGroup(self):
        """根据消费组名称过滤消费详情
        :rtype: str
        """
        return self._FilterTrackGroup

    @FilterTrackGroup.setter
    def FilterTrackGroup(self, FilterTrackGroup):
        self._FilterTrackGroup = FilterTrackGroup


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._MsgId = params.get("MsgId")
        self._PulsarMsgId = params.get("PulsarMsgId")
        self._QueryDlqMsg = params.get("QueryDlqMsg")
        self._QueryDeadLetterMessage = params.get("QueryDeadLetterMessage")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterTrackGroup = params.get("FilterTrackGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQMsgResponse(AbstractModel):
    """DescribeRocketMQMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Body: 消息体
        :type Body: str
        :param _Properties: 详情参数
        :type Properties: str
        :param _ProduceTime: 生产时间
        :type ProduceTime: str
        :param _MsgId: 消息id
        :type MsgId: str
        :param _ProducerAddr: 生产者地址
        :type ProducerAddr: str
        :param _MessageTracks: 消费组消费情况列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageTracks: list of RocketMQMessageTrack
        :param _ShowTopicName: 详情页展示的topic名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowTopicName: str
        :param _MessageTracksCount: 消费组消费情况列表总数
        :type MessageTracksCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Body = None
        self._Properties = None
        self._ProduceTime = None
        self._MsgId = None
        self._ProducerAddr = None
        self._MessageTracks = None
        self._ShowTopicName = None
        self._MessageTracksCount = None
        self._RequestId = None

    @property
    def Body(self):
        """消息体
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Properties(self):
        """详情参数
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ProduceTime(self):
        """生产时间
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ProducerAddr(self):
        """生产者地址
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def MessageTracks(self):
        """消费组消费情况列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQMessageTrack
        """
        return self._MessageTracks

    @MessageTracks.setter
    def MessageTracks(self, MessageTracks):
        self._MessageTracks = MessageTracks

    @property
    def ShowTopicName(self):
        """详情页展示的topic名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ShowTopicName

    @ShowTopicName.setter
    def ShowTopicName(self, ShowTopicName):
        self._ShowTopicName = ShowTopicName

    @property
    def MessageTracksCount(self):
        """消费组消费情况列表总数
        :rtype: int
        """
        return self._MessageTracksCount

    @MessageTracksCount.setter
    def MessageTracksCount(self, MessageTracksCount):
        self._MessageTracksCount = MessageTracksCount

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
        self._Body = params.get("Body")
        self._Properties = params.get("Properties")
        self._ProduceTime = params.get("ProduceTime")
        self._MsgId = params.get("MsgId")
        self._ProducerAddr = params.get("ProducerAddr")
        if params.get("MessageTracks") is not None:
            self._MessageTracks = []
            for item in params.get("MessageTracks"):
                obj = RocketMQMessageTrack()
                obj._deserialize(item)
                self._MessageTracks.append(obj)
        self._ShowTopicName = params.get("ShowTopicName")
        self._MessageTracksCount = params.get("MessageTracksCount")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQMsgTraceRequest(AbstractModel):
    """DescribeRocketMQMsgTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _EnvironmentId: 命名空间
        :type EnvironmentId: str
        :param _TopicName: 主题，rocketmq查询死信时值为groupId
        :type TopicName: str
        :param _MsgId: 消息id
        :type MsgId: str
        :param _GroupName: 消费组、订阅
        :type GroupName: str
        :param _QueryDLQMsg: 查询死信时该值为true
        :type QueryDLQMsg: bool
        :param _QueryDeadLetterMessage: 查询死信时该值为true
        :type QueryDeadLetterMessage: str
        """
        self._ClusterId = None
        self._EnvironmentId = None
        self._TopicName = None
        self._MsgId = None
        self._GroupName = None
        self._QueryDLQMsg = None
        self._QueryDeadLetterMessage = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """命名空间
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题，rocketmq查询死信时值为groupId
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def GroupName(self):
        """消费组、订阅
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def QueryDLQMsg(self):
        warnings.warn("parameter `QueryDLQMsg` is deprecated", DeprecationWarning) 

        """查询死信时该值为true
        :rtype: bool
        """
        return self._QueryDLQMsg

    @QueryDLQMsg.setter
    def QueryDLQMsg(self, QueryDLQMsg):
        warnings.warn("parameter `QueryDLQMsg` is deprecated", DeprecationWarning) 

        self._QueryDLQMsg = QueryDLQMsg

    @property
    def QueryDeadLetterMessage(self):
        """查询死信时该值为true
        :rtype: str
        """
        return self._QueryDeadLetterMessage

    @QueryDeadLetterMessage.setter
    def QueryDeadLetterMessage(self, QueryDeadLetterMessage):
        self._QueryDeadLetterMessage = QueryDeadLetterMessage


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._MsgId = params.get("MsgId")
        self._GroupName = params.get("GroupName")
        self._QueryDLQMsg = params.get("QueryDLQMsg")
        self._QueryDeadLetterMessage = params.get("QueryDeadLetterMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQMsgTraceResponse(AbstractModel):
    """DescribeRocketMQMsgTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 轨迹详情列表
        :type Result: list of TraceResult
        :param _ShowTopicName: 消息轨迹页展示的topic名称
        :type ShowTopicName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._ShowTopicName = None
        self._RequestId = None

    @property
    def Result(self):
        """轨迹详情列表
        :rtype: list of TraceResult
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ShowTopicName(self):
        """消息轨迹页展示的topic名称
        :rtype: str
        """
        return self._ShowTopicName

    @ShowTopicName.setter
    def ShowTopicName(self, ShowTopicName):
        self._ShowTopicName = ShowTopicName

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = TraceResult()
                obj._deserialize(item)
                self._Result.append(obj)
        self._ShowTopicName = params.get("ShowTopicName")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQNamespacesRequest(AbstractModel):
    """DescribeRocketMQNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _NameKeyword: 按名称搜索
        :type NameKeyword: str
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._NameKeyword = None

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
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def NameKeyword(self):
        """按名称搜索
        :rtype: str
        """
        return self._NameKeyword

    @NameKeyword.setter
    def NameKeyword(self, NameKeyword):
        self._NameKeyword = NameKeyword


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NameKeyword = params.get("NameKeyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQNamespacesResponse(AbstractModel):
    """DescribeRocketMQNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespaces: 命名空间列表
        :type Namespaces: list of RocketMQNamespace
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Namespaces = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Namespaces(self):
        """命名空间列表
        :rtype: list of RocketMQNamespace
        """
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def TotalCount(self):
        """总条数
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
        if params.get("Namespaces") is not None:
            self._Namespaces = []
            for item in params.get("Namespaces"):
                obj = RocketMQNamespace()
                obj._deserialize(item)
                self._Namespaces.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQPublicAccessMonitorDataRequest(AbstractModel):
    """DescribeRocketMQPublicAccessMonitorData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 专享集群ID
        :type InstanceId: str
        :param _MetricName: 指标名称，仅支持单指标拉取。目前仅支持：ClientIntraffic; ClientOuttraffic
        :type MetricName: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间，默认为当前时间
        :type EndTime: str
        :param _Period: 监控统计周期，如60。默认为取值为300，单位为s。
        :type Period: int
        """
        self._InstanceId = None
        self._MetricName = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def InstanceId(self):
        """专享集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MetricName(self):
        """指标名称，仅支持单指标拉取。目前仅支持：ClientIntraffic; ClientOuttraffic
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def StartTime(self):
        """起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，默认为当前时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """监控统计周期，如60。默认为取值为300，单位为s。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MetricName = params.get("MetricName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQPublicAccessMonitorDataResponse(AbstractModel):
    """DescribeRocketMQPublicAccessMonitorData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _Period: 监控统计周期，如60。默认为取值为300，单位为s。
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        :param _StartTime: 起始时间，如2018-09-22T19:51:23+08:00
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间，如2018-09-22T20:51:23+08:00，默认为当前时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _DataPoints: 数据点数组
注意：此字段可能返回 null，表示取不到有效值。
        :type DataPoints: list of RocketMQDataPoint
        :param _Msg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._DataPoints = None
        self._Msg = None
        self._RequestId = None

    @property
    def MetricName(self):
        """指标名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        """监控统计周期，如60。默认为取值为300，单位为s。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """起始时间，如2018-09-22T19:51:23+08:00
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如2018-09-22T20:51:23+08:00，默认为当前时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def DataPoints(self):
        """数据点数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQDataPoint
        """
        return self._DataPoints

    @DataPoints.setter
    def DataPoints(self, DataPoints):
        self._DataPoints = DataPoints

    @property
    def Msg(self):
        """返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("DataPoints") is not None:
            self._DataPoints = []
            for item in params.get("DataPoints"):
                obj = RocketMQDataPoint()
                obj._deserialize(item)
                self._DataPoints.append(obj)
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQPublicAccessPointRequest(AbstractModel):
    """DescribeRocketMQPublicAccessPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID，当前只支持专享集群
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群ID，当前只支持专享集群
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
        


class DescribeRocketMQPublicAccessPointResponse(AbstractModel):
    """DescribeRocketMQPublicAccessPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 公网接入点状态：
0， 已开启
1， 已关闭
2，开启中
3，关闭中
4，修改中
        :type Status: int
        :param _PayStatus: 支付状态：
0, 未知
1，正常
2，欠费
        :type PayStatus: int
        :param _AccessUrl: 接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessUrl: str
        :param _Rules: 安全访问规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of PublicAccessRule
        :param _Bandwidth: 带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type Bandwidth: int
        :param _PayMode: 付费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _BillingFlow: 公网是否按流量计费
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingFlow: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._PayStatus = None
        self._AccessUrl = None
        self._Rules = None
        self._Bandwidth = None
        self._PayMode = None
        self._BillingFlow = None
        self._RequestId = None

    @property
    def Status(self):
        """公网接入点状态：
0， 已开启
1， 已关闭
2，开启中
3，关闭中
4，修改中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PayStatus(self):
        """支付状态：
0, 未知
1，正常
2，欠费
        :rtype: int
        """
        return self._PayStatus

    @PayStatus.setter
    def PayStatus(self, PayStatus):
        self._PayStatus = PayStatus

    @property
    def AccessUrl(self):
        """接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessUrl

    @AccessUrl.setter
    def AccessUrl(self, AccessUrl):
        self._AccessUrl = AccessUrl

    @property
    def Rules(self):
        """安全访问规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Bandwidth(self):
        """带宽
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def PayMode(self):
        """付费模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def BillingFlow(self):
        """公网是否按流量计费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._BillingFlow

    @BillingFlow.setter
    def BillingFlow(self, BillingFlow):
        self._BillingFlow = BillingFlow

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
        self._Status = params.get("Status")
        self._PayStatus = params.get("PayStatus")
        self._AccessUrl = params.get("AccessUrl")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Bandwidth = params.get("Bandwidth")
        self._PayMode = params.get("PayMode")
        self._BillingFlow = params.get("BillingFlow")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQRolesRequest(AbstractModel):
    """DescribeRocketMQRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        :param _RoleName: 角色名称，模糊查询
        :type RoleName: str
        :param _Filters: RoleName按照角色名进行过滤，精确查询。类型：String必选：否
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._ClusterId = None
        self._RoleName = None
        self._Filters = None

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        """角色名称，模糊查询
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Filters(self):
        """RoleName按照角色名进行过滤，精确查询。类型：String必选：否
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
        self._RoleName = params.get("RoleName")
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
        


class DescribeRocketMQRolesResponse(AbstractModel):
    """DescribeRocketMQRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数。
        :type TotalCount: int
        :param _RoleSets: 角色数组。
        :type RoleSets: list of Role
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RoleSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RoleSets(self):
        """角色数组。
        :rtype: list of Role
        """
        return self._RoleSets

    @RoleSets.setter
    def RoleSets(self, RoleSets):
        self._RoleSets = RoleSets

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
        if params.get("RoleSets") is not None:
            self._RoleSets = []
            for item in params.get("RoleSets"):
                obj = Role()
                obj._deserialize(item)
                self._RoleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQSmoothMigrationTaskListRequest(AbstractModel):
    """DescribeRocketMQSmoothMigrationTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询起始偏移量
        :type Offset: int
        :param _Limit: 查询最大数量
        :type Limit: int
        :param _Filters: 查询过滤器，
支持的字段如下
TaskStatus, 支持多选
ConnectionType，支持多选
ClusterId，精确搜索
TaskName，支持模糊搜索
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """查询起始偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询最大数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """查询过滤器，
支持的字段如下
TaskStatus, 支持多选
ConnectionType，支持多选
ClusterId，精确搜索
TaskName，支持模糊搜索
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeRocketMQSmoothMigrationTaskListResponse(AbstractModel):
    """DescribeRocketMQSmoothMigrationTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 任务总数
        :type TotalCount: int
        :param _Data: 任务列表
        :type Data: list of RocketMQSmoothMigrationTaskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """任务总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """任务列表
        :rtype: list of RocketMQSmoothMigrationTaskItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RocketMQSmoothMigrationTaskItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQSmoothMigrationTaskRequest(AbstractModel):
    """DescribeRocketMQSmoothMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQSmoothMigrationTaskResponse(AbstractModel):
    """DescribeRocketMQSmoothMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _ClusterId: 目标集群ID
        :type ClusterId: str
        :param _SourceClusterName: 源集群名称
        :type SourceClusterName: str
        :param _ConnectionType: 网络连接类型，
PUBLIC 公网
VPC 私有网络
OTHER 其它
        :type ConnectionType: str
        :param _SourceClusterNameServer: 源集群NameServer地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceClusterNameServer: str
        :param _VpcId: 源集群所在私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 源集群所在子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _EnableACL: 是否开启ACL
        :type EnableACL: bool
        :param _AccessKey: 源集群AccessKey
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param _SecretKey: 元集群SecretKey
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _TaskError: 配置源集群时发生的错误
TIMEOUT 连接超时，
SERVER_ERROR 服务错误，
INTERNAL_ERROR 内部错误，
CONNECT_NAMESERVER_ERROR 连接nameserver错误
CONNECT_BROKER_ERROR 连接broker错误
ACL_WRONG ACL信息不正确

注意：此字段可能返回 null，表示取不到有效值。
        :type TaskError: str
        :param _TaskStatus: 任务状态
Configuration 迁移配置
SourceConnecting 连接源集群中
SourceConnectionFailure 连接源集群失败
MetaDataImport 元数据导入
EndpointSetup 切换接入点
ServiceMigration 切流中
Completed 已完成
Cancelled 已取消
        :type TaskStatus: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TopicTypeDistribution: 主题类型分布情况
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicTypeDistribution: list of RocketMQTopicDistribution
        :param _TopicStageDistribution: 主题迁移进度分布情况
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicStageDistribution: list of RocketMQMigrationTopicDistribution
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskName = None
        self._ClusterId = None
        self._SourceClusterName = None
        self._ConnectionType = None
        self._SourceClusterNameServer = None
        self._VpcId = None
        self._SubnetId = None
        self._EnableACL = None
        self._AccessKey = None
        self._SecretKey = None
        self._TaskError = None
        self._TaskStatus = None
        self._TaskId = None
        self._TopicTypeDistribution = None
        self._TopicStageDistribution = None
        self._RequestId = None

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def ClusterId(self):
        """目标集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SourceClusterName(self):
        """源集群名称
        :rtype: str
        """
        return self._SourceClusterName

    @SourceClusterName.setter
    def SourceClusterName(self, SourceClusterName):
        self._SourceClusterName = SourceClusterName

    @property
    def ConnectionType(self):
        """网络连接类型，
PUBLIC 公网
VPC 私有网络
OTHER 其它
        :rtype: str
        """
        return self._ConnectionType

    @ConnectionType.setter
    def ConnectionType(self, ConnectionType):
        self._ConnectionType = ConnectionType

    @property
    def SourceClusterNameServer(self):
        """源集群NameServer地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceClusterNameServer

    @SourceClusterNameServer.setter
    def SourceClusterNameServer(self, SourceClusterNameServer):
        self._SourceClusterNameServer = SourceClusterNameServer

    @property
    def VpcId(self):
        """源集群所在私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """源集群所在子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EnableACL(self):
        """是否开启ACL
        :rtype: bool
        """
        return self._EnableACL

    @EnableACL.setter
    def EnableACL(self, EnableACL):
        self._EnableACL = EnableACL

    @property
    def AccessKey(self):
        """源集群AccessKey
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """元集群SecretKey
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def TaskError(self):
        """配置源集群时发生的错误
TIMEOUT 连接超时，
SERVER_ERROR 服务错误，
INTERNAL_ERROR 内部错误，
CONNECT_NAMESERVER_ERROR 连接nameserver错误
CONNECT_BROKER_ERROR 连接broker错误
ACL_WRONG ACL信息不正确

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskError

    @TaskError.setter
    def TaskError(self, TaskError):
        self._TaskError = TaskError

    @property
    def TaskStatus(self):
        """任务状态
Configuration 迁移配置
SourceConnecting 连接源集群中
SourceConnectionFailure 连接源集群失败
MetaDataImport 元数据导入
EndpointSetup 切换接入点
ServiceMigration 切流中
Completed 已完成
Cancelled 已取消
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TopicTypeDistribution(self):
        """主题类型分布情况
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQTopicDistribution
        """
        return self._TopicTypeDistribution

    @TopicTypeDistribution.setter
    def TopicTypeDistribution(self, TopicTypeDistribution):
        self._TopicTypeDistribution = TopicTypeDistribution

    @property
    def TopicStageDistribution(self):
        """主题迁移进度分布情况
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQMigrationTopicDistribution
        """
        return self._TopicStageDistribution

    @TopicStageDistribution.setter
    def TopicStageDistribution(self, TopicStageDistribution):
        self._TopicStageDistribution = TopicStageDistribution

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
        self._TaskName = params.get("TaskName")
        self._ClusterId = params.get("ClusterId")
        self._SourceClusterName = params.get("SourceClusterName")
        self._ConnectionType = params.get("ConnectionType")
        self._SourceClusterNameServer = params.get("SourceClusterNameServer")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._EnableACL = params.get("EnableACL")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._TaskError = params.get("TaskError")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskId = params.get("TaskId")
        if params.get("TopicTypeDistribution") is not None:
            self._TopicTypeDistribution = []
            for item in params.get("TopicTypeDistribution"):
                obj = RocketMQTopicDistribution()
                obj._deserialize(item)
                self._TopicTypeDistribution.append(obj)
        if params.get("TopicStageDistribution") is not None:
            self._TopicStageDistribution = []
            for item in params.get("TopicStageDistribution"):
                obj = RocketMQMigrationTopicDistribution()
                obj._deserialize(item)
                self._TopicStageDistribution.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQSourceClusterGroupListRequest(AbstractModel):
    """DescribeRocketMQSourceClusterGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _TaskId: 迁移任务名称
        :type TaskId: str
        :param _Filters: 查询过滤器，支持字段groupName，imported
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._TaskId = None
        self._Filters = None

    @property
    def Limit(self):
        """页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TaskId(self):
        """迁移任务名称
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Filters(self):
        """查询过滤器，支持字段groupName，imported
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TaskId = params.get("TaskId")
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
        


class DescribeRocketMQSourceClusterGroupListResponse(AbstractModel):
    """DescribeRocketMQSourceClusterGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: group列表
        :type Groups: list of RocketMQGroupConfigOutput
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Groups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Groups(self):
        """group列表
        :rtype: list of RocketMQGroupConfigOutput
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def TotalCount(self):
        """总条数
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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = RocketMQGroupConfigOutput()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQSourceClusterTopicListRequest(AbstractModel):
    """DescribeRocketMQSourceClusterTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _TaskId: 迁移任务名
        :type TaskId: str
        :param _Filters: 查询过滤器，支持字段如下
TopicName,
Type，Imported
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._TaskId = None
        self._Filters = None

    @property
    def Limit(self):
        """分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TaskId(self):
        """迁移任务名
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Filters(self):
        """查询过滤器，支持字段如下
TopicName,
Type，Imported
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._TaskId = params.get("TaskId")
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
        


class DescribeRocketMQSourceClusterTopicListResponse(AbstractModel):
    """DescribeRocketMQSourceClusterTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topics: topic层列表
        :type Topics: list of RocketMQTopicConfigOutput
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topics = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Topics(self):
        """topic层列表
        :rtype: list of RocketMQTopicConfigOutput
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def TotalCount(self):
        """总条数
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
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = RocketMQTopicConfigOutput()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQSubscriptionsRequest(AbstractModel):
    """DescribeRocketMQSubscriptions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _Group: 消费组名称
        :type Group: str
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询限制条数
        :type Limit: int
        """
        self._ClusterId = None
        self._Namespace = None
        self._Group = None
        self._Offset = None
        self._Limit = None

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
    def Namespace(self):
        """命名空间名称
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        """消费组名称
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Offset(self):
        """查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQSubscriptionsResponse(AbstractModel):
    """DescribeRocketMQSubscriptions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Subscriptions: 订阅关系列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Subscriptions: list of RocketMQSubscription
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Subscriptions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Subscriptions(self):
        """订阅关系列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQSubscription
        """
        return self._Subscriptions

    @Subscriptions.setter
    def Subscriptions(self, Subscriptions):
        self._Subscriptions = Subscriptions

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
        if params.get("Subscriptions") is not None:
            self._Subscriptions = []
            for item in params.get("Subscriptions"):
                obj = RocketMQSubscription()
                obj._deserialize(item)
                self._Subscriptions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQTopUsagesRequest(AbstractModel):
    """DescribeRocketMQTopUsages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _MetricName: 指标名称，支持以下：
consumeLag，消费组堆积数量
deadLetterCount，死信数量
topicRateIn,   Topic生产速率
topicRateOut，Topic消费速率
topicStorageSize，Topic存储空间
topicApiCalls，Topic API调用次数
        :type MetricName: str
        :param _Limit: 排序数量，最大20
        :type Limit: int
        """
        self._ClusterId = None
        self._MetricName = None
        self._Limit = None

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
    def MetricName(self):
        """指标名称，支持以下：
consumeLag，消费组堆积数量
deadLetterCount，死信数量
topicRateIn,   Topic生产速率
topicRateOut，Topic消费速率
topicStorageSize，Topic存储空间
topicApiCalls，Topic API调用次数
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Limit(self):
        """排序数量，最大20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._MetricName = params.get("MetricName")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQTopUsagesResponse(AbstractModel):
    """DescribeRocketMQTopUsages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Values: 指标值列表
        :type Values: list of int
        :param _Dimensions: 指标值对应的维度组合，本接口存在以下几个维度：
tenant，namespace，group，topic
        :type Dimensions: list of DimensionInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Values = None
        self._Dimensions = None
        self._RequestId = None

    @property
    def Values(self):
        """指标值列表
        :rtype: list of int
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Dimensions(self):
        """指标值对应的维度组合，本接口存在以下几个维度：
tenant，namespace，group，topic
        :rtype: list of DimensionInstance
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

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
        self._Values = params.get("Values")
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionInstance()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQTopicMsgsRequest(AbstractModel):
    """DescribeRocketMQTopicMsgs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _EnvironmentId: 命名空间
        :type EnvironmentId: str
        :param _TopicName: 主题名称，查询死信时为groupId
        :type TopicName: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _MsgId: 消息 ID
        :type MsgId: str
        :param _MsgKey: 消息 key
        :type MsgKey: str
        :param _Offset: 查询偏移
        :type Offset: int
        :param _Limit: 查询限额
        :type Limit: int
        :param _TaskRequestId: 标志一次分页事务
        :type TaskRequestId: str
        :param _QueryDlqMsg: 死信查询时该值为true，只对Rocketmq有效
        :type QueryDlqMsg: bool
        :param _NumOfLatestMsg: 查询最近N条消息 最大不超过1024，默认-1为其他查询条件
        :type NumOfLatestMsg: int
        :param _Tag: TAG表达式
        :type Tag: str
        :param _QueryDeadLetterMessage: 死信查询时该值为true，只对Rocketmq有效
        :type QueryDeadLetterMessage: bool
        """
        self._ClusterId = None
        self._EnvironmentId = None
        self._TopicName = None
        self._StartTime = None
        self._EndTime = None
        self._MsgId = None
        self._MsgKey = None
        self._Offset = None
        self._Limit = None
        self._TaskRequestId = None
        self._QueryDlqMsg = None
        self._NumOfLatestMsg = None
        self._Tag = None
        self._QueryDeadLetterMessage = None

    @property
    def ClusterId(self):
        """集群 ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """命名空间
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称，查询死信时为groupId
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MsgId(self):
        """消息 ID
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def MsgKey(self):
        """消息 key
        :rtype: str
        """
        return self._MsgKey

    @MsgKey.setter
    def MsgKey(self, MsgKey):
        self._MsgKey = MsgKey

    @property
    def Offset(self):
        """查询偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询限额
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TaskRequestId(self):
        """标志一次分页事务
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

    @property
    def QueryDlqMsg(self):
        warnings.warn("parameter `QueryDlqMsg` is deprecated", DeprecationWarning) 

        """死信查询时该值为true，只对Rocketmq有效
        :rtype: bool
        """
        return self._QueryDlqMsg

    @QueryDlqMsg.setter
    def QueryDlqMsg(self, QueryDlqMsg):
        warnings.warn("parameter `QueryDlqMsg` is deprecated", DeprecationWarning) 

        self._QueryDlqMsg = QueryDlqMsg

    @property
    def NumOfLatestMsg(self):
        """查询最近N条消息 最大不超过1024，默认-1为其他查询条件
        :rtype: int
        """
        return self._NumOfLatestMsg

    @NumOfLatestMsg.setter
    def NumOfLatestMsg(self, NumOfLatestMsg):
        self._NumOfLatestMsg = NumOfLatestMsg

    @property
    def Tag(self):
        """TAG表达式
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def QueryDeadLetterMessage(self):
        """死信查询时该值为true，只对Rocketmq有效
        :rtype: bool
        """
        return self._QueryDeadLetterMessage

    @QueryDeadLetterMessage.setter
    def QueryDeadLetterMessage(self, QueryDeadLetterMessage):
        self._QueryDeadLetterMessage = QueryDeadLetterMessage


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MsgId = params.get("MsgId")
        self._MsgKey = params.get("MsgKey")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TaskRequestId = params.get("TaskRequestId")
        self._QueryDlqMsg = params.get("QueryDlqMsg")
        self._NumOfLatestMsg = params.get("NumOfLatestMsg")
        self._Tag = params.get("Tag")
        self._QueryDeadLetterMessage = params.get("QueryDeadLetterMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQTopicMsgsResponse(AbstractModel):
    """DescribeRocketMQTopicMsgs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _TopicMsgLogSets: 消息列表
        :type TopicMsgLogSets: list of RocketMQMsgLog
        :param _TaskRequestId: 标志一次分页事务
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TopicMsgLogSets = None
        self._TaskRequestId = None
        self._RequestId = None

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
    def TopicMsgLogSets(self):
        """消息列表
        :rtype: list of RocketMQMsgLog
        """
        return self._TopicMsgLogSets

    @TopicMsgLogSets.setter
    def TopicMsgLogSets(self, TopicMsgLogSets):
        self._TopicMsgLogSets = TopicMsgLogSets

    @property
    def TaskRequestId(self):
        """标志一次分页事务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

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
        if params.get("TopicMsgLogSets") is not None:
            self._TopicMsgLogSets = []
            for item in params.get("TopicMsgLogSets"):
                obj = RocketMQMsgLog()
                obj._deserialize(item)
                self._TopicMsgLogSets.append(obj)
        self._TaskRequestId = params.get("TaskRequestId")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQTopicStatsRequest(AbstractModel):
    """DescribeRocketMQTopicStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 实例ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间
        :type NamespaceId: str
        :param _TopicName: 主题名
        :type TopicName: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._TopicName = None

    @property
    def ClusterId(self):
        """实例ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        """命名空间
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQTopicStatsResponse(AbstractModel):
    """DescribeRocketMQTopicStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicStatsList: 生产详情列表
        :type TopicStatsList: list of TopicStats
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicStatsList = None
        self._RequestId = None

    @property
    def TopicStatsList(self):
        """生产详情列表
        :rtype: list of TopicStats
        """
        return self._TopicStatsList

    @TopicStatsList.setter
    def TopicStatsList(self, TopicStatsList):
        self._TopicStatsList = TopicStatsList

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
        if params.get("TopicStatsList") is not None:
            self._TopicStatsList = []
            for item in params.get("TopicStatsList"):
                obj = TopicStats()
                obj._deserialize(item)
                self._TopicStatsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQTopicsByGroupRequest(AbstractModel):
    """DescribeRocketMQTopicsByGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _GroupId: 消费组名称
        :type GroupId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制条数
        :type Limit: int
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._Offset = None
        self._Limit = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        """消费组名称
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQTopicsByGroupResponse(AbstractModel):
    """DescribeRocketMQTopicsByGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Topics: 主题列表
        :type Topics: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Topics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Topics(self):
        """主题列表
        :rtype: list of str
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

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
        self._Topics = params.get("Topics")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQTopicsRequest(AbstractModel):
    """DescribeRocketMQTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询限制数
        :type Limit: int
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间
        :type NamespaceId: str
        :param _FilterType: 按主题类型过滤查询结果，可选择Normal, GlobalOrder, PartitionedOrder, Transaction
        :type FilterType: list of str
        :param _FilterName: 按主题名称搜索，支持模糊查询
        :type FilterName: str
        :param _FilterGroup: 按订阅消费组名称过滤
        :type FilterGroup: str
        """
        self._Offset = None
        self._Limit = None
        self._ClusterId = None
        self._NamespaceId = None
        self._FilterType = None
        self._FilterName = None
        self._FilterGroup = None

    @property
    def Offset(self):
        """查询偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询限制数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

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
    def NamespaceId(self):
        """命名空间
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def FilterType(self):
        """按主题类型过滤查询结果，可选择Normal, GlobalOrder, PartitionedOrder, Transaction
        :rtype: list of str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def FilterName(self):
        """按主题名称搜索，支持模糊查询
        :rtype: str
        """
        return self._FilterName

    @FilterName.setter
    def FilterName(self, FilterName):
        self._FilterName = FilterName

    @property
    def FilterGroup(self):
        """按订阅消费组名称过滤
        :rtype: str
        """
        return self._FilterGroup

    @FilterGroup.setter
    def FilterGroup(self, FilterGroup):
        self._FilterGroup = FilterGroup


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._FilterType = params.get("FilterType")
        self._FilterName = params.get("FilterName")
        self._FilterGroup = params.get("FilterGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQTopicsResponse(AbstractModel):
    """DescribeRocketMQTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _Topics: 主题信息列表
        :type Topics: list of RocketMQTopic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Topics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Topics(self):
        """主题信息列表
        :rtype: list of RocketMQTopic
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

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
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = RocketMQTopic()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQVipInstanceDetailRequest(AbstractModel):
    """DescribeRocketMQVipInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQVipInstanceDetailResponse(AbstractModel):
    """DescribeRocketMQVipInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: 集群信息
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param _InstanceConfig: 集群配置
        :type InstanceConfig: :class:`tencentcloud.tdmq.v20200217.models.RocketMQInstanceConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._InstanceConfig = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        """集群信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        """
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def InstanceConfig(self):
        """集群配置
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQInstanceConfig`
        """
        return self._InstanceConfig

    @InstanceConfig.setter
    def InstanceConfig(self, InstanceConfig):
        self._InstanceConfig = InstanceConfig

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
            self._ClusterInfo = RocketMQClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("InstanceConfig") is not None:
            self._InstanceConfig = RocketMQInstanceConfig()
            self._InstanceConfig._deserialize(params.get("InstanceConfig"))
        self._RequestId = params.get("RequestId")


class DescribeRocketMQVipInstancesRequest(AbstractModel):
    """DescribeRocketMQVipInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件过滤器，支持的查询条件如下：
instanceIds - 实例ID
instanceName - 实例名称
status - 实例状态
        :type Filters: list of Filter
        :param _Limit: 查询数目上限，默认20
        :type Limit: int
        :param _Offset: 查询起始位置
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        """查询条件过滤器，支持的查询条件如下：
instanceIds - 实例ID
instanceName - 实例名称
status - 实例状态
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """查询数目上限，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询起始位置
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
        


class DescribeRocketMQVipInstancesResponse(AbstractModel):
    """DescribeRocketMQVipInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 未分页的总数目
        :type TotalCount: int
        :param _Instances: 实例信息列表
        :type Instances: list of RocketMQVipInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """未分页的总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """实例信息列表
        :rtype: list of RocketMQVipInstance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RocketMQVipInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRolesRequest(AbstractModel):
    """DescribeRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        :param _RoleName: 角色名称，模糊查询
        :type RoleName: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _Filters: * RoleName
按照角色名进行过滤，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self._ClusterId = None
        self._RoleName = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        """角色名称，模糊查询
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """* RoleName
按照角色名进行过滤，精确查询。
类型：String
必选：否
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RoleName = params.get("RoleName")
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
        


class DescribeRolesResponse(AbstractModel):
    """DescribeRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录数。
        :type TotalCount: int
        :param _RoleSets: 角色数组。
        :type RoleSets: list of Role
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RoleSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RoleSets(self):
        """角色数组。
        :rtype: list of Role
        """
        return self._RoleSets

    @RoleSets.setter
    def RoleSets(self, RoleSets):
        self._RoleSets = RoleSets

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
        if params.get("RoleSets") is not None:
            self._RoleSets = []
            for item in params.get("RoleSets"):
                obj = Role()
                obj._deserialize(item)
                self._RoleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscriptionsRequest(AbstractModel):
    """DescribeSubscriptions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名称。
        :type TopicName: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _SubscriptionName: 订阅者名称，模糊匹配。
        :type SubscriptionName: str
        :param _Filters: 数据过滤条件。
        :type Filters: list of FilterSubscription
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._SubscriptionName = None
        self._Filters = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SubscriptionName(self):
        """订阅者名称，模糊匹配。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def Filters(self):
        """数据过滤条件。
        :rtype: list of FilterSubscription
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SubscriptionName = params.get("SubscriptionName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterSubscription()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionsResponse(AbstractModel):
    """DescribeSubscriptions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubscriptionSets: 订阅者集合数组。
        :type SubscriptionSets: list of Subscription
        :param _TotalCount: 数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubscriptionSets = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SubscriptionSets(self):
        """订阅者集合数组。
        :rtype: list of Subscription
        """
        return self._SubscriptionSets

    @SubscriptionSets.setter
    def SubscriptionSets(self, SubscriptionSets):
        self._SubscriptionSets = SubscriptionSets

    @property
    def TotalCount(self):
        """数量。
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
        if params.get("SubscriptionSets") is not None:
            self._SubscriptionSets = []
            for item in params.get("SubscriptionSets"):
                obj = Subscription()
                obj._deserialize(item)
                self._SubscriptionSets.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTopicMsgsRequest(AbstractModel):
    """DescribeTopicMsgs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名。
        :type TopicName: str
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _MsgId: 消息ID。
        :type MsgId: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._MsgId = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def StartTime(self):
        """开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MsgId(self):
        """消息ID。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MsgId = params.get("MsgId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicMsgsResponse(AbstractModel):
    """DescribeTopicMsgs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数。
        :type TotalCount: int
        :param _TopicMsgLogSets: 消息日志列表。
        :type TopicMsgLogSets: list of MsgLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TopicMsgLogSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总记录数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicMsgLogSets(self):
        """消息日志列表。
        :rtype: list of MsgLog
        """
        return self._TopicMsgLogSets

    @TopicMsgLogSets.setter
    def TopicMsgLogSets(self, TopicMsgLogSets):
        self._TopicMsgLogSets = TopicMsgLogSets

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
        if params.get("TopicMsgLogSets") is not None:
            self._TopicMsgLogSets = []
            for item in params.get("TopicMsgLogSets"):
                obj = MsgLog()
                obj._deserialize(item)
                self._TopicMsgLogSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _TopicName: 主题名模糊匹配。
        :type TopicName: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param _TopicType: topic类型描述：
0：非持久非分区主题类型；
1：非持久分区主题类型；
2：持久非分区主题类型；
3：持久分区主题类型；
        :type TopicType: int
        :param _Filters: * TopicName
按照主题名字查询，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        :param _TopicCreator: 创建来源：
1：用户创建
2：系统创建
        :type TopicCreator: int
        """
        self._EnvironmentId = None
        self._ClusterId = None
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._TopicType = None
        self._Filters = None
        self._TopicCreator = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TopicName(self):
        """主题名模糊匹配。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TopicType(self):
        """topic类型描述：
0：非持久非分区主题类型；
1：非持久分区主题类型；
2：持久非分区主题类型；
3：持久分区主题类型；
        :rtype: int
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def Filters(self):
        """* TopicName
按照主题名字查询，精确查询。
类型：String
必选：否
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TopicCreator(self):
        """创建来源：
1：用户创建
2：系统创建
        :rtype: int
        """
        return self._TopicCreator

    @TopicCreator.setter
    def TopicCreator(self, TopicCreator):
        self._TopicCreator = TopicCreator


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterId = params.get("ClusterId")
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TopicType = params.get("TopicType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TopicCreator = params.get("TopicCreator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicSets: 主题集合数组。
        :type TopicSets: list of Topic
        :param _TotalCount: 主题数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicSets = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TopicSets(self):
        """主题集合数组。
        :rtype: list of Topic
        """
        return self._TopicSets

    @TopicSets.setter
    def TopicSets(self, TopicSets):
        self._TopicSets = TopicSets

    @property
    def TotalCount(self):
        """主题数量。
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
        if params.get("TopicSets") is not None:
            self._TopicSets = []
            for item in params.get("TopicSets"):
                obj = Topic()
                obj._deserialize(item)
                self._TopicSets.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetailedRolePerm(AbstractModel):
    """Topic&Group维度的权限配置

    """

    def __init__(self):
        r"""
        :param _Resource: 权限对应的资源
        :type Resource: str
        :param _PermWrite: 是否开启生产权限
        :type PermWrite: bool
        :param _PermRead: 是否开启消费权限
        :type PermRead: bool
        :param _ResourceType: 授权资源类型（Topic:主题; Group:消费组）
        :type ResourceType: str
        :param _Remark: 资源备注
        :type Remark: str
        """
        self._Resource = None
        self._PermWrite = None
        self._PermRead = None
        self._ResourceType = None
        self._Remark = None

    @property
    def Resource(self):
        """权限对应的资源
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def PermWrite(self):
        """是否开启生产权限
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def PermRead(self):
        """是否开启消费权限
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def ResourceType(self):
        """授权资源类型（Topic:主题; Group:消费组）
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Remark(self):
        """资源备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._PermWrite = params.get("PermWrite")
        self._PermRead = params.get("PermRead")
        self._ResourceType = params.get("ResourceType")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionInstance(AbstractModel):
    """实例维度组合数组

    """

    def __init__(self):
        r"""
        :param _Dimensions: 实例的维度组合
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: list of DimensionOpt
        """
        self._Dimensions = None

    @property
    def Dimensions(self):
        """实例的维度组合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DimensionOpt
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionOpt()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DimensionOpt(AbstractModel):
    """指标维度对象

    """

    def __init__(self):
        r"""
        :param _Name: 查询的维度名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 查询维度的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """查询的维度名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """查询维度的值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    """命名空间信息

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间名称
        :type EnvironmentId: str
        :param _Remark: 说明
        :type Remark: str
        :param _MsgTTL: 未消费消息过期时间，单位：秒，最大1296000（15天）
        :type MsgTTL: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 最近修改时间
        :type UpdateTime: str
        :param _NamespaceId: 命名空间ID
        :type NamespaceId: str
        :param _NamespaceName: 命名空间名称
        :type NamespaceName: str
        :param _TopicNum: Topic数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNum: int
        :param _RetentionPolicy: 消息保留策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        :param _AutoSubscriptionCreation: 是否自动创建订阅
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSubscriptionCreation: bool
        """
        self._EnvironmentId = None
        self._Remark = None
        self._MsgTTL = None
        self._CreateTime = None
        self._UpdateTime = None
        self._NamespaceId = None
        self._NamespaceName = None
        self._TopicNum = None
        self._RetentionPolicy = None
        self._AutoSubscriptionCreation = None

    @property
    def EnvironmentId(self):
        """命名空间名称
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Remark(self):
        """说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒，最大1296000（15天）
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

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
    def UpdateTime(self):
        """最近修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NamespaceId(self):
        """命名空间ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def NamespaceName(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def TopicNum(self):
        """Topic数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def RetentionPolicy(self):
        """消息保留策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        return self._RetentionPolicy

    @RetentionPolicy.setter
    def RetentionPolicy(self, RetentionPolicy):
        self._RetentionPolicy = RetentionPolicy

    @property
    def AutoSubscriptionCreation(self):
        """是否自动创建订阅
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoSubscriptionCreation

    @AutoSubscriptionCreation.setter
    def AutoSubscriptionCreation(self, AutoSubscriptionCreation):
        self._AutoSubscriptionCreation = AutoSubscriptionCreation


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Remark = params.get("Remark")
        self._MsgTTL = params.get("MsgTTL")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._NamespaceId = params.get("NamespaceId")
        self._NamespaceName = params.get("NamespaceName")
        self._TopicNum = params.get("TopicNum")
        if params.get("RetentionPolicy") is not None:
            self._RetentionPolicy = RetentionPolicy()
            self._RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        self._AutoSubscriptionCreation = params.get("AutoSubscriptionCreation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentRole(AbstractModel):
    """环境角色集合

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）。
        :type EnvironmentId: str
        :param _RoleName: 角色名称。
        :type RoleName: str
        :param _Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param _RoleDescribe: 角色描述。
        :type RoleDescribe: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._RoleDescribe = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        """角色名称。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        """授权项，最多只能包含produce、consume两项的非空字符串数组。
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def RoleDescribe(self):
        """角色描述。
        :rtype: str
        """
        return self._RoleDescribe

    @RoleDescribe.setter
    def RoleDescribe(self, RoleDescribe):
        self._RoleDescribe = RoleDescribe

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._RoleDescribe = params.get("RoleDescribe")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentRoleSet(AbstractModel):
    """批量绑定名字空间和角色权限关系

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 需要绑定的命名空间Id，不重复且存在资源
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param _Permissions: 名字空间需要绑定的权限，枚举为 "consume" "produce" 组合，但是不为空

注意：此字段可能返回 null，表示取不到有效值。
        :type Permissions: list of str
        """
        self._EnvironmentId = None
        self._Permissions = None

    @property
    def EnvironmentId(self):
        """需要绑定的命名空间Id，不重复且存在资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Permissions(self):
        """名字空间需要绑定的权限，枚举为 "consume" "produce" 组合，但是不为空

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Permissions = params.get("Permissions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class ExportRocketMQMessageDetailRequest(AbstractModel):
    """ExportRocketMQMessageDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _EnvironmentId: 应用命名空间
        :type EnvironmentId: str
        :param _TopicName: Topic名称
如果是死信消息 isDlqMsg=true
        :type TopicName: str
        :param _MsgId: 消息id
        :type MsgId: str
        :param _IncludeMsgBody: 是否包含消息体
        :type IncludeMsgBody: bool
        :param _DeadLetterMsg: 是否死信消息
        :type DeadLetterMsg: bool
        """
        self._ClusterId = None
        self._EnvironmentId = None
        self._TopicName = None
        self._MsgId = None
        self._IncludeMsgBody = None
        self._DeadLetterMsg = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        """应用命名空间
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """Topic名称
如果是死信消息 isDlqMsg=true
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def IncludeMsgBody(self):
        """是否包含消息体
        :rtype: bool
        """
        return self._IncludeMsgBody

    @IncludeMsgBody.setter
    def IncludeMsgBody(self, IncludeMsgBody):
        self._IncludeMsgBody = IncludeMsgBody

    @property
    def DeadLetterMsg(self):
        """是否死信消息
        :rtype: bool
        """
        return self._DeadLetterMsg

    @DeadLetterMsg.setter
    def DeadLetterMsg(self, DeadLetterMsg):
        self._DeadLetterMsg = DeadLetterMsg


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._MsgId = params.get("MsgId")
        self._IncludeMsgBody = params.get("IncludeMsgBody")
        self._DeadLetterMsg = params.get("DeadLetterMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportRocketMQMessageDetailResponse(AbstractModel):
    """ExportRocketMQMessageDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息id
        :type MsgId: str
        :param _BornTimestamp: 消息生成时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type BornTimestamp: int
        :param _StoreTimestamp: 消息存储时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type StoreTimestamp: int
        :param _BornHost: 消息生产客户端地址
注意：此字段可能返回 null，表示取不到有效值。
        :type BornHost: str
        :param _MsgTag: 消息Tag
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgTag: str
        :param _MsgKey: 消息Key
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgKey: str
        :param _Properties: 消息属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Properties: str
        :param _ReConsumeTimes: 消息重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReConsumeTimes: int
        :param _MsgBody: Base64编码格式字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgBody: str
        :param _MsgBodyCRC: 消息内容的CRC32 Code
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgBodyCRC: int
        :param _MsgBodySize: 消息体大小（单位K）
当大于2048时不返回消息
        :type MsgBodySize: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MsgId = None
        self._BornTimestamp = None
        self._StoreTimestamp = None
        self._BornHost = None
        self._MsgTag = None
        self._MsgKey = None
        self._Properties = None
        self._ReConsumeTimes = None
        self._MsgBody = None
        self._MsgBodyCRC = None
        self._MsgBodySize = None
        self._RequestId = None

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def BornTimestamp(self):
        """消息生成时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BornTimestamp

    @BornTimestamp.setter
    def BornTimestamp(self, BornTimestamp):
        self._BornTimestamp = BornTimestamp

    @property
    def StoreTimestamp(self):
        """消息存储时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StoreTimestamp

    @StoreTimestamp.setter
    def StoreTimestamp(self, StoreTimestamp):
        self._StoreTimestamp = StoreTimestamp

    @property
    def BornHost(self):
        """消息生产客户端地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BornHost

    @BornHost.setter
    def BornHost(self, BornHost):
        self._BornHost = BornHost

    @property
    def MsgTag(self):
        """消息Tag
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgTag

    @MsgTag.setter
    def MsgTag(self, MsgTag):
        self._MsgTag = MsgTag

    @property
    def MsgKey(self):
        """消息Key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgKey

    @MsgKey.setter
    def MsgKey(self, MsgKey):
        self._MsgKey = MsgKey

    @property
    def Properties(self):
        """消息属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ReConsumeTimes(self):
        """消息重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReConsumeTimes

    @ReConsumeTimes.setter
    def ReConsumeTimes(self, ReConsumeTimes):
        self._ReConsumeTimes = ReConsumeTimes

    @property
    def MsgBody(self):
        """Base64编码格式字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgBody

    @MsgBody.setter
    def MsgBody(self, MsgBody):
        self._MsgBody = MsgBody

    @property
    def MsgBodyCRC(self):
        """消息内容的CRC32 Code
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MsgBodyCRC

    @MsgBodyCRC.setter
    def MsgBodyCRC(self, MsgBodyCRC):
        self._MsgBodyCRC = MsgBodyCRC

    @property
    def MsgBodySize(self):
        """消息体大小（单位K）
当大于2048时不返回消息
        :rtype: int
        """
        return self._MsgBodySize

    @MsgBodySize.setter
    def MsgBodySize(self, MsgBodySize):
        self._MsgBodySize = MsgBodySize

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
        self._MsgId = params.get("MsgId")
        self._BornTimestamp = params.get("BornTimestamp")
        self._StoreTimestamp = params.get("StoreTimestamp")
        self._BornHost = params.get("BornHost")
        self._MsgTag = params.get("MsgTag")
        self._MsgKey = params.get("MsgKey")
        self._Properties = params.get("Properties")
        self._ReConsumeTimes = params.get("ReConsumeTimes")
        self._MsgBody = params.get("MsgBody")
        self._MsgBodyCRC = params.get("MsgBodyCRC")
        self._MsgBodySize = params.get("MsgBodySize")
        self._RequestId = params.get("RequestId")


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
        


class FilterSubscription(AbstractModel):
    """过滤订阅列表

    """

    def __init__(self):
        r"""
        :param _ConsumerHasCount: 是否仅展示包含真实消费者的订阅。
        :type ConsumerHasCount: bool
        :param _ConsumerHasBacklog: 是否仅展示消息堆积的订阅。
        :type ConsumerHasBacklog: bool
        :param _ConsumerHasExpired: 是否仅展示存在消息超期丢弃的订阅。
        :type ConsumerHasExpired: bool
        :param _SubscriptionNames: 按照订阅名过滤，精确查询。
        :type SubscriptionNames: list of str
        """
        self._ConsumerHasCount = None
        self._ConsumerHasBacklog = None
        self._ConsumerHasExpired = None
        self._SubscriptionNames = None

    @property
    def ConsumerHasCount(self):
        """是否仅展示包含真实消费者的订阅。
        :rtype: bool
        """
        return self._ConsumerHasCount

    @ConsumerHasCount.setter
    def ConsumerHasCount(self, ConsumerHasCount):
        self._ConsumerHasCount = ConsumerHasCount

    @property
    def ConsumerHasBacklog(self):
        """是否仅展示消息堆积的订阅。
        :rtype: bool
        """
        return self._ConsumerHasBacklog

    @ConsumerHasBacklog.setter
    def ConsumerHasBacklog(self, ConsumerHasBacklog):
        self._ConsumerHasBacklog = ConsumerHasBacklog

    @property
    def ConsumerHasExpired(self):
        """是否仅展示存在消息超期丢弃的订阅。
        :rtype: bool
        """
        return self._ConsumerHasExpired

    @ConsumerHasExpired.setter
    def ConsumerHasExpired(self, ConsumerHasExpired):
        self._ConsumerHasExpired = ConsumerHasExpired

    @property
    def SubscriptionNames(self):
        """按照订阅名过滤，精确查询。
        :rtype: list of str
        """
        return self._SubscriptionNames

    @SubscriptionNames.setter
    def SubscriptionNames(self, SubscriptionNames):
        self._SubscriptionNames = SubscriptionNames


    def _deserialize(self, params):
        self._ConsumerHasCount = params.get("ConsumerHasCount")
        self._ConsumerHasBacklog = params.get("ConsumerHasBacklog")
        self._ConsumerHasExpired = params.get("ConsumerHasExpired")
        self._SubscriptionNames = params.get("SubscriptionNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTopicListRequest(AbstractModel):
    """GetTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param _Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        """
        self._EnvironmentId = None
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        """起始下标，不填默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，不填则默认为10，最大值为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTopicListResponse(AbstractModel):
    """GetTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 主题数量。
        :type TotalCount: int
        :param _TopicList: 主题列表
        :type TopicList: list of Topic_Simplification
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TopicList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """主题数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicList(self):
        """主题列表
        :rtype: list of Topic_Simplification
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

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
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = Topic_Simplification()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._RequestId = params.get("RequestId")


class ImportRocketMQConsumerGroupsRequest(AbstractModel):
    """ImportRocketMQConsumerGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Groups: 导入topic
        :type Groups: list of RocketMQGroupConfig
        :param _TaskId: 任务id
        :type TaskId: str
        """
        self._Groups = None
        self._TaskId = None

    @property
    def Groups(self):
        """导入topic
        :rtype: list of RocketMQGroupConfig
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = RocketMQGroupConfig()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportRocketMQConsumerGroupsResponse(AbstractModel):
    """ImportRocketMQConsumerGroups返回参数结构体

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


class ImportRocketMQTopicsRequest(AbstractModel):
    """ImportRocketMQTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topics: 导入topic
        :type Topics: list of RocketMQTopicConfig
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._Topics = None
        self._TaskId = None

    @property
    def Topics(self):
        """导入topic
        :rtype: list of RocketMQTopicConfig
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = RocketMQTopicConfig()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportRocketMQTopicsResponse(AbstractModel):
    """ImportRocketMQTopics返回参数结构体

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


class InstanceNodeDistribution(AbstractModel):
    """实例节点分布信息

    """

    def __init__(self):
        r"""
        :param _ZoneName: 可用区
        :type ZoneName: str
        :param _ZoneId: 可用区id
        :type ZoneId: str
        :param _NodeCount: 节点数
        :type NodeCount: int
        :param _NodePermWipeFlag: 有调度任务且没有切回的可用区，此标识为true
        :type NodePermWipeFlag: bool
        :param _ZoneStatus: 可用区状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneStatus: str
        """
        self._ZoneName = None
        self._ZoneId = None
        self._NodeCount = None
        self._NodePermWipeFlag = None
        self._ZoneStatus = None

    @property
    def ZoneName(self):
        """可用区
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        """可用区id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NodeCount(self):
        """节点数
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def NodePermWipeFlag(self):
        """有调度任务且没有切回的可用区，此标识为true
        :rtype: bool
        """
        return self._NodePermWipeFlag

    @NodePermWipeFlag.setter
    def NodePermWipeFlag(self, NodePermWipeFlag):
        self._NodePermWipeFlag = NodePermWipeFlag

    @property
    def ZoneStatus(self):
        """可用区状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneStatus

    @ZoneStatus.setter
    def ZoneStatus(self, ZoneStatus):
        self._ZoneStatus = ZoneStatus


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._NodeCount = params.get("NodeCount")
        self._NodePermWipeFlag = params.get("NodePermWipeFlag")
        self._ZoneStatus = params.get("ZoneStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternalTenant(AbstractModel):
    """面向运营端的虚拟集群信息

    """

    def __init__(self):
        r"""
        :param _TenantId: 虚拟集群ID
        :type TenantId: str
        :param _TenantName: 虚拟集群名称
        :type TenantName: str
        :param _CustomerUin: 客户UIN
        :type CustomerUin: str
        :param _CustomerAppId: 客户的APPID
        :type CustomerAppId: str
        :param _ClusterName: 物理集群名称
        :type ClusterName: str
        :param _Type: 集群协议类型，支持的值为TDMQ，ROCKETMQ，AMQP，CMQ
        :type Type: str
        :param _MaxNamespaces: 命名空间配额
        :type MaxNamespaces: int
        :param _UsedNamespaces: 已使用命名空间配额
        :type UsedNamespaces: int
        :param _MaxTopics: Topic配额
        :type MaxTopics: int
        :param _UsedTopics: 已使用Topic配额
        :type UsedTopics: int
        :param _MaxPartitions: Topic分区数配额
        :type MaxPartitions: int
        :param _UsedPartitions: 已使用Topic分区数配额
        :type UsedPartitions: int
        :param _MaxMsgBacklogSize: 存储配额, byte为单位
        :type MaxMsgBacklogSize: int
        :param _MaxPublishTps: 命名空间最大生产TPS
        :type MaxPublishTps: int
        :param _MaxRetention: 消息最大保留时间，秒为单位
        :type MaxRetention: int
        :param _CreateTime: 创建时间，毫秒为单位
        :type CreateTime: int
        :param _UpdateTime: 修改时间，毫秒为单位
        :type UpdateTime: int
        :param _MaxDispatchTps: 命名空间最大消费TPS
        :type MaxDispatchTps: int
        :param _MaxDispatchRateInBytes: 命名空间最大消费带宽，byte为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDispatchRateInBytes: int
        :param _MaxPublishRateInBytes: 命名空间最大生产带宽，byte为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPublishRateInBytes: int
        :param _MaxRetentionSizeInMB: 消息最大保留空间，MB为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetentionSizeInMB: int
        :param _PublicAccessEnabled: public Access Enabled
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccessEnabled: bool
        """
        self._TenantId = None
        self._TenantName = None
        self._CustomerUin = None
        self._CustomerAppId = None
        self._ClusterName = None
        self._Type = None
        self._MaxNamespaces = None
        self._UsedNamespaces = None
        self._MaxTopics = None
        self._UsedTopics = None
        self._MaxPartitions = None
        self._UsedPartitions = None
        self._MaxMsgBacklogSize = None
        self._MaxPublishTps = None
        self._MaxRetention = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MaxDispatchTps = None
        self._MaxDispatchRateInBytes = None
        self._MaxPublishRateInBytes = None
        self._MaxRetentionSizeInMB = None
        self._PublicAccessEnabled = None

    @property
    def TenantId(self):
        """虚拟集群ID
        :rtype: str
        """
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def TenantName(self):
        """虚拟集群名称
        :rtype: str
        """
        return self._TenantName

    @TenantName.setter
    def TenantName(self, TenantName):
        self._TenantName = TenantName

    @property
    def CustomerUin(self):
        """客户UIN
        :rtype: str
        """
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

    @property
    def CustomerAppId(self):
        """客户的APPID
        :rtype: str
        """
        return self._CustomerAppId

    @CustomerAppId.setter
    def CustomerAppId(self, CustomerAppId):
        self._CustomerAppId = CustomerAppId

    @property
    def ClusterName(self):
        """物理集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Type(self):
        """集群协议类型，支持的值为TDMQ，ROCKETMQ，AMQP，CMQ
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MaxNamespaces(self):
        """命名空间配额
        :rtype: int
        """
        return self._MaxNamespaces

    @MaxNamespaces.setter
    def MaxNamespaces(self, MaxNamespaces):
        self._MaxNamespaces = MaxNamespaces

    @property
    def UsedNamespaces(self):
        """已使用命名空间配额
        :rtype: int
        """
        return self._UsedNamespaces

    @UsedNamespaces.setter
    def UsedNamespaces(self, UsedNamespaces):
        self._UsedNamespaces = UsedNamespaces

    @property
    def MaxTopics(self):
        """Topic配额
        :rtype: int
        """
        return self._MaxTopics

    @MaxTopics.setter
    def MaxTopics(self, MaxTopics):
        self._MaxTopics = MaxTopics

    @property
    def UsedTopics(self):
        """已使用Topic配额
        :rtype: int
        """
        return self._UsedTopics

    @UsedTopics.setter
    def UsedTopics(self, UsedTopics):
        self._UsedTopics = UsedTopics

    @property
    def MaxPartitions(self):
        """Topic分区数配额
        :rtype: int
        """
        return self._MaxPartitions

    @MaxPartitions.setter
    def MaxPartitions(self, MaxPartitions):
        self._MaxPartitions = MaxPartitions

    @property
    def UsedPartitions(self):
        """已使用Topic分区数配额
        :rtype: int
        """
        return self._UsedPartitions

    @UsedPartitions.setter
    def UsedPartitions(self, UsedPartitions):
        self._UsedPartitions = UsedPartitions

    @property
    def MaxMsgBacklogSize(self):
        """存储配额, byte为单位
        :rtype: int
        """
        return self._MaxMsgBacklogSize

    @MaxMsgBacklogSize.setter
    def MaxMsgBacklogSize(self, MaxMsgBacklogSize):
        self._MaxMsgBacklogSize = MaxMsgBacklogSize

    @property
    def MaxPublishTps(self):
        """命名空间最大生产TPS
        :rtype: int
        """
        return self._MaxPublishTps

    @MaxPublishTps.setter
    def MaxPublishTps(self, MaxPublishTps):
        self._MaxPublishTps = MaxPublishTps

    @property
    def MaxRetention(self):
        """消息最大保留时间，秒为单位
        :rtype: int
        """
        return self._MaxRetention

    @MaxRetention.setter
    def MaxRetention(self, MaxRetention):
        self._MaxRetention = MaxRetention

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
    def UpdateTime(self):
        """修改时间，毫秒为单位
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MaxDispatchTps(self):
        """命名空间最大消费TPS
        :rtype: int
        """
        return self._MaxDispatchTps

    @MaxDispatchTps.setter
    def MaxDispatchTps(self, MaxDispatchTps):
        self._MaxDispatchTps = MaxDispatchTps

    @property
    def MaxDispatchRateInBytes(self):
        """命名空间最大消费带宽，byte为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxDispatchRateInBytes

    @MaxDispatchRateInBytes.setter
    def MaxDispatchRateInBytes(self, MaxDispatchRateInBytes):
        self._MaxDispatchRateInBytes = MaxDispatchRateInBytes

    @property
    def MaxPublishRateInBytes(self):
        """命名空间最大生产带宽，byte为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxPublishRateInBytes

    @MaxPublishRateInBytes.setter
    def MaxPublishRateInBytes(self, MaxPublishRateInBytes):
        self._MaxPublishRateInBytes = MaxPublishRateInBytes

    @property
    def MaxRetentionSizeInMB(self):
        """消息最大保留空间，MB为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxRetentionSizeInMB

    @MaxRetentionSizeInMB.setter
    def MaxRetentionSizeInMB(self, MaxRetentionSizeInMB):
        self._MaxRetentionSizeInMB = MaxRetentionSizeInMB

    @property
    def PublicAccessEnabled(self):
        """public Access Enabled
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled


    def _deserialize(self, params):
        self._TenantId = params.get("TenantId")
        self._TenantName = params.get("TenantName")
        self._CustomerUin = params.get("CustomerUin")
        self._CustomerAppId = params.get("CustomerAppId")
        self._ClusterName = params.get("ClusterName")
        self._Type = params.get("Type")
        self._MaxNamespaces = params.get("MaxNamespaces")
        self._UsedNamespaces = params.get("UsedNamespaces")
        self._MaxTopics = params.get("MaxTopics")
        self._UsedTopics = params.get("UsedTopics")
        self._MaxPartitions = params.get("MaxPartitions")
        self._UsedPartitions = params.get("UsedPartitions")
        self._MaxMsgBacklogSize = params.get("MaxMsgBacklogSize")
        self._MaxPublishTps = params.get("MaxPublishTps")
        self._MaxRetention = params.get("MaxRetention")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MaxDispatchTps = params.get("MaxDispatchTps")
        self._MaxDispatchRateInBytes = params.get("MaxDispatchRateInBytes")
        self._MaxPublishRateInBytes = params.get("MaxPublishRateInBytes")
        self._MaxRetentionSizeInMB = params.get("MaxRetentionSizeInMB")
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateTopic(AbstractModel):
    """迁移topic列表数据

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _TopicName: topic名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _MigrationStatus: 迁移状态
S_RW_D_NA 源集群读写
S_RW_D_R 源集群读写目标集群读
S_RW_D_RW 源集群读写目标集群读写
S_R_D_RW 源集群读目标集群读写
S_NA_D_RW 目标集群读写
注意：此字段可能返回 null，表示取不到有效值。
        :type MigrationStatus: str
        :param _HealthCheckPassed: 是否完成健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckPassed: bool
        :param _HealthCheckError: 上次健康检查返回的错误信息，仅在HealthCheckPassed为false时有效。
NotChecked 未执行检查，
Unknown 未知错误,
TopicNotImported 主题未导入,
 TopicNotExistsInSourceCluster  主题在源集群中不存在,
    TopicNotExistsInTargetCluster 主题在目标集群中不存在,
    ConsumerConnectedOnTarget 目标集群上存在消费者连接,
    SourceTopicHasNewMessagesIn5Minutes 源集群主题前5分钟内有新消息写入,
TargetTopicHasNewMessagesIn5Minutes 目标集群主题前5分钟内有新消息写入,
    SourceTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入,
TargetTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入,
    ConsumerGroupCountNotMatch 订阅组数量不一致,
    SourceTopicHasUnconsumedMessages 源集群主题存在未消费消息,
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckError: str
        """
        self._Namespace = None
        self._TopicName = None
        self._MigrationStatus = None
        self._HealthCheckPassed = None
        self._HealthCheckError = None

    @property
    def Namespace(self):
        """命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TopicName(self):
        """topic名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MigrationStatus(self):
        """迁移状态
S_RW_D_NA 源集群读写
S_RW_D_R 源集群读写目标集群读
S_RW_D_RW 源集群读写目标集群读写
S_R_D_RW 源集群读目标集群读写
S_NA_D_RW 目标集群读写
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MigrationStatus

    @MigrationStatus.setter
    def MigrationStatus(self, MigrationStatus):
        self._MigrationStatus = MigrationStatus

    @property
    def HealthCheckPassed(self):
        """是否完成健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HealthCheckPassed

    @HealthCheckPassed.setter
    def HealthCheckPassed(self, HealthCheckPassed):
        self._HealthCheckPassed = HealthCheckPassed

    @property
    def HealthCheckError(self):
        """上次健康检查返回的错误信息，仅在HealthCheckPassed为false时有效。
NotChecked 未执行检查，
Unknown 未知错误,
TopicNotImported 主题未导入,
 TopicNotExistsInSourceCluster  主题在源集群中不存在,
    TopicNotExistsInTargetCluster 主题在目标集群中不存在,
    ConsumerConnectedOnTarget 目标集群上存在消费者连接,
    SourceTopicHasNewMessagesIn5Minutes 源集群主题前5分钟内有新消息写入,
TargetTopicHasNewMessagesIn5Minutes 目标集群主题前5分钟内有新消息写入,
    SourceTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入,
TargetTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入,
    ConsumerGroupCountNotMatch 订阅组数量不一致,
    SourceTopicHasUnconsumedMessages 源集群主题存在未消费消息,
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HealthCheckError

    @HealthCheckError.setter
    def HealthCheckError(self, HealthCheckError):
        self._HealthCheckError = HealthCheckError


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._TopicName = params.get("TopicName")
        self._MigrationStatus = params.get("MigrationStatus")
        self._HealthCheckPassed = params.get("HealthCheckPassed")
        self._HealthCheckError = params.get("HealthCheckError")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterRequest(AbstractModel):
    """ModifyCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: Pulsar 集群的ID，需要更新的集群Id。
        :type ClusterId: str
        :param _ClusterName: 更新后的集群名称。
        :type ClusterName: str
        :param _Remark: 说明信息。长度限制为 128 字节
        :type Remark: str
        :param _PublicAccessEnabled: 开启公网访问，只能为true
        :type PublicAccessEnabled: bool
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None
        self._PublicAccessEnabled = None

    @property
    def ClusterId(self):
        """Pulsar 集群的ID，需要更新的集群Id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """更新后的集群名称。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        """说明信息。长度限制为 128 字节
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicAccessEnabled(self):
        """开启公网访问，只能为true
        :rtype: bool
        """
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterResponse(AbstractModel):
    """ModifyCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class ModifyCmqQueueAttributeRequest(AbstractModel):
    """ModifyCmqQueueAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一账号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param _MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :type VisibilityTimeout: int
        :param _MaxMsgSize: 消息最大长度，新版CMQ新建的队列默认1024KB，不支持修改
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: 消息最长未确认时间。取值范围 30-43200 秒（30秒~12小时），默认值 3600 (1 小时)。
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: 队列是否开启回溯消息能力，该参数取值范围0-1296000，0表示不开启。
        :type RewindSeconds: int
        :param _FirstQueryInterval: 第一次查询时间
        :type FirstQueryInterval: int
        :param _MaxQueryCount: 最大查询次数
        :type MaxQueryCount: int
        :param _DeadLetterQueueName: 死信队列名称
        :type DeadLetterQueueName: str
        :param _MaxTimeToLive: policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds
        :type MaxTimeToLive: int
        :param _MaxReceiveCount: 最大接收次数
        :type MaxReceiveCount: int
        :param _Policy: 死信队列策略
        :type Policy: int
        :param _Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :type Trace: bool
        :param _Transaction: 是否开启事务，1开启，0不开启
        :type Transaction: int
        :param _RetentionSizeInMB: 队列可回溯存储空间：若开启消息回溯，取值范围：10240MB - 512000MB，若不开启消息回溯，取值：0
        :type RetentionSizeInMB: int
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
        self._Transaction = None
        self._RetentionSizeInMB = None

    @property
    def QueueName(self):
        """队列名字，在单个地域同一账号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MaxMsgHeapNum(self):
        """最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
        :rtype: int
        """
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        """消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。
        :rtype: int
        """
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def VisibilityTimeout(self):
        """消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。
        :rtype: int
        """
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        """消息最大长度，新版CMQ新建的队列默认1024KB，不支持修改
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        """消息最长未确认时间。取值范围 30-43200 秒（30秒~12小时），默认值 3600 (1 小时)。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def RewindSeconds(self):
        """队列是否开启回溯消息能力，该参数取值范围0-1296000，0表示不开启。
        :rtype: int
        """
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def FirstQueryInterval(self):
        """第一次查询时间
        :rtype: int
        """
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        """最大查询次数
        :rtype: int
        """
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def DeadLetterQueueName(self):
        """死信队列名称
        :rtype: str
        """
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def MaxTimeToLive(self):
        """policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds
        :rtype: int
        """
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def MaxReceiveCount(self):
        """最大接收次数
        :rtype: int
        """
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount

    @property
    def Policy(self):
        """死信队列策略
        :rtype: int
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Trace(self):
        """是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :rtype: bool
        """
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace

    @property
    def Transaction(self):
        """是否开启事务，1开启，0不开启
        :rtype: int
        """
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def RetentionSizeInMB(self):
        """队列可回溯存储空间：若开启消息回溯，取值范围：10240MB - 512000MB，若不开启消息回溯，取值：0
        :rtype: int
        """
        return self._RetentionSizeInMB

    @RetentionSizeInMB.setter
    def RetentionSizeInMB(self, RetentionSizeInMB):
        self._RetentionSizeInMB = RetentionSizeInMB


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
        self._Transaction = params.get("Transaction")
        self._RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCmqQueueAttributeResponse(AbstractModel):
    """ModifyCmqQueueAttribute返回参数结构体

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


class ModifyCmqSubscriptionAttributeRequest(AbstractModel):
    """ModifyCmqSubscriptionAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :type TopicName: str
        :param _SubscriptionName: 订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
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
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        """订阅名字，在单个地域同一账号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def NotifyStrategy(self):
        """向 Endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值如下：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息。
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s···由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
        :rtype: str
        """
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def NotifyContentFormat(self):
        """推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 Protocol 是 queue，则取值必须为 SIMPLIFIED。如果 Protocol 是 HTTP，两个值均可以，默认值是 JSON。
        :rtype: str
        """
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat

    @property
    def FilterTags(self):
        """消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。
        :rtype: list of str
        """
        return self._FilterTags

    @FilterTags.setter
    def FilterTags(self, FilterTags):
        self._FilterTags = FilterTags

    @property
    def BindingKey(self):
        """BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。
        :rtype: list of str
        """
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
        


class ModifyCmqSubscriptionAttributeResponse(AbstractModel):
    """ModifyCmqSubscriptionAttribute返回参数结构体

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


class ModifyCmqTopicAttributeRequest(AbstractModel):
    """ModifyCmqTopicAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
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
        """主题名字，在单个地域同一账号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MaxMsgSize(self):
        """消息最大长度。取值范围1024 - 65536 Byte（即1 - 64K），默认值65536。
        :rtype: int
        """
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        """消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。
        :rtype: int
        """
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Trace(self):
        """是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。
        :rtype: bool
        """
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
        


class ModifyCmqTopicAttributeResponse(AbstractModel):
    """ModifyCmqTopicAttribute返回参数结构体

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


class ModifyEnvironmentAttributesRequest(AbstractModel):
    """ModifyEnvironmentAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间名称。
        :type EnvironmentId: str
        :param _MsgTTL: 未消费消息过期时间，单位：秒，范围60秒~15天。
        :type MsgTTL: int
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Remark: 备注，字符串最长不超过128。
        :type Remark: str
        :param _RetentionPolicy: 消息保留策略
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        :param _AutoSubscriptionCreation: 是否开启自动创建订阅
        :type AutoSubscriptionCreation: bool
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._ClusterId = None
        self._Remark = None
        self._RetentionPolicy = None
        self._AutoSubscriptionCreation = None

    @property
    def EnvironmentId(self):
        """命名空间名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒，范围60秒~15天。
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

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
    def Remark(self):
        """备注，字符串最长不超过128。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RetentionPolicy(self):
        """消息保留策略
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        return self._RetentionPolicy

    @RetentionPolicy.setter
    def RetentionPolicy(self, RetentionPolicy):
        self._RetentionPolicy = RetentionPolicy

    @property
    def AutoSubscriptionCreation(self):
        """是否开启自动创建订阅
        :rtype: bool
        """
        return self._AutoSubscriptionCreation

    @AutoSubscriptionCreation.setter
    def AutoSubscriptionCreation(self, AutoSubscriptionCreation):
        self._AutoSubscriptionCreation = AutoSubscriptionCreation


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        if params.get("RetentionPolicy") is not None:
            self._RetentionPolicy = RetentionPolicy()
            self._RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        self._AutoSubscriptionCreation = params.get("AutoSubscriptionCreation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentAttributesResponse(AbstractModel):
    """ModifyEnvironmentAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间名称。
        :type EnvironmentId: str
        :param _MsgTTL: 未消费消息过期时间，单位：秒。
        :type MsgTTL: int
        :param _Remark: 备注，字符串最长不超过128。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _NamespaceId: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._Remark = None
        self._NamespaceId = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        """命名空间名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒。
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def Remark(self):
        """备注，字符串最长不超过128。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def NamespaceId(self):
        """命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

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
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._Remark = params.get("Remark")
        self._NamespaceId = params.get("NamespaceId")
        self._RequestId = params.get("RequestId")


class ModifyEnvironmentRoleRequest(AbstractModel):
    """ModifyEnvironmentRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _RoleName: 角色名称。
        :type RoleName: str
        :param _Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param _ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        """角色名称。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        """授权项，最多只能包含produce、consume两项的非空字符串数组。
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def ClusterId(self):
        """必填字段，集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentRoleResponse(AbstractModel):
    """ModifyEnvironmentRole返回参数结构体

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


class ModifyPublicNetworkSecurityPolicyRequest(AbstractModel):
    """ModifyPublicNetworkSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _PolicyList: 策略列表
        :type PolicyList: list of SecurityPolicy
        """
        self._InstanceId = None
        self._PolicyList = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyList(self):
        """策略列表
        :rtype: list of SecurityPolicy
        """
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPublicNetworkSecurityPolicyResponse(AbstractModel):
    """ModifyPublicNetworkSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModifyResult: SUCCESS或者FAILURE
        :type ModifyResult: str
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModifyResult = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def ModifyResult(self):
        """SUCCESS或者FAILURE
        :rtype: str
        """
        return self._ModifyResult

    @ModifyResult.setter
    def ModifyResult(self, ModifyResult):
        self._ModifyResult = ModifyResult

    @property
    def InstanceId(self):
        """集群id
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
        self._ModifyResult = params.get("ModifyResult")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class ModifyRabbitMQPermissionRequest(AbstractModel):
    """ModifyRabbitMQPermission请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，权限关联的用户
        :type User: str
        :param _VirtualHost: vhost名称
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
        """vhost名称
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
        


class ModifyRabbitMQPermissionResponse(AbstractModel):
    """ModifyRabbitMQPermission返回参数结构体

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


class ModifyRabbitMQUserRequest(AbstractModel):
    """ModifyRabbitMQUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _User: 用户名，登录时使用
        :type User: str
        :param _Password: 密码，登录时使用
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
        


class ModifyRabbitMQUserResponse(AbstractModel):
    """ModifyRabbitMQUser返回参数结构体

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


class ModifyRabbitMQVipInstanceRequest(AbstractModel):
    """ModifyRabbitMQVipInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._ClusterName = None
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
    def ClusterName(self):
        """集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRabbitMQVipInstanceResponse(AbstractModel):
    """ModifyRabbitMQVipInstance返回参数结构体

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


class ModifyRabbitMQVirtualHostRequest(AbstractModel):
    """ModifyRabbitMQVirtualHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例Id
        :type InstanceId: str
        :param _VirtualHost: vhost名
        :type VirtualHost: str
        :param _Description: 描述
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
        """描述
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
        


class ModifyRabbitMQVirtualHostResponse(AbstractModel):
    """ModifyRabbitMQVirtualHost返回参数结构体

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


class ModifyRocketMQClusterRequest(AbstractModel):
    """ModifyRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: RocketMQ集群ID
        :type ClusterId: str
        :param _ClusterName: 3-64个字符，只能包含字母、数字、“-”及“_”
        :type ClusterName: str
        :param _Remark: 说明信息，不超过128个字符
        :type Remark: str
        :param _PublicAccessEnabled: 是否开启HTTP公网访问
        :type PublicAccessEnabled: bool
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None
        self._PublicAccessEnabled = None

    @property
    def ClusterId(self):
        """RocketMQ集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """3-64个字符，只能包含字母、数字、“-”及“_”
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        """说明信息，不超过128个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicAccessEnabled(self):
        """是否开启HTTP公网访问
        :rtype: bool
        """
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQClusterResponse(AbstractModel):
    """ModifyRocketMQCluster返回参数结构体

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


class ModifyRocketMQEnvironmentRoleRequest(AbstractModel):
    """ModifyRocketMQEnvironmentRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _RoleName: 角色名称。
        :type RoleName: str
        :param _Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param _ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        :param _DetailedPerms: Topic&Group维度权限配置
        :type DetailedPerms: list of DetailedRolePerm
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._ClusterId = None
        self._DetailedPerms = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        """角色名称。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        """授权项，最多只能包含produce、consume两项的非空字符串数组。
        :rtype: list of str
        """
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def ClusterId(self):
        """必填字段，集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DetailedPerms(self):
        """Topic&Group维度权限配置
        :rtype: list of DetailedRolePerm
        """
        return self._DetailedPerms

    @DetailedPerms.setter
    def DetailedPerms(self, DetailedPerms):
        self._DetailedPerms = DetailedPerms


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._ClusterId = params.get("ClusterId")
        if params.get("DetailedPerms") is not None:
            self._DetailedPerms = []
            for item in params.get("DetailedPerms"):
                obj = DetailedRolePerm()
                obj._deserialize(item)
                self._DetailedPerms.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQEnvironmentRoleResponse(AbstractModel):
    """ModifyRocketMQEnvironmentRole返回参数结构体

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


class ModifyRocketMQGroupRequest(AbstractModel):
    """ModifyRocketMQGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间
        :type NamespaceId: str
        :param _GroupId: 消费组名称
        :type GroupId: str
        :param _Remark: 说明信息，最长128个字符
        :type Remark: str
        :param _ReadEnable: 是否开启消费
        :type ReadEnable: bool
        :param _BroadcastEnable: 是否开启广播消费
        :type BroadcastEnable: bool
        :param _RetryMaxTimes: 最大重试次数
        :type RetryMaxTimes: int
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._Remark = None
        self._ReadEnable = None
        self._BroadcastEnable = None
        self._RetryMaxTimes = None

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
    def NamespaceId(self):
        """命名空间
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        """消费组名称
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Remark(self):
        """说明信息，最长128个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReadEnable(self):
        """是否开启消费
        :rtype: bool
        """
        return self._ReadEnable

    @ReadEnable.setter
    def ReadEnable(self, ReadEnable):
        self._ReadEnable = ReadEnable

    @property
    def BroadcastEnable(self):
        """是否开启广播消费
        :rtype: bool
        """
        return self._BroadcastEnable

    @BroadcastEnable.setter
    def BroadcastEnable(self, BroadcastEnable):
        self._BroadcastEnable = BroadcastEnable

    @property
    def RetryMaxTimes(self):
        """最大重试次数
        :rtype: int
        """
        return self._RetryMaxTimes

    @RetryMaxTimes.setter
    def RetryMaxTimes(self, RetryMaxTimes):
        self._RetryMaxTimes = RetryMaxTimes


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._Remark = params.get("Remark")
        self._ReadEnable = params.get("ReadEnable")
        self._BroadcastEnable = params.get("BroadcastEnable")
        self._RetryMaxTimes = params.get("RetryMaxTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQGroupResponse(AbstractModel):
    """ModifyRocketMQGroup返回参数结构体

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


class ModifyRocketMQInstanceRequest(AbstractModel):
    """ModifyRocketMQInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 专享实例ID
        :type InstanceId: str
        :param _Name: 实例名称
        :type Name: str
        :param _Remark: 实例备注信息
        :type Remark: str
        :param _MessageRetention: 实例消息保留时间，小时为单位
        :type MessageRetention: int
        """
        self._InstanceId = None
        self._Name = None
        self._Remark = None
        self._MessageRetention = None

    @property
    def InstanceId(self):
        """专享实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """实例备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageRetention(self):
        """实例消息保留时间，小时为单位
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._MessageRetention = params.get("MessageRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQInstanceResponse(AbstractModel):
    """ModifyRocketMQInstance返回参数结构体

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


class ModifyRocketMQInstanceSpecRequest(AbstractModel):
    """ModifyRocketMQInstanceSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 专享实例ID
        :type InstanceId: str
        :param _Specification: 实例规格，
rocket-vip-basic-1 基础型
rocket-vip-basic-2 标准型
rocket-vip-basic-3 高阶Ⅰ型
rocket-vip-basic-4 高阶Ⅱ型
        :type Specification: str
        :param _NodeCount: 节点数量
        :type NodeCount: int
        :param _StorageSize: 存储空间，GB为单位
        :type StorageSize: int
        """
        self._InstanceId = None
        self._Specification = None
        self._NodeCount = None
        self._StorageSize = None

    @property
    def InstanceId(self):
        """专享实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Specification(self):
        """实例规格，
rocket-vip-basic-1 基础型
rocket-vip-basic-2 标准型
rocket-vip-basic-3 高阶Ⅰ型
rocket-vip-basic-4 高阶Ⅱ型
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def NodeCount(self):
        """节点数量
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def StorageSize(self):
        """存储空间，GB为单位
        :rtype: int
        """
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Specification = params.get("Specification")
        self._NodeCount = params.get("NodeCount")
        self._StorageSize = params.get("StorageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQInstanceSpecResponse(AbstractModel):
    """ModifyRocketMQInstanceSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单号
        :type OrderId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._RequestId = None

    @property
    def OrderId(self):
        """订单号
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

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
        self._OrderId = params.get("OrderId")
        self._RequestId = params.get("RequestId")


class ModifyRocketMQNamespaceRequest(AbstractModel):
    """ModifyRocketMQNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type NamespaceId: str
        :param _Ttl: 已废弃
        :type Ttl: int
        :param _RetentionTime: 已废弃
        :type RetentionTime: int
        :param _Remark: 说明，最大128个字符
        :type Remark: str
        :param _PublicAccessEnabled: 是否开启公网访问
        :type PublicAccessEnabled: bool
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Ttl = None
        self._RetentionTime = None
        self._Remark = None
        self._PublicAccessEnabled = None

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
    def NamespaceId(self):
        """命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Ttl(self):
        """已废弃
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def RetentionTime(self):
        """已废弃
        :rtype: int
        """
        return self._RetentionTime

    @RetentionTime.setter
    def RetentionTime(self, RetentionTime):
        self._RetentionTime = RetentionTime

    @property
    def Remark(self):
        """说明，最大128个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicAccessEnabled(self):
        """是否开启公网访问
        :rtype: bool
        """
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Ttl = params.get("Ttl")
        self._RetentionTime = params.get("RetentionTime")
        self._Remark = params.get("Remark")
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQNamespaceResponse(AbstractModel):
    """ModifyRocketMQNamespace返回参数结构体

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


class ModifyRocketMQRoleRequest(AbstractModel):
    """ModifyRocketMQRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :type RoleName: str
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        :param _Remark: 备注说明，长度必须大等于0且小等于128。
        :type Remark: str
        :param _PermType: 权限类型，默认按集群授权（Cluster：集群级别；TopicAndGroup：主题&消费组级别）
        :type PermType: str
        """
        self._RoleName = None
        self._ClusterId = None
        self._Remark = None
        self._PermType = None

    @property
    def RoleName(self):
        """角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        """备注说明，长度必须大等于0且小等于128。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PermType(self):
        """权限类型，默认按集群授权（Cluster：集群级别；TopicAndGroup：主题&消费组级别）
        :rtype: str
        """
        return self._PermType

    @PermType.setter
    def PermType(self, PermType):
        self._PermType = PermType


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._PermType = params.get("PermType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQRoleResponse(AbstractModel):
    """ModifyRocketMQRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _Remark: 备注说明
        :type Remark: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleName = None
        self._Remark = None
        self._RequestId = None

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class ModifyRocketMQTopicRequest(AbstractModel):
    """ModifyRocketMQTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Remark: 说明信息，最大128个字符
        :type Remark: str
        :param _PartitionNum: 分区数，全局类型无效，不可小于当前分区数
        :type PartitionNum: int
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Topic = None
        self._Remark = None
        self._PartitionNum = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        """说明信息，最大128个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PartitionNum(self):
        """分区数，全局类型无效，不可小于当前分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        self._PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQTopicResponse(AbstractModel):
    """ModifyRocketMQTopic返回参数结构体

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


class ModifyRoleRequest(AbstractModel):
    """ModifyRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :type RoleName: str
        :param _ClusterId: 必填字段，集群Id
        :type ClusterId: str
        :param _Remark: 备注说明，长度必须大等于0且小等于128。
        :type Remark: str
        :param _EnvironmentRoleSets: 批量绑定名字空间信息
        :type EnvironmentRoleSets: list of EnvironmentRoleSet
        :param _UnbindAllEnvironment: 全部解绑名字空间，设置为 true
        :type UnbindAllEnvironment: bool
        """
        self._RoleName = None
        self._ClusterId = None
        self._Remark = None
        self._EnvironmentRoleSets = None
        self._UnbindAllEnvironment = None

    @property
    def RoleName(self):
        """角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def ClusterId(self):
        """必填字段，集群Id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        """备注说明，长度必须大等于0且小等于128。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def EnvironmentRoleSets(self):
        """批量绑定名字空间信息
        :rtype: list of EnvironmentRoleSet
        """
        return self._EnvironmentRoleSets

    @EnvironmentRoleSets.setter
    def EnvironmentRoleSets(self, EnvironmentRoleSets):
        self._EnvironmentRoleSets = EnvironmentRoleSets

    @property
    def UnbindAllEnvironment(self):
        """全部解绑名字空间，设置为 true
        :rtype: bool
        """
        return self._UnbindAllEnvironment

    @UnbindAllEnvironment.setter
    def UnbindAllEnvironment(self, UnbindAllEnvironment):
        self._UnbindAllEnvironment = UnbindAllEnvironment


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        if params.get("EnvironmentRoleSets") is not None:
            self._EnvironmentRoleSets = []
            for item in params.get("EnvironmentRoleSets"):
                obj = EnvironmentRoleSet()
                obj._deserialize(item)
                self._EnvironmentRoleSets.append(obj)
        self._UnbindAllEnvironment = params.get("UnbindAllEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoleResponse(AbstractModel):
    """ModifyRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _Remark: 备注说明
        :type Remark: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleName = None
        self._Remark = None
        self._RequestId = None

    @property
    def RoleName(self):
        """角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

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
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名。
        :type TopicName: str
        :param _Partitions: 分区数，必须大于或者等于原分区数，若想维持原分区数请输入原数目，修改分区数仅对非全局顺序消息起效果，不允许超过32个分区。
        :type Partitions: int
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param _Remark: 备注，128字符以内。
        :type Remark: str
        :param _MsgTTL: 未消费消息过期时间，单位：秒，取值范围：60秒~15天。

        :type MsgTTL: int
        :param _UnackPolicy: 不传默认是原生策略，DefaultPolicy表示当订阅下达到最大未确认消息数 5000 时，服务端将不再向当前订阅下的所有消费者推送消息，DynamicPolicy表示动态调整订阅下的最大未确认消息数，具体配额是在 5000 和消费者数量*20之间取最大值。每个消费者默认最大 unack 消息数为 20，超过该限制时仅影响该消费者，不影响其他消费者。
        :type UnackPolicy: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Partitions = None
        self._ClusterId = None
        self._Remark = None
        self._MsgTTL = None
        self._UnackPolicy = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partitions(self):
        """分区数，必须大于或者等于原分区数，若想维持原分区数请输入原数目，修改分区数仅对非全局顺序消息起效果，不允许超过32个分区。
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        """备注，128字符以内。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒，取值范围：60秒~15天。

        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def UnackPolicy(self):
        """不传默认是原生策略，DefaultPolicy表示当订阅下达到最大未确认消息数 5000 时，服务端将不再向当前订阅下的所有消费者推送消息，DynamicPolicy表示动态调整订阅下的最大未确认消息数，具体配额是在 5000 和消费者数量*20之间取最大值。每个消费者默认最大 unack 消息数为 20，超过该限制时仅影响该消费者，不影响其他消费者。
        :rtype: str
        """
        return self._UnackPolicy

    @UnackPolicy.setter
    def UnackPolicy(self, UnackPolicy):
        self._UnackPolicy = UnackPolicy


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Partitions = params.get("Partitions")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._MsgTTL = params.get("MsgTTL")
        self._UnackPolicy = params.get("UnackPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Partitions: 分区数
        :type Partitions: int
        :param _Remark: 备注，128字符以内。
        :type Remark: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Partitions = None
        self._Remark = None
        self._RequestId = None

    @property
    def Partitions(self):
        """分区数
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Remark(self):
        """备注，128字符以内。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

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
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class MsgLog(AbstractModel):
    """消息日志

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息ID。
        :type MsgId: str
        :param _ProducerName: 生产者名称。
        :type ProducerName: str
        :param _ProduceTime: 生产时间。
        :type ProduceTime: str
        :param _ProducerAddr: 生产客户端地址。
        :type ProducerAddr: str
        """
        self._MsgId = None
        self._ProducerName = None
        self._ProduceTime = None
        self._ProducerAddr = None

    @property
    def MsgId(self):
        """消息ID。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ProducerName(self):
        """生产者名称。
        :rtype: str
        """
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def ProduceTime(self):
        """生产时间。
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def ProducerAddr(self):
        """生产客户端地址。
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._ProducerName = params.get("ProducerName")
        self._ProduceTime = params.get("ProduceTime")
        self._ProducerAddr = params.get("ProducerAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionsTopic(AbstractModel):
    """分区topic

    """

    def __init__(self):
        r"""
        :param _AverageMsgSize: 最后一次间隔内发布消息的平均byte大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageMsgSize: str
        :param _ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerCount: str
        :param _LastConfirmedEntry: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastConfirmedEntry: str
        :param _LastLedgerCreatedTimestamp: 最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLedgerCreatedTimestamp: str
        :param _MsgRateIn: 本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: str
        :param _MsgRateOut: 本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateOut: str
        :param _MsgThroughputIn: 本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: str
        :param _MsgThroughputOut: 本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputOut: str
        :param _NumberOfEntries: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfEntries: str
        :param _Partitions: 子分区id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param _ProducerCount: 生产者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerCount: str
        :param _TotalSize: 以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: str
        :param _TopicType: topic类型描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicType: int
        """
        self._AverageMsgSize = None
        self._ConsumerCount = None
        self._LastConfirmedEntry = None
        self._LastLedgerCreatedTimestamp = None
        self._MsgRateIn = None
        self._MsgRateOut = None
        self._MsgThroughputIn = None
        self._MsgThroughputOut = None
        self._NumberOfEntries = None
        self._Partitions = None
        self._ProducerCount = None
        self._TotalSize = None
        self._TopicType = None

    @property
    def AverageMsgSize(self):
        """最后一次间隔内发布消息的平均byte大小。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AverageMsgSize

    @AverageMsgSize.setter
    def AverageMsgSize(self, AverageMsgSize):
        self._AverageMsgSize = AverageMsgSize

    @property
    def ConsumerCount(self):
        """消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerCount

    @ConsumerCount.setter
    def ConsumerCount(self, ConsumerCount):
        self._ConsumerCount = ConsumerCount

    @property
    def LastConfirmedEntry(self):
        """被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastConfirmedEntry

    @LastConfirmedEntry.setter
    def LastConfirmedEntry(self, LastConfirmedEntry):
        self._LastConfirmedEntry = LastConfirmedEntry

    @property
    def LastLedgerCreatedTimestamp(self):
        """最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastLedgerCreatedTimestamp

    @LastLedgerCreatedTimestamp.setter
    def LastLedgerCreatedTimestamp(self, LastLedgerCreatedTimestamp):
        self._LastLedgerCreatedTimestamp = LastLedgerCreatedTimestamp

    @property
    def MsgRateIn(self):
        """本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgRateOut(self):
        """本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputIn(self):
        """本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def MsgThroughputOut(self):
        """本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def NumberOfEntries(self):
        """被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NumberOfEntries

    @NumberOfEntries.setter
    def NumberOfEntries(self, NumberOfEntries):
        self._NumberOfEntries = NumberOfEntries

    @property
    def Partitions(self):
        """子分区id。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def ProducerCount(self):
        """生产者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProducerCount

    @ProducerCount.setter
    def ProducerCount(self, ProducerCount):
        self._ProducerCount = ProducerCount

    @property
    def TotalSize(self):
        """以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def TopicType(self):
        """topic类型描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType


    def _deserialize(self, params):
        self._AverageMsgSize = params.get("AverageMsgSize")
        self._ConsumerCount = params.get("ConsumerCount")
        self._LastConfirmedEntry = params.get("LastConfirmedEntry")
        self._LastLedgerCreatedTimestamp = params.get("LastLedgerCreatedTimestamp")
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._NumberOfEntries = params.get("NumberOfEntries")
        self._Partitions = params.get("Partitions")
        self._ProducerCount = params.get("ProducerCount")
        self._TotalSize = params.get("TotalSize")
        self._TopicType = params.get("TopicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProducerLog(AbstractModel):
    """消息生产信息

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息ID。
        :type MsgId: str
        :param _ProducerName: 生产者名称。
        :type ProducerName: str
        :param _ProduceTime: 消息生产时间。
        :type ProduceTime: str
        :param _ProducerAddr: 生产者客户端。
        :type ProducerAddr: str
        :param _ProduceUseTime: 生产耗时（秒）。
        :type ProduceUseTime: int
        :param _Status: 状态。
        :type Status: str
        """
        self._MsgId = None
        self._ProducerName = None
        self._ProduceTime = None
        self._ProducerAddr = None
        self._ProduceUseTime = None
        self._Status = None

    @property
    def MsgId(self):
        """消息ID。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ProducerName(self):
        """生产者名称。
        :rtype: str
        """
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def ProduceTime(self):
        """消息生产时间。
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def ProducerAddr(self):
        """生产者客户端。
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def ProduceUseTime(self):
        """生产耗时（秒）。
        :rtype: int
        """
        return self._ProduceUseTime

    @ProduceUseTime.setter
    def ProduceUseTime(self, ProduceUseTime):
        self._ProduceUseTime = ProduceUseTime

    @property
    def Status(self):
        """状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._ProducerName = params.get("ProducerName")
        self._ProduceTime = params.get("ProduceTime")
        self._ProducerAddr = params.get("ProducerAddr")
        self._ProduceUseTime = params.get("ProduceUseTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusEndpointInfo(AbstractModel):
    """rabbitmq Prometheus信息

    """

    def __init__(self):
        r"""
        :param _PrometheusEndpointStatus: Prometheus开关的状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrometheusEndpointStatus: str
        :param _VpcPrometheusEndpoint: prometheus信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcPrometheusEndpoint: list of str
        :param _NodePrometheusAddress: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePrometheusAddress: list of str
        :param _VpcEndpointInfo: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcEndpointInfo: :class:`tencentcloud.tdmq.v20200217.models.VpcEndpointInfo`
        """
        self._PrometheusEndpointStatus = None
        self._VpcPrometheusEndpoint = None
        self._NodePrometheusAddress = None
        self._VpcEndpointInfo = None

    @property
    def PrometheusEndpointStatus(self):
        """Prometheus开关的状态。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrometheusEndpointStatus

    @PrometheusEndpointStatus.setter
    def PrometheusEndpointStatus(self, PrometheusEndpointStatus):
        self._PrometheusEndpointStatus = PrometheusEndpointStatus

    @property
    def VpcPrometheusEndpoint(self):
        """prometheus信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._VpcPrometheusEndpoint

    @VpcPrometheusEndpoint.setter
    def VpcPrometheusEndpoint(self, VpcPrometheusEndpoint):
        self._VpcPrometheusEndpoint = VpcPrometheusEndpoint

    @property
    def NodePrometheusAddress(self):
        """节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._NodePrometheusAddress

    @NodePrometheusAddress.setter
    def NodePrometheusAddress(self, NodePrometheusAddress):
        self._NodePrometheusAddress = NodePrometheusAddress

    @property
    def VpcEndpointInfo(self):
        """vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.VpcEndpointInfo`
        """
        return self._VpcEndpointInfo

    @VpcEndpointInfo.setter
    def VpcEndpointInfo(self, VpcEndpointInfo):
        self._VpcEndpointInfo = VpcEndpointInfo


    def _deserialize(self, params):
        self._PrometheusEndpointStatus = params.get("PrometheusEndpointStatus")
        self._VpcPrometheusEndpoint = params.get("VpcPrometheusEndpoint")
        self._NodePrometheusAddress = params.get("NodePrometheusAddress")
        if params.get("VpcEndpointInfo") is not None:
            self._VpcEndpointInfo = VpcEndpointInfo()
            self._VpcEndpointInfo._deserialize(params.get("VpcEndpointInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicAccessRule(AbstractModel):
    """公网访问安全规则

    """

    def __init__(self):
        r"""
        :param _IpRule: ip网段信息
        :type IpRule: str
        :param _Allow: 允许或者拒绝
        :type Allow: bool
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._IpRule = None
        self._Allow = None
        self._Remark = None

    @property
    def IpRule(self):
        """ip网段信息
        :rtype: str
        """
        return self._IpRule

    @IpRule.setter
    def IpRule(self, IpRule):
        self._IpRule = IpRule

    @property
    def Allow(self):
        """允许或者拒绝
        :rtype: bool
        """
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def Remark(self):
        """备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._IpRule = params.get("IpRule")
        self._Allow = params.get("Allow")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCmqMsgRequest(AbstractModel):
    """PublishCmqMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名
        :type TopicName: str
        :param _MsgContent: 消息内容，消息总大小需不大于1024K
        :type MsgContent: str
        :param _MsgTag: 消息标签，支持传递多标签或单路由，单个标签、路由长度不能超过64个字符。
        :type MsgTag: list of str
        """
        self._TopicName = None
        self._MsgContent = None
        self._MsgTag = None

    @property
    def TopicName(self):
        """主题名
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgContent(self):
        """消息内容，消息总大小需不大于1024K
        :rtype: str
        """
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

    @property
    def MsgTag(self):
        """消息标签，支持传递多标签或单路由，单个标签、路由长度不能超过64个字符。
        :rtype: list of str
        """
        return self._MsgTag

    @MsgTag.setter
    def MsgTag(self, MsgTag):
        self._MsgTag = MsgTag


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MsgContent = params.get("MsgContent")
        self._MsgTag = params.get("MsgTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCmqMsgResponse(AbstractModel):
    """PublishCmqMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: true表示发送成功
        :type Result: bool
        :param _MsgId: 消息id
        :type MsgId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._MsgId = None
        self._RequestId = None

    @property
    def Result(self):
        """true表示发送成功
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

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
        self._Result = params.get("Result")
        self._MsgId = params.get("MsgId")
        self._RequestId = params.get("RequestId")


class Publisher(AbstractModel):
    """生产者信息

    """

    def __init__(self):
        r"""
        :param _ProducerId: 生产者id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerId: int
        :param _ProducerName: 生产者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerName: str
        :param _Address: 生产者地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _ClientVersion: 客户端版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientVersion: str
        :param _MsgRateIn: 消息生产速率（条/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: float
        :param _MsgThroughputIn: 消息生产吞吐速率（字节/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: float
        :param _AverageMsgSize: 平均消息大小（字节）
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageMsgSize: float
        :param _ConnectedSince: 连接时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectedSince: str
        :param _Partition: 生产者连接的主题分区号
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: int
        """
        self._ProducerId = None
        self._ProducerName = None
        self._Address = None
        self._ClientVersion = None
        self._MsgRateIn = None
        self._MsgThroughputIn = None
        self._AverageMsgSize = None
        self._ConnectedSince = None
        self._Partition = None

    @property
    def ProducerId(self):
        """生产者id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProducerId

    @ProducerId.setter
    def ProducerId(self, ProducerId):
        self._ProducerId = ProducerId

    @property
    def ProducerName(self):
        """生产者名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def Address(self):
        """生产者地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ClientVersion(self):
        """客户端版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientVersion

    @ClientVersion.setter
    def ClientVersion(self, ClientVersion):
        self._ClientVersion = ClientVersion

    @property
    def MsgRateIn(self):
        """消息生产速率（条/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgThroughputIn(self):
        """消息生产吞吐速率（字节/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def AverageMsgSize(self):
        """平均消息大小（字节）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._AverageMsgSize

    @AverageMsgSize.setter
    def AverageMsgSize(self, AverageMsgSize):
        self._AverageMsgSize = AverageMsgSize

    @property
    def ConnectedSince(self):
        """连接时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConnectedSince

    @ConnectedSince.setter
    def ConnectedSince(self, ConnectedSince):
        self._ConnectedSince = ConnectedSince

    @property
    def Partition(self):
        """生产者连接的主题分区号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._ProducerId = params.get("ProducerId")
        self._ProducerName = params.get("ProducerName")
        self._Address = params.get("Address")
        self._ClientVersion = params.get("ClientVersion")
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._AverageMsgSize = params.get("AverageMsgSize")
        self._ConnectedSince = params.get("ConnectedSince")
        self._Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarNetworkAccessPointInfo(AbstractModel):
    """Pulsar 网络接入点信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc的id，支撑网和公网接入点，该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网id，支撑网和公网接入点，该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Endpoint: 接入地址
        :type Endpoint: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _RouteType: 接入点类型：
0：支撑网接入点 
1：VPC接入点 
2：公网接入点
        :type RouteType: int
        :param _OperationType: 0：本地域访问，由于并没有配置跨地域容灾，所该类型的接入点，无法进行异地切换、异地访问切回；
1：本地域访问，由于配置了跨地域容灾，随时可以进行异地切换，该状态用于主集群的接入点
2：跨地域访问，已经完成了异地切换，该状态用于源集群的接入点，该状态下的接入点不可删除
3：跨地域访问，随时可以进行异地访问切回，该状态用于目标集群的接入点，该状态下的接入点不可删除
4:跨地域访问，目标集群已经完成异地切回，等待删除状态
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationType: int
        :param _AccessPointsType: 接入点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessPointsType: str
        :param _Bandwidth: 带宽，目前只有公网会有这个值
注意：此字段可能返回 null，表示取不到有效值。
        :type Bandwidth: int
        :param _SecurityPolicy: 类
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityPolicy: list of SecurityPolicy
        :param _StandardAccessPoint: 是否是标准的接入点 true是标准的 false不是标准的
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardAccessPoint: bool
        :param _ZoneName: 可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._Endpoint = None
        self._InstanceId = None
        self._RouteType = None
        self._OperationType = None
        self._AccessPointsType = None
        self._Bandwidth = None
        self._SecurityPolicy = None
        self._StandardAccessPoint = None
        self._ZoneName = None

    @property
    def VpcId(self):
        """vpc的id，支撑网和公网接入点，该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id，支撑网和公网接入点，该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Endpoint(self):
        """接入地址
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

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
    def RouteType(self):
        """接入点类型：
0：支撑网接入点 
1：VPC接入点 
2：公网接入点
        :rtype: int
        """
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def OperationType(self):
        """0：本地域访问，由于并没有配置跨地域容灾，所该类型的接入点，无法进行异地切换、异地访问切回；
1：本地域访问，由于配置了跨地域容灾，随时可以进行异地切换，该状态用于主集群的接入点
2：跨地域访问，已经完成了异地切换，该状态用于源集群的接入点，该状态下的接入点不可删除
3：跨地域访问，随时可以进行异地访问切回，该状态用于目标集群的接入点，该状态下的接入点不可删除
4:跨地域访问，目标集群已经完成异地切回，等待删除状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def AccessPointsType(self):
        """接入点类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessPointsType

    @AccessPointsType.setter
    def AccessPointsType(self, AccessPointsType):
        self._AccessPointsType = AccessPointsType

    @property
    def Bandwidth(self):
        """带宽，目前只有公网会有这个值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def SecurityPolicy(self):
        """类
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SecurityPolicy
        """
        return self._SecurityPolicy

    @SecurityPolicy.setter
    def SecurityPolicy(self, SecurityPolicy):
        self._SecurityPolicy = SecurityPolicy

    @property
    def StandardAccessPoint(self):
        """是否是标准的接入点 true是标准的 false不是标准的
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._StandardAccessPoint

    @StandardAccessPoint.setter
    def StandardAccessPoint(self, StandardAccessPoint):
        self._StandardAccessPoint = StandardAccessPoint

    @property
    def ZoneName(self):
        """可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Endpoint = params.get("Endpoint")
        self._InstanceId = params.get("InstanceId")
        self._RouteType = params.get("RouteType")
        self._OperationType = params.get("OperationType")
        self._AccessPointsType = params.get("AccessPointsType")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("SecurityPolicy") is not None:
            self._SecurityPolicy = []
            for item in params.get("SecurityPolicy"):
                obj = SecurityPolicy()
                obj._deserialize(item)
                self._SecurityPolicy.append(obj)
        self._StandardAccessPoint = params.get("StandardAccessPoint")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarProClusterInfo(AbstractModel):
    """Pulsar专业版集群信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群Id。
        :type ClusterId: str
        :param _ClusterName: 集群名称。
        :type ClusterName: str
        :param _Remark: 说明信息。
        :type Remark: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Status: 集群状态，0:创建中，1:正常，2:隔离
        :type Status: int
        :param _Version: 集群版本
        :type Version: str
        :param _NodeDistribution: 节点分布情况
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeDistribution: list of InstanceNodeDistribution
        :param _MaxStorage: 最大储存容量，单位：MB
        :type MaxStorage: int
        :param _CanEditRoute: 是否可以修改路由
注意：此字段可能返回 null，表示取不到有效值。
        :type CanEditRoute: bool
        :param _BillingLabelVersion: 代表是专业版和小规格专业版的不同计费规格PULSAR.P1固定存储PULSAR.P2弹性存储
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingLabelVersion: str
        :param _ExpireTime: 实例到期时间戳，毫秒级精度。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param _AutoCreateTopicStatus: 是否开启自动创建主题
true就是开启了，false是关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoCreateTopicStatus: bool
        :param _DefaultPartitionNumber: 自动创建主题的默认分区数，如果没开启就是0
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultPartitionNumber: int
        :param _Tenant: 用户自定义的租户别名，如果没有，会复用专业集群 ID

        :type Tenant: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None
        self._CreateTime = None
        self._Status = None
        self._Version = None
        self._NodeDistribution = None
        self._MaxStorage = None
        self._CanEditRoute = None
        self._BillingLabelVersion = None
        self._ExpireTime = None
        self._AutoCreateTopicStatus = None
        self._DefaultPartitionNumber = None
        self._Tenant = None

    @property
    def ClusterId(self):
        """集群Id。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """集群名称。
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        """说明信息。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

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
    def Status(self):
        """集群状态，0:创建中，1:正常，2:隔离
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        """集群版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def NodeDistribution(self):
        """节点分布情况
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNodeDistribution
        """
        return self._NodeDistribution

    @NodeDistribution.setter
    def NodeDistribution(self, NodeDistribution):
        self._NodeDistribution = NodeDistribution

    @property
    def MaxStorage(self):
        """最大储存容量，单位：MB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def CanEditRoute(self):
        """是否可以修改路由
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._CanEditRoute

    @CanEditRoute.setter
    def CanEditRoute(self, CanEditRoute):
        self._CanEditRoute = CanEditRoute

    @property
    def BillingLabelVersion(self):
        """代表是专业版和小规格专业版的不同计费规格PULSAR.P1固定存储PULSAR.P2弹性存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BillingLabelVersion

    @BillingLabelVersion.setter
    def BillingLabelVersion(self, BillingLabelVersion):
        self._BillingLabelVersion = BillingLabelVersion

    @property
    def ExpireTime(self):
        """实例到期时间戳，毫秒级精度。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoCreateTopicStatus(self):
        """是否开启自动创建主题
true就是开启了，false是关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoCreateTopicStatus

    @AutoCreateTopicStatus.setter
    def AutoCreateTopicStatus(self, AutoCreateTopicStatus):
        self._AutoCreateTopicStatus = AutoCreateTopicStatus

    @property
    def DefaultPartitionNumber(self):
        """自动创建主题的默认分区数，如果没开启就是0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DefaultPartitionNumber

    @DefaultPartitionNumber.setter
    def DefaultPartitionNumber(self, DefaultPartitionNumber):
        self._DefaultPartitionNumber = DefaultPartitionNumber

    @property
    def Tenant(self):
        """用户自定义的租户别名，如果没有，会复用专业集群 ID

        :rtype: str
        """
        return self._Tenant

    @Tenant.setter
    def Tenant(self, Tenant):
        self._Tenant = Tenant


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._Version = params.get("Version")
        if params.get("NodeDistribution") is not None:
            self._NodeDistribution = []
            for item in params.get("NodeDistribution"):
                obj = InstanceNodeDistribution()
                obj._deserialize(item)
                self._NodeDistribution.append(obj)
        self._MaxStorage = params.get("MaxStorage")
        self._CanEditRoute = params.get("CanEditRoute")
        self._BillingLabelVersion = params.get("BillingLabelVersion")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoCreateTopicStatus = params.get("AutoCreateTopicStatus")
        self._DefaultPartitionNumber = params.get("DefaultPartitionNumber")
        self._Tenant = params.get("Tenant")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarProClusterSpecInfo(AbstractModel):
    """Pulsar专业版集群规格信息

    """

    def __init__(self):
        r"""
        :param _SpecName: 集群规格名称
        :type SpecName: str
        :param _MaxTps: 峰值tps
        :type MaxTps: int
        :param _MaxBandWidth: 峰值带宽。单位：mbps
        :type MaxBandWidth: int
        :param _MaxNamespaces: 最大命名空间个数
        :type MaxNamespaces: int
        :param _MaxTopics: 最大主题分区数
        :type MaxTopics: int
        :param _ScalableTps: 规格外弹性TPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalableTps: int
        :param _MaxPartitions: 32或者128
当前集群topic的最大分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPartitions: int
        :param _MaxDelayedMessages: 商品最大延迟消息数量。0代表没有限制	
        :type MaxDelayedMessages: int
        """
        self._SpecName = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._MaxNamespaces = None
        self._MaxTopics = None
        self._ScalableTps = None
        self._MaxPartitions = None
        self._MaxDelayedMessages = None

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
    def MaxBandWidth(self):
        """峰值带宽。单位：mbps
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def MaxNamespaces(self):
        """最大命名空间个数
        :rtype: int
        """
        return self._MaxNamespaces

    @MaxNamespaces.setter
    def MaxNamespaces(self, MaxNamespaces):
        self._MaxNamespaces = MaxNamespaces

    @property
    def MaxTopics(self):
        """最大主题分区数
        :rtype: int
        """
        return self._MaxTopics

    @MaxTopics.setter
    def MaxTopics(self, MaxTopics):
        self._MaxTopics = MaxTopics

    @property
    def ScalableTps(self):
        """规格外弹性TPS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScalableTps

    @ScalableTps.setter
    def ScalableTps(self, ScalableTps):
        self._ScalableTps = ScalableTps

    @property
    def MaxPartitions(self):
        """32或者128
当前集群topic的最大分区数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxPartitions

    @MaxPartitions.setter
    def MaxPartitions(self, MaxPartitions):
        self._MaxPartitions = MaxPartitions

    @property
    def MaxDelayedMessages(self):
        """商品最大延迟消息数量。0代表没有限制	
        :rtype: int
        """
        return self._MaxDelayedMessages

    @MaxDelayedMessages.setter
    def MaxDelayedMessages(self, MaxDelayedMessages):
        self._MaxDelayedMessages = MaxDelayedMessages


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._MaxNamespaces = params.get("MaxNamespaces")
        self._MaxTopics = params.get("MaxTopics")
        self._ScalableTps = params.get("ScalableTps")
        self._MaxPartitions = params.get("MaxPartitions")
        self._MaxDelayedMessages = params.get("MaxDelayedMessages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarProInstance(AbstractModel):
    """Pulsar专业版实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceVersion: 实例版本
        :type InstanceVersion: str
        :param _Status: 实例状态，0-创建中，1-正常，2-隔离中，3-已销毁，4 - 异常, 5 - 发货失败，6-变配中，7-变配失败
        :type Status: int
        :param _ConfigDisplay: 实例配置规格名称
        :type ConfigDisplay: str
        :param _MaxTps: 峰值TPS
        :type MaxTps: int
        :param _MaxStorage: 存储容量，GB为单位
        :type MaxStorage: int
        :param _ExpireTime: 实例到期时间，毫秒为单位
        :type ExpireTime: int
        :param _AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type AutoRenewFlag: int
        :param _PayMode: 0-后付费，1-预付费
        :type PayMode: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _SpecName: 实例配置ID
        :type SpecName: str
        :param _ScalableTps: 规格外弹性TPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ScalableTps: int
        :param _VpcId: VPC的id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _MaxBandWidth: 峰值带宽。单位：mbps
        :type MaxBandWidth: int
        :param _Tags: 集群的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _BillingLabelVersion: 代表是专业版和小规格专业版的不同计费规格PULSAR.P1固定存储PULSAR.P2弹性存储
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingLabelVersion: str
        :param _Tenant: 自定义租户
        :type Tenant: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._ConfigDisplay = None
        self._MaxTps = None
        self._MaxStorage = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None
        self._ScalableTps = None
        self._VpcId = None
        self._SubnetId = None
        self._MaxBandWidth = None
        self._Tags = None
        self._CreateTime = None
        self._BillingLabelVersion = None
        self._Tenant = None

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
        """实例版本
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        """实例状态，0-创建中，1-正常，2-隔离中，3-已销毁，4 - 异常, 5 - 发货失败，6-变配中，7-变配失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ConfigDisplay(self):
        """实例配置规格名称
        :rtype: str
        """
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def MaxTps(self):
        """峰值TPS
        :rtype: int
        """
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxStorage(self):
        """存储容量，GB为单位
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def ExpireTime(self):
        """实例到期时间，毫秒为单位
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
        """备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        """实例配置ID
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def ScalableTps(self):
        """规格外弹性TPS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ScalableTps

    @ScalableTps.setter
    def ScalableTps(self, ScalableTps):
        self._ScalableTps = ScalableTps

    @property
    def VpcId(self):
        """VPC的id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MaxBandWidth(self):
        """峰值带宽。单位：mbps
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def Tags(self):
        """集群的标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        """集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BillingLabelVersion(self):
        """代表是专业版和小规格专业版的不同计费规格PULSAR.P1固定存储PULSAR.P2弹性存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BillingLabelVersion

    @BillingLabelVersion.setter
    def BillingLabelVersion(self, BillingLabelVersion):
        self._BillingLabelVersion = BillingLabelVersion

    @property
    def Tenant(self):
        """自定义租户
        :rtype: str
        """
        return self._Tenant

    @Tenant.setter
    def Tenant(self, Tenant):
        self._Tenant = Tenant


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._MaxTps = params.get("MaxTps")
        self._MaxStorage = params.get("MaxStorage")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        self._ScalableTps = params.get("ScalableTps")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MaxBandWidth = params.get("MaxBandWidth")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._BillingLabelVersion = params.get("BillingLabelVersion")
        self._Tenant = params.get("Tenant")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class RabbitMQClusterAccessInfo(AbstractModel):
    """RabbitMQ集群访问信息

    """

    def __init__(self):
        r"""
        :param _PublicAccessEndpoint: 集群公网接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccessEndpoint: str
        :param _WebConsoleEndpoint: 集群控制台访问地址
        :type WebConsoleEndpoint: str
        :param _WebConsoleUsername: 集群控制台登录用户名
        :type WebConsoleUsername: str
        :param _WebConsolePassword: 集群控制台登录密码
        :type WebConsolePassword: str
        :param _PublicAccessEndpointStatus: 已废弃
        :type PublicAccessEndpointStatus: bool
        :param _PublicControlConsoleSwitchStatus: 已废弃
        :type PublicControlConsoleSwitchStatus: bool
        :param _VpcControlConsoleSwitchStatus: 已废弃
        :type VpcControlConsoleSwitchStatus: bool
        :param _VpcWebConsoleEndpoint: Vpc管控台访问地址，示例值，http://1.1.1.1:15672
        :type VpcWebConsoleEndpoint: str
        :param _PublicWebConsoleSwitchStatus: 公网管控台开关状态，示例值，OFF/ON/CREATING/DELETING
        :type PublicWebConsoleSwitchStatus: str
        :param _VpcWebConsoleSwitchStatus: Vpc管控台开关状态，示例值，
OFF/ON/CREATING/DELETING
        :type VpcWebConsoleSwitchStatus: str
        :param _PublicDataStreamStatus: 公网管控台开关状态，示例值，OFF/ON/CREATING/DELETING
        :type PublicDataStreamStatus: str
        :param _PrometheusEndpointInfo: Prometheus信息
        :type PrometheusEndpointInfo: :class:`tencentcloud.tdmq.v20200217.models.PrometheusEndpointInfo`
        :param _WebConsoleDomainEndpoint: 公网域名接入点
        :type WebConsoleDomainEndpoint: str
        :param _ControlPlaneEndpointInfo: 控制面所使用的VPC信息
        :type ControlPlaneEndpointInfo: :class:`tencentcloud.tdmq.v20200217.models.VpcEndpointInfo`
        """
        self._PublicAccessEndpoint = None
        self._WebConsoleEndpoint = None
        self._WebConsoleUsername = None
        self._WebConsolePassword = None
        self._PublicAccessEndpointStatus = None
        self._PublicControlConsoleSwitchStatus = None
        self._VpcControlConsoleSwitchStatus = None
        self._VpcWebConsoleEndpoint = None
        self._PublicWebConsoleSwitchStatus = None
        self._VpcWebConsoleSwitchStatus = None
        self._PublicDataStreamStatus = None
        self._PrometheusEndpointInfo = None
        self._WebConsoleDomainEndpoint = None
        self._ControlPlaneEndpointInfo = None

    @property
    def PublicAccessEndpoint(self):
        """集群公网接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicAccessEndpoint

    @PublicAccessEndpoint.setter
    def PublicAccessEndpoint(self, PublicAccessEndpoint):
        self._PublicAccessEndpoint = PublicAccessEndpoint

    @property
    def WebConsoleEndpoint(self):
        """集群控制台访问地址
        :rtype: str
        """
        return self._WebConsoleEndpoint

    @WebConsoleEndpoint.setter
    def WebConsoleEndpoint(self, WebConsoleEndpoint):
        self._WebConsoleEndpoint = WebConsoleEndpoint

    @property
    def WebConsoleUsername(self):
        """集群控制台登录用户名
        :rtype: str
        """
        return self._WebConsoleUsername

    @WebConsoleUsername.setter
    def WebConsoleUsername(self, WebConsoleUsername):
        self._WebConsoleUsername = WebConsoleUsername

    @property
    def WebConsolePassword(self):
        """集群控制台登录密码
        :rtype: str
        """
        return self._WebConsolePassword

    @WebConsolePassword.setter
    def WebConsolePassword(self, WebConsolePassword):
        self._WebConsolePassword = WebConsolePassword

    @property
    def PublicAccessEndpointStatus(self):
        """已废弃
        :rtype: bool
        """
        return self._PublicAccessEndpointStatus

    @PublicAccessEndpointStatus.setter
    def PublicAccessEndpointStatus(self, PublicAccessEndpointStatus):
        self._PublicAccessEndpointStatus = PublicAccessEndpointStatus

    @property
    def PublicControlConsoleSwitchStatus(self):
        """已废弃
        :rtype: bool
        """
        return self._PublicControlConsoleSwitchStatus

    @PublicControlConsoleSwitchStatus.setter
    def PublicControlConsoleSwitchStatus(self, PublicControlConsoleSwitchStatus):
        self._PublicControlConsoleSwitchStatus = PublicControlConsoleSwitchStatus

    @property
    def VpcControlConsoleSwitchStatus(self):
        """已废弃
        :rtype: bool
        """
        return self._VpcControlConsoleSwitchStatus

    @VpcControlConsoleSwitchStatus.setter
    def VpcControlConsoleSwitchStatus(self, VpcControlConsoleSwitchStatus):
        self._VpcControlConsoleSwitchStatus = VpcControlConsoleSwitchStatus

    @property
    def VpcWebConsoleEndpoint(self):
        """Vpc管控台访问地址，示例值，http://1.1.1.1:15672
        :rtype: str
        """
        return self._VpcWebConsoleEndpoint

    @VpcWebConsoleEndpoint.setter
    def VpcWebConsoleEndpoint(self, VpcWebConsoleEndpoint):
        self._VpcWebConsoleEndpoint = VpcWebConsoleEndpoint

    @property
    def PublicWebConsoleSwitchStatus(self):
        """公网管控台开关状态，示例值，OFF/ON/CREATING/DELETING
        :rtype: str
        """
        return self._PublicWebConsoleSwitchStatus

    @PublicWebConsoleSwitchStatus.setter
    def PublicWebConsoleSwitchStatus(self, PublicWebConsoleSwitchStatus):
        self._PublicWebConsoleSwitchStatus = PublicWebConsoleSwitchStatus

    @property
    def VpcWebConsoleSwitchStatus(self):
        """Vpc管控台开关状态，示例值，
OFF/ON/CREATING/DELETING
        :rtype: str
        """
        return self._VpcWebConsoleSwitchStatus

    @VpcWebConsoleSwitchStatus.setter
    def VpcWebConsoleSwitchStatus(self, VpcWebConsoleSwitchStatus):
        self._VpcWebConsoleSwitchStatus = VpcWebConsoleSwitchStatus

    @property
    def PublicDataStreamStatus(self):
        """公网管控台开关状态，示例值，OFF/ON/CREATING/DELETING
        :rtype: str
        """
        return self._PublicDataStreamStatus

    @PublicDataStreamStatus.setter
    def PublicDataStreamStatus(self, PublicDataStreamStatus):
        self._PublicDataStreamStatus = PublicDataStreamStatus

    @property
    def PrometheusEndpointInfo(self):
        """Prometheus信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.PrometheusEndpointInfo`
        """
        return self._PrometheusEndpointInfo

    @PrometheusEndpointInfo.setter
    def PrometheusEndpointInfo(self, PrometheusEndpointInfo):
        self._PrometheusEndpointInfo = PrometheusEndpointInfo

    @property
    def WebConsoleDomainEndpoint(self):
        """公网域名接入点
        :rtype: str
        """
        return self._WebConsoleDomainEndpoint

    @WebConsoleDomainEndpoint.setter
    def WebConsoleDomainEndpoint(self, WebConsoleDomainEndpoint):
        self._WebConsoleDomainEndpoint = WebConsoleDomainEndpoint

    @property
    def ControlPlaneEndpointInfo(self):
        """控制面所使用的VPC信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.VpcEndpointInfo`
        """
        return self._ControlPlaneEndpointInfo

    @ControlPlaneEndpointInfo.setter
    def ControlPlaneEndpointInfo(self, ControlPlaneEndpointInfo):
        self._ControlPlaneEndpointInfo = ControlPlaneEndpointInfo


    def _deserialize(self, params):
        self._PublicAccessEndpoint = params.get("PublicAccessEndpoint")
        self._WebConsoleEndpoint = params.get("WebConsoleEndpoint")
        self._WebConsoleUsername = params.get("WebConsoleUsername")
        self._WebConsolePassword = params.get("WebConsolePassword")
        self._PublicAccessEndpointStatus = params.get("PublicAccessEndpointStatus")
        self._PublicControlConsoleSwitchStatus = params.get("PublicControlConsoleSwitchStatus")
        self._VpcControlConsoleSwitchStatus = params.get("VpcControlConsoleSwitchStatus")
        self._VpcWebConsoleEndpoint = params.get("VpcWebConsoleEndpoint")
        self._PublicWebConsoleSwitchStatus = params.get("PublicWebConsoleSwitchStatus")
        self._VpcWebConsoleSwitchStatus = params.get("VpcWebConsoleSwitchStatus")
        self._PublicDataStreamStatus = params.get("PublicDataStreamStatus")
        if params.get("PrometheusEndpointInfo") is not None:
            self._PrometheusEndpointInfo = PrometheusEndpointInfo()
            self._PrometheusEndpointInfo._deserialize(params.get("PrometheusEndpointInfo"))
        self._WebConsoleDomainEndpoint = params.get("WebConsoleDomainEndpoint")
        if params.get("ControlPlaneEndpointInfo") is not None:
            self._ControlPlaneEndpointInfo = VpcEndpointInfo()
            self._ControlPlaneEndpointInfo._deserialize(params.get("ControlPlaneEndpointInfo"))
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
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _InstanceType: 实例类型，0 专享版、1 Serverless 版
        :type InstanceType: int
        :param _IsolatedTime: 开始隔离时间
        :type IsolatedTime: int
        :param _Container: 是否为容器实例，默认 true
        :type Container: bool
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
        self._IsolatedTime = None
        self._Container = None

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
注意：此字段可能返回 null，表示取不到有效值。
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
        """实例类型，0 专享版、1 Serverless 版
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def IsolatedTime(self):
        """开始隔离时间
        :rtype: int
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def Container(self):
        """是否为容器实例，默认 true
        :rtype: bool
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container


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
        self._IsolatedTime = params.get("IsolatedTime")
        self._Container = params.get("Container")
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
        :param _NodeCount: 节点数量
        :type NodeCount: int
        :param _MaxTps: 峰值tps
        :type MaxTps: int
        :param _MaxBandWidth: 峰值带宽。单位：mbps
        :type MaxBandWidth: int
        :param _MaxStorage: 存储容量。单位：GB
        :type MaxStorage: int
        :param _PublicNetworkTps: 公网带宽tps。单位：Mbps
        :type PublicNetworkTps: int
        """
        self._SpecName = None
        self._NodeCount = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._MaxStorage = None
        self._PublicNetworkTps = None

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
    def NodeCount(self):
        """节点数量
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

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
    def MaxBandWidth(self):
        """峰值带宽。单位：mbps
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def MaxStorage(self):
        """存储容量。单位：GB
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def PublicNetworkTps(self):
        """公网带宽tps。单位：Mbps
        :rtype: int
        """
        return self._PublicNetworkTps

    @PublicNetworkTps.setter
    def PublicNetworkTps(self, PublicNetworkTps):
        self._PublicNetworkTps = PublicNetworkTps


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._NodeCount = params.get("NodeCount")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._MaxStorage = params.get("MaxStorage")
        self._PublicNetworkTps = params.get("PublicNetworkTps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQClusterWhiteListInfo(AbstractModel):
    """RabbiteMQ集群白名单信息

    """

    def __init__(self):
        r"""
        :param _WhiteList: 废弃
        :type WhiteList: str
        :param _PublicControlConsoleWhiteList: 公网管控台白名单
        :type PublicControlConsoleWhiteList: str
        :param _PublicDataStreamWhiteList: 公网数据流白名单
        :type PublicDataStreamWhiteList: str
        :param _PublicControlConsoleWhiteListStatus: 公网管控台白名单状态
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicControlConsoleWhiteListStatus: str
        :param _PublicDataStreamWhiteListStatus: 公网数据流白名单状态
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicDataStreamWhiteListStatus: str
        """
        self._WhiteList = None
        self._PublicControlConsoleWhiteList = None
        self._PublicDataStreamWhiteList = None
        self._PublicControlConsoleWhiteListStatus = None
        self._PublicDataStreamWhiteListStatus = None

    @property
    def WhiteList(self):
        """废弃
        :rtype: str
        """
        return self._WhiteList

    @WhiteList.setter
    def WhiteList(self, WhiteList):
        self._WhiteList = WhiteList

    @property
    def PublicControlConsoleWhiteList(self):
        """公网管控台白名单
        :rtype: str
        """
        return self._PublicControlConsoleWhiteList

    @PublicControlConsoleWhiteList.setter
    def PublicControlConsoleWhiteList(self, PublicControlConsoleWhiteList):
        self._PublicControlConsoleWhiteList = PublicControlConsoleWhiteList

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
    def PublicControlConsoleWhiteListStatus(self):
        """公网管控台白名单状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicControlConsoleWhiteListStatus

    @PublicControlConsoleWhiteListStatus.setter
    def PublicControlConsoleWhiteListStatus(self, PublicControlConsoleWhiteListStatus):
        self._PublicControlConsoleWhiteListStatus = PublicControlConsoleWhiteListStatus

    @property
    def PublicDataStreamWhiteListStatus(self):
        """公网数据流白名单状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicDataStreamWhiteListStatus

    @PublicDataStreamWhiteListStatus.setter
    def PublicDataStreamWhiteListStatus(self, PublicDataStreamWhiteListStatus):
        self._PublicDataStreamWhiteListStatus = PublicDataStreamWhiteListStatus


    def _deserialize(self, params):
        self._WhiteList = params.get("WhiteList")
        self._PublicControlConsoleWhiteList = params.get("PublicControlConsoleWhiteList")
        self._PublicDataStreamWhiteList = params.get("PublicDataStreamWhiteList")
        self._PublicControlConsoleWhiteListStatus = params.get("PublicControlConsoleWhiteListStatus")
        self._PublicDataStreamWhiteListStatus = params.get("PublicDataStreamWhiteListStatus")
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageRateIn: float
        :param _MessageRateOut: 输出消息速率
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: str
        :param _Arguments: 扩展参数 key-value 对象
        :type Arguments: str
        :param _MessagesDelayed: 未调度的延时消息数量
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        """输出消息速率
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
        


class RabbitMQPrivateNode(AbstractModel):
    """RabbitMQ节点信息

    """

    def __init__(self):
        r"""
        :param _NodeName: 节点名字
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _NodeStatus: 节点状态
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeStatus: str
        :param _CPUUsage: CPU使用率
注意：此字段可能返回 null，表示取不到有效值。
        :type CPUUsage: str
        :param _Memory: 内存使用情况，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _DiskUsage: 磁盘使用率
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskUsage: str
        :param _ProcessNumber: Rabbitmq的Erlang进程数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessNumber: int
        """
        self._NodeName = None
        self._NodeStatus = None
        self._CPUUsage = None
        self._Memory = None
        self._DiskUsage = None
        self._ProcessNumber = None

    @property
    def NodeName(self):
        """节点名字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def NodeStatus(self):
        """节点状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeStatus

    @NodeStatus.setter
    def NodeStatus(self, NodeStatus):
        self._NodeStatus = NodeStatus

    @property
    def CPUUsage(self):
        """CPU使用率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CPUUsage

    @CPUUsage.setter
    def CPUUsage(self, CPUUsage):
        self._CPUUsage = CPUUsage

    @property
    def Memory(self):
        """内存使用情况，单位MB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskUsage(self):
        """磁盘使用率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def ProcessNumber(self):
        """Rabbitmq的Erlang进程数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProcessNumber

    @ProcessNumber.setter
    def ProcessNumber(self, ProcessNumber):
        self._ProcessNumber = ProcessNumber


    def _deserialize(self, params):
        self._NodeName = params.get("NodeName")
        self._NodeStatus = params.get("NodeStatus")
        self._CPUUsage = params.get("CPUUsage")
        self._Memory = params.get("Memory")
        self._DiskUsage = params.get("DiskUsage")
        self._ProcessNumber = params.get("ProcessNumber")
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumersNumber: int
        """
        self._ConsumersNumber = None

    @property
    def ConsumersNumber(self):
        """消费者数量
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _ConsumerDetail: 消费者信息
        :type ConsumerDetail: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQQueueListConsumerDetailInfo`
        :param _QueueType: 队列类型，取值 "classic"，"quorum"
        :type QueueType: str
        :param _MessageHeapCount: 消息堆积数
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageHeapCount: int
        :param _MessageRateIn: 消息生产速率，每秒
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageRateIn: float
        :param _MessageRateOut: 消息消费速率，每秒
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsumerDetail(self):
        """消费者信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQQueueListConsumerDetailInfo`
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MessageHeapCount

    @MessageHeapCount.setter
    def MessageHeapCount(self, MessageHeapCount):
        self._MessageHeapCount = MessageHeapCount

    @property
    def MessageRateIn(self):
        """消息生产速率，每秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._MessageRateIn

    @MessageRateIn.setter
    def MessageRateIn(self, MessageRateIn):
        self._MessageRateIn = MessageRateIn

    @property
    def MessageRateOut(self):
        """消息消费速率，每秒
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _MaxConnections: 单个用户最大可用连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxConnections: int
        :param _MaxChannels: 单个用户最大可用通道数
注意：此字段可能返回 null，表示取不到有效值。
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
        """单个用户最大可用连接数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxConnections

    @MaxConnections.setter
    def MaxConnections(self, MaxConnections):
        self._MaxConnections = MaxConnections

    @property
    def MaxChannels(self):
        """单个用户最大可用通道数
注意：此字段可能返回 null，表示取不到有效值。
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
        


class RabbitMQVipInstance(AbstractModel):
    """RabbitMQ专享实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceVersion: 实例版本
        :type InstanceVersion: str
        :param _Status: 实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败
        :type Status: int
        :param _NodeCount: 节点数量
        :type NodeCount: int
        :param _ConfigDisplay: 实例配置规格名称
        :type ConfigDisplay: str
        :param _MaxTps: 峰值TPS
        :type MaxTps: int
        :param _MaxBandWidth: 峰值带宽，Mbps为单位
        :type MaxBandWidth: int
        :param _MaxStorage: 存储容量，GB为单位
        :type MaxStorage: int
        :param _ExpireTime: 实例到期时间，毫秒为单位
        :type ExpireTime: int
        :param _AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type AutoRenewFlag: int
        :param _PayMode: 0-后付费，1-预付费
        :type PayMode: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _SpecName: 实例配置ID
        :type SpecName: str
        :param _ExceptionInformation: 集群异常。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptionInformation: str
        :param _ClusterStatus: 实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败
为了和计费区分开，额外开启一个状态位，用于显示。
        :type ClusterStatus: int
        :param _PublicAccessEndpoint: 公网接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccessEndpoint: str
        :param _Vpcs: VPC 接入点列表
        :type Vpcs: list of VpcEndpointInfo
        :param _CreateTime: 创建时间，毫秒为单位
        :type CreateTime: int
        :param _InstanceType: 实例类型，0 专享版、1 Serverless 版
        :type InstanceType: int
        :param _IsolatedTime: 隔离时间，毫秒为单位
        :type IsolatedTime: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._NodeCount = None
        self._ConfigDisplay = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._MaxStorage = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None
        self._ExceptionInformation = None
        self._ClusterStatus = None
        self._PublicAccessEndpoint = None
        self._Vpcs = None
        self._CreateTime = None
        self._InstanceType = None
        self._IsolatedTime = None

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
        """实例版本
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
    def NodeCount(self):
        """节点数量
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def ConfigDisplay(self):
        """实例配置规格名称
        :rtype: str
        """
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def MaxTps(self):
        """峰值TPS
        :rtype: int
        """
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxBandWidth(self):
        """峰值带宽，Mbps为单位
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def MaxStorage(self):
        """存储容量，GB为单位
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def ExpireTime(self):
        """实例到期时间，毫秒为单位
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
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        """实例配置ID
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def ExceptionInformation(self):
        """集群异常。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExceptionInformation

    @ExceptionInformation.setter
    def ExceptionInformation(self, ExceptionInformation):
        self._ExceptionInformation = ExceptionInformation

    @property
    def ClusterStatus(self):
        """实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败
为了和计费区分开，额外开启一个状态位，用于显示。
        :rtype: int
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def PublicAccessEndpoint(self):
        """公网接入点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicAccessEndpoint

    @PublicAccessEndpoint.setter
    def PublicAccessEndpoint(self, PublicAccessEndpoint):
        self._PublicAccessEndpoint = PublicAccessEndpoint

    @property
    def Vpcs(self):
        """VPC 接入点列表
        :rtype: list of VpcEndpointInfo
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

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
    def InstanceType(self):
        """实例类型，0 专享版、1 Serverless 版
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def IsolatedTime(self):
        """隔离时间，毫秒为单位
        :rtype: int
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._NodeCount = params.get("NodeCount")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._MaxStorage = params.get("MaxStorage")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        self._ExceptionInformation = params.get("ExceptionInformation")
        self._ClusterStatus = params.get("ClusterStatus")
        self._PublicAccessEndpoint = params.get("PublicAccessEndpoint")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcEndpointInfo()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._InstanceType = params.get("InstanceType")
        self._IsolatedTime = params.get("IsolatedTime")
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
        :type VirtualHostStatistics: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQVirtualHostStatistics`
        :param _TraceFlag: 消息轨迹开关,true打开,false关闭
        :type TraceFlag: bool
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
        self._TraceFlag = None
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
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RabbitMQVirtualHostStatistics`
        """
        return self._VirtualHostStatistics

    @VirtualHostStatistics.setter
    def VirtualHostStatistics(self, VirtualHostStatistics):
        self._VirtualHostStatistics = VirtualHostStatistics

    @property
    def TraceFlag(self):
        """消息轨迹开关,true打开,false关闭
        :rtype: bool
        """
        return self._TraceFlag

    @TraceFlag.setter
    def TraceFlag(self, TraceFlag):
        self._TraceFlag = TraceFlag

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
        self._TraceFlag = params.get("TraceFlag")
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
        


class ReceiveMessageRequest(AbstractModel):
    """ReceiveMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: 接收消息的topic的名字, 这里尽量需要使用topic的全路径，如果不指定，即：tenant/namespace/topic。默认使用的是：public/default
        :type Topic: str
        :param _SubscriptionName: 订阅者的名字
        :type SubscriptionName: str
        :param _ReceiverQueueSize: 默认值为1000，consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
        :type ReceiverQueueSize: int
        :param _SubInitialPosition: 默认值为：Earliest。用作判定consumer初始接收消息的位置，可选参数为：Earliest, Latest
        :type SubInitialPosition: str
        :param _MaxNumMessages: 用于设置BatchReceivePolicy，指在一次batch中最多接收多少条消息，默认是 0。即不开启BatchReceivePolicy
        :type MaxNumMessages: int
        :param _MaxNumBytes: 用于设置BatchReceivePolicy，指在一次batch中最多接收的消息体有多大，单位是 bytes。默认是 0，即不开启BatchReceivePolicy
        :type MaxNumBytes: int
        :param _Timeout: 用于设置BatchReceivePolicy，指在一次batch消息的接收z中最多等待的超时时间，单位是毫秒。默认是 0，即不开启BatchReceivePolicy
        :type Timeout: int
        """
        self._Topic = None
        self._SubscriptionName = None
        self._ReceiverQueueSize = None
        self._SubInitialPosition = None
        self._MaxNumMessages = None
        self._MaxNumBytes = None
        self._Timeout = None

    @property
    def Topic(self):
        """接收消息的topic的名字, 这里尽量需要使用topic的全路径，如果不指定，即：tenant/namespace/topic。默认使用的是：public/default
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def SubscriptionName(self):
        """订阅者的名字
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def ReceiverQueueSize(self):
        """默认值为1000，consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
        :rtype: int
        """
        return self._ReceiverQueueSize

    @ReceiverQueueSize.setter
    def ReceiverQueueSize(self, ReceiverQueueSize):
        self._ReceiverQueueSize = ReceiverQueueSize

    @property
    def SubInitialPosition(self):
        """默认值为：Earliest。用作判定consumer初始接收消息的位置，可选参数为：Earliest, Latest
        :rtype: str
        """
        return self._SubInitialPosition

    @SubInitialPosition.setter
    def SubInitialPosition(self, SubInitialPosition):
        self._SubInitialPosition = SubInitialPosition

    @property
    def MaxNumMessages(self):
        """用于设置BatchReceivePolicy，指在一次batch中最多接收多少条消息，默认是 0。即不开启BatchReceivePolicy
        :rtype: int
        """
        return self._MaxNumMessages

    @MaxNumMessages.setter
    def MaxNumMessages(self, MaxNumMessages):
        self._MaxNumMessages = MaxNumMessages

    @property
    def MaxNumBytes(self):
        """用于设置BatchReceivePolicy，指在一次batch中最多接收的消息体有多大，单位是 bytes。默认是 0，即不开启BatchReceivePolicy
        :rtype: int
        """
        return self._MaxNumBytes

    @MaxNumBytes.setter
    def MaxNumBytes(self, MaxNumBytes):
        self._MaxNumBytes = MaxNumBytes

    @property
    def Timeout(self):
        """用于设置BatchReceivePolicy，指在一次batch消息的接收z中最多等待的超时时间，单位是毫秒。默认是 0，即不开启BatchReceivePolicy
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._SubscriptionName = params.get("SubscriptionName")
        self._ReceiverQueueSize = params.get("ReceiverQueueSize")
        self._SubInitialPosition = params.get("SubInitialPosition")
        self._MaxNumMessages = params.get("MaxNumMessages")
        self._MaxNumBytes = params.get("MaxNumBytes")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveMessageResponse(AbstractModel):
    """ReceiveMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageID: 用作标识消息的唯一主键
        :type MessageID: str
        :param _MessagePayload: 接收消息的内容
        :type MessagePayload: str
        :param _AckTopic: 提供给 Ack 接口，用来Ack哪一个topic中的消息
        :type AckTopic: str
        :param _ErrorMsg: 返回的错误信息，如果为空，说明没有错误
        :type ErrorMsg: str
        :param _SubName: 返回订阅者的名字，用来创建 ack consumer时使用
        :type SubName: str
        :param _MessageIDList: BatchReceivePolicy 一次性返回的多条消息的 MessageID，用 ‘###’ 来区分不同的 MessageID
        :type MessageIDList: str
        :param _MessagesPayload: BatchReceivePolicy 一次性返回的多条消息的消息内容，用 ‘###’ 来区分不同的消息内容
        :type MessagesPayload: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageID = None
        self._MessagePayload = None
        self._AckTopic = None
        self._ErrorMsg = None
        self._SubName = None
        self._MessageIDList = None
        self._MessagesPayload = None
        self._RequestId = None

    @property
    def MessageID(self):
        """用作标识消息的唯一主键
        :rtype: str
        """
        return self._MessageID

    @MessageID.setter
    def MessageID(self, MessageID):
        self._MessageID = MessageID

    @property
    def MessagePayload(self):
        """接收消息的内容
        :rtype: str
        """
        return self._MessagePayload

    @MessagePayload.setter
    def MessagePayload(self, MessagePayload):
        self._MessagePayload = MessagePayload

    @property
    def AckTopic(self):
        """提供给 Ack 接口，用来Ack哪一个topic中的消息
        :rtype: str
        """
        return self._AckTopic

    @AckTopic.setter
    def AckTopic(self, AckTopic):
        self._AckTopic = AckTopic

    @property
    def ErrorMsg(self):
        """返回的错误信息，如果为空，说明没有错误
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def SubName(self):
        """返回订阅者的名字，用来创建 ack consumer时使用
        :rtype: str
        """
        return self._SubName

    @SubName.setter
    def SubName(self, SubName):
        self._SubName = SubName

    @property
    def MessageIDList(self):
        """BatchReceivePolicy 一次性返回的多条消息的 MessageID，用 ‘###’ 来区分不同的 MessageID
        :rtype: str
        """
        return self._MessageIDList

    @MessageIDList.setter
    def MessageIDList(self, MessageIDList):
        self._MessageIDList = MessageIDList

    @property
    def MessagesPayload(self):
        """BatchReceivePolicy 一次性返回的多条消息的消息内容，用 ‘###’ 来区分不同的消息内容
        :rtype: str
        """
        return self._MessagesPayload

    @MessagesPayload.setter
    def MessagesPayload(self, MessagesPayload):
        self._MessagesPayload = MessagesPayload

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
        self._MessageID = params.get("MessageID")
        self._MessagePayload = params.get("MessagePayload")
        self._AckTopic = params.get("AckTopic")
        self._ErrorMsg = params.get("ErrorMsg")
        self._SubName = params.get("SubName")
        self._MessageIDList = params.get("MessageIDList")
        self._MessagesPayload = params.get("MessagesPayload")
        self._RequestId = params.get("RequestId")


class ResetMsgSubOffsetByTimestampRequest(AbstractModel):
    """ResetMsgSubOffsetByTimestamp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 命名空间名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名称。
        :type TopicName: str
        :param _Subscription: 订阅者名称。
        :type Subscription: str
        :param _ToTimestamp: 时间戳，精确到毫秒。
        :type ToTimestamp: int
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Subscription = None
        self._ToTimestamp = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """命名空间名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Subscription(self):
        """订阅者名称。
        :rtype: str
        """
        return self._Subscription

    @Subscription.setter
    def Subscription(self, Subscription):
        self._Subscription = Subscription

    @property
    def ToTimestamp(self):
        """时间戳，精确到毫秒。
        :rtype: int
        """
        return self._ToTimestamp

    @ToTimestamp.setter
    def ToTimestamp(self, ToTimestamp):
        self._ToTimestamp = ToTimestamp

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Subscription = params.get("Subscription")
        self._ToTimestamp = params.get("ToTimestamp")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetMsgSubOffsetByTimestampResponse(AbstractModel):
    """ResetMsgSubOffsetByTimestamp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ResetRocketMQConsumerOffSetRequest(AbstractModel):
    """ResetRocketMQConsumerOffSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _GroupId: 消费组名称
        :type GroupId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Type: 重置方式，0表示从最新位点开始，1表示从指定时间点开始
        :type Type: int
        :param _ResetTimestamp: 重置指定的时间戳，仅在 Type 为1是生效，以毫秒为单位
        :type ResetTimestamp: int
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._Topic = None
        self._Type = None
        self._ResetTimestamp = None

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
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        """消费组名称
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Type(self):
        """重置方式，0表示从最新位点开始，1表示从指定时间点开始
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResetTimestamp(self):
        """重置指定的时间戳，仅在 Type 为1是生效，以毫秒为单位
        :rtype: int
        """
        return self._ResetTimestamp

    @ResetTimestamp.setter
    def ResetTimestamp(self, ResetTimestamp):
        self._ResetTimestamp = ResetTimestamp


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._Topic = params.get("Topic")
        self._Type = params.get("Type")
        self._ResetTimestamp = params.get("ResetTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRocketMQConsumerOffSetResponse(AbstractModel):
    """ResetRocketMQConsumerOffSet返回参数结构体

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


class RetentionPolicy(AbstractModel):
    """消息保留策略

    """

    def __init__(self):
        r"""
        :param _TimeInMinutes: 消息保留时长
        :type TimeInMinutes: int
        :param _SizeInMB: 消息保留大小
        :type SizeInMB: int
        """
        self._TimeInMinutes = None
        self._SizeInMB = None

    @property
    def TimeInMinutes(self):
        """消息保留时长
        :rtype: int
        """
        return self._TimeInMinutes

    @TimeInMinutes.setter
    def TimeInMinutes(self, TimeInMinutes):
        self._TimeInMinutes = TimeInMinutes

    @property
    def SizeInMB(self):
        """消息保留大小
        :rtype: int
        """
        return self._SizeInMB

    @SizeInMB.setter
    def SizeInMB(self, SizeInMB):
        self._SizeInMB = SizeInMB


    def _deserialize(self, params):
        self._TimeInMinutes = params.get("TimeInMinutes")
        self._SizeInMB = params.get("SizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRocketMQDlqMessageRequest(AbstractModel):
    """RetryRocketMQDlqMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param _GroupName: group名称
        :type GroupName: str
        :param _MessageIds: 死信消息ID
        :type MessageIds: list of str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupName = None
        self._MessageIds = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        """命名空间名称
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupName(self):
        """group名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MessageIds(self):
        """死信消息ID
        :rtype: list of str
        """
        return self._MessageIds

    @MessageIds.setter
    def MessageIds(self, MessageIds):
        self._MessageIds = MessageIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupName = params.get("GroupName")
        self._MessageIds = params.get("MessageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRocketMQDlqMessageResponse(AbstractModel):
    """RetryRocketMQDlqMessage返回参数结构体

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


class RewindCmqQueueRequest(AbstractModel):
    """RewindCmqQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名字，在单个地域同一账号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        :param _StartConsumeTime: 设定该时间，则（Batch）receiveMessage接口，会按照生产消息的先后顺序消费该时间戳以后的消息。
        :type StartConsumeTime: int
        """
        self._QueueName = None
        self._StartConsumeTime = None

    @property
    def QueueName(self):
        """队列名字，在单个地域同一账号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :rtype: str
        """
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def StartConsumeTime(self):
        """设定该时间，则（Batch）receiveMessage接口，会按照生产消息的先后顺序消费该时间戳以后的消息。
        :rtype: int
        """
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
        


class RewindCmqQueueResponse(AbstractModel):
    """RewindCmqQueue返回参数结构体

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


class RocketMQClusterConfig(AbstractModel):
    """RocketMQ集群配置

    """

    def __init__(self):
        r"""
        :param _MaxTpsPerNamespace: 单命名空间TPS上限
        :type MaxTpsPerNamespace: int
        :param _MaxNamespaceNum: 最大命名空间数量
        :type MaxNamespaceNum: int
        :param _UsedNamespaceNum: 已使用命名空间数量
        :type UsedNamespaceNum: int
        :param _MaxTopicNum: 最大Topic数量
        :type MaxTopicNum: int
        :param _UsedTopicNum: 已使用Topic数量
        :type UsedTopicNum: int
        :param _MaxGroupNum: 最大Group数量
        :type MaxGroupNum: int
        :param _UsedGroupNum: 已使用Group数量
        :type UsedGroupNum: int
        :param _MaxRetentionTime: 消息最大保留时间，以毫秒为单位
        :type MaxRetentionTime: int
        :param _MaxLatencyTime: 消息最长延时，以毫秒为单位
        :type MaxLatencyTime: int
        :param _MaxQueuesPerTopic: 单个主题最大队列数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxQueuesPerTopic: int
        :param _TopicDistribution: topic分布
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicDistribution: list of RocketMQTopicDistribution
        """
        self._MaxTpsPerNamespace = None
        self._MaxNamespaceNum = None
        self._UsedNamespaceNum = None
        self._MaxTopicNum = None
        self._UsedTopicNum = None
        self._MaxGroupNum = None
        self._UsedGroupNum = None
        self._MaxRetentionTime = None
        self._MaxLatencyTime = None
        self._MaxQueuesPerTopic = None
        self._TopicDistribution = None

    @property
    def MaxTpsPerNamespace(self):
        warnings.warn("parameter `MaxTpsPerNamespace` is deprecated", DeprecationWarning) 

        """单命名空间TPS上限
        :rtype: int
        """
        return self._MaxTpsPerNamespace

    @MaxTpsPerNamespace.setter
    def MaxTpsPerNamespace(self, MaxTpsPerNamespace):
        warnings.warn("parameter `MaxTpsPerNamespace` is deprecated", DeprecationWarning) 

        self._MaxTpsPerNamespace = MaxTpsPerNamespace

    @property
    def MaxNamespaceNum(self):
        """最大命名空间数量
        :rtype: int
        """
        return self._MaxNamespaceNum

    @MaxNamespaceNum.setter
    def MaxNamespaceNum(self, MaxNamespaceNum):
        self._MaxNamespaceNum = MaxNamespaceNum

    @property
    def UsedNamespaceNum(self):
        """已使用命名空间数量
        :rtype: int
        """
        return self._UsedNamespaceNum

    @UsedNamespaceNum.setter
    def UsedNamespaceNum(self, UsedNamespaceNum):
        self._UsedNamespaceNum = UsedNamespaceNum

    @property
    def MaxTopicNum(self):
        """最大Topic数量
        :rtype: int
        """
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def UsedTopicNum(self):
        """已使用Topic数量
        :rtype: int
        """
        return self._UsedTopicNum

    @UsedTopicNum.setter
    def UsedTopicNum(self, UsedTopicNum):
        self._UsedTopicNum = UsedTopicNum

    @property
    def MaxGroupNum(self):
        """最大Group数量
        :rtype: int
        """
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def UsedGroupNum(self):
        """已使用Group数量
        :rtype: int
        """
        return self._UsedGroupNum

    @UsedGroupNum.setter
    def UsedGroupNum(self, UsedGroupNum):
        self._UsedGroupNum = UsedGroupNum

    @property
    def MaxRetentionTime(self):
        """消息最大保留时间，以毫秒为单位
        :rtype: int
        """
        return self._MaxRetentionTime

    @MaxRetentionTime.setter
    def MaxRetentionTime(self, MaxRetentionTime):
        self._MaxRetentionTime = MaxRetentionTime

    @property
    def MaxLatencyTime(self):
        """消息最长延时，以毫秒为单位
        :rtype: int
        """
        return self._MaxLatencyTime

    @MaxLatencyTime.setter
    def MaxLatencyTime(self, MaxLatencyTime):
        self._MaxLatencyTime = MaxLatencyTime

    @property
    def MaxQueuesPerTopic(self):
        """单个主题最大队列数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxQueuesPerTopic

    @MaxQueuesPerTopic.setter
    def MaxQueuesPerTopic(self, MaxQueuesPerTopic):
        self._MaxQueuesPerTopic = MaxQueuesPerTopic

    @property
    def TopicDistribution(self):
        """topic分布
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQTopicDistribution
        """
        return self._TopicDistribution

    @TopicDistribution.setter
    def TopicDistribution(self, TopicDistribution):
        self._TopicDistribution = TopicDistribution


    def _deserialize(self, params):
        self._MaxTpsPerNamespace = params.get("MaxTpsPerNamespace")
        self._MaxNamespaceNum = params.get("MaxNamespaceNum")
        self._UsedNamespaceNum = params.get("UsedNamespaceNum")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._UsedTopicNum = params.get("UsedTopicNum")
        self._MaxGroupNum = params.get("MaxGroupNum")
        self._UsedGroupNum = params.get("UsedGroupNum")
        self._MaxRetentionTime = params.get("MaxRetentionTime")
        self._MaxLatencyTime = params.get("MaxLatencyTime")
        self._MaxQueuesPerTopic = params.get("MaxQueuesPerTopic")
        if params.get("TopicDistribution") is not None:
            self._TopicDistribution = []
            for item in params.get("TopicDistribution"):
                obj = RocketMQTopicDistribution()
                obj._deserialize(item)
                self._TopicDistribution.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterDetail(AbstractModel):
    """租户RocketMQ集群详细信息

    """

    def __init__(self):
        r"""
        :param _Info: 集群基本信息
        :type Info: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param _Config: 集群配置信息
        :type Config: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        :param _Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._Info = None
        self._Config = None
        self._Status = None

    @property
    def Info(self):
        """集群基本信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Config(self):
        """集群配置信息
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        """集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = RocketMQClusterInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("Config") is not None:
            self._Config = RocketMQClusterConfig()
            self._Config._deserialize(params.get("Config"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterInfo(AbstractModel):
    """RocketMQ集群基本信息

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
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _PublicEndPoint: 公网接入地址
        :type PublicEndPoint: str
        :param _VpcEndPoint: VPC接入地址
        :type VpcEndPoint: str
        :param _SupportNamespaceEndpoint: 是否支持命名空间接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportNamespaceEndpoint: bool
        :param _Vpcs: VPC信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Vpcs: list of VpcConfig
        :param _IsVip: 是否为专享实例
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param _RocketMQFlag: Rocketmq集群标识
注意：此字段可能返回 null，表示取不到有效值。
        :type RocketMQFlag: bool
        :param _Status: 计费状态，1表示正常，2表示已停服，3表示已销毁
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _IsolateTime: 欠费停服时间，毫秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: int
        :param _HttpPublicEndpoint: HTTP协议公网接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpPublicEndpoint: str
        :param _HttpVpcEndpoint: HTTP协议VPC接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpVpcEndpoint: str
        :param _InternalEndpoint: TCP内部接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalEndpoint: str
        :param _HttpInternalEndpoint: HTTP协议内部接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpInternalEndpoint: str
        :param _AclEnabled: 是否开启ACL鉴权，专享实例支持关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type AclEnabled: bool
        :param _PublicClbId: 公网CLB实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicClbId: str
        :param _Vip: vip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _VpcId: 所属VPC
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SupportMigration: 是否支持迁移
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportMigration: bool
        :param _InstanceStatus: 实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败，6 - 变配中，7 - 变配失败
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatus: int
        :param _ZoneId: 集群所属可用区，表明集群归属的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _ZoneIds: 集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._CreateTime = None
        self._Remark = None
        self._PublicEndPoint = None
        self._VpcEndPoint = None
        self._SupportNamespaceEndpoint = None
        self._Vpcs = None
        self._IsVip = None
        self._RocketMQFlag = None
        self._Status = None
        self._IsolateTime = None
        self._HttpPublicEndpoint = None
        self._HttpVpcEndpoint = None
        self._InternalEndpoint = None
        self._HttpInternalEndpoint = None
        self._AclEnabled = None
        self._PublicClbId = None
        self._Vip = None
        self._VpcId = None
        self._SupportMigration = None
        self._InstanceStatus = None
        self._ZoneId = None
        self._ZoneIds = None

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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicEndPoint(self):
        """公网接入地址
        :rtype: str
        """
        return self._PublicEndPoint

    @PublicEndPoint.setter
    def PublicEndPoint(self, PublicEndPoint):
        self._PublicEndPoint = PublicEndPoint

    @property
    def VpcEndPoint(self):
        """VPC接入地址
        :rtype: str
        """
        return self._VpcEndPoint

    @VpcEndPoint.setter
    def VpcEndPoint(self, VpcEndPoint):
        self._VpcEndPoint = VpcEndPoint

    @property
    def SupportNamespaceEndpoint(self):
        """是否支持命名空间接入点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SupportNamespaceEndpoint

    @SupportNamespaceEndpoint.setter
    def SupportNamespaceEndpoint(self, SupportNamespaceEndpoint):
        self._SupportNamespaceEndpoint = SupportNamespaceEndpoint

    @property
    def Vpcs(self):
        """VPC信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VpcConfig
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def IsVip(self):
        """是否为专享实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def RocketMQFlag(self):
        """Rocketmq集群标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._RocketMQFlag

    @RocketMQFlag.setter
    def RocketMQFlag(self, RocketMQFlag):
        self._RocketMQFlag = RocketMQFlag

    @property
    def Status(self):
        """计费状态，1表示正常，2表示已停服，3表示已销毁
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsolateTime(self):
        """欠费停服时间，毫秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def HttpPublicEndpoint(self):
        """HTTP协议公网接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HttpPublicEndpoint

    @HttpPublicEndpoint.setter
    def HttpPublicEndpoint(self, HttpPublicEndpoint):
        self._HttpPublicEndpoint = HttpPublicEndpoint

    @property
    def HttpVpcEndpoint(self):
        """HTTP协议VPC接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HttpVpcEndpoint

    @HttpVpcEndpoint.setter
    def HttpVpcEndpoint(self, HttpVpcEndpoint):
        self._HttpVpcEndpoint = HttpVpcEndpoint

    @property
    def InternalEndpoint(self):
        """TCP内部接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InternalEndpoint

    @InternalEndpoint.setter
    def InternalEndpoint(self, InternalEndpoint):
        self._InternalEndpoint = InternalEndpoint

    @property
    def HttpInternalEndpoint(self):
        """HTTP协议内部接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HttpInternalEndpoint

    @HttpInternalEndpoint.setter
    def HttpInternalEndpoint(self, HttpInternalEndpoint):
        self._HttpInternalEndpoint = HttpInternalEndpoint

    @property
    def AclEnabled(self):
        """是否开启ACL鉴权，专享实例支持关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AclEnabled

    @AclEnabled.setter
    def AclEnabled(self, AclEnabled):
        self._AclEnabled = AclEnabled

    @property
    def PublicClbId(self):
        """公网CLB实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicClbId

    @PublicClbId.setter
    def PublicClbId(self, PublicClbId):
        self._PublicClbId = PublicClbId

    @property
    def Vip(self):
        """vip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VpcId(self):
        """所属VPC
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SupportMigration(self):
        """是否支持迁移
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SupportMigration

    @SupportMigration.setter
    def SupportMigration(self, SupportMigration):
        self._SupportMigration = SupportMigration

    @property
    def InstanceStatus(self):
        """实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败，6 - 变配中，7 - 变配失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def ZoneId(self):
        """集群所属可用区，表明集群归属的可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneIds(self):
        """集群节点所在的可用区，若该集群为跨可用区集群，则包含该集群节点所在的多个可用区。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        self._PublicEndPoint = params.get("PublicEndPoint")
        self._VpcEndPoint = params.get("VpcEndPoint")
        self._SupportNamespaceEndpoint = params.get("SupportNamespaceEndpoint")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcConfig()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        self._IsVip = params.get("IsVip")
        self._RocketMQFlag = params.get("RocketMQFlag")
        self._Status = params.get("Status")
        self._IsolateTime = params.get("IsolateTime")
        self._HttpPublicEndpoint = params.get("HttpPublicEndpoint")
        self._HttpVpcEndpoint = params.get("HttpVpcEndpoint")
        self._InternalEndpoint = params.get("InternalEndpoint")
        self._HttpInternalEndpoint = params.get("HttpInternalEndpoint")
        self._AclEnabled = params.get("AclEnabled")
        self._PublicClbId = params.get("PublicClbId")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SupportMigration = params.get("SupportMigration")
        self._InstanceStatus = params.get("InstanceStatus")
        self._ZoneId = params.get("ZoneId")
        self._ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterRecentStats(AbstractModel):
    """RocketMQ近期使用量

    """

    def __init__(self):
        r"""
        :param _TopicNum: Topic数量
        :type TopicNum: int
        :param _ProducedMsgNum: 消息生产数
        :type ProducedMsgNum: int
        :param _ConsumedMsgNum: 消息消费数
        :type ConsumedMsgNum: int
        :param _AccumulativeMsgNum: 消息堆积数
        :type AccumulativeMsgNum: int
        """
        self._TopicNum = None
        self._ProducedMsgNum = None
        self._ConsumedMsgNum = None
        self._AccumulativeMsgNum = None

    @property
    def TopicNum(self):
        """Topic数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ProducedMsgNum(self):
        """消息生产数
        :rtype: int
        """
        return self._ProducedMsgNum

    @ProducedMsgNum.setter
    def ProducedMsgNum(self, ProducedMsgNum):
        self._ProducedMsgNum = ProducedMsgNum

    @property
    def ConsumedMsgNum(self):
        """消息消费数
        :rtype: int
        """
        return self._ConsumedMsgNum

    @ConsumedMsgNum.setter
    def ConsumedMsgNum(self, ConsumedMsgNum):
        self._ConsumedMsgNum = ConsumedMsgNum

    @property
    def AccumulativeMsgNum(self):
        """消息堆积数
        :rtype: int
        """
        return self._AccumulativeMsgNum

    @AccumulativeMsgNum.setter
    def AccumulativeMsgNum(self, AccumulativeMsgNum):
        self._AccumulativeMsgNum = AccumulativeMsgNum


    def _deserialize(self, params):
        self._TopicNum = params.get("TopicNum")
        self._ProducedMsgNum = params.get("ProducedMsgNum")
        self._ConsumedMsgNum = params.get("ConsumedMsgNum")
        self._AccumulativeMsgNum = params.get("AccumulativeMsgNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQConsumerConnection(AbstractModel):
    """在线消费者情况

    """

    def __init__(self):
        r"""
        :param _ClientId: 消费者实例ID
        :type ClientId: str
        :param _ClientAddr: 消费者实例的地址和端口
        :type ClientAddr: str
        :param _Language: 消费者应用的语言版本
        :type Language: str
        :param _Accumulative: 消息堆积量
        :type Accumulative: int
        :param _Version: 消费端版本
        :type Version: str
        """
        self._ClientId = None
        self._ClientAddr = None
        self._Language = None
        self._Accumulative = None
        self._Version = None

    @property
    def ClientId(self):
        """消费者实例ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientAddr(self):
        """消费者实例的地址和端口
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def Language(self):
        """消费者应用的语言版本
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Accumulative(self):
        """消息堆积量
        :rtype: int
        """
        return self._Accumulative

    @Accumulative.setter
    def Accumulative(self, Accumulative):
        self._Accumulative = Accumulative

    @property
    def Version(self):
        """消费端版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._ClientAddr = params.get("ClientAddr")
        self._Language = params.get("Language")
        self._Accumulative = params.get("Accumulative")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQConsumerTopic(AbstractModel):
    """消费者详情中的主题信息

    """

    def __init__(self):
        r"""
        :param _Topic: 主题名称
        :type Topic: str
        :param _Type: 主题类型，Normal表示普通，GlobalOrder表示全局顺序，PartitionedOrder表示局部顺序，Transaction表示事务，Retry表示重试，DeadLetter表示死信
        :type Type: str
        :param _PartitionNum: 分区数
        :type PartitionNum: int
        :param _Accumulative: 消息堆积数
        :type Accumulative: int
        :param _LastConsumptionTime: 最后消费时间，以毫秒为单位
        :type LastConsumptionTime: int
        :param _SubRule: 订阅规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SubRule: str
        """
        self._Topic = None
        self._Type = None
        self._PartitionNum = None
        self._Accumulative = None
        self._LastConsumptionTime = None
        self._SubRule = None

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Type(self):
        """主题类型，Normal表示普通，GlobalOrder表示全局顺序，PartitionedOrder表示局部顺序，Transaction表示事务，Retry表示重试，DeadLetter表示死信
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PartitionNum(self):
        """分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def Accumulative(self):
        """消息堆积数
        :rtype: int
        """
        return self._Accumulative

    @Accumulative.setter
    def Accumulative(self, Accumulative):
        self._Accumulative = Accumulative

    @property
    def LastConsumptionTime(self):
        """最后消费时间，以毫秒为单位
        :rtype: int
        """
        return self._LastConsumptionTime

    @LastConsumptionTime.setter
    def LastConsumptionTime(self, LastConsumptionTime):
        self._LastConsumptionTime = LastConsumptionTime

    @property
    def SubRule(self):
        """订阅规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubRule

    @SubRule.setter
    def SubRule(self, SubRule):
        self._SubRule = SubRule


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Type = params.get("Type")
        self._PartitionNum = params.get("PartitionNum")
        self._Accumulative = params.get("Accumulative")
        self._LastConsumptionTime = params.get("LastConsumptionTime")
        self._SubRule = params.get("SubRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQDataPoint(AbstractModel):
    """监控数据点

    """

    def __init__(self):
        r"""
        :param _Timestamps: 监控值数组，该数组和Timestamps一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamps: list of int
        :param _Values: 监控数据点位置，比如一天按分钟划分有1440个点，每个点的序号是0 - 1439之间的一个数，当某个序号不在该数组中，说明掉点了
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of float
        """
        self._Timestamps = None
        self._Values = None

    @property
    def Timestamps(self):
        """监控值数组，该数组和Timestamps一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """监控数据点位置，比如一天按分钟划分有1440个点，每个点的序号是0 - 1439之间的一个数，当某个序号不在该数组中，说明掉点了
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQGroup(AbstractModel):
    """RocketMQ消费组信息

    """

    def __init__(self):
        r"""
        :param _Name: 消费组名称
        :type Name: str
        :param _ConsumerNum: 在线消费者数量
        :type ConsumerNum: int
        :param _TPS: 消费TPS
        :type TPS: int
        :param _TotalAccumulative: 总堆积数量
        :type TotalAccumulative: int
        :param _ConsumptionMode: 0表示集群消费模式，1表示广播消费模式，-1表示未知
        :type ConsumptionMode: int
        :param _ReadEnabled: 是否允许消费
        :type ReadEnabled: bool
        :param _RetryPartitionNum: 重试队列分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryPartitionNum: int
        :param _CreateTime: 创建时间，以毫秒为单位
        :type CreateTime: int
        :param _UpdateTime: 修改时间，以毫秒为单位
        :type UpdateTime: int
        :param _ClientProtocol: 客户端协议
        :type ClientProtocol: str
        :param _Remark: 说明信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _ConsumerType: 消费者类型，枚举值ACTIVELY, PASSIVELY
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerType: str
        :param _BroadcastEnabled: 是否开启广播消费
        :type BroadcastEnabled: bool
        :param _GroupType: Group类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupType: str
        :param _RetryMaxTimes: 重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryMaxTimes: int
        """
        self._Name = None
        self._ConsumerNum = None
        self._TPS = None
        self._TotalAccumulative = None
        self._ConsumptionMode = None
        self._ReadEnabled = None
        self._RetryPartitionNum = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ClientProtocol = None
        self._Remark = None
        self._ConsumerType = None
        self._BroadcastEnabled = None
        self._GroupType = None
        self._RetryMaxTimes = None

    @property
    def Name(self):
        """消费组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ConsumerNum(self):
        """在线消费者数量
        :rtype: int
        """
        return self._ConsumerNum

    @ConsumerNum.setter
    def ConsumerNum(self, ConsumerNum):
        self._ConsumerNum = ConsumerNum

    @property
    def TPS(self):
        """消费TPS
        :rtype: int
        """
        return self._TPS

    @TPS.setter
    def TPS(self, TPS):
        self._TPS = TPS

    @property
    def TotalAccumulative(self):
        """总堆积数量
        :rtype: int
        """
        return self._TotalAccumulative

    @TotalAccumulative.setter
    def TotalAccumulative(self, TotalAccumulative):
        self._TotalAccumulative = TotalAccumulative

    @property
    def ConsumptionMode(self):
        """0表示集群消费模式，1表示广播消费模式，-1表示未知
        :rtype: int
        """
        return self._ConsumptionMode

    @ConsumptionMode.setter
    def ConsumptionMode(self, ConsumptionMode):
        self._ConsumptionMode = ConsumptionMode

    @property
    def ReadEnabled(self):
        """是否允许消费
        :rtype: bool
        """
        return self._ReadEnabled

    @ReadEnabled.setter
    def ReadEnabled(self, ReadEnabled):
        self._ReadEnabled = ReadEnabled

    @property
    def RetryPartitionNum(self):
        """重试队列分区数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryPartitionNum

    @RetryPartitionNum.setter
    def RetryPartitionNum(self, RetryPartitionNum):
        self._RetryPartitionNum = RetryPartitionNum

    @property
    def CreateTime(self):
        """创建时间，以毫秒为单位
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """修改时间，以毫秒为单位
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ClientProtocol(self):
        """客户端协议
        :rtype: str
        """
        return self._ClientProtocol

    @ClientProtocol.setter
    def ClientProtocol(self, ClientProtocol):
        self._ClientProtocol = ClientProtocol

    @property
    def Remark(self):
        """说明信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsumerType(self):
        """消费者类型，枚举值ACTIVELY, PASSIVELY
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerType

    @ConsumerType.setter
    def ConsumerType(self, ConsumerType):
        self._ConsumerType = ConsumerType

    @property
    def BroadcastEnabled(self):
        """是否开启广播消费
        :rtype: bool
        """
        return self._BroadcastEnabled

    @BroadcastEnabled.setter
    def BroadcastEnabled(self, BroadcastEnabled):
        self._BroadcastEnabled = BroadcastEnabled

    @property
    def GroupType(self):
        """Group类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def RetryMaxTimes(self):
        """重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RetryMaxTimes

    @RetryMaxTimes.setter
    def RetryMaxTimes(self, RetryMaxTimes):
        self._RetryMaxTimes = RetryMaxTimes


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ConsumerNum = params.get("ConsumerNum")
        self._TPS = params.get("TPS")
        self._TotalAccumulative = params.get("TotalAccumulative")
        self._ConsumptionMode = params.get("ConsumptionMode")
        self._ReadEnabled = params.get("ReadEnabled")
        self._RetryPartitionNum = params.get("RetryPartitionNum")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ClientProtocol = params.get("ClientProtocol")
        self._Remark = params.get("Remark")
        self._ConsumerType = params.get("ConsumerType")
        self._BroadcastEnabled = params.get("BroadcastEnabled")
        self._GroupType = params.get("GroupType")
        self._RetryMaxTimes = params.get("RetryMaxTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQGroupConfig(AbstractModel):
    """RocketMQ消费组配置信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _GroupName: 消费组名称
        :type GroupName: str
        :param _ConsumeBroadcastEnable: 是否开启广播消费
        :type ConsumeBroadcastEnable: bool
        :param _ConsumeEnable: 是否开启消费
        :type ConsumeEnable: bool
        :param _Remark: 备注信息
        :type Remark: str
        :param _ConsumerGroupType: 协议类型，支持以下枚举值
TCP;
HTTP;
        :type ConsumerGroupType: str
        """
        self._Namespace = None
        self._GroupName = None
        self._ConsumeBroadcastEnable = None
        self._ConsumeEnable = None
        self._Remark = None
        self._ConsumerGroupType = None

    @property
    def Namespace(self):
        """命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def GroupName(self):
        """消费组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ConsumeBroadcastEnable(self):
        """是否开启广播消费
        :rtype: bool
        """
        return self._ConsumeBroadcastEnable

    @ConsumeBroadcastEnable.setter
    def ConsumeBroadcastEnable(self, ConsumeBroadcastEnable):
        self._ConsumeBroadcastEnable = ConsumeBroadcastEnable

    @property
    def ConsumeEnable(self):
        """是否开启消费
        :rtype: bool
        """
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

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
    def ConsumerGroupType(self):
        """协议类型，支持以下枚举值
TCP;
HTTP;
        :rtype: str
        """
        return self._ConsumerGroupType

    @ConsumerGroupType.setter
    def ConsumerGroupType(self, ConsumerGroupType):
        self._ConsumerGroupType = ConsumerGroupType


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._GroupName = params.get("GroupName")
        self._ConsumeBroadcastEnable = params.get("ConsumeBroadcastEnable")
        self._ConsumeEnable = params.get("ConsumeEnable")
        self._Remark = params.get("Remark")
        self._ConsumerGroupType = params.get("ConsumerGroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQGroupConfigOutput(AbstractModel):
    """RocketMQ消费组配置信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _GroupName: 消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Imported: 是否已导入
注意：此字段可能返回 null，表示取不到有效值。
        :type Imported: bool
        :param _Remark: remark
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._Namespace = None
        self._GroupName = None
        self._Imported = None
        self._Remark = None

    @property
    def Namespace(self):
        """命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def GroupName(self):
        """消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Imported(self):
        """是否已导入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Imported

    @Imported.setter
    def Imported(self, Imported):
        self._Imported = Imported

    @property
    def Remark(self):
        """remark
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._GroupName = params.get("GroupName")
        self._Imported = params.get("Imported")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQInstanceConfig(AbstractModel):
    """RocketMQ专享集群实例配置

    """

    def __init__(self):
        r"""
        :param _MaxTpsPerNamespace: 单命名空间TPS上线
        :type MaxTpsPerNamespace: int
        :param _MaxNamespaceNum: 最大命名空间数量
        :type MaxNamespaceNum: int
        :param _UsedNamespaceNum: 已使用命名空间数量
        :type UsedNamespaceNum: int
        :param _MaxTopicNum: 最大Topic数量
        :type MaxTopicNum: int
        :param _UsedTopicNum: 已使用Topic数量
        :type UsedTopicNum: int
        :param _MaxGroupNum: 最大Group数量
        :type MaxGroupNum: int
        :param _UsedGroupNum: 已使用Group数量
        :type UsedGroupNum: int
        :param _ConfigDisplay: 集群类型
        :type ConfigDisplay: str
        :param _NodeCount: 集群节点数
        :type NodeCount: int
        :param _NodeDistribution: 节点分布情况
        :type NodeDistribution: list of InstanceNodeDistribution
        :param _TopicDistribution: topic分布情况
        :type TopicDistribution: list of RocketMQTopicDistribution
        :param _MaxQueuesPerTopic: 每个主题最大队列数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxQueuesPerTopic: int
        :param _MaxRetention: 最大可设置消息保留时间，小时为单位	
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetention: int
        :param _MinRetention: 最小可设置消息保留时间，小时为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MinRetention: int
        :param _Retention: 实例消息保留时间，小时为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Retention: int
        :param _TopicNumLowerLimit: Topic个数最小配额，即免费额度，默认为集群规格单节点最小配额*节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNumLowerLimit: int
        :param _TopicNumUpperLimit: Topic个数最大配额，默认为集群规格单节点最大配额*节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNumUpperLimit: int
        """
        self._MaxTpsPerNamespace = None
        self._MaxNamespaceNum = None
        self._UsedNamespaceNum = None
        self._MaxTopicNum = None
        self._UsedTopicNum = None
        self._MaxGroupNum = None
        self._UsedGroupNum = None
        self._ConfigDisplay = None
        self._NodeCount = None
        self._NodeDistribution = None
        self._TopicDistribution = None
        self._MaxQueuesPerTopic = None
        self._MaxRetention = None
        self._MinRetention = None
        self._Retention = None
        self._TopicNumLowerLimit = None
        self._TopicNumUpperLimit = None

    @property
    def MaxTpsPerNamespace(self):
        """单命名空间TPS上线
        :rtype: int
        """
        return self._MaxTpsPerNamespace

    @MaxTpsPerNamespace.setter
    def MaxTpsPerNamespace(self, MaxTpsPerNamespace):
        self._MaxTpsPerNamespace = MaxTpsPerNamespace

    @property
    def MaxNamespaceNum(self):
        """最大命名空间数量
        :rtype: int
        """
        return self._MaxNamespaceNum

    @MaxNamespaceNum.setter
    def MaxNamespaceNum(self, MaxNamespaceNum):
        self._MaxNamespaceNum = MaxNamespaceNum

    @property
    def UsedNamespaceNum(self):
        """已使用命名空间数量
        :rtype: int
        """
        return self._UsedNamespaceNum

    @UsedNamespaceNum.setter
    def UsedNamespaceNum(self, UsedNamespaceNum):
        self._UsedNamespaceNum = UsedNamespaceNum

    @property
    def MaxTopicNum(self):
        """最大Topic数量
        :rtype: int
        """
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def UsedTopicNum(self):
        """已使用Topic数量
        :rtype: int
        """
        return self._UsedTopicNum

    @UsedTopicNum.setter
    def UsedTopicNum(self, UsedTopicNum):
        self._UsedTopicNum = UsedTopicNum

    @property
    def MaxGroupNum(self):
        """最大Group数量
        :rtype: int
        """
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def UsedGroupNum(self):
        """已使用Group数量
        :rtype: int
        """
        return self._UsedGroupNum

    @UsedGroupNum.setter
    def UsedGroupNum(self, UsedGroupNum):
        self._UsedGroupNum = UsedGroupNum

    @property
    def ConfigDisplay(self):
        """集群类型
        :rtype: str
        """
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def NodeCount(self):
        """集群节点数
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def NodeDistribution(self):
        """节点分布情况
        :rtype: list of InstanceNodeDistribution
        """
        return self._NodeDistribution

    @NodeDistribution.setter
    def NodeDistribution(self, NodeDistribution):
        self._NodeDistribution = NodeDistribution

    @property
    def TopicDistribution(self):
        """topic分布情况
        :rtype: list of RocketMQTopicDistribution
        """
        return self._TopicDistribution

    @TopicDistribution.setter
    def TopicDistribution(self, TopicDistribution):
        self._TopicDistribution = TopicDistribution

    @property
    def MaxQueuesPerTopic(self):
        """每个主题最大队列数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxQueuesPerTopic

    @MaxQueuesPerTopic.setter
    def MaxQueuesPerTopic(self, MaxQueuesPerTopic):
        self._MaxQueuesPerTopic = MaxQueuesPerTopic

    @property
    def MaxRetention(self):
        """最大可设置消息保留时间，小时为单位	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxRetention

    @MaxRetention.setter
    def MaxRetention(self, MaxRetention):
        self._MaxRetention = MaxRetention

    @property
    def MinRetention(self):
        """最小可设置消息保留时间，小时为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinRetention

    @MinRetention.setter
    def MinRetention(self, MinRetention):
        self._MinRetention = MinRetention

    @property
    def Retention(self):
        """实例消息保留时间，小时为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def TopicNumLowerLimit(self):
        """Topic个数最小配额，即免费额度，默认为集群规格单节点最小配额*节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNumLowerLimit

    @TopicNumLowerLimit.setter
    def TopicNumLowerLimit(self, TopicNumLowerLimit):
        self._TopicNumLowerLimit = TopicNumLowerLimit

    @property
    def TopicNumUpperLimit(self):
        """Topic个数最大配额，默认为集群规格单节点最大配额*节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNumUpperLimit

    @TopicNumUpperLimit.setter
    def TopicNumUpperLimit(self, TopicNumUpperLimit):
        self._TopicNumUpperLimit = TopicNumUpperLimit


    def _deserialize(self, params):
        self._MaxTpsPerNamespace = params.get("MaxTpsPerNamespace")
        self._MaxNamespaceNum = params.get("MaxNamespaceNum")
        self._UsedNamespaceNum = params.get("UsedNamespaceNum")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._UsedTopicNum = params.get("UsedTopicNum")
        self._MaxGroupNum = params.get("MaxGroupNum")
        self._UsedGroupNum = params.get("UsedGroupNum")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._NodeCount = params.get("NodeCount")
        if params.get("NodeDistribution") is not None:
            self._NodeDistribution = []
            for item in params.get("NodeDistribution"):
                obj = InstanceNodeDistribution()
                obj._deserialize(item)
                self._NodeDistribution.append(obj)
        if params.get("TopicDistribution") is not None:
            self._TopicDistribution = []
            for item in params.get("TopicDistribution"):
                obj = RocketMQTopicDistribution()
                obj._deserialize(item)
                self._TopicDistribution.append(obj)
        self._MaxQueuesPerTopic = params.get("MaxQueuesPerTopic")
        self._MaxRetention = params.get("MaxRetention")
        self._MinRetention = params.get("MinRetention")
        self._Retention = params.get("Retention")
        self._TopicNumLowerLimit = params.get("TopicNumLowerLimit")
        self._TopicNumUpperLimit = params.get("TopicNumUpperLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQMessageTrack(AbstractModel):
    """Rocketmq消息消费track信息

    """

    def __init__(self):
        r"""
        :param _Group: 消费者组
        :type Group: str
        :param _ConsumeStatus: 消费状态,
CONSUMED: 已消费
CONSUMED_BUT_FILTERED: 已过滤
NOT_CONSUME: 未消费
ENTER_RETRY: 进入重试队列
ENTER_DLQ: 进入死信队列
UNKNOWN: 查询不到消费状态
        :type ConsumeStatus: str
        :param _TrackType: 消息track类型
        :type TrackType: str
        :param _ExceptionDesc: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptionDesc: str
        """
        self._Group = None
        self._ConsumeStatus = None
        self._TrackType = None
        self._ExceptionDesc = None

    @property
    def Group(self):
        """消费者组
        :rtype: str
        """
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def ConsumeStatus(self):
        """消费状态,
CONSUMED: 已消费
CONSUMED_BUT_FILTERED: 已过滤
NOT_CONSUME: 未消费
ENTER_RETRY: 进入重试队列
ENTER_DLQ: 进入死信队列
UNKNOWN: 查询不到消费状态
        :rtype: str
        """
        return self._ConsumeStatus

    @ConsumeStatus.setter
    def ConsumeStatus(self, ConsumeStatus):
        self._ConsumeStatus = ConsumeStatus

    @property
    def TrackType(self):
        """消息track类型
        :rtype: str
        """
        return self._TrackType

    @TrackType.setter
    def TrackType(self, TrackType):
        self._TrackType = TrackType

    @property
    def ExceptionDesc(self):
        """异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExceptionDesc

    @ExceptionDesc.setter
    def ExceptionDesc(self, ExceptionDesc):
        self._ExceptionDesc = ExceptionDesc


    def _deserialize(self, params):
        self._Group = params.get("Group")
        self._ConsumeStatus = params.get("ConsumeStatus")
        self._TrackType = params.get("TrackType")
        self._ExceptionDesc = params.get("ExceptionDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQMigrationTopicDistribution(AbstractModel):
    """迁移主题的阶段分布

    """

    def __init__(self):
        r"""
        :param _Stage: 迁移主题阶段
注意：此字段可能返回 null，表示取不到有效值。
        :type Stage: str
        :param _Count: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._Stage = None
        self._Count = None

    @property
    def Stage(self):
        """迁移主题阶段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def Count(self):
        """数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Stage = params.get("Stage")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQMsgLog(AbstractModel):
    """rocketmq消息日志

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息id
        :type MsgId: str
        :param _MsgTag: 消息tag
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgTag: str
        :param _MsgKey: 消息key
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgKey: str
        :param _ProducerAddr: 客户端地址
        :type ProducerAddr: str
        :param _ProduceTime: 消息发送时间
        :type ProduceTime: str
        :param _PulsarMsgId: pulsar消息id
        :type PulsarMsgId: str
        :param _DeadLetterResendTimes: 死信重发次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterResendTimes: int
        :param _ResendSuccessCount: 死信重发成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResendSuccessCount: int
        """
        self._MsgId = None
        self._MsgTag = None
        self._MsgKey = None
        self._ProducerAddr = None
        self._ProduceTime = None
        self._PulsarMsgId = None
        self._DeadLetterResendTimes = None
        self._ResendSuccessCount = None

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def MsgTag(self):
        """消息tag
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgTag

    @MsgTag.setter
    def MsgTag(self, MsgTag):
        self._MsgTag = MsgTag

    @property
    def MsgKey(self):
        """消息key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgKey

    @MsgKey.setter
    def MsgKey(self, MsgKey):
        self._MsgKey = MsgKey

    @property
    def ProducerAddr(self):
        """客户端地址
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def ProduceTime(self):
        """消息发送时间
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def PulsarMsgId(self):
        """pulsar消息id
        :rtype: str
        """
        return self._PulsarMsgId

    @PulsarMsgId.setter
    def PulsarMsgId(self, PulsarMsgId):
        self._PulsarMsgId = PulsarMsgId

    @property
    def DeadLetterResendTimes(self):
        """死信重发次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeadLetterResendTimes

    @DeadLetterResendTimes.setter
    def DeadLetterResendTimes(self, DeadLetterResendTimes):
        self._DeadLetterResendTimes = DeadLetterResendTimes

    @property
    def ResendSuccessCount(self):
        """死信重发成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResendSuccessCount

    @ResendSuccessCount.setter
    def ResendSuccessCount(self, ResendSuccessCount):
        self._ResendSuccessCount = ResendSuccessCount


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._MsgTag = params.get("MsgTag")
        self._MsgKey = params.get("MsgKey")
        self._ProducerAddr = params.get("ProducerAddr")
        self._ProduceTime = params.get("ProduceTime")
        self._PulsarMsgId = params.get("PulsarMsgId")
        self._DeadLetterResendTimes = params.get("DeadLetterResendTimes")
        self._ResendSuccessCount = params.get("ResendSuccessCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQNamespace(AbstractModel):
    """RocketMQ命名空间信息

    """

    def __init__(self):
        r"""
        :param _NamespaceId: 命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type NamespaceId: str
        :param _Ttl: 已废弃，未消费消息的保留时间，以毫秒单位，范围60秒到15天
        :type Ttl: int
        :param _RetentionTime: 消息持久化后保留的时间，以毫秒单位
        :type RetentionTime: int
        :param _Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _PublicEndpoint: 公网接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicEndpoint: str
        :param _VpcEndpoint: VPC接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcEndpoint: str
        :param _InternalEndpoint: 内部接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalEndpoint: str
        """
        self._NamespaceId = None
        self._Ttl = None
        self._RetentionTime = None
        self._Remark = None
        self._PublicEndpoint = None
        self._VpcEndpoint = None
        self._InternalEndpoint = None

    @property
    def NamespaceId(self):
        """命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Ttl(self):
        """已废弃，未消费消息的保留时间，以毫秒单位，范围60秒到15天
        :rtype: int
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def RetentionTime(self):
        """消息持久化后保留的时间，以毫秒单位
        :rtype: int
        """
        return self._RetentionTime

    @RetentionTime.setter
    def RetentionTime(self, RetentionTime):
        self._RetentionTime = RetentionTime

    @property
    def Remark(self):
        """说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicEndpoint(self):
        """公网接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicEndpoint

    @PublicEndpoint.setter
    def PublicEndpoint(self, PublicEndpoint):
        self._PublicEndpoint = PublicEndpoint

    @property
    def VpcEndpoint(self):
        """VPC接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcEndpoint

    @VpcEndpoint.setter
    def VpcEndpoint(self, VpcEndpoint):
        self._VpcEndpoint = VpcEndpoint

    @property
    def InternalEndpoint(self):
        """内部接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InternalEndpoint

    @InternalEndpoint.setter
    def InternalEndpoint(self, InternalEndpoint):
        self._InternalEndpoint = InternalEndpoint


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._Ttl = params.get("Ttl")
        self._RetentionTime = params.get("RetentionTime")
        self._Remark = params.get("Remark")
        self._PublicEndpoint = params.get("PublicEndpoint")
        self._VpcEndpoint = params.get("VpcEndpoint")
        self._InternalEndpoint = params.get("InternalEndpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQSmoothMigrationTaskItem(AbstractModel):
    """RocketMQ平滑迁移任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param _SourceClusterName: 源集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceClusterName: str
        :param _ClusterId: 目标集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ConnectionType: 网络连接类型，
PUBLIC 公网
VPC 私有网络
OTHER 其他
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionType: str
        :param _SourceNameServer: 源集群NameServer地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceNameServer: str
        :param _TaskStatus: 任务状态
Configuration 迁移配置
SourceConnecting 连接源集群中
MetaDataImport 元数据导入
EndpointSetup 切换接入点
ServiceMigration 切流中
Completed 已完成
Cancelled 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        """
        self._TaskId = None
        self._TaskName = None
        self._SourceClusterName = None
        self._ClusterId = None
        self._ConnectionType = None
        self._SourceNameServer = None
        self._TaskStatus = None

    @property
    def TaskId(self):
        """任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        """任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def SourceClusterName(self):
        """源集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceClusterName

    @SourceClusterName.setter
    def SourceClusterName(self, SourceClusterName):
        self._SourceClusterName = SourceClusterName

    @property
    def ClusterId(self):
        """目标集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ConnectionType(self):
        """网络连接类型，
PUBLIC 公网
VPC 私有网络
OTHER 其他
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConnectionType

    @ConnectionType.setter
    def ConnectionType(self, ConnectionType):
        self._ConnectionType = ConnectionType

    @property
    def SourceNameServer(self):
        """源集群NameServer地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceNameServer

    @SourceNameServer.setter
    def SourceNameServer(self, SourceNameServer):
        self._SourceNameServer = SourceNameServer

    @property
    def TaskStatus(self):
        """任务状态
Configuration 迁移配置
SourceConnecting 连接源集群中
MetaDataImport 元数据导入
EndpointSetup 切换接入点
ServiceMigration 切流中
Completed 已完成
Cancelled 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._SourceClusterName = params.get("SourceClusterName")
        self._ClusterId = params.get("ClusterId")
        self._ConnectionType = params.get("ConnectionType")
        self._SourceNameServer = params.get("SourceNameServer")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQSubscription(AbstractModel):
    """RocketMQ消费组订阅信息

    """

    def __init__(self):
        r"""
        :param _Topic: 主题名称
        :type Topic: str
        :param _Type: 主题类型：
Normal 普通,
GlobalOrder 全局顺序,
PartitionedOrder 局部顺序,
Transaction 事务消息,
DelayScheduled 延时消息,
Retry 重试,
DeadLetter 死信
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _PartitionNum: 分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type PartitionNum: int
        :param _ExpressionType: 过滤模式，TAG，SQL
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpressionType: str
        :param _SubString: 过滤表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type SubString: str
        :param _Status: 订阅状态：
0，订阅关系一致
1，订阅关系不一致
2，未知
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ConsumerLag: 消费堆积数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLag: int
        :param _ClusterId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _ConsumerGroup: 消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerGroup: str
        :param _IsOnline: 是否在线
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOnline: bool
        :param _ConsumeType: 消费类型
0: 广播消费
1: 集群消费
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumeType: int
        :param _Consistency: 订阅一致性
注意：此字段可能返回 null，表示取不到有效值。
        :type Consistency: int
        :param _LastUpdateTime: 最后消费进度更新时间，秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: int
        :param _MaxRetryTimes: 最大重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetryTimes: int
        :param _ClientProtocol: 协议类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientProtocol: str
        :param _ClientSubscriptionInfos: 客户端订阅详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientSubscriptionInfos: list of ClientSubscriptionInfo
        """
        self._Topic = None
        self._Type = None
        self._PartitionNum = None
        self._ExpressionType = None
        self._SubString = None
        self._Status = None
        self._ConsumerLag = None
        self._ClusterId = None
        self._ConsumerGroup = None
        self._IsOnline = None
        self._ConsumeType = None
        self._Consistency = None
        self._LastUpdateTime = None
        self._MaxRetryTimes = None
        self._ClientProtocol = None
        self._ClientSubscriptionInfos = None

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Type(self):
        """主题类型：
Normal 普通,
GlobalOrder 全局顺序,
PartitionedOrder 局部顺序,
Transaction 事务消息,
DelayScheduled 延时消息,
Retry 重试,
DeadLetter 死信
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PartitionNum(self):
        """分区数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def ExpressionType(self):
        """过滤模式，TAG，SQL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpressionType

    @ExpressionType.setter
    def ExpressionType(self, ExpressionType):
        self._ExpressionType = ExpressionType

    @property
    def SubString(self):
        """过滤表达式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubString

    @SubString.setter
    def SubString(self, SubString):
        self._SubString = SubString

    @property
    def Status(self):
        """订阅状态：
0，订阅关系一致
1，订阅关系不一致
2，未知
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ConsumerLag(self):
        """消费堆积数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

    @property
    def ClusterId(self):
        """实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ConsumerGroup(self):
        """消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def IsOnline(self):
        """是否在线
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsOnline

    @IsOnline.setter
    def IsOnline(self, IsOnline):
        self._IsOnline = IsOnline

    @property
    def ConsumeType(self):
        """消费类型
0: 广播消费
1: 集群消费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConsumeType

    @ConsumeType.setter
    def ConsumeType(self, ConsumeType):
        self._ConsumeType = ConsumeType

    @property
    def Consistency(self):
        """订阅一致性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency

    @property
    def LastUpdateTime(self):
        """最后消费进度更新时间，秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def MaxRetryTimes(self):
        """最大重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def ClientProtocol(self):
        """协议类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientProtocol

    @ClientProtocol.setter
    def ClientProtocol(self, ClientProtocol):
        self._ClientProtocol = ClientProtocol

    @property
    def ClientSubscriptionInfos(self):
        """客户端订阅详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClientSubscriptionInfo
        """
        return self._ClientSubscriptionInfos

    @ClientSubscriptionInfos.setter
    def ClientSubscriptionInfos(self, ClientSubscriptionInfos):
        self._ClientSubscriptionInfos = ClientSubscriptionInfos


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Type = params.get("Type")
        self._PartitionNum = params.get("PartitionNum")
        self._ExpressionType = params.get("ExpressionType")
        self._SubString = params.get("SubString")
        self._Status = params.get("Status")
        self._ConsumerLag = params.get("ConsumerLag")
        self._ClusterId = params.get("ClusterId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._IsOnline = params.get("IsOnline")
        self._ConsumeType = params.get("ConsumeType")
        self._Consistency = params.get("Consistency")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._ClientProtocol = params.get("ClientProtocol")
        if params.get("ClientSubscriptionInfos") is not None:
            self._ClientSubscriptionInfos = []
            for item in params.get("ClientSubscriptionInfos"):
                obj = ClientSubscriptionInfo()
                obj._deserialize(item)
                self._ClientSubscriptionInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQTopic(AbstractModel):
    """RocketMQ主题信息

    """

    def __init__(self):
        r"""
        :param _Name: 主题名称
        :type Name: str
        :param _Type: 主题的类别，为枚举类型，Normal，GlobalOrder，PartitionedOrder，Transaction，Retry及DeadLetter
        :type Type: str
        :param _GroupNum: 订阅组数量
        :type GroupNum: int
        :param _Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _PartitionNum: 读写分区数
        :type PartitionNum: int
        :param _CreateTime: 创建时间，以毫秒为单位
        :type CreateTime: int
        :param _UpdateTime: 创建时间，以毫秒为单位
        :type UpdateTime: int
        :param _LastUpdateTime: 最后写入时间，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: int
        :param _SubscriptionCount: 订阅数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionCount: int
        :param _SubscriptionData: 订阅关系列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionData: list of RocketMQSubscription
        """
        self._Name = None
        self._Type = None
        self._GroupNum = None
        self._Remark = None
        self._PartitionNum = None
        self._CreateTime = None
        self._UpdateTime = None
        self._LastUpdateTime = None
        self._SubscriptionCount = None
        self._SubscriptionData = None

    @property
    def Name(self):
        """主题名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """主题的类别，为枚举类型，Normal，GlobalOrder，PartitionedOrder，Transaction，Retry及DeadLetter
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GroupNum(self):
        """订阅组数量
        :rtype: int
        """
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def Remark(self):
        """说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PartitionNum(self):
        """读写分区数
        :rtype: int
        """
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def CreateTime(self):
        """创建时间，以毫秒为单位
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """创建时间，以毫秒为单位
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastUpdateTime(self):
        """最后写入时间，单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def SubscriptionCount(self):
        """订阅数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SubscriptionCount

    @SubscriptionCount.setter
    def SubscriptionCount(self, SubscriptionCount):
        self._SubscriptionCount = SubscriptionCount

    @property
    def SubscriptionData(self):
        """订阅关系列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RocketMQSubscription
        """
        return self._SubscriptionData

    @SubscriptionData.setter
    def SubscriptionData(self, SubscriptionData):
        self._SubscriptionData = SubscriptionData


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._GroupNum = params.get("GroupNum")
        self._Remark = params.get("Remark")
        self._PartitionNum = params.get("PartitionNum")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._SubscriptionCount = params.get("SubscriptionCount")
        if params.get("SubscriptionData") is not None:
            self._SubscriptionData = []
            for item in params.get("SubscriptionData"):
                obj = RocketMQSubscription()
                obj._deserialize(item)
                self._SubscriptionData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQTopicConfig(AbstractModel):
    """RocketMQ主题配置信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _Type: 主题类型：
Normal，普通
PartitionedOrder, 分区顺序
Transaction，事务消息
DelayScheduled，延迟/定时消息
        :type Type: str
        :param _Partitions: 分区个数
        :type Partitions: int
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._Namespace = None
        self._TopicName = None
        self._Type = None
        self._Partitions = None
        self._Remark = None

    @property
    def Namespace(self):
        """命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Type(self):
        """主题类型：
Normal，普通
PartitionedOrder, 分区顺序
Transaction，事务消息
DelayScheduled，延迟/定时消息
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Partitions(self):
        """分区个数
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

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
        self._Namespace = params.get("Namespace")
        self._TopicName = params.get("TopicName")
        self._Type = params.get("Type")
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQTopicConfigOutput(AbstractModel):
    """RocketMQ主题配置信息

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _TopicName: 主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _Type: 主题类型：
Normal，普通
GlobalOrder， 全局顺序
PartitionedOrder, 分区顺序
Transaction，事务消息
DelayScheduled，延迟/定时消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Partitions: 分区个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Imported: 是否导入
注意：此字段可能返回 null，表示取不到有效值。
        :type Imported: bool
        """
        self._Namespace = None
        self._TopicName = None
        self._Type = None
        self._Partitions = None
        self._Remark = None
        self._Imported = None

    @property
    def Namespace(self):
        """命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def TopicName(self):
        """主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Type(self):
        """主题类型：
Normal，普通
GlobalOrder， 全局顺序
PartitionedOrder, 分区顺序
Transaction，事务消息
DelayScheduled，延迟/定时消息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Partitions(self):
        """分区个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Remark(self):
        """备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Imported(self):
        """是否导入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Imported

    @Imported.setter
    def Imported(self, Imported):
        self._Imported = Imported


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._TopicName = params.get("TopicName")
        self._Type = params.get("Type")
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        self._Imported = params.get("Imported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQTopicDistribution(AbstractModel):
    """RocketMQtopic分布情况

    """

    def __init__(self):
        r"""
        :param _TopicType: topic类型
        :type TopicType: str
        :param _Count: topic数量
        :type Count: int
        """
        self._TopicType = None
        self._Count = None

    @property
    def TopicType(self):
        """topic类型
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def Count(self):
        """topic数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._TopicType = params.get("TopicType")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQVipInstance(AbstractModel):
    """RocketMQ专享实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceVersion: 实例版本
        :type InstanceVersion: str
        :param _Status: 实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败，6 - 变配中，7 - 变配失败
        :type Status: int
        :param _NodeCount: 节点数量
        :type NodeCount: int
        :param _ConfigDisplay: 实例配置规格名称
        :type ConfigDisplay: str
        :param _MaxTps: 峰值TPS
        :type MaxTps: int
        :param _MaxBandWidth: 峰值带宽，Mbps为单位
        :type MaxBandWidth: int
        :param _MaxStorage: 存储容量，GB为单位
        :type MaxStorage: int
        :param _ExpireTime: 实例到期时间，毫秒为单位
        :type ExpireTime: int
        :param _AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type AutoRenewFlag: int
        :param _PayMode: 0-后付费，1-预付费
        :type PayMode: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _SpecName: 实例配置ID
        :type SpecName: str
        :param _MaxRetention: 最大可设置消息保留时间，小时为单位
        :type MaxRetention: int
        :param _MinRetention: 最小可设置消息保留时间，小时为单位
        :type MinRetention: int
        :param _Retention: 实例消息保留时间，小时为单位
        :type Retention: int
        :param _AclEnabled: 是否开启ACL鉴权
        :type AclEnabled: bool
        :param _DestroyTime: 销毁时间
        :type DestroyTime: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._NodeCount = None
        self._ConfigDisplay = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._MaxStorage = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None
        self._MaxRetention = None
        self._MinRetention = None
        self._Retention = None
        self._AclEnabled = None
        self._DestroyTime = None

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
        """实例版本
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        """实例状态，0表示创建中，1表示正常，2表示隔离中，3表示已销毁，4 - 异常, 5 - 发货失败，6 - 变配中，7 - 变配失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeCount(self):
        """节点数量
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def ConfigDisplay(self):
        """实例配置规格名称
        :rtype: str
        """
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def MaxTps(self):
        """峰值TPS
        :rtype: int
        """
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxBandWidth(self):
        """峰值带宽，Mbps为单位
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def MaxStorage(self):
        """存储容量，GB为单位
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def ExpireTime(self):
        """实例到期时间，毫秒为单位
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
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        """实例配置ID
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def MaxRetention(self):
        """最大可设置消息保留时间，小时为单位
        :rtype: int
        """
        return self._MaxRetention

    @MaxRetention.setter
    def MaxRetention(self, MaxRetention):
        self._MaxRetention = MaxRetention

    @property
    def MinRetention(self):
        """最小可设置消息保留时间，小时为单位
        :rtype: int
        """
        return self._MinRetention

    @MinRetention.setter
    def MinRetention(self, MinRetention):
        self._MinRetention = MinRetention

    @property
    def Retention(self):
        """实例消息保留时间，小时为单位
        :rtype: int
        """
        return self._Retention

    @Retention.setter
    def Retention(self, Retention):
        self._Retention = Retention

    @property
    def AclEnabled(self):
        """是否开启ACL鉴权
        :rtype: bool
        """
        return self._AclEnabled

    @AclEnabled.setter
    def AclEnabled(self, AclEnabled):
        self._AclEnabled = AclEnabled

    @property
    def DestroyTime(self):
        """销毁时间
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._NodeCount = params.get("NodeCount")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._MaxStorage = params.get("MaxStorage")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        self._MaxRetention = params.get("MaxRetention")
        self._MinRetention = params.get("MinRetention")
        self._Retention = params.get("Retention")
        self._AclEnabled = params.get("AclEnabled")
        self._DestroyTime = params.get("DestroyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Role(AbstractModel):
    """角色实例

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称。
        :type RoleName: str
        :param _Token: 角色token值。
        :type Token: str
        :param _Remark: 备注说明。
        :type Remark: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _PermType: 授权类型（Cluster：集群；TopicAndGroup：主题或消费组）
        :type PermType: str
        """
        self._RoleName = None
        self._Token = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._PermType = None

    @property
    def RoleName(self):
        """角色名称。
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Token(self):
        """角色token值。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Remark(self):
        """备注说明。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PermType(self):
        """授权类型（Cluster：集群；TopicAndGroup：主题或消费组）
        :rtype: str
        """
        return self._PermType

    @PermType.setter
    def PermType(self, PermType):
        self._PermType = PermType


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Token = params.get("Token")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._PermType = params.get("PermType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicy(AbstractModel):
    """安全策略

    """

    def __init__(self):
        r"""
        :param _Route: ip或者网段
注意：此字段可能返回 null，表示取不到有效值。
        :type Route: str
        :param _Policy: 策略 true就是允许，白名单或者 false 拒绝 黑名单

注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: bool
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._Route = None
        self._Policy = None
        self._Remark = None

    @property
    def Route(self):
        """ip或者网段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Route

    @Route.setter
    def Route(self, Route):
        self._Route = Route

    @property
    def Policy(self):
        """策略 true就是允许，白名单或者 false 拒绝 黑名单

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Remark(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Route = params.get("Route")
        self._Policy = params.get("Policy")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesRequest(AbstractModel):
    """SendBatchMessages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: 消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :type Topic: str
        :param _Payload: 需要发送消息的内容
        :type Payload: str
        :param _StringToken: String 类型的 token，可以不填，系统会自动获取
        :type StringToken: str
        :param _ProducerName: producer 的名字，要求全局是唯一的，如果不设置，系统会自动生成
        :type ProducerName: str
        :param _SendTimeout: 单位：s。消息发送的超时时间。默认值为：30s
        :type SendTimeout: int
        :param _MaxPendingMessages: 内存中允许缓存的生产消息的最大数量，默认值：1000条
        :type MaxPendingMessages: int
        :param _BatchingMaxMessages: 每一个batch中消息的最大数量，默认值：1000条/batch
        :type BatchingMaxMessages: int
        :param _BatchingMaxPublishDelay: 每一个batch最大等待的时间，超过这个时间，不管是否达到指定的batch中消息的数量和大小，都会将该batch发送出去，默认：10ms
        :type BatchingMaxPublishDelay: int
        :param _BatchingMaxBytes: 每一个batch中最大允许的消息的大小，默认：128KB
        :type BatchingMaxBytes: int
        """
        self._Topic = None
        self._Payload = None
        self._StringToken = None
        self._ProducerName = None
        self._SendTimeout = None
        self._MaxPendingMessages = None
        self._BatchingMaxMessages = None
        self._BatchingMaxPublishDelay = None
        self._BatchingMaxBytes = None

    @property
    def Topic(self):
        """消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        """需要发送消息的内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def StringToken(self):
        """String 类型的 token，可以不填，系统会自动获取
        :rtype: str
        """
        return self._StringToken

    @StringToken.setter
    def StringToken(self, StringToken):
        self._StringToken = StringToken

    @property
    def ProducerName(self):
        """producer 的名字，要求全局是唯一的，如果不设置，系统会自动生成
        :rtype: str
        """
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def SendTimeout(self):
        """单位：s。消息发送的超时时间。默认值为：30s
        :rtype: int
        """
        return self._SendTimeout

    @SendTimeout.setter
    def SendTimeout(self, SendTimeout):
        self._SendTimeout = SendTimeout

    @property
    def MaxPendingMessages(self):
        """内存中允许缓存的生产消息的最大数量，默认值：1000条
        :rtype: int
        """
        return self._MaxPendingMessages

    @MaxPendingMessages.setter
    def MaxPendingMessages(self, MaxPendingMessages):
        self._MaxPendingMessages = MaxPendingMessages

    @property
    def BatchingMaxMessages(self):
        """每一个batch中消息的最大数量，默认值：1000条/batch
        :rtype: int
        """
        return self._BatchingMaxMessages

    @BatchingMaxMessages.setter
    def BatchingMaxMessages(self, BatchingMaxMessages):
        self._BatchingMaxMessages = BatchingMaxMessages

    @property
    def BatchingMaxPublishDelay(self):
        """每一个batch最大等待的时间，超过这个时间，不管是否达到指定的batch中消息的数量和大小，都会将该batch发送出去，默认：10ms
        :rtype: int
        """
        return self._BatchingMaxPublishDelay

    @BatchingMaxPublishDelay.setter
    def BatchingMaxPublishDelay(self, BatchingMaxPublishDelay):
        self._BatchingMaxPublishDelay = BatchingMaxPublishDelay

    @property
    def BatchingMaxBytes(self):
        """每一个batch中最大允许的消息的大小，默认：128KB
        :rtype: int
        """
        return self._BatchingMaxBytes

    @BatchingMaxBytes.setter
    def BatchingMaxBytes(self, BatchingMaxBytes):
        self._BatchingMaxBytes = BatchingMaxBytes


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Payload = params.get("Payload")
        self._StringToken = params.get("StringToken")
        self._ProducerName = params.get("ProducerName")
        self._SendTimeout = params.get("SendTimeout")
        self._MaxPendingMessages = params.get("MaxPendingMessages")
        self._BatchingMaxMessages = params.get("BatchingMaxMessages")
        self._BatchingMaxPublishDelay = params.get("BatchingMaxPublishDelay")
        self._BatchingMaxBytes = params.get("BatchingMaxBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesResponse(AbstractModel):
    """SendBatchMessages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageId: 消息的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: str
        :param _ErrorMsg: 错误消息，返回为 ""，代表没有错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def MessageId(self):
        """消息的唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ErrorMsg(self):
        """错误消息，返回为 ""，代表没有错误
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._MessageId = params.get("MessageId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SendCmqMsgRequest(AbstractModel):
    """SendCmqMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名
        :type QueueName: str
        :param _MsgContent: 消息内容
        :type MsgContent: str
        :param _DelaySeconds: 延迟时间。单位为秒，默认值为0秒，最大不能超过队列配置的消息最长未确认时间。
        :type DelaySeconds: int
        """
        self._QueueName = None
        self._MsgContent = None
        self._DelaySeconds = None

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
    def MsgContent(self):
        """消息内容
        :rtype: str
        """
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

    @property
    def DelaySeconds(self):
        """延迟时间。单位为秒，默认值为0秒，最大不能超过队列配置的消息最长未确认时间。
        :rtype: int
        """
        return self._DelaySeconds

    @DelaySeconds.setter
    def DelaySeconds(self, DelaySeconds):
        self._DelaySeconds = DelaySeconds


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MsgContent = params.get("MsgContent")
        self._DelaySeconds = params.get("DelaySeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCmqMsgResponse(AbstractModel):
    """SendCmqMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: true表示发送成功
        :type Result: bool
        :param _MsgId: 消息id
        :type MsgId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._MsgId = None
        self._RequestId = None

    @property
    def Result(self):
        """true表示发送成功
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

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
        self._Result = params.get("Result")
        self._MsgId = params.get("MsgId")
        self._RequestId = params.get("RequestId")


class SendMessagesRequest(AbstractModel):
    """SendMessages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: 消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :type Topic: str
        :param _Payload: 要发送的消息的内容
        :type Payload: str
        :param _StringToken: Token 是用来做鉴权使用的，可以不填，系统会自动获取
        :type StringToken: str
        :param _ProducerName: 设置 producer 的名字，要求全局唯一。该参数建议用户无需手动配置，此时系统会随机生成，如果手动设置有可能会造成创建 Producer 失败进而导致消息发送失败。
该参数主要用于某些特定场景下，只允许特定的 Producer 生产消息时设置，用户的大部分场景使用不到该特性。
        :type ProducerName: str
        :param _SendTimeout: 设置消息发送的超时时间，默认为30s
        :type SendTimeout: int
        :param _MaxPendingMessages: 内存中缓存的最大的生产消息的数量，默认为1000条
        :type MaxPendingMessages: int
        """
        self._Topic = None
        self._Payload = None
        self._StringToken = None
        self._ProducerName = None
        self._SendTimeout = None
        self._MaxPendingMessages = None

    @property
    def Topic(self):
        """消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        """要发送的消息的内容
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def StringToken(self):
        """Token 是用来做鉴权使用的，可以不填，系统会自动获取
        :rtype: str
        """
        return self._StringToken

    @StringToken.setter
    def StringToken(self, StringToken):
        self._StringToken = StringToken

    @property
    def ProducerName(self):
        """设置 producer 的名字，要求全局唯一。该参数建议用户无需手动配置，此时系统会随机生成，如果手动设置有可能会造成创建 Producer 失败进而导致消息发送失败。
该参数主要用于某些特定场景下，只允许特定的 Producer 生产消息时设置，用户的大部分场景使用不到该特性。
        :rtype: str
        """
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def SendTimeout(self):
        """设置消息发送的超时时间，默认为30s
        :rtype: int
        """
        return self._SendTimeout

    @SendTimeout.setter
    def SendTimeout(self, SendTimeout):
        self._SendTimeout = SendTimeout

    @property
    def MaxPendingMessages(self):
        """内存中缓存的最大的生产消息的数量，默认为1000条
        :rtype: int
        """
        return self._MaxPendingMessages

    @MaxPendingMessages.setter
    def MaxPendingMessages(self, MaxPendingMessages):
        self._MaxPendingMessages = MaxPendingMessages


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Payload = params.get("Payload")
        self._StringToken = params.get("StringToken")
        self._ProducerName = params.get("ProducerName")
        self._SendTimeout = params.get("SendTimeout")
        self._MaxPendingMessages = params.get("MaxPendingMessages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessagesResponse(AbstractModel):
    """SendMessages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageId: 消息的messageID, 是全局唯一的，用来标识消息的元数据信息
        :type MessageId: str
        :param _ErrorMsg: 返回的错误消息，如果返回为 “”，说明没有错误
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def MessageId(self):
        """消息的messageID, 是全局唯一的，用来标识消息的元数据信息
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ErrorMsg(self):
        """返回的错误消息，如果返回为 “”，说明没有错误
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._MessageId = params.get("MessageId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SendMsgRequest(AbstractModel):
    """SendMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名称，如果是分区topic需要指定具体分区，如果没有指定则默认发到0分区，例如：my_topic-partition-0。
        :type TopicName: str
        :param _MsgContent: 消息内容，不能为空且大小不得大于5242880个byte。
        :type MsgContent: str
        :param _ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._MsgContent = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称，如果是分区topic需要指定具体分区，如果没有指定则默认发到0分区，例如：my_topic-partition-0。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgContent(self):
        """消息内容，不能为空且大小不得大于5242880个byte。
        :rtype: str
        """
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

    @property
    def ClusterId(self):
        """Pulsar 集群的ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._MsgContent = params.get("MsgContent")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMsgResponse(AbstractModel):
    """SendMsg返回参数结构体

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


class SendRocketMQMessageRequest(AbstractModel):
    """SendRocketMQMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _NamespaceId: 命名空间
        :type NamespaceId: str
        :param _TopicName: topic名称
        :type TopicName: str
        :param _MsgBody: 信息内容
        :type MsgBody: str
        :param _MsgKey: 消息key信息
        :type MsgKey: str
        :param _MsgTag: 消息tag信息
        :type MsgTag: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._TopicName = None
        self._MsgBody = None
        self._MsgKey = None
        self._MsgTag = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        """命名空间
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def TopicName(self):
        """topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgBody(self):
        """信息内容
        :rtype: str
        """
        return self._MsgBody

    @MsgBody.setter
    def MsgBody(self, MsgBody):
        self._MsgBody = MsgBody

    @property
    def MsgKey(self):
        """消息key信息
        :rtype: str
        """
        return self._MsgKey

    @MsgKey.setter
    def MsgKey(self, MsgKey):
        self._MsgKey = MsgKey

    @property
    def MsgTag(self):
        """消息tag信息
        :rtype: str
        """
        return self._MsgTag

    @MsgTag.setter
    def MsgTag(self, MsgTag):
        self._MsgTag = MsgTag


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._TopicName = params.get("TopicName")
        self._MsgBody = params.get("MsgBody")
        self._MsgKey = params.get("MsgKey")
        self._MsgTag = params.get("MsgTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendRocketMQMessageResponse(AbstractModel):
    """SendRocketMQMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 发送结果
        :type Result: bool
        :param _MsgId: 消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._MsgId = None
        self._RequestId = None

    @property
    def Result(self):
        """发送结果
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def MsgId(self):
        """消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

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
        self._Result = params.get("Result")
        self._MsgId = params.get("MsgId")
        self._RequestId = params.get("RequestId")


class ServerLog(AbstractModel):
    """服务方信息

    """

    def __init__(self):
        r"""
        :param _SaveTime: 存储时间。
        :type SaveTime: str
        :param _Status: 状态。
        :type Status: str
        """
        self._SaveTime = None
        self._Status = None

    @property
    def SaveTime(self):
        """存储时间。
        :rtype: str
        """
        return self._SaveTime

    @SaveTime.setter
    def SaveTime(self, SaveTime):
        self._SaveTime = SaveTime

    @property
    def Status(self):
        """状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._SaveTime = params.get("SaveTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRocketMQPublicAccessPointRequest(AbstractModel):
    """SetRocketMQPublicAccessPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID，当前只支持专享集群
        :type InstanceId: str
        :param _Enabled: 开启或关闭访问
        :type Enabled: bool
        :param _Bandwidth: 带宽大小，开启或者调整公网时必须指定，Mbps为单位
        :type Bandwidth: int
        :param _PayMode: 付费模式，开启公网时必须指定，0为按小时计费，1为包年包月，当前只支持按小时计费
        :type PayMode: int
        :param _Rules: 公网访问安全规则列表，Enabled为true时必须传入
        :type Rules: list of PublicAccessRule
        :param _BillingFlow: 公网是否按流量计费
        :type BillingFlow: bool
        """
        self._InstanceId = None
        self._Enabled = None
        self._Bandwidth = None
        self._PayMode = None
        self._Rules = None
        self._BillingFlow = None

    @property
    def InstanceId(self):
        """集群ID，当前只支持专享集群
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Enabled(self):
        """开启或关闭访问
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Bandwidth(self):
        """带宽大小，开启或者调整公网时必须指定，Mbps为单位
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def PayMode(self):
        """付费模式，开启公网时必须指定，0为按小时计费，1为包年包月，当前只支持按小时计费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Rules(self):
        """公网访问安全规则列表，Enabled为true时必须传入
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def BillingFlow(self):
        """公网是否按流量计费
        :rtype: bool
        """
        return self._BillingFlow

    @BillingFlow.setter
    def BillingFlow(self, BillingFlow):
        self._BillingFlow = BillingFlow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Enabled = params.get("Enabled")
        self._Bandwidth = params.get("Bandwidth")
        self._PayMode = params.get("PayMode")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._BillingFlow = params.get("BillingFlow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRocketMQPublicAccessPointResponse(AbstractModel):
    """SetRocketMQPublicAccessPoint返回参数结构体

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


class Sort(AbstractModel):
    """排序器

    """

    def __init__(self):
        r"""
        :param _Name: 排序字段
        :type Name: str
        :param _Order: 升序ASC，降序DESC
        :type Order: str
        """
        self._Name = None
        self._Order = None

    @property
    def Name(self):
        """排序字段
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Order(self):
        """升序ASC，降序DESC
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Subscription(AbstractModel):
    """订阅者

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名称。
        :type TopicName: str
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _ConnectedSince: 消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectedSince: str
        :param _ConsumerAddr: 消费者地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerAddr: str
        :param _ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerCount: str
        :param _ConsumerName: 消费者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerName: str
        :param _MsgBacklog: 堆积的消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgBacklog: str
        :param _MsgRateExpired: 于TTL，此订阅下没有被发送而是被丢弃的比例。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateExpired: str
        :param _MsgRateOut: 消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateOut: str
        :param _MsgThroughputOut: 消费者每秒消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputOut: str
        :param _SubscriptionName: 订阅名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionName: str
        :param _ConsumerSets: 消费者集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerSets: list of Consumer
        :param _IsOnline: 是否在线。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOnline: bool
        :param _ConsumersScheduleSets: 消费进度集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumersScheduleSets: list of ConsumersSchedule
        :param _Remark: 备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _SubType: 订阅类型，Exclusive，Shared，Failover， Key_Shared，空或NULL表示未知，
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param _BlockedSubscriptionOnUnackedMsgs: 是否由于未 ack 数到达上限而被 block
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockedSubscriptionOnUnackedMsgs: bool
        :param _MaxUnackedMsgNum: 未 ack 消息数上限
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxUnackedMsgNum: int
        """
        self._TopicName = None
        self._EnvironmentId = None
        self._ConnectedSince = None
        self._ConsumerAddr = None
        self._ConsumerCount = None
        self._ConsumerName = None
        self._MsgBacklog = None
        self._MsgRateExpired = None
        self._MsgRateOut = None
        self._MsgThroughputOut = None
        self._SubscriptionName = None
        self._ConsumerSets = None
        self._IsOnline = None
        self._ConsumersScheduleSets = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._SubType = None
        self._BlockedSubscriptionOnUnackedMsgs = None
        self._MaxUnackedMsgNum = None

    @property
    def TopicName(self):
        """主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ConnectedSince(self):
        """消费者开始连接的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConnectedSince

    @ConnectedSince.setter
    def ConnectedSince(self, ConnectedSince):
        self._ConnectedSince = ConnectedSince

    @property
    def ConsumerAddr(self):
        """消费者地址。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerAddr

    @ConsumerAddr.setter
    def ConsumerAddr(self, ConsumerAddr):
        self._ConsumerAddr = ConsumerAddr

    @property
    def ConsumerCount(self):
        """消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerCount

    @ConsumerCount.setter
    def ConsumerCount(self, ConsumerCount):
        self._ConsumerCount = ConsumerCount

    @property
    def ConsumerName(self):
        """消费者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerName

    @ConsumerName.setter
    def ConsumerName(self, ConsumerName):
        self._ConsumerName = ConsumerName

    @property
    def MsgBacklog(self):
        """堆积的消息数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgBacklog

    @MsgBacklog.setter
    def MsgBacklog(self, MsgBacklog):
        self._MsgBacklog = MsgBacklog

    @property
    def MsgRateExpired(self):
        """于TTL，此订阅下没有被发送而是被丢弃的比例。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgRateExpired

    @MsgRateExpired.setter
    def MsgRateExpired(self, MsgRateExpired):
        self._MsgRateExpired = MsgRateExpired

    @property
    def MsgRateOut(self):
        """消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputOut(self):
        """消费者每秒消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def SubscriptionName(self):
        """订阅名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def ConsumerSets(self):
        """消费者集合。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Consumer
        """
        return self._ConsumerSets

    @ConsumerSets.setter
    def ConsumerSets(self, ConsumerSets):
        self._ConsumerSets = ConsumerSets

    @property
    def IsOnline(self):
        """是否在线。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsOnline

    @IsOnline.setter
    def IsOnline(self, IsOnline):
        self._IsOnline = IsOnline

    @property
    def ConsumersScheduleSets(self):
        """消费进度集合。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConsumersSchedule
        """
        return self._ConsumersScheduleSets

    @ConsumersScheduleSets.setter
    def ConsumersScheduleSets(self, ConsumersScheduleSets):
        self._ConsumersScheduleSets = ConsumersScheduleSets

    @property
    def Remark(self):
        """备注。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def SubType(self):
        """订阅类型，Exclusive，Shared，Failover， Key_Shared，空或NULL表示未知，
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def BlockedSubscriptionOnUnackedMsgs(self):
        """是否由于未 ack 数到达上限而被 block
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._BlockedSubscriptionOnUnackedMsgs

    @BlockedSubscriptionOnUnackedMsgs.setter
    def BlockedSubscriptionOnUnackedMsgs(self, BlockedSubscriptionOnUnackedMsgs):
        self._BlockedSubscriptionOnUnackedMsgs = BlockedSubscriptionOnUnackedMsgs

    @property
    def MaxUnackedMsgNum(self):
        """未 ack 消息数上限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxUnackedMsgNum

    @MaxUnackedMsgNum.setter
    def MaxUnackedMsgNum(self, MaxUnackedMsgNum):
        self._MaxUnackedMsgNum = MaxUnackedMsgNum


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._EnvironmentId = params.get("EnvironmentId")
        self._ConnectedSince = params.get("ConnectedSince")
        self._ConsumerAddr = params.get("ConsumerAddr")
        self._ConsumerCount = params.get("ConsumerCount")
        self._ConsumerName = params.get("ConsumerName")
        self._MsgBacklog = params.get("MsgBacklog")
        self._MsgRateExpired = params.get("MsgRateExpired")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._SubscriptionName = params.get("SubscriptionName")
        if params.get("ConsumerSets") is not None:
            self._ConsumerSets = []
            for item in params.get("ConsumerSets"):
                obj = Consumer()
                obj._deserialize(item)
                self._ConsumerSets.append(obj)
        self._IsOnline = params.get("IsOnline")
        if params.get("ConsumersScheduleSets") is not None:
            self._ConsumersScheduleSets = []
            for item in params.get("ConsumersScheduleSets"):
                obj = ConsumersSchedule()
                obj._deserialize(item)
                self._ConsumersScheduleSets.append(obj)
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._SubType = params.get("SubType")
        self._BlockedSubscriptionOnUnackedMsgs = params.get("BlockedSubscriptionOnUnackedMsgs")
        self._MaxUnackedMsgNum = params.get("MaxUnackedMsgNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscriptionTopic(AbstractModel):
    """订阅关系

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名称。
        :type TopicName: str
        :param _SubscriptionName: 订阅名称。
        :type SubscriptionName: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        """订阅名称。
        :rtype: str
        """
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签的key/value的类型

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的key的值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签的Value的值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签的key的值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签的Value的值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class Topic(AbstractModel):
    """主题实例

    """

    def __init__(self):
        r"""
        :param _AverageMsgSize: 最后一次间隔内发布消息的平均byte大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageMsgSize: str
        :param _ConsumerCount: 消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerCount: str
        :param _LastConfirmedEntry: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastConfirmedEntry: str
        :param _LastLedgerCreatedTimestamp: 最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLedgerCreatedTimestamp: str
        :param _MsgRateIn: 本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: str
        :param _MsgRateOut: 本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateOut: str
        :param _MsgThroughputIn: 本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: str
        :param _MsgThroughputOut: 本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputOut: str
        :param _NumberOfEntries: 被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type NumberOfEntries: str
        :param _Partitions: 分区数<=0：topic下无子分区。
注意：此字段可能返回 null，表示取不到有效值。
        :type Partitions: int
        :param _ProducerCount: 生产者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerCount: str
        :param _TotalSize: 以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: str
        :param _SubTopicSets: 分区topic里面的子分区。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubTopicSets: list of PartitionsTopic
        :param _TopicType: topic类型描述：
0：普通消息；
1：全局顺序消息；
2：局部顺序消息；
3：重试队列；
4：死信队列；
5：事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicType: int
        :param _EnvironmentId: 环境（命名空间）名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentId: str
        :param _TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _Remark: 说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _ProducerLimit: 生产者上限。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerLimit: str
        :param _ConsumerLimit: 消费者上限。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLimit: str
        :param _PulsarTopicType: 0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
注意：此字段可能返回 null，表示取不到有效值。
        :type PulsarTopicType: int
        :param _MsgTTL: 未消费消息过期时间，单位：秒

注意：此字段可能返回 null，表示取不到有效值。
        :type MsgTTL: int
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Tenant: 用户自定义的租户别名，如果没有，会复用专业集群 ID

        :type Tenant: str
        """
        self._AverageMsgSize = None
        self._ConsumerCount = None
        self._LastConfirmedEntry = None
        self._LastLedgerCreatedTimestamp = None
        self._MsgRateIn = None
        self._MsgRateOut = None
        self._MsgThroughputIn = None
        self._MsgThroughputOut = None
        self._NumberOfEntries = None
        self._Partitions = None
        self._ProducerCount = None
        self._TotalSize = None
        self._SubTopicSets = None
        self._TopicType = None
        self._EnvironmentId = None
        self._TopicName = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ProducerLimit = None
        self._ConsumerLimit = None
        self._PulsarTopicType = None
        self._MsgTTL = None
        self._ClusterId = None
        self._Tenant = None

    @property
    def AverageMsgSize(self):
        """最后一次间隔内发布消息的平均byte大小。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AverageMsgSize

    @AverageMsgSize.setter
    def AverageMsgSize(self, AverageMsgSize):
        self._AverageMsgSize = AverageMsgSize

    @property
    def ConsumerCount(self):
        """消费者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerCount

    @ConsumerCount.setter
    def ConsumerCount(self, ConsumerCount):
        self._ConsumerCount = ConsumerCount

    @property
    def LastConfirmedEntry(self):
        """被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastConfirmedEntry

    @LastConfirmedEntry.setter
    def LastConfirmedEntry(self, LastConfirmedEntry):
        self._LastConfirmedEntry = LastConfirmedEntry

    @property
    def LastLedgerCreatedTimestamp(self):
        """最后一个ledger创建的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastLedgerCreatedTimestamp

    @LastLedgerCreatedTimestamp.setter
    def LastLedgerCreatedTimestamp(self, LastLedgerCreatedTimestamp):
        self._LastLedgerCreatedTimestamp = LastLedgerCreatedTimestamp

    @property
    def MsgRateIn(self):
        """本地和复制的发布者每秒发布消息的速率。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgRateOut(self):
        """本地和复制的消费者每秒分发消息的数量之和。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputIn(self):
        """本地和复制的发布者每秒发布消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def MsgThroughputOut(self):
        """本地和复制的消费者每秒分发消息的byte。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def NumberOfEntries(self):
        """被记录下来的消息总数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NumberOfEntries

    @NumberOfEntries.setter
    def NumberOfEntries(self, NumberOfEntries):
        self._NumberOfEntries = NumberOfEntries

    @property
    def Partitions(self):
        """分区数<=0：topic下无子分区。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def ProducerCount(self):
        """生产者数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProducerCount

    @ProducerCount.setter
    def ProducerCount(self, ProducerCount):
        self._ProducerCount = ProducerCount

    @property
    def TotalSize(self):
        """以byte计算的所有消息存储总量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def SubTopicSets(self):
        """分区topic里面的子分区。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PartitionsTopic
        """
        return self._SubTopicSets

    @SubTopicSets.setter
    def SubTopicSets(self, SubTopicSets):
        self._SubTopicSets = SubTopicSets

    @property
    def TopicType(self):
        """topic类型描述：
0：普通消息；
1：全局顺序消息；
2：局部顺序消息；
3：重试队列；
4：死信队列；
5：事务消息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Remark(self):
        """说明，128个字符以内。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        """创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最近修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ProducerLimit(self):
        """生产者上限。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProducerLimit

    @ProducerLimit.setter
    def ProducerLimit(self, ProducerLimit):
        self._ProducerLimit = ProducerLimit

    @property
    def ConsumerLimit(self):
        """消费者上限。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerLimit

    @ConsumerLimit.setter
    def ConsumerLimit(self, ConsumerLimit):
        self._ConsumerLimit = ConsumerLimit

    @property
    def PulsarTopicType(self):
        """0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PulsarTopicType

    @PulsarTopicType.setter
    def PulsarTopicType(self, PulsarTopicType):
        self._PulsarTopicType = PulsarTopicType

    @property
    def MsgTTL(self):
        """未消费消息过期时间，单位：秒

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def ClusterId(self):
        """集群 ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Tenant(self):
        """用户自定义的租户别名，如果没有，会复用专业集群 ID

        :rtype: str
        """
        return self._Tenant

    @Tenant.setter
    def Tenant(self, Tenant):
        self._Tenant = Tenant


    def _deserialize(self, params):
        self._AverageMsgSize = params.get("AverageMsgSize")
        self._ConsumerCount = params.get("ConsumerCount")
        self._LastConfirmedEntry = params.get("LastConfirmedEntry")
        self._LastLedgerCreatedTimestamp = params.get("LastLedgerCreatedTimestamp")
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._NumberOfEntries = params.get("NumberOfEntries")
        self._Partitions = params.get("Partitions")
        self._ProducerCount = params.get("ProducerCount")
        self._TotalSize = params.get("TotalSize")
        if params.get("SubTopicSets") is not None:
            self._SubTopicSets = []
            for item in params.get("SubTopicSets"):
                obj = PartitionsTopic()
                obj._deserialize(item)
                self._SubTopicSets.append(obj)
        self._TopicType = params.get("TopicType")
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ProducerLimit = params.get("ProducerLimit")
        self._ConsumerLimit = params.get("ConsumerLimit")
        self._PulsarTopicType = params.get("PulsarTopicType")
        self._MsgTTL = params.get("MsgTTL")
        self._ClusterId = params.get("ClusterId")
        self._Tenant = params.get("Tenant")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRecord(AbstractModel):
    """主题关键信息

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param _TopicName: 主题名称。
        :type TopicName: str
        """
        self._EnvironmentId = None
        self._TopicName = None

    @property
    def EnvironmentId(self):
        """环境（命名空间）名称。
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        """主题名称。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicStats(AbstractModel):
    """Topic状态

    """

    def __init__(self):
        r"""
        :param _BrokerName: 所属Broker节点
注意：此字段可能返回 null，表示取不到有效值。
        :type BrokerName: str
        :param _QueueId: 队列编号
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueId: int
        :param _MinOffset: 最小位点
注意：此字段可能返回 null，表示取不到有效值。
        :type MinOffset: int
        :param _MaxOffset: 最大位点
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxOffset: int
        :param _MessageCount: 消息条数
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageCount: int
        :param _LastUpdateTimestamp: 消息最后写入时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTimestamp: int
        """
        self._BrokerName = None
        self._QueueId = None
        self._MinOffset = None
        self._MaxOffset = None
        self._MessageCount = None
        self._LastUpdateTimestamp = None

    @property
    def BrokerName(self):
        """所属Broker节点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BrokerName

    @BrokerName.setter
    def BrokerName(self, BrokerName):
        self._BrokerName = BrokerName

    @property
    def QueueId(self):
        """队列编号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def MinOffset(self):
        """最小位点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinOffset

    @MinOffset.setter
    def MinOffset(self, MinOffset):
        self._MinOffset = MinOffset

    @property
    def MaxOffset(self):
        """最大位点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxOffset

    @MaxOffset.setter
    def MaxOffset(self, MaxOffset):
        self._MaxOffset = MaxOffset

    @property
    def MessageCount(self):
        """消息条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def LastUpdateTimestamp(self):
        """消息最后写入时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastUpdateTimestamp

    @LastUpdateTimestamp.setter
    def LastUpdateTimestamp(self, LastUpdateTimestamp):
        self._LastUpdateTimestamp = LastUpdateTimestamp


    def _deserialize(self, params):
        self._BrokerName = params.get("BrokerName")
        self._QueueId = params.get("QueueId")
        self._MinOffset = params.get("MinOffset")
        self._MaxOffset = params.get("MaxOffset")
        self._MessageCount = params.get("MessageCount")
        self._LastUpdateTimestamp = params.get("LastUpdateTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Topic_Simplification(AbstractModel):
    """主题实例

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _PulsarTopicType: 0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
注意：此字段可能返回 null，表示取不到有效值。
        :type PulsarTopicType: int
        """
        self._TopicName = None
        self._PulsarTopicType = None

    @property
    def TopicName(self):
        """主题名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def PulsarTopicType(self):
        """0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PulsarTopicType

    @PulsarTopicType.setter
    def PulsarTopicType(self, PulsarTopicType):
        self._PulsarTopicType = PulsarTopicType


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._PulsarTopicType = params.get("PulsarTopicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceResult(AbstractModel):
    """消息轨迹结果

    """

    def __init__(self):
        r"""
        :param _Stage: 阶段
        :type Stage: str
        :param _Data: 内容详情
        :type Data: str
        """
        self._Stage = None
        self._Data = None

    @property
    def Stage(self):
        """阶段
        :rtype: str
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def Data(self):
        """内容详情
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Stage = params.get("Stage")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCmqDeadLetterRequest(AbstractModel):
    """UnbindCmqDeadLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceQueueName: 死信策略源队列名称，调用本接口会清空该队列的死信队列策略。
        :type SourceQueueName: str
        """
        self._SourceQueueName = None

    @property
    def SourceQueueName(self):
        """死信策略源队列名称，调用本接口会清空该队列的死信队列策略。
        :rtype: str
        """
        return self._SourceQueueName

    @SourceQueueName.setter
    def SourceQueueName(self, SourceQueueName):
        self._SourceQueueName = SourceQueueName


    def _deserialize(self, params):
        self._SourceQueueName = params.get("SourceQueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCmqDeadLetterResponse(AbstractModel):
    """UnbindCmqDeadLetter返回参数结构体

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


class VerifyRocketMQConsumeRequest(AbstractModel):
    """VerifyRocketMQConsume请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群id
        :type ClusterId: str
        :param _NamespaceId: 命名空间
        :type NamespaceId: str
        :param _GroupId: 消费组ID
        :type GroupId: str
        :param _MsgId: 消息id
        :type MsgId: str
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _TopicName: 主题名称
        :type TopicName: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._MsgId = None
        self._ClientId = None
        self._TopicName = None

    @property
    def ClusterId(self):
        """集群id
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        """命名空间
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        """消费组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MsgId(self):
        """消息id
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def ClientId(self):
        """客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def TopicName(self):
        """主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._MsgId = params.get("MsgId")
        self._ClientId = params.get("ClientId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyRocketMQConsumeResponse(AbstractModel):
    """VerifyRocketMQConsume返回参数结构体

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


class VirtualHostQuota(AbstractModel):
    """vhost使用配额信息

    """

    def __init__(self):
        r"""
        :param _MaxVirtualHost: 允许创建最大vhost数
        :type MaxVirtualHost: int
        :param _UsedVirtualHost: 已创建vhost数
        :type UsedVirtualHost: int
        """
        self._MaxVirtualHost = None
        self._UsedVirtualHost = None

    @property
    def MaxVirtualHost(self):
        """允许创建最大vhost数
        :rtype: int
        """
        return self._MaxVirtualHost

    @MaxVirtualHost.setter
    def MaxVirtualHost(self, MaxVirtualHost):
        self._MaxVirtualHost = MaxVirtualHost

    @property
    def UsedVirtualHost(self):
        """已创建vhost数
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
        


class VpcBindRecord(AbstractModel):
    """vcp绑定记录

    """

    def __init__(self):
        r"""
        :param _UniqueVpcId: 租户Vpc Id
        :type UniqueVpcId: str
        :param _UniqueSubnetId: 租户Vpc子网Id
        :type UniqueSubnetId: str
        :param _RouterId: 路由Id
        :type RouterId: str
        :param _Ip: Vpc的Id
        :type Ip: str
        :param _Port: Vpc的Port
        :type Port: int
        :param _Remark: 说明，128个字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._RouterId = None
        self._Ip = None
        self._Port = None
        self._Remark = None

    @property
    def UniqueVpcId(self):
        """租户Vpc Id
        :rtype: str
        """
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        """租户Vpc子网Id
        :rtype: str
        """
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def RouterId(self):
        """路由Id
        :rtype: str
        """
        return self._RouterId

    @RouterId.setter
    def RouterId(self, RouterId):
        self._RouterId = RouterId

    @property
    def Ip(self):
        """Vpc的Id
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Vpc的Port
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Remark(self):
        """说明，128个字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._RouterId = params.get("RouterId")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConfig(AbstractModel):
    """VPC配置信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc的id
        :type VpcId: str
        :param _SubnetId: 子网id
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
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
        :param _VpcDataStreamEndpointStatus: vpc接入点状态 OFF/ON/CREATING/DELETING
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
        """vpc接入点状态 OFF/ON/CREATING/DELETING
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
        


class VpcInfo(AbstractModel):
    """vpc信息（由UniqVpcId和UniqSubnetId组成）

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc信息
        :type VpcId: str
        :param _SubnetId: 子网信息
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        """vpc信息
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网信息
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        