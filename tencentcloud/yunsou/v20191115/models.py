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
        """
        :param OpType: 操作类型，add或del\n        :type OpType: str\n        :param Encoding: 数据编码类型\n        :type Encoding: str\n        :param Contents: 数据\n        :type Contents: str\n        :param ResourceId: 应用Id\n        :type ResourceId: int\n        """
        self.OpType = None
        self.Encoding = None
        self.Contents = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.OpType = params.get("OpType")
        self.Encoding = params.get("Encoding")
        self.Contents = params.get("Contents")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataManipulationResponse(AbstractModel):
    """DataManipulation返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 数据操作结果\n        :type Data: :class:`tencentcloud.yunsou.v20191115.models.DataManipulationResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DataManipulationResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DataManipulationResult(AbstractModel):
    """数据操作结果

    """

    def __init__(self):
        """
        :param AppId: 应用ID\n        :type AppId: int\n        :param Seq: 序号\n        :type Seq: int\n        :param TotalResult: 结果\n        :type TotalResult: str\n        :param Result: 操作结果明细
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: list of DataManipulationResultItem\n        :param ErrorResult: 异常信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorResult: str\n        """
        self.AppId = None
        self.Seq = None
        self.TotalResult = None
        self.Result = None
        self.ErrorResult = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Seq = params.get("Seq")
        self.TotalResult = params.get("TotalResult")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = DataManipulationResultItem()
                obj._deserialize(item)
                self.Result.append(obj)
        self.ErrorResult = params.get("ErrorResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataManipulationResultItem(AbstractModel):
    """数据操作结果明细

    """

    def __init__(self):
        """
        :param Result: 结果\n        :type Result: str\n        :param DocId: 文档ID\n        :type DocId: str\n        :param Errno: 错误码\n        :type Errno: int\n        """
        self.Result = None
        self.DocId = None
        self.Errno = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.DocId = params.get("DocId")
        self.Errno = params.get("Errno")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchRequest(AbstractModel):
    """DataSearch请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 云搜的业务ID，用以表明当前数据请求的业务\n        :type ResourceId: int\n        :param SearchQuery: 检索串\n        :type SearchQuery: str\n        :param PageId: 当前页，从第0页开始计算\n        :type PageId: int\n        :param NumPerPage: 每页结果数\n        :type NumPerPage: int\n        :param SearchId: 当前检索号，用于定位问题，建议指定并且全局唯一\n        :type SearchId: str\n        :param QueryEncode: 请求编码，0表示utf8，1表示gbk，建议指定\n        :type QueryEncode: int\n        :param RankType: 排序类型\n        :type RankType: int\n        :param NumFilter: 数值过滤，结果中按属性过滤\n        :type NumFilter: str\n        :param ClFilter: 分类过滤，导航类检索请求\n        :type ClFilter: str\n        :param Extra: 检索用户相关字段\n        :type Extra: str\n        :param SourceId: 检索来源\n        :type SourceId: int\n        :param SecondSearch: 是否进行二次检索，0关闭，1打开\n        :type SecondSearch: int\n        :param MaxDocReturn: 指定返回最大篇数，无特殊原因不建议指定\n        :type MaxDocReturn: int\n        :param IsSmartbox: 是否smartbox检索，0关闭，1打开\n        :type IsSmartbox: int\n        :param EnableAbsHighlight: 是否打开高红标亮，0关闭，1打开\n        :type EnableAbsHighlight: int\n        :param QcBid: 指定访问QC纠错业务ID\n        :type QcBid: int\n        :param GroupBy: 按指定字段进行group by，只能对数值字段进行操作\n        :type GroupBy: str\n        :param Distinct: 按指定字段进行distinct，只能对数值字段进行操作\n        :type Distinct: str\n        :param L4RankExpression: 高级排序参数，具体参见高级排序说明\n        :type L4RankExpression: str\n        :param MatchValue: 高级排序参数，具体参见高级排序说明\n        :type MatchValue: str\n        :param Longitude: 经度信息\n        :type Longitude: float\n        :param Latitude: 纬度信息\n        :type Latitude: float\n        :param MultiFilter: 分类过滤并集\n        :type MultiFilter: list of str\n        """
        self.ResourceId = None
        self.SearchQuery = None
        self.PageId = None
        self.NumPerPage = None
        self.SearchId = None
        self.QueryEncode = None
        self.RankType = None
        self.NumFilter = None
        self.ClFilter = None
        self.Extra = None
        self.SourceId = None
        self.SecondSearch = None
        self.MaxDocReturn = None
        self.IsSmartbox = None
        self.EnableAbsHighlight = None
        self.QcBid = None
        self.GroupBy = None
        self.Distinct = None
        self.L4RankExpression = None
        self.MatchValue = None
        self.Longitude = None
        self.Latitude = None
        self.MultiFilter = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.SearchQuery = params.get("SearchQuery")
        self.PageId = params.get("PageId")
        self.NumPerPage = params.get("NumPerPage")
        self.SearchId = params.get("SearchId")
        self.QueryEncode = params.get("QueryEncode")
        self.RankType = params.get("RankType")
        self.NumFilter = params.get("NumFilter")
        self.ClFilter = params.get("ClFilter")
        self.Extra = params.get("Extra")
        self.SourceId = params.get("SourceId")
        self.SecondSearch = params.get("SecondSearch")
        self.MaxDocReturn = params.get("MaxDocReturn")
        self.IsSmartbox = params.get("IsSmartbox")
        self.EnableAbsHighlight = params.get("EnableAbsHighlight")
        self.QcBid = params.get("QcBid")
        self.GroupBy = params.get("GroupBy")
        self.Distinct = params.get("Distinct")
        self.L4RankExpression = params.get("L4RankExpression")
        self.MatchValue = params.get("MatchValue")
        self.Longitude = params.get("Longitude")
        self.Latitude = params.get("Latitude")
        self.MultiFilter = params.get("MultiFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSearchResponse(AbstractModel):
    """DataSearch返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 检索结果\n        :type Data: :class:`tencentcloud.yunsou.v20191115.models.SearchResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SearchResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """搜索结果

    """

    def __init__(self):
        """
        :param CostTime: 检索耗时，单位ms\n        :type CostTime: int\n        :param DisplayNum: 搜索最多可以展示的结果数，多页\n        :type DisplayNum: int\n        :param Echo: 和检索请求中的echo相对应\n        :type Echo: str\n        :param EResultNum: 检索结果的估算篇数，由索引平台估算\n        :type EResultNum: int\n        :param ResultNum: 检索返回的当前页码结果数\n        :type ResultNum: int\n        :param ResultList: 检索结果列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultList: list of SearchResultItem\n        :param SegList: 检索的分词结果，array类型，可包含多个
注意：此字段可能返回 null，表示取不到有效值。\n        :type SegList: list of SearchResultSeg\n        """
        self.CostTime = None
        self.DisplayNum = None
        self.Echo = None
        self.EResultNum = None
        self.ResultNum = None
        self.ResultList = None
        self.SegList = None


    def _deserialize(self, params):
        self.CostTime = params.get("CostTime")
        self.DisplayNum = params.get("DisplayNum")
        self.Echo = params.get("Echo")
        self.EResultNum = params.get("EResultNum")
        self.ResultNum = params.get("ResultNum")
        if params.get("ResultList") is not None:
            self.ResultList = []
            for item in params.get("ResultList"):
                obj = SearchResultItem()
                obj._deserialize(item)
                self.ResultList.append(obj)
        if params.get("SegList") is not None:
            self.SegList = []
            for item in params.get("SegList"):
                obj = SearchResultSeg()
                obj._deserialize(item)
                self.SegList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResultItem(AbstractModel):
    """搜索结果元素

    """

    def __init__(self):
        """
        :param DocAbs: 动态摘要信息\n        :type DocAbs: str\n        :param DocId: 检索文档id\n        :type DocId: str\n        :param DocMeta: 原始文档信息\n        :type DocMeta: str\n        :param L2Score: 精计算得分\n        :type L2Score: float\n        :param SearchDebuginfo: 文档级回传信息\n        :type SearchDebuginfo: str\n        """
        self.DocAbs = None
        self.DocId = None
        self.DocMeta = None
        self.L2Score = None
        self.SearchDebuginfo = None


    def _deserialize(self, params):
        self.DocAbs = params.get("DocAbs")
        self.DocId = params.get("DocId")
        self.DocMeta = params.get("DocMeta")
        self.L2Score = params.get("L2Score")
        self.SearchDebuginfo = params.get("SearchDebuginfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResultSeg(AbstractModel):
    """SearchResultSeg

    """

    def __init__(self):
        """
        :param SegStr: 分词\n        :type SegStr: str\n        """
        self.SegStr = None


    def _deserialize(self, params):
        self.SegStr = params.get("SegStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        