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
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.EventId = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EventId = params.get("EventId")
        self.Product = params.get("Product")


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
        :param StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 结束时间，如“2019-09-11 12:13:14”，结束时间与开始时间的间隔最大可为2天。
        :type EndTime: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")


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


class DescribeDBSpaceStatusRequest(AbstractModel):
    """DescribeDBSpaceStatus请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param RangeDays: 时间段天数，截止日期为当日，默认为7天。
        :type RangeDays: int
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.RangeDays = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RangeDays = params.get("RangeDays")
        self.Product = params.get("Product")


class DescribeDBSpaceStatusResponse(AbstractModel):
    """DescribeDBSpaceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Growth: 磁盘增长量(MB)。
        :type Growth: int
        :param Remain: 磁盘剩余(MB)。
        :type Remain: int
        :param Total: 磁盘总量(MB)。
        :type Total: int
        :param AvailableDays: 预计可用天数。
        :type AvailableDays: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Growth = None
        self.Remain = None
        self.Total = None
        self.AvailableDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Growth = params.get("Growth")
        self.Remain = params.get("Remain")
        self.Total = params.get("Total")
        self.AvailableDays = params.get("AvailableDays")
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 结束时间，如“2019-09-10 12:13:14”，结束时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Product = params.get("Product")


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
        :param StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 截止时间，如“2019-09-10 12:13:14”，截止时间与开始时间的间隔最大可为7天。
        :type EndTime: str
        :param SortBy: 排序键，目前支持 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序键。
        :type SortBy: str
        :param OrderBy: 排序方式，支持ASC（升序）以及DESC（降序）。
        :type OrderBy: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param SchemaList: 数据库名称数组。
        :type SchemaList: list of SchemaItem
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SortBy = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None
        self.SchemaList = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SortBy = params.get("SortBy")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("SchemaList") is not None:
            self.SchemaList = []
            for item in params.get("SchemaList"):
                obj = SchemaItem()
                obj._deserialize(item)
                self.SchemaList.append(obj)
        self.Product = params.get("Product")


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


class DescribeTopSpaceTableTimeSeriesRequest(AbstractModel):
    """DescribeTopSpaceTableTimeSeries请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param Limit: 返回的Top表数量，最大值为20，默认为最大值。
        :type Limit: int
        :param SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。
        :type SortBy: str
        :param StartDate: 开始日期，最早为当日的前第29天，默认为截止日期的前第6天。
        :type StartDate: str
        :param EndDate: 截止日期，最早为当日的前第29天，默认为当日。
        :type EndDate: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.StartDate = None
        self.EndDate = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Product = params.get("Product")


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries返回参数结构体

    """

    def __init__(self):
        """
        :param TopSpaceTableTimeSeries: 返回的Top表空间统计信息的时序数据列表。
        :type TopSpaceTableTimeSeries: list of TableSpaceTimeSeries
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopSpaceTableTimeSeries = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceTableTimeSeries") is not None:
            self.TopSpaceTableTimeSeries = []
            for item in params.get("TopSpaceTableTimeSeries"):
                obj = TableSpaceTimeSeries()
                obj._deserialize(item)
                self.TopSpaceTableTimeSeries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopSpaceTablesRequest(AbstractModel):
    """DescribeTopSpaceTables请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例 ID 。
        :type InstanceId: str
        :param Limit: 返回的Top表数量，最大值为20，默认为最大值。
        :type Limit: int
        :param SortBy: 筛选Top表所用的排序字段，可选字段包含DataLength、IndexLength、TotalLength、DataFree、FragRatio、TableRows、PhysicalFileSize，默认为 PhysicalFileSize。
        :type SortBy: str
        :param Product: 服务产品类型，支持值包括： "mysql" - 云数据库 MySQL， "cynosdb" - 云数据库 CynosDB  for MySQL，默认为"mysql"。
        :type Product: str
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.Product = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.Product = params.get("Product")


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables返回参数结构体

    """

    def __init__(self):
        """
        :param TopSpaceTables: 返回的Top表空间统计信息列表。
        :type TopSpaceTables: list of TableSpaceData
        :param Timestamp: 采集表空间数据的时间戳（秒）。
        :type Timestamp: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopSpaceTables = None
        self.Timestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopSpaceTables") is not None:
            self.TopSpaceTables = []
            for item in params.get("TopSpaceTables"):
                obj = TableSpaceData()
                obj._deserialize(item)
                self.TopSpaceTables.append(obj)
        self.Timestamp = params.get("Timestamp")
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


class MonitorFloatMetric(AbstractModel):
    """监控数据（浮点型）

    """

    def __init__(self):
        """
        :param Metric: 指标名称。
        :type Metric: str
        :param Unit: 指标单位。
        :type Unit: str
        :param Values: 指标值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of float
        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")


class MonitorFloatMetricSeriesData(AbstractModel):
    """单位时间间隔内的监控指标数据（浮点型）

    """

    def __init__(self):
        """
        :param Series: 监控指标。
        :type Series: list of MonitorFloatMetric
        :param Timestamp: 监控指标对应的时间戳。
        :type Timestamp: list of int
        """
        self.Series = None
        self.Timestamp = None


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self.Series = []
            for item in params.get("Series"):
                obj = MonitorFloatMetric()
                obj._deserialize(item)
                self.Series.append(obj)
        self.Timestamp = params.get("Timestamp")


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


class SchemaItem(AbstractModel):
    """SchemaItem数组

    """

    def __init__(self):
        """
        :param Schema: 数据库名称
        :type Schema: str
        """
        self.Schema = None


    def _deserialize(self, params):
        self.Schema = params.get("Schema")


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
        :param Schema: 数据库名
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


class TableSpaceData(AbstractModel):
    """库表空间统计数据。

    """

    def __init__(self):
        """
        :param TableName: 表名。
        :type TableName: str
        :param TableSchema: 库名。
        :type TableSchema: str
        :param Engine: 库表的存储引擎。
        :type Engine: str
        :param DataLength: 数据空间（MB）。
        :type DataLength: float
        :param IndexLength: 索引空间（MB）。
        :type IndexLength: float
        :param DataFree: 碎片空间（MB）。
        :type DataFree: float
        :param TotalLength: 总使用空间（MB）。
        :type TotalLength: float
        :param FragRatio: 碎片率（%）。
        :type FragRatio: float
        :param TableRows: 行数。
        :type TableRows: int
        :param PhysicalFileSize: 表对应的独立物理文件大小（MB）。
        :type PhysicalFileSize: float
        """
        self.TableName = None
        self.TableSchema = None
        self.Engine = None
        self.DataLength = None
        self.IndexLength = None
        self.DataFree = None
        self.TotalLength = None
        self.FragRatio = None
        self.TableRows = None
        self.PhysicalFileSize = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableSchema = params.get("TableSchema")
        self.Engine = params.get("Engine")
        self.DataLength = params.get("DataLength")
        self.IndexLength = params.get("IndexLength")
        self.DataFree = params.get("DataFree")
        self.TotalLength = params.get("TotalLength")
        self.FragRatio = params.get("FragRatio")
        self.TableRows = params.get("TableRows")
        self.PhysicalFileSize = params.get("PhysicalFileSize")


class TableSpaceTimeSeries(AbstractModel):
    """库表空间时序数据

    """

    def __init__(self):
        """
        :param TableName: 表名。
        :type TableName: str
        :param TableSchema: 库名。
        :type TableSchema: str
        :param Engine: 库表的存储引擎。
        :type Engine: str
        :param SeriesData: 单位时间间隔内的空间指标数据。
        :type SeriesData: :class:`tencentcloud.dbbrain.v20191016.models.MonitorFloatMetricSeriesData`
        """
        self.TableName = None
        self.TableSchema = None
        self.Engine = None
        self.SeriesData = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableSchema = params.get("TableSchema")
        self.Engine = params.get("Engine")
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorFloatMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))


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