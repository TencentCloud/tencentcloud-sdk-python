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


class APMKVItem(AbstractModel):
    """Apm通用KV结构

    """

    def __init__(self):
        r"""
        :param Key: Key值定义
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: Value值定义
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ApmAgentInfo(AbstractModel):
    """apm Agent信息

    """

    def __init__(self):
        r"""
        :param AgentDownloadURL: Agent下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentDownloadURL: str
        :param CollectorURL: Collector上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectorURL: str
        :param Token: Token信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param PublicCollectorURL: 外网上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicCollectorURL: str
        :param InnerCollectorURL: 自研VPC上报地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerCollectorURL: str
        :param PrivateLinkCollectorURL: 内网上报地址(Private Link上报地址)
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateLinkCollectorURL: str
        """
        self.AgentDownloadURL = None
        self.CollectorURL = None
        self.Token = None
        self.PublicCollectorURL = None
        self.InnerCollectorURL = None
        self.PrivateLinkCollectorURL = None


    def _deserialize(self, params):
        self.AgentDownloadURL = params.get("AgentDownloadURL")
        self.CollectorURL = params.get("CollectorURL")
        self.Token = params.get("Token")
        self.PublicCollectorURL = params.get("PublicCollectorURL")
        self.InnerCollectorURL = params.get("InnerCollectorURL")
        self.PrivateLinkCollectorURL = params.get("PrivateLinkCollectorURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmField(AbstractModel):
    """指标维度信息

    """

    def __init__(self):
        r"""
        :param CompareVal: 昨日同比指标值，已弃用，不建议使用
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareVal: str
        :param CompareVals: Compare值结果数组，推荐使用
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareVals: list of APMKVItem
        :param Value: 指标值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        :param Unit: 指标所对应的单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Key: 请求数
        :type Key: str
        """
        self.CompareVal = None
        self.CompareVals = None
        self.Value = None
        self.Unit = None
        self.Key = None


    def _deserialize(self, params):
        self.CompareVal = params.get("CompareVal")
        if params.get("CompareVals") is not None:
            self.CompareVals = []
            for item in params.get("CompareVals"):
                obj = APMKVItem()
                obj._deserialize(item)
                self.CompareVals.append(obj)
        self.Value = params.get("Value")
        self.Unit = params.get("Unit")
        self.Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmInstanceDetail(AbstractModel):
    """apm实例信息

    """

    def __init__(self):
        r"""
        :param AmountOfUsedStorage: 存储使用量(MB)
注意：此字段可能返回 null，表示取不到有效值。
        :type AmountOfUsedStorage: float
        :param Name: 实例名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Tags: 实例所属tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApmTag
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param CreateUin: 创建人Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        :param ServiceCount: 该实例已上报的服务端应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param CountOfReportSpanPerDay: 日均上报Span数
注意：此字段可能返回 null，表示取不到有效值。
        :type CountOfReportSpanPerDay: int
        :param AppId: AppId信息
        :type AppId: int
        :param TraceDuration: Trace数据保存时长
注意：此字段可能返回 null，表示取不到有效值。
        :type TraceDuration: int
        :param Description: 实例描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Status: 实例状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Region: 实例所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param SpanDailyCounters: 实例上报额度
注意：此字段可能返回 null，表示取不到有效值。
        :type SpanDailyCounters: int
        :param BillingInstance: 实例是否开通计费
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInstance: int
        :param ErrRateThreshold: 错误率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrRateThreshold: int
        :param SampleRate: 采样率阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleRate: int
        :param ErrorSample: 是否开启错误采样 0  关 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorSample: int
        :param SlowRequestSavedThreshold: 慢调用保存阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowRequestSavedThreshold: int
        :param LogRegion: cls日志所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type LogRegion: str
        :param LogSource: 日志来源
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSource: str
        :param IsRelatedLog: 日志功能开关 0 关 | 1 开
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRelatedLog: int
        :param LogTopicID: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicID: str
        :param ClientCount: 该实例已上报的客户端应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCount: int
        :param TotalCount: 该实例已上报的总应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.AmountOfUsedStorage = None
        self.Name = None
        self.Tags = None
        self.InstanceId = None
        self.CreateUin = None
        self.ServiceCount = None
        self.CountOfReportSpanPerDay = None
        self.AppId = None
        self.TraceDuration = None
        self.Description = None
        self.Status = None
        self.Region = None
        self.SpanDailyCounters = None
        self.BillingInstance = None
        self.ErrRateThreshold = None
        self.SampleRate = None
        self.ErrorSample = None
        self.SlowRequestSavedThreshold = None
        self.LogRegion = None
        self.LogSource = None
        self.IsRelatedLog = None
        self.LogTopicID = None
        self.ClientCount = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.AmountOfUsedStorage = params.get("AmountOfUsedStorage")
        self.Name = params.get("Name")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.CreateUin = params.get("CreateUin")
        self.ServiceCount = params.get("ServiceCount")
        self.CountOfReportSpanPerDay = params.get("CountOfReportSpanPerDay")
        self.AppId = params.get("AppId")
        self.TraceDuration = params.get("TraceDuration")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.SpanDailyCounters = params.get("SpanDailyCounters")
        self.BillingInstance = params.get("BillingInstance")
        self.ErrRateThreshold = params.get("ErrRateThreshold")
        self.SampleRate = params.get("SampleRate")
        self.ErrorSample = params.get("ErrorSample")
        self.SlowRequestSavedThreshold = params.get("SlowRequestSavedThreshold")
        self.LogRegion = params.get("LogRegion")
        self.LogSource = params.get("LogSource")
        self.IsRelatedLog = params.get("IsRelatedLog")
        self.LogTopicID = params.get("LogTopicID")
        self.ClientCount = params.get("ClientCount")
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmMetricRecord(AbstractModel):
    """指标列表单元

    """

    def __init__(self):
        r"""
        :param Fields: field数组
        :type Fields: list of ApmField
        :param Tags: tag数组
        :type Tags: list of ApmTag
        """
        self.Fields = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Fields") is not None:
            self.Fields = []
            for item in params.get("Fields"):
                obj = ApmField()
                obj._deserialize(item)
                self.Fields.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApmTag(AbstractModel):
    """维度（标签）对象

    """

    def __init__(self):
        r"""
        :param Key: 维度Key(列名，标签Key)
        :type Key: str
        :param Value: 维度值（标签值）
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
        


class CreateApmInstanceRequest(AbstractModel):
    """CreateApmInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 实例名
        :type Name: str
        :param Description: 实例描述信息
        :type Description: str
        :param TraceDuration: Trace数据保存时长
        :type TraceDuration: int
        :param Tags: 标签列表
        :type Tags: list of ApmTag
        :param SpanDailyCounters: 实例上报额度值
        :type SpanDailyCounters: int
        """
        self.Name = None
        self.Description = None
        self.TraceDuration = None
        self.Tags = None
        self.SpanDailyCounters = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.TraceDuration = params.get("TraceDuration")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SpanDailyCounters = params.get("SpanDailyCounters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApmInstanceResponse(AbstractModel):
    """CreateApmInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DescribeApmAgentRequest(AbstractModel):
    """DescribeApmAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param AgentType: 接入方式
        :type AgentType: str
        :param NetworkMode: 环境
        :type NetworkMode: str
        :param LanguageEnvironment: 语言
        :type LanguageEnvironment: str
        :param ReportMethod: 上报方式
        :type ReportMethod: str
        """
        self.InstanceId = None
        self.AgentType = None
        self.NetworkMode = None
        self.LanguageEnvironment = None
        self.ReportMethod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AgentType = params.get("AgentType")
        self.NetworkMode = params.get("NetworkMode")
        self.LanguageEnvironment = params.get("LanguageEnvironment")
        self.ReportMethod = params.get("ReportMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmAgentResponse(AbstractModel):
    """DescribeApmAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApmAgent: Agent信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApmAgent: :class:`tencentcloud.apm.v20210622.models.ApmAgentInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApmAgent = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApmAgent") is not None:
            self.ApmAgent = ApmAgentInfo()
            self.ApmAgent._deserialize(params.get("ApmAgent"))
        self.RequestId = params.get("RequestId")


class DescribeApmInstancesRequest(AbstractModel):
    """DescribeApmInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Tags: Tag列表
        :type Tags: list of ApmTag
        :param InstanceName: 搜索实例名
        :type InstanceName: str
        :param InstanceIds: 过滤实例ID
        :type InstanceIds: list of str
        :param DemoInstanceFlag: 是否查询官方demo实例
        :type DemoInstanceFlag: int
        """
        self.Tags = None
        self.InstanceName = None
        self.InstanceIds = None
        self.DemoInstanceFlag = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceName = params.get("InstanceName")
        self.InstanceIds = params.get("InstanceIds")
        self.DemoInstanceFlag = params.get("DemoInstanceFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApmInstancesResponse(AbstractModel):
    """DescribeApmInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: apm实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of ApmInstanceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = ApmInstanceDetail()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGeneralMetricDataRequest(AbstractModel):
    """DescribeGeneralMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 要过滤的维度信息，支持：service.name（服务名）、span.kind（客户端/服务端视角）为维度进行过滤。

span.kind:

       server:服务端视角
       client:客户端视角

默认为服务端视角进行查询。
        :type Filters: list of GeneralFilter
        :param Metrics: 需要查询的指标，不可自定义输入。支持：service_request_count（总请求）、service_duration（平均响应时间）的指标数据。
        :type Metrics: list of str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param ViewName: 视图名称，不可自定义输入。支持：service_metric
        :type ViewName: str
        :param GroupBy: 聚合维度，支持：service.name（服务名）、span.kind （客户端/服务端视角）维度进行聚合。
        :type GroupBy: list of str
        :param StartTime: 起始时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :type StartTime: int
        :param EndTime: 结束时间的时间戳，单位为秒，只支持查询2天内最多1小时的指标数据。
        :type EndTime: int
        :param Period: 聚合粒度，单位为秒，最小为60s，即一分钟的聚合粒度；如果为空或0则计算开始时间到截止时间的指标数据，上报其他值会报错。
        :type Period: int
        """
        self.Filters = None
        self.Metrics = None
        self.InstanceId = None
        self.ViewName = None
        self.GroupBy = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = GeneralFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Metrics = params.get("Metrics")
        self.InstanceId = params.get("InstanceId")
        self.ViewName = params.get("ViewName")
        self.GroupBy = params.get("GroupBy")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralMetricDataResponse(AbstractModel):
    """DescribeGeneralMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Records: 指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of Line
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = Line()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMetricRecordsRequest(AbstractModel):
    """DescribeMetricRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Metrics: 指标列表
        :type Metrics: list of QueryMetricItem
        :param GroupBy: 聚合维度
        :type GroupBy: list of str
        :param OrderBy: 排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Limit: 每页大小
        :type Limit: int
        :param StartTime: 开始时间
        :type StartTime: int
        :param Offset: 分页起始点
        :type Offset: int
        :param EndTime: 结束时间
        :type EndTime: int
        :param BusinessName: 业务名称（默认值：taw）
        :type BusinessName: str
        """
        self.Filters = None
        self.Metrics = None
        self.GroupBy = None
        self.OrderBy = None
        self.InstanceId = None
        self.Limit = None
        self.StartTime = None
        self.Offset = None
        self.EndTime = None
        self.BusinessName = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.GroupBy = params.get("GroupBy")
        if params.get("OrderBy") is not None:
            self.OrderBy = OrderBy()
            self.OrderBy._deserialize(params.get("OrderBy"))
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.Offset = params.get("Offset")
        self.EndTime = params.get("EndTime")
        self.BusinessName = params.get("BusinessName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMetricRecordsResponse(AbstractModel):
    """DescribeMetricRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Records: 指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of ApmMetricRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServiceOverviewRequest(AbstractModel):
    """DescribeServiceOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Metrics: 指标列表
        :type Metrics: list of QueryMetricItem
        :param GroupBy: 聚合维度
        :type GroupBy: list of str
        :param OrderBy: 排序
        :type OrderBy: :class:`tencentcloud.apm.v20210622.models.OrderBy`
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Limit: 每页大小
        :type Limit: int
        :param StartTime: 开始时间
        :type StartTime: int
        :param Offset: 分页起始点
        :type Offset: int
        :param EndTime: 结束时间
        :type EndTime: int
        """
        self.Filters = None
        self.Metrics = None
        self.GroupBy = None
        self.OrderBy = None
        self.InstanceId = None
        self.Limit = None
        self.StartTime = None
        self.Offset = None
        self.EndTime = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = QueryMetricItem()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.GroupBy = params.get("GroupBy")
        if params.get("OrderBy") is not None:
            self.OrderBy = OrderBy()
            self.OrderBy._deserialize(params.get("OrderBy"))
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.Offset = params.get("Offset")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceOverviewResponse(AbstractModel):
    """DescribeServiceOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param Records: 指标结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of ApmMetricRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = ApmMetricRecord()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查询过滤参数

    """

    def __init__(self):
        r"""
        :param Type: 过滤方式（=, !=, in）
        :type Type: str
        :param Key: 过滤维度名
        :type Key: str
        :param Value: 过滤值，in过滤方式用逗号分割多个值
        :type Value: str
        """
        self.Type = None
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralFilter(AbstractModel):
    """查询过滤参数

    """

    def __init__(self):
        r"""
        :param Key: 过滤维度名
        :type Key: str
        :param Value: 过滤值
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
        


class Line(AbstractModel):
    """指标曲线数据

    """

    def __init__(self):
        r"""
        :param MetricName: 指标名
        :type MetricName: str
        :param MetricNameCN: 指标中文名
        :type MetricNameCN: str
        :param TimeSerial: 时间序列
        :type TimeSerial: list of int
        :param DataSerial: 数据序列
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSerial: list of float
        :param Tags: 维度列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApmTag
        """
        self.MetricName = None
        self.MetricNameCN = None
        self.TimeSerial = None
        self.DataSerial = None
        self.Tags = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.MetricNameCN = params.get("MetricNameCN")
        self.TimeSerial = params.get("TimeSerial")
        self.DataSerial = params.get("DataSerial")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApmTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderBy(AbstractModel):
    """sql排序字段

    """

    def __init__(self):
        r"""
        :param Key: 需要排序的字段
        :type Key: str
        :param Value: 顺序排序/倒序排序
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
        


class QueryMetricItem(AbstractModel):
    """查询

    """

    def __init__(self):
        r"""
        :param MetricName: 指标名
        :type MetricName: str
        :param Compare: 同比，已弃用，不建议使用
        :type Compare: str
        :param Compares: 同比，支持多种同比方式
        :type Compares: list of str
        """
        self.MetricName = None
        self.Compare = None
        self.Compares = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Compare = params.get("Compare")
        self.Compares = params.get("Compares")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        