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


class CreateProbeTasksRequest(AbstractModel):
    """CreateProbeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTasks: 批量任务名-地址
        :type BatchTasks: list of ProbeTaskBasicConfiguration
        :param _TaskType: 任务类型，如1、2、3、4、5、6、7；1-页面性能、2-文件上传、3-文件下载、4-端口性能、5-网络质量、6-音视频体验、7-域名whois
        :type TaskType: int
        :param _Nodes: 拨测节点，如10001，具体拨测地域运营商对应的拨测点编号可联系云拨测确认。
        :type Nodes: list of str
        :param _Interval: 拨测间隔
        :type Interval: int
        :param _Parameters: 拨测参数，详细可参考云拨测官方文档,链接:https://cloud.tencent.com/document/product/248/87308#createprobetasks。
        :type Parameters: str
        :param _TaskCategory: 任务分类
<li>1 = PC</li>
<li> 2 = Mobile </li>
        :type TaskCategory: int
        :param _Cron: 定时任务cron表达式
        :type Cron: str
        :param _Tag: 资源标签值
        :type Tag: list of Tag
        :param _ProbeType: 测试类型，包含定时测试与即时测试。0-定时拨测，其它表示即时拨测。
        :type ProbeType: int
        :param _PluginSource: 插件类型，如CDN，详情参考云拨测官方文档。
        :type PluginSource: str
        :param _ClientNum: 客户端ID
        :type ClientNum: str
        :param _NodeIpType: 拨测点IP类型：0-不限制IP类型，1-IPv4，2-IPv6
        :type NodeIpType: int
        """
        self._BatchTasks = None
        self._TaskType = None
        self._Nodes = None
        self._Interval = None
        self._Parameters = None
        self._TaskCategory = None
        self._Cron = None
        self._Tag = None
        self._ProbeType = None
        self._PluginSource = None
        self._ClientNum = None
        self._NodeIpType = None

    @property
    def BatchTasks(self):
        return self._BatchTasks

    @BatchTasks.setter
    def BatchTasks(self, BatchTasks):
        self._BatchTasks = BatchTasks

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def TaskCategory(self):
        return self._TaskCategory

    @TaskCategory.setter
    def TaskCategory(self, TaskCategory):
        self._TaskCategory = TaskCategory

    @property
    def Cron(self):
        return self._Cron

    @Cron.setter
    def Cron(self, Cron):
        self._Cron = Cron

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def ProbeType(self):
        return self._ProbeType

    @ProbeType.setter
    def ProbeType(self, ProbeType):
        self._ProbeType = ProbeType

    @property
    def PluginSource(self):
        return self._PluginSource

    @PluginSource.setter
    def PluginSource(self, PluginSource):
        self._PluginSource = PluginSource

    @property
    def ClientNum(self):
        return self._ClientNum

    @ClientNum.setter
    def ClientNum(self, ClientNum):
        self._ClientNum = ClientNum

    @property
    def NodeIpType(self):
        return self._NodeIpType

    @NodeIpType.setter
    def NodeIpType(self, NodeIpType):
        self._NodeIpType = NodeIpType


    def _deserialize(self, params):
        if params.get("BatchTasks") is not None:
            self._BatchTasks = []
            for item in params.get("BatchTasks"):
                obj = ProbeTaskBasicConfiguration()
                obj._deserialize(item)
                self._BatchTasks.append(obj)
        self._TaskType = params.get("TaskType")
        self._Nodes = params.get("Nodes")
        self._Interval = params.get("Interval")
        self._Parameters = params.get("Parameters")
        self._TaskCategory = params.get("TaskCategory")
        self._Cron = params.get("Cron")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        self._ProbeType = params.get("ProbeType")
        self._PluginSource = params.get("PluginSource")
        self._ClientNum = params.get("ClientNum")
        self._NodeIpType = params.get("NodeIpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProbeTasksResponse(AbstractModel):
    """CreateProbeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIDs: 任务ID列表
        :type TaskIDs: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskIDs = None
        self._RequestId = None

    @property
    def TaskIDs(self):
        return self._TaskIDs

    @TaskIDs.setter
    def TaskIDs(self, TaskIDs):
        self._TaskIDs = TaskIDs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskIDs = params.get("TaskIDs")
        self._RequestId = params.get("RequestId")


class DeleteProbeTaskRequest(AbstractModel):
    """DeleteProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self._TaskIds = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProbeTaskResponse(AbstractModel):
    """DeleteProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 任务总量
        :type Total: int
        :param _SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param _Results: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._SuccessCount = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDetailedSingleProbeDataRequest(AbstractModel):
    """DescribeDetailedSingleProbeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 开始时间戳（毫秒级）
        :type BeginTime: int
        :param _EndTime: 结束时间戳（毫秒级）
        :type EndTime: int
        :param _TaskType: 任务类型
AnalyzeTaskType_Network：网络质量
AnalyzeTaskType_Browse：页面性能
AnalyzeTaskType_UploadDownload：文件传输（含文件上传、文件下载）
AnalyzeTaskType_Transport：端口性能
AnalyzeTaskType_MediaStream：音视频体验
        :type TaskType: str
        :param _SortField: 待排序字段
可以填写 ProbeTime 拨测时间排序
也可填写SelectedFields 中的选中字段
        :type SortField: str
        :param _Ascending: true表示升序
        :type Ascending: bool
        :param _SelectedFields: 选中字段，如ProbeTime、TransferTime、TransferSize等。
        :type SelectedFields: list of str
        :param _Offset: 起始取数位置
        :type Offset: int
        :param _Limit: 取数数量
        :type Limit: int
        :param _TaskID: 任务ID
        :type TaskID: list of str
        :param _Operators: 拨测点运营商
	
这里实际按拨测结果中的运营商来填写即可

电信：中国电信
移动：中国移动
联通：中国联通
        :type Operators: list of str
        :param _Districts: 拨测点地区
	
这里实际按拨测结果中的地区来填写即可

国内一般是省级单位，如广东、广西、中国香港；直辖市则填北京、上海

境外一般是国家名，如澳大利亚、新加坡
        :type Districts: list of str
        :param _ErrorTypes: 错误类型
        :type ErrorTypes: list of str
        :param _City: 城市
这里实际按拨测结果中的城市来填写即可

示例：

深圳市
武汉市
首尔
多伦多
        :type City: list of str
        :param _ScrollID: es scroll查询id
        :type ScrollID: str
        :param _QueryFlag: 详情数据下载
        :type QueryFlag: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._TaskType = None
        self._SortField = None
        self._Ascending = None
        self._SelectedFields = None
        self._Offset = None
        self._Limit = None
        self._TaskID = None
        self._Operators = None
        self._Districts = None
        self._ErrorTypes = None
        self._City = None
        self._ScrollID = None
        self._QueryFlag = None

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
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def SortField(self):
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def Ascending(self):
        return self._Ascending

    @Ascending.setter
    def Ascending(self, Ascending):
        self._Ascending = Ascending

    @property
    def SelectedFields(self):
        return self._SelectedFields

    @SelectedFields.setter
    def SelectedFields(self, SelectedFields):
        self._SelectedFields = SelectedFields

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
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Operators(self):
        return self._Operators

    @Operators.setter
    def Operators(self, Operators):
        self._Operators = Operators

    @property
    def Districts(self):
        return self._Districts

    @Districts.setter
    def Districts(self, Districts):
        self._Districts = Districts

    @property
    def ErrorTypes(self):
        return self._ErrorTypes

    @ErrorTypes.setter
    def ErrorTypes(self, ErrorTypes):
        self._ErrorTypes = ErrorTypes

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def ScrollID(self):
        return self._ScrollID

    @ScrollID.setter
    def ScrollID(self, ScrollID):
        self._ScrollID = ScrollID

    @property
    def QueryFlag(self):
        return self._QueryFlag

    @QueryFlag.setter
    def QueryFlag(self, QueryFlag):
        self._QueryFlag = QueryFlag


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._TaskType = params.get("TaskType")
        self._SortField = params.get("SortField")
        self._Ascending = params.get("Ascending")
        self._SelectedFields = params.get("SelectedFields")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TaskID = params.get("TaskID")
        self._Operators = params.get("Operators")
        self._Districts = params.get("Districts")
        self._ErrorTypes = params.get("ErrorTypes")
        self._City = params.get("City")
        self._ScrollID = params.get("ScrollID")
        self._QueryFlag = params.get("QueryFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDetailedSingleProbeDataResponse(AbstractModel):
    """DescribeDetailedSingleProbeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataSet: 单次详情数据
        :type DataSet: list of DetailedSingleDataDefine
        :param _TotalNumber: 符合条件的数据总数
        :type TotalNumber: int
        :param _ScrollID: es scroll查询的id
        :type ScrollID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataSet = None
        self._TotalNumber = None
        self._ScrollID = None
        self._RequestId = None

    @property
    def DataSet(self):
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet

    @property
    def TotalNumber(self):
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def ScrollID(self):
        return self._ScrollID

    @ScrollID.setter
    def ScrollID(self, ScrollID):
        self._ScrollID = ScrollID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataSet") is not None:
            self._DataSet = []
            for item in params.get("DataSet"):
                obj = DetailedSingleDataDefine()
                obj._deserialize(item)
                self._DataSet.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._ScrollID = params.get("ScrollID")
        self._RequestId = params.get("RequestId")


class DescribeInstantTasksRequest(AbstractModel):
    """DescribeInstantTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量
        :type Limit: int
        :param _Offset: 起始位置
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstantTasksResponse(AbstractModel):
    """DescribeInstantTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of SingleInstantTask
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._Total = None
        self._RequestId = None

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = SingleInstantTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeNodesRequest(AbstractModel):
    """DescribeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type NodeType: int
        :param _Location: 节点区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 境外</li>
        :type Location: int
        :param _IsIPv6: 是否IPv6
        :type IsIPv6: bool
        :param _NodeName: 名字模糊搜索
        :type NodeName: str
        :param _PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param _TaskType: 任务类型
<li>1 = 页面性能</li>
<li>2 = 文件上传</li>
<li>3 = 文件下载</li>
<li>4 = 端口性能</li>
<li>5 = 网络质量</li>
<li>6 = 音视频体验</li>
        :type TaskType: int
        """
        self._NodeType = None
        self._Location = None
        self._IsIPv6 = None
        self._NodeName = None
        self._PayMode = None
        self._TaskType = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def IsIPv6(self):
        return self._IsIPv6

    @IsIPv6.setter
    def IsIPv6(self, IsIPv6):
        self._IsIPv6 = IsIPv6

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._Location = params.get("Location")
        self._IsIPv6 = params.get("IsIPv6")
        self._NodeName = params.get("NodeName")
        self._PayMode = params.get("PayMode")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodesResponse(AbstractModel):
    """DescribeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeSet: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of NodeDefineExt
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeSet = None
        self._RequestId = None

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeDefineExt()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProbeMetricDataRequest(AbstractModel):
    """DescribeProbeMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AnalyzeTaskType: 分析任务类型，支持以下几种类型：
AnalyzeTaskType_Network：网络质量
AnalyzeTaskType_Browse：页面性能
AnalyzeTaskType_Transport：端口性能
AnalyzeTaskType_UploadDownload：文件传输
AnalyzeTaskType_MediaStream：音视频体验
        :type AnalyzeTaskType: str
        :param _MetricType: 指标类型（counter、gauge以及histogram），指标查询默认传gauge
        :type MetricType: str
        :param _Field: 指标详细字段，可以传递传具体的指标也可以对指标进行聚合查询例如："avg(ping_time)"代表整体时延(ms)；不同的任务类型支持不同的field查询，以及聚合规则，详情可见https://cloud.tencent.com/document/product/248/87584。
        :type Field: str
        :param _Filter: 过滤条件可以传单个过滤条件也可以拼接多个参数
        :type Filter: str
        :param _GroupBy: 聚合时间, 1m、1d、30d 等等
        :type GroupBy: str
        :param _Filters: 多条件过滤，支持多个过滤条件组合查询
例如：[""host" = 'www.test.com'", "time >= now()-1h"]
        :type Filters: list of str
        """
        self._AnalyzeTaskType = None
        self._MetricType = None
        self._Field = None
        self._Filter = None
        self._GroupBy = None
        self._Filters = None

    @property
    def AnalyzeTaskType(self):
        return self._AnalyzeTaskType

    @AnalyzeTaskType.setter
    def AnalyzeTaskType(self, AnalyzeTaskType):
        self._AnalyzeTaskType = AnalyzeTaskType

    @property
    def MetricType(self):
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AnalyzeTaskType = params.get("AnalyzeTaskType")
        self._MetricType = params.get("MetricType")
        self._Field = params.get("Field")
        self._Filter = params.get("Filter")
        self._GroupBy = params.get("GroupBy")
        self._Filters = params.get("Filters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeMetricDataResponse(AbstractModel):
    """DescribeProbeMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricSet: 返回指标 JSON 序列化后的字符串,具体如下所示：
"[{\"name\":\"task_navigate_request_gauge\",\"columns\":[\"time\",\"avg(first_screen_time) / 1000\"],\"values\":[[1641571200,6.756600000000001]],\"tags\":null}]"
        :type MetricSet: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricSet = None
        self._RequestId = None

    @property
    def MetricSet(self):
        return self._MetricSet

    @MetricSet.setter
    def MetricSet(self, MetricSet):
        self._MetricSet = MetricSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MetricSet = params.get("MetricSet")
        self._RequestId = params.get("RequestId")


class DescribeProbeNodesRequest(AbstractModel):
    """DescribeProbeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeType: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type NodeType: int
        :param _Location: 节点区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 海外 </li>
        :type Location: int
        :param _IsIPv6: 是否IPv6
        :type IsIPv6: bool
        :param _NodeName: 名字模糊搜索
        :type NodeName: str
        :param _PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        """
        self._NodeType = None
        self._Location = None
        self._IsIPv6 = None
        self._NodeName = None
        self._PayMode = None

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def IsIPv6(self):
        return self._IsIPv6

    @IsIPv6.setter
    def IsIPv6(self, IsIPv6):
        self._IsIPv6 = IsIPv6

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._NodeType = params.get("NodeType")
        self._Location = params.get("Location")
        self._IsIPv6 = params.get("IsIPv6")
        self._NodeName = params.get("NodeName")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeNodesResponse(AbstractModel):
    """DescribeProbeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeSet: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of NodeDefine
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeSet = None
        self._RequestId = None

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeDefine()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProbeTasksRequest(AbstractModel):
    """DescribeProbeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIDs: 任务 ID  列表
        :type TaskIDs: list of str
        :param _TaskName: 任务名
        :type TaskName: str
        :param _TargetAddress: 拨测目标
        :type TargetAddress: str
        :param _TaskStatus: 任务状态列表
<li>1 = 创建中</li>
<li> 2 = 运行中 </li>
<li> 3 = 运行异常 </li>
<li> 4 = 暂停中 </li>
<li> 5 = 暂停异常 </li>
<li> 6 = 任务暂停 </li>
<li> 7 = 任务删除中 </li>
<li> 8 = 任务删除异常 </li>
<li> 9 = 任务删除</li>
<li> 10 = 定时任务暂停中 </li>
        :type TaskStatus: list of int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param _OrderState: 订单状态
<li>1 = 正常</li>
<li> 2 = 欠费 </li>
        :type OrderState: int
        :param _TaskType: 拨测类型
<li>1 = 页面浏览</li>
<li> 2 =文件上传 </li>
<li> 3 = 文件下载</li>
<li> 4 = 端口性能 </li>
<li> 5 = 网络质量 </li>
<li> 6 =流媒体 </li>

即使拨测只支持页面浏览，网络质量，文件下载
        :type TaskType: list of int
        :param _TaskCategory: 节点类型
        :type TaskCategory: list of int
        :param _OrderBy: 排序的列
        :type OrderBy: str
        :param _Ascend: 是否正序
        :type Ascend: bool
        :param _TagFilters: 资源标签值
        :type TagFilters: list of KeyValuePair
        """
        self._TaskIDs = None
        self._TaskName = None
        self._TargetAddress = None
        self._TaskStatus = None
        self._Offset = None
        self._Limit = None
        self._PayMode = None
        self._OrderState = None
        self._TaskType = None
        self._TaskCategory = None
        self._OrderBy = None
        self._Ascend = None
        self._TagFilters = None

    @property
    def TaskIDs(self):
        return self._TaskIDs

    @TaskIDs.setter
    def TaskIDs(self, TaskIDs):
        self._TaskIDs = TaskIDs

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TargetAddress(self):
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

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
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def OrderState(self):
        return self._OrderState

    @OrderState.setter
    def OrderState(self, OrderState):
        self._OrderState = OrderState

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskCategory(self):
        return self._TaskCategory

    @TaskCategory.setter
    def TaskCategory(self, TaskCategory):
        self._TaskCategory = TaskCategory

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._TaskIDs = params.get("TaskIDs")
        self._TaskName = params.get("TaskName")
        self._TargetAddress = params.get("TargetAddress")
        self._TaskStatus = params.get("TaskStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PayMode = params.get("PayMode")
        self._OrderState = params.get("OrderState")
        self._TaskType = params.get("TaskType")
        self._TaskCategory = params.get("TaskCategory")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = KeyValuePair()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeTasksResponse(AbstractModel):
    """DescribeProbeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSet: list of ProbeTask
        :param _Total: 任务总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskSet(self):
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

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
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = ProbeTask()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DetailedSingleDataDefine(AbstractModel):
    """单条详细拨测数据

    """

    def __init__(self):
        r"""
        :param _ProbeTime: 拨测时间戳
        :type ProbeTime: int
        :param _Labels: 储存所有string类型字段
        :type Labels: list of Label
        :param _Fields: 储存所有float类型字段
        :type Fields: list of Field
        """
        self._ProbeTime = None
        self._Labels = None
        self._Fields = None

    @property
    def ProbeTime(self):
        return self._ProbeTime

    @ProbeTime.setter
    def ProbeTime(self, ProbeTime):
        self._ProbeTime = ProbeTime

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Fields(self):
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._ProbeTime = params.get("ProbeTime")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Fields") is not None:
            self._Fields = []
            for item in params.get("Fields"):
                obj = Field()
                obj._deserialize(item)
                self._Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Field(AbstractModel):
    """储存float类型字段

    """

    def __init__(self):
        r"""
        :param _ID: 自定义字段编号
        :type ID: int
        :param _Name: 自定义字段名称/说明
        :type Name: str
        :param _Value: 字段值
        :type Value: float
        """
        self._ID = None
        self._Name = None
        self._Value = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValuePair(AbstractModel):
    """健值对

    """

    def __init__(self):
        r"""
        :param _Key: 健
        :type Key: str
        :param _Value: 值
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
        


class Label(AbstractModel):
    """保存string类型字段

    """

    def __init__(self):
        r"""
        :param _ID: 自定义字段编号
        :type ID: int
        :param _Name: 自定义字段名称/说明
        :type Name: str
        :param _Value: 字段值
        :type Value: str
        """
        self._ID = None
        self._Name = None
        self._Value = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeDefine(AbstractModel):
    """探测节点

    """

    def __init__(self):
        r"""
        :param _Name: 节点名称
        :type Name: str
        :param _Code: 节点代码
        :type Code: str
        :param _Type: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type Type: int
        :param _NetService: 网络服务商
        :type NetService: str
        :param _District: 区域
        :type District: str
        :param _City: 城市
        :type City: str
        :param _IPType: IP 类型
<li> 1 = IPv4 </li>
<li> 2 = IPv6 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IPType: int
        :param _Location: 区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 国外 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: int
        :param _CodeType: 节点类型  如果为base 则为可用性拨测点，为空则为高级拨测点
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: str
        :param _NodeDefineStatus: 节点状态：1-运行,2-下线
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeDefineStatus: int
        """
        self._Name = None
        self._Code = None
        self._Type = None
        self._NetService = None
        self._District = None
        self._City = None
        self._IPType = None
        self._Location = None
        self._CodeType = None
        self._NodeDefineStatus = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NetService(self):
        return self._NetService

    @NetService.setter
    def NetService(self, NetService):
        self._NetService = NetService

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def IPType(self):
        return self._IPType

    @IPType.setter
    def IPType(self, IPType):
        self._IPType = IPType

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def NodeDefineStatus(self):
        return self._NodeDefineStatus

    @NodeDefineStatus.setter
    def NodeDefineStatus(self, NodeDefineStatus):
        self._NodeDefineStatus = NodeDefineStatus


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Code = params.get("Code")
        self._Type = params.get("Type")
        self._NetService = params.get("NetService")
        self._District = params.get("District")
        self._City = params.get("City")
        self._IPType = params.get("IPType")
        self._Location = params.get("Location")
        self._CodeType = params.get("CodeType")
        self._NodeDefineStatus = params.get("NodeDefineStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeDefineExt(AbstractModel):
    """探测节点

    """

    def __init__(self):
        r"""
        :param _Name: 节点名称
        :type Name: str
        :param _Code: 节点代码
        :type Code: str
        :param _Type: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type Type: int
        :param _NetService: 网络服务商
        :type NetService: str
        :param _District: 区域
        :type District: str
        :param _City: 城市
        :type City: str
        :param _IPType: IP 类型
<li> 1 = IPv4 </li>
<li> 2 = IPv6 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IPType: int
        :param _Location: 区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 境外 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: int
        :param _CodeType: 节点类型  如果为base 则为可用性拨测点，为空则为高级拨测点
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: str
        :param _TaskTypes: 节点支持的任务类型。1: 页面性能 2: 文件上传 3: 文件下载 4: 端口性能 5: 网络质量 6: 音视频体验
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypes: list of int
        """
        self._Name = None
        self._Code = None
        self._Type = None
        self._NetService = None
        self._District = None
        self._City = None
        self._IPType = None
        self._Location = None
        self._CodeType = None
        self._TaskTypes = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NetService(self):
        return self._NetService

    @NetService.setter
    def NetService(self, NetService):
        self._NetService = NetService

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def IPType(self):
        return self._IPType

    @IPType.setter
    def IPType(self, IPType):
        self._IPType = IPType

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def CodeType(self):
        return self._CodeType

    @CodeType.setter
    def CodeType(self, CodeType):
        self._CodeType = CodeType

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Code = params.get("Code")
        self._Type = params.get("Type")
        self._NetService = params.get("NetService")
        self._District = params.get("District")
        self._City = params.get("City")
        self._IPType = params.get("IPType")
        self._Location = params.get("Location")
        self._CodeType = params.get("CodeType")
        self._TaskTypes = params.get("TaskTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProbeTask(AbstractModel):
    """拨测任务

    """

    def __init__(self):
        r"""
        :param _Name: 任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _TaskType: 拨测类型
<li>1 = 页面浏览</li>
<li> 2 =文件上传 </li>
<li> 3 = 文件下载</li>
<li> 4 = 端口性能 </li>
<li> 5 = 网络质量 </li>
<li> 6 =流媒体 </li>

即时拨测只支持页面浏览，网络质量，文件下载
        :type TaskType: int
        :param _Nodes: 拨测节点列表
        :type Nodes: list of str
        :param _NodeIpType: 拨测任务所选的拨测点IP类型，0-不限，1-IPv4，2-IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeIpType: int
        :param _Interval: 拨测间隔
        :type Interval: int
        :param _Parameters: 拨测参数
        :type Parameters: str
        :param _Status: 任务状态
<li>1 = 创建中</li>
<li> 2 = 运行中 </li>
<li> 3 = 运行异常 </li>
<li> 4 = 暂停中 </li>
<li> 5 = 暂停异常 </li>
<li> 6 = 任务暂停 </li>
<li> 7 = 任务删除中 </li>
<li> 8 = 任务删除异常 </li>
<li> 9 = 任务删除</li>
<li> 10 = 定时任务暂停中 </li>
        :type Status: int
        :param _TargetAddress: 目标地址
        :type TargetAddress: str
        :param _PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param _OrderState: 订单状态
<li>1 = 正常</li>
<li> 2 = 欠费 </li>
        :type OrderState: int
        :param _TaskCategory: 任务分类
<li>1 = PC</li>
<li> 2 = Mobile </li>
        :type TaskCategory: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _Cron: 定时任务cron表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type Cron: str
        :param _CronState: 定时任务启动状态
<li>1 = 定时任务表达式生效</li>
<li> 2 = 定时任务表达式未生效（一般为任务手动暂停）</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type CronState: int
        :param _TagInfoList: 任务当前绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfoList: list of KeyValuePair
        """
        self._Name = None
        self._TaskId = None
        self._TaskType = None
        self._Nodes = None
        self._NodeIpType = None
        self._Interval = None
        self._Parameters = None
        self._Status = None
        self._TargetAddress = None
        self._PayMode = None
        self._OrderState = None
        self._TaskCategory = None
        self._CreatedAt = None
        self._Cron = None
        self._CronState = None
        self._TagInfoList = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def NodeIpType(self):
        return self._NodeIpType

    @NodeIpType.setter
    def NodeIpType(self, NodeIpType):
        self._NodeIpType = NodeIpType

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TargetAddress(self):
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def OrderState(self):
        return self._OrderState

    @OrderState.setter
    def OrderState(self, OrderState):
        self._OrderState = OrderState

    @property
    def TaskCategory(self):
        return self._TaskCategory

    @TaskCategory.setter
    def TaskCategory(self, TaskCategory):
        self._TaskCategory = TaskCategory

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Cron(self):
        return self._Cron

    @Cron.setter
    def Cron(self, Cron):
        self._Cron = Cron

    @property
    def CronState(self):
        return self._CronState

    @CronState.setter
    def CronState(self, CronState):
        self._CronState = CronState

    @property
    def TagInfoList(self):
        return self._TagInfoList

    @TagInfoList.setter
    def TagInfoList(self, TagInfoList):
        self._TagInfoList = TagInfoList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._Nodes = params.get("Nodes")
        self._NodeIpType = params.get("NodeIpType")
        self._Interval = params.get("Interval")
        self._Parameters = params.get("Parameters")
        self._Status = params.get("Status")
        self._TargetAddress = params.get("TargetAddress")
        self._PayMode = params.get("PayMode")
        self._OrderState = params.get("OrderState")
        self._TaskCategory = params.get("TaskCategory")
        self._CreatedAt = params.get("CreatedAt")
        self._Cron = params.get("Cron")
        self._CronState = params.get("CronState")
        if params.get("TagInfoList") is not None:
            self._TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = KeyValuePair()
                obj._deserialize(item)
                self._TagInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProbeTaskBasicConfiguration(AbstractModel):
    """拨测任务基础配置

    """

    def __init__(self):
        r"""
        :param _Name: 拨测任务名称
        :type Name: str
        :param _TargetAddress: 拨测目标地址
        :type TargetAddress: str
        """
        self._Name = None
        self._TargetAddress = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TargetAddress(self):
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TargetAddress = params.get("TargetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProbeTaskRequest(AbstractModel):
    """ResumeProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self._TaskIds = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProbeTaskResponse(AbstractModel):
    """ResumeProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 任务总量
        :type Total: int
        :param _SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param _Results: 任务执行详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._SuccessCount = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class SingleInstantTask(AbstractModel):
    """单个即时拨测任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TargetAddress: 任务地址
        :type TargetAddress: str
        :param _TaskType: 任务类型
        :type TaskType: int
        :param _ProbeTime: 测试时间
        :type ProbeTime: int
        :param _Status: 任务状态
        :type Status: str
        :param _SuccessRate: 成功率
        :type SuccessRate: float
        :param _NodeCount: 节点数量
        :type NodeCount: int
        :param _TaskCategory: 节点类型
        :type TaskCategory: int
        """
        self._TaskId = None
        self._TargetAddress = None
        self._TaskType = None
        self._ProbeTime = None
        self._Status = None
        self._SuccessRate = None
        self._NodeCount = None
        self._TaskCategory = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TargetAddress(self):
        return self._TargetAddress

    @TargetAddress.setter
    def TargetAddress(self, TargetAddress):
        self._TargetAddress = TargetAddress

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ProbeTime(self):
        return self._ProbeTime

    @ProbeTime.setter
    def ProbeTime(self, ProbeTime):
        self._ProbeTime = ProbeTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuccessRate(self):
        return self._SuccessRate

    @SuccessRate.setter
    def SuccessRate(self, SuccessRate):
        self._SuccessRate = SuccessRate

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def TaskCategory(self):
        return self._TaskCategory

    @TaskCategory.setter
    def TaskCategory(self, TaskCategory):
        self._TaskCategory = TaskCategory


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TargetAddress = params.get("TargetAddress")
        self._TaskType = params.get("TaskType")
        self._ProbeTime = params.get("ProbeTime")
        self._Status = params.get("Status")
        self._SuccessRate = params.get("SuccessRate")
        self._NodeCount = params.get("NodeCount")
        self._TaskCategory = params.get("TaskCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendProbeTaskRequest(AbstractModel):
    """SuspendProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self._TaskIds = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendProbeTaskResponse(AbstractModel):
    """SuspendProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 任务总量
        :type Total: int
        :param _SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param _Results: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._SuccessCount = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """资源的标签，通过标签对资源进行划分用于支持细粒度的鉴权、分账等场景

    """

    def __init__(self):
        r"""
        :param _TagKey: key
        :type TagKey: str
        :param _TagValue: value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """任务执行结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _Success: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: bool
        :param _ErrorMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        """
        self._TaskId = None
        self._Success = None
        self._ErrorMessage = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Success = params.get("Success")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProbeTaskAttributesRequest(AbstractModel):
    """UpdateProbeTaskAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务 ID
        :type TaskId: str
        :param _Name: 任务名
        :type Name: str
        """
        self._TaskId = None
        self._Name = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProbeTaskAttributesResponse(AbstractModel):
    """UpdateProbeTaskAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UpdateProbeTaskConfigurationListRequest(AbstractModel):
    """UpdateProbeTaskConfigurationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务 ID，如task-n1wchki8
        :type TaskIds: list of str
        :param _Nodes: 拨测节点，如10001，详细地区运营商拨测编号请联系云拨测。
        :type Nodes: list of str
        :param _Interval: 拨测间隔，如30，单位为分钟。
        :type Interval: int
        :param _Parameters: 拨测参数，详细参数配置可参考云拨测官网文档。
        :type Parameters: str
        :param _Cron: 定时任务cron表达式
        :type Cron: str
        :param _ResourceIDs: 预付费套餐id
需要与taskId对应
        :type ResourceIDs: list of str
        :param _NodeIpType: 拨测节点的IP类型，0-不限，1-IPv4，2-IPv6
        :type NodeIpType: int
        """
        self._TaskIds = None
        self._Nodes = None
        self._Interval = None
        self._Parameters = None
        self._Cron = None
        self._ResourceIDs = None
        self._NodeIpType = None

    @property
    def TaskIds(self):
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Cron(self):
        return self._Cron

    @Cron.setter
    def Cron(self, Cron):
        self._Cron = Cron

    @property
    def ResourceIDs(self):
        return self._ResourceIDs

    @ResourceIDs.setter
    def ResourceIDs(self, ResourceIDs):
        self._ResourceIDs = ResourceIDs

    @property
    def NodeIpType(self):
        return self._NodeIpType

    @NodeIpType.setter
    def NodeIpType(self, NodeIpType):
        self._NodeIpType = NodeIpType


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        self._Nodes = params.get("Nodes")
        self._Interval = params.get("Interval")
        self._Parameters = params.get("Parameters")
        self._Cron = params.get("Cron")
        self._ResourceIDs = params.get("ResourceIDs")
        self._NodeIpType = params.get("NodeIpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProbeTaskConfigurationListResponse(AbstractModel):
    """UpdateProbeTaskConfigurationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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