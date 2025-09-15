# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class DataManipulationRequest(AbstractModel):
    r"""DataManipulation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OpType: 操作类型，add或del
        :type OpType: str
        :param _Encoding: 数据编码类型
        :type Encoding: str
        :param _Contents: 数据
        :type Contents: str
        :param _ResourceId: 应用Id
        :type ResourceId: int
        """
        self._OpType = None
        self._Encoding = None
        self._Contents = None
        self._ResourceId = None

    @property
    def OpType(self):
        r"""操作类型，add或del
        :rtype: str
        """
        return self._OpType

    @OpType.setter
    def OpType(self, OpType):
        self._OpType = OpType

    @property
    def Encoding(self):
        r"""数据编码类型
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Contents(self):
        r"""数据
        :rtype: str
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def ResourceId(self):
        r"""应用Id
        :rtype: int
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._OpType = params.get("OpType")
        self._Encoding = params.get("Encoding")
        self._Contents = params.get("Contents")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataManipulationResponse(AbstractModel):
    r"""DataManipulation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RetMsg: 返回信息
        :type RetMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RetMsg = None
        self._RequestId = None

    @property
    def RetMsg(self):
        r"""返回信息
        :rtype: str
        """
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RetMsg = params.get("RetMsg")
        self._RequestId = params.get("RequestId")


class DataSearchRequest(AbstractModel):
    r"""DataSearch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 云搜的业务ID，用以表明当前数据请求的业务
        :type ResourceId: int
        :param _SearchQuery: 检索串
        :type SearchQuery: str
        :param _PageId: 当前页，从第0页开始计算
        :type PageId: int
        :param _NumPerPage: 每页结果数
        :type NumPerPage: int
        :param _SearchId: 当前检索号，用于定位问题，建议指定并且全局唯一
        :type SearchId: str
        :param _QueryEncode: 请求编码，0表示utf8，1表示gbk，建议指定
        :type QueryEncode: int
        :param _RankType: 排序类型
        :type RankType: int
        :param _NumFilter: 数值过滤，结果中按属性过滤
        :type NumFilter: str
        :param _ClFilter: 分类过滤，导航类检索请求
        :type ClFilter: str
        :param _Extra: 检索用户相关字段
        :type Extra: str
        :param _SourceId: 检索来源
        :type SourceId: int
        :param _SecondSearch: 是否进行二次检索，0关闭，1打开
        :type SecondSearch: int
        :param _MaxDocReturn: 指定返回最大篇数，无特殊原因不建议指定
        :type MaxDocReturn: int
        :param _IsSmartbox: 是否smartbox检索，0关闭，1打开
        :type IsSmartbox: int
        :param _EnableAbsHighlight: 是否打开高红标亮，0关闭，1打开
        :type EnableAbsHighlight: int
        :param _QcBid: 指定访问QC纠错业务ID
        :type QcBid: int
        :param _GroupBy: 按指定字段进行group by，只能对数值字段进行操作
        :type GroupBy: str
        :param _Distinct: 按指定字段进行distinct，只能对数值字段进行操作
        :type Distinct: str
        :param _L4RankExpression: 高级排序参数，具体参见高级排序说明
        :type L4RankExpression: str
        :param _MatchValue: 高级排序参数，具体参见高级排序说明
        :type MatchValue: str
        :param _Longitude: 经度信息
        :type Longitude: float
        :param _Latitude: 纬度信息
        :type Latitude: float
        :param _MultiFilter: 分类过滤并集
        :type MultiFilter: list of str
        """
        self._ResourceId = None
        self._SearchQuery = None
        self._PageId = None
        self._NumPerPage = None
        self._SearchId = None
        self._QueryEncode = None
        self._RankType = None
        self._NumFilter = None
        self._ClFilter = None
        self._Extra = None
        self._SourceId = None
        self._SecondSearch = None
        self._MaxDocReturn = None
        self._IsSmartbox = None
        self._EnableAbsHighlight = None
        self._QcBid = None
        self._GroupBy = None
        self._Distinct = None
        self._L4RankExpression = None
        self._MatchValue = None
        self._Longitude = None
        self._Latitude = None
        self._MultiFilter = None

    @property
    def ResourceId(self):
        r"""云搜的业务ID，用以表明当前数据请求的业务
        :rtype: int
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def SearchQuery(self):
        r"""检索串
        :rtype: str
        """
        return self._SearchQuery

    @SearchQuery.setter
    def SearchQuery(self, SearchQuery):
        self._SearchQuery = SearchQuery

    @property
    def PageId(self):
        r"""当前页，从第0页开始计算
        :rtype: int
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def NumPerPage(self):
        r"""每页结果数
        :rtype: int
        """
        return self._NumPerPage

    @NumPerPage.setter
    def NumPerPage(self, NumPerPage):
        self._NumPerPage = NumPerPage

    @property
    def SearchId(self):
        r"""当前检索号，用于定位问题，建议指定并且全局唯一
        :rtype: str
        """
        return self._SearchId

    @SearchId.setter
    def SearchId(self, SearchId):
        self._SearchId = SearchId

    @property
    def QueryEncode(self):
        r"""请求编码，0表示utf8，1表示gbk，建议指定
        :rtype: int
        """
        return self._QueryEncode

    @QueryEncode.setter
    def QueryEncode(self, QueryEncode):
        self._QueryEncode = QueryEncode

    @property
    def RankType(self):
        r"""排序类型
        :rtype: int
        """
        return self._RankType

    @RankType.setter
    def RankType(self, RankType):
        self._RankType = RankType

    @property
    def NumFilter(self):
        r"""数值过滤，结果中按属性过滤
        :rtype: str
        """
        return self._NumFilter

    @NumFilter.setter
    def NumFilter(self, NumFilter):
        self._NumFilter = NumFilter

    @property
    def ClFilter(self):
        r"""分类过滤，导航类检索请求
        :rtype: str
        """
        return self._ClFilter

    @ClFilter.setter
    def ClFilter(self, ClFilter):
        self._ClFilter = ClFilter

    @property
    def Extra(self):
        r"""检索用户相关字段
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def SourceId(self):
        r"""检索来源
        :rtype: int
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SecondSearch(self):
        r"""是否进行二次检索，0关闭，1打开
        :rtype: int
        """
        return self._SecondSearch

    @SecondSearch.setter
    def SecondSearch(self, SecondSearch):
        self._SecondSearch = SecondSearch

    @property
    def MaxDocReturn(self):
        r"""指定返回最大篇数，无特殊原因不建议指定
        :rtype: int
        """
        return self._MaxDocReturn

    @MaxDocReturn.setter
    def MaxDocReturn(self, MaxDocReturn):
        self._MaxDocReturn = MaxDocReturn

    @property
    def IsSmartbox(self):
        r"""是否smartbox检索，0关闭，1打开
        :rtype: int
        """
        return self._IsSmartbox

    @IsSmartbox.setter
    def IsSmartbox(self, IsSmartbox):
        self._IsSmartbox = IsSmartbox

    @property
    def EnableAbsHighlight(self):
        r"""是否打开高红标亮，0关闭，1打开
        :rtype: int
        """
        return self._EnableAbsHighlight

    @EnableAbsHighlight.setter
    def EnableAbsHighlight(self, EnableAbsHighlight):
        self._EnableAbsHighlight = EnableAbsHighlight

    @property
    def QcBid(self):
        r"""指定访问QC纠错业务ID
        :rtype: int
        """
        return self._QcBid

    @QcBid.setter
    def QcBid(self, QcBid):
        self._QcBid = QcBid

    @property
    def GroupBy(self):
        r"""按指定字段进行group by，只能对数值字段进行操作
        :rtype: str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Distinct(self):
        r"""按指定字段进行distinct，只能对数值字段进行操作
        :rtype: str
        """
        return self._Distinct

    @Distinct.setter
    def Distinct(self, Distinct):
        self._Distinct = Distinct

    @property
    def L4RankExpression(self):
        r"""高级排序参数，具体参见高级排序说明
        :rtype: str
        """
        return self._L4RankExpression

    @L4RankExpression.setter
    def L4RankExpression(self, L4RankExpression):
        self._L4RankExpression = L4RankExpression

    @property
    def MatchValue(self):
        r"""高级排序参数，具体参见高级排序说明
        :rtype: str
        """
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def Longitude(self):
        r"""经度信息
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""纬度信息
        :rtype: float
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def MultiFilter(self):
        r"""分类过滤并集
        :rtype: list of str
        """
        return self._MultiFilter

    @MultiFilter.setter
    def MultiFilter(self, MultiFilter):
        self._MultiFilter = MultiFilter


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._SearchQuery = params.get("SearchQuery")
        self._PageId = params.get("PageId")
        self._NumPerPage = params.get("NumPerPage")
        self._SearchId = params.get("SearchId")
        self._QueryEncode = params.get("QueryEncode")
        self._RankType = params.get("RankType")
        self._NumFilter = params.get("NumFilter")
        self._ClFilter = params.get("ClFilter")
        self._Extra = params.get("Extra")
        self._SourceId = params.get("SourceId")
        self._SecondSearch = params.get("SecondSearch")
        self._MaxDocReturn = params.get("MaxDocReturn")
        self._IsSmartbox = params.get("IsSmartbox")
        self._EnableAbsHighlight = params.get("EnableAbsHighlight")
        self._QcBid = params.get("QcBid")
        self._GroupBy = params.get("GroupBy")
        self._Distinct = params.get("Distinct")
        self._L4RankExpression = params.get("L4RankExpression")
        self._MatchValue = params.get("MatchValue")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._MultiFilter = params.get("MultiFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchResponse(AbstractModel):
    r"""DataSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RetMsg: 数据返回信息
        :type RetMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RetMsg = None
        self._RequestId = None

    @property
    def RetMsg(self):
        r"""数据返回信息
        :rtype: str
        """
        return self._RetMsg

    @RetMsg.setter
    def RetMsg(self, RetMsg):
        self._RetMsg = RetMsg

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RetMsg = params.get("RetMsg")
        self._RequestId = params.get("RequestId")