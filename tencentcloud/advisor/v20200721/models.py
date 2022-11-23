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


class DescribeStrategie(AbstractModel):
    """评估项信息

    """

    def __init__(self):
        r"""
        :param StrategyId: 评估项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param Name: 评估项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Desc: 评估项描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Product: 评估项对应产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param ProductDesc: 评估项对应产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductDesc: str
        :param Repair: 评估项优化建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Repair: str
        :param GroupId: 评估项类别ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param GroupName: 评估项类别名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param Conditions: 评估项风险列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of DescribeStrategiesCondition
        """
        self.StrategyId = None
        self.Name = None
        self.Desc = None
        self.Product = None
        self.ProductDesc = None
        self.Repair = None
        self.GroupId = None
        self.GroupName = None
        self.Conditions = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Product = params.get("Product")
        self.ProductDesc = params.get("ProductDesc")
        self.Repair = params.get("Repair")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = DescribeStrategiesCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategiesCondition(AbstractModel):
    """评估项警告条件

    """

    def __init__(self):
        r"""
        :param ConditionId: 警告条件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionId: int
        :param Level: 警告级别，2:中风险，3:高风险
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param LevelDesc: 警告级别描述
注意：此字段可能返回 null，表示取不到有效值。
        :type LevelDesc: str
        :param Desc: 警告条件描述
        :type Desc: str
        """
        self.ConditionId = None
        self.Level = None
        self.LevelDesc = None
        self.Desc = None


    def _deserialize(self, params):
        self.ConditionId = params.get("ConditionId")
        self.Level = params.get("Level")
        self.LevelDesc = params.get("LevelDesc")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategiesRequest(AbstractModel):
    """DescribeStrategies请求参数结构体

    """


class DescribeStrategiesResponse(AbstractModel):
    """DescribeStrategies返回参数结构体

    """

    def __init__(self):
        r"""
        :param Strategies: 评估项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Strategies: list of DescribeStrategie
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Strategies = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Strategies") is not None:
            self.Strategies = []
            for item in params.get("Strategies"):
                obj = DescribeStrategie()
                obj._deserialize(item)
                self.Strategies.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskStrategyRisksRequest(AbstractModel):
    """DescribeTaskStrategyRisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param StrategyId: 评估项ID
        :type StrategyId: int
        :param Limit: 返回数量,默认值为100,最大值为200
        :type Limit: int
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Env: 环境
        :type Env: str
        :param TaskType: 任务类型
        :type TaskType: str
        """
        self.StrategyId = None
        self.Limit = None
        self.Offset = None
        self.Env = None
        self.TaskType = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Env = params.get("Env")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStrategyRisksResponse(AbstractModel):
    """DescribeTaskStrategyRisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RiskFieldsDesc: 根据此配置，匹配风险实例列表（Risks）对应字段，例如:
{"Response":{"RequestId":"111","RiskFieldsDesc":[{"Field":"InstanceId","FieldName":"ID","FieldType":"string","FieldDict":{}},{"Field":"InstanceName","FieldName":"名称","FieldType":"string","FieldDict":{}},{"Field":"InstanceState","FieldName":"状态","FieldType":"string","FieldDict":{"LAUNCH_FAILED":"创建失败","PENDING":"创建中","REBOOTING":"重启中","RUNNING":"运行中","SHUTDOWN":"停止待销毁","STARTING":"开机中","STOPPED":"关机","STOPPING":"关机中","TERMINATING":"销毁中"}},{"Field":"Zone","FieldName":"可用区","FieldType":"string","FieldDict":{}},{"Field":"PrivateIPAddresses","FieldName":"IP地址(内)","FieldType":"stringSlice","FieldDict":{}},{"Field":"PublicIPAddresses","FieldName":"IP地址(公)","FieldType":"stringSlice","FieldDict":{}},{"Field":"Region","FieldName":"地域","FieldType":"string","FieldDict":{}},{"Field":"Tags","FieldName":"标签","FieldType":"tags","FieldDict":{}}],"RiskTotalCount":3,"Risks":"[{\"InstanceId\":\"ins-xxx1\",\"InstanceName\":\"xxx1\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.2\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"},{\"InstanceId\":\"ins-xxx2\",\"InstanceName\":\"xxx2\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.11\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"}]","StrategyId":9}}
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskFieldsDesc: list of RiskFieldsDesc
        :param StrategyId: 评估项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param RiskTotalCount: 风险实例个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskTotalCount: int
        :param Risks: 风险实例详情列表，需要json decode
注意：此字段可能返回 null，表示取不到有效值。
        :type Risks: str
        :param ResourceCount: 巡检资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RiskFieldsDesc = None
        self.StrategyId = None
        self.RiskTotalCount = None
        self.Risks = None
        self.ResourceCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RiskFieldsDesc") is not None:
            self.RiskFieldsDesc = []
            for item in params.get("RiskFieldsDesc"):
                obj = RiskFieldsDesc()
                obj._deserialize(item)
                self.RiskFieldsDesc.append(obj)
        self.StrategyId = params.get("StrategyId")
        self.RiskTotalCount = params.get("RiskTotalCount")
        self.Risks = params.get("Risks")
        self.ResourceCount = params.get("ResourceCount")
        self.RequestId = params.get("RequestId")


class KeyValue(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param Key: 键名
        :type Key: str
        :param Value: 键名对应值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskFieldsDesc(AbstractModel):
    """风险实例字段描述

    """

    def __init__(self):
        r"""
        :param Field: 字段ID
        :type Field: str
        :param FieldName: 字段名称
        :type FieldName: str
        :param FieldType: 字段类型, 
string: 字符串类型，例如"aa"
int: 整形，例如 111
stringSlice : 字符串数组类型，例如["a", "b"]
tags: 标签类型, 例如: [{"Key":"kkk","Value":"vvv"},{"Key":"kkk2","Value":"vvv2"}]
        :type FieldType: str
        :param FieldDict: 字段值对应字典
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldDict: list of KeyValue
        """
        self.Field = None
        self.FieldName = None
        self.FieldType = None
        self.FieldDict = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.FieldName = params.get("FieldName")
        self.FieldType = params.get("FieldType")
        if params.get("FieldDict") is not None:
            self.FieldDict = []
            for item in params.get("FieldDict"):
                obj = KeyValue()
                obj._deserialize(item)
                self.FieldDict.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        