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


class AttributeMap(AbstractModel):
    """玩家属性字典类型值

    """

    def __init__(self):
        r"""
        :param Key: 属性字典 key [a-zA-Z0-9-\.]*
        :type Key: str
        :param Value: 属性字典 value
        :type Value: int
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
        


class CancelMatchingRequest(AbstractModel):
    """CancelMatching请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配 Code
        :type MatchCode: str
        :param MatchTicketId: 要取消的匹配匹配票据 ID
        :type MatchTicketId: str
        """
        self.MatchCode = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelMatchingResponse(AbstractModel):
    """CancelMatching返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码
        :type ErrCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.RequestId = params.get("RequestId")


class CreateMatchRequest(AbstractModel):
    """CreateMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchName: 匹配名称，[a-zA-Z0-9-\.]* 长度128
        :type MatchName: str
        :param RuleCode: 规则code
        :type RuleCode: str
        :param Timeout: 超时时间，1-600秒
        :type Timeout: int
        :param ServerType: 是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源
        :type ServerType: int
        :param MatchDesc: 匹配描述，最长1024
        :type MatchDesc: str
        :param NotifyUrl: 只支持https 和 http 协议
        :type NotifyUrl: str
        :param ServerRegion: 游戏服务器队列地域
        :type ServerRegion: str
        :param ServerQueue: 游戏服务器队列
        :type ServerQueue: str
        :param CustomPushData: 自定义推送数据
        :type CustomPushData: str
        :param ServerSessionData: 游戏服务器会话数据
        :type ServerSessionData: str
        :param GameProperties: 游戏属性，key-value结构的数组
        :type GameProperties: list of StringKV
        :param LogSwitch: 日志开关，0表示关，1表示开
        :type LogSwitch: int
        :param Tags: 标签，key-value结构的数组
        :type Tags: list of StringKV
        """
        self.MatchName = None
        self.RuleCode = None
        self.Timeout = None
        self.ServerType = None
        self.MatchDesc = None
        self.NotifyUrl = None
        self.ServerRegion = None
        self.ServerQueue = None
        self.CustomPushData = None
        self.ServerSessionData = None
        self.GameProperties = None
        self.LogSwitch = None
        self.Tags = None


    def _deserialize(self, params):
        self.MatchName = params.get("MatchName")
        self.RuleCode = params.get("RuleCode")
        self.Timeout = params.get("Timeout")
        self.ServerType = params.get("ServerType")
        self.MatchDesc = params.get("MatchDesc")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ServerRegion = params.get("ServerRegion")
        self.ServerQueue = params.get("ServerQueue")
        self.CustomPushData = params.get("CustomPushData")
        self.ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMatchResponse(AbstractModel):
    """CreateMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchInfo: 匹配信息
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称，[a-zA-Z0-9-\.]* 长度128
        :type RuleName: str
        :param RuleScript: 规则脚本，长度65535
        :type RuleScript: str
        :param RuleDesc: 规则描述，最长1024
        :type RuleDesc: str
        :param Tags: 标签，key-value结构的数组，最多关联50组标签
        :type Tags: list of StringKV
        """
        self.RuleName = None
        self.RuleScript = None
        self.RuleDesc = None
        self.Tags = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.RuleScript = params.get("RuleScript")
        self.RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfo: 规则信息
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")


class DeleteMatchRequest(AbstractModel):
    """DeleteMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配code
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMatchResponse(AbstractModel):
    """DeleteMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleCode: 规则code
        :type RuleCode: str
        """
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    """DescribeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param EndTime: 截止时间，单位：秒
        :type EndTime: int
        :param TimeType: 时间粒度，1表示1天；2表示1小时；3表示1分钟；4表示10分钟；5表示30分钟
        :type TimeType: int
        :param MatchCode: 匹配code
        :type MatchCode: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TimeType = None
        self.MatchCode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TimeType = params.get("TimeType")
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param OverviewData: 匹配概况
注意：此字段可能返回 null，表示取不到有效值。
        :type OverviewData: :class:`tencentcloud.gpm.v20200820.models.ReportOverviewData`
        :param TrendData: 匹配请求次数趋势数据
注意：此字段可能返回 null，表示取不到有效值。
        :type TrendData: :class:`tencentcloud.gpm.v20200820.models.ReportTrendData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OverviewData = None
        self.TrendData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OverviewData") is not None:
            self.OverviewData = ReportOverviewData()
            self.OverviewData._deserialize(params.get("OverviewData"))
        if params.get("TrendData") is not None:
            self.TrendData = ReportTrendData()
            self.TrendData._deserialize(params.get("TrendData"))
        self.RequestId = params.get("RequestId")


class DescribeMatchCodesRequest(AbstractModel):
    """DescribeMatchCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，页码
        :type Offset: int
        :param Limit: 每页数量
        :type Limit: int
        :param MatchCode: 搜索的字符串
        :type MatchCode: str
        """
        self.Offset = None
        self.Limit = None
        self.MatchCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchCodesResponse(AbstractModel):
    """DescribeMatchCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCodes: 匹配Code
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchCodes: list of MatchCodeAttr
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchCodes = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchCodes") is not None:
            self.MatchCodes = []
            for item in params.get("MatchCodes"):
                obj = MatchCodeAttr()
                obj._deserialize(item)
                self.MatchCodes.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMatchRequest(AbstractModel):
    """DescribeMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配code
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchResponse(AbstractModel):
    """DescribeMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchInfo: 匹配信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")


class DescribeMatchesRequest(AbstractModel):
    """DescribeMatches请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 当前页号，不传则获取所有有权限的资源。
        :type PageNumber: int
        :param PageSize: 单页大小，不传则获取所有有权限的资源。
        :type PageSize: int
        :param SearchType: 查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。
        :type SearchType: str
        :param Keyword: 查询关键词，针对SearchType进行具体过滤的内容。
        :type Keyword: str
        :param Tags: 标签列表，用于过滤。
        :type Tags: list of Tag
        """
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchesResponse(AbstractModel):
    """DescribeMatches返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchInfoList: 匹配信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchInfoList: list of MatchInfo
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param PageNumber: 当前页号，不填默认返回第一页
        :type PageNumber: int
        :param PageSize: 单页大小，不填默认取 30，最大值不能超过 30
        :type PageSize: int
        :param SearchType: 查询类型（可选）：matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value
        :type SearchType: str
        :param Keyword: 查询关键词（可选）
        :type Keyword: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchInfoList = None
        self.TotalCount = None
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfoList") is not None:
            self.MatchInfoList = []
            for item in params.get("MatchInfoList"):
                obj = MatchInfo()
                obj._deserialize(item)
                self.MatchInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        self.RequestId = params.get("RequestId")


class DescribeMatchingProgressRequest(AbstractModel):
    """DescribeMatchingProgress请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchTicketIds: 匹配票据 ID列表, 列表长度 12。
        :type MatchTicketIds: list of MTicket
        """
        self.MatchTicketIds = None


    def _deserialize(self, params):
        if params.get("MatchTicketIds") is not None:
            self.MatchTicketIds = []
            for item in params.get("MatchTicketIds"):
                obj = MTicket()
                obj._deserialize(item)
                self.MatchTicketIds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchingProgressResponse(AbstractModel):
    """DescribeMatchingProgress返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchTickets: 匹配票据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchTickets: list of MatchTicket
        :param ErrCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchTickets = None
        self.ErrCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchTickets") is not None:
            self.MatchTickets = []
            for item in params.get("MatchTickets"):
                obj = MatchTicket()
                obj._deserialize(item)
                self.MatchTickets.append(obj)
        self.ErrCode = params.get("ErrCode")
        self.RequestId = params.get("RequestId")


class DescribeRuleRequest(AbstractModel):
    """DescribeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleCode: 规则code
        :type RuleCode: str
        """
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfo: 规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNumber: 当前页号，不传则返回第一页
        :type PageNumber: int
        :param PageSize: 单页大小，最大 30，不填默认30
        :type PageSize: int
        :param SearchType: 查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。
        :type SearchType: str
        :param Keyword: 查询关键词，针对SearchType进行具体过滤的内容。
        :type Keyword: str
        :param Tags: 标签列表，用于过滤。
        :type Tags: list of Tag
        """
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfoList: 规则信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleInfoList: list of RuleBriefInfo
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param PageNumber: 当前页号
        :type PageNumber: int
        :param PageSize: 单页大小
        :type PageSize: int
        :param SearchType: 查询类型（可选）matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value
        :type SearchType: str
        :param Keyword: 查询关键词（可选）
        :type Keyword: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleInfoList = None
        self.TotalCount = None
        self.PageNumber = None
        self.PageSize = None
        self.SearchType = None
        self.Keyword = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfoList") is not None:
            self.RuleInfoList = []
            for item in params.get("RuleInfoList"):
                obj = RuleBriefInfo()
                obj._deserialize(item)
                self.RuleInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.SearchType = params.get("SearchType")
        self.Keyword = params.get("Keyword")
        self.RequestId = params.get("RequestId")


class DescribeTokenRequest(AbstractModel):
    """DescribeToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配code
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenResponse(AbstractModel):
    """DescribeToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchToken: 当前的MatchCode对应的Token。如果当前MatchCode没有Token，该参数可能取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchToken: str
        :param CompatibleSpan: 当Token被替换后，GPM将兼容推送原始Token的时间（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CompatibleSpan: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchToken = None
        self.CompatibleSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MatchToken = params.get("MatchToken")
        self.CompatibleSpan = params.get("CompatibleSpan")
        self.RequestId = params.get("RequestId")


class MTicket(AbstractModel):
    """matchCode和匹配票据 ID组合结构

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配Code
        :type MatchCode: str
        :param MatchTicketId: 匹配票据 ID
        :type MatchTicketId: str
        """
        self.MatchCode = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchAttribute(AbstractModel):
    """玩家匹配属性

    """

    def __init__(self):
        r"""
        :param Name: 属性名 长度 128 [a-zA-Z0-9-\.]*
        :type Name: str
        :param Type: 属性类型: 0 数值; 1 string; 默认 0
        :type Type: int
        :param NumberValue: 数字属性值 默认 0.0
        :type NumberValue: float
        :param StringValue: 字符串属性值 长度 128 默认 ""
        :type StringValue: str
        :param ListValue: list 属性值
        :type ListValue: list of str
        :param MapValue: 字典属性值
        :type MapValue: list of AttributeMap
        """
        self.Name = None
        self.Type = None
        self.NumberValue = None
        self.StringValue = None
        self.ListValue = None
        self.MapValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.NumberValue = params.get("NumberValue")
        self.StringValue = params.get("StringValue")
        self.ListValue = params.get("ListValue")
        if params.get("MapValue") is not None:
            self.MapValue = []
            for item in params.get("MapValue"):
                obj = AttributeMap()
                obj._deserialize(item)
                self.MapValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchCodeAttr(AbstractModel):
    """匹配code

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配code
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchCode: str
        """
        self.MatchCode = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchInfo(AbstractModel):
    """匹配信息

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配code
        :type MatchCode: str
        :param MatchName: 匹配名称
        :type MatchName: str
        :param MatchDesc: 匹配描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchDesc: str
        :param RuleCode: 规则code
        :type RuleCode: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Timeout: 超时时间
        :type Timeout: int
        :param NotifyUrl: 接收通知地址
        :type NotifyUrl: str
        :param ServerType: 是否为匹配结果请求服务器资源，0否，1请求GSE资源
        :type ServerType: int
        :param ServerRegion: 服务器队列所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerRegion: str
        :param ServerQueue: 服务器队列
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerQueue: str
        :param CustomPushData: 自定义推送数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomPushData: str
        :param ServerSessionData: 游戏服务器会话数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerSessionData: str
        :param GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of StringKV
        :param LogSwitch: 日志开关，0表示关，1表示开
        :type LogSwitch: int
        :param LogsetId: 日志集id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param LogsetName: 日志集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetName: str
        :param LogTopicId: 日志主题id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        :param LogTopicName: 日志主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicName: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of StringKV
        :param Region: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param Uin: 用户主账号Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param CreateUin: 用户创建账号Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        :param RuleName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param LogStatus: 日志状态，0表示正常，1表示日志集不存在，2表示日志主题不存在，3表示日志集和日志主题都不存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogStatus: int
        """
        self.MatchCode = None
        self.MatchName = None
        self.MatchDesc = None
        self.RuleCode = None
        self.CreateTime = None
        self.Timeout = None
        self.NotifyUrl = None
        self.ServerType = None
        self.ServerRegion = None
        self.ServerQueue = None
        self.CustomPushData = None
        self.ServerSessionData = None
        self.GameProperties = None
        self.LogSwitch = None
        self.LogsetId = None
        self.LogsetName = None
        self.LogTopicId = None
        self.LogTopicName = None
        self.Tags = None
        self.Region = None
        self.AppId = None
        self.Uin = None
        self.CreateUin = None
        self.RuleName = None
        self.LogStatus = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.MatchName = params.get("MatchName")
        self.MatchDesc = params.get("MatchDesc")
        self.RuleCode = params.get("RuleCode")
        self.CreateTime = params.get("CreateTime")
        self.Timeout = params.get("Timeout")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ServerType = params.get("ServerType")
        self.ServerRegion = params.get("ServerRegion")
        self.ServerQueue = params.get("ServerQueue")
        self.CustomPushData = params.get("CustomPushData")
        self.ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.LogSwitch = params.get("LogSwitch")
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.LogTopicId = params.get("LogTopicId")
        self.LogTopicName = params.get("LogTopicName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.CreateUin = params.get("CreateUin")
        self.RuleName = params.get("RuleName")
        self.LogStatus = params.get("LogStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchTicket(AbstractModel):
    """匹配票据信息

    """

    def __init__(self):
        r"""
        :param Id: 匹配票据 ID长度 128 [a-zA-Z0-9-\.]*
        :type Id: str
        :param MatchCode: 匹配 Code
        :type MatchCode: str
        :param MatchResult: 根据 MatchType 取不同的结构序列化结果
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchResult: str
        :param MatchType: 表示不同的匹配类型,NORMAL | GSE
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchType: str
        :param Players: 玩家信息列表
        :type Players: list of Player
        :param Status: 匹配状态: SEARCHING 匹配中; PLACING 匹配放置中; COMPLETED 匹配完成; CANCELLED 匹配取消; TIMEDOUT 匹配超时; FAILED 匹配失败
        :type Status: str
        :param StatusMessage: 匹配状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMessage: str
        :param StatusReason: 匹配状态原因
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReason: str
        :param StartTime: 收到发起匹配请求的时间 eg: "2020-08-17T08:14:38.077Z"
        :type StartTime: str
        :param EndTime: 匹配请求因完成、失败、超时、被取消而停止执行的时间 eg: "2020-08-17T08:14:38.077Z"
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.Id = None
        self.MatchCode = None
        self.MatchResult = None
        self.MatchType = None
        self.Players = None
        self.Status = None
        self.StatusMessage = None
        self.StatusReason = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MatchCode = params.get("MatchCode")
        self.MatchResult = params.get("MatchResult")
        self.MatchType = params.get("MatchType")
        if params.get("Players") is not None:
            self.Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self.Players.append(obj)
        self.Status = params.get("Status")
        self.StatusMessage = params.get("StatusMessage")
        self.StatusReason = params.get("StatusReason")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchRequest(AbstractModel):
    """ModifyMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchName: 匹配名称，[a-zA-Z0-9-\.]* 长度128
        :type MatchName: str
        :param RuleCode: 规则code
        :type RuleCode: str
        :param Timeout: 超时时间，1-600秒
        :type Timeout: int
        :param ServerType: 是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源
        :type ServerType: int
        :param MatchCode: 匹配code
        :type MatchCode: str
        :param MatchDesc: 匹配描述，最长1024
        :type MatchDesc: str
        :param NotifyUrl: 只支持 http 和 https 协议
        :type NotifyUrl: str
        :param ServerRegion: 游戏服务器队列地域
        :type ServerRegion: str
        :param ServerQueue: 游戏服务器队列
        :type ServerQueue: str
        :param CustomPushData: 自定义推送数据
        :type CustomPushData: str
        :param ServerSessionData: 游戏服务器会话数据
        :type ServerSessionData: str
        :param GameProperties: 游戏属性，key-value结构的数组
        :type GameProperties: list of StringKV
        :param LogSwitch: 日志开关，0表示关，1表示开
        :type LogSwitch: int
        :param Tags: 标签，key-value结构的数组
        :type Tags: list of StringKV
        """
        self.MatchName = None
        self.RuleCode = None
        self.Timeout = None
        self.ServerType = None
        self.MatchCode = None
        self.MatchDesc = None
        self.NotifyUrl = None
        self.ServerRegion = None
        self.ServerQueue = None
        self.CustomPushData = None
        self.ServerSessionData = None
        self.GameProperties = None
        self.LogSwitch = None
        self.Tags = None


    def _deserialize(self, params):
        self.MatchName = params.get("MatchName")
        self.RuleCode = params.get("RuleCode")
        self.Timeout = params.get("Timeout")
        self.ServerType = params.get("ServerType")
        self.MatchCode = params.get("MatchCode")
        self.MatchDesc = params.get("MatchDesc")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ServerRegion = params.get("ServerRegion")
        self.ServerQueue = params.get("ServerQueue")
        self.CustomPushData = params.get("CustomPushData")
        self.ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchResponse(AbstractModel):
    """ModifyMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchInfo: 匹配信息
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchInfo") is not None:
            self.MatchInfo = MatchInfo()
            self.MatchInfo._deserialize(params.get("MatchInfo"))
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleCode: 规则code
        :type RuleCode: str
        :param RuleName: 规则名称，只能包含数字、字母、. 和 -
        :type RuleName: str
        :param RuleDesc: 规则描述，最长1024
        :type RuleDesc: str
        :param Tags: 标签，key-value结构的数组，最多关联50组标签
        :type Tags: list of StringKV
        """
        self.RuleCode = None
        self.RuleName = None
        self.RuleDesc = None
        self.Tags = None


    def _deserialize(self, params):
        self.RuleCode = params.get("RuleCode")
        self.RuleName = params.get("RuleName")
        self.RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleInfo: 规则信息
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleInfo") is not None:
            self.RuleInfo = RuleInfo()
            self.RuleInfo._deserialize(params.get("RuleInfo"))
        self.RequestId = params.get("RequestId")


class ModifyTokenRequest(AbstractModel):
    """ModifyToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配Code。
        :type MatchCode: str
        :param CompatibleSpan: 单位秒，取值0-1800。此参数表示当前Token被替换后，GPM将持续推送原Token的时间。在CompatibleSpan时间范围内，用户将在事件消息中收到当前和原始Token。
        :type CompatibleSpan: int
        :param MatchToken: Token，[a-zA-Z0-9-_.], 长度0-64。如果为空，将由GPM随机生成。
        :type MatchToken: str
        """
        self.MatchCode = None
        self.CompatibleSpan = None
        self.MatchToken = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        self.CompatibleSpan = params.get("CompatibleSpan")
        self.MatchToken = params.get("MatchToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenResponse(AbstractModel):
    """ModifyToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchToken: 成功设置的Token。
        :type MatchToken: str
        :param CompatibleSpan: 当前Token被替换后，GPM将持续推送原Token的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CompatibleSpan: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchToken = None
        self.CompatibleSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MatchToken = params.get("MatchToken")
        self.CompatibleSpan = params.get("CompatibleSpan")
        self.RequestId = params.get("RequestId")


class Player(AbstractModel):
    """玩家信息。

    """

    def __init__(self):
        r"""
        :param Id: 玩家 PlayerId 长度 128 [a-zA-Z\d-\._]*
        :type Id: str
        :param Name: 玩家昵称，长度 128
        :type Name: str
        :param MatchAttributes: 玩家匹配属性，最多 10 条
        :type MatchAttributes: list of MatchAttribute
        :param Team: 队伍名，可以传递不同队伍名，长度 128 [a-zA-Z0-9-\.]*
        :type Team: str
        :param CustomPlayerStatus: 自定义玩家状态 透传参数 [0, 99999]
        :type CustomPlayerStatus: int
        :param CustomProfile: 自定义玩家信息 透传参数 长度 1024
        :type CustomProfile: str
        :param RegionLatencies: 各区域延迟，最多 20 条
        :type RegionLatencies: list of RegionLatency
        """
        self.Id = None
        self.Name = None
        self.MatchAttributes = None
        self.Team = None
        self.CustomPlayerStatus = None
        self.CustomProfile = None
        self.RegionLatencies = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("MatchAttributes") is not None:
            self.MatchAttributes = []
            for item in params.get("MatchAttributes"):
                obj = MatchAttribute()
                obj._deserialize(item)
                self.MatchAttributes.append(obj)
        self.Team = params.get("Team")
        self.CustomPlayerStatus = params.get("CustomPlayerStatus")
        self.CustomProfile = params.get("CustomProfile")
        if params.get("RegionLatencies") is not None:
            self.RegionLatencies = []
            for item in params.get("RegionLatencies"):
                obj = RegionLatency()
                obj._deserialize(item)
                self.RegionLatencies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionLatency(AbstractModel):
    """玩家到各区域的延迟

    """

    def __init__(self):
        r"""
        :param Region: 地域
ap-beijing          华北地区(北京)
ap-chengdu          西南地区(成都)
ap-guangzhou          华南地区(广州)
ap-hongkong          港澳台地区(中国香港)
ap-seoul          亚太地区(首尔)
ap-shanghai          华东地区(上海)
ap-singapore          东南亚地区(新加坡)
eu-frankfurt          欧洲地区(法兰克福)
na-siliconvalley          美国西部(硅谷)
na-toronto          北美地区(多伦多)
ap-mumbai          亚太地区(孟买)
na-ashburn          美国东部(弗吉尼亚)
ap-bangkok          亚太地区(曼谷)
eu-moscow          欧洲地区(莫斯科)
ap-tokyo          亚太地区(东京)
        :type Region: str
        :param Latency: 毫秒延迟 0～999999
        :type Latency: int
        """
        self.Region = None
        self.Latency = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Latency = params.get("Latency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportOverviewData(AbstractModel):
    """匹配概况

    """

    def __init__(self):
        r"""
        :param TotalTimes: 总次数
        :type TotalTimes: str
        :param SuccessPercent: 成功率
        :type SuccessPercent: float
        :param TimeoutPercent: 超时率
        :type TimeoutPercent: float
        :param FailPercent: 失败率
        :type FailPercent: float
        :param AverageSec: 平均匹配时间
        :type AverageSec: float
        """
        self.TotalTimes = None
        self.SuccessPercent = None
        self.TimeoutPercent = None
        self.FailPercent = None
        self.AverageSec = None


    def _deserialize(self, params):
        self.TotalTimes = params.get("TotalTimes")
        self.SuccessPercent = params.get("SuccessPercent")
        self.TimeoutPercent = params.get("TimeoutPercent")
        self.FailPercent = params.get("FailPercent")
        self.AverageSec = params.get("AverageSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTrendData(AbstractModel):
    """统计数据之趋势数据

    """

    def __init__(self):
        r"""
        :param TotalList: 总次数
        :type TotalList: list of str
        :param CancelList: 被取消次数
        :type CancelList: list of str
        :param SuccessList: 成功次数
        :type SuccessList: list of str
        :param FailList: 失败次数
        :type FailList: list of str
        :param TimeoutList: 超时次数
        :type TimeoutList: list of str
        :param TimeList: 时间数组，单位：秒
        :type TimeList: list of str
        """
        self.TotalList = None
        self.CancelList = None
        self.SuccessList = None
        self.FailList = None
        self.TimeoutList = None
        self.TimeList = None


    def _deserialize(self, params):
        self.TotalList = params.get("TotalList")
        self.CancelList = params.get("CancelList")
        self.SuccessList = params.get("SuccessList")
        self.FailList = params.get("FailList")
        self.TimeoutList = params.get("TimeoutList")
        self.TimeList = params.get("TimeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleBriefInfo(AbstractModel):
    """规则简单信息

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称 [a-zA-Z\d-\.]*
        :type RuleName: str
        :param MatchCodeList: 关联匹配
        :type MatchCodeList: list of StringKV
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param RuleCode: 规则code
        :type RuleCode: str
        """
        self.RuleName = None
        self.MatchCodeList = None
        self.CreateTime = None
        self.RuleCode = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("MatchCodeList") is not None:
            self.MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self.MatchCodeList.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称 [a-zA-Z0-9-\.]*
        :type RuleName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param RuleDesc: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDesc: str
        :param RuleScript: 规则脚本
        :type RuleScript: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of StringKV
        :param MatchCodeList: 关联匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchCodeList: list of StringKV
        :param RuleCode: 规则code
        :type RuleCode: str
        :param Region: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param CreateUin: 用户OwnerUin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        """
        self.RuleName = None
        self.CreateTime = None
        self.RuleDesc = None
        self.RuleScript = None
        self.Tags = None
        self.MatchCodeList = None
        self.RuleCode = None
        self.Region = None
        self.AppId = None
        self.Uin = None
        self.CreateUin = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.CreateTime = params.get("CreateTime")
        self.RuleDesc = params.get("RuleDesc")
        self.RuleScript = params.get("RuleScript")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("MatchCodeList") is not None:
            self.MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self.MatchCodeList.append(obj)
        self.RuleCode = params.get("RuleCode")
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.CreateUin = params.get("CreateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillRequest(AbstractModel):
    """StartMatchingBackfill请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配code
        :type MatchCode: str
        :param Players: 玩家信息
        :type Players: list of Player
        :param GameServerSessionId: 游戏服务器回话 ID [1-256] 个ASCII 字符
        :type GameServerSessionId: str
        :param MatchTicketId: 匹配票据 Id 默认 "" 为空则由 GPM 自动生成 长度 [1, 128]
        :type MatchTicketId: str
        """
        self.MatchCode = None
        self.Players = None
        self.GameServerSessionId = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self.Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self.Players.append(obj)
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillResponse(AbstractModel):
    """StartMatchingBackfill返回参数结构体

    """

    def __init__(self):
        r"""
        :param MatchTicket: 匹配票据
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchTicket: :class:`tencentcloud.gpm.v20200820.models.MatchTicket`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MatchTicket = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MatchTicket") is not None:
            self.MatchTicket = MatchTicket()
            self.MatchTicket._deserialize(params.get("MatchTicket"))
        self.RequestId = params.get("RequestId")


class StartMatchingRequest(AbstractModel):
    """StartMatching请求参数结构体

    """

    def __init__(self):
        r"""
        :param MatchCode: 匹配 Code。
        :type MatchCode: str
        :param Players: 玩家信息 最多 200 条。
        :type Players: list of Player
        :param MatchTicketId: 匹配票据 ID 默认空字符串，为空则由 GPM 自动生成 长度 128，只能包含数字、字母、. 和 -
        :type MatchTicketId: str
        """
        self.MatchCode = None
        self.Players = None
        self.MatchTicketId = None


    def _deserialize(self, params):
        self.MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self.Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self.Players.append(obj)
        self.MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingResponse(AbstractModel):
    """StartMatching返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
        :type ErrCode: int
        :param MatchTicketId: 匹配票据 ID长度 128。
        :type MatchTicketId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.MatchTicketId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.MatchTicketId = params.get("MatchTicketId")
        self.RequestId = params.get("RequestId")


class StringKV(AbstractModel):
    """string keyValue解构

    """

    def __init__(self):
        r"""
        :param Key: 键
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
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
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
        