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
        :param MaxTpsPerVHost: 单Vhost TPS上限
        :type MaxTpsPerVHost: int
        :param MaxConnNumPerVHost: 单Vhost客户端连接数上限
        :type MaxConnNumPerVHost: int
        :param MaxVHostNum: 最大Vhost数量
        :type MaxVHostNum: int
        :param MaxExchangeNum: 最大exchange数量
        :type MaxExchangeNum: int
        :param MaxQueueNum: 最大Queue数量
        :type MaxQueueNum: int
        :param MaxRetentionTime: 消息最大保留时间，以毫秒为单位
        :type MaxRetentionTime: int
        :param UsedVHostNum: 已使用Vhost数量
        :type UsedVHostNum: int
        :param UsedExchangeNum: 已使用exchange数量
        :type UsedExchangeNum: int
        :param UsedQueueNum: 已使用queue数量
        :type UsedQueueNum: int
        """
        self.MaxTpsPerVHost = None
        self.MaxConnNumPerVHost = None
        self.MaxVHostNum = None
        self.MaxExchangeNum = None
        self.MaxQueueNum = None
        self.MaxRetentionTime = None
        self.UsedVHostNum = None
        self.UsedExchangeNum = None
        self.UsedQueueNum = None


    def _deserialize(self, params):
        self.MaxTpsPerVHost = params.get("MaxTpsPerVHost")
        self.MaxConnNumPerVHost = params.get("MaxConnNumPerVHost")
        self.MaxVHostNum = params.get("MaxVHostNum")
        self.MaxExchangeNum = params.get("MaxExchangeNum")
        self.MaxQueueNum = params.get("MaxQueueNum")
        self.MaxRetentionTime = params.get("MaxRetentionTime")
        self.UsedVHostNum = params.get("UsedVHostNum")
        self.UsedExchangeNum = params.get("UsedExchangeNum")
        self.UsedQueueNum = params.get("UsedQueueNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPClusterDetail(AbstractModel):
    """租户AMQP集群详细信息

    """

    def __init__(self):
        r"""
        :param Info: 集群基本信息
        :type Info: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterInfo`
        :param Config: 集群配置信息
        :type Config: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterConfig`
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.Info = None
        self.Config = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = AMQPClusterInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("Config") is not None:
            self.Config = AMQPClusterConfig()
            self.Config._deserialize(params.get("Config"))
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
        


class AMQPClusterInfo(AbstractModel):
    """AMQP集群基本信息

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Region: 地域信息
        :type Region: str
        :param CreateTime: 创建时间，毫秒为单位
        :type CreateTime: int
        :param Remark: 集群说明信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param PublicEndPoint: 公网接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicEndPoint: str
        :param VpcEndPoint: VPC接入地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcEndPoint: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.CreateTime = None
        self.Remark = None
        self.PublicEndPoint = None
        self.VpcEndPoint = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")
        self.PublicEndPoint = params.get("PublicEndPoint")
        self.VpcEndPoint = params.get("VpcEndPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPClusterRecentStats(AbstractModel):
    """AMQP集群近期使用量

    """

    def __init__(self):
        r"""
        :param QueueNum: Queue数量
        :type QueueNum: int
        :param ProducedMsgNum: 消息生产数
        :type ProducedMsgNum: int
        :param AccumulativeMsgNum: 消息堆积数
        :type AccumulativeMsgNum: int
        :param ExchangeNum: Exchange数量
        :type ExchangeNum: int
        """
        self.QueueNum = None
        self.ProducedMsgNum = None
        self.AccumulativeMsgNum = None
        self.ExchangeNum = None


    def _deserialize(self, params):
        self.QueueNum = params.get("QueueNum")
        self.ProducedMsgNum = params.get("ProducedMsgNum")
        self.AccumulativeMsgNum = params.get("AccumulativeMsgNum")
        self.ExchangeNum = params.get("ExchangeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPExchange(AbstractModel):
    """AMQP Exchange信息

    """

    def __init__(self):
        r"""
        :param Name: Exchange名称
        :type Name: str
        :param Type: Exchange的类别，为枚举类型:Direct, Fanout, Topic
        :type Type: str
        :param SourceBindedNum: 主绑定数
        :type SourceBindedNum: int
        :param Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param DestBindedNum: 被绑定数
        :type DestBindedNum: int
        :param CreateTime: 创建时间，以毫秒为单位
        :type CreateTime: int
        :param UpdateTime: 创建时间，以毫秒为单位
        :type UpdateTime: int
        :param Internal: 是否为内部Exchange(以amq.前缀开头的)
        :type Internal: bool
        """
        self.Name = None
        self.Type = None
        self.SourceBindedNum = None
        self.Remark = None
        self.DestBindedNum = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Internal = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.SourceBindedNum = params.get("SourceBindedNum")
        self.Remark = params.get("Remark")
        self.DestBindedNum = params.get("DestBindedNum")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Internal = params.get("Internal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPQueueDetail(AbstractModel):
    """AMQP 队列信息

    """

    def __init__(self):
        r"""
        :param Name: Queue名称
        :type Name: str
        :param Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param DestBindedNum: 被绑定数
注意：此字段可能返回 null，表示取不到有效值。
        :type DestBindedNum: int
        :param CreateTime: 创建时间，以毫秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 创建时间，以毫秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param OnlineConsumerNum: 在线消费者数
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineConsumerNum: int
        :param Tps: 每秒钟的事务数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tps: int
        :param AccumulativeMsgNum: 消息堆积数
注意：此字段可能返回 null，表示取不到有效值。
        :type AccumulativeMsgNum: int
        :param AutoDelete: 是否自动删除
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoDelete: bool
        :param DeadLetterExchange: 死信交换机
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterExchange: str
        :param DeadLetterRoutingKey: 死信交换机路由键
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterRoutingKey: str
        """
        self.Name = None
        self.Remark = None
        self.DestBindedNum = None
        self.CreateTime = None
        self.UpdateTime = None
        self.OnlineConsumerNum = None
        self.Tps = None
        self.AccumulativeMsgNum = None
        self.AutoDelete = None
        self.DeadLetterExchange = None
        self.DeadLetterRoutingKey = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.DestBindedNum = params.get("DestBindedNum")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.OnlineConsumerNum = params.get("OnlineConsumerNum")
        self.Tps = params.get("Tps")
        self.AccumulativeMsgNum = params.get("AccumulativeMsgNum")
        self.AutoDelete = params.get("AutoDelete")
        self.DeadLetterExchange = params.get("DeadLetterExchange")
        self.DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPRouteRelation(AbstractModel):
    """AMQP路由关系

    """

    def __init__(self):
        r"""
        :param RouteRelationId: 路由关系ID
        :type RouteRelationId: str
        :param SourceExchange: 源Exchange
        :type SourceExchange: str
        :param DestType: 目标类型:Queue|Exchange
        :type DestType: str
        :param DestValue: 目标值
        :type DestValue: str
        :param RoutingKey: 绑定key
        :type RoutingKey: str
        :param SourceExchangeType: 源路由类型:Direct|Topic|Fanout
        :type SourceExchangeType: str
        :param CreateTime: 创建时间，以毫秒为单位
        :type CreateTime: int
        :param UpdateTime: 修改时间，以毫秒为单位
        :type UpdateTime: int
        :param Remark: 说明信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.RouteRelationId = None
        self.SourceExchange = None
        self.DestType = None
        self.DestValue = None
        self.RoutingKey = None
        self.SourceExchangeType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.RouteRelationId = params.get("RouteRelationId")
        self.SourceExchange = params.get("SourceExchange")
        self.DestType = params.get("DestType")
        self.DestValue = params.get("DestValue")
        self.RoutingKey = params.get("RoutingKey")
        self.SourceExchangeType = params.get("SourceExchangeType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AMQPVHost(AbstractModel):
    """vhostd信息

    """

    def __init__(self):
        r"""
        :param VHostId: 命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type VHostId: str
        :param MsgTtl: 未消费消息的保留时间，以毫秒单位，范围60秒到15天
        :type MsgTtl: int
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间，以毫秒为单位
        :type CreateTime: int
        :param UpdateTime: 更新时间，以毫秒为单位
        :type UpdateTime: int
        :param Username: 用户名
        :type Username: str
        :param Password: 密码
        :type Password: str
        """
        self.VHostId = None
        self.MsgTtl = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.VHostId = params.get("VHostId")
        self.MsgTtl = params.get("MsgTtl")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcknowledgeMessageRequest(AbstractModel):
    """AcknowledgeMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param MessageId: 用作标识消息的唯一的ID（可从 receiveMessage 的返回值中获得）
        :type MessageId: str
        :param AckTopic: Topic 名字（可从 receiveMessage 的返回值中获得）这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :type AckTopic: str
        :param SubName: 订阅者的名字，可以从receiveMessage的返回值中获取到。这里尽量与receiveMessage中的订阅者保持一致，否则没办法正确ack 接收回来的消息。
        :type SubName: str
        """
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
        r"""
        :param ErrorMsg: 如果为“”，则说明没有错误返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class BindCluster(AbstractModel):
    """用户专享集群信息

    """

    def __init__(self):
        r"""
        :param ClusterName: 物理集群的名称
        :type ClusterName: str
        """
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
        r"""
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
        :type Status: int
        :param MaxNamespaceNum: 最大命名空间数量
        :type MaxNamespaceNum: int
        :param MaxTopicNum: 最大Topic数量
        :type MaxTopicNum: int
        :param MaxQps: 最大QPS
        :type MaxQps: int
        :param MessageRetentionTime: 最大消息保留时间，秒为单位
        :type MessageRetentionTime: int
        :param MaxStorageCapacity: 最大存储容量
        :type MaxStorageCapacity: int
        :param Version: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param PublicEndPoint: 公网访问接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicEndPoint: str
        :param VpcEndPoint: VPC访问接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcEndPoint: str
        :param NamespaceNum: 命名空间数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceNum: int
        :param UsedStorageBudget: 已使用存储限制，MB为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedStorageBudget: int
        :param MaxPublishRateInMessages: 最大生产消息速率，以条数为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPublishRateInMessages: int
        :param MaxDispatchRateInMessages: 最大推送消息速率，以条数为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDispatchRateInMessages: int
        :param MaxPublishRateInBytes: 最大生产消息速率，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPublishRateInBytes: int
        :param MaxDispatchRateInBytes: 最大推送消息速率，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDispatchRateInBytes: int
        :param TopicNum: 已创建主题数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNum: int
        :param MaxMessageDelayInSeconds: 最长消息延时，以秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMessageDelayInSeconds: int
        :param PublicAccessEnabled: 是否开启公网访问，不填时默认开启
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicAccessEnabled: bool
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param PayMode: 计费模式：
0: 按量计费
1: 包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
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
        self.Version = None
        self.PublicEndPoint = None
        self.VpcEndPoint = None
        self.NamespaceNum = None
        self.UsedStorageBudget = None
        self.MaxPublishRateInMessages = None
        self.MaxDispatchRateInMessages = None
        self.MaxPublishRateInBytes = None
        self.MaxDispatchRateInBytes = None
        self.TopicNum = None
        self.MaxMessageDelayInSeconds = None
        self.PublicAccessEnabled = None
        self.Tags = None
        self.PayMode = None


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
        self.UsedStorageBudget = params.get("UsedStorageBudget")
        self.MaxPublishRateInMessages = params.get("MaxPublishRateInMessages")
        self.MaxDispatchRateInMessages = params.get("MaxDispatchRateInMessages")
        self.MaxPublishRateInBytes = params.get("MaxPublishRateInBytes")
        self.MaxDispatchRateInBytes = params.get("MaxDispatchRateInBytes")
        self.TopicNum = params.get("TopicNum")
        self.MaxMessageDelayInSeconds = params.get("MaxMessageDelayInSeconds")
        self.PublicAccessEnabled = params.get("PublicAccessEnabled")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.PayMode = params.get("PayMode")
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
        r"""
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
        r"""
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
        r"""
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
        :param Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param MaxUnackedMsgNum: 最大未确认消息数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxUnackedMsgNum: int
        :param MaxMsgBacklogSize: 最大消息堆积大小（字节）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMsgBacklogSize: int
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
        self.Status = None
        self.MaxUnackedMsgNum = None
        self.MaxMsgBacklogSize = None


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
        self.Status = params.get("Status")
        self.MaxUnackedMsgNum = params.get("MaxUnackedMsgNum")
        self.MaxMsgBacklogSize = params.get("MaxMsgBacklogSize")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param Partition: 消费者连接的主题分区号
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: int
        """
        self.ConnectedSince = None
        self.ConsumerAddr = None
        self.ConsumerName = None
        self.ClientVersion = None
        self.Partition = None


    def _deserialize(self, params):
        self.ConnectedSince = params.get("ConnectedSince")
        self.ConsumerAddr = params.get("ConsumerAddr")
        self.ConsumerName = params.get("ConsumerName")
        self.ClientVersion = params.get("ClientVersion")
        self.Partition = params.get("Partition")
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAMQPClusterRequest(AbstractModel):
    """CreateAMQPCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 3-64个字符，只能包含字母、数字、“-”及“_”
        :type Name: str
        :param Remark: 集群描述，128个字符以内
        :type Remark: str
        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAMQPClusterResponse(AbstractModel):
    """CreateAMQPCluster返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateAMQPExchangeRequest(AbstractModel):
    """CreateAMQPExchange请求参数结构体

    """

    def __init__(self):
        r"""
        :param Exchange: 交换机名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type Exchange: str
        :param VHosts: 交换机所在的vhost，目前支持在单个vhost下创建主题
        :type VHosts: list of str
        :param Type: 交换机类型，可选值为Direct, Fanout, Topic
        :type Type: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Remark: 交换机说明，最大128个字符
        :type Remark: str
        :param AlternateExchange: 备用交换机名称
        :type AlternateExchange: str
        """
        self.Exchange = None
        self.VHosts = None
        self.Type = None
        self.ClusterId = None
        self.Remark = None
        self.AlternateExchange = None


    def _deserialize(self, params):
        self.Exchange = params.get("Exchange")
        self.VHosts = params.get("VHosts")
        self.Type = params.get("Type")
        self.ClusterId = params.get("ClusterId")
        self.Remark = params.get("Remark")
        self.AlternateExchange = params.get("AlternateExchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAMQPExchangeResponse(AbstractModel):
    """CreateAMQPExchange返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAMQPQueueRequest(AbstractModel):
    """CreateAMQPQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param Queue: 队列名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type Queue: str
        :param VHostId: 队列所在的vhost名称
        :type VHostId: str
        :param AutoDelete: 是否自动清除
        :type AutoDelete: bool
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Remark: 队列说明，最大128个字符
        :type Remark: str
        :param DeadLetterExchange: 死信exchange
        :type DeadLetterExchange: str
        :param DeadLetterRoutingKey: 路由键
        :type DeadLetterRoutingKey: str
        """
        self.Queue = None
        self.VHostId = None
        self.AutoDelete = None
        self.ClusterId = None
        self.Remark = None
        self.DeadLetterExchange = None
        self.DeadLetterRoutingKey = None


    def _deserialize(self, params):
        self.Queue = params.get("Queue")
        self.VHostId = params.get("VHostId")
        self.AutoDelete = params.get("AutoDelete")
        self.ClusterId = params.get("ClusterId")
        self.Remark = params.get("Remark")
        self.DeadLetterExchange = params.get("DeadLetterExchange")
        self.DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAMQPQueueResponse(AbstractModel):
    """CreateAMQPQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAMQPRouteRelationRequest(AbstractModel):
    """CreateAMQPRouteRelation请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: 交换机所在的vhost
        :type VHostId: str
        :param SourceExchange: 源Exchange名称
        :type SourceExchange: str
        :param DestType: 目标类型:Queue|Exchange
        :type DestType: str
        :param DestValue: 目标值
        :type DestValue: str
        :param Remark: 交换机说明，最大128个字符
        :type Remark: str
        :param RoutingKey: 绑定key,缺省值为default
        :type RoutingKey: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.SourceExchange = None
        self.DestType = None
        self.DestValue = None
        self.Remark = None
        self.RoutingKey = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.SourceExchange = params.get("SourceExchange")
        self.DestType = params.get("DestType")
        self.DestValue = params.get("DestValue")
        self.Remark = params.get("Remark")
        self.RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAMQPRouteRelationResponse(AbstractModel):
    """CreateAMQPRouteRelation返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAMQPVHostRequest(AbstractModel):
    """CreateAMQPVHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: vhost名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type VHostId: str
        :param MsgTtl: 未消费消息的保留时间，以毫秒为单位，60秒-15天
        :type MsgTtl: int
        :param Remark: 说明，最大128个字符
        :type Remark: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.MsgTtl = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.MsgTtl = params.get("MsgTtl")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAMQPVHostResponse(AbstractModel):
    """CreateAMQPVHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterName: 集群名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。
        :type ClusterName: str
        :param BindClusterId: 用户专享物理集群ID，如果不传，则默认在公共集群上创建用户集群资源。
        :type BindClusterId: int
        :param Remark: 说明，128个字符以内。
        :type Remark: str
        :param Tags: 集群的标签列表(已废弃)
        :type Tags: list of Tag
        :param PublicAccessEnabled: 是否开启公网访问，不填时默认开启
        :type PublicAccessEnabled: bool
        """
        self.ClusterName = None
        self.BindClusterId = None
        self.Remark = None
        self.Tags = None
        self.PublicAccessEnabled = None


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
        self.PublicAccessEnabled = params.get("PublicAccessEnabled")
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
        r"""
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
        r"""
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
        :param Tags: 标签数组
        :type Tags: list of Tag
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
        self.Tags = None


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
        


class CreateCmqQueueResponse(AbstractModel):
    """CreateCmqQueue返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param Tags: 标签数组
        :type Tags: list of Tag
        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.FilterType = None
        self.MsgRetentionSeconds = None
        self.Trace = None
        self.Tags = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.FilterType = params.get("FilterType")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")
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
        


class CreateCmqTopicResponse(AbstractModel):
    """CreateCmqTopic返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param EnvironmentId: 环境（命名空间）名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒，最小60，最大1296000，（15天）。
        :type MsgTTL: int
        :param Remark: 说明，128个字符以内。
        :type Remark: str
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param RetentionPolicy: 消息保留策略
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None
        self.RetentionPolicy = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        if params.get("RetentionPolicy") is not None:
            self.RetentionPolicy = RetentionPolicy()
            self.RetentionPolicy._deserialize(params.get("RetentionPolicy"))
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
        r"""
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


class CreateEnvironmentRoleRequest(AbstractModel):
    """CreateEnvironmentRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param RoleName: 角色名称。
        :type RoleName: str
        :param Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.RoleName = None
        self.Permissions = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.RoleName = params.get("RoleName")
        self.Permissions = params.get("Permissions")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRoleResponse(AbstractModel):
    """CreateEnvironmentRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRocketMQClusterRequest(AbstractModel):
    """CreateRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 集群名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type Name: str
        :param Remark: 集群描述，128个字符以内
        :type Remark: str
        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQClusterResponse(AbstractModel):
    """CreateRocketMQCluster返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateRocketMQGroupRequest(AbstractModel):
    """CreateRocketMQGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: Group名称，8~64个字符
        :type GroupId: str
        :param Namespaces: 命名空间，目前只支持单个命名空间
        :type Namespaces: list of str
        :param ReadEnable: 是否开启消费
        :type ReadEnable: bool
        :param BroadcastEnable: 是否开启广播消费
        :type BroadcastEnable: bool
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Remark: 说明信息，最长128个字符
        :type Remark: str
        """
        self.GroupId = None
        self.Namespaces = None
        self.ReadEnable = None
        self.BroadcastEnable = None
        self.ClusterId = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Namespaces = params.get("Namespaces")
        self.ReadEnable = params.get("ReadEnable")
        self.BroadcastEnable = params.get("BroadcastEnable")
        self.ClusterId = params.get("ClusterId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQGroupResponse(AbstractModel):
    """CreateRocketMQGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRocketMQNamespaceRequest(AbstractModel):
    """CreateRocketMQNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type NamespaceId: str
        :param Ttl: 未消费消息的保留时间，以毫秒为单位，60秒-15天
        :type Ttl: int
        :param RetentionTime: 消息持久化后保留的时间，以毫秒为单位
        :type RetentionTime: int
        :param Remark: 说明，最大128个字符
        :type Remark: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Ttl = None
        self.RetentionTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Ttl = params.get("Ttl")
        self.RetentionTime = params.get("RetentionTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQNamespaceResponse(AbstractModel):
    """CreateRocketMQNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRocketMQTopicRequest(AbstractModel):
    """CreateRocketMQTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param Topic: 主题名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type Topic: str
        :param Namespaces: 主题所在的命名空间，目前支持在单个命名空间下创建主题
        :type Namespaces: list of str
        :param Type: 主题类型，可选值为Normal, GlobalOrder, PartitionedOrder
        :type Type: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Remark: 主题说明，最大128个字符
        :type Remark: str
        :param PartitionNum: 分区数，全局顺序无效
        :type PartitionNum: int
        """
        self.Topic = None
        self.Namespaces = None
        self.Type = None
        self.ClusterId = None
        self.Remark = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Namespaces = params.get("Namespaces")
        self.Type = params.get("Type")
        self.ClusterId = params.get("ClusterId")
        self.Remark = params.get("Remark")
        self.PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQTopicResponse(AbstractModel):
    """CreateRocketMQTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :type RoleName: str
        :param Remark: 备注说明，长度必须大等于0且小等于128。
        :type Remark: str
        :param ClusterId: 必填字段，集群Id
        :type ClusterId: str
        """
        self.RoleName = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称
        :type RoleName: str
        :param Token: 角色token
        :type Token: str
        :param Remark: 备注说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoleName = None
        self.Token = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Token = params.get("Token")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class CreateSubscriptionRequest(AbstractModel):
    """CreateSubscription请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param PostFixPattern: 指定死信和重试主题名称规范，LEGACY表示历史命名规则，COMMUNITY表示Pulsar社区命名规范
        :type PostFixPattern: str
        """
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
        r"""
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
        r"""
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名，不支持中字以及除了短线和下划线外的特殊字符且不超过64个字符。
        :type TopicName: str
        :param Partitions: 0：非分区topic，无分区；非0：具体分区topic的分区数，最大不允许超过128。
        :type Partitions: int
        :param Remark: 备注，128字符以内。
        :type Remark: str
        :param TopicType: 0： 普通消息；
1 ：全局顺序消息；
2 ：局部顺序消息；
3 ：重试队列；
4 ：死信队列。
        :type TopicType: int
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        :param PulsarTopicType: Pulsar 主题类型
0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
        :type PulsarTopicType: int
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.Remark = None
        self.TopicType = None
        self.ClusterId = None
        self.PulsarTopicType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.TopicType = params.get("TopicType")
        self.ClusterId = params.get("ClusterId")
        self.PulsarTopicType = params.get("PulsarTopicType")
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
        r"""
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


class DeleteAMQPClusterRequest(AbstractModel):
    """DeleteAMQPCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 待删除的集群Id。
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAMQPClusterResponse(AbstractModel):
    """DeleteAMQPCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAMQPExchangeRequest(AbstractModel):
    """DeleteAMQPExchange请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost名称
        :type VHostId: str
        :param Exchange: 交换机名称
        :type Exchange: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.Exchange = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.Exchange = params.get("Exchange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAMQPExchangeResponse(AbstractModel):
    """DeleteAMQPExchange返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAMQPQueueRequest(AbstractModel):
    """DeleteAMQPQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost名称
        :type VHostId: str
        :param Queue: 队列名称
        :type Queue: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.Queue = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.Queue = params.get("Queue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAMQPQueueResponse(AbstractModel):
    """DeleteAMQPQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAMQPRouteRelationRequest(AbstractModel):
    """DeleteAMQPRouteRelation请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost名称
        :type VHostId: str
        :param RouteRelationId: 路由关系ID
        :type RouteRelationId: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.RouteRelationId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.RouteRelationId = params.get("RouteRelationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAMQPRouteRelationResponse(AbstractModel):
    """DeleteAMQPRouteRelation返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAMQPVHostRequest(AbstractModel):
    """DeleteAMQPVHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: vhost名称
        :type VHostId: str
        """
        self.ClusterId = None
        self.VHostId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAMQPVHostResponse(AbstractModel):
    """DeleteAMQPVHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id，传入需要删除的集群Id。
        :type ClusterId: str
        """
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
        r"""
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
        r"""
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type QueueName: str
        """
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
        :type TopicName: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEnvironmentRolesRequest(AbstractModel):
    """DeleteEnvironmentRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param RoleNames: 角色名称数组。
        :type RoleNames: list of str
        :param ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.RoleNames = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.RoleNames = params.get("RoleNames")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRolesResponse(AbstractModel):
    """DeleteEnvironmentRoles返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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


class DeleteRocketMQClusterRequest(AbstractModel):
    """DeleteRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 待删除的集群Id。
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQClusterResponse(AbstractModel):
    """DeleteRocketMQCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRocketMQGroupRequest(AbstractModel):
    """DeleteRocketMQGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param GroupId: 消费组名称
        :type GroupId: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQGroupResponse(AbstractModel):
    """DeleteRocketMQGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRocketMQNamespaceRequest(AbstractModel):
    """DeleteRocketMQNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间名称
        :type NamespaceId: str
        """
        self.ClusterId = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQNamespaceResponse(AbstractModel):
    """DeleteRocketMQNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRocketMQTopicRequest(AbstractModel):
    """DeleteRocketMQTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param Topic: 主题名称
        :type Topic: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Topic = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQTopicResponse(AbstractModel):
    """DeleteRocketMQTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRolesRequest(AbstractModel):
    """DeleteRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleNames: 角色名称数组。
        :type RoleNames: list of str
        :param ClusterId: 必填字段，集群Id
        :type ClusterId: str
        """
        self.RoleNames = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.RoleNames = params.get("RoleNames")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolesResponse(AbstractModel):
    """DeleteRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoleNames: 成功删除的角色名称数组。
        :type RoleNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoleNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleNames = params.get("RoleNames")
        self.RequestId = params.get("RequestId")


class DeleteSubscriptionsRequest(AbstractModel):
    """DeleteSubscriptions请求参数结构体

    """

    def __init__(self):
        r"""
        :param SubscriptionTopicSets: 订阅关系集合，每次最多删除20个。
        :type SubscriptionTopicSets: list of SubscriptionTopic
        :param ClusterId: pulsar集群Id。
        :type ClusterId: str
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param Force: 是否强制删除，默认为false
        :type Force: bool
        """
        self.SubscriptionTopicSets = None
        self.ClusterId = None
        self.EnvironmentId = None
        self.Force = None


    def _deserialize(self, params):
        if params.get("SubscriptionTopicSets") is not None:
            self.SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self.SubscriptionTopicSets.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.Force = params.get("Force")
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
        r"""
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
        r"""
        :param TopicSets: 主题集合，每次最多删除20个。
        :type TopicSets: list of TopicRecord
        :param ClusterId: pulsar集群Id。
        :type ClusterId: str
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param Force: 是否强制删除，默认为false
        :type Force: bool
        """
        self.TopicSets = None
        self.ClusterId = None
        self.EnvironmentId = None
        self.Force = None


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self.TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self.TopicSets.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.Force = params.get("Force")
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
        r"""
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


class DescribeAMQPClusterRequest(AbstractModel):
    """DescribeAMQPCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAMQPClusterResponse(AbstractModel):
    """DescribeAMQPCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterInfo: 集群信息
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterInfo`
        :param ClusterConfig: 集群配置
        :type ClusterConfig: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterConfig`
        :param ClusterStats: 集群最近使用量
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStats: :class:`tencentcloud.tdmq.v20200217.models.AMQPClusterRecentStats`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterInfo = None
        self.ClusterConfig = None
        self.ClusterStats = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterInfo") is not None:
            self.ClusterInfo = AMQPClusterInfo()
            self.ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("ClusterConfig") is not None:
            self.ClusterConfig = AMQPClusterConfig()
            self.ClusterConfig._deserialize(params.get("ClusterConfig"))
        if params.get("ClusterStats") is not None:
            self.ClusterStats = AMQPClusterRecentStats()
            self.ClusterStats._deserialize(params.get("ClusterStats"))
        self.RequestId = params.get("RequestId")


class DescribeAMQPClustersRequest(AbstractModel):
    """DescribeAMQPClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param IdKeyword: 按照集群ID关键字搜索
        :type IdKeyword: str
        :param NameKeyword: 按照集群名称关键字搜索
        :type NameKeyword: str
        :param ClusterIdList: 集群ID列表过滤
        :type ClusterIdList: list of str
        :param IsTagFilter: 标签过滤查找时，需要设置为true
        :type IsTagFilter: bool
        :param Filters: 过滤器。目前支持按标签过滤。
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.IdKeyword = None
        self.NameKeyword = None
        self.ClusterIdList = None
        self.IsTagFilter = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IdKeyword = params.get("IdKeyword")
        self.NameKeyword = params.get("NameKeyword")
        self.ClusterIdList = params.get("ClusterIdList")
        self.IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeAMQPClustersResponse(AbstractModel):
    """DescribeAMQPClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterList: 集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of AMQPClusterDetail
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = AMQPClusterDetail()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAMQPCreateQuotaRequest(AbstractModel):
    """DescribeAMQPCreateQuota请求参数结构体

    """


class DescribeAMQPCreateQuotaResponse(AbstractModel):
    """DescribeAMQPCreateQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param MaxClusterNum: 租户总共可使用集群数量
        :type MaxClusterNum: int
        :param UsedClusterNum: 租户已创建集群数量
        :type UsedClusterNum: int
        :param ExchangeCapacity: Exchange容量
        :type ExchangeCapacity: int
        :param QueueCapacity: Queue容量
        :type QueueCapacity: int
        :param MaxTpsPerVHost: 单Vhost TPS
        :type MaxTpsPerVHost: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaxClusterNum = None
        self.UsedClusterNum = None
        self.ExchangeCapacity = None
        self.QueueCapacity = None
        self.MaxTpsPerVHost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxClusterNum = params.get("MaxClusterNum")
        self.UsedClusterNum = params.get("UsedClusterNum")
        self.ExchangeCapacity = params.get("ExchangeCapacity")
        self.QueueCapacity = params.get("QueueCapacity")
        self.MaxTpsPerVHost = params.get("MaxTpsPerVHost")
        self.RequestId = params.get("RequestId")


class DescribeAMQPExchangesRequest(AbstractModel):
    """DescribeAMQPExchanges请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询限制数
        :type Limit: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost ID
        :type VHostId: str
        :param FilterType: 按路由类型过滤查询结果，可选择Direct, Fanout, Topic
        :type FilterType: list of str
        :param FilterName: 按exchange名称搜索，支持模糊查询
        :type FilterName: str
        :param FilterInternal: 过滤查询内部或者外部exchange
        :type FilterInternal: bool
        """
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.VHostId = None
        self.FilterType = None
        self.FilterName = None
        self.FilterInternal = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.FilterType = params.get("FilterType")
        self.FilterName = params.get("FilterName")
        self.FilterInternal = params.get("FilterInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAMQPExchangesResponse(AbstractModel):
    """DescribeAMQPExchanges返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Exchanges: 主题信息列表
        :type Exchanges: list of AMQPExchange
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Exchanges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Exchanges") is not None:
            self.Exchanges = []
            for item in params.get("Exchanges"):
                obj = AMQPExchange()
                obj._deserialize(item)
                self.Exchanges.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAMQPQueuesRequest(AbstractModel):
    """DescribeAMQPQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询限制数
        :type Limit: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost名称
        :type VHostId: str
        :param NameKeyword: 按队列名称搜索，支持模糊查询
        :type NameKeyword: str
        :param SortOrder: 查询结果排序规则，ASC为升序，DESC为降序
        :type SortOrder: str
        :param SortedBy: 对查询结果排序，此为排序字段，目前支持Accumulative（消息堆积量）、Tps
        :type SortedBy: str
        :param FilterOneQueue: 队列名称，指定此参数后将只返回该队列信息
        :type FilterOneQueue: str
        """
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.VHostId = None
        self.NameKeyword = None
        self.SortOrder = None
        self.SortedBy = None
        self.FilterOneQueue = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.NameKeyword = params.get("NameKeyword")
        self.SortOrder = params.get("SortOrder")
        self.SortedBy = params.get("SortedBy")
        self.FilterOneQueue = params.get("FilterOneQueue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAMQPQueuesResponse(AbstractModel):
    """DescribeAMQPQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Queues: 队列信息列表
        :type Queues: list of AMQPQueueDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Queues = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Queues") is not None:
            self.Queues = []
            for item in params.get("Queues"):
                obj = AMQPQueueDetail()
                obj._deserialize(item)
                self.Queues.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAMQPRouteRelationsRequest(AbstractModel):
    """DescribeAMQPRouteRelations请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询限制数
        :type Limit: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost名称
        :type VHostId: str
        :param FilterSourceExchange: 按源exchange名称过滤查询结果，支持模糊查询
        :type FilterSourceExchange: str
        :param FilterDestType: 按绑定的目标类型过滤查询结果，可选值:Exchange、Queue
        :type FilterDestType: str
        :param FilterDestValue: 按目标名称过滤查询结果，支持模糊查询
        :type FilterDestValue: str
        """
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.VHostId = None
        self.FilterSourceExchange = None
        self.FilterDestType = None
        self.FilterDestValue = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.FilterSourceExchange = params.get("FilterSourceExchange")
        self.FilterDestType = params.get("FilterDestType")
        self.FilterDestValue = params.get("FilterDestValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAMQPRouteRelationsResponse(AbstractModel):
    """DescribeAMQPRouteRelations返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param RouteRelations: 路由关系列表
        :type RouteRelations: list of AMQPRouteRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteRelations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteRelations") is not None:
            self.RouteRelations = []
            for item in params.get("RouteRelations"):
                obj = AMQPRouteRelation()
                obj._deserialize(item)
                self.RouteRelations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAMQPVHostsRequest(AbstractModel):
    """DescribeAMQPVHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param NameKeyword: 按名称搜索
        :type NameKeyword: str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.NameKeyword = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NameKeyword = params.get("NameKeyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAMQPVHostsResponse(AbstractModel):
    """DescribeAMQPVHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param VHosts: Vhost 列表
        :type VHosts: list of AMQPVHost
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VHosts = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VHosts") is not None:
            self.VHosts = []
            for item in params.get("VHosts"):
                obj = AMQPVHost()
                obj._deserialize(item)
                self.VHosts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAllTenantsRequest(AbstractModel):
    """DescribeAllTenants请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询限制条数
        :type Limit: int
        :param ClusterName: 物理集群名称
        :type ClusterName: str
        :param TenantId: 虚拟集群ID
        :type TenantId: str
        :param TenantName: 虚拟集群名称
        :type TenantName: str
        :param Types: 协议类型数组
        :type Types: list of str
        :param SortBy: 排序字段名，支持createTime，updateTime
        :type SortBy: str
        :param SortOrder: 升序排列ASC，降序排列DESC
        :type SortOrder: str
        """
        self.Offset = None
        self.Limit = None
        self.ClusterName = None
        self.TenantId = None
        self.TenantName = None
        self.Types = None
        self.SortBy = None
        self.SortOrder = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterName = params.get("ClusterName")
        self.TenantId = params.get("TenantId")
        self.TenantName = params.get("TenantName")
        self.Types = params.get("Types")
        self.SortBy = params.get("SortBy")
        self.SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllTenantsResponse(AbstractModel):
    """DescribeAllTenants返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param Tenants: 虚拟集群列表
        :type Tenants: list of InternalTenant
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tenants = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tenants") is not None:
            self.Tenants = []
            for item in params.get("Tenants"):
                obj = InternalTenant()
                obj._deserialize(item)
                self.Tenants.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBindClustersRequest(AbstractModel):
    """DescribeBindClusters请求参数结构体

    """


class DescribeBindClustersResponse(AbstractModel):
    """DescribeBindClusters返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param ClusterId: 集群的ID
        :type ClusterId: str
        """
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
        r"""
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
        r"""
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param ClusterIdList: 集群ID列表过滤
        :type ClusterIdList: list of str
        :param IsTagFilter: 是否标签过滤
        :type IsTagFilter: bool
        :param Filters: 过滤器。目前支持按标签过滤。
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.ClusterIdList = None
        self.IsTagFilter = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterIdList = params.get("ClusterIdList")
        self.IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param QueueName: 精确匹配QueueName
        :type QueueName: str
        """
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
        r"""
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
        r"""
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param QueueName: 根据QueueName进行过滤
        :type QueueName: str
        :param QueueNameList: CMQ 队列名称列表过滤
        :type QueueNameList: list of str
        :param IsTagFilter: 标签过滤查找时，需要设置为 true
        :type IsTagFilter: bool
        :param Filters: 过滤器。目前支持按标签过滤。
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.QueueName = None
        self.QueueNameList = None
        self.IsTagFilter = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.QueueName = params.get("QueueName")
        self.QueueNameList = params.get("QueueNameList")
        self.IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeCmqQueuesResponse(AbstractModel):
    """DescribeCmqQueues返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param TopicName: 精确匹配TopicName。
        :type TopicName: str
        """
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
        r"""
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
        r"""
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0
        :type Offset: int
        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。
        :type Limit: int
        :param TopicName: 根据TopicName进行模糊搜索
        :type TopicName: str
        :param TopicNameList: CMQ 主题名称列表过滤
        :type TopicNameList: list of str
        :param IsTagFilter: 标签过滤查找时，需要设置为 true
        :type IsTagFilter: bool
        :param Filters: 过滤器。目前支持按标签过滤。
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.TopicName = None
        self.TopicNameList = None
        self.IsTagFilter = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TopicName = params.get("TopicName")
        self.TopicNameList = params.get("TopicNameList")
        self.IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeCmqTopicsResponse(AbstractModel):
    """DescribeCmqTopics返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param EnvironmentId: 必填字段，环境（命名空间）名称。
        :type EnvironmentId: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param ClusterId: 必填字段，Pulsar 集群的ID
        :type ClusterId: str
        :param RoleName: 角色名称
        :type RoleName: str
        :param Filters: * RoleName
按照角色名进行过滤，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self.EnvironmentId = None
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.RoleName = None
        self.Filters = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.RoleName = params.get("RoleName")
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
        


class DescribeEnvironmentRolesResponse(AbstractModel):
    """DescribeEnvironmentRoles返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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


class DescribeNamespaceBundlesOptRequest(AbstractModel):
    """DescribeNamespaceBundlesOpt请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterName: 物理集群名
        :type ClusterName: str
        :param TenantId: 虚拟集群（租户）ID
        :type TenantId: str
        :param NamespaceName: 命名空间名
        :type NamespaceName: str
        :param NeedMetrics: 是否需要监控指标，若传false，则不需要传Limit和Offset分页参数
        :type NeedMetrics: bool
        :param Limit: 查询限制条数
        :type Limit: int
        :param Offset: 查询偏移量
        :type Offset: int
        """
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
        r"""
        :param TotalCount: 记录条数
        :type TotalCount: int
        :param BundleSet: bundle列表
        :type BundleSet: list of BundleSetOpt
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param InstanceId: 节点实例ID
        :type InstanceId: str
        """
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
        r"""
        :param NodeState: 0-异常；1-正常
        :type NodeState: int
        :param LatestHealthCheckTime: 最近一次健康检查的时间
        :type LatestHealthCheckTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeState = None
        self.LatestHealthCheckTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeState = params.get("NodeState")
        self.LatestHealthCheckTime = params.get("LatestHealthCheckTime")
        self.RequestId = params.get("RequestId")


class DescribePublisherSummaryRequest(AbstractModel):
    """DescribePublisherSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param Topic: 主题名称
        :type Topic: str
        """
        self.ClusterId = None
        self.Namespace = None
        self.Topic = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublisherSummaryResponse(AbstractModel):
    """DescribePublisherSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param MsgRateIn: 生产速率（条/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: float
        :param MsgThroughputIn: 生产速率（字节/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: float
        :param PublisherCount: 生产者数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PublisherCount: int
        :param StorageSize: 消息存储大小，以字节为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MsgRateIn = None
        self.MsgThroughputIn = None
        self.PublisherCount = None
        self.StorageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MsgRateIn = params.get("MsgRateIn")
        self.MsgThroughputIn = params.get("MsgThroughputIn")
        self.PublisherCount = params.get("PublisherCount")
        self.StorageSize = params.get("StorageSize")
        self.RequestId = params.get("RequestId")


class DescribePublishersRequest(AbstractModel):
    """DescribePublishers请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param Topic: 主题名称
        :type Topic: str
        :param Filters: 参数过滤器，支持ProducerName，Address字段
        :type Filters: list of Filter
        :param Offset: 查询偏移量，默认为0
        :type Offset: int
        :param Limit: 查询条数，默认为20
        :type Limit: int
        :param Sort: 排序器
        :type Sort: :class:`tencentcloud.tdmq.v20200217.models.Sort`
        """
        self.ClusterId = None
        self.Namespace = None
        self.Topic = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Sort = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.Topic = params.get("Topic")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self.Sort = Sort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublishersResponse(AbstractModel):
    """DescribePublishers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param Publishers: 生产者信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Publishers: list of Publisher
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Publishers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Publishers") is not None:
            self.Publishers = []
            for item in params.get("Publishers"):
                obj = Publisher()
                obj._deserialize(item)
                self.Publishers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRocketMQClusterRequest(AbstractModel):
    """DescribeRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQClusterResponse(AbstractModel):
    """DescribeRocketMQCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterInfo: 集群信息
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param ClusterConfig: 集群配置
        :type ClusterConfig: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        :param ClusterStats: 集群最近使用量
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterStats: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterRecentStats`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterInfo = None
        self.ClusterConfig = None
        self.ClusterStats = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterInfo") is not None:
            self.ClusterInfo = RocketMQClusterInfo()
            self.ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("ClusterConfig") is not None:
            self.ClusterConfig = RocketMQClusterConfig()
            self.ClusterConfig._deserialize(params.get("ClusterConfig"))
        if params.get("ClusterStats") is not None:
            self.ClusterStats = RocketMQClusterRecentStats()
            self.ClusterStats._deserialize(params.get("ClusterStats"))
        self.RequestId = params.get("RequestId")


class DescribeRocketMQClustersRequest(AbstractModel):
    """DescribeRocketMQClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param IdKeyword: 按照集群ID关键字搜索
        :type IdKeyword: str
        :param NameKeyword: 按照集群名称关键字搜索
        :type NameKeyword: str
        :param ClusterIdList: 集群ID列表过滤
        :type ClusterIdList: list of str
        :param IsTagFilter: 标签过滤查找时，需要设置为true
        :type IsTagFilter: bool
        :param Filters: 过滤器。目前支持标签过滤。
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.IdKeyword = None
        self.NameKeyword = None
        self.ClusterIdList = None
        self.IsTagFilter = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IdKeyword = params.get("IdKeyword")
        self.NameKeyword = params.get("NameKeyword")
        self.ClusterIdList = params.get("ClusterIdList")
        self.IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeRocketMQClustersResponse(AbstractModel):
    """DescribeRocketMQClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterList: 集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterList: list of RocketMQClusterDetail
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = RocketMQClusterDetail()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRocketMQGroupsRequest(AbstractModel):
    """DescribeRocketMQGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间
        :type NamespaceId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制条数
        :type Limit: int
        :param FilterTopic: 主题名称，输入此参数可查询该主题下所有的订阅组
        :type FilterTopic: str
        :param FilterGroup: 按消费组名称查询消费组，支持模糊查询
        :type FilterGroup: str
        :param SortedBy: 按照指定字段排序，可选值为tps，accumulative
        :type SortedBy: str
        :param SortOrder: 按升序或降序排列，可选值为asc，desc
        :type SortOrder: str
        :param FilterOneGroup: 订阅组名称，指定此参数后将只返回该订阅组信息
        :type FilterOneGroup: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Offset = None
        self.Limit = None
        self.FilterTopic = None
        self.FilterGroup = None
        self.SortedBy = None
        self.SortOrder = None
        self.FilterOneGroup = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterTopic = params.get("FilterTopic")
        self.FilterGroup = params.get("FilterGroup")
        self.SortedBy = params.get("SortedBy")
        self.SortOrder = params.get("SortOrder")
        self.FilterOneGroup = params.get("FilterOneGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQGroupsResponse(AbstractModel):
    """DescribeRocketMQGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param Groups: 订阅组列表
        :type Groups: list of RocketMQGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = RocketMQGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRocketMQNamespacesRequest(AbstractModel):
    """DescribeRocketMQNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制数目
        :type Limit: int
        :param NameKeyword: 按名称搜索
        :type NameKeyword: str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.NameKeyword = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NameKeyword = params.get("NameKeyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQNamespacesResponse(AbstractModel):
    """DescribeRocketMQNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param Namespaces: 命名空间列表
        :type Namespaces: list of RocketMQNamespace
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Namespaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Namespaces") is not None:
            self.Namespaces = []
            for item in params.get("Namespaces"):
                obj = RocketMQNamespace()
                obj._deserialize(item)
                self.Namespaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRocketMQTopicsRequest(AbstractModel):
    """DescribeRocketMQTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询限制数
        :type Limit: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间
        :type NamespaceId: str
        :param FilterType: 按主题类型过滤查询结果，可选择Normal, GlobalOrder, PartitionedOrder, Transaction
        :type FilterType: list of str
        :param FilterName: 按主题名称搜索，支持模糊查询
        :type FilterName: str
        """
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.NamespaceId = None
        self.FilterType = None
        self.FilterName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.FilterType = params.get("FilterType")
        self.FilterName = params.get("FilterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQTopicsResponse(AbstractModel):
    """DescribeRocketMQTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param Topics: 主题信息列表
        :type Topics: list of RocketMQTopic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Topics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = RocketMQTopic()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRolesRequest(AbstractModel):
    """DescribeRoles请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称，模糊查询
        :type RoleName: str
        :param Offset: 起始下标，不填默认为0。
        :type Offset: int
        :param Limit: 返回数量，不填则默认为10，最大值为20。
        :type Limit: int
        :param ClusterId: 必填字段，集群Id
        :type ClusterId: str
        :param Filters: * RoleName
按照角色名进行过滤，精确查询。
类型：String
必选：否
        :type Filters: list of Filter
        """
        self.RoleName = None
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.Filters = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
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
        


class DescribeRolesResponse(AbstractModel):
    """DescribeRoles返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录数。
        :type TotalCount: int
        :param RoleSets: 角色数组。
        :type RoleSets: list of Role
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RoleSets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RoleSets") is not None:
            self.RoleSets = []
            for item in params.get("RoleSets"):
                obj = Role()
                obj._deserialize(item)
                self.RoleSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscriptionsRequest(AbstractModel):
    """DescribeSubscriptions请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        :param TopicNum: Topic数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNum: int
        :param RetentionPolicy: 消息保留策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self.EnvironmentId = None
        self.Remark = None
        self.MsgTTL = None
        self.CreateTime = None
        self.UpdateTime = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.TopicNum = None
        self.RetentionPolicy = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Remark = params.get("Remark")
        self.MsgTTL = params.get("MsgTTL")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.TopicNum = params.get("TopicNum")
        if params.get("RetentionPolicy") is not None:
            self.RetentionPolicy = RetentionPolicy()
            self.RetentionPolicy._deserialize(params.get("RetentionPolicy"))
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
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternalTenant(AbstractModel):
    """面向运营端的虚拟集群信息

    """

    def __init__(self):
        r"""
        :param TenantId: 虚拟集群ID
        :type TenantId: str
        :param TenantName: 虚拟集群名称
        :type TenantName: str
        :param CustomerUin: 客户UIN
        :type CustomerUin: str
        :param CustomerAppId: 客户的APPID
        :type CustomerAppId: str
        :param ClusterName: 物理集群名称
        :type ClusterName: str
        :param Type: 集群协议类型，支持的值为TDMQ，ROCKETMQ，AMQP，CMQ
        :type Type: str
        :param MaxNamespaces: 命名空间配额
        :type MaxNamespaces: int
        :param UsedNamespaces: 已使用命名空间配额
        :type UsedNamespaces: int
        :param MaxTopics: Topic配额
        :type MaxTopics: int
        :param UsedTopics: 已使用Topic配额
        :type UsedTopics: int
        :param MaxPartitions: Topic分区数配额
        :type MaxPartitions: int
        :param UsedPartitions: 已使用Topic分区数配额
        :type UsedPartitions: int
        :param MaxMsgBacklogSize: 存储配额, byte为单位
        :type MaxMsgBacklogSize: int
        :param MaxPublishTps: 命名空间最大生产TPS
        :type MaxPublishTps: int
        :param MaxRetention: 消息最大保留时间，秒为单位
        :type MaxRetention: int
        :param CreateTime: 创建时间，毫秒为单位
        :type CreateTime: int
        :param UpdateTime: 修改时间，毫秒为单位
        :type UpdateTime: int
        :param MaxDispatchTps: 命名空间最大消费TPS
        :type MaxDispatchTps: int
        :param MaxDispatchRateInBytes: 命名空间最大消费带宽，byte为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxDispatchRateInBytes: int
        :param MaxPublishRateInBytes: 命名空间最大生产带宽，byte为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxPublishRateInBytes: int
        :param MaxRetentionSizeInMB: 消息最大保留空间，MB为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetentionSizeInMB: int
        """
        self.TenantId = None
        self.TenantName = None
        self.CustomerUin = None
        self.CustomerAppId = None
        self.ClusterName = None
        self.Type = None
        self.MaxNamespaces = None
        self.UsedNamespaces = None
        self.MaxTopics = None
        self.UsedTopics = None
        self.MaxPartitions = None
        self.UsedPartitions = None
        self.MaxMsgBacklogSize = None
        self.MaxPublishTps = None
        self.MaxRetention = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MaxDispatchTps = None
        self.MaxDispatchRateInBytes = None
        self.MaxPublishRateInBytes = None
        self.MaxRetentionSizeInMB = None


    def _deserialize(self, params):
        self.TenantId = params.get("TenantId")
        self.TenantName = params.get("TenantName")
        self.CustomerUin = params.get("CustomerUin")
        self.CustomerAppId = params.get("CustomerAppId")
        self.ClusterName = params.get("ClusterName")
        self.Type = params.get("Type")
        self.MaxNamespaces = params.get("MaxNamespaces")
        self.UsedNamespaces = params.get("UsedNamespaces")
        self.MaxTopics = params.get("MaxTopics")
        self.UsedTopics = params.get("UsedTopics")
        self.MaxPartitions = params.get("MaxPartitions")
        self.UsedPartitions = params.get("UsedPartitions")
        self.MaxMsgBacklogSize = params.get("MaxMsgBacklogSize")
        self.MaxPublishTps = params.get("MaxPublishTps")
        self.MaxRetention = params.get("MaxRetention")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MaxDispatchTps = params.get("MaxDispatchTps")
        self.MaxDispatchRateInBytes = params.get("MaxDispatchRateInBytes")
        self.MaxPublishRateInBytes = params.get("MaxPublishRateInBytes")
        self.MaxRetentionSizeInMB = params.get("MaxRetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAMQPClusterRequest(AbstractModel):
    """ModifyAMQPCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 3-64个字符，只能包含字母、数字、“-”及“_”
        :type ClusterName: str
        :param Remark: 说明信息，不超过128个字符
        :type Remark: str
        """
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
        


class ModifyAMQPClusterResponse(AbstractModel):
    """ModifyAMQPCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAMQPExchangeRequest(AbstractModel):
    """ModifyAMQPExchange请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost间名称
        :type VHostId: str
        :param Exchange: 交换机名称
        :type Exchange: str
        :param Remark: 说明信息，最大128个字符
        :type Remark: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.Exchange = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.Exchange = params.get("Exchange")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAMQPExchangeResponse(AbstractModel):
    """ModifyAMQPExchange返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAMQPQueueRequest(AbstractModel):
    """ModifyAMQPQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: Vhost名称
        :type VHostId: str
        :param Queue: 队列名称
        :type Queue: str
        :param AutoDelete: 是否自动清除
        :type AutoDelete: bool
        :param Remark: 说明信息，最大128个字符
        :type Remark: str
        :param DeadLetterExchange: 死信exchange
        :type DeadLetterExchange: str
        :param DeadLetterRoutingKey: 路由键
        :type DeadLetterRoutingKey: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.Queue = None
        self.AutoDelete = None
        self.Remark = None
        self.DeadLetterExchange = None
        self.DeadLetterRoutingKey = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.Queue = params.get("Queue")
        self.AutoDelete = params.get("AutoDelete")
        self.Remark = params.get("Remark")
        self.DeadLetterExchange = params.get("DeadLetterExchange")
        self.DeadLetterRoutingKey = params.get("DeadLetterRoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAMQPQueueResponse(AbstractModel):
    """ModifyAMQPQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAMQPVHostRequest(AbstractModel):
    """ModifyAMQPVHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VHostId: vhost名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type VHostId: str
        :param MsgTtl: 未消费消息的保留时间，以毫秒为单位，60秒-15天
        :type MsgTtl: int
        :param Remark: 说明，最大128个字符
        :type Remark: str
        """
        self.ClusterId = None
        self.VHostId = None
        self.MsgTtl = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VHostId = params.get("VHostId")
        self.MsgTtl = params.get("MsgTtl")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAMQPVHostResponse(AbstractModel):
    """ModifyAMQPVHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterRequest(AbstractModel):
    """ModifyCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: Pulsar 集群的ID，需要更新的集群Id。
        :type ClusterId: str
        :param ClusterName: 更新后的集群名称。
        :type ClusterName: str
        :param Remark: 说明信息。
        :type Remark: str
        :param PublicAccessEnabled: 开启公网访问，只能为true
        :type PublicAccessEnabled: bool
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Remark = None
        self.PublicAccessEnabled = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Remark = params.get("Remark")
        self.PublicAccessEnabled = params.get("PublicAccessEnabled")
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param EnvironmentId: 命名空间名称。
        :type EnvironmentId: str
        :param MsgTTL: 未消费消息过期时间，单位：秒，最大1296000。
        :type MsgTTL: int
        :param Remark: 备注，字符串最长不超过128。
        :type Remark: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param RetentionPolicy: 消息保留策略
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None
        self.RetentionPolicy = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        if params.get("RetentionPolicy") is not None:
            self.RetentionPolicy = RetentionPolicy()
            self.RetentionPolicy._deserialize(params.get("RetentionPolicy"))
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
        r"""
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


class ModifyEnvironmentRoleRequest(AbstractModel):
    """ModifyEnvironmentRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param RoleName: 角色名称。
        :type RoleName: str
        :param Permissions: 授权项，最多只能包含produce、consume两项的非空字符串数组。
        :type Permissions: list of str
        :param ClusterId: 必填字段，集群的ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.RoleName = None
        self.Permissions = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.RoleName = params.get("RoleName")
        self.Permissions = params.get("Permissions")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentRoleResponse(AbstractModel):
    """ModifyEnvironmentRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQClusterRequest(AbstractModel):
    """ModifyRocketMQCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: RocketMQ集群ID
        :type ClusterId: str
        :param ClusterName: 3-64个字符，只能包含字母、数字、“-”及“_”
        :type ClusterName: str
        :param Remark: 说明信息，不超过128个字符
        :type Remark: str
        """
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
        


class ModifyRocketMQClusterResponse(AbstractModel):
    """ModifyRocketMQCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQGroupRequest(AbstractModel):
    """ModifyRocketMQGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间
        :type NamespaceId: str
        :param GroupId: 消费组名称
        :type GroupId: str
        :param Remark: 说明信息，最长128个字符
        :type Remark: str
        :param ReadEnable: 是否开启消费
        :type ReadEnable: bool
        :param BroadcastEnable: 是否开启广播消费
        :type BroadcastEnable: bool
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.GroupId = None
        self.Remark = None
        self.ReadEnable = None
        self.BroadcastEnable = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupId = params.get("GroupId")
        self.Remark = params.get("Remark")
        self.ReadEnable = params.get("ReadEnable")
        self.BroadcastEnable = params.get("BroadcastEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQGroupResponse(AbstractModel):
    """ModifyRocketMQGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQNamespaceRequest(AbstractModel):
    """ModifyRocketMQNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type NamespaceId: str
        :param Ttl: 未消费消息的保留时间，以毫秒为单位，60秒-15天
        :type Ttl: int
        :param RetentionTime: 消息持久化后保留的时间，以毫秒为单位
        :type RetentionTime: int
        :param Remark: 说明，最大128个字符
        :type Remark: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Ttl = None
        self.RetentionTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Ttl = params.get("Ttl")
        self.RetentionTime = params.get("RetentionTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQNamespaceResponse(AbstractModel):
    """ModifyRocketMQNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQTopicRequest(AbstractModel):
    """ModifyRocketMQTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空间名称
        :type NamespaceId: str
        :param Topic: 主题名称
        :type Topic: str
        :param Remark: 说明信息，最大128个字符
        :type Remark: str
        :param PartitionNum: 分区数，全局类型无效，不可小于当前分区数
        :type PartitionNum: int
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Topic = None
        self.Remark = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Topic = params.get("Topic")
        self.Remark = params.get("Remark")
        self.PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQTopicResponse(AbstractModel):
    """ModifyRocketMQTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoleRequest(AbstractModel):
    """ModifyRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称，不支持中字以及除了短线和下划线外的特殊字符且长度必须大于0且小等于32。
        :type RoleName: str
        :param Remark: 备注说明，长度必须大等于0且小等于128。
        :type Remark: str
        :param ClusterId: 必填字段，集群Id
        :type ClusterId: str
        """
        self.RoleName = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoleResponse(AbstractModel):
    """ModifyRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称
        :type RoleName: str
        :param Remark: 备注说明
        :type Remark: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoleName = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
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


class Publisher(AbstractModel):
    """生产者信息

    """

    def __init__(self):
        r"""
        :param ProducerId: 生产者id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerId: int
        :param ProducerName: 生产者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerName: str
        :param Address: 生产者地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param ClientVersion: 客户端版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientVersion: str
        :param MsgRateIn: 消息生产速率（条/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgRateIn: float
        :param MsgThroughputIn: 消息生产吞吐速率（字节/秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgThroughputIn: float
        :param AverageMsgSize: 平均消息大小（字节）
注意：此字段可能返回 null，表示取不到有效值。
        :type AverageMsgSize: float
        :param ConnectedSince: 连接时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectedSince: str
        :param Partition: 生产者连接的主题分区号
注意：此字段可能返回 null，表示取不到有效值。
        :type Partition: int
        """
        self.ProducerId = None
        self.ProducerName = None
        self.Address = None
        self.ClientVersion = None
        self.MsgRateIn = None
        self.MsgThroughputIn = None
        self.AverageMsgSize = None
        self.ConnectedSince = None
        self.Partition = None


    def _deserialize(self, params):
        self.ProducerId = params.get("ProducerId")
        self.ProducerName = params.get("ProducerName")
        self.Address = params.get("Address")
        self.ClientVersion = params.get("ClientVersion")
        self.MsgRateIn = params.get("MsgRateIn")
        self.MsgThroughputIn = params.get("MsgThroughputIn")
        self.AverageMsgSize = params.get("AverageMsgSize")
        self.ConnectedSince = params.get("ConnectedSince")
        self.Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveMessageRequest(AbstractModel):
    """ReceiveMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param Topic: 接收消息的topic的名字, 这里尽量需要使用topic的全路径，如果不指定，即：tenant/namespace/topic。默认使用的是：public/default
        :type Topic: str
        :param SubscriptionName: 订阅者的名字
        :type SubscriptionName: str
        :param ReceiverQueueSize: 默认值为1000，consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
        :type ReceiverQueueSize: int
        :param SubInitialPosition: 默认值为：Latest。用作判定consumer初始接收消息的位置，可选参数为：Earliest, Latest
        :type SubInitialPosition: str
        """
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
        r"""
        :param MessageID: 用作标识消息的唯一主键
        :type MessageID: str
        :param MessagePayload: 接收消息的内容
        :type MessagePayload: str
        :param AckTopic: 提供给 Ack 接口，用来Ack哪一个topic中的消息
        :type AckTopic: str
        :param ErrorMsg: 返回的错误信息，如果为空，说明没有错误
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param SubName: 返回订阅者的名字，用来创建 ack consumer时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type SubName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
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
        r"""
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


class RetentionPolicy(AbstractModel):
    """消息保留策略

    """

    def __init__(self):
        r"""
        :param TimeInMinutes: 消息保留时长
        :type TimeInMinutes: int
        :param SizeInMB: 消息保留大小
        :type SizeInMB: int
        """
        self.TimeInMinutes = None
        self.SizeInMB = None


    def _deserialize(self, params):
        self.TimeInMinutes = params.get("TimeInMinutes")
        self.SizeInMB = params.get("SizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindCmqQueueRequest(AbstractModel):
    """RewindCmqQueue请求参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RocketMQClusterConfig(AbstractModel):
    """RocketMQ集群配置

    """

    def __init__(self):
        r"""
        :param MaxTpsPerNamespace: 单命名空间TPS上线
        :type MaxTpsPerNamespace: int
        :param MaxNamespaceNum: 最大命名空间数量
        :type MaxNamespaceNum: int
        :param UsedNamespaceNum: 已使用命名空间数量
        :type UsedNamespaceNum: int
        :param MaxTopicNum: 最大Topic数量
        :type MaxTopicNum: int
        :param UsedTopicNum: 已使用Topic数量
        :type UsedTopicNum: int
        :param MaxGroupNum: 最大Group数量
        :type MaxGroupNum: int
        :param UsedGroupNum: 已使用Group数量
        :type UsedGroupNum: int
        :param MaxRetentionTime: 消息最大保留时间，以毫秒为单位
        :type MaxRetentionTime: int
        :param MaxLatencyTime: 消息最长延时，以毫秒为单位
        :type MaxLatencyTime: int
        """
        self.MaxTpsPerNamespace = None
        self.MaxNamespaceNum = None
        self.UsedNamespaceNum = None
        self.MaxTopicNum = None
        self.UsedTopicNum = None
        self.MaxGroupNum = None
        self.UsedGroupNum = None
        self.MaxRetentionTime = None
        self.MaxLatencyTime = None


    def _deserialize(self, params):
        self.MaxTpsPerNamespace = params.get("MaxTpsPerNamespace")
        self.MaxNamespaceNum = params.get("MaxNamespaceNum")
        self.UsedNamespaceNum = params.get("UsedNamespaceNum")
        self.MaxTopicNum = params.get("MaxTopicNum")
        self.UsedTopicNum = params.get("UsedTopicNum")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.UsedGroupNum = params.get("UsedGroupNum")
        self.MaxRetentionTime = params.get("MaxRetentionTime")
        self.MaxLatencyTime = params.get("MaxLatencyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterDetail(AbstractModel):
    """租户RocketMQ集群详细信息

    """

    def __init__(self):
        r"""
        :param Info: 集群基本信息
        :type Info: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param Config: 集群配置信息
        :type Config: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        :param Status: 集群状态，0:创建中，1:正常，2:销毁中，3:已删除，4: 隔离中，5:创建失败，6: 删除失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.Info = None
        self.Config = None
        self.Status = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = RocketMQClusterInfo()
            self.Info._deserialize(params.get("Info"))
        if params.get("Config") is not None:
            self.Config = RocketMQClusterConfig()
            self.Config._deserialize(params.get("Config"))
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterInfo(AbstractModel):
    """RocketMQ集群基本信息

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Region: 地域信息
        :type Region: str
        :param CreateTime: 创建时间，毫秒为单位
        :type CreateTime: int
        :param Remark: 集群说明信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param PublicEndPoint: 公网接入地址
        :type PublicEndPoint: str
        :param VpcEndPoint: VPC接入地址
        :type VpcEndPoint: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.CreateTime = None
        self.Remark = None
        self.PublicEndPoint = None
        self.VpcEndPoint = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")
        self.PublicEndPoint = params.get("PublicEndPoint")
        self.VpcEndPoint = params.get("VpcEndPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterRecentStats(AbstractModel):
    """RocketMQ近期使用量

    """

    def __init__(self):
        r"""
        :param TopicNum: Topic数量
        :type TopicNum: int
        :param ProducedMsgNum: 消息生产数
        :type ProducedMsgNum: int
        :param ConsumedMsgNum: 消息消费数
        :type ConsumedMsgNum: int
        :param AccumulativeMsgNum: 消息堆积数
        :type AccumulativeMsgNum: int
        """
        self.TopicNum = None
        self.ProducedMsgNum = None
        self.ConsumedMsgNum = None
        self.AccumulativeMsgNum = None


    def _deserialize(self, params):
        self.TopicNum = params.get("TopicNum")
        self.ProducedMsgNum = params.get("ProducedMsgNum")
        self.ConsumedMsgNum = params.get("ConsumedMsgNum")
        self.AccumulativeMsgNum = params.get("AccumulativeMsgNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQGroup(AbstractModel):
    """RocketMQ消费组信息

    """

    def __init__(self):
        r"""
        :param Name: 消费组名称
        :type Name: str
        :param ConsumerNum: 在线消费者数量
        :type ConsumerNum: int
        :param TPS: 消费TPS
        :type TPS: int
        :param TotalAccumulative: 总堆积数量
        :type TotalAccumulative: int
        :param ConsumptionMode: 0表示集群消费模式，1表示广播消费模式，-1表示未知
        :type ConsumptionMode: int
        :param ReadEnabled: 是否允许消费
        :type ReadEnabled: bool
        :param RetryPartitionNum: 重试队列分区数
注意：此字段可能返回 null，表示取不到有效值。
        :type RetryPartitionNum: int
        :param CreateTime: 创建时间，以毫秒为单位
        :type CreateTime: int
        :param UpdateTime: 修改时间，以毫秒为单位
        :type UpdateTime: int
        :param ClientProtocol: 客户端协议
        :type ClientProtocol: str
        :param Remark: 说明信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param ConsumerType: 消费者类型，枚举值ACTIVELY, PASSIVELY
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerType: str
        :param BroadcastEnabled: 是否开启广播消费
        :type BroadcastEnabled: bool
        """
        self.Name = None
        self.ConsumerNum = None
        self.TPS = None
        self.TotalAccumulative = None
        self.ConsumptionMode = None
        self.ReadEnabled = None
        self.RetryPartitionNum = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClientProtocol = None
        self.Remark = None
        self.ConsumerType = None
        self.BroadcastEnabled = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ConsumerNum = params.get("ConsumerNum")
        self.TPS = params.get("TPS")
        self.TotalAccumulative = params.get("TotalAccumulative")
        self.ConsumptionMode = params.get("ConsumptionMode")
        self.ReadEnabled = params.get("ReadEnabled")
        self.RetryPartitionNum = params.get("RetryPartitionNum")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ClientProtocol = params.get("ClientProtocol")
        self.Remark = params.get("Remark")
        self.ConsumerType = params.get("ConsumerType")
        self.BroadcastEnabled = params.get("BroadcastEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQNamespace(AbstractModel):
    """RocketMQ命名空间信息

    """

    def __init__(self):
        r"""
        :param NamespaceId: 命名空间名称，3-64个字符，只能包含字母、数字、“-”及“_”
        :type NamespaceId: str
        :param Ttl: 未消费消息的保留时间，以毫秒单位，范围60秒到15天
        :type Ttl: int
        :param RetentionTime: 消息持久化后保留的时间，以毫秒单位
        :type RetentionTime: int
        :param Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.NamespaceId = None
        self.Ttl = None
        self.RetentionTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Ttl = params.get("Ttl")
        self.RetentionTime = params.get("RetentionTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQTopic(AbstractModel):
    """RocketMQ主题信息

    """

    def __init__(self):
        r"""
        :param Name: 主题名称
        :type Name: str
        :param Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param PartitionNum: 读写分区数
        :type PartitionNum: int
        :param CreateTime: 创建时间，以毫秒为单位
        :type CreateTime: int
        :param UpdateTime: 创建时间，以毫秒为单位
        :type UpdateTime: int
        """
        self.Name = None
        self.Remark = None
        self.PartitionNum = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.PartitionNum = params.get("PartitionNum")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Role(AbstractModel):
    """角色实例

    """

    def __init__(self):
        r"""
        :param RoleName: 角色名称。
        :type RoleName: str
        :param Token: 角色token值。
        :type Token: str
        :param Remark: 备注说明。
        :type Remark: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self.RoleName = None
        self.Token = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Token = params.get("Token")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesRequest(AbstractModel):
    """SendBatchMessages请求参数结构体

    """

    def __init__(self):
        r"""
        :param Topic: 消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :type Topic: str
        :param Payload: 需要发送消息的内容
        :type Payload: str
        :param StringToken: String 类型的 token，可以不填，系统会自动获取
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
        r"""
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
        r"""
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
        r"""
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
        r"""
        :param Topic: 消息要发送的topic的名字, 这里尽量需要使用topic的全路径，即：tenant/namespace/topic。如果不指定，默认使用的是：public/default
        :type Topic: str
        :param Payload: 要发送的消息的内容
        :type Payload: str
        :param StringToken: Token 是用来做鉴权使用的，可以不填，系统会自动获取
        :type StringToken: str
        :param ProducerName: 设置 producer 的名字，要求全局唯一，用户不配置，系统会随机生成
        :type ProducerName: str
        :param SendTimeout: 设置消息发送的超时时间，默认为30s
        :type SendTimeout: int
        :param MaxPendingMessages: 内存中缓存的最大的生产消息的数量，默认为1000条
        :type MaxPendingMessages: int
        """
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
        r"""
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


class SendMsgRequest(AbstractModel):
    """SendMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvironmentId: 环境（命名空间）名称。
        :type EnvironmentId: str
        :param TopicName: 主题名称，如果是分区topic需要指定具体分区，如果没有指定则默认发到0分区，例如：my_topic-partition-0。
        :type TopicName: str
        :param MsgContent: 消息内容，不能为空且大小不得大于5242880个byte。
        :type MsgContent: str
        :param ClusterId: Pulsar 集群的ID
        :type ClusterId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Sort(AbstractModel):
    """排序器

    """

    def __init__(self):
        r"""
        :param Name: 排序字段
        :type Name: str
        :param Order: 升序ASC，降序DESC
        :type Order: str
        """
        self.Name = None
        self.Order = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Subscription(AbstractModel):
    """订阅者

    """

    def __init__(self):
        r"""
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
        :param SubType: 订阅类型，Exclusive，Shared，Failover， Key_Shared，空或NULL表示未知，
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param BlockedSubscriptionOnUnackedMsgs: 是否由于未 ack 数到达上限而被 block
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockedSubscriptionOnUnackedMsgs: bool
        :param MaxUnackedMsgNum: 未 ack 消息数上限
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxUnackedMsgNum: int
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
        self.SubType = None
        self.BlockedSubscriptionOnUnackedMsgs = None
        self.MaxUnackedMsgNum = None


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
        self.SubType = params.get("SubType")
        self.BlockedSubscriptionOnUnackedMsgs = params.get("BlockedSubscriptionOnUnackedMsgs")
        self.MaxUnackedMsgNum = params.get("MaxUnackedMsgNum")
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
        r"""
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
        r"""
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
        r"""
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
        :param PulsarTopicType: 0: 非持久非分区
1: 非持久分区
2: 持久非分区
3: 持久分区
注意：此字段可能返回 null，表示取不到有效值。
        :type PulsarTopicType: int
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
        self.PulsarTopicType = None


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
        self.PulsarTopicType = params.get("PulsarTopicType")
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
        r"""
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
        r"""
        :param SourceQueueName: 死信策略源队列名称，调用本接口会清空该队列的死信队列策略。
        :type SourceQueueName: str
        """
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        