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


class ACLCondition(AbstractModel):
    """精准防护条件

    """

    def __init__(self):
        r"""
        :param MatchFrom: 匹配字段
        :type MatchFrom: str
        :param MatchParam: 匹配字符串
        :type MatchParam: str
        :param Operator: 匹配关系
        :type Operator: str
        :param MatchContent: 匹配内容
        :type MatchContent: str
        """
        self.MatchFrom = None
        self.MatchParam = None
        self.Operator = None
        self.MatchContent = None


    def _deserialize(self, params):
        self.MatchFrom = params.get("MatchFrom")
        self.MatchParam = params.get("MatchParam")
        self.Operator = params.get("Operator")
        self.MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ACLUserRule(AbstractModel):
    """ACL用户规则

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名
        :type RuleName: str
        :param Action: 动作
        :type Action: str
        :param RuleStatus: 状态
        :type RuleStatus: str
        :param Conditions: ACL规则
        :type Conditions: list of ACLCondition
        :param RulePriority: 规则优先级
        :type RulePriority: int
        :param RuleID: 规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param PunishTime: ip封禁的惩罚时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param PunishTimeUnit: ip封禁的惩罚时间单位
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTimeUnit: str
        :param Name: 自定义返回页面的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param PageId: 自定义返回页面的实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: int
        :param RedirectUrl: 重定向时候的地址，必须为本用户接入的站点子域名
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param ResponseCode: 重定向时候的返回码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseCode: int
        """
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.Conditions = None
        self.RulePriority = None
        self.RuleID = None
        self.UpdateTime = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.Name = None
        self.PageId = None
        self.RedirectUrl = None
        self.ResponseCode = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ACLCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.Name = params.get("Name")
        self.PageId = params.get("PageId")
        self.RedirectUrl = params.get("RedirectUrl")
        self.ResponseCode = params.get("ResponseCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclConfig(AbstractModel):
    """ACL配置

    """

    def __init__(self):
        r"""
        :param Switch: 开关
        :type Switch: str
        :param UserRules: ACL用户规则
        :type UserRules: list of ACLUserRule
        """
        self.Switch = None
        self.UserRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("UserRules") is not None:
            self.UserRules = []
            for item in params.get("UserRules"):
                obj = ACLUserRule()
                obj._deserialize(item)
                self.UserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRule(AbstractModel):
    """AI规则引擎防护

    """

    def __init__(self):
        r"""
        :param Mode: smart_status_close-关闭；smart_status_open-拦截处置；
smart_status_observe-观察处置
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        """
        self.Mode = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxy(AbstractModel):
    """应用代理实例

    """

    def __init__(self):
        r"""
        :param ProxyId: 代理ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param ProxyName: 代理名称
当ProxyType=hostname时，表示域名或者子域名
当ProxyType=instance时，表示实例名称
        :type ProxyName: str
        :param PlatType: 调度模式：
ip表示Anycast IP
domain表示CNAME
        :type PlatType: str
        :param SecurityType: 0关闭安全，1开启安全
        :type SecurityType: int
        :param AccelerateType: 0关闭加速，1开启加速
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经移至Rule.ForwardClientIp
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经移至Rule.SessionPersist
        :type SessionPersist: bool
        :param Rule: 规则列表
        :type Rule: list of ApplicationProxyRule
        :param Status: 状态：
online：启用
offline：停用
progress：部署中
stopping：停用中
fail：部署失败/停用失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ScheduleValue: 调度信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduleValue: list of str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ZoneId: 站点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param ZoneName: 站点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param SessionPersistTime: 会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名模式
instance：实例模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyType: str
        :param HostId: 当ProxyType=hostname时：
ProxyName为域名，如：test.123.com
HostId表示该域名，即test.123.com对应的代理加速唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type HostId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxyRule(AbstractModel):
    """应用代理规则

    """

    def __init__(self):
        r"""
        :param Proto: 协议，取值为TCP或者UDP
        :type Proto: str
        :param Port: 端口，支持格式：
80：80端口
81-90：81至90端口
        :type Port: list of str
        :param OriginType: 源站类型，取值：
custom：手动添加
origins：源站组
        :type OriginType: str
        :param OriginValue: 源站信息：
当OriginType=custom时，表示一个或多个源站，如：
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

当OriginType=origins时，包含一个元素，表示源站组ID，如：
OriginValue=["origin-xxx"]
        :type OriginValue: list of str
        :param RuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param Status: 状态：
online：启用
offline：停用
progress：部署中
stopping：停用中
fail：部署失败/停用失败
        :type Status: str
        :param ForwardClientIp: 传递客户端IP，当Proto=TCP时，取值：
TOA：TOA
PPV1: Proxy Protocol传递，协议版本V1
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
当Proto=UDP时，取值：
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持
        :type SessionPersist: bool
        """
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.RuleId = None
        self.Status = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotConfig(AbstractModel):
    """安全Bot配置

    """

    def __init__(self):
        r"""
        :param Switch: bot开关
        :type Switch: str
        :param ManagedRule: 预置规则
        :type ManagedRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param UaBotRule: 保留
        :type UaBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param IspBotRule: 保留
        :type IspBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param PortraitRule: 用户画像规则
        :type PortraitRule: :class:`tencentcloud.teo.v20220106.models.BotPortraitRule`
        :param IntelligenceRule: Bot智能分析
注意：此字段可能返回 null，表示取不到有效值。
        :type IntelligenceRule: :class:`tencentcloud.teo.v20220106.models.IntelligenceRule`
        """
        self.Switch = None
        self.ManagedRule = None
        self.UaBotRule = None
        self.IspBotRule = None
        self.PortraitRule = None
        self.IntelligenceRule = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("ManagedRule") is not None:
            self.ManagedRule = BotManagedRule()
            self.ManagedRule._deserialize(params.get("ManagedRule"))
        if params.get("UaBotRule") is not None:
            self.UaBotRule = BotManagedRule()
            self.UaBotRule._deserialize(params.get("UaBotRule"))
        if params.get("IspBotRule") is not None:
            self.IspBotRule = BotManagedRule()
            self.IspBotRule._deserialize(params.get("IspBotRule"))
        if params.get("PortraitRule") is not None:
            self.PortraitRule = BotPortraitRule()
            self.PortraitRule._deserialize(params.get("PortraitRule"))
        if params.get("IntelligenceRule") is not None:
            self.IntelligenceRule = IntelligenceRule()
            self.IntelligenceRule._deserialize(params.get("IntelligenceRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotLog(AbstractModel):
    """Bot攻击日志

    """

    def __init__(self):
        r"""
        :param AttackTime: 攻击时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackTime: int
        :param AttackIp: 攻击ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackIp: str
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param RequestUri: 请求uri
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestUri: str
        :param AttackType: 攻击类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackType: str
        :param RequestMethod: 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestMethod: str
        :param AttackContent: 攻击内容
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackContent: str
        :param RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param RuleId: 规则编号
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param SipCountryCode: IP所在国家
注意：此字段可能返回 null，表示取不到有效值。
        :type SipCountryCode: str
        :param EventId: 事件id
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param DisposalMethod: 处置方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalMethod: str
        :param HttpLog: http_log
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpLog: str
        :param Ua: user agent
注意：此字段可能返回 null，表示取不到有效值。
        :type Ua: str
        :param DetectionMethod: 检出方法
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionMethod: str
        :param Confidence: 置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: str
        :param Maliciousness: 恶意度
注意：此字段可能返回 null，表示取不到有效值。
        :type Maliciousness: str
        """
        self.AttackTime = None
        self.AttackIp = None
        self.Domain = None
        self.RequestUri = None
        self.AttackType = None
        self.RequestMethod = None
        self.AttackContent = None
        self.RiskLevel = None
        self.RuleId = None
        self.SipCountryCode = None
        self.EventId = None
        self.DisposalMethod = None
        self.HttpLog = None
        self.Ua = None
        self.DetectionMethod = None
        self.Confidence = None
        self.Maliciousness = None


    def _deserialize(self, params):
        self.AttackTime = params.get("AttackTime")
        self.AttackIp = params.get("AttackIp")
        self.Domain = params.get("Domain")
        self.RequestUri = params.get("RequestUri")
        self.AttackType = params.get("AttackType")
        self.RequestMethod = params.get("RequestMethod")
        self.AttackContent = params.get("AttackContent")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleId = params.get("RuleId")
        self.SipCountryCode = params.get("SipCountryCode")
        self.EventId = params.get("EventId")
        self.DisposalMethod = params.get("DisposalMethod")
        self.HttpLog = params.get("HttpLog")
        self.Ua = params.get("Ua")
        self.DetectionMethod = params.get("DetectionMethod")
        self.Confidence = params.get("Confidence")
        self.Maliciousness = params.get("Maliciousness")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotLogData(AbstractModel):
    """限速拦截日志

    """

    def __init__(self):
        r"""
        :param List: Bot攻击日志数据集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of BotLog
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BotLog()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRule(AbstractModel):
    """Bot 规则

    """

    def __init__(self):
        r"""
        :param ManagedIds: 想开启的规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagedIds: list of int
        :param RuleID: 本规则的id
        :type RuleID: int
        :param Action: drop/trans/monitor/alg
        :type Action: str
        :param PunishTime: ip封禁的惩罚时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param PunishTimeUnit: 单位
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTimeUnit: str
        :param Name: 自定义返回页面的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param PageId: 自定义返回页面的实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: int
        :param RedirectUrl: 重定向时候的地址，必须为本用户接入的站点子域名，使用URLENCODE
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param ResponseCode: 重定向时候的返回码
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseCode: int
        :param TransManagedIds: 放行的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TransManagedIds: list of int
        :param AlgManagedIds: JS挑战的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param CapManagedIds: 数字验证码的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param MonManagedIds: 观察的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param DropManagedIds: 拦截的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        """
        self.ManagedIds = None
        self.RuleID = None
        self.Action = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.Name = None
        self.PageId = None
        self.RedirectUrl = None
        self.ResponseCode = None
        self.TransManagedIds = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None


    def _deserialize(self, params):
        self.ManagedIds = params.get("ManagedIds")
        self.RuleID = params.get("RuleID")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.Name = params.get("Name")
        self.PageId = params.get("PageId")
        self.RedirectUrl = params.get("RedirectUrl")
        self.ResponseCode = params.get("ResponseCode")
        self.TransManagedIds = params.get("TransManagedIds")
        self.AlgManagedIds = params.get("AlgManagedIds")
        self.CapManagedIds = params.get("CapManagedIds")
        self.MonManagedIds = params.get("MonManagedIds")
        self.DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRuleDetail(AbstractModel):
    """bot托管规则详情

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: int
        :param Description: 规则描述
        :type Description: str
        :param RuleTypeName: 规则分类
        :type RuleTypeName: str
        :param Status: 该规则开启/关闭
        :type Status: str
        """
        self.RuleId = None
        self.Description = None
        self.RuleTypeName = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotPortraitRule(AbstractModel):
    """bot 用户画像规则

    """

    def __init__(self):
        r"""
        :param RuleID: 本规则的id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param AlgManagedIds: JS挑战的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param CapManagedIds: 数字验证码的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param MonManagedIds: 观察的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param DropManagedIds: 拦截的规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        :param Switch: 本功能的开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.RuleID = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None
        self.Switch = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.AlgManagedIds = params.get("AlgManagedIds")
        self.CapManagedIds = params.get("CapManagedIds")
        self.MonManagedIds = params.get("MonManagedIds")
        self.DropManagedIds = params.get("DropManagedIds")
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCInterceptEvent(AbstractModel):
    """CC拦截事件

    """

    def __init__(self):
        r"""
        :param ClientIp: 客户端ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIp: str
        :param InterceptNum: 拦截次数/min
注意：此字段可能返回 null，表示取不到有效值。
        :type InterceptNum: int
        :param InterceptTime: 速拦截时间，分钟时间/min,单位为s
        :type InterceptTime: int
        """
        self.ClientIp = None
        self.InterceptNum = None
        self.InterceptTime = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.InterceptNum = params.get("InterceptNum")
        self.InterceptTime = params.get("InterceptTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCInterceptEventData(AbstractModel):
    """CC拦截事件数据

    """

    def __init__(self):
        r"""
        :param List: 攻击事件数据集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of CCInterceptEvent
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = CCInterceptEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLog(AbstractModel):
    """限速拦截日志

    """

    def __init__(self):
        r"""
        :param AttackTime: 攻击时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackTime: int
        :param AttackSip: 攻击源ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackSip: str
        :param AttackDomain: 攻击域名
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackDomain: str
        :param RequestUri: 请求uri
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestUri: str
        :param HitCount: 命中次数
注意：此字段可能返回 null，表示取不到有效值。
        :type HitCount: int
        :param SipCountryCode: IP所在国家
注意：此字段可能返回 null，表示取不到有效值。
        :type SipCountryCode: str
        :param EventId: 事件id
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param DisposalMethod: 处置方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalMethod: str
        :param HttpLog: http_log
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpLog: str
        :param RuleId: 规则编号
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        """
        self.AttackTime = None
        self.AttackSip = None
        self.AttackDomain = None
        self.RequestUri = None
        self.HitCount = None
        self.SipCountryCode = None
        self.EventId = None
        self.DisposalMethod = None
        self.HttpLog = None
        self.RuleId = None
        self.RiskLevel = None


    def _deserialize(self, params):
        self.AttackTime = params.get("AttackTime")
        self.AttackSip = params.get("AttackSip")
        self.AttackDomain = params.get("AttackDomain")
        self.RequestUri = params.get("RequestUri")
        self.HitCount = params.get("HitCount")
        self.SipCountryCode = params.get("SipCountryCode")
        self.EventId = params.get("EventId")
        self.DisposalMethod = params.get("DisposalMethod")
        self.HttpLog = params.get("HttpLog")
        self.RuleId = params.get("RuleId")
        self.RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLogData(AbstractModel):
    """限速拦截日志

    """

    def __init__(self):
        r"""
        :param List: CC拦截日志数据集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of CCLog
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = CCLog()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """缓存规则配置。

    """

    def __init__(self):
        r"""
        :param Cache: 缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfigCache`
        :param NoCache: 不缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCache: :class:`tencentcloud.teo.v20220106.models.CacheConfigNoCache`
        :param FollowOrigin: 遵循源站配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: :class:`tencentcloud.teo.v20220106.models.CacheConfigFollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfigCache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = CacheConfigNoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = CacheConfigFollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """缓存时间设置

    """

    def __init__(self):
        r"""
        :param Switch: 缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        :param IgnoreCacheControl: 是否开启强制缓存
开启：on
关闭：off
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        """
        self.Switch = None
        self.CacheTime = None
        self.IgnoreCacheControl = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CacheTime = params.get("CacheTime")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigFollowOrigin(AbstractModel):
    """缓存遵循源站配置

    """

    def __init__(self):
        r"""
        :param Switch: 遵循源站配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigNoCache(AbstractModel):
    """不缓存配置

    """

    def __init__(self):
        r"""
        :param Switch: 不缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """缓存键配置

    """

    def __init__(self):
        r"""
        :param FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数忽略）
off：关闭全路径缓存（即开启参数忽略）
注意：此字段可能返回 null，表示取不到有效值。
        :type FullUrlCache: str
        :param IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.teo.v20220106.models.QueryString`
        """
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = QueryString()
            self.QueryString._deserialize(params.get("QueryString"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CachePrefresh(AbstractModel):
    """缓存预刷新

    """

    def __init__(self):
        r"""
        :param Switch: 缓存预刷新配置开关
        :type Switch: str
        :param Percent: 缓存预刷新百分比：1-99
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        """
        self.Switch = None
        self.Percent = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertFilter(AbstractModel):
    """证书查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名，支持的列表如下:
 - host：域名。
 - certId: 证书ID
 - certAlias: 证书备用名
 - certType: default: 默认证书, upload: 上传证书, managed:腾讯云证书
        :type Name: str
        :param Values: 过滤字段值
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名host。
模糊查询时，Value长度最大为1。
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertSort(AbstractModel):
    """查询结果排序条件。

    """

    def __init__(self):
        r"""
        :param Key: 排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
certDeployTime,  证书部署时间
        :type Key: str
        :param Sequence: asc/desc，默认desc。
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateRequest(AbstractModel):
    """CheckCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Certificate: 证书
        :type Certificate: str
        :param PrivateKey: 私钥
        :type PrivateKey: str
        """
        self.Certificate = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateResponse(AbstractModel):
    """CheckCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClientIp(AbstractModel):
    """客户端IP头部

    """

    def __init__(self):
        r"""
        :param Switch: 客户端IP头部配置开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param HeaderName: 回源客户端IP请求头名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderName: str
        """
        self.Switch = None
        self.HeaderName = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CnameStatus(AbstractModel):
    """CNAME 状态

    """

    def __init__(self):
        r"""
        :param Name: 记录名称
        :type Name: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Status: 状态
生效：active
不生效：moved
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.Name = None
        self.Cname = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """智能压缩配置

    """

    def __init__(self):
        r"""
        :param Switch: 智能压缩配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param ProxyName: 代理名称
当ProxyType=hostname时，表示域名或者子域名
当ProxyType=instance时，表示实例名称
        :type ProxyName: str
        :param PlatType: 调度模式：
ip表示Anycast IP
domain表示CNAME
        :type PlatType: str
        :param SecurityType: 0关闭安全，1开启安全
        :type SecurityType: int
        :param AccelerateType: 0关闭加速，1开启加速
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经移至Rule.ForwardClientIp
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经移至Rule.SessionPersist
        :type SessionPersist: bool
        :param Rule: 规则详细信息
        :type Rule: list of ApplicationProxyRule
        :param SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名模式
instance：实例模式
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyResponse(AbstractModel):
    """CreateApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 新增的四层代理应用ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRuleRequest(AbstractModel):
    """CreateApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param Proto: 协议，取值为TCP或者UDP
        :type Proto: str
        :param Port: 端口，支持格式：
80：80端口
81-90：81至90端口
        :type Port: list of str
        :param OriginType: 源站类型，取值：
custom：手动添加
origins：源站组
        :type OriginType: str
        :param OriginValue: 源站信息：
当OriginType=custom时，表示多个：
IP:端口
域名:端口
当OriginType=origins时，包含一个元素，表示源站组ID
        :type OriginValue: list of str
        :param ForwardClientIp: 传递客户端IP，当Proto=TCP时，取值：
TOA：TOA
PPV1: Proxy Protocol传递，协议版本V1
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
当Proto=UDP时，取值：
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRuleResponse(AbstractModel):
    """CreateApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRulesRequest(AbstractModel):
    """CreateApplicationProxyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param Rule: 规则列表
        :type Rule: list of ApplicationProxyRule
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Rule = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRulesResponse(AbstractModel):
    """CreateApplicationProxyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 新增的规则ID数组
        :type RuleId: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateCustomErrorPageRequest(AbstractModel):
    """CreateCustomErrorPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: zone的id
        :type ZoneId: str
        :param Entity: 具体所属实体
        :type Entity: str
        :param Name: 自定义页面的文件名
        :type Name: str
        :param Content: 自定义页面的内容
        :type Content: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Name = None
        self.Content = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomErrorPageResponse(AbstractModel):
    """CreateCustomErrorPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param PageId: 自定义页面上传后的唯一id
        :type PageId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageId = params.get("PageId")
        self.RequestId = params.get("RequestId")


class CreateDnsRecordRequest(AbstractModel):
    """CreateDnsRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Mode: 代理模式，可选值：dns_only, cdn_only, secure_cdn
        :type Mode: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        """
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
        self.Priority = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDnsRecordResponse(AbstractModel):
    """CreateDnsRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名称
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        :param Mode: 代理模式
        :type Mode: str
        :param Status: 解析状态
active: 生效
pending: 不生效
        :type Status: str
        :param Locked: 已锁定
        :type Locked: bool
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancingRequest(AbstractModel):
    """CreateLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Host: 子域名
        :type Host: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        """
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancingResponse(AbstractModel):
    """CreateLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class CreateOriginGroupRequest(AbstractModel):
    """CreateOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param OriginName: 源站组名称
        :type OriginName: str
        :param Type: 配置类型，当OriginType=self 时，需要填写：
area: 按区域配置
weight: 按权重配置
当OriginType=third_party/cos 时，不需要填写
        :type Type: str
        :param Record: 源站记录
        :type Record: list of OriginRecord
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param OriginType: 源站类型
self：自有源站
third_party：第三方源站
cos：腾讯云COS源站
        :type OriginType: str
        """
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.ZoneId = None
        self.OriginType = None


    def _deserialize(self, params):
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.ZoneId = params.get("ZoneId")
        self.OriginType = params.get("OriginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOriginGroupResponse(AbstractModel):
    """CreateOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginId: 新增的源站组ID
        :type OriginId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Targets: 要预热的资源列表，每个元素格式类似如下:
http://www.example.com/example.txt
        :type Targets: list of str
        :param EncodeUrl: 是否对url进行encode
若内容含有非 ASCII 字符集的字符，请开启此开关，编码转换（编码规则遵循 RFC3986）
        :type EncodeUrl: bool
        :param Headers: 附带的http头部信息
        :type Headers: list of Header
        """
        self.ZoneId = None
        self.Targets = None
        self.EncodeUrl = None
        self.Headers = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param FailedList: 失败的任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Type: 类型，当前支持的类型：
- purge_url：URL
- purge_prefix：前缀
- purge_host：Hostname
- purge_all：全部缓存
        :type Type: str
        :param Targets: 要刷新的资源列表，每个元素格式依据Type而定
1) Type = purge_host 时
形如：www.example.com 或 foo.bar.example.com
2) Type = purge_prefix 时
形如：http://www.example.com/example
3) Type = purge_url 时
形如：https://www.example.com/example.jpg
4）Type = purge_all 时
Targets可为空，不需要填写
        :type Targets: list of str
        :param EncodeUrl: 若有编码转换，仅清除编码转换后匹配的资源
若内容含有非 ASCII 字符集的字符，请开启此开关，编码转换（编码规则遵循 RFC3986）
        :type EncodeUrl: bool
        """
        self.ZoneId = None
        self.Type = None
        self.Targets = None
        self.EncodeUrl = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Targets = params.get("Targets")
        self.EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param FailedList: 失败的任务列表及原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.FailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self.FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self.FailedList.append(obj)
        self.RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名字
        :type Name: str
        :param Type: 接入方式，默认full
- full NS接入
- partial CNAME接入
        :type Type: str
        :param JumpStart: 是否跳过站点历史解析记录扫描
        :type JumpStart: bool
        :param Tags: 资源标签
        :type Tags: list of Tag
        """
        self.Name = None
        self.Type = None
        self.JumpStart = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.JumpStart = params.get("JumpStart")
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
        


class CreateZoneResponse(AbstractModel):
    """CreateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Type: 站点接入方式
        :type Type: str
        :param Status: 站点状态
- pending 未切换NS
- active NS 已切换到分配的 NS
- moved NS 从腾讯云切走
        :type Status: str
        :param OriginalNameServers: 当前使用的 NS 列表
        :type OriginalNameServers: list of str
        :param NameServers: 给用户分配的 NS 列表
        :type NameServers: list of str
        :param CreatedOn: 站点创建时间
        :type CreatedOn: str
        :param ModifiedOn: 站点更新时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.Status = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DDoSAcl(AbstractModel):
    """DDoS配置端口过滤

    """

    def __init__(self):
        r"""
        :param DportEnd: 目的端口end
        :type DportEnd: int
        :param DportStart: 目的端口start
        :type DportStart: int
        :param SportEnd: 源端口end
        :type SportEnd: int
        :param SportStart: 源端口start
        :type SportStart: int
        :param Protocol: 协议 'tcp', 'udp', 'all'
        :type Protocol: str
        :param Action: 动作  drop-丢弃,；transmit-放行； forward-继续防护
        :type Action: str
        :param Default: 是否为系统配置 0-人工配置；1-系统配置
        :type Default: int
        """
        self.DportEnd = None
        self.DportStart = None
        self.SportEnd = None
        self.SportStart = None
        self.Protocol = None
        self.Action = None
        self.Default = None


    def _deserialize(self, params):
        self.DportEnd = params.get("DportEnd")
        self.DportStart = params.get("DportStart")
        self.SportEnd = params.get("SportEnd")
        self.SportStart = params.get("SportStart")
        self.Protocol = params.get("Protocol")
        self.Action = params.get("Action")
        self.Default = params.get("Default")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAntiPly(AbstractModel):
    """DDoS协议防护+连接防护

    """

    def __init__(self):
        r"""
        :param DropTcp: tcp协议封禁 on-开；off-关
        :type DropTcp: str
        :param DropUdp: udp协议封禁 on-开；off-关
        :type DropUdp: str
        :param DropIcmp: icmp协议封禁 on-开；off-关
        :type DropIcmp: str
        :param DropOther: 其他协议封禁 on-开；off-关
        :type DropOther: str
        :param SourceCreateLimit: 源每秒新建数限制  0-4294967295
        :type SourceCreateLimit: int
        :param SourceConnectLimit: 源并发连接控制 0-4294967295
        :type SourceConnectLimit: int
        :param DestinationCreateLimit: 目的每秒新建数限制 0-4294967295
        :type DestinationCreateLimit: int
        :param DestinationConnectLimit: 目的端口的并发连接控制 0-4294967295
        :type DestinationConnectLimit: int
        :param AbnormalConnectNum: 异常连接数阈值  0-4294967295
        :type AbnormalConnectNum: int
        :param AbnormalSynRatio: syn占比异常阈值 0-100
        :type AbnormalSynRatio: int
        :param AbnormalSynNum: syn个数异常阈值 0-65535
        :type AbnormalSynNum: int
        :param ConnectTimeout: 连接超时检测 0-65535
        :type ConnectTimeout: int
        :param EmptyConnectProtect: 空连接防护开启 0-1
        :type EmptyConnectProtect: str
        :param UdpShard: UDP分片开关；off-关闭，on-开启
注意：此字段可能返回 null，表示取不到有效值。
        :type UdpShard: str
        """
        self.DropTcp = None
        self.DropUdp = None
        self.DropIcmp = None
        self.DropOther = None
        self.SourceCreateLimit = None
        self.SourceConnectLimit = None
        self.DestinationCreateLimit = None
        self.DestinationConnectLimit = None
        self.AbnormalConnectNum = None
        self.AbnormalSynRatio = None
        self.AbnormalSynNum = None
        self.ConnectTimeout = None
        self.EmptyConnectProtect = None
        self.UdpShard = None


    def _deserialize(self, params):
        self.DropTcp = params.get("DropTcp")
        self.DropUdp = params.get("DropUdp")
        self.DropIcmp = params.get("DropIcmp")
        self.DropOther = params.get("DropOther")
        self.SourceCreateLimit = params.get("SourceCreateLimit")
        self.SourceConnectLimit = params.get("SourceConnectLimit")
        self.DestinationCreateLimit = params.get("DestinationCreateLimit")
        self.DestinationConnectLimit = params.get("DestinationConnectLimit")
        self.AbnormalConnectNum = params.get("AbnormalConnectNum")
        self.AbnormalSynRatio = params.get("AbnormalSynRatio")
        self.AbnormalSynNum = params.get("AbnormalSynNum")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.EmptyConnectProtect = params.get("EmptyConnectProtect")
        self.UdpShard = params.get("UdpShard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSApplication(AbstractModel):
    """DDoS7层应用

    """

    def __init__(self):
        r"""
        :param Host: 二级域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param Status: 域名状态；
init  待切ns
offline 需要dns开启站点加速
process 在部署中，稍等一会
online 正常状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param AccelerateType: 加速开关；on-开启加速；off-关闭加速（AccelerateType：on，SecurityType：on，安全加速，未开防护增强；AccelerateType：off，SecurityType：on，安全加速，开启防护增强；AccelerateType：on，SecurityType：off，内容加速，未开防护增强）
注意：此字段可能返回 null，表示取不到有效值。
        :type AccelerateType: str
        :param SecurityType: 安全开关；on-开启安全；off-关闭安全（AccelerateType：on，SecurityType：on，安全加速，未开防护增强；AccelerateType：off，SecurityType：on，安全加速，开启防护增强；AccelerateType：on，SecurityType：off，内容加速，未开防护增强）
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityType: str
        """
        self.Host = None
        self.Status = None
        self.AccelerateType = None
        self.SecurityType = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Status = params.get("Status")
        self.AccelerateType = params.get("AccelerateType")
        self.SecurityType = params.get("SecurityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSConfig(AbstractModel):
    """DDoS配置

    """

    def __init__(self):
        r"""
        :param Switch: 开关
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSFeaturesFilter(AbstractModel):
    """DDoS特征过滤

    """

    def __init__(self):
        r"""
        :param Action: 动作 drop-丢弃；transmit-放行；drop_block-丢弃并拉黑；forward-继续防护
        :type Action: str
        :param Depth: 深度值1
        :type Depth: int
        :param Depth2: 深度值2
        :type Depth2: int
        :param DportEnd: 目标端口结束
        :type DportEnd: int
        :param DportStart: 目标端口开始
        :type DportStart: int
        :param IsNot: 取非判断1
        :type IsNot: int
        :param IsNot2: 取非判断2
        :type IsNot2: int
        :param MatchLogic: 多特征关系（单特征时(none)，第二特征相关配置可不填） none；and；or
        :type MatchLogic: str
        :param MatchType: 匹配方式1 pcre-正则匹配, sunday-字符串匹配
        :type MatchType: str
        :param MatchType2: 匹配方式2 pcre-正则匹配, sunday-字符串匹配
        :type MatchType2: str
        :param Offset: 偏移量1
        :type Offset: int
        :param Offset2: 偏移量2
        :type Offset2: int
        :param PacketMax: 最大包长
        :type PacketMax: int
        :param PacketMin: 最小包长
        :type PacketMin: int
        :param Protocol: 协议 tcp；udp；icmp；all
        :type Protocol: str
        :param SportEnd: 源端口结束
        :type SportEnd: int
        :param SportStart: 源端口开始
        :type SportStart: int
        :param Str: 匹配字符串1
        :type Str: str
        :param Str2: 匹配字符串2
        :type Str2: str
        :param MatchBegin: 匹配开始层级，层级参考计算机网络结构 begin_l5, no_match, begin_l3, begin_l4
        :type MatchBegin: str
        :param MatchBegin2: 匹配开始层级，层级参考计算机网络结构 begin_l5, no_match, begin_l3, begin_l4
        :type MatchBegin2: str
        """
        self.Action = None
        self.Depth = None
        self.Depth2 = None
        self.DportEnd = None
        self.DportStart = None
        self.IsNot = None
        self.IsNot2 = None
        self.MatchLogic = None
        self.MatchType = None
        self.MatchType2 = None
        self.Offset = None
        self.Offset2 = None
        self.PacketMax = None
        self.PacketMin = None
        self.Protocol = None
        self.SportEnd = None
        self.SportStart = None
        self.Str = None
        self.Str2 = None
        self.MatchBegin = None
        self.MatchBegin2 = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Depth = params.get("Depth")
        self.Depth2 = params.get("Depth2")
        self.DportEnd = params.get("DportEnd")
        self.DportStart = params.get("DportStart")
        self.IsNot = params.get("IsNot")
        self.IsNot2 = params.get("IsNot2")
        self.MatchLogic = params.get("MatchLogic")
        self.MatchType = params.get("MatchType")
        self.MatchType2 = params.get("MatchType2")
        self.Offset = params.get("Offset")
        self.Offset2 = params.get("Offset2")
        self.PacketMax = params.get("PacketMax")
        self.PacketMin = params.get("PacketMin")
        self.Protocol = params.get("Protocol")
        self.SportEnd = params.get("SportEnd")
        self.SportStart = params.get("SportStart")
        self.Str = params.get("Str")
        self.Str2 = params.get("Str2")
        self.MatchBegin = params.get("MatchBegin")
        self.MatchBegin2 = params.get("MatchBegin2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIp(AbstractModel):
    """DDoS地域封禁

    """

    def __init__(self):
        r"""
        :param RegionId: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: list of int
        :param Switch: 区域封禁清空标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.RegionId = None
        self.Switch = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSStatusInfo(AbstractModel):
    """DDoS封禁等级

    """

    def __init__(self):
        r"""
        :param AiStatus: 不支持，填off
        :type AiStatus: str
        :param Appid: 用户appid
        :type Appid: str
        :param PlyLevel: 策略等级 low, middle, high
        :type PlyLevel: str
        """
        self.AiStatus = None
        self.Appid = None
        self.PlyLevel = None


    def _deserialize(self, params):
        self.AiStatus = params.get("AiStatus")
        self.Appid = params.get("Appid")
        self.PlyLevel = params.get("PlyLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSUserAllowBlockIP(AbstractModel):
    """DDoS黑白名单

    """

    def __init__(self):
        r"""
        :param Ip: 用户ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Mask: 掩码
注意：此字段可能返回 null，表示取不到有效值。
        :type Mask: int
        :param Type: 类型 block-丢弃；allow-允许
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param UpdateTime: 时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param Ip2: 用户ip范围截止
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip2: str
        :param Mask2: 掩码截止范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Mask2: int
        """
        self.Ip = None
        self.Mask = None
        self.Type = None
        self.UpdateTime = None
        self.Ip2 = None
        self.Mask2 = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Mask = params.get("Mask")
        self.Type = params.get("Type")
        self.UpdateTime = params.get("UpdateTime")
        self.Ip2 = params.get("Ip2")
        self.Mask2 = params.get("Mask2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEvent(AbstractModel):
    """DDos攻击事件对象

    """

    def __init__(self):
        r"""
        :param PolicyId: ddos 策略组id
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param AttackType: 攻击类型(对应交互事件名称)
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackType: str
        :param AttackStatus: 攻击状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackStatus: int
        :param AttackMaxBandWidth: 攻击最大带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackMaxBandWidth: int
        :param AttackPacketMaxRate: 攻击包速率峰值
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackPacketMaxRate: int
        :param AttackStartTime: 攻击开始时间 单位为s
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackStartTime: int
        :param AttackEndTime: 攻击结束时间 单位为s
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackEndTime: int
        :param EventId: 事件ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param ZoneId: 站点id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        """
        self.PolicyId = None
        self.AttackType = None
        self.AttackStatus = None
        self.AttackMaxBandWidth = None
        self.AttackPacketMaxRate = None
        self.AttackStartTime = None
        self.AttackEndTime = None
        self.EventId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttackType = params.get("AttackType")
        self.AttackStatus = params.get("AttackStatus")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self.AttackStartTime = params.get("AttackStartTime")
        self.AttackEndTime = params.get("AttackEndTime")
        self.EventId = params.get("EventId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEventData(AbstractModel):
    """DDos攻击事件数据

    """

    def __init__(self):
        r"""
        :param List: 攻击事件数据集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DDosAttackEvent
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DDosAttackEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackEventDetailData(AbstractModel):
    """ddos 攻击事件的详情

    """

    def __init__(self):
        r"""
        :param AttackStatus: 攻击状态
        :type AttackStatus: int
        :param AttackType: 攻击类型
        :type AttackType: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param StartTime: 开始时间
        :type StartTime: int
        :param MaxBandWidth: 最大带宽
        :type MaxBandWidth: int
        :param PacketMaxRate: 最大包速率
        :type PacketMaxRate: int
        :param EventId: 事件Id
        :type EventId: str
        :param PolicyId: ddos 策略组id
        :type PolicyId: int
        """
        self.AttackStatus = None
        self.AttackType = None
        self.EndTime = None
        self.StartTime = None
        self.MaxBandWidth = None
        self.PacketMaxRate = None
        self.EventId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.AttackStatus = params.get("AttackStatus")
        self.AttackType = params.get("AttackType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.MaxBandWidth = params.get("MaxBandWidth")
        self.PacketMaxRate = params.get("PacketMaxRate")
        self.EventId = params.get("EventId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackSourceEvent(AbstractModel):
    """DDos攻击事件对象

    """

    def __init__(self):
        r"""
        :param AttackSourceIp: 攻击源ip
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackSourceIp: str
        :param AttackRegion: 地区(国家)
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackRegion: str
        :param AttackFlow: 累计攻击流量
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackFlow: int
        :param AttackPacketNum: 累计攻击包量
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackPacketNum: int
        """
        self.AttackSourceIp = None
        self.AttackRegion = None
        self.AttackFlow = None
        self.AttackPacketNum = None


    def _deserialize(self, params):
        self.AttackSourceIp = params.get("AttackSourceIp")
        self.AttackRegion = params.get("AttackRegion")
        self.AttackFlow = params.get("AttackFlow")
        self.AttackPacketNum = params.get("AttackPacketNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosAttackSourceEventData(AbstractModel):
    """DDos攻击源数据

    """

    def __init__(self):
        r"""
        :param List: DDos攻击源数据集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DDosAttackSourceEvent
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DDosAttackSourceEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosMajorAttackEvent(AbstractModel):
    """DDos主攻击事件

    """

    def __init__(self):
        r"""
        :param PolicyId: ddos 策略组id
        :type PolicyId: int
        :param AttackMaxBandWidth: 攻击最大带宽
        :type AttackMaxBandWidth: int
        :param AttackTime: 攻击时间 单位为s
        :type AttackTime: int
        """
        self.PolicyId = None
        self.AttackMaxBandWidth = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosMajorAttackEventData(AbstractModel):
    """主攻击对象Data

    """

    def __init__(self):
        r"""
        :param List: DDosMajorAttackEvent ddos 攻击事件
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DDosMajorAttackEvent
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DDosMajorAttackEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataItem(AbstractModel):
    """统计曲线数据项

    """

    def __init__(self):
        r"""
        :param Time: 时间
        :type Time: str
        :param Value: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosAcls(AbstractModel):
    """ddos端口过滤

    """

    def __init__(self):
        r"""
        :param Switch: 开关 off清空规则标识
        :type Switch: str
        :param Acl: 端口过了详细参数
        :type Acl: list of DDoSAcl
        """
        self.Switch = None
        self.Acl = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Acl") is not None:
            self.Acl = []
            for item in params.get("Acl"):
                obj = DDoSAcl()
                obj._deserialize(item)
                self.Acl.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosAllowBlock(AbstractModel):
    """ddos黑白名单

    """

    def __init__(self):
        r"""
        :param Switch: 开关标识防护是否清空
        :type Switch: str
        :param UserAllowBlockIp: 黑白名单数组
        :type UserAllowBlockIp: list of DDoSUserAllowBlockIP
        """
        self.Switch = None
        self.UserAllowBlockIp = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("UserAllowBlockIp") is not None:
            self.UserAllowBlockIp = []
            for item in params.get("UserAllowBlockIp"):
                obj = DDoSUserAllowBlockIP()
                obj._deserialize(item)
                self.UserAllowBlockIp.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosPacketFilter(AbstractModel):
    """ddos特征过滤

    """

    def __init__(self):
        r"""
        :param Switch: 特征过滤清空标识，off清空处理
        :type Switch: str
        :param PacketFilter: 特征过滤数组
        :type PacketFilter: list of DDoSFeaturesFilter
        """
        self.Switch = None
        self.PacketFilter = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PacketFilter") is not None:
            self.PacketFilter = []
            for item in params.get("PacketFilter"):
                obj = DDoSFeaturesFilter()
                obj._deserialize(item)
                self.PacketFilter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosRule(AbstractModel):
    """Ddos防护配置

    """

    def __init__(self):
        r"""
        :param DdosStatusInfo: DDoS防护等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosStatusInfo: :class:`tencentcloud.teo.v20220106.models.DDoSStatusInfo`
        :param DdosGeoIp: DDoS地域封禁
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosGeoIp: :class:`tencentcloud.teo.v20220106.models.DDoSGeoIp`
        :param DdosAllowBlock: DDoS黑白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosAllowBlock: :class:`tencentcloud.teo.v20220106.models.DdosAllowBlock`
        :param DdosAntiPly: DDoS 协议封禁+连接防护
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosAntiPly: :class:`tencentcloud.teo.v20220106.models.DDoSAntiPly`
        :param DdosPacketFilter: DDoS特征过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosPacketFilter: :class:`tencentcloud.teo.v20220106.models.DdosPacketFilter`
        :param DdosAcl: DDoS端口过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosAcl: :class:`tencentcloud.teo.v20220106.models.DdosAcls`
        :param Switch: DDoS开关 on-开启；off-关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param UdpShardOpen: UDP分片功能是否支持，off-不支持，on-支持
注意：此字段可能返回 null，表示取不到有效值。
        :type UdpShardOpen: str
        """
        self.DdosStatusInfo = None
        self.DdosGeoIp = None
        self.DdosAllowBlock = None
        self.DdosAntiPly = None
        self.DdosPacketFilter = None
        self.DdosAcl = None
        self.Switch = None
        self.UdpShardOpen = None


    def _deserialize(self, params):
        if params.get("DdosStatusInfo") is not None:
            self.DdosStatusInfo = DDoSStatusInfo()
            self.DdosStatusInfo._deserialize(params.get("DdosStatusInfo"))
        if params.get("DdosGeoIp") is not None:
            self.DdosGeoIp = DDoSGeoIp()
            self.DdosGeoIp._deserialize(params.get("DdosGeoIp"))
        if params.get("DdosAllowBlock") is not None:
            self.DdosAllowBlock = DdosAllowBlock()
            self.DdosAllowBlock._deserialize(params.get("DdosAllowBlock"))
        if params.get("DdosAntiPly") is not None:
            self.DdosAntiPly = DDoSAntiPly()
            self.DdosAntiPly._deserialize(params.get("DdosAntiPly"))
        if params.get("DdosPacketFilter") is not None:
            self.DdosPacketFilter = DdosPacketFilter()
            self.DdosPacketFilter._deserialize(params.get("DdosPacketFilter"))
        if params.get("DdosAcl") is not None:
            self.DdosAcl = DdosAcls()
            self.DdosAcl._deserialize(params.get("DdosAcl"))
        self.Switch = params.get("Switch")
        self.UdpShardOpen = params.get("UdpShardOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultServerCertInfo(AbstractModel):
    """https 服务端证书配置

    """

    def __init__(self):
        r"""
        :param CertId: 服务器证书 ID, 默认证书ID, 或在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Alias: 证书备注名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Type: 证书类型:
default: 默认证书
upload:用户上传
managed:腾讯云托管
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ExpireTime: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param EffectiveTime: 证书生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectiveTime: str
        :param CommonName: 证书公用名
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        :param SubjectAltName: 证书SAN域名
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param Status: 证书状态:
applying: 证书申请中
failed: 证书(申请)失败
processing: 证书部署中
deployed: 证书已部署
disabled: 证书被禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Message: Status为失败时,此字段返回失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.EffectiveTime = None
        self.CommonName = None
        self.SubjectAltName = None
        self.Status = None
        self.Message = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.EffectiveTime = params.get("EffectiveTime")
        self.CommonName = params.get("CommonName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        """
        self.ZoneId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyResponse(AbstractModel):
    """DeleteApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RuleId: 规则ID
        :type RuleId: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRuleResponse(AbstractModel):
    """DeleteApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class DeleteDnsRecordsRequest(AbstractModel):
    """DeleteDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Ids: 记录 ID
        :type Ids: list of str
        """
        self.ZoneId = None
        self.Ids = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDnsRecordsResponse(AbstractModel):
    """DeleteDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 记录 ID
        :type Ids: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancingRequest(AbstractModel):
    """DeleteLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancingResponse(AbstractModel):
    """DeleteLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class DeleteOriginGroupRequest(AbstractModel):
    """DeleteOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        """
        self.OriginId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOriginGroupResponse(AbstractModel):
    """DeleteOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyDetailRequest(AbstractModel):
    """DescribeApplicationProxyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 实例ID
        :type ProxyId: str
        """
        self.ZoneId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyDetailResponse(AbstractModel):
    """DescribeApplicationProxyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 实例ID
        :type ProxyId: str
        :param ProxyName: 代理名称
当ProxyType=hostname时，表示域名或者子域名
当ProxyType=instance时，表示实例名称
        :type ProxyName: str
        :param PlatType: 调度模式：
ip表示Anycast IP
domain表示CNAME
        :type PlatType: str
        :param SecurityType: 0关闭安全，1开启安全
        :type SecurityType: int
        :param AccelerateType: 0关闭加速，1开启加速
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经移至Rule.ForwardClientIp
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经移至Rule.SessionPersist
        :type SessionPersist: bool
        :param Rule: 规则列表
        :type Rule: list of ApplicationProxyRule
        :param Status: 状态：
online：启用
offline：停用
progress：部署中
        :type Status: str
        :param ScheduleValue: 调度信息
        :type ScheduleValue: list of str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param SessionPersistTime: 会话保持时间
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名模式
instance：实例模式
        :type ProxyType: str
        :param HostId: 当ProxyType=hostname时：
ProxyName为域名，如：test.123.com
HostId表示该域名，即test.123.com对应的代理加速唯一标识
        :type HostId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.Rule = None
        self.Status = None
        self.ScheduleValue = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.HostId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.Status = params.get("Status")
        self.ScheduleValue = params.get("ScheduleValue")
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        self.HostId = params.get("HostId")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyRequest(AbstractModel):
    """DescribeApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Offset: 分页参数Offset
        :type Offset: int
        :param Limit: 分页参数Limit
        :type Limit: int
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxyResponse(AbstractModel):
    """DescribeApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ApplicationProxy
        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Quota: 字段已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type Quota: int
        :param IpCount: 表示套餐内PlatType为ip的Anycast IP实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type IpCount: int
        :param DomainCount: 表示套餐内PlatType为domain的CNAME实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.Quota = None
        self.IpCount = None
        self.DomainCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.Quota = params.get("Quota")
        self.IpCount = params.get("IpCount")
        self.DomainCount = params.get("DomainCount")
        self.RequestId = params.get("RequestId")


class DescribeBotLogRequest(AbstractModel):
    """DescribeBotLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 每页条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param Domains: 域名集合
        :type Domains: list of str
        :param QueryCondition: 查询条件
        :type QueryCondition: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotLogResponse(AbstractModel):
    """DescribeBotLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: Bot攻击Data
        :type Data: :class:`tencentcloud.teo.v20220106.models.BotLogData`
        :param Status: 状态，1：失败，0:成功
        :type Status: int
        :param Msg: 返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = BotLogData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeBotManagedRulesRequest(AbstractModel):
    """DescribeBotManagedRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param Entity: 子域名/应用名
        :type Entity: str
        :param Page: 页数
        :type Page: int
        :param PerPage: 每页数量
        :type PerPage: int
        :param RuleType: idcid/sipbot/uabot规则类型，空代表拉取全部
        :type RuleType: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Page = None
        self.PerPage = None
        self.RuleType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Page = params.get("Page")
        self.PerPage = params.get("PerPage")
        self.RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBotManagedRulesResponse(AbstractModel):
    """DescribeBotManagedRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 本次返回的规则数
        :type Count: int
        :param Rules: Bot规则
        :type Rules: list of BotManagedRuleDetail
        :param Total: 总规则数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = BotManagedRuleDetail()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCnameStatusRequest(AbstractModel):
    """DescribeCnameStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Names: 域名列表
        :type Names: list of str
        """
        self.ZoneId = None
        self.Names = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCnameStatusResponse(AbstractModel):
    """DescribeCnameStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 状态列表
        :type Status: list of CnameStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Status") is not None:
            self.Status = []
            for item in params.get("Status"):
                obj = CnameStatus()
                obj._deserialize(item)
                self.Status.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略组id
        :type PolicyId: int
        :param ZoneId: 一级域名zone
        :type ZoneId: str
        """
        self.PolicyId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSPolicyResponse(AbstractModel):
    """DescribeDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackDataRequest(AbstractModel):
    """DescribeDDosAttackData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricNames: 统计指标列表
        :type MetricNames: list of str
        :param ZoneIds: 站点id列表
        :type ZoneIds: list of str
        :param PolicyIds: ddos策略组id列表
        :type PolicyIds: list of int
        :param Port: 端口号
        :type Port: int
        :param ProtocolType: 协议类型,tcp,udp,all
        :type ProtocolType: str
        :param AttackType: 攻击类型,flood,icmpFlood......,all
        :type AttackType: str
        :param Interval: 查询时间粒度，可选{min,5min,hour,day}
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Port = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Port = params.get("Port")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackDataResponse(AbstractModel):
    """DescribeDDosAttackData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDos攻击数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回数据
        :type Msg: str
        :param Interval: 查询时间粒度，可选{min,5min,hour,day}
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackEventDetailRequest(AbstractModel):
    """DescribeDDosAttackEventDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventId: 事件id
        :type EventId: str
        """
        self.EventId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackEventDetailResponse(AbstractModel):
    """DescribeDDosAttackEventDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDos攻击事件详情
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventDetailData`
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosAttackEventDetailData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackEventRequest(AbstractModel):
    """DescribeDDosAttackEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param PolicyIds: ddos策略组id 集合
        :type PolicyIds: list of int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param ProtocolType: 协议类型,{tcp,udp,all}
        :type ProtocolType: str
        :param IsShowDetail: 选填{Y、N},默认为Y；Y：展示，N：不展示
        :type IsShowDetail: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.ProtocolType = None
        self.IsShowDetail = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.ProtocolType = params.get("ProtocolType")
        self.IsShowDetail = params.get("IsShowDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackEventResponse(AbstractModel):
    """DescribeDDosAttackEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDos攻击事件数据
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventData`
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosAttackEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackSourceEventRequest(AbstractModel):
    """DescribeDDosAttackSourceEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param PolicyIds: ddos策略组id 集合
        :type PolicyIds: list of int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param ProtocolType: 协议类型,{tcp,udp,all}
        :type ProtocolType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.ProtocolType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.ProtocolType = params.get("ProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackSourceEventResponse(AbstractModel):
    """DescribeDDosAttackSourceEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDos攻击源数据
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackSourceEventData`
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosAttackSourceEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackTopDataRequest(AbstractModel):
    """DescribeDDosAttackTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricName: 过滤指标
        :type MetricName: str
        :param Limit: 查询前多少名,传值为0 全量
        :type Limit: int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param PolicyIds: ddos策略组id 集合
        :type PolicyIds: list of int
        :param Port: 端口号
        :type Port: int
        :param ProtocolType: 协议类型,tcp,udp,all
        :type ProtocolType: str
        :param AttackType: 攻击类型,flood,icmpFlood......,all
        :type AttackType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Port = None
        self.ProtocolType = None
        self.AttackType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Port = params.get("Port")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosAttackTopDataResponse(AbstractModel):
    """DescribeDDosAttackTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: topn数据
        :type Data: list of TopNEntry
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回消息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopNEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDDosMajorAttackEventRequest(AbstractModel):
    """DescribeDDosMajorAttackEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param PolicyIds: ddos 策略组id集合
        :type PolicyIds: list of int
        :param ProtocolType: 协议类型，{tcp,udp,all}
        :type ProtocolType: str
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ProtocolType = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ProtocolType = params.get("ProtocolType")
        self.ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDosMajorAttackEventResponse(AbstractModel):
    """DescribeDDosMajorAttackEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDos查询主攻击事件
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosMajorAttackEventData`
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回消息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DDosMajorAttackEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 证书总数
        :type TotalCount: int
        :param CertInfo: 默认证书列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: list of DefaultServerCertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Filters: 过滤参数
        :type Filters: list of DnsDataFilter
        :param Interval: 时间粒度，默认为1分钟粒度，服务端根据时间范围自适应。
支持指定以下几种粒度：
min：1分钟粒度
5min：5分钟粒度
hour：1小时粒度
day：天粒度
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DnsDataFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsDataResponse(AbstractModel):
    """DescribeDnsData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 统计曲线数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DataItem
        :param Interval: 时间粒度
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeDnsRecordsRequest(AbstractModel):
    """DescribeDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 查询条件过滤器
        :type Filters: list of DnsRecordFilter
        :param Order: 排序
        :type Order: str
        :param Direction: 可选值 asc, desc
        :type Direction: str
        :param Match: 可选值 all, any
        :type Match: str
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param ZoneId: 站点 ID
        :type ZoneId: str
        """
        self.Filters = None
        self.Order = None
        self.Direction = None
        self.Match = None
        self.Limit = None
        self.Offset = None
        self.ZoneId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DnsRecordFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.Direction = params.get("Direction")
        self.Match = params.get("Match")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnsRecordsResponse(AbstractModel):
    """DescribeDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数，用于分页查询
        :type TotalCount: int
        :param Records: DNS 记录列表
        :type Records: list of DnsRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Records = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = DnsRecord()
                obj._deserialize(item)
                self.Records.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnssecRequest(AbstractModel):
    """DescribeDnssec请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDnssecResponse(AbstractModel):
    """DescribeDnssec返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Status: DNSSEC 状态
- enabled 开启
- disabled 关闭
        :type Status: str
        :param Dnssec: DNSSEC 相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class DescribeHostsCertificateRequest(AbstractModel):
    """DescribeHostsCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Filters: 查询条件过滤器
        :type Filters: list of CertFilter
        :param Sort: 排序方式
        :type Sort: :class:`tencentcloud.teo.v20220106.models.CertSort`
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = CertFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = CertSort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsCertificateResponse(AbstractModel):
    """DescribeHostsCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数，用于分页查询
        :type TotalCount: int
        :param Hosts: 域名证书配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Hosts: list of HostCertSetting
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Hosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = HostCertSetting()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Hosts: 指定域名查询
        :type Hosts: list of str
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Hosts = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Hosts = params.get("Hosts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param Hosts: 域名列表
        :type Hosts: list of DetailHost
        :param TotalNumber: 域名数量
        :type TotalNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Hosts = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Hosts") is not None:
            self.Hosts = []
            for item in params.get("Hosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self.Hosts.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIdentificationRequest(AbstractModel):
    """DescribeIdentification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationResponse(AbstractModel):
    """DescribeIdentification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param Status: 验证状态
- pending 验证中
- finished 验证完成
        :type Status: str
        :param Subdomain: 子域
        :type Subdomain: str
        :param RecordType: 记录类型
        :type RecordType: str
        :param RecordValue: 记录值
        :type RecordValue: str
        :param OriginalNameServers: 域名当前的 NS 记录
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalNameServers: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Status = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.OriginalNameServers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingDetailRequest(AbstractModel):
    """DescribeLoadBalancingDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingDetailResponse(AbstractModel):
    """DescribeLoadBalancingDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Host: 子域名，填写@表示根域
        :type Host: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param Origin: 使用的源站信息
        :type Origin: list of OriginGroup
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Status: 状态
        :type Status: str
        :param Cname: 调度域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancingRequest(AbstractModel):
    """DescribeLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Offset: 分页参数Offset
        :type Offset: int
        :param Limit: 分页参数Limit
        :type Limit: int
        :param Host: 过滤参数Host
        :type Host: str
        :param Fuzzy: 过滤参数Host是否支持模糊匹配
        :type Fuzzy: bool
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Host = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Host = params.get("Host")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancingResponse(AbstractModel):
    """DescribeLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param Data: 负载均衡信息
        :type Data: list of LoadBalancing
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = LoadBalancing()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOriginGroupDetailRequest(AbstractModel):
    """DescribeOriginGroupDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        """
        self.OriginId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupDetailResponse(AbstractModel):
    """DescribeOriginGroupDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param OriginName: 源站组名称
        :type OriginName: str
        :param Type: 源站组配置类型
area：表示按照Record记录中的Area字段进行按客户端IP所在区域回源。
weight：表示按照Record记录中的Weight字段进行按权重回源。
        :type Type: str
        :param Record: 记录
        :type Record: list of OriginRecord
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param OriginType: 源站类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param ApplicationProxyUsed: 当前源站组是否被四层代理使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationProxyUsed: bool
        :param LoadBalancingUsed: 当前源站组是否被负载均衡使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancingUsed: bool
        :param LoadBalancingUsedType: 使用当前源站组的负载均衡的类型：
none：未被使用
dns_only：被仅DNS类型负载均衡使用
proxied：被代理加速类型负载均衡使用
both：同时被仅DNS和代理加速类型负载均衡使用
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancingUsedType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.OriginType = None
        self.ApplicationProxyUsed = None
        self.LoadBalancingUsed = None
        self.LoadBalancingUsedType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginType = params.get("OriginType")
        self.ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self.LoadBalancingUsed = params.get("LoadBalancingUsed")
        self.LoadBalancingUsedType = params.get("LoadBalancingUsedType")
        self.RequestId = params.get("RequestId")


class DescribeOriginGroupRequest(AbstractModel):
    """DescribeOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页参数Offset
        :type Offset: int
        :param Limit: 分页参数Limit
        :type Limit: int
        :param Filters: 过滤参数
        :type Filters: list of OriginFilter
        :param ZoneId: 站点ID
不填写获取所有站点源站组
        :type ZoneId: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = OriginFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupResponse(AbstractModel):
    """DescribeOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 源站组信息
        :type Data: list of OriginGroup
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: RFC3339格式，客户端时间
        :type StartTime: str
        :param EndTime: RFC3339格式，客户端时间
        :type EndTime: str
        :param MetricNames: 指标列表，支持的指标
l7Flow_outFlux: 访问流量
l7Flow_request: 访问请求数
l7Flow_outBandwidth: 访问带宽
        :type MetricNames: list of str
        :param Interval: 时间间隔，选填{min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: ZoneId列表，仅在zone/domain维度下查询时该参数有效
        :type ZoneIds: list of str
        :param Domains: Domain列表，仅在domain维度下查询时该参数有效
        :type Domains: list of str
        :param Protocol: 协议类型， 选填{http,http2,https,all}
        :type Protocol: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Domains = None
        self.Protocol = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewL7DataResponse(AbstractModel):
    """DescribeOverviewL7Data返回参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 查询维度
        :type Type: str
        :param Interval: 时间间隔
        :type Interval: str
        :param Data: 详细数据
        :type Data: list of TimingDataRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Type = None
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Offset: 查询起始偏移量
        :type Offset: int
        :param Limit: 查询最大返回的结果条数
        :type Limit: int
        :param Statuses: 查询的状态
允许的值为：processing、success、failed、timeout、invalid
        :type Statuses: list of str
        :param ZoneId: zone id
        :type ZoneId: str
        :param Domains: 查询的域名列表
        :type Domains: list of str
        :param Target: 查询的资源
        :type Target: str
        """
        self.JobId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 该查询条件总共条目数
        :type TotalCount: int
        :param Tasks: 任务结果列表
        :type Tasks: list of Task
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param Type: 类型
        :type Type: str
        :param StartTime: 查询起始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Offset: 查询起始偏移量
        :type Offset: int
        :param Limit: 查询最大返回的结果条数
        :type Limit: int
        :param Statuses: 查询的状态
允许的值为：processing、success、failed、timeout、invalid
        :type Statuses: list of str
        :param ZoneId: zone id
        :type ZoneId: str
        :param Domains: 查询的域名列表
        :type Domains: list of str
        :param Target: 查询内容
        :type Target: str
        """
        self.JobId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Statuses = None
        self.ZoneId = None
        self.Domains = None
        self.Target = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Statuses = params.get("Statuses")
        self.ZoneId = params.get("ZoneId")
        self.Domains = params.get("Domains")
        self.Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 该查询条件总共条目数
        :type TotalCount: int
        :param Tasks: 任务结果列表
        :type Tasks: list of Task
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyListRequest(AbstractModel):
    """DescribeSecurityPolicyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyListResponse(AbstractModel):
    """DescribeSecurityPolicyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Entities: 防护资源列表
        :type Entities: list of SecurityEntity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Entities = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Entities") is not None:
            self.Entities = []
            for item in params.get("Entities"):
                obj = SecurityEntity()
                obj._deserialize(item)
                self.Entities.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyManagedRulesIdRequest(AbstractModel):
    """DescribeSecurityPolicyManagedRulesId请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则id集合
        :type RuleId: list of int
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyManagedRulesIdResponse(AbstractModel):
    """DescribeSecurityPolicyManagedRulesId返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回总数
        :type Total: int
        :param Rules: 门神规则
        :type Rules: list of ManagedRule
        :param Count: 返回总数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Rules = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ManagedRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyManagedRulesRequest(AbstractModel):
    """DescribeSecurityPolicyManagedRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param Entity: 子域名/应用名
        :type Entity: str
        :param Page: 页数
        :type Page: int
        :param PerPage: 每页数量
        :type PerPage: int
        """
        self.ZoneId = None
        self.Entity = None
        self.Page = None
        self.PerPage = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Page = params.get("Page")
        self.PerPage = params.get("PerPage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyManagedRulesResponse(AbstractModel):
    """DescribeSecurityPolicyManagedRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 本次返回的规则数
        :type Count: int
        :param Rules: 门神规则
        :type Rules: list of ManagedRule
        :param Total: 总规则数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ManagedRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyRegionsRequest(AbstractModel):
    """DescribeSecurityPolicyRegions请求参数结构体

    """


class DescribeSecurityPolicyRegionsResponse(AbstractModel):
    """DescribeSecurityPolicyRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 总数
        :type Count: int
        :param GeoIp: 地域信息
        :type GeoIp: list of GeoIp
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.GeoIp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("GeoIp") is not None:
            self.GeoIp = []
            for item in params.get("GeoIp"):
                obj = GeoIp()
                obj._deserialize(item)
                self.GeoIp.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyRequest(AbstractModel):
    """DescribeSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param Entity: 二级域名
        :type Entity: str
        """
        self.ZoneId = None
        self.Entity = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyResponse(AbstractModel):
    """DescribeSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppId: 用户id
        :type AppId: int
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param Entity: 二级域名
        :type Entity: str
        :param Config: 安全配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Entity = None
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        if params.get("Config") is not None:
            self.Config = SecurityConfig()
            self.Config._deserialize(params.get("Config"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityPortraitRulesRequest(AbstractModel):
    """DescribeSecurityPortraitRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param Entity: 子域名/应用名
        :type Entity: str
        """
        self.ZoneId = None
        self.Entity = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPortraitRulesResponse(AbstractModel):
    """DescribeSecurityPortraitRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 本次返回的规则数
        :type Count: int
        :param Rules: Bot用户画像规则
        :type Rules: list of PortraitManagedRuleDetail
        :param Total: 总规则数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = PortraitManagedRuleDetail()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: RFC3339格式，客户端时间
        :type StartTime: str
        :param EndTime: RFC3339格式，客户端时间
        :type EndTime: str
        :param MetricNames: 支持的指标：
l4Flow_connections: 访问连接数
l4Flow_flux: 访问总流量
l4Flow_inFlux: 访问入流量
l4Flow_outFlux: 访问出流量
        :type MetricNames: list of str
        :param ZoneIds: 站点id列表
        :type ZoneIds: list of str
        :param InstanceIds: 该字段已废弃，请使用ProxyIds字段
        :type InstanceIds: list of str
        :param Protocol: 该字段当前无效
        :type Protocol: str
        :param Interval: 时间间隔，选填{min, 5min, hour, day}
        :type Interval: str
        :param RuleId: 该字段当前无效，请使用Filter筛选
        :type RuleId: str
        :param Filters: 支持的 Filter：proxyd,ruleId
        :type Filters: list of Filter
        :param ProxyIds: 四层实例列表
        :type ProxyIds: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.InstanceIds = None
        self.Protocol = None
        self.Interval = None
        self.RuleId = None
        self.Filters = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.InstanceIds = params.get("InstanceIds")
        self.Protocol = params.get("Protocol")
        self.Interval = params.get("Interval")
        self.RuleId = params.get("RuleId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL4DataResponse(AbstractModel):
    """DescribeTimingL4Data返回参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 查询维度
        :type Type: str
        :param Interval: 时间间隔
        :type Interval: str
        :param Data: 详细数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Type = None
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimingL7AnalysisDataRequest(AbstractModel):
    """DescribeTimingL7AnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: RFC3339标准，客户端时间
        :type StartTime: str
        :param EndTime: RFC3339标准，客户端时间
        :type EndTime: str
        :param MetricNames: 指标列表，支持的指标
l7Flow_outFlux: 访问流量
l7Flow_request: 访问请求数
l7Flow_outBandwidth: 访问带宽
        :type MetricNames: list of str
        :param Interval: 时间间隔，选填{min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: ZoneId数组
        :type ZoneIds: list of str
        :param Filters: 筛选条件
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7AnalysisDataResponse(AbstractModel):
    """DescribeTimingL7AnalysisData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 详细数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
        :param Type: 查询维度
        :type Type: str
        :param Interval: 时间间隔
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: RFC3339标准，客户端时间
        :type StartTime: str
        :param EndTime: RFC3339标准，客户端时间
        :type EndTime: str
        :param MetricNames: 时序类访问流量指标列表，支持的指标
l7Cache_outFlux: 访问流量
l7Cache_request: 访问请求数
        :type MetricNames: list of str
        :param Interval: 时间间隔，选填{min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: 站点id列表
        :type ZoneIds: list of str
        :param Filters: 筛选条件，筛选EO/源站响应如下：
EO响应：{Key: "cacheType", Value: ["hit"], Operator: "equals"}；
源站响应：{Key: "cacheType", Value: ["miss", "dynamic"], Operator: "equals"}
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7CacheDataResponse(AbstractModel):
    """DescribeTimingL7CacheData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 详细数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
        :param Type: 查询维度
        :type Type: str
        :param Interval: 时间间隔
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: RFC3339标准，客户端时间
        :type StartTime: str
        :param EndTime: RFC3339标准，客户端时间
        :type EndTime: str
        :param MetricName: 时序类访问流量指标
        :type MetricName: str
        :param Limit: topN,填0时返回全量数据
        :type Limit: int
        :param Interval: 时间间隔，选填{min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: ZoneId数组
        :type ZoneIds: list of str
        :param Filters: 筛选条件
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7AnalysisDataResponse(AbstractModel):
    """DescribeTopL7AnalysisData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: top详细数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopDataRecord
        :param Type: 查询维度
        :type Type: str
        :param MetricName: 查询指标
        :type MetricName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: RFC3339标准，客户端时间
        :type StartTime: str
        :param EndTime: RFC3339标准，客户端时间
        :type EndTime: str
        :param MetricName: 时序类访问流量指标
        :type MetricName: str
        :param Limit: topN,填0时返回全量数据
        :type Limit: int
        :param Interval: 时间间隔，选填{min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: ZoneId数组
        :type ZoneIds: list of str
        :param Filters: 筛选条件
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7CacheDataResponse(AbstractModel):
    """DescribeTopL7CacheData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: top详细数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopDataRecord
        :param Type: 查询维度
        :type Type: str
        :param MetricName: 查询指标
        :type MetricName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Type = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Type = params.get("Type")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesAttackEventsRequest(AbstractModel):
    """DescribeWebManagedRulesAttackEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param PolicyIds: ddos策略组id列表
        :type PolicyIds: list of int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param Domains: 子域名列表
        :type Domains: list of str
        :param IsShowDetail: 选填{Y、N},默认为Y；Y：展示，N：不展示
        :type IsShowDetail: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.Domains = None
        self.IsShowDetail = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.IsShowDetail = params.get("IsShowDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesAttackEventsResponse(AbstractModel):
    """DescribeWebManagedRulesAttackEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: Web攻击事件数据
        :type Data: :class:`tencentcloud.teo.v20220106.models.WebEventData`
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回数据
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WebEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesDataRequest(AbstractModel):
    """DescribeWebManagedRulesData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricNames: 统计指标列表
        :type MetricNames: list of str
        :param ZoneIds: 站点id列表
        :type ZoneIds: list of str
        :param Domains: 子域名列表
        :type Domains: list of str
        :param ProtocolType: 协议类型
        :type ProtocolType: str
        :param AttackType: "webshell" : Webshell检测防护
"oa" : 常见OA漏洞防护
"xss" : XSS跨站脚本攻击防护
"xxe" : XXE攻击防护
"webscan" : 扫描器攻击漏洞防护
"cms" : 常见CMS漏洞防护
"upload" : 恶意文件上传攻击防护
"sql" : SQL注入攻击防护
"cmd_inject": 命令/代码注入攻击防护
"osc" : 开源组件漏洞防护
"file_read" : 任意文件读取
"ldap" : LDAP注入攻击防护
"other" : 其它漏洞防护

"all":"所有"
        :type AttackType: str
        :param Interval: 查询时间粒度，可选{min,5min,hour,day}
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesDataResponse(AbstractModel):
    """DescribeWebManagedRulesData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: Web攻击日志实体
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回消息
        :type Msg: str
        :param Interval: 查询时间粒度，可选{min,5min,hour,day}
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesLogRequest(AbstractModel):
    """DescribeWebManagedRulesLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 每页条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param Domains: 域名集合
        :type Domains: list of str
        :param QueryCondition: 查询条件
        :type QueryCondition: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesLogResponse(AbstractModel):
    """DescribeWebManagedRulesLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: web攻击日志data
        :type Data: :class:`tencentcloud.teo.v20220106.models.WebLogData`
        :param Status: 状态，1:失败，0:失败
        :type Status: int
        :param Msg: 返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WebLogData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesTopDataRequest(AbstractModel):
    """DescribeWebManagedRulesTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricName: 过滤指标
        :type MetricName: str
        :param Limit: 查询前多少名,传值为0 全量
        :type Limit: int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param PolicyIds: ddos策略组id 集合
        :type PolicyIds: list of int
        :param Port: 端口号
        :type Port: int
        :param ProtocolType: 协议类型,tcp,udp,all
        :type ProtocolType: str
        :param AttackType: 攻击类型,flood,icmpFlood......,all
        :type AttackType: str
        :param Domains: 域名集合
        :type Domains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Port = None
        self.ProtocolType = None
        self.AttackType = None
        self.Domains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Limit = params.get("Limit")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Port = params.get("Port")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesTopDataResponse(AbstractModel):
    """DescribeWebManagedRulesTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: topn数据
        :type Data: list of TopNEntry
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回消息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopNEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionAttackEventsRequest(AbstractModel):
    """DescribeWebProtectionAttackEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param Domains: 域名
        :type Domains: list of str
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.Domains = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Domains = params.get("Domains")
        self.ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionAttackEventsResponse(AbstractModel):
    """DescribeWebProtectionAttackEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDos攻击事件数据
        :type Data: :class:`tencentcloud.teo.v20220106.models.CCInterceptEventData`
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 返回消息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CCInterceptEventData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionDataRequest(AbstractModel):
    """DescribeWebProtectionData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricNames: 统计指标列表
        :type MetricNames: list of str
        :param ZoneIds: 站点id列表
        :type ZoneIds: list of str
        :param Domains: 子域名列表
        :type Domains: list of str
        :param ProtocolType: 协议类型
        :type ProtocolType: str
        :param AttackType: "webshell" : Webshell检测防护
"oa" : 常见OA漏洞防护
"xss" : XSS跨站脚本攻击防护
"xxe" : XXE攻击防护
"webscan" : 扫描器攻击漏洞防护
"cms" : 常见CMS漏洞防护
"upload" : 恶意文件上传攻击防护
"sql" : SQL注入攻击防护
"cmd_inject": 命令/代码注入攻击防护
"osc" : 开源组件漏洞防护
"file_read" : 任意文件读取
"ldap" : LDAP注入攻击防护
"other" : 其它漏洞防护

"all":"所有"
        :type AttackType: str
        :param Interval: 查询时间粒度，可选{min,5min,hour,day}
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionDataResponse(AbstractModel):
    """DescribeWebProtectionData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 数据详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param Status: 状态，1:失败，0:成功
        :type Status: int
        :param Msg: 消息
        :type Msg: str
        :param Interval: 查询时间粒度，可选{min,5min,hour,day}
        :type Interval: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.Interval = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.Interval = params.get("Interval")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionLogRequest(AbstractModel):
    """DescribeWebProtectionLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageSize: 每页条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param ZoneIds: 站点集合
        :type ZoneIds: list of str
        :param Domains: 域名集合
        :type Domains: list of str
        :param QueryCondition: 查询条件
        :type QueryCondition: list of QueryCondition
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionLogResponse(AbstractModel):
    """DescribeWebProtectionLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 限速拦截Data
        :type Data: :class:`tencentcloud.teo.v20220106.models.CCLogData`
        :param Status: 状态，1：失败，0:成功
        :type Status: int
        :param Msg: 返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Status = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CCLogData()
            self.Data._deserialize(params.get("Data"))
        self.Status = params.get("Status")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeZoneDDoSPolicyRequest(AbstractModel):
    """DescribeZoneDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名id
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDDoSPolicyResponse(AbstractModel):
    """DescribeZoneDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppId: 用户appid
        :type AppId: int
        :param ShieldAreas: 防护分区
        :type ShieldAreas: list of ShieldArea
        :param Domains: 所有子域名信息，包含安全加速/内容加速
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of DDoSApplication
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.ShieldAreas = None
        self.Domains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        if params.get("ShieldAreas") is not None:
            self.ShieldAreas = []
            for item in params.get("ShieldAreas"):
                obj = ShieldArea()
                obj._deserialize(item)
                self.ShieldAreas.append(obj)
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DDoSApplication()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneDetailsRequest(AbstractModel):
    """DescribeZoneDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneDetailsResponse(AbstractModel):
    """DescribeZoneDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param OriginalNameServers: 用户当前使用的 NS 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalNameServers: list of str
        :param NameServers: 腾讯云分配给用户的 NS 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NameServers: list of str
        :param Status: 站点状态
- active：NS 已切换
- pending：NS 未切换
- moved：NS 已切走
- deactivated：被封禁
        :type Status: str
        :param Type: 站点接入方式
- full：NS 接入
- partial：CNAME 接入
        :type Type: str
        :param Paused: 站点是否关闭
        :type Paused: bool
        :param CreatedOn: 站点创建时间
        :type CreatedOn: str
        :param ModifiedOn: 站点修改时间
        :type ModifiedOn: str
        :param VanityNameServers: 用户自定义 NS 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        :param VanityNameServersIps: 用户自定义 NS IP 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServersIps: list of VanityNameServersIps
        :param CnameSpeedUp: 是否开启 CNAME 加速
- enabled：开启
- disabled：关闭
        :type CnameSpeedUp: str
        :param CnameStatus: cname切换验证状态
- finished 切换完成
- pending 切换验证中
注意：此字段可能返回 null，表示取不到有效值。
        :type CnameStatus: str
        :param Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.VanityNameServers = None
        self.VanityNameServersIps = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneSettingResponse(AbstractModel):
    """DescribeZoneSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param Cache: 缓存过期时间配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: 节点缓存键配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: 浏览器缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: 离线缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: Quic访问
注意：此字段可能返回 null，表示取不到有效值。
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: POST请求传输配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: 智能压缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: http2回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制https跳转配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: Https 加速配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: 源站配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: 动态加速配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Zone: 站点域名
        :type Zone: str
        :param WebSocket: WebSocket配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: 客户端IP回源请求头配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: 缓存预刷新配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Cache = None
        self.CacheKey = None
        self.MaxAge = None
        self.OfflineCache = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.Https = None
        self.Origin = None
        self.SmartRouting = None
        self.ZoneId = None
        self.Zone = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页参数，页偏移
        :type Offset: int
        :param Limit: 分页参数，每页返回的站点个数
        :type Limit: int
        :param Filters: 查询条件过滤器，复杂类型
        :type Filters: list of ZoneFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = ZoneFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的站点数
        :type TotalCount: int
        :param Zones: 站点详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of Zone
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Zones = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RequestId = params.get("RequestId")


class DetailHost(AbstractModel):
    """域名配置信息

    """

    def __init__(self):
        r"""
        :param AppId: 腾讯云账号ID
        :type AppId: int
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Status: 加速服务状态
process：部署中
online：已启动
offline：已关闭
        :type Status: str
        :param Host: 域名
        :type Host: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Status = None
        self.Host = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsDataFilter(AbstractModel):
    """Dns数据曲线过滤参数

    """

    def __init__(self):
        r"""
        :param Name: 参数名称，取值范围：
zone：站点名
host：域名
type：dns解析类型
code：dns返回状态码
area：解析服务器所在区域
        :type Name: str
        :param Value: 参数值
当Name=area时，Value取值范围：
亚洲：Asia
欧洲：Europe
非洲：Africa
大洋洲：Oceania
美洲：Americas

当Name=code时，Value取值范围：
NoError：成功的响应
NXDomain：只在权威域名服务器的响应消息中有效，标示请求中请求的域不存在
NotImp：域名服务器不支持请求的类型
Refused：域名服务器因为策略的原因拒绝执行请求的操作
        :type Value: str
        :param Values: 参数值
当Name=area时，Value取值范围：
亚洲：Asia
欧洲：Europe
非洲：Africa
大洋洲：Oceania
美洲：Americas

当Name=code时，Value取值范围：
NoError：成功的响应
NXDomain：只在权威域名服务器的响应消息中有效，标示请求中请求的域不存在
NotImp：域名服务器不支持请求的类型
Refused：域名服务器因为策略的原因拒绝执行请求的操作
        :type Values: list of str
        """
        self.Name = None
        self.Value = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecord(AbstractModel):
    """DNS 记录

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 主机记录
        :type Name: str
        :param Content: 记录值
        :type Content: str
        :param Mode: 代理模式
        :type Mode: str
        :param Ttl: TTL 值
        :type Ttl: int
        :param Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param Locked: 域名锁
        :type Locked: bool
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param Status: 解析状态
active: 生效
pending: 不生效
        :type Status: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param DomainStatus: 域名是否开启了负载均衡，四层代理，安全
- lb 负载均衡
- security 安全
- l4 四层代理
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainStatus: list of str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Mode = None
        self.Ttl = None
        self.Priority = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Locked = None
        self.ZoneId = None
        self.ZoneName = None
        self.Status = None
        self.Cname = None
        self.DomainStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Locked = params.get("Locked")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.DomainStatus = params.get("DomainStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsRecordFilter(AbstractModel):
    """DNS 记录查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名，支持的列表如下：
- name: 站点名。
- status: 站点状态
        :type Name: str
        :param Values: 过滤字段值
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为name。模糊查询时，Values长度最大为1
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnssecInfo(AbstractModel):
    """DNSSEC 相关信息

    """

    def __init__(self):
        r"""
        :param Flags: 标志
        :type Flags: int
        :param Algorithm: 加密算法
        :type Algorithm: str
        :param KeyType: 加密类型
        :type KeyType: str
        :param DigestType: 摘要类型
        :type DigestType: str
        :param DigestAlgorithm: 摘要算法
        :type DigestAlgorithm: str
        :param Digest: 摘要信息
        :type Digest: str
        :param DS: DS 记录值
        :type DS: str
        :param KeyTag: 密钥标签
        :type KeyTag: int
        :param PublicKey: 公钥
        :type PublicKey: str
        """
        self.Flags = None
        self.Algorithm = None
        self.KeyType = None
        self.DigestType = None
        self.DigestAlgorithm = None
        self.Digest = None
        self.DS = None
        self.KeyTag = None
        self.PublicKey = None


    def _deserialize(self, params):
        self.Flags = params.get("Flags")
        self.Algorithm = params.get("Algorithm")
        self.KeyType = params.get("KeyType")
        self.DigestType = params.get("DigestType")
        self.DigestAlgorithm = params.get("DigestAlgorithm")
        self.Digest = params.get("Digest")
        self.DS = params.get("DS")
        self.KeyTag = params.get("KeyTag")
        self.PublicKey = params.get("PublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间(需严格按照RFC3339标准传参)
        :type StartTime: str
        :param EndTime: 结束时间(需严格按照RFC3339标准传参)
        :type EndTime: str
        :param PageSize: 每页展示条数
        :type PageSize: int
        :param PageNo: 当前页
        :type PageNo: int
        :param Zones: 站点名集合
        :type Zones: list of str
        :param Domains: 子域名集合
        :type Domains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.Zones = None
        self.Domains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Zones = params.get("Zones")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 七层离线日志data
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of L7OfflineLog
        :param PageSize: 页面大小
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param PageNo: 页号
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.PageSize = None
        self.PageNo = None
        self.Pages = None
        self.TotalSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        self.RequestId = params.get("RequestId")


class FailReason(AbstractModel):
    """失败原因

    """

    def __init__(self):
        r"""
        :param Reason: 失败原因
        :type Reason: str
        :param Targets: 处理失败的资源列表。
该列表元素来源于输入参数中的Targets，因此格式和入参中的Targets保持一致
        :type Targets: list of str
        """
        self.Reason = None
        self.Targets = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param Key: 筛选维度
        :type Key: str
        :param Operator: 操作符
        :type Operator: str
        :param Value: 筛选维度值
        :type Value: list of str
        """
        self.Key = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """访问协议强制https跳转配置

    """

    def __init__(self):
        r"""
        :param Switch: 访问强制跳转配置开关
on：开启
off：关闭
        :type Switch: str
        :param RedirectStatusCode: 重定向状态码
301
302
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeoIp(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param RegionId: 地域ID
        :type RegionId: int
        :param Country: 国家名
        :type Country: str
        :param Continent: 洲
        :type Continent: str
        :param CountryEn: 国家英文名
        :type CountryEn: str
        :param ContinentEn: 洲
        :type ContinentEn: str
        """
        self.RegionId = None
        self.Country = None
        self.Continent = None
        self.CountryEn = None
        self.ContinentEn = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Country = params.get("Country")
        self.Continent = params.get("Continent")
        self.CountryEn = params.get("CountryEn")
        self.ContinentEn = params.get("ContinentEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """刷新预热附带的头部信息

    """

    def __init__(self):
        r"""
        :param Name: HTTP头部
        :type Name: str
        :param Value: HTTP头部值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostCertSetting(AbstractModel):
    """域名证书配置

    """

    def __init__(self):
        r"""
        :param Host: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param CertInfo: 服务端证书配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: list of ServerCertInfo
        """
        self.Host = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """Hsts配置

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启，on或off。
        :type Switch: str
        :param MaxAge: MaxAge数值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: int
        :param IncludeSubDomains: 是否包含子域名，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeSubDomains: str
        :param Preload: 是否预加载，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Preload: str
        """
        self.Switch = None
        self.MaxAge = None
        self.IncludeSubDomains = None
        self.Preload = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxAge = params.get("MaxAge")
        self.IncludeSubDomains = params.get("IncludeSubDomains")
        self.Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """域名 https 加速配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param Http2: http2 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param OcspStapling: OCSP 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param TlsVersion: Tls版本设置，支持设置 TLSv1, TLSV1.1, TLSV1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TlsVersion: list of str
        :param Hsts: HSTS 配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.teo.v20220106.models.Hsts`
        """
        self.Http2 = None
        self.OcspStapling = None
        self.TlsVersion = None
        self.Hsts = None


    def _deserialize(self, params):
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneRequest(AbstractModel):
    """IdentifyZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param Subdomain: 子域
        :type Subdomain: str
        :param RecordType: 记录类型
        :type RecordType: str
        :param RecordValue: 记录值
        :type RecordValue: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        self.RequestId = params.get("RequestId")


class ImportDnsRecordsRequest(AbstractModel):
    """ImportDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param File: 文件内容
        :type File: str
        """
        self.ZoneId = None
        self.File = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.File = params.get("File")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportDnsRecordsResponse(AbstractModel):
    """ImportDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 记录 ID
        :type Ids: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ids = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.RequestId = params.get("RequestId")


class IntelligenceRule(AbstractModel):
    """智能分析规则

    """

    def __init__(self):
        r"""
        :param Switch: 开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Items: 规则详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of IntelligenceRuleItem
        """
        self.Switch = None
        self.Items = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = IntelligenceRuleItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceRuleItem(AbstractModel):
    """Bot智能分析规则详情

    """

    def __init__(self):
        r"""
        :param Label: 恶意BOT
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Action: 动作
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        """
        self.Label = None
        self.Action = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableConfig(AbstractModel):
    """IP黑白名单及IP区域控制配置

    """

    def __init__(self):
        r"""
        :param Switch: 开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Rules: []
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of IpTableRule
        """
        self.Switch = None
        self.Rules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableRule(AbstractModel):
    """IP黑白名单详细规则

    """

    def __init__(self):
        r"""
        :param Action: 动作: drop拦截，trans放行，monitor观察
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param MatchFrom: 根据类型匹配：ip(根据ip), area(根据区域)
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchFrom: str
        :param MatchContent: 匹配内容
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchContent: str
        :param RuleID: 规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Action = None
        self.MatchFrom = None
        self.MatchContent = None
        self.RuleID = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.MatchFrom = params.get("MatchFrom")
        self.MatchContent = params.get("MatchContent")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7OfflineLog(AbstractModel):
    """离线日志详细信息

    """

    def __init__(self):
        r"""
        :param LogTime: 日志打包开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTime: int
        :param Domain: 子域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Size: 原始大小 单位byte
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param Url: 下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param LogPacketName: 日志数据包名
注意：此字段可能返回 null，表示取不到有效值。
        :type LogPacketName: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancing(AbstractModel):
    """负载均衡信息

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param Host: 子域名，填写@表示根域
        :type Host: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param Origin: 使用的源站信息
        :type Origin: list of OriginGroup
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Status: 状态
        :type Status: str
        :param Cname: 调度域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        """
        self.LoadBalancingId = None
        self.ZoneId = None
        self.Host = None
        self.Type = None
        self.TTL = None
        self.OriginId = None
        self.Origin = None
        self.UpdateTime = None
        self.Status = None
        self.Cname = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.Type = params.get("Type")
        self.TTL = params.get("TTL")
        self.OriginId = params.get("OriginId")
        if params.get("Origin") is not None:
            self.Origin = []
            for item in params.get("Origin"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.Origin.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagedRule(AbstractModel):
    """门神规则

    """

    def __init__(self):
        r"""
        :param RuleId: 规则id
        :type RuleId: int
        :param Description: 规则描述
        :type Description: str
        :param RuleTypeName: 规则类型名
        :type RuleTypeName: str
        :param RuleLevelDesc: 策略规则防护等级
        :type RuleLevelDesc: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Status: 规则当前状态  block, allow
        :type Status: str
        :param RuleTags: 规则标签
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTags: list of str
        :param RuleTypeDesc: 规则类型详细描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTypeDesc: str
        :param RuleTypeId: 规则类型id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTypeId: int
        """
        self.RuleId = None
        self.Description = None
        self.RuleTypeName = None
        self.RuleLevelDesc = None
        self.UpdateTime = None
        self.Status = None
        self.RuleTags = None
        self.RuleTypeDesc = None
        self.RuleTypeId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.RuleLevelDesc = params.get("RuleLevelDesc")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.RuleTags = params.get("RuleTags")
        self.RuleTypeDesc = params.get("RuleTypeDesc")
        self.RuleTypeId = params.get("RuleTypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """浏览器缓存规则配置，用于设置 MaxAge 默认值，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param MaxAgeTime: MaxAge 时间设置，单位秒，最大365天
注意：时间为0，即不缓存。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAgeTime: int
        :param FollowOrigin: 是否遵循源站，on或off，开启时忽略时间设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        """
        self.MaxAgeTime = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        self.MaxAgeTime = params.get("MaxAgeTime")
        self.FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param ProxyName: 代理名称
当ProxyType=hostname时，表示域名或者子域名
当ProxyType=instance时，表示实例名称
        :type ProxyName: str
        :param ForwardClientIp: 参数已经废弃
        :type ForwardClientIp: str
        :param SessionPersist: 参数已经废弃
        :type SessionPersist: bool
        :param SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒
        :type SessionPersistTime: int
        :param ProxyType: 服务类型
hostname：子域名模式
instance：实例模式
        :type ProxyType: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.ProxyName = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.SessionPersistTime = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyResponse(AbstractModel):
    """ModifyApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param Proto: 协议，取值为TCP或者UDP
        :type Proto: str
        :param Port: 端口，支持格式：
80：80端口
81-90：81至90端口
        :type Port: list of str
        :param OriginType: 源站类型，取值：
custom：手动添加
origins：源站组
        :type OriginType: str
        :param OriginValue: 源站信息：
当OriginType=custom时，表示一个或多个源站，如：
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]

当OriginType=origins时，包含一个元素，表示源站组ID，如：
OriginValue=["origin-xxx"]
        :type OriginValue: list of str
        :param ForwardClientIp: 传递客户端IP，当Proto=TCP时，取值：
TOA：TOA
PPV1: Proxy Protocol传递，协议版本V1
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
当Proto=UDP时，取值：
PPV2: Proxy Protocol传递，协议版本V2
OFF：不传递
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持
        :type SessionPersist: bool
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleResponse(AbstractModel):
    """ModifyApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param Status: 状态
offline: 停用
online: 启用
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleStatusResponse(AbstractModel):
    """ModifyApplicationProxyRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param Status: 状态
offline: 停用
online: 启用
        :type Status: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyStatusResponse(AbstractModel):
    """ModifyApplicationProxyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 代理ID
        :type ProxyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyHostRequest(AbstractModel):
    """ModifyDDoSPolicyHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点id
        :type ZoneId: str
        :param Host: 二级域名
        :type Host: str
        :param AccelerateType: 加速开关 on-开启加速；off-关闭加速（AccelerateType：on，SecurityType：on，安全加速，未开防护增强；AccelerateType：off，SecurityType：on，安全加速，开启防护增强；AccelerateType：on，SecurityType：off，内容加速，未开防护增强）
        :type AccelerateType: str
        :param PolicyId: 策略id
        :type PolicyId: int
        :param SecurityType: 安全开关 on-开启安全；off-关闭安全（AccelerateType：on，SecurityType：on，安全加速，未开防护增强；AccelerateType：off，SecurityType：on，安全加速，开启防护增强；AccelerateType：on，SecurityType：off，内容加速，未开防护增强）
        :type SecurityType: str
        """
        self.ZoneId = None
        self.Host = None
        self.AccelerateType = None
        self.PolicyId = None
        self.SecurityType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        self.AccelerateType = params.get("AccelerateType")
        self.PolicyId = params.get("PolicyId")
        self.SecurityType = params.get("SecurityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyHostResponse(AbstractModel):
    """ModifyDDoSPolicyHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param Host: 修改成功的host
        :type Host: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Host = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略组ID
        :type PolicyId: int
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param DdosRule: DDoS具体防护配置
        :type DdosRule: :class:`tencentcloud.teo.v20220106.models.DdosRule`
        """
        self.PolicyId = None
        self.ZoneId = None
        self.DdosRule = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
        if params.get("DdosRule") is not None:
            self.DdosRule = DdosRule()
            self.DdosRule._deserialize(params.get("DdosRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyResponse(AbstractModel):
    """ModifyDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略组ID
        :type PolicyId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param CertId: 默认证书ID
        :type CertId: str
        :param Status: 证书状态
deployed: 部署证书
disabled:禁用证书
失败状态下重新deployed即可重试失败
        :type Status: str
        """
        self.ZoneId = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultCertificateResponse(AbstractModel):
    """ModifyDefaultCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDnsRecordRequest(AbstractModel):
    """ModifyDnsRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名称
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        :param Mode: 代理模式
        :type Mode: str
        """
        self.Id = None
        self.ZoneId = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnsRecordResponse(AbstractModel):
    """ModifyDnsRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 记录 ID
        :type Id: str
        :param Type: 记录类型
        :type Type: str
        :param Name: 记录名称
        :type Name: str
        :param Content: 记录内容
        :type Content: str
        :param Ttl: 生存时间值
        :type Ttl: int
        :param Priority: 优先级
        :type Priority: int
        :param Mode: 代理模式
        :type Mode: str
        :param Status: 解析状态
        :type Status: str
        :param Cname: CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Locked: 锁定状态
        :type Locked: bool
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param ZoneId: 站点 ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.Content = None
        self.Ttl = None
        self.Priority = None
        self.Mode = None
        self.Status = None
        self.Cname = None
        self.Locked = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.ZoneName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        self.Ttl = params.get("Ttl")
        self.Priority = params.get("Priority")
        self.Mode = params.get("Mode")
        self.Status = params.get("Status")
        self.Cname = params.get("Cname")
        self.Locked = params.get("Locked")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.RequestId = params.get("RequestId")


class ModifyDnssecRequest(AbstractModel):
    """ModifyDnssec请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Status: DNSSEC 状态
- enabled 开启
- disabled 关闭
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDnssecResponse(AbstractModel):
    """ModifyDnssec返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Status: DNSSEC 状态
- enabled 开启
- disabled 关闭
        :type Status: str
        :param Dnssec: DNSSEC 相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Dnssec: :class:`tencentcloud.teo.v20220106.models.DnssecInfo`
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.Dnssec = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        if params.get("Dnssec") is not None:
            self.Dnssec = DnssecInfo()
            self.Dnssec._deserialize(params.get("Dnssec"))
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: Zone ID
        :type ZoneId: str
        :param Hosts: 本次变更的域名
        :type Hosts: list of str
        :param CertInfo: 证书信息, 只需要传入 CertId 即可, 如果为空, 则使用默认证书
        :type CertInfo: list of ServerCertInfo
        """
        self.ZoneId = None
        self.Hosts = None
        self.CertInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsCertificateResponse(AbstractModel):
    """ModifyHostsCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingRequest(AbstractModel):
    """ModifyLoadBalancing请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param Type: 代理模式：
dns_only: 仅DNS
proxied: 开启代理
        :type Type: str
        :param OriginId: 使用的源站组ID
        :type OriginId: list of str
        :param TTL: 当Type=dns_only表示DNS的TTL时间
        :type TTL: int
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Type = None
        self.OriginId = None
        self.TTL = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Type = params.get("Type")
        self.OriginId = params.get("OriginId")
        self.TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingResponse(AbstractModel):
    """ModifyLoadBalancing返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancingStatusRequest(AbstractModel):
    """ModifyLoadBalancingStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param Status: 状态
online: 启用
offline: 停用
        :type Status: str
        """
        self.ZoneId = None
        self.LoadBalancingId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancingStatusResponse(AbstractModel):
    """ModifyLoadBalancingStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param LoadBalancingId: 负载均衡ID
        :type LoadBalancingId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancingId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancingId = params.get("LoadBalancingId")
        self.RequestId = params.get("RequestId")


class ModifyOriginGroupRequest(AbstractModel):
    """ModifyOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param OriginName: 源站组名称
        :type OriginName: str
        :param Type: 配置类型，当OriginType=self 时，需要填写：
area: 按区域配置
weight: 按权重配置
当OriginType=third_party/cos 时，不需要填写
        :type Type: str
        :param Record: 源站记录
        :type Record: list of OriginRecord
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param OriginType: 源站类型
self：自有源站
third_party：第三方源站
cos：腾讯云COS源站
        :type OriginType: str
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.ZoneId = None
        self.OriginType = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.ZoneId = params.get("ZoneId")
        self.OriginType = params.get("OriginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOriginGroupResponse(AbstractModel):
    """ModifyOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param Entity: 二级域名/应用名
        :type Entity: str
        :param Config: 安全配置
        :type Config: :class:`tencentcloud.teo.v20220106.models.SecurityConfig`
        """
        self.ZoneId = None
        self.Entity = None
        self.Config = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        if params.get("Config") is not None:
            self.Config = SecurityConfig()
            self.Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneCnameSpeedUpRequest(AbstractModel):
    """ModifyZoneCnameSpeedUp请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Status: CNAME 加速状态
- enabled 开启
- disabled 关闭
        :type Status: str
        """
        self.Id = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneCnameSpeedUpResponse(AbstractModel):
    """ModifyZoneCnameSpeedUp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Status: CNAME 加速状态
- enabled 开启
- disabled 关闭
        :type Status: str
        :param ModifiedOn: 更新时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID，用于唯一标识站点信息
        :type Id: str
        :param Type: 站点接入方式
- full NS 接入
- partial CNAME 接入
        :type Type: str
        :param VanityNameServers: 自定义站点信息
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        """
        self.Id = None
        self.Type = None
        self.VanityNameServers = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneResponse(AbstractModel):
    """ModifyZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param OriginalNameServers: 站点当前使用的 NS
        :type OriginalNameServers: list of str
        :param Status: 站点状态
- pending 未接入 NS
- active 已接入 NS
- moved NS 已切走
        :type Status: str
        :param Type: 站点接入方式
- full NS 接入
- partial CNAME 接入
        :type Type: str
        :param NameServers: 腾讯云分配的 NS 列表
        :type NameServers: list of str
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param ModifiedOn: 修改时间
        :type ModifiedOn: str
        :param CnameStatus: cname 接入状态
- finished 站点验证完成
- pending 站点验证中
注意：此字段可能返回 null，表示取不到有效值。
        :type CnameStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.Status = None
        self.Type = None
        self.NameServers = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.CnameStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.NameServers = params.get("NameServers")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.CnameStatus = params.get("CnameStatus")
        self.RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 待变更的站点ID
        :type ZoneId: str
        :param Cache: 缓存过期时间配置
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: 节点缓存键配置
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: 浏览器缓存配置
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: 离线缓存
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: Quic访问
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: POST请求传输配置
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: 智能压缩配置
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: http2回源配置
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制https跳转配置
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: Https 加速配置
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: 源站配置
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: 智能加速配置
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param WebSocket: WebSocket配置
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: 客户端IP回源请求头配置
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: 缓存预刷新配置
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        """
        self.ZoneId = None
        self.Cache = None
        self.CacheKey = None
        self.MaxAge = None
        self.OfflineCache = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.Https = None
        self.Origin = None
        self.SmartRouting = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostMaxSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self.UpstreamHttp2 = UpstreamHttp2()
            self.UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneSettingResponse(AbstractModel):
    """ModifyZoneSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Paused: 站点状态
- false 开启站点
- true 关闭站点
        :type Paused: bool
        """
        self.Id = None
        self.Paused = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Paused = params.get("Paused")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneStatusResponse(AbstractModel):
    """ModifyZoneStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 站点 ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param Paused: 站点状态
- false 开启站点
- true 关闭站点
        :type Paused: bool
        :param ModifiedOn: 更新时间
        :type ModifiedOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Name = None
        self.Paused = None
        self.ModifiedOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Paused = params.get("Paused")
        self.ModifiedOn = params.get("ModifiedOn")
        self.RequestId = params.get("RequestId")


class OfflineCache(AbstractModel):
    """离线缓存是否开启

    """

    def __init__(self):
        r"""
        :param Switch: on | off, 离线缓存是否开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """源站配置。

    """

    def __init__(self):
        r"""
        :param OriginPullProtocol: 回源协议配置
http：强制 http 回源
follow：协议跟随回源
https：强制 https 回源，https 回源时仅支持源站 443 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        """
        self.OriginPullProtocol = None


    def _deserialize(self, params):
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCheckOriginStatus(AbstractModel):
    """源站健康检查，源站状态信息

    """

    def __init__(self):
        r"""
        :param Status: healthy: 健康，unhealthy: 不健康，process: 探测中
        :type Status: str
        :param Host: host列表，源站组不健康时存在值
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: list of str
        """
        self.Status = None
        self.Host = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginFilter(AbstractModel):
    """源站组查询过滤参数

    """

    def __init__(self):
        r"""
        :param Name: 要过滤的字段，支持：name
        :type Name: str
        :param Value: 要过滤的值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroup(AbstractModel):
    """源站组信息

    """

    def __init__(self):
        r"""
        :param OriginId: 源站组ID
        :type OriginId: str
        :param OriginName: 源站组名称
        :type OriginName: str
        :param Type: 源站组配置类型
area：表示按照Record记录中的Area字段进行按客户端IP所在区域回源。
weight：表示按照Record记录中的Weight字段进行按权重回源。
        :type Type: str
        :param Record: 记录
        :type Record: list of OriginRecord
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ZoneId: 站点ID
        :type ZoneId: str
        :param ZoneName: 站点名称
        :type ZoneName: str
        :param OriginType: 源站类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param ApplicationProxyUsed: 当前源站组是否被四层代理使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationProxyUsed: bool
        :param LoadBalancingUsed: 当前源站组是否被负载均衡使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancingUsed: bool
        :param Status: 源站状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.teo.v20220106.models.OriginCheckOriginStatus`
        :param LoadBalancingUsedType: 使用当前源站组的负载均衡的类型：
none：未被使用
dns_only：被仅DNS类型负载均衡使用
proxied：被代理加速类型负载均衡使用
both：同时被仅DNS和代理加速类型负载均衡使用
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancingUsedType: str
        """
        self.OriginId = None
        self.OriginName = None
        self.Type = None
        self.Record = None
        self.UpdateTime = None
        self.ZoneId = None
        self.ZoneName = None
        self.OriginType = None
        self.ApplicationProxyUsed = None
        self.LoadBalancingUsed = None
        self.Status = None
        self.LoadBalancingUsedType = None


    def _deserialize(self, params):
        self.OriginId = params.get("OriginId")
        self.OriginName = params.get("OriginName")
        self.Type = params.get("Type")
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.Record.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginType = params.get("OriginType")
        self.ApplicationProxyUsed = params.get("ApplicationProxyUsed")
        self.LoadBalancingUsed = params.get("LoadBalancingUsed")
        if params.get("Status") is not None:
            self.Status = OriginCheckOriginStatus()
            self.Status._deserialize(params.get("Status"))
        self.LoadBalancingUsedType = params.get("LoadBalancingUsedType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecord(AbstractModel):
    """源站组记录

    """

    def __init__(self):
        r"""
        :param Record: 记录值
        :type Record: str
        :param Area: 当源站配置类型Type=area时，表示区域
为空表示默认区域
        :type Area: list of str
        :param Weight: 当源站配置类型Type=weight时，表示权重
取值范围为[1-100]
源站组内多个源站权重总和应为100
        :type Weight: int
        :param Port: 端口
        :type Port: int
        :param RecordId: 记录ID
        :type RecordId: str
        :param Private: 是否私有鉴权
当源站类型OriginType=third_part时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Private: bool
        :param PrivateParameter: 私有鉴权参数
当源站类型Private=true时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateParameter: list of OriginRecordPrivateParameter
        """
        self.Record = None
        self.Area = None
        self.Weight = None
        self.Port = None
        self.RecordId = None
        self.Private = None
        self.PrivateParameter = None


    def _deserialize(self, params):
        self.Record = params.get("Record")
        self.Area = params.get("Area")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.RecordId = params.get("RecordId")
        self.Private = params.get("Private")
        if params.get("PrivateParameter") is not None:
            self.PrivateParameter = []
            for item in params.get("PrivateParameter"):
                obj = OriginRecordPrivateParameter()
                obj._deserialize(item)
                self.PrivateParameter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecordPrivateParameter(AbstractModel):
    """源站记录私有鉴权参数

    """

    def __init__(self):
        r"""
        :param Name: 私有鉴权参数名称：
"AccessKeyId"：Access Key ID
"SecretAccessKey"：Secret Access Key
        :type Name: str
        :param Value: 私有鉴权参数数值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortraitManagedRuleDetail(AbstractModel):
    """用户画像规则详情

    """

    def __init__(self):
        r"""
        :param RuleId: 规则唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param Description: 规则的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param RuleTypeName: 规则所属类型的名字, botdb(用户画像)
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTypeName: str
        :param ClassificationId: 规则内的功能分类Id(扫描器，Bot行为等)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationId: int
        :param Status: 规则当前所属动作状态(block, alg, ...)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.RuleId = None
        self.Description = None
        self.RuleTypeName = None
        self.ClassificationId = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.ClassificationId = params.get("ClassificationId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostMaxSize(AbstractModel):
    """POST请求上传文件流式传输最大限制

    """

    def __init__(self):
        r"""
        :param Switch: 是调整POST请求限制，平台默认为32MB。
关闭：off，
开启：on。
        :type Switch: str
        :param MaxSize: 最大限制，取值在1MB和500MB之间。单位字节
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self.Switch = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCondition(AbstractModel):
    """查询条件

    """

    def __init__(self):
        r"""
        :param Key: 维度
        :type Key: str
        :param Operator: 操作符
        :type Operator: str
        :param Value: 维度值
        :type Value: list of str
        """
        self.Key = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryString(AbstractModel):
    """CacheKey中包含请求参数

    """

    def __init__(self):
        r"""
        :param Switch: on | off CacheKey是否由QueryString组成
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Action: includeCustom:使用部分url参数
excludeCustom:排除部分url参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param Value: 使用/排除的url参数数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
        self.Switch = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """Quic配置项

    """

    def __init__(self):
        r"""
        :param Switch: 是否启动Quic配置
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitConfig(AbstractModel):
    """RateLimit配置

    """

    def __init__(self):
        r"""
        :param Switch: 开关
        :type Switch: str
        :param UserRules: 用户规则
        :type UserRules: list of RateLimitUserRule
        :param Template: 默认模板
注意：此字段可能返回 null，表示取不到有效值。
        :type Template: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplate`
        :param Intelligence: 智能客户端过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type Intelligence: :class:`tencentcloud.teo.v20220106.models.RateLimitIntelligence`
        """
        self.Switch = None
        self.UserRules = None
        self.Template = None
        self.Intelligence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("UserRules") is not None:
            self.UserRules = []
            for item in params.get("UserRules"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self.UserRules.append(obj)
        if params.get("Template") is not None:
            self.Template = RateLimitTemplate()
            self.Template._deserialize(params.get("Template"))
        if params.get("Intelligence") is not None:
            self.Intelligence = RateLimitIntelligence()
            self.Intelligence._deserialize(params.get("Intelligence"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitIntelligence(AbstractModel):
    """智能客户端过滤

    """

    def __init__(self):
        r"""
        :param Switch: 功能开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Action: 执行动作 monitor(观察), alg(挑战)
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        """
        self.Switch = None
        self.Action = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplate(AbstractModel):
    """速率限制模板

    """

    def __init__(self):
        r"""
        :param Mode: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param Detail: 模板值详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplateDetail`
        """
        self.Mode = None
        self.Detail = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        if params.get("Detail") is not None:
            self.Detail = RateLimitTemplateDetail()
            self.Detail._deserialize(params.get("Detail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplateDetail(AbstractModel):
    """模板当前详细配置

    """

    def __init__(self):
        r"""
        :param Mode: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param ID: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param Action: 处置动作
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param PunishTime: 惩罚时间，秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param Threshold: 阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: int
        :param Period: 统计周期
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: int
        """
        self.Mode = None
        self.ID = None
        self.Action = None
        self.PunishTime = None
        self.Threshold = None
        self.Period = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.ID = params.get("ID")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitUserRule(AbstractModel):
    """RateLimit规则

    """

    def __init__(self):
        r"""
        :param Threshold: RateLimit统计阈值
        :type Threshold: int
        :param Period: RateLimit统计时间
        :type Period: int
        :param RuleName: 规则名
        :type RuleName: str
        :param Action: 动作：monitor(观察), drop(拦截)
        :type Action: str
        :param PunishTime: 惩罚时长
        :type PunishTime: int
        :param PunishTimeUnit: 处罚时长单位，second
        :type PunishTimeUnit: str
        :param RuleStatus: 规则状态
        :type RuleStatus: str
        :param Conditions: 规则
        :type Conditions: list of ACLCondition
        :param RulePriority: 规则权重
        :type RulePriority: int
        :param RuleID: 规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param FreqFields: 过滤词
注意：此字段可能返回 null，表示取不到有效值。
        :type FreqFields: list of str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Threshold = None
        self.Period = None
        self.RuleName = None
        self.Action = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.RuleStatus = None
        self.Conditions = None
        self.RulePriority = None
        self.RuleID = None
        self.FreqFields = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ACLCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.RuleID = params.get("RuleID")
        self.FreqFields = params.get("FreqFields")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimZoneResponse(AbstractModel):
    """ReclaimZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 站点名称
        :type Name: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RequestId = params.get("RequestId")


class ScanDnsRecordsRequest(AbstractModel):
    """ScanDnsRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID
        :type ZoneId: str
        """
        self.ZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanDnsRecordsResponse(AbstractModel):
    """ScanDnsRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 扫描状态
- doing 扫描中
- done 扫描完成
        :type Status: str
        :param RecordsAdded: 扫描后添加的记录数
        :type RecordsAdded: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RecordsAdded = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RecordsAdded = params.get("RecordsAdded")
        self.RequestId = params.get("RequestId")


class SecEntry(AbstractModel):
    """安全数据Entry返回值

    """

    def __init__(self):
        r"""
        :param Key: Entry的Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: Entry的Value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of SecEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = SecEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntryValue(AbstractModel):
    """安全数据Entry对应的值

    """

    def __init__(self):
        r"""
        :param Metric: 指标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param Detail: 指标数据明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of TimingDataItem
        :param Max: 最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: int
        :param Avg: 平均值
注意：此字段可能返回 null，表示取不到有效值。
        :type Avg: float
        :param Sum: 数据总和
注意：此字段可能返回 null，表示取不到有效值。
        :type Sum: float
        """
        self.Metric = None
        self.Detail = None
        self.Max = None
        self.Avg = None
        self.Sum = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityConfig(AbstractModel):
    """安全配置

    """

    def __init__(self):
        r"""
        :param WafConfig: 门神配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WafConfig: :class:`tencentcloud.teo.v20220106.models.WafConfig`
        :param RateLimitConfig: RateLimit配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220106.models.RateLimitConfig`
        :param DdosConfig: DDoS配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosConfig: :class:`tencentcloud.teo.v20220106.models.DDoSConfig`
        :param AclConfig: ACL配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AclConfig: :class:`tencentcloud.teo.v20220106.models.AclConfig`
        :param BotConfig: Bot配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BotConfig: :class:`tencentcloud.teo.v20220106.models.BotConfig`
        :param SwitchConfig: 总开关
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchConfig: :class:`tencentcloud.teo.v20220106.models.SwitchConfig`
        :param IpTableConfig: IP黑白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTableConfig: :class:`tencentcloud.teo.v20220106.models.IpTableConfig`
        """
        self.WafConfig = None
        self.RateLimitConfig = None
        self.DdosConfig = None
        self.AclConfig = None
        self.BotConfig = None
        self.SwitchConfig = None
        self.IpTableConfig = None


    def _deserialize(self, params):
        if params.get("WafConfig") is not None:
            self.WafConfig = WafConfig()
            self.WafConfig._deserialize(params.get("WafConfig"))
        if params.get("RateLimitConfig") is not None:
            self.RateLimitConfig = RateLimitConfig()
            self.RateLimitConfig._deserialize(params.get("RateLimitConfig"))
        if params.get("DdosConfig") is not None:
            self.DdosConfig = DDoSConfig()
            self.DdosConfig._deserialize(params.get("DdosConfig"))
        if params.get("AclConfig") is not None:
            self.AclConfig = AclConfig()
            self.AclConfig._deserialize(params.get("AclConfig"))
        if params.get("BotConfig") is not None:
            self.BotConfig = BotConfig()
            self.BotConfig._deserialize(params.get("BotConfig"))
        if params.get("SwitchConfig") is not None:
            self.SwitchConfig = SwitchConfig()
            self.SwitchConfig._deserialize(params.get("SwitchConfig"))
        if params.get("IpTableConfig") is not None:
            self.IpTableConfig = IpTableConfig()
            self.IpTableConfig._deserialize(params.get("IpTableConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityEntity(AbstractModel):
    """安全防护实例

    """

    def __init__(self):
        r"""
        :param AppId: 用户appid
        :type AppId: int
        :param ZoneId: 一级域名
        :type ZoneId: str
        :param Entity: 二级域名
        :type Entity: str
        :param EntityType: 类型 domain/application
        :type EntityType: str
        """
        self.AppId = None
        self.ZoneId = None
        self.Entity = None
        self.EntityType = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.EntityType = params.get("EntityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCertInfo(AbstractModel):
    """https 服务端证书配置

    """

    def __init__(self):
        r"""
        :param CertId: 服务器证书 ID, 默认证书ID, 或在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Alias: 证书备注名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Type: 证书类型:
default: 默认证书
upload:用户上传
managed:腾讯云托管
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ExpireTime: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书部署时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param Status: 部署状态:
processing: 部署中
deployed: 已部署
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShieldArea(AbstractModel):
    """DDoS防护分区

    """

    def __init__(self):
        r"""
        :param ZoneId: 一级域名id
        :type ZoneId: str
        :param PolicyId: 策略id
        :type PolicyId: int
        :param Type: 防护类型 domain/application
        :type Type: str
        :param EntityName: 四层应用名
注意：此字段可能返回 null，表示取不到有效值。
        :type EntityName: str
        :param Application: 7层域名参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Application: list of DDoSApplication
        :param TcpNum: 四层tcp转发规则数
注意：此字段可能返回 null，表示取不到有效值。
        :type TcpNum: int
        :param UdpNum: 四层udp转发规则数
注意：此字段可能返回 null，表示取不到有效值。
        :type UdpNum: int
        :param Entity: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Entity: str
        :param Share: 是否为共享资源客户，注意共享资源用户不可以切换代理模式，true-是；false-否
注意：此字段可能返回 null，表示取不到有效值。
        :type Share: bool
        """
        self.ZoneId = None
        self.PolicyId = None
        self.Type = None
        self.EntityName = None
        self.Application = None
        self.TcpNum = None
        self.UdpNum = None
        self.Entity = None
        self.Share = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PolicyId = params.get("PolicyId")
        self.Type = params.get("Type")
        self.EntityName = params.get("EntityName")
        if params.get("Application") is not None:
            self.Application = []
            for item in params.get("Application"):
                obj = DDoSApplication()
                obj._deserialize(item)
                self.Application.append(obj)
        self.TcpNum = params.get("TcpNum")
        self.UdpNum = params.get("UdpNum")
        self.Entity = params.get("Entity")
        self.Share = params.get("Share")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartRouting(AbstractModel):
    """智能加速配置

    """

    def __init__(self):
        r"""
        :param Switch: 智能加速配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchConfig(AbstractModel):
    """功能总开关

    """

    def __init__(self):
        r"""
        :param WebSwitch: Web类型的安全总开关：Web基础防护，自定义规则，速率限制
        :type WebSwitch: str
        """
        self.WebSwitch = None


    def _deserialize(self, params):
        self.WebSwitch = params.get("WebSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签配置

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class Task(AbstractModel):
    """内容管理任务结果

    """

    def __init__(self):
        r"""
        :param JobId: 任务ID
        :type JobId: str
        :param Status: 状态
        :type Status: str
        :param Target: 资源
        :type Target: str
        :param Type: 任务类型
        :type Type: str
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param UpdateTime: 任务完成时间
        :type UpdateTime: str
        """
        self.JobId = None
        self.Status = None
        self.Target = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Status = params.get("Status")
        self.Target = params.get("Target")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataItem(AbstractModel):
    """统计曲线数据项

    """

    def __init__(self):
        r"""
        :param Timestamp: 秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param Value: 数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        """
        self.Timestamp = None
        self.Value = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataRecord(AbstractModel):
    """L7数据分析时序数据

    """

    def __init__(self):
        r"""
        :param TypeKey: 查询维度值
        :type TypeKey: str
        :param TypeValue: 详细时序数据
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeValue: list of TimingTypeValue
        """
        self.TypeKey = None
        self.TypeValue = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self.TypeValue = []
            for item in params.get("TypeValue"):
                obj = TimingTypeValue()
                obj._deserialize(item)
                self.TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingTypeValue(AbstractModel):
    """时序类型详细数据

    """

    def __init__(self):
        r"""
        :param Sum: 数据和
注意：此字段可能返回 null，表示取不到有效值。
        :type Sum: int
        :param Max: 最大
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: int
        :param Avg: 平均
注意：此字段可能返回 null，表示取不到有效值。
        :type Avg: int
        :param MetricName: 指标名
        :type MetricName: str
        :param DetailData: 废弃字段，即将下线，请使用Detail字段
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailData: list of int
        :param Detail: 详细数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of TimingDataItem
        """
        self.Sum = None
        self.Max = None
        self.Avg = None
        self.MetricName = None
        self.DetailData = None
        self.Detail = None


    def _deserialize(self, params):
        self.Sum = params.get("Sum")
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.MetricName = params.get("MetricName")
        self.DetailData = params.get("DetailData")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDataRecord(AbstractModel):
    """七层数据分析类top数据

    """

    def __init__(self):
        r"""
        :param TypeKey: 查询维度值
        :type TypeKey: str
        :param DetailData: top数据排行
注意：此字段可能返回 null，表示取不到有效值。
        :type DetailData: list of TopDetailData
        """
        self.TypeKey = None
        self.DetailData = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """用于对top数据排序的结构体

    """

    def __init__(self):
        r"""
        :param Key: 字段名
        :type Key: str
        :param Value: 字段值
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
        


class TopNEntry(AbstractModel):
    """TopN entry

    """

    def __init__(self):
        r"""
        :param Key: Entry key
        :type Key: str
        :param Value: TopN数据
        :type Value: list of TopNEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = TopNEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopNEntryValue(AbstractModel):
    """TopN数据Entry

    """

    def __init__(self):
        r"""
        :param Name: Entry的name
        :type Name: str
        :param Count: 数量
        :type Count: int
        """
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHttp2(AbstractModel):
    """Http2回源配置

    """

    def __init__(self):
        r"""
        :param Switch: http2回源配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServers(AbstractModel):
    """自定义 nameservers

    """

    def __init__(self):
        r"""
        :param Switch: 自定义 ns 开关
- on 开启
- off 关闭
        :type Switch: str
        :param Servers: 自定义 ns 列表
        :type Servers: list of str
        """
        self.Switch = None
        self.Servers = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Servers = params.get("Servers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServersIps(AbstractModel):
    """自定义名字服务器 IP 信息

    """

    def __init__(self):
        r"""
        :param Name: 自定义名字服务器名称
        :type Name: str
        :param IPv4: 自定义名字服务器 IPv4 地址
        :type IPv4: str
        """
        self.Name = None
        self.IPv4 = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IPv4 = params.get("IPv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafConfig(AbstractModel):
    """门神配置

    """

    def __init__(self):
        r"""
        :param Switch: 开关
        :type Switch: str
        :param Level: 防护级别，loose/normal/strict/stricter/custom
        :type Level: str
        :param Mode: 模式 block-阻断；observe-观察模式；close-关闭
        :type Mode: str
        :param WafRules: 门神黑白名单
        :type WafRules: :class:`tencentcloud.teo.v20220106.models.WafRule`
        :param AiRule: AI规则引擎防护
注意：此字段可能返回 null，表示取不到有效值。
        :type AiRule: :class:`tencentcloud.teo.v20220106.models.AiRule`
        """
        self.Switch = None
        self.Level = None
        self.Mode = None
        self.WafRules = None
        self.AiRule = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Level = params.get("Level")
        self.Mode = params.get("Mode")
        if params.get("WafRules") is not None:
            self.WafRules = WafRule()
            self.WafRules._deserialize(params.get("WafRules"))
        if params.get("AiRule") is not None:
            self.AiRule = AiRule()
            self.AiRule._deserialize(params.get("AiRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafRule(AbstractModel):
    """Waf规则

    """

    def __init__(self):
        r"""
        :param BlockRuleIDs: 黑名单
        :type BlockRuleIDs: list of int
        :param Switch: id的开关
        :type Switch: str
        :param ObserveRuleIDs: 观察模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ObserveRuleIDs: list of int
        """
        self.BlockRuleIDs = None
        self.Switch = None
        self.ObserveRuleIDs = None


    def _deserialize(self, params):
        self.BlockRuleIDs = params.get("BlockRuleIDs")
        self.Switch = params.get("Switch")
        self.ObserveRuleIDs = params.get("ObserveRuleIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebAttackEvent(AbstractModel):
    """Web拦截事件

    """

    def __init__(self):
        r"""
        :param ClientIp: 客户端ip
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIp: str
        :param AttackUrl: 攻击URL
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackUrl: str
        :param AttackTime: 攻击时间 单位为s
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackTime: int
        """
        self.ClientIp = None
        self.AttackUrl = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.AttackUrl = params.get("AttackUrl")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebEventData(AbstractModel):
    """web事件数据

    """

    def __init__(self):
        r"""
        :param List: 攻击事件数据集合
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of WebAttackEvent
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = WebAttackEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebLogData(AbstractModel):
    """web攻击日志Data

    """

    def __init__(self):
        r"""
        :param List: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of WebLogs
        :param PageNo: 当前页
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 每页展示条数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSize: int
        """
        self.List = None
        self.PageNo = None
        self.PageSize = None
        self.Pages = None
        self.TotalSize = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = WebLogs()
                obj._deserialize(item)
                self.List.append(obj)
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Pages = params.get("Pages")
        self.TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebLogs(AbstractModel):
    """web攻击日志

    """

    def __init__(self):
        r"""
        :param AttackContent: 攻击内容
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackContent: str
        :param AttackIp: 攻击IP
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackIp: str
        :param AttackType: 攻击类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackType: str
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Msuuid: uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Msuuid: str
        :param RequestMethod: 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestMethod: str
        :param RequestUri: 请求URI
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestUri: str
        :param RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param RuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param SipCountryCode: IP所在国家
注意：此字段可能返回 null，表示取不到有效值。
        :type SipCountryCode: str
        :param EventId: 事件id
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param DisposalMethod: 处置方式
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalMethod: str
        :param HttpLog: http_log
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpLog: str
        :param Ua: user agent
注意：此字段可能返回 null，表示取不到有效值。
        :type Ua: str
        :param AttackTime: 攻击时间，为保持统一，原参数time更名为AttackTime
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackTime: int
        """
        self.AttackContent = None
        self.AttackIp = None
        self.AttackType = None
        self.Domain = None
        self.Msuuid = None
        self.RequestMethod = None
        self.RequestUri = None
        self.RiskLevel = None
        self.RuleId = None
        self.SipCountryCode = None
        self.EventId = None
        self.DisposalMethod = None
        self.HttpLog = None
        self.Ua = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.AttackContent = params.get("AttackContent")
        self.AttackIp = params.get("AttackIp")
        self.AttackType = params.get("AttackType")
        self.Domain = params.get("Domain")
        self.Msuuid = params.get("Msuuid")
        self.RequestMethod = params.get("RequestMethod")
        self.RequestUri = params.get("RequestUri")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleId = params.get("RuleId")
        self.SipCountryCode = params.get("SipCountryCode")
        self.EventId = params.get("EventId")
        self.DisposalMethod = params.get("DisposalMethod")
        self.HttpLog = params.get("HttpLog")
        self.Ua = params.get("Ua")
        self.AttackTime = params.get("AttackTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket配置

    """

    def __init__(self):
        r"""
        :param Switch: WebSocket 超时配置开关, 开关为off时，平台仍支持WebSocket连接，此时超时时间默认为15秒，若需要调整超时时间，将开关置为on.
        :type Switch: str
        :param Timeout: 设置超时时间，单位为秒，最大超时时间120秒。
        :type Timeout: int
        """
        self.Switch = None
        self.Timeout = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """站点信息

    """

    def __init__(self):
        r"""
        :param Id: 站点ID
        :type Id: str
        :param Name: 站点名称
        :type Name: str
        :param OriginalNameServers: 站点当前使用的 NS 列表
        :type OriginalNameServers: list of str
        :param NameServers: 腾讯云分配的 NS 列表
        :type NameServers: list of str
        :param Status: 站点状态
- active：NS 已切换
- pending：NS 未切换
- moved：NS 已切走
- deactivated：被封禁
        :type Status: str
        :param Type: 站点接入方式
- full：NS 接入
- partial：CNAME 接入
        :type Type: str
        :param Paused: 站点是否关闭
        :type Paused: bool
        :param CreatedOn: 站点创建时间
        :type CreatedOn: str
        :param ModifiedOn: 站点修改时间
        :type ModifiedOn: str
        :param CnameStatus: cname 接入状态
- finished 站点已验证
- pending 站点验证中
注意：此字段可能返回 null，表示取不到有效值。
        :type CnameStatus: str
        :param Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.CnameStatus = None
        self.Tags = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.CnameStatus = params.get("CnameStatus")
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
        


class ZoneFilter(AbstractModel):
    """站点查询过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名，支持的列表如下：
- name: 站点名。
- status: 站点状态
- tagKey: 标签键
- tagValue: 标签值
        :type Name: str
        :param Values: 过滤字段值
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为name。模糊查询时，Values长度最大为1
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        