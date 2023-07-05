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
        :param _Status: 规则的开关
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
        :param _Domain: 需要防御的域名
        :type Domain: str
        :param _CertType: 证书类型，0表示没有证书，CertType=1表示自有证书,2 为托管证书
        :type CertType: int
        :param _IsCdn: 表示是否开启了CDN代理，1：有部署CDN，0：未部署CDN
        :type IsCdn: int
        :param _UpstreamType: 回源类型，0表示通过IP回源,1 表示通过域名回源
        :type UpstreamType: int
        :param _IsWebsocket: 是否开启WebSocket支持，1表示开启，0不开启
        :type IsWebsocket: int
        :param _LoadBalance: 负载均衡策略，0表示轮徇，1表示IP hash
        :type LoadBalance: str
        :param _Cert: CertType=1时，需要填次参数，表示证书内容
        :type Cert: str
        :param _PrivateKey: CertType=1时，需要填次参数，表示证书的私钥
        :type PrivateKey: str
        :param _SSLId: CertType=2时，需要填次参数，表示证书的ID
        :type SSLId: str
        :param _ResourceId: Waf的资源ID
        :type ResourceId: str
        :param _UpstreamScheme: HTTPS回源协议，填http或者https
        :type UpstreamScheme: str
        :param _HttpsUpstreamPort: HTTPS回源端口,仅UpstreamScheme为http时需要填当前字段
        :type HttpsUpstreamPort: str
        :param _IsGray: 是否开启灰度，0表示不开启灰度
        :type IsGray: int
        :param _GrayAreas: 灰度的地区
        :type GrayAreas: list of str
        :param _UpstreamDomain: UpstreamType=1时，填次字段表示回源域名
        :type UpstreamDomain: str
        :param _SrcList: UpstreamType=0时，填次字段表示回源IP
        :type SrcList: list of str
        :param _IsHttp2: 是否开启HTTP2,开启HTTP2需要HTTPS支持
        :type IsHttp2: int
        :param _HttpsRewrite: 表示是否强制跳转到HTTPS，1强制跳转Https，0不强制跳转
        :type HttpsRewrite: int
        :param _Ports: 服务有多端口需要设置此字段
        :type Ports: list of PortItem
        :param _Edition: WAF实例类型，sparta-waf表示SAAS型WAF，clb-waf表示负载均衡型WAF，cdn-waf表示CDN上的Web防护能力
        :type Edition: str
        :param _IsKeepAlive: 是否开启长连接，仅IP回源时可以用填次参数，域名回源时这个参数无效
        :type IsKeepAlive: str
        :param _InstanceID: 实例id，上线之后带上此字段
        :type InstanceID: str
        :param _Anycast: anycast IP类型开关： 0 普通IP 1 Anycast IP
        :type Anycast: int
        :param _Weights: src权重
        :type Weights: list of int
        :param _ActiveCheck: 是否开启主动健康检测，1表示开启，0表示不开启
        :type ActiveCheck: int
        :param _TLSVersion: TLS版本信息
        :type TLSVersion: int
        :param _Ciphers: 加密套件信息
        :type Ciphers: list of int
        :param _CipherTemplate: 0:不支持选择：默认模版  1:通用型模版 2:安全型模版 3:自定义模版
        :type CipherTemplate: int
        :param _ProxyReadTimeout: 300s
        :type ProxyReadTimeout: int
        :param _ProxySendTimeout: 300s
        :type ProxySendTimeout: int
        :param _SniType: 0:关闭SNI；1:开启SNI，SNI=源请求host；2:开启SNI，SNI=修改为源站host；3：开启SNI，自定义host，SNI=SniHost；
        :type SniType: int
        :param _SniHost: SniType=3时，需要填此参数，表示自定义的host；
        :type SniHost: str
        :param _IpHeaders: is_cdn=3时，需要填此参数，表示自定义header
        :type IpHeaders: list of str
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
        self._UpstreamScheme = None
        self._HttpsUpstreamPort = None
        self._IsGray = None
        self._GrayAreas = None
        self._UpstreamDomain = None
        self._SrcList = None
        self._IsHttp2 = None
        self._HttpsRewrite = None
        self._Ports = None
        self._Edition = None
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
    def HttpsRewrite(self):
        return self._HttpsRewrite

    @HttpsRewrite.setter
    def HttpsRewrite(self, HttpsRewrite):
        self._HttpsRewrite = HttpsRewrite

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
        self._UpstreamScheme = params.get("UpstreamScheme")
        self._HttpsUpstreamPort = params.get("HttpsUpstreamPort")
        self._IsGray = params.get("IsGray")
        self._GrayAreas = params.get("GrayAreas")
        self._UpstreamDomain = params.get("UpstreamDomain")
        self._SrcList = params.get("SrcList")
        self._IsHttp2 = params.get("IsHttp2")
        self._HttpsRewrite = params.get("HttpsRewrite")
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
        self._Ciphers = params.get("Ciphers")
        self._CipherTemplate = params.get("CipherTemplate")
        self._ProxyReadTimeout = params.get("ProxyReadTimeout")
        self._ProxySendTimeout = params.get("ProxySendTimeout")
        self._SniType = params.get("SniType")
        self._SniHost = params.get("SniHost")
        self._IpHeaders = params.get("IpHeaders")
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


class DeleteIpAccessControlRequest(AbstractModel):
    """DeleteIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Items: 删除的ip数组
        :type Items: list of str
        :param _DeleteAll: 是否删除对应的域名下的所有黑/白IP名单，true表示全部删除，false表示只删除指定ip名单
        :type DeleteAll: bool
        :param _SourceType: 是否为多域名黑白名单
        :type SourceType: str
        """
        self._Domain = None
        self._Items = None
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
        """
        self._TopicId = None
        self._From = None
        self._To = None
        self._Query = None
        self._FieldName = None

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


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._FieldName = params.get("FieldName")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessCount = None
        self._AttackCount = None
        self._ACLCount = None
        self._CCCount = None
        self._BotCount = None
        self._ApiAssetsCount = None
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
        :param _Offset: 数据偏移量，从1开始。
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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移
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
        :param _MetricName: 十三个值可选：
access-峰值qps趋势图
botAccess- bot峰值qps趋势图
down-下行峰值带宽趋势图
up-上行峰值带宽趋势图
attack-Web攻击总数趋势图
cc-CC攻击总数趋势图
StatusServerError-WAF返回给客户端状态码次数趋势图
StatusClientError-WAF返回给客户端状态码次数趋势图
StatusRedirect-WAF返回给客户端状态码次数趋势图
StatusOk-WAF返回给客户端状态码次数趋势图
UpstreamServerError-源站返回给WAF状态码次数趋势图
UpstreamClientError-源站返回给WAF状态码次数趋势图
UpstreamRedirect-源站返回给WAF状态码次数趋势图
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


class DescribeRuleLimitRequest(AbstractModel):
    """DescribeRuleLimit请求参数结构体

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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttackThreshold = None
        self._TimeThreshold = None
        self._DenyTimeThreshold = None
        self._DefenseStatus = None
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
        :param _Mode: 规则防御模式,0观察模式 1拦截模式
        :type Mode: int
        :param _Engine: AI防御模式,10规则引擎观察&&AI引擎关闭模式 11规则引擎观察&&AI引擎观察模式 12规则引擎观察&&AI引擎拦截模式 20规则引擎拦截&&AI引擎关闭模式 21规则引擎拦截&&AI引擎观察模式 22规则引擎拦截&&AI引擎拦截模式
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
        :type ResourceIds: str
        :param _ValidTime: 过期时间
        :type ValidTime: str
        :param _RenewFlag: 是否自动续费，1：自动续费，0：不自动续费
        :type RenewFlag: int
        :param _Count: 套餐购买个数
        :type Count: int
        :param _Region: 套餐购买地域，clb-waf暂时没有用到
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
        


class DomainsPartInfo(AbstractModel):
    """saas域名详情

    """

    def __init__(self):
        r"""
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
        :param _CipherTemplate: 模版
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
        """
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


    def _deserialize(self, params):
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
        :param _Mode: waf模式，同saas waf保持一致
        :type Mode: int
        :param _Status: waf和LD的绑定，0：没有绑定，1：绑定
        :type Status: int
        :param _State: 域名状态，0：正常，1：未检测到流量，2：即将过期，3：过期
        :type State: int
        :param _Engine: 使用的规则，同saas waf保持一致
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
        :param _MaxBandwidth: 带宽峰值
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
        """
        self._ActionType = None
        self._Ip = None
        self._Note = None
        self._Source = None
        self._TsVersion = None
        self._ValidTs = None

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


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        self._Ip = params.get("Ip")
        self._Note = params.get("Note")
        self._Source = params.get("Source")
        self._TsVersion = params.get("TsVersion")
        self._ValidTs = params.get("ValidTs")
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


class ModifyAreaBanStatusRequest(AbstractModel):
    """ModifyAreaBanStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 修要修改的域名
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
        :param _Bypass: 放行时是否继续执行其它检查逻辑，继续执行地域封禁防护：geoip、继续执行CC策略防护：cc、继续执行WEB应用防护：owasp、继续执行AI引擎防护：ai、继续执行信息防泄漏防护：antileakage。如果多个勾选那么以,串接。
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
        :param _CipherTemplate: 0:不支持选择：默认模版  1:通用型模版 2:安全型模版 3:自定义模版
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
        :param _DefenseStatus: 自动封禁状态
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
        :param _StatusServerError: WAF返回给客户端状态码次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusServerError: int
        :param _StatusClientError: WAF返回给客户端状态码次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusClientError: int
        :param _StatusRedirect: WAF返回给客户端状态码次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusRedirect: int
        :param _StatusOk: WAF返回给客户端状态码次数
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusOk: int
        :param _UpstreamServerError: 源站返回给WAF状态码次数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamServerError: int
        :param _UpstreamClientError: 源站返回给WAF状态码次数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamClientError: int
        :param _UpstreamRedirect: 源站返回给WAF状态码次数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamRedirect: int
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
        :type ResourceIds: str
        :param _ValidTime: 过期时间
        :type ValidTime: str
        :param _RenewFlag: 是否自动续费，1：自动续费，0：不自动续费
        :type RenewFlag: int
        :param _Count: 套餐购买个数
        :type Count: int
        :param _Region: 套餐购买地域，clb-waf暂时没有用到
        :type Region: str
        :param _BillingItem: 计费项
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
        :param _Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。
新版本此字段填空填
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
        :param _Context: 加载后续内容的Context
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
        :param _Context: 查询的游标。第一次请求使用空字符串即可，后续请求使用上一次请求返回的最后一条记录的context的值即可。
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
        :param _Context: 翻页游标，如果没有下一页了，这个参数为空""
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Field: str
        :param _CompareFunc: 逻辑符号
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareFunc: str
        :param _Content: 匹配内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Arg: 匹配参数
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
        


class SwitchDomainRulesRequest(AbstractModel):
    """SwitchDomainRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Ids: 规则列表
        :type Ids: list of int non-negative
        :param _Status: 开关状态
        :type Status: int
        :param _Reason: 设置为观察模式原因
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


class UpsertIpAccessControlRequest(AbstractModel):
    """UpsertIpAccessControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Items: ip 参数列表，json数组由ip，source，note，action，valid_ts组成。ip对应配置的ip地址，source固定为custom值，note为注释，action值42为黑名单，40为白名单，valid_ts为有效日期，值为秒级时间戳（（如1680570420代表2023-04-04 09:07:00））
        :type Items: list of str
        :param _Edition: WAF实例类型，sparta-waf表示SAAS型WAF，clb-waf表示负载均衡型WAF
        :type Edition: str
        :param _SourceType: 是否为多域名黑白名单，当为多域名的黑白名单时，取值为batch，否则为空
        :type SourceType: str
        """
        self._Domain = None
        self._Items = None
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
        