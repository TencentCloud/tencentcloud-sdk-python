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


class DataPoint(AbstractModel):
    """监控数据点

    """

    def __init__(self):
        """
        :param Dimensions: 实例对象维度组合
        :type Dimensions: list of Dimension
        :param Timestamps: 时间戳数组，表示那些时间点有数据，缺失的时间戳，没有数据点，可以理解为掉点了
        :type Timestamps: list of float
        :param Values: 监控值数组，该数组和Timestamps一一对应
        :type Values: list of float
        """
        self.Dimensions = None
        self.Timestamps = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.Timestamps = params.get("Timestamps")
        self.Values = params.get("Values")


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 业务命名空间
        :type Namespace: str
        :param MetricName: 指标名
        :type MetricName: str
        """
        self.Namespace = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics返回参数结构体

    """

    def __init__(self):
        """
        :param MetricSet: 查询得到的指标描述列表
        :type MetricSet: list of MetricSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self.MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricSet()
                obj._deserialize(item)
                self.MetricSet.append(obj)
        self.RequestId = params.get("RequestId")


class Dimension(AbstractModel):
    """实例对象的维度组合

    """

    def __init__(self):
        """
        :param Name: 实例维度名称
        :type Name: str
        :param Value: 实例维度值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class DimensionsDesc(AbstractModel):
    """维度信息

    """

    def __init__(self):
        """
        :param Dimensions: 维度名数组
        :type Dimensions: list of str
        """
        self.Dimensions = None


    def _deserialize(self, params):
        self.Dimensions = params.get("Dimensions")


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData请求参数结构体

    """

    def __init__(self):
        """
        :param Namespace: 命名空间，每个云产品会有一个命名空间
        :type Namespace: str
        :param MetricName: 指标名称
        :type MetricName: str
        :param Instances: 实例对象的维度组合
        :type Instances: list of Instance
        :param Period: 监控统计周期。默认为取值为300，单位为s
        :type Period: int
        :param StartTime: 起始时间，如2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param EndTime: 结束时间，默认为当前时间。 EndTime不能小于EtartTime
        :type EndTime: str
        """
        self.Namespace = None
        self.MetricName = None
        self.Instances = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData返回参数结构体

    """

    def __init__(self):
        """
        :param Period: 统计周期
        :type Period: int
        :param MetricName: 指标名
        :type MetricName: str
        :param DataPoints: 数据点数组
        :type DataPoints: list of DataPoint
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Period = None
        self.MetricName = None
        self.DataPoints = None
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """实例维度组合数组

    """

    def __init__(self):
        """
        :param Dimensions: 实例的维度组合
        :type Dimensions: list of Dimension
        """
        self.Dimensions = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class MetricObjectMeaning(AbstractModel):
    """指标数据的解释

    """

    def __init__(self):
        """
        :param En: 指标英文解释
        :type En: str
        :param Zh: 指标中文解释
        :type Zh: str
        """
        self.En = None
        self.Zh = None


    def _deserialize(self, params):
        self.En = params.get("En")
        self.Zh = params.get("Zh")


class MetricSet(AbstractModel):
    """对业务指标的单位及支持统计周期的描述

    """

    def __init__(self):
        """
        :param Namespace: 命名空间，每个云产品会有一个命名空间
        :type Namespace: str
        :param MetricName: 指标名称
        :type MetricName: str
        :param Unit: 指标使用的单位
        :type Unit: str
        :param UnitCname: 指标使用的单位
        :type UnitCname: str
        :param Period: 指标支持的统计周期，单位是秒，如60、300
        :type Period: list of int
        :param Periods: 统计周期内指标方式
        :type Periods: list of PeriodsSt
        :param Meaning: 统计指标含义解释
        :type Meaning: :class:`tencentcloud.monitor.v20180724.models.MetricObjectMeaning`
        :param Dimensions: 维度描述信息
        :type Dimensions: list of DimensionsDesc
        """
        self.Namespace = None
        self.MetricName = None
        self.Unit = None
        self.UnitCname = None
        self.Period = None
        self.Periods = None
        self.Meaning = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Unit = params.get("Unit")
        self.UnitCname = params.get("UnitCname")
        self.Period = params.get("Period")
        if params.get("Periods") is not None:
            self.Periods = []
            for item in params.get("Periods"):
                obj = PeriodsSt()
                obj._deserialize(item)
                self.Periods.append(obj)
        if params.get("Meaning") is not None:
            self.Meaning = MetricObjectMeaning()
            self.Meaning._deserialize(params.get("Meaning"))
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionsDesc()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class PeriodsSt(AbstractModel):
    """周期内的统计方式

    """

    def __init__(self):
        """
        :param Period: 周期
        :type Period: str
        :param StatType: 统计方式
        :type StatType: list of str
        """
        self.Period = None
        self.StatType = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.StatType = params.get("StatType")