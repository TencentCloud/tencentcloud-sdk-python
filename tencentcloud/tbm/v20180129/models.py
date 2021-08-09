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
        """
        :param AgeRange: 年龄区间\n        :type AgeRange: str\n        :param Percent: 百分比\n        :type Percent: float\n        """
        self.AgeRange = None
        self.Percent = None


    def _deserialize(self, params):
        self.AgeRange = params.get("AgeRange")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgePortraitInfo(AbstractModel):
    """用户年龄画像元素数组

    """

    def __init__(self):
        """
        :param PortraitSet: 用户年龄画像数组\n        :type PortraitSet: list of AgePortrait\n        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = AgePortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BrandReportArticle(AbstractModel):
    """文章信息

    """

    def __init__(self):
        """
        :param Title: 文章标题\n        :type Title: str\n        :param Url: 文章url地址\n        :type Url: str\n        :param FromSite: 文章来源\n        :type FromSite: str\n        :param PubTime: 文章发表日期\n        :type PubTime: str\n        :param Flag: 文章标识\n        :type Flag: int\n        :param Hot: 文章热度值\n        :type Hot: int\n        :param Level: 文章来源等级\n        :type Level: int\n        :param Abstract: 文章摘要\n        :type Abstract: str\n        :param ArticleId: 文章ID\n        :type ArticleId: str\n        """
        self.Title = None
        self.Url = None
        self.FromSite = None
        self.PubTime = None
        self.Flag = None
        self.Hot = None
        self.Level = None
        self.Abstract = None
        self.ArticleId = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Url = params.get("Url")
        self.FromSite = params.get("FromSite")
        self.PubTime = params.get("PubTime")
        self.Flag = params.get("Flag")
        self.Hot = params.get("Hot")
        self.Level = params.get("Level")
        self.Abstract = params.get("Abstract")
        self.ArticleId = params.get("ArticleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Comment(AbstractModel):
    """用户好评差评个数信息

    """

    def __init__(self):
        """
        :param Date: 评论的日期\n        :type Date: str\n        :param NegCommentCount: 差评的个数\n        :type NegCommentCount: int\n        :param PosCommentCount: 好评的个数\n        :type PosCommentCount: int\n        """
        self.Date = None
        self.NegCommentCount = None
        self.PosCommentCount = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.NegCommentCount = params.get("NegCommentCount")
        self.PosCommentCount = params.get("PosCommentCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommentInfo(AbstractModel):
    """用户评论内容类型

    """

    def __init__(self):
        """
        :param Comment: 用户评论内容\n        :type Comment: str\n        :param Date: 评论的时间\n        :type Date: str\n        """
        self.Comment = None
        self.Date = None


    def _deserialize(self, params):
        self.Comment = params.get("Comment")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DateCount(AbstractModel):
    """按日期的统计数据

    """

    def __init__(self):
        """
        :param Date: 统计日期\n        :type Date: str\n        :param Count: 统计值\n        :type Count: int\n        """
        self.Date = None
        self.Count = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandCommentCountRequest(AbstractModel):
    """DescribeBrandCommentCount请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        :param StartDate: 查询开始日期\n        :type StartDate: str\n        :param EndDate: 查询结束日期\n        :type EndDate: str\n        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandCommentCountResponse(AbstractModel):
    """DescribeBrandCommentCount返回参数结构体

    """

    def __init__(self):
        """
        :param CommentSet: 按天统计好评/差评数\n        :type CommentSet: list of Comment\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CommentSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CommentSet") is not None:
            self.CommentSet = []
            for item in params.get("CommentSet"):
                obj = Comment()
                obj._deserialize(item)
                self.CommentSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandExposureRequest(AbstractModel):
    """DescribeBrandExposure请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        :param StartDate: 查询开始时间\n        :type StartDate: str\n        :param EndDate: 查询结束时间\n        :type EndDate: str\n        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandExposureResponse(AbstractModel):
    """DescribeBrandExposure返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 累计曝光量\n        :type TotalCount: int\n        :param DateCountSet: 按天计算的统计数据\n        :type DateCountSet: list of DateCount\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandMediaReportRequest(AbstractModel):
    """DescribeBrandMediaReport请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        :param StartDate: 查询开始时间\n        :type StartDate: str\n        :param EndDate: 查询结束时间\n        :type EndDate: str\n        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandMediaReportResponse(AbstractModel):
    """DescribeBrandMediaReport返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询范围内文章总数\n        :type TotalCount: int\n        :param DateCountSet: 按天计算的每天文章数\n        :type DateCountSet: list of DateCount\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandNegCommentsRequest(AbstractModel):
    """DescribeBrandNegComments请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        :param StartDate: 查询开始时间\n        :type StartDate: str\n        :param EndDate: 查询结束时间\n        :type EndDate: str\n        :param Limit: 查询条数上限，默认20\n        :type Limit: int\n        :param Offset: 查询偏移，默认从0开始\n        :type Offset: int\n        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandNegCommentsResponse(AbstractModel):
    """DescribeBrandNegComments返回参数结构体

    """

    def __init__(self):
        """
        :param BrandCommentSet: 评论列表\n        :type BrandCommentSet: list of CommentInfo\n        :param TotalComments: 总的差评个数\n        :type TotalComments: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BrandCommentSet = None
        self.TotalComments = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BrandCommentSet") is not None:
            self.BrandCommentSet = []
            for item in params.get("BrandCommentSet"):
                obj = CommentInfo()
                obj._deserialize(item)
                self.BrandCommentSet.append(obj)
        self.TotalComments = params.get("TotalComments")
        self.RequestId = params.get("RequestId")


class DescribeBrandPosCommentsRequest(AbstractModel):
    """DescribeBrandPosComments请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        :param StartDate: 查询开始时间\n        :type StartDate: str\n        :param EndDate: 查询结束时间\n        :type EndDate: str\n        :param Limit: 查询条数上限，默认20\n        :type Limit: int\n        :param Offset: 查询偏移，从0开始\n        :type Offset: int\n        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandPosCommentsResponse(AbstractModel):
    """DescribeBrandPosComments返回参数结构体

    """

    def __init__(self):
        """
        :param BrandCommentSet: 评论列表\n        :type BrandCommentSet: list of CommentInfo\n        :param TotalComments: 总的好评个数\n        :type TotalComments: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BrandCommentSet = None
        self.TotalComments = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BrandCommentSet") is not None:
            self.BrandCommentSet = []
            for item in params.get("BrandCommentSet"):
                obj = CommentInfo()
                obj._deserialize(item)
                self.BrandCommentSet.append(obj)
        self.TotalComments = params.get("TotalComments")
        self.RequestId = params.get("RequestId")


class DescribeBrandSocialOpinionRequest(AbstractModel):
    """DescribeBrandSocialOpinion请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        :param StartDate: 检索开始时间\n        :type StartDate: str\n        :param EndDate: 检索结束时间\n        :type EndDate: str\n        :param Offset: 查询偏移，默认从0开始\n        :type Offset: int\n        :param Limit: 查询条数上限，默认20\n        :type Limit: int\n        :param ShowList: 列表显示标记，若为true，则返回文章列表详情\n        :type ShowList: bool\n        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None
        self.ShowList = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ShowList = params.get("ShowList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandSocialOpinionResponse(AbstractModel):
    """DescribeBrandSocialOpinion返回参数结构体

    """

    def __init__(self):
        """
        :param ArticleCount: 文章总数\n        :type ArticleCount: int\n        :param FromCount: 来源统计总数\n        :type FromCount: int\n        :param AdverseCount: 疑似负面报道总数\n        :type AdverseCount: int\n        :param ArticleSet: 文章列表详情\n        :type ArticleSet: list of BrandReportArticle\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ArticleCount = None
        self.FromCount = None
        self.AdverseCount = None
        self.ArticleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ArticleCount = params.get("ArticleCount")
        self.FromCount = params.get("FromCount")
        self.AdverseCount = params.get("AdverseCount")
        if params.get("ArticleSet") is not None:
            self.ArticleSet = []
            for item in params.get("ArticleSet"):
                obj = BrandReportArticle()
                obj._deserialize(item)
                self.ArticleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandSocialReportRequest(AbstractModel):
    """DescribeBrandSocialReport请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        :param StartDate: 查询开始时间\n        :type StartDate: str\n        :param EndDate: 查询结束时间\n        :type EndDate: str\n        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBrandSocialReportResponse(AbstractModel):
    """DescribeBrandSocialReport返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 累计统计数据\n        :type TotalCount: int\n        :param DateCountSet: 按天计算的统计数据\n        :type DateCountSet: list of DateCount\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIndustryNewsRequest(AbstractModel):
    """DescribeIndustryNews请求参数结构体

    """

    def __init__(self):
        """
        :param IndustryId: 行业ID\n        :type IndustryId: str\n        :param StartDate: 查询开始时间\n        :type StartDate: str\n        :param EndDate: 查询结束时间\n        :type EndDate: str\n        :param ShowList: 是否显示列表，若为 true，则返回文章列表\n        :type ShowList: bool\n        :param Offset: 查询偏移，默认从0开始\n        :type Offset: int\n        :param Limit: 查询条数上限，默认20\n        :type Limit: int\n        """
        self.IndustryId = None
        self.StartDate = None
        self.EndDate = None
        self.ShowList = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.IndustryId = params.get("IndustryId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ShowList = params.get("ShowList")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIndustryNewsResponse(AbstractModel):
    """DescribeIndustryNews返回参数结构体

    """

    def __init__(self):
        """
        :param NewsCount: 总计文章数量\n        :type NewsCount: int\n        :param FromCount: 总计来源数量\n        :type FromCount: int\n        :param AdverseCount: 总计疑似负面数量\n        :type AdverseCount: int\n        :param NewsSet: 文章列表\n        :type NewsSet: list of IndustryNews\n        :param DateCountSet: 按天统计的数量列表\n        :type DateCountSet: list of DateCount\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NewsCount = None
        self.FromCount = None
        self.AdverseCount = None
        self.NewsSet = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NewsCount = params.get("NewsCount")
        self.FromCount = params.get("FromCount")
        self.AdverseCount = params.get("AdverseCount")
        if params.get("NewsSet") is not None:
            self.NewsSet = []
            for item in params.get("NewsSet"):
                obj = IndustryNews()
                obj._deserialize(item)
                self.NewsSet.append(obj)
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserPortraitRequest(AbstractModel):
    """DescribeUserPortrait请求参数结构体

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID\n        :type BrandId: str\n        """
        self.BrandId = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserPortraitResponse(AbstractModel):
    """DescribeUserPortrait返回参数结构体

    """

    def __init__(self):
        """
        :param Age: 年龄画像\n        :type Age: :class:`tencentcloud.tbm.v20180129.models.AgePortraitInfo`\n        :param Gender: 性别画像\n        :type Gender: :class:`tencentcloud.tbm.v20180129.models.GenderPortraitInfo`\n        :param Province: 省份画像\n        :type Province: :class:`tencentcloud.tbm.v20180129.models.ProvincePortraitInfo`\n        :param Movie: 电影喜好画像\n        :type Movie: :class:`tencentcloud.tbm.v20180129.models.MoviePortraitInfo`\n        :param Star: 明星喜好画像\n        :type Star: :class:`tencentcloud.tbm.v20180129.models.StarPortraitInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Age = None
        self.Gender = None
        self.Province = None
        self.Movie = None
        self.Star = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Age") is not None:
            self.Age = AgePortraitInfo()
            self.Age._deserialize(params.get("Age"))
        if params.get("Gender") is not None:
            self.Gender = GenderPortraitInfo()
            self.Gender._deserialize(params.get("Gender"))
        if params.get("Province") is not None:
            self.Province = ProvincePortraitInfo()
            self.Province._deserialize(params.get("Province"))
        if params.get("Movie") is not None:
            self.Movie = MoviePortraitInfo()
            self.Movie._deserialize(params.get("Movie"))
        if params.get("Star") is not None:
            self.Star = StarPortraitInfo()
            self.Star._deserialize(params.get("Star"))
        self.RequestId = params.get("RequestId")


class GenderPortrait(AbstractModel):
    """性别画像元素

    """

    def __init__(self):
        """
        :param Gender: 性别\n        :type Gender: str\n        :param Percent: 百分比\n        :type Percent: int\n        """
        self.Gender = None
        self.Percent = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenderPortraitInfo(AbstractModel):
    """用户性别画像元素数组

    """

    def __init__(self):
        """
        :param PortraitSet: 用户性别画像数组\n        :type PortraitSet: list of GenderPortrait\n        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = GenderPortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IndustryNews(AbstractModel):
    """行业报道新闻

    """

    def __init__(self):
        """
        :param IndustryId: 行业报道ID\n        :type IndustryId: str\n        :param PubTime: 报道发表时间\n        :type PubTime: str\n        :param FromSite: 报道来源\n        :type FromSite: str\n        :param Title: 报道标题\n        :type Title: str\n        :param Url: 报道来源url\n        :type Url: str\n        :param Level: 报道来源等级\n        :type Level: int\n        :param Hot: 热度值\n        :type Hot: int\n        :param Flag: 报道标识\n        :type Flag: int\n        :param Abstract: 报道摘要\n        :type Abstract: str\n        """
        self.IndustryId = None
        self.PubTime = None
        self.FromSite = None
        self.Title = None
        self.Url = None
        self.Level = None
        self.Hot = None
        self.Flag = None
        self.Abstract = None


    def _deserialize(self, params):
        self.IndustryId = params.get("IndustryId")
        self.PubTime = params.get("PubTime")
        self.FromSite = params.get("FromSite")
        self.Title = params.get("Title")
        self.Url = params.get("Url")
        self.Level = params.get("Level")
        self.Hot = params.get("Hot")
        self.Flag = params.get("Flag")
        self.Abstract = params.get("Abstract")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoviePortrait(AbstractModel):
    """电影喜好画像元素

    """

    def __init__(self):
        """
        :param Name: 电影名称\n        :type Name: str\n        :param Percent: 百分比\n        :type Percent: float\n        """
        self.Name = None
        self.Percent = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoviePortraitInfo(AbstractModel):
    """用户喜好电影画像元素数组

    """

    def __init__(self):
        """
        :param PortraitSet: 用户喜好电影画像数组\n        :type PortraitSet: list of MoviePortrait\n        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = MoviePortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProvincePortrait(AbstractModel):
    """省份画像元素

    """

    def __init__(self):
        """
        :param Province: 省份名称\n        :type Province: str\n        :param Percent: 百分比\n        :type Percent: float\n        """
        self.Province = None
        self.Percent = None


    def _deserialize(self, params):
        self.Province = params.get("Province")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProvincePortraitInfo(AbstractModel):
    """用户省份画像元素数组

    """

    def __init__(self):
        """
        :param PortraitSet: 用户省份画像数组\n        :type PortraitSet: list of ProvincePortrait\n        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = ProvincePortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StarPortrait(AbstractModel):
    """明星喜好画像元素

    """

    def __init__(self):
        """
        :param Name: 喜欢的明星名字\n        :type Name: str\n        :param Percent: 百分比\n        :type Percent: float\n        """
        self.Name = None
        self.Percent = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StarPortraitInfo(AbstractModel):
    """用户喜好的明星画像元素数组

    """

    def __init__(self):
        """
        :param PortraitSet: 用户喜好的明星画像数组\n        :type PortraitSet: list of StarPortrait\n        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = StarPortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        