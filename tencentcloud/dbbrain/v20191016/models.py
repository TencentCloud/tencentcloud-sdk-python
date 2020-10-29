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
        :param StartTime: 开始时间，如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 结束时间，如“2019-09-11 12:13:14”，结束时间与开始时间的间隔最大可为2天。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        """
        self.InstanceId = None
        self.RangeDays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RangeDays = params.get("RangeDays")


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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeTopSpaceTableTimeSeriesResponse(AbstractModel):
    """DescribeTopSpaceTableTimeSeries返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        """
        self.InstanceId = None
        self.Limit = None
        self.SortBy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")


class DescribeTopSpaceTablesResponse(AbstractModel):
    """DescribeTopSpaceTables返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")