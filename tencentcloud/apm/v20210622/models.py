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
        """Key值定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Value值定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
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
        """Key值定义
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Value值定义
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
        """Agent下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AgentDownloadURL

    @AgentDownloadURL.setter
    def AgentDownloadURL(self, AgentDownloadURL):
        self._AgentDownloadURL = AgentDownloadURL

    @property
    def CollectorURL(self):
        """Collector上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CollectorURL

    @CollectorURL.setter
    def CollectorURL(self, CollectorURL):
        self._CollectorURL = CollectorURL

    @property
    def Token(self):
        """Token信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def PublicCollectorURL(self):
        """外网上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicCollectorURL

    @PublicCollectorURL.setter
    def PublicCollectorURL(self, PublicCollectorURL):
        self._PublicCollectorURL = PublicCollectorURL

    @property
    def InnerCollectorURL(self):
        """自研VPC上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InnerCollectorURL

    @InnerCollectorURL.setter
    def InnerCollectorURL(self, InnerCollectorURL):
        self._InnerCollectorURL = InnerCollectorURL

    @property
    def PrivateLinkCollectorURL(self):
        """内网上报地址(Private Link上报地址)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class ApmApplicationConfigView(AbstractModel):
    """应用相关的配置列表项

    """

    def __init__(self):
        r"""
        :param _InstanceKey: 业务系统ID	
        :type InstanceKey: str
        :param _ServiceName: 应用名	
        :type ServiceName: str
        :param _OperationNameFilter: 接口过滤
        :type OperationNameFilter: str
        :param _ExceptionFilter: 错误类型过滤
        :type ExceptionFilter: str
        :param _ErrorCodeFilter: HTTP状态码过滤
        :type ErrorCodeFilter: str
        :param _EventEnable: 应用诊断开关（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type EventEnable: bool
        :param _UrlConvergenceSwitch: URL收敛开关 0 关 1 开
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: URL收敛阈值	
        :type UrlConvergenceThreshold: int
        :param _UrlConvergence: URL收敛规则正则	
        :type UrlConvergence: str
        :param _UrlExclude: URL排除规则正则
        :type UrlExclude: str
        :param _IsRelatedLog: 是否开启日志 0 关 1 开
        :type IsRelatedLog: int
        :param _LogSource: 日志源	
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSource: str
        :param _LogSet: 日志集 
        :type LogSet: str
        :param _LogTopicID: 日志主题
        :type LogTopicID: str
        :param _SnapshotEnable: 方法栈快照开关 true 开启 false 关闭
        :type SnapshotEnable: bool
        :param _SnapshotTimeout: 慢调用监听触发阈值
        :type SnapshotTimeout: int
        :param _AgentEnable: 探针总开关
        :type AgentEnable: bool
        :param _InstrumentList: 组件列表开关（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type InstrumentList: list of Instrument
        :param _TraceSquash: 链路压缩开关（已废弃）
        :type TraceSquash: bool
        """
        self._InstanceKey = None
        self._ServiceName = None
        self._OperationNameFilter = None
        self._ExceptionFilter = None
        self._ErrorCodeFilter = None
        self._EventEnable = None
        self._UrlConvergenceSwitch = None
        self._UrlConvergenceThreshold = None
        self._UrlConvergence = None
        self._UrlExclude = None
        self._IsRelatedLog = None
        self._LogSource = None
        self._LogSet = None
        self._LogTopicID = None
        self._SnapshotEnable = None
        self._SnapshotTimeout = None
        self._AgentEnable = None
        self._InstrumentList = None
        self._TraceSquash = None

    @property
    def InstanceKey(self):
        """业务系统ID	
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        """应用名	
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OperationNameFilter(self):
        """接口过滤
        :rtype: str
        """
        return self._OperationNameFilter

    @OperationNameFilter.setter
    def OperationNameFilter(self, OperationNameFilter):
        self._OperationNameFilter = OperationNameFilter

    @property
    def ExceptionFilter(self):
        """错误类型过滤
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def ErrorCodeFilter(self):
        """HTTP状态码过滤
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def EventEnable(self):
        """应用诊断开关（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def UrlConvergenceSwitch(self):
        """URL收敛开关 0 关 1 开
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        """URL收敛阈值	
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def UrlConvergence(self):
        """URL收敛规则正则	
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def UrlExclude(self):
        """URL排除规则正则
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def IsRelatedLog(self):
        """是否开启日志 0 关 1 开
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogSource(self):
        """日志源	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def LogSet(self):
        """日志集 
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogTopicID(self):
        """日志主题
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def SnapshotEnable(self):
        """方法栈快照开关 true 开启 false 关闭
        :rtype: bool
        """
        return self._SnapshotEnable

    @SnapshotEnable.setter
    def SnapshotEnable(self, SnapshotEnable):
        self._SnapshotEnable = SnapshotEnable

    @property
    def SnapshotTimeout(self):
        """慢调用监听触发阈值
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        """探针总开关
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def InstrumentList(self):
        """组件列表开关（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def TraceSquash(self):
        """链路压缩开关（已废弃）
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ServiceName = params.get("ServiceName")
        self._OperationNameFilter = params.get("OperationNameFilter")
        self._ExceptionFilter = params.get("ExceptionFilter")
        self._ErrorCodeFilter = params.get("ErrorCodeFilter")
        self._EventEnable = params.get("EventEnable")
        self._UrlConvergenceSwitch = params.get("UrlConvergenceSwitch")
        self._UrlConvergenceThreshold = params.get("UrlConvergenceThreshold")
        self._UrlConvergence = params.get("UrlConvergence")
        self._UrlExclude = params.get("UrlExclude")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogSource = params.get("LogSource")
        self._LogSet = params.get("LogSet")
        self._LogTopicID = params.get("LogTopicID")
        self._SnapshotEnable = params.get("SnapshotEnable")
        self._SnapshotTimeout = params.get("SnapshotTimeout")
        self._AgentEnable = params.get("AgentEnable")
        if params.get("InstrumentList") is not None:
            self._InstrumentList = []
            for item in params.get("InstrumentList"):
                obj = Instrument()
                obj._deserialize(item)
                self._InstrumentList.append(obj)
        self._TraceSquash = params.get("TraceSquash")
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
        """昨日同比指标值，已弃用，不建议使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompareVal

    @CompareVal.setter
    def CompareVal(self, CompareVal):
        self._CompareVal = CompareVal

    @property
    def CompareVals(self):
        """Compare值结果数组，推荐使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of APMKVItem
        """
        return self._CompareVals

    @CompareVals.setter
    def CompareVals(self, CompareVals):
        self._CompareVals = CompareVals

    @property
    def Value(self):
        """指标值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        """指标所对应的单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Key(self):
        """请求数
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def LastPeriodValue(self):
        """同环比上周期具体数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of APMKV
        """
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
        :param _CustomShowTags: 用户自定义展示标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomShowTags: list of str
        :param _PayMode: 实例计费模式
1为预付费
0为按量付费
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _PayModeEffective: 实例计费模式是否生效
注意：此字段可能返回 null，表示取不到有效值。
        :type PayModeEffective: bool
        :param _ResponseDurationWarningThreshold: 响应时间满意阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseDurationWarningThreshold: int
        :param _Free: 是否免费（0=否，1=限额免费，2=完全免费），默认0
注意：此字段可能返回 null，表示取不到有效值。
        :type Free: int
        :param _DefaultTSF: 是否tsf默认业务系统（0=否，1-是）
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultTSF: int
        :param _IsRelatedDashboard: 是否关联dashboard： 0 关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: dashboard ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DashboardTopicID: str
        :param _IsInstrumentationVulnerabilityScan: 是否开启组件漏洞检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsSqlInjectionAnalysis: 是否开启SQL注入分析
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSqlInjectionAnalysis: int
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
        self._CustomShowTags = None
        self._PayMode = None
        self._PayModeEffective = None
        self._ResponseDurationWarningThreshold = None
        self._Free = None
        self._DefaultTSF = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._IsInstrumentationVulnerabilityScan = None
        self._IsSqlInjectionAnalysis = None

    @property
    def AmountOfUsedStorage(self):
        """存储使用量(MB)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._AmountOfUsedStorage

    @AmountOfUsedStorage.setter
    def AmountOfUsedStorage(self, AmountOfUsedStorage):
        self._AmountOfUsedStorage = AmountOfUsedStorage

    @property
    def Name(self):
        """实例名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        """实例所属tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreateUin(self):
        """创建人Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def ServiceCount(self):
        """该实例已上报的服务端应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def CountOfReportSpanPerDay(self):
        """日均上报Span数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CountOfReportSpanPerDay

    @CountOfReportSpanPerDay.setter
    def CountOfReportSpanPerDay(self, CountOfReportSpanPerDay):
        self._CountOfReportSpanPerDay = CountOfReportSpanPerDay

    @property
    def AppId(self):
        """AppId信息
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def TraceDuration(self):
        """Trace数据保存时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def Description(self):
        """实例描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        """实例所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SpanDailyCounters(self):
        """实例上报额度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def BillingInstance(self):
        """实例是否开通计费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BillingInstance

    @BillingInstance.setter
    def BillingInstance(self, BillingInstance):
        self._BillingInstance = BillingInstance

    @property
    def ErrRateThreshold(self):
        """错误率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        """采样率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        """是否开启错误采样 0  关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        """慢调用保存阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def LogRegion(self):
        """cls日志所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogSource(self):
        """日志来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def IsRelatedLog(self):
        """日志功能开关 0 关 | 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogTopicID(self):
        """日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def ClientCount(self):
        """该实例已上报的客户端应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClientCount

    @ClientCount.setter
    def ClientCount(self, ClientCount):
        self._ClientCount = ClientCount

    @property
    def TotalCount(self):
        """该实例已上报的总应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogSet(self):
        """CLS日志集 | ES集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def MetricDuration(self):
        """Metric数据保存时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MetricDuration

    @MetricDuration.setter
    def MetricDuration(self, MetricDuration):
        self._MetricDuration = MetricDuration

    @property
    def CustomShowTags(self):
        """用户自定义展示标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CustomShowTags

    @CustomShowTags.setter
    def CustomShowTags(self, CustomShowTags):
        self._CustomShowTags = CustomShowTags

    @property
    def PayMode(self):
        """实例计费模式
1为预付费
0为按量付费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeEffective(self):
        """实例计费模式是否生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._PayModeEffective

    @PayModeEffective.setter
    def PayModeEffective(self, PayModeEffective):
        self._PayModeEffective = PayModeEffective

    @property
    def ResponseDurationWarningThreshold(self):
        """响应时间满意阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def Free(self):
        """是否免费（0=否，1=限额免费，2=完全免费），默认0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free

    @property
    def DefaultTSF(self):
        """是否tsf默认业务系统（0=否，1-是）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DefaultTSF

    @DefaultTSF.setter
    def DefaultTSF(self, DefaultTSF):
        self._DefaultTSF = DefaultTSF

    @property
    def IsRelatedDashboard(self):
        """是否关联dashboard： 0 关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        """dashboard ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def IsInstrumentationVulnerabilityScan(self):
        """是否开启组件漏洞检测
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsSqlInjectionAnalysis(self):
        """是否开启SQL注入分析
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis


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
        self._CustomShowTags = params.get("CustomShowTags")
        self._PayMode = params.get("PayMode")
        self._PayModeEffective = params.get("PayModeEffective")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
        self._Free = params.get("Free")
        self._DefaultTSF = params.get("DefaultTSF")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
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
        """field数组
        :rtype: list of ApmField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Tags(self):
        """tag数组
        :rtype: list of ApmTag
        """
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
        """维度Key(列名，标签Key)
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """维度值（标签值）
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
        


class CreateApmInstanceRequest(AbstractModel):
    """CreateApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 业务系统名
        :type Name: str
        :param _Description: 业务系统描述信息
        :type Description: str
        :param _TraceDuration: Trace数据保存时长，单位为天默认存储为3天
        :type TraceDuration: int
        :param _Tags: 标签列表
        :type Tags: list of ApmTag
        :param _SpanDailyCounters: 业务系统上报额度值，默认赋值为0表示不限制上报额度
        :type SpanDailyCounters: int
        :param _PayMode: 业务系统的计费模式
        :type PayMode: int
        :param _Free: （0=付费版；1=tsf受限免费版；2=免费版）
        :type Free: int
        """
        self._Name = None
        self._Description = None
        self._TraceDuration = None
        self._Tags = None
        self._SpanDailyCounters = None
        self._PayMode = None
        self._Free = None

    @property
    def Name(self):
        """业务系统名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """业务系统描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        """Trace数据保存时长，单位为天默认存储为3天
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def Tags(self):
        """标签列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SpanDailyCounters(self):
        """业务系统上报额度值，默认赋值为0表示不限制上报额度
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def PayMode(self):
        """业务系统的计费模式
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Free(self):
        """（0=付费版；1=tsf受限免费版；2=免费版）
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free


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
        self._PayMode = params.get("PayMode")
        self._Free = params.get("Free")
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
        :param _InstanceId: 业务系统ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """业务系统ID
注意：此字段可能返回 null，表示取不到有效值。
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


class DescribeApmAgentRequest(AbstractModel):
    """DescribeApmAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
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
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentType(self):
        """接入方式
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def NetworkMode(self):
        """环境
        :rtype: str
        """
        return self._NetworkMode

    @NetworkMode.setter
    def NetworkMode(self, NetworkMode):
        self._NetworkMode = NetworkMode

    @property
    def LanguageEnvironment(self):
        """语言
        :rtype: str
        """
        return self._LanguageEnvironment

    @LanguageEnvironment.setter
    def LanguageEnvironment(self, LanguageEnvironment):
        self._LanguageEnvironment = LanguageEnvironment

    @property
    def ReportMethod(self):
        """上报方式
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmAgent = None
        self._RequestId = None

    @property
    def ApmAgent(self):
        """Agent信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        """
        return self._ApmAgent

    @ApmAgent.setter
    def ApmAgent(self, ApmAgent):
        self._ApmAgent = ApmAgent

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
        """Tag列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceName(self):
        """搜索实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceIds(self):
        """过滤实例ID
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DemoInstanceFlag(self):
        """是否查询官方demo实例
        :rtype: int
        """
        return self._DemoInstanceFlag

    @DemoInstanceFlag.setter
    def DemoInstanceFlag(self, DemoInstanceFlag):
        self._DemoInstanceFlag = DemoInstanceFlag

    @property
    def AllRegionsFlag(self):
        """是否查询全地域实例
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._RequestId = None

    @property
    def Instances(self):
        """apm实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmInstanceDetail
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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = ApmInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGeneralApmApplicationConfigRequest(AbstractModel):
    """DescribeGeneralApmApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceName: 应用名
        :type ServiceName: str
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        """
        self._ServiceName = None
        self._InstanceId = None

    @property
    def ServiceName(self):
        """应用名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralApmApplicationConfigResponse(AbstractModel):
    """DescribeGeneralApmApplicationConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmApplicationConfigView: 应用配置项
        :type ApmApplicationConfigView: :class:`tencentcloud.apm.v20210622.models.ApmApplicationConfigView`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmApplicationConfigView = None
        self._RequestId = None

    @property
    def ApmApplicationConfigView(self):
        """应用配置项
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmApplicationConfigView`
        """
        return self._ApmApplicationConfigView

    @ApmApplicationConfigView.setter
    def ApmApplicationConfigView(self, ApmApplicationConfigView):
        self._ApmApplicationConfigView = ApmApplicationConfigView

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
        if params.get("ApmApplicationConfigView") is not None:
            self._ApmApplicationConfigView = ApmApplicationConfigView()
            self._ApmApplicationConfigView._deserialize(params.get("ApmApplicationConfigView"))
        self._RequestId = params.get("RequestId")


class DescribeGeneralMetricDataRequest(AbstractModel):
    """DescribeGeneralMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Metrics: 需要查询的指标名称，不可自定义输入，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type Metrics: list of str
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _ViewName: 视图名称，不可自定义输入。[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type ViewName: str
        :param _Filters: 要过滤的维度信息，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type Filters: list of GeneralFilter
        :param _GroupBy: 聚合维度，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type GroupBy: list of str
        :param _StartTime: 起始时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :type StartTime: int
        :param _EndTime: 结束时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :type EndTime: int
        :param _Period: 聚合粒度，单位为秒，最小为60s，即一分钟的聚合粒度；如果为空或0则计算开始时间到截止时间的指标数据，上报其他值会报错。
        :type Period: int
        :param _OrderBy: 对查询指标进行排序：
Key 填写云 API 指标名称，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
Value 填写排序方式：     
- asc:对查询指标进行升序排序
- desc：对查询指标进行降序排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _PageSize: 查询指标的限制条数，目前最多展示50条数据，PageSize取值为1-50，上送PageSize则根据PageSize的值展示限制条数。
        :type PageSize: int
        """
        self._Metrics = None
        self._InstanceId = None
        self._ViewName = None
        self._Filters = None
        self._GroupBy = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._OrderBy = None
        self._PageSize = None

    @property
    def Metrics(self):
        """需要查询的指标名称，不可自定义输入，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: list of str
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def InstanceId(self):
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ViewName(self):
        """视图名称，不可自定义输入。[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Filters(self):
        """要过滤的维度信息，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: list of GeneralFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def GroupBy(self):
        """聚合维度，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def StartTime(self):
        """起始时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """聚合粒度，单位为秒，最小为60s，即一分钟的聚合粒度；如果为空或0则计算开始时间到截止时间的指标数据，上报其他值会报错。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def OrderBy(self):
        """对查询指标进行排序：
Key 填写云 API 指标名称，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
Value 填写排序方式：     
- asc:对查询指标进行升序排序
- desc：对查询指标进行降序排序
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def PageSize(self):
        """查询指标的限制条数，目前最多展示50条数据，PageSize取值为1-50，上送PageSize则根据PageSize的值展示限制条数。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Metrics = params.get("Metrics")
        self._InstanceId = params.get("InstanceId")
        self._ViewName = params.get("ViewName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = GeneralFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._RequestId = None

    @property
    def Records(self):
        """指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Line
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = Line()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGeneralSpanListRequest(AbstractModel):
    """DescribeGeneralSpanList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页
        :type Offset: int
        :param _Limit: 列表项个数
        :type Limit: int
        :param _OrderBy: 排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _StartTime: span查询开始时间戳（单位:秒）
        :type StartTime: int
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _Filters: 通用过滤参数
        :type Filters: list of Filter
        :param _BusinessName: 业务自身服务名
        :type BusinessName: str
        :param _EndTime: span查询结束时间戳（单位:秒）
        :type EndTime: int
        """
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._StartTime = None
        self._InstanceId = None
        self._Filters = None
        self._BusinessName = None
        self._EndTime = None

    @property
    def Offset(self):
        """分页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """列表项个数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderBy(self):
        """排序
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        """span查询开始时间戳（单位:秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def InstanceId(self):
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        """通用过滤参数
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def BusinessName(self):
        """业务自身服务名
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def EndTime(self):
        """span查询结束时间戳（单位:秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._StartTime = params.get("StartTime")
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._BusinessName = params.get("BusinessName")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralSpanListResponse(AbstractModel):
    """DescribeGeneralSpanList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Spans: Span分页列表
        :type Spans: list of Span
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Spans = None
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
    def Spans(self):
        """Span分页列表
        :rtype: list of Span
        """
        return self._Spans

    @Spans.setter
    def Spans(self, Spans):
        self._Spans = Spans

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
        if params.get("Spans") is not None:
            self._Spans = []
            for item in params.get("Spans"):
                obj = Span()
                obj._deserialize(item)
                self._Spans.append(obj)
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
        :param _InstanceId: 业务系统ID
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
        :param _Type: 数据来源
        :type Type: str
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
        self._Type = None

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Metrics(self):
        """指标列表
        :rtype: list of QueryMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def GroupBy(self):
        """聚合维度
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        """排序
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def InstanceId(self):
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """每页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Offset(self):
        """分页起始点
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndTime(self):
        """结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BusinessName(self):
        """业务名称（默认值：taw）
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def PageIndex(self):
        """页码
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        """页长
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def OrFilters(self):
        """Or过滤条件
        :rtype: list of Filter
        """
        return self._OrFilters

    @OrFilters.setter
    def OrFilters(self, OrFilters):
        self._OrFilters = OrFilters

    @property
    def Type(self):
        """数据来源
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


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
        self._Type = params.get("Type")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Records(self):
        """指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmMetricRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def TotalCount(self):
        """查询指标结果集条数
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _InstanceId: 业务系统ID
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
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Metrics(self):
        """指标列表
        :rtype: list of QueryMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def GroupBy(self):
        """聚合维度
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        """排序
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def InstanceId(self):
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        """每页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Offset(self):
        """分页起始点
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndTime(self):
        """结束时间
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._RequestId = None

    @property
    def Records(self):
        """指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmMetricRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    """DescribeTagValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 维度名
        :type TagKey: str
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _OrFilters: Or过滤条件
        :type OrFilters: list of Filter
        :param _Type: 使用类型
        :type Type: str
        """
        self._TagKey = None
        self._InstanceId = None
        self._EndTime = None
        self._Filters = None
        self._StartTime = None
        self._OrFilters = None
        self._Type = None

    @property
    def TagKey(self):
        """维度名
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def InstanceId(self):
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EndTime(self):
        """结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def OrFilters(self):
        """Or过滤条件
        :rtype: list of Filter
        """
        return self._OrFilters

    @OrFilters.setter
    def OrFilters(self, OrFilters):
        self._OrFilters = OrFilters

    @property
    def Type(self):
        """使用类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._InstanceId = params.get("InstanceId")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        if params.get("OrFilters") is not None:
            self._OrFilters = []
            for item in params.get("OrFilters"):
                obj = Filter()
                obj._deserialize(item)
                self._OrFilters.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesResponse(AbstractModel):
    """DescribeTagValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Values: 维度值列表
        :type Values: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Values = None
        self._RequestId = None

    @property
    def Values(self):
        """维度值列表
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

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
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询过滤参数

    """

    def __init__(self):
        r"""
        :param _Type: 过滤方式（=, !=, in）
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Key: 过滤维度名
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 过滤值，in过滤方式用逗号分割多个值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Type = None
        self._Key = None
        self._Value = None

    @property
    def Type(self):
        """过滤方式（=, !=, in）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        """过滤维度名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """过滤值，in过滤方式用逗号分割多个值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """过滤维度名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """过滤值
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
        


class Instrument(AbstractModel):
    """组件

    """

    def __init__(self):
        r"""
        :param _Name: 组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Enable: 组件开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        """
        self._Name = None
        self._Enable = None

    @property
    def Name(self):
        """组件名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enable(self):
        """组件开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Enable = params.get("Enable")
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
        """指标名
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricNameCN(self):
        """指标中文名
        :rtype: str
        """
        return self._MetricNameCN

    @MetricNameCN.setter
    def MetricNameCN(self, MetricNameCN):
        self._MetricNameCN = MetricNameCN

    @property
    def TimeSerial(self):
        """时间序列
        :rtype: list of int
        """
        return self._TimeSerial

    @TimeSerial.setter
    def TimeSerial(self, TimeSerial):
        self._TimeSerial = TimeSerial

    @property
    def DataSerial(self):
        """数据序列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of float
        """
        return self._DataSerial

    @DataSerial.setter
    def DataSerial(self, DataSerial):
        self._DataSerial = DataSerial

    @property
    def Tags(self):
        """维度列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmTag
        """
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
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _Name: 业务系统名
        :type Name: str
        :param _Tags: 标签列表
        :type Tags: list of ApmTag
        :param _Description: 业务系统详情
        :type Description: str
        :param _TraceDuration: Trace数据保存时长
        :type TraceDuration: int
        :param _OpenBilling: 是否开启计费
        :type OpenBilling: bool
        :param _SpanDailyCounters: 业务系统上报额度
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
        :param _CustomShowTags: 用户自定义展示标签列表
        :type CustomShowTags: list of str
        :param _PayMode: 修改计费模式
1为预付费
0为按量付费
        :type PayMode: int
        :param _ResponseDurationWarningThreshold: 响应时间满意阈值
        :type ResponseDurationWarningThreshold: int
        :param _Free: （0=付费版；1=tsf受限免费版；2=免费版）
        :type Free: int
        :param _IsRelatedDashboard: 是否关联dashboard： 0 关 1 开
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: dashboard ID
        :type DashboardTopicID: str
        :param _IsSqlInjectionAnalysis: 是否开启SQL注入检测
        :type IsSqlInjectionAnalysis: int
        :param _IsInstrumentationVulnerabilityScan: 是否开启组件漏洞检测
        :type IsInstrumentationVulnerabilityScan: int
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
        self._CustomShowTags = None
        self._PayMode = None
        self._ResponseDurationWarningThreshold = None
        self._Free = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._IsSqlInjectionAnalysis = None
        self._IsInstrumentationVulnerabilityScan = None

    @property
    def InstanceId(self):
        """业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """业务系统名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        """标签列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        """业务系统详情
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        """Trace数据保存时长
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def OpenBilling(self):
        """是否开启计费
        :rtype: bool
        """
        return self._OpenBilling

    @OpenBilling.setter
    def OpenBilling(self, OpenBilling):
        self._OpenBilling = OpenBilling

    @property
    def SpanDailyCounters(self):
        """业务系统上报额度
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def ErrRateThreshold(self):
        """错误率阈值
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        """采样率
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        """是否开启错误采样 0 关 1 开
        :rtype: int
        """
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        """慢请求阈值
        :rtype: int
        """
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def IsRelatedLog(self):
        """是否开启日志功能 0 关 1 开
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogRegion(self):
        """日志地域
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogTopicID(self):
        """CLS日志主题ID | ES 索引名
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def LogSet(self):
        """CLS日志集 | ES集群ID
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogSource(self):
        """CLS | ES
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def CustomShowTags(self):
        """用户自定义展示标签列表
        :rtype: list of str
        """
        return self._CustomShowTags

    @CustomShowTags.setter
    def CustomShowTags(self, CustomShowTags):
        self._CustomShowTags = CustomShowTags

    @property
    def PayMode(self):
        """修改计费模式
1为预付费
0为按量付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResponseDurationWarningThreshold(self):
        """响应时间满意阈值
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def Free(self):
        """（0=付费版；1=tsf受限免费版；2=免费版）
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free

    @property
    def IsRelatedDashboard(self):
        """是否关联dashboard： 0 关 1 开
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        """dashboard ID
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def IsSqlInjectionAnalysis(self):
        """是否开启SQL注入检测
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsInstrumentationVulnerabilityScan(self):
        """是否开启组件漏洞检测
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan


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
        self._CustomShowTags = params.get("CustomShowTags")
        self._PayMode = params.get("PayMode")
        self._ResponseDurationWarningThreshold = params.get("ResponseDurationWarningThreshold")
        self._Free = params.get("Free")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
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


class ModifyGeneralApmApplicationConfigRequest(AbstractModel):
    """ModifyGeneralApmApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统Id
        :type InstanceId: str
        :param _Tags: 需要修改的字段key value分别指定字段名、字段值
[具体字段请见](https://cloud.tencent.com/document/product/248/111241)
        :type Tags: list of ApmTag
        :param _ServiceNames: 需要修改配置的应用列表名称	
        :type ServiceNames: list of str
        """
        self._InstanceId = None
        self._Tags = None
        self._ServiceNames = None

    @property
    def InstanceId(self):
        """业务系统Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Tags(self):
        """需要修改的字段key value分别指定字段名、字段值
[具体字段请见](https://cloud.tencent.com/document/product/248/111241)
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceNames(self):
        """需要修改配置的应用列表名称	
        :rtype: list of str
        """
        return self._ServiceNames

    @ServiceNames.setter
    def ServiceNames(self, ServiceNames):
        self._ServiceNames = ServiceNames


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ServiceNames = params.get("ServiceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGeneralApmApplicationConfigResponse(AbstractModel):
    """ModifyGeneralApmApplicationConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Message: 返回值描述
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Message = None
        self._RequestId = None

    @property
    def Message(self):
        """返回值描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Message = params.get("Message")
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
        """需要排序的字段
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """顺序排序/倒序排序
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
        """指标名
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Compare(self):
        """同比，已弃用，不建议使用
        :rtype: str
        """
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Compares(self):
        """同比，支持多种同比方式
        :rtype: list of str
        """
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
        


class Span(AbstractModel):
    """Span对象

    """

    def __init__(self):
        r"""
        :param _TraceID: Trace Id
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceID: str
        :param _Logs: 日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Logs: list of SpanLog
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of SpanTag
        :param _Process: 上报应用服务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: :class:`tencentcloud.apm.v20210622.models.SpanProcess`
        :param _Timestamp: 产生时间戳(毫秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param _OperationName: Span名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationName: str
        :param _References: 关联关系
注意：此字段可能返回 null，表示取不到有效值。
        :type References: list of SpanReference
        :param _StartTime: 产生时间戳(微秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _Duration: 持续耗时(微妙)
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _SpanID: Span Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SpanID: str
        :param _StartTimeMillis: 产生时间戳(毫秒)
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeMillis: int
        :param _ParentSpanID: Parent Span Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentSpanID: str
        """
        self._TraceID = None
        self._Logs = None
        self._Tags = None
        self._Process = None
        self._Timestamp = None
        self._OperationName = None
        self._References = None
        self._StartTime = None
        self._Duration = None
        self._SpanID = None
        self._StartTimeMillis = None
        self._ParentSpanID = None

    @property
    def TraceID(self):
        """Trace Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TraceID

    @TraceID.setter
    def TraceID(self, TraceID):
        self._TraceID = TraceID

    @property
    def Logs(self):
        """日志
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SpanLog
        """
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SpanTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Process(self):
        """上报应用服务信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apm.v20210622.models.SpanProcess`
        """
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def Timestamp(self):
        """产生时间戳(毫秒)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def OperationName(self):
        """Span名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def References(self):
        """关联关系
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SpanReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def StartTime(self):
        """产生时间戳(微秒)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        """持续耗时(微妙)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def SpanID(self):
        """Span Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SpanID

    @SpanID.setter
    def SpanID(self, SpanID):
        self._SpanID = SpanID

    @property
    def StartTimeMillis(self):
        """产生时间戳(毫秒)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartTimeMillis

    @StartTimeMillis.setter
    def StartTimeMillis(self, StartTimeMillis):
        self._StartTimeMillis = StartTimeMillis

    @property
    def ParentSpanID(self):
        """Parent Span Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentSpanID

    @ParentSpanID.setter
    def ParentSpanID(self, ParentSpanID):
        self._ParentSpanID = ParentSpanID


    def _deserialize(self, params):
        self._TraceID = params.get("TraceID")
        if params.get("Logs") is not None:
            self._Logs = []
            for item in params.get("Logs"):
                obj = SpanLog()
                obj._deserialize(item)
                self._Logs.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = SpanTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Process") is not None:
            self._Process = SpanProcess()
            self._Process._deserialize(params.get("Process"))
        self._Timestamp = params.get("Timestamp")
        self._OperationName = params.get("OperationName")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = SpanReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._SpanID = params.get("SpanID")
        self._StartTimeMillis = params.get("StartTimeMillis")
        self._ParentSpanID = params.get("ParentSpanID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanLog(AbstractModel):
    """Span日志部分


    """

    def __init__(self):
        r"""
        :param _Timestamp: 日志时间戳
        :type Timestamp: int
        :param _Fields: 标签
        :type Fields: list of SpanTag
        """
        self._Timestamp = None
        self._Fields = None

    @property
    def Timestamp(self):
        """日志时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Fields(self):
        """标签
        :rtype: list of SpanTag
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = SpanTag()
                obj._deserialize(item)
                self._Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanProcess(AbstractModel):
    """服务相关信息

    """

    def __init__(self):
        r"""
        :param _ServiceName: 应用服务名称
        :type ServiceName: str
        :param _Tags: Tags 标签数组
        :type Tags: list of SpanTag
        """
        self._ServiceName = None
        self._Tags = None

    @property
    def ServiceName(self):
        """应用服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Tags(self):
        """Tags 标签数组
        :rtype: list of SpanTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = SpanTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanReference(AbstractModel):
    """Span上下游关联关系

    """

    def __init__(self):
        r"""
        :param _RefType: 关联关系类型
        :type RefType: str
        :param _SpanID: Span ID
        :type SpanID: str
        :param _TraceID: Trace ID
        :type TraceID: str
        """
        self._RefType = None
        self._SpanID = None
        self._TraceID = None

    @property
    def RefType(self):
        """关联关系类型
        :rtype: str
        """
        return self._RefType

    @RefType.setter
    def RefType(self, RefType):
        self._RefType = RefType

    @property
    def SpanID(self):
        """Span ID
        :rtype: str
        """
        return self._SpanID

    @SpanID.setter
    def SpanID(self, SpanID):
        self._SpanID = SpanID

    @property
    def TraceID(self):
        """Trace ID
        :rtype: str
        """
        return self._TraceID

    @TraceID.setter
    def TraceID(self, TraceID):
        self._TraceID = TraceID


    def _deserialize(self, params):
        self._RefType = params.get("RefType")
        self._SpanID = params.get("SpanID")
        self._TraceID = params.get("TraceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpanTag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _Type: 标签类型
        :type Type: str
        :param _Key: 标签Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Type = None
        self._Key = None
        self._Value = None

    @property
    def Type(self):
        """标签类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        """标签Key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class TerminateApmInstanceRequest(AbstractModel):
    """TerminateApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """业务系统ID
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
        


class TerminateApmInstanceResponse(AbstractModel):
    """TerminateApmInstance返回参数结构体

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