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


class APIGWParams(AbstractModel):
    """APIGWParams描述

    """

    def __init__(self):
        r"""
        :param Protocol: HTTPS
        :type Protocol: str
        :param Method: POST
        :type Method: str
        """
        self.Protocol = None
        self.Method = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRuleRequest(AbstractModel):
    """CheckRule请求参数结构体

    """


class CheckRuleResponse(AbstractModel):
    """CheckRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckTransformationRequest(AbstractModel):
    """CheckTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param Input: 待处理的json字符串
        :type Input: str
        :param Transformations: 一个转换规则列表
        :type Transformations: list of Transformation
        """
        self.Input = None
        self.Transformations = None


    def _deserialize(self, params):
        self.Input = params.get("Input")
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckTransformationResponse(AbstractModel):
    """CheckTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param Output: 经过Transformations处理之后的数据
        :type Output: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Output = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Output = params.get("Output")
        self.RequestId = params.get("RequestId")


class CkafkaDeliveryParams(AbstractModel):
    """用来描述需要投递到kafka topic的参数

    """

    def __init__(self):
        r"""
        :param TopicName: ckafka topic name
        :type TopicName: str
        :param ResourceDescription: ckafka资源qcs六段式
        :type ResourceDescription: str
        """
        self.TopicName = None
        self.ResourceDescription = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.ResourceDescription = params.get("ResourceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaParams(AbstractModel):
    """Ckafka 连接器参数

    """

    def __init__(self):
        r"""
        :param Offset: kafka offset
        :type Offset: str
        :param TopicName: ckafka  topic
        :type TopicName: str
        """
        self.Offset = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaTargetParams(AbstractModel):
    """用来描述ckafka投递目标

    """

    def __init__(self):
        r"""
        :param TopicName: 要投递到的ckafka topic
        :type TopicName: str
        :param RetryPolicy: 重试策略
        :type RetryPolicy: :class:`tencentcloud.eb.v20210416.models.RetryPolicy`
        """
        self.TopicName = None
        self.RetryPolicy = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        if params.get("RetryPolicy") is not None:
            self.RetryPolicy = RetryPolicy()
            self.RetryPolicy._deserialize(params.get("RetryPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Connection(AbstractModel):
    """Connection信息

    """

    def __init__(self):
        r"""
        :param Status: 状态
        :type Status: str
        :param ModTime: 更新时间
        :type ModTime: str
        :param Enable: 使能开关
        :type Enable: bool
        :param Description: 描述
        :type Description: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param ConnectionId: 连接器ID
        :type ConnectionId: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param ConnectionDescription: 连接器描述
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param ConnectionName: 连接器名称
        :type ConnectionName: str
        :param Type: 类型
        :type Type: str
        """
        self.Status = None
        self.ModTime = None
        self.Enable = None
        self.Description = None
        self.AddTime = None
        self.ConnectionId = None
        self.EventBusId = None
        self.ConnectionDescription = None
        self.ConnectionName = None
        self.Type = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ModTime = params.get("ModTime")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ConnectionId = params.get("ConnectionId")
        self.EventBusId = params.get("EventBusId")
        if params.get("ConnectionDescription") is not None:
            self.ConnectionDescription = ConnectionDescription()
            self.ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self.ConnectionName = params.get("ConnectionName")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionDescription(AbstractModel):
    """ConnectionDescription描述

    """

    def __init__(self):
        r"""
        :param ResourceDescription: 资源qcs六段式，更多参考 [资源六段式](https://cloud.tencent.com/document/product/598/10606)
        :type ResourceDescription: str
        :param APIGWParams: apigw参数
注意：此字段可能返回 null，表示取不到有效值。
        :type APIGWParams: :class:`tencentcloud.eb.v20210416.models.APIGWParams`
        :param CkafkaParams: ckafka参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CkafkaParams: :class:`tencentcloud.eb.v20210416.models.CkafkaParams`
        """
        self.ResourceDescription = None
        self.APIGWParams = None
        self.CkafkaParams = None


    def _deserialize(self, params):
        self.ResourceDescription = params.get("ResourceDescription")
        if params.get("APIGWParams") is not None:
            self.APIGWParams = APIGWParams()
            self.APIGWParams._deserialize(params.get("APIGWParams"))
        if params.get("CkafkaParams") is not None:
            self.CkafkaParams = CkafkaParams()
            self.CkafkaParams._deserialize(params.get("CkafkaParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionRequest(AbstractModel):
    """CreateConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConnectionDescription: 连接器描述
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param ConnectionName: 连接器名称
        :type ConnectionName: str
        :param Description: 描述
        :type Description: str
        :param Enable: 使能开关
        :type Enable: bool
        :param Type: 类型
        :type Type: str
        """
        self.ConnectionDescription = None
        self.EventBusId = None
        self.ConnectionName = None
        self.Description = None
        self.Enable = None
        self.Type = None


    def _deserialize(self, params):
        if params.get("ConnectionDescription") is not None:
            self.ConnectionDescription = ConnectionDescription()
            self.ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self.EventBusId = params.get("EventBusId")
        self.ConnectionName = params.get("ConnectionName")
        self.Description = params.get("Description")
        self.Enable = params.get("Enable")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionResponse(AbstractModel):
    """CreateConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param ConnectionId: 连接器ID
        :type ConnectionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConnectionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConnectionId = params.get("ConnectionId")
        self.RequestId = params.get("RequestId")


class CreateEventBusRequest(AbstractModel):
    """CreateEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type EventBusName: str
        :param Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        """
        self.EventBusName = None
        self.Description = None


    def _deserialize(self, params):
        self.EventBusName = params.get("EventBusName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEventBusResponse(AbstractModel):
    """CreateEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBusId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventPattern: 参考：[事件模式](https://cloud.tencent.com/document/product/1359/56084)
        :type EventPattern: str
        :param EventBusId: 事件集ID。
        :type EventBusId: str
        :param RuleName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type RuleName: str
        :param Enable: 使能开关。
        :type Enable: bool
        :param Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        """
        self.EventPattern = None
        self.EventBusId = None
        self.RuleName = None
        self.Enable = None
        self.Description = None


    def _deserialize(self, params):
        self.EventPattern = params.get("EventPattern")
        self.EventBusId = params.get("EventBusId")
        self.RuleName = params.get("RuleName")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 事件规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateTargetRequest(AbstractModel):
    """CreateTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param Type: 目标类型
        :type Type: str
        :param TargetDescription: 目标描述
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param RuleId: 事件规则ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.Type = None
        self.TargetDescription = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.Type = params.get("Type")
        if params.get("TargetDescription") is not None:
            self.TargetDescription = TargetDescription()
            self.TargetDescription._deserialize(params.get("TargetDescription"))
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetResponse(AbstractModel):
    """CreateTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param TargetId: 目标ID
        :type TargetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TargetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetId = params.get("TargetId")
        self.RequestId = params.get("RequestId")


class CreateTransformationRequest(AbstractModel):
    """CreateTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件总线 id
        :type EventBusId: str
        :param RuleId: 规则id
        :type RuleId: str
        :param Transformations: 一个转换规则列表，当前仅限定一个
        :type Transformations: list of Transformation
        """
        self.EventBusId = None
        self.RuleId = None
        self.Transformations = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTransformationResponse(AbstractModel):
    """CreateTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param TransformationId: 生成的转换器id
        :type TransformationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TransformationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransformationId = params.get("TransformationId")
        self.RequestId = params.get("RequestId")


class DeadLetterConfig(AbstractModel):
    """rule对应的dlq配置

    """

    def __init__(self):
        r"""
        :param DisposeMethod: 支持dlq、丢弃、忽略错误继续传递三种模式, 分别对应: DLQ,DROP,IGNORE_ERROR
        :type DisposeMethod: str
        :param CkafkaDeliveryParams: 设置了DLQ方式后,此选项必填. 错误消息会被投递到对应的kafka topic中
注意：此字段可能返回 null，表示取不到有效值。
        :type CkafkaDeliveryParams: :class:`tencentcloud.eb.v20210416.models.CkafkaDeliveryParams`
        """
        self.DisposeMethod = None
        self.CkafkaDeliveryParams = None


    def _deserialize(self, params):
        self.DisposeMethod = params.get("DisposeMethod")
        if params.get("CkafkaDeliveryParams") is not None:
            self.CkafkaDeliveryParams = CkafkaDeliveryParams()
            self.CkafkaDeliveryParams._deserialize(params.get("CkafkaDeliveryParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionRequest(AbstractModel):
    """DeleteConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConnectionId: 连接器ID
        :type ConnectionId: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        """
        self.ConnectionId = None
        self.EventBusId = None


    def _deserialize(self, params):
        self.ConnectionId = params.get("ConnectionId")
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionResponse(AbstractModel):
    """DeleteConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEventBusRequest(AbstractModel):
    """DeleteEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        """
        self.EventBusId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEventBusResponse(AbstractModel):
    """DeleteEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RuleId: 事件规则ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTargetRequest(AbstractModel):
    """DeleteTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param TargetId: 事件目标ID
        :type TargetId: str
        :param RuleId: 事件规则ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.TargetId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.TargetId = params.get("TargetId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetResponse(AbstractModel):
    """DeleteTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTransformationRequest(AbstractModel):
    """DeleteTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param TransformationId: 转换器id
        :type TransformationId: str
        """
        self.EventBusId = None
        self.RuleId = None
        self.TransformationId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTransformationResponse(AbstractModel):
    """DeleteTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ESTargetParams(AbstractModel):
    """描述Es规则目标

    """

    def __init__(self):
        r"""
        :param NetMode: 网络连接类型
        :type NetMode: str
        :param IndexPrefix: 索引前缀
        :type IndexPrefix: str
        :param RotationInterval: es日志轮换粒度
        :type RotationInterval: str
        :param OutputMode: DTS事件配置
        :type OutputMode: str
        :param IndexSuffixMode: DTS索引配置
        :type IndexSuffixMode: str
        :param IndexTemplateType: es模版类型
        :type IndexTemplateType: str
        """
        self.NetMode = None
        self.IndexPrefix = None
        self.RotationInterval = None
        self.OutputMode = None
        self.IndexSuffixMode = None
        self.IndexTemplateType = None


    def _deserialize(self, params):
        self.NetMode = params.get("NetMode")
        self.IndexPrefix = params.get("IndexPrefix")
        self.RotationInterval = params.get("RotationInterval")
        self.OutputMode = params.get("OutputMode")
        self.IndexSuffixMode = params.get("IndexSuffixMode")
        self.IndexTemplateType = params.get("IndexTemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtlFilter(AbstractModel):
    """描述如何过滤数据

    """

    def __init__(self):
        r"""
        :param Filter: 语法Rule规则保持一致
        :type Filter: str
        """
        self.Filter = None


    def _deserialize(self, params):
        self.Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Event(AbstractModel):
    """eb event信息

    """

    def __init__(self):
        r"""
        :param Source: 事件源的信息,新产品上报必须符合EB的规范
        :type Source: str
        :param Data: 事件数据，内容由创建事件的系统来控制，当前datacontenttype仅支持application/json;charset=utf-8，所以该字段是json字符串
        :type Data: str
        :param Type: 事件类型，可自定义，选填。云服务默认写 COS:Created:PostObject，用“：”分割类型字段
        :type Type: str
        :param Subject: 事件来源详细描述，可自定义，选填。云服务默认为标准qcs资源表示语法：qcs::dts:ap-guangzhou:appid/uin:xxx
        :type Subject: str
        :param Time: 事件发生的毫秒时间戳，
time.Now().UnixNano()/1e6
        :type Time: int
        """
        self.Source = None
        self.Data = None
        self.Type = None
        self.Subject = None
        self.Time = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Data = params.get("Data")
        self.Type = params.get("Type")
        self.Subject = params.get("Subject")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventBus(AbstractModel):
    """事件集信息

    """

    def __init__(self):
        r"""
        :param ModTime: 更新时间
        :type ModTime: str
        :param Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param EventBusName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type EventBusName: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param Type: 事件集类型
        :type Type: str
        """
        self.ModTime = None
        self.Description = None
        self.AddTime = None
        self.EventBusName = None
        self.EventBusId = None
        self.Type = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.EventBusName = params.get("EventBusName")
        self.EventBusId = params.get("EventBusId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Extraction(AbstractModel):
    """描述如何提取数据

    """

    def __init__(self):
        r"""
        :param ExtractionInputPath: JsonPath, 不指定则使用默认值$.
        :type ExtractionInputPath: str
        :param Format: 取值: TEXT/JSON
        :type Format: str
        :param TextParams: 仅在Text需要传递
注意：此字段可能返回 null，表示取不到有效值。
        :type TextParams: :class:`tencentcloud.eb.v20210416.models.TextParams`
        """
        self.ExtractionInputPath = None
        self.Format = None
        self.TextParams = None


    def _deserialize(self, params):
        self.ExtractionInputPath = params.get("ExtractionInputPath")
        self.Format = params.get("Format")
        if params.get("TextParams") is not None:
            self.TextParams = TextParams()
            self.TextParams._deserialize(params.get("TextParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    * 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    * 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param Name: 过滤键的名称。
        :type Name: str
        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusRequest(AbstractModel):
    """GetEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        """
        self.EventBusId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusResponse(AbstractModel):
    """GetEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModTime: 更新时间
        :type ModTime: str
        :param Description: 事件集描述
        :type Description: str
        :param ClsTopicId: 日志主题ID
        :type ClsTopicId: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param ClsLogsetId: 日志集ID
        :type ClsLogsetId: str
        :param EventBusName: 事件集名称
        :type EventBusName: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param Type: （已废弃）事件集类型
        :type Type: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModTime = None
        self.Description = None
        self.ClsTopicId = None
        self.AddTime = None
        self.ClsLogsetId = None
        self.EventBusName = None
        self.EventBusId = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Description = params.get("Description")
        self.ClsTopicId = params.get("ClsTopicId")
        self.AddTime = params.get("AddTime")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.EventBusName = params.get("EventBusName")
        self.EventBusId = params.get("EventBusId")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class GetRuleRequest(AbstractModel):
    """GetRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RuleId: 事件规则ID
        :type RuleId: str
        """
        self.EventBusId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuleResponse(AbstractModel):
    """GetRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集id
        :type EventBusId: str
        :param RuleId: 事件规则id
        :type RuleId: str
        :param RuleName: 事件规则名称
        :type RuleName: str
        :param Status: 事件规则状态
        :type Status: str
        :param Enable: 使能开关
        :type Enable: bool
        :param Description: 事件规则描述
        :type Description: str
        :param EventPattern: 事件模式
        :type EventPattern: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param ModTime: 更新时间
        :type ModTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBusId = None
        self.RuleId = None
        self.RuleName = None
        self.Status = None
        self.Enable = None
        self.Description = None
        self.EventPattern = None
        self.AddTime = None
        self.ModTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.EventPattern = params.get("EventPattern")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        self.RequestId = params.get("RequestId")


class GetTransformationRequest(AbstractModel):
    """GetTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param TransformationId: 转换器id
        :type TransformationId: str
        """
        self.EventBusId = None
        self.RuleId = None
        self.TransformationId = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTransformationResponse(AbstractModel):
    """GetTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param Transformations: 转换规则列表
        :type Transformations: list of Transformation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Transformations = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        self.RequestId = params.get("RequestId")


class ListConnectionsRequest(AbstractModel):
    """ListConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param OrderBy: 根据哪个字段进行返回结果排序，目前支持如下以下字段：AddTime, ModTime
        :type OrderBy: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.EventBusId = None
        self.OrderBy = None
        self.Limit = None
        self.Order = None
        self.Offset = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConnectionsResponse(AbstractModel):
    """ListConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param Connections: 连接器信息
        :type Connections: list of Connection
        :param TotalCount: 连接器总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Connections = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Connections") is not None:
            self.Connections = []
            for item in params.get("Connections"):
                obj = Connection()
                obj._deserialize(item)
                self.Connections.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListEventBusesRequest(AbstractModel):
    """ListEventBuses请求参数结构体

    """

    def __init__(self):
        r"""
        :param OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime（创建时间）, ModTime（修改时间）
        :type OrderBy: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC（升序） 和 DESC（降序）
        :type Order: str
        :param Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param Offset: 分页偏移量，默认为0。
        :type Offset: int
        """
        self.OrderBy = None
        self.Limit = None
        self.Order = None
        self.Filters = None
        self.Offset = None


    def _deserialize(self, params):
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventBusesResponse(AbstractModel):
    """ListEventBuses返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventBuses: 事件集信息
        :type EventBuses: list of EventBus
        :param TotalCount: 事件集总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventBuses = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventBuses") is not None:
            self.EventBuses = []
            for item in params.get("EventBuses"):
                obj = EventBus()
                obj._deserialize(item)
                self.EventBuses.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListRulesRequest(AbstractModel):
    """ListRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime（创建时间）, ModTime（修改时间）
        :type OrderBy: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 分页偏移量，默认为0。
        :type Offset: int
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC（升序） 和 DESC（降序）
        :type Order: str
        """
        self.EventBusId = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRulesResponse(AbstractModel):
    """ListRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Rules: 事件规则信息
        :type Rules: list of Rule
        :param TotalCount: 事件规则总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListTargetsRequest(AbstractModel):
    """ListTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime（创建时间）, ModTime（修改时间）
        :type OrderBy: str
        :param RuleId: 事件规则ID
        :type RuleId: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 分页偏移量，默认为0。
        :type Offset: int
        :param Order: 以升序还是降序的方式返回结果，可选值 ASC（升序） 和 DESC（降序）
        :type Order: str
        """
        self.EventBusId = None
        self.OrderBy = None
        self.RuleId = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.OrderBy = params.get("OrderBy")
        self.RuleId = params.get("RuleId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTargetsResponse(AbstractModel):
    """ListTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 目标总数
        :type TotalCount: int
        :param Targets: 目标信息
        :type Targets: list of Target
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Targets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")


class OutputStructParam(AbstractModel):
    """Transform输出参数

    """

    def __init__(self):
        r"""
        :param Key: 对应输出json中的key
        :type Key: str
        :param Value: 可以填json-path也可以支持常量或者内置关键字date类型
        :type Value: str
        :param ValueType: value的数据类型, 可选值: STRING, NUMBER,BOOLEAN,NULL,SYS_VARIABLE,JSONPATH
        :type ValueType: str
        """
        self.Key = None
        self.Value = None
        self.ValueType = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishEventRequest(AbstractModel):
    """PublishEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventList: 事件列表
        :type EventList: list of Event
        :param EventBusId: 事件集ID
        :type EventBusId: str
        """
        self.EventList = None
        self.EventBusId = None


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = Event()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishEventResponse(AbstractModel):
    """PublishEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutEventsRequest(AbstractModel):
    """PutEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventList: 事件列表
        :type EventList: list of Event
        :param EventBusId: 事件集ID
        :type EventBusId: str
        """
        self.EventList = None
        self.EventBusId = None


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = Event()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutEventsResponse(AbstractModel):
    """PutEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RetryPolicy(AbstractModel):
    """用来描述一个ckafka投递目标的重试策略

    """

    def __init__(self):
        r"""
        :param RetryInterval: 重试间隔 单位:秒
        :type RetryInterval: int
        :param MaxRetryAttempts: 最大重试次数
        :type MaxRetryAttempts: int
        """
        self.RetryInterval = None
        self.MaxRetryAttempts = None


    def _deserialize(self, params):
        self.RetryInterval = params.get("RetryInterval")
        self.MaxRetryAttempts = params.get("MaxRetryAttempts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """规则信息

    """

    def __init__(self):
        r"""
        :param Status: 状态
        :type Status: str
        :param ModTime: 修改时间
        :type ModTime: str
        :param Enable: 使能开关
        :type Enable: bool
        :param Description: 描述
        :type Description: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param AddTime: 创建时间
        :type AddTime: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RuleName: 规则名称
        :type RuleName: str
        :param Targets: Target 简要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of TargetBrief
        :param DeadLetterConfig: rule设置的dlq规则. 可能为null
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterConfig: :class:`tencentcloud.eb.v20210416.models.DeadLetterConfig`
        """
        self.Status = None
        self.ModTime = None
        self.Enable = None
        self.Description = None
        self.RuleId = None
        self.AddTime = None
        self.EventBusId = None
        self.RuleName = None
        self.Targets = None
        self.DeadLetterConfig = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ModTime = params.get("ModTime")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.RuleId = params.get("RuleId")
        self.AddTime = params.get("AddTime")
        self.EventBusId = params.get("EventBusId")
        self.RuleName = params.get("RuleName")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetBrief()
                obj._deserialize(item)
                self.Targets.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SCFParams(AbstractModel):
    """云函数参数

    """

    def __init__(self):
        r"""
        :param BatchTimeout: 批量投递最长等待时间
        :type BatchTimeout: int
        :param BatchEventCount: 批量投递最大事件条数
        :type BatchEventCount: int
        :param EnableBatchDelivery: 开启批量投递使能
        :type EnableBatchDelivery: bool
        """
        self.BatchTimeout = None
        self.BatchEventCount = None
        self.EnableBatchDelivery = None


    def _deserialize(self, params):
        self.BatchTimeout = params.get("BatchTimeout")
        self.BatchEventCount = params.get("BatchEventCount")
        self.EnableBatchDelivery = params.get("EnableBatchDelivery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Target(AbstractModel):
    """Target信息

    """

    def __init__(self):
        r"""
        :param Type: 目标类型
        :type Type: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param TargetId: 目标ID
        :type TargetId: str
        :param TargetDescription: 目标描述
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param RuleId: 事件规则ID
        :type RuleId: str
        :param EnableBatchDelivery: 开启批量投递使能
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableBatchDelivery: bool
        :param BatchTimeout: 批量投递最长等待时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchTimeout: int
        :param BatchEventCount: 批量投递最大事件条数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchEventCount: int
        """
        self.Type = None
        self.EventBusId = None
        self.TargetId = None
        self.TargetDescription = None
        self.RuleId = None
        self.EnableBatchDelivery = None
        self.BatchTimeout = None
        self.BatchEventCount = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.EventBusId = params.get("EventBusId")
        self.TargetId = params.get("TargetId")
        if params.get("TargetDescription") is not None:
            self.TargetDescription = TargetDescription()
            self.TargetDescription._deserialize(params.get("TargetDescription"))
        self.RuleId = params.get("RuleId")
        self.EnableBatchDelivery = params.get("EnableBatchDelivery")
        self.BatchTimeout = params.get("BatchTimeout")
        self.BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetBrief(AbstractModel):
    """目标简要信息

    """

    def __init__(self):
        r"""
        :param TargetId: 目标ID
        :type TargetId: str
        :param Type: 目标类型
        :type Type: str
        """
        self.TargetId = None
        self.Type = None


    def _deserialize(self, params):
        self.TargetId = params.get("TargetId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetDescription(AbstractModel):
    """TargetDescription描述

    """

    def __init__(self):
        r"""
        :param ResourceDescription: QCS资源六段式，更多参考 [资源六段式](https://cloud.tencent.com/document/product/598/10606)
        :type ResourceDescription: str
        :param SCFParams: 云函数参数
        :type SCFParams: :class:`tencentcloud.eb.v20210416.models.SCFParams`
        :param CkafkaTargetParams: Ckafka参数
        :type CkafkaTargetParams: :class:`tencentcloud.eb.v20210416.models.CkafkaTargetParams`
        :param ESTargetParams: ElasticSearch参数
        :type ESTargetParams: :class:`tencentcloud.eb.v20210416.models.ESTargetParams`
        """
        self.ResourceDescription = None
        self.SCFParams = None
        self.CkafkaTargetParams = None
        self.ESTargetParams = None


    def _deserialize(self, params):
        self.ResourceDescription = params.get("ResourceDescription")
        if params.get("SCFParams") is not None:
            self.SCFParams = SCFParams()
            self.SCFParams._deserialize(params.get("SCFParams"))
        if params.get("CkafkaTargetParams") is not None:
            self.CkafkaTargetParams = CkafkaTargetParams()
            self.CkafkaTargetParams._deserialize(params.get("CkafkaTargetParams"))
        if params.get("ESTargetParams") is not None:
            self.ESTargetParams = ESTargetParams()
            self.ESTargetParams._deserialize(params.get("ESTargetParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextParams(AbstractModel):
    """描述如何切分数据

    """

    def __init__(self):
        r"""
        :param Separator: 逗号、| 、制表符、空格、换行符、%、#，限制长度为 1。
注意：此字段可能返回 null，表示取不到有效值。
        :type Separator: str
        :param Regex: 填写正则表达式：长度128
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: str
        """
        self.Separator = None
        self.Regex = None


    def _deserialize(self, params):
        self.Separator = params.get("Separator")
        self.Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transform(AbstractModel):
    """描述如何数据转换

    """

    def __init__(self):
        r"""
        :param OutputStructs: 描述如何数据转换
        :type OutputStructs: list of OutputStructParam
        """
        self.OutputStructs = None


    def _deserialize(self, params):
        if params.get("OutputStructs") is not None:
            self.OutputStructs = []
            for item in params.get("OutputStructs"):
                obj = OutputStructParam()
                obj._deserialize(item)
                self.OutputStructs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transformation(AbstractModel):
    """一个转换器

    """

    def __init__(self):
        r"""
        :param Extraction: 描述如何提取数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Extraction: :class:`tencentcloud.eb.v20210416.models.Extraction`
        :param EtlFilter: 描述如何过滤数据
注意：此字段可能返回 null，表示取不到有效值。
        :type EtlFilter: :class:`tencentcloud.eb.v20210416.models.EtlFilter`
        :param Transform: 描述如何数据转换
注意：此字段可能返回 null，表示取不到有效值。
        :type Transform: :class:`tencentcloud.eb.v20210416.models.Transform`
        """
        self.Extraction = None
        self.EtlFilter = None
        self.Transform = None


    def _deserialize(self, params):
        if params.get("Extraction") is not None:
            self.Extraction = Extraction()
            self.Extraction._deserialize(params.get("Extraction"))
        if params.get("EtlFilter") is not None:
            self.EtlFilter = EtlFilter()
            self.EtlFilter._deserialize(params.get("EtlFilter"))
        if params.get("Transform") is not None:
            self.Transform = Transform()
            self.Transform._deserialize(params.get("Transform"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionRequest(AbstractModel):
    """UpdateConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param ConnectionId: 连接器ID
        :type ConnectionId: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param Enable: 使能开关
        :type Enable: bool
        :param Description: 描述
        :type Description: str
        :param ConnectionName: 连接器名称
        :type ConnectionName: str
        """
        self.ConnectionId = None
        self.EventBusId = None
        self.Enable = None
        self.Description = None
        self.ConnectionName = None


    def _deserialize(self, params):
        self.ConnectionId = params.get("ConnectionId")
        self.EventBusId = params.get("EventBusId")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.ConnectionName = params.get("ConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionResponse(AbstractModel):
    """UpdateConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateEventBusRequest(AbstractModel):
    """UpdateEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        :param EventBusName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type EventBusName: str
        """
        self.EventBusId = None
        self.Description = None
        self.EventBusName = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.Description = params.get("Description")
        self.EventBusName = params.get("EventBusName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEventBusResponse(AbstractModel):
    """UpdateEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRuleRequest(AbstractModel):
    """UpdateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 事件规则ID
        :type RuleId: str
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param Enable: 使能开关。
        :type Enable: bool
        :param Description: 规则描述，不限字符类型，200字符描述以内。
        :type Description: str
        :param RuleName: 事件规则名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type RuleName: str
        """
        self.RuleId = None
        self.EventBusId = None
        self.Enable = None
        self.Description = None
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.EventBusId = params.get("EventBusId")
        self.Enable = params.get("Enable")
        self.Description = params.get("Description")
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuleResponse(AbstractModel):
    """UpdateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateTargetRequest(AbstractModel):
    """UpdateTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RuleId: 事件规则ID
        :type RuleId: str
        :param TargetId: 事件目标ID
        :type TargetId: str
        :param EnableBatchDelivery: 开启批量投递使能
        :type EnableBatchDelivery: bool
        :param BatchTimeout: 批量投递最长等待时间
        :type BatchTimeout: int
        :param BatchEventCount: 批量投递最大事件条数
        :type BatchEventCount: int
        """
        self.EventBusId = None
        self.RuleId = None
        self.TargetId = None
        self.EnableBatchDelivery = None
        self.BatchTimeout = None
        self.BatchEventCount = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TargetId = params.get("TargetId")
        self.EnableBatchDelivery = params.get("EnableBatchDelivery")
        self.BatchTimeout = params.get("BatchTimeout")
        self.BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTargetResponse(AbstractModel):
    """UpdateTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateTransformationRequest(AbstractModel):
    """UpdateTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventBusId: 事件集ID
        :type EventBusId: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param TransformationId: 转换器id
        :type TransformationId: str
        :param Transformations: 一个转换规则列表，当前仅限定一个
        :type Transformations: list of Transformation
        """
        self.EventBusId = None
        self.RuleId = None
        self.TransformationId = None
        self.Transformations = None


    def _deserialize(self, params):
        self.EventBusId = params.get("EventBusId")
        self.RuleId = params.get("RuleId")
        self.TransformationId = params.get("TransformationId")
        if params.get("Transformations") is not None:
            self.Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self.Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTransformationResponse(AbstractModel):
    """UpdateTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")