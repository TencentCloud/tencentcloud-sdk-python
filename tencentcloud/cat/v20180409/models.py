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
        :param BatchTasks: 批量任务名-地址
        :type BatchTasks: list of ProbeTaskBasicConfiguration
        :param TaskType: 任务类型
        :type TaskType: int
        :param Nodes: 拨测节点
        :type Nodes: list of str
        :param Interval: 拨测间隔
        :type Interval: int
        :param Parameters: 拨测参数
        :type Parameters: str
        :param TaskCategory: 任务分类
<li>1 = PC</li>
<li> 2 = Mobile </li>
        :type TaskCategory: int
        :param Cron: 定时任务cron表达式
        :type Cron: str
        :param Tag: 资源标签值
        :type Tag: list of Tag
        :param ProbeType: 测试类型，包含定时测试与即时测试
        :type ProbeType: int
        :param PluginSource: 插件类型
        :type PluginSource: str
        :param ClientNum: 客户端ID
        :type ClientNum: str
        """
        self.BatchTasks = None
        self.TaskType = None
        self.Nodes = None
        self.Interval = None
        self.Parameters = None
        self.TaskCategory = None
        self.Cron = None
        self.Tag = None
        self.ProbeType = None
        self.PluginSource = None
        self.ClientNum = None


    def _deserialize(self, params):
        if params.get("BatchTasks") is not None:
            self.BatchTasks = []
            for item in params.get("BatchTasks"):
                obj = ProbeTaskBasicConfiguration()
                obj._deserialize(item)
                self.BatchTasks.append(obj)
        self.TaskType = params.get("TaskType")
        self.Nodes = params.get("Nodes")
        self.Interval = params.get("Interval")
        self.Parameters = params.get("Parameters")
        self.TaskCategory = params.get("TaskCategory")
        self.Cron = params.get("Cron")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.ProbeType = params.get("ProbeType")
        self.PluginSource = params.get("PluginSource")
        self.ClientNum = params.get("ClientNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProbeTasksResponse(AbstractModel):
    """CreateProbeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIDs: 任务ID列表
        :type TaskIDs: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskIDs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIDs = params.get("TaskIDs")
        self.RequestId = params.get("RequestId")


class DeleteProbeTaskRequest(AbstractModel):
    """DeleteProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProbeTaskResponse(AbstractModel):
    """DeleteProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 任务总量
        :type Total: int
        :param SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param Results: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.SuccessCount = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDetailedSingleProbeDataRequest(AbstractModel):
    """DescribeDetailedSingleProbeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginTime: 开始时间戳（毫秒级）
        :type BeginTime: int
        :param EndTime: 结束时间戳（毫秒级）
        :type EndTime: int
        :param TaskType: 任务类型
AnalyzeTaskType_Network：网络质量
AnalyzeTaskType_Browse：页面性能
AnalyzeTaskType_UploadDownload：文件传输（含文件上传、文件下载）
AnalyzeTaskType_Transport：端口性能
AnalyzeTaskType_MediaStream：音视频体验
        :type TaskType: str
        :param SortField: 待排序字段
可以填写 ProbeTime 拨测时间排序
也可填写SelectedFields 中的选中字段
        :type SortField: str
        :param Ascending: true表示升序
        :type Ascending: bool
        :param SelectedFields: 选中字段
        :type SelectedFields: list of str
        :param Offset: 起始取数位置
        :type Offset: int
        :param Limit: 取数数量
        :type Limit: int
        :param TaskID: 任务ID
        :type TaskID: list of str
        :param Operators: 拨测点运营商
	
这里实际按拨测结果中的运营商来填写即可

电信：中国电信
移动：中国移动
联通：中国联通
        :type Operators: list of str
        :param Districts: 拨测点地区
	
这里实际按拨测结果中的地区来填写即可

国内一般是省级单位，如广东、广西、中国香港、新疆；直辖市则填北京、上海

境外一般是国家名，如澳大利亚、新加坡
        :type Districts: list of str
        :param ErrorTypes: 错误类型
        :type ErrorTypes: list of str
        :param City: 城市
这里实际按拨测结果中的城市来填写即可

示例：

深圳市
武汉市
首尔
多伦多
        :type City: list of str
        """
        self.BeginTime = None
        self.EndTime = None
        self.TaskType = None
        self.SortField = None
        self.Ascending = None
        self.SelectedFields = None
        self.Offset = None
        self.Limit = None
        self.TaskID = None
        self.Operators = None
        self.Districts = None
        self.ErrorTypes = None
        self.City = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TaskType = params.get("TaskType")
        self.SortField = params.get("SortField")
        self.Ascending = params.get("Ascending")
        self.SelectedFields = params.get("SelectedFields")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TaskID = params.get("TaskID")
        self.Operators = params.get("Operators")
        self.Districts = params.get("Districts")
        self.ErrorTypes = params.get("ErrorTypes")
        self.City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDetailedSingleProbeDataResponse(AbstractModel):
    """DescribeDetailedSingleProbeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataSet: 单次详情数据
        :type DataSet: list of DetailedSingleDataDefine
        :param TotalNumber: 符合条件的数据总数
        :type TotalNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataSet = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataSet") is not None:
            self.DataSet = []
            for item in params.get("DataSet"):
                obj = DetailedSingleDataDefine()
                obj._deserialize(item)
                self.DataSet.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeNodesRequest(AbstractModel):
    """DescribeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeType: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type NodeType: int
        :param Location: 节点区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 境外</li>
        :type Location: int
        :param IsIPv6: 是否IPv6
        :type IsIPv6: bool
        :param NodeName: 名字模糊搜索
        :type NodeName: str
        :param PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param TaskType: 任务类型
<li>1 = 页面性能</li>
<li>2 = 文件上传</li>
<li>3 = 文件下载</li>
<li>4 = 端口性能</li>
<li>5 = 网络质量</li>
<li>6 = 音视频体验</li>
        :type TaskType: int
        """
        self.NodeType = None
        self.Location = None
        self.IsIPv6 = None
        self.NodeName = None
        self.PayMode = None
        self.TaskType = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.Location = params.get("Location")
        self.IsIPv6 = params.get("IsIPv6")
        self.NodeName = params.get("NodeName")
        self.PayMode = params.get("PayMode")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodesResponse(AbstractModel):
    """DescribeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param NodeSet: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of NodeDefineExt
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeDefineExt()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProbeMetricDataRequest(AbstractModel):
    """DescribeProbeMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnalyzeTaskType: 分析任务类型，支持以下几种类型：
AnalyzeTaskType_Network：网络质量
AnalyzeTaskType_Browse：页面性能
AnalyzeTaskType_Transport：端口性能
AnalyzeTaskType_UploadDownload：文件传输
AnalyzeTaskType_MediaStream：音视频体验
        :type AnalyzeTaskType: str
        :param MetricType: 指标类型，指标查询默认传gauge
        :type MetricType: str
        :param Field: 指标详细字段，可以传递传具体的指标也可以对指标进行聚合查询例如："avg(ping_time)"代表整体时延(ms)
        :type Field: str
        :param Filter: 过滤条件可以传单个过滤条件也可以拼接多个参数
        :type Filter: str
        :param GroupBy: 聚合时间, 1m、1d、30d 等等
        :type GroupBy: str
        :param Filters: 多条件过滤，支持多个过滤条件组合查询
例如：[""host" = 'www.test.com'", "time >= now()-1h"]
        :type Filters: list of str
        """
        self.AnalyzeTaskType = None
        self.MetricType = None
        self.Field = None
        self.Filter = None
        self.GroupBy = None
        self.Filters = None


    def _deserialize(self, params):
        self.AnalyzeTaskType = params.get("AnalyzeTaskType")
        self.MetricType = params.get("MetricType")
        self.Field = params.get("Field")
        self.Filter = params.get("Filter")
        self.GroupBy = params.get("GroupBy")
        self.Filters = params.get("Filters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeMetricDataResponse(AbstractModel):
    """DescribeProbeMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricSet: 返回指标 JSON 序列化后的字符串,具体如下所示：
"[{\"name\":\"task_navigate_request_gauge\",\"columns\":[\"time\",\"avg(first_screen_time) / 1000\"],\"values\":[[1641571200,6.756600000000001]],\"tags\":null}]"
        :type MetricSet: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MetricSet = params.get("MetricSet")
        self.RequestId = params.get("RequestId")


class DescribeProbeNodesRequest(AbstractModel):
    """DescribeProbeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param NodeType: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type NodeType: int
        :param Location: 节点区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 海外 </li>
        :type Location: int
        :param IsIPv6: 是否IPv6
        :type IsIPv6: bool
        :param NodeName: 名字模糊搜索
        :type NodeName: str
        :param PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        """
        self.NodeType = None
        self.Location = None
        self.IsIPv6 = None
        self.NodeName = None
        self.PayMode = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.Location = params.get("Location")
        self.IsIPv6 = params.get("IsIPv6")
        self.NodeName = params.get("NodeName")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeNodesResponse(AbstractModel):
    """DescribeProbeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param NodeSet: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of NodeDefine
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeDefine()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProbeTasksRequest(AbstractModel):
    """DescribeProbeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIDs: 任务 ID  列表
        :type TaskIDs: list of str
        :param TaskName: 任务名
        :type TaskName: str
        :param TargetAddress: 拨测目标
        :type TargetAddress: str
        :param TaskStatus: 任务状态列表
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
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param OrderState: 订单状态
<li>1 = 正常</li>
<li> 2 = 欠费 </li>
        :type OrderState: int
        :param TaskType: 拨测类型
<li>1 = 页面浏览</li>
<li> 2 =文件上传 </li>
<li> 3 = 文件下载</li>
<li> 4 = 端口性能 </li>
<li> 5 = 网络质量 </li>
<li> 6 =流媒体 </li>

即使拨测只支持页面浏览，网络质量，文件下载
        :type TaskType: list of int
        :param TaskCategory: 节点类型
        :type TaskCategory: list of int
        :param OrderBy: 排序的列
        :type OrderBy: str
        :param Ascend: 是否正序
        :type Ascend: bool
        :param TagFilters: 资源标签值
        :type TagFilters: list of KeyValuePair
        """
        self.TaskIDs = None
        self.TaskName = None
        self.TargetAddress = None
        self.TaskStatus = None
        self.Offset = None
        self.Limit = None
        self.PayMode = None
        self.OrderState = None
        self.TaskType = None
        self.TaskCategory = None
        self.OrderBy = None
        self.Ascend = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.TaskIDs = params.get("TaskIDs")
        self.TaskName = params.get("TaskName")
        self.TargetAddress = params.get("TargetAddress")
        self.TaskStatus = params.get("TaskStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PayMode = params.get("PayMode")
        self.OrderState = params.get("OrderState")
        self.TaskType = params.get("TaskType")
        self.TaskCategory = params.get("TaskCategory")
        self.OrderBy = params.get("OrderBy")
        self.Ascend = params.get("Ascend")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = KeyValuePair()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProbeTasksResponse(AbstractModel):
    """DescribeProbeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskSet: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskSet: list of ProbeTask
        :param Total: 任务总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = ProbeTask()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DetailedSingleDataDefine(AbstractModel):
    """单条详细拨测数据

    """

    def __init__(self):
        r"""
        :param ProbeTime: 拨测时间戳
        :type ProbeTime: int
        :param Labels: 储存所有string类型字段
        :type Labels: list of Label
        :param Fields: 储存所有float类型字段
        :type Fields: list of Field
        """
        self.ProbeTime = None
        self.Labels = None
        self.Fields = None


    def _deserialize(self, params):
        self.ProbeTime = params.get("ProbeTime")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Fields") is not None:
            self.Fields = []
            for item in params.get("Fields"):
                obj = Field()
                obj._deserialize(item)
                self.Fields.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Field(AbstractModel):
    """储存float类型字段

    """

    def __init__(self):
        r"""
        :param ID: 自定义字段编号
        :type ID: int
        :param Name: 自定义字段名称/说明
        :type Name: str
        :param Value: 字段值
        :type Value: float
        """
        self.ID = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValuePair(AbstractModel):
    """健值对

    """

    def __init__(self):
        r"""
        :param Key: 健
        :type Key: str
        :param Value: 值
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
        


class Label(AbstractModel):
    """保存string类型字段

    """

    def __init__(self):
        r"""
        :param ID: 自定义字段编号
        :type ID: int
        :param Name: 自定义字段名称/说明
        :type Name: str
        :param Value: 字段值
        :type Value: str
        """
        self.ID = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeDefine(AbstractModel):
    """探测节点

    """

    def __init__(self):
        r"""
        :param Name: 节点名称
        :type Name: str
        :param Code: 节点代码
        :type Code: str
        :param Type: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type Type: int
        :param NetService: 网络服务商
        :type NetService: str
        :param District: 区域
        :type District: str
        :param City: 城市
        :type City: str
        :param IPType: IP 类型
<li> 1 = IPv4 </li>
<li> 2 = IPv6 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IPType: int
        :param Location: 区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 国外 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: int
        :param CodeType: 节点类型  如果为base 则为可用性拨测点，为空则为高级拨测点
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: str
        :param NodeDefineStatus: 节点状态：1-运行,2-下线
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeDefineStatus: int
        """
        self.Name = None
        self.Code = None
        self.Type = None
        self.NetService = None
        self.District = None
        self.City = None
        self.IPType = None
        self.Location = None
        self.CodeType = None
        self.NodeDefineStatus = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        self.NetService = params.get("NetService")
        self.District = params.get("District")
        self.City = params.get("City")
        self.IPType = params.get("IPType")
        self.Location = params.get("Location")
        self.CodeType = params.get("CodeType")
        self.NodeDefineStatus = params.get("NodeDefineStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeDefineExt(AbstractModel):
    """探测节点

    """

    def __init__(self):
        r"""
        :param Name: 节点名称
        :type Name: str
        :param Code: 节点代码
        :type Code: str
        :param Type: 节点类型
<li> 1 = IDC </li>
<li> 2 = LastMile </li>
<li> 3 = Mobile </li>
        :type Type: int
        :param NetService: 网络服务商
        :type NetService: str
        :param District: 区域
        :type District: str
        :param City: 城市
        :type City: str
        :param IPType: IP 类型
<li> 1 = IPv4 </li>
<li> 2 = IPv6 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IPType: int
        :param Location: 区域
<li> 1 = 中国大陆 </li>
<li> 2 = 港澳台 </li>
<li> 3 = 境外 </li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: int
        :param CodeType: 节点类型  如果为base 则为可用性拨测点，为空则为高级拨测点
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeType: str
        :param TaskTypes: 节点支持的任务类型。1: 页面性能 2: 文件上传 3: 文件下载 4: 端口性能 5: 网络质量 6: 音视频体验
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskTypes: list of int
        """
        self.Name = None
        self.Code = None
        self.Type = None
        self.NetService = None
        self.District = None
        self.City = None
        self.IPType = None
        self.Location = None
        self.CodeType = None
        self.TaskTypes = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        self.NetService = params.get("NetService")
        self.District = params.get("District")
        self.City = params.get("City")
        self.IPType = params.get("IPType")
        self.Location = params.get("Location")
        self.CodeType = params.get("CodeType")
        self.TaskTypes = params.get("TaskTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProbeTask(AbstractModel):
    """拨测任务

    """

    def __init__(self):
        r"""
        :param Name: 任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param TaskId: 任务 ID
        :type TaskId: str
        :param TaskType: 任务类型
        :type TaskType: int
        :param Nodes: 拨测节点列表
        :type Nodes: list of str
        :param Interval: 拨测间隔
        :type Interval: int
        :param Parameters: 拨测参数
        :type Parameters: str
        :param Status: 任务状态
        :type Status: int
        :param TargetAddress: 目标地址
        :type TargetAddress: str
        :param PayMode: 付费模式
<li>1 = 试用版本</li>
<li> 2 = 付费版本 </li>
        :type PayMode: int
        :param OrderState: 订单状态
<li>1 = 正常</li>
<li> 2 = 欠费 </li>
        :type OrderState: int
        :param TaskCategory: 任务分类
<li>1 = PC</li>
<li> 2 = Mobile </li>
        :type TaskCategory: int
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param Cron: 定时任务cron表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type Cron: str
        :param CronState: 定时任务启动状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CronState: int
        :param TagInfoList: 任务当前绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfoList: list of KeyValuePair
        """
        self.Name = None
        self.TaskId = None
        self.TaskType = None
        self.Nodes = None
        self.Interval = None
        self.Parameters = None
        self.Status = None
        self.TargetAddress = None
        self.PayMode = None
        self.OrderState = None
        self.TaskCategory = None
        self.CreatedAt = None
        self.Cron = None
        self.CronState = None
        self.TagInfoList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.Nodes = params.get("Nodes")
        self.Interval = params.get("Interval")
        self.Parameters = params.get("Parameters")
        self.Status = params.get("Status")
        self.TargetAddress = params.get("TargetAddress")
        self.PayMode = params.get("PayMode")
        self.OrderState = params.get("OrderState")
        self.TaskCategory = params.get("TaskCategory")
        self.CreatedAt = params.get("CreatedAt")
        self.Cron = params.get("Cron")
        self.CronState = params.get("CronState")
        if params.get("TagInfoList") is not None:
            self.TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = KeyValuePair()
                obj._deserialize(item)
                self.TagInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProbeTaskBasicConfiguration(AbstractModel):
    """拨测任务基础配置

    """

    def __init__(self):
        r"""
        :param Name: 拨测任务名称
        :type Name: str
        :param TargetAddress: 拨测目标地址
        :type TargetAddress: str
        """
        self.Name = None
        self.TargetAddress = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TargetAddress = params.get("TargetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProbeTaskRequest(AbstractModel):
    """ResumeProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProbeTaskResponse(AbstractModel):
    """ResumeProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 任务总量
        :type Total: int
        :param SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param Results: 任务执行详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.SuccessCount = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class SuspendProbeTaskRequest(AbstractModel):
    """SuspendProbeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuspendProbeTaskResponse(AbstractModel):
    """SuspendProbeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 任务总量
        :type Total: int
        :param SuccessCount: 任务成功量
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCount: int
        :param Results: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.SuccessCount = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.SuccessCount = params.get("SuccessCount")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """资源的标签，通过标签对资源进行划分用于支持细粒度的鉴权、分账等场景

    """

    def __init__(self):
        r"""
        :param TagKey: key
        :type TagKey: str
        :param TagValue: value
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """任务执行结果

    """

    def __init__(self):
        r"""
        :param TaskId: 任务 ID
        :type TaskId: str
        :param Success: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Success: bool
        :param ErrorMessage: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        """
        self.TaskId = None
        self.Success = None
        self.ErrorMessage = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Success = params.get("Success")
        self.ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProbeTaskConfigurationListRequest(AbstractModel):
    """UpdateProbeTaskConfigurationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskIds: 任务 ID
        :type TaskIds: list of str
        :param Nodes: 拨测节点
        :type Nodes: list of str
        :param Interval: 拨测间隔
        :type Interval: int
        :param Parameters: 拨测参数
        :type Parameters: str
        :param Cron: 定时任务cron表达式
        :type Cron: str
        :param ResourceIDs: 预付费套餐id
需要与taskId对应
        :type ResourceIDs: list of str
        """
        self.TaskIds = None
        self.Nodes = None
        self.Interval = None
        self.Parameters = None
        self.Cron = None
        self.ResourceIDs = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.Nodes = params.get("Nodes")
        self.Interval = params.get("Interval")
        self.Parameters = params.get("Parameters")
        self.Cron = params.get("Cron")
        self.ResourceIDs = params.get("ResourceIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProbeTaskConfigurationListResponse(AbstractModel):
    """UpdateProbeTaskConfigurationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")