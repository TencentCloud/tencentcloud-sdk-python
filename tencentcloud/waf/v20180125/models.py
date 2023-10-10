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


class AccessFullTextInfo(AbstractModel):
    """DescribeAccessIndex

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type CaseSensitive: bool
        :param _Tokenizer: 全文索引的分词符，字符串中每个字符代表一个分词符
注意：此字段可能返回 null，表示取不到有效值。
        :type Tokenizer: str
        :param _ContainZH: 是否包含中文
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self._CaseSensitive = None
        self._Tokenizer = None
        self._ContainZH = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def Tokenizer(self):
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def ContainZH(self):
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        self._Tokenizer = params.get("Tokenizer")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessHistogramItem(AbstractModel):
    """用于接口DescribeAccessHistogram 的出参

    """

    def __init__(self):
        r"""
        :param _BTime: 时间，单位ms
        :type BTime: int
        :param _Count: 日志条数
        :type Count: int
        """
        self._BTime = None
        self._Count = None

    @property
    def BTime(self):
        return self._BTime

    @BTime.setter
    def BTime(self, BTime):
        self._BTime = BTime

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._BTime = params.get("BTime")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessKeyValueInfo(AbstractModel):
    """用于 DescribeAccessIndex 的出参

    """

    def __init__(self):
        r"""
        :param _Key: 需要配置键值或者元字段索引的字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 字段的索引描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.waf.v20180125.models.AccessValueInfo`
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
        if params.get("Value") is not None:
            self._Value = AccessValueInfo()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessLogInfo(AbstractModel):
    """单条日志数据描述

    """

    def __init__(self):
        r"""
        :param _Time: 日志时间，单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param _TopicId: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _TopicName: 日志主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param _Source: 日志来源IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _FileName: 日志文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _PkgId: 日志上报请求包的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param _PkgLogId: 请求包内日志的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgLogId: str
        :param _LogJson: 日志内容的Json序列化字符串
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogJson: str
        """
        self._Time = None
        self._TopicId = None
        self._TopicName = None
        self._Source = None
        self._FileName = None
        self._PkgId = None
        self._PkgLogId = None
        self._LogJson = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def LogJson(self):
        return self._LogJson

    @LogJson.setter
    def LogJson(self, LogJson):
        self._LogJson = LogJson


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Source = params.get("Source")
        self._FileName = params.get("FileName")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._LogJson = params.get("LogJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessLogItem(AbstractModel):
    """日志KeyValue对

    """

    def __init__(self):
        r"""
        :param _Key: 日记Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 日志Value
注意：此字段可能返回 null，表示取不到有效值。
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
        


class AccessLogItems(AbstractModel):
    """日志KeyValue对数组，用于搜索访问日志

    """

    def __init__(self):
        r"""
        :param _Data: 分析结果返回的KV数据对
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of AccessLogItem
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AccessLogItem()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRuleInfo(AbstractModel):
    """DescribeAccessIndex接口的出参数

    """

    def __init__(self):
        r"""
        :param _FullText: 全文索引配置
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type FullText: :class:`tencentcloud.waf.v20180125.models.AccessFullTextInfo`
        :param _KeyValue: 键值索引配置
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValue: :class:`tencentcloud.waf.v20180125.models.AccessRuleKeyValueInfo`
        :param _Tag: 元字段索引配置
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: :class:`tencentcloud.waf.v20180125.models.AccessRuleTagInfo`
        """
        self._FullText = None
        self._KeyValue = None
        self._Tag = None

    @property
    def FullText(self):
        return self._FullText

    @FullText.setter
    def FullText(self, FullText):
        self._FullText = FullText

    @property
    def KeyValue(self):
        return self._KeyValue

    @KeyValue.setter
    def KeyValue(self, KeyValue):
        self._KeyValue = KeyValue

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        if params.get("FullText") is not None:
            self._FullText = AccessFullTextInfo()
            self._FullText._deserialize(params.get("FullText"))
        if params.get("KeyValue") is not None:
            self._KeyValue = AccessRuleKeyValueInfo()
            self._KeyValue._deserialize(params.get("KeyValue"))
        if params.get("Tag") is not None:
            self._Tag = AccessRuleTagInfo()
            self._Tag._deserialize(params.get("Tag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRuleKeyValueInfo(AbstractModel):
    """DescribeAccessIndex接口的出参

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type CaseSensitive: bool
        :param _KeyValues: 需要建立索引的键值对信息；最大只能配置100个键值对
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValues: list of AccessKeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = AccessKeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRuleTagInfo(AbstractModel):
    """DescribeAccessIndex接口的出参

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 是否大小写敏感
注意：此字段可能返回 null，表示取不到有效值。
        :type CaseSensitive: bool
        :param _KeyValues: 标签索引配置中的字段信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyValues: list of AccessKeyValueInfo
        """
        self._CaseSensitive = None
        self._KeyValues = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def KeyValues(self):
        return self._KeyValues

    @KeyValues.setter
    def KeyValues(self, KeyValues):
        self._KeyValues = KeyValues


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        if params.get("KeyValues") is not None:
            self._KeyValues = []
            for item in params.get("KeyValues"):
                obj = AccessKeyValueInfo()
                obj._deserialize(item)
                self._KeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessValueInfo(AbstractModel):
    """用于DescribeAccessIndex接口的出参

    """

    def __init__(self):
        r"""
        :param _Type: 字段类型，目前支持的类型有：long、text、double
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Tokenizer: 字段的分词符，只有当字段类型为text时才有意义；输入字符串中的每个字符代表一个分词符
注意：此字段可能返回 null，表示取不到有效值。
        :type Tokenizer: str
        :param _SqlFlag: 字段是否开启分析功能
注意：此字段可能返回 null，表示取不到有效值。
        :type SqlFlag: bool
        :param _ContainZH: 是否包含中文
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainZH: bool
        """
        self._Type = None
        self._Tokenizer = None
        self._SqlFlag = None
        self._ContainZH = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tokenizer(self):
        return self._Tokenizer

    @Tokenizer.setter
    def Tokenizer(self, Tokenizer):
        self._Tokenizer = Tokenizer

    @property
    def SqlFlag(self):
        return self._SqlFlag

    @SqlFlag.setter
    def SqlFlag(self, SqlFlag):
        self._SqlFlag = SqlFlag

    @property
    def ContainZH(self):
        return self._ContainZH

    @ContainZH.setter
    def ContainZH(self, ContainZH):
        self._ContainZH = ContainZH


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Tokenizer = params.get("Tokenizer")
        self._SqlFlag = params.get("SqlFlag")
        self._ContainZH = params.get("ContainZH")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAntiFakeUrlRequest(AbstractModel):
    """AddAntiFakeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Name: 名称
        :type Name: str
        :param _Uri: uri
        :type Uri: str
        """
        self._Domain = None
        self._Name = None
        self._Uri = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Name = params.get("Name")
        self._Uri = params.get("Uri")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAntiFakeUrlResponse(AbstractModel):
    """AddAntiFakeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果
        :type Result: str
        :param _Id: 规则ID
        :type Id: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Id = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class AddAntiInfoLeakRulesRequest(AbstractModel):
    """AddAntiInfoLeakRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Name: 规则名称
        :type Name: str
        :param _ActionType: 动作，0（告警）、1（替换）、2（仅显示前四位）、3（仅显示后四位）、4（阻断）
        :type ActionType: int
        :param _Strategies: 策略详情
        :type Strategies: list of StrategyForAntiInfoLeak
        :param _Uri: 网址
        :type Uri: str
        """
        self._Domain = None
        self._Name = None
        self._ActionType = None
        self._Strategies = None
        self._Uri = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Name = params.get("Name")
        self._ActionType = params.get("ActionType")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = StrategyForAntiInfoLeak()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._Uri = params.get("Uri")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAntiInfoLeakRulesResponse(AbstractModel):
    """AddAntiInfoLeakRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class AddCustomRuleRequest(AbstractModel):
    """AddCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _SortId: 优先级
        :type SortId: str
        :param _ExpireTime: 过期时间，单位为秒级时间戳，例如1677254399表示过期时间为2023-02-24 23:59:59. 0表示永不过期
        :type ExpireTime: str
        :param _Strategies: 策略详情
        :type Strategies: list of Strategy
        :param _Domain: 需要添加策略的域名
        :type Domain: str
        :param _ActionType: 动作类型，1代表阻断，2代表人机识别，3代表观察，4代表重定向
        :type ActionType: str
        :param _Redirect: 如果动作是重定向，则表示重定向的地址；其他情况可以为空
        :type Redirect: str
        :param _Edition: WAF实例类型，sparta-waf表示SAAS型WAF，clb-waf表示负载均衡型WAF
        :type Edition: str
        :param _Bypass: 放行的详情
        :type Bypass: str
        :param _EventId: 添加规则的来源，默认为空
        :type EventId: str
        """
        self._Name = None
        self._SortId = None
        self._ExpireTime = None
        self._Strategies = None
        self._Domain = None
        self._ActionType = None
        self._Redirect = None
        self._Edition = None
        self._Bypass = None
        self._EventId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Redirect(self):
        return self._Redirect

    @Redirect.setter
    def Redirect(self, Redirect):
        self._Redirect = Redirect

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Bypass(self):
        return self._Bypass

    @Bypass.setter
    def Bypass(self, Bypass):
        self._Bypass = Bypass

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SortId = params.get("SortId")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = Strategy()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._Domain = params.get("Domain")
        self._ActionType = params.get("ActionType")
        self._Redirect = params.get("Redirect")
        self._Edition = params.get("Edition")
        self._Bypass = params.get("Bypass")
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCustomRuleResponse(AbstractModel):
    """AddCustomRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RuleId: 添加成功的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RuleId = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class AddCustomWhiteRuleRequest(AbstractModel):
    """AddCustomWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 规则名称
        :type Name: str
        :param _SortId: 优先级
        :type SortId: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _Strategies: 策略详情
        :type Strategies: list of Strategy
        :param _Domain: 需要添加策略的域名
        :type Domain: str
        :param _Bypass: 放行的详情
        :type Bypass: str
        """
        self._Name = None
        self._SortId = None
        self._ExpireTime = None
        self._Strategies = None
        self._Domain = None
        self._Bypass = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Bypass(self):
        return self._Bypass

    @Bypass.setter
    def Bypass(self, Bypass):
        self._Bypass = Bypass


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SortId = params.get("SortId")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = Strategy()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._Domain = params.get("Domain")
        self._Bypass = params.get("Bypass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCustomWhiteRuleResponse(AbstractModel):
    """AddCustomWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RuleId: 添加成功的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RuleId = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class AddDomainWhiteRuleRequest(AbstractModel):
    """AddDomainWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要添加的域名
        :type Domain: str
        :param _Rules: 需要添加的规则
        :type Rules: list of int non-negative
        :param _Url: 需要添加的规则url
        :type Url: str
        :param _Function: 规则的方法
        :type Function: str
        :param _Status: 规则的开关，0表示规则关闭，1表示规则打开
        :type Status: int
        """
        self._Domain = None
        self._Rules = None
        self._Url = None
        self._Function = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Rules = params.get("Rules")
        self._Url = params.get("Url")
        self._Function = params.get("Function")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDomainWhiteRuleResponse(AbstractModel):
    """AddDomainWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 规则id
        :type Id: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class AddSpartaProtectionRequest(AbstractModel):
    """AddSpartaProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要防护的域名
        :type Domain: str
        :param _CertType: 证书类型。
0：仅配置HTTP监听端口，没有证书
1：证书来源为自有证书
2：证书来源为托管证书
        :type CertType: int
        :param _IsCdn: waf前是否部署有七层代理服务。
0：没有部署代理服务
1：有部署代理服务，waf将使用XFF获取客户端IP
2：有部署代理服务，waf将使用remote_addr获取客户端IP
3：有部署代理服务，waf将使用ip_headers中的自定义header获取客户端IP
        :type IsCdn: int
        :param _UpstreamType: 回源类型。
0：通过IP回源
1：通过域名回源
        :type UpstreamType: int
        :param _IsWebsocket: 是否开启WebSocket支持。
0：关闭
1：开启
        :type IsWebsocket: int
        :param _LoadBalance: 回源负载均衡策略。
0：轮询
1：IP hash
2：加权轮询
        :type LoadBalance: str
        :param _Cert: CertType为1时，需要填充此参数，表示自有证书的证书链
        :type Cert: str
        :param _PrivateKey: CertType为1时，需要填充此参数，表示自有证书的私钥
        :type PrivateKey: str
        :param _SSLId: CertType为2时，需要填充此参数，表示腾讯云SSL平台托管的证书id
        :type SSLId: str
        :param _ResourceId: 待废弃，可不填。Waf的资源ID。
        :type ResourceId: str
        :param _IpHeaders: IsCdn为3时，需要填此参数，表示自定义header
        :type IpHeaders: list of str
        :param _UpstreamScheme: 服务配置有HTTPS端口时，HTTPS的回源协议。
http：使用http协议回源，和HttpsUpstreamPort配合使用
https：使用https协议回源
        :type UpstreamScheme: str
        :param _HttpsUpstreamPort: HTTPS回源端口,仅UpstreamScheme为http时需要填当前字段
        :type HttpsUpstreamPort: str
        :param _IsGray: 待废弃，可不填。是否开启灰度，0表示不开启灰度。
        :type IsGray: int
        :param _GrayAreas: 待废弃，可不填。灰度的地区
        :type GrayAreas: list of str
        :param _HttpsRewrite: 是否开启HTTP强制跳转到HTTPS。
0：不强制跳转
1：开启强制跳转
        :type HttpsRewrite: int
        :param _UpstreamDomain: 域名回源时的回源域名。UpstreamType为1时，需要填充此字段
        :type UpstreamDomain: str
        :param _SrcList: IP回源时的回源IP列表。UpstreamType为0时，需要填充此字段
        :type SrcList: list of str
        :param _IsHttp2: 是否开启HTTP2，需要开启HTTPS协议支持。
0：关闭
1：开启
        :type IsHttp2: int
        :param _Ports: 服务端口列表配置。
NginxServerId：新增域名时填'0'
Port：监听端口号
Protocol：端口协议
UpstreamPort：与Port相同
UpstreamProtocol：与Protocol相同
        :type Ports: list of PortItem
        :param _Edition: 待废弃，可不填。WAF实例类型。
sparta-waf：SAAS型WAF
clb-waf：负载均衡型WAF
cdn-waf：CDN上的Web防护能力
        :type Edition: str
        :param _IsKeepAlive: 是否开启长连接。
0： 短连接
1： 长连接
        :type IsKeepAlive: str
        :param _InstanceID: 域名所属实例id
        :type InstanceID: str
        :param _Anycast: 待废弃，目前填0即可。anycast IP类型开关： 0 普通IP 1 Anycast IP
        :type Anycast: int
        :param _Weights: 回源IP列表各IP的权重，和SrcList一一对应。当且仅当UpstreamType为0，并且SrcList有多个IP，并且LoadBalance为2时需要填写，否则填 []
        :type Weights: list of int
        :param _ActiveCheck: 是否开启主动健康检测。
0：不开启
1：开启
        :type ActiveCheck: int
        :param _TLSVersion: TLS版本信息
        :type TLSVersion: int
        :param _CipherTemplate: 加密套件模板。
0：不支持选择，使用默认模版  
1：通用型模版 
2：安全型模版 
3：自定义模版
        :type CipherTemplate: int
        :param _Ciphers: 自定义的加密套件列表。CipherTemplate为3时需要填此字段，表示自定义的加密套件，值通过DescribeCiphersDetail接口获取。
        :type Ciphers: list of int
        :param _ProxyReadTimeout: WAF与源站的读超时时间，默认300s。
        :type ProxyReadTimeout: int
        :param _ProxySendTimeout: WAF与源站的写超时时间，默认300s。
        :type ProxySendTimeout: int
        :param _SniType: WAF回源时的SNI类型。
0：关闭SNI，不配置client_hello中的server_name
1：开启SNI，client_hello中的server_name为防护域名
2：开启SNI，SNI为域名回源时的源站域名
3：开启SNI，SNI为自定义域名
        :type SniType: int
        :param _SniHost: SniType为3时，需要填此参数，表示自定义的SNI；
        :type SniHost: str
        :param _XFFReset: 是否开启XFF重置。
0：关闭
1：开启
        :type XFFReset: int
        """
        self._Domain = None
        self._CertType = None
        self._IsCdn = None
        self._UpstreamType = None
        self._IsWebsocket = None
        self._LoadBalance = None
        self._Cert = None
        self._PrivateKey = None
        self._SSLId = None
        self._ResourceId = None
        self._IpHeaders = None
        self._UpstreamScheme = None
        self._HttpsUpstreamPort = None
        self._IsGray = None
        self._GrayAreas = None
        self._HttpsRewrite = None
        self._UpstreamDomain = None
        self._SrcList = None
        self._IsHttp2 = None
        self._Ports = None
        self._Edition = None
        self._IsKeepAlive = None
        self._InstanceID = None
        self._Anycast = None
        self._Weights = None
        self._ActiveCheck = None
        self._TLSVersion = None
        self._CipherTemplate = None
        self._Ciphers = None
        self._ProxyReadTimeout = None
        self._ProxySendTimeout = None
        self._SniType = None
        self._SniHost = None
        self._XFFReset = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def IsCdn(self):
        return self._IsCdn

    @IsCdn.setter
    def IsCdn(self, IsCdn):
        self._IsCdn = IsCdn

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def IsWebsocket(self):
        return self._IsWebsocket

    @IsWebsocket.setter
    def IsWebsocket(self, IsWebsocket):
        self._IsWebsocket = IsWebsocket

    @property
    def LoadBalance(self):
        return self._LoadBalance

    @LoadBalance.setter
    def LoadBalance(self, LoadBalance):
        self._LoadBalance = LoadBalance

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def IpHeaders(self):
        return self._IpHeaders

    @IpHeaders.setter
    def IpHeaders(self, IpHeaders):
        self._IpHeaders = IpHeaders

    @property
    def UpstreamScheme(self):
        return self._UpstreamScheme

    @UpstreamScheme.setter
    def UpstreamScheme(self, UpstreamScheme):
        self._UpstreamScheme = UpstreamScheme

    @property
    def HttpsUpstreamPort(self):
        return self._HttpsUpstreamPort

    @HttpsUpstreamPort.setter
    def HttpsUpstreamPort(self, HttpsUpstreamPort):
        self._HttpsUpstreamPort = HttpsUpstreamPort

    @property
    def IsGray(self):
        return self._IsGray

    @IsGray.setter
    def IsGray(self, IsGray):
        self._IsGray = IsGray

    @property
    def GrayAreas(self):
        return self._GrayAreas

    @GrayAreas.setter
    def GrayAreas(self, GrayAreas):
        self._GrayAreas = GrayAreas

    @property
    def HttpsRewrite(self):
        return self._HttpsRewrite

    @HttpsRewrite.setter
    def HttpsRewrite(self, HttpsRewrite):
        self._HttpsRewrite = HttpsRewrite

    @property
    def UpstreamDomain(self):
        return self._UpstreamDomain

    @UpstreamDomain.setter
    def UpstreamDomain(self, UpstreamDomain):
        self._UpstreamDomain = UpstreamDomain

    @property
    def SrcList(self):
        return self._SrcList

    @SrcList.setter
    def SrcList(self, SrcList):
        self._SrcList = SrcList

    @property
    def IsHttp2(self):
        return self._IsHttp2

    @IsHttp2.setter
    def IsHttp2(self, IsHttp2):
        self._IsHttp2 = IsHttp2

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def IsKeepAlive(self):
        return self._IsKeepAlive

    @IsKeepAlive.setter
    def IsKeepAlive(self, IsKeepAlive):
        self._IsKeepAlive = IsKeepAlive

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Anycast(self):
        return self._Anycast

    @Anycast.setter
    def Anycast(self, Anycast):
        self._Anycast = Anycast

    @property
    def Weights(self):
        return self._Weights

    @Weights.setter
    def Weights(self, Weights):
        self._Weights = Weights

    @property
    def ActiveCheck(self):
        return self._ActiveCheck

    @ActiveCheck.setter
    def ActiveCheck(self, ActiveCheck):
        self._ActiveCheck = ActiveCheck

    @property
    def TLSVersion(self):
        return self._TLSVersion

    @TLSVersion.setter
    def TLSVersion(self, TLSVersion):
        self._TLSVersion = TLSVersion

    @property
    def CipherTemplate(self):
        return self._CipherTemplate

    @CipherTemplate.setter
    def CipherTemplate(self, CipherTemplate):
        self._CipherTemplate = CipherTemplate

    @property
    def Ciphers(self):
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def ProxyReadTimeout(self):
        return self._ProxyReadTimeout

    @ProxyReadTimeout.setter
    def ProxyReadTimeout(self, ProxyReadTimeout):
        self._ProxyReadTimeout = ProxyReadTimeout

    @property
    def ProxySendTimeout(self):
        return self._ProxySendTimeout

    @ProxySendTimeout.setter
    def ProxySendTimeout(self, ProxySendTimeout):
        self._ProxySendTimeout = ProxySendTimeout

    @property
    def SniType(self):
        return self._SniType

    @SniType.setter
    def SniType(self, SniType):
        self._SniType = SniType

    @property
    def SniHost(self):
        return self._SniHost

    @SniHost.setter
    def SniHost(self, SniHost):
        self._SniHost = SniHost

    @property
    def XFFReset(self):
        return self._XFFReset

    @XFFReset.setter
    def XFFReset(self, XFFReset):
        self._XFFReset = XFFReset


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertType = params.get("CertType")
        self._IsCdn = params.get("IsCdn")
        self._UpstreamType = params.get("UpstreamType")
        self._IsWebsocket = params.get("IsWebsocket")
        self._LoadBalance = params.get("LoadBalance")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._SSLId = params.get("SSLId")
        self._ResourceId = params.get("ResourceId")
        self._IpHeaders = params.get("IpHeaders")
        self._UpstreamScheme = params.get("UpstreamScheme")
        self._HttpsUpstreamPort = params.get("HttpsUpstreamPort")
        self._IsGray = params.get("IsGray")
        self._GrayAreas = params.get("GrayAreas")
        self._HttpsRewrite = params.get("HttpsRewrite")
        self._UpstreamDomain = params.get("UpstreamDomain")
        self._SrcList = params.get("SrcList")
        self._IsHttp2 = params.get("IsHttp2")
        if params.get("Ports") is not None:
            self._Ports = []
            for item in params.get("Ports"):
                obj = PortItem()
                obj._deserialize(item)
                self._Ports.append(obj)
        self._Edition = params.get("Edition")
        self._IsKeepAlive = params.get("IsKeepAlive")
        self._InstanceID = params.get("InstanceID")
        self._Anycast = params.get("Anycast")
        self._Weights = params.get("Weights")
        self._ActiveCheck = params.get("ActiveCheck")
        self._TLSVersion = params.get("TLSVersion")
        self._CipherTemplate = params.get("CipherTemplate")
        self._Ciphers = params.get("Ciphers")
        self._ProxyReadTimeout = params.get("ProxyReadTimeout")
        self._ProxySendTimeout = params.get("ProxySendTimeout")
        self._SniType = params.get("SniType")
        self._SniHost = params.get("SniHost")
        self._XFFReset = params.get("XFFReset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSpartaProtectionResponse(AbstractModel):
    """AddSpartaProtection返回参数结构体

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


class AttackLogInfo(AbstractModel):
    """攻击日志详情

    """

    def __init__(self):
        r"""
        :param _Content: 攻击日志的详情内容
        :type Content: str
        :param _FileName: CLS返回内容
        :type FileName: str
        :param _Source: CLS返回内容
        :type Source: str
        :param _TimeStamp: CLS返回内容
        :type TimeStamp: str
        """
        self._Content = None
        self._FileName = None
        self._Source = None
        self._TimeStamp = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._FileName = params.get("FileName")
        self._Source = params.get("Source")
        self._TimeStamp = params.get("TimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoDenyDetail(AbstractModel):
    """Waf 攻击自动封禁详情

    """

    def __init__(self):
        r"""
        :param _AttackTags: 攻击封禁类型标签
        :type AttackTags: list of str
        :param _AttackThreshold: 攻击次数阈值
        :type AttackThreshold: int
        :param _DefenseStatus: 自动封禁状态
        :type DefenseStatus: int
        :param _TimeThreshold: 攻击时间阈值
        :type TimeThreshold: int
        :param _DenyTimeThreshold: 自动封禁时间
        :type DenyTimeThreshold: int
        :param _LastUpdateTime: 最后更新时间
        :type LastUpdateTime: str
        """
        self._AttackTags = None
        self._AttackThreshold = None
        self._DefenseStatus = None
        self._TimeThreshold = None
        self._DenyTimeThreshold = None
        self._LastUpdateTime = None

    @property
    def AttackTags(self):
        return self._AttackTags

    @AttackTags.setter
    def AttackTags(self, AttackTags):
        self._AttackTags = AttackTags

    @property
    def AttackThreshold(self):
        return self._AttackThreshold

    @AttackThreshold.setter
    def AttackThreshold(self, AttackThreshold):
        self._AttackThreshold = AttackThreshold

    @property
    def DefenseStatus(self):
        return self._DefenseStatus

    @DefenseStatus.setter
    def DefenseStatus(self, DefenseStatus):
        self._DefenseStatus = DefenseStatus

    @property
    def TimeThreshold(self):
        return self._TimeThreshold

    @TimeThreshold.setter
    def TimeThreshold(self, TimeThreshold):
        self._TimeThreshold = TimeThreshold

    @property
    def DenyTimeThreshold(self):
        return self._DenyTimeThreshold

    @DenyTimeThreshold.setter
    def DenyTimeThreshold(self, DenyTimeThreshold):
        self._DenyTimeThreshold = DenyTimeThreshold

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._AttackTags = params.get("AttackTags")
        self._AttackThreshold = params.get("AttackThreshold")
        self._DefenseStatus = params.get("DefenseStatus")
        self._TimeThreshold = params.get("TimeThreshold")
        self._DenyTimeThreshold = params.get("DenyTimeThreshold")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchIpAccessControlData(AbstractModel):
    """多域名黑白名单describe返回

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Res: 黑白名单条目
        :type Res: list of BatchIpAccessControlItem
        """
        self._TotalCount = None
        self._Res = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Res(self):
        return self._Res

    @Res.setter
    def Res(self, Res):
        self._Res = Res


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Res") is not None:
            self._Res = []
            for item in params.get("Res"):
                obj = BatchIpAccessControlItem()
                obj._deserialize(item)
                self._Res.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchIpAccessControlItem(AbstractModel):
    """多域名黑白名单列表Ip

    """

    def __init__(self):
        r"""
        :param _Id: mongo表自增Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _ActionType: 黑名单42或白名单40
        :type ActionType: int
        :param _Ip: 黑白名单的IP
        :type Ip: str
        :param _Note: 备注
        :type Note: str
        :param _Source: 添加路径
        :type Source: str
        :param _TsVersion: 修改时间
        :type TsVersion: int
        :param _ValidTs: 超时时间
        :type ValidTs: int
        :param _Hosts: 域名列表
        :type Hosts: list of str
        """
        self._Id = None
        self._ActionType = None
        self._Ip = None
        self._Note = None
        self._Source = None
        self._TsVersion = None
        self._ValidTs = None
        self._Hosts = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def TsVersion(self):
        return self._TsVersion

    @TsVersion.setter
    def TsVersion(self, TsVersion):
        self._TsVersion = TsVersion

    @property
    def ValidTs(self):
        return self._ValidTs

    @ValidTs.setter
    def ValidTs(self, ValidTs):
        self._ValidTs = ValidTs

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ActionType = params.get("ActionType")
        self._Ip = params.get("Ip")
        self._Note = params.get("Note")
        self._Source = params.get("Source")
        self._TsVersion = params.get("TsVersion")
        self._ValidTs = params.get("ValidTs")
        self._Hosts = params.get("Hosts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotPkg(AbstractModel):
    """Bot资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _InquireNum: 申请数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InquireNum: int
        :param _UsedNum: 使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedNum: int
        :param _Type: 子产品code
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _RenewFlag: 续费标志	
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _BotCPWaf: 购买页bot6折
注意：此字段可能返回 null，表示取不到有效值。
        :type BotCPWaf: int
        :param _BotNPWaf: 控制台买bot5折
注意：此字段可能返回 null，表示取不到有效值。
        :type BotNPWaf: int
        """
        self._ResourceIds = None
        self._Status = None
        self._Region = None
        self._BeginTime = None
        self._EndTime = None
        self._InquireNum = None
        self._UsedNum = None
        self._Type = None
        self._RenewFlag = None
        self._BotCPWaf = None
        self._BotNPWaf = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InquireNum(self):
        return self._InquireNum

    @InquireNum.setter
    def InquireNum(self, InquireNum):
        self._InquireNum = InquireNum

    @property
    def UsedNum(self):
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def BotCPWaf(self):
        return self._BotCPWaf

    @BotCPWaf.setter
    def BotCPWaf(self, BotCPWaf):
        self._BotCPWaf = BotCPWaf

    @property
    def BotNPWaf(self):
        return self._BotNPWaf

    @BotNPWaf.setter
    def BotNPWaf(self, BotNPWaf):
        self._BotNPWaf = BotNPWaf


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._InquireNum = params.get("InquireNum")
        self._UsedNum = params.get("UsedNum")
        self._Type = params.get("Type")
        self._RenewFlag = params.get("RenewFlag")
        self._BotCPWaf = params.get("BotCPWaf")
        self._BotNPWaf = params.get("BotNPWaf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotQPS(AbstractModel):
    """bot的qps详情

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 资源id
        :type ResourceIds: str
        :param _ValidTime: 有效时间
        :type ValidTime: str
        :param _Count: 资源数量
        :type Count: int
        :param _Region: 资源所在地区
        :type Region: str
        :param _MaxBotQPS: 使用qps的最大值
        :type MaxBotQPS: int
        :param _RenewFlag: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        """
        self._ResourceIds = None
        self._ValidTime = None
        self._Count = None
        self._Region = None
        self._MaxBotQPS = None
        self._RenewFlag = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ValidTime(self):
        return self._ValidTime

    @ValidTime.setter
    def ValidTime(self, ValidTime):
        self._ValidTime = ValidTime

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def MaxBotQPS(self):
        return self._MaxBotQPS

    @MaxBotQPS.setter
    def MaxBotQPS(self, MaxBotQPS):
        self._MaxBotQPS = MaxBotQPS

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._ValidTime = params.get("ValidTime")
        self._Count = params.get("Count")
        self._Region = params.get("Region")
        self._MaxBotQPS = params.get("MaxBotQPS")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotStatPointItem(AbstractModel):
    """bot的趋势图对象

    """

    def __init__(self):
        r"""
        :param _TimeStamp: 横坐标
        :type TimeStamp: str
        :param _Key: value的所属对象
        :type Key: str
        :param _Value: 纵列表
        :type Value: int
        :param _Label: Key对应的页面展示内容
        :type Label: str
        """
        self._TimeStamp = None
        self._Key = None
        self._Value = None
        self._Label = None

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp

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

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._TimeStamp = params.get("TimeStamp")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRuleData(AbstractModel):
    """数据封装

    """

    def __init__(self):
        r"""
        :param _Res: cc规则
        :type Res: list of CCRuleItem
        :param _TotalCount: 规则数目
        :type TotalCount: int
        """
        self._Res = None
        self._TotalCount = None

    @property
    def Res(self):
        return self._Res

    @Res.setter
    def Res(self, Res):
        self._Res = Res

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("Res") is not None:
            self._Res = []
            for item in params.get("Res"):
                obj = CCRuleItem()
                obj._deserialize(item)
                self._Res.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRuleItem(AbstractModel):
    """cc规则

    """

    def __init__(self):
        r"""
        :param _ActionType: 动作
        :type ActionType: int
        :param _Advance: 高级模式
        :type Advance: int
        :param _Interval: 时间周期
        :type Interval: int
        :param _Limit: 限制次数
        :type Limit: int
        :param _MatchFunc: 匹配方法
        :type MatchFunc: int
        :param _Name: 名称
        :type Name: str
        :param _Priority: 优先级
        :type Priority: int
        :param _Status: 状态
        :type Status: int
        :param _TsVersion: 更新时间戳
        :type TsVersion: int
        :param _Url: 匹配url
        :type Url: str
        :param _ValidTime: 策略动作有效时间
        :type ValidTime: int
        :param _OptionsArr: 高级参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionsArr: str
        """
        self._ActionType = None
        self._Advance = None
        self._Interval = None
        self._Limit = None
        self._MatchFunc = None
        self._Name = None
        self._Priority = None
        self._Status = None
        self._TsVersion = None
        self._Url = None
        self._ValidTime = None
        self._OptionsArr = None

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Advance(self):
        return self._Advance

    @Advance.setter
    def Advance(self, Advance):
        self._Advance = Advance

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MatchFunc(self):
        return self._MatchFunc

    @MatchFunc.setter
    def MatchFunc(self, MatchFunc):
        self._MatchFunc = MatchFunc

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TsVersion(self):
        return self._TsVersion

    @TsVersion.setter
    def TsVersion(self, TsVersion):
        self._TsVersion = TsVersion

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ValidTime(self):
        return self._ValidTime

    @ValidTime.setter
    def ValidTime(self, ValidTime):
        self._ValidTime = ValidTime

    @property
    def OptionsArr(self):
        return self._OptionsArr

    @OptionsArr.setter
    def OptionsArr(self, OptionsArr):
        self._OptionsArr = OptionsArr


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._Advance = params.get("Advance")
        self._Interval = params.get("Interval")
        self._Limit = params.get("Limit")
        self._MatchFunc = params.get("MatchFunc")
        self._Name = params.get("Name")
        self._Priority = params.get("Priority")
        self._Status = params.get("Status")
        self._TsVersion = params.get("TsVersion")
        self._Url = params.get("Url")
        self._ValidTime = params.get("ValidTime")
        self._OptionsArr = params.get("OptionsArr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheUrlItem(AbstractModel):
    """防篡改url元素

    """

    def __init__(self):
        r"""
        :param _Id: Id
        :type Id: str
        :param _Name: 名称
        :type Name: str
        :param _Domain: 域名
        :type Domain: str
        :param _Uri: uri
        :type Uri: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Status: 状态
        :type Status: str
        """
        self._Id = None
        self._Name = None
        self._Domain = None
        self._Uri = None
        self._Protocol = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Domain = params.get("Domain")
        self._Uri = params.get("Uri")
        self._Protocol = params.get("Protocol")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheUrlItems(AbstractModel):
    """防篡改url元素

    """

    def __init__(self):
        r"""
        :param _Id: 标识
        :type Id: int
        :param _Name: 名字
        :type Name: str
        :param _Domain: 域名
        :type Domain: str
        :param _Uri: 网址
        :type Uri: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Status: 状态
        :type Status: int
        """
        self._Id = None
        self._Name = None
        self._Domain = None
        self._Uri = None
        self._Protocol = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Domain = params.get("Domain")
        self._Uri = params.get("Uri")
        self._Protocol = params.get("Protocol")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdcCluster(AbstractModel):
    """CDC场景下负载均衡WAF的集群信息

    """

    def __init__(self):
        r"""
        :param _Id: cdc的集群id
        :type Id: str
        :param _Name: cdc的集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdcRegion(AbstractModel):
    """CDC场景下负载均衡WAF的地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _Clusters: 该地域对应的集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Clusters: list of CdcCluster
        """
        self._Region = None
        self._Clusters = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Clusters(self):
        return self._Clusters

    @Clusters.setter
    def Clusters(self, Clusters):
        self._Clusters = Clusters


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("Clusters") is not None:
            self._Clusters = []
            for item in params.get("Clusters"):
                obj = CdcCluster()
                obj._deserialize(item)
                self._Clusters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbDomainsInfo(AbstractModel):
    """clb域名详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名id
        :type DomainId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _Edition: waf类型
        :type Edition: str
        :param _IsCdn: 是否是cdn
        :type IsCdn: int
        :param _LoadBalancerSet: 负载均衡算法
        :type LoadBalancerSet: list of LoadBalancerPackageNew
        :param _FlowMode: 镜像模式
        :type FlowMode: int
        :param _State: 绑定clb状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _AlbType: 负载均衡类型，clb或者apisix
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbType: str
        :param _IpHeaders: IsCdn=3时，表示自定义header
注意：此字段可能返回 null，表示取不到有效值。
        :type IpHeaders: list of str
        :param _CdcClusters: cdc类型会增加集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcClusters: str
        :param _CloudType: 云类型:public:公有云；private:私有云;hybrid:混合云
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudType: str
        """
        self._Domain = None
        self._DomainId = None
        self._InstanceId = None
        self._InstanceName = None
        self._Edition = None
        self._IsCdn = None
        self._LoadBalancerSet = None
        self._FlowMode = None
        self._State = None
        self._AlbType = None
        self._IpHeaders = None
        self._CdcClusters = None
        self._CloudType = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

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
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def IsCdn(self):
        return self._IsCdn

    @IsCdn.setter
    def IsCdn(self, IsCdn):
        self._IsCdn = IsCdn

    @property
    def LoadBalancerSet(self):
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def FlowMode(self):
        return self._FlowMode

    @FlowMode.setter
    def FlowMode(self, FlowMode):
        self._FlowMode = FlowMode

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AlbType(self):
        return self._AlbType

    @AlbType.setter
    def AlbType(self, AlbType):
        self._AlbType = AlbType

    @property
    def IpHeaders(self):
        return self._IpHeaders

    @IpHeaders.setter
    def IpHeaders(self, IpHeaders):
        self._IpHeaders = IpHeaders

    @property
    def CdcClusters(self):
        return self._CdcClusters

    @CdcClusters.setter
    def CdcClusters(self, CdcClusters):
        self._CdcClusters = CdcClusters

    @property
    def CloudType(self):
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Edition = params.get("Edition")
        self._IsCdn = params.get("IsCdn")
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancerPackageNew()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._FlowMode = params.get("FlowMode")
        self._State = params.get("State")
        self._AlbType = params.get("AlbType")
        self._IpHeaders = params.get("IpHeaders")
        self._CdcClusters = params.get("CdcClusters")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbHostResult(AbstractModel):
    """CLB查询对应绑定的WAF状态的结果参数

    """

    def __init__(self):
        r"""
        :param _LoadBalancer: WAF绑定的监听器实例
        :type LoadBalancer: :class:`tencentcloud.waf.v20180125.models.LoadBalancer`
        :param _Domain: WAF绑定的域名
        :type Domain: str
        :param _DomainId: WAF绑定的实例ID
        :type DomainId: str
        :param _Status: 是否有绑定WAF，1：绑定了WAF，0：没有绑定WAF
        :type Status: int
        :param _FlowMode: 绑定了WAF的情况下，WAF流量模式，1：清洗模式，0：镜像模式（默认）
        :type FlowMode: int
        """
        self._LoadBalancer = None
        self._Domain = None
        self._DomainId = None
        self._Status = None
        self._FlowMode = None

    @property
    def LoadBalancer(self):
        return self._LoadBalancer

    @LoadBalancer.setter
    def LoadBalancer(self, LoadBalancer):
        self._LoadBalancer = LoadBalancer

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FlowMode(self):
        return self._FlowMode

    @FlowMode.setter
    def FlowMode(self, FlowMode):
        self._FlowMode = FlowMode


    def _deserialize(self, params):
        if params.get("LoadBalancer") is not None:
            self._LoadBalancer = LoadBalancer()
            self._LoadBalancer._deserialize(params.get("LoadBalancer"))
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Status = params.get("Status")
        self._FlowMode = params.get("FlowMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbHostsParams(AbstractModel):
    """CLB回调WAF接口（获取、删除）的参数

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID，如果不传次参数则默认认为操作的是整个AppId的监听器，如果此参数不为空则认为操作的是对应负载均衡实例。
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器ID，，如果不传次参数则默认认为操作的是整个负载均衡实例，如果此参数不为空则认为操作的是对应负载均衡监听器。
        :type ListenerId: str
        :param _DomainId: WAF实例ID，，如果不传次参数则默认认为操作的是整个负载均衡监听器实例，如果此参数不为空则认为操作的是对应负载均衡监听器的某一个具体的域名。
        :type DomainId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._DomainId = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessExportRequest(AbstractModel):
    """CreateAccessExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题
        :type TopicId: str
        :param _From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param _To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param _Query: 日志导出检索语句
        :type Query: str
        :param _Count: 日志导出数量，最大值100w
        :type Count: int
        :param _Format: 日志导出数据格式。json，csv，默认为json
        :type Format: str
        :param _Order: 日志导出时间排序。desc，asc，默认为desc
        :type Order: str
        """
        self._TopicId = None
        self._From = None
        self._To = None
        self._Query = None
        self._Count = None
        self._Format = None
        self._Order = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._Count = params.get("Count")
        self._Format = params.get("Format")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccessExportResponse(AbstractModel):
    """CreateAccessExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportId: 日志导出ID。
        :type ExportId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ExportId = None
        self._RequestId = None

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        self._RequestId = params.get("RequestId")


class CreateHostRequest(AbstractModel):
    """CreateHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Host: 防护域名配置信息
        :type Host: :class:`tencentcloud.waf.v20180125.models.HostRecord`
        :param _InstanceID: 实例id
        :type InstanceID: str
        """
        self._Host = None
        self._InstanceID = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        if params.get("Host") is not None:
            self._Host = HostRecord()
            self._Host._deserialize(params.get("Host"))
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHostResponse(AbstractModel):
    """CreateHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 新增防护域名ID
        :type DomainId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainId = None
        self._RequestId = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._RequestId = params.get("RequestId")


class DealData(AbstractModel):
    """计费下单响应实体

    """

    def __init__(self):
        r"""
        :param _DealNames: 订单号列表，元素个数与请求包的goods数组的元素个数一致，商品详情与订单按顺序对应
        :type DealNames: list of str
        :param _BigDealId: 大订单号，一个大订单号下可以有多个子订单，说明是同一次下单[{},{}]
        :type BigDealId: str
        """
        self._DealNames = None
        self._BigDealId = None

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def BigDealId(self):
        return self._BigDealId

    @BigDealId.setter
    def BigDealId(self, BigDealId):
        self._BigDealId = BigDealId


    def _deserialize(self, params):
        self._DealNames = params.get("DealNames")
        self._BigDealId = params.get("BigDealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessExportRequest(AbstractModel):
    """DeleteAccessExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExportId: 日志导出ID
        :type ExportId: str
        :param _TopicId: 日志主题
        :type TopicId: str
        """
        self._ExportId = None
        self._TopicId = None

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccessExportResponse(AbstractModel):
    """DeleteAccessExport返回参数结构体

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


class DeleteAntiFakeUrlRequest(AbstractModel):
    """DeleteAntiFakeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Id: Id
        :type Id: int
        """
        self._Domain = None
        self._Id = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAntiFakeUrlResponse(AbstractModel):
    """DeleteAntiFakeUrl返回参数结构体

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


class DeleteAntiInfoLeakRuleRequest(AbstractModel):
    """DeleteAntiInfoLeakRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RuleId: 规则id
        :type RuleId: int
        """
        self._Domain = None
        self._RuleId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAntiInfoLeakRuleResponse(AbstractModel):
    """DeleteAntiInfoLeakRule返回参数结构体

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


class DeleteAttackDownloadRecordRequest(AbstractModel):
    """DeleteAttackDownloadRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 下载任务记录唯一标记
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttackDownloadRecordResponse(AbstractModel):
    """DeleteAttackDownloadRecord返回参数结构体

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


class DeleteCCRuleRequest(AbstractModel):
    """DeleteCCRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Name: 规则名称
        :type Name: str
        :param _Edition: clb-waf或者sparta-waf
        :type Edition: str
        :param _RuleId: 规则Id
        :type RuleId: int
        """
        self._Domain = None
        self._Name = None
        self._Edition = None
        self._RuleId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Name = params.get("Name")
        self._Edition = params.get("Edition")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCRuleResponse(AbstractModel):
    """DeleteCCRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 一般为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RuleId: 操作的规则Id
        :type RuleId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RuleId = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class DeleteCustomRuleRequest(AbstractModel):
    """DeleteCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 删除的域名
        :type Domain: str
        :param _RuleId: 删除的规则ID
        :type RuleId: str
        :param _Edition: WAF的版本，clb-waf代表负载均衡WAF、sparta-waf代表SaaS WAF，默认是sparta-waf。
        :type Edition: str
        """
        self._Domain = None
        self._RuleId = None
        self._Edition = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomRuleResponse(AbstractModel):
    """DeleteCustomRule返回参数结构体

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


class DeleteCustomWhiteRuleRequest(AbstractModel):
    """DeleteCustomWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 删除的域名
        :type Domain: str
        :param _RuleId: 删除的规则ID
        :type RuleId: int
        """
        self._Domain = None
        self._RuleId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomWhiteRuleResponse(AbstractModel):
    """DeleteCustomWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteDomainWhiteRulesRequest(AbstractModel):
    """DeleteDomainWhiteRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要删除的规则域名
        :type Domain: str
        :param _Ids: 需要删除的白名单规则
        :type Ids: list of int non-negative
        """
        self._Domain = None
        self._Ids = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainWhiteRulesResponse(AbstractModel):
    """DeleteDomainWhiteRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DeleteDownloadRecordRequest(AbstractModel):
    """DeleteDownloadRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Flow: 记录id
        :type Flow: str
        """
        self._Flow = None

    @property
    def Flow(self):
        return self._Flow

    @Flow.setter
    def Flow(self, Flow):
        self._Flow = Flow


    def _deserialize(self, params):
        self._Flow = params.get("Flow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDownloadRecordResponse(AbstractModel):
    """DeleteDownloadRecord返回参数结构体

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


class DeleteHostRequest(AbstractModel):
    """DeleteHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HostsDel: 删除的域名列表
        :type HostsDel: list of HostDel
        """
        self._HostsDel = None

    @property
    def HostsDel(self):
        return self._HostsDel

    @HostsDel.setter
    def HostsDel(self, HostsDel):
        self._HostsDel = HostsDel


    def _deserialize(self, params):
        if params.get("HostsDel") is not None:
            self._HostsDel = []
            for item in params.get("HostsDel"):
                obj = HostDel()
                obj._deserialize(item)
                self._HostsDel.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHostResponse(AbstractModel):
    """DeleteHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteIpAccessControlRequest(AbstractModel):
    """DeleteIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Items: 删除的ip数组
        :type Items: list of str
        :param _IsId: 若IsId字段为True，则Items列表元素需为Id，否则为IP
        :type IsId: bool
        :param _DeleteAll: 是否删除对应的域名下的所有黑/白IP名单，true表示全部删除，false表示只删除指定ip名单
        :type DeleteAll: bool
        :param _SourceType: 是否为多域名黑白名单
        :type SourceType: str
        """
        self._Domain = None
        self._Items = None
        self._IsId = None
        self._DeleteAll = None
        self._SourceType = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def IsId(self):
        return self._IsId

    @IsId.setter
    def IsId(self, IsId):
        self._IsId = IsId

    @property
    def DeleteAll(self):
        return self._DeleteAll

    @DeleteAll.setter
    def DeleteAll(self, DeleteAll):
        self._DeleteAll = DeleteAll

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Items = params.get("Items")
        self._IsId = params.get("IsId")
        self._DeleteAll = params.get("DeleteAll")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIpAccessControlResponse(AbstractModel):
    """DeleteIpAccessControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedItems: 删除失败的条目
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedItems: str
        :param _FailedCount: 删除失败的条目数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedItems = None
        self._FailedCount = None
        self._RequestId = None

    @property
    def FailedItems(self):
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

    @property
    def FailedCount(self):
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedItems = params.get("FailedItems")
        self._FailedCount = params.get("FailedCount")
        self._RequestId = params.get("RequestId")


class DeleteSessionRequest(AbstractModel):
    """DeleteSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Edition: clb-waf 或者 sprta-waf
        :type Edition: str
        :param _SessionID: 要删除的SessionID
        :type SessionID: int
        """
        self._Domain = None
        self._Edition = None
        self._SessionID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def SessionID(self):
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Edition = params.get("Edition")
        self._SessionID = params.get("SessionID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSessionResponse(AbstractModel):
    """DeleteSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DeleteSpartaProtectionRequest(AbstractModel):
    """DeleteSpartaProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 域名列表
        :type Domains: list of str
        :param _Edition: 实例类型
        :type Edition: str
        :param _InstanceID: 实例id
        :type InstanceID: str
        """
        self._Domains = None
        self._Edition = None
        self._InstanceID = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._Edition = params.get("Edition")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSpartaProtectionResponse(AbstractModel):
    """DeleteSpartaProtection返回参数结构体

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


class DescribeAccessExportsRequest(AbstractModel):
    """DescribeAccessExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题
        :type TopicId: str
        :param _Offset: 分页的偏移量，默认值为0
        :type Offset: int
        :param _Limit: 分页单页限制数目，默认值为20，最大值100
        :type Limit: int
        """
        self._TopicId = None
        self._Offset = None
        self._Limit = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

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


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessExportsResponse(AbstractModel):
    """DescribeAccessExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 日志导出ID。
        :type TotalCount: int
        :param _Exports: 日志导出列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Exports: list of ExportAccessInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Exports = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Exports(self):
        return self._Exports

    @Exports.setter
    def Exports(self, Exports):
        self._Exports = Exports

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Exports") is not None:
            self._Exports = []
            for item in params.get("Exports"):
                obj = ExportAccessInfo()
                obj._deserialize(item)
                self._Exports.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccessFastAnalysisRequest(AbstractModel):
    """DescribeAccessFastAnalysis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题
        :type TopicId: str
        :param _From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param _To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param _Query: 查询语句，语句长度最大为4096，由于本接口是分析接口，如果无过滤条件，必须传 * 表示匹配所有，参考CLS的分析统计语句的文档
        :type Query: str
        :param _FieldName: 需要分析统计的字段名
        :type FieldName: str
        :param _Sort: 排序字段,升序asc,降序desc，默认降序desc 
        :type Sort: str
        :param _Count: 返回的top数，默认返回top5
        :type Count: int
        """
        self._TopicId = None
        self._From = None
        self._To = None
        self._Query = None
        self._FieldName = None
        self._Sort = None
        self._Count = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._FieldName = params.get("FieldName")
        self._Sort = params.get("Sort")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessFastAnalysisResponse(AbstractModel):
    """DescribeAccessFastAnalysis返回参数结构体

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


class DescribeAccessHistogramRequest(AbstractModel):
    """DescribeAccessHistogram请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 老版本查询的日志主题ID，新版本传空字符串即可
        :type TopicId: str
        :param _From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param _To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param _Query: 查询语句，语句长度最大为4096
        :type Query: str
        :param _Interval: 柱状图间隔时间差，单位ms
        :type Interval: int
        """
        self._TopicId = None
        self._From = None
        self._To = None
        self._Query = None
        self._Interval = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessHistogramResponse(AbstractModel):
    """DescribeAccessHistogram返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Interval: 柱状图间隔时间差，单位ms
        :type Interval: int
        :param _TotalCount: 满足条件的日志条数
        :type TotalCount: int
        :param _HistogramInfos: 注意：此字段可能返回 null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type HistogramInfos: list of AccessHistogramItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Interval = None
        self._TotalCount = None
        self._HistogramInfos = None
        self._RequestId = None

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HistogramInfos(self):
        return self._HistogramInfos

    @HistogramInfos.setter
    def HistogramInfos(self, HistogramInfos):
        self._HistogramInfos = HistogramInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._TotalCount = params.get("TotalCount")
        if params.get("HistogramInfos") is not None:
            self._HistogramInfos = []
            for item in params.get("HistogramInfos"):
                obj = AccessHistogramItem()
                obj._deserialize(item)
                self._HistogramInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccessIndexRequest(AbstractModel):
    """DescribeAccessIndex请求参数结构体

    """


class DescribeAccessIndexResponse(AbstractModel):
    """DescribeAccessIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 是否生效，true表示生效，false表示未生效
        :type Status: bool
        :param _Rule: 索引配置信息
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Rule: :class:`tencentcloud.waf.v20180125.models.AccessRuleInfo`
        :param _ModifyTime: 索引修改时间，初始值为索引创建时间。
        :type ModifyTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Rule = None
        self._ModifyTime = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("Rule") is not None:
            self._Rule = AccessRuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        self._ModifyTime = params.get("ModifyTime")
        self._RequestId = params.get("RequestId")


class DescribeAntiFakeRulesRequest(AbstractModel):
    """DescribeAntiFakeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Offset: 偏移
        :type Offset: int
        :param _Limit: 容量
        :type Limit: int
        :param _Filters: 过滤数组,name可以是如下的值： RuleID,ParamName,Url,Action,Method,Source,Status
        :type Filters: list of FiltersItemNew
        :param _Order: asc或者desc
        :type Order: str
        :param _By: 目前支持根据ts排序
        :type By: str
        """
        self._Domain = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._By = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FiltersItemNew()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiFakeRulesResponse(AbstractModel):
    """DescribeAntiFakeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CacheUrlItems
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CacheUrlItems()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAntiFakeUrlRequest(AbstractModel):
    """DescribeAntiFakeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _PageInfo: 翻页参数
        :type PageInfo: :class:`tencentcloud.waf.v20180125.models.PageInfo`
        """
        self._Domain = None
        self._PageInfo = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def PageInfo(self):
        return self._PageInfo

    @PageInfo.setter
    def PageInfo(self, PageInfo):
        self._PageInfo = PageInfo


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("PageInfo") is not None:
            self._PageInfo = PageInfo()
            self._PageInfo._deserialize(params.get("PageInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiFakeUrlResponse(AbstractModel):
    """DescribeAntiFakeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: str
        :param _List: 信息
        :type List: list of CacheUrlItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CacheUrlItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAntiInfoLeakRulesRequest(AbstractModel):
    """DescribeAntiInfoLeakRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _ActionType: 动作类型
        :type ActionType: int
        :param _PageInfo: 翻页
        :type PageInfo: :class:`tencentcloud.waf.v20180125.models.PageInfo`
        """
        self._Domain = None
        self._ActionType = None
        self._PageInfo = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def PageInfo(self):
        return self._PageInfo

    @PageInfo.setter
    def PageInfo(self, PageInfo):
        self._PageInfo = PageInfo


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._ActionType = params.get("ActionType")
        if params.get("PageInfo") is not None:
            self._PageInfo = PageInfo()
            self._PageInfo._deserialize(params.get("PageInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiInfoLeakRulesResponse(AbstractModel):
    """DescribeAntiInfoLeakRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录条数
        :type TotalCount: str
        :param _RuleList: 规则列表
        :type RuleList: list of DescribeAntiInfoLeakRulesRuleItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RuleList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = DescribeAntiInfoLeakRulesRuleItem()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAntiInfoLeakRulesRuleItem(AbstractModel):
    """DescribeAntiInfoLeakRules返回的规则列表元素

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Name: 规则名称
        :type Name: str
        :param _Status: 规则状态
        :type Status: str
        :param _ActionType: 规则动作类型
        :type ActionType: str
        :param _CreateTime: 规则创建时间
        :type CreateTime: str
        :param _Strategies: 详细的规则
        :type Strategies: list of DescribeAntiInfoLeakRulesStrategyItem
        """
        self._RuleId = None
        self._Name = None
        self._Status = None
        self._ActionType = None
        self._CreateTime = None
        self._Strategies = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ActionType = params.get("ActionType")
        self._CreateTime = params.get("CreateTime")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = DescribeAntiInfoLeakRulesStrategyItem()
                obj._deserialize(item)
                self._Strategies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiInfoLeakRulesStrategyItem(AbstractModel):
    """DescribeAntiInfoLeakRules返回的规则元素中的具体的规则元素

    """

    def __init__(self):
        r"""
        :param _Field: 字段
        :type Field: str
        :param _CompareFunc: 条件
        :type CompareFunc: str
        :param _Content: 内容
        :type Content: str
        """
        self._Field = None
        self._CompareFunc = None
        self._Content = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def CompareFunc(self):
        return self._CompareFunc

    @CompareFunc.setter
    def CompareFunc(self, CompareFunc):
        self._CompareFunc = CompareFunc

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._CompareFunc = params.get("CompareFunc")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiInfoLeakageRulesRequest(AbstractModel):
    """DescribeAntiInfoLeakageRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiInfoLeakageRulesResponse(AbstractModel):
    """DescribeAntiInfoLeakageRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 记录条数
        :type Total: int
        :param _RuleList: 规则列表
        :type RuleList: list of DescribeAntiLeakageItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RuleList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = DescribeAntiLeakageItem()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAntiLeakageItem(AbstractModel):
    """出参

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Name: 名称
        :type Name: str
        :param _Status: 状态值
        :type Status: int
        :param _Action: 动作
        :type Action: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Strategies: 匹配条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Strategies: list of DescribeAntiInfoLeakRulesStrategyItem
        :param _Uri: 匹配的URL
注意：此字段可能返回 null，表示取不到有效值。
        :type Uri: str
        """
        self._RuleId = None
        self._Name = None
        self._Status = None
        self._Action = None
        self._CreateTime = None
        self._Strategies = None
        self._Uri = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Action = params.get("Action")
        self._CreateTime = params.get("CreateTime")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = DescribeAntiInfoLeakRulesStrategyItem()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._Uri = params.get("Uri")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttackOverviewRequest(AbstractModel):
    """DescribeAttackOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTime: 查询开始时间
        :type FromTime: str
        :param _ToTime: 查询结束时间
        :type ToTime: str
        :param _Appid: 客户的Appid
        :type Appid: int
        :param _Domain: 被查询的域名
        :type Domain: str
        :param _Edition: 只有两个值有效，sparta-waf，clb-waf，不传则不过滤
        :type Edition: str
        :param _InstanceID: WAF实例ID，不传则不过滤
        :type InstanceID: str
        """
        self._FromTime = None
        self._ToTime = None
        self._Appid = None
        self._Domain = None
        self._Edition = None
        self._InstanceID = None

    @property
    def FromTime(self):
        return self._FromTime

    @FromTime.setter
    def FromTime(self, FromTime):
        self._FromTime = FromTime

    @property
    def ToTime(self):
        return self._ToTime

    @ToTime.setter
    def ToTime(self, ToTime):
        self._ToTime = ToTime

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._FromTime = params.get("FromTime")
        self._ToTime = params.get("ToTime")
        self._Appid = params.get("Appid")
        self._Domain = params.get("Domain")
        self._Edition = params.get("Edition")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttackOverviewResponse(AbstractModel):
    """DescribeAttackOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessCount: 访问请求总数
        :type AccessCount: int
        :param _AttackCount: Web攻击总数
        :type AttackCount: int
        :param _ACLCount: 访问控制总数
        :type ACLCount: int
        :param _CCCount: CC攻击总数
        :type CCCount: int
        :param _BotCount: Bot攻击总数
        :type BotCount: int
        :param _ApiAssetsCount: api资产总数
        :type ApiAssetsCount: int
        :param _ApiRiskEventCount: api风险事件数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiRiskEventCount: int
        :param _IPBlackCount: 黑名单总数
注意：此字段可能返回 null，表示取不到有效值。
        :type IPBlackCount: int
        :param _TamperCount: 防篡改总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TamperCount: int
        :param _LeakCount: 信息泄露总数
注意：此字段可能返回 null，表示取不到有效值。
        :type LeakCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessCount = None
        self._AttackCount = None
        self._ACLCount = None
        self._CCCount = None
        self._BotCount = None
        self._ApiAssetsCount = None
        self._ApiRiskEventCount = None
        self._IPBlackCount = None
        self._TamperCount = None
        self._LeakCount = None
        self._RequestId = None

    @property
    def AccessCount(self):
        return self._AccessCount

    @AccessCount.setter
    def AccessCount(self, AccessCount):
        self._AccessCount = AccessCount

    @property
    def AttackCount(self):
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount

    @property
    def ACLCount(self):
        return self._ACLCount

    @ACLCount.setter
    def ACLCount(self, ACLCount):
        self._ACLCount = ACLCount

    @property
    def CCCount(self):
        return self._CCCount

    @CCCount.setter
    def CCCount(self, CCCount):
        self._CCCount = CCCount

    @property
    def BotCount(self):
        return self._BotCount

    @BotCount.setter
    def BotCount(self, BotCount):
        self._BotCount = BotCount

    @property
    def ApiAssetsCount(self):
        return self._ApiAssetsCount

    @ApiAssetsCount.setter
    def ApiAssetsCount(self, ApiAssetsCount):
        self._ApiAssetsCount = ApiAssetsCount

    @property
    def ApiRiskEventCount(self):
        return self._ApiRiskEventCount

    @ApiRiskEventCount.setter
    def ApiRiskEventCount(self, ApiRiskEventCount):
        self._ApiRiskEventCount = ApiRiskEventCount

    @property
    def IPBlackCount(self):
        return self._IPBlackCount

    @IPBlackCount.setter
    def IPBlackCount(self, IPBlackCount):
        self._IPBlackCount = IPBlackCount

    @property
    def TamperCount(self):
        return self._TamperCount

    @TamperCount.setter
    def TamperCount(self, TamperCount):
        self._TamperCount = TamperCount

    @property
    def LeakCount(self):
        return self._LeakCount

    @LeakCount.setter
    def LeakCount(self, LeakCount):
        self._LeakCount = LeakCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccessCount = params.get("AccessCount")
        self._AttackCount = params.get("AttackCount")
        self._ACLCount = params.get("ACLCount")
        self._CCCount = params.get("CCCount")
        self._BotCount = params.get("BotCount")
        self._ApiAssetsCount = params.get("ApiAssetsCount")
        self._ApiRiskEventCount = params.get("ApiRiskEventCount")
        self._IPBlackCount = params.get("IPBlackCount")
        self._TamperCount = params.get("TamperCount")
        self._LeakCount = params.get("LeakCount")
        self._RequestId = params.get("RequestId")


class DescribeAutoDenyIPRequest(AbstractModel):
    """DescribeAutoDenyIP请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Ip: 查询IP自动封禁状态
        :type Ip: str
        :param _Count: 计数标识
        :type Count: int
        :param _Category: 类别
        :type Category: str
        :param _VtsMin: 有效时间最小时间戳
        :type VtsMin: int
        :param _VtsMax: 有效时间最大时间戳
        :type VtsMax: int
        :param _CtsMin: 创建时间最小时间戳
        :type CtsMin: int
        :param _CtsMax: 创建时间最大时间戳
        :type CtsMax: int
        :param _Skip: 偏移量
        :type Skip: int
        :param _Limit: 限制条数
        :type Limit: int
        :param _Name: 策略名字
        :type Name: str
        :param _Sort: 排序参数
        :type Sort: str
        """
        self._Domain = None
        self._Ip = None
        self._Count = None
        self._Category = None
        self._VtsMin = None
        self._VtsMax = None
        self._CtsMin = None
        self._CtsMax = None
        self._Skip = None
        self._Limit = None
        self._Name = None
        self._Sort = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def VtsMin(self):
        return self._VtsMin

    @VtsMin.setter
    def VtsMin(self, VtsMin):
        self._VtsMin = VtsMin

    @property
    def VtsMax(self):
        return self._VtsMax

    @VtsMax.setter
    def VtsMax(self, VtsMax):
        self._VtsMax = VtsMax

    @property
    def CtsMin(self):
        return self._CtsMin

    @CtsMin.setter
    def CtsMin(self, CtsMin):
        self._CtsMin = CtsMin

    @property
    def CtsMax(self):
        return self._CtsMax

    @CtsMax.setter
    def CtsMax(self, CtsMax):
        self._CtsMax = CtsMax

    @property
    def Skip(self):
        return self._Skip

    @Skip.setter
    def Skip(self, Skip):
        self._Skip = Skip

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Ip = params.get("Ip")
        self._Count = params.get("Count")
        self._Category = params.get("Category")
        self._VtsMin = params.get("VtsMin")
        self._VtsMax = params.get("VtsMax")
        self._CtsMin = params.get("CtsMin")
        self._CtsMax = params.get("CtsMax")
        self._Skip = params.get("Skip")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoDenyIPResponse(AbstractModel):
    """DescribeAutoDenyIP返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询IP封禁状态返回结果
        :type Data: :class:`tencentcloud.waf.v20180125.models.IpHitItemsData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = IpHitItemsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeBatchIpAccessControlRequest(AbstractModel):
    """DescribeBatchIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选条件，支持 ActionType 40/42，Ip：ip地址，Domain：域名三类
        :type Filters: list of FiltersItemNew
        :param _OffSet: 偏移
        :type OffSet: int
        :param _Limit: 限制
        :type Limit: int
        :param _Sort: 排序参数
        :type Sort: str
        """
        self._Filters = None
        self._OffSet = None
        self._Limit = None
        self._Sort = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OffSet(self):
        return self._OffSet

    @OffSet.setter
    def OffSet(self, OffSet):
        self._OffSet = OffSet

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FiltersItemNew()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OffSet = params.get("OffSet")
        self._Limit = params.get("Limit")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchIpAccessControlResponse(AbstractModel):
    """DescribeBatchIpAccessControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 输出
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.BatchIpAccessControlData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = BatchIpAccessControlData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCCRuleListRequest(AbstractModel):
    """DescribeCCRuleList请求参数结构体

    """


class DescribeCCRuleListResponse(AbstractModel):
    """DescribeCCRuleList返回参数结构体

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


class DescribeCCRuleRequest(AbstractModel):
    """DescribeCCRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Offset: 页码
        :type Offset: int
        :param _Limit: 页的数目
        :type Limit: int
        :param _Sort: 排序参数
        :type Sort: str
        :param _Edition: clb-waf 或者 sparta-waf
        :type Edition: str
        :param _Name: 过滤条件
        :type Name: str
        """
        self._Domain = None
        self._Offset = None
        self._Limit = None
        self._Sort = None
        self._Edition = None
        self._Name = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Sort = params.get("Sort")
        self._Edition = params.get("Edition")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCRuleResponse(AbstractModel):
    """DescribeCCRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.CCRuleData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = CCRuleData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCertificateVerifyResultRequest(AbstractModel):
    """DescribeCertificateVerifyResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertType: 证书类型
        :type CertType: int
        :param _Certificate: 证书公钥
        :type Certificate: str
        :param _CertID: 证书ID
        :type CertID: str
        :param _PrivateKey: 私钥信息
        :type PrivateKey: str
        """
        self._Domain = None
        self._CertType = None
        self._Certificate = None
        self._CertID = None
        self._PrivateKey = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def CertID(self):
        return self._CertID

    @CertID.setter
    def CertID(self, CertID):
        self._CertID = CertID

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertType = params.get("CertType")
        self._Certificate = params.get("Certificate")
        self._CertID = params.get("CertID")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateVerifyResultResponse(AbstractModel):
    """DescribeCertificateVerifyResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态码
        :type Status: int
        :param _Detail: 错误详情
        :type Detail: list of str
        :param _NotAfter: 过期时间
        :type NotAfter: str
        :param _Changed: 证书是否改变:1有改变，0没有改变
注意：此字段可能返回 null，表示取不到有效值。
        :type Changed: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Detail = None
        self._NotAfter = None
        self._Changed = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def NotAfter(self):
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def Changed(self):
        return self._Changed

    @Changed.setter
    def Changed(self, Changed):
        self._Changed = Changed

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Detail = params.get("Detail")
        self._NotAfter = params.get("NotAfter")
        self._Changed = params.get("Changed")
        self._RequestId = params.get("RequestId")


class DescribeCiphersDetailRequest(AbstractModel):
    """DescribeCiphersDetail请求参数结构体

    """


class DescribeCiphersDetailResponse(AbstractModel):
    """DescribeCiphersDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ciphers: 加密套件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Ciphers: list of TLSCiphers
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ciphers = None
        self._RequestId = None

    @property
    def Ciphers(self):
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ciphers") is not None:
            self._Ciphers = []
            for item in params.get("Ciphers"):
                obj = TLSCiphers()
                obj._deserialize(item)
                self._Ciphers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomRuleListRequest(AbstractModel):
    """DescribeCustomRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Offset: 偏移
        :type Offset: int
        :param _Limit: 容量
        :type Limit: int
        :param _Filters: 过滤数组,name可以是如下的值： RuleID,RuleName,Match
        :type Filters: list of FiltersItemNew
        :param _Order: asc或者desc
        :type Order: str
        :param _By: exp_ts或者mod_ts
        :type By: str
        """
        self._Domain = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._By = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FiltersItemNew()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomRuleListResponse(AbstractModel):
    """DescribeCustomRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleList: 规则详情
        :type RuleList: list of DescribeCustomRulesRspRuleListItem
        :param _TotalCount: 规则条数
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = DescribeCustomRulesRspRuleListItem()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCustomRulesRspRuleListItem(AbstractModel):
    """DescribeCustomRules接口回包中的复杂类型

    """

    def __init__(self):
        r"""
        :param _ActionType: 动作类型
        :type ActionType: str
        :param _Bypass: 跳过的策略
        :type Bypass: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _Name: 策略名称
        :type Name: str
        :param _Redirect: 重定向地址
        :type Redirect: str
        :param _RuleId: 策略ID
        :type RuleId: str
        :param _SortId: 优先级
        :type SortId: str
        :param _Status: 状态
        :type Status: str
        :param _Strategies: 策略详情
        :type Strategies: list of Strategy
        :param _EventId: 事件id
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        """
        self._ActionType = None
        self._Bypass = None
        self._CreateTime = None
        self._ExpireTime = None
        self._Name = None
        self._Redirect = None
        self._RuleId = None
        self._SortId = None
        self._Status = None
        self._Strategies = None
        self._EventId = None

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Bypass(self):
        return self._Bypass

    @Bypass.setter
    def Bypass(self, Bypass):
        self._Bypass = Bypass

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Redirect(self):
        return self._Redirect

    @Redirect.setter
    def Redirect(self, Redirect):
        self._Redirect = Redirect

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._Bypass = params.get("Bypass")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Name = params.get("Name")
        self._Redirect = params.get("Redirect")
        self._RuleId = params.get("RuleId")
        self._SortId = params.get("SortId")
        self._Status = params.get("Status")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = Strategy()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomWhiteRuleRequest(AbstractModel):
    """DescribeCustomWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 容量
        :type Limit: int
        :param _Filters: 过滤数组,name可以是如下的值： RuleID,RuleName,Match
        :type Filters: list of FiltersItemNew
        :param _Order: asc或者desc
        :type Order: str
        :param _By: exp_ts或者mod_ts
        :type By: str
        """
        self._Domain = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._By = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FiltersItemNew()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomWhiteRuleResponse(AbstractModel):
    """DescribeCustomWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleList: 规则详情
        :type RuleList: list of DescribeCustomRulesRspRuleListItem
        :param _TotalCount: 规则条数
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = DescribeCustomRulesRspRuleListItem()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDomainCountInfoRequest(AbstractModel):
    """DescribeDomainCountInfo请求参数结构体

    """


class DescribeDomainCountInfoResponse(AbstractModel):
    """DescribeDomainCountInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllDomain: 域名总数
        :type AllDomain: int
        :param _UpdateTime: 最近发现时间
        :type UpdateTime: str
        :param _WafDomainCount: 接入域名总数
        :type WafDomainCount: int
        :param _LeftDomainCount: 剩下配额
        :type LeftDomainCount: int
        :param _OpenWafDomain: 开启防护域名数
        :type OpenWafDomain: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllDomain = None
        self._UpdateTime = None
        self._WafDomainCount = None
        self._LeftDomainCount = None
        self._OpenWafDomain = None
        self._RequestId = None

    @property
    def AllDomain(self):
        return self._AllDomain

    @AllDomain.setter
    def AllDomain(self, AllDomain):
        self._AllDomain = AllDomain

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def WafDomainCount(self):
        return self._WafDomainCount

    @WafDomainCount.setter
    def WafDomainCount(self, WafDomainCount):
        self._WafDomainCount = WafDomainCount

    @property
    def LeftDomainCount(self):
        return self._LeftDomainCount

    @LeftDomainCount.setter
    def LeftDomainCount(self, LeftDomainCount):
        self._LeftDomainCount = LeftDomainCount

    @property
    def OpenWafDomain(self):
        return self._OpenWafDomain

    @OpenWafDomain.setter
    def OpenWafDomain(self, OpenWafDomain):
        self._OpenWafDomain = OpenWafDomain

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllDomain = params.get("AllDomain")
        self._UpdateTime = params.get("UpdateTime")
        self._WafDomainCount = params.get("WafDomainCount")
        self._LeftDomainCount = params.get("LeftDomainCount")
        self._OpenWafDomain = params.get("OpenWafDomain")
        self._RequestId = params.get("RequestId")


class DescribeDomainDetailsClbRequest(AbstractModel):
    """DescribeDomainDetailsClb请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名id
        :type DomainId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._Domain = None
        self._DomainId = None
        self._InstanceId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainDetailsClbResponse(AbstractModel):
    """DescribeDomainDetailsClb返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainsClbPartInfo: clb域名详情
        :type DomainsClbPartInfo: :class:`tencentcloud.waf.v20180125.models.ClbDomainsInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainsClbPartInfo = None
        self._RequestId = None

    @property
    def DomainsClbPartInfo(self):
        return self._DomainsClbPartInfo

    @DomainsClbPartInfo.setter
    def DomainsClbPartInfo(self, DomainsClbPartInfo):
        self._DomainsClbPartInfo = DomainsClbPartInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainsClbPartInfo") is not None:
            self._DomainsClbPartInfo = ClbDomainsInfo()
            self._DomainsClbPartInfo._deserialize(params.get("DomainsClbPartInfo"))
        self._RequestId = params.get("RequestId")


class DescribeDomainDetailsSaasRequest(AbstractModel):
    """DescribeDomainDetailsSaas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名id
        :type DomainId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        """
        self._Domain = None
        self._DomainId = None
        self._InstanceId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainDetailsSaasResponse(AbstractModel):
    """DescribeDomainDetailsSaas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainsPartInfo: 域名详情
        :type DomainsPartInfo: :class:`tencentcloud.waf.v20180125.models.DomainsPartInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainsPartInfo = None
        self._RequestId = None

    @property
    def DomainsPartInfo(self):
        return self._DomainsPartInfo

    @DomainsPartInfo.setter
    def DomainsPartInfo(self, DomainsPartInfo):
        self._DomainsPartInfo = DomainsPartInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainsPartInfo") is not None:
            self._DomainsPartInfo = DomainsPartInfo()
            self._DomainsPartInfo._deserialize(params.get("DomainsPartInfo"))
        self._RequestId = params.get("RequestId")


class DescribeDomainRulesRequest(AbstractModel):
    """DescribeDomainRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要查询的域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainRulesResponse(AbstractModel):
    """DescribeDomainRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表详情
        :type Rules: list of Rule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainVerifyResultRequest(AbstractModel):
    """DescribeDomainVerifyResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _InstanceID: 实例id
        :type InstanceID: str
        """
        self._Domain = None
        self._InstanceID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainVerifyResultResponse(AbstractModel):
    """DescribeDomainVerifyResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 结果描述；如果可以添加返回空字符串
        :type Msg: str
        :param _VerifyCode: 检验状态：0表示可以添加，大于0为不能添加
        :type VerifyCode: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._VerifyCode = None
        self._RequestId = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def VerifyCode(self):
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._VerifyCode = params.get("VerifyCode")
        self._RequestId = params.get("RequestId")


class DescribeDomainWhiteRulesRequest(AbstractModel):
    """DescribeDomainWhiteRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要查询的域名
        :type Domain: str
        :param _Url: 请求的白名单匹配路径
        :type Url: str
        :param _Page: 翻到多少页
        :type Page: int
        :param _Count: 每页展示的条数
        :type Count: int
        :param _Sort: 排序方式,desc表示降序，asc表示升序
        :type Sort: str
        :param _RuleId: 规则ID
        :type RuleId: str
        """
        self._Domain = None
        self._Url = None
        self._Page = None
        self._Count = None
        self._Sort = None
        self._RuleId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._Page = params.get("Page")
        self._Count = params.get("Count")
        self._Sort = params.get("Sort")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainWhiteRulesResponse(AbstractModel):
    """DescribeDomainWhiteRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleList: 规则列表
        :type RuleList: list of RuleList
        :param _Total: 规则的数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleList = None
        self._Total = None
        self._RequestId = None

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = RuleList()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，取Limit整数倍。最小值为0，最大值= Total/Limit向上取整
        :type Offset: int
        :param _Limit: 返回域名的数量
        :type Limit: int
        :param _Filters: 过滤数组
        :type Filters: list of FiltersItemNew
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FiltersItemNew()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Domains: domain列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of DomainInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Domains = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DomainInfo()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFindDomainListRequest(AbstractModel):
    """DescribeFindDomainList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页
        :type Offset: int
        :param _Limit: 每页容量
        :type Limit: int
        :param _Key: 过滤条件
        :type Key: str
        :param _IsWafDomain: 是否接入waf
        :type IsWafDomain: str
        :param _By: 排序参数
        :type By: str
        :param _Order: 排序方式
        :type Order: str
        """
        self._Offset = None
        self._Limit = None
        self._Key = None
        self._IsWafDomain = None
        self._By = None
        self._Order = None

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
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def IsWafDomain(self):
        return self._IsWafDomain

    @IsWafDomain.setter
    def IsWafDomain(self, IsWafDomain):
        self._IsWafDomain = IsWafDomain

    @property
    def By(self):
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Key = params.get("Key")
        self._IsWafDomain = params.get("IsWafDomain")
        self._By = params.get("By")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFindDomainListResponse(AbstractModel):
    """DescribeFindDomainList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 域名总数
        :type Total: int
        :param _List: 域名信息列表
        :type List: list of FindAllDomainDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = FindAllDomainDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowTrendRequest(AbstractModel):
    """DescribeFlowTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要获取流量趋势的域名, all表示所有域名
        :type Domain: str
        :param _StartTs: 起始时间戳，精度秒
        :type StartTs: int
        :param _EndTs: 结束时间戳，精度秒
        :type EndTs: int
        """
        self._Domain = None
        self._StartTs = None
        self._EndTs = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTs(self):
        return self._StartTs

    @StartTs.setter
    def StartTs(self, StartTs):
        self._StartTs = StartTs

    @property
    def EndTs(self):
        return self._EndTs

    @EndTs.setter
    def EndTs(self, EndTs):
        self._EndTs = EndTs


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartTs = params.get("StartTs")
        self._EndTs = params.get("EndTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowTrendResponse(AbstractModel):
    """DescribeFlowTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 流量趋势数据
        :type Data: list of BotStatPointItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BotStatPointItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostLimitRequest(AbstractModel):
    """DescribeHostLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 添加的域名
        :type Domain: str
        :param _InstanceID: 实例id
        :type InstanceID: str
        :param _AlbType: 流量来源
        :type AlbType: str
        """
        self._Domain = None
        self._InstanceID = None
        self._AlbType = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def AlbType(self):
        return self._AlbType

    @AlbType.setter
    def AlbType(self, AlbType):
        self._AlbType = AlbType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._InstanceID = params.get("InstanceID")
        self._AlbType = params.get("AlbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostLimitResponse(AbstractModel):
    """DescribeHostLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功返回的状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DescribeHostRequest(AbstractModel):
    """DescribeHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        """
        self._Domain = None
        self._DomainId = None
        self._InstanceID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostResponse(AbstractModel):
    """DescribeHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Host: 域名详情
        :type Host: :class:`tencentcloud.waf.v20180125.models.HostRecord`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Host = None
        self._RequestId = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Host") is not None:
            self._Host = HostRecord()
            self._Host._deserialize(params.get("Host"))
        self._RequestId = params.get("RequestId")


class DescribeHostsRequest(AbstractModel):
    """DescribeHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 防护域名，如果是要查询某一具体的防护域名则传入此参数，要求是准确的域名，此参数不支持模糊搜索
        :type Domain: str
        :param _DomainId: 防护域名ID，如果是要查询某一具体的防护域名则传入此参数，要求是准确的域名ID，此参数不支持模糊搜索
        :type DomainId: str
        :param _Search: 搜索条件，根据此参数对域名做模糊搜索
        :type Search: str
        :param _Item: 复杂的搜索条件
        :type Item: :class:`tencentcloud.waf.v20180125.models.SearchItem`
        :param _InstanceID: 实例id
        :type InstanceID: str
        """
        self._Domain = None
        self._DomainId = None
        self._Search = None
        self._Item = None
        self._InstanceID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Search(self):
        return self._Search

    @Search.setter
    def Search(self, Search):
        self._Search = Search

    @property
    def Item(self):
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Search = params.get("Search")
        if params.get("Item") is not None:
            self._Item = SearchItem()
            self._Item._deserialize(params.get("Item"))
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsResponse(AbstractModel):
    """DescribeHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 防护域名列表的长度
        :type TotalCount: int
        :param _HostList: 防护域名的列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HostList: list of HostRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HostList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HostList(self):
        return self._HostList

    @HostList.setter
    def HostList(self, HostList):
        self._HostList = HostList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("HostList") is not None:
            self._HostList = []
            for item in params.get("HostList"):
                obj = HostRecord()
                obj._deserialize(item)
                self._HostList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 容量
        :type Limit: int
        :param _Filters: 过滤数组
        :type Filters: list of FiltersItemNew
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FiltersItemNew()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Instances: instance列表
        :type Instances: list of InstanceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Instances = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpAccessControlRequest(AbstractModel):
    """DescribeIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Count: 计数标识
        :type Count: int
        :param _ActionType: 动作，40表示查询白名单，42表示查询黑名单
        :type ActionType: int
        :param _VtsMin: 最小有效时间的时间戳
        :type VtsMin: int
        :param _VtsMax: 最大有效时间的时间戳
        :type VtsMax: int
        :param _CtsMin: 最小创建时间的时间戳
        :type CtsMin: int
        :param _CtsMax: 最大创建时间的时间戳
        :type CtsMax: int
        :param _OffSet: 分页开始条数
        :type OffSet: int
        :param _Limit: 每页的条数
        :type Limit: int
        :param _Source: 来源
        :type Source: str
        :param _Sort: 排序参数
        :type Sort: str
        :param _Ip: ip
        :type Ip: str
        :param _ValidStatus: 生效状态
        :type ValidStatus: int
        """
        self._Domain = None
        self._Count = None
        self._ActionType = None
        self._VtsMin = None
        self._VtsMax = None
        self._CtsMin = None
        self._CtsMax = None
        self._OffSet = None
        self._Limit = None
        self._Source = None
        self._Sort = None
        self._Ip = None
        self._ValidStatus = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def VtsMin(self):
        return self._VtsMin

    @VtsMin.setter
    def VtsMin(self, VtsMin):
        self._VtsMin = VtsMin

    @property
    def VtsMax(self):
        return self._VtsMax

    @VtsMax.setter
    def VtsMax(self, VtsMax):
        self._VtsMax = VtsMax

    @property
    def CtsMin(self):
        return self._CtsMin

    @CtsMin.setter
    def CtsMin(self, CtsMin):
        self._CtsMin = CtsMin

    @property
    def CtsMax(self):
        return self._CtsMax

    @CtsMax.setter
    def CtsMax(self, CtsMax):
        self._CtsMax = CtsMax

    @property
    def OffSet(self):
        return self._OffSet

    @OffSet.setter
    def OffSet(self, OffSet):
        self._OffSet = OffSet

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ValidStatus(self):
        return self._ValidStatus

    @ValidStatus.setter
    def ValidStatus(self, ValidStatus):
        self._ValidStatus = ValidStatus


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Count = params.get("Count")
        self._ActionType = params.get("ActionType")
        self._VtsMin = params.get("VtsMin")
        self._VtsMax = params.get("VtsMax")
        self._CtsMin = params.get("CtsMin")
        self._CtsMax = params.get("CtsMax")
        self._OffSet = params.get("OffSet")
        self._Limit = params.get("Limit")
        self._Source = params.get("Source")
        self._Sort = params.get("Sort")
        self._Ip = params.get("Ip")
        self._ValidStatus = params.get("ValidStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpAccessControlResponse(AbstractModel):
    """DescribeIpAccessControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 输出
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.IpAccessControlData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = IpAccessControlData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeIpHitItemsRequest(AbstractModel):
    """DescribeIpHitItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Count: 计数标识
        :type Count: int
        :param _Category: 类别
        :type Category: str
        :param _VtsMin: 有效时间最小时间戳
        :type VtsMin: int
        :param _VtsMax: 有效时间最大时间戳
        :type VtsMax: int
        :param _CtsMin: 创建时间最小时间戳
        :type CtsMin: int
        :param _CtsMax: 创建时间最大时间戳
        :type CtsMax: int
        :param _Skip: 偏移参数
        :type Skip: int
        :param _Limit: 限制数目
        :type Limit: int
        :param _Name: 策略名称
        :type Name: str
        :param _Sort: 排序参数
        :type Sort: str
        :param _Ip: IP
        :type Ip: str
        """
        self._Domain = None
        self._Count = None
        self._Category = None
        self._VtsMin = None
        self._VtsMax = None
        self._CtsMin = None
        self._CtsMax = None
        self._Skip = None
        self._Limit = None
        self._Name = None
        self._Sort = None
        self._Ip = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def VtsMin(self):
        return self._VtsMin

    @VtsMin.setter
    def VtsMin(self, VtsMin):
        self._VtsMin = VtsMin

    @property
    def VtsMax(self):
        return self._VtsMax

    @VtsMax.setter
    def VtsMax(self, VtsMax):
        self._VtsMax = VtsMax

    @property
    def CtsMin(self):
        return self._CtsMin

    @CtsMin.setter
    def CtsMin(self, CtsMin):
        self._CtsMin = CtsMin

    @property
    def CtsMax(self):
        return self._CtsMax

    @CtsMax.setter
    def CtsMax(self, CtsMax):
        self._CtsMax = CtsMax

    @property
    def Skip(self):
        return self._Skip

    @Skip.setter
    def Skip(self, Skip):
        self._Skip = Skip

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Count = params.get("Count")
        self._Category = params.get("Category")
        self._VtsMin = params.get("VtsMin")
        self._VtsMax = params.get("VtsMax")
        self._CtsMin = params.get("CtsMin")
        self._CtsMax = params.get("CtsMax")
        self._Skip = params.get("Skip")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        self._Sort = params.get("Sort")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpHitItemsResponse(AbstractModel):
    """DescribeIpHitItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.IpHitItemsData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = IpHitItemsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribePeakPointsRequest(AbstractModel):
    """DescribePeakPoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTime: 查询起始时间
        :type FromTime: str
        :param _ToTime: 查询终止时间
        :type ToTime: str
        :param _Domain: 查询的域名，如果查询所有域名数据，该参数不填写
        :type Domain: str
        :param _Edition: 只有两个值有效，sparta-waf，clb-waf，不传则不过滤
        :type Edition: str
        :param _InstanceID: WAF实例ID，不传则不过滤
        :type InstanceID: str
        :param _MetricName: 十一个值可选：
access-峰值qps趋势图
botAccess- bot峰值qps趋势图
down-下行峰值带宽趋势图
up-上行峰值带宽趋势图
attack-Web攻击总数趋势图
cc-CC攻击总数趋势图
bw-黑IP攻击总数趋势图
tamper-防篡改攻击总数趋势图
leak-防泄露攻击总数趋势图
acl-访问控制攻击总数趋势图
http_status-状态码各次数趋势图
        :type MetricName: str
        """
        self._FromTime = None
        self._ToTime = None
        self._Domain = None
        self._Edition = None
        self._InstanceID = None
        self._MetricName = None

    @property
    def FromTime(self):
        return self._FromTime

    @FromTime.setter
    def FromTime(self, FromTime):
        self._FromTime = FromTime

    @property
    def ToTime(self):
        return self._ToTime

    @ToTime.setter
    def ToTime(self, ToTime):
        self._ToTime = ToTime

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName


    def _deserialize(self, params):
        self._FromTime = params.get("FromTime")
        self._ToTime = params.get("ToTime")
        self._Domain = params.get("Domain")
        self._Edition = params.get("Edition")
        self._InstanceID = params.get("InstanceID")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakPointsResponse(AbstractModel):
    """DescribePeakPoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Points: 数据点
        :type Points: list of PeakPointsItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Points = None
        self._RequestId = None

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = PeakPointsItem()
                obj._deserialize(item)
                self._Points.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePeakValueRequest(AbstractModel):
    """DescribePeakValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FromTime: 查询起始时间
        :type FromTime: str
        :param _ToTime: 查询结束时间
        :type ToTime: str
        :param _Domain: 需要查询的域名，当前用户所有域名可以不传
        :type Domain: str
        :param _Edition: 只有两个值有效，sparta-waf，clb-waf，不传则不过滤
        :type Edition: str
        :param _InstanceID: WAF实例ID，不传则不过滤
        :type InstanceID: str
        :param _MetricName: 五个值可选：
access-峰值qps
down-下行峰值带宽
up-上行峰值带宽
attack-Web攻击总数
cc-CC攻击总数趋势图
        :type MetricName: str
        """
        self._FromTime = None
        self._ToTime = None
        self._Domain = None
        self._Edition = None
        self._InstanceID = None
        self._MetricName = None

    @property
    def FromTime(self):
        return self._FromTime

    @FromTime.setter
    def FromTime(self, FromTime):
        self._FromTime = FromTime

    @property
    def ToTime(self):
        return self._ToTime

    @ToTime.setter
    def ToTime(self, ToTime):
        self._ToTime = ToTime

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName


    def _deserialize(self, params):
        self._FromTime = params.get("FromTime")
        self._ToTime = params.get("ToTime")
        self._Domain = params.get("Domain")
        self._Edition = params.get("Edition")
        self._InstanceID = params.get("InstanceID")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakValueResponse(AbstractModel):
    """DescribePeakValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Access: QPS峰值
        :type Access: int
        :param _Up: 上行带宽峰值，单位B
        :type Up: int
        :param _Down: 下行带宽峰值，单位B
        :type Down: int
        :param _Attack: Web攻击总数
        :type Attack: int
        :param _Cc: CC攻击总数
        :type Cc: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Access = None
        self._Up = None
        self._Down = None
        self._Attack = None
        self._Cc = None
        self._RequestId = None

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Up(self):
        return self._Up

    @Up.setter
    def Up(self, Up):
        self._Up = Up

    @property
    def Down(self):
        return self._Down

    @Down.setter
    def Down(self, Down):
        self._Down = Down

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Cc(self):
        return self._Cc

    @Cc.setter
    def Cc(self, Cc):
        self._Cc = Cc

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Access = params.get("Access")
        self._Up = params.get("Up")
        self._Down = params.get("Down")
        self._Attack = params.get("Attack")
        self._Cc = params.get("Cc")
        self._RequestId = params.get("RequestId")


class DescribePolicyStatusRequest(AbstractModel):
    """DescribePolicyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Edition: clb-waf或者saas-waf
        :type Edition: str
        """
        self._Domain = None
        self._Edition = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyStatusResponse(AbstractModel):
    """DescribePolicyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Status: 防护状态
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Status = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribePortsRequest(AbstractModel):
    """DescribePorts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Edition: 实例类型
        :type Edition: str
        """
        self._InstanceID = None
        self._Edition = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePortsResponse(AbstractModel):
    """DescribePorts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HttpPorts: http端口列表
        :type HttpPorts: list of str
        :param _HttpsPorts: https端口列表
        :type HttpsPorts: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HttpPorts = None
        self._HttpsPorts = None
        self._RequestId = None

    @property
    def HttpPorts(self):
        return self._HttpPorts

    @HttpPorts.setter
    def HttpPorts(self, HttpPorts):
        self._HttpPorts = HttpPorts

    @property
    def HttpsPorts(self):
        return self._HttpsPorts

    @HttpsPorts.setter
    def HttpsPorts(self, HttpsPorts):
        self._HttpsPorts = HttpsPorts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HttpPorts = params.get("HttpPorts")
        self._HttpsPorts = params.get("HttpsPorts")
        self._RequestId = params.get("RequestId")


class DescribeRuleLimitRequest(AbstractModel):
    """DescribeRuleLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        """
        self._Domain = None
        self._InstanceId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleLimitResponse(AbstractModel):
    """DescribeRuleLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Res: waf模块的规格
        :type Res: :class:`tencentcloud.waf.v20180125.models.WafRuleLimit`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Res = None
        self._RequestId = None

    @property
    def Res(self):
        return self._Res

    @Res.setter
    def Res(self, Res):
        self._Res = Res

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Res") is not None:
            self._Res = WafRuleLimit()
            self._Res._deserialize(params.get("Res"))
        self._RequestId = params.get("RequestId")


class DescribeSessionRequest(AbstractModel):
    """DescribeSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Edition: clb-waf或者sparta-waf
        :type Edition: str
        """
        self._Domain = None
        self._Edition = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionResponse(AbstractModel):
    """DescribeSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.SessionData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = SessionData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTlsVersionRequest(AbstractModel):
    """DescribeTlsVersion请求参数结构体

    """


class DescribeTlsVersionResponse(AbstractModel):
    """DescribeTlsVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TLS: TLS key value
        :type TLS: list of TLSVersion
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TLS = None
        self._RequestId = None

    @property
    def TLS(self):
        return self._TLS

    @TLS.setter
    def TLS(self, TLS):
        self._TLS = TLS

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TLS") is not None:
            self._TLS = []
            for item in params.get("TLS"):
                obj = TLSVersion()
                obj._deserialize(item)
                self._TLS.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserCdcClbWafRegionsRequest(AbstractModel):
    """DescribeUserCdcClbWafRegions请求参数结构体

    """


class DescribeUserCdcClbWafRegionsResponse(AbstractModel):
    """DescribeUserCdcClbWafRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: CdcRegion的类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CdcRegion
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CdcRegion()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserClbWafRegionsRequest(AbstractModel):
    """DescribeUserClbWafRegions请求参数结构体

    """


class DescribeUserClbWafRegionsResponse(AbstractModel):
    """DescribeUserClbWafRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 地域（标准的ap-格式）列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeUserDomainInfoRequest(AbstractModel):
    """DescribeUserDomainInfo请求参数结构体

    """


class DescribeUserDomainInfoResponse(AbstractModel):
    """DescribeUserDomainInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsersInfo: saas和clb域名信息
        :type UsersInfo: list of UserDomainInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsersInfo = None
        self._RequestId = None

    @property
    def UsersInfo(self):
        return self._UsersInfo

    @UsersInfo.setter
    def UsersInfo(self, UsersInfo):
        self._UsersInfo = UsersInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UsersInfo") is not None:
            self._UsersInfo = []
            for item in params.get("UsersInfo"):
                obj = UserDomainInfo()
                obj._deserialize(item)
                self._UsersInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserSignatureRuleRequest(AbstractModel):
    """DescribeUserSignatureRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要查询的域名
        :type Domain: str
        :param _Offset: 分页
        :type Offset: int
        :param _Limit: 每页容量
        :type Limit: int
        :param _By: 排序字段，支持 signature_id, modify_time
        :type By: str
        :param _Order: 排序方式
        :type Order: str
        :param _Filters: 筛选条件，支持 MainClassName，SubClassID ,CveID, Status, ID;  ID为规则id
        :type Filters: list of FiltersItemNew
        """
        self._Domain = None
        self._Offset = None
        self._Limit = None
        self._By = None
        self._Order = None
        self._Filters = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
    def By(self):
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._By = params.get("By")
        self._Order = params.get("Order")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FiltersItemNew()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserSignatureRuleResponse(AbstractModel):
    """DescribeUserSignatureRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 规则总数
        :type Total: int
        :param _Rules: 规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of UserSignatureRule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Rules = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = UserSignatureRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVipInfoRequest(AbstractModel):
    """DescribeVipInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: waf实例id列表
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVipInfoResponse(AbstractModel):
    """DescribeVipInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VipInfo: VIP信息
        :type VipInfo: list of VipInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VipInfo = None
        self._RequestId = None

    @property
    def VipInfo(self):
        return self._VipInfo

    @VipInfo.setter
    def VipInfo(self, VipInfo):
        self._VipInfo = VipInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VipInfo") is not None:
            self._VipInfo = []
            for item in params.get("VipInfo"):
                obj = VipInfo()
                obj._deserialize(item)
                self._VipInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWafAutoDenyRulesRequest(AbstractModel):
    """DescribeWafAutoDenyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        """
        self._Domain = None
        self._InstanceId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafAutoDenyRulesResponse(AbstractModel):
    """DescribeWafAutoDenyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttackThreshold: 攻击次数阈值
        :type AttackThreshold: int
        :param _TimeThreshold: 攻击时间阈值
        :type TimeThreshold: int
        :param _DenyTimeThreshold: 自动封禁时间
        :type DenyTimeThreshold: int
        :param _DefenseStatus: 自动封禁状态
        :type DefenseStatus: int
        :param _HWState: 重保护网域名状态
        :type HWState: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttackThreshold = None
        self._TimeThreshold = None
        self._DenyTimeThreshold = None
        self._DefenseStatus = None
        self._HWState = None
        self._RequestId = None

    @property
    def AttackThreshold(self):
        return self._AttackThreshold

    @AttackThreshold.setter
    def AttackThreshold(self, AttackThreshold):
        self._AttackThreshold = AttackThreshold

    @property
    def TimeThreshold(self):
        return self._TimeThreshold

    @TimeThreshold.setter
    def TimeThreshold(self, TimeThreshold):
        self._TimeThreshold = TimeThreshold

    @property
    def DenyTimeThreshold(self):
        return self._DenyTimeThreshold

    @DenyTimeThreshold.setter
    def DenyTimeThreshold(self, DenyTimeThreshold):
        self._DenyTimeThreshold = DenyTimeThreshold

    @property
    def DefenseStatus(self):
        return self._DefenseStatus

    @DefenseStatus.setter
    def DefenseStatus(self, DefenseStatus):
        self._DefenseStatus = DefenseStatus

    @property
    def HWState(self):
        return self._HWState

    @HWState.setter
    def HWState(self, HWState):
        self._HWState = HWState

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AttackThreshold = params.get("AttackThreshold")
        self._TimeThreshold = params.get("TimeThreshold")
        self._DenyTimeThreshold = params.get("DenyTimeThreshold")
        self._DefenseStatus = params.get("DefenseStatus")
        self._HWState = params.get("HWState")
        self._RequestId = params.get("RequestId")


class DescribeWafAutoDenyStatusRequest(AbstractModel):
    """DescribeWafAutoDenyStatus请求参数结构体

    """


class DescribeWafAutoDenyStatusResponse(AbstractModel):
    """DescribeWafAutoDenyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WafAutoDenyDetails: WAF 自动封禁详情
        :type WafAutoDenyDetails: :class:`tencentcloud.waf.v20180125.models.AutoDenyDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WafAutoDenyDetails = None
        self._RequestId = None

    @property
    def WafAutoDenyDetails(self):
        return self._WafAutoDenyDetails

    @WafAutoDenyDetails.setter
    def WafAutoDenyDetails(self, WafAutoDenyDetails):
        self._WafAutoDenyDetails = WafAutoDenyDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WafAutoDenyDetails") is not None:
            self._WafAutoDenyDetails = AutoDenyDetail()
            self._WafAutoDenyDetails._deserialize(params.get("WafAutoDenyDetails"))
        self._RequestId = params.get("RequestId")


class DescribeWafInfoRequest(AbstractModel):
    """DescribeWafInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Params: CLB回调WAF接口（获取、删除）的参数
        :type Params: list of ClbHostsParams
        """
        self._Params = None

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ClbHostsParams()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafInfoResponse(AbstractModel):
    """DescribeWafInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回的WAF信息数组的长度，为0则表示没有查询到对应的信息
        :type Total: int
        :param _HostList: 对应的WAF信息的数组。
        :type HostList: list of ClbHostResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._HostList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def HostList(self):
        return self._HostList

    @HostList.setter
    def HostList(self, HostList):
        self._HostList = HostList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("HostList") is not None:
            self._HostList = []
            for item in params.get("HostList"):
                obj = ClbHostResult()
                obj._deserialize(item)
                self._HostList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWafThreatenIntelligenceRequest(AbstractModel):
    """DescribeWafThreatenIntelligence请求参数结构体

    """


class DescribeWafThreatenIntelligenceResponse(AbstractModel):
    """DescribeWafThreatenIntelligence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WafThreatenIntelligenceDetails: WAF 威胁情报封禁信息
        :type WafThreatenIntelligenceDetails: :class:`tencentcloud.waf.v20180125.models.WafThreatenIntelligenceDetails`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WafThreatenIntelligenceDetails = None
        self._RequestId = None

    @property
    def WafThreatenIntelligenceDetails(self):
        return self._WafThreatenIntelligenceDetails

    @WafThreatenIntelligenceDetails.setter
    def WafThreatenIntelligenceDetails(self, WafThreatenIntelligenceDetails):
        self._WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WafThreatenIntelligenceDetails") is not None:
            self._WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails()
            self._WafThreatenIntelligenceDetails._deserialize(params.get("WafThreatenIntelligenceDetails"))
        self._RequestId = params.get("RequestId")


class DomainInfo(AbstractModel):
    """domain列表

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Cname: cname地址
        :type Cname: str
        :param _Edition: 实例类型,sparta-waf表示saaswaf实例域名,clb-waf表示clbwaf实例域名,cdc-clb-waf表示CDC环境下clbwaf实例域名,cdn-waf表示cdnwaf实例域名
        :type Edition: str
        :param _Region: 地域
        :type Region: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _ClsStatus: 日志包
        :type ClsStatus: int
        :param _FlowMode: clbwaf使用模式,0镜像模式 1清洗模式
        :type FlowMode: int
        :param _Status: waf开关,0关闭 1开启
        :type Status: int
        :param _Mode: 规则引擎防护模式,0观察模式 1拦截模式
        :type Mode: int
        :param _Engine: 规则引擎和AI引擎防护模式联合状态,10规则引擎观察&&AI引擎关闭模式 11规则引擎观察&&AI引擎观察模式 12规则引擎观察&&AI引擎拦截模式 20规则引擎拦截&&AI引擎关闭模式 21规则引擎拦截&&AI引擎观察模式 22规则引擎拦截&&AI引擎拦截模式
        :type Engine: int
        :param _CCList: CC列表
        :type CCList: list of str
        :param _RsList: 回源ip
        :type RsList: list of str
        :param _Ports: 服务端口配置
        :type Ports: list of PortInfo
        :param _LoadBalancerSet: 负载均衡器
        :type LoadBalancerSet: list of LoadBalancerPackageNew
        :param _AppId: 用户id
        :type AppId: int
        :param _State: clbwaf域名监听器状态,0操作成功 4正在绑定LB 6正在解绑LB 7解绑LB失败 8绑定LB失败 10内部错误
        :type State: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Ipv6Status: Ipv6开关状态,0关闭 1开启
        :type Ipv6Status: int
        :param _BotStatus: BOT开关状态,0关闭 1开启
        :type BotStatus: int
        :param _Level: 版本信息
        :type Level: int
        :param _PostCLSStatus: 是否开启投递CLS功能,0关闭 1开启
        :type PostCLSStatus: int
        :param _PostCKafkaStatus: 是否开启投递CKafka功能,0关闭 1开启
        :type PostCKafkaStatus: int
        :param _CdcClusters: cdc实例域名接入的集群信息,非cdc实例忽略
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcClusters: str
        :param _ApiStatus: api安全开关状态,0关闭 1开启
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiStatus: int
        :param _AlbType: 应用型负载均衡类型,clb或者apisix，默认clb
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbType: str
        :param _SgState: 安全组状态,0不展示 1非腾讯云源站 2安全组绑定失败 3安全组发生变更
注意：此字段可能返回 null，表示取不到有效值。
        :type SgState: int
        :param _SgDetail: 安全组状态的详细解释
注意：此字段可能返回 null，表示取不到有效值。
        :type SgDetail: str
        :param _CloudType: 域名类型:hybrid表示混合云域名，public表示公有云域名
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudType: str
        """
        self._Domain = None
        self._DomainId = None
        self._InstanceId = None
        self._Cname = None
        self._Edition = None
        self._Region = None
        self._InstanceName = None
        self._ClsStatus = None
        self._FlowMode = None
        self._Status = None
        self._Mode = None
        self._Engine = None
        self._CCList = None
        self._RsList = None
        self._Ports = None
        self._LoadBalancerSet = None
        self._AppId = None
        self._State = None
        self._CreateTime = None
        self._Ipv6Status = None
        self._BotStatus = None
        self._Level = None
        self._PostCLSStatus = None
        self._PostCKafkaStatus = None
        self._CdcClusters = None
        self._ApiStatus = None
        self._AlbType = None
        self._SgState = None
        self._SgDetail = None
        self._CloudType = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClsStatus(self):
        return self._ClsStatus

    @ClsStatus.setter
    def ClsStatus(self, ClsStatus):
        self._ClsStatus = ClsStatus

    @property
    def FlowMode(self):
        return self._FlowMode

    @FlowMode.setter
    def FlowMode(self, FlowMode):
        self._FlowMode = FlowMode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def CCList(self):
        return self._CCList

    @CCList.setter
    def CCList(self, CCList):
        self._CCList = CCList

    @property
    def RsList(self):
        return self._RsList

    @RsList.setter
    def RsList(self, RsList):
        self._RsList = RsList

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def LoadBalancerSet(self):
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Ipv6Status(self):
        return self._Ipv6Status

    @Ipv6Status.setter
    def Ipv6Status(self, Ipv6Status):
        self._Ipv6Status = Ipv6Status

    @property
    def BotStatus(self):
        return self._BotStatus

    @BotStatus.setter
    def BotStatus(self, BotStatus):
        self._BotStatus = BotStatus

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def PostCLSStatus(self):
        return self._PostCLSStatus

    @PostCLSStatus.setter
    def PostCLSStatus(self, PostCLSStatus):
        self._PostCLSStatus = PostCLSStatus

    @property
    def PostCKafkaStatus(self):
        return self._PostCKafkaStatus

    @PostCKafkaStatus.setter
    def PostCKafkaStatus(self, PostCKafkaStatus):
        self._PostCKafkaStatus = PostCKafkaStatus

    @property
    def CdcClusters(self):
        return self._CdcClusters

    @CdcClusters.setter
    def CdcClusters(self, CdcClusters):
        self._CdcClusters = CdcClusters

    @property
    def ApiStatus(self):
        return self._ApiStatus

    @ApiStatus.setter
    def ApiStatus(self, ApiStatus):
        self._ApiStatus = ApiStatus

    @property
    def AlbType(self):
        return self._AlbType

    @AlbType.setter
    def AlbType(self, AlbType):
        self._AlbType = AlbType

    @property
    def SgState(self):
        return self._SgState

    @SgState.setter
    def SgState(self, SgState):
        self._SgState = SgState

    @property
    def SgDetail(self):
        return self._SgDetail

    @SgDetail.setter
    def SgDetail(self, SgDetail):
        self._SgDetail = SgDetail

    @property
    def CloudType(self):
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceId = params.get("InstanceId")
        self._Cname = params.get("Cname")
        self._Edition = params.get("Edition")
        self._Region = params.get("Region")
        self._InstanceName = params.get("InstanceName")
        self._ClsStatus = params.get("ClsStatus")
        self._FlowMode = params.get("FlowMode")
        self._Status = params.get("Status")
        self._Mode = params.get("Mode")
        self._Engine = params.get("Engine")
        self._CCList = params.get("CCList")
        self._RsList = params.get("RsList")
        if params.get("Ports") is not None:
            self._Ports = []
            for item in params.get("Ports"):
                obj = PortInfo()
                obj._deserialize(item)
                self._Ports.append(obj)
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancerPackageNew()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._AppId = params.get("AppId")
        self._State = params.get("State")
        self._CreateTime = params.get("CreateTime")
        self._Ipv6Status = params.get("Ipv6Status")
        self._BotStatus = params.get("BotStatus")
        self._Level = params.get("Level")
        self._PostCLSStatus = params.get("PostCLSStatus")
        self._PostCKafkaStatus = params.get("PostCKafkaStatus")
        self._CdcClusters = params.get("CdcClusters")
        self._ApiStatus = params.get("ApiStatus")
        self._AlbType = params.get("AlbType")
        self._SgState = params.get("SgState")
        self._SgDetail = params.get("SgDetail")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainPackageNew(AbstractModel):
    """clb-waf 域名扩展套餐

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param _ValidTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidTime: str
        :param _RenewFlag: 是否自动续费，1：自动续费，0：不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _Count: 套餐购买个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Region: 套餐购买地域，clb-waf暂时没有用到
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._ResourceIds = None
        self._ValidTime = None
        self._RenewFlag = None
        self._Count = None
        self._Region = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ValidTime(self):
        return self._ValidTime

    @ValidTime.setter
    def ValidTime(self, ValidTime):
        self._ValidTime = ValidTime

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._ValidTime = params.get("ValidTime")
        self._RenewFlag = params.get("RenewFlag")
        self._Count = params.get("Count")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainURI(AbstractModel):
    """唯一定位Domain

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Edition: 版本
        :type Edition: str
        """
        self._Domain = None
        self._Edition = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainsPartInfo(AbstractModel):
    """saas域名详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名id
        :type DomainId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Edition: 类型
        :type Edition: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _Cert: 证书
        :type Cert: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Engine: AI防御模式
        :type Engine: int
        :param _HttpsRewrite: 是否开启httpRewrite
        :type HttpsRewrite: int
        :param _HttpsUpstreamPort: https回源端口
        :type HttpsUpstreamPort: str
        :param _IsCdn: 是否是cdn
        :type IsCdn: int
        :param _IsGray: 是否开启gray
        :type IsGray: int
        :param _IsHttp2: 是否是http2
        :type IsHttp2: int
        :param _IsWebsocket: 是否开启websocket
        :type IsWebsocket: int
        :param _LoadBalance: 负载均衡
        :type LoadBalance: int
        :param _Mode: 防御模式
        :type Mode: int
        :param _PrivateKey: 私钥
        :type PrivateKey: str
        :param _SSLId: ssl id
        :type SSLId: str
        :param _UpstreamDomain: 回源域名
        :type UpstreamDomain: str
        :param _UpstreamType: 回源类型
        :type UpstreamType: int
        :param _SrcList: 回源ip
        :type SrcList: list of str
        :param _Ports: 服务端口配置
        :type Ports: list of PortInfo
        :param _CertType: 证书类型
        :type CertType: int
        :param _UpstreamScheme: 回源方式
        :type UpstreamScheme: str
        :param _Cls: 日志包
        :type Cls: int
        :param _Cname: 一级cname
        :type Cname: str
        :param _IsKeepAlive: 是否长连接
        :type IsKeepAlive: int
        :param _ActiveCheck: 是否开启主动健康检测，1表示开启，0表示不开启
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveCheck: int
        :param _TLSVersion: TLS版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TLSVersion: int
        :param _Ciphers: 加密套件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Ciphers: list of int
        :param _CipherTemplate: 模板
注意：此字段可能返回 null，表示取不到有效值。
        :type CipherTemplate: int
        :param _ProxyReadTimeout: 300s
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyReadTimeout: int
        :param _ProxySendTimeout: 300s
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxySendTimeout: int
        :param _SniType: 0:关闭SNI；1:开启SNI，SNI=源请求host；2:开启SNI，SNI=修改为源站host；3：开启SNI，自定义host，SNI=SniHost；
注意：此字段可能返回 null，表示取不到有效值。
        :type SniType: int
        :param _SniHost: SniType=3时，需要填此参数，表示自定义的host；
注意：此字段可能返回 null，表示取不到有效值。
        :type SniHost: str
        :param _Weights: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Weights: list of str
        :param _IpHeaders: IsCdn=3时，表示自定义header
注意：此字段可能返回 null，表示取不到有效值。
        :type IpHeaders: list of str
        :param _XFFReset: 0:关闭xff重置；1:开启xff重置
注意：此字段可能返回 null，表示取不到有效值。
        :type XFFReset: int
        """
        self._Domain = None
        self._DomainId = None
        self._InstanceId = None
        self._Edition = None
        self._InstanceName = None
        self._Cert = None
        self._CreateTime = None
        self._Engine = None
        self._HttpsRewrite = None
        self._HttpsUpstreamPort = None
        self._IsCdn = None
        self._IsGray = None
        self._IsHttp2 = None
        self._IsWebsocket = None
        self._LoadBalance = None
        self._Mode = None
        self._PrivateKey = None
        self._SSLId = None
        self._UpstreamDomain = None
        self._UpstreamType = None
        self._SrcList = None
        self._Ports = None
        self._CertType = None
        self._UpstreamScheme = None
        self._Cls = None
        self._Cname = None
        self._IsKeepAlive = None
        self._ActiveCheck = None
        self._TLSVersion = None
        self._Ciphers = None
        self._CipherTemplate = None
        self._ProxyReadTimeout = None
        self._ProxySendTimeout = None
        self._SniType = None
        self._SniHost = None
        self._Weights = None
        self._IpHeaders = None
        self._XFFReset = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def HttpsRewrite(self):
        return self._HttpsRewrite

    @HttpsRewrite.setter
    def HttpsRewrite(self, HttpsRewrite):
        self._HttpsRewrite = HttpsRewrite

    @property
    def HttpsUpstreamPort(self):
        return self._HttpsUpstreamPort

    @HttpsUpstreamPort.setter
    def HttpsUpstreamPort(self, HttpsUpstreamPort):
        self._HttpsUpstreamPort = HttpsUpstreamPort

    @property
    def IsCdn(self):
        return self._IsCdn

    @IsCdn.setter
    def IsCdn(self, IsCdn):
        self._IsCdn = IsCdn

    @property
    def IsGray(self):
        return self._IsGray

    @IsGray.setter
    def IsGray(self, IsGray):
        self._IsGray = IsGray

    @property
    def IsHttp2(self):
        return self._IsHttp2

    @IsHttp2.setter
    def IsHttp2(self, IsHttp2):
        self._IsHttp2 = IsHttp2

    @property
    def IsWebsocket(self):
        return self._IsWebsocket

    @IsWebsocket.setter
    def IsWebsocket(self, IsWebsocket):
        self._IsWebsocket = IsWebsocket

    @property
    def LoadBalance(self):
        return self._LoadBalance

    @LoadBalance.setter
    def LoadBalance(self, LoadBalance):
        self._LoadBalance = LoadBalance

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def UpstreamDomain(self):
        return self._UpstreamDomain

    @UpstreamDomain.setter
    def UpstreamDomain(self, UpstreamDomain):
        self._UpstreamDomain = UpstreamDomain

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def SrcList(self):
        return self._SrcList

    @SrcList.setter
    def SrcList(self, SrcList):
        self._SrcList = SrcList

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def UpstreamScheme(self):
        return self._UpstreamScheme

    @UpstreamScheme.setter
    def UpstreamScheme(self, UpstreamScheme):
        self._UpstreamScheme = UpstreamScheme

    @property
    def Cls(self):
        return self._Cls

    @Cls.setter
    def Cls(self, Cls):
        self._Cls = Cls

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def IsKeepAlive(self):
        return self._IsKeepAlive

    @IsKeepAlive.setter
    def IsKeepAlive(self, IsKeepAlive):
        self._IsKeepAlive = IsKeepAlive

    @property
    def ActiveCheck(self):
        return self._ActiveCheck

    @ActiveCheck.setter
    def ActiveCheck(self, ActiveCheck):
        self._ActiveCheck = ActiveCheck

    @property
    def TLSVersion(self):
        return self._TLSVersion

    @TLSVersion.setter
    def TLSVersion(self, TLSVersion):
        self._TLSVersion = TLSVersion

    @property
    def Ciphers(self):
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def CipherTemplate(self):
        return self._CipherTemplate

    @CipherTemplate.setter
    def CipherTemplate(self, CipherTemplate):
        self._CipherTemplate = CipherTemplate

    @property
    def ProxyReadTimeout(self):
        return self._ProxyReadTimeout

    @ProxyReadTimeout.setter
    def ProxyReadTimeout(self, ProxyReadTimeout):
        self._ProxyReadTimeout = ProxyReadTimeout

    @property
    def ProxySendTimeout(self):
        return self._ProxySendTimeout

    @ProxySendTimeout.setter
    def ProxySendTimeout(self, ProxySendTimeout):
        self._ProxySendTimeout = ProxySendTimeout

    @property
    def SniType(self):
        return self._SniType

    @SniType.setter
    def SniType(self, SniType):
        self._SniType = SniType

    @property
    def SniHost(self):
        return self._SniHost

    @SniHost.setter
    def SniHost(self, SniHost):
        self._SniHost = SniHost

    @property
    def Weights(self):
        return self._Weights

    @Weights.setter
    def Weights(self, Weights):
        self._Weights = Weights

    @property
    def IpHeaders(self):
        return self._IpHeaders

    @IpHeaders.setter
    def IpHeaders(self, IpHeaders):
        self._IpHeaders = IpHeaders

    @property
    def XFFReset(self):
        return self._XFFReset

    @XFFReset.setter
    def XFFReset(self, XFFReset):
        self._XFFReset = XFFReset


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceId = params.get("InstanceId")
        self._Edition = params.get("Edition")
        self._InstanceName = params.get("InstanceName")
        self._Cert = params.get("Cert")
        self._CreateTime = params.get("CreateTime")
        self._Engine = params.get("Engine")
        self._HttpsRewrite = params.get("HttpsRewrite")
        self._HttpsUpstreamPort = params.get("HttpsUpstreamPort")
        self._IsCdn = params.get("IsCdn")
        self._IsGray = params.get("IsGray")
        self._IsHttp2 = params.get("IsHttp2")
        self._IsWebsocket = params.get("IsWebsocket")
        self._LoadBalance = params.get("LoadBalance")
        self._Mode = params.get("Mode")
        self._PrivateKey = params.get("PrivateKey")
        self._SSLId = params.get("SSLId")
        self._UpstreamDomain = params.get("UpstreamDomain")
        self._UpstreamType = params.get("UpstreamType")
        self._SrcList = params.get("SrcList")
        if params.get("Ports") is not None:
            self._Ports = []
            for item in params.get("Ports"):
                obj = PortInfo()
                obj._deserialize(item)
                self._Ports.append(obj)
        self._CertType = params.get("CertType")
        self._UpstreamScheme = params.get("UpstreamScheme")
        self._Cls = params.get("Cls")
        self._Cname = params.get("Cname")
        self._IsKeepAlive = params.get("IsKeepAlive")
        self._ActiveCheck = params.get("ActiveCheck")
        self._TLSVersion = params.get("TLSVersion")
        self._Ciphers = params.get("Ciphers")
        self._CipherTemplate = params.get("CipherTemplate")
        self._ProxyReadTimeout = params.get("ProxyReadTimeout")
        self._ProxySendTimeout = params.get("ProxySendTimeout")
        self._SniType = params.get("SniType")
        self._SniHost = params.get("SniHost")
        self._Weights = params.get("Weights")
        self._IpHeaders = params.get("IpHeaders")
        self._XFFReset = params.get("XFFReset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadAttackRecordInfo(AbstractModel):
    """下载攻击日志记录数据项

    """

    def __init__(self):
        r"""
        :param _Id: 记录ID
        :type Id: int
        :param _TaskName: 下载任务名
        :type TaskName: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _Host: 域名
        :type Host: str
        :param _Count: 当前下载任务的日志条数
        :type Count: int
        :param _Status: 下载任务运行状态：-1-下载超时，0-下载等待，1-下载完成，2-下载失败，4-正在下载
        :type Status: int
        :param _Url: 下载文件URL
        :type Url: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 最后更新修改时间
        :type ModifyTime: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _TotalCount: 下载任务需下载的日志总条数
        :type TotalCount: int
        """
        self._Id = None
        self._TaskName = None
        self._TaskId = None
        self._Host = None
        self._Count = None
        self._Status = None
        self._Url = None
        self._CreateTime = None
        self._ModifyTime = None
        self._ExpireTime = None
        self._TotalCount = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TaskName = params.get("TaskName")
        self._TaskId = params.get("TaskId")
        self._Host = params.get("Host")
        self._Count = params.get("Count")
        self._Status = params.get("Status")
        self._Url = params.get("Url")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._ExpireTime = params.get("ExpireTime")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAccessInfo(AbstractModel):
    """DescribeAccessExports接口

    """

    def __init__(self):
        r"""
        :param _ExportId: 日志导出任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportId: str
        :param _Query: 日志导出查询语句
注意：此字段可能返回 null，表示取不到有效值。
        :type Query: str
        :param _FileName: 日志导出文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 日志文件大小
        :type FileSize: int
        :param _Order: 日志导出时间排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: str
        :param _Format: 日志导出格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param _Count: 日志导出数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Status: 日志下载状态。Processing:导出正在进行中，Complete:导出完成，Failed:导出失败，Expired:日志导出已过期（三天有效期）
        :type Status: str
        :param _From: 日志导出起始时间
        :type From: int
        :param _To: 日志导出结束时间
        :type To: int
        :param _CosPath: 日志导出路径
        :type CosPath: str
        :param _CreateTime: 日志导出创建时间
        :type CreateTime: str
        """
        self._ExportId = None
        self._Query = None
        self._FileName = None
        self._FileSize = None
        self._Order = None
        self._Format = None
        self._Count = None
        self._Status = None
        self._From = None
        self._To = None
        self._CosPath = None
        self._CreateTime = None

    @property
    def ExportId(self):
        return self._ExportId

    @ExportId.setter
    def ExportId(self, ExportId):
        self._ExportId = ExportId

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def CosPath(self):
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ExportId = params.get("ExportId")
        self._Query = params.get("Query")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        self._Count = params.get("Count")
        self._Status = params.get("Status")
        self._From = params.get("From")
        self._To = params.get("To")
        self._CosPath = params.get("CosPath")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FiltersItemNew(AbstractModel):
    """过滤数组

    """

    def __init__(self):
        r"""
        :param _Name: 字段名
        :type Name: str
        :param _Values: 过滤值
        :type Values: list of str
        :param _ExactMatch: 是否精确查找
        :type ExactMatch: bool
        """
        self._Name = None
        self._Values = None
        self._ExactMatch = None

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

    @property
    def ExactMatch(self):
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FindAllDomainDetail(AbstractModel):
    """域名列表

    """

    def __init__(self):
        r"""
        :param _Appid: 用户id
        :type Appid: int
        :param _Domain: 域名
        :type Domain: str
        :param _Ips: 域名ip
        :type Ips: list of str
        :param _FindTime: 发现时间
        :type FindTime: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _DomainId: 域名id
        :type DomainId: str
        :param _Edition: waf类型
        :type Edition: str
        :param _IsWafDomain: 是否接入waf
        :type IsWafDomain: int
        """
        self._Appid = None
        self._Domain = None
        self._Ips = None
        self._FindTime = None
        self._InstanceId = None
        self._DomainId = None
        self._Edition = None
        self._IsWafDomain = None

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def FindTime(self):
        return self._FindTime

    @FindTime.setter
    def FindTime(self, FindTime):
        self._FindTime = FindTime

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def IsWafDomain(self):
        return self._IsWafDomain

    @IsWafDomain.setter
    def IsWafDomain(self, IsWafDomain):
        self._IsWafDomain = IsWafDomain


    def _deserialize(self, params):
        self._Appid = params.get("Appid")
        self._Domain = params.get("Domain")
        self._Ips = params.get("Ips")
        self._FindTime = params.get("FindTime")
        self._InstanceId = params.get("InstanceId")
        self._DomainId = params.get("DomainId")
        self._Edition = params.get("Edition")
        self._IsWafDomain = params.get("IsWafDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FraudPkg(AbstractModel):
    """业务安全资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _InquireNum: 申请数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InquireNum: int
        :param _UsedNum: 使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedNum: int
        :param _RenewFlag: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        """
        self._ResourceIds = None
        self._Status = None
        self._Region = None
        self._BeginTime = None
        self._EndTime = None
        self._InquireNum = None
        self._UsedNum = None
        self._RenewFlag = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InquireNum(self):
        return self._InquireNum

    @InquireNum.setter
    def InquireNum(self, InquireNum):
        self._InquireNum = InquireNum

    @property
    def UsedNum(self):
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._InquireNum = params.get("InquireNum")
        self._UsedNum = params.get("UsedNum")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreshAntiFakeUrlRequest(AbstractModel):
    """FreshAntiFakeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Id: Id
        :type Id: int
        """
        self._Domain = None
        self._Id = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreshAntiFakeUrlResponse(AbstractModel):
    """FreshAntiFakeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果成功与否
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class GenerateDealsAndPayNewRequest(AbstractModel):
    """GenerateDealsAndPayNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Goods: 计费下单入参
        :type Goods: list of GoodNews
        """
        self._Goods = None

    @property
    def Goods(self):
        return self._Goods

    @Goods.setter
    def Goods(self, Goods):
        self._Goods = Goods


    def _deserialize(self, params):
        if params.get("Goods") is not None:
            self._Goods = []
            for item in params.get("Goods"):
                obj = GoodNews()
                obj._deserialize(item)
                self._Goods.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDealsAndPayNewResponse(AbstractModel):
    """GenerateDealsAndPayNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 计费下单响应结构体
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.waf.v20180125.models.DealData`
        :param _Status: 1:成功，0:失败
        :type Status: int
        :param _ReturnMessage: 返回message
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnMessage: str
        :param _InstanceId: 购买的实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._ReturnMessage = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReturnMessage(self):
        return self._ReturnMessage

    @ReturnMessage.setter
    def ReturnMessage(self, ReturnMessage):
        self._ReturnMessage = ReturnMessage

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
        if params.get("Data") is not None:
            self._Data = DealData()
            self._Data._deserialize(params.get("Data"))
        self._Status = params.get("Status")
        self._ReturnMessage = params.get("ReturnMessage")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class GetAttackDownloadRecordsRequest(AbstractModel):
    """GetAttackDownloadRecords请求参数结构体

    """


class GetAttackDownloadRecordsResponse(AbstractModel):
    """GetAttackDownloadRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 下载攻击日志记录数组
        :type Records: list of DownloadAttackRecordInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._RequestId = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = DownloadAttackRecordInfo()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class GetAttackHistogramRequest(AbstractModel):
    """GetAttackHistogram请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 查询的域名，所有域名使用all
        :type Domain: str
        :param _StartTime: 查询起始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _QueryString: Lucene语法
        :type QueryString: str
        """
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._QueryString = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryString = params.get("QueryString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttackHistogramResponse(AbstractModel):
    """GetAttackHistogram返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 统计详情
        :type Data: list of LogHistogramInfo
        :param _Period: 时间段大小
        :type Period: int
        :param _TotalCount: 统计的条目数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Period = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LogHistogramInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Period = params.get("Period")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetAttackTotalCountRequest(AbstractModel):
    """GetAttackTotalCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Domain: 查询的域名，全部域名不指定
        :type Domain: str
        :param _QueryString: 查询条件，默认为""
        :type QueryString: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Domain = None
        self._QueryString = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domain = params.get("Domain")
        self._QueryString = params.get("QueryString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAttackTotalCountResponse(AbstractModel):
    """GetAttackTotalCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 攻击总次数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetInstanceQpsLimitRequest(AbstractModel):
    """GetInstanceQpsLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 套餐实例id
        :type InstanceId: str
        :param _Type: 套餐类型
        :type Type: str
        """
        self._InstanceId = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetInstanceQpsLimitResponse(AbstractModel):
    """GetInstanceQpsLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QpsData: 弹性qps相关值集合
        :type QpsData: :class:`tencentcloud.waf.v20180125.models.QpsData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QpsData = None
        self._RequestId = None

    @property
    def QpsData(self):
        return self._QpsData

    @QpsData.setter
    def QpsData(self, QpsData):
        self._QpsData = QpsData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QpsData") is not None:
            self._QpsData = QpsData()
            self._QpsData._deserialize(params.get("QpsData"))
        self._RequestId = params.get("RequestId")


class GoodNews(AbstractModel):
    """计费下单接口出入参Goods

    """

    def __init__(self):
        r"""
        :param _GoodsNum: 商品数量
        :type GoodsNum: int
        :param _GoodsDetail: 商品明细
        :type GoodsDetail: :class:`tencentcloud.waf.v20180125.models.GoodsDetailNew`
        :param _GoodsCategoryId: 订单类型ID，用来唯一标识一个业务的一种场景（总共三种场景：新购、配置变更、续费）
高级版: 102375(新购),102376(续费),102377(变配)
企业版 : 102378(新购),102379(续费),102380(变配)
旗舰版 : 102369(新购),102370(续费),102371(变配)
域名包 : 102372(新购),102373(续费),102374(变配)
业务扩展包 : 101040(新购),101041(续费),101042(变配)

高级版-CLB: 新购 101198  续费 101199 变配 101200
企业版-CLB 101204(新购),101205(续费),101206(变配)
旗舰版-CLB : 101201(新购),101202(续费),101203(变配)
域名包-CLB: 101207(新购),101208(续费),101209(变配)
业务扩展包-CLB: 101210(新购),101211(续费),101212(变配)

注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsCategoryId: int
        :param _RegionId: 购买waf实例区域ID
1 表示购买大陆资源;
9表示购买非中国大陆资源
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        """
        self._GoodsNum = None
        self._GoodsDetail = None
        self._GoodsCategoryId = None
        self._RegionId = None

    @property
    def GoodsNum(self):
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def GoodsDetail(self):
        return self._GoodsDetail

    @GoodsDetail.setter
    def GoodsDetail(self, GoodsDetail):
        self._GoodsDetail = GoodsDetail

    @property
    def GoodsCategoryId(self):
        return self._GoodsCategoryId

    @GoodsCategoryId.setter
    def GoodsCategoryId(self, GoodsCategoryId):
        self._GoodsCategoryId = GoodsCategoryId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._GoodsNum = params.get("GoodsNum")
        if params.get("GoodsDetail") is not None:
            self._GoodsDetail = GoodsDetailNew()
            self._GoodsDetail._deserialize(params.get("GoodsDetail"))
        self._GoodsCategoryId = params.get("GoodsCategoryId")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GoodsDetailNew(AbstractModel):
    """产品明细

    """

    def __init__(self):
        r"""
        :param _TimeSpan: 时间间隔
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param _TimeUnit: 单位，支持购买d、m、y 即（日、月、年）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param _SubProductCode: 子产品标签,。新购，续费必传，变配时放在oldConfig newConfig里面

Saas 高级版 ：sp_wsm_waf_premium
Saas企业版 ：sp_wsm_waf_enterprise
Saas旗舰版 ：sp_wsm_waf_ultimate
Saas 业务扩展包：sp_wsm_waf_qpsep
Saas 域名扩展包：sp_wsm_waf_domain

高级版-CLB:sp_wsm_waf_premium_clb
企业版-CLB : sp_wsm_waf_enterprise_clb
旗舰版-CLB:sp_wsm_waf_ultimate_clb
 业务扩展包-CLB：sp_wsm_waf_qpsep_clb
域名扩展包-CLB：sp_wsm_waf_domain_clb

注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductCode: str
        :param _Pid: 业务产品申请的pid（对应一个定价公式），通过pid计费查询到定价模型
高级版 ：1000827
企业版 ：1000830
旗舰版 ：1000832
域名包 : 1000834
业务扩展包 : 1000481
高级版-CLB:1001150
企业版-CLB : 1001152
旗舰版-CLB:1001154
域名包-CLB: 1001156
业务扩展包-CLB : 1001160

注意：此字段可能返回 null，表示取不到有效值。
        :type Pid: int
        :param _InstanceName: waf实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _AutoRenewFlag: 1:自动续费，0:不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _RealRegion: waf购买的实际地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RealRegion: int
        :param _LabelTypes: 计费细项标签数组
Saas 高级版  sv_wsm_waf_package_premium 
Saas 企业版  sv_wsm_waf_package_enterprise
Saas 旗舰版  sv_wsm_waf_package_ultimate 
Saas 非中国大陆高级版  sv_wsm_waf_package_premium_intl
Saas 非中国大陆企业版   sv_wsm_waf_package_enterprise_intl
Saas 非中国大陆旗舰版  sv_wsm_waf_package_ultimate _intl
Saas 业务扩展包  sv_wsm_waf_qps_ep
Saas 域名扩展包  sv_wsm_waf_domain

高级版CLB   sv_wsm_waf_package_premium_clb
企业版CLB  sv_wsm_waf_package_enterprise_clb
旗舰版CLB   sv_wsm_waf_package_ultimate_clb
非中国大陆高级版 CLB sv_wsm_waf_package_premium_clb_intl
非中国大陆企业版CLB   sv_wsm_waf_package_premium_clb_intl
非中国大陆旗舰版CLB  sv_wsm_waf_package_ultimate_clb _intl
业务扩展包CLB sv_wsm_waf_qps_ep_clb
域名扩展包CLB  sv_wsm_waf_domain_clb

注意：此字段可能返回 null，表示取不到有效值。
        :type LabelTypes: list of str
        :param _LabelCounts: 计费细项标签数量，一般和SvLabelType一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCounts: list of int
        :param _CurDeadline: 变配使用，实例到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        :param _InstanceId: 对存在的实例购买bot 或api 安全
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ResourceId: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        """
        self._TimeSpan = None
        self._TimeUnit = None
        self._SubProductCode = None
        self._Pid = None
        self._InstanceName = None
        self._AutoRenewFlag = None
        self._RealRegion = None
        self._LabelTypes = None
        self._LabelCounts = None
        self._CurDeadline = None
        self._InstanceId = None
        self._ResourceId = None

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def SubProductCode(self):
        return self._SubProductCode

    @SubProductCode.setter
    def SubProductCode(self, SubProductCode):
        self._SubProductCode = SubProductCode

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def RealRegion(self):
        return self._RealRegion

    @RealRegion.setter
    def RealRegion(self, RealRegion):
        self._RealRegion = RealRegion

    @property
    def LabelTypes(self):
        return self._LabelTypes

    @LabelTypes.setter
    def LabelTypes(self, LabelTypes):
        self._LabelTypes = LabelTypes

    @property
    def LabelCounts(self):
        return self._LabelCounts

    @LabelCounts.setter
    def LabelCounts(self, LabelCounts):
        self._LabelCounts = LabelCounts

    @property
    def CurDeadline(self):
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._SubProductCode = params.get("SubProductCode")
        self._Pid = params.get("Pid")
        self._InstanceName = params.get("InstanceName")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._RealRegion = params.get("RealRegion")
        self._LabelTypes = params.get("LabelTypes")
        self._LabelCounts = params.get("LabelCounts")
        self._CurDeadline = params.get("CurDeadline")
        self._InstanceId = params.get("InstanceId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostDel(AbstractModel):
    """CLB-WAF删除域名参数

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _InstanceID: 实例类型
        :type InstanceID: str
        """
        self._Domain = None
        self._DomainId = None
        self._InstanceID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostRecord(AbstractModel):
    """clb-waf防护域名

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _MainDomain: 主域名，入参时为空
        :type MainDomain: str
        :param _Mode: 规则引擎防护模式，0 观察模式，1拦截模式
        :type Mode: int
        :param _Status: waf和LD的绑定，0：没有绑定，1：绑定
        :type Status: int
        :param _State: 域名状态，0：正常，1：未检测到流量，2：即将过期，3：过期
        :type State: int
        :param _Engine: 规则引擎和AI引擎防护模式联合状态,10规则引擎观察&&AI引擎关闭模式 11规则引擎观察&&AI引擎观察模式 12规则引擎观察&&AI引擎拦截模式 20规则引擎拦截&&AI引擎关闭模式 21规则引擎拦截&&AI引擎观察模式 22规则引擎拦截&&AI引擎拦截模式
        :type Engine: int
        :param _IsCdn: 是否开启代理，0：不开启，1：开启
        :type IsCdn: int
        :param _LoadBalancerSet: 绑定的LB列表
        :type LoadBalancerSet: list of LoadBalancer
        :param _Region: 域名绑定的LB的地域，以,分割多个地域
        :type Region: str
        :param _Edition: 产品分类，取值为：sparta-waf、clb-waf、cdn-waf
        :type Edition: str
        :param _FlowMode: WAF的流量模式，1：清洗模式，0：镜像模式
        :type FlowMode: int
        :param _ClsStatus: 是否开启访问日志，1：开启，0：关闭
        :type ClsStatus: int
        :param _Level: 防护等级，可选值100,200,300
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _CdcClusters: 域名需要下发到的cdc集群列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcClusters: list of str
        :param _AlbType: 应用型负载均衡类型: clb或者apisix，默认clb
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbType: str
        :param _IpHeaders: IsCdn=3时，需要填此参数，表示自定义header
注意：此字段可能返回 null，表示取不到有效值。
        :type IpHeaders: list of str
        :param _EngineType: 规则引擎类型， 1: menshen,   2:tiga
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineType: int
        :param _CloudType: 云类型:public:公有云；private:私有云;hybrid:混合云
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudType: str
        """
        self._Domain = None
        self._DomainId = None
        self._MainDomain = None
        self._Mode = None
        self._Status = None
        self._State = None
        self._Engine = None
        self._IsCdn = None
        self._LoadBalancerSet = None
        self._Region = None
        self._Edition = None
        self._FlowMode = None
        self._ClsStatus = None
        self._Level = None
        self._CdcClusters = None
        self._AlbType = None
        self._IpHeaders = None
        self._EngineType = None
        self._CloudType = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def MainDomain(self):
        return self._MainDomain

    @MainDomain.setter
    def MainDomain(self, MainDomain):
        self._MainDomain = MainDomain

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def IsCdn(self):
        return self._IsCdn

    @IsCdn.setter
    def IsCdn(self, IsCdn):
        self._IsCdn = IsCdn

    @property
    def LoadBalancerSet(self):
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def FlowMode(self):
        return self._FlowMode

    @FlowMode.setter
    def FlowMode(self, FlowMode):
        self._FlowMode = FlowMode

    @property
    def ClsStatus(self):
        return self._ClsStatus

    @ClsStatus.setter
    def ClsStatus(self, ClsStatus):
        self._ClsStatus = ClsStatus

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def CdcClusters(self):
        return self._CdcClusters

    @CdcClusters.setter
    def CdcClusters(self, CdcClusters):
        self._CdcClusters = CdcClusters

    @property
    def AlbType(self):
        return self._AlbType

    @AlbType.setter
    def AlbType(self, AlbType):
        self._AlbType = AlbType

    @property
    def IpHeaders(self):
        return self._IpHeaders

    @IpHeaders.setter
    def IpHeaders(self, IpHeaders):
        self._IpHeaders = IpHeaders

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def CloudType(self):
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._MainDomain = params.get("MainDomain")
        self._Mode = params.get("Mode")
        self._Status = params.get("Status")
        self._State = params.get("State")
        self._Engine = params.get("Engine")
        self._IsCdn = params.get("IsCdn")
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._Region = params.get("Region")
        self._Edition = params.get("Edition")
        self._FlowMode = params.get("FlowMode")
        self._ClsStatus = params.get("ClsStatus")
        self._Level = params.get("Level")
        self._CdcClusters = params.get("CdcClusters")
        self._AlbType = params.get("AlbType")
        self._IpHeaders = params.get("IpHeaders")
        self._EngineType = params.get("EngineType")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostStatus(AbstractModel):
    """设置WAF状态的结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _Status: WAF的开关，1：开，0：关
        :type Status: int
        :param _InstanceID: 实例ID
        :type InstanceID: str
        """
        self._Domain = None
        self._DomainId = None
        self._Status = None
        self._InstanceID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Status = params.get("Status")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HybridPkg(AbstractModel):
    """混合云节点资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _InquireNum: 申请数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InquireNum: int
        :param _UsedNum: 使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedNum: int
        :param _RenewFlag: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        """
        self._ResourceIds = None
        self._Status = None
        self._Region = None
        self._BeginTime = None
        self._EndTime = None
        self._InquireNum = None
        self._UsedNum = None
        self._RenewFlag = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InquireNum(self):
        return self._InquireNum

    @InquireNum.setter
    def InquireNum(self, InquireNum):
        self._InquireNum = InquireNum

    @property
    def UsedNum(self):
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._InquireNum = params.get("InquireNum")
        self._UsedNum = params.get("UsedNum")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """一个实例的详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: id
        :type InstanceId: str
        :param _InstanceName: Name
        :type InstanceName: str
        :param _ResourceIds: 资源id
        :type ResourceIds: str
        :param _Region: 地域
        :type Region: str
        :param _PayMode: 付费模式
        :type PayMode: int
        :param _RenewFlag: 自动续费
        :type RenewFlag: int
        :param _Mode: 弹性计费
        :type Mode: int
        :param _Level: 套餐版本
        :type Level: int
        :param _ValidTime: 过期时间
        :type ValidTime: str
        :param _BeginTime: 开始时间
        :type BeginTime: str
        :param _DomainCount: 已用
        :type DomainCount: int
        :param _SubDomainLimit: 上限
        :type SubDomainLimit: int
        :param _MainDomainCount: 已用
        :type MainDomainCount: int
        :param _MainDomainLimit: 上限
        :type MainDomainLimit: int
        :param _MaxQPS: 峰值
        :type MaxQPS: int
        :param _QPS: qps套餐
        :type QPS: :class:`tencentcloud.waf.v20180125.models.QPSPackageNew`
        :param _DomainPkg: 域名套餐
        :type DomainPkg: :class:`tencentcloud.waf.v20180125.models.DomainPackageNew`
        :param _AppId: 用户appid
        :type AppId: int
        :param _Edition: clb或saas
        :type Edition: str
        :param _FraudPkg: 业务安全包
注意：此字段可能返回 null，表示取不到有效值。
        :type FraudPkg: :class:`tencentcloud.waf.v20180125.models.FraudPkg`
        :param _BotPkg: Bot资源包
注意：此字段可能返回 null，表示取不到有效值。
        :type BotPkg: :class:`tencentcloud.waf.v20180125.models.BotPkg`
        :param _BotQPS: bot的qps详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BotQPS: :class:`tencentcloud.waf.v20180125.models.BotQPS`
        :param _ElasticBilling: qps弹性计费上限
注意：此字段可能返回 null，表示取不到有效值。
        :type ElasticBilling: int
        :param _AttackLogPost: 攻击日志投递开关
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackLogPost: int
        :param _MaxBandwidth: 带宽峰值，单位为B/s(字节每秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxBandwidth: int
        :param _APISecurity: api安全是否购买
        :type APISecurity: int
        :param _QpsStandard: 购买的qps规格
注意：此字段可能返回 null，表示取不到有效值。
        :type QpsStandard: int
        :param _BandwidthStandard: 购买的带宽规格
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthStandard: int
        :param _Status: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _SandboxQps: 实例沙箱值
注意：此字段可能返回 null，表示取不到有效值。
        :type SandboxQps: int
        :param _IsAPISecurityTrial: 是否api 安全试用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAPISecurityTrial: int
        :param _MajorEventsPkg: 重保包
注意：此字段可能返回 null，表示取不到有效值。
        :type MajorEventsPkg: :class:`tencentcloud.waf.v20180125.models.MajorEventsPkg`
        :param _HybridPkg: 混合云子节点包
注意：此字段可能返回 null，表示取不到有效值。
        :type HybridPkg: :class:`tencentcloud.waf.v20180125.models.HybridPkg`
        """
        self._InstanceId = None
        self._InstanceName = None
        self._ResourceIds = None
        self._Region = None
        self._PayMode = None
        self._RenewFlag = None
        self._Mode = None
        self._Level = None
        self._ValidTime = None
        self._BeginTime = None
        self._DomainCount = None
        self._SubDomainLimit = None
        self._MainDomainCount = None
        self._MainDomainLimit = None
        self._MaxQPS = None
        self._QPS = None
        self._DomainPkg = None
        self._AppId = None
        self._Edition = None
        self._FraudPkg = None
        self._BotPkg = None
        self._BotQPS = None
        self._ElasticBilling = None
        self._AttackLogPost = None
        self._MaxBandwidth = None
        self._APISecurity = None
        self._QpsStandard = None
        self._BandwidthStandard = None
        self._Status = None
        self._SandboxQps = None
        self._IsAPISecurityTrial = None
        self._MajorEventsPkg = None
        self._HybridPkg = None

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
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def ValidTime(self):
        return self._ValidTime

    @ValidTime.setter
    def ValidTime(self, ValidTime):
        self._ValidTime = ValidTime

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def DomainCount(self):
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def SubDomainLimit(self):
        return self._SubDomainLimit

    @SubDomainLimit.setter
    def SubDomainLimit(self, SubDomainLimit):
        self._SubDomainLimit = SubDomainLimit

    @property
    def MainDomainCount(self):
        return self._MainDomainCount

    @MainDomainCount.setter
    def MainDomainCount(self, MainDomainCount):
        self._MainDomainCount = MainDomainCount

    @property
    def MainDomainLimit(self):
        return self._MainDomainLimit

    @MainDomainLimit.setter
    def MainDomainLimit(self, MainDomainLimit):
        self._MainDomainLimit = MainDomainLimit

    @property
    def MaxQPS(self):
        return self._MaxQPS

    @MaxQPS.setter
    def MaxQPS(self, MaxQPS):
        self._MaxQPS = MaxQPS

    @property
    def QPS(self):
        return self._QPS

    @QPS.setter
    def QPS(self, QPS):
        self._QPS = QPS

    @property
    def DomainPkg(self):
        return self._DomainPkg

    @DomainPkg.setter
    def DomainPkg(self, DomainPkg):
        self._DomainPkg = DomainPkg

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def FraudPkg(self):
        return self._FraudPkg

    @FraudPkg.setter
    def FraudPkg(self, FraudPkg):
        self._FraudPkg = FraudPkg

    @property
    def BotPkg(self):
        return self._BotPkg

    @BotPkg.setter
    def BotPkg(self, BotPkg):
        self._BotPkg = BotPkg

    @property
    def BotQPS(self):
        return self._BotQPS

    @BotQPS.setter
    def BotQPS(self, BotQPS):
        self._BotQPS = BotQPS

    @property
    def ElasticBilling(self):
        return self._ElasticBilling

    @ElasticBilling.setter
    def ElasticBilling(self, ElasticBilling):
        self._ElasticBilling = ElasticBilling

    @property
    def AttackLogPost(self):
        return self._AttackLogPost

    @AttackLogPost.setter
    def AttackLogPost(self, AttackLogPost):
        self._AttackLogPost = AttackLogPost

    @property
    def MaxBandwidth(self):
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def APISecurity(self):
        return self._APISecurity

    @APISecurity.setter
    def APISecurity(self, APISecurity):
        self._APISecurity = APISecurity

    @property
    def QpsStandard(self):
        return self._QpsStandard

    @QpsStandard.setter
    def QpsStandard(self, QpsStandard):
        self._QpsStandard = QpsStandard

    @property
    def BandwidthStandard(self):
        return self._BandwidthStandard

    @BandwidthStandard.setter
    def BandwidthStandard(self, BandwidthStandard):
        self._BandwidthStandard = BandwidthStandard

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SandboxQps(self):
        return self._SandboxQps

    @SandboxQps.setter
    def SandboxQps(self, SandboxQps):
        self._SandboxQps = SandboxQps

    @property
    def IsAPISecurityTrial(self):
        return self._IsAPISecurityTrial

    @IsAPISecurityTrial.setter
    def IsAPISecurityTrial(self, IsAPISecurityTrial):
        self._IsAPISecurityTrial = IsAPISecurityTrial

    @property
    def MajorEventsPkg(self):
        return self._MajorEventsPkg

    @MajorEventsPkg.setter
    def MajorEventsPkg(self, MajorEventsPkg):
        self._MajorEventsPkg = MajorEventsPkg

    @property
    def HybridPkg(self):
        return self._HybridPkg

    @HybridPkg.setter
    def HybridPkg(self, HybridPkg):
        self._HybridPkg = HybridPkg


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ResourceIds = params.get("ResourceIds")
        self._Region = params.get("Region")
        self._PayMode = params.get("PayMode")
        self._RenewFlag = params.get("RenewFlag")
        self._Mode = params.get("Mode")
        self._Level = params.get("Level")
        self._ValidTime = params.get("ValidTime")
        self._BeginTime = params.get("BeginTime")
        self._DomainCount = params.get("DomainCount")
        self._SubDomainLimit = params.get("SubDomainLimit")
        self._MainDomainCount = params.get("MainDomainCount")
        self._MainDomainLimit = params.get("MainDomainLimit")
        self._MaxQPS = params.get("MaxQPS")
        if params.get("QPS") is not None:
            self._QPS = QPSPackageNew()
            self._QPS._deserialize(params.get("QPS"))
        if params.get("DomainPkg") is not None:
            self._DomainPkg = DomainPackageNew()
            self._DomainPkg._deserialize(params.get("DomainPkg"))
        self._AppId = params.get("AppId")
        self._Edition = params.get("Edition")
        if params.get("FraudPkg") is not None:
            self._FraudPkg = FraudPkg()
            self._FraudPkg._deserialize(params.get("FraudPkg"))
        if params.get("BotPkg") is not None:
            self._BotPkg = BotPkg()
            self._BotPkg._deserialize(params.get("BotPkg"))
        if params.get("BotQPS") is not None:
            self._BotQPS = BotQPS()
            self._BotQPS._deserialize(params.get("BotQPS"))
        self._ElasticBilling = params.get("ElasticBilling")
        self._AttackLogPost = params.get("AttackLogPost")
        self._MaxBandwidth = params.get("MaxBandwidth")
        self._APISecurity = params.get("APISecurity")
        self._QpsStandard = params.get("QpsStandard")
        self._BandwidthStandard = params.get("BandwidthStandard")
        self._Status = params.get("Status")
        self._SandboxQps = params.get("SandboxQps")
        self._IsAPISecurityTrial = params.get("IsAPISecurityTrial")
        if params.get("MajorEventsPkg") is not None:
            self._MajorEventsPkg = MajorEventsPkg()
            self._MajorEventsPkg._deserialize(params.get("MajorEventsPkg"))
        if params.get("HybridPkg") is not None:
            self._HybridPkg = HybridPkg()
            self._HybridPkg._deserialize(params.get("HybridPkg"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAccessControlData(AbstractModel):
    """数据封装

    """

    def __init__(self):
        r"""
        :param _Res: ip黑白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type Res: list of IpAccessControlItem
        :param _TotalCount: 计数
        :type TotalCount: int
        """
        self._Res = None
        self._TotalCount = None

    @property
    def Res(self):
        return self._Res

    @Res.setter
    def Res(self, Res):
        self._Res = Res

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("Res") is not None:
            self._Res = []
            for item in params.get("Res"):
                obj = IpAccessControlItem()
                obj._deserialize(item)
                self._Res.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAccessControlItem(AbstractModel):
    """ip黑白名单

    """

    def __init__(self):
        r"""
        :param _Id: mongo表自增Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _ActionType: 动作
        :type ActionType: int
        :param _Ip: ip
        :type Ip: str
        :param _Note: 备注
        :type Note: str
        :param _Source: 来源
        :type Source: str
        :param _TsVersion: 更新时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TsVersion: int
        :param _ValidTs: 有效截止时间戳
        :type ValidTs: int
        :param _ValidStatus: 生效状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidStatus: int
        """
        self._Id = None
        self._ActionType = None
        self._Ip = None
        self._Note = None
        self._Source = None
        self._TsVersion = None
        self._ValidTs = None
        self._ValidStatus = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def TsVersion(self):
        return self._TsVersion

    @TsVersion.setter
    def TsVersion(self, TsVersion):
        self._TsVersion = TsVersion

    @property
    def ValidTs(self):
        return self._ValidTs

    @ValidTs.setter
    def ValidTs(self, ValidTs):
        self._ValidTs = ValidTs

    @property
    def ValidStatus(self):
        return self._ValidStatus

    @ValidStatus.setter
    def ValidStatus(self, ValidStatus):
        self._ValidStatus = ValidStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ActionType = params.get("ActionType")
        self._Ip = params.get("Ip")
        self._Note = params.get("Note")
        self._Source = params.get("Source")
        self._TsVersion = params.get("TsVersion")
        self._ValidTs = params.get("ValidTs")
        self._ValidStatus = params.get("ValidStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpHitItem(AbstractModel):
    """ip封堵状态数据

    """

    def __init__(self):
        r"""
        :param _Action: 动作
        :type Action: int
        :param _Category: 类别
        :type Category: str
        :param _Ip: ip
        :type Ip: str
        :param _Name: 规则名称
        :type Name: str
        :param _TsVersion: 时间戳
        :type TsVersion: int
        :param _ValidTs: 有效截止时间戳
        :type ValidTs: int
        """
        self._Action = None
        self._Category = None
        self._Ip = None
        self._Name = None
        self._TsVersion = None
        self._ValidTs = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TsVersion(self):
        return self._TsVersion

    @TsVersion.setter
    def TsVersion(self, TsVersion):
        self._TsVersion = TsVersion

    @property
    def ValidTs(self):
        return self._ValidTs

    @ValidTs.setter
    def ValidTs(self, ValidTs):
        self._ValidTs = ValidTs


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Category = params.get("Category")
        self._Ip = params.get("Ip")
        self._Name = params.get("Name")
        self._TsVersion = params.get("TsVersion")
        self._ValidTs = params.get("ValidTs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpHitItemsData(AbstractModel):
    """封装参数

    """

    def __init__(self):
        r"""
        :param _Res: 数组封装
        :type Res: list of IpHitItem
        :param _TotalCount: 总数目
        :type TotalCount: int
        """
        self._Res = None
        self._TotalCount = None

    @property
    def Res(self):
        return self._Res

    @Res.setter
    def Res(self, Res):
        self._Res = Res

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("Res") is not None:
            self._Res = []
            for item in params.get("Res"):
                obj = IpHitItem()
                obj._deserialize(item)
                self._Res.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """负载均衡的监听器

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡LD的ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡LD的名称
        :type LoadBalancerName: str
        :param _ListenerId: 负载均衡监听器的ID
        :type ListenerId: str
        :param _ListenerName: 负载均衡监听器的名称
        :type ListenerName: str
        :param _Vip: 负载均衡实例的IP
        :type Vip: str
        :param _Vport: 负载均衡实例的端口
        :type Vport: int
        :param _Region: 负载均衡LD的地域
        :type Region: str
        :param _Protocol: 监听器协议，http、https
        :type Protocol: str
        :param _Zone: 负载均衡监听器所在的zone
        :type Zone: str
        :param _NumericalVpcId: 负载均衡的VPCID，公网为-1，内网按实际填写
注意：此字段可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        :param _LoadBalancerType: 负载均衡的网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _LoadBalancerDomain: 负载均衡的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDomain: str
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._ListenerId = None
        self._ListenerName = None
        self._Vip = None
        self._Vport = None
        self._Region = None
        self._Protocol = None
        self._Zone = None
        self._NumericalVpcId = None
        self._LoadBalancerType = None
        self._LoadBalancerDomain = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NumericalVpcId(self):
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Region = params.get("Region")
        self._Protocol = params.get("Protocol")
        self._Zone = params.get("Zone")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerPackageNew(AbstractModel):
    """负载均衡器

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听id
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _ListenerName: 监听名
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _LoadBalancerId: 负载均衡id
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡名
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Region: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Vip: 接入IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _Vport: 接入端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param _Zone: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _NumericalVpcId: VPCID
注意：此字段可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        :param _LoadBalancerType: CLB类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _LoadBalancerDomain: 负载均衡器的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerDomain: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Protocol = None
        self._Region = None
        self._Vip = None
        self._Vport = None
        self._Zone = None
        self._NumericalVpcId = None
        self._LoadBalancerType = None
        self._LoadBalancerDomain = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NumericalVpcId(self):
        return self._NumericalVpcId

    @NumericalVpcId.setter
    def NumericalVpcId(self, NumericalVpcId):
        self._NumericalVpcId = NumericalVpcId

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerDomain(self):
        return self._LoadBalancerDomain

    @LoadBalancerDomain.setter
    def LoadBalancerDomain(self, LoadBalancerDomain):
        self._LoadBalancerDomain = LoadBalancerDomain


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._Protocol = params.get("Protocol")
        self._Region = params.get("Region")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._Zone = params.get("Zone")
        self._NumericalVpcId = params.get("NumericalVpcId")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerDomain = params.get("LoadBalancerDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogHistogramInfo(AbstractModel):
    """攻击日志统计详情

    """

    def __init__(self):
        r"""
        :param _Count: 日志条数
        :type Count: int
        :param _TimeStamp: 时间戳
        :type TimeStamp: int
        """
        self._Count = None
        self._TimeStamp = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._TimeStamp = params.get("TimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MajorEventsPkg(AbstractModel):
    """重保防护资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param _BeginTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _InquireNum: 申请数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InquireNum: int
        :param _UsedNum: 使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedNum: int
        :param _RenewFlag: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _BillingItem: 计费项
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingItem: str
        :param _HWState: 护网包状态
注意：此字段可能返回 null，表示取不到有效值。
        :type HWState: int
        """
        self._ResourceIds = None
        self._Status = None
        self._Region = None
        self._BeginTime = None
        self._EndTime = None
        self._InquireNum = None
        self._UsedNum = None
        self._RenewFlag = None
        self._BillingItem = None
        self._HWState = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InquireNum(self):
        return self._InquireNum

    @InquireNum.setter
    def InquireNum(self, InquireNum):
        self._InquireNum = InquireNum

    @property
    def UsedNum(self):
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def BillingItem(self):
        return self._BillingItem

    @BillingItem.setter
    def BillingItem(self, BillingItem):
        self._BillingItem = BillingItem

    @property
    def HWState(self):
        return self._HWState

    @HWState.setter
    def HWState(self, HWState):
        self._HWState = HWState


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._InquireNum = params.get("InquireNum")
        self._UsedNum = params.get("UsedNum")
        self._RenewFlag = params.get("RenewFlag")
        self._BillingItem = params.get("BillingItem")
        self._HWState = params.get("HWState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessPeriodRequest(AbstractModel):
    """ModifyAccessPeriod请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 访问日志保存期限，范围为[1, 30]
        :type Period: int
        :param _TopicId: 日志主题
        :type TopicId: str
        """
        self._Period = None
        self._TopicId = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccessPeriodResponse(AbstractModel):
    """ModifyAccessPeriod返回参数结构体

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


class ModifyAntiFakeUrlRequest(AbstractModel):
    """ModifyAntiFakeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Name: 名称
        :type Name: str
        :param _Uri: uri
        :type Uri: str
        :param _Id: ID
        :type Id: int
        """
        self._Domain = None
        self._Name = None
        self._Uri = None
        self._Id = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Name = params.get("Name")
        self._Uri = params.get("Uri")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAntiFakeUrlResponse(AbstractModel):
    """ModifyAntiFakeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyAntiFakeUrlStatusRequest(AbstractModel):
    """ModifyAntiFakeUrlStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Status: 状态
        :type Status: int
        :param _Ids: Id列表
        :type Ids: list of int non-negative
        """
        self._Domain = None
        self._Status = None
        self._Ids = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAntiFakeUrlStatusResponse(AbstractModel):
    """ModifyAntiFakeUrlStatus返回参数结构体

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


class ModifyAntiInfoLeakRuleStatusRequest(AbstractModel):
    """ModifyAntiInfoLeakRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RuleId: 规则
        :type RuleId: int
        :param _Status: 状态
        :type Status: int
        """
        self._Domain = None
        self._RuleId = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAntiInfoLeakRuleStatusResponse(AbstractModel):
    """ModifyAntiInfoLeakRuleStatus返回参数结构体

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


class ModifyAntiInfoLeakRulesRequest(AbstractModel):
    """ModifyAntiInfoLeakRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Name: 规则名称
        :type Name: str
        :param _Domain: 域名
        :type Domain: str
        :param _ActionType: Action 值
        :type ActionType: int
        :param _Strategies: 策略数组
        :type Strategies: list of StrategyForAntiInfoLeak
        """
        self._RuleId = None
        self._Name = None
        self._Domain = None
        self._ActionType = None
        self._Strategies = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._Domain = params.get("Domain")
        self._ActionType = params.get("ActionType")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = StrategyForAntiInfoLeak()
                obj._deserialize(item)
                self._Strategies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAntiInfoLeakRulesResponse(AbstractModel):
    """ModifyAntiInfoLeakRules返回参数结构体

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


class ModifyApiAnalyzeStatusRequest(AbstractModel):
    """ModifyApiAnalyzeStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 开关状态
        :type Status: int
        :param _Domain: 域名
        :type Domain: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _TargetList: 需要批量开启的实体列表
        :type TargetList: list of TargetEntity
        """
        self._Status = None
        self._Domain = None
        self._InstanceId = None
        self._TargetList = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TargetList(self):
        return self._TargetList

    @TargetList.setter
    def TargetList(self, TargetList):
        self._TargetList = TargetList


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Domain = params.get("Domain")
        self._InstanceId = params.get("InstanceId")
        if params.get("TargetList") is not None:
            self._TargetList = []
            for item in params.get("TargetList"):
                obj = TargetEntity()
                obj._deserialize(item)
                self._TargetList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiAnalyzeStatusResponse(AbstractModel):
    """ModifyApiAnalyzeStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 已经开启的数量,如果返回值为3（大于支持的域名开启数量），则表示开启失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _UnSupportedList: 不支持开启的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UnSupportedList: list of str
        :param _FailDomainList: 开启/关闭失败的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailDomainList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._UnSupportedList = None
        self._FailDomainList = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def UnSupportedList(self):
        return self._UnSupportedList

    @UnSupportedList.setter
    def UnSupportedList(self, UnSupportedList):
        self._UnSupportedList = UnSupportedList

    @property
    def FailDomainList(self):
        return self._FailDomainList

    @FailDomainList.setter
    def FailDomainList(self, FailDomainList):
        self._FailDomainList = FailDomainList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._UnSupportedList = params.get("UnSupportedList")
        self._FailDomainList = params.get("FailDomainList")
        self._RequestId = params.get("RequestId")


class ModifyAreaBanStatusRequest(AbstractModel):
    """ModifyAreaBanStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要修改的域名
        :type Domain: str
        :param _Status: 状态值，0表示关闭，1表示开启
        :type Status: int
        """
        self._Domain = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAreaBanStatusResponse(AbstractModel):
    """ModifyAreaBanStatus返回参数结构体

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


class ModifyBotStatusRequest(AbstractModel):
    """ModifyBotStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Category: 类别
        :type Category: str
        :param _Status: 状态
        :type Status: str
        :param _InstanceID: 实例id
        :type InstanceID: str
        :param _IsVersionFour: 是否是bot4.0版本
        :type IsVersionFour: bool
        :param _BotVersion: 传入Bot版本号，场景化版本为"4.1.0"
        :type BotVersion: str
        """
        self._Domain = None
        self._Category = None
        self._Status = None
        self._InstanceID = None
        self._IsVersionFour = None
        self._BotVersion = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def IsVersionFour(self):
        return self._IsVersionFour

    @IsVersionFour.setter
    def IsVersionFour(self, IsVersionFour):
        self._IsVersionFour = IsVersionFour

    @property
    def BotVersion(self):
        return self._BotVersion

    @BotVersion.setter
    def BotVersion(self, BotVersion):
        self._BotVersion = BotVersion


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Category = params.get("Category")
        self._Status = params.get("Status")
        self._InstanceID = params.get("InstanceID")
        self._IsVersionFour = params.get("IsVersionFour")
        self._BotVersion = params.get("BotVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBotStatusResponse(AbstractModel):
    """ModifyBotStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 正常情况为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyCustomRuleRequest(AbstractModel):
    """ModifyCustomRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 编辑的域名
        :type Domain: str
        :param _RuleId: 编辑的规则ID
        :type RuleId: int
        :param _RuleName: 编辑的规则名称
        :type RuleName: str
        :param _RuleAction: 执行动作，0：放行、1：阻断、2：人机识别、3：观察、4：重定向
        :type RuleAction: str
        :param _Strategies: 匹配条件数组
        :type Strategies: list of Strategy
        :param _Edition: WAF的版本，clb-waf代表负载均衡WAF、sparta-waf代表SaaS WAF，默认是sparta-waf。
        :type Edition: str
        :param _Redirect: 动作为重定向的时候重定向URL，默认为"/"
        :type Redirect: str
        :param _Bypass: 放行时是否继续执行其它检查逻辑，继续执行地域封禁防护：geoip、继续执行CC策略防护：cc、继续执行WEB应用防护：owasp、继续执行AI引擎防护：ai、继续执行信息防泄漏防护：antileakage。如果多个勾选那么以,串接。
默认是"geoip,cc,owasp,ai,antileakage"
        :type Bypass: str
        :param _SortId: 优先级，1~100的整数，数字越小，代表这条规则的执行优先级越高。
默认是100
        :type SortId: int
        :param _ExpireTime: 规则生效截止时间，0：永久生效，其它值为对应时间的时间戳。
默认是0
        :type ExpireTime: int
        """
        self._Domain = None
        self._RuleId = None
        self._RuleName = None
        self._RuleAction = None
        self._Strategies = None
        self._Edition = None
        self._Redirect = None
        self._Bypass = None
        self._SortId = None
        self._ExpireTime = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleAction(self):
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Redirect(self):
        return self._Redirect

    @Redirect.setter
    def Redirect(self, Redirect):
        self._Redirect = Redirect

    @property
    def Bypass(self):
        return self._Bypass

    @Bypass.setter
    def Bypass(self, Bypass):
        self._Bypass = Bypass

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RuleAction = params.get("RuleAction")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = Strategy()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._Edition = params.get("Edition")
        self._Redirect = params.get("Redirect")
        self._Bypass = params.get("Bypass")
        self._SortId = params.get("SortId")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomRuleResponse(AbstractModel):
    """ModifyCustomRule返回参数结构体

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


class ModifyCustomRuleStatusRequest(AbstractModel):
    """ModifyCustomRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Status: 开关的状态，1是开启、0是关闭
        :type Status: int
        :param _Edition: WAF的版本，clb-waf代表负载均衡WAF、sparta-waf代表SaaS WAF，默认是sparta-waf。
        :type Edition: str
        """
        self._Domain = None
        self._RuleId = None
        self._Status = None
        self._Edition = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomRuleStatusResponse(AbstractModel):
    """ModifyCustomRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCustomWhiteRuleRequest(AbstractModel):
    """ModifyCustomWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 编辑的域名
        :type Domain: str
        :param _RuleId: 编辑的规则ID
        :type RuleId: int
        :param _RuleName: 编辑的规则名称
        :type RuleName: str
        :param _Bypass: 放行时是否继续执行其它检查逻辑，继续执行地域封禁防护：geoip、继续执行CC策略防护：cc、继续执行WEB应用防护：owasp、继续执行AI引擎防护：ai、继续执行信息防泄漏防护：antileakage。如果勾选多个，则以“，”串接。
        :type Bypass: str
        :param _SortId: 优先级，1~100的整数，数字越小，代表这条规则的执行优先级越高。
        :type SortId: int
        :param _ExpireTime: 规则生效截止时间，0：永久生效，其它值为对应时间的时间戳。
        :type ExpireTime: int
        :param _Strategies: 匹配条件数组
        :type Strategies: list of Strategy
        """
        self._Domain = None
        self._RuleId = None
        self._RuleName = None
        self._Bypass = None
        self._SortId = None
        self._ExpireTime = None
        self._Strategies = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Bypass(self):
        return self._Bypass

    @Bypass.setter
    def Bypass(self, Bypass):
        self._Bypass = Bypass

    @property
    def SortId(self):
        return self._SortId

    @SortId.setter
    def SortId(self, SortId):
        self._SortId = SortId

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Bypass = params.get("Bypass")
        self._SortId = params.get("SortId")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = Strategy()
                obj._deserialize(item)
                self._Strategies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomWhiteRuleResponse(AbstractModel):
    """ModifyCustomWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCustomWhiteRuleStatusRequest(AbstractModel):
    """ModifyCustomWhiteRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _Status: 开关的状态，1是开启、0是关闭
        :type Status: int
        """
        self._Domain = None
        self._RuleId = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomWhiteRuleStatusResponse(AbstractModel):
    """ModifyCustomWhiteRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDomainIpv6StatusRequest(AbstractModel):
    """ModifyDomainIpv6Status请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要修改的域名所属的实例ID
        :type InstanceId: str
        :param _Domain: 需要修改的域名
        :type Domain: str
        :param _DomainId: 需要修改的域名ID
        :type DomainId: str
        :param _Status: 修改域名的Ipv6开关为Status （1:开启 2:关闭）
        :type Status: int
        """
        self._InstanceId = None
        self._Domain = None
        self._DomainId = None
        self._Status = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainIpv6StatusResponse(AbstractModel):
    """ModifyDomainIpv6Status返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ipv6Status: 返回的状态 （0: 操作失败 1:操作成功 2:企业版以上不支持 3:企业版以下不支持 ）
        :type Ipv6Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ipv6Status = None
        self._RequestId = None

    @property
    def Ipv6Status(self):
        return self._Ipv6Status

    @Ipv6Status.setter
    def Ipv6Status(self, Ipv6Status):
        self._Ipv6Status = Ipv6Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ipv6Status = params.get("Ipv6Status")
        self._RequestId = params.get("RequestId")


class ModifyDomainWhiteRuleRequest(AbstractModel):
    """ModifyDomainWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 需要更改的规则的域名
        :type Domain: str
        :param _Id: 白名单id
        :type Id: int
        :param _Rules: 规则的id列表
        :type Rules: list of int non-negative
        :param _Url: 规则匹配路径
        :type Url: str
        :param _Function: 规则匹配方法
        :type Function: str
        :param _Status: 规则的开关状态，0表示关闭开关，1表示打开开关
        :type Status: int
        """
        self._Domain = None
        self._Id = None
        self._Rules = None
        self._Url = None
        self._Function = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
        self._Rules = params.get("Rules")
        self._Url = params.get("Url")
        self._Function = params.get("Function")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainWhiteRuleResponse(AbstractModel):
    """ModifyDomainWhiteRule返回参数结构体

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


class ModifyDomainsCLSStatusRequest(AbstractModel):
    """ModifyDomainsCLSStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 需要修改的域名列表
        :type Domains: list of DomainURI
        :param _Status: 修改域名的访问日志开关为Status
        :type Status: int
        """
        self._Domains = None
        self._Status = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DomainURI()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainsCLSStatusResponse(AbstractModel):
    """ModifyDomainsCLSStatus返回参数结构体

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


class ModifyHostFlowModeRequest(AbstractModel):
    """ModifyHostFlowMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _FlowMode: WAF流量模式，1：清洗模式，0：镜像模式（默认）
        :type FlowMode: int
        :param _InstanceID: 实例ID
        :type InstanceID: str
        """
        self._Domain = None
        self._DomainId = None
        self._FlowMode = None
        self._InstanceID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def FlowMode(self):
        return self._FlowMode

    @FlowMode.setter
    def FlowMode(self, FlowMode):
        self._FlowMode = FlowMode

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._FlowMode = params.get("FlowMode")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostFlowModeResponse(AbstractModel):
    """ModifyHostFlowMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功的状态码
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyHostModeRequest(AbstractModel):
    """ModifyHostMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _Mode: 防护状态：
10：规则观察&&AI关闭模式，11：规则观察&&AI观察模式，12：规则观察&&AI拦截模式
20：规则拦截&&AI关闭模式，21：规则拦截&&AI观察模式，22：规则拦截&&AI拦截模式
        :type Mode: int
        :param _Type: 0:修改防护模式，1:修改AI
        :type Type: int
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Edition: 实例类型
        :type Edition: str
        """
        self._Domain = None
        self._DomainId = None
        self._Mode = None
        self._Type = None
        self._InstanceID = None
        self._Edition = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._Mode = params.get("Mode")
        self._Type = params.get("Type")
        self._InstanceID = params.get("InstanceID")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostModeResponse(AbstractModel):
    """ModifyHostMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 操作的状态码，如果所有的资源操作成功则返回的是成功的状态码，如果有资源操作失败则需要解析Message的内容来查看哪个资源失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyHostRequest(AbstractModel):
    """ModifyHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Host: 编辑的域名配置信息
        :type Host: :class:`tencentcloud.waf.v20180125.models.HostRecord`
        :param _InstanceID: 实例id
        :type InstanceID: str
        """
        self._Host = None
        self._InstanceID = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        if params.get("Host") is not None:
            self._Host = HostRecord()
            self._Host._deserialize(params.get("Host"))
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostResponse(AbstractModel):
    """ModifyHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 编辑的域名ID
        :type DomainId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainId = None
        self._RequestId = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._RequestId = params.get("RequestId")


class ModifyHostStatusRequest(AbstractModel):
    """ModifyHostStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HostsStatus: 域名状态列表
        :type HostsStatus: list of HostStatus
        """
        self._HostsStatus = None

    @property
    def HostsStatus(self):
        return self._HostsStatus

    @HostsStatus.setter
    def HostsStatus(self, HostsStatus):
        self._HostsStatus = HostsStatus


    def _deserialize(self, params):
        if params.get("HostsStatus") is not None:
            self._HostsStatus = []
            for item in params.get("HostsStatus"):
                obj = HostStatus()
                obj._deserialize(item)
                self._HostsStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostStatusResponse(AbstractModel):
    """ModifyHostStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功的状态码，需要JSON解码后再使用，返回的格式是{"域名":"状态"}，成功的状态码为Success，其它的为失败的状态码（yunapi定义的错误码）
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyInstanceElasticModeRequest(AbstractModel):
    """ModifyInstanceElasticMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Mode: 弹性计费开关
        :type Mode: int
        """
        self._InstanceId = None
        self._Mode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceElasticModeResponse(AbstractModel):
    """ModifyInstanceElasticMode返回参数结构体

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


class ModifyInstanceNameRequest(AbstractModel):
    """ModifyInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 新名称
        :type InstanceName: str
        :param _InstanceID: 实例id
        :type InstanceID: str
        :param _Edition: 版本
        :type Edition: str
        """
        self._InstanceName = None
        self._InstanceID = None
        self._Edition = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._InstanceID = params.get("InstanceID")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameResponse(AbstractModel):
    """ModifyInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModifyCode: 修改状态：0为成功
        :type ModifyCode: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModifyCode = None
        self._RequestId = None

    @property
    def ModifyCode(self):
        return self._ModifyCode

    @ModifyCode.setter
    def ModifyCode(self, ModifyCode):
        self._ModifyCode = ModifyCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModifyCode = params.get("ModifyCode")
        self._RequestId = params.get("RequestId")


class ModifyInstanceQpsLimitRequest(AbstractModel):
    """ModifyInstanceQpsLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 套餐实例id
        :type InstanceId: str
        :param _QpsLimit: qps上限
        :type QpsLimit: int
        """
        self._InstanceId = None
        self._QpsLimit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def QpsLimit(self):
        return self._QpsLimit

    @QpsLimit.setter
    def QpsLimit(self, QpsLimit):
        self._QpsLimit = QpsLimit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._QpsLimit = params.get("QpsLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceQpsLimitResponse(AbstractModel):
    """ModifyInstanceQpsLimit返回参数结构体

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


class ModifyInstanceRenewFlagRequest(AbstractModel):
    """ModifyInstanceRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RenewFlag: 续费开关
        :type RenewFlag: int
        """
        self._InstanceId = None
        self._RenewFlag = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRenewFlagResponse(AbstractModel):
    """ModifyInstanceRenewFlag返回参数结构体

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


class ModifyModuleStatusRequest(AbstractModel):
    """ModifyModuleStatus请求参数结构体

    """


class ModifyModuleStatusResponse(AbstractModel):
    """ModifyModuleStatus返回参数结构体

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


class ModifyProtectionStatusRequest(AbstractModel):
    """ModifyProtectionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Status: 状态
        :type Status: int
        :param _Edition: WAF的版本，clb-waf代表负载均衡WAF、sparta-waf代表SaaS WAF，默认是sparta-waf。
        :type Edition: str
        """
        self._Domain = None
        self._Status = None
        self._Edition = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._Edition = params.get("Edition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProtectionStatusResponse(AbstractModel):
    """ModifyProtectionStatus返回参数结构体

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


class ModifySpartaProtectionModeRequest(AbstractModel):
    """ModifySpartaProtectionMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Mode: 防护状态：
10：规则观察&&AI关闭模式，11：规则观察&&AI观察模式，12：规则观察&&AI拦截模式
20：规则拦截&&AI关闭模式，21：规则拦截&&AI观察模式，22：规则拦截&&AI拦截模式
        :type Mode: int
        :param _Edition: WAF的版本，clb-waf代表负载均衡WAF、sparta-waf代表SaaS WAF，默认是sparta-waf。
        :type Edition: str
        :param _Type: 0是修改规则引擎状态，1是修改AI的状态
        :type Type: int
        """
        self._Domain = None
        self._Mode = None
        self._Edition = None
        self._Type = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Mode = params.get("Mode")
        self._Edition = params.get("Edition")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySpartaProtectionModeResponse(AbstractModel):
    """ModifySpartaProtectionMode返回参数结构体

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


class ModifySpartaProtectionRequest(AbstractModel):
    """ModifySpartaProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _CertType: 证书类型，0表示没有证书，CertType=1表示自有证书,2 为托管证书
        :type CertType: int
        :param _Cert: CertType=1时，需要填次参数，表示证书内容
        :type Cert: str
        :param _PrivateKey: CertType=1时，需要填次参数，表示证书的私钥
        :type PrivateKey: str
        :param _SSLId: CertType=2时，需要填次参数，表示证书的ID
        :type SSLId: str
        :param _IsCdn: 表示是否开启了CDN代理
        :type IsCdn: int
        :param _UpstreamScheme: HTTPS回源协议
        :type UpstreamScheme: str
        :param _HttpsUpstreamPort: HTTPS回源端口,仅UpstreamScheme为http时需要填当前字段
        :type HttpsUpstreamPort: str
        :param _HttpsRewrite: 表示是否强制跳转到HTTPS，1表示开启，0表示不开启
        :type HttpsRewrite: int
        :param _UpstreamType: 回源类型，0表示通过IP回源,1 表示通过域名回源
        :type UpstreamType: int
        :param _UpstreamDomain: UpstreamType=1时，填次字段表示回源域名
        :type UpstreamDomain: str
        :param _SrcList: UpstreamType=0时，填次字段表示回源ip
        :type SrcList: list of str
        :param _IsHttp2: 是否开启HTTP2，1表示开启，0表示不开启http2。开启HTTP2需要HTTPS支持
        :type IsHttp2: int
        :param _IsWebsocket: 是否开启WebSocket， 1：开启WebSocket，0：不开启WebSocket
        :type IsWebsocket: int
        :param _LoadBalance: 负载均衡策略，0表示轮徇，1表示IP hash
        :type LoadBalance: int
        :param _IsGray: 是否灰度
        :type IsGray: int
        :param _Edition: WAF版本
        :type Edition: str
        :param _Ports: 端口信息
        :type Ports: list of SpartaProtectionPort
        :param _IsKeepAlive: 长短连接标志，仅IP回源时有效
        :type IsKeepAlive: str
        :param _InstanceID: 实例id
        :type InstanceID: str
        :param _Anycast: 是否为Anycast ip类型：1 Anycast 0 普通ip
        :type Anycast: int
        :param _Weights: src的权重
        :type Weights: list of int
        :param _ActiveCheck: 是否开启源站的主动健康检测，1表示开启，0表示不开启
        :type ActiveCheck: int
        :param _TLSVersion: TLS版本信息
        :type TLSVersion: int
        :param _Ciphers: 加密套件信息
        :type Ciphers: list of int
        :param _CipherTemplate: 0:不支持选择：默认模板  1:通用型模板 2:安全型模板 3:自定义模板
        :type CipherTemplate: int
        :param _ProxyReadTimeout: 300s
        :type ProxyReadTimeout: int
        :param _ProxySendTimeout: 300s
        :type ProxySendTimeout: int
        :param _SniType: 0:关闭SNI；1:开启SNI，SNI=源请求host；2:开启SNI，SNI=修改为源站host；3：开启SNI，自定义host，SNI=SniHost；
        :type SniType: int
        :param _SniHost: SniType=3时，需要填此参数，表示自定义的host；
        :type SniHost: str
        :param _IpHeaders: IsCdn=3时，需要填此参数，表示自定义header
        :type IpHeaders: list of str
        :param _XFFReset: 0:关闭xff重置；1:开启xff重置，只有在IsCdn=0时可以开启
        :type XFFReset: int
        """
        self._Domain = None
        self._DomainId = None
        self._CertType = None
        self._Cert = None
        self._PrivateKey = None
        self._SSLId = None
        self._IsCdn = None
        self._UpstreamScheme = None
        self._HttpsUpstreamPort = None
        self._HttpsRewrite = None
        self._UpstreamType = None
        self._UpstreamDomain = None
        self._SrcList = None
        self._IsHttp2 = None
        self._IsWebsocket = None
        self._LoadBalance = None
        self._IsGray = None
        self._Edition = None
        self._Ports = None
        self._IsKeepAlive = None
        self._InstanceID = None
        self._Anycast = None
        self._Weights = None
        self._ActiveCheck = None
        self._TLSVersion = None
        self._Ciphers = None
        self._CipherTemplate = None
        self._ProxyReadTimeout = None
        self._ProxySendTimeout = None
        self._SniType = None
        self._SniHost = None
        self._IpHeaders = None
        self._XFFReset = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def IsCdn(self):
        return self._IsCdn

    @IsCdn.setter
    def IsCdn(self, IsCdn):
        self._IsCdn = IsCdn

    @property
    def UpstreamScheme(self):
        return self._UpstreamScheme

    @UpstreamScheme.setter
    def UpstreamScheme(self, UpstreamScheme):
        self._UpstreamScheme = UpstreamScheme

    @property
    def HttpsUpstreamPort(self):
        return self._HttpsUpstreamPort

    @HttpsUpstreamPort.setter
    def HttpsUpstreamPort(self, HttpsUpstreamPort):
        self._HttpsUpstreamPort = HttpsUpstreamPort

    @property
    def HttpsRewrite(self):
        return self._HttpsRewrite

    @HttpsRewrite.setter
    def HttpsRewrite(self, HttpsRewrite):
        self._HttpsRewrite = HttpsRewrite

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def UpstreamDomain(self):
        return self._UpstreamDomain

    @UpstreamDomain.setter
    def UpstreamDomain(self, UpstreamDomain):
        self._UpstreamDomain = UpstreamDomain

    @property
    def SrcList(self):
        return self._SrcList

    @SrcList.setter
    def SrcList(self, SrcList):
        self._SrcList = SrcList

    @property
    def IsHttp2(self):
        return self._IsHttp2

    @IsHttp2.setter
    def IsHttp2(self, IsHttp2):
        self._IsHttp2 = IsHttp2

    @property
    def IsWebsocket(self):
        return self._IsWebsocket

    @IsWebsocket.setter
    def IsWebsocket(self, IsWebsocket):
        self._IsWebsocket = IsWebsocket

    @property
    def LoadBalance(self):
        return self._LoadBalance

    @LoadBalance.setter
    def LoadBalance(self, LoadBalance):
        self._LoadBalance = LoadBalance

    @property
    def IsGray(self):
        return self._IsGray

    @IsGray.setter
    def IsGray(self, IsGray):
        self._IsGray = IsGray

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def IsKeepAlive(self):
        return self._IsKeepAlive

    @IsKeepAlive.setter
    def IsKeepAlive(self, IsKeepAlive):
        self._IsKeepAlive = IsKeepAlive

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Anycast(self):
        return self._Anycast

    @Anycast.setter
    def Anycast(self, Anycast):
        self._Anycast = Anycast

    @property
    def Weights(self):
        return self._Weights

    @Weights.setter
    def Weights(self, Weights):
        self._Weights = Weights

    @property
    def ActiveCheck(self):
        return self._ActiveCheck

    @ActiveCheck.setter
    def ActiveCheck(self, ActiveCheck):
        self._ActiveCheck = ActiveCheck

    @property
    def TLSVersion(self):
        return self._TLSVersion

    @TLSVersion.setter
    def TLSVersion(self, TLSVersion):
        self._TLSVersion = TLSVersion

    @property
    def Ciphers(self):
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def CipherTemplate(self):
        return self._CipherTemplate

    @CipherTemplate.setter
    def CipherTemplate(self, CipherTemplate):
        self._CipherTemplate = CipherTemplate

    @property
    def ProxyReadTimeout(self):
        return self._ProxyReadTimeout

    @ProxyReadTimeout.setter
    def ProxyReadTimeout(self, ProxyReadTimeout):
        self._ProxyReadTimeout = ProxyReadTimeout

    @property
    def ProxySendTimeout(self):
        return self._ProxySendTimeout

    @ProxySendTimeout.setter
    def ProxySendTimeout(self, ProxySendTimeout):
        self._ProxySendTimeout = ProxySendTimeout

    @property
    def SniType(self):
        return self._SniType

    @SniType.setter
    def SniType(self, SniType):
        self._SniType = SniType

    @property
    def SniHost(self):
        return self._SniHost

    @SniHost.setter
    def SniHost(self, SniHost):
        self._SniHost = SniHost

    @property
    def IpHeaders(self):
        return self._IpHeaders

    @IpHeaders.setter
    def IpHeaders(self, IpHeaders):
        self._IpHeaders = IpHeaders

    @property
    def XFFReset(self):
        return self._XFFReset

    @XFFReset.setter
    def XFFReset(self, XFFReset):
        self._XFFReset = XFFReset


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._CertType = params.get("CertType")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._SSLId = params.get("SSLId")
        self._IsCdn = params.get("IsCdn")
        self._UpstreamScheme = params.get("UpstreamScheme")
        self._HttpsUpstreamPort = params.get("HttpsUpstreamPort")
        self._HttpsRewrite = params.get("HttpsRewrite")
        self._UpstreamType = params.get("UpstreamType")
        self._UpstreamDomain = params.get("UpstreamDomain")
        self._SrcList = params.get("SrcList")
        self._IsHttp2 = params.get("IsHttp2")
        self._IsWebsocket = params.get("IsWebsocket")
        self._LoadBalance = params.get("LoadBalance")
        self._IsGray = params.get("IsGray")
        self._Edition = params.get("Edition")
        if params.get("Ports") is not None:
            self._Ports = []
            for item in params.get("Ports"):
                obj = SpartaProtectionPort()
                obj._deserialize(item)
                self._Ports.append(obj)
        self._IsKeepAlive = params.get("IsKeepAlive")
        self._InstanceID = params.get("InstanceID")
        self._Anycast = params.get("Anycast")
        self._Weights = params.get("Weights")
        self._ActiveCheck = params.get("ActiveCheck")
        self._TLSVersion = params.get("TLSVersion")
        self._Ciphers = params.get("Ciphers")
        self._CipherTemplate = params.get("CipherTemplate")
        self._ProxyReadTimeout = params.get("ProxyReadTimeout")
        self._ProxySendTimeout = params.get("ProxySendTimeout")
        self._SniType = params.get("SniType")
        self._SniHost = params.get("SniHost")
        self._IpHeaders = params.get("IpHeaders")
        self._XFFReset = params.get("XFFReset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySpartaProtectionResponse(AbstractModel):
    """ModifySpartaProtection返回参数结构体

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


class ModifyUserLevelRequest(AbstractModel):
    """ModifyUserLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Level: 防护规则等级 300=standard，400=extended
        :type Level: int
        """
        self._Domain = None
        self._Level = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserLevelResponse(AbstractModel):
    """ModifyUserLevel返回参数结构体

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


class ModifyUserSignatureRuleRequest(AbstractModel):
    """ModifyUserSignatureRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _MainClassID: 主类id
        :type MainClassID: str
        :param _Status: 主类开关0=关闭，1=开启，2=只告警
        :type Status: int
        :param _RuleID: 下发修改的规则列表
        :type RuleID: list of ReqUserRule
        """
        self._Domain = None
        self._MainClassID = None
        self._Status = None
        self._RuleID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def MainClassID(self):
        return self._MainClassID

    @MainClassID.setter
    def MainClassID(self, MainClassID):
        self._MainClassID = MainClassID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._MainClassID = params.get("MainClassID")
        self._Status = params.get("Status")
        if params.get("RuleID") is not None:
            self._RuleID = []
            for item in params.get("RuleID"):
                obj = ReqUserRule()
                obj._deserialize(item)
                self._RuleID.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserSignatureRuleResponse(AbstractModel):
    """ModifyUserSignatureRule返回参数结构体

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


class ModifyWafAutoDenyRulesRequest(AbstractModel):
    """ModifyWafAutoDenyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _AttackThreshold: 触发IP封禁的攻击次数阈值，范围为2~100次
        :type AttackThreshold: int
        :param _TimeThreshold: IP封禁统计时间，范围为1-60分钟
        :type TimeThreshold: int
        :param _DenyTimeThreshold: 触发IP封禁后的封禁时间，范围为5~360分钟
        :type DenyTimeThreshold: int
        :param _DefenseStatus: 自动封禁状态，0表示关闭，1表示打开
        :type DefenseStatus: int
        """
        self._Domain = None
        self._AttackThreshold = None
        self._TimeThreshold = None
        self._DenyTimeThreshold = None
        self._DefenseStatus = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AttackThreshold(self):
        return self._AttackThreshold

    @AttackThreshold.setter
    def AttackThreshold(self, AttackThreshold):
        self._AttackThreshold = AttackThreshold

    @property
    def TimeThreshold(self):
        return self._TimeThreshold

    @TimeThreshold.setter
    def TimeThreshold(self, TimeThreshold):
        self._TimeThreshold = TimeThreshold

    @property
    def DenyTimeThreshold(self):
        return self._DenyTimeThreshold

    @DenyTimeThreshold.setter
    def DenyTimeThreshold(self, DenyTimeThreshold):
        self._DenyTimeThreshold = DenyTimeThreshold

    @property
    def DefenseStatus(self):
        return self._DefenseStatus

    @DefenseStatus.setter
    def DefenseStatus(self, DefenseStatus):
        self._DefenseStatus = DefenseStatus


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._AttackThreshold = params.get("AttackThreshold")
        self._TimeThreshold = params.get("TimeThreshold")
        self._DenyTimeThreshold = params.get("DenyTimeThreshold")
        self._DefenseStatus = params.get("DefenseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWafAutoDenyRulesResponse(AbstractModel):
    """ModifyWafAutoDenyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功的状态码，需要JSON解码后再使用，返回的格式是{"域名":"状态"}，成功的状态码为Success，其它的为失败的状态码（yunapi定义的错误码）
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyWafAutoDenyStatusRequest(AbstractModel):
    """ModifyWafAutoDenyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WafAutoDenyDetails: WAF 自动封禁配置项
        :type WafAutoDenyDetails: :class:`tencentcloud.waf.v20180125.models.AutoDenyDetail`
        """
        self._WafAutoDenyDetails = None

    @property
    def WafAutoDenyDetails(self):
        return self._WafAutoDenyDetails

    @WafAutoDenyDetails.setter
    def WafAutoDenyDetails(self, WafAutoDenyDetails):
        self._WafAutoDenyDetails = WafAutoDenyDetails


    def _deserialize(self, params):
        if params.get("WafAutoDenyDetails") is not None:
            self._WafAutoDenyDetails = AutoDenyDetail()
            self._WafAutoDenyDetails._deserialize(params.get("WafAutoDenyDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWafAutoDenyStatusResponse(AbstractModel):
    """ModifyWafAutoDenyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WafAutoDenyDetails: WAF 自动封禁配置项
        :type WafAutoDenyDetails: :class:`tencentcloud.waf.v20180125.models.AutoDenyDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WafAutoDenyDetails = None
        self._RequestId = None

    @property
    def WafAutoDenyDetails(self):
        return self._WafAutoDenyDetails

    @WafAutoDenyDetails.setter
    def WafAutoDenyDetails(self, WafAutoDenyDetails):
        self._WafAutoDenyDetails = WafAutoDenyDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WafAutoDenyDetails") is not None:
            self._WafAutoDenyDetails = AutoDenyDetail()
            self._WafAutoDenyDetails._deserialize(params.get("WafAutoDenyDetails"))
        self._RequestId = params.get("RequestId")


class ModifyWafThreatenIntelligenceRequest(AbstractModel):
    """ModifyWafThreatenIntelligence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WafThreatenIntelligenceDetails: 配置WAF威胁情报封禁模块详情
        :type WafThreatenIntelligenceDetails: :class:`tencentcloud.waf.v20180125.models.WafThreatenIntelligenceDetails`
        """
        self._WafThreatenIntelligenceDetails = None

    @property
    def WafThreatenIntelligenceDetails(self):
        return self._WafThreatenIntelligenceDetails

    @WafThreatenIntelligenceDetails.setter
    def WafThreatenIntelligenceDetails(self, WafThreatenIntelligenceDetails):
        self._WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails


    def _deserialize(self, params):
        if params.get("WafThreatenIntelligenceDetails") is not None:
            self._WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails()
            self._WafThreatenIntelligenceDetails._deserialize(params.get("WafThreatenIntelligenceDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWafThreatenIntelligenceResponse(AbstractModel):
    """ModifyWafThreatenIntelligence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WafThreatenIntelligenceDetails: 当前WAF威胁情报封禁模块详情
        :type WafThreatenIntelligenceDetails: :class:`tencentcloud.waf.v20180125.models.WafThreatenIntelligenceDetails`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WafThreatenIntelligenceDetails = None
        self._RequestId = None

    @property
    def WafThreatenIntelligenceDetails(self):
        return self._WafThreatenIntelligenceDetails

    @WafThreatenIntelligenceDetails.setter
    def WafThreatenIntelligenceDetails(self, WafThreatenIntelligenceDetails):
        self._WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WafThreatenIntelligenceDetails") is not None:
            self._WafThreatenIntelligenceDetails = WafThreatenIntelligenceDetails()
            self._WafThreatenIntelligenceDetails._deserialize(params.get("WafThreatenIntelligenceDetails"))
        self._RequestId = params.get("RequestId")


class ModifyWebshellStatusRequest(AbstractModel):
    """ModifyWebshellStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Webshell: 域名webshell状态
        :type Webshell: :class:`tencentcloud.waf.v20180125.models.WebshellStatus`
        """
        self._Webshell = None

    @property
    def Webshell(self):
        return self._Webshell

    @Webshell.setter
    def Webshell(self, Webshell):
        self._Webshell = Webshell


    def _deserialize(self, params):
        if params.get("Webshell") is not None:
            self._Webshell = WebshellStatus()
            self._Webshell._deserialize(params.get("Webshell"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebshellStatusResponse(AbstractModel):
    """ModifyWebshellStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功的状态码，需要JSON解码后再使用，返回的格式是{"域名":"状态"}，成功的状态码为Success，其它的为失败的状态码（yunapi定义的错误码）
        :type Success: :class:`tencentcloud.waf.v20180125.models.ResponseCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = ResponseCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class PageInfo(AbstractModel):
    """公共翻页参数

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码
        :type PageNumber: str
        :param _PageSize: 页条目数量
        :type PageSize: str
        """
        self._PageNumber = None
        self._PageSize = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakPointsItem(AbstractModel):
    """PeakPoints数组项

    """

    def __init__(self):
        r"""
        :param _Time: 秒级别时间戳
        :type Time: int
        :param _Access: QPS
        :type Access: int
        :param _Up: 上行带宽峰值，单位B
        :type Up: int
        :param _Down: 下行带宽峰值，单位B
        :type Down: int
        :param _Attack: Web攻击次数
        :type Attack: int
        :param _Cc: CC攻击次数
        :type Cc: int
        :param _BotAccess: Bot qps
        :type BotAccess: int
        :param _StatusServerError: WAF返回给客户端状态码5xx次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusServerError: int
        :param _StatusClientError: WAF返回给客户端状态码4xx次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusClientError: int
        :param _StatusRedirect: WAF返回给客户端状态码302次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusRedirect: int
        :param _StatusOk: WAF返回给客户端状态码202次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusOk: int
        :param _UpstreamServerError: 源站返回给WAF状态码5xx次数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamServerError: int
        :param _UpstreamClientError: 源站返回给WAF状态码4xx次数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamClientError: int
        :param _UpstreamRedirect: 源站返回给WAF状态码302次数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamRedirect: int
        :param _BlackIP: 黑名单次数
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackIP: int
        :param _Tamper: 防篡改次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tamper: int
        :param _Leak: 信息防泄露次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Leak: int
        :param _ACL: 访问控制 
注意：此字段可能返回 null，表示取不到有效值。
        :type ACL: int
        """
        self._Time = None
        self._Access = None
        self._Up = None
        self._Down = None
        self._Attack = None
        self._Cc = None
        self._BotAccess = None
        self._StatusServerError = None
        self._StatusClientError = None
        self._StatusRedirect = None
        self._StatusOk = None
        self._UpstreamServerError = None
        self._UpstreamClientError = None
        self._UpstreamRedirect = None
        self._BlackIP = None
        self._Tamper = None
        self._Leak = None
        self._ACL = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Access(self):
        return self._Access

    @Access.setter
    def Access(self, Access):
        self._Access = Access

    @property
    def Up(self):
        return self._Up

    @Up.setter
    def Up(self, Up):
        self._Up = Up

    @property
    def Down(self):
        return self._Down

    @Down.setter
    def Down(self, Down):
        self._Down = Down

    @property
    def Attack(self):
        return self._Attack

    @Attack.setter
    def Attack(self, Attack):
        self._Attack = Attack

    @property
    def Cc(self):
        return self._Cc

    @Cc.setter
    def Cc(self, Cc):
        self._Cc = Cc

    @property
    def BotAccess(self):
        return self._BotAccess

    @BotAccess.setter
    def BotAccess(self, BotAccess):
        self._BotAccess = BotAccess

    @property
    def StatusServerError(self):
        return self._StatusServerError

    @StatusServerError.setter
    def StatusServerError(self, StatusServerError):
        self._StatusServerError = StatusServerError

    @property
    def StatusClientError(self):
        return self._StatusClientError

    @StatusClientError.setter
    def StatusClientError(self, StatusClientError):
        self._StatusClientError = StatusClientError

    @property
    def StatusRedirect(self):
        return self._StatusRedirect

    @StatusRedirect.setter
    def StatusRedirect(self, StatusRedirect):
        self._StatusRedirect = StatusRedirect

    @property
    def StatusOk(self):
        return self._StatusOk

    @StatusOk.setter
    def StatusOk(self, StatusOk):
        self._StatusOk = StatusOk

    @property
    def UpstreamServerError(self):
        return self._UpstreamServerError

    @UpstreamServerError.setter
    def UpstreamServerError(self, UpstreamServerError):
        self._UpstreamServerError = UpstreamServerError

    @property
    def UpstreamClientError(self):
        return self._UpstreamClientError

    @UpstreamClientError.setter
    def UpstreamClientError(self, UpstreamClientError):
        self._UpstreamClientError = UpstreamClientError

    @property
    def UpstreamRedirect(self):
        return self._UpstreamRedirect

    @UpstreamRedirect.setter
    def UpstreamRedirect(self, UpstreamRedirect):
        self._UpstreamRedirect = UpstreamRedirect

    @property
    def BlackIP(self):
        return self._BlackIP

    @BlackIP.setter
    def BlackIP(self, BlackIP):
        self._BlackIP = BlackIP

    @property
    def Tamper(self):
        return self._Tamper

    @Tamper.setter
    def Tamper(self, Tamper):
        self._Tamper = Tamper

    @property
    def Leak(self):
        return self._Leak

    @Leak.setter
    def Leak(self, Leak):
        self._Leak = Leak

    @property
    def ACL(self):
        return self._ACL

    @ACL.setter
    def ACL(self, ACL):
        self._ACL = ACL


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Access = params.get("Access")
        self._Up = params.get("Up")
        self._Down = params.get("Down")
        self._Attack = params.get("Attack")
        self._Cc = params.get("Cc")
        self._BotAccess = params.get("BotAccess")
        self._StatusServerError = params.get("StatusServerError")
        self._StatusClientError = params.get("StatusClientError")
        self._StatusRedirect = params.get("StatusRedirect")
        self._StatusOk = params.get("StatusOk")
        self._UpstreamServerError = params.get("UpstreamServerError")
        self._UpstreamClientError = params.get("UpstreamClientError")
        self._UpstreamRedirect = params.get("UpstreamRedirect")
        self._BlackIP = params.get("BlackIP")
        self._Tamper = params.get("Tamper")
        self._Leak = params.get("Leak")
        self._ACL = params.get("ACL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortInfo(AbstractModel):
    """服务端口配置

    """

    def __init__(self):
        r"""
        :param _NginxServerId: Nginx的服务器id
        :type NginxServerId: int
        :param _Port: 监听端口配置
        :type Port: str
        :param _Protocol: 与端口对应的协议
        :type Protocol: str
        :param _UpstreamPort: 回源端口
        :type UpstreamPort: str
        :param _UpstreamProtocol: 回源协议
        :type UpstreamProtocol: str
        """
        self._NginxServerId = None
        self._Port = None
        self._Protocol = None
        self._UpstreamPort = None
        self._UpstreamProtocol = None

    @property
    def NginxServerId(self):
        return self._NginxServerId

    @NginxServerId.setter
    def NginxServerId(self, NginxServerId):
        self._NginxServerId = NginxServerId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UpstreamPort(self):
        return self._UpstreamPort

    @UpstreamPort.setter
    def UpstreamPort(self, UpstreamPort):
        self._UpstreamPort = UpstreamPort

    @property
    def UpstreamProtocol(self):
        return self._UpstreamProtocol

    @UpstreamProtocol.setter
    def UpstreamProtocol(self, UpstreamProtocol):
        self._UpstreamProtocol = UpstreamProtocol


    def _deserialize(self, params):
        self._NginxServerId = params.get("NginxServerId")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._UpstreamPort = params.get("UpstreamPort")
        self._UpstreamProtocol = params.get("UpstreamProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortItem(AbstractModel):
    """防护域名端口配置信息

    """

    def __init__(self):
        r"""
        :param _Port: 监听端口配置
        :type Port: str
        :param _Protocol: 与Port一一对应，表示端口对应的协议
        :type Protocol: str
        :param _UpstreamPort: 与Port一一对应,  表示回源端口
        :type UpstreamPort: str
        :param _UpstreamProtocol: 与Port一一对应,  表示回源协议
        :type UpstreamProtocol: str
        :param _NginxServerId: Nginx的服务器ID
        :type NginxServerId: str
        """
        self._Port = None
        self._Protocol = None
        self._UpstreamPort = None
        self._UpstreamProtocol = None
        self._NginxServerId = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UpstreamPort(self):
        return self._UpstreamPort

    @UpstreamPort.setter
    def UpstreamPort(self, UpstreamPort):
        self._UpstreamPort = UpstreamPort

    @property
    def UpstreamProtocol(self):
        return self._UpstreamProtocol

    @UpstreamProtocol.setter
    def UpstreamProtocol(self, UpstreamProtocol):
        self._UpstreamProtocol = UpstreamProtocol

    @property
    def NginxServerId(self):
        return self._NginxServerId

    @NginxServerId.setter
    def NginxServerId(self, NginxServerId):
        self._NginxServerId = NginxServerId


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._UpstreamPort = params.get("UpstreamPort")
        self._UpstreamProtocol = params.get("UpstreamProtocol")
        self._NginxServerId = params.get("NginxServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostAttackDownloadTaskRequest(AbstractModel):
    """PostAttackDownloadTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 查询的域名，所有域名使用all
        :type Domain: str
        :param _StartTime: 查询起始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _QueryString: Lucene语法
        :type QueryString: str
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _Sort: 默认为desc，可以取值desc和asc
        :type Sort: str
        :param _Count: 下载的日志条数
        :type Count: int
        """
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._QueryString = None
        self._TaskName = None
        self._Sort = None
        self._Count = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._QueryString = params.get("QueryString")
        self._TaskName = params.get("TaskName")
        self._Sort = params.get("Sort")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostAttackDownloadTaskResponse(AbstractModel):
    """PostAttackDownloadTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Flow: 任务task id
        :type Flow: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Flow = None
        self._RequestId = None

    @property
    def Flow(self):
        return self._Flow

    @Flow.setter
    def Flow(self, Flow):
        self._Flow = Flow

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Flow = params.get("Flow")
        self._RequestId = params.get("RequestId")


class QPSPackageNew(AbstractModel):
    """clb-waf QPS套餐 New

    """

    def __init__(self):
        r"""
        :param _ResourceIds: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: str
        :param _ValidTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidTime: str
        :param _RenewFlag: 是否自动续费，1：自动续费，0：不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _Count: 套餐购买个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Region: 套餐购买地域，clb-waf暂时没有用到
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _BillingItem: 计费项
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingItem: str
        """
        self._ResourceIds = None
        self._ValidTime = None
        self._RenewFlag = None
        self._Count = None
        self._Region = None
        self._BillingItem = None

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ValidTime(self):
        return self._ValidTime

    @ValidTime.setter
    def ValidTime(self, ValidTime):
        self._ValidTime = ValidTime

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BillingItem(self):
        return self._BillingItem

    @BillingItem.setter
    def BillingItem(self, BillingItem):
        self._BillingItem = BillingItem


    def _deserialize(self, params):
        self._ResourceIds = params.get("ResourceIds")
        self._ValidTime = params.get("ValidTime")
        self._RenewFlag = params.get("RenewFlag")
        self._Count = params.get("Count")
        self._Region = params.get("Region")
        self._BillingItem = params.get("BillingItem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QpsData(AbstractModel):
    """获取弹性qps的默认相关值

    """

    def __init__(self):
        r"""
        :param _ElasticBillingDefault: 弹性qps默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type ElasticBillingDefault: int
        :param _ElasticBillingMin: 弹性qps最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type ElasticBillingMin: int
        :param _ElasticBillingMax: 弹性qps最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type ElasticBillingMax: int
        :param _QPSExtendMax: 业务扩展包最大qps
注意：此字段可能返回 null，表示取不到有效值。
        :type QPSExtendMax: int
        :param _QPSExtendIntlMax: 海外业务扩展包最大qps
注意：此字段可能返回 null，表示取不到有效值。
        :type QPSExtendIntlMax: int
        """
        self._ElasticBillingDefault = None
        self._ElasticBillingMin = None
        self._ElasticBillingMax = None
        self._QPSExtendMax = None
        self._QPSExtendIntlMax = None

    @property
    def ElasticBillingDefault(self):
        return self._ElasticBillingDefault

    @ElasticBillingDefault.setter
    def ElasticBillingDefault(self, ElasticBillingDefault):
        self._ElasticBillingDefault = ElasticBillingDefault

    @property
    def ElasticBillingMin(self):
        return self._ElasticBillingMin

    @ElasticBillingMin.setter
    def ElasticBillingMin(self, ElasticBillingMin):
        self._ElasticBillingMin = ElasticBillingMin

    @property
    def ElasticBillingMax(self):
        return self._ElasticBillingMax

    @ElasticBillingMax.setter
    def ElasticBillingMax(self, ElasticBillingMax):
        self._ElasticBillingMax = ElasticBillingMax

    @property
    def QPSExtendMax(self):
        return self._QPSExtendMax

    @QPSExtendMax.setter
    def QPSExtendMax(self, QPSExtendMax):
        self._QPSExtendMax = QPSExtendMax

    @property
    def QPSExtendIntlMax(self):
        return self._QPSExtendIntlMax

    @QPSExtendIntlMax.setter
    def QPSExtendIntlMax(self, QPSExtendIntlMax):
        self._QPSExtendIntlMax = QPSExtendIntlMax


    def _deserialize(self, params):
        self._ElasticBillingDefault = params.get("ElasticBillingDefault")
        self._ElasticBillingMin = params.get("ElasticBillingMin")
        self._ElasticBillingMax = params.get("ElasticBillingMax")
        self._QPSExtendMax = params.get("QPSExtendMax")
        self._QPSExtendIntlMax = params.get("QPSExtendIntlMax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshAccessCheckResultRequest(AbstractModel):
    """RefreshAccessCheckResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshAccessCheckResultResponse(AbstractModel):
    """RefreshAccessCheckResult返回参数结构体

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


class ReqUserRule(AbstractModel):
    """用户规则更新输出规则子项

    """

    def __init__(self):
        r"""
        :param _Id: 特征序号
        :type Id: str
        :param _Status: 规则开关
0：关
1：开
2：只告警
        :type Status: int
        :param _Reason: 修改原因
0：无(兼容记录为空)
1：业务自身特性误报避免
2：规则误报上报
3：核心业务规则灰度
4：其它
        :type Reason: int
        """
        self._Id = None
        self._Status = None
        self._Reason = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseCode(AbstractModel):
    """响应体的返回码

    """

    def __init__(self):
        r"""
        :param _Code: 如果成功则返回Success，失败则返回云api定义的错误码
        :type Code: str
        :param _Message: 如果成功则返回Success，失败则返回WAF定义的二级错误码
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """规则列表详情

    """

    def __init__(self):
        r"""
        :param _Id: 规则id
        :type Id: int
        :param _Type: 规则类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Level: 规则等级
        :type Level: str
        :param _Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CVE: 规则防护的CVE编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CVE: str
        :param _Status: 规则的状态
        :type Status: int
        :param _ModifyTime: 规则修改的时间
        :type ModifyTime: str
        :param _AddTime: 门神规则新增/更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        """
        self._Id = None
        self._Type = None
        self._Level = None
        self._Description = None
        self._CVE = None
        self._Status = None
        self._ModifyTime = None
        self._AddTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CVE(self):
        return self._CVE

    @CVE.setter
    def CVE(self, CVE):
        self._CVE = CVE

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        self._Description = params.get("Description")
        self._CVE = params.get("CVE")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        self._AddTime = params.get("AddTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleList(AbstractModel):
    """规则白名单

    """

    def __init__(self):
        r"""
        :param _Id: 规则Id
        :type Id: int
        :param _Rules: 规则列表的id
        :type Rules: list of int non-negative
        :param _Url: 请求url
        :type Url: str
        :param _Function: 请求的方法
        :type Function: str
        :param _Time: 时间戳
        :type Time: str
        :param _Status: 开关状态
        :type Status: int
        """
        self._Id = None
        self._Rules = None
        self._Url = None
        self._Function = None
        self._Time = None
        self._Status = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Rules = params.get("Rules")
        self._Url = params.get("Url")
        self._Function = params.get("Function")
        self._Time = params.get("Time")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAccessLogRequest(AbstractModel):
    """SearchAccessLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 客户要查询的日志主题ID，每个客户都有对应的一个主题，新版本此字段填空字符串
        :type TopicId: str
        :param _From: 要查询的日志的起始时间，Unix时间戳，单位ms
        :type From: int
        :param _To: 要查询的日志的结束时间，Unix时间戳，单位ms
        :type To: int
        :param _Query: 查询语句，语句长度最大为4096
        :type Query: str
        :param _Limit: 单次查询返回的日志条数，最大值为100
        :type Limit: int
        :param _Context: 新版本此字段失效，填空字符串，翻页使用Page
        :type Context: str
        :param _Sort: 日志接口是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
        :type Sort: str
        :param _Page: 第几页，从0开始。新版本接口字段
        :type Page: int
        """
        self._TopicId = None
        self._From = None
        self._To = None
        self._Query = None
        self._Limit = None
        self._Context = None
        self._Sort = None
        self._Page = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAccessLogResponse(AbstractModel):
    """SearchAccessLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 新接口此字段失效，默认返回空字符串
        :type Context: str
        :param _ListOver: 日志查询结果是否全部返回，其中，“true”表示结果返回，“false”表示结果为返回
        :type ListOver: bool
        :param _Analysis: 返回的是否为分析结果，其中，“true”表示返回分析结果，“false”表示未返回分析结果
        :type Analysis: bool
        :param _ColNames: 如果Analysis为True，则返回分析结果的列名，否则为空
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param _Results: 日志查询结果；当Analysis为True时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of AccessLogInfo
        :param _AnalysisResults: 日志分析结果；当Analysis为False时，可能返回为null
注意：此字段可能返回 null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of AccessLogItems
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._ColNames = None
        self._Results = None
        self._AnalysisResults = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def ColNames(self):
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def AnalysisResults(self):
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        self._ColNames = params.get("ColNames")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = AccessLogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = AccessLogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._RequestId = params.get("RequestId")


class SearchAttackLogRequest(AbstractModel):
    """SearchAttackLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 查询的域名，所有域名使用all
        :type Domain: str
        :param _StartTime: 查询起始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _Context: 接口升级，这个字段传空字符串,翻页使用Page字段
        :type Context: str
        :param _QueryString: Lucene语法
        :type QueryString: str
        :param _Count: 查询的数量，默认10条，最多100条
        :type Count: int
        :param _Sort: 默认为desc，可以取值desc和asc
        :type Sort: str
        :param _Page: 第几页，从0开始
        :type Page: int
        """
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._QueryString = None
        self._Count = None
        self._Sort = None
        self._Page = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Context = params.get("Context")
        self._QueryString = params.get("QueryString")
        self._Count = params.get("Count")
        self._Sort = params.get("Sort")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchAttackLogResponse(AbstractModel):
    """SearchAttackLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 当前返回的攻击日志条数
        :type Count: int
        :param _Context: 接口升级，此字段无效，默认返回空字符串
        :type Context: str
        :param _Data: 攻击日志数组条目内容
        :type Data: list of AttackLogInfo
        :param _ListOver: CLS接口返回内容
        :type ListOver: bool
        :param _SqlFlag: CLS接口返回内容，标志是否启动新版本索引
        :type SqlFlag: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._Context = None
        self._Data = None
        self._ListOver = None
        self._SqlFlag = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ListOver(self):
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def SqlFlag(self):
        return self._SqlFlag

    @SqlFlag.setter
    def SqlFlag(self, SqlFlag):
        self._SqlFlag = SqlFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Context = params.get("Context")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AttackLogInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._ListOver = params.get("ListOver")
        self._SqlFlag = params.get("SqlFlag")
        self._RequestId = params.get("RequestId")


class SearchItem(AbstractModel):
    """接入列表查询复杂条件

    """

    def __init__(self):
        r"""
        :param _ClsStatus: 日志开关
        :type ClsStatus: str
        :param _Status: waf开关
        :type Status: str
        :param _FlowMode: 流量模式
        :type FlowMode: str
        """
        self._ClsStatus = None
        self._Status = None
        self._FlowMode = None

    @property
    def ClsStatus(self):
        return self._ClsStatus

    @ClsStatus.setter
    def ClsStatus(self, ClsStatus):
        self._ClsStatus = ClsStatus

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FlowMode(self):
        return self._FlowMode

    @FlowMode.setter
    def FlowMode(self, FlowMode):
        self._FlowMode = FlowMode


    def _deserialize(self, params):
        self._ClsStatus = params.get("ClsStatus")
        self._Status = params.get("Status")
        self._FlowMode = params.get("FlowMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionData(AbstractModel):
    """参数包装

    """

    def __init__(self):
        r"""
        :param _Res: session定义
        :type Res: list of SessionItem
        """
        self._Res = None

    @property
    def Res(self):
        return self._Res

    @Res.setter
    def Res(self, Res):
        self._Res = Res


    def _deserialize(self, params):
        if params.get("Res") is not None:
            self._Res = []
            for item in params.get("Res"):
                obj = SessionItem()
                obj._deserialize(item)
                self._Res.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionItem(AbstractModel):
    """session定义

    """

    def __init__(self):
        r"""
        :param _Category: 匹配类型
        :type Category: str
        :param _KeyOrStartMat: 起始模式
        :type KeyOrStartMat: str
        :param _EndMat: 结束模式
        :type EndMat: str
        :param _StartOffset: 起始偏移
        :type StartOffset: str
        :param _EndOffset: 结束偏移
        :type EndOffset: str
        :param _Source: 数据源
        :type Source: str
        :param _TsVersion: 更新时间戳
        :type TsVersion: str
        """
        self._Category = None
        self._KeyOrStartMat = None
        self._EndMat = None
        self._StartOffset = None
        self._EndOffset = None
        self._Source = None
        self._TsVersion = None

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def KeyOrStartMat(self):
        return self._KeyOrStartMat

    @KeyOrStartMat.setter
    def KeyOrStartMat(self, KeyOrStartMat):
        self._KeyOrStartMat = KeyOrStartMat

    @property
    def EndMat(self):
        return self._EndMat

    @EndMat.setter
    def EndMat(self, EndMat):
        self._EndMat = EndMat

    @property
    def StartOffset(self):
        return self._StartOffset

    @StartOffset.setter
    def StartOffset(self, StartOffset):
        self._StartOffset = StartOffset

    @property
    def EndOffset(self):
        return self._EndOffset

    @EndOffset.setter
    def EndOffset(self, EndOffset):
        self._EndOffset = EndOffset

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def TsVersion(self):
        return self._TsVersion

    @TsVersion.setter
    def TsVersion(self, TsVersion):
        self._TsVersion = TsVersion


    def _deserialize(self, params):
        self._Category = params.get("Category")
        self._KeyOrStartMat = params.get("KeyOrStartMat")
        self._EndMat = params.get("EndMat")
        self._StartOffset = params.get("StartOffset")
        self._EndOffset = params.get("EndOffset")
        self._Source = params.get("Source")
        self._TsVersion = params.get("TsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpartaProtectionPort(AbstractModel):
    """waf斯巴达-编辑防护域名中的端口结构

    """

    def __init__(self):
        r"""
        :param _NginxServerId: nginx Id
        :type NginxServerId: int
        :param _Port: 端口
        :type Port: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _UpstreamPort: 后端端口
        :type UpstreamPort: str
        :param _UpstreamProtocol: 后端协议
        :type UpstreamProtocol: str
        """
        self._NginxServerId = None
        self._Port = None
        self._Protocol = None
        self._UpstreamPort = None
        self._UpstreamProtocol = None

    @property
    def NginxServerId(self):
        return self._NginxServerId

    @NginxServerId.setter
    def NginxServerId(self, NginxServerId):
        self._NginxServerId = NginxServerId

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def UpstreamPort(self):
        return self._UpstreamPort

    @UpstreamPort.setter
    def UpstreamPort(self, UpstreamPort):
        self._UpstreamPort = UpstreamPort

    @property
    def UpstreamProtocol(self):
        return self._UpstreamProtocol

    @UpstreamProtocol.setter
    def UpstreamProtocol(self, UpstreamProtocol):
        self._UpstreamProtocol = UpstreamProtocol


    def _deserialize(self, params):
        self._NginxServerId = params.get("NginxServerId")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._UpstreamPort = params.get("UpstreamPort")
        self._UpstreamProtocol = params.get("UpstreamProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Strategy(AbstractModel):
    """自定义规则的匹配条件结构体

    """

    def __init__(self):
        r"""
        :param _Field: 匹配字段

    匹配字段不同，相应的匹配参数、逻辑符号、匹配内容有所不同具体如下所示：
<table><thead><tr><th>匹配字段</th><th>匹配参数</th><th>逻辑符号</th><th>匹配内容</th></tr></thead><tbody><tr><td>IP（来源IP）</td><td>不支持参数</td><td>ipmatch（匹配）<br/>ipnmatch（不匹配）</td><td>多个IP以英文逗号隔开,最多20个</td></tr><tr><td>IPV6（来源IPv6）</td><td>不支持参数</td><td>ipmatch（匹配）<br/>ipnmatch（不匹配）</td><td>支持单个IPV6地址</td></tr><tr><td>Referer（Referer）</td><td>不支持参数</td><td>empty（内容为空）<br/>null（不存在）<br/>eq（等于）<br/>neq（不等于）<br/>contains（包含）<br/>ncontains（不包含）<br/>len_eq（长度等于）<br/>len_gt（长度大于）<br/>len_lt（长度小于）<br/>strprefix（前缀匹配）<br/>strsuffix（后缀匹配）<br/>rematch（正则匹配）</td><td>请输入内容,512个字符以内</td></tr><tr><td>URL（请求路径）</td><td>不支持参数</td><td>eq（等于）<br/>neq（不等于）<br/>contains（包含）<br/>ncontains（不包含）<br/>len_eq（长度等于）<br/>len_gt（长度大于）<br/>len_lt（长度小于）<br/>strprefix（前缀匹配）<br/>strsuffix（后缀匹配）<br/>rematch（正则匹配）<br/></td><td>请以/开头,512个字符以内</td></tr><tr><td>UserAgent（UserAgent）</td><td>不支持参数</td><td>同匹配字段<font color="Red">Referer</font>逻辑符号</td><td>请输入内容,512个字符以内</td></tr><tr><td>HTTP_METHOD（HTTP请求方法）</td><td>不支持参数</td><td>eq（等于）<br/>neq（不等于）</td><td>请输入方法名称,建议大写</td></tr><tr><td>QUERY_STRING（请求字符串）</td><td>不支持参数</td><td>同匹配字段<font color="Red">请求路径</font>逻辑符号</td><td>请输入内容,512个字符以内</td></tr><tr><td>GET（GET参数值）</td><td>支持参数录入</td><td>contains（包含）<br/>ncontains（不包含）<br/>len_eq（长度等于）<br/>len_gt（长度大于）<br/>len_lt（长度小于）<br/>strprefix（前缀匹配）<br/>strsuffix（后缀匹配）</td><td>请输入内容,512个字符以内</td></tr><tr><td>GET_PARAMS_NAMES（GET参数名）</td><td>不支持参数</td><td>exsit（存在参数）<br/>nexsit（不存在参数）<br/>len_eq（长度等于）<br/>len_gt（长度大于）<br/>len_lt（长度小于）<br/>strprefix（前缀匹配）<br/>strsuffix（后缀匹配）</td><td>请输入内容,512个字符以内</td></tr><tr><td>POST（POST参数值）</td><td>支持参数录入</td><td>同匹配字段<font color="Red">GET参数值</font>逻辑符号</td><td>请输入内容,512个字符以内</td></tr><tr><td>GET_POST_NAMES（POST参数名）</td><td>不支持参数</td><td>同匹配字段<font color="Red">GET参数名</font>逻辑符号</td><td>请输入内容,512个字符以内</td></tr><tr><td>POST_BODY（完整BODY）</td><td>不支持参数</td><td>同匹配字段<font color="Red">请求路径</font>逻辑符号</td><td>请输入BODY内容,512个字符以内</td></tr><tr><td>COOKIE（Cookie）</td><td>不支持参数</td><td>empty（内容为空）<br/>null（不存在）<br/>rematch（正则匹配）</td><td><font color="Red">暂不支持</font></td></tr><tr><td>GET_COOKIES_NAMES（Cookie参数名）</td><td>不支持参数</td><td>同匹配字段<font color="Red">GET参数名</font>逻辑符号</td><td>请输入内容,512个字符以内</td></tr><tr><td>ARGS_COOKIE（Cookie参数值）</td><td>支持参数录入</td><td>同匹配字段<font color="Red">GET参数值</font>逻辑符号</td><td>请输入内容,512个字符以内</td></tr><tr><td>GET_HEADERS_NAMES（Header参数名）</td><td>不支持参数</td><td>exsit（存在参数）<br/>nexsit（不存在参数）<br/>len_eq（长度等于）<br/>len_gt（长度大于）<br/>len_lt（长度小于）<br/>strprefix（前缀匹配）<br/>strsuffix（后缀匹配）<br/>rematch（正则匹配）</td><td>请输入内容,建议小写,512个字符以内</td></tr><tr><td>ARGS_HEADER（Header参数值）</td><td>支持参数录入</td><td>contains（包含）<br/>ncontains（不包含）<br/>len_eq（长度等于）<br/>len_gt（长度大于）<br/>len_lt（长度小于）<br/>strprefix（前缀匹配）<br/>strsuffix（后缀匹配）<br/>rematch（正则匹配）</td><td>请输入内容,512个字符以内</td></tr></tbody></table>
注意：此字段可能返回 null，表示取不到有效值。
        :type Field: str
        :param _CompareFunc: 逻辑符号 

    逻辑符号一共分为以下几种类型：
        empty （ 内容为空）
        null （不存在）
        eq （ 等于）
        neq （ 不等于）
        contains （ 包含）
        ncontains （ 不包含）
        strprefix （ 前缀匹配）
        strsuffix （ 后缀匹配）
        len_eq （ 长度等于）
        len_gt （ 长度大于）
        len_lt （ 长度小于）
        ipmatch （ 属于）
        ipnmatch （ 不属于）
    各匹配字段对应的逻辑符号不同，详见上述匹配字段表格

注意：此字段可能返回 null，表示取不到有效值。
        :type CompareFunc: str
        :param _Content: 匹配内容

    目前 当匹配字段为COOKIE（Cookie）时，不需要输入 匹配内容其他都需要

注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Arg: 匹配参数

    配置参数一共分2种类型 不支持参数与支持参数
    当匹配字段为以下4个时，匹配参数才能录入，否则不支持该参数
        GET（GET参数值）		
        POST（POST参数值）		
        ARGS_COOKIE（Cookie参数值）		
        ARGS_HEADER（Header参数值）

注意：此字段可能返回 null，表示取不到有效值。
        :type Arg: str
        """
        self._Field = None
        self._CompareFunc = None
        self._Content = None
        self._Arg = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def CompareFunc(self):
        return self._CompareFunc

    @CompareFunc.setter
    def CompareFunc(self, CompareFunc):
        self._CompareFunc = CompareFunc

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Arg(self):
        return self._Arg

    @Arg.setter
    def Arg(self, Arg):
        self._Arg = Arg


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._CompareFunc = params.get("CompareFunc")
        self._Content = params.get("Content")
        self._Arg = params.get("Arg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StrategyForAntiInfoLeak(AbstractModel):
    """防信息泄露的匹配条件结构体

    """

    def __init__(self):
        r"""
        :param _Field: 匹配条件，returncode（响应码）、keywords（关键字）、information（敏感信息）
        :type Field: str
        :param _CompareFunc: 逻辑符号，固定取值为contains
        :type CompareFunc: str
        :param _Content: 匹配内容。
以下三个对应Field为information时可取的匹配内容：
idcard（身份证）、phone（手机号）、bankcard（银行卡）。
以下为对应Field为returncode时可取的匹配内容：
400（状态码400）、403（状态码403）、404（状态码404）、4xx（其它4xx状态码）、500（状态码500）、501（状态码501）、502（状态码502）、504（状态码504）、5xx（其它5xx状态码）。
当对应Field为keywords时由用户自己输入匹配内容。

        :type Content: str
        """
        self._Field = None
        self._CompareFunc = None
        self._Content = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def CompareFunc(self):
        return self._CompareFunc

    @CompareFunc.setter
    def CompareFunc(self, CompareFunc):
        self._CompareFunc = CompareFunc

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._CompareFunc = params.get("CompareFunc")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDomainRulesRequest(AbstractModel):
    """SwitchDomainRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Ids: 规则列表
        :type Ids: list of int non-negative
        :param _Status: 开关状态，0表示关闭，1表示开启，2表示只观察
        :type Status: int
        :param _Reason: 设置为观察模式原因，
1表示业务自身原因观察，2表示系统规则误报上报，3表示核心业务灰度观察，4表示其他
        :type Reason: int
        """
        self._Domain = None
        self._Ids = None
        self._Status = None
        self._Reason = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Ids = params.get("Ids")
        self._Status = params.get("Status")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchDomainRulesResponse(AbstractModel):
    """SwitchDomainRules返回参数结构体

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


class SwitchElasticModeRequest(AbstractModel):
    """SwitchElasticMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Edition: 版本，只能是sparta-waf, clb-waf, cdn-waf
        :type Edition: str
        :param _Mode: 0代表关闭，1代表打开
        :type Mode: int
        :param _InstanceID: 实例id
        :type InstanceID: str
        """
        self._Edition = None
        self._Mode = None
        self._InstanceID = None

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._Edition = params.get("Edition")
        self._Mode = params.get("Mode")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchElasticModeResponse(AbstractModel):
    """SwitchElasticMode返回参数结构体

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


class TLSCiphers(AbstractModel):
    """TLS 加密套件

    """

    def __init__(self):
        r"""
        :param _VersionId: TLS版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param _CipherId: 加密套件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CipherId: int
        :param _CipherName: 加密套件
注意：此字段可能返回 null，表示取不到有效值。
        :type CipherName: str
        """
        self._VersionId = None
        self._CipherId = None
        self._CipherName = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def CipherId(self):
        return self._CipherId

    @CipherId.setter
    def CipherId(self, CipherId):
        self._CipherId = CipherId

    @property
    def CipherName(self):
        return self._CipherName

    @CipherName.setter
    def CipherName(self, CipherName):
        self._CipherName = CipherName


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._CipherId = params.get("CipherId")
        self._CipherName = params.get("CipherName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TLSVersion(AbstractModel):
    """TLS信息

    """

    def __init__(self):
        r"""
        :param _VersionId: TLSVERSION的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param _VersionName: TLSVERSION的NAME
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        """
        self._VersionId = None
        self._VersionName = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetEntity(AbstractModel):
    """需要开启/关闭API安全的 实例+域名 组合实体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Domain: 域名
        :type Domain: str
        """
        self._InstanceId = None
        self._Domain = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpsertCCRuleRequest(AbstractModel):
    """UpsertCCRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Name: 名称
        :type Name: str
        :param _Status: 状态
        :type Status: int
        :param _Advance: 高级模式
        :type Advance: str
        :param _Limit: CC检测阈值
        :type Limit: str
        :param _Interval: CC检测周期
        :type Interval: str
        :param _Url: 检测Url
        :type Url: str
        :param _MatchFunc: 匹配方法
        :type MatchFunc: int
        :param _ActionType: 动作
        :type ActionType: str
        :param _Priority: 优先级
        :type Priority: int
        :param _ValidTime: 动作有效时间
        :type ValidTime: int
        :param _OptionsArr: 附加参数
        :type OptionsArr: str
        :param _Edition: waf版本
        :type Edition: str
        :param _Type: 操作类型
        :type Type: int
        :param _EventId: 添加规则的来源事件id
        :type EventId: str
        :param _SessionApplied: 规则需要启用的SessionID
        :type SessionApplied: list of int
        :param _RuleId: 规则ID，新增时填0
        :type RuleId: int
        """
        self._Domain = None
        self._Name = None
        self._Status = None
        self._Advance = None
        self._Limit = None
        self._Interval = None
        self._Url = None
        self._MatchFunc = None
        self._ActionType = None
        self._Priority = None
        self._ValidTime = None
        self._OptionsArr = None
        self._Edition = None
        self._Type = None
        self._EventId = None
        self._SessionApplied = None
        self._RuleId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Advance(self):
        return self._Advance

    @Advance.setter
    def Advance(self, Advance):
        self._Advance = Advance

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def MatchFunc(self):
        return self._MatchFunc

    @MatchFunc.setter
    def MatchFunc(self, MatchFunc):
        self._MatchFunc = MatchFunc

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def ValidTime(self):
        return self._ValidTime

    @ValidTime.setter
    def ValidTime(self, ValidTime):
        self._ValidTime = ValidTime

    @property
    def OptionsArr(self):
        return self._OptionsArr

    @OptionsArr.setter
    def OptionsArr(self, OptionsArr):
        self._OptionsArr = OptionsArr

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def SessionApplied(self):
        return self._SessionApplied

    @SessionApplied.setter
    def SessionApplied(self, SessionApplied):
        self._SessionApplied = SessionApplied

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Advance = params.get("Advance")
        self._Limit = params.get("Limit")
        self._Interval = params.get("Interval")
        self._Url = params.get("Url")
        self._MatchFunc = params.get("MatchFunc")
        self._ActionType = params.get("ActionType")
        self._Priority = params.get("Priority")
        self._ValidTime = params.get("ValidTime")
        self._OptionsArr = params.get("OptionsArr")
        self._Edition = params.get("Edition")
        self._Type = params.get("Type")
        self._EventId = params.get("EventId")
        self._SessionApplied = params.get("SessionApplied")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpsertCCRuleResponse(AbstractModel):
    """UpsertCCRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 一般为null
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RuleId: 操作的RuleId
        :type RuleId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RuleId = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class UpsertIpAccessControlRequest(AbstractModel):
    """UpsertIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Items: ip 参数列表，json数组由ip，source，note，action，valid_ts组成。ip对应配置的ip地址，source固定为custom值，note为注释，action值42为黑名单，40为白名单，valid_ts为有效日期，值为秒级时间戳（（如1680570420代表2023-04-04 09:07:00））
        :type Items: list of str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Edition: WAF实例类型，sparta-waf表示SAAS型WAF，clb-waf表示负载均衡型WAF
        :type Edition: str
        :param _SourceType: 是否为多域名黑白名单，当为多域名的黑白名单时，取值为batch，否则为空
        :type SourceType: str
        """
        self._Domain = None
        self._Items = None
        self._InstanceId = None
        self._Edition = None
        self._SourceType = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Items = params.get("Items")
        self._InstanceId = params.get("InstanceId")
        self._Edition = params.get("Edition")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpsertIpAccessControlResponse(AbstractModel):
    """UpsertIpAccessControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedItems: 添加或修改失败的条目
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedItems: str
        :param _FailedCount: 添加或修改失败的数目
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedItems = None
        self._FailedCount = None
        self._RequestId = None

    @property
    def FailedItems(self):
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

    @property
    def FailedCount(self):
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedItems = params.get("FailedItems")
        self._FailedCount = params.get("FailedCount")
        self._RequestId = params.get("RequestId")


class UpsertSessionRequest(AbstractModel):
    """UpsertSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Source: session来源位置
        :type Source: str
        :param _Category: 提取类别
        :type Category: str
        :param _KeyOrStartMat: 提取key或者起始匹配模式
        :type KeyOrStartMat: str
        :param _EndMat: 结束匹配模式
        :type EndMat: str
        :param _StartOffset: 起始偏移位置
        :type StartOffset: str
        :param _EndOffset: 结束偏移位置
        :type EndOffset: str
        :param _Edition: 版本
        :type Edition: str
        :param _SessionName: Session名
        :type SessionName: str
        :param _SessionID: Session对应ID
        :type SessionID: int
        """
        self._Domain = None
        self._Source = None
        self._Category = None
        self._KeyOrStartMat = None
        self._EndMat = None
        self._StartOffset = None
        self._EndOffset = None
        self._Edition = None
        self._SessionName = None
        self._SessionID = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def KeyOrStartMat(self):
        return self._KeyOrStartMat

    @KeyOrStartMat.setter
    def KeyOrStartMat(self, KeyOrStartMat):
        self._KeyOrStartMat = KeyOrStartMat

    @property
    def EndMat(self):
        return self._EndMat

    @EndMat.setter
    def EndMat(self, EndMat):
        self._EndMat = EndMat

    @property
    def StartOffset(self):
        return self._StartOffset

    @StartOffset.setter
    def StartOffset(self, StartOffset):
        self._StartOffset = StartOffset

    @property
    def EndOffset(self):
        return self._EndOffset

    @EndOffset.setter
    def EndOffset(self, EndOffset):
        self._EndOffset = EndOffset

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def SessionName(self):
        return self._SessionName

    @SessionName.setter
    def SessionName(self, SessionName):
        self._SessionName = SessionName

    @property
    def SessionID(self):
        return self._SessionID

    @SessionID.setter
    def SessionID(self, SessionID):
        self._SessionID = SessionID


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Source = params.get("Source")
        self._Category = params.get("Category")
        self._KeyOrStartMat = params.get("KeyOrStartMat")
        self._EndMat = params.get("EndMat")
        self._StartOffset = params.get("StartOffset")
        self._EndOffset = params.get("EndOffset")
        self._Edition = params.get("Edition")
        self._SessionName = params.get("SessionName")
        self._SessionID = params.get("SessionID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpsertSessionResponse(AbstractModel):
    """UpsertSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class UserDomainInfo(AbstractModel):
    """saas和clb信息

    """

    def __init__(self):
        r"""
        :param _Appid: 用户id
        :type Appid: int
        :param _Domain: 域名
        :type Domain: str
        :param _DomainId: 域名id
        :type DomainId: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _Edition: waf类型
        :type Edition: str
        :param _Level: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param _WriteConfig: 指定域名访问日志字段的开关
注意：此字段可能返回 null，表示取不到有效值。
        :type WriteConfig: str
        :param _Cls: 指定域名是否写cls的开关 1:写 0:不写
注意：此字段可能返回 null，表示取不到有效值。
        :type Cls: int
        :param _CloudType: 标记是否是混合云接入。hybrid表示混合云接入域名
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudType: str
        """
        self._Appid = None
        self._Domain = None
        self._DomainId = None
        self._InstanceId = None
        self._InstanceName = None
        self._Edition = None
        self._Level = None
        self._WriteConfig = None
        self._Cls = None
        self._CloudType = None

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

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
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def WriteConfig(self):
        return self._WriteConfig

    @WriteConfig.setter
    def WriteConfig(self, WriteConfig):
        self._WriteConfig = WriteConfig

    @property
    def Cls(self):
        return self._Cls

    @Cls.setter
    def Cls(self, Cls):
        self._Cls = Cls

    @property
    def CloudType(self):
        return self._CloudType

    @CloudType.setter
    def CloudType(self, CloudType):
        self._CloudType = CloudType


    def _deserialize(self, params):
        self._Appid = params.get("Appid")
        self._Domain = params.get("Domain")
        self._DomainId = params.get("DomainId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Edition = params.get("Edition")
        self._Level = params.get("Level")
        self._WriteConfig = params.get("WriteConfig")
        self._Cls = params.get("Cls")
        self._CloudType = params.get("CloudType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSignatureRule(AbstractModel):
    """用户特征规则描述

    """

    def __init__(self):
        r"""
        :param _ID: 特征ID
        :type ID: str
        :param _Status: 规则开关
        :type Status: int
        :param _MainClassID: 主类ID
        :type MainClassID: str
        :param _SubClassID: 子类ID
        :type SubClassID: str
        :param _CveID: CVE ID
        :type CveID: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 更新时间
        :type ModifyTime: str
        :param _MainClassName: 主类名字，根据Language字段输出中文/英文
        :type MainClassName: str
        :param _SubClassName: 子类名字，根据Language字段输出中文/英文，若子类id为00000000，此字段为空
        :type SubClassName: str
        :param _Description: 规则描述
        :type Description: str
        :param _Reason: 0/1
        :type Reason: int
        """
        self._ID = None
        self._Status = None
        self._MainClassID = None
        self._SubClassID = None
        self._CveID = None
        self._CreateTime = None
        self._ModifyTime = None
        self._MainClassName = None
        self._SubClassName = None
        self._Description = None
        self._Reason = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MainClassID(self):
        return self._MainClassID

    @MainClassID.setter
    def MainClassID(self, MainClassID):
        self._MainClassID = MainClassID

    @property
    def SubClassID(self):
        return self._SubClassID

    @SubClassID.setter
    def SubClassID(self, SubClassID):
        self._SubClassID = SubClassID

    @property
    def CveID(self):
        return self._CveID

    @CveID.setter
    def CveID(self, CveID):
        self._CveID = CveID

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def MainClassName(self):
        return self._MainClassName

    @MainClassName.setter
    def MainClassName(self, MainClassName):
        self._MainClassName = MainClassName

    @property
    def SubClassName(self):
        return self._SubClassName

    @SubClassName.setter
    def SubClassName(self, SubClassName):
        self._SubClassName = SubClassName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Status = params.get("Status")
        self._MainClassID = params.get("MainClassID")
        self._SubClassID = params.get("SubClassID")
        self._CveID = params.get("CveID")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._MainClassName = params.get("MainClassName")
        self._SubClassName = params.get("SubClassName")
        self._Description = params.get("Description")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VipInfo(AbstractModel):
    """Vip信息

    """

    def __init__(self):
        r"""
        :param _Vip: Virtual IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _InstanceId: waf实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        """
        self._Vip = None
        self._InstanceId = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafRuleLimit(AbstractModel):
    """waf模块的规格

    """

    def __init__(self):
        r"""
        :param _CC: 自定义CC的规格
        :type CC: int
        :param _CustomRule: 自定义策略的规格
        :type CustomRule: int
        :param _IPControl: 黑白名单的规格
        :type IPControl: int
        :param _AntiLeak: 信息防泄漏的规格
        :type AntiLeak: int
        :param _AntiTamper: 防篡改的规格
        :type AntiTamper: int
        :param _AutoCC: 紧急CC的规格
        :type AutoCC: int
        :param _AreaBan: 地域封禁的规格
        :type AreaBan: int
        :param _CCSession: 自定义CC中配置session
        :type CCSession: int
        :param _AI: AI的规格
        :type AI: int
        :param _CustomWhite: 精准白名单的规格
        :type CustomWhite: int
        :param _ApiSecurity: api安全的规格
        :type ApiSecurity: int
        :param _ClientMsg: 客户端流量标记的规格
        :type ClientMsg: int
        :param _TrafficMarking: 流量标记的规格
        :type TrafficMarking: int
        """
        self._CC = None
        self._CustomRule = None
        self._IPControl = None
        self._AntiLeak = None
        self._AntiTamper = None
        self._AutoCC = None
        self._AreaBan = None
        self._CCSession = None
        self._AI = None
        self._CustomWhite = None
        self._ApiSecurity = None
        self._ClientMsg = None
        self._TrafficMarking = None

    @property
    def CC(self):
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def CustomRule(self):
        return self._CustomRule

    @CustomRule.setter
    def CustomRule(self, CustomRule):
        self._CustomRule = CustomRule

    @property
    def IPControl(self):
        return self._IPControl

    @IPControl.setter
    def IPControl(self, IPControl):
        self._IPControl = IPControl

    @property
    def AntiLeak(self):
        return self._AntiLeak

    @AntiLeak.setter
    def AntiLeak(self, AntiLeak):
        self._AntiLeak = AntiLeak

    @property
    def AntiTamper(self):
        return self._AntiTamper

    @AntiTamper.setter
    def AntiTamper(self, AntiTamper):
        self._AntiTamper = AntiTamper

    @property
    def AutoCC(self):
        return self._AutoCC

    @AutoCC.setter
    def AutoCC(self, AutoCC):
        self._AutoCC = AutoCC

    @property
    def AreaBan(self):
        return self._AreaBan

    @AreaBan.setter
    def AreaBan(self, AreaBan):
        self._AreaBan = AreaBan

    @property
    def CCSession(self):
        return self._CCSession

    @CCSession.setter
    def CCSession(self, CCSession):
        self._CCSession = CCSession

    @property
    def AI(self):
        return self._AI

    @AI.setter
    def AI(self, AI):
        self._AI = AI

    @property
    def CustomWhite(self):
        return self._CustomWhite

    @CustomWhite.setter
    def CustomWhite(self, CustomWhite):
        self._CustomWhite = CustomWhite

    @property
    def ApiSecurity(self):
        return self._ApiSecurity

    @ApiSecurity.setter
    def ApiSecurity(self, ApiSecurity):
        self._ApiSecurity = ApiSecurity

    @property
    def ClientMsg(self):
        return self._ClientMsg

    @ClientMsg.setter
    def ClientMsg(self, ClientMsg):
        self._ClientMsg = ClientMsg

    @property
    def TrafficMarking(self):
        return self._TrafficMarking

    @TrafficMarking.setter
    def TrafficMarking(self, TrafficMarking):
        self._TrafficMarking = TrafficMarking


    def _deserialize(self, params):
        self._CC = params.get("CC")
        self._CustomRule = params.get("CustomRule")
        self._IPControl = params.get("IPControl")
        self._AntiLeak = params.get("AntiLeak")
        self._AntiTamper = params.get("AntiTamper")
        self._AutoCC = params.get("AutoCC")
        self._AreaBan = params.get("AreaBan")
        self._CCSession = params.get("CCSession")
        self._AI = params.get("AI")
        self._CustomWhite = params.get("CustomWhite")
        self._ApiSecurity = params.get("ApiSecurity")
        self._ClientMsg = params.get("ClientMsg")
        self._TrafficMarking = params.get("TrafficMarking")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafThreatenIntelligenceDetails(AbstractModel):
    """当前WAF威胁情报封禁模块详情

    """

    def __init__(self):
        r"""
        :param _Tags: 封禁属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _DefenseStatus: 封禁模组启用状态
        :type DefenseStatus: int
        :param _LastUpdateTime: 最后更新时间
        :type LastUpdateTime: str
        """
        self._Tags = None
        self._DefenseStatus = None
        self._LastUpdateTime = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DefenseStatus(self):
        return self._DefenseStatus

    @DefenseStatus.setter
    def DefenseStatus(self, DefenseStatus):
        self._DefenseStatus = DefenseStatus

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._Tags = params.get("Tags")
        self._DefenseStatus = params.get("DefenseStatus")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebshellStatus(AbstractModel):
    """域名的webshell开启状态

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Status: webshell开关，1：开。0：关。2：观察
        :type Status: int
        """
        self._Domain = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        