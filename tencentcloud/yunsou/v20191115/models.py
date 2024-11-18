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


class DataManipulationRequest(AbstractModel):
    """DataManipulation请求参数结构体

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
        """操作类型，add或del
        :rtype: str
        """
        return self._OpType

    @OpType.setter
    def OpType(self, OpType):
        self._OpType = OpType

    @property
    def Encoding(self):
        """数据编码类型
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Contents(self):
        """数据
        :rtype: str
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def ResourceId(self):
        """应用Id
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
    """DataManipulation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据操作结果
        :type Data: :class:`tencentcloud.yunsou.v20191115.models.DataManipulationResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """数据操作结果
        :rtype: :class:`tencentcloud.yunsou.v20191115.models.DataManipulationResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DataManipulationResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DataManipulationResult(AbstractModel):
    """数据操作结果

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: int
        :param _Seq: 序号
        :type Seq: int
        :param _TotalResult: 结果
        :type TotalResult: str
        :param _Result: 操作结果明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of DataManipulationResultItem
        :param _ErrorResult: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorResult: str
        """
        self._AppId = None
        self._Seq = None
        self._TotalResult = None
        self._Result = None
        self._ErrorResult = None

    @property
    def AppId(self):
        """应用ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Seq(self):
        """序号
        :rtype: int
        """
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def TotalResult(self):
        """结果
        :rtype: str
        """
        return self._TotalResult

    @TotalResult.setter
    def TotalResult(self, TotalResult):
        self._TotalResult = TotalResult

    @property
    def Result(self):
        """操作结果明细
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DataManipulationResultItem
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrorResult(self):
        """异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorResult

    @ErrorResult.setter
    def ErrorResult(self, ErrorResult):
        self._ErrorResult = ErrorResult


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Seq = params.get("Seq")
        self._TotalResult = params.get("TotalResult")
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = DataManipulationResultItem()
                obj._deserialize(item)
                self._Result.append(obj)
        self._ErrorResult = params.get("ErrorResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataManipulationResultItem(AbstractModel):
    """数据操作结果明细

    """

    def __init__(self):
        r"""
        :param _Result: 结果
        :type Result: str
        :param _DocId: 文档ID
        :type DocId: str
        :param _Errno: 错误码
        :type Errno: int
        """
        self._Result = None
        self._DocId = None
        self._Errno = None

    @property
    def Result(self):
        """结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def DocId(self):
        """文档ID
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def Errno(self):
        """错误码
        :rtype: int
        """
        return self._Errno

    @Errno.setter
    def Errno(self, Errno):
        self._Errno = Errno


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._DocId = params.get("DocId")
        self._Errno = params.get("Errno")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchRequest(AbstractModel):
    """DataSearch请求参数结构体

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
        """云搜的业务ID，用以表明当前数据请求的业务
        :rtype: int
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def SearchQuery(self):
        """检索串
        :rtype: str
        """
        return self._SearchQuery

    @SearchQuery.setter
    def SearchQuery(self, SearchQuery):
        self._SearchQuery = SearchQuery

    @property
    def PageId(self):
        """当前页，从第0页开始计算
        :rtype: int
        """
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def NumPerPage(self):
        """每页结果数
        :rtype: int
        """
        return self._NumPerPage

    @NumPerPage.setter
    def NumPerPage(self, NumPerPage):
        self._NumPerPage = NumPerPage

    @property
    def SearchId(self):
        """当前检索号，用于定位问题，建议指定并且全局唯一
        :rtype: str
        """
        return self._SearchId

    @SearchId.setter
    def SearchId(self, SearchId):
        self._SearchId = SearchId

    @property
    def QueryEncode(self):
        """请求编码，0表示utf8，1表示gbk，建议指定
        :rtype: int
        """
        return self._QueryEncode

    @QueryEncode.setter
    def QueryEncode(self, QueryEncode):
        self._QueryEncode = QueryEncode

    @property
    def RankType(self):
        """排序类型
        :rtype: int
        """
        return self._RankType

    @RankType.setter
    def RankType(self, RankType):
        self._RankType = RankType

    @property
    def NumFilter(self):
        """数值过滤，结果中按属性过滤
        :rtype: str
        """
        return self._NumFilter

    @NumFilter.setter
    def NumFilter(self, NumFilter):
        self._NumFilter = NumFilter

    @property
    def ClFilter(self):
        """分类过滤，导航类检索请求
        :rtype: str
        """
        return self._ClFilter

    @ClFilter.setter
    def ClFilter(self, ClFilter):
        self._ClFilter = ClFilter

    @property
    def Extra(self):
        """检索用户相关字段
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def SourceId(self):
        """检索来源
        :rtype: int
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SecondSearch(self):
        """是否进行二次检索，0关闭，1打开
        :rtype: int
        """
        return self._SecondSearch

    @SecondSearch.setter
    def SecondSearch(self, SecondSearch):
        self._SecondSearch = SecondSearch

    @property
    def MaxDocReturn(self):
        """指定返回最大篇数，无特殊原因不建议指定
        :rtype: int
        """
        return self._MaxDocReturn

    @MaxDocReturn.setter
    def MaxDocReturn(self, MaxDocReturn):
        self._MaxDocReturn = MaxDocReturn

    @property
    def IsSmartbox(self):
        """是否smartbox检索，0关闭，1打开
        :rtype: int
        """
        return self._IsSmartbox

    @IsSmartbox.setter
    def IsSmartbox(self, IsSmartbox):
        self._IsSmartbox = IsSmartbox

    @property
    def EnableAbsHighlight(self):
        """是否打开高红标亮，0关闭，1打开
        :rtype: int
        """
        return self._EnableAbsHighlight

    @EnableAbsHighlight.setter
    def EnableAbsHighlight(self, EnableAbsHighlight):
        self._EnableAbsHighlight = EnableAbsHighlight

    @property
    def QcBid(self):
        """指定访问QC纠错业务ID
        :rtype: int
        """
        return self._QcBid

    @QcBid.setter
    def QcBid(self, QcBid):
        self._QcBid = QcBid

    @property
    def GroupBy(self):
        """按指定字段进行group by，只能对数值字段进行操作
        :rtype: str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def Distinct(self):
        """按指定字段进行distinct，只能对数值字段进行操作
        :rtype: str
        """
        return self._Distinct

    @Distinct.setter
    def Distinct(self, Distinct):
        self._Distinct = Distinct

    @property
    def L4RankExpression(self):
        """高级排序参数，具体参见高级排序说明
        :rtype: str
        """
        return self._L4RankExpression

    @L4RankExpression.setter
    def L4RankExpression(self, L4RankExpression):
        self._L4RankExpression = L4RankExpression

    @property
    def MatchValue(self):
        """高级排序参数，具体参见高级排序说明
        :rtype: str
        """
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def Longitude(self):
        """经度信息
        :rtype: float
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        """纬度信息
        :rtype: float
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def MultiFilter(self):
        """分类过滤并集
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
    """DataSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 检索结果
        :type Data: :class:`tencentcloud.yunsou.v20191115.models.SearchResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """检索结果
        :rtype: :class:`tencentcloud.yunsou.v20191115.models.SearchResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SearchResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """搜索结果

    """

    def __init__(self):
        r"""
        :param _CostTime: 检索耗时，单位ms
        :type CostTime: int
        :param _DisplayNum: 搜索最多可以展示的结果数，多页
        :type DisplayNum: int
        :param _Echo: 和检索请求中的echo相对应
        :type Echo: str
        :param _EResultNum: 检索结果的估算篇数，由索引平台估算
        :type EResultNum: int
        :param _ResultNum: 检索返回的当前页码结果数
        :type ResultNum: int
        :param _ResultList: 检索结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultList: list of SearchResultItem
        :param _SegList: 检索的分词结果，array类型，可包含多个
注意：此字段可能返回 null，表示取不到有效值。
        :type SegList: list of SearchResultSeg
        """
        self._CostTime = None
        self._DisplayNum = None
        self._Echo = None
        self._EResultNum = None
        self._ResultNum = None
        self._ResultList = None
        self._SegList = None

    @property
    def CostTime(self):
        """检索耗时，单位ms
        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def DisplayNum(self):
        """搜索最多可以展示的结果数，多页
        :rtype: int
        """
        return self._DisplayNum

    @DisplayNum.setter
    def DisplayNum(self, DisplayNum):
        self._DisplayNum = DisplayNum

    @property
    def Echo(self):
        """和检索请求中的echo相对应
        :rtype: str
        """
        return self._Echo

    @Echo.setter
    def Echo(self, Echo):
        self._Echo = Echo

    @property
    def EResultNum(self):
        """检索结果的估算篇数，由索引平台估算
        :rtype: int
        """
        return self._EResultNum

    @EResultNum.setter
    def EResultNum(self, EResultNum):
        self._EResultNum = EResultNum

    @property
    def ResultNum(self):
        """检索返回的当前页码结果数
        :rtype: int
        """
        return self._ResultNum

    @ResultNum.setter
    def ResultNum(self, ResultNum):
        self._ResultNum = ResultNum

    @property
    def ResultList(self):
        """检索结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SearchResultItem
        """
        return self._ResultList

    @ResultList.setter
    def ResultList(self, ResultList):
        self._ResultList = ResultList

    @property
    def SegList(self):
        """检索的分词结果，array类型，可包含多个
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SearchResultSeg
        """
        return self._SegList

    @SegList.setter
    def SegList(self, SegList):
        self._SegList = SegList


    def _deserialize(self, params):
        self._CostTime = params.get("CostTime")
        self._DisplayNum = params.get("DisplayNum")
        self._Echo = params.get("Echo")
        self._EResultNum = params.get("EResultNum")
        self._ResultNum = params.get("ResultNum")
        if params.get("ResultList") is not None:
            self._ResultList = []
            for item in params.get("ResultList"):
                obj = SearchResultItem()
                obj._deserialize(item)
                self._ResultList.append(obj)
        if params.get("SegList") is not None:
            self._SegList = []
            for item in params.get("SegList"):
                obj = SearchResultSeg()
                obj._deserialize(item)
                self._SegList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResultItem(AbstractModel):
    """搜索结果元素

    """

    def __init__(self):
        r"""
        :param _DocAbs: 动态摘要信息
        :type DocAbs: str
        :param _DocId: 检索文档id
        :type DocId: str
        :param _DocMeta: 原始文档信息
        :type DocMeta: str
        :param _L2Score: 精计算得分
        :type L2Score: float
        :param _SearchDebuginfo: 文档级回传信息
        :type SearchDebuginfo: str
        """
        self._DocAbs = None
        self._DocId = None
        self._DocMeta = None
        self._L2Score = None
        self._SearchDebuginfo = None

    @property
    def DocAbs(self):
        """动态摘要信息
        :rtype: str
        """
        return self._DocAbs

    @DocAbs.setter
    def DocAbs(self, DocAbs):
        self._DocAbs = DocAbs

    @property
    def DocId(self):
        """检索文档id
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def DocMeta(self):
        """原始文档信息
        :rtype: str
        """
        return self._DocMeta

    @DocMeta.setter
    def DocMeta(self, DocMeta):
        self._DocMeta = DocMeta

    @property
    def L2Score(self):
        """精计算得分
        :rtype: float
        """
        return self._L2Score

    @L2Score.setter
    def L2Score(self, L2Score):
        self._L2Score = L2Score

    @property
    def SearchDebuginfo(self):
        """文档级回传信息
        :rtype: str
        """
        return self._SearchDebuginfo

    @SearchDebuginfo.setter
    def SearchDebuginfo(self, SearchDebuginfo):
        self._SearchDebuginfo = SearchDebuginfo


    def _deserialize(self, params):
        self._DocAbs = params.get("DocAbs")
        self._DocId = params.get("DocId")
        self._DocMeta = params.get("DocMeta")
        self._L2Score = params.get("L2Score")
        self._SearchDebuginfo = params.get("SearchDebuginfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResultSeg(AbstractModel):
    """SearchResultSeg

    """

    def __init__(self):
        r"""
        :param _SegStr: 分词
        :type SegStr: str
        """
        self._SegStr = None

    @property
    def SegStr(self):
        """分词
        :rtype: str
        """
        return self._SegStr

    @SegStr.setter
    def SegStr(self, SegStr):
        self._SegStr = SegStr


    def _deserialize(self, params):
        self._SegStr = params.get("SegStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        