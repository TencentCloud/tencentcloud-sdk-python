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
        """
        :param Key: 属性字典 key [a-zA-Z0-9-\.]*\n        :type Key: str\n        :param Value: 属性字典 value\n        :type Value: int\n        """
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
        """
        :param MatchCode: 匹配 Code\n        :type MatchCode: str\n        :param MatchTicketId: 要取消的匹配匹配票据 ID\n        :type MatchTicketId: str\n        """
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
        """
        :param ErrCode: 错误码\n        :type ErrCode: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ErrCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.RequestId = params.get("RequestId")


class CreateMatchRequest(AbstractModel):
    """CreateMatch请求参数结构体

    """

    def __init__(self):
        """
        :param MatchName: 匹配名称，[a-zA-Z0-9-\.]* 长度128\n        :type MatchName: str\n        :param RuleCode: 规则code\n        :type RuleCode: str\n        :param Timeout: 超时时间，1-600秒\n        :type Timeout: int\n        :param ServerType: 是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源\n        :type ServerType: int\n        :param MatchDesc: 匹配描述，最长1024\n        :type MatchDesc: str\n        :param NotifyUrl: 只支持https 和 http 协议\n        :type NotifyUrl: str\n        :param ServerRegion: 游戏服务器队列地域\n        :type ServerRegion: str\n        :param ServerQueue: 游戏服务器队列\n        :type ServerQueue: str\n        :param CustomPushData: 自定义推送数据\n        :type CustomPushData: str\n        :param ServerSessionData: 游戏服务器会话数据\n        :type ServerSessionData: str\n        :param GameProperties: 游戏属性，key-value结构的数组\n        :type GameProperties: list of StringKV\n        :param LogSwitch: 日志开关，0表示关，1表示开\n        :type LogSwitch: int\n        :param Tags: 标签，key-value结构的数组\n        :type Tags: list of StringKV\n        """
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
        """
        :param MatchInfo: 匹配信息\n        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RuleName: 规则名称，[a-zA-Z0-9-\.]* 长度128\n        :type RuleName: str\n        :param RuleScript: 规则脚本，长度65535\n        :type RuleScript: str\n        :param RuleDesc: 规则描述，最长1024\n        :type RuleDesc: str\n        :param Tags: 标签，key-value结构的数组，最多关联50组标签\n        :type Tags: list of StringKV\n        """
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
        """
        :param RuleInfo: 规则信息\n        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MatchCode: 匹配code\n        :type MatchCode: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleCode: 规则code\n        :type RuleCode: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    """DescribeData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间，单位：秒\n        :type StartTime: int\n        :param EndTime: 截止时间，单位：秒\n        :type EndTime: int\n        :param TimeType: 时间粒度，1表示1天；2表示1小时；3表示1分钟；4表示10分钟；5表示30分钟\n        :type TimeType: int\n        :param MatchCode: 匹配code\n        :type MatchCode: str\n        """
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
        """
        :param OverviewData: 匹配概况
注意：此字段可能返回 null，表示取不到有效值。\n        :type OverviewData: :class:`tencentcloud.gpm.v20200820.models.ReportOverviewData`\n        :param TrendData: 匹配请求次数趋势数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type TrendData: :class:`tencentcloud.gpm.v20200820.models.ReportTrendData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Offset: 偏移量，页码\n        :type Offset: int\n        :param Limit: 每页数量\n        :type Limit: int\n        :param MatchCode: 搜索的字符串\n        :type MatchCode: str\n        """
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
        """
        :param MatchCodes: 匹配Code
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchCodes: list of MatchCodeAttr\n        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MatchCode: 匹配code\n        :type MatchCode: str\n        """
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
        """
        :param MatchInfo: 匹配信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param PageNumber: 当前页号，不传则获取所有有权限的资源。\n        :type PageNumber: int\n        :param PageSize: 单页大小，不传则获取所有有权限的资源。\n        :type PageSize: int\n        :param SearchType: 查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。\n        :type SearchType: str\n        :param Keyword: 查询关键词，针对SearchType进行具体过滤的内容。\n        :type Keyword: str\n        :param Tags: 标签列表，用于过滤。\n        :type Tags: list of Tag\n        """
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
        """
        :param MatchInfoList: 匹配信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchInfoList: list of MatchInfo\n        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param PageNumber: 当前页号，不填默认返回第一页\n        :type PageNumber: int\n        :param PageSize: 单页大小，不填默认取 30，最大值不能超过 30\n        :type PageSize: int\n        :param SearchType: 查询类型（可选）：matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value\n        :type SearchType: str\n        :param Keyword: 查询关键词（可选）\n        :type Keyword: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MatchTicketIds: 匹配票据 ID列表, 列表长度 12。\n        :type MatchTicketIds: list of MTicket\n        """
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
        """
        :param MatchTickets: 匹配票据列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchTickets: list of MatchTicket\n        :param ErrCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrCode: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RuleCode: 规则code\n        :type RuleCode: str\n        """
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
        """
        :param RuleInfo: 规则信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param PageNumber: 当前页号，不传则返回第一页\n        :type PageNumber: int\n        :param PageSize: 单页大小，最大 30，不填默认30\n        :type PageSize: int\n        :param SearchType: 查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。\n        :type SearchType: str\n        :param Keyword: 查询关键词，针对SearchType进行具体过滤的内容。\n        :type Keyword: str\n        :param Tags: 标签列表，用于过滤。\n        :type Tags: list of Tag\n        """
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
        """
        :param RuleInfoList: 规则信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleInfoList: list of RuleBriefInfo\n        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param PageNumber: 当前页号\n        :type PageNumber: int\n        :param PageSize: 单页大小\n        :type PageSize: int\n        :param SearchType: 查询类型（可选）matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value\n        :type SearchType: str\n        :param Keyword: 查询关键词（可选）\n        :type Keyword: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MatchCode: 匹配code\n        :type MatchCode: str\n        """
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
        """
        :param MatchToken: 当前的MatchCode对应的Token。如果当前MatchCode没有Token，该参数可能取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchToken: str\n        :param CompatibleSpan: 当Token被替换后，GPM将兼容推送原始Token的时间（秒）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CompatibleSpan: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MatchCode: 匹配Code\n        :type MatchCode: str\n        :param MatchTicketId: 匹配票据 ID\n        :type MatchTicketId: str\n        """
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
        """
        :param Name: 属性名 长度 128 [a-zA-Z0-9-\.]*\n        :type Name: str\n        :param Type: 属性类型: 0 数值; 1 string; 默认 0\n        :type Type: int\n        :param NumberValue: 数字属性值 默认 0.0\n        :type NumberValue: float\n        :param StringValue: 字符串属性值 长度 128 默认 ""\n        :type StringValue: str\n        :param ListValue: list 属性值\n        :type ListValue: list of str\n        :param MapValue: 字典属性值\n        :type MapValue: list of AttributeMap\n        """
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
        """
        :param MatchCode: 匹配code
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchCode: str\n        """
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
        """
        :param MatchCode: 匹配code\n        :type MatchCode: str\n        :param MatchName: 匹配名称\n        :type MatchName: str\n        :param MatchDesc: 匹配描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchDesc: str\n        :param RuleCode: 规则code\n        :type RuleCode: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param Timeout: 超时时间\n        :type Timeout: int\n        :param NotifyUrl: 接收通知地址\n        :type NotifyUrl: str\n        :param ServerType: 是否为匹配结果请求服务器资源，0否，1请求GSE资源\n        :type ServerType: int\n        :param ServerRegion: 服务器队列所在地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerRegion: str\n        :param ServerQueue: 服务器队列
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerQueue: str\n        :param CustomPushData: 自定义推送数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomPushData: str\n        :param ServerSessionData: 游戏服务器会话数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerSessionData: str\n        :param GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type GameProperties: list of StringKV\n        :param LogSwitch: 日志开关，0表示关，1表示开\n        :type LogSwitch: int\n        :param LogsetId: 日志集id
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogsetId: str\n        :param LogsetName: 日志集名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogsetName: str\n        :param LogTopicId: 日志主题id
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogTopicId: str\n        :param LogTopicName: 日志主题名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogTopicName: str\n        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of StringKV\n        :param Region: 地区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: str\n        :param Uin: 用户主账号Uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uin: str\n        :param CreateUin: 用户创建账号Uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUin: str\n        :param RuleName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleName: str\n        :param LogStatus: 日志状态，0表示正常，1表示日志集不存在，2表示日志主题不存在，3表示日志集和日志主题都不存在。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogStatus: int\n        """
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
        """
        :param Id: 匹配票据 ID长度 128 [a-zA-Z0-9-\.]*\n        :type Id: str\n        :param MatchCode: 匹配 Code\n        :type MatchCode: str\n        :param MatchResult: 根据 MatchType 取不同的结构序列化结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchResult: str\n        :param MatchType: 表示不同的匹配类型,NORMAL | GSE
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchType: str\n        :param Players: 玩家信息列表\n        :type Players: list of Player\n        :param Status: 匹配状态: SEARCHING 匹配中; PLACING 匹配放置中; COMPLETED 匹配完成; CANCELLED 匹配取消; TIMEDOUT 匹配超时; FAILED 匹配失败\n        :type Status: str\n        :param StatusMessage: 匹配状态信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusMessage: str\n        :param StatusReason: 匹配状态原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusReason: str\n        :param StartTime: 收到发起匹配请求的时间 eg: "2020-08-17T08:14:38.077Z"\n        :type StartTime: str\n        :param EndTime: 匹配请求因完成、失败、超时、被取消而停止执行的时间 eg: "2020-08-17T08:14:38.077Z"
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        """
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
        """
        :param MatchName: 匹配名称，[a-zA-Z0-9-\.]* 长度128\n        :type MatchName: str\n        :param RuleCode: 规则code\n        :type RuleCode: str\n        :param Timeout: 超时时间，1-600秒\n        :type Timeout: int\n        :param ServerType: 是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源\n        :type ServerType: int\n        :param MatchCode: 匹配code\n        :type MatchCode: str\n        :param MatchDesc: 匹配描述，最长1024\n        :type MatchDesc: str\n        :param NotifyUrl: 只支持 http 和 https 协议\n        :type NotifyUrl: str\n        :param ServerRegion: 游戏服务器队列地域\n        :type ServerRegion: str\n        :param ServerQueue: 游戏服务器队列\n        :type ServerQueue: str\n        :param CustomPushData: 自定义推送数据\n        :type CustomPushData: str\n        :param ServerSessionData: 游戏服务器会话数据\n        :type ServerSessionData: str\n        :param GameProperties: 游戏属性，key-value结构的数组\n        :type GameProperties: list of StringKV\n        :param LogSwitch: 日志开关，0表示关，1表示开\n        :type LogSwitch: int\n        :param Tags: 标签，key-value结构的数组\n        :type Tags: list of StringKV\n        """
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
        """
        :param MatchInfo: 匹配信息\n        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param RuleCode: 规则code\n        :type RuleCode: str\n        :param RuleName: 规则名称，只能包含数字、字母、. 和 -\n        :type RuleName: str\n        :param RuleDesc: 规则描述，最长1024\n        :type RuleDesc: str\n        :param Tags: 标签，key-value结构的数组，最多关联50组标签\n        :type Tags: list of StringKV\n        """
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
        """
        :param RuleInfo: 规则信息\n        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MatchCode: 匹配Code。\n        :type MatchCode: str\n        :param CompatibleSpan: 单位秒，取值0-1800。此参数表示当前Token被替换后，GPM将持续推送原Token的时间。在CompatibleSpan时间范围内，用户将在事件消息中收到当前和原始Token。\n        :type CompatibleSpan: int\n        :param MatchToken: Token，[a-zA-Z0-9-_.], 长度0-64。如果为空，将由GPM随机生成。\n        :type MatchToken: str\n        """
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
        """
        :param MatchToken: 成功设置的Token。\n        :type MatchToken: str\n        :param CompatibleSpan: 当前Token被替换后，GPM将持续推送原Token的时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CompatibleSpan: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Id: 玩家 PlayerId 长度 128 [a-zA-Z\d-\._]*\n        :type Id: str\n        :param Name: 玩家昵称，长度 128\n        :type Name: str\n        :param MatchAttributes: 玩家匹配属性，最多 10 条\n        :type MatchAttributes: list of MatchAttribute\n        :param Team: 队伍名，可以传递不同队伍名，长度 128 [a-zA-Z0-9-\.]*\n        :type Team: str\n        :param CustomPlayerStatus: 自定义玩家状态 透传参数 [0, 99999]\n        :type CustomPlayerStatus: int\n        :param CustomProfile: 自定义玩家信息 透传参数 长度 1024\n        :type CustomProfile: str\n        :param RegionLatencies: 各区域延迟，最多 20 条\n        :type RegionLatencies: list of RegionLatency\n        """
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
        """
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
ap-tokyo          亚太地区(东京)\n        :type Region: str\n        :param Latency: 毫秒延迟 0～999999\n        :type Latency: int\n        """
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
        """
        :param TotalTimes: 总次数\n        :type TotalTimes: str\n        :param SuccessPercent: 成功率\n        :type SuccessPercent: float\n        :param TimeoutPercent: 超时率\n        :type TimeoutPercent: float\n        :param FailPercent: 失败率\n        :type FailPercent: float\n        :param AverageSec: 平均匹配时间\n        :type AverageSec: float\n        """
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
        """
        :param TotalList: 总次数\n        :type TotalList: list of str\n        :param CancelList: 被取消次数\n        :type CancelList: list of str\n        :param SuccessList: 成功次数\n        :type SuccessList: list of str\n        :param FailList: 失败次数\n        :type FailList: list of str\n        :param TimeoutList: 超时次数\n        :type TimeoutList: list of str\n        :param TimeList: 时间数组，单位：秒\n        :type TimeList: list of str\n        """
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
        """
        :param RuleName: 规则名称 [a-zA-Z\d-\.]*\n        :type RuleName: str\n        :param MatchCodeList: 关联匹配\n        :type MatchCodeList: list of StringKV\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param RuleCode: 规则code\n        :type RuleCode: str\n        """
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
        """
        :param RuleName: 规则名称 [a-zA-Z0-9-\.]*\n        :type RuleName: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param RuleDesc: 规则描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleDesc: str\n        :param RuleScript: 规则脚本\n        :type RuleScript: str\n        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of StringKV\n        :param MatchCodeList: 关联匹配
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchCodeList: list of StringKV\n        :param RuleCode: 规则code\n        :type RuleCode: str\n        :param Region: 地区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: str\n        :param Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uin: str\n        :param CreateUin: 用户OwnerUin
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUin: str\n        """
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
        """
        :param MatchCode: 匹配code\n        :type MatchCode: str\n        :param Players: 玩家信息\n        :type Players: list of Player\n        :param GameServerSessionId: 游戏服务器回话 ID [1-256] 个ASCII 字符\n        :type GameServerSessionId: str\n        :param MatchTicketId: 匹配票据 Id 默认 "" 为空则由 GPM 自动生成 长度 [1, 128]\n        :type MatchTicketId: str\n        """
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
        """
        :param MatchTicket: 匹配票据
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchTicket: :class:`tencentcloud.gpm.v20200820.models.MatchTicket`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param MatchCode: 匹配 Code。\n        :type MatchCode: str\n        :param Players: 玩家信息 最多 200 条。\n        :type Players: list of Player\n        :param MatchTicketId: 匹配票据 ID 默认空字符串，为空则由 GPM 自动生成 长度 128，只能包含数字、字母、. 和 -\n        :type MatchTicketId: str\n        """
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
        """
        :param ErrCode: 错误码。\n        :type ErrCode: int\n        :param MatchTicketId: 匹配票据 ID长度 128。\n        :type MatchTicketId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Key: 键\n        :type Key: str\n        :param Value: 值\n        :type Value: str\n        """
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
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
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
        