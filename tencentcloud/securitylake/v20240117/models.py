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


class DescribeSecurityAlarmTableListRequest(AbstractModel):
    r"""DescribeSecurityAlarmTableList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdlId: 实例ID
        :type SdlId: str
        :param _Filters: 过滤条件
        :type Filters: list of WebSearchFilter
        :param _Limit: 长度
        :type Limit: int
        :param _Offset: 偏移
        :type Offset: int
        :param _Order: 排序
        :type Order: str
        :param _By: 排序字段
        :type By: str
        :param _StartTime: 开始时间,毫秒
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._SdlId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdlId(self):
        r"""实例ID
        :rtype: str
        """
        return self._SdlId

    @SdlId.setter
    def SdlId(self, SdlId):
        self._SdlId = SdlId

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of WebSearchFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""长度
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def StartTime(self):
        r"""开始时间,毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdlId = params.get("SdlId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = WebSearchFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityAlarmTableListResponse(AbstractModel):
    r"""DescribeSecurityAlarmTableList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmList: 字段列表
        :type AlarmList: list of SecurityAlarmTable
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _Limit: 限制
        :type Limit: int
        :param _Offset: 偏移
        :type Offset: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmList = None
        self._TotalCount = None
        self._Limit = None
        self._Offset = None
        self._RequestId = None

    @property
    def AlarmList(self):
        r"""字段列表
        :rtype: list of SecurityAlarmTable
        """
        return self._AlarmList

    @AlarmList.setter
    def AlarmList(self, AlarmList):
        self._AlarmList = AlarmList

    @property
    def TotalCount(self):
        r"""数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Limit(self):
        r"""限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlarmList") is not None:
            self._AlarmList = []
            for item in params.get("AlarmList"):
                obj = SecurityAlarmTable()
                obj._deserialize(item)
                self._AlarmList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._RequestId = params.get("RequestId")


class SecurityAlarmTable(AbstractModel):
    r"""告警列表

    """

    def __init__(self):
        r"""
        :param _Timestamp: 时间
        :type Timestamp: str
        :param _AlarmName: 告警名称
        :type AlarmName: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _AlarmId: 告警id
        :type AlarmId: int
        :param _Severity: 安全性
        :type Severity: int
        :param _Score: 评分
        :type Score: int
        :param _Category: 分类
        :type Category: str
        :param _SubCategory: 子分类
        :type SubCategory: str
        :param _Tags: 标签
        :type Tags: str
        :param _Payload: 有效载荷
        :type Payload: str
        :param _Result: 结果
        :type Result: str
        :param _Confidence: 可信度
        :type Confidence: int
        :param _Status: 状态
        :type Status: str
        :param _RuleTopic: 规则主题
        :type RuleTopic: str
        :param _HandleTime: 处理时间
        :type HandleTime: str
        :param _Suggestion: 建议
        :type Suggestion: str
        :param _Description: 描述
        :type Description: str
        :param _SourceName: 来源名称
        :type SourceName: str
        :param _AppId: APPID
        :type AppId: int
        :param _RuleId: 规则ID
        :type RuleId: int
        :param _EventTime: 事件时间
        :type EventTime: str
        :param _RuleType: 规则类型
        :type RuleType: str
        :param _AttackNum: 攻击次数
        :type AttackNum: int
        :param _AlarmCount: 告警数量
        :type AlarmCount: int
        :param _AttackSubTechnique: ATT&CK子技术
        :type AttackSubTechnique: str
        :param _AttackTechnique: ATT&CK技术
        :type AttackTechnique: str
        :param _AttackTactic: ATT&CK战术
        :type AttackTactic: str
        :param _AttackSubTechniqueName: ATT&CK子技术名称
        :type AttackSubTechniqueName: str
        :param _AttackTechniqueName: ATT&CK技术名称
        :type AttackTechniqueName: str
        :param _AttackTacticName: 凭证访问
        :type AttackTacticName: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _RuleExpression: 规则表达式
        :type RuleExpression: str
        :param _ExpressionType: 表达式类型
        :type ExpressionType: str
        :param _DrillDownExpression: 下钻表达式
        :type DrillDownExpression: str
        :param _SrcIp: 源IP
        :type SrcIp: str
        :param _SrcPort: 源端口
        :type SrcPort: int
        :param _DstIp: 目的IP
        :type DstIp: str
        :param _DstPort: 目的端口
        :type DstPort: int
        :param _HostIp: 主机IP
        :type HostIp: str
        :param _HostAsset: 主机资产
        :type HostAsset: str
        :param _SdlId: 实例id
        :type SdlId: str
        :param _RichCustomInfos: 自定义富化字段信息
        :type RichCustomInfos: list of str
        :param _AttackerIp: 攻击者ip
        :type AttackerIp: str
        :param _AttackerAsset: 攻击者资产ID
        :type AttackerAsset: str
        :param _VictimIp: 受害者ip
        :type VictimIp: str
        :param _VictimAsset: 受害者资产ID
        :type VictimAsset: str
        :param _AttackDirection: 攻击方向
        :type AttackDirection: str
        :param _TrafficDirection: 流量方向
        :type TrafficDirection: str
        :param _SecurityGroupAlertInfos: 测试
        :type SecurityGroupAlertInfos: list of SecurityGroupAlertInfo
        """
        self._Timestamp = None
        self._AlarmName = None
        self._RuleName = None
        self._AlarmId = None
        self._Severity = None
        self._Score = None
        self._Category = None
        self._SubCategory = None
        self._Tags = None
        self._Payload = None
        self._Result = None
        self._Confidence = None
        self._Status = None
        self._RuleTopic = None
        self._HandleTime = None
        self._Suggestion = None
        self._Description = None
        self._SourceName = None
        self._AppId = None
        self._RuleId = None
        self._EventTime = None
        self._RuleType = None
        self._AttackNum = None
        self._AlarmCount = None
        self._AttackSubTechnique = None
        self._AttackTechnique = None
        self._AttackTactic = None
        self._AttackSubTechniqueName = None
        self._AttackTechniqueName = None
        self._AttackTacticName = None
        self._StartTime = None
        self._EndTime = None
        self._RuleExpression = None
        self._ExpressionType = None
        self._DrillDownExpression = None
        self._SrcIp = None
        self._SrcPort = None
        self._DstIp = None
        self._DstPort = None
        self._HostIp = None
        self._HostAsset = None
        self._SdlId = None
        self._RichCustomInfos = None
        self._AttackerIp = None
        self._AttackerAsset = None
        self._VictimIp = None
        self._VictimAsset = None
        self._AttackDirection = None
        self._TrafficDirection = None
        self._SecurityGroupAlertInfos = None

    @property
    def Timestamp(self):
        r"""时间
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def AlarmName(self):
        r"""告警名称
        :rtype: str
        """
        return self._AlarmName

    @AlarmName.setter
    def AlarmName(self, AlarmName):
        self._AlarmName = AlarmName

    @property
    def RuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def AlarmId(self):
        r"""告警id
        :rtype: int
        """
        return self._AlarmId

    @AlarmId.setter
    def AlarmId(self, AlarmId):
        self._AlarmId = AlarmId

    @property
    def Severity(self):
        r"""安全性
        :rtype: int
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity

    @property
    def Score(self):
        r"""评分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Category(self):
        r"""分类
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def SubCategory(self):
        r"""子分类
        :rtype: str
        """
        return self._SubCategory

    @SubCategory.setter
    def SubCategory(self, SubCategory):
        self._SubCategory = SubCategory

    @property
    def Tags(self):
        r"""标签
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Payload(self):
        r"""有效载荷
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Result(self):
        r"""结果
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Confidence(self):
        r"""可信度
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Status(self):
        r"""状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleTopic(self):
        r"""规则主题
        :rtype: str
        """
        return self._RuleTopic

    @RuleTopic.setter
    def RuleTopic(self, RuleTopic):
        self._RuleTopic = RuleTopic

    @property
    def HandleTime(self):
        r"""处理时间
        :rtype: str
        """
        return self._HandleTime

    @HandleTime.setter
    def HandleTime(self, HandleTime):
        self._HandleTime = HandleTime

    @property
    def Suggestion(self):
        r"""建议
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SourceName(self):
        r"""来源名称
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def AppId(self):
        r"""APPID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: int
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EventTime(self):
        r"""事件时间
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def RuleType(self):
        r"""规则类型
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def AttackNum(self):
        r"""攻击次数
        :rtype: int
        """
        return self._AttackNum

    @AttackNum.setter
    def AttackNum(self, AttackNum):
        self._AttackNum = AttackNum

    @property
    def AlarmCount(self):
        r"""告警数量
        :rtype: int
        """
        return self._AlarmCount

    @AlarmCount.setter
    def AlarmCount(self, AlarmCount):
        self._AlarmCount = AlarmCount

    @property
    def AttackSubTechnique(self):
        r"""ATT&CK子技术
        :rtype: str
        """
        return self._AttackSubTechnique

    @AttackSubTechnique.setter
    def AttackSubTechnique(self, AttackSubTechnique):
        self._AttackSubTechnique = AttackSubTechnique

    @property
    def AttackTechnique(self):
        r"""ATT&CK技术
        :rtype: str
        """
        return self._AttackTechnique

    @AttackTechnique.setter
    def AttackTechnique(self, AttackTechnique):
        self._AttackTechnique = AttackTechnique

    @property
    def AttackTactic(self):
        r"""ATT&CK战术
        :rtype: str
        """
        return self._AttackTactic

    @AttackTactic.setter
    def AttackTactic(self, AttackTactic):
        self._AttackTactic = AttackTactic

    @property
    def AttackSubTechniqueName(self):
        r"""ATT&CK子技术名称
        :rtype: str
        """
        return self._AttackSubTechniqueName

    @AttackSubTechniqueName.setter
    def AttackSubTechniqueName(self, AttackSubTechniqueName):
        self._AttackSubTechniqueName = AttackSubTechniqueName

    @property
    def AttackTechniqueName(self):
        r"""ATT&CK技术名称
        :rtype: str
        """
        return self._AttackTechniqueName

    @AttackTechniqueName.setter
    def AttackTechniqueName(self, AttackTechniqueName):
        self._AttackTechniqueName = AttackTechniqueName

    @property
    def AttackTacticName(self):
        r"""凭证访问
        :rtype: str
        """
        return self._AttackTacticName

    @AttackTacticName.setter
    def AttackTacticName(self, AttackTacticName):
        self._AttackTacticName = AttackTacticName

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RuleExpression(self):
        r"""规则表达式
        :rtype: str
        """
        return self._RuleExpression

    @RuleExpression.setter
    def RuleExpression(self, RuleExpression):
        self._RuleExpression = RuleExpression

    @property
    def ExpressionType(self):
        r"""表达式类型
        :rtype: str
        """
        return self._ExpressionType

    @ExpressionType.setter
    def ExpressionType(self, ExpressionType):
        self._ExpressionType = ExpressionType

    @property
    def DrillDownExpression(self):
        r"""下钻表达式
        :rtype: str
        """
        return self._DrillDownExpression

    @DrillDownExpression.setter
    def DrillDownExpression(self, DrillDownExpression):
        self._DrillDownExpression = DrillDownExpression

    @property
    def SrcIp(self):
        r"""源IP
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def SrcPort(self):
        r"""源端口
        :rtype: int
        """
        return self._SrcPort

    @SrcPort.setter
    def SrcPort(self, SrcPort):
        self._SrcPort = SrcPort

    @property
    def DstIp(self):
        r"""目的IP
        :rtype: str
        """
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def DstPort(self):
        r"""目的端口
        :rtype: int
        """
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def HostIp(self):
        r"""主机IP
        :rtype: str
        """
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def HostAsset(self):
        r"""主机资产
        :rtype: str
        """
        return self._HostAsset

    @HostAsset.setter
    def HostAsset(self, HostAsset):
        self._HostAsset = HostAsset

    @property
    def SdlId(self):
        r"""实例id
        :rtype: str
        """
        return self._SdlId

    @SdlId.setter
    def SdlId(self, SdlId):
        self._SdlId = SdlId

    @property
    def RichCustomInfos(self):
        r"""自定义富化字段信息
        :rtype: list of str
        """
        return self._RichCustomInfos

    @RichCustomInfos.setter
    def RichCustomInfos(self, RichCustomInfos):
        self._RichCustomInfos = RichCustomInfos

    @property
    def AttackerIp(self):
        r"""攻击者ip
        :rtype: str
        """
        return self._AttackerIp

    @AttackerIp.setter
    def AttackerIp(self, AttackerIp):
        self._AttackerIp = AttackerIp

    @property
    def AttackerAsset(self):
        r"""攻击者资产ID
        :rtype: str
        """
        return self._AttackerAsset

    @AttackerAsset.setter
    def AttackerAsset(self, AttackerAsset):
        self._AttackerAsset = AttackerAsset

    @property
    def VictimIp(self):
        r"""受害者ip
        :rtype: str
        """
        return self._VictimIp

    @VictimIp.setter
    def VictimIp(self, VictimIp):
        self._VictimIp = VictimIp

    @property
    def VictimAsset(self):
        r"""受害者资产ID
        :rtype: str
        """
        return self._VictimAsset

    @VictimAsset.setter
    def VictimAsset(self, VictimAsset):
        self._VictimAsset = VictimAsset

    @property
    def AttackDirection(self):
        r"""攻击方向
        :rtype: str
        """
        return self._AttackDirection

    @AttackDirection.setter
    def AttackDirection(self, AttackDirection):
        self._AttackDirection = AttackDirection

    @property
    def TrafficDirection(self):
        r"""流量方向
        :rtype: str
        """
        return self._TrafficDirection

    @TrafficDirection.setter
    def TrafficDirection(self, TrafficDirection):
        self._TrafficDirection = TrafficDirection

    @property
    def SecurityGroupAlertInfos(self):
        r"""测试
        :rtype: list of SecurityGroupAlertInfo
        """
        return self._SecurityGroupAlertInfos

    @SecurityGroupAlertInfos.setter
    def SecurityGroupAlertInfos(self, SecurityGroupAlertInfos):
        self._SecurityGroupAlertInfos = SecurityGroupAlertInfos


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._AlarmName = params.get("AlarmName")
        self._RuleName = params.get("RuleName")
        self._AlarmId = params.get("AlarmId")
        self._Severity = params.get("Severity")
        self._Score = params.get("Score")
        self._Category = params.get("Category")
        self._SubCategory = params.get("SubCategory")
        self._Tags = params.get("Tags")
        self._Payload = params.get("Payload")
        self._Result = params.get("Result")
        self._Confidence = params.get("Confidence")
        self._Status = params.get("Status")
        self._RuleTopic = params.get("RuleTopic")
        self._HandleTime = params.get("HandleTime")
        self._Suggestion = params.get("Suggestion")
        self._Description = params.get("Description")
        self._SourceName = params.get("SourceName")
        self._AppId = params.get("AppId")
        self._RuleId = params.get("RuleId")
        self._EventTime = params.get("EventTime")
        self._RuleType = params.get("RuleType")
        self._AttackNum = params.get("AttackNum")
        self._AlarmCount = params.get("AlarmCount")
        self._AttackSubTechnique = params.get("AttackSubTechnique")
        self._AttackTechnique = params.get("AttackTechnique")
        self._AttackTactic = params.get("AttackTactic")
        self._AttackSubTechniqueName = params.get("AttackSubTechniqueName")
        self._AttackTechniqueName = params.get("AttackTechniqueName")
        self._AttackTacticName = params.get("AttackTacticName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RuleExpression = params.get("RuleExpression")
        self._ExpressionType = params.get("ExpressionType")
        self._DrillDownExpression = params.get("DrillDownExpression")
        self._SrcIp = params.get("SrcIp")
        self._SrcPort = params.get("SrcPort")
        self._DstIp = params.get("DstIp")
        self._DstPort = params.get("DstPort")
        self._HostIp = params.get("HostIp")
        self._HostAsset = params.get("HostAsset")
        self._SdlId = params.get("SdlId")
        self._RichCustomInfos = params.get("RichCustomInfos")
        self._AttackerIp = params.get("AttackerIp")
        self._AttackerAsset = params.get("AttackerAsset")
        self._VictimIp = params.get("VictimIp")
        self._VictimAsset = params.get("VictimAsset")
        self._AttackDirection = params.get("AttackDirection")
        self._TrafficDirection = params.get("TrafficDirection")
        if params.get("SecurityGroupAlertInfos") is not None:
            self._SecurityGroupAlertInfos = []
            for item in params.get("SecurityGroupAlertInfos"):
                obj = SecurityGroupAlertInfo()
                obj._deserialize(item)
                self._SecurityGroupAlertInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupAlertInfo(AbstractModel):
    r"""被归并的原始告警信息

    """

    def __init__(self):
        r"""
        :param _AlarmUuid: 告警Uuid
        :type AlarmUuid: str
        :param _Timestamp: 告警生成时间
        :type Timestamp: str
        """
        self._AlarmUuid = None
        self._Timestamp = None

    @property
    def AlarmUuid(self):
        r"""告警Uuid
        :rtype: str
        """
        return self._AlarmUuid

    @AlarmUuid.setter
    def AlarmUuid(self, AlarmUuid):
        self._AlarmUuid = AlarmUuid

    @property
    def Timestamp(self):
        r"""告警生成时间
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._AlarmUuid = params.get("AlarmUuid")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSearchFilter(AbstractModel):
    r"""web搜索过滤

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段
        :type Name: str
        :param _Values: 值
        :type Values: list of str
        :param _ExactMatch: 是否全匹配
        :type ExactMatch: bool
        """
        self._Name = None
        self._Values = None
        self._ExactMatch = None

    @property
    def Name(self):
        r"""过滤字段
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ExactMatch(self):
        r"""是否全匹配
        :rtype: bool
        """
        return self._ExactMatch

    @ExactMatch.setter
    def ExactMatch(self, ExactMatch):
        self._ExactMatch = ExactMatch


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        