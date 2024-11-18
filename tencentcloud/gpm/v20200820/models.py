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
        :param _Key: 属性字典 key [a-zA-Z0-9-\.]*
        :type Key: str
        :param _Value: 属性字典 value
        :type Value: int
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """属性字典 key [a-zA-Z0-9-\.]*
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """属性字典 value
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelMatchingRequest(AbstractModel):
    """CancelMatching请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配 Code
        :type MatchCode: str
        :param _MatchTicketId: 要取消的匹配匹配票据 ID
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        """匹配 Code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchTicketId(self):
        """要取消的匹配匹配票据 ID
        :rtype: str
        """
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelMatchingResponse(AbstractModel):
    """CancelMatching返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrCode: 错误码
        :type ErrCode: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrCode = None
        self._RequestId = None

    @property
    def ErrCode(self):
        """错误码
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

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
        self._ErrCode = params.get("ErrCode")
        self._RequestId = params.get("RequestId")


class CreateMatchRequest(AbstractModel):
    """CreateMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchName: 匹配名称，[a-zA-Z0-9-\.]* 长度128
        :type MatchName: str
        :param _RuleCode: 规则code
        :type RuleCode: str
        :param _Timeout: 超时时间，1-600秒
        :type Timeout: int
        :param _ServerType: 是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源
        :type ServerType: int
        :param _MatchDesc: 匹配描述，最长1024
        :type MatchDesc: str
        :param _NotifyUrl: 只支持https 和 http 协议
        :type NotifyUrl: str
        :param _ServerRegion: 游戏服务器队列地域
        :type ServerRegion: str
        :param _ServerQueue: 游戏服务器队列
        :type ServerQueue: str
        :param _CustomPushData: 自定义推送数据
        :type CustomPushData: str
        :param _ServerSessionData: 游戏服务器会话数据
        :type ServerSessionData: str
        :param _GameProperties: 游戏属性，key-value结构的数组
        :type GameProperties: list of StringKV
        :param _LogSwitch: 日志开关，0表示关，1表示开
        :type LogSwitch: int
        :param _Tags: 标签，key-value结构的数组
        :type Tags: list of StringKV
        """
        self._MatchName = None
        self._RuleCode = None
        self._Timeout = None
        self._ServerType = None
        self._MatchDesc = None
        self._NotifyUrl = None
        self._ServerRegion = None
        self._ServerQueue = None
        self._CustomPushData = None
        self._ServerSessionData = None
        self._GameProperties = None
        self._LogSwitch = None
        self._Tags = None

    @property
    def MatchName(self):
        """匹配名称，[a-zA-Z0-9-\.]* 长度128
        :rtype: str
        """
        return self._MatchName

    @MatchName.setter
    def MatchName(self, MatchName):
        self._MatchName = MatchName

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def Timeout(self):
        """超时时间，1-600秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ServerType(self):
        """是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源
        :rtype: int
        """
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def MatchDesc(self):
        """匹配描述，最长1024
        :rtype: str
        """
        return self._MatchDesc

    @MatchDesc.setter
    def MatchDesc(self, MatchDesc):
        self._MatchDesc = MatchDesc

    @property
    def NotifyUrl(self):
        """只支持https 和 http 协议
        :rtype: str
        """
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def ServerRegion(self):
        """游戏服务器队列地域
        :rtype: str
        """
        return self._ServerRegion

    @ServerRegion.setter
    def ServerRegion(self, ServerRegion):
        self._ServerRegion = ServerRegion

    @property
    def ServerQueue(self):
        """游戏服务器队列
        :rtype: str
        """
        return self._ServerQueue

    @ServerQueue.setter
    def ServerQueue(self, ServerQueue):
        self._ServerQueue = ServerQueue

    @property
    def CustomPushData(self):
        """自定义推送数据
        :rtype: str
        """
        return self._CustomPushData

    @CustomPushData.setter
    def CustomPushData(self, CustomPushData):
        self._CustomPushData = CustomPushData

    @property
    def ServerSessionData(self):
        """游戏服务器会话数据
        :rtype: str
        """
        return self._ServerSessionData

    @ServerSessionData.setter
    def ServerSessionData(self, ServerSessionData):
        self._ServerSessionData = ServerSessionData

    @property
    def GameProperties(self):
        """游戏属性，key-value结构的数组
        :rtype: list of StringKV
        """
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def LogSwitch(self):
        """日志开关，0表示关，1表示开
        :rtype: int
        """
        return self._LogSwitch

    @LogSwitch.setter
    def LogSwitch(self, LogSwitch):
        self._LogSwitch = LogSwitch

    @property
    def Tags(self):
        """标签，key-value结构的数组
        :rtype: list of StringKV
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MatchName = params.get("MatchName")
        self._RuleCode = params.get("RuleCode")
        self._Timeout = params.get("Timeout")
        self._ServerType = params.get("ServerType")
        self._MatchDesc = params.get("MatchDesc")
        self._NotifyUrl = params.get("NotifyUrl")
        self._ServerRegion = params.get("ServerRegion")
        self._ServerQueue = params.get("ServerQueue")
        self._CustomPushData = params.get("CustomPushData")
        self._ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMatchResponse(AbstractModel):
    """CreateMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchInfo: 匹配信息
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchInfo = None
        self._RequestId = None

    @property
    def MatchInfo(self):
        """匹配信息
        :rtype: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        """
        return self._MatchInfo

    @MatchInfo.setter
    def MatchInfo(self, MatchInfo):
        self._MatchInfo = MatchInfo

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
        if params.get("MatchInfo") is not None:
            self._MatchInfo = MatchInfo()
            self._MatchInfo._deserialize(params.get("MatchInfo"))
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称，[a-zA-Z0-9-\.]* 长度128
        :type RuleName: str
        :param _RuleScript: 规则脚本，长度65535
        :type RuleScript: str
        :param _RuleDesc: 规则描述，最长1024
        :type RuleDesc: str
        :param _Tags: 标签，key-value结构的数组，最多关联50组标签
        :type Tags: list of StringKV
        """
        self._RuleName = None
        self._RuleScript = None
        self._RuleDesc = None
        self._Tags = None

    @property
    def RuleName(self):
        """规则名称，[a-zA-Z0-9-\.]* 长度128
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleScript(self):
        """规则脚本，长度65535
        :rtype: str
        """
        return self._RuleScript

    @RuleScript.setter
    def RuleScript(self, RuleScript):
        self._RuleScript = RuleScript

    @property
    def RuleDesc(self):
        """规则描述，最长1024
        :rtype: str
        """
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def Tags(self):
        """标签，key-value结构的数组，最多关联50组标签
        :rtype: list of StringKV
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._RuleScript = params.get("RuleScript")
        self._RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleInfo: 规则信息
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleInfo = None
        self._RequestId = None

    @property
    def RuleInfo(self):
        """规则信息
        :rtype: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        """
        return self._RuleInfo

    @RuleInfo.setter
    def RuleInfo(self, RuleInfo):
        self._RuleInfo = RuleInfo

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
        if params.get("RuleInfo") is not None:
            self._RuleInfo = RuleInfo()
            self._RuleInfo._deserialize(params.get("RuleInfo"))
        self._RequestId = params.get("RequestId")


class DeleteMatchRequest(AbstractModel):
    """DeleteMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配code
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        """匹配code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMatchResponse(AbstractModel):
    """DeleteMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleCode: 规则code
        :type RuleCode: str
        """
        self._RuleCode = None

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode


    def _deserialize(self, params):
        self._RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    """DescribeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param _EndTime: 截止时间，单位：秒
        :type EndTime: int
        :param _TimeType: 时间粒度，1表示1天；2表示1小时；3表示1分钟；4表示10分钟；5表示30分钟
        :type TimeType: int
        :param _MatchCode: 匹配code
        :type MatchCode: str
        """
        self._StartTime = None
        self._EndTime = None
        self._TimeType = None
        self._MatchCode = None

    @property
    def StartTime(self):
        """起始时间，单位：秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """截止时间，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TimeType(self):
        """时间粒度，1表示1天；2表示1小时；3表示1分钟；4表示10分钟；5表示30分钟
        :rtype: int
        """
        return self._TimeType

    @TimeType.setter
    def TimeType(self, TimeType):
        self._TimeType = TimeType

    @property
    def MatchCode(self):
        """匹配code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TimeType = params.get("TimeType")
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OverviewData: 匹配概况
注意：此字段可能返回 null，表示取不到有效值。
        :type OverviewData: :class:`tencentcloud.gpm.v20200820.models.ReportOverviewData`
        :param _TrendData: 匹配请求次数趋势数据
注意：此字段可能返回 null，表示取不到有效值。
        :type TrendData: :class:`tencentcloud.gpm.v20200820.models.ReportTrendData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OverviewData = None
        self._TrendData = None
        self._RequestId = None

    @property
    def OverviewData(self):
        """匹配概况
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ReportOverviewData`
        """
        return self._OverviewData

    @OverviewData.setter
    def OverviewData(self, OverviewData):
        self._OverviewData = OverviewData

    @property
    def TrendData(self):
        """匹配请求次数趋势数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ReportTrendData`
        """
        return self._TrendData

    @TrendData.setter
    def TrendData(self, TrendData):
        self._TrendData = TrendData

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
        if params.get("OverviewData") is not None:
            self._OverviewData = ReportOverviewData()
            self._OverviewData._deserialize(params.get("OverviewData"))
        if params.get("TrendData") is not None:
            self._TrendData = ReportTrendData()
            self._TrendData._deserialize(params.get("TrendData"))
        self._RequestId = params.get("RequestId")


class DescribeMatchCodesRequest(AbstractModel):
    """DescribeMatchCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，页码
        :type Offset: int
        :param _Limit: 每页数量
        :type Limit: int
        :param _MatchCode: 搜索的字符串
        :type MatchCode: str
        """
        self._Offset = None
        self._Limit = None
        self._MatchCode = None

    @property
    def Offset(self):
        """偏移量，页码
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MatchCode(self):
        """搜索的字符串
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchCodesResponse(AbstractModel):
    """DescribeMatchCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCodes: 匹配Code
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchCodes: list of MatchCodeAttr
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchCodes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MatchCodes(self):
        """匹配Code
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MatchCodeAttr
        """
        return self._MatchCodes

    @MatchCodes.setter
    def MatchCodes(self, MatchCodes):
        self._MatchCodes = MatchCodes

    @property
    def TotalCount(self):
        """总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("MatchCodes") is not None:
            self._MatchCodes = []
            for item in params.get("MatchCodes"):
                obj = MatchCodeAttr()
                obj._deserialize(item)
                self._MatchCodes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMatchRequest(AbstractModel):
    """DescribeMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配code
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        """匹配code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchResponse(AbstractModel):
    """DescribeMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchInfo: 匹配信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchInfo = None
        self._RequestId = None

    @property
    def MatchInfo(self):
        """匹配信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        """
        return self._MatchInfo

    @MatchInfo.setter
    def MatchInfo(self, MatchInfo):
        self._MatchInfo = MatchInfo

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
        if params.get("MatchInfo") is not None:
            self._MatchInfo = MatchInfo()
            self._MatchInfo._deserialize(params.get("MatchInfo"))
        self._RequestId = params.get("RequestId")


class DescribeMatchesRequest(AbstractModel):
    """DescribeMatches请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 当前页号，不传则获取所有有权限的资源。
        :type PageNumber: int
        :param _PageSize: 单页大小，不传则获取所有有权限的资源。
        :type PageSize: int
        :param _SearchType: 查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。
        :type SearchType: str
        :param _Keyword: 查询关键词，针对SearchType进行具体过滤的内容。
        :type Keyword: str
        :param _Tags: 标签列表，用于过滤。
        :type Tags: list of Tag
        """
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._Tags = None

    @property
    def PageNumber(self):
        """当前页号，不传则获取所有有权限的资源。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """单页大小，不传则获取所有有权限的资源。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        """查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。
        :rtype: str
        """
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        """查询关键词，针对SearchType进行具体过滤的内容。
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Tags(self):
        """标签列表，用于过滤。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchesResponse(AbstractModel):
    """DescribeMatches返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchInfoList: 匹配信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchInfoList: list of MatchInfo
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _PageNumber: 当前页号，不填默认返回第一页
        :type PageNumber: int
        :param _PageSize: 单页大小，不填默认取 30，最大值不能超过 30
        :type PageSize: int
        :param _SearchType: 查询类型（可选）：matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value
        :type SearchType: str
        :param _Keyword: 查询关键词（可选）
        :type Keyword: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchInfoList = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._RequestId = None

    @property
    def MatchInfoList(self):
        """匹配信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MatchInfo
        """
        return self._MatchInfoList

    @MatchInfoList.setter
    def MatchInfoList(self, MatchInfoList):
        self._MatchInfoList = MatchInfoList

    @property
    def TotalCount(self):
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        """当前页号，不填默认返回第一页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """单页大小，不填默认取 30，最大值不能超过 30
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        """查询类型（可选）：matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value
        :rtype: str
        """
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        """查询关键词（可选）
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

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
        if params.get("MatchInfoList") is not None:
            self._MatchInfoList = []
            for item in params.get("MatchInfoList"):
                obj = MatchInfo()
                obj._deserialize(item)
                self._MatchInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        self._RequestId = params.get("RequestId")


class DescribeMatchingProgressRequest(AbstractModel):
    """DescribeMatchingProgress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchTicketIds: 匹配票据 ID列表, 列表长度 12。
        :type MatchTicketIds: list of MTicket
        """
        self._MatchTicketIds = None

    @property
    def MatchTicketIds(self):
        """匹配票据 ID列表, 列表长度 12。
        :rtype: list of MTicket
        """
        return self._MatchTicketIds

    @MatchTicketIds.setter
    def MatchTicketIds(self, MatchTicketIds):
        self._MatchTicketIds = MatchTicketIds


    def _deserialize(self, params):
        if params.get("MatchTicketIds") is not None:
            self._MatchTicketIds = []
            for item in params.get("MatchTicketIds"):
                obj = MTicket()
                obj._deserialize(item)
                self._MatchTicketIds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMatchingProgressResponse(AbstractModel):
    """DescribeMatchingProgress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchTickets: 匹配票据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchTickets: list of MatchTicket
        :param _ErrCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchTickets = None
        self._ErrCode = None
        self._RequestId = None

    @property
    def MatchTickets(self):
        """匹配票据列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MatchTicket
        """
        return self._MatchTickets

    @MatchTickets.setter
    def MatchTickets(self, MatchTickets):
        self._MatchTickets = MatchTickets

    @property
    def ErrCode(self):
        """错误码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

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
        if params.get("MatchTickets") is not None:
            self._MatchTickets = []
            for item in params.get("MatchTickets"):
                obj = MatchTicket()
                obj._deserialize(item)
                self._MatchTickets.append(obj)
        self._ErrCode = params.get("ErrCode")
        self._RequestId = params.get("RequestId")


class DescribeRuleRequest(AbstractModel):
    """DescribeRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleCode: 规则code
        :type RuleCode: str
        """
        self._RuleCode = None

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode


    def _deserialize(self, params):
        self._RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleResponse(AbstractModel):
    """DescribeRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleInfo: 规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleInfo = None
        self._RequestId = None

    @property
    def RuleInfo(self):
        """规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        """
        return self._RuleInfo

    @RuleInfo.setter
    def RuleInfo(self, RuleInfo):
        self._RuleInfo = RuleInfo

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
        if params.get("RuleInfo") is not None:
            self._RuleInfo = RuleInfo()
            self._RuleInfo._deserialize(params.get("RuleInfo"))
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 当前页号，不传则返回第一页
        :type PageNumber: int
        :param _PageSize: 单页大小，最大 30，不填默认30
        :type PageSize: int
        :param _SearchType: 查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。
        :type SearchType: str
        :param _Keyword: 查询关键词，针对SearchType进行具体过滤的内容。
        :type Keyword: str
        :param _Tags: 标签列表，用于过滤。
        :type Tags: list of Tag
        """
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._Tags = None

    @property
    def PageNumber(self):
        """当前页号，不传则返回第一页
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """单页大小，最大 30，不填默认30
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        """查询类型（可选）：match表示通过matchCode或者matchName来搜索，rule表示通过ruleCode或者ruleName来搜索，其余类型不做过滤处理。
        :rtype: str
        """
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        """查询关键词，针对SearchType进行具体过滤的内容。
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Tags(self):
        """标签列表，用于过滤。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleInfoList: 规则信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleInfoList: list of RuleBriefInfo
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _PageNumber: 当前页号
        :type PageNumber: int
        :param _PageSize: 单页大小
        :type PageSize: int
        :param _SearchType: 查询类型（可选）matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value
        :type SearchType: str
        :param _Keyword: 查询关键词（可选）
        :type Keyword: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleInfoList = None
        self._TotalCount = None
        self._PageNumber = None
        self._PageSize = None
        self._SearchType = None
        self._Keyword = None
        self._RequestId = None

    @property
    def RuleInfoList(self):
        """规则信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RuleBriefInfo
        """
        return self._RuleInfoList

    @RuleInfoList.setter
    def RuleInfoList(self, RuleInfoList):
        self._RuleInfoList = RuleInfoList

    @property
    def TotalCount(self):
        """总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PageNumber(self):
        """当前页号
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """单页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SearchType(self):
        """查询类型（可选）matchName表示匹配名称，matchCode表示匹配code，ruleName表示规则名称，tag表示标签Key/Value
        :rtype: str
        """
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Keyword(self):
        """查询关键词（可选）
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

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
        if params.get("RuleInfoList") is not None:
            self._RuleInfoList = []
            for item in params.get("RuleInfoList"):
                obj = RuleBriefInfo()
                obj._deserialize(item)
                self._RuleInfoList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SearchType = params.get("SearchType")
        self._Keyword = params.get("Keyword")
        self._RequestId = params.get("RequestId")


class DescribeTokenRequest(AbstractModel):
    """DescribeToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配code
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        """匹配code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenResponse(AbstractModel):
    """DescribeToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchToken: 当前的MatchCode对应的Token。如果当前MatchCode没有Token，该参数可能取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchToken: str
        :param _CompatibleSpan: 当Token被替换后，GPM将兼容推送原始Token的时间（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CompatibleSpan: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchToken = None
        self._CompatibleSpan = None
        self._RequestId = None

    @property
    def MatchToken(self):
        """当前的MatchCode对应的Token。如果当前MatchCode没有Token，该参数可能取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchToken

    @MatchToken.setter
    def MatchToken(self, MatchToken):
        self._MatchToken = MatchToken

    @property
    def CompatibleSpan(self):
        """当Token被替换后，GPM将兼容推送原始Token的时间（秒）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CompatibleSpan

    @CompatibleSpan.setter
    def CompatibleSpan(self, CompatibleSpan):
        self._CompatibleSpan = CompatibleSpan

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
        self._MatchToken = params.get("MatchToken")
        self._CompatibleSpan = params.get("CompatibleSpan")
        self._RequestId = params.get("RequestId")


class MTicket(AbstractModel):
    """matchCode和匹配票据 ID组合结构

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配Code
        :type MatchCode: str
        :param _MatchTicketId: 匹配票据 ID
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        """匹配Code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchTicketId(self):
        """匹配票据 ID
        :rtype: str
        """
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchAttribute(AbstractModel):
    """玩家匹配属性

    """

    def __init__(self):
        r"""
        :param _Name: 属性名 长度 128 [a-zA-Z0-9-\.]*
        :type Name: str
        :param _Type: 属性类型: 0 数值; 1 string; 默认 0
        :type Type: int
        :param _NumberValue: 数字属性值 默认 0.0
        :type NumberValue: float
        :param _StringValue: 字符串属性值 长度 128 默认 ""
        :type StringValue: str
        :param _ListValue: list 属性值
        :type ListValue: list of str
        :param _MapValue: 字典属性值
        :type MapValue: list of AttributeMap
        """
        self._Name = None
        self._Type = None
        self._NumberValue = None
        self._StringValue = None
        self._ListValue = None
        self._MapValue = None

    @property
    def Name(self):
        """属性名 长度 128 [a-zA-Z0-9-\.]*
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """属性类型: 0 数值; 1 string; 默认 0
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NumberValue(self):
        """数字属性值 默认 0.0
        :rtype: float
        """
        return self._NumberValue

    @NumberValue.setter
    def NumberValue(self, NumberValue):
        self._NumberValue = NumberValue

    @property
    def StringValue(self):
        """字符串属性值 长度 128 默认 ""
        :rtype: str
        """
        return self._StringValue

    @StringValue.setter
    def StringValue(self, StringValue):
        self._StringValue = StringValue

    @property
    def ListValue(self):
        """list 属性值
        :rtype: list of str
        """
        return self._ListValue

    @ListValue.setter
    def ListValue(self, ListValue):
        self._ListValue = ListValue

    @property
    def MapValue(self):
        """字典属性值
        :rtype: list of AttributeMap
        """
        return self._MapValue

    @MapValue.setter
    def MapValue(self, MapValue):
        self._MapValue = MapValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._NumberValue = params.get("NumberValue")
        self._StringValue = params.get("StringValue")
        self._ListValue = params.get("ListValue")
        if params.get("MapValue") is not None:
            self._MapValue = []
            for item in params.get("MapValue"):
                obj = AttributeMap()
                obj._deserialize(item)
                self._MapValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchCodeAttr(AbstractModel):
    """匹配code

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配code
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchCode: str
        """
        self._MatchCode = None

    @property
    def MatchCode(self):
        """匹配code
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchInfo(AbstractModel):
    """匹配信息

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配code
        :type MatchCode: str
        :param _MatchName: 匹配名称
        :type MatchName: str
        :param _MatchDesc: 匹配描述
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchDesc: str
        :param _RuleCode: 规则code
        :type RuleCode: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Timeout: 超时时间
        :type Timeout: int
        :param _NotifyUrl: 接收通知地址
        :type NotifyUrl: str
        :param _ServerType: 是否为匹配结果请求服务器资源，0否，1请求GSE资源
        :type ServerType: int
        :param _ServerRegion: 服务器队列所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerRegion: str
        :param _ServerQueue: 服务器队列
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerQueue: str
        :param _CustomPushData: 自定义推送数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomPushData: str
        :param _ServerSessionData: 游戏服务器会话数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerSessionData: str
        :param _GameProperties: 游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :type GameProperties: list of StringKV
        :param _LogSwitch: 日志开关，0表示关，1表示开
        :type LogSwitch: int
        :param _LogsetId: 日志集id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param _LogsetName: 日志集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetName: str
        :param _LogTopicId: 日志主题id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        :param _LogTopicName: 日志主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicName: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of StringKV
        :param _Region: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _Uin: 用户主账号Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _CreateUin: 用户创建账号Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        :param _RuleName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _LogStatus: 日志状态，0表示正常，1表示日志集不存在，2表示日志主题不存在，3表示日志集和日志主题都不存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogStatus: int
        """
        self._MatchCode = None
        self._MatchName = None
        self._MatchDesc = None
        self._RuleCode = None
        self._CreateTime = None
        self._Timeout = None
        self._NotifyUrl = None
        self._ServerType = None
        self._ServerRegion = None
        self._ServerQueue = None
        self._CustomPushData = None
        self._ServerSessionData = None
        self._GameProperties = None
        self._LogSwitch = None
        self._LogsetId = None
        self._LogsetName = None
        self._LogTopicId = None
        self._LogTopicName = None
        self._Tags = None
        self._Region = None
        self._AppId = None
        self._Uin = None
        self._CreateUin = None
        self._RuleName = None
        self._LogStatus = None

    @property
    def MatchCode(self):
        """匹配code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchName(self):
        """匹配名称
        :rtype: str
        """
        return self._MatchName

    @MatchName.setter
    def MatchName(self, MatchName):
        self._MatchName = MatchName

    @property
    def MatchDesc(self):
        """匹配描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchDesc

    @MatchDesc.setter
    def MatchDesc(self, MatchDesc):
        self._MatchDesc = MatchDesc

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Timeout(self):
        """超时时间
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def NotifyUrl(self):
        """接收通知地址
        :rtype: str
        """
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def ServerType(self):
        """是否为匹配结果请求服务器资源，0否，1请求GSE资源
        :rtype: int
        """
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def ServerRegion(self):
        """服务器队列所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerRegion

    @ServerRegion.setter
    def ServerRegion(self, ServerRegion):
        self._ServerRegion = ServerRegion

    @property
    def ServerQueue(self):
        """服务器队列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerQueue

    @ServerQueue.setter
    def ServerQueue(self, ServerQueue):
        self._ServerQueue = ServerQueue

    @property
    def CustomPushData(self):
        """自定义推送数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomPushData

    @CustomPushData.setter
    def CustomPushData(self, CustomPushData):
        self._CustomPushData = CustomPushData

    @property
    def ServerSessionData(self):
        """游戏服务器会话数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerSessionData

    @ServerSessionData.setter
    def ServerSessionData(self, ServerSessionData):
        self._ServerSessionData = ServerSessionData

    @property
    def GameProperties(self):
        """游戏属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StringKV
        """
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def LogSwitch(self):
        """日志开关，0表示关，1表示开
        :rtype: int
        """
        return self._LogSwitch

    @LogSwitch.setter
    def LogSwitch(self, LogSwitch):
        self._LogSwitch = LogSwitch

    @property
    def LogsetId(self):
        """日志集id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def LogTopicId(self):
        """日志主题id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def LogTopicName(self):
        """日志主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogTopicName

    @LogTopicName.setter
    def LogTopicName(self, LogTopicName):
        self._LogTopicName = LogTopicName

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StringKV
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Region(self):
        """地区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        """用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """用户主账号Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CreateUin(self):
        """用户创建账号Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def RuleName(self):
        """规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def LogStatus(self):
        """日志状态，0表示正常，1表示日志集不存在，2表示日志主题不存在，3表示日志集和日志主题都不存在。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LogStatus

    @LogStatus.setter
    def LogStatus(self, LogStatus):
        self._LogStatus = LogStatus


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._MatchName = params.get("MatchName")
        self._MatchDesc = params.get("MatchDesc")
        self._RuleCode = params.get("RuleCode")
        self._CreateTime = params.get("CreateTime")
        self._Timeout = params.get("Timeout")
        self._NotifyUrl = params.get("NotifyUrl")
        self._ServerType = params.get("ServerType")
        self._ServerRegion = params.get("ServerRegion")
        self._ServerQueue = params.get("ServerQueue")
        self._CustomPushData = params.get("CustomPushData")
        self._ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._LogSwitch = params.get("LogSwitch")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._LogTopicId = params.get("LogTopicId")
        self._LogTopicName = params.get("LogTopicName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._CreateUin = params.get("CreateUin")
        self._RuleName = params.get("RuleName")
        self._LogStatus = params.get("LogStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MatchTicket(AbstractModel):
    """匹配票据信息

    """

    def __init__(self):
        r"""
        :param _Id: 匹配票据 ID长度 128 [a-zA-Z0-9-\.]*
        :type Id: str
        :param _MatchCode: 匹配 Code
        :type MatchCode: str
        :param _MatchResult: 根据 MatchType 取不同的结构序列化结果
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchResult: str
        :param _MatchType: 表示不同的匹配类型,NORMAL | GSE
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchType: str
        :param _Players: 玩家信息列表
        :type Players: list of Player
        :param _Status: 匹配状态: SEARCHING 匹配中; PLACING 匹配放置中; COMPLETED 匹配完成; CANCELLED 匹配取消; TIMEDOUT 匹配超时; FAILED 匹配失败
        :type Status: str
        :param _StatusMessage: 匹配状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMessage: str
        :param _StatusReason: 匹配状态原因
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusReason: str
        :param _StartTime: 收到发起匹配请求的时间 eg: "2020-08-17T08:14:38.077Z"
        :type StartTime: str
        :param _EndTime: 匹配请求因完成、失败、超时、被取消而停止执行的时间 eg: "2020-08-17T08:14:38.077Z"
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._Id = None
        self._MatchCode = None
        self._MatchResult = None
        self._MatchType = None
        self._Players = None
        self._Status = None
        self._StatusMessage = None
        self._StatusReason = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Id(self):
        """匹配票据 ID长度 128 [a-zA-Z0-9-\.]*
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MatchCode(self):
        """匹配 Code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchResult(self):
        """根据 MatchType 取不同的结构序列化结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchResult

    @MatchResult.setter
    def MatchResult(self, MatchResult):
        self._MatchResult = MatchResult

    @property
    def MatchType(self):
        """表示不同的匹配类型,NORMAL | GSE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def Players(self):
        """玩家信息列表
        :rtype: list of Player
        """
        return self._Players

    @Players.setter
    def Players(self, Players):
        self._Players = Players

    @property
    def Status(self):
        """匹配状态: SEARCHING 匹配中; PLACING 匹配放置中; COMPLETED 匹配完成; CANCELLED 匹配取消; TIMEDOUT 匹配超时; FAILED 匹配失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMessage(self):
        """匹配状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage

    @property
    def StatusReason(self):
        """匹配状态原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def StartTime(self):
        """收到发起匹配请求的时间 eg: "2020-08-17T08:14:38.077Z"
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """匹配请求因完成、失败、超时、被取消而停止执行的时间 eg: "2020-08-17T08:14:38.077Z"
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MatchCode = params.get("MatchCode")
        self._MatchResult = params.get("MatchResult")
        self._MatchType = params.get("MatchType")
        if params.get("Players") is not None:
            self._Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self._Players.append(obj)
        self._Status = params.get("Status")
        self._StatusMessage = params.get("StatusMessage")
        self._StatusReason = params.get("StatusReason")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchRequest(AbstractModel):
    """ModifyMatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchName: 匹配名称，[a-zA-Z0-9-\.]* 长度128
        :type MatchName: str
        :param _RuleCode: 规则code
        :type RuleCode: str
        :param _Timeout: 超时时间，1-600秒
        :type Timeout: int
        :param _ServerType: 是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源
        :type ServerType: int
        :param _MatchCode: 匹配code
        :type MatchCode: str
        :param _MatchDesc: 匹配描述，最长1024
        :type MatchDesc: str
        :param _NotifyUrl: 只支持 http 和 https 协议
        :type NotifyUrl: str
        :param _ServerRegion: 游戏服务器队列地域
        :type ServerRegion: str
        :param _ServerQueue: 游戏服务器队列
        :type ServerQueue: str
        :param _CustomPushData: 自定义推送数据
        :type CustomPushData: str
        :param _ServerSessionData: 游戏服务器会话数据
        :type ServerSessionData: str
        :param _GameProperties: 游戏属性，key-value结构的数组
        :type GameProperties: list of StringKV
        :param _LogSwitch: 日志开关，0表示关，1表示开
        :type LogSwitch: int
        :param _Tags: 标签，key-value结构的数组
        :type Tags: list of StringKV
        """
        self._MatchName = None
        self._RuleCode = None
        self._Timeout = None
        self._ServerType = None
        self._MatchCode = None
        self._MatchDesc = None
        self._NotifyUrl = None
        self._ServerRegion = None
        self._ServerQueue = None
        self._CustomPushData = None
        self._ServerSessionData = None
        self._GameProperties = None
        self._LogSwitch = None
        self._Tags = None

    @property
    def MatchName(self):
        """匹配名称，[a-zA-Z0-9-\.]* 长度128
        :rtype: str
        """
        return self._MatchName

    @MatchName.setter
    def MatchName(self, MatchName):
        self._MatchName = MatchName

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def Timeout(self):
        """超时时间，1-600秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ServerType(self):
        """是否为匹配结果请求服务器资源，0表示否，1表示请求GSE资源
        :rtype: int
        """
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def MatchCode(self):
        """匹配code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def MatchDesc(self):
        """匹配描述，最长1024
        :rtype: str
        """
        return self._MatchDesc

    @MatchDesc.setter
    def MatchDesc(self, MatchDesc):
        self._MatchDesc = MatchDesc

    @property
    def NotifyUrl(self):
        """只支持 http 和 https 协议
        :rtype: str
        """
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def ServerRegion(self):
        """游戏服务器队列地域
        :rtype: str
        """
        return self._ServerRegion

    @ServerRegion.setter
    def ServerRegion(self, ServerRegion):
        self._ServerRegion = ServerRegion

    @property
    def ServerQueue(self):
        """游戏服务器队列
        :rtype: str
        """
        return self._ServerQueue

    @ServerQueue.setter
    def ServerQueue(self, ServerQueue):
        self._ServerQueue = ServerQueue

    @property
    def CustomPushData(self):
        """自定义推送数据
        :rtype: str
        """
        return self._CustomPushData

    @CustomPushData.setter
    def CustomPushData(self, CustomPushData):
        self._CustomPushData = CustomPushData

    @property
    def ServerSessionData(self):
        """游戏服务器会话数据
        :rtype: str
        """
        return self._ServerSessionData

    @ServerSessionData.setter
    def ServerSessionData(self, ServerSessionData):
        self._ServerSessionData = ServerSessionData

    @property
    def GameProperties(self):
        """游戏属性，key-value结构的数组
        :rtype: list of StringKV
        """
        return self._GameProperties

    @GameProperties.setter
    def GameProperties(self, GameProperties):
        self._GameProperties = GameProperties

    @property
    def LogSwitch(self):
        """日志开关，0表示关，1表示开
        :rtype: int
        """
        return self._LogSwitch

    @LogSwitch.setter
    def LogSwitch(self, LogSwitch):
        self._LogSwitch = LogSwitch

    @property
    def Tags(self):
        """标签，key-value结构的数组
        :rtype: list of StringKV
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MatchName = params.get("MatchName")
        self._RuleCode = params.get("RuleCode")
        self._Timeout = params.get("Timeout")
        self._ServerType = params.get("ServerType")
        self._MatchCode = params.get("MatchCode")
        self._MatchDesc = params.get("MatchDesc")
        self._NotifyUrl = params.get("NotifyUrl")
        self._ServerRegion = params.get("ServerRegion")
        self._ServerQueue = params.get("ServerQueue")
        self._CustomPushData = params.get("CustomPushData")
        self._ServerSessionData = params.get("ServerSessionData")
        if params.get("GameProperties") is not None:
            self._GameProperties = []
            for item in params.get("GameProperties"):
                obj = StringKV()
                obj._deserialize(item)
                self._GameProperties.append(obj)
        self._LogSwitch = params.get("LogSwitch")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMatchResponse(AbstractModel):
    """ModifyMatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchInfo: 匹配信息
        :type MatchInfo: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchInfo = None
        self._RequestId = None

    @property
    def MatchInfo(self):
        """匹配信息
        :rtype: :class:`tencentcloud.gpm.v20200820.models.MatchInfo`
        """
        return self._MatchInfo

    @MatchInfo.setter
    def MatchInfo(self, MatchInfo):
        self._MatchInfo = MatchInfo

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
        if params.get("MatchInfo") is not None:
            self._MatchInfo = MatchInfo()
            self._MatchInfo._deserialize(params.get("MatchInfo"))
        self._RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleCode: 规则code
        :type RuleCode: str
        :param _RuleName: 规则名称，只能包含数字、字母、. 和 -
        :type RuleName: str
        :param _RuleDesc: 规则描述，最长1024
        :type RuleDesc: str
        :param _Tags: 标签，key-value结构的数组，最多关联50组标签
        :type Tags: list of StringKV
        """
        self._RuleCode = None
        self._RuleName = None
        self._RuleDesc = None
        self._Tags = None

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def RuleName(self):
        """规则名称，只能包含数字、字母、. 和 -
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleDesc(self):
        """规则描述，最长1024
        :rtype: str
        """
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def Tags(self):
        """标签，key-value结构的数组，最多关联50组标签
        :rtype: list of StringKV
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RuleCode = params.get("RuleCode")
        self._RuleName = params.get("RuleName")
        self._RuleDesc = params.get("RuleDesc")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleInfo: 规则信息
        :type RuleInfo: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleInfo = None
        self._RequestId = None

    @property
    def RuleInfo(self):
        """规则信息
        :rtype: :class:`tencentcloud.gpm.v20200820.models.RuleInfo`
        """
        return self._RuleInfo

    @RuleInfo.setter
    def RuleInfo(self, RuleInfo):
        self._RuleInfo = RuleInfo

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
        if params.get("RuleInfo") is not None:
            self._RuleInfo = RuleInfo()
            self._RuleInfo._deserialize(params.get("RuleInfo"))
        self._RequestId = params.get("RequestId")


class ModifyTokenRequest(AbstractModel):
    """ModifyToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配Code。
        :type MatchCode: str
        :param _CompatibleSpan: 单位秒，取值0-1800。此参数表示当前Token被替换后，GPM将持续推送原Token的时间。在CompatibleSpan时间范围内，用户将在事件消息中收到当前和原始Token。
        :type CompatibleSpan: int
        :param _MatchToken: Token，[a-zA-Z0-9-_.], 长度0-64。如果为空，将由GPM随机生成。
        :type MatchToken: str
        """
        self._MatchCode = None
        self._CompatibleSpan = None
        self._MatchToken = None

    @property
    def MatchCode(self):
        """匹配Code。
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def CompatibleSpan(self):
        """单位秒，取值0-1800。此参数表示当前Token被替换后，GPM将持续推送原Token的时间。在CompatibleSpan时间范围内，用户将在事件消息中收到当前和原始Token。
        :rtype: int
        """
        return self._CompatibleSpan

    @CompatibleSpan.setter
    def CompatibleSpan(self, CompatibleSpan):
        self._CompatibleSpan = CompatibleSpan

    @property
    def MatchToken(self):
        """Token，[a-zA-Z0-9-_.], 长度0-64。如果为空，将由GPM随机生成。
        :rtype: str
        """
        return self._MatchToken

    @MatchToken.setter
    def MatchToken(self, MatchToken):
        self._MatchToken = MatchToken


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        self._CompatibleSpan = params.get("CompatibleSpan")
        self._MatchToken = params.get("MatchToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenResponse(AbstractModel):
    """ModifyToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchToken: 成功设置的Token。
        :type MatchToken: str
        :param _CompatibleSpan: 当前Token被替换后，GPM将持续推送原Token的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CompatibleSpan: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchToken = None
        self._CompatibleSpan = None
        self._RequestId = None

    @property
    def MatchToken(self):
        """成功设置的Token。
        :rtype: str
        """
        return self._MatchToken

    @MatchToken.setter
    def MatchToken(self, MatchToken):
        self._MatchToken = MatchToken

    @property
    def CompatibleSpan(self):
        """当前Token被替换后，GPM将持续推送原Token的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CompatibleSpan

    @CompatibleSpan.setter
    def CompatibleSpan(self, CompatibleSpan):
        self._CompatibleSpan = CompatibleSpan

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
        self._MatchToken = params.get("MatchToken")
        self._CompatibleSpan = params.get("CompatibleSpan")
        self._RequestId = params.get("RequestId")


class Player(AbstractModel):
    """玩家信息。

    """

    def __init__(self):
        r"""
        :param _Id: 玩家 PlayerId 长度 128 [a-zA-Z\d-\._]*
        :type Id: str
        :param _Name: 玩家昵称，长度 128
        :type Name: str
        :param _MatchAttributes: 玩家匹配属性，最多 10 条
        :type MatchAttributes: list of MatchAttribute
        :param _Team: 队伍名，可以传递不同队伍名，长度 128 [a-zA-Z0-9-\.]*
        :type Team: str
        :param _CustomPlayerStatus: 自定义玩家状态 透传参数 [0, 99999]
        :type CustomPlayerStatus: int
        :param _CustomProfile: 自定义玩家信息 透传参数 长度 1024
        :type CustomProfile: str
        :param _RegionLatencies: 各区域延迟，最多 20 条
        :type RegionLatencies: list of RegionLatency
        """
        self._Id = None
        self._Name = None
        self._MatchAttributes = None
        self._Team = None
        self._CustomPlayerStatus = None
        self._CustomProfile = None
        self._RegionLatencies = None

    @property
    def Id(self):
        """玩家 PlayerId 长度 128 [a-zA-Z\d-\._]*
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """玩家昵称，长度 128
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MatchAttributes(self):
        """玩家匹配属性，最多 10 条
        :rtype: list of MatchAttribute
        """
        return self._MatchAttributes

    @MatchAttributes.setter
    def MatchAttributes(self, MatchAttributes):
        self._MatchAttributes = MatchAttributes

    @property
    def Team(self):
        """队伍名，可以传递不同队伍名，长度 128 [a-zA-Z0-9-\.]*
        :rtype: str
        """
        return self._Team

    @Team.setter
    def Team(self, Team):
        self._Team = Team

    @property
    def CustomPlayerStatus(self):
        """自定义玩家状态 透传参数 [0, 99999]
        :rtype: int
        """
        return self._CustomPlayerStatus

    @CustomPlayerStatus.setter
    def CustomPlayerStatus(self, CustomPlayerStatus):
        self._CustomPlayerStatus = CustomPlayerStatus

    @property
    def CustomProfile(self):
        """自定义玩家信息 透传参数 长度 1024
        :rtype: str
        """
        return self._CustomProfile

    @CustomProfile.setter
    def CustomProfile(self, CustomProfile):
        self._CustomProfile = CustomProfile

    @property
    def RegionLatencies(self):
        """各区域延迟，最多 20 条
        :rtype: list of RegionLatency
        """
        return self._RegionLatencies

    @RegionLatencies.setter
    def RegionLatencies(self, RegionLatencies):
        self._RegionLatencies = RegionLatencies


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("MatchAttributes") is not None:
            self._MatchAttributes = []
            for item in params.get("MatchAttributes"):
                obj = MatchAttribute()
                obj._deserialize(item)
                self._MatchAttributes.append(obj)
        self._Team = params.get("Team")
        self._CustomPlayerStatus = params.get("CustomPlayerStatus")
        self._CustomProfile = params.get("CustomProfile")
        if params.get("RegionLatencies") is not None:
            self._RegionLatencies = []
            for item in params.get("RegionLatencies"):
                obj = RegionLatency()
                obj._deserialize(item)
                self._RegionLatencies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionLatency(AbstractModel):
    """玩家到各区域的延迟

    """

    def __init__(self):
        r"""
        :param _Region: 地域
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
        :param _Latency: 毫秒延迟 0～999999
        :type Latency: int
        """
        self._Region = None
        self._Latency = None

    @property
    def Region(self):
        """地域
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
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Latency(self):
        """毫秒延迟 0～999999
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Latency = params.get("Latency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportOverviewData(AbstractModel):
    """匹配概况

    """

    def __init__(self):
        r"""
        :param _TotalTimes: 总次数
        :type TotalTimes: str
        :param _SuccessPercent: 成功率
        :type SuccessPercent: float
        :param _TimeoutPercent: 超时率
        :type TimeoutPercent: float
        :param _FailPercent: 失败率
        :type FailPercent: float
        :param _AverageSec: 平均匹配时间
        :type AverageSec: float
        """
        self._TotalTimes = None
        self._SuccessPercent = None
        self._TimeoutPercent = None
        self._FailPercent = None
        self._AverageSec = None

    @property
    def TotalTimes(self):
        """总次数
        :rtype: str
        """
        return self._TotalTimes

    @TotalTimes.setter
    def TotalTimes(self, TotalTimes):
        self._TotalTimes = TotalTimes

    @property
    def SuccessPercent(self):
        """成功率
        :rtype: float
        """
        return self._SuccessPercent

    @SuccessPercent.setter
    def SuccessPercent(self, SuccessPercent):
        self._SuccessPercent = SuccessPercent

    @property
    def TimeoutPercent(self):
        """超时率
        :rtype: float
        """
        return self._TimeoutPercent

    @TimeoutPercent.setter
    def TimeoutPercent(self, TimeoutPercent):
        self._TimeoutPercent = TimeoutPercent

    @property
    def FailPercent(self):
        """失败率
        :rtype: float
        """
        return self._FailPercent

    @FailPercent.setter
    def FailPercent(self, FailPercent):
        self._FailPercent = FailPercent

    @property
    def AverageSec(self):
        """平均匹配时间
        :rtype: float
        """
        return self._AverageSec

    @AverageSec.setter
    def AverageSec(self, AverageSec):
        self._AverageSec = AverageSec


    def _deserialize(self, params):
        self._TotalTimes = params.get("TotalTimes")
        self._SuccessPercent = params.get("SuccessPercent")
        self._TimeoutPercent = params.get("TimeoutPercent")
        self._FailPercent = params.get("FailPercent")
        self._AverageSec = params.get("AverageSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportTrendData(AbstractModel):
    """统计数据之趋势数据

    """

    def __init__(self):
        r"""
        :param _TotalList: 总次数
        :type TotalList: list of str
        :param _CancelList: 被取消次数
        :type CancelList: list of str
        :param _SuccessList: 成功次数
        :type SuccessList: list of str
        :param _FailList: 失败次数
        :type FailList: list of str
        :param _TimeoutList: 超时次数
        :type TimeoutList: list of str
        :param _TimeList: 时间数组，单位：秒
        :type TimeList: list of str
        """
        self._TotalList = None
        self._CancelList = None
        self._SuccessList = None
        self._FailList = None
        self._TimeoutList = None
        self._TimeList = None

    @property
    def TotalList(self):
        """总次数
        :rtype: list of str
        """
        return self._TotalList

    @TotalList.setter
    def TotalList(self, TotalList):
        self._TotalList = TotalList

    @property
    def CancelList(self):
        """被取消次数
        :rtype: list of str
        """
        return self._CancelList

    @CancelList.setter
    def CancelList(self, CancelList):
        self._CancelList = CancelList

    @property
    def SuccessList(self):
        """成功次数
        :rtype: list of str
        """
        return self._SuccessList

    @SuccessList.setter
    def SuccessList(self, SuccessList):
        self._SuccessList = SuccessList

    @property
    def FailList(self):
        """失败次数
        :rtype: list of str
        """
        return self._FailList

    @FailList.setter
    def FailList(self, FailList):
        self._FailList = FailList

    @property
    def TimeoutList(self):
        """超时次数
        :rtype: list of str
        """
        return self._TimeoutList

    @TimeoutList.setter
    def TimeoutList(self, TimeoutList):
        self._TimeoutList = TimeoutList

    @property
    def TimeList(self):
        """时间数组，单位：秒
        :rtype: list of str
        """
        return self._TimeList

    @TimeList.setter
    def TimeList(self, TimeList):
        self._TimeList = TimeList


    def _deserialize(self, params):
        self._TotalList = params.get("TotalList")
        self._CancelList = params.get("CancelList")
        self._SuccessList = params.get("SuccessList")
        self._FailList = params.get("FailList")
        self._TimeoutList = params.get("TimeoutList")
        self._TimeList = params.get("TimeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleBriefInfo(AbstractModel):
    """规则简单信息

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称 [a-zA-Z\d-\.]*
        :type RuleName: str
        :param _MatchCodeList: 关联匹配
        :type MatchCodeList: list of StringKV
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _RuleCode: 规则code
        :type RuleCode: str
        """
        self._RuleName = None
        self._MatchCodeList = None
        self._CreateTime = None
        self._RuleCode = None

    @property
    def RuleName(self):
        """规则名称 [a-zA-Z\d-\.]*
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def MatchCodeList(self):
        """关联匹配
        :rtype: list of StringKV
        """
        return self._MatchCodeList

    @MatchCodeList.setter
    def MatchCodeList(self, MatchCodeList):
        self._MatchCodeList = MatchCodeList

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("MatchCodeList") is not None:
            self._MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self._MatchCodeList.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._RuleCode = params.get("RuleCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称 [a-zA-Z0-9-\.]*
        :type RuleName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _RuleDesc: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDesc: str
        :param _RuleScript: 规则脚本
        :type RuleScript: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of StringKV
        :param _MatchCodeList: 关联匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchCodeList: list of StringKV
        :param _RuleCode: 规则code
        :type RuleCode: str
        :param _Region: 地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _AppId: 用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _CreateUin: 用户OwnerUin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateUin: str
        """
        self._RuleName = None
        self._CreateTime = None
        self._RuleDesc = None
        self._RuleScript = None
        self._Tags = None
        self._MatchCodeList = None
        self._RuleCode = None
        self._Region = None
        self._AppId = None
        self._Uin = None
        self._CreateUin = None

    @property
    def RuleName(self):
        """规则名称 [a-zA-Z0-9-\.]*
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RuleDesc(self):
        """规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleDesc

    @RuleDesc.setter
    def RuleDesc(self, RuleDesc):
        self._RuleDesc = RuleDesc

    @property
    def RuleScript(self):
        """规则脚本
        :rtype: str
        """
        return self._RuleScript

    @RuleScript.setter
    def RuleScript(self, RuleScript):
        self._RuleScript = RuleScript

    @property
    def Tags(self):
        """标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StringKV
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def MatchCodeList(self):
        """关联匹配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StringKV
        """
        return self._MatchCodeList

    @MatchCodeList.setter
    def MatchCodeList(self, MatchCodeList):
        self._MatchCodeList = MatchCodeList

    @property
    def RuleCode(self):
        """规则code
        :rtype: str
        """
        return self._RuleCode

    @RuleCode.setter
    def RuleCode(self, RuleCode):
        self._RuleCode = RuleCode

    @property
    def Region(self):
        """地区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        """用户AppId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CreateUin(self):
        """用户OwnerUin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._CreateTime = params.get("CreateTime")
        self._RuleDesc = params.get("RuleDesc")
        self._RuleScript = params.get("RuleScript")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = StringKV()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("MatchCodeList") is not None:
            self._MatchCodeList = []
            for item in params.get("MatchCodeList"):
                obj = StringKV()
                obj._deserialize(item)
                self._MatchCodeList.append(obj)
        self._RuleCode = params.get("RuleCode")
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._CreateUin = params.get("CreateUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillRequest(AbstractModel):
    """StartMatchingBackfill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配code
        :type MatchCode: str
        :param _Players: 玩家信息
        :type Players: list of Player
        :param _GameServerSessionId: 游戏服务器回话 ID [1-256] 个ASCII 字符
        :type GameServerSessionId: str
        :param _MatchTicketId: 匹配票据 Id 默认 "" 为空则由 GPM 自动生成 长度 [1, 128]
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._Players = None
        self._GameServerSessionId = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        """匹配code
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def Players(self):
        """玩家信息
        :rtype: list of Player
        """
        return self._Players

    @Players.setter
    def Players(self, Players):
        self._Players = Players

    @property
    def GameServerSessionId(self):
        """游戏服务器回话 ID [1-256] 个ASCII 字符
        :rtype: str
        """
        return self._GameServerSessionId

    @GameServerSessionId.setter
    def GameServerSessionId(self, GameServerSessionId):
        self._GameServerSessionId = GameServerSessionId

    @property
    def MatchTicketId(self):
        """匹配票据 Id 默认 "" 为空则由 GPM 自动生成 长度 [1, 128]
        :rtype: str
        """
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self._Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self._Players.append(obj)
        self._GameServerSessionId = params.get("GameServerSessionId")
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingBackfillResponse(AbstractModel):
    """StartMatchingBackfill返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchTicket: 匹配票据
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchTicket: :class:`tencentcloud.gpm.v20200820.models.MatchTicket`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MatchTicket = None
        self._RequestId = None

    @property
    def MatchTicket(self):
        """匹配票据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gpm.v20200820.models.MatchTicket`
        """
        return self._MatchTicket

    @MatchTicket.setter
    def MatchTicket(self, MatchTicket):
        self._MatchTicket = MatchTicket

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
        if params.get("MatchTicket") is not None:
            self._MatchTicket = MatchTicket()
            self._MatchTicket._deserialize(params.get("MatchTicket"))
        self._RequestId = params.get("RequestId")


class StartMatchingRequest(AbstractModel):
    """StartMatching请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MatchCode: 匹配 Code。
        :type MatchCode: str
        :param _Players: 玩家信息 最多 200 条。
        :type Players: list of Player
        :param _MatchTicketId: 匹配票据 ID 默认空字符串，为空则由 GPM 自动生成 长度 128，只能包含数字、字母、. 和 -
        :type MatchTicketId: str
        """
        self._MatchCode = None
        self._Players = None
        self._MatchTicketId = None

    @property
    def MatchCode(self):
        """匹配 Code。
        :rtype: str
        """
        return self._MatchCode

    @MatchCode.setter
    def MatchCode(self, MatchCode):
        self._MatchCode = MatchCode

    @property
    def Players(self):
        """玩家信息 最多 200 条。
        :rtype: list of Player
        """
        return self._Players

    @Players.setter
    def Players(self, Players):
        self._Players = Players

    @property
    def MatchTicketId(self):
        """匹配票据 ID 默认空字符串，为空则由 GPM 自动生成 长度 128，只能包含数字、字母、. 和 -
        :rtype: str
        """
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId


    def _deserialize(self, params):
        self._MatchCode = params.get("MatchCode")
        if params.get("Players") is not None:
            self._Players = []
            for item in params.get("Players"):
                obj = Player()
                obj._deserialize(item)
                self._Players.append(obj)
        self._MatchTicketId = params.get("MatchTicketId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMatchingResponse(AbstractModel):
    """StartMatching返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrCode: 错误码。
        :type ErrCode: int
        :param _MatchTicketId: 匹配票据 ID长度 128。
        :type MatchTicketId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrCode = None
        self._MatchTicketId = None
        self._RequestId = None

    @property
    def ErrCode(self):
        """错误码。
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def MatchTicketId(self):
        """匹配票据 ID长度 128。
        :rtype: str
        """
        return self._MatchTicketId

    @MatchTicketId.setter
    def MatchTicketId(self, MatchTicketId):
        self._MatchTicketId = MatchTicketId

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
        self._ErrCode = params.get("ErrCode")
        self._MatchTicketId = params.get("MatchTicketId")
        self._RequestId = params.get("RequestId")


class StringKV(AbstractModel):
    """string keyValue解构

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        