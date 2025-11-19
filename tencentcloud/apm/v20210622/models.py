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


class APMKV(AbstractModel):
    r"""APM 浮点数类型键值对

    """

    def __init__(self):
        r"""
        :param _Key: Key 值定义
        :type Key: str
        :param _Value: Value 值定义
        :type Value: float
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key 值定义
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value 值定义
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
    r"""APM 通用 KV 结构

    """

    def __init__(self):
        r"""
        :param _Key: Key 值定义
        :type Key: str
        :param _Value: Value 值定义
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Key 值定义
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Value 值定义
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
        


class AgentOperationConfigView(AbstractModel):
    r"""探针有关接口的相关配置

    """

    def __init__(self):
        r"""
        :param _RetentionValid: 当前接口配置是否开启了接口白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionValid: bool
        :param _IgnoreOperation: RetentionValid为false时生效，接口配置中的黑名单配置，配置中的接口不采集
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreOperation: str
        :param _RetentionOperation: RetentionValid为true时生效，接口配置中的白名单配置，仅采集配置中的接口
注意：此字段可能返回 null，表示取不到有效值。
        :type RetentionOperation: str
        """
        self._RetentionValid = None
        self._IgnoreOperation = None
        self._RetentionOperation = None

    @property
    def RetentionValid(self):
        r"""当前接口配置是否开启了接口白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._RetentionValid

    @RetentionValid.setter
    def RetentionValid(self, RetentionValid):
        self._RetentionValid = RetentionValid

    @property
    def IgnoreOperation(self):
        r"""RetentionValid为false时生效，接口配置中的黑名单配置，配置中的接口不采集
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreOperation

    @IgnoreOperation.setter
    def IgnoreOperation(self, IgnoreOperation):
        self._IgnoreOperation = IgnoreOperation

    @property
    def RetentionOperation(self):
        r"""RetentionValid为true时生效，接口配置中的白名单配置，仅采集配置中的接口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RetentionOperation

    @RetentionOperation.setter
    def RetentionOperation(self, RetentionOperation):
        self._RetentionOperation = RetentionOperation


    def _deserialize(self, params):
        self._RetentionValid = params.get("RetentionValid")
        self._IgnoreOperation = params.get("IgnoreOperation")
        self._RetentionOperation = params.get("RetentionOperation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmAgentInfo(AbstractModel):
    r"""APM Agent 信息

    """

    def __init__(self):
        r"""
        :param _AgentDownloadURL: Agent 下载地址
        :type AgentDownloadURL: str
        :param _CollectorURL: Collector 上报地址
        :type CollectorURL: str
        :param _Token: Token 信息
        :type Token: str
        :param _PublicCollectorURL: 外网上报地址
        :type PublicCollectorURL: str
        :param _InnerCollectorURL: 自研 VPC 上报地址
        :type InnerCollectorURL: str
        :param _PrivateLinkCollectorURL: 内网上报地址( Private Link 上报地址)
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
        r"""Agent 下载地址
        :rtype: str
        """
        return self._AgentDownloadURL

    @AgentDownloadURL.setter
    def AgentDownloadURL(self, AgentDownloadURL):
        self._AgentDownloadURL = AgentDownloadURL

    @property
    def CollectorURL(self):
        r"""Collector 上报地址
        :rtype: str
        """
        return self._CollectorURL

    @CollectorURL.setter
    def CollectorURL(self, CollectorURL):
        self._CollectorURL = CollectorURL

    @property
    def Token(self):
        r"""Token 信息
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def PublicCollectorURL(self):
        r"""外网上报地址
        :rtype: str
        """
        return self._PublicCollectorURL

    @PublicCollectorURL.setter
    def PublicCollectorURL(self, PublicCollectorURL):
        self._PublicCollectorURL = PublicCollectorURL

    @property
    def InnerCollectorURL(self):
        r"""自研 VPC 上报地址
        :rtype: str
        """
        return self._InnerCollectorURL

    @InnerCollectorURL.setter
    def InnerCollectorURL(self, InnerCollectorURL):
        self._InnerCollectorURL = InnerCollectorURL

    @property
    def PrivateLinkCollectorURL(self):
        r"""内网上报地址( Private Link 上报地址)
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
        


class ApmAppConfig(AbstractModel):
    r"""查询应用配置返回参数

    """

    def __init__(self):
        r"""
        :param _InstanceKey: 实例ID
        :type InstanceKey: str
        :param _ServiceName: 服务名
        :type ServiceName: str
        :param _UrlConvergenceSwitch: URL收敛开关
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: URL收敛阈值
        :type UrlConvergenceThreshold: int
        :param _UrlConvergence: URL收敛正则
        :type UrlConvergence: str
        :param _ExceptionFilter: 异常过滤正则
        :type ExceptionFilter: str
        :param _ErrorCodeFilter: 错误码过滤
        :type ErrorCodeFilter: str
        :param _Components: 服务组件类型
        :type Components: str
        :param _UrlExclude: URL排除正则
        :type UrlExclude: str
        :param _LogSource: 日志来源
        :type LogSource: str
        :param _LogRegion: 日志所在地域
        :type LogRegion: str
        :param _IsRelatedLog: 是否开启日志 0 关 1 开
        :type IsRelatedLog: int
        :param _LogTopicID: 日志主题ID
        :type LogTopicID: str
        :param _IgnoreOperationName: 需过滤的接口名
        :type IgnoreOperationName: str
        :param _LogSet: CLS日志集 | ES集群ID
        :type LogSet: str
        :param _TraceRateLimit: 探针每秒上报trace数
        :type TraceRateLimit: int
        :param _EnableSnapshot: 是否开启线程剖析
        :type EnableSnapshot: bool
        :param _SnapshotTimeout: 线程剖析超时阈值
        :type SnapshotTimeout: int
        :param _AgentEnable: 是否开启agent
        :type AgentEnable: bool
        :param _InstrumentList: 组件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstrumentList: list of Instrument
        :param _TraceSquash: 是否开启链路压缩
        :type TraceSquash: bool
        :param _EventEnable: 是否开启应用诊断开关
        :type EventEnable: bool
        :param _AgentOperationConfigView: 探针接口相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentOperationConfigView: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        :param _EnableLogConfig: 是否开启应用日志配置
        :type EnableLogConfig: bool
        :param _ServiceID: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceID: str
        :param _EnableDashboardConfig: 应用是否开启dashboard配置： false 关（与业务系统保持一致）/true 开（应用级配置）
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDashboardConfig: bool
        :param _IsRelatedDashboard: 是否关联dashboard： 0 关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: dashboard ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DashboardTopicID: str
        :param _EnableSecurityConfig: 是否开启应用级别配置
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableSecurityConfig: bool
        :param _IsInstrumentationVulnerabilityScan: 是否开启组件漏洞检测
注意：此字段可能返回 null，表示取不到有效值。
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsSqlInjectionAnalysis: 是否开启SQL注入分析
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSqlInjectionAnalysis: int
        :param _IsRemoteCommandExecutionAnalysis: 是否开启远程命令执行分析
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: 是否开启内存马检测分析
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMemoryHijackingAnalysis: int
        :param _LogIndexType: CLS索引类型(0=全文索引，1=键值索引)
        :type LogIndexType: int
        :param _LogTraceIdKey: traceId的索引key: 当CLS索引类型为键值索引时生效
        :type LogTraceIdKey: str
        :param _IsDeleteAnyFileAnalysis: 是否开启删除任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: 是否开启读取任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: 是否开启上传任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: 是否开启包含任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: 是否开启目录遍历检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: 是否开启模板引擎注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: 是否开启脚本引擎注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: 是否开启表达式注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: 是否开启JNDI注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: 是否开启JNI注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: 是否开启Webshell后门检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: 是否开启反序列化检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeserializationAnalysis: int
        :param _UrlAutoConvergenceEnable: 接口名称自动收敛开关（0-关闭，1-开启）
        :type UrlAutoConvergenceEnable: bool
        :param _UrlLongSegmentThreshold: URL长分段收敛阈值
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: URL数字分段收敛阈值
        :type UrlNumberSegmentThreshold: int
        :param _DisableMemoryUsed: 探针熔断内存阈值
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: 探针熔断CPU阈值
        :type DisableCpuUsed: int
        """
        self._InstanceKey = None
        self._ServiceName = None
        self._UrlConvergenceSwitch = None
        self._UrlConvergenceThreshold = None
        self._UrlConvergence = None
        self._ExceptionFilter = None
        self._ErrorCodeFilter = None
        self._Components = None
        self._UrlExclude = None
        self._LogSource = None
        self._LogRegion = None
        self._IsRelatedLog = None
        self._LogTopicID = None
        self._IgnoreOperationName = None
        self._LogSet = None
        self._TraceRateLimit = None
        self._EnableSnapshot = None
        self._SnapshotTimeout = None
        self._AgentEnable = None
        self._InstrumentList = None
        self._TraceSquash = None
        self._EventEnable = None
        self._AgentOperationConfigView = None
        self._EnableLogConfig = None
        self._ServiceID = None
        self._EnableDashboardConfig = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._EnableSecurityConfig = None
        self._IsInstrumentationVulnerabilityScan = None
        self._IsSqlInjectionAnalysis = None
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._UrlAutoConvergenceEnable = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None
        self._DisableMemoryUsed = None
        self._DisableCpuUsed = None

    @property
    def InstanceKey(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UrlConvergenceSwitch(self):
        r"""URL收敛开关
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""URL收敛阈值
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def UrlConvergence(self):
        r"""URL收敛正则
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def ExceptionFilter(self):
        r"""异常过滤正则
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def ErrorCodeFilter(self):
        r"""错误码过滤
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def Components(self):
        r"""服务组件类型
        :rtype: str
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def UrlExclude(self):
        r"""URL排除正则
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def LogSource(self):
        r"""日志来源
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def LogRegion(self):
        r"""日志所在地域
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def IsRelatedLog(self):
        r"""是否开启日志 0 关 1 开
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogTopicID(self):
        r"""日志主题ID
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def IgnoreOperationName(self):
        r"""需过滤的接口名
        :rtype: str
        """
        return self._IgnoreOperationName

    @IgnoreOperationName.setter
    def IgnoreOperationName(self, IgnoreOperationName):
        self._IgnoreOperationName = IgnoreOperationName

    @property
    def LogSet(self):
        r"""CLS日志集 | ES集群ID
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def TraceRateLimit(self):
        r"""探针每秒上报trace数
        :rtype: int
        """
        return self._TraceRateLimit

    @TraceRateLimit.setter
    def TraceRateLimit(self, TraceRateLimit):
        self._TraceRateLimit = TraceRateLimit

    @property
    def EnableSnapshot(self):
        r"""是否开启线程剖析
        :rtype: bool
        """
        return self._EnableSnapshot

    @EnableSnapshot.setter
    def EnableSnapshot(self, EnableSnapshot):
        self._EnableSnapshot = EnableSnapshot

    @property
    def SnapshotTimeout(self):
        r"""线程剖析超时阈值
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""是否开启agent
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def InstrumentList(self):
        r"""组件列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def TraceSquash(self):
        r"""是否开启链路压缩
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def EventEnable(self):
        r"""是否开启应用诊断开关
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def AgentOperationConfigView(self):
        r"""探针接口相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        """
        return self._AgentOperationConfigView

    @AgentOperationConfigView.setter
    def AgentOperationConfigView(self, AgentOperationConfigView):
        self._AgentOperationConfigView = AgentOperationConfigView

    @property
    def EnableLogConfig(self):
        r"""是否开启应用日志配置
        :rtype: bool
        """
        return self._EnableLogConfig

    @EnableLogConfig.setter
    def EnableLogConfig(self, EnableLogConfig):
        self._EnableLogConfig = EnableLogConfig

    @property
    def ServiceID(self):
        r"""应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def EnableDashboardConfig(self):
        r"""应用是否开启dashboard配置： false 关（与业务系统保持一致）/true 开（应用级配置）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableDashboardConfig

    @EnableDashboardConfig.setter
    def EnableDashboardConfig(self, EnableDashboardConfig):
        self._EnableDashboardConfig = EnableDashboardConfig

    @property
    def IsRelatedDashboard(self):
        r"""是否关联dashboard： 0 关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""dashboard ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def EnableSecurityConfig(self):
        r"""是否开启应用级别配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableSecurityConfig

    @EnableSecurityConfig.setter
    def EnableSecurityConfig(self, EnableSecurityConfig):
        self._EnableSecurityConfig = EnableSecurityConfig

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""是否开启组件漏洞检测
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsSqlInjectionAnalysis(self):
        r"""是否开启SQL注入分析
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""是否开启远程命令执行分析
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""是否开启内存马检测分析
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def LogIndexType(self):
        r"""CLS索引类型(0=全文索引，1=键值索引)
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""traceId的索引key: 当CLS索引类型为键值索引时生效
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""是否开启删除任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""是否开启读取任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""是否开启上传任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""是否开启包含任意文件检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""是否开启目录遍历检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""是否开启模板引擎注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""是否开启脚本引擎注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""是否开启表达式注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""是否开启JNDI注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""是否开启JNI注入检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""是否开启Webshell后门检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""是否开启反序列化检测（0-关闭，1-开启）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlAutoConvergenceEnable(self):
        r"""接口名称自动收敛开关（0-关闭，1-开启）
        :rtype: bool
        """
        return self._UrlAutoConvergenceEnable

    @UrlAutoConvergenceEnable.setter
    def UrlAutoConvergenceEnable(self, UrlAutoConvergenceEnable):
        self._UrlAutoConvergenceEnable = UrlAutoConvergenceEnable

    @property
    def UrlLongSegmentThreshold(self):
        r"""URL长分段收敛阈值
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""URL数字分段收敛阈值
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold

    @property
    def DisableMemoryUsed(self):
        r"""探针熔断内存阈值
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""探针熔断CPU阈值
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ServiceName = params.get("ServiceName")
        self._UrlConvergenceSwitch = params.get("UrlConvergenceSwitch")
        self._UrlConvergenceThreshold = params.get("UrlConvergenceThreshold")
        self._UrlConvergence = params.get("UrlConvergence")
        self._ExceptionFilter = params.get("ExceptionFilter")
        self._ErrorCodeFilter = params.get("ErrorCodeFilter")
        self._Components = params.get("Components")
        self._UrlExclude = params.get("UrlExclude")
        self._LogSource = params.get("LogSource")
        self._LogRegion = params.get("LogRegion")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogTopicID = params.get("LogTopicID")
        self._IgnoreOperationName = params.get("IgnoreOperationName")
        self._LogSet = params.get("LogSet")
        self._TraceRateLimit = params.get("TraceRateLimit")
        self._EnableSnapshot = params.get("EnableSnapshot")
        self._SnapshotTimeout = params.get("SnapshotTimeout")
        self._AgentEnable = params.get("AgentEnable")
        if params.get("InstrumentList") is not None:
            self._InstrumentList = []
            for item in params.get("InstrumentList"):
                obj = Instrument()
                obj._deserialize(item)
                self._InstrumentList.append(obj)
        self._TraceSquash = params.get("TraceSquash")
        self._EventEnable = params.get("EventEnable")
        if params.get("AgentOperationConfigView") is not None:
            self._AgentOperationConfigView = AgentOperationConfigView()
            self._AgentOperationConfigView._deserialize(params.get("AgentOperationConfigView"))
        self._EnableLogConfig = params.get("EnableLogConfig")
        self._ServiceID = params.get("ServiceID")
        self._EnableDashboardConfig = params.get("EnableDashboardConfig")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._EnableSecurityConfig = params.get("EnableSecurityConfig")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._UrlAutoConvergenceEnable = params.get("UrlAutoConvergenceEnable")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        self._DisableMemoryUsed = params.get("DisableMemoryUsed")
        self._DisableCpuUsed = params.get("DisableCpuUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmApplicationConfigView(AbstractModel):
    r"""应用相关的配置列表项

    """

    def __init__(self):
        r"""
        :param _InstanceKey: 业务系统 ID
        :type InstanceKey: str
        :param _ServiceName: 应用名	
        :type ServiceName: str
        :param _OperationNameFilter: 接口过滤
        :type OperationNameFilter: str
        :param _ExceptionFilter: 错误类型过滤
        :type ExceptionFilter: str
        :param _ErrorCodeFilter: HTTP 状态码过滤
        :type ErrorCodeFilter: str
        :param _EventEnable: 应用诊断开关（已废弃）
        :type EventEnable: bool
        :param _UrlConvergenceSwitch: URL 收敛开关 0 关 1 开
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: URL 收敛阈值	
        :type UrlConvergenceThreshold: int
        :param _UrlConvergence: URL 收敛规则正则	
        :type UrlConvergence: str
        :param _UrlExclude: URL 排除规则正则
        :type UrlExclude: str
        :param _IsRelatedLog: 是否开启日志 0 关 1 开
        :type IsRelatedLog: int
        :param _LogSource: 日志源	
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
        :type InstrumentList: list of Instrument
        :param _TraceSquash: 链路压缩开关（已废弃）
        :type TraceSquash: bool
        :param _DisableMemoryUsed: 探针熔断内存阈值
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: 探针熔断CPU阈值
        :type DisableCpuUsed: int
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
        self._DisableMemoryUsed = None
        self._DisableCpuUsed = None

    @property
    def InstanceKey(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""应用名	
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OperationNameFilter(self):
        r"""接口过滤
        :rtype: str
        """
        return self._OperationNameFilter

    @OperationNameFilter.setter
    def OperationNameFilter(self, OperationNameFilter):
        self._OperationNameFilter = OperationNameFilter

    @property
    def ExceptionFilter(self):
        r"""错误类型过滤
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def ErrorCodeFilter(self):
        r"""HTTP 状态码过滤
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def EventEnable(self):
        r"""应用诊断开关（已废弃）
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def UrlConvergenceSwitch(self):
        r"""URL 收敛开关 0 关 1 开
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""URL 收敛阈值	
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def UrlConvergence(self):
        r"""URL 收敛规则正则	
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def UrlExclude(self):
        r"""URL 排除规则正则
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def IsRelatedLog(self):
        r"""是否开启日志 0 关 1 开
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogSource(self):
        r"""日志源	
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def LogSet(self):
        r"""日志集 
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogTopicID(self):
        r"""日志主题
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def SnapshotEnable(self):
        r"""方法栈快照开关 true 开启 false 关闭
        :rtype: bool
        """
        return self._SnapshotEnable

    @SnapshotEnable.setter
    def SnapshotEnable(self, SnapshotEnable):
        self._SnapshotEnable = SnapshotEnable

    @property
    def SnapshotTimeout(self):
        r"""慢调用监听触发阈值
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""探针总开关
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def InstrumentList(self):
        r"""组件列表开关（已废弃）
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def TraceSquash(self):
        r"""链路压缩开关（已废弃）
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def DisableMemoryUsed(self):
        r"""探针熔断内存阈值
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""探针熔断CPU阈值
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed


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
        self._DisableMemoryUsed = params.get("DisableMemoryUsed")
        self._DisableCpuUsed = params.get("DisableCpuUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmAssociation(AbstractModel):
    r"""展示apm业务系统与其他云产品关联关系返回体

    """

    def __init__(self):
        r"""
        :param _PeerId: 关联产品的实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerId: str
        :param _Status: 关联关系状态：1（启用）、2（不启用）、3（已失效）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Topic: CKafka消息主题
        :type Topic: str
        """
        self._PeerId = None
        self._Status = None
        self._Topic = None

    @property
    def PeerId(self):
        r"""关联产品的实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def Status(self):
        r"""关联关系状态：1（启用）、2（不启用）、3（已失效）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Topic(self):
        r"""CKafka消息主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._PeerId = params.get("PeerId")
        self._Status = params.get("Status")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmField(AbstractModel):
    r"""指标维度信息

    """

    def __init__(self):
        r"""
        :param _Key: 指标名
        :type Key: str
        :param _Value: 指标数值
        :type Value: float
        :param _Unit: 指标所对应的单位
        :type Unit: str
        :param _CompareVals: 同比结果数组，推荐使用
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareVals: list of APMKVItem
        :param _LastPeriodValue: 同比上一个周期的具体指标数值
注意：此字段可能返回 null，表示取不到有效值。
        :type LastPeriodValue: list of APMKV
        :param _CompareVal: 同比指标值，已弃用，不建议使用
        :type CompareVal: str
        :param _NameCN: 指标中文名
        :type NameCN: str
        :param _NameEN: 指标英文名
        :type NameEN: str
        """
        self._Key = None
        self._Value = None
        self._Unit = None
        self._CompareVals = None
        self._LastPeriodValue = None
        self._CompareVal = None
        self._NameCN = None
        self._NameEN = None

    @property
    def Key(self):
        r"""指标名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""指标数值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Unit(self):
        r"""指标所对应的单位
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def CompareVals(self):
        r"""同比结果数组，推荐使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of APMKVItem
        """
        return self._CompareVals

    @CompareVals.setter
    def CompareVals(self, CompareVals):
        self._CompareVals = CompareVals

    @property
    def LastPeriodValue(self):
        r"""同比上一个周期的具体指标数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of APMKV
        """
        return self._LastPeriodValue

    @LastPeriodValue.setter
    def LastPeriodValue(self, LastPeriodValue):
        self._LastPeriodValue = LastPeriodValue

    @property
    def CompareVal(self):
        r"""同比指标值，已弃用，不建议使用
        :rtype: str
        """
        return self._CompareVal

    @CompareVal.setter
    def CompareVal(self, CompareVal):
        self._CompareVal = CompareVal

    @property
    def NameCN(self):
        r"""指标中文名
        :rtype: str
        """
        return self._NameCN

    @NameCN.setter
    def NameCN(self, NameCN):
        self._NameCN = NameCN

    @property
    def NameEN(self):
        r"""指标英文名
        :rtype: str
        """
        return self._NameEN

    @NameEN.setter
    def NameEN(self, NameEN):
        self._NameEN = NameEN


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Unit = params.get("Unit")
        if params.get("CompareVals") is not None:
            self._CompareVals = []
            for item in params.get("CompareVals"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._CompareVals.append(obj)
        if params.get("LastPeriodValue") is not None:
            self._LastPeriodValue = []
            for item in params.get("LastPeriodValue"):
                obj = APMKV()
                obj._deserialize(item)
                self._LastPeriodValue.append(obj)
        self._CompareVal = params.get("CompareVal")
        self._NameCN = params.get("NameCN")
        self._NameEN = params.get("NameEN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmInstanceDetail(AbstractModel):
    r"""APM 业务系统信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _Name: 业务系统名
        :type Name: str
        :param _Description: 业务系统描述信息
        :type Description: str
        :param _Status: 业务系统状态。{
1: 初始化中; 2: 运行中; 4: 限流}
        :type Status: int
        :param _Region: 业务系统所属地域
        :type Region: str
        :param _Tags: 业务系统 Tag 列表
        :type Tags: list of ApmTag
        :param _AppId: AppID 信息
        :type AppId: int
        :param _CreateUin: 创建人 Uin
        :type CreateUin: str
        :param _AmountOfUsedStorage: 存储使用量(单位：MB)
        :type AmountOfUsedStorage: float
        :param _ServiceCount: 该业务系统服务端应用数量
        :type ServiceCount: int
        :param _CountOfReportSpanPerDay: 日均上报 Span 数
        :type CountOfReportSpanPerDay: int
        :param _TraceDuration: Trace 数据保存时长（单位：天）
        :type TraceDuration: int
        :param _SpanDailyCounters: 业务系统上报额度
        :type SpanDailyCounters: int
        :param _BillingInstance: 业务系统是否已开通计费（0=未开通，1=已开通）
        :type BillingInstance: int
        :param _ErrRateThreshold: 错误警示线（单位：%）
        :type ErrRateThreshold: int
        :param _SampleRate: 采样率（单位：%）
        :type SampleRate: int
        :param _ErrorSample: 是否开启错误采样（0=关, 1=开）
        :type ErrorSample: int
        :param _SlowRequestSavedThreshold: 采样慢调用保存阈值（单位：ms）
        :type SlowRequestSavedThreshold: int
        :param _LogRegion: CLS 日志所在地域
        :type LogRegion: str
        :param _LogSource: 日志源
        :type LogSource: str
        :param _IsRelatedLog: 日志功能开关（0=关， 1=开）
        :type IsRelatedLog: int
        :param _LogTopicID: 日志主题 ID
        :type LogTopicID: str
        :param _ClientCount: 该业务系统客户端应用数量
        :type ClientCount: int
        :param _TotalCount: 该业务系统最近2天活跃应用数量
        :type TotalCount: int
        :param _LogSet: CLS 日志集
        :type LogSet: str
        :param _MetricDuration: Metric 数据保存时长（单位：天）
        :type MetricDuration: int
        :param _CustomShowTags: 用户自定义展示标签列表
        :type CustomShowTags: list of str
        :param _PayMode: 业务系统计费模式（1为预付费，0为按量付费）
        :type PayMode: int
        :param _PayModeEffective: 业务系统计费模式是否生效
        :type PayModeEffective: bool
        :param _ResponseDurationWarningThreshold: 响应时间警示线（单位：ms）
        :type ResponseDurationWarningThreshold: int
        :param _Free: 是否免费（0=否，1=限额免费，2=完全免费），默认0
        :type Free: int
        :param _DefaultTSF: 是否 TSF 默认业务系统（0=否，1=是）
        :type DefaultTSF: int
        :param _IsRelatedDashboard: 是否关联 Dashboard（0=关, 1=开）
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: 关联的 Dashboard ID
        :type DashboardTopicID: str
        :param _IsInstrumentationVulnerabilityScan: 是否开启组件漏洞检测（0=关， 1=开）
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsSqlInjectionAnalysis: 是否开启 SQL 注入分析（0=关， 1=开）
        :type IsSqlInjectionAnalysis: int
        :param _StopReason: 限流原因。{
1: 正式版限额;
2: 试用版限额;
4: 试用版到期;
8: 账号欠费
}
        :type StopReason: int
        :param _IsRemoteCommandExecutionAnalysis: 是否开远程命令执行检测（0=关， 1=开）
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: 是否开内存马执行检测（0=关， 1=开）
        :type IsMemoryHijackingAnalysis: int
        :param _LogIndexType: CLS索引类型(0=全文索引，1=键值索引)
        :type LogIndexType: int
        :param _LogTraceIdKey: traceId的索引key: 当CLS索引类型为键值索引时生效
        :type LogTraceIdKey: str
        :param _IsDeleteAnyFileAnalysis: 是否开启删除任意文件检测（0-关闭，1-开启）
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: 是否开启读取任意文件检测（0-关闭，1-开启）
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: 是否开启上传任意文件检测（0-关闭，1-开启）
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: 是否开启包含任意文件检测（0-关闭，1-开启）
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: 是否开启目录遍历检测（0-关闭，1-开启）
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: 是否开启模板引擎注入检测（0-关闭，1-开启）
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: 是否开启脚本引擎注入检测（0-关闭，1-开启）
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: 是否开启表达式注入检测（0-关闭，1-开启）
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: 是否开启JNDI注入检测（0-关闭，1-开启）
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: 是否开启JNI注入检测（0-关闭，1-开启）
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: 是否开启Webshell后门检测（0-关闭，1-开启）
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: 是否开启反序列化检测（0-关闭，1-开启）
        :type IsDeserializationAnalysis: int
        :param _Token: 业务系统鉴权 token
        :type Token: str
        :param _UrlLongSegmentThreshold: URL长分段收敛阈值
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: URL数字分段收敛阈值
        :type UrlNumberSegmentThreshold: int
        """
        self._InstanceId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Region = None
        self._Tags = None
        self._AppId = None
        self._CreateUin = None
        self._AmountOfUsedStorage = None
        self._ServiceCount = None
        self._CountOfReportSpanPerDay = None
        self._TraceDuration = None
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
        self._StopReason = None
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._Token = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""业务系统名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""业务系统描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""业务系统状态。{
1: 初始化中; 2: 运行中; 4: 限流}
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""业务系统所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        r"""业务系统 Tag 列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AppId(self):
        r"""AppID 信息
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreateUin(self):
        r"""创建人 Uin
        :rtype: str
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def AmountOfUsedStorage(self):
        r"""存储使用量(单位：MB)
        :rtype: float
        """
        return self._AmountOfUsedStorage

    @AmountOfUsedStorage.setter
    def AmountOfUsedStorage(self, AmountOfUsedStorage):
        self._AmountOfUsedStorage = AmountOfUsedStorage

    @property
    def ServiceCount(self):
        r"""该业务系统服务端应用数量
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def CountOfReportSpanPerDay(self):
        r"""日均上报 Span 数
        :rtype: int
        """
        return self._CountOfReportSpanPerDay

    @CountOfReportSpanPerDay.setter
    def CountOfReportSpanPerDay(self, CountOfReportSpanPerDay):
        self._CountOfReportSpanPerDay = CountOfReportSpanPerDay

    @property
    def TraceDuration(self):
        r"""Trace 数据保存时长（单位：天）
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def SpanDailyCounters(self):
        r"""业务系统上报额度
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def BillingInstance(self):
        r"""业务系统是否已开通计费（0=未开通，1=已开通）
        :rtype: int
        """
        return self._BillingInstance

    @BillingInstance.setter
    def BillingInstance(self, BillingInstance):
        self._BillingInstance = BillingInstance

    @property
    def ErrRateThreshold(self):
        r"""错误警示线（单位：%）
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        r"""采样率（单位：%）
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        r"""是否开启错误采样（0=关, 1=开）
        :rtype: int
        """
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        r"""采样慢调用保存阈值（单位：ms）
        :rtype: int
        """
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def LogRegion(self):
        r"""CLS 日志所在地域
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogSource(self):
        r"""日志源
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def IsRelatedLog(self):
        r"""日志功能开关（0=关， 1=开）
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogTopicID(self):
        r"""日志主题 ID
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def ClientCount(self):
        r"""该业务系统客户端应用数量
        :rtype: int
        """
        return self._ClientCount

    @ClientCount.setter
    def ClientCount(self, ClientCount):
        self._ClientCount = ClientCount

    @property
    def TotalCount(self):
        r"""该业务系统最近2天活跃应用数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LogSet(self):
        r"""CLS 日志集
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def MetricDuration(self):
        r"""Metric 数据保存时长（单位：天）
        :rtype: int
        """
        return self._MetricDuration

    @MetricDuration.setter
    def MetricDuration(self, MetricDuration):
        self._MetricDuration = MetricDuration

    @property
    def CustomShowTags(self):
        r"""用户自定义展示标签列表
        :rtype: list of str
        """
        return self._CustomShowTags

    @CustomShowTags.setter
    def CustomShowTags(self, CustomShowTags):
        self._CustomShowTags = CustomShowTags

    @property
    def PayMode(self):
        r"""业务系统计费模式（1为预付费，0为按量付费）
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def PayModeEffective(self):
        r"""业务系统计费模式是否生效
        :rtype: bool
        """
        return self._PayModeEffective

    @PayModeEffective.setter
    def PayModeEffective(self, PayModeEffective):
        self._PayModeEffective = PayModeEffective

    @property
    def ResponseDurationWarningThreshold(self):
        r"""响应时间警示线（单位：ms）
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def Free(self):
        r"""是否免费（0=否，1=限额免费，2=完全免费），默认0
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free

    @property
    def DefaultTSF(self):
        r"""是否 TSF 默认业务系统（0=否，1=是）
        :rtype: int
        """
        return self._DefaultTSF

    @DefaultTSF.setter
    def DefaultTSF(self, DefaultTSF):
        self._DefaultTSF = DefaultTSF

    @property
    def IsRelatedDashboard(self):
        r"""是否关联 Dashboard（0=关, 1=开）
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""关联的 Dashboard ID
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""是否开启组件漏洞检测（0=关， 1=开）
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsSqlInjectionAnalysis(self):
        r"""是否开启 SQL 注入分析（0=关， 1=开）
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def StopReason(self):
        r"""限流原因。{
1: 正式版限额;
2: 试用版限额;
4: 试用版到期;
8: 账号欠费
}
        :rtype: int
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""是否开远程命令执行检测（0=关， 1=开）
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""是否开内存马执行检测（0=关， 1=开）
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def LogIndexType(self):
        r"""CLS索引类型(0=全文索引，1=键值索引)
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""traceId的索引key: 当CLS索引类型为键值索引时生效
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""是否开启删除任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""是否开启读取任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""是否开启上传任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""是否开启包含任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""是否开启目录遍历检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""是否开启模板引擎注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""是否开启脚本引擎注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""是否开启表达式注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""是否开启JNDI注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""是否开启JNI注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""是否开启Webshell后门检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""是否开启反序列化检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def Token(self):
        r"""业务系统鉴权 token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def UrlLongSegmentThreshold(self):
        r"""URL长分段收敛阈值
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""URL数字分段收敛阈值
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AppId = params.get("AppId")
        self._CreateUin = params.get("CreateUin")
        self._AmountOfUsedStorage = params.get("AmountOfUsedStorage")
        self._ServiceCount = params.get("ServiceCount")
        self._CountOfReportSpanPerDay = params.get("CountOfReportSpanPerDay")
        self._TraceDuration = params.get("TraceDuration")
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
        self._StopReason = params.get("StopReason")
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._Token = params.get("Token")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmMetricRecord(AbstractModel):
    r"""指标列表单元

    """

    def __init__(self):
        r"""
        :param _Fields: field数组，用于指标的查询结果
        :type Fields: list of ApmField
        :param _Tags: tag数组，用于区分 Groupby 的对象
        :type Tags: list of ApmTag
        """
        self._Fields = None
        self._Tags = None

    @property
    def Fields(self):
        r"""field数组，用于指标的查询结果
        :rtype: list of ApmField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Tags(self):
        r"""tag数组，用于区分 Groupby 的对象
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
        


class ApmPrometheusRules(AbstractModel):
    r"""展示apm业务系统关联prometheus关系返回体

    """

    def __init__(self):
        r"""
        :param _Id: 指标匹配规则ID
        :type Id: int
        :param _Name: 指标匹配规则名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ServiceName: 规则生效的应用。生效于全部应用就传空字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _Status: 指标匹配规则状态：1(启用)、2（不启用）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _MetricNameRule: 指标匹配规则
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricNameRule: str
        :param _MetricMatchType: 匹配类型：0精准匹配，1前缀匹配，2后缀匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricMatchType: int
        """
        self._Id = None
        self._Name = None
        self._ServiceName = None
        self._Status = None
        self._MetricNameRule = None
        self._MetricMatchType = None

    @property
    def Id(self):
        r"""指标匹配规则ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""指标匹配规则名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ServiceName(self):
        r"""规则生效的应用。生效于全部应用就传空字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Status(self):
        r"""指标匹配规则状态：1(启用)、2（不启用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MetricNameRule(self):
        r"""指标匹配规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MetricNameRule

    @MetricNameRule.setter
    def MetricNameRule(self, MetricNameRule):
        self._MetricNameRule = MetricNameRule

    @property
    def MetricMatchType(self):
        r"""匹配类型：0精准匹配，1前缀匹配，2后缀匹配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MetricMatchType

    @MetricMatchType.setter
    def MetricMatchType(self, MetricMatchType):
        self._MetricMatchType = MetricMatchType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ServiceName = params.get("ServiceName")
        self._Status = params.get("Status")
        self._MetricNameRule = params.get("MetricNameRule")
        self._MetricMatchType = params.get("MetricMatchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmSampleConfig(AbstractModel):
    r"""采样配置信息

    """

    def __init__(self):
        r"""
        :param _InstanceKey: 实例ID
        :type InstanceKey: str
        :param _ServiceName: 服务名
        :type ServiceName: str
        :param _SampleName: 采样名字
        :type SampleName: str
        :param _OperationName: 接口名
        :type OperationName: str
        :param _SpanNum: 采样的span数
        :type SpanNum: int
        :param _Status: 采样配置开关 0 关 1 开
        :type Status: int
        :param _Tags: tags数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of APMKVItem
        :param _SampleRate: 采样率
        :type SampleRate: int
        :param _OperationType: 0=精确匹配（默认）；1=前缀匹配；2=后缀匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationType: int
        :param _Id: 配置Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        """
        self._InstanceKey = None
        self._ServiceName = None
        self._SampleName = None
        self._OperationName = None
        self._SpanNum = None
        self._Status = None
        self._Tags = None
        self._SampleRate = None
        self._OperationType = None
        self._Id = None

    @property
    def InstanceKey(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def ServiceName(self):
        r"""服务名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def SampleName(self):
        r"""采样名字
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName

    @property
    def OperationName(self):
        r"""接口名
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def SpanNum(self):
        r"""采样的span数
        :rtype: int
        """
        return self._SpanNum

    @SpanNum.setter
    def SpanNum(self, SpanNum):
        self._SpanNum = SpanNum

    @property
    def Status(self):
        r"""采样配置开关 0 关 1 开
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""tags数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of APMKVItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SampleRate(self):
        r"""采样率
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def OperationType(self):
        r"""0=精确匹配（默认）；1=前缀匹配；2=后缀匹配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def Id(self):
        r"""配置Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._InstanceKey = params.get("InstanceKey")
        self._ServiceName = params.get("ServiceName")
        self._SampleName = params.get("SampleName")
        self._OperationName = params.get("OperationName")
        self._SpanNum = params.get("SpanNum")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SampleRate = params.get("SampleRate")
        self._OperationType = params.get("OperationType")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmServiceMetric(AbstractModel):
    r"""apm应用指标信息

    """

    def __init__(self):
        r"""
        :param _Fields: filed数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Fields: list of ApmField
        :param _Tags: tag数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApmTag
        :param _ServiceDetail: 应用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDetail: :class:`tencentcloud.apm.v20210622.models.ServiceDetail`
        """
        self._Fields = None
        self._Tags = None
        self._ServiceDetail = None

    @property
    def Fields(self):
        r"""filed数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmField
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Tags(self):
        r"""tag数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceDetail(self):
        r"""应用信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apm.v20210622.models.ServiceDetail`
        """
        return self._ServiceDetail

    @ServiceDetail.setter
    def ServiceDetail(self, ServiceDetail):
        self._ServiceDetail = ServiceDetail


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
        if params.get("ServiceDetail") is not None:
            self._ServiceDetail = ServiceDetail()
            self._ServiceDetail._deserialize(params.get("ServiceDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmTag(AbstractModel):
    r"""维度（标签）对象

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
        r"""维度Key(列名，标签Key)
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""维度值（标签值）
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
    r"""CreateApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 业务系统名
        :type Name: str
        :param _Description: 业务系统描述信息
        :type Description: str
        :param _TraceDuration: Trace 数据保存时长（单位：天，默认存储时长为3天）
        :type TraceDuration: int
        :param _Tags: 业务系统 Tag 列表
        :type Tags: list of ApmTag
        :param _SpanDailyCounters: 业务系统上报额度值，默认赋值为0表示不限制上报额度，已废弃
        :type SpanDailyCounters: int
        :param _PayMode: 业务系统的计费模式（0=按量付费，1=预付费）
        :type PayMode: int
        :param _Free: 是否为免费版业务系统（0=付费版；1=TSF 受限免费版；2=免费版）
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
        r"""业务系统名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""业务系统描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        r"""Trace 数据保存时长（单位：天，默认存储时长为3天）
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def Tags(self):
        r"""业务系统 Tag 列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SpanDailyCounters(self):
        r"""业务系统上报额度值，默认赋值为0表示不限制上报额度，已废弃
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def PayMode(self):
        r"""业务系统的计费模式（0=按量付费，1=预付费）
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Free(self):
        r"""是否为免费版业务系统（0=付费版；1=TSF 受限免费版；2=免费版）
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
    r"""CreateApmInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
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


class CreateApmPrometheusRuleRequest(AbstractModel):
    r"""CreateApmPrometheusRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 指标匹配规则名
        :type Name: str
        :param _ServiceName: 规则生效的应用。作用全部应用就传空字符串
        :type ServiceName: str
        :param _MetricMatchType: 指标匹配类型：0精准匹配，1前缀匹配，2后缀匹配
        :type MetricMatchType: int
        :param _MetricNameRule: 客户定义的命中指标名规则。
        :type MetricNameRule: str
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        """
        self._Name = None
        self._ServiceName = None
        self._MetricMatchType = None
        self._MetricNameRule = None
        self._InstanceId = None

    @property
    def Name(self):
        r"""指标匹配规则名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ServiceName(self):
        r"""规则生效的应用。作用全部应用就传空字符串
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def MetricMatchType(self):
        r"""指标匹配类型：0精准匹配，1前缀匹配，2后缀匹配
        :rtype: int
        """
        return self._MetricMatchType

    @MetricMatchType.setter
    def MetricMatchType(self, MetricMatchType):
        self._MetricMatchType = MetricMatchType

    @property
    def MetricNameRule(self):
        r"""客户定义的命中指标名规则。
        :rtype: str
        """
        return self._MetricNameRule

    @MetricNameRule.setter
    def MetricNameRule(self, MetricNameRule):
        self._MetricNameRule = MetricNameRule

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ServiceName = params.get("ServiceName")
        self._MetricMatchType = params.get("MetricMatchType")
        self._MetricNameRule = params.get("MetricNameRule")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmPrometheusRuleResponse(AbstractModel):
    r"""CreateApmPrometheusRule返回参数结构体

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


class CreateApmSampleConfigRequest(AbstractModel):
    r"""CreateApmSampleConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _SampleRate: 采样率
        :type SampleRate: int
        :param _ServiceName: 应用名
        :type ServiceName: str
        :param _SampleName: 采样规则名
        :type SampleName: str
        :param _Tags: 采样Tags
        :type Tags: list of APMKVItem
        :param _OperationName: 接口名
        :type OperationName: str
        :param _OperationType: 0=精确匹配（默认）；1=前缀匹配；2=后缀匹配
        :type OperationType: int
        """
        self._InstanceId = None
        self._SampleRate = None
        self._ServiceName = None
        self._SampleName = None
        self._Tags = None
        self._OperationName = None
        self._OperationType = None

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleRate(self):
        r"""采样率
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ServiceName(self):
        r"""应用名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def SampleName(self):
        r"""采样规则名
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName

    @property
    def Tags(self):
        r"""采样Tags
        :rtype: list of APMKVItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def OperationName(self):
        r"""接口名
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def OperationType(self):
        r"""0=精确匹配（默认）；1=前缀匹配；2=后缀匹配
        :rtype: int
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleRate = params.get("SampleRate")
        self._ServiceName = params.get("ServiceName")
        self._SampleName = params.get("SampleName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._OperationName = params.get("OperationName")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmSampleConfigResponse(AbstractModel):
    r"""CreateApmSampleConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmSampleConfig: 采样配置参数
        :type ApmSampleConfig: :class:`tencentcloud.apm.v20210622.models.ApmSampleConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmSampleConfig = None
        self._RequestId = None

    @property
    def ApmSampleConfig(self):
        r"""采样配置参数
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmSampleConfig`
        """
        return self._ApmSampleConfig

    @ApmSampleConfig.setter
    def ApmSampleConfig(self, ApmSampleConfig):
        self._ApmSampleConfig = ApmSampleConfig

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
        if params.get("ApmSampleConfig") is not None:
            self._ApmSampleConfig = ApmSampleConfig()
            self._ApmSampleConfig._deserialize(params.get("ApmSampleConfig"))
        self._RequestId = params.get("RequestId")


class CreateProfileTaskRequest(AbstractModel):
    r"""CreateProfileTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceName: 应用名称
        :type ServiceName: str
        :param _InstanceId: APM业务系统ID
        :type InstanceId: str
        :param _ServiceInstance: 应用实例（在线）
        :type ServiceInstance: str
        :param _Event: 事件类型（cpu、alloc）
        :type Event: str
        :param _Duration: 任务持续时长(单位：毫秒)，范围限制在5~180秒
        :type Duration: int
        :param _AllTimes: 执行次数，范围限制在1~100次
        :type AllTimes: int
        :param _StartTime: 开始时间戳，0代表从当前开始(单位：秒)
        :type StartTime: int
        :param _TaskInterval: 任务执行间隔(单位：毫秒)，范围限制在10~600秒，不可小于1.5倍的Duration
        :type TaskInterval: int
        """
        self._ServiceName = None
        self._InstanceId = None
        self._ServiceInstance = None
        self._Event = None
        self._Duration = None
        self._AllTimes = None
        self._StartTime = None
        self._TaskInterval = None

    @property
    def ServiceName(self):
        r"""应用名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        r"""APM业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceInstance(self):
        r"""应用实例（在线）
        :rtype: str
        """
        return self._ServiceInstance

    @ServiceInstance.setter
    def ServiceInstance(self, ServiceInstance):
        self._ServiceInstance = ServiceInstance

    @property
    def Event(self):
        r"""事件类型（cpu、alloc）
        :rtype: str
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def Duration(self):
        r"""任务持续时长(单位：毫秒)，范围限制在5~180秒
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def AllTimes(self):
        r"""执行次数，范围限制在1~100次
        :rtype: int
        """
        return self._AllTimes

    @AllTimes.setter
    def AllTimes(self, AllTimes):
        self._AllTimes = AllTimes

    @property
    def StartTime(self):
        r"""开始时间戳，0代表从当前开始(单位：秒)
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def TaskInterval(self):
        r"""任务执行间隔(单位：毫秒)，范围限制在10~600秒，不可小于1.5倍的Duration
        :rtype: int
        """
        return self._TaskInterval

    @TaskInterval.setter
    def TaskInterval(self, TaskInterval):
        self._TaskInterval = TaskInterval


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._InstanceId = params.get("InstanceId")
        self._ServiceInstance = params.get("ServiceInstance")
        self._Event = params.get("Event")
        self._Duration = params.get("Duration")
        self._AllTimes = params.get("AllTimes")
        self._StartTime = params.get("StartTime")
        self._TaskInterval = params.get("TaskInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProfileTaskResponse(AbstractModel):
    r"""CreateProfileTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteApmSampleConfigRequest(AbstractModel):
    r"""DeleteApmSampleConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _SampleName: 采样规则名
        :type SampleName: str
        """
        self._InstanceId = None
        self._SampleName = None

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleName(self):
        r"""采样规则名
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleName = params.get("SampleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApmSampleConfigResponse(AbstractModel):
    r"""DeleteApmSampleConfig返回参数结构体

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


class DescribeApmAgentRequest(AbstractModel):
    r"""DescribeApmAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _AgentType: 接入方式，现支持 skywalking, ot, ebpf 方式接入上报，不填默认为 ot
        :type AgentType: str
        :param _NetworkMode: 上报环境，现支持 pl (内网上报), public (外网), inner (自研 VPC )环境上报，不传默认为 public
        :type NetworkMode: str
        :param _LanguageEnvironment: 语言，现支持 java, golang, php, python, dotNet, nodejs 语言上报，不传默认为 golang
        :type LanguageEnvironment: str
        :param _ReportMethod: 上报方式，已弃用
        :type ReportMethod: str
        """
        self._InstanceId = None
        self._AgentType = None
        self._NetworkMode = None
        self._LanguageEnvironment = None
        self._ReportMethod = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AgentType(self):
        r"""接入方式，现支持 skywalking, ot, ebpf 方式接入上报，不填默认为 ot
        :rtype: str
        """
        return self._AgentType

    @AgentType.setter
    def AgentType(self, AgentType):
        self._AgentType = AgentType

    @property
    def NetworkMode(self):
        r"""上报环境，现支持 pl (内网上报), public (外网), inner (自研 VPC )环境上报，不传默认为 public
        :rtype: str
        """
        return self._NetworkMode

    @NetworkMode.setter
    def NetworkMode(self, NetworkMode):
        self._NetworkMode = NetworkMode

    @property
    def LanguageEnvironment(self):
        r"""语言，现支持 java, golang, php, python, dotNet, nodejs 语言上报，不传默认为 golang
        :rtype: str
        """
        return self._LanguageEnvironment

    @LanguageEnvironment.setter
    def LanguageEnvironment(self, LanguageEnvironment):
        self._LanguageEnvironment = LanguageEnvironment

    @property
    def ReportMethod(self):
        r"""上报方式，已弃用
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
    r"""DescribeApmAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmAgent: Agent 信息
        :type ApmAgent: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmAgent = None
        self._RequestId = None

    @property
    def ApmAgent(self):
        r"""Agent 信息
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        """
        return self._ApmAgent

    @ApmAgent.setter
    def ApmAgent(self, ApmAgent):
        self._ApmAgent = ApmAgent

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
        if params.get("ApmAgent") is not None:
            self._ApmAgent = ApmAgentInfo()
            self._ApmAgent._deserialize(params.get("ApmAgent"))
        self._RequestId = params.get("RequestId")


class DescribeApmApplicationConfigRequest(AbstractModel):
    r"""DescribeApmApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        """
        self._InstanceId = None
        self._ServiceName = None

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
    def ServiceName(self):
        r"""服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmApplicationConfigResponse(AbstractModel):
    r"""DescribeApmApplicationConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmAppConfig: Apm应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmAppConfig: :class:`tencentcloud.apm.v20210622.models.ApmAppConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmAppConfig = None
        self._RequestId = None

    @property
    def ApmAppConfig(self):
        r"""Apm应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmAppConfig`
        """
        return self._ApmAppConfig

    @ApmAppConfig.setter
    def ApmAppConfig(self, ApmAppConfig):
        self._ApmAppConfig = ApmAppConfig

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
        if params.get("ApmAppConfig") is not None:
            self._ApmAppConfig = ApmAppConfig()
            self._ApmAppConfig._deserialize(params.get("ApmAppConfig"))
        self._RequestId = params.get("RequestId")


class DescribeApmAssociationRequest(AbstractModel):
    r"""DescribeApmAssociation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 关联的产品名，当前只支持Prometheus
        :type ProductName: str
        :param _InstanceId: 业务系统名
        :type InstanceId: str
        """
        self._ProductName = None
        self._InstanceId = None

    @property
    def ProductName(self):
        r"""关联的产品名，当前只支持Prometheus
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def InstanceId(self):
        r"""业务系统名
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmAssociationResponse(AbstractModel):
    r"""DescribeApmAssociation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmAssociation: 关联的产品实例ID
        :type ApmAssociation: :class:`tencentcloud.apm.v20210622.models.ApmAssociation`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmAssociation = None
        self._RequestId = None

    @property
    def ApmAssociation(self):
        r"""关联的产品实例ID
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmAssociation`
        """
        return self._ApmAssociation

    @ApmAssociation.setter
    def ApmAssociation(self, ApmAssociation):
        self._ApmAssociation = ApmAssociation

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
        if params.get("ApmAssociation") is not None:
            self._ApmAssociation = ApmAssociation()
            self._ApmAssociation._deserialize(params.get("ApmAssociation"))
        self._RequestId = params.get("RequestId")


class DescribeApmInstancesRequest(AbstractModel):
    r"""DescribeApmInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tags: Tag 列表
        :type Tags: list of ApmTag
        :param _InstanceName: 按业务系统名过滤，支持模糊检索
        :type InstanceName: str
        :param _InstanceId: 按业务系统 ID 过滤，支持模糊检索
        :type InstanceId: str
        :param _InstanceIds: 按业务系统 ID 过滤
        :type InstanceIds: list of str
        :param _DemoInstanceFlag: 是否查询官方 Demo 业务系统（0=非 Demo 业务系统，1=Demo 业务系统，默认为0）
        :type DemoInstanceFlag: int
        :param _AllRegionsFlag: 是否查询全地域业务系统（0=不查询全地域，1=查询全地域，默认为0）
        :type AllRegionsFlag: int
        """
        self._Tags = None
        self._InstanceName = None
        self._InstanceId = None
        self._InstanceIds = None
        self._DemoInstanceFlag = None
        self._AllRegionsFlag = None

    @property
    def Tags(self):
        r"""Tag 列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceName(self):
        r"""按业务系统名过滤，支持模糊检索
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        r"""按业务系统 ID 过滤，支持模糊检索
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceIds(self):
        r"""按业务系统 ID 过滤
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DemoInstanceFlag(self):
        r"""是否查询官方 Demo 业务系统（0=非 Demo 业务系统，1=Demo 业务系统，默认为0）
        :rtype: int
        """
        return self._DemoInstanceFlag

    @DemoInstanceFlag.setter
    def DemoInstanceFlag(self, DemoInstanceFlag):
        self._DemoInstanceFlag = DemoInstanceFlag

    @property
    def AllRegionsFlag(self):
        r"""是否查询全地域业务系统（0=不查询全地域，1=查询全地域，默认为0）
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
        self._InstanceId = params.get("InstanceId")
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
    r"""DescribeApmInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: APM 业务系统列表
        :type Instances: list of ApmInstanceDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""APM 业务系统列表
        :rtype: list of ApmInstanceDetail
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

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
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = ApmInstanceDetail()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApmPrometheusRuleRequest(AbstractModel):
    r"""DescribeApmPrometheusRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""业务系统ID
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
        


class DescribeApmPrometheusRuleResponse(AbstractModel):
    r"""DescribeApmPrometheusRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmPrometheusRules: 指标匹配规则
        :type ApmPrometheusRules: list of ApmPrometheusRules
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmPrometheusRules = None
        self._RequestId = None

    @property
    def ApmPrometheusRules(self):
        r"""指标匹配规则
        :rtype: list of ApmPrometheusRules
        """
        return self._ApmPrometheusRules

    @ApmPrometheusRules.setter
    def ApmPrometheusRules(self, ApmPrometheusRules):
        self._ApmPrometheusRules = ApmPrometheusRules

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
        if params.get("ApmPrometheusRules") is not None:
            self._ApmPrometheusRules = []
            for item in params.get("ApmPrometheusRules"):
                obj = ApmPrometheusRules()
                obj._deserialize(item)
                self._ApmPrometheusRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApmSampleConfigRequest(AbstractModel):
    r"""DescribeApmSampleConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _SampleName: 采样规则名
        :type SampleName: str
        """
        self._InstanceId = None
        self._SampleName = None

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleName(self):
        r"""采样规则名
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleName = params.get("SampleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmSampleConfigResponse(AbstractModel):
    r"""DescribeApmSampleConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApmSampleConfigs: 采样配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmSampleConfigs: list of ApmSampleConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApmSampleConfigs = None
        self._RequestId = None

    @property
    def ApmSampleConfigs(self):
        r"""采样配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmSampleConfig
        """
        return self._ApmSampleConfigs

    @ApmSampleConfigs.setter
    def ApmSampleConfigs(self, ApmSampleConfigs):
        self._ApmSampleConfigs = ApmSampleConfigs

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
        if params.get("ApmSampleConfigs") is not None:
            self._ApmSampleConfigs = []
            for item in params.get("ApmSampleConfigs"):
                obj = ApmSampleConfig()
                obj._deserialize(item)
                self._ApmSampleConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApmServiceMetricRequest(AbstractModel):
    r"""DescribeApmServiceMetric请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _ServiceName: 应用名
        :type ServiceName: str
        :param _ServiceID: 应用ID
        :type ServiceID: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _OrderBy: 排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _Demo: 是否demo模式
        :type Demo: bool
        :param _ServiceStatus: 应用状态筛选，可枚举的值为：health、warning、error。如果选中多个状态用逗号隔开，例如："warning,error"
        :type ServiceStatus: str
        :param _Tags: 标签列表
        :type Tags: list of ApmTag
        :param _Page: 页码
        :type Page: int
        :param _PageSize: 页大小
        :type PageSize: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._InstanceId = None
        self._ServiceName = None
        self._ServiceID = None
        self._StartTime = None
        self._EndTime = None
        self._OrderBy = None
        self._Demo = None
        self._ServiceStatus = None
        self._Tags = None
        self._Page = None
        self._PageSize = None
        self._Filters = None

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""应用名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceID(self):
        r"""应用ID
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

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
    def OrderBy(self):
        r"""排序
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Demo(self):
        r"""是否demo模式
        :rtype: bool
        """
        return self._Demo

    @Demo.setter
    def Demo(self, Demo):
        self._Demo = Demo

    @property
    def ServiceStatus(self):
        r"""应用状态筛选，可枚举的值为：health、warning、error。如果选中多个状态用逗号隔开，例如："warning,error"
        :rtype: str
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def Tags(self):
        r"""标签列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Page(self):
        r"""页码
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceID = params.get("ServiceID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._Demo = params.get("Demo")
        self._ServiceStatus = params.get("ServiceStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
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
        


class DescribeApmServiceMetricResponse(AbstractModel):
    r"""DescribeApmServiceMetric返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceMetricList: 应用指标列表
        :type ServiceMetricList: list of ApmServiceMetric
        :param _TotalCount: 符合筛选条件的应用数
        :type TotalCount: int
        :param _WarningErrorCount: 警示异常应用数
        :type WarningErrorCount: int
        :param _ApplicationCount: 应用总数
        :type ApplicationCount: int
        :param _Page: 页码
        :type Page: int
        :param _PageSize: 页大小
        :type PageSize: int
        :param _ErrorCount: 异常应用数
        :type ErrorCount: int
        :param _WarningCount: 警示应用数
        :type WarningCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceMetricList = None
        self._TotalCount = None
        self._WarningErrorCount = None
        self._ApplicationCount = None
        self._Page = None
        self._PageSize = None
        self._ErrorCount = None
        self._WarningCount = None
        self._RequestId = None

    @property
    def ServiceMetricList(self):
        r"""应用指标列表
        :rtype: list of ApmServiceMetric
        """
        return self._ServiceMetricList

    @ServiceMetricList.setter
    def ServiceMetricList(self, ServiceMetricList):
        self._ServiceMetricList = ServiceMetricList

    @property
    def TotalCount(self):
        r"""符合筛选条件的应用数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def WarningErrorCount(self):
        r"""警示异常应用数
        :rtype: int
        """
        return self._WarningErrorCount

    @WarningErrorCount.setter
    def WarningErrorCount(self, WarningErrorCount):
        self._WarningErrorCount = WarningErrorCount

    @property
    def ApplicationCount(self):
        r"""应用总数
        :rtype: int
        """
        return self._ApplicationCount

    @ApplicationCount.setter
    def ApplicationCount(self, ApplicationCount):
        self._ApplicationCount = ApplicationCount

    @property
    def Page(self):
        r"""页码
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ErrorCount(self):
        r"""异常应用数
        :rtype: int
        """
        return self._ErrorCount

    @ErrorCount.setter
    def ErrorCount(self, ErrorCount):
        self._ErrorCount = ErrorCount

    @property
    def WarningCount(self):
        r"""警示应用数
        :rtype: int
        """
        return self._WarningCount

    @WarningCount.setter
    def WarningCount(self, WarningCount):
        self._WarningCount = WarningCount

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
        if params.get("ServiceMetricList") is not None:
            self._ServiceMetricList = []
            for item in params.get("ServiceMetricList"):
                obj = ApmServiceMetric()
                obj._deserialize(item)
                self._ServiceMetricList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._WarningErrorCount = params.get("WarningErrorCount")
        self._ApplicationCount = params.get("ApplicationCount")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._ErrorCount = params.get("ErrorCount")
        self._WarningCount = params.get("WarningCount")
        self._RequestId = params.get("RequestId")


class DescribeGeneralApmApplicationConfigRequest(AbstractModel):
    r"""DescribeGeneralApmApplicationConfig请求参数结构体

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
        r"""应用名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def InstanceId(self):
        r"""业务系统ID
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
    r"""DescribeGeneralApmApplicationConfig返回参数结构体

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
        r"""应用配置项
        :rtype: :class:`tencentcloud.apm.v20210622.models.ApmApplicationConfigView`
        """
        return self._ApmApplicationConfigView

    @ApmApplicationConfigView.setter
    def ApmApplicationConfigView(self, ApmApplicationConfigView):
        self._ApmApplicationConfigView = ApmApplicationConfigView

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
        if params.get("ApmApplicationConfigView") is not None:
            self._ApmApplicationConfigView = ApmApplicationConfigView()
            self._ApmApplicationConfigView._deserialize(params.get("ApmApplicationConfigView"))
        self._RequestId = params.get("RequestId")


class DescribeGeneralMetricDataRequest(AbstractModel):
    r"""DescribeGeneralMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Metrics: 需要查询的指标名称，不可自定义输入，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type Metrics: list of str
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _ViewName: 视图名称，不可自定义输入。[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type ViewName: str
        :param _Filters: 要过滤的维度信息，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type Filters: list of GeneralFilter
        :param _GroupBy: 聚合维度，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :type GroupBy: list of str
        :param _StartTime: 起始时间的时间戳，支持查询30天内的指标数据。（单位：秒）
        :type StartTime: int
        :param _EndTime: 结束时间的时间戳，支持查询30天内的指标数据。（单位：秒）
        :type EndTime: int
        :param _Period: 是否按固定时间跨度聚合，填入1及大于1的值按1处理，不填按0处理。
- 填入0，则计算开始时间到截止时间的指标数据。
- 填入1，则会按照开始时间到截止时间的时间跨度选择聚合粒度：
 - 时间跨度 (0,12) 小时，则按一分钟粒度聚合。
 - 时间跨度 [12,48] 小时，则按五分钟粒度聚合。
 - 时间跨度 (48, +∞) 小时，则按一小时粒度聚合。
        :type Period: int
        :param _OrderBy: 对查询指标进行排序：
Key 填写云 API 指标名称，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
Value 填写排序方式：     
- asc：对查询指标进行升序排序
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
        r"""需要查询的指标名称，不可自定义输入，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: list of str
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ViewName(self):
        r"""视图名称，不可自定义输入。[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Filters(self):
        r"""要过滤的维度信息，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: list of GeneralFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def GroupBy(self):
        r"""聚合维度，不同视图有对应的指标维度，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def StartTime(self):
        r"""起始时间的时间戳，支持查询30天内的指标数据。（单位：秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间的时间戳，支持查询30天内的指标数据。（单位：秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""是否按固定时间跨度聚合，填入1及大于1的值按1处理，不填按0处理。
- 填入0，则计算开始时间到截止时间的指标数据。
- 填入1，则会按照开始时间到截止时间的时间跨度选择聚合粒度：
 - 时间跨度 (0,12) 小时，则按一分钟粒度聚合。
 - 时间跨度 [12,48] 小时，则按五分钟粒度聚合。
 - 时间跨度 (48, +∞) 小时，则按一小时粒度聚合。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def OrderBy(self):
        r"""对查询指标进行排序：
Key 填写云 API 指标名称，[详情请见。](https://cloud.tencent.com/document/product/248/101681)
Value 填写排序方式：     
- asc：对查询指标进行升序排序
- desc：对查询指标进行降序排序
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def PageSize(self):
        r"""查询指标的限制条数，目前最多展示50条数据，PageSize取值为1-50，上送PageSize则根据PageSize的值展示限制条数。
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
    r"""DescribeGeneralMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 指标结果集
        :type Records: list of Line
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._RequestId = None

    @property
    def Records(self):
        r"""指标结果集
        :rtype: list of Line
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = Line()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGeneralOTSpanListRequest(AbstractModel):
    r"""DescribeGeneralOTSpanList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _StartTime: Span 查询开始时间戳（单位：秒）
        :type StartTime: int
        :param _EndTime: Span 查询结束时间戳（单位：秒）
        :type EndTime: int
        :param _Filters: 通用过滤参数
        :type Filters: list of Filter
        :param _OrderBy: 排序
现支持的 Key 有：

- startTime(开始时间)
- endTime(结束时间)
- duration(响应时间)

现支持的 Value 有：

- desc(降序排序)
- asc(升序排序)
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: 业务自身服务名，控制台用户请填写taw
        :type BusinessName: str
        :param _Limit: 单页项目个数，默认为10000，合法取值范围为0～10000
        :type Limit: int
        :param _Offset: 分页
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._OrderBy = None
        self._BusinessName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Span 查询开始时间戳（单位：秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Span 查询结束时间戳（单位：秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""通用过滤参数
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""排序
现支持的 Key 有：

- startTime(开始时间)
- endTime(结束时间)
- duration(响应时间)

现支持的 Value 有：

- desc(降序排序)
- asc(升序排序)
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""业务自身服务名，控制台用户请填写taw
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Limit(self):
        r"""单页项目个数，默认为10000，合法取值范围为0～10000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._BusinessName = params.get("BusinessName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralOTSpanListResponse(AbstractModel):
    r"""DescribeGeneralOTSpanList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Spans: Spans字段中包含了链路数据的全部内容，由于数据经过了压缩，需要对结果进行如下三步转换，以还原始的文本。
1. 将Spans字段中的文本进行 Base64 解码，得到经过压缩后字节数组。
2. 使用 gzip 对压缩后的字节数组进行解压，得到压缩前的字节数组。
3. 使用 UTF-8 字符集，将压缩前的字节数组转换为文本。

        :type Spans: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Spans = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Spans(self):
        r"""Spans字段中包含了链路数据的全部内容，由于数据经过了压缩，需要对结果进行如下三步转换，以还原始的文本。
1. 将Spans字段中的文本进行 Base64 解码，得到经过压缩后字节数组。
2. 使用 gzip 对压缩后的字节数组进行解压，得到压缩前的字节数组。
3. 使用 UTF-8 字符集，将压缩前的字节数组转换为文本。

        :rtype: str
        """
        return self._Spans

    @Spans.setter
    def Spans(self, Spans):
        self._Spans = Spans

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
        self._Spans = params.get("Spans")
        self._RequestId = params.get("RequestId")


class DescribeGeneralSpanListRequest(AbstractModel):
    r"""DescribeGeneralSpanList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _StartTime: Span 查询开始时间戳（单位：秒）
        :type StartTime: int
        :param _EndTime: Span 查询结束时间戳（单位：秒）
        :type EndTime: int
        :param _Filters: 通用过滤参数
        :type Filters: list of Filter
        :param _OrderBy: 排序
现支持的 Key 有：

- startTime(开始时间)
- endTime(结束时间)
- duration(响应时间)

现支持的 Value 有：

- desc(降序排序)
- asc(升序排序)
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: 业务自身服务名，控制台用户请填写taw
        :type BusinessName: str
        :param _Limit: 单页项目个数，默认为10000，合法取值范围为0～10000
        :type Limit: int
        :param _Offset: 分页
        :type Offset: int
        """
        self._InstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._OrderBy = None
        self._BusinessName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StartTime(self):
        r"""Span 查询开始时间戳（单位：秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Span 查询结束时间戳（单位：秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""通用过滤参数
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""排序
现支持的 Key 有：

- startTime(开始时间)
- endTime(结束时间)
- duration(响应时间)

现支持的 Value 有：

- desc(降序排序)
- asc(升序排序)
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""业务自身服务名，控制台用户请填写taw
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Limit(self):
        r"""单页项目个数，默认为10000，合法取值范围为0～10000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._BusinessName = params.get("BusinessName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralSpanListResponse(AbstractModel):
    r"""DescribeGeneralSpanList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Spans: Span 分页列表
        :type Spans: list of Span
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Spans = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Spans(self):
        r"""Span 分页列表
        :rtype: list of Span
        """
        return self._Spans

    @Spans.setter
    def Spans(self, Spans):
        self._Spans = Spans

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
        if params.get("Spans") is not None:
            self._Spans = []
            for item in params.get("Spans"):
                obj = Span()
                obj._deserialize(item)
                self._Spans.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMetricRecordsRequest(AbstractModel):
    r"""DescribeMetricRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _Metrics: 指标列表
        :type Metrics: list of QueryMetricItem
        :param _StartTime: 开始时间（单位为秒）
        :type StartTime: int
        :param _EndTime: 结束时间（单位为秒）
        :type EndTime: int
        :param _GroupBy: 聚合维度
        :type GroupBy: list of str
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _OrFilters: Or 过滤条件
        :type OrFilters: list of Filter
        :param _OrderBy: 排序
现支持的 Key 有：

- startTime(开始时间)
- endTime(结束时间)
- duration(响应时间)

现支持的 Value 有：

- desc(降序排序)
- asc(升序排序)
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _BusinessName: 业务名称，控制台用户请填写taw。
        :type BusinessName: str
        :param _Type: 特殊处理查询结果
        :type Type: str
        :param _Limit: 每页大小，默认为1000，合法取值范围为0~1000
        :type Limit: int
        :param _Offset: 分页起始点
        :type Offset: int
        :param _PageIndex: 页码
        :type PageIndex: int
        :param _PageSize: 页长
        :type PageSize: int
        """
        self._InstanceId = None
        self._Metrics = None
        self._StartTime = None
        self._EndTime = None
        self._GroupBy = None
        self._Filters = None
        self._OrFilters = None
        self._OrderBy = None
        self._BusinessName = None
        self._Type = None
        self._Limit = None
        self._Offset = None
        self._PageIndex = None
        self._PageSize = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Metrics(self):
        r"""指标列表
        :rtype: list of QueryMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def StartTime(self):
        r"""开始时间（单位为秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（单位为秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def GroupBy(self):
        r"""聚合维度
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrFilters(self):
        r"""Or 过滤条件
        :rtype: list of Filter
        """
        return self._OrFilters

    @OrFilters.setter
    def OrFilters(self, OrFilters):
        self._OrFilters = OrFilters

    @property
    def OrderBy(self):
        r"""排序
现支持的 Key 有：

- startTime(开始时间)
- endTime(结束时间)
- duration(响应时间)

现支持的 Value 有：

- desc(降序排序)
- asc(升序排序)
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def BusinessName(self):
        r"""业务名称，控制台用户请填写taw。
        :rtype: str
        """
        return self._BusinessName

    @BusinessName.setter
    def BusinessName(self, BusinessName):
        self._BusinessName = BusinessName

    @property
    def Type(self):
        r"""特殊处理查询结果
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Limit(self):
        r"""每页大小，默认为1000，合法取值范围为0~1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页起始点
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def PageIndex(self):
        r"""页码
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        r"""页长
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._GroupBy = params.get("GroupBy")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrFilters") is not None:
            self._OrFilters = []
            for item in params.get("OrFilters"):
                obj = Filter()
                obj._deserialize(item)
                self._OrFilters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._BusinessName = params.get("BusinessName")
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMetricRecordsResponse(AbstractModel):
    r"""DescribeMetricRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 指标结果集
        :type Records: list of ApmMetricRecord
        :param _TotalCount: 查询指标结果集条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Records(self):
        r"""指标结果集
        :rtype: list of ApmMetricRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def TotalCount(self):
        r"""查询指标结果集条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeServiceOverviewRequest(AbstractModel):
    r"""DescribeServiceOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _Metrics: 指标列表
        :type Metrics: list of QueryMetricItem
        :param _StartTime: 开始时间（单位：秒）
        :type StartTime: int
        :param _EndTime: 结束时间（单位：秒）
        :type EndTime: int
        :param _GroupBy: 聚合维度
        :type GroupBy: list of str
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _OrderBy: 排序方式
Value 填写：
- asc：对查询指标进行升序排序
- desc：对查询指标进行降序排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param _Limit: 每页大小
        :type Limit: int
        :param _Offset: 分页起始点
        :type Offset: int
        """
        self._InstanceId = None
        self._Metrics = None
        self._StartTime = None
        self._EndTime = None
        self._GroupBy = None
        self._Filters = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Metrics(self):
        r"""指标列表
        :rtype: list of QueryMetricItem
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def StartTime(self):
        r"""开始时间（单位：秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（单位：秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def GroupBy(self):
        r"""聚合维度
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderBy(self):
        r"""排序方式
Value 填写：
- asc：对查询指标进行升序排序
- desc：对查询指标进行降序排序
        :rtype: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""每页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页起始点
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._GroupBy = params.get("GroupBy")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("OrderBy") is not None:
            self._OrderBy = OrderBy()
            self._OrderBy._deserialize(params.get("OrderBy"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceOverviewResponse(AbstractModel):
    r"""DescribeServiceOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 指标结果集
        :type Records: list of ApmMetricRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._RequestId = None

    @property
    def Records(self):
        r"""指标结果集
        :rtype: list of ApmMetricRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    r"""DescribeTagValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _TagKey: 维度名
        :type TagKey: str
        :param _StartTime: 开始时间（单位为秒）
        :type StartTime: int
        :param _EndTime: 结束时间（单位为秒）
        :type EndTime: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _OrFilters: Or 过滤条件
        :type OrFilters: list of Filter
        :param _Type: 使用类型
        :type Type: str
        """
        self._InstanceId = None
        self._TagKey = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._OrFilters = None
        self._Type = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TagKey(self):
        r"""维度名
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def StartTime(self):
        r"""开始时间（单位为秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（单位为秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrFilters(self):
        r"""Or 过滤条件
        :rtype: list of Filter
        """
        return self._OrFilters

    @OrFilters.setter
    def OrFilters(self, OrFilters):
        self._OrFilters = OrFilters

    @property
    def Type(self):
        r"""使用类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TagKey = params.get("TagKey")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
    r"""DescribeTagValues返回参数结构体

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
        r"""维度值列表
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

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
        self._Values = params.get("Values")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""查询过滤参数

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
        r"""过滤方式（=, !=, in）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        r"""过滤维度名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""过滤值，in过滤方式用逗号分割多个值
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
    r"""查询过滤参数

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
        r"""过滤维度名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""过滤值
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
    r"""组件

    """

    def __init__(self):
        r"""
        :param _Name: 组件名称
        :type Name: str
        :param _Enable: 组件开关
        :type Enable: bool
        """
        self._Name = None
        self._Enable = None

    @property
    def Name(self):
        r"""组件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enable(self):
        r"""组件开关
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
    r"""指标曲线数据

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
        :type DataSerial: list of float
        :param _Tags: 维度列表
        :type Tags: list of ApmTag
        :param _MetricUnit: 指标数据单位
        :type MetricUnit: str
        """
        self._MetricName = None
        self._MetricNameCN = None
        self._TimeSerial = None
        self._DataSerial = None
        self._Tags = None
        self._MetricUnit = None

    @property
    def MetricName(self):
        r"""指标名
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricNameCN(self):
        r"""指标中文名
        :rtype: str
        """
        return self._MetricNameCN

    @MetricNameCN.setter
    def MetricNameCN(self, MetricNameCN):
        self._MetricNameCN = MetricNameCN

    @property
    def TimeSerial(self):
        r"""时间序列
        :rtype: list of int
        """
        return self._TimeSerial

    @TimeSerial.setter
    def TimeSerial(self, TimeSerial):
        self._TimeSerial = TimeSerial

    @property
    def DataSerial(self):
        r"""数据序列
        :rtype: list of float
        """
        return self._DataSerial

    @DataSerial.setter
    def DataSerial(self, DataSerial):
        self._DataSerial = DataSerial

    @property
    def Tags(self):
        r"""维度列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MetricUnit(self):
        r"""指标数据单位
        :rtype: str
        """
        return self._MetricUnit

    @MetricUnit.setter
    def MetricUnit(self, MetricUnit):
        self._MetricUnit = MetricUnit


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
        self._MetricUnit = params.get("MetricUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmApplicationConfigRequest(AbstractModel):
    r"""ModifyApmApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _ServiceName: 应用名
        :type ServiceName: str
        :param _UrlConvergenceSwitch: URL收敛开关,0 关 | 1 开
        :type UrlConvergenceSwitch: int
        :param _UrlConvergenceThreshold: URL收敛阈值
        :type UrlConvergenceThreshold: int
        :param _ExceptionFilter: 异常过滤正则规则，逗号分隔
        :type ExceptionFilter: str
        :param _UrlConvergence: URL收敛正则规则，逗号分隔
        :type UrlConvergence: str
        :param _ErrorCodeFilter: 错误码过滤，逗号分隔
        :type ErrorCodeFilter: str
        :param _UrlExclude: URL排除正则规则，逗号分隔
        :type UrlExclude: str
        :param _IsRelatedLog: 日志开关 0 关 1 开
        :type IsRelatedLog: int
        :param _LogRegion: 日志地域
        :type LogRegion: str
        :param _LogTopicID: 日志主题ID
        :type LogTopicID: str
        :param _LogSet: CLS 日志集 | ES 集群ID
        :type LogSet: str
        :param _LogSource: 日志来源 CLS | ES
        :type LogSource: str
        :param _IgnoreOperationName: 需过滤的接口
        :type IgnoreOperationName: str
        :param _EnableSnapshot: 是否开启线程剖析
        :type EnableSnapshot: bool
        :param _SnapshotTimeout: 线程剖析超时阈值
        :type SnapshotTimeout: int
        :param _AgentEnable: 是否开启agent
        :type AgentEnable: bool
        :param _TraceSquash: 是否开启链路压缩
        :type TraceSquash: bool
        :param _EventEnable: 是否开启应用诊断的开关
        :type EventEnable: bool
        :param _InstrumentList: 组件列表
        :type InstrumentList: list of Instrument
        :param _AgentOperationConfigView: 探针接口相关配置
        :type AgentOperationConfigView: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        :param _EnableLogConfig: 是否开启应用日志配置
        :type EnableLogConfig: bool
        :param _EnableDashboardConfig: 应用是否开启dashboard配置： false 关（与业务系统保持一致）/true 开（应用级配置）
        :type EnableDashboardConfig: bool
        :param _IsRelatedDashboard: 是否关联dashboard： 0 关 1 开
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: dashboard ID
        :type DashboardTopicID: str
        :param _LogIndexType: CLS索引类型(0=全文索引，1=键值索引)
        :type LogIndexType: int
        :param _LogTraceIdKey: traceId的索引key: 当CLS索引类型为键值索引时生效
        :type LogTraceIdKey: str
        :param _EnableSecurityConfig: 是否开启应用安全配置
        :type EnableSecurityConfig: bool
        :param _IsSqlInjectionAnalysis: 是否开启SQL注入分析
        :type IsSqlInjectionAnalysis: int
        :param _IsInstrumentationVulnerabilityScan: 是否开启组件漏洞检测
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsRemoteCommandExecutionAnalysis: 是否开启远程命令检测
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: 是否开启内存马检测
        :type IsMemoryHijackingAnalysis: int
        :param _IsDeleteAnyFileAnalysis: 是否开启删除任意文件检测（0-关闭，1-开启）
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: 是否开启读取任意文件检测（0-关闭，1-开启）
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: 是否开启上传任意文件检测（0-关闭，1-开启）
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: 是否开启包含任意文件检测（0-关闭，1-开启）
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: 是否开启目录遍历检测（0-关闭，1-开启）
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: 是否开启模板引擎注入检测（0-关闭，1-开启）
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: 是否开启脚本引擎注入检测（0-关闭，1-开启）
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: 是否开启表达式注入检测（0-关闭，1-开启）
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: 是否开启JNDI注入检测（0-关闭，1-开启）
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: 是否开启JNI注入检测（0-关闭，1-开启）
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: 是否开启Webshell后门检测（0-关闭，1-开启）
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: 是否开启反序列化检测（0-关闭，1-开启）
        :type IsDeserializationAnalysis: int
        :param _UrlAutoConvergenceEnable: 接口自动收敛开关,0 关 | 1 开
        :type UrlAutoConvergenceEnable: bool
        :param _UrlLongSegmentThreshold: URL长分段收敛阈值
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: URL数字分段收敛阈值
        :type UrlNumberSegmentThreshold: int
        :param _DisableMemoryUsed: 探针熔断内存阈值
        :type DisableMemoryUsed: int
        :param _DisableCpuUsed: 探针熔断CPU阈值
        :type DisableCpuUsed: int
        """
        self._InstanceId = None
        self._ServiceName = None
        self._UrlConvergenceSwitch = None
        self._UrlConvergenceThreshold = None
        self._ExceptionFilter = None
        self._UrlConvergence = None
        self._ErrorCodeFilter = None
        self._UrlExclude = None
        self._IsRelatedLog = None
        self._LogRegion = None
        self._LogTopicID = None
        self._LogSet = None
        self._LogSource = None
        self._IgnoreOperationName = None
        self._EnableSnapshot = None
        self._SnapshotTimeout = None
        self._AgentEnable = None
        self._TraceSquash = None
        self._EventEnable = None
        self._InstrumentList = None
        self._AgentOperationConfigView = None
        self._EnableLogConfig = None
        self._EnableDashboardConfig = None
        self._IsRelatedDashboard = None
        self._DashboardTopicID = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._EnableSecurityConfig = None
        self._IsSqlInjectionAnalysis = None
        self._IsInstrumentationVulnerabilityScan = None
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._UrlAutoConvergenceEnable = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None
        self._DisableMemoryUsed = None
        self._DisableCpuUsed = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""应用名
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UrlConvergenceSwitch(self):
        r"""URL收敛开关,0 关 | 1 开
        :rtype: int
        """
        return self._UrlConvergenceSwitch

    @UrlConvergenceSwitch.setter
    def UrlConvergenceSwitch(self, UrlConvergenceSwitch):
        self._UrlConvergenceSwitch = UrlConvergenceSwitch

    @property
    def UrlConvergenceThreshold(self):
        r"""URL收敛阈值
        :rtype: int
        """
        return self._UrlConvergenceThreshold

    @UrlConvergenceThreshold.setter
    def UrlConvergenceThreshold(self, UrlConvergenceThreshold):
        self._UrlConvergenceThreshold = UrlConvergenceThreshold

    @property
    def ExceptionFilter(self):
        r"""异常过滤正则规则，逗号分隔
        :rtype: str
        """
        return self._ExceptionFilter

    @ExceptionFilter.setter
    def ExceptionFilter(self, ExceptionFilter):
        self._ExceptionFilter = ExceptionFilter

    @property
    def UrlConvergence(self):
        r"""URL收敛正则规则，逗号分隔
        :rtype: str
        """
        return self._UrlConvergence

    @UrlConvergence.setter
    def UrlConvergence(self, UrlConvergence):
        self._UrlConvergence = UrlConvergence

    @property
    def ErrorCodeFilter(self):
        r"""错误码过滤，逗号分隔
        :rtype: str
        """
        return self._ErrorCodeFilter

    @ErrorCodeFilter.setter
    def ErrorCodeFilter(self, ErrorCodeFilter):
        self._ErrorCodeFilter = ErrorCodeFilter

    @property
    def UrlExclude(self):
        r"""URL排除正则规则，逗号分隔
        :rtype: str
        """
        return self._UrlExclude

    @UrlExclude.setter
    def UrlExclude(self, UrlExclude):
        self._UrlExclude = UrlExclude

    @property
    def IsRelatedLog(self):
        r"""日志开关 0 关 1 开
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogRegion(self):
        r"""日志地域
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogTopicID(self):
        r"""日志主题ID
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def LogSet(self):
        r"""CLS 日志集 | ES 集群ID
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogSource(self):
        r"""日志来源 CLS | ES
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def IgnoreOperationName(self):
        r"""需过滤的接口
        :rtype: str
        """
        return self._IgnoreOperationName

    @IgnoreOperationName.setter
    def IgnoreOperationName(self, IgnoreOperationName):
        self._IgnoreOperationName = IgnoreOperationName

    @property
    def EnableSnapshot(self):
        r"""是否开启线程剖析
        :rtype: bool
        """
        return self._EnableSnapshot

    @EnableSnapshot.setter
    def EnableSnapshot(self, EnableSnapshot):
        self._EnableSnapshot = EnableSnapshot

    @property
    def SnapshotTimeout(self):
        r"""线程剖析超时阈值
        :rtype: int
        """
        return self._SnapshotTimeout

    @SnapshotTimeout.setter
    def SnapshotTimeout(self, SnapshotTimeout):
        self._SnapshotTimeout = SnapshotTimeout

    @property
    def AgentEnable(self):
        r"""是否开启agent
        :rtype: bool
        """
        return self._AgentEnable

    @AgentEnable.setter
    def AgentEnable(self, AgentEnable):
        self._AgentEnable = AgentEnable

    @property
    def TraceSquash(self):
        r"""是否开启链路压缩
        :rtype: bool
        """
        return self._TraceSquash

    @TraceSquash.setter
    def TraceSquash(self, TraceSquash):
        self._TraceSquash = TraceSquash

    @property
    def EventEnable(self):
        r"""是否开启应用诊断的开关
        :rtype: bool
        """
        return self._EventEnable

    @EventEnable.setter
    def EventEnable(self, EventEnable):
        self._EventEnable = EventEnable

    @property
    def InstrumentList(self):
        r"""组件列表
        :rtype: list of Instrument
        """
        return self._InstrumentList

    @InstrumentList.setter
    def InstrumentList(self, InstrumentList):
        self._InstrumentList = InstrumentList

    @property
    def AgentOperationConfigView(self):
        r"""探针接口相关配置
        :rtype: :class:`tencentcloud.apm.v20210622.models.AgentOperationConfigView`
        """
        return self._AgentOperationConfigView

    @AgentOperationConfigView.setter
    def AgentOperationConfigView(self, AgentOperationConfigView):
        self._AgentOperationConfigView = AgentOperationConfigView

    @property
    def EnableLogConfig(self):
        r"""是否开启应用日志配置
        :rtype: bool
        """
        return self._EnableLogConfig

    @EnableLogConfig.setter
    def EnableLogConfig(self, EnableLogConfig):
        self._EnableLogConfig = EnableLogConfig

    @property
    def EnableDashboardConfig(self):
        r"""应用是否开启dashboard配置： false 关（与业务系统保持一致）/true 开（应用级配置）
        :rtype: bool
        """
        return self._EnableDashboardConfig

    @EnableDashboardConfig.setter
    def EnableDashboardConfig(self, EnableDashboardConfig):
        self._EnableDashboardConfig = EnableDashboardConfig

    @property
    def IsRelatedDashboard(self):
        r"""是否关联dashboard： 0 关 1 开
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""dashboard ID
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def LogIndexType(self):
        r"""CLS索引类型(0=全文索引，1=键值索引)
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""traceId的索引key: 当CLS索引类型为键值索引时生效
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def EnableSecurityConfig(self):
        r"""是否开启应用安全配置
        :rtype: bool
        """
        return self._EnableSecurityConfig

    @EnableSecurityConfig.setter
    def EnableSecurityConfig(self, EnableSecurityConfig):
        self._EnableSecurityConfig = EnableSecurityConfig

    @property
    def IsSqlInjectionAnalysis(self):
        r"""是否开启SQL注入分析
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""是否开启组件漏洞检测
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""是否开启远程命令检测
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""是否开启内存马检测
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""是否开启删除任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""是否开启读取任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""是否开启上传任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""是否开启包含任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""是否开启目录遍历检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""是否开启模板引擎注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""是否开启脚本引擎注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""是否开启表达式注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""是否开启JNDI注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""是否开启JNI注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""是否开启Webshell后门检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""是否开启反序列化检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlAutoConvergenceEnable(self):
        r"""接口自动收敛开关,0 关 | 1 开
        :rtype: bool
        """
        return self._UrlAutoConvergenceEnable

    @UrlAutoConvergenceEnable.setter
    def UrlAutoConvergenceEnable(self, UrlAutoConvergenceEnable):
        self._UrlAutoConvergenceEnable = UrlAutoConvergenceEnable

    @property
    def UrlLongSegmentThreshold(self):
        r"""URL长分段收敛阈值
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""URL数字分段收敛阈值
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold

    @property
    def DisableMemoryUsed(self):
        r"""探针熔断内存阈值
        :rtype: int
        """
        return self._DisableMemoryUsed

    @DisableMemoryUsed.setter
    def DisableMemoryUsed(self, DisableMemoryUsed):
        self._DisableMemoryUsed = DisableMemoryUsed

    @property
    def DisableCpuUsed(self):
        r"""探针熔断CPU阈值
        :rtype: int
        """
        return self._DisableCpuUsed

    @DisableCpuUsed.setter
    def DisableCpuUsed(self, DisableCpuUsed):
        self._DisableCpuUsed = DisableCpuUsed


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        self._UrlConvergenceSwitch = params.get("UrlConvergenceSwitch")
        self._UrlConvergenceThreshold = params.get("UrlConvergenceThreshold")
        self._ExceptionFilter = params.get("ExceptionFilter")
        self._UrlConvergence = params.get("UrlConvergence")
        self._ErrorCodeFilter = params.get("ErrorCodeFilter")
        self._UrlExclude = params.get("UrlExclude")
        self._IsRelatedLog = params.get("IsRelatedLog")
        self._LogRegion = params.get("LogRegion")
        self._LogTopicID = params.get("LogTopicID")
        self._LogSet = params.get("LogSet")
        self._LogSource = params.get("LogSource")
        self._IgnoreOperationName = params.get("IgnoreOperationName")
        self._EnableSnapshot = params.get("EnableSnapshot")
        self._SnapshotTimeout = params.get("SnapshotTimeout")
        self._AgentEnable = params.get("AgentEnable")
        self._TraceSquash = params.get("TraceSquash")
        self._EventEnable = params.get("EventEnable")
        if params.get("InstrumentList") is not None:
            self._InstrumentList = []
            for item in params.get("InstrumentList"):
                obj = Instrument()
                obj._deserialize(item)
                self._InstrumentList.append(obj)
        if params.get("AgentOperationConfigView") is not None:
            self._AgentOperationConfigView = AgentOperationConfigView()
            self._AgentOperationConfigView._deserialize(params.get("AgentOperationConfigView"))
        self._EnableLogConfig = params.get("EnableLogConfig")
        self._EnableDashboardConfig = params.get("EnableDashboardConfig")
        self._IsRelatedDashboard = params.get("IsRelatedDashboard")
        self._DashboardTopicID = params.get("DashboardTopicID")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._EnableSecurityConfig = params.get("EnableSecurityConfig")
        self._IsSqlInjectionAnalysis = params.get("IsSqlInjectionAnalysis")
        self._IsInstrumentationVulnerabilityScan = params.get("IsInstrumentationVulnerabilityScan")
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._UrlAutoConvergenceEnable = params.get("UrlAutoConvergenceEnable")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        self._DisableMemoryUsed = params.get("DisableMemoryUsed")
        self._DisableCpuUsed = params.get("DisableCpuUsed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmApplicationConfigResponse(AbstractModel):
    r"""ModifyApmApplicationConfig返回参数结构体

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


class ModifyApmAssociationRequest(AbstractModel):
    r"""ModifyApmAssociation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 关联的产品名，当前只支持Prometheus
        :type ProductName: str
        :param _Status: 关联关系的状态：// 关联关系状态：1（启用）、2（不启用）、4（已删除）
        :type Status: int
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _PeerId: 关联的产品实例ID
        :type PeerId: str
        :param _Topic: CKafka消息主题
        :type Topic: str
        """
        self._ProductName = None
        self._Status = None
        self._InstanceId = None
        self._PeerId = None
        self._Topic = None

    @property
    def ProductName(self):
        r"""关联的产品名，当前只支持Prometheus
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Status(self):
        r"""关联关系的状态：// 关联关系状态：1（启用）、2（不启用）、4（已删除）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PeerId(self):
        r"""关联的产品实例ID
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def Topic(self):
        r"""CKafka消息主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._Status = params.get("Status")
        self._InstanceId = params.get("InstanceId")
        self._PeerId = params.get("PeerId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmAssociationResponse(AbstractModel):
    r"""ModifyApmAssociation返回参数结构体

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


class ModifyApmInstanceRequest(AbstractModel):
    r"""ModifyApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统 ID
        :type InstanceId: str
        :param _Name: 业务系统名
        :type Name: str
        :param _Tags: Tag 列表
        :type Tags: list of ApmTag
        :param _Description: 业务系统描述
        :type Description: str
        :param _TraceDuration: Trace 数据保存时长（单位：天）
        :type TraceDuration: int
        :param _OpenBilling: 是否开启计费
        :type OpenBilling: bool
        :param _SpanDailyCounters: 业务系统上报额度
        :type SpanDailyCounters: int
        :param _ErrRateThreshold: 错误率警示线，当应用的平均错误率超出该阈值时，系统会给出异常提示。
        :type ErrRateThreshold: int
        :param _SampleRate: 采样率（单位：%）
        :type SampleRate: int
        :param _ErrorSample: 是否开启错误采样（0=关, 1=开）
        :type ErrorSample: int
        :param _SlowRequestSavedThreshold: 采样慢调用保存阈值（单位：ms）
        :type SlowRequestSavedThreshold: int
        :param _IsRelatedLog: 是否开启日志功能（0=关, 1=开）
        :type IsRelatedLog: int
        :param _LogRegion: 日志地域，开启日志功能后才会生效
        :type LogRegion: str
        :param _LogTopicID: CLS 日志主题 ID，开启日志功能后才会生效
        :type LogTopicID: str
        :param _LogSet: 日志集，开启日志功能后才会生效
        :type LogSet: str
        :param _LogSource: 日志源，开启日志功能后才会生效
        :type LogSource: str
        :param _CustomShowTags: 用户自定义展示标签列表
        :type CustomShowTags: list of str
        :param _PayMode: 修改计费模式（1为预付费，0为按量付费）
        :type PayMode: int
        :param _ResponseDurationWarningThreshold: 响应时间警示线
        :type ResponseDurationWarningThreshold: int
        :param _Free: 是否免费（0=付费版；1=TSF 受限免费版；2=免费版），默认0
        :type Free: int
        :param _IsRelatedDashboard: 是否关联 Dashboard（0=关,1=开）
        :type IsRelatedDashboard: int
        :param _DashboardTopicID: 关联的 Dashboard ID，开启关联 Dashboard 后才会生效
        :type DashboardTopicID: str
        :param _IsSqlInjectionAnalysis: 是否开启 SQL 注入检测（0=关,1=开）
        :type IsSqlInjectionAnalysis: int
        :param _IsInstrumentationVulnerabilityScan: 是否开启组件漏洞检测（0=关,1=开）
        :type IsInstrumentationVulnerabilityScan: int
        :param _IsRemoteCommandExecutionAnalysis: 是否开启远程命令攻击检测
        :type IsRemoteCommandExecutionAnalysis: int
        :param _IsMemoryHijackingAnalysis: 是否开启内存马检测
        :type IsMemoryHijackingAnalysis: int
        :param _LogIndexType: CLS索引类型(0=全文索引，1=键值索引)
        :type LogIndexType: int
        :param _LogTraceIdKey: traceId的索引key: 当CLS索引类型为键值索引时生效
        :type LogTraceIdKey: str
        :param _IsDeleteAnyFileAnalysis: 是否开启删除任意文件检测（0-关闭，1-开启）
        :type IsDeleteAnyFileAnalysis: int
        :param _IsReadAnyFileAnalysis: 是否开启读取任意文件检测（0-关闭，1-开启）
        :type IsReadAnyFileAnalysis: int
        :param _IsUploadAnyFileAnalysis: 是否开启上传任意文件检测（0-关闭，1-开启）
        :type IsUploadAnyFileAnalysis: int
        :param _IsIncludeAnyFileAnalysis: 是否开启包含任意文件检测（0-关闭，1-开启）
        :type IsIncludeAnyFileAnalysis: int
        :param _IsDirectoryTraversalAnalysis: 是否开启目录遍历检测（0-关闭，1-开启）
        :type IsDirectoryTraversalAnalysis: int
        :param _IsTemplateEngineInjectionAnalysis: 是否开启模板引擎注入检测（0-关闭，1-开启）
        :type IsTemplateEngineInjectionAnalysis: int
        :param _IsScriptEngineInjectionAnalysis: 是否开启脚本引擎注入检测（0-关闭，1-开启）
        :type IsScriptEngineInjectionAnalysis: int
        :param _IsExpressionInjectionAnalysis: 是否开启表达式注入检测（0-关闭，1-开启）
        :type IsExpressionInjectionAnalysis: int
        :param _IsJNDIInjectionAnalysis: 是否开启JNDI注入检测（0-关闭，1-开启）
        :type IsJNDIInjectionAnalysis: int
        :param _IsJNIInjectionAnalysis: 是否开启JNI注入检测（0-关闭，1-开启）
        :type IsJNIInjectionAnalysis: int
        :param _IsWebshellBackdoorAnalysis: 是否开启Webshell后门检测（0-关闭，1-开启）
        :type IsWebshellBackdoorAnalysis: int
        :param _IsDeserializationAnalysis: 是否开启反序列化检测（0-关闭，1-开启）
        :type IsDeserializationAnalysis: int
        :param _UrlLongSegmentThreshold: URL长分段收敛阈值
        :type UrlLongSegmentThreshold: int
        :param _UrlNumberSegmentThreshold: URL数字分段收敛阈值
        :type UrlNumberSegmentThreshold: int
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
        self._IsRemoteCommandExecutionAnalysis = None
        self._IsMemoryHijackingAnalysis = None
        self._LogIndexType = None
        self._LogTraceIdKey = None
        self._IsDeleteAnyFileAnalysis = None
        self._IsReadAnyFileAnalysis = None
        self._IsUploadAnyFileAnalysis = None
        self._IsIncludeAnyFileAnalysis = None
        self._IsDirectoryTraversalAnalysis = None
        self._IsTemplateEngineInjectionAnalysis = None
        self._IsScriptEngineInjectionAnalysis = None
        self._IsExpressionInjectionAnalysis = None
        self._IsJNDIInjectionAnalysis = None
        self._IsJNIInjectionAnalysis = None
        self._IsWebshellBackdoorAnalysis = None
        self._IsDeserializationAnalysis = None
        self._UrlLongSegmentThreshold = None
        self._UrlNumberSegmentThreshold = None

    @property
    def InstanceId(self):
        r"""业务系统 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""业务系统名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        r"""Tag 列表
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        r"""业务系统描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def TraceDuration(self):
        r"""Trace 数据保存时长（单位：天）
        :rtype: int
        """
        return self._TraceDuration

    @TraceDuration.setter
    def TraceDuration(self, TraceDuration):
        self._TraceDuration = TraceDuration

    @property
    def OpenBilling(self):
        r"""是否开启计费
        :rtype: bool
        """
        return self._OpenBilling

    @OpenBilling.setter
    def OpenBilling(self, OpenBilling):
        self._OpenBilling = OpenBilling

    @property
    def SpanDailyCounters(self):
        r"""业务系统上报额度
        :rtype: int
        """
        return self._SpanDailyCounters

    @SpanDailyCounters.setter
    def SpanDailyCounters(self, SpanDailyCounters):
        self._SpanDailyCounters = SpanDailyCounters

    @property
    def ErrRateThreshold(self):
        r"""错误率警示线，当应用的平均错误率超出该阈值时，系统会给出异常提示。
        :rtype: int
        """
        return self._ErrRateThreshold

    @ErrRateThreshold.setter
    def ErrRateThreshold(self, ErrRateThreshold):
        self._ErrRateThreshold = ErrRateThreshold

    @property
    def SampleRate(self):
        r"""采样率（单位：%）
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ErrorSample(self):
        r"""是否开启错误采样（0=关, 1=开）
        :rtype: int
        """
        return self._ErrorSample

    @ErrorSample.setter
    def ErrorSample(self, ErrorSample):
        self._ErrorSample = ErrorSample

    @property
    def SlowRequestSavedThreshold(self):
        r"""采样慢调用保存阈值（单位：ms）
        :rtype: int
        """
        return self._SlowRequestSavedThreshold

    @SlowRequestSavedThreshold.setter
    def SlowRequestSavedThreshold(self, SlowRequestSavedThreshold):
        self._SlowRequestSavedThreshold = SlowRequestSavedThreshold

    @property
    def IsRelatedLog(self):
        r"""是否开启日志功能（0=关, 1=开）
        :rtype: int
        """
        return self._IsRelatedLog

    @IsRelatedLog.setter
    def IsRelatedLog(self, IsRelatedLog):
        self._IsRelatedLog = IsRelatedLog

    @property
    def LogRegion(self):
        r"""日志地域，开启日志功能后才会生效
        :rtype: str
        """
        return self._LogRegion

    @LogRegion.setter
    def LogRegion(self, LogRegion):
        self._LogRegion = LogRegion

    @property
    def LogTopicID(self):
        r"""CLS 日志主题 ID，开启日志功能后才会生效
        :rtype: str
        """
        return self._LogTopicID

    @LogTopicID.setter
    def LogTopicID(self, LogTopicID):
        self._LogTopicID = LogTopicID

    @property
    def LogSet(self):
        r"""日志集，开启日志功能后才会生效
        :rtype: str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def LogSource(self):
        r"""日志源，开启日志功能后才会生效
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def CustomShowTags(self):
        r"""用户自定义展示标签列表
        :rtype: list of str
        """
        return self._CustomShowTags

    @CustomShowTags.setter
    def CustomShowTags(self, CustomShowTags):
        self._CustomShowTags = CustomShowTags

    @property
    def PayMode(self):
        r"""修改计费模式（1为预付费，0为按量付费）
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ResponseDurationWarningThreshold(self):
        r"""响应时间警示线
        :rtype: int
        """
        return self._ResponseDurationWarningThreshold

    @ResponseDurationWarningThreshold.setter
    def ResponseDurationWarningThreshold(self, ResponseDurationWarningThreshold):
        self._ResponseDurationWarningThreshold = ResponseDurationWarningThreshold

    @property
    def Free(self):
        r"""是否免费（0=付费版；1=TSF 受限免费版；2=免费版），默认0
        :rtype: int
        """
        return self._Free

    @Free.setter
    def Free(self, Free):
        self._Free = Free

    @property
    def IsRelatedDashboard(self):
        r"""是否关联 Dashboard（0=关,1=开）
        :rtype: int
        """
        return self._IsRelatedDashboard

    @IsRelatedDashboard.setter
    def IsRelatedDashboard(self, IsRelatedDashboard):
        self._IsRelatedDashboard = IsRelatedDashboard

    @property
    def DashboardTopicID(self):
        r"""关联的 Dashboard ID，开启关联 Dashboard 后才会生效
        :rtype: str
        """
        return self._DashboardTopicID

    @DashboardTopicID.setter
    def DashboardTopicID(self, DashboardTopicID):
        self._DashboardTopicID = DashboardTopicID

    @property
    def IsSqlInjectionAnalysis(self):
        r"""是否开启 SQL 注入检测（0=关,1=开）
        :rtype: int
        """
        return self._IsSqlInjectionAnalysis

    @IsSqlInjectionAnalysis.setter
    def IsSqlInjectionAnalysis(self, IsSqlInjectionAnalysis):
        self._IsSqlInjectionAnalysis = IsSqlInjectionAnalysis

    @property
    def IsInstrumentationVulnerabilityScan(self):
        r"""是否开启组件漏洞检测（0=关,1=开）
        :rtype: int
        """
        return self._IsInstrumentationVulnerabilityScan

    @IsInstrumentationVulnerabilityScan.setter
    def IsInstrumentationVulnerabilityScan(self, IsInstrumentationVulnerabilityScan):
        self._IsInstrumentationVulnerabilityScan = IsInstrumentationVulnerabilityScan

    @property
    def IsRemoteCommandExecutionAnalysis(self):
        r"""是否开启远程命令攻击检测
        :rtype: int
        """
        return self._IsRemoteCommandExecutionAnalysis

    @IsRemoteCommandExecutionAnalysis.setter
    def IsRemoteCommandExecutionAnalysis(self, IsRemoteCommandExecutionAnalysis):
        self._IsRemoteCommandExecutionAnalysis = IsRemoteCommandExecutionAnalysis

    @property
    def IsMemoryHijackingAnalysis(self):
        r"""是否开启内存马检测
        :rtype: int
        """
        return self._IsMemoryHijackingAnalysis

    @IsMemoryHijackingAnalysis.setter
    def IsMemoryHijackingAnalysis(self, IsMemoryHijackingAnalysis):
        self._IsMemoryHijackingAnalysis = IsMemoryHijackingAnalysis

    @property
    def LogIndexType(self):
        r"""CLS索引类型(0=全文索引，1=键值索引)
        :rtype: int
        """
        return self._LogIndexType

    @LogIndexType.setter
    def LogIndexType(self, LogIndexType):
        self._LogIndexType = LogIndexType

    @property
    def LogTraceIdKey(self):
        r"""traceId的索引key: 当CLS索引类型为键值索引时生效
        :rtype: str
        """
        return self._LogTraceIdKey

    @LogTraceIdKey.setter
    def LogTraceIdKey(self, LogTraceIdKey):
        self._LogTraceIdKey = LogTraceIdKey

    @property
    def IsDeleteAnyFileAnalysis(self):
        r"""是否开启删除任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDeleteAnyFileAnalysis

    @IsDeleteAnyFileAnalysis.setter
    def IsDeleteAnyFileAnalysis(self, IsDeleteAnyFileAnalysis):
        self._IsDeleteAnyFileAnalysis = IsDeleteAnyFileAnalysis

    @property
    def IsReadAnyFileAnalysis(self):
        r"""是否开启读取任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsReadAnyFileAnalysis

    @IsReadAnyFileAnalysis.setter
    def IsReadAnyFileAnalysis(self, IsReadAnyFileAnalysis):
        self._IsReadAnyFileAnalysis = IsReadAnyFileAnalysis

    @property
    def IsUploadAnyFileAnalysis(self):
        r"""是否开启上传任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsUploadAnyFileAnalysis

    @IsUploadAnyFileAnalysis.setter
    def IsUploadAnyFileAnalysis(self, IsUploadAnyFileAnalysis):
        self._IsUploadAnyFileAnalysis = IsUploadAnyFileAnalysis

    @property
    def IsIncludeAnyFileAnalysis(self):
        r"""是否开启包含任意文件检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsIncludeAnyFileAnalysis

    @IsIncludeAnyFileAnalysis.setter
    def IsIncludeAnyFileAnalysis(self, IsIncludeAnyFileAnalysis):
        self._IsIncludeAnyFileAnalysis = IsIncludeAnyFileAnalysis

    @property
    def IsDirectoryTraversalAnalysis(self):
        r"""是否开启目录遍历检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDirectoryTraversalAnalysis

    @IsDirectoryTraversalAnalysis.setter
    def IsDirectoryTraversalAnalysis(self, IsDirectoryTraversalAnalysis):
        self._IsDirectoryTraversalAnalysis = IsDirectoryTraversalAnalysis

    @property
    def IsTemplateEngineInjectionAnalysis(self):
        r"""是否开启模板引擎注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsTemplateEngineInjectionAnalysis

    @IsTemplateEngineInjectionAnalysis.setter
    def IsTemplateEngineInjectionAnalysis(self, IsTemplateEngineInjectionAnalysis):
        self._IsTemplateEngineInjectionAnalysis = IsTemplateEngineInjectionAnalysis

    @property
    def IsScriptEngineInjectionAnalysis(self):
        r"""是否开启脚本引擎注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsScriptEngineInjectionAnalysis

    @IsScriptEngineInjectionAnalysis.setter
    def IsScriptEngineInjectionAnalysis(self, IsScriptEngineInjectionAnalysis):
        self._IsScriptEngineInjectionAnalysis = IsScriptEngineInjectionAnalysis

    @property
    def IsExpressionInjectionAnalysis(self):
        r"""是否开启表达式注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsExpressionInjectionAnalysis

    @IsExpressionInjectionAnalysis.setter
    def IsExpressionInjectionAnalysis(self, IsExpressionInjectionAnalysis):
        self._IsExpressionInjectionAnalysis = IsExpressionInjectionAnalysis

    @property
    def IsJNDIInjectionAnalysis(self):
        r"""是否开启JNDI注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsJNDIInjectionAnalysis

    @IsJNDIInjectionAnalysis.setter
    def IsJNDIInjectionAnalysis(self, IsJNDIInjectionAnalysis):
        self._IsJNDIInjectionAnalysis = IsJNDIInjectionAnalysis

    @property
    def IsJNIInjectionAnalysis(self):
        r"""是否开启JNI注入检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsJNIInjectionAnalysis

    @IsJNIInjectionAnalysis.setter
    def IsJNIInjectionAnalysis(self, IsJNIInjectionAnalysis):
        self._IsJNIInjectionAnalysis = IsJNIInjectionAnalysis

    @property
    def IsWebshellBackdoorAnalysis(self):
        r"""是否开启Webshell后门检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsWebshellBackdoorAnalysis

    @IsWebshellBackdoorAnalysis.setter
    def IsWebshellBackdoorAnalysis(self, IsWebshellBackdoorAnalysis):
        self._IsWebshellBackdoorAnalysis = IsWebshellBackdoorAnalysis

    @property
    def IsDeserializationAnalysis(self):
        r"""是否开启反序列化检测（0-关闭，1-开启）
        :rtype: int
        """
        return self._IsDeserializationAnalysis

    @IsDeserializationAnalysis.setter
    def IsDeserializationAnalysis(self, IsDeserializationAnalysis):
        self._IsDeserializationAnalysis = IsDeserializationAnalysis

    @property
    def UrlLongSegmentThreshold(self):
        r"""URL长分段收敛阈值
        :rtype: int
        """
        return self._UrlLongSegmentThreshold

    @UrlLongSegmentThreshold.setter
    def UrlLongSegmentThreshold(self, UrlLongSegmentThreshold):
        self._UrlLongSegmentThreshold = UrlLongSegmentThreshold

    @property
    def UrlNumberSegmentThreshold(self):
        r"""URL数字分段收敛阈值
        :rtype: int
        """
        return self._UrlNumberSegmentThreshold

    @UrlNumberSegmentThreshold.setter
    def UrlNumberSegmentThreshold(self, UrlNumberSegmentThreshold):
        self._UrlNumberSegmentThreshold = UrlNumberSegmentThreshold


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
        self._IsRemoteCommandExecutionAnalysis = params.get("IsRemoteCommandExecutionAnalysis")
        self._IsMemoryHijackingAnalysis = params.get("IsMemoryHijackingAnalysis")
        self._LogIndexType = params.get("LogIndexType")
        self._LogTraceIdKey = params.get("LogTraceIdKey")
        self._IsDeleteAnyFileAnalysis = params.get("IsDeleteAnyFileAnalysis")
        self._IsReadAnyFileAnalysis = params.get("IsReadAnyFileAnalysis")
        self._IsUploadAnyFileAnalysis = params.get("IsUploadAnyFileAnalysis")
        self._IsIncludeAnyFileAnalysis = params.get("IsIncludeAnyFileAnalysis")
        self._IsDirectoryTraversalAnalysis = params.get("IsDirectoryTraversalAnalysis")
        self._IsTemplateEngineInjectionAnalysis = params.get("IsTemplateEngineInjectionAnalysis")
        self._IsScriptEngineInjectionAnalysis = params.get("IsScriptEngineInjectionAnalysis")
        self._IsExpressionInjectionAnalysis = params.get("IsExpressionInjectionAnalysis")
        self._IsJNDIInjectionAnalysis = params.get("IsJNDIInjectionAnalysis")
        self._IsJNIInjectionAnalysis = params.get("IsJNIInjectionAnalysis")
        self._IsWebshellBackdoorAnalysis = params.get("IsWebshellBackdoorAnalysis")
        self._IsDeserializationAnalysis = params.get("IsDeserializationAnalysis")
        self._UrlLongSegmentThreshold = params.get("UrlLongSegmentThreshold")
        self._UrlNumberSegmentThreshold = params.get("UrlNumberSegmentThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmInstanceResponse(AbstractModel):
    r"""ModifyApmInstance返回参数结构体

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


class ModifyApmPrometheusRuleRequest(AbstractModel):
    r"""ModifyApmPrometheusRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 规则ID
        :type Id: int
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _Name: 所要修改的规则名
        :type Name: str
        :param _Status: 规则状态：1(启用)、2（不启用）、3（删除）
        :type Status: int
        :param _ServiceName: 规则生效的应用。生效于全部应用就传空（这个如果不修改也要传旧的规则）
        :type ServiceName: str
        :param _MetricMatchType: 匹配类型：0精准匹配，1前缀匹配，2后缀匹配（这个如果不修改也要传旧的规则）
        :type MetricMatchType: int
        :param _MetricNameRule: 客户定义的命中指标名规则。
        :type MetricNameRule: str
        """
        self._Id = None
        self._InstanceId = None
        self._Name = None
        self._Status = None
        self._ServiceName = None
        self._MetricMatchType = None
        self._MetricNameRule = None

    @property
    def Id(self):
        r"""规则ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        r"""所要修改的规则名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""规则状态：1(启用)、2（不启用）、3（删除）
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ServiceName(self):
        r"""规则生效的应用。生效于全部应用就传空（这个如果不修改也要传旧的规则）
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def MetricMatchType(self):
        r"""匹配类型：0精准匹配，1前缀匹配，2后缀匹配（这个如果不修改也要传旧的规则）
        :rtype: int
        """
        return self._MetricMatchType

    @MetricMatchType.setter
    def MetricMatchType(self, MetricMatchType):
        self._MetricMatchType = MetricMatchType

    @property
    def MetricNameRule(self):
        r"""客户定义的命中指标名规则。
        :rtype: str
        """
        return self._MetricNameRule

    @MetricNameRule.setter
    def MetricNameRule(self, MetricNameRule):
        self._MetricNameRule = MetricNameRule


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._ServiceName = params.get("ServiceName")
        self._MetricMatchType = params.get("MetricMatchType")
        self._MetricNameRule = params.get("MetricNameRule")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmPrometheusRuleResponse(AbstractModel):
    r"""ModifyApmPrometheusRule返回参数结构体

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


class ModifyApmSampleConfigRequest(AbstractModel):
    r"""ModifyApmSampleConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        :param _SampleName: 采样规则名
        :type SampleName: str
        :param _SampleRate: 采样率
        :type SampleRate: int
        :param _ServiceName: 应用名，生效于所有应用则填空
        :type ServiceName: str
        :param _OperationName: 接口名
        :type OperationName: str
        :param _Tags: 采样tag
        :type Tags: list of APMKVItem
        :param _Status: 采样开关 0关 1开 2删除
        :type Status: int
        :param _Id: 配置Id
        :type Id: int
        :param _OperationType: 0=精确匹配（默认）；1=前缀匹配；2=后缀匹配
        :type OperationType: int
        """
        self._InstanceId = None
        self._SampleName = None
        self._SampleRate = None
        self._ServiceName = None
        self._OperationName = None
        self._Tags = None
        self._Status = None
        self._Id = None
        self._OperationType = None

    @property
    def InstanceId(self):
        r"""业务系统ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SampleName(self):
        r"""采样规则名
        :rtype: str
        """
        return self._SampleName

    @SampleName.setter
    def SampleName(self, SampleName):
        self._SampleName = SampleName

    @property
    def SampleRate(self):
        r"""采样率
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def ServiceName(self):
        r"""应用名，生效于所有应用则填空
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OperationName(self):
        r"""接口名
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def Tags(self):
        r"""采样tag
        :rtype: list of APMKVItem
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        r"""采样开关 0关 1开 2删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Id(self):
        r"""配置Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OperationType(self):
        r"""0=精确匹配（默认）；1=前缀匹配；2=后缀匹配
        :rtype: int
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SampleName = params.get("SampleName")
        self._SampleRate = params.get("SampleRate")
        self._ServiceName = params.get("ServiceName")
        self._OperationName = params.get("OperationName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = APMKVItem()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        self._Id = params.get("Id")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApmSampleConfigResponse(AbstractModel):
    r"""ModifyApmSampleConfig返回参数结构体

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


class ModifyGeneralApmApplicationConfigRequest(AbstractModel):
    r"""ModifyGeneralApmApplicationConfig请求参数结构体

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
        r"""业务系统Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Tags(self):
        r"""需要修改的字段key value分别指定字段名、字段值
[具体字段请见](https://cloud.tencent.com/document/product/248/111241)
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ServiceNames(self):
        r"""需要修改配置的应用列表名称	
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
    r"""ModifyGeneralApmApplicationConfig返回参数结构体

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
        r"""返回值描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class OrderBy(AbstractModel):
    r"""排序字段

    """

    def __init__(self):
        r"""
        :param _Key: 需要排序的字段，现支持 startTIme, endTime, duration
        :type Key: str
        :param _Value: asc 顺序排序 / desc 倒序排序
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""需要排序的字段，现支持 startTIme, endTime, duration
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""asc 顺序排序 / desc 倒序排序
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
    r"""查询

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Compares: 同比，现支持 CompareByYesterday (与昨天相比)和CompareByLastWeek (与上周相比) 
        :type Compares: list of str
        :param _Compare: 同比，已弃用，不建议使用
        :type Compare: str
        """
        self._MetricName = None
        self._Compares = None
        self._Compare = None

    @property
    def MetricName(self):
        r"""指标名
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Compares(self):
        r"""同比，现支持 CompareByYesterday (与昨天相比)和CompareByLastWeek (与上周相比) 
        :rtype: list of str
        """
        return self._Compares

    @Compares.setter
    def Compares(self, Compares):
        self._Compares = Compares

    @property
    def Compare(self):
        r"""同比，已弃用，不建议使用
        :rtype: str
        """
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Compares = params.get("Compares")
        self._Compare = params.get("Compare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceDetail(AbstractModel):
    r"""应用详细信息

    """

    def __init__(self):
        r"""
        :param _ServiceID: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceID: str
        :param _InstanceKey: 业务系统ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceKey: str
        :param _AppID: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: int
        :param _CreateUIN: 主账号uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUIN: str
        :param _ServiceName: 应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _ServiceDescription: 应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDescription: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApmTag
        :param _InstanceName: 业务系统名称
        :type InstanceName: str
        """
        self._ServiceID = None
        self._InstanceKey = None
        self._AppID = None
        self._CreateUIN = None
        self._ServiceName = None
        self._ServiceDescription = None
        self._Region = None
        self._Tags = None
        self._InstanceName = None

    @property
    def ServiceID(self):
        r"""应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def InstanceKey(self):
        r"""业务系统ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def AppID(self):
        r"""用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def CreateUIN(self):
        r"""主账号uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUIN

    @CreateUIN.setter
    def CreateUIN(self, CreateUIN):
        self._CreateUIN = CreateUIN

    @property
    def ServiceName(self):
        r"""应用名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDescription(self):
        r"""应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def Region(self):
        r"""地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Tags(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ApmTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceName(self):
        r"""业务系统名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._ServiceID = params.get("ServiceID")
        self._InstanceKey = params.get("InstanceKey")
        self._AppID = params.get("AppID")
        self._CreateUIN = params.get("CreateUIN")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDescription = params.get("ServiceDescription")
        self._Region = params.get("Region")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Span(AbstractModel):
    r"""Span 对象

    """

    def __init__(self):
        r"""
        :param _TraceID: Trace ID
        :type TraceID: str
        :param _Logs: 日志
        :type Logs: list of SpanLog
        :param _Tags: 标签
        :type Tags: list of SpanTag
        :param _Process: 上报应用服务信息
        :type Process: :class:`tencentcloud.apm.v20210622.models.SpanProcess`
        :param _Timestamp: 产生时间戳(毫秒)
        :type Timestamp: int
        :param _OperationName: Span 名称
        :type OperationName: str
        :param _References: 关联关系
        :type References: list of SpanReference
        :param _StartTime: 产生时间戳(微秒)
        :type StartTime: int
        :param _Duration: 持续耗时(微妙)
        :type Duration: int
        :param _SpanID: Span ID
        :type SpanID: str
        :param _StartTimeMillis: 产生时间戳(毫秒)
        :type StartTimeMillis: int
        :param _ParentSpanID: Parent Span ID
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
        r"""Trace ID
        :rtype: str
        """
        return self._TraceID

    @TraceID.setter
    def TraceID(self, TraceID):
        self._TraceID = TraceID

    @property
    def Logs(self):
        r"""日志
        :rtype: list of SpanLog
        """
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def Tags(self):
        r"""标签
        :rtype: list of SpanTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Process(self):
        r"""上报应用服务信息
        :rtype: :class:`tencentcloud.apm.v20210622.models.SpanProcess`
        """
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def Timestamp(self):
        r"""产生时间戳(毫秒)
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def OperationName(self):
        r"""Span 名称
        :rtype: str
        """
        return self._OperationName

    @OperationName.setter
    def OperationName(self, OperationName):
        self._OperationName = OperationName

    @property
    def References(self):
        r"""关联关系
        :rtype: list of SpanReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def StartTime(self):
        r"""产生时间戳(微秒)
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        r"""持续耗时(微妙)
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def SpanID(self):
        r"""Span ID
        :rtype: str
        """
        return self._SpanID

    @SpanID.setter
    def SpanID(self, SpanID):
        self._SpanID = SpanID

    @property
    def StartTimeMillis(self):
        r"""产生时间戳(毫秒)
        :rtype: int
        """
        return self._StartTimeMillis

    @StartTimeMillis.setter
    def StartTimeMillis(self, StartTimeMillis):
        self._StartTimeMillis = StartTimeMillis

    @property
    def ParentSpanID(self):
        r"""Parent Span ID
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
    r"""Span日志部分


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
        r"""日志时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Fields(self):
        r"""标签
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
    r"""服务相关信息

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
        r"""应用服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Tags(self):
        r"""Tags 标签数组
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
    r"""Span上下游关联关系

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
        r"""关联关系类型
        :rtype: str
        """
        return self._RefType

    @RefType.setter
    def RefType(self, RefType):
        self._RefType = RefType

    @property
    def SpanID(self):
        r"""Span ID
        :rtype: str
        """
        return self._SpanID

    @SpanID.setter
    def SpanID(self, SpanID):
        self._SpanID = SpanID

    @property
    def TraceID(self):
        r"""Trace ID
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
    r"""标签

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
        r"""标签类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        r"""标签Key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
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
    r"""TerminateApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 业务系统ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""业务系统ID
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
    r"""TerminateApmInstance返回参数结构体

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