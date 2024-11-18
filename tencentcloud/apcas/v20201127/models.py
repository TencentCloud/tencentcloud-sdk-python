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


class CallDetailItem(AbstractModel):
    """调用明细结构体

    """

    def __init__(self):
        r"""
        :param _DataType: 数据类型 0 imei 1 qimei 2 qq 3 phone 7:IDFA 8:MD5(imei)
        :type DataType: int
        :param _ValidAmount: 有效数据量
        :type ValidAmount: int
        :param _Date: 调用时间
        :type Date: str
        """
        self._DataType = None
        self._ValidAmount = None
        self._Date = None

    @property
    def DataType(self):
        """数据类型 0 imei 1 qimei 2 qq 3 phone 7:IDFA 8:MD5(imei)
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def ValidAmount(self):
        """有效数据量
        :rtype: int
        """
        return self._ValidAmount

    @ValidAmount.setter
    def ValidAmount(self, ValidAmount):
        self._ValidAmount = ValidAmount

    @property
    def Date(self):
        """调用时间
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._DataType = params.get("DataType")
        self._ValidAmount = params.get("ValidAmount")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallDetails(AbstractModel):
    """调用明细返回数据体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的总条数
        :type TotalCount: int
        :param _CallDetailSet: 调用明细数组
        :type CallDetailSet: list of CallDetailItem
        """
        self._TotalCount = None
        self._CallDetailSet = None

    @property
    def TotalCount(self):
        """符合条件的总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CallDetailSet(self):
        """调用明细数组
        :rtype: list of CallDetailItem
        """
        return self._CallDetailSet

    @CallDetailSet.setter
    def CallDetailSet(self, CallDetailSet):
        self._CallDetailSet = CallDetailSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CallDetailSet") is not None:
            self._CallDetailSet = []
            for item in params.get("CallDetailSet"):
                obj = CallDetailItem()
                obj._deserialize(item)
                self._CallDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallStatItem(AbstractModel):
    """调用量统计item

    """

    def __init__(self):
        r"""
        :param _Date: 当前统计量的时间段
        :type Date: str
        :param _Amount: 当前时间段的调用量
        :type Amount: int
        """
        self._Date = None
        self._Amount = None

    @property
    def Date(self):
        """当前统计量的时间段
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Amount(self):
        """当前时间段的调用量
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneralStat(AbstractModel):
    """调用量统计信息，包括周/日/月/总调用量

    """

    def __init__(self):
        r"""
        :param _TodayAmount: 今日调用量
        :type TodayAmount: int
        :param _WeekAmount: 本周调用量
        :type WeekAmount: int
        :param _MonthAmount: 本月调用量
        :type MonthAmount: int
        :param _TotalAmount: 总调用量
        :type TotalAmount: int
        """
        self._TodayAmount = None
        self._WeekAmount = None
        self._MonthAmount = None
        self._TotalAmount = None

    @property
    def TodayAmount(self):
        """今日调用量
        :rtype: int
        """
        return self._TodayAmount

    @TodayAmount.setter
    def TodayAmount(self, TodayAmount):
        self._TodayAmount = TodayAmount

    @property
    def WeekAmount(self):
        """本周调用量
        :rtype: int
        """
        return self._WeekAmount

    @WeekAmount.setter
    def WeekAmount(self, WeekAmount):
        self._WeekAmount = WeekAmount

    @property
    def MonthAmount(self):
        """本月调用量
        :rtype: int
        """
        return self._MonthAmount

    @MonthAmount.setter
    def MonthAmount(self, MonthAmount):
        self._MonthAmount = MonthAmount

    @property
    def TotalAmount(self):
        """总调用量
        :rtype: int
        """
        return self._TotalAmount

    @TotalAmount.setter
    def TotalAmount(self, TotalAmount):
        self._TotalAmount = TotalAmount


    def _deserialize(self, params):
        self._TodayAmount = params.get("TodayAmount")
        self._WeekAmount = params.get("WeekAmount")
        self._MonthAmount = params.get("MonthAmount")
        self._TotalAmount = params.get("TotalAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskDetailRequest(AbstractModel):
    """GetTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 任务ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """任务ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskDetailResponse(AbstractModel):
    """GetTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskDetailDataList: 画像洞察任务TAG详细数据列表
        :type TaskDetailDataList: list of TaskDetailData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskDetailDataList = None
        self._RequestId = None

    @property
    def TaskDetailDataList(self):
        """画像洞察任务TAG详细数据列表
        :rtype: list of TaskDetailData
        """
        return self._TaskDetailDataList

    @TaskDetailDataList.setter
    def TaskDetailDataList(self, TaskDetailDataList):
        self._TaskDetailDataList = TaskDetailDataList

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskDetailDataList") is not None:
            self._TaskDetailDataList = []
            for item in params.get("TaskDetailDataList"):
                obj = TaskDetailData()
                obj._deserialize(item)
                self._TaskDetailDataList.append(obj)
        self._RequestId = params.get("RequestId")


class GetTaskListRequest(AbstractModel):
    """GetTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 查询分页页码
        :type PageNumber: int
        :param _PageSize: 查询分页大小
        :type PageSize: int
        :param _StartTime: 查询起始时间（13位数字的UNIX时间戳，单位毫秒 ）
        :type StartTime: int
        :param _EndTime: 查询结束时间（13位数字的UNIX时间戳，单位毫秒 ）
        :type EndTime: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _TaskStatus: 查询任务状态 0:默认状态 1:任务正在运行 2:任务运行成功 3:任务运行失败
        :type TaskStatus: int
        """
        self._PageNumber = None
        self._PageSize = None
        self._StartTime = None
        self._EndTime = None
        self._TaskName = None
        self._TaskStatus = None

    @property
    def PageNumber(self):
        """查询分页页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """查询分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def StartTime(self):
        """查询起始时间（13位数字的UNIX时间戳，单位毫秒 ）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间（13位数字的UNIX时间戳，单位毫秒 ）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskStatus(self):
        """查询任务状态 0:默认状态 1:任务正在运行 2:任务运行成功 3:任务运行失败
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskName = params.get("TaskName")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskListResponse(AbstractModel):
    """GetTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskListData: 任务列表对象
        :type TaskListData: :class:`tencentcloud.apcas.v20201127.models.TaskListData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskListData = None
        self._RequestId = None

    @property
    def TaskListData(self):
        """任务列表对象
        :rtype: :class:`tencentcloud.apcas.v20201127.models.TaskListData`
        """
        return self._TaskListData

    @TaskListData.setter
    def TaskListData(self, TaskListData):
        self._TaskListData = TaskListData

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskListData") is not None:
            self._TaskListData = TaskListData()
            self._TaskListData._deserialize(params.get("TaskListData"))
        self._RequestId = params.get("RequestId")


class LabelDetailData(AbstractModel):
    """画像标签详情数据对象

    """

    def __init__(self):
        r"""
        :param _Value: 标签数据对象
        :type Value: :class:`tencentcloud.apcas.v20201127.models.LabelValue`
        :param _Label: 标签表述，如"汽车资讯"、"游戏#手游"等
        :type Label: str
        """
        self._Value = None
        self._Label = None

    @property
    def Value(self):
        """标签数据对象
        :rtype: :class:`tencentcloud.apcas.v20201127.models.LabelValue`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Label(self):
        """标签表述，如"汽车资讯"、"游戏#手游"等
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self._Value = LabelValue()
            self._Value._deserialize(params.get("Value"))
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LabelValue(AbstractModel):
    """标签数据

    """

    def __init__(self):
        r"""
        :param _Proportion: 标签覆盖率占比（在整个上传的ID列表中的覆盖率）
        :type Proportion: float
        :param _Market: 标签大盘覆盖率占比
        :type Market: float
        :param _Tgi: TGI指数，由Proportion除以Market得到
        :type Tgi: float
        """
        self._Proportion = None
        self._Market = None
        self._Tgi = None

    @property
    def Proportion(self):
        """标签覆盖率占比（在整个上传的ID列表中的覆盖率）
        :rtype: float
        """
        return self._Proportion

    @Proportion.setter
    def Proportion(self, Proportion):
        self._Proportion = Proportion

    @property
    def Market(self):
        """标签大盘覆盖率占比
        :rtype: float
        """
        return self._Market

    @Market.setter
    def Market(self, Market):
        self._Market = Market

    @property
    def Tgi(self):
        """TGI指数，由Proportion除以Market得到
        :rtype: float
        """
        return self._Tgi

    @Tgi.setter
    def Tgi(self, Tgi):
        self._Tgi = Tgi


    def _deserialize(self, params):
        self._Proportion = params.get("Proportion")
        self._Market = params.get("Market")
        self._Tgi = params.get("Tgi")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListModel(AbstractModel):
    """任务列表项Model

    """

    def __init__(self):
        r"""
        :param _ID: 任务ID
        :type ID: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _StartTime: 任务起始时间（13位数字的UNIX 时间戳，单位毫秒 ）
        :type StartTime: int
        :param _Status: 任务状态 0:默认状态 1:任务正在运行 2:任务运行成功 3:任务运行失败
        :type Status: int
        :param _Available: 画像覆盖人数
        :type Available: int
        :param _ErrMsg: 任务失败描述信息
        :type ErrMsg: str
        """
        self._ID = None
        self._TaskName = None
        self._StartTime = None
        self._Status = None
        self._Available = None
        self._ErrMsg = None

    @property
    def ID(self):
        """任务ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        """任务起始时间（13位数字的UNIX 时间戳，单位毫秒 ）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        """任务状态 0:默认状态 1:任务正在运行 2:任务运行成功 3:任务运行失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Available(self):
        """画像覆盖人数
        :rtype: int
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def ErrMsg(self):
        """任务失败描述信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._Available = params.get("Available")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PredictRatingRequest(AbstractModel):
    """PredictRating请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: ID标志的类型，0:IMEI 7:IDFA 8:MD5(imei) 100: 手机号明文 101: 手机号md5加密
        :type Type: int
        :param _Id: 请求唯一标志ID
        :type Id: str
        """
        self._Type = None
        self._Id = None

    @property
    def Type(self):
        """ID标志的类型，0:IMEI 7:IDFA 8:MD5(imei) 100: 手机号明文 101: 手机号md5加密
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Id(self):
        """请求唯一标志ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PredictRatingResponse(AbstractModel):
    """PredictRating返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RatingData: 意向评级
        :type RatingData: :class:`tencentcloud.apcas.v20201127.models.RatingData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RatingData = None
        self._RequestId = None

    @property
    def RatingData(self):
        """意向评级
        :rtype: :class:`tencentcloud.apcas.v20201127.models.RatingData`
        """
        return self._RatingData

    @RatingData.setter
    def RatingData(self, RatingData):
        self._RatingData = RatingData

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RatingData") is not None:
            self._RatingData = RatingData()
            self._RatingData._deserialize(params.get("RatingData"))
        self._RequestId = params.get("RequestId")


class QueryCallDetailsRequest(AbstractModel):
    """QueryCallDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 请求类型 1:人群特征洞察统计 2:购车意向预测统计
        :type Type: int
        :param _StartTime: 开始时间戳（毫秒）
        :type StartTime: int
        :param _EndTime: 结束时间戳（毫秒）
        :type EndTime: int
        :param _PageNumber: 页数
        :type PageNumber: int
        :param _PageSize: 每页个数
        :type PageSize: int
        """
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Type(self):
        """请求类型 1:人群特征洞察统计 2:购车意向预测统计
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        """开始时间戳（毫秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间戳（毫秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNumber(self):
        """页数
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页个数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCallDetailsResponse(AbstractModel):
    """QueryCallDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CallDetails: 调用明细
        :type CallDetails: :class:`tencentcloud.apcas.v20201127.models.CallDetails`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CallDetails = None
        self._RequestId = None

    @property
    def CallDetails(self):
        """调用明细
        :rtype: :class:`tencentcloud.apcas.v20201127.models.CallDetails`
        """
        return self._CallDetails

    @CallDetails.setter
    def CallDetails(self, CallDetails):
        self._CallDetails = CallDetails

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CallDetails") is not None:
            self._CallDetails = CallDetails()
            self._CallDetails._deserialize(params.get("CallDetails"))
        self._RequestId = params.get("RequestId")


class QueryCallStatRequest(AbstractModel):
    """QueryCallStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 请求类型 1:人群特征洞察统计 2:购车意向预测统计
        :type Type: int
        :param _StartTime: 开始时间戳（毫秒）
        :type StartTime: int
        :param _EndTime: 结束时间戳（毫秒）
        :type EndTime: int
        """
        self._Type = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Type(self):
        """请求类型 1:人群特征洞察统计 2:购车意向预测统计
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        """开始时间戳（毫秒）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间戳（毫秒）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCallStatResponse(AbstractModel):
    """QueryCallStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CallSet: 调用量数组
        :type CallSet: list of CallStatItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CallSet = None
        self._RequestId = None

    @property
    def CallSet(self):
        """调用量数组
        :rtype: list of CallStatItem
        """
        return self._CallSet

    @CallSet.setter
    def CallSet(self, CallSet):
        self._CallSet = CallSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CallSet") is not None:
            self._CallSet = []
            for item in params.get("CallSet"):
                obj = CallStatItem()
                obj._deserialize(item)
                self._CallSet.append(obj)
        self._RequestId = params.get("RequestId")


class QueryGeneralStatRequest(AbstractModel):
    """QueryGeneralStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 请求类型:1,人群特征洞察统计 2购车意向预测统计
        :type Type: int
        """
        self._Type = None

    @property
    def Type(self):
        """请求类型:1,人群特征洞察统计 2购车意向预测统计
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryGeneralStatResponse(AbstractModel):
    """QueryGeneralStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GeneralStat: 调用量信息
        :type GeneralStat: :class:`tencentcloud.apcas.v20201127.models.GeneralStat`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GeneralStat = None
        self._RequestId = None

    @property
    def GeneralStat(self):
        """调用量信息
        :rtype: :class:`tencentcloud.apcas.v20201127.models.GeneralStat`
        """
        return self._GeneralStat

    @GeneralStat.setter
    def GeneralStat(self, GeneralStat):
        self._GeneralStat = GeneralStat

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GeneralStat") is not None:
            self._GeneralStat = GeneralStat()
            self._GeneralStat._deserialize(params.get("GeneralStat"))
        self._RequestId = params.get("RequestId")


class RatingData(AbstractModel):
    """返回购车意向评级

    """

    def __init__(self):
        r"""
        :param _Rank: 线索评级（取值：0、1、2、3分别代表无、低、中、高意愿）
        :type Rank: int
        """
        self._Rank = None

    @property
    def Rank(self):
        """线索评级（取值：0、1、2、3分别代表无、低、中、高意愿）
        :rtype: int
        """
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank


    def _deserialize(self, params):
        self._Rank = params.get("Rank")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskData(AbstractModel):
    """任务ID信息

    """

    def __init__(self):
        r"""
        :param _Id: 画像洞察任务ID
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """画像洞察任务ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskDetailData(AbstractModel):
    """画像任务详情对象

    """

    def __init__(self):
        r"""
        :param _TagId: 画像TAG ID
        :type TagId: int
        :param _TagDesc: 画像TAG描述（如“省份分布”）
        :type TagDesc: str
        :param _LabelDetailDataList: 画像Label对象列表（一个TAG对于N个Label，例如“省份分布”TAG对应“广东省”、“浙江省”等多个Label）
        :type LabelDetailDataList: list of LabelDetailData
        """
        self._TagId = None
        self._TagDesc = None
        self._LabelDetailDataList = None

    @property
    def TagId(self):
        """画像TAG ID
        :rtype: int
        """
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def TagDesc(self):
        """画像TAG描述（如“省份分布”）
        :rtype: str
        """
        return self._TagDesc

    @TagDesc.setter
    def TagDesc(self, TagDesc):
        self._TagDesc = TagDesc

    @property
    def LabelDetailDataList(self):
        """画像Label对象列表（一个TAG对于N个Label，例如“省份分布”TAG对应“广东省”、“浙江省”等多个Label）
        :rtype: list of LabelDetailData
        """
        return self._LabelDetailDataList

    @LabelDetailDataList.setter
    def LabelDetailDataList(self, LabelDetailDataList):
        self._LabelDetailDataList = LabelDetailDataList


    def _deserialize(self, params):
        self._TagId = params.get("TagId")
        self._TagDesc = params.get("TagDesc")
        if params.get("LabelDetailDataList") is not None:
            self._LabelDetailDataList = []
            for item in params.get("LabelDetailDataList"):
                obj = LabelDetailData()
                obj._deserialize(item)
                self._LabelDetailDataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskListData(AbstractModel):
    """任务列表对象

    """

    def __init__(self):
        r"""
        :param _PageNumber: 查询分页页码
        :type PageNumber: int
        :param _PageSize: 查询分页大小
        :type PageSize: int
        :param _TotalCount: 任务列表总记录数
        :type TotalCount: int
        :param _TaskList: 任务列表
        :type TaskList: list of ListModel
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._TaskList = None

    @property
    def PageNumber(self):
        """查询分页页码
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """查询分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        """任务列表总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskList(self):
        """任务列表
        :rtype: list of ListModel
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = ListModel()
                obj._deserialize(item)
                self._TaskList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIdRequest(AbstractModel):
    """UploadId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: id标志的类型: 0:imei 7:IDFA 8:MD5(imei)
        :type Type: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _IdListBase64: ID列表（ID间使用换行符分割、然后使用Base64编码）
        :type IdListBase64: str
        """
        self._Type = None
        self._TaskName = None
        self._IdListBase64 = None

    @property
    def Type(self):
        """id标志的类型: 0:imei 7:IDFA 8:MD5(imei)
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TaskName(self):
        """任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def IdListBase64(self):
        """ID列表（ID间使用换行符分割、然后使用Base64编码）
        :rtype: str
        """
        return self._IdListBase64

    @IdListBase64.setter
    def IdListBase64(self, IdListBase64):
        self._IdListBase64 = IdListBase64


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TaskName = params.get("TaskName")
        self._IdListBase64 = params.get("IdListBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadIdResponse(AbstractModel):
    """UploadId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskData: 画像洞察任务ID等信息
        :type TaskData: :class:`tencentcloud.apcas.v20201127.models.TaskData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskData = None
        self._RequestId = None

    @property
    def TaskData(self):
        """画像洞察任务ID等信息
        :rtype: :class:`tencentcloud.apcas.v20201127.models.TaskData`
        """
        return self._TaskData

    @TaskData.setter
    def TaskData(self, TaskData):
        self._TaskData = TaskData

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskData") is not None:
            self._TaskData = TaskData()
            self._TaskData._deserialize(params.get("TaskData"))
        self._RequestId = params.get("RequestId")