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
        :param _StrategyId: 评估项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param _Name: 评估项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Desc: 评估项描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Product: 评估项对应产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param _ProductDesc: 评估项对应产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductDesc: str
        :param _Repair: 评估项优化建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Repair: str
        :param _GroupId: 评估项类别ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param _GroupName: 评估项类别名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Conditions: 评估项风险列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of DescribeStrategiesCondition
        """
        self._StrategyId = None
        self._Name = None
        self._Desc = None
        self._Product = None
        self._ProductDesc = None
        self._Repair = None
        self._GroupId = None
        self._GroupName = None
        self._Conditions = None

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProductDesc(self):
        return self._ProductDesc

    @ProductDesc.setter
    def ProductDesc(self, ProductDesc):
        self._ProductDesc = ProductDesc

    @property
    def Repair(self):
        return self._Repair

    @Repair.setter
    def Repair(self, Repair):
        self._Repair = Repair

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Product = params.get("Product")
        self._ProductDesc = params.get("ProductDesc")
        self._Repair = params.get("Repair")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = DescribeStrategiesCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategiesCondition(AbstractModel):
    """评估项警告条件

    """

    def __init__(self):
        r"""
        :param _ConditionId: 警告条件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionId: int
        :param _Level: 警告级别，2:中风险，3:高风险
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _LevelDesc: 警告级别描述
注意：此字段可能返回 null，表示取不到有效值。
        :type LevelDesc: str
        :param _Desc: 警告条件描述
        :type Desc: str
        """
        self._ConditionId = None
        self._Level = None
        self._LevelDesc = None
        self._Desc = None

    @property
    def ConditionId(self):
        return self._ConditionId

    @ConditionId.setter
    def ConditionId(self, ConditionId):
        self._ConditionId = ConditionId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def LevelDesc(self):
        return self._LevelDesc

    @LevelDesc.setter
    def LevelDesc(self, LevelDesc):
        self._LevelDesc = LevelDesc

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ConditionId = params.get("ConditionId")
        self._Level = params.get("Level")
        self._LevelDesc = params.get("LevelDesc")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
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
        :param _Strategies: 评估项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Strategies: list of DescribeStrategie
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Strategies = None
        self._RequestId = None

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = DescribeStrategie()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskStrategyRisksRequest(AbstractModel):
    """DescribeTaskStrategyRisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyId: 评估项ID
        :type StrategyId: int
        :param _Limit: 返回数量,默认值为100,最大值为200
        :type Limit: int
        :param _Offset: 偏移量,默认0
        :type Offset: int
        :param _Env: 环境
        :type Env: str
        :param _TaskType: 任务类型
        :type TaskType: str
        """
        self._StrategyId = None
        self._Limit = None
        self._Offset = None
        self._Env = None
        self._TaskType = None

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

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
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Env = params.get("Env")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStrategyRisksResponse(AbstractModel):
    """DescribeTaskStrategyRisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskFieldsDesc: 根据此配置，匹配风险实例列表（Risks）对应字段，例如:
{"Response":{"RequestId":"111","RiskFieldsDesc":[{"Field":"InstanceId","FieldName":"ID","FieldType":"string","FieldDict":{}},{"Field":"InstanceName","FieldName":"名称","FieldType":"string","FieldDict":{}},{"Field":"InstanceState","FieldName":"状态","FieldType":"string","FieldDict":{"LAUNCH_FAILED":"创建失败","PENDING":"创建中","REBOOTING":"重启中","RUNNING":"运行中","SHUTDOWN":"停止待销毁","STARTING":"开机中","STOPPED":"关机","STOPPING":"关机中","TERMINATING":"销毁中"}},{"Field":"Zone","FieldName":"可用区","FieldType":"string","FieldDict":{}},{"Field":"PrivateIPAddresses","FieldName":"IP地址(内)","FieldType":"stringSlice","FieldDict":{}},{"Field":"PublicIPAddresses","FieldName":"IP地址(公)","FieldType":"stringSlice","FieldDict":{}},{"Field":"Region","FieldName":"地域","FieldType":"string","FieldDict":{}},{"Field":"Tags","FieldName":"标签","FieldType":"tags","FieldDict":{}}],"RiskTotalCount":3,"Risks":"[{\"InstanceId\":\"ins-xxx1\",\"InstanceName\":\"xxx1\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.2\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"},{\"InstanceId\":\"ins-xxx2\",\"InstanceName\":\"xxx2\",\"InstanceState\":\"RUNNING\",\"PrivateIPAddresses\":[\"1.17.64.11\"],\"PublicIPAddresses\":null,\"Region\":\"ap-shanghai\",\"Tags\":null,\"Zone\":\"ap-shanghai-2\"}]","StrategyId":9}}
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskFieldsDesc: list of RiskFieldsDesc
        :param _StrategyId: 评估项ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param _RiskTotalCount: 风险实例个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskTotalCount: int
        :param _Risks: 风险实例详情列表，需要json decode
注意：此字段可能返回 null，表示取不到有效值。
        :type Risks: str
        :param _ResourceCount: 巡检资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RiskFieldsDesc = None
        self._StrategyId = None
        self._RiskTotalCount = None
        self._Risks = None
        self._ResourceCount = None
        self._RequestId = None

    @property
    def RiskFieldsDesc(self):
        return self._RiskFieldsDesc

    @RiskFieldsDesc.setter
    def RiskFieldsDesc(self, RiskFieldsDesc):
        self._RiskFieldsDesc = RiskFieldsDesc

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def RiskTotalCount(self):
        return self._RiskTotalCount

    @RiskTotalCount.setter
    def RiskTotalCount(self, RiskTotalCount):
        self._RiskTotalCount = RiskTotalCount

    @property
    def Risks(self):
        return self._Risks

    @Risks.setter
    def Risks(self, Risks):
        self._Risks = Risks

    @property
    def ResourceCount(self):
        return self._ResourceCount

    @ResourceCount.setter
    def ResourceCount(self, ResourceCount):
        self._ResourceCount = ResourceCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RiskFieldsDesc") is not None:
            self._RiskFieldsDesc = []
            for item in params.get("RiskFieldsDesc"):
                obj = RiskFieldsDesc()
                obj._deserialize(item)
                self._RiskFieldsDesc.append(obj)
        self._StrategyId = params.get("StrategyId")
        self._RiskTotalCount = params.get("RiskTotalCount")
        self._Risks = params.get("Risks")
        self._ResourceCount = params.get("ResourceCount")
        self._RequestId = params.get("RequestId")


class KeyValue(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Key: 键名
        :type Key: str
        :param _Value: 键名对应值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class RiskFieldsDesc(AbstractModel):
    """风险实例字段描述

    """

    def __init__(self):
        r"""
        :param _Field: 字段ID
        :type Field: str
        :param _FieldName: 字段名称
        :type FieldName: str
        :param _FieldType: 字段类型, 
string: 字符串类型，例如"aa"
int: 整形，例如 111
stringSlice : 字符串数组类型，例如["a", "b"]
tags: 标签类型, 例如: [{"Key":"kkk","Value":"vvv"},{"Key":"kkk2","Value":"vvv2"}]
        :type FieldType: str
        :param _FieldDict: 字段值对应字典
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldDict: list of KeyValue
        """
        self._Field = None
        self._FieldName = None
        self._FieldType = None
        self._FieldDict = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def FieldType(self):
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def FieldDict(self):
        return self._FieldDict

    @FieldDict.setter
    def FieldDict(self, FieldDict):
        self._FieldDict = FieldDict


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._FieldName = params.get("FieldName")
        self._FieldType = params.get("FieldType")
        if params.get("FieldDict") is not None:
            self._FieldDict = []
            for item in params.get("FieldDict"):
                obj = KeyValue()
                obj._deserialize(item)
                self._FieldDict.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        