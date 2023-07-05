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


class APMKV(AbstractModel):
    """APM浮点数类型键值对

    """

    def __init__(self):
        r"""
        :param _Key: Key值定义
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: Value值定义
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
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
        


class APMKVItem(AbstractModel):
    """Apm通用KV结构

    """

    def __init__(self):
        r"""
        :param _Key: Key值定义
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: Value值定义
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
        


class ApmAgentInfo(AbstractModel):
    """apm Agent信息

    """

    def __init__(self):
        r"""
        :param _AgentDownloadURL: Agent下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentDownloadURL: str
        :param _CollectorURL: Collector上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorURL: str
        :param _Token: Token信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _PublicCollectorURL: 外网上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicCollectorURL: str
        :param _InnerCollectorURL: 自研VPC上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerCollectorURL: str
        :param _PrivateLinkCollectorURL: 内网上报地址(Private Link上报地址)
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateLinkCollectorURL: str
        """
        self._AgentDownloadURL = None
        self._CollectorURL = None
        self._Token = None
        self._PublicCollectorURL = None
        self._InnerCollectorURL = None
        self._PrivateLinkCollectorURL = None

    @property
    def AgentDownloadURL(self):
        return self._AgentDownloadURL

    @AgentDownloadURL.setter
    def AgentDownloadURL(self, AgentDownloadURL):
        self._AgentDownloadURL = AgentDownloadURL

    @property
    def CollectorURL(self):
        return self._CollectorURL

    @CollectorURL.setter
    def CollectorURL(self, CollectorURL):
        self._CollectorURL = CollectorURL

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def PublicCollectorURL(self):
        return self._PublicCollectorURL

    @PublicCollectorURL.setter
    def PublicCollectorURL(self, PublicCollectorURL):
        self._PublicCollectorURL = PublicCollectorURL

    @property
    def InnerCollectorURL(self):
        return self._InnerCollectorURL

    @InnerCollectorURL.setter
    def InnerCollectorURL(self, InnerCollectorURL):
        self._InnerCollectorURL = InnerCollectorURL

    @property
    def PrivateLinkCollectorURL(self):
        return self._PrivateLinkCollectorURL

    @PrivateLinkCollectorURL.setter
    def PrivateLinkCollectorURL(self, PrivateLinkCollectorURL):
        self._PrivateLinkCollectorURL = PrivateLinkCollectorURL


    def _deserialize(self, params):
        self._AgentDownloadURL = params.get("AgentDownloadURL")
        self._CollectorURL = params.get("CollectorURL")
        self._Token = params.get("Token")
        self._PublicCollectorURL = params.get("PublicCollectorURL")
        self._InnerCollectorURL = params.get("InnerCollectorURL")
        self._PrivateLinkCollectorURL = params.get("PrivateLinkCollectorURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmField(AbstractModel):
    """指标维度信息

    """

    def __init__(self):
        r"""
        :param _CompareVal: 昨日同比指标值，已弃用，不建议使用
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareVal: str
        :param _CompareVals: Compare值结果数组，推荐使用
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareVals: list of APMKVItem
        :param _Value: 指标值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        :param _Unit: 指标所对应的单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Key: 请求数
        :type Key: str
        :param _LastPeriodValue: 同环比上周期具体数值
注意：此字段可能返回 null，表示取不到有效值。
        :type LastPeriodValue: list of APMKV
        """
        self._CompareVal = None
        self._CompareVals = None
        self._Value = None
        self._Unit = None
        self._Key = None
        self._LastPeriodValue = None

    @property
    def CompareVal(self):
        return self._CompareVal

    @CompareVal.setter
    def CompareVal(self, CompareVal):
        self._CompareVal = CompareVal

    @property
    def CompareVals(self):
        return self._CompareVals

    @CompareVals.setter
    def CompareVals(self, CompareVals):
        self._CompareVals = CompareVals

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def LastPeriodValue(self):
        return self._LastPeriodValue

    @LastPeriodValue.setter
    def LastPeriodValue(self, LastPeriodValue):
        self._LastPeriodValue = LastPeriodValue


    def _deserialize(self, params):
        self._CompareVal = params.get("CompareVal")
        if params.get("CompareVals") is not None:
            self._CompareVals = []
            for item in params.get("CompareVals"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._CompareVals.append(obj)
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        self._Key = params.get("Key")
        if params.get("LastPeriodValue") is not None:
            self._LastPeriodValue = []
            for item in params.get("LastPeriodValue"):
                obj = APMKV()
                obj._deserialize(item)
                self._LastPeriodValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmInstanceDetail(AbstractModel):
    """apm实例信息

    """

    def __init__(self):
        r"""
        :param _AmountOfUsedStorage: 存储使用量(MB)
注意：此字段可能返回 null，表示取不到有效值。
        :type AmountOfUsedStorage: float
        :param _Name: 实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Tags: 实例所属tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApmTag
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _CreateUin: 创建人Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        :param _ServiceCount: 该实例已上报的服务端应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param _CountOfReportSpanPerDay: 日均上报Span数
注意：此字段可能返回 null，表示取不到有效值。
        :type CountOfReportSpanPerDay: int
        :param _AppId: AppId信息
        :type AppId: int
        :param _TraceDuration: Trace数据保存时长
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceDuration: int
        :param _Description: 实例描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Status: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Region: 实例所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _SpanDailyCounters: 实例上报额度
注意：此字段可能返回 null，表示取不到有效值。
        :type SpanDailyCounters: int
        :param _BillingInstance: 实例是否开通计费
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInstance: int
        :param _ErrRateThreshold: 错误率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrRateThreshold: int
        :param _SampleRate: 采样率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleRate: int
        :param _ErrorSample: 是否开启错误采样 0  关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorSample: int
        :param _SlowRequestSavedThreshold: 慢调用保存阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowRequestSavedThreshold: int
        :param _LogRegion: cls日志所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRegion: str
        :param _LogSource: 日志来源
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSource: str
        :param _IsRelatedLog: 日志功能开关 0 关 | 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRelatedLog: int
        :param _LogTopicID: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicID: str
        :param _ClientCount: 该实例已上报的客户端应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCount: int
        :param _TotalCount: 该实例已上报的总应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _LogSet: CLS日志集 | ES集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSet: str
        :param _MetricDuration: Metric数据保存时长
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricDuration: int
        """
        self._AmountOfUsedStorage = None
        self._Name = None
        self._Tags = None
        self._InstanceId = None
        self._CreateUin = None
        self._ServiceCount = None
        self._CountOfReportSpanPerDay = None
        self._AppId = None
        self._TraceDuration = None
        self._Description = None
        self._Status = None
        self._Region = None
        self._SpanDailyCounters = None
        self._BillingInstance = None
        self._ErrRateThreshold = None
        self._SampleRate = None
        self._ErrorSample = None
        self._SlowRequestSavedThreshold = None
        self._LogRegion = None
        self._LogSource = None
        self._IsRelatedLog = None
        self._LogTopicID = None
        self._ClientCount = None
        self._TotalCount = None
        self._LogSet = None
        self._MetricDuration = None

    @property
    def AmountOfUsedStorage(self):
        return self._AmountOfUsedStorage

    @AmountOfUsedStorage.setter
    def AmountOfUsedStorage(self, AmountOfUsedStorage):
        self._AmountOfUsedStorage = AmountOfUsedStorage

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def ServiceCount(self):
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def CountOfReportSpanPerDay(self):
        return self._CountOfReportSpanPerDay

    @CountOfReportSpanPerDay.setter
    def CountOfReportSpanPerDay(self, CountOfReportSpanPerDay):
        self._CountOfReportSpanPerDay = CountOfReportSpanPerDay

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def TraceDuration(self):
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    def SpanDailyCounters(self):
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def BillingInstance(self):
        return self._BillingInstance

    @BillingInstance.setter
    def BillingInstance(self, BillingInstance):
        self._BillingInstance = BillingInstance

    @property
    def ErrRateThreshold(self):
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def LogRegion(self):
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogSource(self):
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def IsRelatedLog(self):
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogTopicID(self):
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def ClientCount(self):
        return self._ClientCount

    @ClientCount.setter
    def ClientCount(self, ClientCount):
        self._ClientCount = ClientCount

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def MetricDuration(self):
        return self._MetricDuration

    @MetricDuration.setter
    def MetricDuration(self, MetricDuration):
        self._MetricDuration = MetricDuration


    def _deserialize(self, params):
        self._AmountOfUsedStorage = params.get("AmountOfUsedStorage")
        self._Name = params.get("Name")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._CreateUin = params.get("CreateUin")
        self._ServiceCount = params.get("ServiceCount")
        self._CountOfReportSpanPerDay = params.get("CountOfReportSpanPerDay")
        self._AppId = params.get("AppId")
        self._TraceDuration = params.get("TraceDuration")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._SpanDailyCounters = params.get("SpanDailyCounters")
        self._BillingInstance = params.get("BillingInstance")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._SampleRate = params.get("SampleRate")
        self._ErrorSample = params.get("ErrorSample")
        self._SlowRequestSavedThreshold = params.get("SlowRequestSavedThreshold")
        self._LogRegion = params.get("LogRegion")
        self._LogSource = params.get("LogSource")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogTopicID = params.get("LogTopicID")
        self._ClientCount = params.get("ClientCount")
        self._TotalCount = params.get("TotalCount")
        self._LogSet = params.get("LogSet")
        self._MetricDuration = params.get("MetricDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmMetricRecord(AbstractModel):
    """指标列表单元

    """

    def __init__(self):
        r"""
        :param _Fields: field数组
        :type Fields: list of ApmField
        :param _Tags: tag数组
        :type Tags: list of ApmTag
        """
        self._Fields = None
        self._Tags = None

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = ApmField()
                obj._deserialize(item)
                self._Fields.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmTag(AbstractModel):
    """维度（标签）对象

    """

    def __init__(self):
        r"""
        :param _Key: 维度Key(列名，标签Key)
        :type Key: str
        :param _Value: 维度值（标签值）
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
        


class CreateApmInstanceRequest(AbstractModel):
    """CreateApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 实例名
        :type Name: str
        :param _Description: 实例描述信息
        :type Description: str
        :param _TraceDuration: Trace数据保存时长
        :type TraceDuration: int
        :param _Tags: 标签列表
        :type Tags: list of ApmTag
        :param _SpanDailyCounters: 实例上报额度值
        :type SpanDailyCounters: int
        """
        self._Name = None
        self._Description = None
        self._TraceDuration = None
        self._Tags = None
        self._SpanDailyCounters = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SpanDailyCounters(self):
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._TraceDuration = params.get("TraceDuration")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SpanDailyCounters = params.get("SpanDailyCounters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmInstanceResponse(AbstractModel):
    """CreateApmInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
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


class DescribeApmAgentRequest(AbstractModel):
    """DescribeApmAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AgentType: 接入方式
        :type AgentType: str
        :param _NetworkMode: 环境
        :type NetworkMode: str
        :param _LanguageEnvironment: 语言
        :type LanguageEnvironment: str
        :param _ReportMethod: 上报方式
        :type ReportMethod: str
        """
        self._InstanceId = None
        self._AgentType = None
        self._NetworkMode = None
        self._LanguageEnvironment = None
        self._ReportMethod = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentType(self):
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def NetworkMode(self):
        return self._NetworkMode

    @NetworkMode.setter
    def NetworkMode(self, NetworkMode):
        self._NetworkMode = NetworkMode

    @property
    def LanguageEnvironment(self):
        return self._LanguageEnvironment

    @LanguageEnvironment.setter
    def LanguageEnvironment(self, LanguageEnvironment):
        self._LanguageEnvironment = LanguageEnvironment

    @property
    def ReportMethod(self):
        return self._ReportMethod

    @ReportMethod.setter
    def ReportMethod(self, ReportMethod):
        self._ReportMethod = ReportMethod


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AgentType = params.get("AgentType")
        self._NetworkMode = params.get("NetworkMode")
        self._LanguageEnvironment = params.get("LanguageEnvironment")
        self._ReportMethod = params.get("ReportMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmAgentResponse(AbstractModel):
    """DescribeApmAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmAgent: Agent信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmAgent: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmAgent = None
        self._RequestId = None

    @property
    def ApmAgent(self):
        return self._ApmAgent

    @ApmAgent.setter
    def ApmAgent(self, ApmAgent):
        self._ApmAgent = ApmAgent

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApmAgent") is not None:
            self._ApmAgent = ApmAgentInfo()
            self._ApmAgent._deserialize(params.get("ApmAgent"))
        self._RequestId = params.get("RequestId")


class DescribeApmInstancesRequest(AbstractModel):
    """DescribeApmInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tags: Tag列表
        :type Tags: list of ApmTag
        :param _InstanceName: 搜索实例名
        :type InstanceName: str
        :param _InstanceIds: 过滤实例ID
        :type InstanceIds: list of str
        :param _DemoInstanceFlag: 是否查询官方demo实例
        :type DemoInstanceFlag: int
        :param _AllRegionsFlag: 是否查询全地域实例
        :type AllRegionsFlag: int
        """
        self._Tags = None
        self._InstanceName = None
        self._InstanceIds = None
        self._DemoInstanceFlag = None
        self._AllRegionsFlag = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DemoInstanceFlag(self):
        return self._DemoInstanceFlag

    @DemoInstanceFlag.setter
    def DemoInstanceFlag(self, DemoInstanceFlag):
        self._DemoInstanceFlag = DemoInstanceFlag

    @property
    def AllRegionsFlag(self):
        return self._AllRegionsFlag

    @AllRegionsFlag.setter
    def AllRegionsFlag(self, AllRegionsFlag):
        self._AllRegionsFlag = AllRegionsFlag


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceName = params.get("InstanceName")
        self._InstanceIds = params.get("InstanceIds")
        self._DemoInstanceFlag = params.get("DemoInstanceFlag")
        self._AllRegionsFlag = params.get("AllRegionsFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmInstancesResponse(AbstractModel):
    """DescribeApmInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: apm实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of ApmInstanceDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._RequestId = None

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = ApmInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGeneralMetricDataRequest(AbstractModel):
    """DescribeGeneralMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 要过滤的维度信息：
service_metric视图支持：service.name（服务名）、span.kind（客户端/服务端视角）为维度进行过滤，service.name（服务名）必填。
span.kind:
	server:服务端视角
	client:客户端视角
默认为服务端视角进行查询。
runtime_metric视图支持：service.name（服务名）维度进行过滤，service.name（服务名）必填。
sql_metric视图支持：service.name（服务名）、db.instance（数据库名称）、db.ip（数据库实例ip）维度进行过滤，查询service_slow_sql_count（慢sql）指标时service.name必填，查询sql_duration_avg（耗时）指标时db.instance（数据库名称）必填。
        :type Filters: list of GeneralFilter
        :param _Metrics: 需要查询的指标，不可自定义输入。
service_metric视图支持：service_request_count（总请求）、service_duration（平均响应时间）、service_error_req_rate（平均错误率）、service_slow_call_count（慢调用）、service_error_request_count（异常数量）。
runtime_metric视图支持：service_gc_full_count（Full GC）。
sql_metric视图支持：service_slow_sql_count（慢sql）、sql_duration_avg（耗时）。
        :type Metrics: list of str
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _ViewName: 视图名称，不可自定义输入。支持：service_metric、runtime_metric、sql_metric。
        :type ViewName: str
        :param _GroupBy: 聚合维度：
service_metric视图支持：service.name（服务名）、span.kind （客户端/服务端视角）维度进行聚合，service.name（服务名）必填。
runtime_metric视图支持：service.name（服务名）维度进行聚合，service.name（服务名）必填。
sql_metric视图支持：service.name（服务名）、db.statement（sql语句）维度进行聚合，查询service_slow_sql_count（慢sql）时service.name（服务名）必填，查询sql_duration_avg（耗时）指标时service.name（服务名）、db.statement（sql语句）必填。
        :type GroupBy: list of str
        :param _StartTime: 起始时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :type StartTime: int
        :param _EndTime: 结束时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :type EndTime: int
        :param _Period: 聚合粒度，单位为秒，最小为60s，即一分钟的聚合粒度；如果为空或0则计算开始时间到截止时间的指标数据，上报其他值会报错。
        :type Period: int
        :param _OrderBy: 对查询指标进行排序：
service_metric视图支持：service_request_count（总请求）、service_duration（平均响应时间）、service_error_req_rate（平均错误率）、service_slow_call_count（慢调用）、service_error_request_count（异常数量）。
runtime_metric视图支持：service_gc_full_count（Full GC）。
sql_metric视图支持：service_slow_sql_count（慢sql）、sql_duration_avg（耗时）。
asc:对查询指标进行升序排序
desc：对查询指标进行降序排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _PageSize: 查询指标的限制条数，目前最多展示50条数据，PageSize取值为1-50，上送PageSize则根据PageSize的值展示限制条数。
        :type PageSize: int
        """
        self._Filters = None
        self._Metrics = None
        self._InstanceId = None
        self._ViewName = None
        self._GroupBy = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._OrderBy = None
        self._PageSize = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ViewName(self):
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

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
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = GeneralFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Metrics = params.get("Metrics")
        self._InstanceId = params.get("InstanceId")
        self._ViewName = params.get("ViewName")
        self._GroupBy = params.get("GroupBy")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralMetricDataResponse(AbstractModel):
    """DescribeGeneralMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of Line
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
                obj = Line()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMetricRecordsRequest(AbstractModel):
    """DescribeMetricRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Metrics: 指标列表
        :type Metrics: list of QueryMetricItem
        :param _GroupBy: 聚合维度
        :type GroupBy: list of str
        :param _OrderBy: 排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Limit: 每页大小
        :type Limit: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Offset: 分页起始点
        :type Offset: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _BusinessName: 业务名称（默认值：taw）
        :type BusinessName: str
        :param _PageIndex: 页码
        :type PageIndex: int
        :param _PageSize: 页长
        :type PageSize: int
        :param _OrFilters: Or过滤条件
        :type OrFilters: list of Filter
        """
        self._Filters = None
        self._Metrics = None
        self._GroupBy = None
        self._OrderBy = None
        self._InstanceId = None
        self._Limit = None
        self._StartTime = None
        self._Offset = None
        self._EndTime = None
        self._BusinessName = None
        self._PageIndex = None
        self._PageSize = None
        self._OrFilters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BusinessName(self):
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def PageIndex(self):
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OrFilters(self):
        return self._OrFilters

    @OrFilters.setter
    def OrFilters(self, OrFilters):
        self._OrFilters = OrFilters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._GroupBy = params.get("GroupBy")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._Offset = params.get("Offset")
        self._EndTime = params.get("EndTime")
        self._BusinessName = params.get("BusinessName")
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        if params.get("OrFilters") is not None:
            self._OrFilters = []
            for item in params.get("OrFilters"):
                obj = Filter()
                obj._deserialize(item)
                self._OrFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMetricRecordsResponse(AbstractModel):
    """DescribeMetricRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of ApmMetricRecord
        :param _TotalCount: 查询指标结果集条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeServiceOverviewRequest(AbstractModel):
    """DescribeServiceOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Metrics: 指标列表
        :type Metrics: list of QueryMetricItem
        :param _GroupBy: 聚合维度
        :type GroupBy: list of str
        :param _OrderBy: 排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Limit: 每页大小
        :type Limit: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Offset: 分页起始点
        :type Offset: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._Filters = None
        self._Metrics = None
        self._GroupBy = None
        self._OrderBy = None
        self._InstanceId = None
        self._Limit = None
        self._StartTime = None
        self._Offset = None
        self._EndTime = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._GroupBy = params.get("GroupBy")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._Offset = params.get("Offset")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceOverviewResponse(AbstractModel):
    """DescribeServiceOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of ApmMetricRecord
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
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询过滤参数

    """

    def __init__(self):
        r"""
        :param _Type: 过滤方式（=, !=, in）
        :type Type: str
        :param _Key: 过滤维度名
        :type Key: str
        :param _Value: 过滤值，in过滤方式用逗号分割多个值
        :type Value: str
        """
        self._Type = None
        self._Key = None
        self._Value = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralFilter(AbstractModel):
    """查询过滤参数

    """

    def __init__(self):
        r"""
        :param _Key: 过滤维度名
        :type Key: str
        :param _Value: 过滤值
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
        


class Line(AbstractModel):
    """指标曲线数据

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _MetricNameCN: 指标中文名
        :type MetricNameCN: str
        :param _TimeSerial: 时间序列
        :type TimeSerial: list of int
        :param _DataSerial: 数据序列
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSerial: list of float
        :param _Tags: 维度列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApmTag
        """
        self._MetricName = None
        self._MetricNameCN = None
        self._TimeSerial = None
        self._DataSerial = None
        self._Tags = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricNameCN(self):
        return self._MetricNameCN

    @MetricNameCN.setter
    def MetricNameCN(self, MetricNameCN):
        self._MetricNameCN = MetricNameCN

    @property
    def TimeSerial(self):
        return self._TimeSerial

    @TimeSerial.setter
    def TimeSerial(self, TimeSerial):
        self._TimeSerial = TimeSerial

    @property
    def DataSerial(self):
        return self._DataSerial

    @DataSerial.setter
    def DataSerial(self, DataSerial):
        self._DataSerial = DataSerial

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._MetricNameCN = params.get("MetricNameCN")
        self._TimeSerial = params.get("TimeSerial")
        self._DataSerial = params.get("DataSerial")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmInstanceRequest(AbstractModel):
    """ModifyApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 实例名
        :type Name: str
        :param _Tags: 标签列表
        :type Tags: list of ApmTag
        :param _Description: 实例详情
        :type Description: str
        :param _TraceDuration: Trace数据保存时长
        :type TraceDuration: int
        :param _OpenBilling: 是否开启计费
        :type OpenBilling: bool
        :param _SpanDailyCounters: 实例上报额度
        :type SpanDailyCounters: int
        :param _ErrRateThreshold: 错误率阈值
        :type ErrRateThreshold: int
        :param _SampleRate: 采样率
        :type SampleRate: int
        :param _ErrorSample: 是否开启错误采样 0 关 1 开
        :type ErrorSample: int
        :param _SlowRequestSavedThreshold: 慢请求阈值
        :type SlowRequestSavedThreshold: int
        :param _IsRelatedLog: 是否开启日志功能 0 关 1 开
        :type IsRelatedLog: int
        :param _LogRegion: 日志地域
        :type LogRegion: str
        :param _LogTopicID: CLS日志主题ID | ES 索引名
        :type LogTopicID: str
        :param _LogSet: CLS日志集 | ES集群ID
        :type LogSet: str
        :param _LogSource: CLS | ES
        :type LogSource: str
        """
        self._InstanceId = None
        self._Name = None
        self._Tags = None
        self._Description = None
        self._TraceDuration = None
        self._OpenBilling = None
        self._SpanDailyCounters = None
        self._ErrRateThreshold = None
        self._SampleRate = None
        self._ErrorSample = None
        self._SlowRequestSavedThreshold = None
        self._IsRelatedLog = None
        self._LogRegion = None
        self._LogTopicID = None
        self._LogSet = None
        self._LogSource = None

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
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def OpenBilling(self):
        return self._OpenBilling

    @OpenBilling.setter
    def OpenBilling(self, OpenBilling):
        self._OpenBilling = OpenBilling

    @property
    def SpanDailyCounters(self):
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def ErrRateThreshold(self):
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def IsRelatedLog(self):
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogRegion(self):
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogTopicID(self):
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogSource(self):
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Description = params.get("Description")
        self._TraceDuration = params.get("TraceDuration")
        self._OpenBilling = params.get("OpenBilling")
        self._SpanDailyCounters = params.get("SpanDailyCounters")
        self._ErrRateThreshold = params.get("ErrRateThreshold")
        self._SampleRate = params.get("SampleRate")
        self._ErrorSample = params.get("ErrorSample")
        self._SlowRequestSavedThreshold = params.get("SlowRequestSavedThreshold")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogRegion = params.get("LogRegion")
        self._LogTopicID = params.get("LogTopicID")
        self._LogSet = params.get("LogSet")
        self._LogSource = params.get("LogSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmInstanceResponse(AbstractModel):
    """ModifyApmInstance返回参数结构体

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


class OrderBy(AbstractModel):
    """sql排序字段

    """

    def __init__(self):
        r"""
        :param _Key: 需要排序的字段
        :type Key: str
        :param _Value: 顺序排序/倒序排序
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
        


class QueryMetricItem(AbstractModel):
    """查询

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Compare: 同比，已弃用，不建议使用
        :type Compare: str
        :param _Compares: 同比，支持多种同比方式
        :type Compares: list of str
        """
        self._MetricName = None
        self._Compare = None
        self._Compares = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Compare(self):
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Compares(self):
        return self._Compares

    @Compares.setter
    def Compares(self, Compares):
        self._Compares = Compares


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Compare = params.get("Compare")
        self._Compares = params.get("Compares")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateApmInstanceRequest(AbstractModel):
    """TerminateApmInstance请求参数结构体

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
        


class TerminateApmInstanceResponse(AbstractModel):
    """TerminateApmInstance返回参数结构体

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