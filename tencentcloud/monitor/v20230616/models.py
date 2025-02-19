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


class DataPoint(AbstractModel):
    """监控数据点

    """

    def __init__(self):
        r"""
        :param _Dimensions: 实例对象维度组合
        :type Dimensions: list of Dimension
        :param _Timestamps: 时间戳数组，表示那些时间点有数据，缺失的时间戳，没有数据点，可以理解为掉点了
        :type Timestamps: list of float
        :param _Values: 监控值数组，该数组和Timestamps一一对应
        :type Values: list of float
        """
        self._Dimensions = None
        self._Timestamps = None
        self._Values = None

    @property
    def Dimensions(self):
        """实例对象维度组合
        :rtype: list of Dimension
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions

    @property
    def Timestamps(self):
        """时间戳数组，表示那些时间点有数据，缺失的时间戳，没有数据点，可以理解为掉点了
        :rtype: list of float
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def Values(self):
        """监控值数组，该数组和Timestamps一一对应
        :rtype: list of float
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        self._Timestamps = params.get("Timestamps")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Dimension(AbstractModel):
    """实例对象的维度组合

    """

    def __init__(self):
        r"""
        :param _Name: 实例维度名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 实例维度值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """实例维度名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """实例维度值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Expr(AbstractModel):
    """计算算子

    """

    def __init__(self):
        r"""
        :param _Function: 算子名称
        :type Function: str
        :param _N: 算子入参值
        :type N: float
        """
        self._Function = None
        self._N = None

    @property
    def Function(self):
        """算子名称
        :rtype: str
        """
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def N(self):
        """算子入参值
        :rtype: float
        """
        return self._N

    @N.setter
    def N(self, N):
        self._N = N


    def _deserialize(self, params):
        self._Function = params.get("Function")
        self._N = params.get("N")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间，如QCE/CVM。各个云产品的详细命名空间说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档
        :type Namespace: str
        :param _MetricName: 指标名称，如CPUUsage，仅支持单指标拉取。各个云产品的详细指标说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的指标英文名即为MetricName
        :type MetricName: str
        :param _Instances: 实例对象的维度组合，格式为key-value键值对形式的集合。不同类型的实例字段完全不同，如CVM为[{"Name":"InstanceId","Value":"ins-j0hk02zo"}]，Ckafka为[{"Name":"instanceId","Value":"ckafka-l49k54dd"}]，COS为[{"Name":"appid","Value":"1258344699"},{"Name":"bucket","Value":"rig-1258344699"}]。各个云产品的维度请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的维度列即为维度组合的key，value为key对应的值。单请求最多支持批量拉取10个实例的监控数据。
        :type Instances: list of Instance
        :param _Period: 监控统计周期，如60。默认为取值为300，单位为s。每个指标支持的统计周期不一定相同，各个云产品支持的统计周期请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的统计周期列即为支持的统计周期。单请求的数据点数限制为1440个。
        :type Period: int
        :param _StartTime: 起始时间，如2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param _EndTime: 结束时间，如2018-09-22T20:51:23+08:00，默认为当前时间。 EndTime不能小于StartTime
        :type EndTime: str
        :param _Expr: 计算算子
        :type Expr: :class:`tencentcloud.monitor.v20230616.models.Expr`
        """
        self._Namespace = None
        self._MetricName = None
        self._Instances = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Expr = None

    @property
    def Namespace(self):
        """命名空间，如QCE/CVM。各个云产品的详细命名空间说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def MetricName(self):
        """指标名称，如CPUUsage，仅支持单指标拉取。各个云产品的详细指标说明请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的指标英文名即为MetricName
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Instances(self):
        """实例对象的维度组合，格式为key-value键值对形式的集合。不同类型的实例字段完全不同，如CVM为[{"Name":"InstanceId","Value":"ins-j0hk02zo"}]，Ckafka为[{"Name":"instanceId","Value":"ckafka-l49k54dd"}]，COS为[{"Name":"appid","Value":"1258344699"},{"Name":"bucket","Value":"rig-1258344699"}]。各个云产品的维度请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的维度列即为维度组合的key，value为key对应的值。单请求最多支持批量拉取10个实例的监控数据。
        :rtype: list of Instance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def Period(self):
        """监控统计周期，如60。默认为取值为300，单位为s。每个指标支持的统计周期不一定相同，各个云产品支持的统计周期请参阅各个产品[监控指标](https://cloud.tencent.com/document/product/248/6140)文档，对应的统计周期列即为支持的统计周期。单请求的数据点数限制为1440个。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """起始时间，如2018-09-22T19:51:23+08:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如2018-09-22T20:51:23+08:00，默认为当前时间。 EndTime不能小于StartTime
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Expr(self):
        """计算算子
        :rtype: :class:`tencentcloud.monitor.v20230616.models.Expr`
        """
        return self._Expr

    @Expr.setter
    def Expr(self, Expr):
        self._Expr = Expr


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Expr") is not None:
            self._Expr = Expr()
            self._Expr._deserialize(params.get("Expr"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 统计周期
        :type Period: int
        :param _MetricName: 指标名
        :type MetricName: str
        :param _DataPoints: 数据点数组
        :type DataPoints: list of DataPoint
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Msg: 返回信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Period = None
        self._MetricName = None
        self._DataPoints = None
        self._StartTime = None
        self._EndTime = None
        self._Msg = None
        self._RequestId = None

    @property
    def Period(self):
        """统计周期
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def DataPoints(self):
        """数据点数组
        :rtype: list of DataPoint
        """
        return self._DataPoints

    @DataPoints.setter
    def DataPoints(self, DataPoints):
        self._DataPoints = DataPoints

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Msg(self):
        """返回信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Period = params.get("Period")
        self._MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self._DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self._DataPoints.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """实例维度组合数组

    """

    def __init__(self):
        r"""
        :param _Dimensions: 实例的维度组合
注意：此字段可能返回 null，表示取不到有效值。
        :type Dimensions: list of Dimension
        """
        self._Dimensions = None

    @property
    def Dimensions(self):
        """实例的维度组合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Dimension
        """
        return self._Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions):
        self._Dimensions = Dimensions


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self._Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self._Dimensions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        