# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param EventId: 事件 ID 。通过“获取实例诊断历史DescribeDBDiagHistory”获取。
        :type EventId: int
        """
        self.InstanceId = None
        self.EventId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EventId = params.get("EventId")


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent返回参数结构体

    """

    def __init__(self):
        """
        :param DiagItem: 诊断项。
        :type DiagItem: str
        :param DiagType: 诊断类型。
        :type DiagType: str
        :param EventId: 事件 ID 。
        :type EventId: int
        :param Explanation: 事件详情。
        :type Explanation: str
        :param Outline: 概要。
        :type Outline: str
        :param Problem: 诊断出的问题。
        :type Problem: str
        :param Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param Suggestions: 建议。
        :type Suggestions: str
        :param Metric: 保留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiagItem = None
        self.DiagType = None
        self.EventId = None
        self.Explanation = None
        self.Outline = None
        self.Problem = None
        self.Severity = None
        self.StartTime = None
        self.Suggestions = None
        self.Metric = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiagItem = params.get("DiagItem")
        self.DiagType = params.get("DiagType")
        self.EventId = params.get("EventId")
        self.Explanation = params.get("Explanation")
        self.Outline = params.get("Outline")
        self.Problem = params.get("Problem")
        self.Severity = params.get("Severity")
        self.StartTime = params.get("StartTime")
        self.Suggestions = params.get("Suggestions")
        self.Metric = params.get("Metric")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间。如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 结束时间。如“2019-09-11 12:13:14”。
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory返回参数结构体

    """

    def __init__(self):
        """
        :param Events: 事件描述。
        :type Events: list of DiagHistoryEventItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats返回参数结构体

    """

    def __init__(self):
        """
        :param Period: 柱间单位时间间隔，单位为秒。
        :type Period: int
        :param TimeSeries: 单位时间间隔内慢日志数量统计。
        :type TimeSeries: list of TimeSlice
        :param SeriesData: 单位时间间隔内的实例 cpu 利用率监控数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Period = None
        self.TimeSeries = None
        self.SeriesData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self.TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self.TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 截止时间。
        :type EndTime: str
        :param SortBy: 排序键，目前支持 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序键。
        :type SortBy: str
        :param OrderBy: 排序方式，支持ASC（升序）以及DESC（降序）。
        :type OrderBy: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SortBy = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SortBy = params.get("SortBy")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
        :type TotalCount: int
        :param Rows: 慢日志 top sql 列表
        :type Rows: list of SlowLogTopSqlItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """实例诊断历史事件

    """

    def __init__(self):
        """
        :param DiagType: 诊断类型。
        :type DiagType: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EventId: 事件 ID 。
        :type EventId: int
        :param Severity: 严重程度。严重程度分为5级，按影响程度从高至低分别为：1：致命，2：严重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param Outline: 概要。
        :type Outline: str
        :param DiagItem: 诊断项。
        :type DiagItem: str
        :param InstanceId: 实例 ID 。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Metric: 保留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self.DiagType = None
        self.EndTime = None
        self.StartTime = None
        self.EventId = None
        self.Severity = None
        self.Outline = None
        self.DiagItem = None
        self.InstanceId = None
        self.Metric = None
        self.Region = None


    def _deserialize(self, params):
        self.DiagType = params.get("DiagType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.EventId = params.get("EventId")
        self.Severity = params.get("Severity")
        self.Outline = params.get("Outline")
        self.DiagItem = params.get("DiagItem")
        self.InstanceId = params.get("InstanceId")
        self.Metric = params.get("Metric")
        self.Region = params.get("Region")


class MonitorMetric(AbstractModel):
    """监控数据

    """

    def __init__(self):
        """
        :param Metric: 指标名称。
        :type Metric: str
        :param Unit: 指标单位。
        :type Unit: str
        :param Values: 指标值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of int
        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")


class MonitorMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据

    """

    def __init__(self):
        """
        :param Series: 监控指标。
        :type Series: list of MonitorMetric
        :param Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self.Series = None
        self.Timestamp = None


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self.Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self.Series.append(obj)
        self.Timestamp = params.get("Timestamp")


class SlowLogTopSqlItem(AbstractModel):
    """慢日志TopSql

    """

    def __init__(self):
        """
        :param LockTime: sql总锁等待时间
        :type LockTime: float
        :param LockTimeMax: 最大锁等待时间
        :type LockTimeMax: float
        :param LockTimeMin: 最小锁等待时间
        :type LockTimeMin: float
        :param RowsExamined: 总扫描行数
        :type RowsExamined: int
        :param RowsExaminedMax: 最大扫描行数
        :type RowsExaminedMax: int
        :param RowsExaminedMin: 最小扫描行数
        :type RowsExaminedMin: int
        :param QueryTime: 总耗时
        :type QueryTime: float
        :param QueryTimeMax: 最大执行时间
        :type QueryTimeMax: float
        :param QueryTimeMin: 最小执行时间
        :type QueryTimeMin: float
        :param RowsSent: 总返回行数
        :type RowsSent: int
        :param RowsSentMax: 最大返回行数
        :type RowsSentMax: int
        :param RowsSentMin: 最小返回行数
        :type RowsSentMin: int
        :param ExecTimes: 执行次数
        :type ExecTimes: int
        :param SqlTemplate: sql模板
        :type SqlTemplate: str
        :param SqlText: 带参数SQL（随机）
        :type SqlText: str
        :param Schema: schema
        :type Schema: str
        :param QueryTimeRatio: 总耗时占比
        :type QueryTimeRatio: float
        :param LockTimeRatio: sql总锁等待时间占比
        :type LockTimeRatio: float
        :param RowsExaminedRatio: 总扫描行数占比
        :type RowsExaminedRatio: float
        :param RowsSentRatio: 总返回行数占比
        :type RowsSentRatio: float
        """
        self.LockTime = None
        self.LockTimeMax = None
        self.LockTimeMin = None
        self.RowsExamined = None
        self.RowsExaminedMax = None
        self.RowsExaminedMin = None
        self.QueryTime = None
        self.QueryTimeMax = None
        self.QueryTimeMin = None
        self.RowsSent = None
        self.RowsSentMax = None
        self.RowsSentMin = None
        self.ExecTimes = None
        self.SqlTemplate = None
        self.SqlText = None
        self.Schema = None
        self.QueryTimeRatio = None
        self.LockTimeRatio = None
        self.RowsExaminedRatio = None
        self.RowsSentRatio = None


    def _deserialize(self, params):
        self.LockTime = params.get("LockTime")
        self.LockTimeMax = params.get("LockTimeMax")
        self.LockTimeMin = params.get("LockTimeMin")
        self.RowsExamined = params.get("RowsExamined")
        self.RowsExaminedMax = params.get("RowsExaminedMax")
        self.RowsExaminedMin = params.get("RowsExaminedMin")
        self.QueryTime = params.get("QueryTime")
        self.QueryTimeMax = params.get("QueryTimeMax")
        self.QueryTimeMin = params.get("QueryTimeMin")
        self.RowsSent = params.get("RowsSent")
        self.RowsSentMax = params.get("RowsSentMax")
        self.RowsSentMin = params.get("RowsSentMin")
        self.ExecTimes = params.get("ExecTimes")
        self.SqlTemplate = params.get("SqlTemplate")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.QueryTimeRatio = params.get("QueryTimeRatio")
        self.LockTimeRatio = params.get("LockTimeRatio")
        self.RowsExaminedRatio = params.get("RowsExaminedRatio")
        self.RowsSentRatio = params.get("RowsSentRatio")


class TimeSlice(AbstractModel):
    """单位时间间隔内的慢日志统计

    """

    def __init__(self):
        """
        :param Count: 总数
        :type Count: int
        :param Timestamp: 统计开始时间
        :type Timestamp: int
        """
        self.Count = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Timestamp = params.get("Timestamp")