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


class CreateConsumerGroupRequest(AbstractModel):
    """CreateConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称
        :type ConsumerGroup: str
        :param _MaxRetryTimes: 最大重试次数
        :type MaxRetryTimes: int
        :param _ConsumeEnable: 是否开启消费
        :type ConsumeEnable: bool
        :param _ConsumeMessageOrderly: 顺序投递：true
并发投递：false
        :type ConsumeMessageOrderly: bool
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._MaxRetryTimes = None
        self._ConsumeEnable = None
        self._ConsumeMessageOrderly = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def MaxRetryTimes(self):
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def ConsumeEnable(self):
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

    @property
    def ConsumeMessageOrderly(self):
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._MaxRetryTimes = params.get("MaxRetryTimes")
        self._ConsumeEnable = params.get("ConsumeEnable")
        self._ConsumeMessageOrderly = params.get("ConsumeMessageOrderly")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConsumerGroupResponse(AbstractModel):
    """CreateConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ConsumerGroup: 消费组
        :type ConsumerGroup: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ConsumerGroup = params.get("ConsumerGroup")
        self._RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

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
experiment_500,
basic_1k,
basic_2k,
basic_4k,
basic_6k
        :type SkuCode: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _TagList: 标签列表
        :type TagList: list of Tag
        :param _VpcList: 实例绑定的VPC信息
        :type VpcList: list of VpcInfo
        :param _EnablePublic: 是否开启公网
        :type EnablePublic: bool
        :param _Bandwidth: 公网带宽
        :type Bandwidth: int
        :param _IpRules: 公网访问白名单
        :type IpRules: list of IpRule
        :param _MessageRetention: 消息保留时长，小时为单位
        :type MessageRetention: int
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
        self._MessageRetention = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def VpcList(self):
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def EnablePublic(self):
        return self._EnablePublic

    @EnablePublic.setter
    def EnablePublic(self, EnablePublic):
        self._EnablePublic = EnablePublic

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules

    @property
    def MessageRetention(self):
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention


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
        self._MessageRetention = params.get("MessageRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Role: 角色名称
        :type Role: str
        :param _Remark: 备注
        :type Remark: str
        :param _PermWrite: 是否开启生产权限
        :type PermWrite: bool
        :param _PermRead: 是否开启消费权限
        :type PermRead: bool
        """
        self._InstanceId = None
        self._Role = None
        self._Remark = None
        self._PermWrite = None
        self._PermRead = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PermWrite(self):
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def PermRead(self):
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Role = params.get("Role")
        self._Remark = params.get("Remark")
        self._PermWrite = params.get("PermWrite")
        self._PermRead = params.get("PermRead")
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
        :param _Role: 角色名
        :type Role: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Role = None
        self._RequestId = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _TopicType: 主题类型
UNSPECIFIED:未指定,
NORMAL:普通消息,
FIFO:顺序消息,
DELAY:延时消息,
TRANSACTION:事务消息
        :type TopicType: str
        :param _QueueNum: 队列数量
        :type QueueNum: int
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._TopicType = None
        self._QueueNum = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def QueueNum(self):
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._TopicType = params.get("TopicType")
        self._QueueNum = params.get("QueueNum")
        self._Remark = params.get("Remark")
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._RequestId = params.get("RequestId")


class DeleteConsumerGroupRequest(AbstractModel):
    """DeleteConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称
        :type ConsumerGroup: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
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
    """DeleteConsumerGroup返回参数结构体

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


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DeleteInstance返回参数结构体

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


class DeleteRoleRequest(AbstractModel):
    """DeleteRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Role: 角色名称
        :type Role: str
        """
        self._InstanceId = None
        self._Role = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Role(self):
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
    """DeleteRole返回参数结构体

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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
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


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ConsumerGroup: 消费组名称
        :type ConsumerGroup: str
        """
        self._InstanceId = None
        self._ConsumerGroup = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
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
    """DescribeConsumerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsumerNum: 在线消费者数量
        :type ConsumerNum: int
        :param _Tps: TPS
        :type Tps: int
        :param _ConsumerLag: 消息堆积数量
        :type ConsumerLag: int
        :param _ConsumeType: 消费者类型
        :type ConsumeType: str
        :param _CreatedTime: 创建时间，秒为单位
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = None

    @property
    def ConsumerNum(self):
        return self._ConsumerNum

    @ConsumerNum.setter
    def ConsumerNum(self, ConsumerNum):
        self._ConsumerNum = ConsumerNum

    @property
    def Tps(self):
        return self._Tps

    @Tps.setter
    def Tps(self, Tps):
        self._Tps = Tps

    @property
    def ConsumerLag(self):
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

    @property
    def ConsumeType(self):
        return self._ConsumeType

    @ConsumeType.setter
    def ConsumeType(self, ConsumeType):
        self._ConsumeType = ConsumeType

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ConsumeMessageOrderly(self):
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def ConsumeEnable(self):
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

    @property
    def MaxRetryTimes(self):
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        :param _Filters: 查询条件列表
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
    def TagFilters(self):
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
        


class DescribeInstanceListResponse(AbstractModel):
    """DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 实例列表
        :type Data: list of InstanceItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，
EXPERIMENT 体验版
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _CreatedTime: 创建时间，秒为单位
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
        :param _InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param _SkuCode: 实例规格
        :type SkuCode: str
        :param _PayMode: 计费模式
        :type PayMode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def TopicNumLimit(self):
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def GroupNumLimit(self):
        return self._GroupNumLimit

    @GroupNumLimit.setter
    def GroupNumLimit(self, GroupNumLimit):
        self._GroupNumLimit = GroupNumLimit

    @property
    def MessageRetention(self):
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def RetentionUpperLimit(self):
        return self._RetentionUpperLimit

    @RetentionUpperLimit.setter
    def RetentionUpperLimit(self, RetentionUpperLimit):
        self._RetentionUpperLimit = RetentionUpperLimit

    @property
    def RetentionLowerLimit(self):
        return self._RetentionLowerLimit

    @RetentionLowerLimit.setter
    def RetentionLowerLimit(self, RetentionLowerLimit):
        self._RetentionLowerLimit = RetentionLowerLimit

    @property
    def TpsLimit(self):
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ScaledTpsLimit(self):
        return self._ScaledTpsLimit

    @ScaledTpsLimit.setter
    def ScaledTpsLimit(self, ScaledTpsLimit):
        self._ScaledTpsLimit = ScaledTpsLimit

    @property
    def MaxMessageDelay(self):
        return self._MaxMessageDelay

    @MaxMessageDelay.setter
    def MaxMessageDelay(self, MaxMessageDelay):
        self._MaxMessageDelay = MaxMessageDelay

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def SendReceiveRatio(self):
        return self._SendReceiveRatio

    @SendReceiveRatio.setter
    def SendReceiveRatio(self, SendReceiveRatio):
        self._SendReceiveRatio = SendReceiveRatio

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def EndpointList(self):
        return self._EndpointList

    @EndpointList.setter
    def EndpointList(self, EndpointList):
        self._EndpointList = EndpointList

    @property
    def TopicQueueNumUpperLimit(self):
        return self._TopicQueueNumUpperLimit

    @TopicQueueNumUpperLimit.setter
    def TopicQueueNumUpperLimit(self, TopicQueueNumUpperLimit):
        self._TopicQueueNumUpperLimit = TopicQueueNumUpperLimit

    @property
    def TopicQueueNumLowerLimit(self):
        return self._TopicQueueNumLowerLimit

    @TopicQueueNumLowerLimit.setter
    def TopicQueueNumLowerLimit(self, TopicQueueNumLowerLimit):
        self._TopicQueueNumLowerLimit = TopicQueueNumLowerLimit

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    """DescribeRoleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    """DescribeRoleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 角色信息列表
        :type Data: list of RoleItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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


class DescribeTopicListRequest(AbstractModel):
    """DescribeTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        


class DescribeTopicListResponse(AbstractModel):
    """DescribeTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Data: 主题列表
        :type Data: list of TopicItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
    """DescribeTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        :param _Filters: 查询条件列表
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._Topic = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

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
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
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
        


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic返回参数结构体

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
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _LastUpdateTime: 最后写入时间，秒为单位
        :type LastUpdateTime: int
        :param _SubscriptionCount: 订阅数量
        :type SubscriptionCount: int
        :param _SubscriptionData: 订阅关系列表
        :type SubscriptionData: list of SubscriptionData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def SubscriptionCount(self):
        return self._SubscriptionCount

    @SubscriptionCount.setter
    def SubscriptionCount(self, SubscriptionCount):
        self._SubscriptionCount = SubscriptionCount

    @property
    def SubscriptionData(self):
        return self._SubscriptionData

    @SubscriptionData.setter
    def SubscriptionData(self, SubscriptionData):
        self._SubscriptionData = SubscriptionData

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class DescribeTopicStatsOpRequest(AbstractModel):
    """DescribeTopicStatsOp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: 主题
        :type Topic: str
        """
        self._Topic = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicStatsOpResponse(AbstractModel):
    """DescribeTopicStatsOp返回参数结构体

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


class Endpoint(AbstractModel):
    """接入点信息

    """

    def __init__(self):
        r"""
        :param _Type: 接入点类型，
VPC，
PUBLIC 公网
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
        """
        self._Type = None
        self._Status = None
        self._PayMode = None
        self._EndpointUrl = None
        self._VpcId = None
        self._SubnetId = None
        self._Bandwidth = None
        self._IpRules = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def EndpointUrl(self):
        return self._EndpointUrl

    @EndpointUrl.setter
    def EndpointUrl(self, EndpointUrl):
        self._EndpointUrl = EndpointUrl

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Bandwidth(self):
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤条件名
        :type Name: str
        :param _Values: 过滤条件的值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
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
        


class InstanceItem(AbstractModel):
    """实例列表页中的实例信息

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
        :param _PayMode: 计费模式，
POSTPAID，按量计费
PREPAID，包年包月
        :type PayMode: str
        :param _ExpiryTime: 到期时间，秒为单位
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaledTpsLimit: int
        :param _MessageRetention: 消息保留时间，小时为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageRetention: int
        :param _MaxMessageDelay: 延迟消息最大时长，小时为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMessageDelay: int
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

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TopicNumLimit(self):
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def GroupNumLimit(self):
        return self._GroupNumLimit

    @GroupNumLimit.setter
    def GroupNumLimit(self, GroupNumLimit):
        self._GroupNumLimit = GroupNumLimit

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ScaledTpsLimit(self):
        return self._ScaledTpsLimit

    @ScaledTpsLimit.setter
    def ScaledTpsLimit(self, ScaledTpsLimit):
        self._ScaledTpsLimit = ScaledTpsLimit

    @property
    def MessageRetention(self):
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def MaxMessageDelay(self):
        return self._MaxMessageDelay

    @MaxMessageDelay.setter
    def MaxMessageDelay(self, MaxMessageDelay):
        self._MaxMessageDelay = MaxMessageDelay


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpRule(AbstractModel):
    """IP规则

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _Allow: 是否允许放行
        :type Allow: bool
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._Ip = None
        self._Allow = None
        self._Remark = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Allow(self):
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def Remark(self):
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
        


class ModifyConsumerGroupRequest(AbstractModel):
    """ModifyConsumerGroup请求参数结构体

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
        """
        self._InstanceId = None
        self._ConsumerGroup = None
        self._ConsumeEnable = None
        self._ConsumeMessageOrderly = None
        self._MaxRetryTimes = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConsumerGroup(self):
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def ConsumeEnable(self):
        return self._ConsumeEnable

    @ConsumeEnable.setter
    def ConsumeEnable(self, ConsumeEnable):
        self._ConsumeEnable = ConsumeEnable

    @property
    def ConsumeMessageOrderly(self):
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly

    @property
    def MaxRetryTimes(self):
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def Remark(self):
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
    """ModifyConsumerGroup返回参数结构体

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


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 实例名称
        :type Name: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _SendReceiveRatio: 消息发送和接收的比例
        :type SendReceiveRatio: float
        :param _SkuCode: 调整实例规格的商品代号
        :type SkuCode: str
        :param _MessageRetention: 消息保留时长，小时为单位
        :type MessageRetention: int
        :param _ScaledTpsEnabled: 是否开启弹性TPS
        :type ScaledTpsEnabled: bool
        """
        self._InstanceId = None
        self._Name = None
        self._Remark = None
        self._SendReceiveRatio = None
        self._SkuCode = None
        self._MessageRetention = None
        self._ScaledTpsEnabled = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SendReceiveRatio(self):
        return self._SendReceiveRatio

    @SendReceiveRatio.setter
    def SendReceiveRatio(self, SendReceiveRatio):
        self._SendReceiveRatio = SendReceiveRatio

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def MessageRetention(self):
        return self._MessageRetention

    @MessageRetention.setter
    def MessageRetention(self, MessageRetention):
        self._MessageRetention = MessageRetention

    @property
    def ScaledTpsEnabled(self):
        return self._ScaledTpsEnabled

    @ScaledTpsEnabled.setter
    def ScaledTpsEnabled(self, ScaledTpsEnabled):
        self._ScaledTpsEnabled = ScaledTpsEnabled


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._SendReceiveRatio = params.get("SendReceiveRatio")
        self._SkuCode = params.get("SkuCode")
        self._MessageRetention = params.get("MessageRetention")
        self._ScaledTpsEnabled = params.get("ScaledTpsEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

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


class ModifyRoleRequest(AbstractModel):
    """ModifyRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Role: 角色名称
        :type Role: str
        :param _PermRead: 是否开启消费
        :type PermRead: bool
        :param _PermWrite: 是否开启生产
        :type PermWrite: bool
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._Role = None
        self._PermRead = None
        self._PermWrite = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def PermRead(self):
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def PermWrite(self):
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Role = params.get("Role")
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
        


class ModifyRoleResponse(AbstractModel):
    """ModifyRole返回参数结构体

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


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _QueueNum: 队列数量
        :type QueueNum: int
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._QueueNum = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def QueueNum(self):
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._QueueNum = params.get("QueueNum")
        self._Remark = params.get("Remark")
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


class RoleItem(AbstractModel):
    """角色信息

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _AccessKey: Access Key
        :type AccessKey: str
        :param _SecretKey: Secret Key
        :type SecretKey: str
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
        self._RoleName = None
        self._AccessKey = None
        self._SecretKey = None
        self._PermRead = None
        self._PermWrite = None
        self._Remark = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def PermRead(self):
        return self._PermRead

    @PermRead.setter
    def PermRead(self, PermRead):
        self._PermRead = PermRead

    @property
    def PermWrite(self):
        return self._PermWrite

    @PermWrite.setter
    def PermWrite(self, PermWrite):
        self._PermWrite = PermWrite

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
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
        


class SubscriptionData(AbstractModel):
    """主题与消费组的订阅关系数据

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
        :param _ConsumeType: 消费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumeType: str
        :param _SubString: 订阅规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SubString: str
        :param _ExpressionType: 过滤类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpressionType: str
        :param _Consistency: 订阅一致性
注意：此字段可能返回 null，表示取不到有效值。
        :type Consistency: int
        :param _ConsumerLag: 消费堆积
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumerLag: int
        :param _LastUpdateTime: 最后消费进度更新时间，秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: int
        :param _MaxRetryTimes: 最大重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRetryTimes: int
        :param _ConsumeMessageOrderly: 是否顺序消费
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsumeMessageOrderly: bool
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

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def TopicQueueNum(self):
        return self._TopicQueueNum

    @TopicQueueNum.setter
    def TopicQueueNum(self, TopicQueueNum):
        self._TopicQueueNum = TopicQueueNum

    @property
    def ConsumerGroup(self):
        return self._ConsumerGroup

    @ConsumerGroup.setter
    def ConsumerGroup(self, ConsumerGroup):
        self._ConsumerGroup = ConsumerGroup

    @property
    def IsOnline(self):
        return self._IsOnline

    @IsOnline.setter
    def IsOnline(self, IsOnline):
        self._IsOnline = IsOnline

    @property
    def ConsumeType(self):
        return self._ConsumeType

    @ConsumeType.setter
    def ConsumeType(self, ConsumeType):
        self._ConsumeType = ConsumeType

    @property
    def SubString(self):
        return self._SubString

    @SubString.setter
    def SubString(self, SubString):
        self._SubString = SubString

    @property
    def ExpressionType(self):
        return self._ExpressionType

    @ExpressionType.setter
    def ExpressionType(self, ExpressionType):
        self._ExpressionType = ExpressionType

    @property
    def Consistency(self):
        return self._Consistency

    @Consistency.setter
    def Consistency(self, Consistency):
        self._Consistency = Consistency

    @property
    def ConsumerLag(self):
        return self._ConsumerLag

    @ConsumerLag.setter
    def ConsumerLag(self, ConsumerLag):
        self._ConsumerLag = ConsumerLag

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def MaxRetryTimes(self):
        return self._MaxRetryTimes

    @MaxRetryTimes.setter
    def MaxRetryTimes(self, MaxRetryTimes):
        self._MaxRetryTimes = MaxRetryTimes

    @property
    def ConsumeMessageOrderly(self):
        return self._ConsumeMessageOrderly

    @ConsumeMessageOrderly.setter
    def ConsumeMessageOrderly(self, ConsumeMessageOrderly):
        self._ConsumeMessageOrderly = ConsumeMessageOrderly


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签数据

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
        


class TagFilter(AbstractModel):
    """标签过滤器

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
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
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
        


class TopicItem(AbstractModel):
    """列表上的主题信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _TopicType: 主题类型
        :type TopicType: str
        :param _QueueNum: 队列数量
        :type QueueNum: int
        :param _Remark: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._TopicType = None
        self._QueueNum = None
        self._Remark = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def QueueNum(self):
        return self._QueueNum

    @QueueNum.setter
    def QueueNum(self, QueueNum):
        self._QueueNum = QueueNum

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._TopicType = params.get("TopicType")
        self._QueueNum = params.get("QueueNum")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """VPC信息

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
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
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
        