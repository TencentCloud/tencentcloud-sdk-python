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


class ChangeMigratingTopicToNextStageRequest(AbstractModel):
    r"""ChangeMigratingTopicToNextStage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        :param _TopicNameList: 主题名称列表，主题名称可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :type TopicNameList: list of str
        :param _NamespaceList: 命名空间列表，仅4.x集群有效，与TopicNameList一一对应，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :type NamespaceList: list of str
        """
        self._TaskId = None
        self._TopicNameList = None
        self._NamespaceList = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TopicNameList(self):
        r"""主题名称列表，主题名称可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :rtype: list of str
        """
        return self._TopicNameList

    @TopicNameList.setter
    def TopicNameList(self, TopicNameList):
        self._TopicNameList = TopicNameList

    @property
    def NamespaceList(self):
        r"""命名空间列表，仅4.x集群有效，与TopicNameList一一对应，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :rtype: list of str
        """
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TopicNameList = params.get("TopicNameList")
        self._NamespaceList = params.get("NamespaceList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeMigratingTopicToNextStageResponse(AbstractModel):
    r"""ChangeMigratingTopicToNextStage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 迁移主题状态修改的结果列表
        :type Results: list of TopicStageChangeResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        r"""迁移主题状态修改的结果列表
        :rtype: list of TopicStageChangeResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

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
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = TopicStageChangeResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class ClientSubscriptionInfo(AbstractModel):
    r"""客户端订阅详情，可用于辅助判断哪些客户端订阅关系不一致

    """

    def __init__(self):
        r"""
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _ClientAddr: 客户端地址
        :type ClientAddr: str
        :param _Topic: 订阅主题
        :type Topic: str
        :param _SubString: 订阅表达式
        :type SubString: str
        :param _ExpressionType: 订阅方式
        :type ExpressionType: str
        """
        self._ClientId = None
        self._ClientAddr = None
        self._Topic = None
        self._SubString = None
        self._ExpressionType = None

    @property
    def ClientId(self):
        r"""客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientAddr(self):
        r"""客户端地址
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def Topic(self):
        r"""订阅主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def SubString(self):
        r"""订阅表达式
        :rtype: str
        """
        return self._SubString

    @SubString.setter
    def SubString(self, SubString):
        self._SubString = SubString

    @property
    def ExpressionType(self):
        r"""订阅方式
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
        


class ConsumeGroupItem(AbstractModel):
    r"""消费组信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称
        :type ConsumerGroup: str
        :param _ConsumeEnable: 是否开启消费
        :type ConsumeEnable: bool
        :param _ConsumeMessageOrderly: 顺序投递：true
并发投递：false
        :type ConsumeMessageOrderly: bool
        :param _MaxRetryTimes: 最大重试次数
        :type MaxRetryTimes: int
        :param _Remark: 备注
        :type Remark: str
        :param _ClusterIdV4: 4.x的集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIdV4: str
        :param _NamespaceV4: 4.x的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceV4: str
        :param _ConsumerGroupV4: 4.x的消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerGroupV4: str
        :param _FullNamespaceV4: 4.x的完整命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type FullNamespaceV4: str
        :param _SubscribeTopicNum: 订阅的主题个数
        :type SubscribeTopicNum: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _TagList: 绑定的标签列表
        :type TagList: list of Tag
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._ConsumeEnable = None
        self._ConsumeMessageOrderly = None
        self._MaxRetryTimes = None
        self._Remark = None
        self._ClusterIdV4 = None
        self._NamespaceV4 = None
        self._ConsumerGroupV4 = None
        self._FullNamespaceV4 = None
        self._SubscribeTopicNum = None
        self._CreateTime = None
        self._TagList = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        r"""消费组名称
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def ConsumeEnable(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

    @property
    def ConsumeMessageOrderly(self):
        r"""顺序投递：true
并发投递：false
        :rtype: bool
        """
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def MaxRetryTimes(self):
        r"""最大重试次数
        :rtype: int
        """
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterIdV4(self):
        r"""4.x的集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterIdV4

    @ClusterIdV4.setter
    def ClusterIdV4(self, ClusterIdV4):
        self._ClusterIdV4 = ClusterIdV4

    @property
    def NamespaceV4(self):
        r"""4.x的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NamespaceV4

    @NamespaceV4.setter
    def NamespaceV4(self, NamespaceV4):
        self._NamespaceV4 = NamespaceV4

    @property
    def ConsumerGroupV4(self):
        r"""4.x的消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerGroupV4

    @ConsumerGroupV4.setter
    def ConsumerGroupV4(self, ConsumerGroupV4):
        self._ConsumerGroupV4 = ConsumerGroupV4

    @property
    def FullNamespaceV4(self):
        r"""4.x的完整命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FullNamespaceV4

    @FullNamespaceV4.setter
    def FullNamespaceV4(self, FullNamespaceV4):
        self._FullNamespaceV4 = FullNamespaceV4

    @property
    def SubscribeTopicNum(self):
        r"""订阅的主题个数
        :rtype: int
        """
        return self._SubscribeTopicNum

    @SubscribeTopicNum.setter
    def SubscribeTopicNum(self, SubscribeTopicNum):
        self._SubscribeTopicNum = SubscribeTopicNum

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TagList(self):
        r"""绑定的标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._ConsumeEnable = params.get("ConsumeEnable")
        self._ConsumeMessageOrderly = params.get("ConsumeMessageOrderly")
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._Remark = params.get("Remark")
        self._ClusterIdV4 = params.get("ClusterIdV4")
        self._NamespaceV4 = params.get("NamespaceV4")
        self._ConsumerGroupV4 = params.get("ConsumerGroupV4")
        self._FullNamespaceV4 = params.get("FullNamespaceV4")
        self._SubscribeTopicNum = params.get("SubscribeTopicNum")
        self._CreateTime = params.get("CreateTime")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerClient(AbstractModel):
    r"""消费者客户端

    """

    def __init__(self):
        r"""
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _ClientAddr: 客户端地址
        :type ClientAddr: str
        :param _Language: 客户端SDK语言
        :type Language: str
        :param _Version: 客户端SDK版本
        :type Version: str
        :param _ConsumerLag: 客户端消费堆积
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLag: int
        :param _ChannelProtocol: 消费者客户端类型，枚举值如下：

- grpc：GRPC协议
- remoting：Remoting协议
- http：HTTP协议
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelProtocol: str
        """
        self._ClientId = None
        self._ClientAddr = None
        self._Language = None
        self._Version = None
        self._ConsumerLag = None
        self._ChannelProtocol = None

    @property
    def ClientId(self):
        r"""客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientAddr(self):
        r"""客户端地址
        :rtype: str
        """
        return self._ClientAddr

    @ClientAddr.setter
    def ClientAddr(self, ClientAddr):
        self._ClientAddr = ClientAddr

    @property
    def Language(self):
        r"""客户端SDK语言
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Version(self):
        r"""客户端SDK版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ConsumerLag(self):
        r"""客户端消费堆积
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

    @property
    def ChannelProtocol(self):
        r"""消费者客户端类型，枚举值如下：

- grpc：GRPC协议
- remoting：Remoting协议
- http：HTTP协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChannelProtocol

    @ChannelProtocol.setter
    def ChannelProtocol(self, ChannelProtocol):
        self._ChannelProtocol = ChannelProtocol


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._ClientAddr = params.get("ClientAddr")
        self._Language = params.get("Language")
        self._Version = params.get("Version")
        self._ConsumerLag = params.get("ConsumerLag")
        self._ChannelProtocol = params.get("ChannelProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerGroupRequest(AbstractModel):
    r"""CreateConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _MaxRetryTimes: 最大重试次数，取值范围0～1000
        :type MaxRetryTimes: int
        :param _ConsumeEnable: 是否开启消费
        :type ConsumeEnable: bool
        :param _ConsumeMessageOrderly: 顺序投递：true
并发投递：false
        :type ConsumeMessageOrderly: bool
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        :param _Remark: 备注信息，最多 128 个字符
        :type Remark: str
        :param _TagList: 标签列表
        :type TagList: list of Tag
        """
        self._InstanceId = None
        self._MaxRetryTimes = None
        self._ConsumeEnable = None
        self._ConsumeMessageOrderly = None
        self._ConsumerGroup = None
        self._Remark = None
        self._TagList = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MaxRetryTimes(self):
        r"""最大重试次数，取值范围0～1000
        :rtype: int
        """
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def ConsumeEnable(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

    @property
    def ConsumeMessageOrderly(self):
        r"""顺序投递：true
并发投递：false
        :rtype: bool
        """
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def Remark(self):
        r"""备注信息，最多 128 个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TagList(self):
        r"""标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._ConsumeEnable = params.get("ConsumeEnable")
        self._ConsumeMessageOrderly = params.get("ConsumeMessageOrderly")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._Remark = params.get("Remark")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerGroupResponse(AbstractModel):
    r"""CreateConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称
        :type ConsumerGroup: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        r"""消费组名称
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

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
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    r"""CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，枚举值如下：

- EXPERIMENT：体验版

- BASIC：基础版

- PRO：专业版

- PLATINUM：铂金版
        :type InstanceType: str
        :param _Name: 集群名称，不能为空， 3-64个字符，只能包含数字、字母、“-”和“_”
        :type Name: str
        :param _SkuCode: 商品规格，从 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参获得。
        :type SkuCode: str
        :param _VpcList: 集群绑定的VPC信息
        :type VpcList: list of VpcInfo
        :param _Remark: 备注信息
        :type Remark: str
        :param _TagList: 标签列表
        :type TagList: list of Tag
        :param _EnablePublic: 是否开启公网，默认值为false表示不开启
        :type EnablePublic: bool
        :param _BillingFlow: 公网是否按流量计费，默认值为false表示不按流量计费
        :type BillingFlow: bool
        :param _Bandwidth: 公网带宽（单位：兆），默认值为0。如果开启公网，该字段必须为大于0的正整数
        :type Bandwidth: int
        :param _IpRules: 公网访问白名单，不填表示拒绝所有 IP 访问
        :type IpRules: list of IpRule
        :param _MessageRetention: 消息保留时长（单位：小时），取值范围参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 默认值：DefaultRetention 参数
- 最小值：RetentionLowerLimit 参数
- 最大值：RetentionUpperLimit 参数
        :type MessageRetention: int
        :param _PayMode: 付费模式（0: 后付费；1: 预付费），默认值为0
        :type PayMode: int
        :param _RenewFlag: 预付费集群是否自动续费（0: 不自动续费；1: 自动续费），默认值为0
        :type RenewFlag: int
        :param _TimeSpan: 预付费集群的购买时长（单位：月），取值范围为1～60，默认值为1
        :type TimeSpan: int
        :param _MaxTopicNum: 最大可创建主题数，从 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 默认值和最小值：TopicNumLimit 参数
- 最大值：TopicNumUpperLimit 参数
        :type MaxTopicNum: int
        :param _ZoneIds: 部署可用区列表，从 [DescribeZones](https://cloud.tencent.com/document/product/1596/77929) 接口返回中的 [ZoneInfo](https://cloud.tencent.com/document/api/1596/77932#ZoneInfo) 数据结构中获得。
        :type ZoneIds: list of int
        """
        self._InstanceType = None
        self._Name = None
        self._SkuCode = None
        self._VpcList = None
        self._Remark = None
        self._TagList = None
        self._EnablePublic = None
        self._BillingFlow = None
        self._Bandwidth = None
        self._IpRules = None
        self._MessageRetention = None
        self._PayMode = None
        self._RenewFlag = None
        self._TimeSpan = None
        self._MaxTopicNum = None
        self._ZoneIds = None

    @property
    def InstanceType(self):
        r"""实例类型，枚举值如下：

- EXPERIMENT：体验版

- BASIC：基础版

- PRO：专业版

- PLATINUM：铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Name(self):
        r"""集群名称，不能为空， 3-64个字符，只能包含数字、字母、“-”和“_”
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SkuCode(self):
        r"""商品规格，从 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参获得。
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def VpcList(self):
        r"""集群绑定的VPC信息
        :rtype: list of VpcInfo
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TagList(self):
        r"""标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def EnablePublic(self):
        r"""是否开启公网，默认值为false表示不开启
        :rtype: bool
        """
        return self._EnablePublic

    @EnablePublic.setter
    def EnablePublic(self, EnablePublic):
        self._EnablePublic = EnablePublic

    @property
    def BillingFlow(self):
        r"""公网是否按流量计费，默认值为false表示不按流量计费
        :rtype: bool
        """
        return self._BillingFlow

    @BillingFlow.setter
    def BillingFlow(self, BillingFlow):
        self._BillingFlow = BillingFlow

    @property
    def Bandwidth(self):
        r"""公网带宽（单位：兆），默认值为0。如果开启公网，该字段必须为大于0的正整数
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        r"""公网访问白名单，不填表示拒绝所有 IP 访问
        :rtype: list of IpRule
        """
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules

    @property
    def MessageRetention(self):
        r"""消息保留时长（单位：小时），取值范围参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 默认值：DefaultRetention 参数
- 最小值：RetentionLowerLimit 参数
- 最大值：RetentionUpperLimit 参数
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def PayMode(self):
        r"""付费模式（0: 后付费；1: 预付费），默认值为0
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        r"""预付费集群是否自动续费（0: 不自动续费；1: 自动续费），默认值为0
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        r"""预付费集群的购买时长（单位：月），取值范围为1～60，默认值为1
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def MaxTopicNum(self):
        r"""最大可创建主题数，从 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 默认值和最小值：TopicNumLimit 参数
- 最大值：TopicNumUpperLimit 参数
        :rtype: int
        """
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def ZoneIds(self):
        r"""部署可用区列表，从 [DescribeZones](https://cloud.tencent.com/document/product/1596/77929) 接口返回中的 [ZoneInfo](https://cloud.tencent.com/document/api/1596/77932#ZoneInfo) 数据结构中获得。
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Name = params.get("Name")
        self._SkuCode = params.get("SkuCode")
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcList.append(obj)
        self._Remark = params.get("Remark")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._EnablePublic = params.get("EnablePublic")
        self._BillingFlow = params.get("BillingFlow")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("IpRules") is not None:
            self._IpRules = []
            for item in params.get("IpRules"):
                obj = IpRule()
                obj._deserialize(item)
                self._IpRules.append(obj)
        self._MessageRetention = params.get("MessageRetention")
        self._PayMode = params.get("PayMode")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    r"""CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateMQTTInsPublicEndpointRequest(AbstractModel):
    r"""CreateMQTTInsPublicEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Bandwidth: 带宽
        :type Bandwidth: int
        :param _Rules: 公网访问规则
        :type Rules: list of PublicAccessRule
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._Rules = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        r"""带宽
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Rules(self):
        r"""公网访问规则
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMQTTInsPublicEndpointResponse(AbstractModel):
    r"""CreateMQTTInsPublicEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateMQTTInstanceRequest(AbstractModel):
    r"""CreateMQTTInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :type InstanceType: str
        :param _Name: 实例名称
        :type Name: str
        :param _SkuCode: 商品规格，可用规格如下：
basic_1k,
        :type SkuCode: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _TagList: 标签列表
        :type TagList: list of Tag
        :param _VpcList: 实例绑定的VPC信息
        :type VpcList: list of VpcInfo
        :param _EnablePublic: 是否开启公网
        :type EnablePublic: bool
        :param _Bandwidth: 公网带宽（单位：兆）
        :type Bandwidth: int
        :param _IpRules: 公网访问白名单
        :type IpRules: list of IpRule
        :param _RenewFlag: 是否自动续费（0: 不自动续费；1: 自动续费）
        :type RenewFlag: int
        :param _TimeSpan: 购买时长（单位：月）
        :type TimeSpan: int
        """
        self._InstanceType = None
        self._Name = None
        self._SkuCode = None
        self._Remark = None
        self._TagList = None
        self._VpcList = None
        self._EnablePublic = None
        self._Bandwidth = None
        self._IpRules = None
        self._RenewFlag = None
        self._TimeSpan = None

    @property
    def InstanceType(self):
        r"""实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Name(self):
        r"""实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SkuCode(self):
        r"""商品规格，可用规格如下：
basic_1k,
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TagList(self):
        r"""标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def VpcList(self):
        r"""实例绑定的VPC信息
        :rtype: list of VpcInfo
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def EnablePublic(self):
        r"""是否开启公网
        :rtype: bool
        """
        return self._EnablePublic

    @EnablePublic.setter
    def EnablePublic(self, EnablePublic):
        self._EnablePublic = EnablePublic

    @property
    def Bandwidth(self):
        r"""公网带宽（单位：兆）
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        r"""公网访问白名单
        :rtype: list of IpRule
        """
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules

    @property
    def RenewFlag(self):
        r"""是否自动续费（0: 不自动续费；1: 自动续费）
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        r"""购买时长（单位：月）
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Name = params.get("Name")
        self._SkuCode = params.get("SkuCode")
        self._Remark = params.get("Remark")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcList.append(obj)
        self._EnablePublic = params.get("EnablePublic")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("IpRules") is not None:
            self._IpRules = []
            for item in params.get("IpRules"):
                obj = IpRule()
                obj._deserialize(item)
                self._IpRules.append(obj)
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMQTTInstanceResponse(AbstractModel):
    r"""CreateMQTTInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateMQTTTopicRequest(AbstractModel):
    r"""CreateMQTTTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMQTTTopicResponse(AbstractModel):
    r"""CreateMQTTTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

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
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._RequestId = params.get("RequestId")


class CreateMQTTUserRequest(AbstractModel):
    r"""CreateMQTTUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Remark: 备注
        :type Remark: str
        :param _PermWrite: 是否开启生产权限
        :type PermWrite: bool
        :param _PermRead: 是否开启消费权限
        :type PermRead: bool
        :param _Username: 用户名
        :type Username: str
        :param _Password: 密码，该字段为空时候则后端会默认生成
        :type Password: str
        """
        self._InstanceId = None
        self._Remark = None
        self._PermWrite = None
        self._PermRead = None
        self._Username = None
        self._Password = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PermWrite(self):
        r"""是否开启生产权限
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def PermRead(self):
        r"""是否开启消费权限
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def Username(self):
        r"""用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""密码，该字段为空时候则后端会默认生成
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Remark = params.get("Remark")
        self._PermWrite = params.get("PermWrite")
        self._PermRead = params.get("PermRead")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMQTTUserResponse(AbstractModel):
    r"""CreateMQTTUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    r"""CreateRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Role: 角色名称，不能为空，只支持数字 大小写字母 分隔符("_","-")，不能超过 32 个字符
        :type Role: str
        :param _PermWrite: 是否开启生产权限
        :type PermWrite: bool
        :param _PermRead: 是否开启消费权限
        :type PermRead: bool
        :param _Remark: 备注
        :type Remark: str
        :param _PermType: 权限类型，默认按集群授权（Cluster：集群级别；TopicAndGroup：主题&消费组级别）
        :type PermType: str
        :param _DetailedPerms: Topic&Group维度权限配置，权限类型为 TopicAndGroup 时必填
        :type DetailedPerms: list of DetailedRolePerm
        """
        self._InstanceId = None
        self._Role = None
        self._PermWrite = None
        self._PermRead = None
        self._Remark = None
        self._PermType = None
        self._DetailedPerms = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Role(self):
        r"""角色名称，不能为空，只支持数字 大小写字母 分隔符("_","-")，不能超过 32 个字符
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def PermWrite(self):
        r"""是否开启生产权限
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def PermRead(self):
        r"""是否开启消费权限
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PermType(self):
        r"""权限类型，默认按集群授权（Cluster：集群级别；TopicAndGroup：主题&消费组级别）
        :rtype: str
        """
        return self._PermType

    @PermType.setter
    def PermType(self, PermType):
        self._PermType = PermType

    @property
    def DetailedPerms(self):
        r"""Topic&Group维度权限配置，权限类型为 TopicAndGroup 时必填
        :rtype: list of DetailedRolePerm
        """
        return self._DetailedPerms

    @DetailedPerms.setter
    def DetailedPerms(self, DetailedPerms):
        self._DetailedPerms = DetailedPerms


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Role = params.get("Role")
        self._PermWrite = params.get("PermWrite")
        self._PermRead = params.get("PermRead")
        self._Remark = params.get("Remark")
        self._PermType = params.get("PermType")
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
        


class CreateRoleResponse(AbstractModel):
    r"""CreateRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Role: 角色名
        :type Role: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Role = None
        self._RequestId = None

    @property
    def Role(self):
        r"""角色名
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

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
        self._Role = params.get("Role")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    r"""CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _TopicType: 主题类型，枚举值如下：

- NORMAL: 普通消息
- FIFO: 顺序消息
- DELAY: 延时消息
- TRANSACTION: 事务消息
        :type TopicType: str
        :param _QueueNum: 队列数量，取值范围3～16
        :type QueueNum: int
        :param _Remark: 备注信息，最多 128 个字符
        :type Remark: str
        :param _MsgTTL: 消息保留时长（单位：小时）
        :type MsgTTL: int
        :param _TagList: 标签列表
        :type TagList: list of Tag
        """
        self._InstanceId = None
        self._Topic = None
        self._TopicType = None
        self._QueueNum = None
        self._Remark = None
        self._MsgTTL = None
        self._TagList = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        r"""主题类型，枚举值如下：

- NORMAL: 普通消息
- FIFO: 顺序消息
- DELAY: 延时消息
- TRANSACTION: 事务消息
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def QueueNum(self):
        r"""队列数量，取值范围3～16
        :rtype: int
        """
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def Remark(self):
        r"""备注信息，最多 128 个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MsgTTL(self):
        r"""消息保留时长（单位：小时）
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def TagList(self):
        r"""标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._TopicType = params.get("TopicType")
        self._QueueNum = params.get("QueueNum")
        self._Remark = params.get("Remark")
        self._MsgTTL = params.get("MsgTTL")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    r"""CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Topic: 主题名
        :type Topic: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

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
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._RequestId = params.get("RequestId")


class CustomMapEntry(AbstractModel):
    r"""map结构返回

    """

    def __init__(self):
        r"""
        :param _Key: key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""value
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerGroupRequest(AbstractModel):
    r"""DeleteConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConsumerGroupResponse(AbstractModel):
    r"""DeleteConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    r"""DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
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
        


class DeleteInstanceResponse(AbstractModel):
    r"""DeleteInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteMQTTInsPublicEndpointRequest(AbstractModel):
    r"""DeleteMQTTInsPublicEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID
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
        


class DeleteMQTTInsPublicEndpointResponse(AbstractModel):
    r"""DeleteMQTTInsPublicEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteMQTTInstanceRequest(AbstractModel):
    r"""DeleteMQTTInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID
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
        


class DeleteMQTTInstanceResponse(AbstractModel):
    r"""DeleteMQTTInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteMQTTTopicRequest(AbstractModel):
    r"""DeleteMQTTTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMQTTTopicResponse(AbstractModel):
    r"""DeleteMQTTTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteMQTTUserRequest(AbstractModel):
    r"""DeleteMQTTUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Username: 用户名
        :type Username: str
        """
        self._InstanceId = None
        self._Username = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Username(self):
        r"""用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMQTTUserResponse(AbstractModel):
    r"""DeleteMQTTUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRoleRequest(AbstractModel):
    r"""DeleteRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Role: 角色名称，从 [DescribeRoleList](https://cloud.tencent.com/document/api/1493/98862) 接口响应中的 [RoleItem](https://cloud.tencent.com/document/api/1493/96031#RoleItem) 或控制台获得。
        :type Role: str
        """
        self._InstanceId = None
        self._Role = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Role(self):
        r"""角色名称，从 [DescribeRoleList](https://cloud.tencent.com/document/api/1493/98862) 接口响应中的 [RoleItem](https://cloud.tencent.com/document/api/1493/96031#RoleItem) 或控制台获得。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleResponse(AbstractModel):
    r"""DeleteRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteSmoothMigrationTaskRequest(AbstractModel):
    r"""DeleteSmoothMigrationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

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
        


class DeleteSmoothMigrationTaskResponse(AbstractModel):
    r"""DeleteSmoothMigrationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    r"""DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    r"""DeleteTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeConsumerClientListRequest(AbstractModel):
    r"""DescribeConsumerClientList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerClientListResponse(AbstractModel):
    r"""DescribeConsumerClientList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 消费客户端
        :type Data: list of ConsumerClient
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""消费客户端
        :rtype: list of ConsumerClient
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumerClient()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConsumerClientRequest(AbstractModel):
    r"""DescribeConsumerClient请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _ClientId: 客户端ID，从 [DescribeConsumerClientList](https://cloud.tencent.com/document/api/1493/120140) 接口中的 [ConsumerClient](https://cloud.tencent.com/document/api/1493/96031#ConsumerClient) 出参中获得。
        :type ClientId: str
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        """
        self._InstanceId = None
        self._ClientId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._ConsumerGroup = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClientId(self):
        r"""客户端ID，从 [DescribeConsumerClientList](https://cloud.tencent.com/document/api/1493/120140) 接口中的 [ConsumerClient](https://cloud.tencent.com/document/api/1493/96031#ConsumerClient) 出参中获得。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClientId = params.get("ClientId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ConsumerGroup = params.get("ConsumerGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerClientResponse(AbstractModel):
    r"""DescribeConsumerClient返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Client: 客户端详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Client: :class:`tencentcloud.trocket.v20230308.models.ConsumerClient`
        :param _TopicList: 主题消费信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of TopicConsumeStats
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Client = None
        self._TopicList = None
        self._RequestId = None

    @property
    def Client(self):
        r"""客户端详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trocket.v20230308.models.ConsumerClient`
        """
        return self._Client

    @Client.setter
    def Client(self, Client):
        self._Client = Client

    @property
    def TopicList(self):
        r"""主题消费信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TopicConsumeStats
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

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
        if params.get("Client") is not None:
            self._Client = ConsumerClient()
            self._Client._deserialize(params.get("Client"))
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = TopicConsumeStats()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConsumerGroupListRequest(AbstractModel):
    r"""DescribeConsumerGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _TagFilters: 标签过滤器
        :type TagFilters: list of TagFilter
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _FromTopic: 查询指定主题下的消费组
        :type FromTopic: str
        :param _SortedBy: 按照指定字段排序，枚举值如下：
- subscribeNum：订阅 Topic 个数
        :type SortedBy: str
        :param _SortOrder: 按升序或降序排列，枚举值如下：

- asc：升序
- desc：降序
        :type SortOrder: str
        """
        self._InstanceId = None
        self._TagFilters = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._FromTopic = None
        self._SortedBy = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TagFilters(self):
        r"""标签过滤器
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FromTopic(self):
        r"""查询指定主题下的消费组
        :rtype: str
        """
        return self._FromTopic

    @FromTopic.setter
    def FromTopic(self, FromTopic):
        self._FromTopic = FromTopic

    @property
    def SortedBy(self):
        r"""按照指定字段排序，枚举值如下：
- subscribeNum：订阅 Topic 个数
        :rtype: str
        """
        return self._SortedBy

    @SortedBy.setter
    def SortedBy(self, SortedBy):
        self._SortedBy = SortedBy

    @property
    def SortOrder(self):
        r"""按升序或降序排列，枚举值如下：

- asc：升序
- desc：降序
        :rtype: str
        """
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FromTopic = params.get("FromTopic")
        self._SortedBy = params.get("SortedBy")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupListResponse(AbstractModel):
    r"""DescribeConsumerGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 消费组列表
        :type Data: list of ConsumeGroupItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""消费组列表
        :rtype: list of ConsumeGroupItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ConsumeGroupItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConsumerGroupRequest(AbstractModel):
    r"""DescribeConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupResponse(AbstractModel):
    r"""DescribeConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsumerNum: 在线消费者数量
        :type ConsumerNum: int
        :param _Tps: TPS
        :type Tps: int
        :param _ConsumerLag: 消息堆积数量
        :type ConsumerLag: int
        :param _ConsumeType: 消费类型，枚举值如下：

- PULL：PULL 消费类型
- PUSH：PUSH 消费类型
- POP：POP 消费类型
        :type ConsumeType: str
        :param _CreatedTime: 创建时间，**Unix时间戳（毫秒）**
        :type CreatedTime: int
        :param _ConsumeMessageOrderly: 顺序投递：true
并发投递：false
        :type ConsumeMessageOrderly: bool
        :param _ConsumeEnable: 是否开启消费
        :type ConsumeEnable: bool
        :param _MaxRetryTimes: 最大重试次数
        :type MaxRetryTimes: int
        :param _Remark: 备注
        :type Remark: str
        :param _MessageModel: 消费模式：
BROADCASTING 广播模式
CLUSTERING 集群模式
        :type MessageModel: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConsumerNum = None
        self._Tps = None
        self._ConsumerLag = None
        self._ConsumeType = None
        self._CreatedTime = None
        self._ConsumeMessageOrderly = None
        self._ConsumeEnable = None
        self._MaxRetryTimes = None
        self._Remark = None
        self._MessageModel = None
        self._RequestId = None

    @property
    def ConsumerNum(self):
        r"""在线消费者数量
        :rtype: int
        """
        return self._ConsumerNum

    @ConsumerNum.setter
    def ConsumerNum(self, ConsumerNum):
        self._ConsumerNum = ConsumerNum

    @property
    def Tps(self):
        r"""TPS
        :rtype: int
        """
        return self._Tps

    @Tps.setter
    def Tps(self, Tps):
        self._Tps = Tps

    @property
    def ConsumerLag(self):
        r"""消息堆积数量
        :rtype: int
        """
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

    @property
    def ConsumeType(self):
        r"""消费类型，枚举值如下：

- PULL：PULL 消费类型
- PUSH：PUSH 消费类型
- POP：POP 消费类型
        :rtype: str
        """
        return self._ConsumeType

    @ConsumeType.setter
    def ConsumeType(self, ConsumeType):
        self._ConsumeType = ConsumeType

    @property
    def CreatedTime(self):
        r"""创建时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ConsumeMessageOrderly(self):
        r"""顺序投递：true
并发投递：false
        :rtype: bool
        """
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def ConsumeEnable(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

    @property
    def MaxRetryTimes(self):
        r"""最大重试次数
        :rtype: int
        """
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MessageModel(self):
        r"""消费模式：
BROADCASTING 广播模式
CLUSTERING 集群模式
        :rtype: str
        """
        return self._MessageModel

    @MessageModel.setter
    def MessageModel(self, MessageModel):
        self._MessageModel = MessageModel

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
        self._ConsumerNum = params.get("ConsumerNum")
        self._Tps = params.get("Tps")
        self._ConsumerLag = params.get("ConsumerLag")
        self._ConsumeType = params.get("ConsumeType")
        self._CreatedTime = params.get("CreatedTime")
        self._ConsumeMessageOrderly = params.get("ConsumeMessageOrderly")
        self._ConsumeEnable = params.get("ConsumeEnable")
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._Remark = params.get("Remark")
        self._MessageModel = params.get("MessageModel")
        self._RequestId = params.get("RequestId")


class DescribeConsumerLagRequest(AbstractModel):
    r"""DescribeConsumerLag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        :param _Namespace: 命名空间，4.x集群必填，从 [DescribeRocketMQNamespaces](https://cloud.tencent.com/document/api/1179/63419) 接口返回的 [RocketMQNamespace](https://cloud.tencent.com/document/api/1179/46089#RocketMQNamespace) 或控制台获得。
        :type Namespace: str
        :param _SubscribeTopic: 订阅主题，不为空则查询订阅了该主题的消费组的堆积，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type SubscribeTopic: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._Namespace = None
        self._SubscribeTopic = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def Namespace(self):
        r"""命名空间，4.x集群必填，从 [DescribeRocketMQNamespaces](https://cloud.tencent.com/document/api/1179/63419) 接口返回的 [RocketMQNamespace](https://cloud.tencent.com/document/api/1179/46089#RocketMQNamespace) 或控制台获得。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def SubscribeTopic(self):
        r"""订阅主题，不为空则查询订阅了该主题的消费组的堆积，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._SubscribeTopic

    @SubscribeTopic.setter
    def SubscribeTopic(self, SubscribeTopic):
        self._SubscribeTopic = SubscribeTopic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._Namespace = params.get("Namespace")
        self._SubscribeTopic = params.get("SubscribeTopic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerLagResponse(AbstractModel):
    r"""DescribeConsumerLag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsumerLag: 堆积数
        :type ConsumerLag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConsumerLag = None
        self._RequestId = None

    @property
    def ConsumerLag(self):
        r"""堆积数
        :rtype: int
        """
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

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
        self._ConsumerLag = params.get("ConsumerLag")
        self._RequestId = params.get("RequestId")


class DescribeFusionInstanceListRequest(AbstractModel):
    r"""DescribeFusionInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤器
        :type TagFilters: list of TagFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagFilters = None

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        r"""标签过滤器
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFusionInstanceListResponse(AbstractModel):
    r"""DescribeFusionInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 实例列表
        :type Data: list of FusionInstanceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""实例列表
        :rtype: list of FusionInstanceItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = FusionInstanceItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    r"""DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤器
        :type TagFilters: list of TagFilter
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        """
        self._Filters = None
        self._TagFilters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        r"""标签过滤器
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    r"""DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 实例列表
        :type Data: list of InstanceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""实例列表
        :rtype: list of InstanceItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = InstanceItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    r"""DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
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
        


class DescribeInstanceResponse(AbstractModel):
    r"""DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :type InstanceType: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _TopicNumLimit: 实例最大主题数量
        :type TopicNumLimit: int
        :param _GroupNum: 消费组数量
        :type GroupNum: int
        :param _GroupNumLimit: 实例最大消费组数量
        :type GroupNumLimit: int
        :param _MessageRetention: 消息保留时间，小时为单位
        :type MessageRetention: int
        :param _RetentionUpperLimit: 最大可调整消息保留时间，小时为单位
        :type RetentionUpperLimit: int
        :param _RetentionLowerLimit: 最小可调整消息保留时间，小时为单位
        :type RetentionLowerLimit: int
        :param _TpsLimit: TPS限流值
        :type TpsLimit: int
        :param _ScaledTpsLimit: 弹性TPS限流值
        :type ScaledTpsLimit: int
        :param _MaxMessageDelay: 延迟消息最长时间，小时为单位
        :type MaxMessageDelay: int
        :param _CreatedTime: 创建时间，**Unix时间戳（毫秒）**
        :type CreatedTime: int
        :param _SendReceiveRatio: 消息发送接收比例
        :type SendReceiveRatio: float
        :param _TagList: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        :param _EndpointList: 接入点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EndpointList: list of Endpoint
        :param _TopicQueueNumUpperLimit: 主题队列数上限
        :type TopicQueueNumUpperLimit: int
        :param _TopicQueueNumLowerLimit: 主题队列数下限
        :type TopicQueueNumLowerLimit: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _InstanceStatus: 实例状态，枚举值如下：

- RUNNING：运行中
- ABNORMAL：异常
- OVERDUE：隔离中
- DESTROYED：已销毁
- CREATING：创建中
- MODIFYING：变配中
- CREATE_FAILURE：创建失败
- MODIFY_FAILURE：变配失败
- DELETING：删除中
        :type InstanceStatus: str
        :param _SkuCode: 实例规格
        :type SkuCode: str
        :param _PayMode: 计费模式，枚举值如下：

- POSTPAID：后付费按量计费
- PREPAID：预付费包年包月
        :type PayMode: str
        :param _ScaledTpsEnabled: 是否开启弹性TPS
        :type ScaledTpsEnabled: bool
        :param _RenewFlag: 预付费集群是否自动续费，枚举值如下：

- 0: 不自动续费
- 1: 自动续费
        :type RenewFlag: int
        :param _ExpiryTime: 到期时间，**Unix时间戳（毫秒）**
        :type ExpiryTime: int
        :param _RoleNumLimit: 角色数量限制
        :type RoleNumLimit: int
        :param _AclEnabled: 是否开启 ACL
注意：此字段可能返回 null，表示取不到有效值。
        :type AclEnabled: bool
        :param _TopicNumLowerLimit: topic个数免费额度
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNumLowerLimit: int
        :param _TopicNumUpperLimit: 最大可设置的topic个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNumUpperLimit: int
        :param _ZoneIds: 所属可用区列表，参考 [DescribeZones](https://cloud.tencent.com/document/product/1596/77929) 接口返回中的 [ZoneInfo](https://cloud.tencent.com/document/api/1596/77932#ZoneInfo) 数据结构。
        :type ZoneIds: list of int
        :param _NodeCount: proxy节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeCount: int
        :param _ZoneScheduledList: proxy调度详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneScheduledList: list of ZoneScheduledItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None
        self._TopicNum = None
        self._TopicNumLimit = None
        self._GroupNum = None
        self._GroupNumLimit = None
        self._MessageRetention = None
        self._RetentionUpperLimit = None
        self._RetentionLowerLimit = None
        self._TpsLimit = None
        self._ScaledTpsLimit = None
        self._MaxMessageDelay = None
        self._CreatedTime = None
        self._SendReceiveRatio = None
        self._TagList = None
        self._EndpointList = None
        self._TopicQueueNumUpperLimit = None
        self._TopicQueueNumLowerLimit = None
        self._Remark = None
        self._InstanceStatus = None
        self._SkuCode = None
        self._PayMode = None
        self._ScaledTpsEnabled = None
        self._RenewFlag = None
        self._ExpiryTime = None
        self._RoleNumLimit = None
        self._AclEnabled = None
        self._TopicNumLowerLimit = None
        self._TopicNumUpperLimit = None
        self._ZoneIds = None
        self._NodeCount = None
        self._ZoneScheduledList = None
        self._RequestId = None

    @property
    def InstanceType(self):
        r"""实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicNum(self):
        r"""主题数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def TopicNumLimit(self):
        r"""实例最大主题数量
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def GroupNum(self):
        r"""消费组数量
        :rtype: int
        """
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def GroupNumLimit(self):
        r"""实例最大消费组数量
        :rtype: int
        """
        return self._GroupNumLimit

    @GroupNumLimit.setter
    def GroupNumLimit(self, GroupNumLimit):
        self._GroupNumLimit = GroupNumLimit

    @property
    def MessageRetention(self):
        r"""消息保留时间，小时为单位
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def RetentionUpperLimit(self):
        r"""最大可调整消息保留时间，小时为单位
        :rtype: int
        """
        return self._RetentionUpperLimit

    @RetentionUpperLimit.setter
    def RetentionUpperLimit(self, RetentionUpperLimit):
        self._RetentionUpperLimit = RetentionUpperLimit

    @property
    def RetentionLowerLimit(self):
        r"""最小可调整消息保留时间，小时为单位
        :rtype: int
        """
        return self._RetentionLowerLimit

    @RetentionLowerLimit.setter
    def RetentionLowerLimit(self, RetentionLowerLimit):
        self._RetentionLowerLimit = RetentionLowerLimit

    @property
    def TpsLimit(self):
        r"""TPS限流值
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ScaledTpsLimit(self):
        r"""弹性TPS限流值
        :rtype: int
        """
        return self._ScaledTpsLimit

    @ScaledTpsLimit.setter
    def ScaledTpsLimit(self, ScaledTpsLimit):
        self._ScaledTpsLimit = ScaledTpsLimit

    @property
    def MaxMessageDelay(self):
        r"""延迟消息最长时间，小时为单位
        :rtype: int
        """
        return self._MaxMessageDelay

    @MaxMessageDelay.setter
    def MaxMessageDelay(self, MaxMessageDelay):
        self._MaxMessageDelay = MaxMessageDelay

    @property
    def CreatedTime(self):
        r"""创建时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def SendReceiveRatio(self):
        r"""消息发送接收比例
        :rtype: float
        """
        return self._SendReceiveRatio

    @SendReceiveRatio.setter
    def SendReceiveRatio(self, SendReceiveRatio):
        self._SendReceiveRatio = SendReceiveRatio

    @property
    def TagList(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def EndpointList(self):
        r"""接入点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Endpoint
        """
        return self._EndpointList

    @EndpointList.setter
    def EndpointList(self, EndpointList):
        self._EndpointList = EndpointList

    @property
    def TopicQueueNumUpperLimit(self):
        r"""主题队列数上限
        :rtype: int
        """
        return self._TopicQueueNumUpperLimit

    @TopicQueueNumUpperLimit.setter
    def TopicQueueNumUpperLimit(self, TopicQueueNumUpperLimit):
        self._TopicQueueNumUpperLimit = TopicQueueNumUpperLimit

    @property
    def TopicQueueNumLowerLimit(self):
        r"""主题队列数下限
        :rtype: int
        """
        return self._TopicQueueNumLowerLimit

    @TopicQueueNumLowerLimit.setter
    def TopicQueueNumLowerLimit(self, TopicQueueNumLowerLimit):
        self._TopicQueueNumLowerLimit = TopicQueueNumLowerLimit

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceStatus(self):
        r"""实例状态，枚举值如下：

- RUNNING：运行中
- ABNORMAL：异常
- OVERDUE：隔离中
- DESTROYED：已销毁
- CREATING：创建中
- MODIFYING：变配中
- CREATE_FAILURE：创建失败
- MODIFY_FAILURE：变配失败
- DELETING：删除中
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SkuCode(self):
        r"""实例规格
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def PayMode(self):
        r"""计费模式，枚举值如下：

- POSTPAID：后付费按量计费
- PREPAID：预付费包年包月
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ScaledTpsEnabled(self):
        r"""是否开启弹性TPS
        :rtype: bool
        """
        return self._ScaledTpsEnabled

    @ScaledTpsEnabled.setter
    def ScaledTpsEnabled(self, ScaledTpsEnabled):
        self._ScaledTpsEnabled = ScaledTpsEnabled

    @property
    def RenewFlag(self):
        r"""预付费集群是否自动续费，枚举值如下：

- 0: 不自动续费
- 1: 自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpiryTime(self):
        r"""到期时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def RoleNumLimit(self):
        r"""角色数量限制
        :rtype: int
        """
        return self._RoleNumLimit

    @RoleNumLimit.setter
    def RoleNumLimit(self, RoleNumLimit):
        self._RoleNumLimit = RoleNumLimit

    @property
    def AclEnabled(self):
        r"""是否开启 ACL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AclEnabled

    @AclEnabled.setter
    def AclEnabled(self, AclEnabled):
        self._AclEnabled = AclEnabled

    @property
    def TopicNumLowerLimit(self):
        r"""topic个数免费额度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNumLowerLimit

    @TopicNumLowerLimit.setter
    def TopicNumLowerLimit(self, TopicNumLowerLimit):
        self._TopicNumLowerLimit = TopicNumLowerLimit

    @property
    def TopicNumUpperLimit(self):
        r"""最大可设置的topic个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNumUpperLimit

    @TopicNumUpperLimit.setter
    def TopicNumUpperLimit(self, TopicNumUpperLimit):
        self._TopicNumUpperLimit = TopicNumUpperLimit

    @property
    def ZoneIds(self):
        r"""所属可用区列表，参考 [DescribeZones](https://cloud.tencent.com/document/product/1596/77929) 接口返回中的 [ZoneInfo](https://cloud.tencent.com/document/api/1596/77932#ZoneInfo) 数据结构。
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def NodeCount(self):
        r"""proxy节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def ZoneScheduledList(self):
        r"""proxy调度详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ZoneScheduledItem
        """
        return self._ZoneScheduledList

    @ZoneScheduledList.setter
    def ZoneScheduledList(self, ZoneScheduledList):
        self._ZoneScheduledList = ZoneScheduledList

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
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._TopicNum = params.get("TopicNum")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._GroupNum = params.get("GroupNum")
        self._GroupNumLimit = params.get("GroupNumLimit")
        self._MessageRetention = params.get("MessageRetention")
        self._RetentionUpperLimit = params.get("RetentionUpperLimit")
        self._RetentionLowerLimit = params.get("RetentionLowerLimit")
        self._TpsLimit = params.get("TpsLimit")
        self._ScaledTpsLimit = params.get("ScaledTpsLimit")
        self._MaxMessageDelay = params.get("MaxMessageDelay")
        self._CreatedTime = params.get("CreatedTime")
        self._SendReceiveRatio = params.get("SendReceiveRatio")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        if params.get("EndpointList") is not None:
            self._EndpointList = []
            for item in params.get("EndpointList"):
                obj = Endpoint()
                obj._deserialize(item)
                self._EndpointList.append(obj)
        self._TopicQueueNumUpperLimit = params.get("TopicQueueNumUpperLimit")
        self._TopicQueueNumLowerLimit = params.get("TopicQueueNumLowerLimit")
        self._Remark = params.get("Remark")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SkuCode = params.get("SkuCode")
        self._PayMode = params.get("PayMode")
        self._ScaledTpsEnabled = params.get("ScaledTpsEnabled")
        self._RenewFlag = params.get("RenewFlag")
        self._ExpiryTime = params.get("ExpiryTime")
        self._RoleNumLimit = params.get("RoleNumLimit")
        self._AclEnabled = params.get("AclEnabled")
        self._TopicNumLowerLimit = params.get("TopicNumLowerLimit")
        self._TopicNumUpperLimit = params.get("TopicNumUpperLimit")
        self._ZoneIds = params.get("ZoneIds")
        self._NodeCount = params.get("NodeCount")
        if params.get("ZoneScheduledList") is not None:
            self._ZoneScheduledList = []
            for item in params.get("ZoneScheduledList"):
                obj = ZoneScheduledItem()
                obj._deserialize(item)
                self._ZoneScheduledList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMQTTClientRequest(AbstractModel):
    r"""DescribeMQTTClient请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ClientId: 客户端详情
        :type ClientId: str
        """
        self._InstanceId = None
        self._ClientId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClientId(self):
        r"""客户端详情
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMQTTClientResponse(AbstractModel):
    r"""DescribeMQTTClient返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientId: 客户端唯一标识
        :type ClientId: str
        :param _ClientAddress: 客户端网络地址
        :type ClientAddress: str
        :param _ProtocolVersion: MQTT 协议版本，4 表示 MQTT 3.1.1
        :type ProtocolVersion: int
        :param _Keepalive: 保持连接时间，单位：秒
        :type Keepalive: int
        :param _ConnectionStatus: 连接状态，CONNECTED 已连接，DISCONNECTED 未连接
        :type ConnectionStatus: str
        :param _CreateTime: 客户端创建时间
        :type CreateTime: int
        :param _ConnectTime: 上次建立连接时间
        :type ConnectTime: int
        :param _DisconnectTime: 上次断开连接时间，仅对持久会话（cleanSession=false）并且客户端当前未连接时有意义
        :type DisconnectTime: int
        :param _MQTTClientSubscriptions: 客户端的订阅列表
        :type MQTTClientSubscriptions: list of MQTTClientSubscription
        :param _Inbound: 服务端到客户端的流量统计
        :type Inbound: :class:`tencentcloud.trocket.v20230308.models.StatisticsReport`
        :param _OutBound: 客户端到服务端的流量统计
        :type OutBound: :class:`tencentcloud.trocket.v20230308.models.StatisticsReport`
        :param _CleanSession: cleansession标志
        :type CleanSession: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClientId = None
        self._ClientAddress = None
        self._ProtocolVersion = None
        self._Keepalive = None
        self._ConnectionStatus = None
        self._CreateTime = None
        self._ConnectTime = None
        self._DisconnectTime = None
        self._MQTTClientSubscriptions = None
        self._Inbound = None
        self._OutBound = None
        self._CleanSession = None
        self._RequestId = None

    @property
    def ClientId(self):
        r"""客户端唯一标识
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientAddress(self):
        r"""客户端网络地址
        :rtype: str
        """
        return self._ClientAddress

    @ClientAddress.setter
    def ClientAddress(self, ClientAddress):
        self._ClientAddress = ClientAddress

    @property
    def ProtocolVersion(self):
        r"""MQTT 协议版本，4 表示 MQTT 3.1.1
        :rtype: int
        """
        return self._ProtocolVersion

    @ProtocolVersion.setter
    def ProtocolVersion(self, ProtocolVersion):
        self._ProtocolVersion = ProtocolVersion

    @property
    def Keepalive(self):
        r"""保持连接时间，单位：秒
        :rtype: int
        """
        return self._Keepalive

    @Keepalive.setter
    def Keepalive(self, Keepalive):
        self._Keepalive = Keepalive

    @property
    def ConnectionStatus(self):
        r"""连接状态，CONNECTED 已连接，DISCONNECTED 未连接
        :rtype: str
        """
        return self._ConnectionStatus

    @ConnectionStatus.setter
    def ConnectionStatus(self, ConnectionStatus):
        self._ConnectionStatus = ConnectionStatus

    @property
    def CreateTime(self):
        r"""客户端创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ConnectTime(self):
        r"""上次建立连接时间
        :rtype: int
        """
        return self._ConnectTime

    @ConnectTime.setter
    def ConnectTime(self, ConnectTime):
        self._ConnectTime = ConnectTime

    @property
    def DisconnectTime(self):
        r"""上次断开连接时间，仅对持久会话（cleanSession=false）并且客户端当前未连接时有意义
        :rtype: int
        """
        return self._DisconnectTime

    @DisconnectTime.setter
    def DisconnectTime(self, DisconnectTime):
        self._DisconnectTime = DisconnectTime

    @property
    def MQTTClientSubscriptions(self):
        r"""客户端的订阅列表
        :rtype: list of MQTTClientSubscription
        """
        return self._MQTTClientSubscriptions

    @MQTTClientSubscriptions.setter
    def MQTTClientSubscriptions(self, MQTTClientSubscriptions):
        self._MQTTClientSubscriptions = MQTTClientSubscriptions

    @property
    def Inbound(self):
        r"""服务端到客户端的流量统计
        :rtype: :class:`tencentcloud.trocket.v20230308.models.StatisticsReport`
        """
        return self._Inbound

    @Inbound.setter
    def Inbound(self, Inbound):
        self._Inbound = Inbound

    @property
    def OutBound(self):
        r"""客户端到服务端的流量统计
        :rtype: :class:`tencentcloud.trocket.v20230308.models.StatisticsReport`
        """
        return self._OutBound

    @OutBound.setter
    def OutBound(self, OutBound):
        self._OutBound = OutBound

    @property
    def CleanSession(self):
        r"""cleansession标志
        :rtype: bool
        """
        return self._CleanSession

    @CleanSession.setter
    def CleanSession(self, CleanSession):
        self._CleanSession = CleanSession

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
        self._ClientId = params.get("ClientId")
        self._ClientAddress = params.get("ClientAddress")
        self._ProtocolVersion = params.get("ProtocolVersion")
        self._Keepalive = params.get("Keepalive")
        self._ConnectionStatus = params.get("ConnectionStatus")
        self._CreateTime = params.get("CreateTime")
        self._ConnectTime = params.get("ConnectTime")
        self._DisconnectTime = params.get("DisconnectTime")
        if params.get("MQTTClientSubscriptions") is not None:
            self._MQTTClientSubscriptions = []
            for item in params.get("MQTTClientSubscriptions"):
                obj = MQTTClientSubscription()
                obj._deserialize(item)
                self._MQTTClientSubscriptions.append(obj)
        if params.get("Inbound") is not None:
            self._Inbound = StatisticsReport()
            self._Inbound._deserialize(params.get("Inbound"))
        if params.get("OutBound") is not None:
            self._OutBound = StatisticsReport()
            self._OutBound._deserialize(params.get("OutBound"))
        self._CleanSession = params.get("CleanSession")
        self._RequestId = params.get("RequestId")


class DescribeMQTTInsPublicEndpointsRequest(AbstractModel):
    r"""DescribeMQTTInsPublicEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群ID
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
        


class DescribeMQTTInsPublicEndpointsResponse(AbstractModel):
    r"""DescribeMQTTInsPublicEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoints: 接入点
        :type Endpoints: list of MQTTEndpointItem
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Bandwidth: 带宽
        :type Bandwidth: int
        :param _Rules: 公网访问规则
        :type Rules: list of PublicAccessRule
        :param _Status: 公网状态：
    NORMAL-正常
    CLOSING-关闭中
    MODIFYING-修改中
    CREATING-开启中
    CLOSE-关闭
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoints = None
        self._InstanceId = None
        self._Bandwidth = None
        self._Rules = None
        self._Status = None
        self._RequestId = None

    @property
    def Endpoints(self):
        r"""接入点
        :rtype: list of MQTTEndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        r"""带宽
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Rules(self):
        r"""公网访问规则
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Status(self):
        r"""公网状态：
    NORMAL-正常
    CLOSING-关闭中
    MODIFYING-修改中
    CREATING-开启中
    CLOSE-关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = MQTTEndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeMQTTInsVPCEndpointsRequest(AbstractModel):
    r"""DescribeMQTTInsVPCEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""实例ID
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
        


class DescribeMQTTInsVPCEndpointsResponse(AbstractModel):
    r"""DescribeMQTTInsVPCEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoints: 接入点
        :type Endpoints: list of MQTTEndpointItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoints = None
        self._RequestId = None

    @property
    def Endpoints(self):
        r"""接入点
        :rtype: list of MQTTEndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

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
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = MQTTEndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMQTTInstanceCertRequest(AbstractModel):
    r"""DescribeMQTTInstanceCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群ID
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
        


class DescribeMQTTInstanceCertResponse(AbstractModel):
    r"""DescribeMQTTInstanceCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _SSLServerCertId: 服务端证书id
注意：此字段可能返回 null，表示取不到有效值。
        :type SSLServerCertId: str
        :param _SSLCaCertId: CA证书id
注意：此字段可能返回 null，表示取不到有效值。
        :type SSLCaCertId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._SSLServerCertId = None
        self._SSLCaCertId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""集群id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SSLServerCertId(self):
        r"""服务端证书id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SSLServerCertId

    @SSLServerCertId.setter
    def SSLServerCertId(self, SSLServerCertId):
        self._SSLServerCertId = SSLServerCertId

    @property
    def SSLCaCertId(self):
        r"""CA证书id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SSLCaCertId

    @SSLCaCertId.setter
    def SSLCaCertId(self, SSLCaCertId):
        self._SSLCaCertId = SSLCaCertId

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
        self._InstanceId = params.get("InstanceId")
        self._SSLServerCertId = params.get("SSLServerCertId")
        self._SSLCaCertId = params.get("SSLCaCertId")
        self._RequestId = params.get("RequestId")


class DescribeMQTTInstanceListRequest(AbstractModel):
    r"""DescribeMQTTInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        :param _IncludeNew: 是否包含新控制台集群：默认为包含
        :type IncludeNew: bool
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._IncludeNew = None

    @property
    def Filters(self):
        r"""查询条件列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def IncludeNew(self):
        r"""是否包含新控制台集群：默认为包含
        :rtype: bool
        """
        return self._IncludeNew

    @IncludeNew.setter
    def IncludeNew(self, IncludeNew):
        self._IncludeNew = IncludeNew


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IncludeNew = params.get("IncludeNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMQTTInstanceListResponse(AbstractModel):
    r"""DescribeMQTTInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 实例列表
        :type Data: list of MQTTInstanceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""实例列表
        :rtype: list of MQTTInstanceItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTInstanceItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMQTTInstanceRequest(AbstractModel):
    r"""DescribeMQTTInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""集群ID
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
        


class DescribeMQTTInstanceResponse(AbstractModel):
    r"""DescribeMQTTInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :type InstanceType: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _TopicNumLimit: 实例最大主题数量
        :type TopicNumLimit: int
        :param _TpsLimit: TPS限流值
        :type TpsLimit: int
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param _SkuCode: 实例规格
        :type SkuCode: str
        :param _SubscriptionNumLimit: 订阅数上限
        :type SubscriptionNumLimit: int
        :param _ClientNumLimit: 客户端数量上限
        :type ClientNumLimit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None
        self._TopicNum = None
        self._TopicNumLimit = None
        self._TpsLimit = None
        self._CreatedTime = None
        self._Remark = None
        self._InstanceStatus = None
        self._SkuCode = None
        self._SubscriptionNumLimit = None
        self._ClientNumLimit = None
        self._RequestId = None

    @property
    def InstanceType(self):
        r"""实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicNum(self):
        r"""主题数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def TopicNumLimit(self):
        r"""实例最大主题数量
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def TpsLimit(self):
        r"""TPS限流值
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreatedTime(self):
        r"""创建时间，秒为单位
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceStatus(self):
        r"""实例状态
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SkuCode(self):
        r"""实例规格
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def SubscriptionNumLimit(self):
        r"""订阅数上限
        :rtype: int
        """
        return self._SubscriptionNumLimit

    @SubscriptionNumLimit.setter
    def SubscriptionNumLimit(self, SubscriptionNumLimit):
        self._SubscriptionNumLimit = SubscriptionNumLimit

    @property
    def ClientNumLimit(self):
        r"""客户端数量上限
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

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
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._TopicNum = params.get("TopicNum")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._TpsLimit = params.get("TpsLimit")
        self._CreatedTime = params.get("CreatedTime")
        self._Remark = params.get("Remark")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SkuCode = params.get("SkuCode")
        self._SubscriptionNumLimit = params.get("SubscriptionNumLimit")
        self._ClientNumLimit = params.get("ClientNumLimit")
        self._RequestId = params.get("RequestId")


class DescribeMQTTMessageListRequest(AbstractModel):
    r"""DescribeMQTTMessageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _TaskRequestId: 请求任务id
        :type TaskRequestId: str
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        """
        self._InstanceId = None
        self._Topic = None
        self._StartTime = None
        self._EndTime = None
        self._TaskRequestId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskRequestId(self):
        r"""请求任务id
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

    @property
    def Offset(self):
        r"""查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskRequestId = params.get("TaskRequestId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMQTTMessageListResponse(AbstractModel):
    r"""DescribeMQTTMessageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 消息记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of MQTTMessageItem
        :param _TaskRequestId: 请求任务id
        :type TaskRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._TaskRequestId = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""消息记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MQTTMessageItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TaskRequestId(self):
        r"""请求任务id
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTMessageItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TaskRequestId = params.get("TaskRequestId")
        self._RequestId = params.get("RequestId")


class DescribeMQTTMessageRequest(AbstractModel):
    r"""DescribeMQTTMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _MsgId: 消息ID
        :type MsgId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._MsgId = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def MsgId(self):
        r"""消息ID
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._MsgId = params.get("MsgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMQTTMessageResponse(AbstractModel):
    r"""DescribeMQTTMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Body: 消息体
        :type Body: str
        :param _Properties: 详情参数
        :type Properties: list of CustomMapEntry
        :param _ProduceTime: 生产时间
        :type ProduceTime: str
        :param _MessageId: 消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: str
        :param _ProducerAddr: 生产者地址
        :type ProducerAddr: str
        :param _ShowTopicName: Topic
        :type ShowTopicName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Body = None
        self._Properties = None
        self._ProduceTime = None
        self._MessageId = None
        self._ProducerAddr = None
        self._ShowTopicName = None
        self._RequestId = None

    @property
    def Body(self):
        r"""消息体
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Properties(self):
        r"""详情参数
        :rtype: list of CustomMapEntry
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ProduceTime(self):
        r"""生产时间
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def MessageId(self):
        r"""消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ProducerAddr(self):
        r"""生产者地址
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def ShowTopicName(self):
        r"""Topic
        :rtype: str
        """
        return self._ShowTopicName

    @ShowTopicName.setter
    def ShowTopicName(self, ShowTopicName):
        self._ShowTopicName = ShowTopicName

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
        self._Body = params.get("Body")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = CustomMapEntry()
                obj._deserialize(item)
                self._Properties.append(obj)
        self._ProduceTime = params.get("ProduceTime")
        self._MessageId = params.get("MessageId")
        self._ProducerAddr = params.get("ProducerAddr")
        self._ShowTopicName = params.get("ShowTopicName")
        self._RequestId = params.get("RequestId")


class DescribeMQTTProductSKUListRequest(AbstractModel):
    r"""DescribeMQTTProductSKUList请求参数结构体

    """


class DescribeMQTTProductSKUListResponse(AbstractModel):
    r"""DescribeMQTTProductSKUList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _MQTTProductSkuList: mqtt商品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MQTTProductSkuList: list of MQTTProductSkuItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MQTTProductSkuList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MQTTProductSkuList(self):
        r"""mqtt商品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MQTTProductSkuItem
        """
        return self._MQTTProductSkuList

    @MQTTProductSkuList.setter
    def MQTTProductSkuList(self, MQTTProductSkuList):
        self._MQTTProductSkuList = MQTTProductSkuList

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
        if params.get("MQTTProductSkuList") is not None:
            self._MQTTProductSkuList = []
            for item in params.get("MQTTProductSkuList"):
                obj = MQTTProductSkuItem()
                obj._deserialize(item)
                self._MQTTProductSkuList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMQTTTopicListRequest(AbstractModel):
    r"""DescribeMQTTTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        r"""查询条件列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMQTTTopicListResponse(AbstractModel):
    r"""DescribeMQTTTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 主题列表
        :type Data: list of MQTTTopicItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""主题列表
        :rtype: list of MQTTTopicItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTTopicItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMQTTTopicRequest(AbstractModel):
    r"""DescribeMQTTTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMQTTTopicResponse(AbstractModel):
    r"""DescribeMQTTTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Remark: 备注
        :type Remark: str
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None
        self._CreatedTime = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        r"""创建时间，秒为单位
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

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
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        self._CreatedTime = params.get("CreatedTime")
        self._RequestId = params.get("RequestId")


class DescribeMQTTUserListRequest(AbstractModel):
    r"""DescribeMQTTUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        r"""查询条件列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMQTTUserListResponse(AbstractModel):
    r"""DescribeMQTTUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 角色信息列表
        :type Data: list of MQTTUserItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""角色信息列表
        :rtype: list of MQTTUserItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTUserItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMessageListRequest(AbstractModel):
    r"""DescribeMessageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _StartTime: 要查询消息的开始时间，**Unix时间戳（毫秒）**
        :type StartTime: int
        :param _EndTime: 要查询消息的结束时间，**Unix时间戳（毫秒）**
        :type EndTime: int
        :param _TaskRequestId: 一次查询标识。第一次查询可传空字符串，当查询结果涉及分页，请求下一页数据时该入参的值取上一次请求响应中的出参TaskRequestId 值即可。
        :type TaskRequestId: str
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        :param _MsgId: 消息 ID，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :type MsgId: str
        :param _MsgKey: 消息 Key，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :type MsgKey: str
        :param _RecentMessageNum: 查询最近N条消息 最大不超过1024，默认-1为其他查询条件
        :type RecentMessageNum: int
        :param _QueryDeadLetterMessage: 是否查询死信消息，默认为false
        :type QueryDeadLetterMessage: bool
        :param _Tag: 消息 Tag，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :type Tag: str
        """
        self._InstanceId = None
        self._Topic = None
        self._StartTime = None
        self._EndTime = None
        self._TaskRequestId = None
        self._Offset = None
        self._Limit = None
        self._ConsumerGroup = None
        self._MsgId = None
        self._MsgKey = None
        self._RecentMessageNum = None
        self._QueryDeadLetterMessage = None
        self._Tag = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def StartTime(self):
        r"""要查询消息的开始时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""要查询消息的结束时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskRequestId(self):
        r"""一次查询标识。第一次查询可传空字符串，当查询结果涉及分页，请求下一页数据时该入参的值取上一次请求响应中的出参TaskRequestId 值即可。
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def MsgId(self):
        r"""消息 ID，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def MsgKey(self):
        r"""消息 Key，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :rtype: str
        """
        return self._MsgKey

    @MsgKey.setter
    def MsgKey(self, MsgKey):
        self._MsgKey = MsgKey

    @property
    def RecentMessageNum(self):
        r"""查询最近N条消息 最大不超过1024，默认-1为其他查询条件
        :rtype: int
        """
        return self._RecentMessageNum

    @RecentMessageNum.setter
    def RecentMessageNum(self, RecentMessageNum):
        self._RecentMessageNum = RecentMessageNum

    @property
    def QueryDeadLetterMessage(self):
        r"""是否查询死信消息，默认为false
        :rtype: bool
        """
        return self._QueryDeadLetterMessage

    @QueryDeadLetterMessage.setter
    def QueryDeadLetterMessage(self, QueryDeadLetterMessage):
        self._QueryDeadLetterMessage = QueryDeadLetterMessage

    @property
    def Tag(self):
        r"""消息 Tag，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskRequestId = params.get("TaskRequestId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._MsgId = params.get("MsgId")
        self._MsgKey = params.get("MsgKey")
        self._RecentMessageNum = params.get("RecentMessageNum")
        self._QueryDeadLetterMessage = params.get("QueryDeadLetterMessage")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageListResponse(AbstractModel):
    r"""DescribeMessageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 消息记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of MessageItem
        :param _TaskRequestId: 一次查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._TaskRequestId = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""消息记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MessageItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TaskRequestId(self):
        r"""一次查询ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MessageItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TaskRequestId = params.get("TaskRequestId")
        self._RequestId = params.get("RequestId")


class DescribeMessageRequest(AbstractModel):
    r"""DescribeMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _MsgId: 消息 ID，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口或业务日志中获得。
        :type MsgId: str
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _QueryDeadLetterMessage: 是否是死信消息，默认为false
        :type QueryDeadLetterMessage: bool
        :param _QueryDelayMessage: 是否是延时消息，默认为false
        :type QueryDelayMessage: bool
        """
        self._InstanceId = None
        self._Topic = None
        self._MsgId = None
        self._Offset = None
        self._Limit = None
        self._QueryDeadLetterMessage = None
        self._QueryDelayMessage = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def MsgId(self):
        r"""消息 ID，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口或业务日志中获得。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QueryDeadLetterMessage(self):
        r"""是否是死信消息，默认为false
        :rtype: bool
        """
        return self._QueryDeadLetterMessage

    @QueryDeadLetterMessage.setter
    def QueryDeadLetterMessage(self, QueryDeadLetterMessage):
        self._QueryDeadLetterMessage = QueryDeadLetterMessage

    @property
    def QueryDelayMessage(self):
        r"""是否是延时消息，默认为false
        :rtype: bool
        """
        return self._QueryDelayMessage

    @QueryDelayMessage.setter
    def QueryDelayMessage(self, QueryDelayMessage):
        self._QueryDelayMessage = QueryDelayMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._MsgId = params.get("MsgId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._QueryDeadLetterMessage = params.get("QueryDeadLetterMessage")
        self._QueryDelayMessage = params.get("QueryDelayMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageResponse(AbstractModel):
    r"""DescribeMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Body: 消息体
        :type Body: str
        :param _Properties: 详情参数
        :type Properties: str
        :param _ProduceTime: 生产时间
        :type ProduceTime: str
        :param _MessageId: 消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageId: str
        :param _ProducerAddr: 生产者地址
        :type ProducerAddr: str
        :param _MessageTracks: 消息消费情况列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageTracks: list of MessageTrackItem
        :param _ShowTopicName: 主题名称
        :type ShowTopicName: str
        :param _MessageTracksCount: 消息消费情况列表总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageTracksCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Body = None
        self._Properties = None
        self._ProduceTime = None
        self._MessageId = None
        self._ProducerAddr = None
        self._MessageTracks = None
        self._ShowTopicName = None
        self._MessageTracksCount = None
        self._RequestId = None

    @property
    def Body(self):
        r"""消息体
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Properties(self):
        r"""详情参数
        :rtype: str
        """
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties

    @property
    def ProduceTime(self):
        r"""生产时间
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def MessageId(self):
        r"""消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ProducerAddr(self):
        r"""生产者地址
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def MessageTracks(self):
        r"""消息消费情况列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MessageTrackItem
        """
        return self._MessageTracks

    @MessageTracks.setter
    def MessageTracks(self, MessageTracks):
        self._MessageTracks = MessageTracks

    @property
    def ShowTopicName(self):
        r"""主题名称
        :rtype: str
        """
        return self._ShowTopicName

    @ShowTopicName.setter
    def ShowTopicName(self, ShowTopicName):
        self._ShowTopicName = ShowTopicName

    @property
    def MessageTracksCount(self):
        r"""消息消费情况列表总条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MessageTracksCount

    @MessageTracksCount.setter
    def MessageTracksCount(self, MessageTracksCount):
        self._MessageTracksCount = MessageTracksCount

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
        self._Body = params.get("Body")
        self._Properties = params.get("Properties")
        self._ProduceTime = params.get("ProduceTime")
        self._MessageId = params.get("MessageId")
        self._ProducerAddr = params.get("ProducerAddr")
        if params.get("MessageTracks") is not None:
            self._MessageTracks = []
            for item in params.get("MessageTracks"):
                obj = MessageTrackItem()
                obj._deserialize(item)
                self._MessageTracks.append(obj)
        self._ShowTopicName = params.get("ShowTopicName")
        self._MessageTracksCount = params.get("MessageTracksCount")
        self._RequestId = params.get("RequestId")


class DescribeMessageTraceRequest(AbstractModel):
    r"""DescribeMessageTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _MsgId: 消息 ID，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :type MsgId: str
        :param _QueryDeadLetterMessage: 是否是死信消息，默认为false
        :type QueryDeadLetterMessage: bool
        :param _QueryDelayMessage: 是否是延时消息，默认为false
        :type QueryDelayMessage: bool
        """
        self._InstanceId = None
        self._Topic = None
        self._MsgId = None
        self._QueryDeadLetterMessage = None
        self._QueryDelayMessage = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def MsgId(self):
        r"""消息 ID，从 [DescribeMessageList](https://cloud.tencent.com/document/api/1493/114593) 接口返回的 [MessageItem](https://cloud.tencent.com/document/api/1493/96031#MessageItem) 或业务日志中获得。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def QueryDeadLetterMessage(self):
        r"""是否是死信消息，默认为false
        :rtype: bool
        """
        return self._QueryDeadLetterMessage

    @QueryDeadLetterMessage.setter
    def QueryDeadLetterMessage(self, QueryDeadLetterMessage):
        self._QueryDeadLetterMessage = QueryDeadLetterMessage

    @property
    def QueryDelayMessage(self):
        r"""是否是延时消息，默认为false
        :rtype: bool
        """
        return self._QueryDelayMessage

    @QueryDelayMessage.setter
    def QueryDelayMessage(self, QueryDelayMessage):
        self._QueryDelayMessage = QueryDelayMessage


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._MsgId = params.get("MsgId")
        self._QueryDeadLetterMessage = params.get("QueryDeadLetterMessage")
        self._QueryDelayMessage = params.get("QueryDelayMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageTraceResponse(AbstractModel):
    r"""DescribeMessageTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ShowTopicName: 主题名称
        :type ShowTopicName: str
        :param _Data: 轨迹详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of MessageTraceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ShowTopicName = None
        self._Data = None
        self._RequestId = None

    @property
    def ShowTopicName(self):
        r"""主题名称
        :rtype: str
        """
        return self._ShowTopicName

    @ShowTopicName.setter
    def ShowTopicName(self, ShowTopicName):
        self._ShowTopicName = ShowTopicName

    @property
    def Data(self):
        r"""轨迹详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MessageTraceItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._ShowTopicName = params.get("ShowTopicName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MessageTraceItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigratingGroupStatsRequest(AbstractModel):
    r"""DescribeMigratingGroupStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。
        :type TaskId: str
        :param _GroupName: 消费组名称，可在[DescribeSourceClusterGroupList](https://cloud.tencent.com/document/api/1493/118006)接口返回的[SourceClusterGroupConfig](https://cloud.tencent.com/document/api/1493/96031#SourceClusterGroupConfig)或控制台中获取。

        :type GroupName: str
        :param _Namespace: 命名空间，仅迁移至4.x集群有效，可在[DescribeSourceClusterGroupList](https://cloud.tencent.com/document/api/1493/118006)接口返回的[SourceClusterGroupConfig](https://cloud.tencent.com/document/api/1493/96031#SourceClusterGroupConfig)或控制台中获取。
        :type Namespace: str
        """
        self._TaskId = None
        self._GroupName = None
        self._Namespace = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GroupName(self):
        r"""消费组名称，可在[DescribeSourceClusterGroupList](https://cloud.tencent.com/document/api/1493/118006)接口返回的[SourceClusterGroupConfig](https://cloud.tencent.com/document/api/1493/96031#SourceClusterGroupConfig)或控制台中获取。

        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Namespace(self):
        r"""命名空间，仅迁移至4.x集群有效，可在[DescribeSourceClusterGroupList](https://cloud.tencent.com/document/api/1493/118006)接口返回的[SourceClusterGroupConfig](https://cloud.tencent.com/document/api/1493/96031#SourceClusterGroupConfig)或控制台中获取。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._GroupName = params.get("GroupName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigratingGroupStatsResponse(AbstractModel):
    r"""DescribeMigratingGroupStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceConsumeLag: 源集群消费组堆积
        :type SourceConsumeLag: int
        :param _TargetConsumeLag: 目标集群消费组堆积
        :type TargetConsumeLag: int
        :param _SourceConsumerClients: 源集群连接客户端列表
        :type SourceConsumerClients: list of ConsumerClient
        :param _TargetConsumerClients: 目标集群连接客户端列表
        :type TargetConsumerClients: list of ConsumerClient
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SourceConsumeLag = None
        self._TargetConsumeLag = None
        self._SourceConsumerClients = None
        self._TargetConsumerClients = None
        self._RequestId = None

    @property
    def SourceConsumeLag(self):
        r"""源集群消费组堆积
        :rtype: int
        """
        return self._SourceConsumeLag

    @SourceConsumeLag.setter
    def SourceConsumeLag(self, SourceConsumeLag):
        self._SourceConsumeLag = SourceConsumeLag

    @property
    def TargetConsumeLag(self):
        r"""目标集群消费组堆积
        :rtype: int
        """
        return self._TargetConsumeLag

    @TargetConsumeLag.setter
    def TargetConsumeLag(self, TargetConsumeLag):
        self._TargetConsumeLag = TargetConsumeLag

    @property
    def SourceConsumerClients(self):
        r"""源集群连接客户端列表
        :rtype: list of ConsumerClient
        """
        return self._SourceConsumerClients

    @SourceConsumerClients.setter
    def SourceConsumerClients(self, SourceConsumerClients):
        self._SourceConsumerClients = SourceConsumerClients

    @property
    def TargetConsumerClients(self):
        r"""目标集群连接客户端列表
        :rtype: list of ConsumerClient
        """
        return self._TargetConsumerClients

    @TargetConsumerClients.setter
    def TargetConsumerClients(self, TargetConsumerClients):
        self._TargetConsumerClients = TargetConsumerClients

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
        self._SourceConsumeLag = params.get("SourceConsumeLag")
        self._TargetConsumeLag = params.get("TargetConsumeLag")
        if params.get("SourceConsumerClients") is not None:
            self._SourceConsumerClients = []
            for item in params.get("SourceConsumerClients"):
                obj = ConsumerClient()
                obj._deserialize(item)
                self._SourceConsumerClients.append(obj)
        if params.get("TargetConsumerClients") is not None:
            self._TargetConsumerClients = []
            for item in params.get("TargetConsumerClients"):
                obj = ConsumerClient()
                obj._deserialize(item)
                self._TargetConsumerClients.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigratingTopicListRequest(AbstractModel):
    r"""DescribeMigratingTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
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
        


class DescribeMigratingTopicListResponse(AbstractModel):
    r"""DescribeMigratingTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _MigrateTopics: 主题列表
        :type MigrateTopics: list of MigratingTopic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MigrateTopics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MigrateTopics(self):
        r"""主题列表
        :rtype: list of MigratingTopic
        """
        return self._MigrateTopics

    @MigrateTopics.setter
    def MigrateTopics(self, MigrateTopics):
        self._MigrateTopics = MigrateTopics

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
        if params.get("MigrateTopics") is not None:
            self._MigrateTopics = []
            for item in params.get("MigrateTopics"):
                obj = MigratingTopic()
                obj._deserialize(item)
                self._MigrateTopics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMigratingTopicStatsRequest(AbstractModel):
    r"""DescribeMigratingTopicStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        :param _TopicName: 主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :type TopicName: str
        :param _Namespace: 命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :type Namespace: str
        """
        self._TaskId = None
        self._TopicName = None
        self._Namespace = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TopicName(self):
        r"""主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Namespace(self):
        r"""命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TopicName = params.get("TopicName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigratingTopicStatsResponse(AbstractModel):
    r"""DescribeMigratingTopicStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceClusterConsumerCount: 源集群的消费者数量
        :type SourceClusterConsumerCount: int
        :param _TargetClusterConsumerCount: 目标集群的消费者数量
        :type TargetClusterConsumerCount: int
        :param _SourceClusterConsumerGroups: 源集群消费组列表
        :type SourceClusterConsumerGroups: list of str
        :param _TargetClusterConsumerGroups: 目标集群消费组列表
        :type TargetClusterConsumerGroups: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SourceClusterConsumerCount = None
        self._TargetClusterConsumerCount = None
        self._SourceClusterConsumerGroups = None
        self._TargetClusterConsumerGroups = None
        self._RequestId = None

    @property
    def SourceClusterConsumerCount(self):
        r"""源集群的消费者数量
        :rtype: int
        """
        return self._SourceClusterConsumerCount

    @SourceClusterConsumerCount.setter
    def SourceClusterConsumerCount(self, SourceClusterConsumerCount):
        self._SourceClusterConsumerCount = SourceClusterConsumerCount

    @property
    def TargetClusterConsumerCount(self):
        r"""目标集群的消费者数量
        :rtype: int
        """
        return self._TargetClusterConsumerCount

    @TargetClusterConsumerCount.setter
    def TargetClusterConsumerCount(self, TargetClusterConsumerCount):
        self._TargetClusterConsumerCount = TargetClusterConsumerCount

    @property
    def SourceClusterConsumerGroups(self):
        r"""源集群消费组列表
        :rtype: list of str
        """
        return self._SourceClusterConsumerGroups

    @SourceClusterConsumerGroups.setter
    def SourceClusterConsumerGroups(self, SourceClusterConsumerGroups):
        self._SourceClusterConsumerGroups = SourceClusterConsumerGroups

    @property
    def TargetClusterConsumerGroups(self):
        r"""目标集群消费组列表
        :rtype: list of str
        """
        return self._TargetClusterConsumerGroups

    @TargetClusterConsumerGroups.setter
    def TargetClusterConsumerGroups(self, TargetClusterConsumerGroups):
        self._TargetClusterConsumerGroups = TargetClusterConsumerGroups

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
        self._SourceClusterConsumerCount = params.get("SourceClusterConsumerCount")
        self._TargetClusterConsumerCount = params.get("TargetClusterConsumerCount")
        self._SourceClusterConsumerGroups = params.get("SourceClusterConsumerGroups")
        self._TargetClusterConsumerGroups = params.get("TargetClusterConsumerGroups")
        self._RequestId = params.get("RequestId")


class DescribeMigrationTaskListRequest(AbstractModel):
    r"""DescribeMigrationTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        r"""查询条件列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationTaskListResponse(AbstractModel):
    r"""DescribeMigrationTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Tasks: 迁移任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of MigrationTaskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        r"""迁移任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MigrationTaskItem
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = MigrationTaskItem()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProducerListRequest(AbstractModel):
    r"""DescribeProducerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
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
        


class DescribeProducerListResponse(AbstractModel):
    r"""DescribeProducerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _ProducerList: 生产者信息列表
        :type ProducerList: list of ProducerInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProducerList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProducerList(self):
        r"""生产者信息列表
        :rtype: list of ProducerInfo
        """
        return self._ProducerList

    @ProducerList.setter
    def ProducerList(self, ProducerList):
        self._ProducerList = ProducerList

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
        if params.get("ProducerList") is not None:
            self._ProducerList = []
            for item in params.get("ProducerList"):
                obj = ProducerInfo()
                obj._deserialize(item)
                self._ProducerList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductSKUsRequest(AbstractModel):
    r"""DescribeProductSKUs请求参数结构体

    """


class DescribeProductSKUsResponse(AbstractModel):
    r"""DescribeProductSKUs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 商品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ProductSKU
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""商品配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProductSKU
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ProductSKU()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    r"""DescribeRoleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
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
        


class DescribeRoleListResponse(AbstractModel):
    r"""DescribeRoleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 角色信息列表
        :type Data: list of RoleItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""角色信息列表
        :rtype: list of RoleItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RoleItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSmoothMigrationTaskListRequest(AbstractModel):
    r"""DescribeSmoothMigrationTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeSmoothMigrationTaskListResponse(AbstractModel):
    r"""DescribeSmoothMigrationTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 任务列表	
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SmoothMigrationTaskItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""任务列表	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SmoothMigrationTaskItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SmoothMigrationTaskItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSourceClusterGroupListRequest(AbstractModel):
    r"""DescribeSourceClusterGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台上获得。

        :type TaskId: str
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台上获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
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
        


class DescribeSourceClusterGroupListResponse(AbstractModel):
    r"""DescribeSourceClusterGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Groups: 消费组配置列表
        :type Groups: list of SourceClusterGroupConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        r"""消费组配置列表
        :rtype: list of SourceClusterGroupConfig
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

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
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = SourceClusterGroupConfig()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicListByGroupRequest(AbstractModel):
    r"""DescribeTopicListByGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._ConsumerGroup = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ConsumerGroup = params.get("ConsumerGroup")
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
        


class DescribeTopicListByGroupResponse(AbstractModel):
    r"""DescribeTopicListByGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 主题列表
        :type Data: list of SubscriptionData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""主题列表
        :rtype: list of SubscriptionData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SubscriptionData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicListRequest(AbstractModel):
    r"""DescribeTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _TagFilters: 标签过滤器
        :type TagFilters: list of TagFilter
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        :param _FromGroup: 按照消费组查询订阅的主题
        :type FromGroup: str
        """
        self._InstanceId = None
        self._TagFilters = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._FromGroup = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TagFilters(self):
        r"""标签过滤器
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FromGroup(self):
        r"""按照消费组查询订阅的主题
        :rtype: str
        """
        return self._FromGroup

    @FromGroup.setter
    def FromGroup(self, FromGroup):
        self._FromGroup = FromGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FromGroup = params.get("FromGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicListResponse(AbstractModel):
    r"""DescribeTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 主题列表
        :type Data: list of TopicItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""主题列表
        :rtype: list of TopicItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopicItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    r"""DescribeTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _Filters: 过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认为0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20。
        :type Limit: int
        """
        self._InstanceId = None
        self._Topic = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Filters(self):
        r"""过滤查询条件列表，请在引用此参数的API说明中了解使用方法。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""查询起始位置，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询结果限制数量，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicResponse(AbstractModel):
    r"""DescribeTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _TopicType: 主题类型
UNSPECIFIED:未指定,
NORMAL:普通消息,
FIFO:顺序消息,
DELAY:延时消息,
TRANSACTION:事务消息
        :type TopicType: str
        :param _Remark: 备注
        :type Remark: str
        :param _CreatedTime: 创建时间，**Unix时间戳（毫秒）**
        :type CreatedTime: int
        :param _LastUpdateTime: 最后写入时间，**Unix时间戳（毫秒）**
        :type LastUpdateTime: int
        :param _SubscriptionCount: 订阅数量
        :type SubscriptionCount: int
        :param _SubscriptionData: 订阅关系列表
        :type SubscriptionData: list of SubscriptionData
        :param _MsgTTL: 消息保留时长，单位：小时
        :type MsgTTL: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._TopicType = None
        self._Remark = None
        self._CreatedTime = None
        self._LastUpdateTime = None
        self._SubscriptionCount = None
        self._SubscriptionData = None
        self._MsgTTL = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        r"""主题类型
UNSPECIFIED:未指定,
NORMAL:普通消息,
FIFO:顺序消息,
DELAY:延时消息,
TRANSACTION:事务消息
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        r"""创建时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def LastUpdateTime(self):
        r"""最后写入时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def SubscriptionCount(self):
        r"""订阅数量
        :rtype: int
        """
        return self._SubscriptionCount

    @SubscriptionCount.setter
    def SubscriptionCount(self, SubscriptionCount):
        self._SubscriptionCount = SubscriptionCount

    @property
    def SubscriptionData(self):
        r"""订阅关系列表
        :rtype: list of SubscriptionData
        """
        return self._SubscriptionData

    @SubscriptionData.setter
    def SubscriptionData(self, SubscriptionData):
        self._SubscriptionData = SubscriptionData

    @property
    def MsgTTL(self):
        r"""消息保留时长，单位：小时
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

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
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._TopicType = params.get("TopicType")
        self._Remark = params.get("Remark")
        self._CreatedTime = params.get("CreatedTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._SubscriptionCount = params.get("SubscriptionCount")
        if params.get("SubscriptionData") is not None:
            self._SubscriptionData = []
            for item in params.get("SubscriptionData"):
                obj = SubscriptionData()
                obj._deserialize(item)
                self._SubscriptionData.append(obj)
        self._MsgTTL = params.get("MsgTTL")
        self._RequestId = params.get("RequestId")


class DetailedRolePerm(AbstractModel):
    r"""Topic&Group维度的权限配置

    """

    def __init__(self):
        r"""
        :param _Resource: 权限对应的资源
可以是主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
可以是消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
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
        r"""权限对应的资源
可以是主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
可以是消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def PermWrite(self):
        r"""是否开启生产权限
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def PermRead(self):
        r"""是否开启消费权限
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def ResourceType(self):
        r"""授权资源类型（Topic:主题; Group:消费组）
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Remark(self):
        r"""资源备注
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
        


class DoHealthCheckOnMigratingTopicRequest(AbstractModel):
    r"""DoHealthCheckOnMigratingTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        :param _TopicName: 主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :type TopicName: str
        :param _IgnoreCheck: 是否忽略当前检查
        :type IgnoreCheck: bool
        :param _Namespace: 命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :type Namespace: str
        """
        self._TaskId = None
        self._TopicName = None
        self._IgnoreCheck = None
        self._Namespace = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TopicName(self):
        r"""主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def IgnoreCheck(self):
        r"""是否忽略当前检查
        :rtype: bool
        """
        return self._IgnoreCheck

    @IgnoreCheck.setter
    def IgnoreCheck(self, IgnoreCheck):
        self._IgnoreCheck = IgnoreCheck

    @property
    def Namespace(self):
        r"""命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TopicName = params.get("TopicName")
        self._IgnoreCheck = params.get("IgnoreCheck")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DoHealthCheckOnMigratingTopicResponse(AbstractModel):
    r"""DoHealthCheckOnMigratingTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Passed: 是否通过	
        :type Passed: bool
        :param _Reason: 健康检查返回的错误信息
NotChecked 未执行检查， 
Unknown 未知错误, 
TopicNotImported 主题未导入,
TopicNotExistsInSourceCluster 主题在源集群中不存在, 
TopicNotExistsInTargetCluster 主题在目标集群中不存在, 
ConsumerConnectedOnTarget 目标集群上存在消费者连接, 
SourceTopicHasNewMessagesIn5Minutes 源集群主题前5分钟内有新消息写入, 
TargetTopicHasNewMessagesIn5Minutes 目标集群主题前5分钟内有新消息写入, 
SourceTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, 
TargetTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, 
ConsumerGroupCountNotMatch 订阅组数量不一致, 
SourceTopicHasUnconsumedMessages 源集群主题存在未消费消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _ReasonList: 健康检查返回的错误信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReasonList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Passed = None
        self._Reason = None
        self._ReasonList = None
        self._RequestId = None

    @property
    def Passed(self):
        r"""是否通过	
        :rtype: bool
        """
        return self._Passed

    @Passed.setter
    def Passed(self, Passed):
        self._Passed = Passed

    @property
    def Reason(self):
        r"""健康检查返回的错误信息
NotChecked 未执行检查， 
Unknown 未知错误, 
TopicNotImported 主题未导入,
TopicNotExistsInSourceCluster 主题在源集群中不存在, 
TopicNotExistsInTargetCluster 主题在目标集群中不存在, 
ConsumerConnectedOnTarget 目标集群上存在消费者连接, 
SourceTopicHasNewMessagesIn5Minutes 源集群主题前5分钟内有新消息写入, 
TargetTopicHasNewMessagesIn5Minutes 目标集群主题前5分钟内有新消息写入, 
SourceTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, 
TargetTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, 
ConsumerGroupCountNotMatch 订阅组数量不一致, 
SourceTopicHasUnconsumedMessages 源集群主题存在未消费消息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ReasonList(self):
        r"""健康检查返回的错误信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ReasonList

    @ReasonList.setter
    def ReasonList(self, ReasonList):
        self._ReasonList = ReasonList

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
        self._Passed = params.get("Passed")
        self._Reason = params.get("Reason")
        self._ReasonList = params.get("ReasonList")
        self._RequestId = params.get("RequestId")


class Endpoint(AbstractModel):
    r"""接入点信息

    """

    def __init__(self):
        r"""
        :param _Type: 接入点类型，枚举值如下：

- VPC：VPC 网络

- PUBLIC：公网

- INTERNAL：支撑网
        :type Type: str
        :param _Status: 状态，
OPEN 开启，
CLOSE 关闭，
PROCESSING 操作中，
        :type Status: str
        :param _PayMode: 付费类型，仅公网
PREPAID 包年包月
POSTPAID 按量付费
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _EndpointUrl: 接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EndpointUrl: str
        :param _VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Bandwidth: 公网带宽，Mbps为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Bandwidth: int
        :param _IpRules: 公网放通规则
注意：此字段可能返回 null，表示取不到有效值。
        :type IpRules: list of IpRule
        :param _BillingFlow: 公网是否按流量计费
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingFlow: bool
        """
        self._Type = None
        self._Status = None
        self._PayMode = None
        self._EndpointUrl = None
        self._VpcId = None
        self._SubnetId = None
        self._Bandwidth = None
        self._IpRules = None
        self._BillingFlow = None

    @property
    def Type(self):
        r"""接入点类型，枚举值如下：

- VPC：VPC 网络

- PUBLIC：公网

- INTERNAL：支撑网
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""状态，
OPEN 开启，
CLOSE 关闭，
PROCESSING 操作中，
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PayMode(self):
        r"""付费类型，仅公网
PREPAID 包年包月
POSTPAID 按量付费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def EndpointUrl(self):
        r"""接入点地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndpointUrl

    @EndpointUrl.setter
    def EndpointUrl(self, EndpointUrl):
        self._EndpointUrl = EndpointUrl

    @property
    def VpcId(self):
        r"""VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Bandwidth(self):
        r"""公网带宽，Mbps为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        r"""公网放通规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IpRule
        """
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules

    @property
    def BillingFlow(self):
        r"""公网是否按流量计费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._BillingFlow

    @BillingFlow.setter
    def BillingFlow(self, BillingFlow):
        self._BillingFlow = BillingFlow


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._PayMode = params.get("PayMode")
        self._EndpointUrl = params.get("EndpointUrl")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("IpRules") is not None:
            self._IpRules = []
            for item in params.get("IpRules"):
                obj = IpRule()
                obj._deserialize(item)
                self._IpRules.append(obj)
        self._BillingFlow = params.get("BillingFlow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""查询过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤条件参数名
        :type Name: str
        :param _Values: 过滤条件的值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤条件参数名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤条件的值
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
        


class FusionInstanceItem(AbstractModel):
    r"""实例列表页中的实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Version: 实例版本
        :type Version: str
        :param _InstanceType: 实例类型，
EXPERIMENT，体验版
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :type InstanceType: str
        :param _InstanceStatus: 实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :type InstanceStatus: str
        :param _TopicNumLimit: 实例主题数上限
        :type TopicNumLimit: int
        :param _GroupNumLimit: 实例消费组数量上限
        :type GroupNumLimit: int
        :param _PayMode: 计费模式，枚举值如下：

- POSTPAID：按量计费

- PREPAID：包年包月
        :type PayMode: str
        :param _ExpiryTime: 到期时间，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiryTime: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _GroupNum: 消费组数量
        :type GroupNum: int
        :param _TagList: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        :param _SkuCode: 商品规格
        :type SkuCode: str
        :param _TpsLimit: TPS限流值
注意：此字段可能返回 null，表示取不到有效值。
        :type TpsLimit: int
        :param _ScaledTpsLimit: 弹性TPS限流值
        :type ScaledTpsLimit: int
        :param _MessageRetention: 消息保留时间，小时为单位
        :type MessageRetention: int
        :param _MaxMessageDelay: 延迟消息最大时长，小时为单位
        :type MaxMessageDelay: int
        :param _RenewFlag: 预付费集群是否自动续费，枚举值如下：

- 0: 不自动续费
- 1: 自动续费
        :type RenewFlag: int
        :param _InstanceItemExtraInfo: 4.x独有数据
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceItemExtraInfo: :class:`tencentcloud.trocket.v20230308.models.InstanceItemExtraInfo`
        :param _DestroyTime: 预销毁时间，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :type DestroyTime: int
        :param _ZoneIds: 所属可用区列表，参考 [DescribeZones](https://cloud.tencent.com/document/product/1596/77929) 接口返回中的 [ZoneInfo](https://cloud.tencent.com/document/api/1596/77932#ZoneInfo) 数据结构。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param _EnableDeletionProtection: 是否开启删除保护
        :type EnableDeletionProtection: bool
        :param _CreateTime: 实例创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _ScaledTpsEnabled: 弹性TPS开关
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaledTpsEnabled: bool
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._TopicNumLimit = None
        self._GroupNumLimit = None
        self._PayMode = None
        self._ExpiryTime = None
        self._Remark = None
        self._TopicNum = None
        self._GroupNum = None
        self._TagList = None
        self._SkuCode = None
        self._TpsLimit = None
        self._ScaledTpsLimit = None
        self._MessageRetention = None
        self._MaxMessageDelay = None
        self._RenewFlag = None
        self._InstanceItemExtraInfo = None
        self._DestroyTime = None
        self._ZoneIds = None
        self._EnableDeletionProtection = None
        self._CreateTime = None
        self._ScaledTpsEnabled = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        r"""实例版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def InstanceType(self):
        r"""实例类型，
EXPERIMENT，体验版
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        r"""实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TopicNumLimit(self):
        r"""实例主题数上限
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def GroupNumLimit(self):
        r"""实例消费组数量上限
        :rtype: int
        """
        return self._GroupNumLimit

    @GroupNumLimit.setter
    def GroupNumLimit(self, GroupNumLimit):
        self._GroupNumLimit = GroupNumLimit

    @property
    def PayMode(self):
        r"""计费模式，枚举值如下：

- POSTPAID：按量计费

- PREPAID：包年包月
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        r"""到期时间，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def Remark(self):
        r"""备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicNum(self):
        r"""主题数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def GroupNum(self):
        r"""消费组数量
        :rtype: int
        """
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def TagList(self):
        r"""标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SkuCode(self):
        r"""商品规格
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        r"""TPS限流值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ScaledTpsLimit(self):
        r"""弹性TPS限流值
        :rtype: int
        """
        return self._ScaledTpsLimit

    @ScaledTpsLimit.setter
    def ScaledTpsLimit(self, ScaledTpsLimit):
        self._ScaledTpsLimit = ScaledTpsLimit

    @property
    def MessageRetention(self):
        r"""消息保留时间，小时为单位
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def MaxMessageDelay(self):
        r"""延迟消息最大时长，小时为单位
        :rtype: int
        """
        return self._MaxMessageDelay

    @MaxMessageDelay.setter
    def MaxMessageDelay(self, MaxMessageDelay):
        self._MaxMessageDelay = MaxMessageDelay

    @property
    def RenewFlag(self):
        r"""预付费集群是否自动续费，枚举值如下：

- 0: 不自动续费
- 1: 自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def InstanceItemExtraInfo(self):
        r"""4.x独有数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trocket.v20230308.models.InstanceItemExtraInfo`
        """
        return self._InstanceItemExtraInfo

    @InstanceItemExtraInfo.setter
    def InstanceItemExtraInfo(self, InstanceItemExtraInfo):
        self._InstanceItemExtraInfo = InstanceItemExtraInfo

    @property
    def DestroyTime(self):
        r"""预销毁时间，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def ZoneIds(self):
        r"""所属可用区列表，参考 [DescribeZones](https://cloud.tencent.com/document/product/1596/77929) 接口返回中的 [ZoneInfo](https://cloud.tencent.com/document/api/1596/77932#ZoneInfo) 数据结构。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def EnableDeletionProtection(self):
        r"""是否开启删除保护
        :rtype: bool
        """
        return self._EnableDeletionProtection

    @EnableDeletionProtection.setter
    def EnableDeletionProtection(self, EnableDeletionProtection):
        self._EnableDeletionProtection = EnableDeletionProtection

    @property
    def CreateTime(self):
        r"""实例创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ScaledTpsEnabled(self):
        r"""弹性TPS开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ScaledTpsEnabled

    @ScaledTpsEnabled.setter
    def ScaledTpsEnabled(self, ScaledTpsEnabled):
        self._ScaledTpsEnabled = ScaledTpsEnabled


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._GroupNumLimit = params.get("GroupNumLimit")
        self._PayMode = params.get("PayMode")
        self._ExpiryTime = params.get("ExpiryTime")
        self._Remark = params.get("Remark")
        self._TopicNum = params.get("TopicNum")
        self._GroupNum = params.get("GroupNum")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._SkuCode = params.get("SkuCode")
        self._TpsLimit = params.get("TpsLimit")
        self._ScaledTpsLimit = params.get("ScaledTpsLimit")
        self._MessageRetention = params.get("MessageRetention")
        self._MaxMessageDelay = params.get("MaxMessageDelay")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("InstanceItemExtraInfo") is not None:
            self._InstanceItemExtraInfo = InstanceItemExtraInfo()
            self._InstanceItemExtraInfo._deserialize(params.get("InstanceItemExtraInfo"))
        self._DestroyTime = params.get("DestroyTime")
        self._ZoneIds = params.get("ZoneIds")
        self._EnableDeletionProtection = params.get("EnableDeletionProtection")
        self._CreateTime = params.get("CreateTime")
        self._ScaledTpsEnabled = params.get("ScaledTpsEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSourceClusterConsumerGroupsRequest(AbstractModel):
    r"""ImportSourceClusterConsumerGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        :param _GroupList: 待导入的消费组列表
        :type GroupList: list of SourceClusterGroupConfig
        """
        self._TaskId = None
        self._GroupList = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GroupList(self):
        r"""待导入的消费组列表
        :rtype: list of SourceClusterGroupConfig
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = SourceClusterGroupConfig()
                obj._deserialize(item)
                self._GroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSourceClusterConsumerGroupsResponse(AbstractModel):
    r"""ImportSourceClusterConsumerGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ImportSourceClusterTopicsRequest(AbstractModel):
    r"""ImportSourceClusterTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        :param _TopicList: 待导入的主题列表
        :type TopicList: list of SourceClusterTopicConfig
        """
        self._TaskId = None
        self._TopicList = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TopicList(self):
        r"""待导入的主题列表
        :rtype: list of SourceClusterTopicConfig
        """
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = SourceClusterTopicConfig()
                obj._deserialize(item)
                self._TopicList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportSourceClusterTopicsResponse(AbstractModel):
    r"""ImportSourceClusterTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class InstanceItem(AbstractModel):
    r"""实例列表页中的实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Version: 实例版本
        :type Version: str
        :param _InstanceType: 实例类型，
EXPERIMENT，体验版
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :type InstanceType: str
        :param _InstanceStatus: 实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :type InstanceStatus: str
        :param _TopicNumLimit: 实例主题数上限
        :type TopicNumLimit: int
        :param _GroupNumLimit: 实例消费组数量上限
        :type GroupNumLimit: int
        :param _PayMode: 计费模式，枚举值如下：

- POSTPAID：按量计费

- PREPAID：包年包月
        :type PayMode: str
        :param _ExpiryTime: 到期时间戳，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiryTime: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _GroupNum: 消费组数量
        :type GroupNum: int
        :param _TagList: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of Tag
        :param _SkuCode: 商品规格
        :type SkuCode: str
        :param _TpsLimit: TPS限流值
        :type TpsLimit: int
        :param _ScaledTpsLimit: 弹性TPS限流值
        :type ScaledTpsLimit: int
        :param _MessageRetention: 消息保留时间，小时为单位
        :type MessageRetention: int
        :param _MaxMessageDelay: 延迟消息最大时长，小时为单位
        :type MaxMessageDelay: int
        :param _RenewFlag: 是否自动续费，仅针对预付费集群（0: 不自动续费；1:自动续费）
        :type RenewFlag: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._TopicNumLimit = None
        self._GroupNumLimit = None
        self._PayMode = None
        self._ExpiryTime = None
        self._Remark = None
        self._TopicNum = None
        self._GroupNum = None
        self._TagList = None
        self._SkuCode = None
        self._TpsLimit = None
        self._ScaledTpsLimit = None
        self._MessageRetention = None
        self._MaxMessageDelay = None
        self._RenewFlag = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        r"""实例版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def InstanceType(self):
        r"""实例类型，
EXPERIMENT，体验版
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        r"""实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TopicNumLimit(self):
        r"""实例主题数上限
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def GroupNumLimit(self):
        r"""实例消费组数量上限
        :rtype: int
        """
        return self._GroupNumLimit

    @GroupNumLimit.setter
    def GroupNumLimit(self, GroupNumLimit):
        self._GroupNumLimit = GroupNumLimit

    @property
    def PayMode(self):
        r"""计费模式，枚举值如下：

- POSTPAID：按量计费

- PREPAID：包年包月
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        r"""到期时间戳，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def Remark(self):
        r"""备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicNum(self):
        r"""主题数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def GroupNum(self):
        r"""消费组数量
        :rtype: int
        """
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def TagList(self):
        r"""标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SkuCode(self):
        r"""商品规格
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        r"""TPS限流值
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ScaledTpsLimit(self):
        r"""弹性TPS限流值
        :rtype: int
        """
        return self._ScaledTpsLimit

    @ScaledTpsLimit.setter
    def ScaledTpsLimit(self, ScaledTpsLimit):
        self._ScaledTpsLimit = ScaledTpsLimit

    @property
    def MessageRetention(self):
        r"""消息保留时间，小时为单位
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def MaxMessageDelay(self):
        r"""延迟消息最大时长，小时为单位
        :rtype: int
        """
        return self._MaxMessageDelay

    @MaxMessageDelay.setter
    def MaxMessageDelay(self, MaxMessageDelay):
        self._MaxMessageDelay = MaxMessageDelay

    @property
    def RenewFlag(self):
        r"""是否自动续费，仅针对预付费集群（0: 不自动续费；1:自动续费）
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._GroupNumLimit = params.get("GroupNumLimit")
        self._PayMode = params.get("PayMode")
        self._ExpiryTime = params.get("ExpiryTime")
        self._Remark = params.get("Remark")
        self._TopicNum = params.get("TopicNum")
        self._GroupNum = params.get("GroupNum")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        self._SkuCode = params.get("SkuCode")
        self._TpsLimit = params.get("TpsLimit")
        self._ScaledTpsLimit = params.get("ScaledTpsLimit")
        self._MessageRetention = params.get("MessageRetention")
        self._MaxMessageDelay = params.get("MaxMessageDelay")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceItemExtraInfo(AbstractModel):
    r"""4.x集群和5.0集群列表统一显示 4.x特殊数据承载接口

    """

    def __init__(self):
        r"""
        :param _IsVip: 是否vip
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param _VipInstanceStatus: 4.x专享集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type VipInstanceStatus: int
        :param _MaxBandWidth: 专享集群峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxBandWidth: int
        :param _SpecName: 专享集群规格
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param _NodeCount: 专享集群节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeCount: int
        :param _MaxStorage: 专享集群最大存储
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStorage: int
        :param _MaxRetention: 专享集群最大保留时间，单位：小时
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetention: int
        :param _MinRetention: 专项集群最大保留时间，单位：小时
注意：此字段可能返回 null，表示取不到有效值。
        :type MinRetention: int
        :param _InstanceStatus: 4.0共享集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatus: int
        :param _IsFrozen: 是否已冻结
        :type IsFrozen: bool
        """
        self._IsVip = None
        self._VipInstanceStatus = None
        self._MaxBandWidth = None
        self._SpecName = None
        self._NodeCount = None
        self._MaxStorage = None
        self._MaxRetention = None
        self._MinRetention = None
        self._InstanceStatus = None
        self._IsFrozen = None

    @property
    def IsVip(self):
        r"""是否vip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def VipInstanceStatus(self):
        r"""4.x专享集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VipInstanceStatus

    @VipInstanceStatus.setter
    def VipInstanceStatus(self, VipInstanceStatus):
        self._VipInstanceStatus = VipInstanceStatus

    @property
    def MaxBandWidth(self):
        r"""专享集群峰值带宽
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def SpecName(self):
        r"""专享集群规格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def NodeCount(self):
        r"""专享集群节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def MaxStorage(self):
        r"""专享集群最大存储
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def MaxRetention(self):
        r"""专享集群最大保留时间，单位：小时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxRetention

    @MaxRetention.setter
    def MaxRetention(self, MaxRetention):
        self._MaxRetention = MaxRetention

    @property
    def MinRetention(self):
        r"""专项集群最大保留时间，单位：小时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinRetention

    @MinRetention.setter
    def MinRetention(self, MinRetention):
        self._MinRetention = MinRetention

    @property
    def InstanceStatus(self):
        r"""4.0共享集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def IsFrozen(self):
        r"""是否已冻结
        :rtype: bool
        """
        return self._IsFrozen

    @IsFrozen.setter
    def IsFrozen(self, IsFrozen):
        self._IsFrozen = IsFrozen


    def _deserialize(self, params):
        self._IsVip = params.get("IsVip")
        self._VipInstanceStatus = params.get("VipInstanceStatus")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._SpecName = params.get("SpecName")
        self._NodeCount = params.get("NodeCount")
        self._MaxStorage = params.get("MaxStorage")
        self._MaxRetention = params.get("MaxRetention")
        self._MinRetention = params.get("MinRetention")
        self._InstanceStatus = params.get("InstanceStatus")
        self._IsFrozen = params.get("IsFrozen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpRule(AbstractModel):
    r"""IP规则

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _Allow: 是否允许放行，默认为false表示拒绝
        :type Allow: bool
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._Ip = None
        self._Allow = None
        self._Remark = None

    @property
    def Ip(self):
        r"""IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Allow(self):
        r"""是否允许放行，默认为false表示拒绝
        :rtype: bool
        """
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Allow = params.get("Allow")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTClientSubscription(AbstractModel):
    r"""MQTT 订阅关系

    """

    def __init__(self):
        r"""
        :param _TopicFilter: topic 订阅
        :type TopicFilter: str
        :param _Qos: 服务质量等级
        :type Qos: int
        """
        self._TopicFilter = None
        self._Qos = None

    @property
    def TopicFilter(self):
        r"""topic 订阅
        :rtype: str
        """
        return self._TopicFilter

    @TopicFilter.setter
    def TopicFilter(self, TopicFilter):
        self._TopicFilter = TopicFilter

    @property
    def Qos(self):
        r"""服务质量等级
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos


    def _deserialize(self, params):
        self._TopicFilter = params.get("TopicFilter")
        self._Qos = params.get("Qos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTEndpointItem(AbstractModel):
    r"""MQTTEndpoint

    """

    def __init__(self):
        r"""
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Url: 接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _VpcId: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Host: 主机
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Ip: 接入点ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        """
        self._Type = None
        self._Url = None
        self._VpcId = None
        self._SubnetId = None
        self._Host = None
        self._Port = None
        self._Ip = None

    @property
    def Type(self):
        r"""类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""接入点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def VpcId(self):
        r"""vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Host(self):
        r"""主机
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Ip(self):
        r"""接入点ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTInstanceItem(AbstractModel):
    r"""MQTT 实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Version: 实例版本
        :type Version: str
        :param _InstanceType: 实例类型，
BASIC，基础版
PRO，专业版
        :type InstanceType: str
        :param _InstanceStatus: 实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :type InstanceStatus: str
        :param _TopicNumLimit: 实例主题数上限
        :type TopicNumLimit: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _SkuCode: 商品规格
        :type SkuCode: str
        :param _TpsLimit: 弹性TPS限流值
注意：此字段可能返回 null，表示取不到有效值。
        :type TpsLimit: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _SubscriptionNumLimit: 订阅关系上限
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionNumLimit: int
        :param _ClientNumLimit: 客户端连接数上线
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientNumLimit: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._TopicNumLimit = None
        self._Remark = None
        self._TopicNum = None
        self._SkuCode = None
        self._TpsLimit = None
        self._CreateTime = None
        self._SubscriptionNumLimit = None
        self._ClientNumLimit = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        r"""实例版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def InstanceType(self):
        r"""实例类型，
BASIC，基础版
PRO，专业版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        r"""实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TopicNumLimit(self):
        r"""实例主题数上限
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def Remark(self):
        r"""备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicNum(self):
        r"""主题数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def SkuCode(self):
        r"""商品规格
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        r"""弹性TPS限流值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SubscriptionNumLimit(self):
        r"""订阅关系上限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SubscriptionNumLimit

    @SubscriptionNumLimit.setter
    def SubscriptionNumLimit(self, SubscriptionNumLimit):
        self._SubscriptionNumLimit = SubscriptionNumLimit

    @property
    def ClientNumLimit(self):
        r"""客户端连接数上线
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._Remark = params.get("Remark")
        self._TopicNum = params.get("TopicNum")
        self._SkuCode = params.get("SkuCode")
        self._TpsLimit = params.get("TpsLimit")
        self._CreateTime = params.get("CreateTime")
        self._SubscriptionNumLimit = params.get("SubscriptionNumLimit")
        self._ClientNumLimit = params.get("ClientNumLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTMessageItem(AbstractModel):
    r"""消息记录

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgId: str
        :param _Tags: 消息tag
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: str
        :param _Keys: 消息key
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: str
        :param _ProducerAddr: 客户端地址	
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerAddr: str
        :param _ProduceTime: 消息发送时间	
注意：此字段可能返回 null，表示取不到有效值。
        :type ProduceTime: str
        :param _DeadLetterResendTimes: 死信重发次数	
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterResendTimes: int
        :param _DeadLetterResendSuccessTimes: 死信重发成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterResendSuccessTimes: int
        :param _SubTopic: 子topic
注意：此字段可能返回 null，表示取不到有效值。
        :type SubTopic: str
        :param _Qos: 消息质量等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Qos: str
        """
        self._MsgId = None
        self._Tags = None
        self._Keys = None
        self._ProducerAddr = None
        self._ProduceTime = None
        self._DeadLetterResendTimes = None
        self._DeadLetterResendSuccessTimes = None
        self._SubTopic = None
        self._Qos = None

    @property
    def MsgId(self):
        r"""消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def Tags(self):
        r"""消息tag
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Keys(self):
        r"""消息key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def ProducerAddr(self):
        r"""客户端地址	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def ProduceTime(self):
        r"""消息发送时间	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def DeadLetterResendTimes(self):
        r"""死信重发次数	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeadLetterResendTimes

    @DeadLetterResendTimes.setter
    def DeadLetterResendTimes(self, DeadLetterResendTimes):
        self._DeadLetterResendTimes = DeadLetterResendTimes

    @property
    def DeadLetterResendSuccessTimes(self):
        r"""死信重发成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeadLetterResendSuccessTimes

    @DeadLetterResendSuccessTimes.setter
    def DeadLetterResendSuccessTimes(self, DeadLetterResendSuccessTimes):
        self._DeadLetterResendSuccessTimes = DeadLetterResendSuccessTimes

    @property
    def SubTopic(self):
        r"""子topic
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubTopic

    @SubTopic.setter
    def SubTopic(self, SubTopic):
        self._SubTopic = SubTopic

    @property
    def Qos(self):
        r"""消息质量等级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._Tags = params.get("Tags")
        self._Keys = params.get("Keys")
        self._ProducerAddr = params.get("ProducerAddr")
        self._ProduceTime = params.get("ProduceTime")
        self._DeadLetterResendTimes = params.get("DeadLetterResendTimes")
        self._DeadLetterResendSuccessTimes = params.get("DeadLetterResendSuccessTimes")
        self._SubTopic = params.get("SubTopic")
        self._Qos = params.get("Qos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTProductSkuItem(AbstractModel):
    r"""MQTT ProductSkuItem

    """

    def __init__(self):
        r"""
        :param _InstanceType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _SkuCode: cide
注意：此字段可能返回 null，表示取不到有效值。
        :type SkuCode: str
        :param _OnSale: sale
注意：此字段可能返回 null，表示取不到有效值。
        :type OnSale: bool
        :param _TopicNumLimit: topic num限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNumLimit: int
        :param _TpsLimit: tps
注意：此字段可能返回 null，表示取不到有效值。
        :type TpsLimit: int
        :param _ClientNumLimit: 客户端连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientNumLimit: int
        :param _SubscriptionNumLimit: 订阅数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionNumLimit: int
        :param _ProxySpecCore: 代理核
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxySpecCore: int
        :param _ProxySpecMemory: 代理内存
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxySpecMemory: int
        :param _ProxySpecCount: 代理总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxySpecCount: int
        """
        self._InstanceType = None
        self._SkuCode = None
        self._OnSale = None
        self._TopicNumLimit = None
        self._TpsLimit = None
        self._ClientNumLimit = None
        self._SubscriptionNumLimit = None
        self._ProxySpecCore = None
        self._ProxySpecMemory = None
        self._ProxySpecCount = None

    @property
    def InstanceType(self):
        r"""类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SkuCode(self):
        r"""cide
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def OnSale(self):
        r"""sale
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._OnSale

    @OnSale.setter
    def OnSale(self, OnSale):
        self._OnSale = OnSale

    @property
    def TopicNumLimit(self):
        r"""topic num限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def TpsLimit(self):
        r"""tps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ClientNumLimit(self):
        r"""客户端连接数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def SubscriptionNumLimit(self):
        r"""订阅数限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SubscriptionNumLimit

    @SubscriptionNumLimit.setter
    def SubscriptionNumLimit(self, SubscriptionNumLimit):
        self._SubscriptionNumLimit = SubscriptionNumLimit

    @property
    def ProxySpecCore(self):
        r"""代理核
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProxySpecCore

    @ProxySpecCore.setter
    def ProxySpecCore(self, ProxySpecCore):
        self._ProxySpecCore = ProxySpecCore

    @property
    def ProxySpecMemory(self):
        r"""代理内存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProxySpecMemory

    @ProxySpecMemory.setter
    def ProxySpecMemory(self, ProxySpecMemory):
        self._ProxySpecMemory = ProxySpecMemory

    @property
    def ProxySpecCount(self):
        r"""代理总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProxySpecCount

    @ProxySpecCount.setter
    def ProxySpecCount(self, ProxySpecCount):
        self._ProxySpecCount = ProxySpecCount


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._SkuCode = params.get("SkuCode")
        self._OnSale = params.get("OnSale")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._TpsLimit = params.get("TpsLimit")
        self._ClientNumLimit = params.get("ClientNumLimit")
        self._SubscriptionNumLimit = params.get("SubscriptionNumLimit")
        self._ProxySpecCore = params.get("ProxySpecCore")
        self._ProxySpecMemory = params.get("ProxySpecMemory")
        self._ProxySpecCount = params.get("ProxySpecCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTTopicItem(AbstractModel):
    r"""MQTT 主题详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Remark: 主题描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        r"""主题描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTUserItem(AbstractModel):
    r"""MQTT集群用户信息

    """

    def __init__(self):
        r"""
        :param _Username: 用户名
        :type Username: str
        :param _Password: 密码
        :type Password: str
        :param _PermRead: 是否开启消费
        :type PermRead: bool
        :param _PermWrite: 是否开启生产
        :type PermWrite: bool
        :param _Remark: 备注信息
        :type Remark: str
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _ModifiedTime: 修改时间，秒为单位
        :type ModifiedTime: int
        """
        self._Username = None
        self._Password = None
        self._PermRead = None
        self._PermWrite = None
        self._Remark = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def Username(self):
        r"""用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def PermRead(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def PermWrite(self):
        r"""是否开启生产
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        r"""创建时间，秒为单位
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""修改时间，秒为单位
        :rtype: int
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._PermRead = params.get("PermRead")
        self._PermWrite = params.get("PermWrite")
        self._Remark = params.get("Remark")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageItem(AbstractModel):
    r"""消息记录

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MsgId: str
        :param _Tags: 消息tag
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: str
        :param _Keys: 消息key
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: str
        :param _ProducerAddr: 客户端地址	
注意：此字段可能返回 null，表示取不到有效值。
        :type ProducerAddr: str
        :param _ProduceTime: 消息发送时间	
注意：此字段可能返回 null，表示取不到有效值。
        :type ProduceTime: str
        :param _DeadLetterResendTimes: 死信重发次数	
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterResendTimes: int
        :param _DeadLetterResendSuccessTimes: 死信重发成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterResendSuccessTimes: int
        """
        self._MsgId = None
        self._Tags = None
        self._Keys = None
        self._ProducerAddr = None
        self._ProduceTime = None
        self._DeadLetterResendTimes = None
        self._DeadLetterResendSuccessTimes = None

    @property
    def MsgId(self):
        r"""消息ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def Tags(self):
        r"""消息tag
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Keys(self):
        r"""消息key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def ProducerAddr(self):
        r"""客户端地址	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def ProduceTime(self):
        r"""消息发送时间	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def DeadLetterResendTimes(self):
        r"""死信重发次数	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeadLetterResendTimes

    @DeadLetterResendTimes.setter
    def DeadLetterResendTimes(self, DeadLetterResendTimes):
        self._DeadLetterResendTimes = DeadLetterResendTimes

    @property
    def DeadLetterResendSuccessTimes(self):
        r"""死信重发成功次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeadLetterResendSuccessTimes

    @DeadLetterResendSuccessTimes.setter
    def DeadLetterResendSuccessTimes(self, DeadLetterResendSuccessTimes):
        self._DeadLetterResendSuccessTimes = DeadLetterResendSuccessTimes


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._Tags = params.get("Tags")
        self._Keys = params.get("Keys")
        self._ProducerAddr = params.get("ProducerAddr")
        self._ProduceTime = params.get("ProduceTime")
        self._DeadLetterResendTimes = params.get("DeadLetterResendTimes")
        self._DeadLetterResendSuccessTimes = params.get("DeadLetterResendSuccessTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageTraceItem(AbstractModel):
    r"""消息轨迹

    """

    def __init__(self):
        r"""
        :param _Stage: 消息处理阶段，枚举值如下：

- produce：消息生产

- persist：消息存储

- consume：消息消费
注意：此字段可能返回 null，表示取不到有效值。
        :type Stage: str
        :param _Data: 轨迹详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self._Stage = None
        self._Data = None

    @property
    def Stage(self):
        r"""消息处理阶段，枚举值如下：

- produce：消息生产

- persist：消息存储

- consume：消息消费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def Data(self):
        r"""轨迹详情
注意：此字段可能返回 null，表示取不到有效值。
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
        


class MessageTrackItem(AbstractModel):
    r"""MessageTrack

    """

    def __init__(self):
        r"""
        :param _ConsumerGroup: 消费组名称
        :type ConsumerGroup: str
        :param _ConsumeStatus: 消费状态, CONSUMED: 已消费 CONSUMED_BUT_FILTERED: 已过滤 NOT_CONSUME: 未消费 ENTER_RETRY: 进入重试队列 ENTER_DLQ: 进入死信队列 UNKNOWN: 查询不到消费状态
        :type ConsumeStatus: str
        :param _TrackType: track类型
        :type TrackType: str
        :param _ExceptionDesc: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptionDesc: str
        """
        self._ConsumerGroup = None
        self._ConsumeStatus = None
        self._TrackType = None
        self._ExceptionDesc = None

    @property
    def ConsumerGroup(self):
        r"""消费组名称
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def ConsumeStatus(self):
        r"""消费状态, CONSUMED: 已消费 CONSUMED_BUT_FILTERED: 已过滤 NOT_CONSUME: 未消费 ENTER_RETRY: 进入重试队列 ENTER_DLQ: 进入死信队列 UNKNOWN: 查询不到消费状态
        :rtype: str
        """
        return self._ConsumeStatus

    @ConsumeStatus.setter
    def ConsumeStatus(self, ConsumeStatus):
        self._ConsumeStatus = ConsumeStatus

    @property
    def TrackType(self):
        r"""track类型
        :rtype: str
        """
        return self._TrackType

    @TrackType.setter
    def TrackType(self, TrackType):
        self._TrackType = TrackType

    @property
    def ExceptionDesc(self):
        r"""异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExceptionDesc

    @ExceptionDesc.setter
    def ExceptionDesc(self, ExceptionDesc):
        self._ExceptionDesc = ExceptionDesc


    def _deserialize(self, params):
        self._ConsumerGroup = params.get("ConsumerGroup")
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
        


class MigratingTopic(AbstractModel):
    r"""迁移中的主题

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _MigrationStatus: 迁移状态 
S_RW_D_NA 源集群读写，
S_RW_D_R 源集群读写目标集群读，
S_RW_D_RW 源集群读写目标集群读写，
S_R_D_RW 源集群读目标集群读写，
S_NA_D_RW 目标集群读写
        :type MigrationStatus: str
        :param _HealthCheckPassed: 是否完成健康检查	
        :type HealthCheckPassed: bool
        :param _HealthCheckError: 上次健康检查返回的错误信息，仅在HealthCheckPassed为false时有效。 NotChecked 未执行检查， Unknown 未知错误, TopicNotImported 主题未导入, TopicNotExistsInSourceCluster 主题在源集群中不存在, TopicNotExistsInTargetCluster 主题在目标集群中不存在, ConsumerConnectedOnTarget 目标集群上存在消费者连接, SourceTopicHasNewMessagesIn5Minutes 源集群主题前5分钟内有新消息写入, TargetTopicHasNewMessagesIn5Minutes 目标集群主题前5分钟内有新消息写入, SourceTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, TargetTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, ConsumerGroupCountNotMatch 订阅组数量不一致, SourceTopicHasUnconsumedMessages 源集群主题存在未消费消息,
        :type HealthCheckError: str
        :param _Namespace: 命名空间，仅4.x集群有效
        :type Namespace: str
        :param _NamespaceV4: 4.x的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceV4: str
        :param _TopicNameV4: 4.x的主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNameV4: str
        :param _FullNamespaceV4: 4.x的完整命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type FullNamespaceV4: str
        :param _HealthCheckErrorList: 上次健康检查返回的错误列表
        :type HealthCheckErrorList: list of str
        """
        self._TopicName = None
        self._MigrationStatus = None
        self._HealthCheckPassed = None
        self._HealthCheckError = None
        self._Namespace = None
        self._NamespaceV4 = None
        self._TopicNameV4 = None
        self._FullNamespaceV4 = None
        self._HealthCheckErrorList = None

    @property
    def TopicName(self):
        r"""主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MigrationStatus(self):
        r"""迁移状态 
S_RW_D_NA 源集群读写，
S_RW_D_R 源集群读写目标集群读，
S_RW_D_RW 源集群读写目标集群读写，
S_R_D_RW 源集群读目标集群读写，
S_NA_D_RW 目标集群读写
        :rtype: str
        """
        return self._MigrationStatus

    @MigrationStatus.setter
    def MigrationStatus(self, MigrationStatus):
        self._MigrationStatus = MigrationStatus

    @property
    def HealthCheckPassed(self):
        r"""是否完成健康检查	
        :rtype: bool
        """
        return self._HealthCheckPassed

    @HealthCheckPassed.setter
    def HealthCheckPassed(self, HealthCheckPassed):
        self._HealthCheckPassed = HealthCheckPassed

    @property
    def HealthCheckError(self):
        r"""上次健康检查返回的错误信息，仅在HealthCheckPassed为false时有效。 NotChecked 未执行检查， Unknown 未知错误, TopicNotImported 主题未导入, TopicNotExistsInSourceCluster 主题在源集群中不存在, TopicNotExistsInTargetCluster 主题在目标集群中不存在, ConsumerConnectedOnTarget 目标集群上存在消费者连接, SourceTopicHasNewMessagesIn5Minutes 源集群主题前5分钟内有新消息写入, TargetTopicHasNewMessagesIn5Minutes 目标集群主题前5分钟内有新消息写入, SourceTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, TargetTopicHasNoMessagesIn5Minutes 源集群前5分钟内没有新消息写入, ConsumerGroupCountNotMatch 订阅组数量不一致, SourceTopicHasUnconsumedMessages 源集群主题存在未消费消息,
        :rtype: str
        """
        return self._HealthCheckError

    @HealthCheckError.setter
    def HealthCheckError(self, HealthCheckError):
        self._HealthCheckError = HealthCheckError

    @property
    def Namespace(self):
        r"""命名空间，仅4.x集群有效
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def NamespaceV4(self):
        r"""4.x的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NamespaceV4

    @NamespaceV4.setter
    def NamespaceV4(self, NamespaceV4):
        self._NamespaceV4 = NamespaceV4

    @property
    def TopicNameV4(self):
        r"""4.x的主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicNameV4

    @TopicNameV4.setter
    def TopicNameV4(self, TopicNameV4):
        self._TopicNameV4 = TopicNameV4

    @property
    def FullNamespaceV4(self):
        r"""4.x的完整命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FullNamespaceV4

    @FullNamespaceV4.setter
    def FullNamespaceV4(self, FullNamespaceV4):
        self._FullNamespaceV4 = FullNamespaceV4

    @property
    def HealthCheckErrorList(self):
        r"""上次健康检查返回的错误列表
        :rtype: list of str
        """
        return self._HealthCheckErrorList

    @HealthCheckErrorList.setter
    def HealthCheckErrorList(self, HealthCheckErrorList):
        self._HealthCheckErrorList = HealthCheckErrorList


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MigrationStatus = params.get("MigrationStatus")
        self._HealthCheckPassed = params.get("HealthCheckPassed")
        self._HealthCheckError = params.get("HealthCheckError")
        self._Namespace = params.get("Namespace")
        self._NamespaceV4 = params.get("NamespaceV4")
        self._TopicNameV4 = params.get("TopicNameV4")
        self._FullNamespaceV4 = params.get("FullNamespaceV4")
        self._HealthCheckErrorList = params.get("HealthCheckErrorList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrationTaskItem(AbstractModel):
    r"""迁移任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 0 - 未指定（存量）
1 - 元数据导入
        :type Type: int
        :param _TopicNum: 主题总数
        :type TopicNum: int
        :param _GroupNum: 消费组总数
        :type GroupNum: int
        :param _Status: 任务状态： 0，迁移中 1，迁移成功 2，迁移完成，只有部分数据完成迁移
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: int
        """
        self._TaskId = None
        self._InstanceId = None
        self._Type = None
        self._TopicNum = None
        self._GroupNum = None
        self._Status = None
        self._CreateTime = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        r"""0 - 未指定（存量）
1 - 元数据导入
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TopicNum(self):
        r"""主题总数
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def GroupNum(self):
        r"""消费组总数
        :rtype: int
        """
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def Status(self):
        r"""任务状态： 0，迁移中 1，迁移成功 2，迁移完成，只有部分数据完成迁移
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._TopicNum = params.get("TopicNum")
        self._GroupNum = params.get("GroupNum")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerGroupRequest(AbstractModel):
    r"""ModifyConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        :param _ConsumeEnable: 是否开启消费
        :type ConsumeEnable: bool
        :param _ConsumeMessageOrderly: 顺序投递：true
并发投递：false
        :type ConsumeMessageOrderly: bool
        :param _MaxRetryTimes: 最大重试次数，取值范围0～1000
        :type MaxRetryTimes: int
        :param _Remark: 备注信息，最多 128 个字符
        :type Remark: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._ConsumeEnable = None
        self._ConsumeMessageOrderly = None
        self._MaxRetryTimes = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def ConsumeEnable(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

    @property
    def ConsumeMessageOrderly(self):
        r"""顺序投递：true
并发投递：false
        :rtype: bool
        """
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def MaxRetryTimes(self):
        r"""最大重试次数，取值范围0～1000
        :rtype: int
        """
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def Remark(self):
        r"""备注信息，最多 128 个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._ConsumeEnable = params.get("ConsumeEnable")
        self._ConsumeMessageOrderly = params.get("ConsumeMessageOrderly")
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsumerGroupResponse(AbstractModel):
    r"""ModifyConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyInstanceEndpointRequest(AbstractModel):
    r"""ModifyInstanceEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Type: 接入点类型，
PUBLIC 公网
        :type Type: str
        :param _Bandwidth: 公网带宽，Mbps为单位
        :type Bandwidth: int
        :param _IpRules: 公网安全组信息
        :type IpRules: list of IpRule
        :param _BillingFlow: 公网是否按流量计费
        :type BillingFlow: bool
        """
        self._InstanceId = None
        self._Type = None
        self._Bandwidth = None
        self._IpRules = None
        self._BillingFlow = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        r"""接入点类型，
PUBLIC 公网
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Bandwidth(self):
        r"""公网带宽，Mbps为单位
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        r"""公网安全组信息
        :rtype: list of IpRule
        """
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules

    @property
    def BillingFlow(self):
        r"""公网是否按流量计费
        :rtype: bool
        """
        return self._BillingFlow

    @BillingFlow.setter
    def BillingFlow(self, BillingFlow):
        self._BillingFlow = BillingFlow


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("IpRules") is not None:
            self._IpRules = []
            for item in params.get("IpRules"):
                obj = IpRule()
                obj._deserialize(item)
                self._IpRules.append(obj)
        self._BillingFlow = params.get("BillingFlow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceEndpointResponse(AbstractModel):
    r"""ModifyInstanceEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    r"""ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Name: 实例名称，不能为空, 3-64个字符，只能包含数字、字母、“-”和“_”
        :type Name: str
        :param _Remark: 备注信息，最多 128 个字符
        :type Remark: str
        :param _SendReceiveRatio: 消息发送和接收的比例
        :type SendReceiveRatio: float
        :param _SkuCode: 商品规格，从 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参获得。
        :type SkuCode: str
        :param _MessageRetention: 消息保留时长（单位：小时），取值范围参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 默认值：DefaultRetention 参数
- 最小值：RetentionLowerLimit 参数
- 最大值：RetentionUpperLimit 参数
        :type MessageRetention: int
        :param _ScaledTpsEnabled: 是否开启弹性TPS
        :type ScaledTpsEnabled: bool
        :param _AclEnabled: 是否开启ACL
        :type AclEnabled: bool
        :param _MaxTopicNum: 最大可创建主题数，取值范围参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 最小值和默认值：TopicNumLimit 参数
- 最大值：TopicNumUpperLimit 参数
        :type MaxTopicNum: int
        :param _ExtraTopicNum: 免费额度之外的主题个数，免费额度参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参中的 TopicNumLimit 参数。
        :type ExtraTopicNum: str
        :param _EnableDeletionProtection: 是否开启删除保护
        :type EnableDeletionProtection: bool
        """
        self._InstanceId = None
        self._Name = None
        self._Remark = None
        self._SendReceiveRatio = None
        self._SkuCode = None
        self._MessageRetention = None
        self._ScaledTpsEnabled = None
        self._AclEnabled = None
        self._MaxTopicNum = None
        self._ExtraTopicNum = None
        self._EnableDeletionProtection = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""实例名称，不能为空, 3-64个字符，只能包含数字、字母、“-”和“_”
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""备注信息，最多 128 个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SendReceiveRatio(self):
        r"""消息发送和接收的比例
        :rtype: float
        """
        return self._SendReceiveRatio

    @SendReceiveRatio.setter
    def SendReceiveRatio(self, SendReceiveRatio):
        self._SendReceiveRatio = SendReceiveRatio

    @property
    def SkuCode(self):
        r"""商品规格，从 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参获得。
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def MessageRetention(self):
        r"""消息保留时长（单位：小时），取值范围参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 默认值：DefaultRetention 参数
- 最小值：RetentionLowerLimit 参数
- 最大值：RetentionUpperLimit 参数
        :rtype: int
        """
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def ScaledTpsEnabled(self):
        r"""是否开启弹性TPS
        :rtype: bool
        """
        return self._ScaledTpsEnabled

    @ScaledTpsEnabled.setter
    def ScaledTpsEnabled(self, ScaledTpsEnabled):
        self._ScaledTpsEnabled = ScaledTpsEnabled

    @property
    def AclEnabled(self):
        r"""是否开启ACL
        :rtype: bool
        """
        return self._AclEnabled

    @AclEnabled.setter
    def AclEnabled(self, AclEnabled):
        self._AclEnabled = AclEnabled

    @property
    def MaxTopicNum(self):
        r"""最大可创建主题数，取值范围参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参：

- 最小值和默认值：TopicNumLimit 参数
- 最大值：TopicNumUpperLimit 参数
        :rtype: int
        """
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def ExtraTopicNum(self):
        r"""免费额度之外的主题个数，免费额度参考 [DescribeProductSKUs](https://cloud.tencent.com/document/api/1493/107676) 接口中的 [ProductSKU](https://cloud.tencent.com/document/api/1493/96031#ProductSKU) 出参中的 TopicNumLimit 参数。
        :rtype: str
        """
        return self._ExtraTopicNum

    @ExtraTopicNum.setter
    def ExtraTopicNum(self, ExtraTopicNum):
        self._ExtraTopicNum = ExtraTopicNum

    @property
    def EnableDeletionProtection(self):
        r"""是否开启删除保护
        :rtype: bool
        """
        return self._EnableDeletionProtection

    @EnableDeletionProtection.setter
    def EnableDeletionProtection(self, EnableDeletionProtection):
        self._EnableDeletionProtection = EnableDeletionProtection


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._SendReceiveRatio = params.get("SendReceiveRatio")
        self._SkuCode = params.get("SkuCode")
        self._MessageRetention = params.get("MessageRetention")
        self._ScaledTpsEnabled = params.get("ScaledTpsEnabled")
        self._AclEnabled = params.get("AclEnabled")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._ExtraTopicNum = params.get("ExtraTopicNum")
        self._EnableDeletionProtection = params.get("EnableDeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    r"""ModifyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyMQTTInsPublicEndpointRequest(AbstractModel):
    r"""ModifyMQTTInsPublicEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Bandwidth: 带宽
        :type Bandwidth: int
        :param _Rules: 公网访问规则
        :type Rules: list of PublicAccessRule
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._Rules = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        r"""带宽
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Rules(self):
        r"""公网访问规则
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMQTTInsPublicEndpointResponse(AbstractModel):
    r"""ModifyMQTTInsPublicEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyMQTTInstanceCertBindingRequest(AbstractModel):
    r"""ModifyMQTTInstanceCertBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _SSLServerCertId: 服务端证书id
        :type SSLServerCertId: str
        :param _SSLCaCertId: CA证书id
        :type SSLCaCertId: str
        """
        self._InstanceId = None
        self._SSLServerCertId = None
        self._SSLCaCertId = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SSLServerCertId(self):
        r"""服务端证书id
        :rtype: str
        """
        return self._SSLServerCertId

    @SSLServerCertId.setter
    def SSLServerCertId(self, SSLServerCertId):
        self._SSLServerCertId = SSLServerCertId

    @property
    def SSLCaCertId(self):
        r"""CA证书id
        :rtype: str
        """
        return self._SSLCaCertId

    @SSLCaCertId.setter
    def SSLCaCertId(self, SSLCaCertId):
        self._SSLCaCertId = SSLCaCertId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SSLServerCertId = params.get("SSLServerCertId")
        self._SSLCaCertId = params.get("SSLCaCertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMQTTInstanceCertBindingResponse(AbstractModel):
    r"""ModifyMQTTInstanceCertBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyMQTTInstanceRequest(AbstractModel):
    r"""ModifyMQTTInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Name: 实例名称
        :type Name: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._InstanceId = None
        self._Name = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMQTTInstanceResponse(AbstractModel):
    r"""ModifyMQTTInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyMQTTTopicRequest(AbstractModel):
    r"""ModifyMQTTTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMQTTTopicResponse(AbstractModel):
    r"""ModifyMQTTTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyMQTTUserRequest(AbstractModel):
    r"""ModifyMQTTUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Username: 用户名
        :type Username: str
        :param _PermRead: 是否开启消费
        :type PermRead: bool
        :param _PermWrite: 是否开启生产
        :type PermWrite: bool
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._Username = None
        self._PermRead = None
        self._PermWrite = None
        self._Remark = None

    @property
    def InstanceId(self):
        r"""集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Username(self):
        r"""用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def PermRead(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def PermWrite(self):
        r"""是否开启生产
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Username = params.get("Username")
        self._PermRead = params.get("PermRead")
        self._PermWrite = params.get("PermWrite")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMQTTUserResponse(AbstractModel):
    r"""ModifyMQTTUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyRoleRequest(AbstractModel):
    r"""ModifyRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Role: 角色名称，从 [DescribeRoleList](https://cloud.tencent.com/document/api/1493/98862) 接口中返回的 [RoleItem](https://cloud.tencent.com/document/api/1493/96031#RoleItem) 或控制台获得。
        :type Role: str
        :param _PermRead: 是否开启消费
        :type PermRead: bool
        :param _PermWrite: 是否开启生产
        :type PermWrite: bool
        :param _PermType: 权限类型，默认按集群授权（Cluster：集群维度；TopicAndGroup：主题和消费组维度）
        :type PermType: str
        :param _Remark: 备注
        :type Remark: str
        :param _DetailedPerms: Topic&Group维度权限配置，权限类型为 TopicAndGroup 时必填
        :type DetailedPerms: list of DetailedRolePerm
        """
        self._InstanceId = None
        self._Role = None
        self._PermRead = None
        self._PermWrite = None
        self._PermType = None
        self._Remark = None
        self._DetailedPerms = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Role(self):
        r"""角色名称，从 [DescribeRoleList](https://cloud.tencent.com/document/api/1493/98862) 接口中返回的 [RoleItem](https://cloud.tencent.com/document/api/1493/96031#RoleItem) 或控制台获得。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def PermRead(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def PermWrite(self):
        r"""是否开启生产
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def PermType(self):
        r"""权限类型，默认按集群授权（Cluster：集群维度；TopicAndGroup：主题和消费组维度）
        :rtype: str
        """
        return self._PermType

    @PermType.setter
    def PermType(self, PermType):
        self._PermType = PermType

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DetailedPerms(self):
        r"""Topic&Group维度权限配置，权限类型为 TopicAndGroup 时必填
        :rtype: list of DetailedRolePerm
        """
        return self._DetailedPerms

    @DetailedPerms.setter
    def DetailedPerms(self, DetailedPerms):
        self._DetailedPerms = DetailedPerms


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Role = params.get("Role")
        self._PermRead = params.get("PermRead")
        self._PermWrite = params.get("PermWrite")
        self._PermType = params.get("PermType")
        self._Remark = params.get("Remark")
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
        


class ModifyRoleResponse(AbstractModel):
    r"""ModifyRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    r"""ModifyTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _QueueNum: 队列数量，取值范围3～16
        :type QueueNum: int
        :param _Remark: 备注信息，最多 128 个字符
        :type Remark: str
        :param _MsgTTL: 消息保留时长（单位：小时）
        :type MsgTTL: int
        """
        self._InstanceId = None
        self._Topic = None
        self._QueueNum = None
        self._Remark = None
        self._MsgTTL = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def QueueNum(self):
        r"""队列数量，取值范围3～16
        :rtype: int
        """
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def Remark(self):
        r"""备注信息，最多 128 个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MsgTTL(self):
        r"""消息保留时长（单位：小时）
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._QueueNum = params.get("QueueNum")
        self._Remark = params.get("Remark")
        self._MsgTTL = params.get("MsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    r"""ModifyTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class PacketStatistics(AbstractModel):
    r"""MQTT客户端监控

    """

    def __init__(self):
        r"""
        :param _MessageType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageType: str
        :param _Qos: 服务质量
注意：此字段可能返回 null，表示取不到有效值。
        :type Qos: int
        :param _Count: 指标值
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._MessageType = None
        self._Qos = None
        self._Count = None

    @property
    def MessageType(self):
        r"""类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def Qos(self):
        r"""服务质量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Count(self):
        r"""指标值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._MessageType = params.get("MessageType")
        self._Qos = params.get("Qos")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceTag(AbstractModel):
    r"""价格标签信息，一个完整的价格标签包含计价类别和计费项标签。

    """

    def __init__(self):
        r"""
        :param _Name: 计价名称（枚举值：tps：TPS基础价；stepTps：TPS步长）
        :type Name: str
        :param _Step: 计费项对应的步长数
注意：此字段可能返回 null，表示取不到有效值。
        :type Step: int
        """
        self._Name = None
        self._Step = None

    @property
    def Name(self):
        r"""计价名称（枚举值：tps：TPS基础价；stepTps：TPS步长）
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Step(self):
        r"""计费项对应的步长数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Step = params.get("Step")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProducerInfo(AbstractModel):
    r"""生产者信息

    """

    def __init__(self):
        r"""
        :param _ClientId: 客户端ID	
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        :param _ClientIp: 客户端IP	
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIp: str
        :param _Language: 客户端语言 
- JAVA((byte) 0)
- CPP((byte) 1) 
- DOTNET((byte) 2) 
- PYTHON((byte) 3)
- DELPHI((byte) 4)
- ERLANG((byte) 5)
- RUBY((byte) 6)
- OTHER((byte) 7)
- HTTP((byte) 8)
- GO((byte) 9)
- PHP((byte) 10)
- OMS((byte) 11)
注意：此字段可能返回 null，表示取不到有效值。
        :type Language: str
        :param _Version: 客户端版本	
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _LastUpdateTimestamp: 最后生产时间，**Unix时间戳（秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTimestamp: int
        :param _ChannelProtocol: 生产者客户端协议类型，枚举如下：

- grpc：GRpc协议
- remoting：Remoting协议
- http：HTTP协议
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelProtocol: str
        """
        self._ClientId = None
        self._ClientIp = None
        self._Language = None
        self._Version = None
        self._LastUpdateTimestamp = None
        self._ChannelProtocol = None

    @property
    def ClientId(self):
        r"""客户端ID	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientIp(self):
        r"""客户端IP	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Language(self):
        r"""客户端语言 
- JAVA((byte) 0)
- CPP((byte) 1) 
- DOTNET((byte) 2) 
- PYTHON((byte) 3)
- DELPHI((byte) 4)
- ERLANG((byte) 5)
- RUBY((byte) 6)
- OTHER((byte) 7)
- HTTP((byte) 8)
- GO((byte) 9)
- PHP((byte) 10)
- OMS((byte) 11)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Version(self):
        r"""客户端版本	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LastUpdateTimestamp(self):
        r"""最后生产时间，**Unix时间戳（秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastUpdateTimestamp

    @LastUpdateTimestamp.setter
    def LastUpdateTimestamp(self, LastUpdateTimestamp):
        self._LastUpdateTimestamp = LastUpdateTimestamp

    @property
    def ChannelProtocol(self):
        r"""生产者客户端协议类型，枚举如下：

- grpc：GRpc协议
- remoting：Remoting协议
- http：HTTP协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChannelProtocol

    @ChannelProtocol.setter
    def ChannelProtocol(self, ChannelProtocol):
        self._ChannelProtocol = ChannelProtocol


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._ClientIp = params.get("ClientIp")
        self._Language = params.get("Language")
        self._Version = params.get("Version")
        self._LastUpdateTimestamp = params.get("LastUpdateTimestamp")
        self._ChannelProtocol = params.get("ChannelProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductSKU(AbstractModel):
    r"""商品售卖信息

    """

    def __init__(self):
        r"""
        :param _InstanceType: 产品类型，
EXPERIMENT，体验版
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :type InstanceType: str
        :param _SkuCode: 规格代码
        :type SkuCode: str
        :param _TpsLimit: TPS上限
        :type TpsLimit: int
        :param _ScaledTpsLimit: 弹性TPS上限
        :type ScaledTpsLimit: int
        :param _TopicNumLimit: 主题数量上限默认值
        :type TopicNumLimit: int
        :param _GroupNumLimit: 消费组数量上限
        :type GroupNumLimit: int
        :param _DefaultRetention: 默认消息保留时间，小时为单位
        :type DefaultRetention: int
        :param _RetentionUpperLimit: 可调整消息保留时间上限，小时为单位
        :type RetentionUpperLimit: int
        :param _RetentionLowerLimit: 可调整消息保留时间下限，小时为单位
        :type RetentionLowerLimit: int
        :param _MaxMessageDelay: 延时消息最大时长，小时为单位
        :type MaxMessageDelay: int
        :param _OnSale: 是否可购买
        :type OnSale: bool
        :param _PriceTags: 计费项信息
        :type PriceTags: list of PriceTag
        :param _TopicNumUpperLimit: 主题数量上限默认最大值
        :type TopicNumUpperLimit: int
        """
        self._InstanceType = None
        self._SkuCode = None
        self._TpsLimit = None
        self._ScaledTpsLimit = None
        self._TopicNumLimit = None
        self._GroupNumLimit = None
        self._DefaultRetention = None
        self._RetentionUpperLimit = None
        self._RetentionLowerLimit = None
        self._MaxMessageDelay = None
        self._OnSale = None
        self._PriceTags = None
        self._TopicNumUpperLimit = None

    @property
    def InstanceType(self):
        r"""产品类型，
EXPERIMENT，体验版
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SkuCode(self):
        r"""规格代码
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        r"""TPS上限
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ScaledTpsLimit(self):
        r"""弹性TPS上限
        :rtype: int
        """
        return self._ScaledTpsLimit

    @ScaledTpsLimit.setter
    def ScaledTpsLimit(self, ScaledTpsLimit):
        self._ScaledTpsLimit = ScaledTpsLimit

    @property
    def TopicNumLimit(self):
        r"""主题数量上限默认值
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def GroupNumLimit(self):
        r"""消费组数量上限
        :rtype: int
        """
        return self._GroupNumLimit

    @GroupNumLimit.setter
    def GroupNumLimit(self, GroupNumLimit):
        self._GroupNumLimit = GroupNumLimit

    @property
    def DefaultRetention(self):
        r"""默认消息保留时间，小时为单位
        :rtype: int
        """
        return self._DefaultRetention

    @DefaultRetention.setter
    def DefaultRetention(self, DefaultRetention):
        self._DefaultRetention = DefaultRetention

    @property
    def RetentionUpperLimit(self):
        r"""可调整消息保留时间上限，小时为单位
        :rtype: int
        """
        return self._RetentionUpperLimit

    @RetentionUpperLimit.setter
    def RetentionUpperLimit(self, RetentionUpperLimit):
        self._RetentionUpperLimit = RetentionUpperLimit

    @property
    def RetentionLowerLimit(self):
        r"""可调整消息保留时间下限，小时为单位
        :rtype: int
        """
        return self._RetentionLowerLimit

    @RetentionLowerLimit.setter
    def RetentionLowerLimit(self, RetentionLowerLimit):
        self._RetentionLowerLimit = RetentionLowerLimit

    @property
    def MaxMessageDelay(self):
        r"""延时消息最大时长，小时为单位
        :rtype: int
        """
        return self._MaxMessageDelay

    @MaxMessageDelay.setter
    def MaxMessageDelay(self, MaxMessageDelay):
        self._MaxMessageDelay = MaxMessageDelay

    @property
    def OnSale(self):
        r"""是否可购买
        :rtype: bool
        """
        return self._OnSale

    @OnSale.setter
    def OnSale(self, OnSale):
        self._OnSale = OnSale

    @property
    def PriceTags(self):
        r"""计费项信息
        :rtype: list of PriceTag
        """
        return self._PriceTags

    @PriceTags.setter
    def PriceTags(self, PriceTags):
        self._PriceTags = PriceTags

    @property
    def TopicNumUpperLimit(self):
        r"""主题数量上限默认最大值
        :rtype: int
        """
        return self._TopicNumUpperLimit

    @TopicNumUpperLimit.setter
    def TopicNumUpperLimit(self, TopicNumUpperLimit):
        self._TopicNumUpperLimit = TopicNumUpperLimit


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._SkuCode = params.get("SkuCode")
        self._TpsLimit = params.get("TpsLimit")
        self._ScaledTpsLimit = params.get("ScaledTpsLimit")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._GroupNumLimit = params.get("GroupNumLimit")
        self._DefaultRetention = params.get("DefaultRetention")
        self._RetentionUpperLimit = params.get("RetentionUpperLimit")
        self._RetentionLowerLimit = params.get("RetentionLowerLimit")
        self._MaxMessageDelay = params.get("MaxMessageDelay")
        self._OnSale = params.get("OnSale")
        if params.get("PriceTags") is not None:
            self._PriceTags = []
            for item in params.get("PriceTags"):
                obj = PriceTag()
                obj._deserialize(item)
                self._PriceTags.append(obj)
        self._TopicNumUpperLimit = params.get("TopicNumUpperLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicAccessRule(AbstractModel):
    r"""公网访问安全规则

    """

    def __init__(self):
        r"""
        :param _IpRule: ip网段信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IpRule: str
        :param _Allow: 允许或者拒绝
注意：此字段可能返回 null，表示取不到有效值。
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
        r"""ip网段信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpRule

    @IpRule.setter
    def IpRule(self, IpRule):
        self._IpRule = IpRule

    @property
    def Allow(self):
        r"""允许或者拒绝
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def Remark(self):
        r"""备注信息
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
        


class RemoveMigratingTopicRequest(AbstractModel):
    r"""RemoveMigratingTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。
        :type TaskId: str
        :param _TopicName: 主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :type TopicName: str
        :param _Namespace: 命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :type Namespace: str
        """
        self._TaskId = None
        self._TopicName = None
        self._Namespace = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TopicName(self):
        r"""主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Namespace(self):
        r"""命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TopicName = params.get("TopicName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveMigratingTopicResponse(AbstractModel):
    r"""RemoveMigratingTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ResendDeadLetterMessageRequest(AbstractModel):
    r"""ResendDeadLetterMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _MessageIds: 死信消息ID列表
        :type MessageIds: list of str
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        """
        self._InstanceId = None
        self._MessageIds = None
        self._ConsumerGroup = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def MessageIds(self):
        r"""死信消息ID列表
        :rtype: list of str
        """
        return self._MessageIds

    @MessageIds.setter
    def MessageIds(self, MessageIds):
        self._MessageIds = MessageIds

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._MessageIds = params.get("MessageIds")
        self._ConsumerGroup = params.get("ConsumerGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResendDeadLetterMessageResponse(AbstractModel):
    r"""ResendDeadLetterMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResendResult: 重发消息结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ResendResult: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResendResult = None
        self._RequestId = None

    @property
    def ResendResult(self):
        r"""重发消息结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ResendResult

    @ResendResult.setter
    def ResendResult(self, ResendResult):
        self._ResendResult = ResendResult

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
        self._ResendResult = params.get("ResendResult")
        self._RequestId = params.get("RequestId")


class ResetConsumerGroupOffsetRequest(AbstractModel):
    r"""ResetConsumerGroupOffset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :type Topic: str
        :param _ResetTimestamp: 重置位点的时间戳（单位：毫秒），指定为 -1 时表示重置到最新位点
        :type ResetTimestamp: int
        :param _ConsumerGroup: 消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :type ConsumerGroup: str
        """
        self._InstanceId = None
        self._Topic = None
        self._ResetTimestamp = None
        self._ConsumerGroup = None

    @property
    def InstanceId(self):
        r"""腾讯云 RocketMQ 实例 ID，从 [DescribeFusionInstanceList](https://cloud.tencent.com/document/api/1493/106745) 接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称，从 [DescribeTopicList](https://cloud.tencent.com/document/api/1493/96030) 接口返回的 [TopicItem](https://cloud.tencent.com/document/api/1493/96031#TopicItem) 或控制台获得。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def ResetTimestamp(self):
        r"""重置位点的时间戳（单位：毫秒），指定为 -1 时表示重置到最新位点
        :rtype: int
        """
        return self._ResetTimestamp

    @ResetTimestamp.setter
    def ResetTimestamp(self, ResetTimestamp):
        self._ResetTimestamp = ResetTimestamp

    @property
    def ConsumerGroup(self):
        r"""消费组名称，从 [DescribeConsumerGroupList](https://cloud.tencent.com/document/api/1493/101535) 接口返回的 [ConsumeGroupItem](https://cloud.tencent.com/document/api/1493/96031#ConsumeGroupItem) 或控制台获得。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._ResetTimestamp = params.get("ResetTimestamp")
        self._ConsumerGroup = params.get("ConsumerGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetConsumerGroupOffsetResponse(AbstractModel):
    r"""ResetConsumerGroupOffset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RoleItem(AbstractModel):
    r"""角色信息

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _PermRead: 是否开启消费
        :type PermRead: bool
        :param _PermWrite: 是否开启生产
        :type PermWrite: bool
        :param _AccessKey: Access Key
        :type AccessKey: str
        :param _SecretKey: Secret Key
        :type SecretKey: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _CreatedTime: 角色的创建时间，**Unix时间戳（毫秒）**
        :type CreatedTime: int
        :param _ModifiedTime: 角色的更新时间，**Unix时间戳（毫秒）**
        :type ModifiedTime: int
        :param _PermType: 权限类型，默认按集群授权（Cluster：集群级别；TopicAndGroup：主题&消费组级别）
        :type PermType: str
        :param _DetailedRolePerms: Topic和Group维度权限配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailedRolePerms: list of DetailedRolePerm
        """
        self._RoleName = None
        self._PermRead = None
        self._PermWrite = None
        self._AccessKey = None
        self._SecretKey = None
        self._Remark = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._PermType = None
        self._DetailedRolePerms = None

    @property
    def RoleName(self):
        r"""角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def PermRead(self):
        r"""是否开启消费
        :rtype: bool
        """
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def PermWrite(self):
        r"""是否开启生产
        :rtype: bool
        """
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def AccessKey(self):
        r"""Access Key
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""Secret Key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        r"""角色的创建时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        r"""角色的更新时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def PermType(self):
        r"""权限类型，默认按集群授权（Cluster：集群级别；TopicAndGroup：主题&消费组级别）
        :rtype: str
        """
        return self._PermType

    @PermType.setter
    def PermType(self, PermType):
        self._PermType = PermType

    @property
    def DetailedRolePerms(self):
        r"""Topic和Group维度权限配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DetailedRolePerm
        """
        return self._DetailedRolePerms

    @DetailedRolePerms.setter
    def DetailedRolePerms(self, DetailedRolePerms):
        self._DetailedRolePerms = DetailedRolePerms


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._PermRead = params.get("PermRead")
        self._PermWrite = params.get("PermWrite")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Remark = params.get("Remark")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._PermType = params.get("PermType")
        if params.get("DetailedRolePerms") is not None:
            self._DetailedRolePerms = []
            for item in params.get("DetailedRolePerms"):
                obj = DetailedRolePerm()
                obj._deserialize(item)
                self._DetailedRolePerms.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackMigratingTopicStageRequest(AbstractModel):
    r"""RollbackMigratingTopicStage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :type TaskId: str
        :param _TopicName: 主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :type TopicName: str
        :param _Namespace: 命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :type Namespace: str
        """
        self._TaskId = None
        self._TopicName = None
        self._Namespace = None

    @property
    def TaskId(self):
        r"""任务ID，可在[DescribeSmoothMigrationTaskList](https://cloud.tencent.com/document/api/1493/119997)接口返回的[SmoothMigrationTaskItem](https://cloud.tencent.com/document/api/1493/96031#SmoothMigrationTaskItem)或控制台中获得。

        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TopicName(self):
        r"""主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。

        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Namespace(self):
        r"""命名空间，仅迁移至4.x集群有效，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TopicName = params.get("TopicName")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackMigratingTopicStageResponse(AbstractModel):
    r"""RollbackMigratingTopicStage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class SmoothMigrationTaskItem(AbstractModel):
    r"""平滑迁移任务

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
        :param _InstanceId: 目标集群实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ConnectionType: 网络连接类型， 
PUBLIC 公网 
VPC 私有网络 
OTHER 其他
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionType: str
        :param _SourceNameServer: 源集群NameServer地址	
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceNameServer: str
        :param _TaskStatus: 任务状态:
Configuration 迁移配置,
SourceConnecting 连接源集群中,
 MetaDataImport 元数据导入,
EndpointSetup 切换接入点,
ServiceMigration 切流中,
Completed 已完成,
Cancelled 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param _InstanceVersion: 目标集群实例版本，
4 表示4.x版本
5 表示5.x版本
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceVersion: str
        """
        self._TaskId = None
        self._TaskName = None
        self._SourceClusterName = None
        self._InstanceId = None
        self._ConnectionType = None
        self._SourceNameServer = None
        self._TaskStatus = None
        self._InstanceVersion = None

    @property
    def TaskId(self):
        r"""任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""任务名称	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def SourceClusterName(self):
        r"""源集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceClusterName

    @SourceClusterName.setter
    def SourceClusterName(self, SourceClusterName):
        self._SourceClusterName = SourceClusterName

    @property
    def InstanceId(self):
        r"""目标集群实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConnectionType(self):
        r"""网络连接类型， 
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
        r"""源集群NameServer地址	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceNameServer

    @SourceNameServer.setter
    def SourceNameServer(self, SourceNameServer):
        self._SourceNameServer = SourceNameServer

    @property
    def TaskStatus(self):
        r"""任务状态:
Configuration 迁移配置,
SourceConnecting 连接源集群中,
 MetaDataImport 元数据导入,
EndpointSetup 切换接入点,
ServiceMigration 切流中,
Completed 已完成,
Cancelled 已取消
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def InstanceVersion(self):
        r"""目标集群实例版本，
4 表示4.x版本
5 表示5.x版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._SourceClusterName = params.get("SourceClusterName")
        self._InstanceId = params.get("InstanceId")
        self._ConnectionType = params.get("ConnectionType")
        self._SourceNameServer = params.get("SourceNameServer")
        self._TaskStatus = params.get("TaskStatus")
        self._InstanceVersion = params.get("InstanceVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceClusterGroupConfig(AbstractModel):
    r"""消费组配置信息

    """

    def __init__(self):
        r"""
        :param _GroupName: 消费组名称，可在[DescribeSourceClusterGroupList](https://cloud.tencent.com/document/api/1493/118006)接口返回的[SourceClusterGroupConfig](https://cloud.tencent.com/document/api/1493/96031#SourceClusterGroupConfig)数据中获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Imported: 是否已导入，作为入参时无效
注意：此字段可能返回 null，表示取不到有效值。
        :type Imported: bool
        :param _Namespace: 命名空间，仅4.x集群有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _ImportStatus: 导入状态
Unknown 未知
Success 成功
Failure 失败
AlreadyExists 已存在

仅作为出参时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type ImportStatus: str
        :param _NamespaceV4: 4.x的命名空间，出参使用
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceV4: str
        :param _GroupNameV4: 4.x的消费组名，出参使用
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNameV4: str
        :param _FullNamespaceV4: 4.x的完整命名空间，出参使用
注意：此字段可能返回 null，表示取不到有效值。
        :type FullNamespaceV4: str
        :param _ConsumeMessageOrderly: 是否为顺序投递，5.0有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumeMessageOrderly: bool
        """
        self._GroupName = None
        self._Remark = None
        self._Imported = None
        self._Namespace = None
        self._ImportStatus = None
        self._NamespaceV4 = None
        self._GroupNameV4 = None
        self._FullNamespaceV4 = None
        self._ConsumeMessageOrderly = None

    @property
    def GroupName(self):
        r"""消费组名称，可在[DescribeSourceClusterGroupList](https://cloud.tencent.com/document/api/1493/118006)接口返回的[SourceClusterGroupConfig](https://cloud.tencent.com/document/api/1493/96031#SourceClusterGroupConfig)数据中获取。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Remark(self):
        r"""备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Imported(self):
        r"""是否已导入，作为入参时无效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Imported

    @Imported.setter
    def Imported(self, Imported):
        self._Imported = Imported

    @property
    def Namespace(self):
        r"""命名空间，仅4.x集群有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ImportStatus(self):
        r"""导入状态
Unknown 未知
Success 成功
Failure 失败
AlreadyExists 已存在

仅作为出参时使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ImportStatus

    @ImportStatus.setter
    def ImportStatus(self, ImportStatus):
        self._ImportStatus = ImportStatus

    @property
    def NamespaceV4(self):
        r"""4.x的命名空间，出参使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NamespaceV4

    @NamespaceV4.setter
    def NamespaceV4(self, NamespaceV4):
        self._NamespaceV4 = NamespaceV4

    @property
    def GroupNameV4(self):
        r"""4.x的消费组名，出参使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupNameV4

    @GroupNameV4.setter
    def GroupNameV4(self, GroupNameV4):
        self._GroupNameV4 = GroupNameV4

    @property
    def FullNamespaceV4(self):
        r"""4.x的完整命名空间，出参使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FullNamespaceV4

    @FullNamespaceV4.setter
    def FullNamespaceV4(self, FullNamespaceV4):
        self._FullNamespaceV4 = FullNamespaceV4

    @property
    def ConsumeMessageOrderly(self):
        r"""是否为顺序投递，5.0有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Remark = params.get("Remark")
        self._Imported = params.get("Imported")
        self._Namespace = params.get("Namespace")
        self._ImportStatus = params.get("ImportStatus")
        self._NamespaceV4 = params.get("NamespaceV4")
        self._GroupNameV4 = params.get("GroupNameV4")
        self._FullNamespaceV4 = params.get("FullNamespaceV4")
        self._ConsumeMessageOrderly = params.get("ConsumeMessageOrderly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceClusterTopicConfig(AbstractModel):
    r"""源集群主题配置

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :type TopicName: str
        :param _TopicType: 主题类型，
5.x版本
UNSPECIFIED 未指定
NORMAL 普通消息
FIFO 顺序消息
DELAY 延迟消息
TRANSACTION 事务消息

4.x版本
Normal 普通消息
PartitionedOrder 分区顺序消息
Transaction 事务消息
DelayScheduled 延时消息

        :type TopicType: str
        :param _QueueNum: 队列数
        :type QueueNum: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _Imported: 是否已导入，作为入参时无效
        :type Imported: bool
        :param _Namespace: 命名空间，仅4.x集群有效
        :type Namespace: str
        :param _ImportStatus: 导入状态，
Unknown 未知，
AlreadyExists 已存在，
Success 成功，
Failure 失败

仅作为出参可用
        :type ImportStatus: str
        :param _NamespaceV4: 4.x的命名空间，出参使用
        :type NamespaceV4: str
        :param _TopicNameV4: 4.x的主题名，出参使用
        :type TopicNameV4: str
        :param _FullNamespaceV4: 4.x的完整命名空间，出参使用
        :type FullNamespaceV4: str
        """
        self._TopicName = None
        self._TopicType = None
        self._QueueNum = None
        self._Remark = None
        self._Imported = None
        self._Namespace = None
        self._ImportStatus = None
        self._NamespaceV4 = None
        self._TopicNameV4 = None
        self._FullNamespaceV4 = None

    @property
    def TopicName(self):
        r"""主题名称，可在[DescribeMigratingTopicList](https://cloud.tencent.com/document/api/1493/118007)接口返回的[MigratingTopic](https://cloud.tencent.com/document/api/1493/96031#MigratingTopic)数据结构中获得。
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicType(self):
        r"""主题类型，
5.x版本
UNSPECIFIED 未指定
NORMAL 普通消息
FIFO 顺序消息
DELAY 延迟消息
TRANSACTION 事务消息

4.x版本
Normal 普通消息
PartitionedOrder 分区顺序消息
Transaction 事务消息
DelayScheduled 延时消息

        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def QueueNum(self):
        r"""队列数
        :rtype: int
        """
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Imported(self):
        r"""是否已导入，作为入参时无效
        :rtype: bool
        """
        return self._Imported

    @Imported.setter
    def Imported(self, Imported):
        self._Imported = Imported

    @property
    def Namespace(self):
        r"""命名空间，仅4.x集群有效
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ImportStatus(self):
        r"""导入状态，
Unknown 未知，
AlreadyExists 已存在，
Success 成功，
Failure 失败

仅作为出参可用
        :rtype: str
        """
        return self._ImportStatus

    @ImportStatus.setter
    def ImportStatus(self, ImportStatus):
        self._ImportStatus = ImportStatus

    @property
    def NamespaceV4(self):
        r"""4.x的命名空间，出参使用
        :rtype: str
        """
        return self._NamespaceV4

    @NamespaceV4.setter
    def NamespaceV4(self, NamespaceV4):
        self._NamespaceV4 = NamespaceV4

    @property
    def TopicNameV4(self):
        r"""4.x的主题名，出参使用
        :rtype: str
        """
        return self._TopicNameV4

    @TopicNameV4.setter
    def TopicNameV4(self, TopicNameV4):
        self._TopicNameV4 = TopicNameV4

    @property
    def FullNamespaceV4(self):
        r"""4.x的完整命名空间，出参使用
        :rtype: str
        """
        return self._FullNamespaceV4

    @FullNamespaceV4.setter
    def FullNamespaceV4(self, FullNamespaceV4):
        self._FullNamespaceV4 = FullNamespaceV4


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._TopicType = params.get("TopicType")
        self._QueueNum = params.get("QueueNum")
        self._Remark = params.get("Remark")
        self._Imported = params.get("Imported")
        self._Namespace = params.get("Namespace")
        self._ImportStatus = params.get("ImportStatus")
        self._NamespaceV4 = params.get("NamespaceV4")
        self._TopicNameV4 = params.get("TopicNameV4")
        self._FullNamespaceV4 = params.get("FullNamespaceV4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticsReport(AbstractModel):
    r"""MQTT客户端数据流量统计

    """

    def __init__(self):
        r"""
        :param _Bytes: 字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type Bytes: int
        :param _Items: 监控指标
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of PacketStatistics
        """
        self._Bytes = None
        self._Items = None

    @property
    def Bytes(self):
        r"""字节数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bytes

    @Bytes.setter
    def Bytes(self, Bytes):
        self._Bytes = Bytes

    @property
    def Items(self):
        r"""监控指标
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PacketStatistics
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._Bytes = params.get("Bytes")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = PacketStatistics()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscriptionData(AbstractModel):
    r"""主题与消费组的订阅关系数据

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Topic: 主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: str
        :param _TopicType: 主题类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicType: str
        :param _TopicQueueNum: 单个节点上主题队列数
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicQueueNum: int
        :param _ConsumerGroup: 消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerGroup: str
        :param _IsOnline: 是否在线
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOnline: bool
        :param _ConsumeType: 消费类型，枚举值如下：

- PULL：PULL 消费类型
- PUSH：PUSH 消费类型
- POP：POP 消费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumeType: str
        :param _SubString: 订阅规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SubString: str
        :param _ExpressionType: 过滤类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpressionType: str
        :param _Consistency: 订阅一致性，枚举如下：

- 0: 订阅一致
- 1: 订阅不一致
注意：此字段可能返回 null，表示取不到有效值。
        :type Consistency: int
        :param _ConsumerLag: 消费堆积
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLag: int
        :param _LastUpdateTime: 最后消费进度更新时间，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: int
        :param _MaxRetryTimes: 最大重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetryTimes: int
        :param _ConsumeMessageOrderly: 是否顺序消费
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumeMessageOrderly: bool
        :param _MessageModel: 消费模式: 
BROADCASTING 广播模式;
CLUSTERING 集群模式;
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageModel: str
        :param _ClientSubscriptionInfos: 订阅不一致的客户端列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientSubscriptionInfos: list of ClientSubscriptionInfo
        """
        self._InstanceId = None
        self._Topic = None
        self._TopicType = None
        self._TopicQueueNum = None
        self._ConsumerGroup = None
        self._IsOnline = None
        self._ConsumeType = None
        self._SubString = None
        self._ExpressionType = None
        self._Consistency = None
        self._ConsumerLag = None
        self._LastUpdateTime = None
        self._MaxRetryTimes = None
        self._ConsumeMessageOrderly = None
        self._MessageModel = None
        self._ClientSubscriptionInfos = None

    @property
    def InstanceId(self):
        r"""实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        r"""主题类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def TopicQueueNum(self):
        r"""单个节点上主题队列数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicQueueNum

    @TopicQueueNum.setter
    def TopicQueueNum(self, TopicQueueNum):
        self._TopicQueueNum = TopicQueueNum

    @property
    def ConsumerGroup(self):
        r"""消费组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def IsOnline(self):
        r"""是否在线
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsOnline

    @IsOnline.setter
    def IsOnline(self, IsOnline):
        self._IsOnline = IsOnline

    @property
    def ConsumeType(self):
        r"""消费类型，枚举值如下：

- PULL：PULL 消费类型
- PUSH：PUSH 消费类型
- POP：POP 消费类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConsumeType

    @ConsumeType.setter
    def ConsumeType(self, ConsumeType):
        self._ConsumeType = ConsumeType

    @property
    def SubString(self):
        r"""订阅规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubString

    @SubString.setter
    def SubString(self, SubString):
        self._SubString = SubString

    @property
    def ExpressionType(self):
        r"""过滤类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpressionType

    @ExpressionType.setter
    def ExpressionType(self, ExpressionType):
        self._ExpressionType = ExpressionType

    @property
    def Consistency(self):
        r"""订阅一致性，枚举如下：

- 0: 订阅一致
- 1: 订阅不一致
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency

    @property
    def ConsumerLag(self):
        r"""消费堆积
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

    @property
    def LastUpdateTime(self):
        r"""最后消费进度更新时间，**Unix时间戳（毫秒）**
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def MaxRetryTimes(self):
        r"""最大重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def ConsumeMessageOrderly(self):
        r"""是否顺序消费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def MessageModel(self):
        r"""消费模式: 
BROADCASTING 广播模式;
CLUSTERING 集群模式;
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MessageModel

    @MessageModel.setter
    def MessageModel(self, MessageModel):
        self._MessageModel = MessageModel

    @property
    def ClientSubscriptionInfos(self):
        r"""订阅不一致的客户端列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClientSubscriptionInfo
        """
        return self._ClientSubscriptionInfos

    @ClientSubscriptionInfos.setter
    def ClientSubscriptionInfos(self, ClientSubscriptionInfos):
        self._ClientSubscriptionInfos = ClientSubscriptionInfos


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._TopicType = params.get("TopicType")
        self._TopicQueueNum = params.get("TopicQueueNum")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._IsOnline = params.get("IsOnline")
        self._ConsumeType = params.get("ConsumeType")
        self._SubString = params.get("SubString")
        self._ExpressionType = params.get("ExpressionType")
        self._Consistency = params.get("Consistency")
        self._ConsumerLag = params.get("ConsumerLag")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._ConsumeMessageOrderly = params.get("ConsumeMessageOrderly")
        self._MessageModel = params.get("MessageModel")
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
        


class Tag(AbstractModel):
    r"""标签数据

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签名称
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
        r"""标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
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
        


class TagFilter(AbstractModel):
    r"""标签过滤器

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键名称
        :type TagKey: str
        :param _TagValues: 标签值列表
        :type TagValues: list of str
        """
        self._TagKey = None
        self._TagValues = None

    @property
    def TagKey(self):
        r"""标签键名称
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
        r"""标签值列表
        :rtype: list of str
        """
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicConsumeStats(AbstractModel):
    r"""主题消费进度

    """

    def __init__(self):
        r"""
        :param _Topic: 主题名称
        :type Topic: str
        :param _TopicType: 主题类型，枚举值如下：

- UNSPECIFIED：未指定
- NORMAL：普通消息
- FIFO：顺序消息
- DELAY：延时消息
- TRANSACTION：事务消息
        :type TopicType: str
        :param _QueueNum: 单节点主题队列数量
        :type QueueNum: int
        :param _ConsumerLag: 消费堆积
        :type ConsumerLag: int
        :param _SubString: 订阅规则，`*`表示订阅全部TAG
        :type SubString: str
        :param _LastUpdateTime: 最后消费进度更新时间，**Unix时间戳（毫秒）**
        :type LastUpdateTime: int
        """
        self._Topic = None
        self._TopicType = None
        self._QueueNum = None
        self._ConsumerLag = None
        self._SubString = None
        self._LastUpdateTime = None

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        r"""主题类型，枚举值如下：

- UNSPECIFIED：未指定
- NORMAL：普通消息
- FIFO：顺序消息
- DELAY：延时消息
- TRANSACTION：事务消息
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def QueueNum(self):
        r"""单节点主题队列数量
        :rtype: int
        """
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def ConsumerLag(self):
        r"""消费堆积
        :rtype: int
        """
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

    @property
    def SubString(self):
        r"""订阅规则，`*`表示订阅全部TAG
        :rtype: str
        """
        return self._SubString

    @SubString.setter
    def SubString(self, SubString):
        self._SubString = SubString

    @property
    def LastUpdateTime(self):
        r"""最后消费进度更新时间，**Unix时间戳（毫秒）**
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._TopicType = params.get("TopicType")
        self._QueueNum = params.get("QueueNum")
        self._ConsumerLag = params.get("ConsumerLag")
        self._SubString = params.get("SubString")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicItem(AbstractModel):
    r"""列表上的主题信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _TopicType: 主题类型
NORMAL:普通消息,
FIFO:顺序消息,
DELAY:延时消息,
TRANSACTION:事务消息
        :type TopicType: str
        :param _QueueNum: 队列数量
        :type QueueNum: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _ClusterIdV4: 4.x的集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIdV4: str
        :param _NamespaceV4: 4.x的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NamespaceV4: str
        :param _TopicV4: 4.x的主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicV4: str
        :param _FullNamespaceV4: 4.x的完整命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type FullNamespaceV4: str
        :param _MsgTTL: 消息保留时长
        :type MsgTTL: int
        :param _TagList: 绑定的标签列表
        :type TagList: list of Tag
        """
        self._InstanceId = None
        self._Topic = None
        self._TopicType = None
        self._QueueNum = None
        self._Remark = None
        self._ClusterIdV4 = None
        self._NamespaceV4 = None
        self._TopicV4 = None
        self._FullNamespaceV4 = None
        self._MsgTTL = None
        self._TagList = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        r"""主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        r"""主题类型
NORMAL:普通消息,
FIFO:顺序消息,
DELAY:延时消息,
TRANSACTION:事务消息
        :rtype: str
        """
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def QueueNum(self):
        r"""队列数量
        :rtype: int
        """
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterIdV4(self):
        r"""4.x的集群id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClusterIdV4

    @ClusterIdV4.setter
    def ClusterIdV4(self, ClusterIdV4):
        self._ClusterIdV4 = ClusterIdV4

    @property
    def NamespaceV4(self):
        r"""4.x的命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NamespaceV4

    @NamespaceV4.setter
    def NamespaceV4(self, NamespaceV4):
        self._NamespaceV4 = NamespaceV4

    @property
    def TopicV4(self):
        r"""4.x的主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicV4

    @TopicV4.setter
    def TopicV4(self, TopicV4):
        self._TopicV4 = TopicV4

    @property
    def FullNamespaceV4(self):
        r"""4.x的完整命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FullNamespaceV4

    @FullNamespaceV4.setter
    def FullNamespaceV4(self, FullNamespaceV4):
        self._FullNamespaceV4 = FullNamespaceV4

    @property
    def MsgTTL(self):
        r"""消息保留时长
        :rtype: int
        """
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def TagList(self):
        r"""绑定的标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._TopicType = params.get("TopicType")
        self._QueueNum = params.get("QueueNum")
        self._Remark = params.get("Remark")
        self._ClusterIdV4 = params.get("ClusterIdV4")
        self._NamespaceV4 = params.get("NamespaceV4")
        self._TopicV4 = params.get("TopicV4")
        self._FullNamespaceV4 = params.get("FullNamespaceV4")
        self._MsgTTL = params.get("MsgTTL")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicStageChangeResult(AbstractModel):
    r"""迁移主题修改状态后的结果

    """

    def __init__(self):
        r"""
        :param _TopicName: 主题名称
        :type TopicName: str
        :param _Success: 是否成功
        :type Success: bool
        :param _Namespace: 命名空间，仅4.x有效
        :type Namespace: str
        """
        self._TopicName = None
        self._Success = None
        self._Namespace = None

    @property
    def TopicName(self):
        r"""主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Success(self):
        r"""是否成功
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Namespace(self):
        r"""命名空间，仅4.x有效
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Success = params.get("Success")
        self._Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    r"""VPC信息

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        r"""VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID
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
        


class ZoneScheduledItem(AbstractModel):
    r"""proxy调度时各个可用区有无调度任务

    """

    def __init__(self):
        r"""
        :param _ZoneId: 可用区ID
        :type ZoneId: str
        :param _NodePermWipeFlag: 有剔除的调度任务且没有切回的可用区时，该值为true，反之为false
        :type NodePermWipeFlag: bool
        """
        self._ZoneId = None
        self._NodePermWipeFlag = None

    @property
    def ZoneId(self):
        r"""可用区ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NodePermWipeFlag(self):
        r"""有剔除的调度任务且没有切回的可用区时，该值为true，反之为false
        :rtype: bool
        """
        return self._NodePermWipeFlag

    @NodePermWipeFlag.setter
    def NodePermWipeFlag(self, NodePermWipeFlag):
        self._NodePermWipeFlag = NodePermWipeFlag


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._NodePermWipeFlag = params.get("NodePermWipeFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        