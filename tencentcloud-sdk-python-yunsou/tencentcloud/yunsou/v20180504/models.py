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

from tencentcloud.common.abstract_model import AbstractModel


class DataManipulationRequest(AbstractModel):
    """DataManipulation请求参数结构体

    """

    def __init__(self):
        """
        :param OpType: 操作类型，add或del
        :type OpType: str
        :param Encoding: 数据编码类型
        :type Encoding: str
        :param Contents: 数据
        :type Contents: str
        :param ResourceId: 应用Id
        :type ResourceId: int
        """
        self.OpType = None
        self.Encoding = None
        self.Contents = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.OpType = params.get("OpType")
        self.Encoding = params.get("Encoding")
        self.Contents = params.get("Contents")
        self.ResourceId = params.get("ResourceId")


class DataManipulationResponse(AbstractModel):
    """DataManipulation返回参数结构体

    """

    def __init__(self):
        """
        :param RetMsg: 返回信息
        :type RetMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RetMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")


class DataSearchRequest(AbstractModel):
    """DataSearch请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 云搜的业务ID，用以表明当前数据请求的业务
        :type ResourceId: int
        :param SearchQuery: 检索串
        :type SearchQuery: str
        :param PageId: 当前页，从第0页开始计算
        :type PageId: int
        :param NumPerPage: 每页结果数
        :type NumPerPage: int
        :param SearchId: 当前检索号，用于定位问题，建议指定并且全局唯一
        :type SearchId: str
        :param QueryEncode: 请求编码，0表示utf8，1表示gbk，建议指定
        :type QueryEncode: int
        :param RankType: 排序类型
        :type RankType: int
        :param NumFilter: 数值过滤，结果中按属性过滤
        :type NumFilter: str
        :param ClFilter: 分类过滤，导航类检索请求
        :type ClFilter: str
        :param Extra: 检索用户相关字段
        :type Extra: str
        :param SourceId: 检索来源
        :type SourceId: int
        :param SecondSearch: 是否进行二次检索，0关闭，1打开
        :type SecondSearch: int
        :param MaxDocReturn: 指定返回最大篇数，无特殊原因不建议指定
        :type MaxDocReturn: int
        :param IsSmartbox: 是否smartbox检索，0关闭，1打开
        :type IsSmartbox: int
        :param EnableAbsHighlight: 是否打开高红标亮，0关闭，1打开
        :type EnableAbsHighlight: int
        :param QcBid: 指定访问QC纠错业务ID
        :type QcBid: int
        :param GroupBy: 按指定字段进行group by，只能对数值字段进行操作
        :type GroupBy: str
        :param Distinct: 按指定字段进行distinct，只能对数值字段进行操作
        :type Distinct: str
        :param L4RankExpression: 高级排序参数，具体参见高级排序说明
        :type L4RankExpression: str
        :param MatchValue: 高级排序参数，具体参见高级排序说明
        :type MatchValue: str
        :param Longitude: 经度信息
        :type Longitude: float
        :param Latitude: 纬度信息
        :type Latitude: float
        :param MultiFilter: 分类过滤并集
        :type MultiFilter: list of str
        """
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


class DataSearchResponse(AbstractModel):
    """DataSearch返回参数结构体

    """

    def __init__(self):
        """
        :param RetMsg: 数据返回信息
        :type RetMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RetMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")