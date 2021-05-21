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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CallDetailItem(AbstractModel):
    """调用明细结构体

    """

    def __init__(self):
        """
        :param DataType: 数据类型 0 imei 1 qimei 2 qq 3 phone 7:IDFA 8:MD5(imei)
        :type DataType: int
        :param ValidAmount: 有效数据量
        :type ValidAmount: int
        :param Date: 调用时间
        :type Date: str
        """
        self.DataType = None
        self.ValidAmount = None
        self.Date = None


    def _deserialize(self, params):
        self.DataType = params.get("DataType")
        self.ValidAmount = params.get("ValidAmount")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CallDetails(AbstractModel):
    """调用明细返回数据体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的总条数
        :type TotalCount: int
        :param CallDetailSet: 调用明细数组
        :type CallDetailSet: list of CallDetailItem
        """
        self.TotalCount = None
        self.CallDetailSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CallDetailSet") is not None:
            self.CallDetailSet = []
            for item in params.get("CallDetailSet"):
                obj = CallDetailItem()
                obj._deserialize(item)
                self.CallDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CallStatItem(AbstractModel):
    """调用量统计item

    """

    def __init__(self):
        """
        :param Date: 当前统计量的时间段
        :type Date: str
        :param Amount: 当前时间段的调用量
        :type Amount: int
        """
        self.Date = None
        self.Amount = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GeneralStat(AbstractModel):
    """调用量统计信息，包括周/日/月/总调用量

    """

    def __init__(self):
        """
        :param TodayAmount: 今日调用量
        :type TodayAmount: int
        :param WeekAmount: 本周调用量
        :type WeekAmount: int
        :param MonthAmount: 本月调用量
        :type MonthAmount: int
        :param TotalAmount: 总调用量
        :type TotalAmount: int
        """
        self.TodayAmount = None
        self.WeekAmount = None
        self.MonthAmount = None
        self.TotalAmount = None


    def _deserialize(self, params):
        self.TodayAmount = params.get("TodayAmount")
        self.WeekAmount = params.get("WeekAmount")
        self.MonthAmount = params.get("MonthAmount")
        self.TotalAmount = params.get("TotalAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetTaskDetailRequest(AbstractModel):
    """GetTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 任务ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetTaskDetailResponse(AbstractModel):
    """GetTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TaskDetailDataList: 画像洞察任务TAG详细数据列表
        :type TaskDetailDataList: list of TaskDetailData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskDetailDataList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskDetailDataList") is not None:
            self.TaskDetailDataList = []
            for item in params.get("TaskDetailDataList"):
                obj = TaskDetailData()
                obj._deserialize(item)
                self.TaskDetailDataList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetTaskListRequest(AbstractModel):
    """GetTaskList请求参数结构体

    """

    def __init__(self):
        """
        :param PageNumber: 查询分页页码
        :type PageNumber: int
        :param PageSize: 查询分页大小
        :type PageSize: int
        :param StartTime: 查询起始时间（13位数字的UNIX时间戳，单位毫秒 ）
        :type StartTime: int
        :param EndTime: 查询结束时间（13位数字的UNIX时间戳，单位毫秒 ）
        :type EndTime: int
        :param TaskName: 任务名称
        :type TaskName: str
        :param TaskStatus: 查询任务状态 0:默认状态 1:任务正在运行 2:任务运行成功 3:任务运行失败
        :type TaskStatus: int
        """
        self.PageNumber = None
        self.PageSize = None
        self.StartTime = None
        self.EndTime = None
        self.TaskName = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskName = params.get("TaskName")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetTaskListResponse(AbstractModel):
    """GetTaskList返回参数结构体

    """

    def __init__(self):
        """
        :param TaskListData: 任务列表对象
        :type TaskListData: :class:`tencentcloud.apcas.v20201127.models.TaskListData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskListData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskListData") is not None:
            self.TaskListData = TaskListData()
            self.TaskListData._deserialize(params.get("TaskListData"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LabelDetailData(AbstractModel):
    """画像标签详情数据对象

    """

    def __init__(self):
        """
        :param Value: 标签数据对象
        :type Value: :class:`tencentcloud.apcas.v20201127.models.LabelValue`
        :param Label: 标签表述，如"汽车资讯"、"游戏#手游"等
        :type Label: str
        """
        self.Value = None
        self.Label = None


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self.Value = LabelValue()
            self.Value._deserialize(params.get("Value"))
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LabelValue(AbstractModel):
    """标签数据

    """

    def __init__(self):
        """
        :param Proportion: 标签覆盖率占比（在整个上传的ID列表中的覆盖率）
        :type Proportion: float
        :param Market: 标签大盘覆盖率占比
        :type Market: float
        :param Tgi: TGI指数，由Proportion除以Market得到
        :type Tgi: float
        """
        self.Proportion = None
        self.Market = None
        self.Tgi = None


    def _deserialize(self, params):
        self.Proportion = params.get("Proportion")
        self.Market = params.get("Market")
        self.Tgi = params.get("Tgi")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListModel(AbstractModel):
    """任务列表项Model

    """

    def __init__(self):
        """
        :param ID: 任务ID
        :type ID: int
        :param TaskName: 任务名称
        :type TaskName: str
        :param StartTime: 任务起始时间（13位数字的UNIX 时间戳，单位毫秒 ）
        :type StartTime: int
        :param Status: 任务状态 0:默认状态 1:任务正在运行 2:任务运行成功 3:任务运行失败
        :type Status: int
        :param Available: 画像覆盖人数
        :type Available: int
        :param ErrMsg: 任务失败描述信息
        :type ErrMsg: str
        """
        self.ID = None
        self.TaskName = None
        self.StartTime = None
        self.Status = None
        self.Available = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.TaskName = params.get("TaskName")
        self.StartTime = params.get("StartTime")
        self.Status = params.get("Status")
        self.Available = params.get("Available")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PredictRatingRequest(AbstractModel):
    """PredictRating请求参数结构体

    """

    def __init__(self):
        """
        :param Type: ID标志的类型，0:IMEI 7:IDFA 8:MD5(imei) 100: 手机号明文 101: 手机号md5加密
        :type Type: int
        :param Id: 请求唯一标志ID
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PredictRatingResponse(AbstractModel):
    """PredictRating返回参数结构体

    """

    def __init__(self):
        """
        :param RatingData: 意向评级
        :type RatingData: :class:`tencentcloud.apcas.v20201127.models.RatingData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RatingData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RatingData") is not None:
            self.RatingData = RatingData()
            self.RatingData._deserialize(params.get("RatingData"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryCallDetailsRequest(AbstractModel):
    """QueryCallDetails请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 请求类型 1:人群特征洞察统计 2:购车意向预测统计
        :type Type: int
        :param StartTime: 开始时间戳（毫秒）
        :type StartTime: int
        :param EndTime: 结束时间戳（毫秒）
        :type EndTime: int
        :param PageNumber: 页数
        :type PageNumber: int
        :param PageSize: 每页个数
        :type PageSize: int
        """
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryCallDetailsResponse(AbstractModel):
    """QueryCallDetails返回参数结构体

    """

    def __init__(self):
        """
        :param CallDetails: 调用明细
        :type CallDetails: :class:`tencentcloud.apcas.v20201127.models.CallDetails`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CallDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CallDetails") is not None:
            self.CallDetails = CallDetails()
            self.CallDetails._deserialize(params.get("CallDetails"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryCallStatRequest(AbstractModel):
    """QueryCallStat请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 请求类型 1:人群特征洞察统计 2:购车意向预测统计
        :type Type: int
        :param StartTime: 开始时间戳（毫秒）
        :type StartTime: int
        :param EndTime: 结束时间戳（毫秒）
        :type EndTime: int
        """
        self.Type = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryCallStatResponse(AbstractModel):
    """QueryCallStat返回参数结构体

    """

    def __init__(self):
        """
        :param CallSet: 调用量数组
        :type CallSet: list of CallStatItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CallSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CallSet") is not None:
            self.CallSet = []
            for item in params.get("CallSet"):
                obj = CallStatItem()
                obj._deserialize(item)
                self.CallSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryGeneralStatRequest(AbstractModel):
    """QueryGeneralStat请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 请求类型:1,人群特征洞察统计 2购车意向预测统计
        :type Type: int
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryGeneralStatResponse(AbstractModel):
    """QueryGeneralStat返回参数结构体

    """

    def __init__(self):
        """
        :param GeneralStat: 调用量信息
        :type GeneralStat: :class:`tencentcloud.apcas.v20201127.models.GeneralStat`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GeneralStat = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GeneralStat") is not None:
            self.GeneralStat = GeneralStat()
            self.GeneralStat._deserialize(params.get("GeneralStat"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RatingData(AbstractModel):
    """返回购车意向评级

    """

    def __init__(self):
        """
        :param Rank: 线索评级（取值：0、1、2、3分别代表无、低、中、高意愿）
        :type Rank: int
        """
        self.Rank = None


    def _deserialize(self, params):
        self.Rank = params.get("Rank")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskData(AbstractModel):
    """任务ID信息

    """

    def __init__(self):
        """
        :param Id: 画像洞察任务ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskDetailData(AbstractModel):
    """画像任务详情对象

    """

    def __init__(self):
        """
        :param TagId: 画像TAG ID
        :type TagId: int
        :param TagDesc: 画像TAG描述（如“省份分布”）
        :type TagDesc: str
        :param LabelDetailDataList: 画像Label对象列表（一个TAG对于N个Label，例如“省份分布”TAG对应“广东省”、“浙江省”等多个Label）
        :type LabelDetailDataList: list of LabelDetailData
        """
        self.TagId = None
        self.TagDesc = None
        self.LabelDetailDataList = None


    def _deserialize(self, params):
        self.TagId = params.get("TagId")
        self.TagDesc = params.get("TagDesc")
        if params.get("LabelDetailDataList") is not None:
            self.LabelDetailDataList = []
            for item in params.get("LabelDetailDataList"):
                obj = LabelDetailData()
                obj._deserialize(item)
                self.LabelDetailDataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskListData(AbstractModel):
    """任务列表对象

    """

    def __init__(self):
        """
        :param PageNumber: 查询分页页码
        :type PageNumber: int
        :param PageSize: 查询分页大小
        :type PageSize: int
        :param TotalCount: 任务列表总记录数
        :type TotalCount: int
        :param TaskList: 任务列表
        :type TaskList: list of ListModel
        """
        self.PageNumber = None
        self.PageSize = None
        self.TotalCount = None
        self.TaskList = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskList") is not None:
            self.TaskList = []
            for item in params.get("TaskList"):
                obj = ListModel()
                obj._deserialize(item)
                self.TaskList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UploadIdRequest(AbstractModel):
    """UploadId请求参数结构体

    """

    def __init__(self):
        """
        :param Type: id标志的类型: 0:imei 7:IDFA 8:MD5(imei)
        :type Type: int
        :param TaskName: 任务名称
        :type TaskName: str
        :param IdListBase64: ID列表（ID间使用换行符分割、然后使用Base64编码）
        :type IdListBase64: str
        """
        self.Type = None
        self.TaskName = None
        self.IdListBase64 = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TaskName = params.get("TaskName")
        self.IdListBase64 = params.get("IdListBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UploadIdResponse(AbstractModel):
    """UploadId返回参数结构体

    """

    def __init__(self):
        """
        :param TaskData: 画像洞察任务ID等信息
        :type TaskData: :class:`tencentcloud.apcas.v20201127.models.TaskData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskData") is not None:
            self.TaskData = TaskData()
            self.TaskData._deserialize(params.get("TaskData"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        