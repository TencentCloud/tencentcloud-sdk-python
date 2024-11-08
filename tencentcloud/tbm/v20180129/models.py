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


class AgePortrait(AbstractModel):
    """用户年龄画像

    """

    def __init__(self):
        r"""
        :param _AgeRange: 年龄区间
        :type AgeRange: str
        :param _Percent: 百分比
        :type Percent: float
        """
        self._AgeRange = None
        self._Percent = None

    @property
    def AgeRange(self):
        """年龄区间
        :rtype: str
        """
        return self._AgeRange

    @AgeRange.setter
    def AgeRange(self, AgeRange):
        self._AgeRange = AgeRange

    @property
    def Percent(self):
        """百分比
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._AgeRange = params.get("AgeRange")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgePortraitInfo(AbstractModel):
    """用户年龄画像元素数组

    """

    def __init__(self):
        r"""
        :param _PortraitSet: 用户年龄画像数组
        :type PortraitSet: list of AgePortrait
        """
        self._PortraitSet = None

    @property
    def PortraitSet(self):
        """用户年龄画像数组
        :rtype: list of AgePortrait
        """
        return self._PortraitSet

    @PortraitSet.setter
    def PortraitSet(self, PortraitSet):
        self._PortraitSet = PortraitSet


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self._PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = AgePortrait()
                obj._deserialize(item)
                self._PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrandReportArticle(AbstractModel):
    """文章信息

    """

    def __init__(self):
        r"""
        :param _Title: 文章标题
        :type Title: str
        :param _Url: 文章url地址
        :type Url: str
        :param _FromSite: 文章来源
        :type FromSite: str
        :param _PubTime: 文章发表日期
        :type PubTime: str
        :param _Flag: 文章标识
        :type Flag: int
        :param _Hot: 文章热度值
        :type Hot: int
        :param _Level: 文章来源等级
        :type Level: int
        :param _Abstract: 文章摘要
        :type Abstract: str
        :param _ArticleId: 文章ID
        :type ArticleId: str
        """
        self._Title = None
        self._Url = None
        self._FromSite = None
        self._PubTime = None
        self._Flag = None
        self._Hot = None
        self._Level = None
        self._Abstract = None
        self._ArticleId = None

    @property
    def Title(self):
        """文章标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Url(self):
        """文章url地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FromSite(self):
        """文章来源
        :rtype: str
        """
        return self._FromSite

    @FromSite.setter
    def FromSite(self, FromSite):
        self._FromSite = FromSite

    @property
    def PubTime(self):
        """文章发表日期
        :rtype: str
        """
        return self._PubTime

    @PubTime.setter
    def PubTime(self, PubTime):
        self._PubTime = PubTime

    @property
    def Flag(self):
        """文章标识
        :rtype: int
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Hot(self):
        """文章热度值
        :rtype: int
        """
        return self._Hot

    @Hot.setter
    def Hot(self, Hot):
        self._Hot = Hot

    @property
    def Level(self):
        """文章来源等级
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Abstract(self):
        """文章摘要
        :rtype: str
        """
        return self._Abstract

    @Abstract.setter
    def Abstract(self, Abstract):
        self._Abstract = Abstract

    @property
    def ArticleId(self):
        """文章ID
        :rtype: str
        """
        return self._ArticleId

    @ArticleId.setter
    def ArticleId(self, ArticleId):
        self._ArticleId = ArticleId


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Url = params.get("Url")
        self._FromSite = params.get("FromSite")
        self._PubTime = params.get("PubTime")
        self._Flag = params.get("Flag")
        self._Hot = params.get("Hot")
        self._Level = params.get("Level")
        self._Abstract = params.get("Abstract")
        self._ArticleId = params.get("ArticleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Comment(AbstractModel):
    """用户好评差评个数信息

    """

    def __init__(self):
        r"""
        :param _Date: 评论的日期
        :type Date: str
        :param _NegCommentCount: 差评的个数
        :type NegCommentCount: int
        :param _PosCommentCount: 好评的个数
        :type PosCommentCount: int
        """
        self._Date = None
        self._NegCommentCount = None
        self._PosCommentCount = None

    @property
    def Date(self):
        """评论的日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def NegCommentCount(self):
        """差评的个数
        :rtype: int
        """
        return self._NegCommentCount

    @NegCommentCount.setter
    def NegCommentCount(self, NegCommentCount):
        self._NegCommentCount = NegCommentCount

    @property
    def PosCommentCount(self):
        """好评的个数
        :rtype: int
        """
        return self._PosCommentCount

    @PosCommentCount.setter
    def PosCommentCount(self, PosCommentCount):
        self._PosCommentCount = PosCommentCount


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._NegCommentCount = params.get("NegCommentCount")
        self._PosCommentCount = params.get("PosCommentCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommentInfo(AbstractModel):
    """用户评论内容类型

    """

    def __init__(self):
        r"""
        :param _Comment: 用户评论内容
        :type Comment: str
        :param _Date: 评论的时间
        :type Date: str
        """
        self._Comment = None
        self._Date = None

    @property
    def Comment(self):
        """用户评论内容
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Date(self):
        """评论的时间
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._Comment = params.get("Comment")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DateCount(AbstractModel):
    """按日期的统计数据

    """

    def __init__(self):
        r"""
        :param _Date: 统计日期
        :type Date: str
        :param _Count: 统计值
        :type Count: int
        """
        self._Date = None
        self._Count = None

    @property
    def Date(self):
        """统计日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Count(self):
        """统计值
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandCommentCountRequest(AbstractModel):
    """DescribeBrandCommentCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        :param _StartDate: 查询开始日期
        :type StartDate: str
        :param _EndDate: 查询结束日期
        :type EndDate: str
        """
        self._BrandId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def StartDate(self):
        """查询开始日期
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询结束日期
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandCommentCountResponse(AbstractModel):
    """DescribeBrandCommentCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CommentSet: 按天统计好评/差评数
        :type CommentSet: list of Comment
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CommentSet = None
        self._RequestId = None

    @property
    def CommentSet(self):
        """按天统计好评/差评数
        :rtype: list of Comment
        """
        return self._CommentSet

    @CommentSet.setter
    def CommentSet(self, CommentSet):
        self._CommentSet = CommentSet

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
        if params.get("CommentSet") is not None:
            self._CommentSet = []
            for item in params.get("CommentSet"):
                obj = Comment()
                obj._deserialize(item)
                self._CommentSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBrandExposureRequest(AbstractModel):
    """DescribeBrandExposure请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        :param _StartDate: 查询开始时间
        :type StartDate: str
        :param _EndDate: 查询结束时间
        :type EndDate: str
        """
        self._BrandId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def StartDate(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandExposureResponse(AbstractModel):
    """DescribeBrandExposure返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 累计曝光量
        :type TotalCount: int
        :param _DateCountSet: 按天计算的统计数据
        :type DateCountSet: list of DateCount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DateCountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """累计曝光量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DateCountSet(self):
        """按天计算的统计数据
        :rtype: list of DateCount
        """
        return self._DateCountSet

    @DateCountSet.setter
    def DateCountSet(self, DateCountSet):
        self._DateCountSet = DateCountSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self._DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self._DateCountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBrandMediaReportRequest(AbstractModel):
    """DescribeBrandMediaReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        :param _StartDate: 查询开始时间
        :type StartDate: str
        :param _EndDate: 查询结束时间
        :type EndDate: str
        """
        self._BrandId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def StartDate(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandMediaReportResponse(AbstractModel):
    """DescribeBrandMediaReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询范围内文章总数
        :type TotalCount: int
        :param _DateCountSet: 按天计算的每天文章数
        :type DateCountSet: list of DateCount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DateCountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询范围内文章总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DateCountSet(self):
        """按天计算的每天文章数
        :rtype: list of DateCount
        """
        return self._DateCountSet

    @DateCountSet.setter
    def DateCountSet(self, DateCountSet):
        self._DateCountSet = DateCountSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self._DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self._DateCountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBrandNegCommentsRequest(AbstractModel):
    """DescribeBrandNegComments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        :param _StartDate: 查询开始时间
        :type StartDate: str
        :param _EndDate: 查询结束时间
        :type EndDate: str
        :param _Limit: 查询条数上限，默认20
        :type Limit: int
        :param _Offset: 查询偏移，默认从0开始
        :type Offset: int
        """
        self._BrandId = None
        self._StartDate = None
        self._EndDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def StartDate(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Limit(self):
        """查询条数上限，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询偏移，默认从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandNegCommentsResponse(AbstractModel):
    """DescribeBrandNegComments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandCommentSet: 评论列表
        :type BrandCommentSet: list of CommentInfo
        :param _TotalComments: 总的差评个数
        :type TotalComments: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BrandCommentSet = None
        self._TotalComments = None
        self._RequestId = None

    @property
    def BrandCommentSet(self):
        """评论列表
        :rtype: list of CommentInfo
        """
        return self._BrandCommentSet

    @BrandCommentSet.setter
    def BrandCommentSet(self, BrandCommentSet):
        self._BrandCommentSet = BrandCommentSet

    @property
    def TotalComments(self):
        """总的差评个数
        :rtype: int
        """
        return self._TotalComments

    @TotalComments.setter
    def TotalComments(self, TotalComments):
        self._TotalComments = TotalComments

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
        if params.get("BrandCommentSet") is not None:
            self._BrandCommentSet = []
            for item in params.get("BrandCommentSet"):
                obj = CommentInfo()
                obj._deserialize(item)
                self._BrandCommentSet.append(obj)
        self._TotalComments = params.get("TotalComments")
        self._RequestId = params.get("RequestId")


class DescribeBrandPosCommentsRequest(AbstractModel):
    """DescribeBrandPosComments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        :param _StartDate: 查询开始时间
        :type StartDate: str
        :param _EndDate: 查询结束时间
        :type EndDate: str
        :param _Limit: 查询条数上限，默认20
        :type Limit: int
        :param _Offset: 查询偏移，从0开始
        :type Offset: int
        """
        self._BrandId = None
        self._StartDate = None
        self._EndDate = None
        self._Limit = None
        self._Offset = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def StartDate(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Limit(self):
        """查询条数上限，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询偏移，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandPosCommentsResponse(AbstractModel):
    """DescribeBrandPosComments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandCommentSet: 评论列表
        :type BrandCommentSet: list of CommentInfo
        :param _TotalComments: 总的好评个数
        :type TotalComments: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BrandCommentSet = None
        self._TotalComments = None
        self._RequestId = None

    @property
    def BrandCommentSet(self):
        """评论列表
        :rtype: list of CommentInfo
        """
        return self._BrandCommentSet

    @BrandCommentSet.setter
    def BrandCommentSet(self, BrandCommentSet):
        self._BrandCommentSet = BrandCommentSet

    @property
    def TotalComments(self):
        """总的好评个数
        :rtype: int
        """
        return self._TotalComments

    @TotalComments.setter
    def TotalComments(self, TotalComments):
        self._TotalComments = TotalComments

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
        if params.get("BrandCommentSet") is not None:
            self._BrandCommentSet = []
            for item in params.get("BrandCommentSet"):
                obj = CommentInfo()
                obj._deserialize(item)
                self._BrandCommentSet.append(obj)
        self._TotalComments = params.get("TotalComments")
        self._RequestId = params.get("RequestId")


class DescribeBrandSocialOpinionRequest(AbstractModel):
    """DescribeBrandSocialOpinion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        :param _StartDate: 检索开始时间
        :type StartDate: str
        :param _EndDate: 检索结束时间
        :type EndDate: str
        :param _Offset: 查询偏移，默认从0开始
        :type Offset: int
        :param _Limit: 查询条数上限，默认20
        :type Limit: int
        :param _ShowList: 列表显示标记，若为true，则返回文章列表详情
        :type ShowList: bool
        """
        self._BrandId = None
        self._StartDate = None
        self._EndDate = None
        self._Offset = None
        self._Limit = None
        self._ShowList = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def StartDate(self):
        """检索开始时间
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """检索结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Offset(self):
        """查询偏移，默认从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询条数上限，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ShowList(self):
        """列表显示标记，若为true，则返回文章列表详情
        :rtype: bool
        """
        return self._ShowList

    @ShowList.setter
    def ShowList(self, ShowList):
        self._ShowList = ShowList


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ShowList = params.get("ShowList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandSocialOpinionResponse(AbstractModel):
    """DescribeBrandSocialOpinion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ArticleCount: 文章总数
        :type ArticleCount: int
        :param _FromCount: 来源统计总数
        :type FromCount: int
        :param _AdverseCount: 疑似负面报道总数
        :type AdverseCount: int
        :param _ArticleSet: 文章列表详情
        :type ArticleSet: list of BrandReportArticle
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ArticleCount = None
        self._FromCount = None
        self._AdverseCount = None
        self._ArticleSet = None
        self._RequestId = None

    @property
    def ArticleCount(self):
        """文章总数
        :rtype: int
        """
        return self._ArticleCount

    @ArticleCount.setter
    def ArticleCount(self, ArticleCount):
        self._ArticleCount = ArticleCount

    @property
    def FromCount(self):
        """来源统计总数
        :rtype: int
        """
        return self._FromCount

    @FromCount.setter
    def FromCount(self, FromCount):
        self._FromCount = FromCount

    @property
    def AdverseCount(self):
        """疑似负面报道总数
        :rtype: int
        """
        return self._AdverseCount

    @AdverseCount.setter
    def AdverseCount(self, AdverseCount):
        self._AdverseCount = AdverseCount

    @property
    def ArticleSet(self):
        """文章列表详情
        :rtype: list of BrandReportArticle
        """
        return self._ArticleSet

    @ArticleSet.setter
    def ArticleSet(self, ArticleSet):
        self._ArticleSet = ArticleSet

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
        self._ArticleCount = params.get("ArticleCount")
        self._FromCount = params.get("FromCount")
        self._AdverseCount = params.get("AdverseCount")
        if params.get("ArticleSet") is not None:
            self._ArticleSet = []
            for item in params.get("ArticleSet"):
                obj = BrandReportArticle()
                obj._deserialize(item)
                self._ArticleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBrandSocialReportRequest(AbstractModel):
    """DescribeBrandSocialReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        :param _StartDate: 查询开始时间
        :type StartDate: str
        :param _EndDate: 查询结束时间
        :type EndDate: str
        """
        self._BrandId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId

    @property
    def StartDate(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandSocialReportResponse(AbstractModel):
    """DescribeBrandSocialReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 累计统计数据
        :type TotalCount: int
        :param _DateCountSet: 按天计算的统计数据
        :type DateCountSet: list of DateCount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DateCountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """累计统计数据
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DateCountSet(self):
        """按天计算的统计数据
        :rtype: list of DateCount
        """
        return self._DateCountSet

    @DateCountSet.setter
    def DateCountSet(self, DateCountSet):
        self._DateCountSet = DateCountSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self._DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self._DateCountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIndustryNewsRequest(AbstractModel):
    """DescribeIndustryNews请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IndustryId: 行业ID
        :type IndustryId: str
        :param _StartDate: 查询开始时间
        :type StartDate: str
        :param _EndDate: 查询结束时间
        :type EndDate: str
        :param _ShowList: 是否显示列表，若为 true，则返回文章列表
        :type ShowList: bool
        :param _Offset: 查询偏移，默认从0开始
        :type Offset: int
        :param _Limit: 查询条数上限，默认20
        :type Limit: int
        """
        self._IndustryId = None
        self._StartDate = None
        self._EndDate = None
        self._ShowList = None
        self._Offset = None
        self._Limit = None

    @property
    def IndustryId(self):
        """行业ID
        :rtype: str
        """
        return self._IndustryId

    @IndustryId.setter
    def IndustryId(self, IndustryId):
        self._IndustryId = IndustryId

    @property
    def StartDate(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def ShowList(self):
        """是否显示列表，若为 true，则返回文章列表
        :rtype: bool
        """
        return self._ShowList

    @ShowList.setter
    def ShowList(self, ShowList):
        self._ShowList = ShowList

    @property
    def Offset(self):
        """查询偏移，默认从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询条数上限，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._IndustryId = params.get("IndustryId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._ShowList = params.get("ShowList")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndustryNewsResponse(AbstractModel):
    """DescribeIndustryNews返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NewsCount: 总计文章数量
        :type NewsCount: int
        :param _FromCount: 总计来源数量
        :type FromCount: int
        :param _AdverseCount: 总计疑似负面数量
        :type AdverseCount: int
        :param _NewsSet: 文章列表
        :type NewsSet: list of IndustryNews
        :param _DateCountSet: 按天统计的数量列表
        :type DateCountSet: list of DateCount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NewsCount = None
        self._FromCount = None
        self._AdverseCount = None
        self._NewsSet = None
        self._DateCountSet = None
        self._RequestId = None

    @property
    def NewsCount(self):
        """总计文章数量
        :rtype: int
        """
        return self._NewsCount

    @NewsCount.setter
    def NewsCount(self, NewsCount):
        self._NewsCount = NewsCount

    @property
    def FromCount(self):
        """总计来源数量
        :rtype: int
        """
        return self._FromCount

    @FromCount.setter
    def FromCount(self, FromCount):
        self._FromCount = FromCount

    @property
    def AdverseCount(self):
        """总计疑似负面数量
        :rtype: int
        """
        return self._AdverseCount

    @AdverseCount.setter
    def AdverseCount(self, AdverseCount):
        self._AdverseCount = AdverseCount

    @property
    def NewsSet(self):
        """文章列表
        :rtype: list of IndustryNews
        """
        return self._NewsSet

    @NewsSet.setter
    def NewsSet(self, NewsSet):
        self._NewsSet = NewsSet

    @property
    def DateCountSet(self):
        """按天统计的数量列表
        :rtype: list of DateCount
        """
        return self._DateCountSet

    @DateCountSet.setter
    def DateCountSet(self, DateCountSet):
        self._DateCountSet = DateCountSet

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
        self._NewsCount = params.get("NewsCount")
        self._FromCount = params.get("FromCount")
        self._AdverseCount = params.get("AdverseCount")
        if params.get("NewsSet") is not None:
            self._NewsSet = []
            for item in params.get("NewsSet"):
                obj = IndustryNews()
                obj._deserialize(item)
                self._NewsSet.append(obj)
        if params.get("DateCountSet") is not None:
            self._DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self._DateCountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserPortraitRequest(AbstractModel):
    """DescribeUserPortrait请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BrandId: 品牌ID
        :type BrandId: str
        """
        self._BrandId = None

    @property
    def BrandId(self):
        """品牌ID
        :rtype: str
        """
        return self._BrandId

    @BrandId.setter
    def BrandId(self, BrandId):
        self._BrandId = BrandId


    def _deserialize(self, params):
        self._BrandId = params.get("BrandId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserPortraitResponse(AbstractModel):
    """DescribeUserPortrait返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Age: 年龄画像
        :type Age: :class:`tencentcloud.tbm.v20180129.models.AgePortraitInfo`
        :param _Gender: 性别画像
        :type Gender: :class:`tencentcloud.tbm.v20180129.models.GenderPortraitInfo`
        :param _Province: 省份画像
        :type Province: :class:`tencentcloud.tbm.v20180129.models.ProvincePortraitInfo`
        :param _Movie: 电影喜好画像
        :type Movie: :class:`tencentcloud.tbm.v20180129.models.MoviePortraitInfo`
        :param _Star: 明星喜好画像
        :type Star: :class:`tencentcloud.tbm.v20180129.models.StarPortraitInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Age = None
        self._Gender = None
        self._Province = None
        self._Movie = None
        self._Star = None
        self._RequestId = None

    @property
    def Age(self):
        """年龄画像
        :rtype: :class:`tencentcloud.tbm.v20180129.models.AgePortraitInfo`
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Gender(self):
        """性别画像
        :rtype: :class:`tencentcloud.tbm.v20180129.models.GenderPortraitInfo`
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Province(self):
        """省份画像
        :rtype: :class:`tencentcloud.tbm.v20180129.models.ProvincePortraitInfo`
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Movie(self):
        """电影喜好画像
        :rtype: :class:`tencentcloud.tbm.v20180129.models.MoviePortraitInfo`
        """
        return self._Movie

    @Movie.setter
    def Movie(self, Movie):
        self._Movie = Movie

    @property
    def Star(self):
        """明星喜好画像
        :rtype: :class:`tencentcloud.tbm.v20180129.models.StarPortraitInfo`
        """
        return self._Star

    @Star.setter
    def Star(self, Star):
        self._Star = Star

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
        if params.get("Age") is not None:
            self._Age = AgePortraitInfo()
            self._Age._deserialize(params.get("Age"))
        if params.get("Gender") is not None:
            self._Gender = GenderPortraitInfo()
            self._Gender._deserialize(params.get("Gender"))
        if params.get("Province") is not None:
            self._Province = ProvincePortraitInfo()
            self._Province._deserialize(params.get("Province"))
        if params.get("Movie") is not None:
            self._Movie = MoviePortraitInfo()
            self._Movie._deserialize(params.get("Movie"))
        if params.get("Star") is not None:
            self._Star = StarPortraitInfo()
            self._Star._deserialize(params.get("Star"))
        self._RequestId = params.get("RequestId")


class GenderPortrait(AbstractModel):
    """性别画像元素

    """

    def __init__(self):
        r"""
        :param _Gender: 性别
        :type Gender: str
        :param _Percent: 百分比
        :type Percent: int
        """
        self._Gender = None
        self._Percent = None

    @property
    def Gender(self):
        """性别
        :rtype: str
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Percent(self):
        """百分比
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Gender = params.get("Gender")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenderPortraitInfo(AbstractModel):
    """用户性别画像元素数组

    """

    def __init__(self):
        r"""
        :param _PortraitSet: 用户性别画像数组
        :type PortraitSet: list of GenderPortrait
        """
        self._PortraitSet = None

    @property
    def PortraitSet(self):
        """用户性别画像数组
        :rtype: list of GenderPortrait
        """
        return self._PortraitSet

    @PortraitSet.setter
    def PortraitSet(self, PortraitSet):
        self._PortraitSet = PortraitSet


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self._PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = GenderPortrait()
                obj._deserialize(item)
                self._PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndustryNews(AbstractModel):
    """行业报道新闻

    """

    def __init__(self):
        r"""
        :param _IndustryId: 行业报道ID
        :type IndustryId: str
        :param _PubTime: 报道发表时间
        :type PubTime: str
        :param _FromSite: 报道来源
        :type FromSite: str
        :param _Title: 报道标题
        :type Title: str
        :param _Url: 报道来源url
        :type Url: str
        :param _Level: 报道来源等级
        :type Level: int
        :param _Hot: 热度值
        :type Hot: int
        :param _Flag: 报道标识
        :type Flag: int
        :param _Abstract: 报道摘要
        :type Abstract: str
        """
        self._IndustryId = None
        self._PubTime = None
        self._FromSite = None
        self._Title = None
        self._Url = None
        self._Level = None
        self._Hot = None
        self._Flag = None
        self._Abstract = None

    @property
    def IndustryId(self):
        """行业报道ID
        :rtype: str
        """
        return self._IndustryId

    @IndustryId.setter
    def IndustryId(self, IndustryId):
        self._IndustryId = IndustryId

    @property
    def PubTime(self):
        """报道发表时间
        :rtype: str
        """
        return self._PubTime

    @PubTime.setter
    def PubTime(self, PubTime):
        self._PubTime = PubTime

    @property
    def FromSite(self):
        """报道来源
        :rtype: str
        """
        return self._FromSite

    @FromSite.setter
    def FromSite(self, FromSite):
        self._FromSite = FromSite

    @property
    def Title(self):
        """报道标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Url(self):
        """报道来源url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Level(self):
        """报道来源等级
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Hot(self):
        """热度值
        :rtype: int
        """
        return self._Hot

    @Hot.setter
    def Hot(self, Hot):
        self._Hot = Hot

    @property
    def Flag(self):
        """报道标识
        :rtype: int
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Abstract(self):
        """报道摘要
        :rtype: str
        """
        return self._Abstract

    @Abstract.setter
    def Abstract(self, Abstract):
        self._Abstract = Abstract


    def _deserialize(self, params):
        self._IndustryId = params.get("IndustryId")
        self._PubTime = params.get("PubTime")
        self._FromSite = params.get("FromSite")
        self._Title = params.get("Title")
        self._Url = params.get("Url")
        self._Level = params.get("Level")
        self._Hot = params.get("Hot")
        self._Flag = params.get("Flag")
        self._Abstract = params.get("Abstract")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoviePortrait(AbstractModel):
    """电影喜好画像元素

    """

    def __init__(self):
        r"""
        :param _Name: 电影名称
        :type Name: str
        :param _Percent: 百分比
        :type Percent: float
        """
        self._Name = None
        self._Percent = None

    @property
    def Name(self):
        """电影名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Percent(self):
        """百分比
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoviePortraitInfo(AbstractModel):
    """用户喜好电影画像元素数组

    """

    def __init__(self):
        r"""
        :param _PortraitSet: 用户喜好电影画像数组
        :type PortraitSet: list of MoviePortrait
        """
        self._PortraitSet = None

    @property
    def PortraitSet(self):
        """用户喜好电影画像数组
        :rtype: list of MoviePortrait
        """
        return self._PortraitSet

    @PortraitSet.setter
    def PortraitSet(self, PortraitSet):
        self._PortraitSet = PortraitSet


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self._PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = MoviePortrait()
                obj._deserialize(item)
                self._PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProvincePortrait(AbstractModel):
    """省份画像元素

    """

    def __init__(self):
        r"""
        :param _Province: 省份名称
        :type Province: str
        :param _Percent: 百分比
        :type Percent: float
        """
        self._Province = None
        self._Percent = None

    @property
    def Province(self):
        """省份名称
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Percent(self):
        """百分比
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Province = params.get("Province")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProvincePortraitInfo(AbstractModel):
    """用户省份画像元素数组

    """

    def __init__(self):
        r"""
        :param _PortraitSet: 用户省份画像数组
        :type PortraitSet: list of ProvincePortrait
        """
        self._PortraitSet = None

    @property
    def PortraitSet(self):
        """用户省份画像数组
        :rtype: list of ProvincePortrait
        """
        return self._PortraitSet

    @PortraitSet.setter
    def PortraitSet(self, PortraitSet):
        self._PortraitSet = PortraitSet


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self._PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = ProvincePortrait()
                obj._deserialize(item)
                self._PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StarPortrait(AbstractModel):
    """明星喜好画像元素

    """

    def __init__(self):
        r"""
        :param _Name: 喜欢的明星名字
        :type Name: str
        :param _Percent: 百分比
        :type Percent: float
        """
        self._Name = None
        self._Percent = None

    @property
    def Name(self):
        """喜欢的明星名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Percent(self):
        """百分比
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StarPortraitInfo(AbstractModel):
    """用户喜好的明星画像元素数组

    """

    def __init__(self):
        r"""
        :param _PortraitSet: 用户喜好的明星画像数组
        :type PortraitSet: list of StarPortrait
        """
        self._PortraitSet = None

    @property
    def PortraitSet(self):
        """用户喜好的明星画像数组
        :rtype: list of StarPortrait
        """
        return self._PortraitSet

    @PortraitSet.setter
    def PortraitSet(self, PortraitSet):
        self._PortraitSet = PortraitSet


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self._PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = StarPortrait()
                obj._deserialize(item)
                self._PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        