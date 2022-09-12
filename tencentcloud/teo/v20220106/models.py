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
        :param RuleName: 规则名。
        :type RuleName: str
        :param Action: 处罚动作。
1. trans 放行
2. drop 拦截
3. monitor 观察
4. ban IP封禁
5. redirect 重定向
6. page 指定页面
7. alg Javascript挑战
        :type Action: str
        :param RuleStatus: 规则状态。
1. on 规则生效
2. off 规则失效
        :type RuleStatus: str
        :param Conditions: ACL规则。
        :type Conditions: list of ACLCondition
        :param RulePriority: 规则优先级，0-100。
        :type RulePriority: int
        :param RuleID: 规则id。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param PunishTime: ip封禁的惩罚时间，0-2天
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param PunishTimeUnit: ip封禁的惩罚时间单位。
1. second 秒
2. 分钟 minutes
3. hour 小时
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTimeUnit: str
        :param PageId: 自定义返回页面的实例id。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: int
        :param Name: 自定义返回页面的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param RedirectUrl: 重定向时候的地址，必须为本用户接入的站点子域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param ResponseCode: 重定向时候的返回码。
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
        self.PageId = None
        self.Name = None
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
        self.PageId = params.get("PageId")
        self.Name = params.get("Name")
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
        :param Switch: 开关。
1. on 开启
2. off 关闭
        :type Switch: str
        :param UserRules: 自定义-用户规则。
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
        :param Mode: AI规则引擎状态，取值有：
<li> smart_status_close：关闭；</li>
<li> smart_status_open：拦截处置；</li>
<li> smart_status_observe：观察处置。</li>
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
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param ProxyName: 当ProxyType=hostname时，表示域名或子域名；
当ProxyType=instance时，表示代理名称。
        :type ProxyName: str
        :param PlatType: 调度模式，取值有：
<li>ip：表示Anycast IP调度；</li>
<li>domain：表示CNAME调度。</li>
        :type PlatType: str
        :param SecurityType: 是否开启安全，取值有：
<li>0：关闭安全；</li>
<li>1：开启安全。</li>
        :type SecurityType: int
        :param AccelerateType: 是否开启加速，取值有：
<li>0：关闭加速；</li>
<li>1：开启加速。</li>
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经废弃。
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经废弃。
        :type SessionPersist: bool
        :param Rule: 规则列表。
        :type Rule: list of ApplicationProxyRule
        :param Status: 状态，取值有：
<li>online：启用；</li>
<li>offline：停用；</li>
<li>progress：部署中；</li>
<li>stopping：停用中；</li>
<li>fail：部署失败/停用失败。</li>
        :type Status: str
        :param ScheduleValue: 调度信息。
        :type ScheduleValue: list of str
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param SessionPersistTime: 会话保持时间。
        :type SessionPersistTime: int
        :param ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>
        :type ProxyType: str
        :param HostId: 当ProxyType=hostname时：
表示代理加速唯一标识。
        :type HostId: str
        :param Ipv6: Ipv6访问配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220106.models.Ipv6Access`
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
默认值：overseas
        :type Area: str
        :param BanStatus: 封禁状态，取值有：
<li>banned：已封禁;</li>
<li>banning：封禁中；</li>
<li>recover：已解封；</li>
<li>recovering：解封禁中。</li>
        :type BanStatus: str
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
        self.Ipv6 = None
        self.Area = None
        self.BanStatus = None


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
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6Access()
            self.Ipv6._deserialize(params.get("Ipv6"))
        self.Area = params.get("Area")
        self.BanStatus = params.get("BanStatus")
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
        :param Proto: 协议，取值有：
<li>TCP：TCP协议；</li>
<li>UDP：UDP协议。</li>
        :type Proto: str
        :param Port: 端口，支持格式：
单个端口，如：80。
端口段，如：81-82。表示81，82两个端口。
注意：一条规则最多可填写20个端口。
        :type Port: list of str
        :param OriginType: 源站类型，取值有：
<li>custom：手动添加；</li>
<li>origins：源站组。</li>
        :type OriginType: str
        :param OriginValue: 源站信息：
当OriginType=custom时，表示一个或多个源站，如：
OriginValue=["8.8.8.8:80","9.9.9.9:80"]
OriginValue=["test.com:80"]；
当OriginType=origins时，要求有且仅有一个元素，表示源站组ID，如：
OriginValue=["origin-537f5b41-162a-11ed-abaa-525400c5da15"]。
        :type OriginValue: list of str
        :param RuleId: 规则ID。
        :type RuleId: str
        :param Status: 状态，取值有：
<li>online：启用；</li>
<li>offline：停用；</li>
<li>progress：部署中；</li>
<li>stopping：停用中；</li>
<li>fail：部署失败/停用失败。</li>
        :type Status: str
        :param ForwardClientIp: 传递客户端IP，取值有：
<li>TOA：TOA（仅Proto=TCP时可选）；</li>
<li>PPV1：Proxy Protocol传递，协议版本V1（仅Proto=TCP时可选）；</li>
<li>PPV2：Proxy Protocol传递，协议版本V2；</li>
<li>OFF：不传递。</li>
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持，取值有：
<li>true：开启；</li>
<li>false：关闭。</li>
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
        :param Switch: 开关。
1. on 开启
2. off 关闭
        :type Switch: str
        :param ManagedRule: 通用详细基础规则。
        :type ManagedRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param UaBotRule: ua基础规则。
        :type UaBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param IspBotRule: isp基础规则。
        :type IspBotRule: :class:`tencentcloud.teo.v20220106.models.BotManagedRule`
        :param PortraitRule: 用户画像规则。
        :type PortraitRule: :class:`tencentcloud.teo.v20220106.models.BotPortraitRule`
        :param IntelligenceRule: Bot智能分析。
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
        :param AttackTime: 攻击时间，采用unix秒级时间戳。
        :type AttackTime: int
        :param AttackIp: 攻击源（客户端）ip。
        :type AttackIp: str
        :param Domain: 受攻击域名。
        :type Domain: str
        :param RequestUri: URI。
        :type RequestUri: str
        :param AttackType: 当前该字段无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackType: str
        :param RequestMethod: 请求方法。
        :type RequestMethod: str
        :param AttackContent: 攻击内容。
        :type AttackContent: str
        :param RiskLevel: 当前该字段无效 。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param RuleId: 当前该字段无效 。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param SipCountryCode: IP所在国家iso-3166中alpha-2编码，编码信息请参考[ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json)。
        :type SipCountryCode: str
        :param EventId: 请求（事件）ID。
        :type EventId: str
        :param DisposalMethod: 该字段当前无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalMethod: str
        :param HttpLog: 该字段当前无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpLog: str
        :param Ua: user agent。
        :type Ua: str
        :param DetectionMethod: 该字段当前无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionMethod: str
        :param Confidence: 该字段当前无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: str
        :param Maliciousness: 该字段当前无效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Maliciousness: str
        :param RuleDetailList: 规则相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDetailList: list of SecRuleRelatedInfo
        :param Label: Bot标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
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
        self.RuleDetailList = None
        self.Label = None


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
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
        self.Label = params.get("Label")
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
        :param List: Bot攻击日志数据集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of BotLog
        :param PageNo: 分页拉取的起始页号。最小值：1。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数。
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
    """Bot 规则，下列规则ID可参考接口 DescribeBotManagedRules返回的ID信息

    """

    def __init__(self):
        r"""
        :param RuleID: 本规则的ID。
        :type RuleID: int
        :param ManagedIds: 老版本的通用规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagedIds: list of int
        :param Action: 触发规则后的处置方式。
1. drop 拦截
2. trans 放行
3. monitor 观察
4. alg Javascript挑战
        :type Action: str
        :param PunishTime: 封禁的惩罚时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param PunishTimeUnit: 封禁的惩罚时间单位。
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTimeUnit: str
        :param TransManagedIds: 放行的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransManagedIds: list of int
        :param AlgManagedIds: JS挑战的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param CapManagedIds: 数字验证码的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param MonManagedIds: 观察的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param DropManagedIds: 拦截的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        :param PageId: 自定义返回页面的实例id。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: int
        :param Name: 自定义返回页面的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param RedirectUrl: 重定向时候的地址，必须为本用户接入的站点子域名，使用URLENCODE。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param ResponseCode: 重定向时候的返回码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseCode: int
        """
        self.RuleID = None
        self.ManagedIds = None
        self.Action = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.TransManagedIds = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None
        self.PageId = None
        self.Name = None
        self.RedirectUrl = None
        self.ResponseCode = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.ManagedIds = params.get("ManagedIds")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.TransManagedIds = params.get("TransManagedIds")
        self.AlgManagedIds = params.get("AlgManagedIds")
        self.CapManagedIds = params.get("CapManagedIds")
        self.MonManagedIds = params.get("MonManagedIds")
        self.DropManagedIds = params.get("DropManagedIds")
        self.PageId = params.get("PageId")
        self.Name = params.get("Name")
        self.RedirectUrl = params.get("RedirectUrl")
        self.ResponseCode = params.get("ResponseCode")
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
        :param Switch: 本功能的开关。
1. on 开启
2. off 关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param RuleID: 本规则的ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param AlgManagedIds: JS挑战的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param CapManagedIds: 数字验证码的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param MonManagedIds: 观察的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param DropManagedIds: 拦截的规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        :param ManagedIds: 保留。
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagedIds: list of int
        :param TransManagedIds: 保留。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransManagedIds: list of int
        """
        self.Switch = None
        self.RuleID = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None
        self.ManagedIds = None
        self.TransManagedIds = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RuleID = params.get("RuleID")
        self.AlgManagedIds = params.get("AlgManagedIds")
        self.CapManagedIds = params.get("CapManagedIds")
        self.MonManagedIds = params.get("MonManagedIds")
        self.DropManagedIds = params.get("DropManagedIds")
        self.ManagedIds = params.get("ManagedIds")
        self.TransManagedIds = params.get("TransManagedIds")
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
    """CC日志

    """

    def __init__(self):
        r"""
        :param AttackTime: 攻击请求时间，采用unix秒级时间戳。
        :type AttackTime: int
        :param AttackSip: 客户端ip。
        :type AttackSip: str
        :param AttackDomain: 受攻击域名。
        :type AttackDomain: str
        :param RequestUri: URI。
        :type RequestUri: str
        :param HitCount: 命中次数。
        :type HitCount: int
        :param SipCountryCode: IP所在国家iso-3166中alpha-2编码，编码信息请参考[ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json)。
        :type SipCountryCode: str
        :param EventId: 请求（事件）ID。
        :type EventId: str
        :param DisposalMethod: 当前该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalMethod: str
        :param HttpLog: 当前该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpLog: str
        :param RuleId: 当前该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param RiskLevel: 当前该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param Ua: User Agent，仅自定义规则日志中存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ua: str
        :param RequestMethod: 请求方法，仅自定义规则日志中存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestMethod: str
        :param RuleDetailList: 规则信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDetailList: list of SecRuleRelatedInfo
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
        self.Ua = None
        self.RequestMethod = None
        self.RuleDetailList = None


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
        self.Ua = params.get("Ua")
        self.RequestMethod = params.get("RequestMethod")
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
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
        :param List: CC拦截日志数据集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of CCLog
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param Pages: 总页数。
        :type Pages: int
        :param TotalSize: 总条数。
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
        :param Cache: 缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfigCache`
        :param NoCache: 不缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCache: :class:`tencentcloud.teo.v20220106.models.CacheConfigNoCache`
        :param FollowOrigin: 遵循源站配置。
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
        :param Switch: 缓存配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param CacheTime: 缓存过期时间设置。
单位为秒，最大可设置为 365 天。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        :param IgnoreCacheControl: 是否开启强制缓存，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
        :param Switch: 遵循源站配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
        :param Switch: 不缓存配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
        :param FullUrlCache: 是否开启全路径缓存，取值有：
<li>on：开启全路径缓存（即关闭参数忽略）；</li>
<li>off：关闭全路径缓存（即开启参数忽略）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FullUrlCache: str
        :param IgnoreCase: 是否忽略大小写缓存，取值有：
<li>on：忽略；</li>
<li>off：不忽略。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param QueryString: CacheKey中包含请求参数。
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
        :param Switch: 缓存预刷新配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param Percent: 缓存预刷新百分比，取值范围：1-99。
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
    """存储客户端请求IP的头部信息配置

    """

    def __init__(self):
        r"""
        :param Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param HeaderName: 回源时，存放客户端IP的请求头名称。
为空则使用默认值：X-Forwarded-IP。
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
        :param Switch: 智能压缩配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param Algorithms: 支持的压缩算法列表，取值有：
<li>brotli：brotli算法；</li>
<li>gzip：gzip算法。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Algorithms: list of str
        """
        self.Switch = None
        self.Algorithms = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Algorithms = params.get("Algorithms")
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param ProxyName: 当ProxyType=hostname时，表示域名或子域名；
当ProxyType=instance时，表示代理名称。
        :type ProxyName: str
        :param PlatType: 调度模式，取值有：
<li>ip：表示Anycast IP调度；</li>
<li>domain：表示CNAME调度。</li>
        :type PlatType: str
        :param SecurityType: 是否开启安全，取值有：
<li>0：关闭安全；</li>
<li>1：开启安全。</li>
        :type SecurityType: int
        :param AccelerateType: 是否开启加速，取值有：
<li>0：关闭加速；</li>
<li>1：开启加速。</li>
        :type AccelerateType: int
        :param SessionPersist: 字段已经废弃。
        :type SessionPersist: bool
        :param ForwardClientIp: 字段已经废弃。
        :type ForwardClientIp: str
        :param Rule: 规则详细信息。
        :type Rule: list of ApplicationProxyRule
        :param ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>不填写使用默认值instance。
        :type ProxyType: str
        :param SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒。
不填写使用默认值600。
        :type SessionPersistTime: int
        :param Ipv6: Ipv6访问配置。
不填写表示关闭Ipv6访问。
        :type Ipv6: :class:`tencentcloud.teo.v20220106.models.Ipv6Access`
        """
        self.ZoneId = None
        self.ZoneName = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.SessionPersist = None
        self.ForwardClientIp = None
        self.Rule = None
        self.ProxyType = None
        self.SessionPersistTime = None
        self.Ipv6 = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.SessionPersist = params.get("SessionPersist")
        self.ForwardClientIp = params.get("ForwardClientIp")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        self.ProxyType = params.get("ProxyType")
        self.SessionPersistTime = params.get("SessionPersistTime")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6Access()
            self.Ipv6._deserialize(params.get("Ipv6"))
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
        :param ProxyId: 新增的四层代理应用ID。
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


class CreatePlanForZoneRequest(AbstractModel):
    """CreatePlanForZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param PlanType: 所要购买套餐的类型，取值有：
<li> sta: 全球内容分发网络（不包括中国大陆）标准版套餐； </li>
<li> sta_with_bot: 全球内容分发网络（不包括中国大陆）标准版套餐附带bot管理；</li>
<li> sta_cm: 中国大陆内容分发网络标准版套餐； </li>
<li> sta_cm_with_bot: 中国大陆内容分发网络标准版套餐附带bot管理；</li>
<li> ent: 全球内容分发网络（不包括中国大陆）企业版套餐； </li>
<li> ent_with_bot: 全球内容分发网络（不包括中国大陆）企业版套餐附带bot管理；</li>
<li> ent_cm: 中国大陆内容分发网络企业版套餐； </li>
<li> ent_cm_with_bot: 中国大陆内容分发网络企业版套餐附带bot管理。</li>当前账户可购买套餐类型请以<a href="https://tcloud4api.woa.com/document/product/1657/80124?!preview&!document=1">DescribeAvailablePlans</a>返回为准。
        :type PlanType: str
        """
        self.ZoneId = None
        self.PlanType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePlanForZoneResponse(AbstractModel):
    """CreatePlanForZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceNames: 购买的资源名字列表。
        :type ResourceNames: list of str
        :param DealNames: 购买的订单号列表。
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResourceNames = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceNames = params.get("ResourceNames")
        self.DealNames = params.get("DealNames")
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


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param RuleName: 规则名称，名称字符串长度 1～255。
        :type RuleName: str
        :param Status: 规则状态，取值有：
<li> enable: 启用； </li>
<li> disable: 未启用。</li>
        :type Status: str
        :param Rules: 规则内容。
        :type Rules: list of RuleItem
        """
        self.ZoneId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleItem()
                obj._deserialize(item)
                self.Rules.append(obj)
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
        :param RuleId: 规则 ID。
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
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
        :param DportEnd: 目的端口结束，取值范围0-65535。
        :type DportEnd: int
        :param DportStart: 目的端口开始，取值范围0-65535。
        :type DportStart: int
        :param SportEnd: 源端口结束，取值范围0-65535。
        :type SportEnd: int
        :param SportStart: 源端口开始，取值范围0-65535。
        :type SportStart: int
        :param Protocol: 协议，取值有：
<li>tcp ：tcp协议 ；</li>
<li>udp ：udp协议 ；</li>
<li>all ：全部协议 。</li>
        :type Protocol: str
        :param Action: 执行动作，取值为：
<li>drop ：丢弃 ；</li>
<li>transmit ：放行 ；</li>
<li>forward ：继续防护 。</li>
        :type Action: str
        :param Default: 是否为系统配置，取值为：
<li>0 ：修改配置 ；</li>
<li>1 ：系统默认配置 。</li>
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
        :param DropTcp: tcp协议封禁，取值有：
<li>off ：关闭 ；</li>
<li>on ：开启 。</li>
        :type DropTcp: str
        :param DropUdp: udp协议封禁，取值有：
<li>off ：关闭 ；</li>
<li>on ：开启 。</li>
        :type DropUdp: str
        :param DropIcmp: icmp协议封禁，取值有：
<li>off ：关闭 ；</li>
<li>on ：开启 。</li>
        :type DropIcmp: str
        :param DropOther: 其他协议封禁，取值有：
<li>off ：关闭 ；</li>
<li>on ：开启 。</li>
        :type DropOther: str
        :param SourceCreateLimit: 源站每秒新连接限速，取值范围0-4294967295。
        :type SourceCreateLimit: int
        :param SourceConnectLimit: 源站并发连接控制，取值范围0-4294967295。
        :type SourceConnectLimit: int
        :param DestinationCreateLimit: 目的端口每秒新连接限速，取值范围0-4294967295。
        :type DestinationCreateLimit: int
        :param DestinationConnectLimit: 目的端口并发连接控制，取值范围0-4294967295。
        :type DestinationConnectLimit: int
        :param AbnormalConnectNum: 每秒异常连接数阈值，取值范围0-4294967295。
        :type AbnormalConnectNum: int
        :param AbnormalSynRatio: 异常syn报文百分比阈值，取值范围0-100。
        :type AbnormalSynRatio: int
        :param AbnormalSynNum: 异常syn报文阈值，取值范围0-65535。
        :type AbnormalSynNum: int
        :param ConnectTimeout: 每秒连接超时检测，取值范围0-65535。
        :type ConnectTimeout: int
        :param EmptyConnectProtect: 空连接防护开启，取值有：
<li>off ：关闭 ；</li>
<li>on ：开启 。</li>
        :type EmptyConnectProtect: str
        :param UdpShard: UDP分片开关，取值有：
<li>off ：关闭 ；</li>
<li>on ：开启 。</li>
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
        :param Action: 执行动作，取值有：
<li>drop ：丢弃 ；</li>
<li>transmit ：放行 ；</li>
<li>drop_block ：丢弃并拉黑 ；</li>
<li>forward ：继续防护 。</li>
        :type Action: str
        :param Protocol: 协议，取值有：
<li>tcp ：tcp协议 ；</li>
<li>udp ：udp协议 ；</li>
<li>icmp ：icmp协议 ；</li>
<li>all ：全部协议 。</li>
        :type Protocol: str
        :param DportStart: 目标端口开始，取值范围0-65535。
        :type DportStart: int
        :param DportEnd: 目标端口结束，取值范围0-65535。
        :type DportEnd: int
        :param PacketMin: 最小包长，取值范围0-1500。
        :type PacketMin: int
        :param PacketMax: 最大包长，取值范围0-1500。
        :type PacketMax: int
        :param SportStart: 源端口开始，取值范围0-65535。
        :type SportStart: int
        :param SportEnd: 源端口结束，取值范围0-65535。
        :type SportEnd: int
        :param MatchType: 匹配方式1，【特征1】，取值有：
<li>pcre ：正则匹配 ；</li>
<li>sunday ：字符串匹配 。</li>默认为空字符串。
        :type MatchType: str
        :param IsNot: 取非判断，该参数对MatchType配合使用，【特征1】，取值有：
<li>0 ：匹配 ；</li>
<li>1 ：不匹配 。</li>
        :type IsNot: int
        :param Offset: 偏移量1，【特征1】，取值范围0-1500。
        :type Offset: int
        :param Depth: 检测包字符深度，【特征1】，取值范围1-1500。
        :type Depth: int
        :param MatchBegin: 匹配开始层级，层级参考计算机网络结构，取值有：
<li>begin_l5 ：载荷开始检测 ；</li>
<li>begin_l4 ：tcp/udp首部开始检测 ；</li>
<li>begin_l3 ：ip首部开始检测 。</li>
        :type MatchBegin: str
        :param Str: 正则或字符串匹配的内容，【特征1】。
        :type Str: str
        :param MatchType2: 匹配方式2，【特征2】，取值有：
<li>pcre ：正则匹配 ；</li>
<li>sunday ：字符串匹配 。</li>默认为空字符串。
        :type MatchType2: str
        :param IsNot2: 取非判断2，该参数对MatchType2配合使用，【特征2】，取值有：
<li>0 ：匹配 ；</li>
<li>1 ：不匹配 。</li>
        :type IsNot2: int
        :param Offset2: 偏移量2，【特征2】，取值范围0-1500。
        :type Offset2: int
        :param Depth2: 检测包字符深度，【特征2】，取值范围1-1500。
        :type Depth2: int
        :param MatchBegin2: 匹配开始层级，层级参考计算机网络结构，取值有：
<li>begin_l5 ：载荷开始检测 ；</li>
<li>begin_l4 ：tcp/udp首部开始检测；</li>
<li>begin_l3 ：ip首部开始检测 。</li>
        :type MatchBegin2: str
        :param Str2: 正则或字符串匹配的内容，【特征2】。
        :type Str2: str
        :param MatchLogic: 多特征关系，仅配置【特征1】时填 none，存在【特征2】配置可不填。
        :type MatchLogic: str
        """
        self.Action = None
        self.Protocol = None
        self.DportStart = None
        self.DportEnd = None
        self.PacketMin = None
        self.PacketMax = None
        self.SportStart = None
        self.SportEnd = None
        self.MatchType = None
        self.IsNot = None
        self.Offset = None
        self.Depth = None
        self.MatchBegin = None
        self.Str = None
        self.MatchType2 = None
        self.IsNot2 = None
        self.Offset2 = None
        self.Depth2 = None
        self.MatchBegin2 = None
        self.Str2 = None
        self.MatchLogic = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Protocol = params.get("Protocol")
        self.DportStart = params.get("DportStart")
        self.DportEnd = params.get("DportEnd")
        self.PacketMin = params.get("PacketMin")
        self.PacketMax = params.get("PacketMax")
        self.SportStart = params.get("SportStart")
        self.SportEnd = params.get("SportEnd")
        self.MatchType = params.get("MatchType")
        self.IsNot = params.get("IsNot")
        self.Offset = params.get("Offset")
        self.Depth = params.get("Depth")
        self.MatchBegin = params.get("MatchBegin")
        self.Str = params.get("Str")
        self.MatchType2 = params.get("MatchType2")
        self.IsNot2 = params.get("IsNot2")
        self.Offset2 = params.get("Offset2")
        self.Depth2 = params.get("Depth2")
        self.MatchBegin2 = params.get("MatchBegin2")
        self.Str2 = params.get("Str2")
        self.MatchLogic = params.get("MatchLogic")
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
        :param Switch: 区域封禁清空标识，取值有：
<li>off ：清空地域封禁列表 ；</li>
<li>on ：不做处理 。</li>
        :type Switch: str
        :param RegionId: 地域信息，ID参考[DescribeSecurityPolicyRegions](https://tcloud4api.woa.com/document/product/1657/76031?!preview&!document=1)。
        :type RegionId: list of int
        """
        self.Switch = None
        self.RegionId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RegionId = params.get("RegionId")
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
        :param AiStatus: 暂不支持，默认值off。
        :type AiStatus: str
        :param Appid: 废弃字段。
        :type Appid: str
        :param PlyLevel: 策略等级，取值有:
<li>low ：宽松 ；</li>
<li>middle ：适中 ；</li>
<li>high : 严格。 </li>
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
        :param Ip: 客户端IP。
        :type Ip: str
        :param Mask: 掩码。
        :type Mask: int
        :param Type: 类型，取值有：
<li>block ：丢弃 ；</li>
<li>allow ：允许。</li>
        :type Type: str
        :param UpdateTime: 10位时间戳，例如1199116800。
        :type UpdateTime: int
        :param Ip2: 客户端IP2，设置IP范围时使用，例如 1.1.1.1-1.1.1.2。
        :type Ip2: str
        :param Mask2: 掩码2，设置IP网段范围时使用，例如 1.1.1.0/24-1.1.2.0/24。
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
        :param List: 攻击事件数据集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DDosAttackEvent
        :param PageNo: 分页拉取的起始页号。最小值：1。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数。
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
        :param AttackStatus: 攻击状态，取值有：
<li>1 ：观察中 ；</li>
<li>2 ：攻击开始 ；</li>
<li>3 ：攻击结束 。</li>
        :type AttackStatus: int
        :param AttackType: 攻击类型。
        :type AttackType: str
        :param EndTime: 结束时间。
        :type EndTime: int
        :param StartTime: 开始时间。
        :type StartTime: int
        :param MaxBandWidth: 最大带宽。
        :type MaxBandWidth: int
        :param PacketMaxRate: 最大包速率。
        :type PacketMaxRate: int
        :param EventId: 事件Id。
        :type EventId: str
        :param PolicyId: ddos 策略组id。
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
        :param AttackSourceIp: 攻击源ip。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackSourceIp: str
        :param AttackRegion: 地区（国家）。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackRegion: str
        :param AttackFlow: 累计攻击流量。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackFlow: int
        :param AttackPacketNum: 累计攻击包量。
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
        :param List: DDos攻击源数据集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DDosAttackSourceEvent
        :param PageNo: 分页拉取的起始页号。最小值：1。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数。
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
        :param PolicyId: ddos 策略组id。
        :type PolicyId: int
        :param AttackMaxBandWidth: 攻击最大带宽。
        :type AttackMaxBandWidth: int
        :param AttackTime: 攻击请求时间，采用unix秒级时间戳。
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
        :param List: DDosMajorAttackEvent ddos 攻击事件。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DDosMajorAttackEvent
        :param PageNo: 分页拉取的起始页号。最小值：1。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: int
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param Pages: 总页数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param TotalSize: 总条数。
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
        :param Acl: 端口过滤规则数组。
        :type Acl: list of DDoSAcl
        :param Switch: 清空规则标识，取值有：
<li>off ：清空端口过滤规则列表，Acl无需填写。 ；</li>
<li>on ：配置端口过滤规则，需填写Acl参数。</li>默认值为on。
        :type Switch: str
        """
        self.Acl = None
        self.Switch = None


    def _deserialize(self, params):
        if params.get("Acl") is not None:
            self.Acl = []
            for item in params.get("Acl"):
                obj = DDoSAcl()
                obj._deserialize(item)
                self.Acl.append(obj)
        self.Switch = params.get("Switch")
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
        :param UserAllowBlockIp: 黑白名单数组。
        :type UserAllowBlockIp: list of DDoSUserAllowBlockIP
        :param Switch: 开关标识防护是否清空，取值有：
<li>off ：清空黑白名单列表，UserAllowBlockIp无需填写。 ；</li>
<li>on ：配置黑白名单，需填写UserAllowBlockIp参数。</li>默认值为on。
        :type Switch: str
        """
        self.UserAllowBlockIp = None
        self.Switch = None


    def _deserialize(self, params):
        if params.get("UserAllowBlockIp") is not None:
            self.UserAllowBlockIp = []
            for item in params.get("UserAllowBlockIp"):
                obj = DDoSUserAllowBlockIP()
                obj._deserialize(item)
                self.UserAllowBlockIp.append(obj)
        self.Switch = params.get("Switch")
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
        :param PacketFilter: 特征过滤规则数组。
        :type PacketFilter: list of DDoSFeaturesFilter
        :param Switch: 特征过滤清空标识，取值有：
<li>off ：清空特征过滤规则，无需填写 PacketFilter 参数 ；</li>
<li>on ：配置特征过滤规则，需填写 PacketFilter 参数。</li>默认值为on。
        :type Switch: str
        """
        self.PacketFilter = None
        self.Switch = None


    def _deserialize(self, params):
        if params.get("PacketFilter") is not None:
            self.PacketFilter = []
            for item in params.get("PacketFilter"):
                obj = DDoSFeaturesFilter()
                obj._deserialize(item)
                self.PacketFilter.append(obj)
        self.Switch = params.get("Switch")
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
        :param DdosStatusInfo: DDoS防护等级。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosStatusInfo: :class:`tencentcloud.teo.v20220106.models.DDoSStatusInfo`
        :param DdosGeoIp: DDoS地域封禁。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosGeoIp: :class:`tencentcloud.teo.v20220106.models.DDoSGeoIp`
        :param DdosAllowBlock: DDoS黑白名单。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosAllowBlock: :class:`tencentcloud.teo.v20220106.models.DdosAllowBlock`
        :param DdosAntiPly: DDoS 协议封禁+连接防护。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosAntiPly: :class:`tencentcloud.teo.v20220106.models.DDoSAntiPly`
        :param DdosPacketFilter: DDoS特征过滤。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosPacketFilter: :class:`tencentcloud.teo.v20220106.models.DdosPacketFilter`
        :param DdosAcl: DDoS端口过滤。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosAcl: :class:`tencentcloud.teo.v20220106.models.DdosAcls`
        :param Switch: DDoS开关，取值有:
<li>on ：开启 ；</li>
<li>off ：关闭 。</li>
        :type Switch: str
        :param UdpShardOpen: UDP分片功能是否支持，取值有:
<li>on ：支持 ；</li>
<li>off ：不支持 。</li>
        :type UdpShardOpen: str
        :param DdosSpeedLimit: DDoS源站访问速率限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosSpeedLimit: :class:`tencentcloud.teo.v20220106.models.DdosSpeedLimit`
        """
        self.DdosStatusInfo = None
        self.DdosGeoIp = None
        self.DdosAllowBlock = None
        self.DdosAntiPly = None
        self.DdosPacketFilter = None
        self.DdosAcl = None
        self.Switch = None
        self.UdpShardOpen = None
        self.DdosSpeedLimit = None


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
        if params.get("DdosSpeedLimit") is not None:
            self.DdosSpeedLimit = DdosSpeedLimit()
            self.DdosSpeedLimit._deserialize(params.get("DdosSpeedLimit"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosSpeedLimit(AbstractModel):
    """DDoS端口限速

    """

    def __init__(self):
        r"""
        :param PackageLimit: 源站包量限制，支持单位有pps、Kpps、Mpps、Gpps。支持范围1 pps-10000 Gpps。"0 pps"或其他单位数值为0，即不限包。""为不更新。
        :type PackageLimit: str
        :param FluxLimit: 源站流量限制，支持单位有bps、Kbps、Mbps、Gbps，支持范围1 bps-10000 Gbps。"0 bps"或其他单位数值为0，即不限流。""为不更新。
        :type FluxLimit: str
        """
        self.PackageLimit = None
        self.FluxLimit = None


    def _deserialize(self, params):
        self.PackageLimit = params.get("PackageLimit")
        self.FluxLimit = params.get("FluxLimit")
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


class DeleteRulesRequest(AbstractModel):
    """DeleteRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param RuleIds: 指定删除的规则 ID 列表。
        :type RuleIds: list of str
        """
        self.ZoneId = None
        self.RuleIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRulesResponse(AbstractModel):
    """DeleteRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 实例ID。
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
        :param ProxyId: 实例ID。
        :type ProxyId: str
        :param ProxyName: 当ProxyType=hostname时，表示域名或子域名；
当ProxyType=instance时，表示代理名称。
        :type ProxyName: str
        :param PlatType: 调度模式，取值有：
<li>ip：表示Anycast IP调度；</li>
<li>domain：表示CNAME调度。</li>
        :type PlatType: str
        :param SecurityType: 是否开启安全，取值有：
<li>0：关闭安全；</li>
<li>1：开启安全。</li>
        :type SecurityType: int
        :param AccelerateType: 是否开启加速，取值有：
<li>0：关闭加速；</li>
<li>1：开启加速。</li>
        :type AccelerateType: int
        :param ForwardClientIp: 字段已经废弃。
        :type ForwardClientIp: str
        :param SessionPersist: 字段已经废弃。
        :type SessionPersist: bool
        :param Rule: 规则列表。
        :type Rule: list of ApplicationProxyRule
        :param Status: 状态，取值有：
<li>online：启用；</li>
<li>offline：停用；</li>
<li>progress：部署中。</li>
        :type Status: str
        :param ScheduleValue: 调度信息。
        :type ScheduleValue: list of str
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param SessionPersistTime: 会话保持时间。
        :type SessionPersistTime: int
        :param ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>
        :type ProxyType: str
        :param HostId: 当ProxyType=hostname时：
表示代理加速唯一标识。
        :type HostId: str
        :param Ipv6: IPv6访问配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220106.models.Ipv6Access`
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
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
        self.Ipv6 = None
        self.Area = None
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
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6Access()
            self.Ipv6._deserialize(params.get("Ipv6"))
        self.Area = params.get("Area")
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxyRequest(AbstractModel):
    """DescribeApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param Offset: 分页查询偏移量，默认为0。
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为10，最大可设置为1000。
        :type Limit: int
        :param ProxyId: 代理ID。
当ProxyId为空时，表示查询站点下所有应用代理的列表。
        :type ProxyId: str
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProxyId = params.get("ProxyId")
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
        :param Data: 应用代理列表。
        :type Data: list of ApplicationProxy
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param Quota: 字段已废弃。
        :type Quota: int
        :param IpCount: 当ProxyId为空时，表示套餐内PlatType为ip的Anycast IP的实例数量。
        :type IpCount: int
        :param DomainCount: 当ProxyId为空时，表示套餐内PlatType为domain的CNAME的实例数量。
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


class DescribeAvailablePlansRequest(AbstractModel):
    """DescribeAvailablePlans请求参数结构体

    """


class DescribeAvailablePlansResponse(AbstractModel):
    """DescribeAvailablePlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param PlanInfoList: 当前账户可购买套餐类型及相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanInfoList: list of PlanInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlanInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlanInfoList") is not None:
            self.PlanInfoList = []
            for item in params.get("PlanInfoList"):
                obj = PlanInfo()
                obj._deserialize(item)
                self.PlanInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBotLogRequest(AbstractModel):
    """DescribeBotLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param ZoneIds: 站点集合，不填默认查询所有站点。
        :type ZoneIds: list of str
        :param Domains: 域名集合，不填默认查询所有子域名。
        :type Domains: list of str
        :param QueryCondition: 筛选条件，取值有：
<li>action ：执行动作（处置方式）；</li>
<li>sipCountryCode ：ip所在国家 ；</li>
<li>attackIp ：攻击ip ；</li>
<li>ruleId ：规则id ；</li>
<li>eventId ：事件id ；</li>
<li>ua ：用户代理 ；</li>
<li>requestMethod ：请求方法 ；</li>
<li>uri ：统一资源标识符 。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Data: Bot攻击数据内容。
        :type Data: :class:`tencentcloud.teo.v20220106.models.BotLogData`
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应信息。
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
        :param DdosRule: DDoS防护配置
        :type DdosRule: :class:`tencentcloud.teo.v20220106.models.DdosRule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DdosRule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DdosRule") is not None:
            self.DdosRule = DdosRule()
            self.DdosRule._deserialize(params.get("DdosRule"))
        self.RequestId = params.get("RequestId")


class DescribeDDosAttackDataRequest(AbstractModel):
    """DescribeDDosAttackData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 统计指标列表，取值有：
<li>ddos_attackMaxBandwidth ：攻击带宽峰值 ；</li>
<li>ddos_attackMaxPackageRate：攻击包速率峰值  ；</li>
<li>ddos_attackBandwidth ：攻击带宽曲线 ；</li>
<li>ddos_attackPackageRate ：攻击包速率曲线 。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点id列表，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param PolicyIds: ddos策略组id列表，不填默认选择全部策略id。
        :type PolicyIds: list of int
        :param Port: 端口号。
        :type Port: int
        :param ProtocolType: 协议类型，取值有：
<li>tcp ；</li>
<li>udp ；</li>
<li>all 。</li>
        :type ProtocolType: str
        :param AttackType: 攻击类型，取值有：
<li>flood ；</li>
<li>icmpFlood ；</li>
<li>all 。</li>
        :type AttackType: str
        :param Interval: 查询时间粒度，取值有：
<li>min ：1分钟 ；</li>
<li>5min ：5分钟 ；</li>
<li>hour ：1小时 ；</li>
<li>day ：1天 。</li>
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
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
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Data: DDos攻击数据内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应信息。
        :type Msg: str
        :param Interval: 查询时间粒度，取值有：
<li>min ：1分钟 ；</li>
<li>5min ：5分钟 ；</li>
<li>hour ：1小时 ；</li>
<li>day ：1天 。</li>
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
        :param EventId: 事件id。
        :type EventId: str
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.EventId = None
        self.Area = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.Area = params.get("Area")
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
        :param Data: DDos攻击事件详情。
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventDetailData`
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应信息。
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
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param PolicyIds: ddos策略组id列表，不填默认选择全部策略Id。
        :type PolicyIds: list of int
        :param ZoneIds: 站点id列表，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param ProtocolType: 协议类型，取值有：
<li>tcp ；</li>
<li>udp ；</li>
<li>all 。</li>
        :type ProtocolType: str
        :param IsShowDetail: 是否展示详情，取值有：
<li>Y ：展示 ；</li>
<li>N ：不展示 。</li>默认为Y。
        :type IsShowDetail: str
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.ProtocolType = None
        self.IsShowDetail = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.ProtocolType = params.get("ProtocolType")
        self.IsShowDetail = params.get("IsShowDetail")
        self.Area = params.get("Area")
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
        :param Data: DDos攻击事件数据。
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackEventData`
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应信息。
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
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param PolicyIds: ddos策略组id 集合，不填默认选择全部策略id。
        :type PolicyIds: list of int
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param ProtocolType: 协议类型，取值有：
<li>tcp ；</li>
<li>udp ；</li>
<li>all 。</li>
        :type ProtocolType: str
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.ProtocolType = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.ProtocolType = params.get("ProtocolType")
        self.Area = params.get("Area")
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
        :param Data: DDos攻击源数据。
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosAttackSourceEventData`
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应信息。
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
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricName: 统计指标列表，取值有：
<li>ddos_attackFlux_protocol ：攻击总流量协议类型分布排行 ；</li>
<li>ddos_attackPackageNum_protocol ：攻击总包量协议类型分布排行 ；</li>
<li>ddos_attackNum_attackType ：攻击总次数攻击类型分布排行 ；</li>
<li>ddos_attackNum_sregion ：攻击总次数攻击源地区分布排行 ；</li>
<li>ddos_attackFlux_sip ：攻击总流量攻击源ip分布排行 ；</li>
<li>ddos_attackFlux_sregion ：攻击总流量攻击源地区分布排行 。</li>
        :type MetricName: str
        :param Limit: 查询前多少个，传值为0返回全量。
        :type Limit: int
        :param ZoneIds: 站点id集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param PolicyIds: ddos策略组id 集合，不填默认选择全部策略id。
        :type PolicyIds: list of int
        :param Port: 端口号。
        :type Port: int
        :param ProtocolType: 协议类型，取值有：
<li>tcp ；</li>
<li>udp ；</li>
<li>all 。</li>
        :type ProtocolType: str
        :param AttackType: 攻击类型，取值有：
<li>flood ；</li>
<li>icmpFlood ；</li>
<li>all 。</li>
        :type AttackType: str
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
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
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Data: top数据内容
        :type Data: list of TopNEntry
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应消息。
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
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param PolicyIds: ddos 策略组id集合，不填默认选择全部策略id。
        :type PolicyIds: list of int
        :param ProtocolType: 协议类型，取值有：
<li>tcp ；</li>
<li>udp ；</li>
<li>all 。</li>
        :type ProtocolType: str
        :param ZoneIds: 站点id列表，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.PolicyIds = None
        self.ProtocolType = None
        self.ZoneIds = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        self.PolicyIds = params.get("PolicyIds")
        self.ProtocolType = params.get("ProtocolType")
        self.ZoneIds = params.get("ZoneIds")
        self.Area = params.get("Area")
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
        :param Data: DDos查询主攻击事件。
        :type Data: :class:`tencentcloud.teo.v20220106.models.DDosMajorAttackEventData`
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应消息。
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
 l7Flow_hit_outFlux: 缓存命中流量
        :type MetricNames: list of str
        :param Interval: 时间间隔，选填{min, 5min, hour, day, week}
        :type Interval: str
        :param ZoneIds: ZoneId列表，仅在zone/domain维度下查询时该参数有效
        :type ZoneIds: list of str
        :param Domains: Domain列表，仅在domain维度下查询时该参数有效
        :type Domains: list of str
        :param Protocol: 协议类型， 选填{http,http2,https,all}
        :type Protocol: str
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Domains = None
        self.Protocol = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Protocol = params.get("Protocol")
        self.Area = params.get("Area")
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


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Filters: 过滤参数，不填默认不过滤。
        :type Filters: list of RuleFilter
        """
        self.ZoneId = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = RuleFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param RuleList: 规则列表，按规则执行顺序从先往后排序。
        :type RuleList: list of RuleSettingDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneId = None
        self.RuleList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = RuleSettingDetail()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesSettingRequest(AbstractModel):
    """DescribeRulesSetting请求参数结构体

    """


class DescribeRulesSettingResponse(AbstractModel):
    """DescribeRulesSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param Actions: 规则引擎可应用匹配请求的设置列表及其详细建议配置信息。
        :type Actions: list of RulesSettingAction
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Actions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = RulesSettingAction()
                obj._deserialize(item)
                self.Actions.append(obj)
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
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
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
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Limit = None
        self.Interval = None
        self.ZoneIds = None
        self.Filters = None
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param StartTime: 开始时间，RFC3339格式。
        :type StartTime: str
        :param EndTime: 结束时间，RFC3339格式。
        :type EndTime: str
        :param MetricNames: 统计指标列表，取值有：
<li>waf_interceptNum ：waf拦截次数 。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点id列表，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 子域名列表，不填默认选择子域名。
        :type Domains: list of str
        :param ProtocolType: 该字段已废弃，请勿传。
        :type ProtocolType: str
        :param AttackType: 该字段已废弃，请勿传。
        :type AttackType: str
        :param Interval: 查询时间粒度，取值有：
<li>min ：1分钟 ；</li>
<li>5min ：5分钟 ；</li>
<li>hour ：1小时 ；</li>
<li>day ：1天 。</li>
        :type Interval: str
        :param QueryCondition: 筛选条件，取值有：
<li>action ：执行动作 。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
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
        :param Data: Web攻击日志实体。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应消息。
        :type Msg: str
        :param Interval: 查询时间粒度，取值有：
<li>min ：1分钟 ；</li>
<li>5min ：5分钟 ；</li>
<li>hour ：1小时 ；</li>
<li>day ：1天 。</li>
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
        :param StartTime: 起始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param QueryCondition: 筛选条件，取值有：
<li>attackType ：攻击类型 ；</li>
<li>riskLevel ：风险等级 ；</li>
<li>action ：执行动作（处置方式） ；</li>
<li>ruleId ：规则id ；</li>
<li>sipCountryCode ：ip所在国家 ；</li>
<li>attackIp ：攻击ip ；</li>
<li>oriDomain ：被攻击的子域名 ；</li>
<li>eventId ：事件id ；</li>
<li>ua ：用户代理 ；</li>
<li>requestMethod ：请求方法 ；</li>
<li>uri ：统一资源标识符 。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Area = None


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
        self.Area = params.get("Area")
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
        :param Data: web攻击日志数据内容。
        :type Data: :class:`tencentcloud.teo.v20220106.models.WebLogData`
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应信息。
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
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricName: 统计指标列表，取值有：
<li>waf_requestNum_url ：url请求数排行 ；</li>
<li>waf_requestNum_cip：客户端ip请求数排行 ；</li>
<li>waf_cipRequestNum_region ：客户端区域请求数排行 。</li>
        :type MetricName: str
        :param Limit: 查询前多少个，传值为0返回全量。
        :type Limit: int
        :param ZoneIds: 站点id列表，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param PolicyIds: 该字段已废弃，请勿传。
        :type PolicyIds: list of int
        :param Port: 该字段已废弃，请勿传。
        :type Port: int
        :param ProtocolType: 该字段已废弃，请勿传。
        :type ProtocolType: str
        :param AttackType: 该字段已废弃，请勿传。
        :type AttackType: str
        :param Domains: 域名列表，不填默认选择全部子域名。
        :type Domains: list of str
        :param Interval: 查询时间粒度，取值有：
<li>min ：1分钟 ；</li>
<li>5min ：5分钟 ；</li>
<li>hour ：1小时 ；</li>
<li>day ：1天 。</li>
        :type Interval: str
        :param QueryCondition: 筛选条件，取值有：
<li>action ：执行动作 。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
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
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


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
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
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
        :param Data: top数据内容。
        :type Data: list of TopNEntry
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应消息。
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
        :param StartTime: 开始时间，RFC3339格式。
        :type StartTime: str
        :param EndTime: 结束时间，RFC3339格式。
        :type EndTime: str
        :param MetricNames: 统计指标列表，取值有：
<li>ccRate_interceptNum ：速率限制规则限制次数 ；</li>
<li>ccAcl_interceptNum ：自定义规则拦截次数 。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点id列表，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 子域名列表，不填默认选择全部子域名。
        :type Domains: list of str
        :param ProtocolType: 该字段已废弃，请勿传。
        :type ProtocolType: str
        :param AttackType: 该字段已废弃，请勿传。
        :type AttackType: str
        :param Interval: 查询时间粒度，取值有：
<li>min ：1分钟 ；</li>
<li>5min ：5分钟 ；</li>
<li>hour ：1小时 ；</li>
<li>day ：1天 。</li>
        :type Interval: str
        :param QueryCondition: 筛选条件，取值有：
<li>action ：执行动作 。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.ProtocolType = None
        self.AttackType = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.ProtocolType = params.get("ProtocolType")
        self.AttackType = params.get("AttackType")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Area = params.get("Area")
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
        :param Data: 数据详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应消息。
        :type Msg: str
        :param Interval: 查询时间粒度，取值有：
<li>min ：1分钟 ；</li>
<li>5min ：5分钟 ；</li>
<li>hour ：1小时 ；</li>
<li>day ：1天 。</li>
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
        :param StartTime: 起始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param ZoneIds: 站点集合，不填默认查询所有站点。
        :type ZoneIds: list of str
        :param Domains: 域名集合，不填默认查询所有域名。
        :type Domains: list of str
        :param QueryCondition: 筛选条件。
限速规则日志中取值有：
<li>action ：执行动作（处置方式）；</li>
<li>ruleId ：规则id ；</li>
<li>oriDomain ：被攻击的子域名 ；</li>
<li>attackIp ：攻击ip 。</li>
自定义规则日志中取值有：
<li>action ：执行动作（处置方式）；</li>
<li>ruleId ：规则id ；</li>
<li>oriDomain ：被攻击的子域名 ；</li>
<li>attackIp ：攻击ip ；</li>
<li>eventId ：事件id ；</li>
<li>ua ：用户代理 ；</li>
<li>requestMethod ：请求方法 ；</li>
<li>uri ：统一资源标识符 。</li>
        :type QueryCondition: list of QueryCondition
        :param EntityType: 日志类型，取值有：
<li>rate ：限速日志 ；</li>
<li>acl ：自定义规则日志 。</li>不填默认为rate。
        :type EntityType: str
        :param Area: 数据归属地区，取值有：
<li>overseas ：全球（除中国大陆地区）数据 ；</li>
<li>mainland ：中国大陆地区数据 。</li>不填默认查询overseas。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PageSize = None
        self.PageNo = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.EntityType = None
        self.Area = None


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
        self.EntityType = params.get("EntityType")
        self.Area = params.get("Area")
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
        :param Data: 限速拦截数据内容。
        :type Data: :class:`tencentcloud.teo.v20220106.models.CCLogData`
        :param Status: 请求响应状态，取值有：
<li>1 ：失败 ；</li>
<li>0 ：成功 。</li>
        :type Status: int
        :param Msg: 请求响应信息。
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
        :type OriginalNameServers: list of str
        :param NameServers: 腾讯云分配给用户的 NS 列表
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
        :param CnameSpeedUp: 是否开启 CNAME 加速
- enabled：开启
- disabled：关闭
        :type CnameSpeedUp: str
        :param CnameStatus: cname切换验证状态
- finished 切换完成
- pending 切换验证中
        :type CnameStatus: str
        :param Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Area: 站点接入地域，取值为：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>
        :type Area: str
        :param Resources: 计费资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of Resource
        :param ModifiedOn: 站点修改时间
        :type ModifiedOn: str
        :param CreatedOn: 站点创建时间
        :type CreatedOn: str
        :param VanityNameServers: 用户自定义 NS 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServers: :class:`tencentcloud.teo.v20220106.models.VanityNameServers`
        :param VanityNameServersIps: 用户自定义 NS IP 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServersIps: list of VanityNameServersIps
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
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.Tags = None
        self.Area = None
        self.Resources = None
        self.ModifiedOn = None
        self.CreatedOn = None
        self.VanityNameServers = None
        self.VanityNameServersIps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Area = params.get("Area")
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.ModifiedOn = params.get("ModifiedOn")
        self.CreatedOn = params.get("CreatedOn")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param Zone: 站点名称。
        :type Zone: str
        :param Cache: 缓存过期时间配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: 节点缓存键配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param Quic: Quic访问配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: POST请求传输配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: Http2回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制Https跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: Https 加速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: 智能加速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param MaxAge: 浏览器缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: 离线缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param WebSocket: WebSocket配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: 客户端IP回源请求头配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: 缓存预刷新配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        :param Ipv6: Ipv6访问配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.teo.v20220106.models.Ipv6Access`
        :param Area: 站点加速区域信息，取值有：
<li>mainland：中国境内加速；</li>
<li>overseas：中国境外加速。</li>
        :type Area: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneId = None
        self.Zone = None
        self.Cache = None
        self.CacheKey = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.Https = None
        self.Origin = None
        self.SmartRouting = None
        self.MaxAge = None
        self.OfflineCache = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.Ipv6 = None
        self.Area = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        if params.get("Cache") is not None:
            self.Cache = CacheConfig()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
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
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self.ClientIpHeader = ClientIp()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6Access()
            self.Ipv6._deserialize(params.get("Ipv6"))
        self.Area = params.get("Area")
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页查询偏移量。默认值：0，最小值：0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：1000，最大值：1000。
        :type Limit: int
        :param Filters: 查询条件过滤器，复杂类型。
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
        :param TotalCount: 符合条件的站点个数。
        :type TotalCount: int
        :param Zones: 站点详细信息列表。
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


class DropPageConfig(AbstractModel):
    """拦截页面的总体配置，用于配置各个模块的拦截后行为。

    """

    def __init__(self):
        r"""
        :param Switch: 配置开关。
1. on 开启
2. off 关闭
        :type Switch: str
        :param Waf: Waf(托管规则)模块的拦截页面配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Waf: :class:`tencentcloud.teo.v20220106.models.DropPageDetail`
        :param Acl: 自定义页面的拦截页面配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Acl: :class:`tencentcloud.teo.v20220106.models.DropPageDetail`
        """
        self.Switch = None
        self.Waf = None
        self.Acl = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Waf") is not None:
            self.Waf = DropPageDetail()
            self.Waf._deserialize(params.get("Waf"))
        if params.get("Acl") is not None:
            self.Acl = DropPageDetail()
            self.Acl._deserialize(params.get("Acl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropPageDetail(AbstractModel):
    """拦截页面的配置信息

    """

    def __init__(self):
        r"""
        :param PageId: 拦截页面的唯一Id。系统默认包含一个自带拦截页面，Id值为0。
该Id可通过创建拦截页面接口进行上传获取。如传入0，代表使用系统默认拦截页面
        :type PageId: int
        :param StatusCode: 拦截页面的HTTP状态码。状态码范围是 100 - 600。
        :type StatusCode: int
        :param Name: 页面的元信息，文件名或url。
        :type Name: str
        :param Type: 页面的类型。
        :type Type: str
        """
        self.PageId = None
        self.StatusCode = None
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.PageId = params.get("PageId")
        self.StatusCode = params.get("StatusCode")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptConfig(AbstractModel):
    """例外规则，用于配置需要跳过特定场景的规则

    """

    def __init__(self):
        r"""
        :param Switch: 开关。
1. on 开启
2. off 关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param UserRules: 例外规则详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserRules: list of ExceptUserRule
        """
        self.Switch = None
        self.UserRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("UserRules") is not None:
            self.UserRules = []
            for item in params.get("UserRules"):
                obj = ExceptUserRule()
                obj._deserialize(item)
                self.UserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRule(AbstractModel):
    """例外规则的配置，包含生效的条件，生效的范围

    """

    def __init__(self):
        r"""
        :param RuleID: 规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param RuleName: 规则名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param Action: 规则的处置方式。
1. skip 跳过
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param RuleStatus: 规则生效状态。
1. on 生效
2. off 失效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleStatus: str
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Conditions: 匹配条件。
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of ExceptUserRuleCondition
        :param Scope: 规则生效的范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type Scope: :class:`tencentcloud.teo.v20220106.models.ExceptUserRuleScope`
        :param RulePriority: 优先级。
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePriority: int
        """
        self.RuleID = None
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.UpdateTime = None
        self.Conditions = None
        self.Scope = None
        self.RulePriority = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.RuleStatus = params.get("RuleStatus")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ExceptUserRuleCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("Scope") is not None:
            self.Scope = ExceptUserRuleScope()
            self.Scope._deserialize(params.get("Scope"))
        self.RulePriority = params.get("RulePriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleCondition(AbstractModel):
    """例外规则生效的具体条件

    """

    def __init__(self):
        r"""
        :param MatchFrom: 匹配项。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchFrom: str
        :param MatchParam: 匹配项的参数。当 MatchFrom 为 header 时，可以填入 header 的 key 作为参数。
        :type MatchParam: str
        :param Operator: 匹配操作符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param MatchContent: 匹配值。
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ExceptUserRuleScope(AbstractModel):
    """例外规则的生效范围

    """

    def __init__(self):
        r"""
        :param Modules: 生效的模块

1. waf Waf防护
2. bot Bot防护
注意：此字段可能返回 null，表示取不到有效值。
        :type Modules: list of str
        """
        self.Modules = None


    def _deserialize(self, params):
        self.Modules = params.get("Modules")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param Switch: 访问强制跳转配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param RedirectStatusCode: 重定向状态码，取值有：
<li>301：301跳转；</li>
<li>302：302跳转。</li>
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
        :param Switch: 是否开启，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param MaxAge: MaxAge数值。单位为秒，最大值为1天。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: int
        :param IncludeSubDomains: 是否包含子域名，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeSubDomains: str
        :param Preload: 是否开启预加载，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
        :param Http2: http2 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param OcspStapling: OCSP 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param TlsVersion: Tls版本设置，取值有：
<li>TLSv1：TLSv1版本；</li>
<li>TLSV1.1：TLSv1.1版本；</li>
<li>TLSV1.2：TLSv1.2版本；</li>
<li>TLSv1.3：TLSv1.3版本。</li>修改时必须开启连续的版本。
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
        :param Switch: 开关。
1. on 开启
2. off 关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Items: 规则详情。
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
        :param Label: 智能分析标签。
1. evil_bot 恶意
2. suspect_bot 疑似恶意
3. good_bot 好的
4. normal 正常
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Action: 触发智能分析标签对应的处置方式。
1. drop 拦截
2. trans 放行
3. monitor 监控
4. alg Javascript挑战
5. captcha 数字验证码
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
    """基础管控规则配置。

    """

    def __init__(self):
        r"""
        :param Switch: 开关。
1. on 开启
2. off 关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Rules: 基础管控规则。
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
    """详细规则。

    """

    def __init__(self):
        r"""
        :param RuleID: 规则ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param Action: 处置动作。
1. drop 拦截
2. trans放行
3. monitor观察
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param MatchFrom: 类型匹配。
1. ip 根据ip
2. area 根据区域
3. ua 根据User-Agent
4. referer 根据Referer
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchFrom: str
        :param MatchContent: 匹配内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchContent: str
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.RuleID = None
        self.Action = None
        self.MatchFrom = None
        self.MatchContent = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.Action = params.get("Action")
        self.MatchFrom = params.get("MatchFrom")
        self.MatchContent = params.get("MatchContent")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Access(AbstractModel):
    """Ipv6访问配置

    """

    def __init__(self):
        r"""
        :param Switch: Ipv6访问功能配置，取值有：
<li>on：开启Ipv6访问功能；</li>
<li>off：关闭Ipv6访问功能。</li>
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
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        """
        self.LogTime = None
        self.Domain = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None
        self.Area = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.Domain = params.get("Domain")
        self.Size = params.get("Size")
        self.Url = params.get("Url")
        self.LogPacketName = params.get("LogPacketName")
        self.Area = params.get("Area")
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
        :param FollowOrigin: 是否遵循源站，取值有：
<li>on：遵循源站，忽略MaxAge 时间设置；</li>
<li>off：不遵循源站，使用MaxAge 时间设置。</li>
        :type FollowOrigin: str
        :param MaxAgeTime: MaxAge 时间设置，单位秒，最大365天。
注意：时间为0，即不缓存。
        :type MaxAgeTime: int
        """
        self.FollowOrigin = None
        self.MaxAgeTime = None


    def _deserialize(self, params):
        self.FollowOrigin = params.get("FollowOrigin")
        self.MaxAgeTime = params.get("MaxAgeTime")
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param ProxyName: 当ProxyType=hostname时，表示域名或子域名；
当ProxyType=instance时，表示代理名称。
        :type ProxyName: str
        :param ForwardClientIp: 参数已经废弃。
        :type ForwardClientIp: str
        :param SessionPersist: 参数已经废弃。
        :type SessionPersist: bool
        :param SessionPersistTime: 会话保持时间，不填写保持原有配置。取值范围：30-3600，单位：秒。
        :type SessionPersistTime: int
        :param ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>不填写保持原有配置。
        :type ProxyType: str
        :param Ipv6: Ipv6访问配置，不填写保持原有配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220106.models.Ipv6Access`
        """
        self.ZoneId = None
        self.ProxyId = None
        self.ProxyName = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.Ipv6 = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6Access()
            self.Ipv6._deserialize(params.get("Ipv6"))
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
        :param ProxyId: 代理ID。
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
        :param PolicyId: 策略id。
        :type PolicyId: int
        :param ZoneId: 站点id。
        :type ZoneId: str
        :param DdosRule: DDoS防护配置详情。
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
        :param PolicyId: 策略id。
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


class ModifyRulePriorityRequest(AbstractModel):
    """ModifyRulePriority请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param RuleIds: 规则 ID 的顺序，多条规则执行顺序依次往下。
        :type RuleIds: list of str
        """
        self.ZoneId = None
        self.RuleIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRulePriorityResponse(AbstractModel):
    """ModifyRulePriority返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param RuleName: 规则名称，字符串名称长度 1~255。
        :type RuleName: str
        :param Rules: 规则内容。
        :type Rules: list of RuleItem
        :param RuleId: 规则 ID。
        :type RuleId: str
        :param Status: 规则状态，取值有：
<li> enable: 启用； </li>
<li> disable: 未启用。</li>
        :type Status: str
        """
        self.ZoneId = None
        self.RuleName = None
        self.Rules = None
        self.RuleId = None
        self.Status = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleItem()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
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
        :param RuleId: 规则 ID。
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
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
        :param ZoneId: 待变更的站点ID。
        :type ZoneId: str
        :param Cache: 缓存过期时间配置。
不填写表示保持原有配置。
        :type Cache: :class:`tencentcloud.teo.v20220106.models.CacheConfig`
        :param CacheKey: 节点缓存键配置。
不填写表示保持原有配置。
        :type CacheKey: :class:`tencentcloud.teo.v20220106.models.CacheKey`
        :param MaxAge: 浏览器缓存配置。
不填写表示保持原有配置。
        :type MaxAge: :class:`tencentcloud.teo.v20220106.models.MaxAge`
        :param OfflineCache: 离线缓存配置。
不填写表示保持原有配置。
        :type OfflineCache: :class:`tencentcloud.teo.v20220106.models.OfflineCache`
        :param Quic: Quic访问配置。
不填写表示保持原有配置。
        :type Quic: :class:`tencentcloud.teo.v20220106.models.Quic`
        :param PostMaxSize: Post请求传输配置。
不填写表示保持原有配置。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220106.models.PostMaxSize`
        :param Compression: 智能压缩配置。
不填写表示保持原有配置。
        :type Compression: :class:`tencentcloud.teo.v20220106.models.Compression`
        :param UpstreamHttp2: Http2回源配置。
不填写表示保持原有配置。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220106.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制Https跳转配置。
不填写表示保持原有配置。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220106.models.ForceRedirect`
        :param Https: Https加速配置。
不填写表示保持原有配置。
        :type Https: :class:`tencentcloud.teo.v20220106.models.Https`
        :param Origin: 源站配置。
不填写表示保持原有配置。
        :type Origin: :class:`tencentcloud.teo.v20220106.models.Origin`
        :param SmartRouting: 智能加速配置。
不填写表示保持原有配置。
        :type SmartRouting: :class:`tencentcloud.teo.v20220106.models.SmartRouting`
        :param WebSocket: WebSocket配置。
不填写表示保持原有配置。
        :type WebSocket: :class:`tencentcloud.teo.v20220106.models.WebSocket`
        :param ClientIpHeader: 客户端IP回源请求头配置。
不填写表示保持原有配置。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220106.models.ClientIp`
        :param CachePrefresh: 缓存预刷新配置。
不填写表示保持原有配置。
        :type CachePrefresh: :class:`tencentcloud.teo.v20220106.models.CachePrefresh`
        :param Ipv6: Ipv6访问配置。
不填写表示保持原有配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220106.models.Ipv6Access`
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
        self.Ipv6 = None


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
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6Access()
            self.Ipv6._deserialize(params.get("Ipv6"))
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
        :param ZoneId: 站点ID。
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
        :param Switch: 离线缓存是否开启，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
        :param Origins: 主源站列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origins: list of str
        :param BackupOrigins: 备源站列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOrigins: list of str
        :param OriginPullProtocol: 回源协议配置，取值有：
<li>http：强制 http 回源；</li>
<li>follow：协议跟随回源；</li>
<li>https：强制 https 回源，https 回源时仅支持源站 443 端口。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param CosPrivateAccess: OriginType 为对象存储（COS）时，可以指定是否允许访问私有 bucket。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPrivateAccess: str
        """
        self.Origins = None
        self.BackupOrigins = None
        self.OriginPullProtocol = None
        self.CosPrivateAccess = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.BackupOrigins = params.get("BackupOrigins")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.CosPrivateAccess = params.get("CosPrivateAccess")
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
源站组内多个源站权重总和应为100。
当源站配置类型Type=proto，表示权重
取值范围为[1-100]
源站组内Proto相同的多个源站权重总和应为100。
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
        :param Proto: 当源站配置类型Type=proto时，表示客户端请求协议，取值：http/https
注意：此字段可能返回 null，表示取不到有效值。
        :type Proto: str
        """
        self.Record = None
        self.Area = None
        self.Weight = None
        self.Port = None
        self.RecordId = None
        self.Private = None
        self.PrivateParameter = None
        self.Proto = None


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
        self.Proto = params.get("Proto")
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
        


class PlanInfo(AbstractModel):
    """edgeone套餐信息

    """

    def __init__(self):
        r"""
        :param Currency: 结算货币类型，取值有：
<li> CNY ：人民币结算； </li>
<li> USD ：美元结算。</li>
        :type Currency: str
        :param Flux: 套餐所含流量（单位：字节）
        :type Flux: int
        :param Frequency: 结算周期，取值有：
<li> y ：按年结算； </li>
<li> m ：按月结算；</li>
<li> h ：按小时结算； </li>
<li> M ：按分钟结算；</li>
<li> s ：按秒结算。 </li>
        :type Frequency: str
        :param PlanType: 套餐类型，取值有：
<li> sta ：全球内容分发网络（不包括中国大陆）标准版套餐； </li>
<li> sta_with_bot ：全球内容分发网络（不包括中国大陆）标准版套餐附带bot管理；</li>
<li> sta_cm ：中国大陆内容分发网络标准版套餐； </li>
<li> sta_cm_with_bot ：中国大陆内容分发网络标准版套餐附带bot管理；</li>
<li> ent ：全球内容分发网络（不包括中国大陆）企业版套餐； </li>
<li> ent_with_bot ： 全球内容分发网络（不包括中国大陆）企业版套餐附带bot管理；</li>
<li> ent_cm ：中国大陆内容分发网络企业版套餐； </li>
<li> ent_cm_with_bot ：中国大陆内容分发网络企业版套餐附带bot管理。</li>
        :type PlanType: str
        :param Price: 套餐价格（单位：分）
        :type Price: float
        :param Request: 套餐所含请求次数（单位：字节）
        :type Request: int
        :param SiteNumber: 套餐所能绑定的站点个数。
        :type SiteNumber: int
        """
        self.Currency = None
        self.Flux = None
        self.Frequency = None
        self.PlanType = None
        self.Price = None
        self.Request = None
        self.SiteNumber = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Flux = params.get("Flux")
        self.Frequency = params.get("Frequency")
        self.PlanType = params.get("PlanType")
        self.Price = params.get("Price")
        self.Request = params.get("Request")
        self.SiteNumber = params.get("SiteNumber")
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
        :param Switch: 是否开启POST请求上传文件限制，平台默认为限制为32MB，取值有：
<li>on：开启限制；</li>
<li>off：关闭限制。</li>
        :type Switch: str
        :param MaxSize: 最大限制，取值在1MB和500MB之间。单位字节。
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
        :param Switch: CacheKey是否由QueryString组成，取值有：
<li>on：是；</li>
<li>off：否。</li>
        :type Switch: str
        :param Action: CacheKey使用QueryString的方式，取值有：
<li>includeCustom：使用部分url参数；</li>
<li>excludeCustom：排除部分url参数。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param Value: 使用/排除的url参数数组。
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
        :param Switch: 是否开启Quic配置，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
        :param Switch: 开关。
1. on 开启RateLimit；
2. off 关闭RateLimit
        :type Switch: str
        :param UserRules: 速率限制-用户规则列表。
        :type UserRules: list of RateLimitUserRule
        :param Template: 速率限制模板功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type Template: :class:`tencentcloud.teo.v20220106.models.RateLimitTemplate`
        :param Intelligence: 智能客户端过滤。
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
        :param Switch: 功能开关。
1. on 开启
2. off 关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Action: 执行动作 
1. monitor(观察)
2. alg(挑战)
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
        :param Mode: 模板等级名称。
1. sup_loose 自适应 - 超级宽松
2. loose     自适应 - 宽松
3. emergency 自适应 - 紧急
4. normal    自适应 - 适中
5. strict    固定阈值 - 严格
6. close     关闭 - 仅精准速率限制生效
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param Detail: 模板值详情。
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
    """模板当前详细配置。

    """

    def __init__(self):
        r"""
        :param Mode: 模板等级名称。
1. sup_loose 自适应 - 超级宽松
2. loose     自适应 - 宽松
3. emergency 自适应 - 紧急
4. normal    自适应 - 适中
5. strict    固定阈值 - 严格
6. close     关闭 - 仅精准速率限制生效
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param ID: 唯一id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param Action: 处置动作。模板阀值触发后的处罚行为。
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param PunishTime: 惩罚时间，单位是秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param Threshold: 阈值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: int
        :param Period: 统计周期。
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
        :param Threshold: RateLimit统计阈值，单位是次，取值范围0-4294967294。
        :type Threshold: int
        :param Period: RateLimit统计时间，取值范围 10/20/30/40/50/60 单位是秒。
        :type Period: int
        :param RuleName: 规则名，只能以英文字符，数字，下划线组合，且不能以下划线开头。
        :type RuleName: str
        :param Action: 处置动作。
1. monitor(观察)；
2. drop(拦截)；
3. alg(Javascript挑战)
        :type Action: str
        :param PunishTime: 惩罚时长，0-100。
        :type PunishTime: int
        :param PunishTimeUnit: 处罚时长单位。
1. second 秒; 
2. minutes 分钟
3. hour 小时
        :type PunishTimeUnit: str
        :param RuleStatus: 规则状态。
1. on 生效
2. off 不生效
        :type RuleStatus: str
        :param Conditions: 规则。
        :type Conditions: list of ACLCondition
        :param RulePriority: 规则权重，取值范围0-100。
        :type RulePriority: int
        :param RuleID: 规则id。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param FreqFields: 过滤词。
注意：此字段可能返回 null，表示取不到有效值。
        :type FreqFields: list of str
        :param UpdateTime: 更新时间.
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


class Resource(AbstractModel):
    """计费资源

    """

    def __init__(self):
        r"""
        :param Id: 资源 ID。
        :type Id: str
        :param PayMode: 付费模式，取值有：
<li>0：后付费。</li>
        :type PayMode: int
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param EnableTime: 生效时间。
        :type EnableTime: str
        :param ExpireTime: 失效时间。
        :type ExpireTime: str
        :param Status: 套餐状态，取值有：
<li>normal：正常；</li>
<li>isolated：隔离；</li>
<li>destroyed：销毁。</li>
        :type Status: str
        :param Sv: 询价参数。
        :type Sv: list of Sv
        :param AutoRenewFlag: 是否自动续费，取值有：
<li>0：默认状态；</li>
<li>1：自动续费；</li>
<li>2：不自动续费。</li>
        :type AutoRenewFlag: int
        :param PlanId: 套餐关联资源 ID。
        :type PlanId: str
        :param Area: 地域，取值有：
<li>mainland：国内；</li>
<li>overseas：海外。</li>
        :type Area: str
        """
        self.Id = None
        self.PayMode = None
        self.CreateTime = None
        self.EnableTime = None
        self.ExpireTime = None
        self.Status = None
        self.Sv = None
        self.AutoRenewFlag = None
        self.PlanId = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.EnableTime = params.get("EnableTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")
        if params.get("Sv") is not None:
            self.Sv = []
            for item in params.get("Sv"):
                obj = Sv()
                obj._deserialize(item)
                self.Sv.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PlanId = params.get("PlanId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAction(AbstractModel):
    """规则引擎功能项操作，对于一种功能只对应下面三种类型的其中一种，RuleAction 数组中的每一项只能是其中一个类型，更多功能项的填写规范可调用接口 [查询规则引擎的设置参数](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) 查看。

    """

    def __init__(self):
        r"""
        :param NormalAction: 常规功能操作，选择该类型的功能项有：
<li> 访问URL 重写（AccessUrlRedirect）；</li>
<li> 回源 URL 重写 （UpstreamUrlRedirect）；</li>
<li> QUIC（QUIC）；</li>
<li> WebSocket （WebSocket）；</li>
<li> 视频拖拽（VideoSeek）；</li>
<li> Token 鉴权（Authentication）；</li>
<li> 自定义CacheKey（CacheKey）；</li>
<li> 节点缓存 TTL （Cache）；</li>
<li> 浏览器缓存 TTL（MaxAge）；</li>
<li> 离线缓存（OfflineCache）；</li>
<li> 智能加速（SmartRouting）；</li>
<li> 分片回源（RangeOriginPull）；</li>
<li> HTTP/2 回源（UpstreamHttp2）；</li>
<li> Host Header 重写（HostHeader）；</li>
<li> 强制 HTTPS（ForceRedirect）；</li>
<li> 回源 HTTPS（OriginPullProtocol）；</li>
<li> 缓存预刷新（CachePrefresh）；</li>
<li> 智能压缩（Compression）；</li>
<li> Hsts；</li>
<li> ClientIpHeader；</li>
<li> TlsVersion；</li>
<li> OcspStapling。</li>
<li> HTTP/2 访问（Http2）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalAction: :class:`tencentcloud.teo.v20220106.models.RuleNormalAction`
        :param RewriteAction: 带有请求头/响应头的功能操作，选择该类型的功能项有：
<li> 修改 HTTP 请求头（RequestHeader）；</li>
<li> 修改HTTP响应头（ResponseHeader）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteAction: :class:`tencentcloud.teo.v20220106.models.RuleRewriteAction`
        :param CodeAction: 带有状态码的功能操作，选择该类型的功能项有：
<li> 自定义错误页面（ErrorPage）；</li>
<li> 状态码缓存 TTL（StatusCodeCache）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeAction: :class:`tencentcloud.teo.v20220106.models.RuleCodeAction`
        """
        self.NormalAction = None
        self.RewriteAction = None
        self.CodeAction = None


    def _deserialize(self, params):
        if params.get("NormalAction") is not None:
            self.NormalAction = RuleNormalAction()
            self.NormalAction._deserialize(params.get("NormalAction"))
        if params.get("RewriteAction") is not None:
            self.RewriteAction = RuleRewriteAction()
            self.RewriteAction._deserialize(params.get("RewriteAction"))
        if params.get("CodeAction") is not None:
            self.CodeAction = RuleCodeAction()
            self.CodeAction._deserialize(params.get("CodeAction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAndConditions(AbstractModel):
    """规则引擎条件且关系条件列表

    """

    def __init__(self):
        r"""
        :param Conditions: 规则引擎条件，该数组内所有项全部满足即判断该条件满足。
        :type Conditions: list of RuleCondition
        """
        self.Conditions = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleChoicePropertiesItem(AbstractModel):
    """规则引擎可应用于匹配请求的设置详细信息，可选参数配置项

    """

    def __init__(self):
        r"""
        :param Name: 参数名称。
        :type Name: str
        :param Type: 参数值类型。
<li> CHOICE：参数值只能在 ChoicesValue 中选择； </li>
<li> TOGGLE：参数值为开关类型，可在 ChoicesValue 中选择；</li>
<li> CUSTOM_NUM：参数值用户自定义，整型类型；</li>
<li> CUSTOM_STRING：参数值用户自定义，字符串类型。</li>
        :type Type: str
        :param ChoicesValue: 参数值的可选值。
注意：若参数值为用户自定义则该数组为空数组。
        :type ChoicesValue: list of str
        :param Min: 数值参数的最小值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Min: int
        :param Max: 数值参数的最大值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Max: int
        :param IsMultiple: 参数值是否支持多选或者填写多个。
        :type IsMultiple: bool
        :param IsAllowEmpty: 是否允许为空。
        :type IsAllowEmpty: bool
        :param ExtraParameter: 特殊参数。
<li> 为 NULL：RuleAction 选择 NormalAction；</li>
<li> 成员参数 Id 为 Action：RuleAction 选择 RewirteAction；</li>
<li> 成员参数 Id 为 StatusCode：RuleAction 选择 CodeAction。</li>
        :type ExtraParameter: :class:`tencentcloud.teo.v20220106.models.RuleExtraParameter`
        """
        self.Name = None
        self.Type = None
        self.ChoicesValue = None
        self.Min = None
        self.Max = None
        self.IsMultiple = None
        self.IsAllowEmpty = None
        self.ExtraParameter = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.ChoicesValue = params.get("ChoicesValue")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.IsMultiple = params.get("IsMultiple")
        self.IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ExtraParameter") is not None:
            self.ExtraParameter = RuleExtraParameter()
            self.ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCodeAction(AbstractModel):
    """规则引擎带有状态码的动作

    """

    def __init__(self):
        r"""
        :param Action: 功能名称，功能名称填写规范可调用接口 [查询规则引擎的设置参数](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) 查看。
        :type Action: str
        :param Parameters: 操作参数。
        :type Parameters: list of RuleCodeActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleCodeActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCodeActionParams(AbstractModel):
    """规则引擎条件使用StatusCode字段动作参数

    """

    def __init__(self):
        r"""
        :param StatusCode: 状态 Code。
        :type StatusCode: int
        :param Name: 参数名称，参数填写规范可调用接口 [查询规则引擎的设置参数](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) 查看。
        :type Name: str
        :param Values: 参数值。
        :type Values: list of str
        """
        self.StatusCode = None
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    """规则引擎条件参数

    """

    def __init__(self):
        r"""
        :param Operator: 运算符，取值有：
<li> equal: 等于； </li>
<li> notequal: 不等于。</li>
        :type Operator: str
        :param Target: 匹配类型，取值有：
<li> 全部（站点任意请求）: host。 </li>
<li> 文件名: filename； </li>
<li> 文件后缀: extension； </li>
<li> HOST: host； </li>
<li> URL Full: full_url，当前站点下完整 URL 路径，必须包含 HTTP 协议，Host 和 路径； </li>
<li> URL Path: url，当前站点下 URL 路径的请求。 </li>
        :type Target: str
        :param Values: 对应匹配类型的参数值，对应匹配类型的取值有：
<li> 文件后缀：jpg、txt等文件后缀；</li>
<li> 文件名称：例如 foo.jpg 中的 foo；</li>
<li> 全部（站点任意请求）： all； </li>
<li> HOST：当前站点下的 host ，例如www.maxx55.com；</li>
<li> URL Path：当前站点下 URL 路径的请求，例如：/example；</li>
<li> URL Full：当前站点下完整 URL 请求，必须包含 HTTP 协议，Host 和 路径，例如：https://www.maxx55.cn/example。</li>
        :type Values: list of str
        """
        self.Operator = None
        self.Target = None
        self.Values = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Target = params.get("Target")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExtraParameter(AbstractModel):
    """规则引擎参数详情信息，特殊参数类型。

    """

    def __init__(self):
        r"""
        :param Id: 参数名，取值有：
<li> Action：修改 HTTP 头部所需参数，RuleAction 选择 RewirteAction；</li>
<li> StatusCode：状态码相关功能所需参数，RuleAction 选择 CodeAction。</li>
        :type Id: str
        :param Type: 参数值类型。
<li> CHOICE：参数值只能在 Values 中选择； </li>
<li> CUSTOM_NUM：参数值用户自定义，整型类型；</li>
<li> CUSTOM_STRING：参数值用户自定义，字符串类型。</li>
        :type Type: str
        :param Choices: 可选参数值。
注意：当 Id 的值为 StatusCode 时数组中的值为整型，填写参数值时请填写字符串的整型数值。
        :type Choices: str
        """
        self.Id = None
        self.Type = None
        self.Choices = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Choices = params.get("Choices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFilter(AbstractModel):
    """规则查询 Filter

    """

    def __init__(self):
        r"""
        :param Name: 过滤参数，取值有：
<li> RULE_ID：规则 ID。 </li>
        :type Name: str
        :param Values: 参数值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleItem(AbstractModel):
    """规则引擎规则项，Conditions 数组内多个项的关系为 或，内层 Conditions 列表内多个项的关系为 且。

    """

    def __init__(self):
        r"""
        :param Conditions: 执行功能判断条件。
注意：满足该数组内任意一项条件，功能即可执行。
        :type Conditions: list of RuleAndConditions
        :param Actions: 执行的功能。
        :type Actions: list of RuleAction
        """
        self.Conditions = None
        self.Actions = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = RuleAction()
                obj._deserialize(item)
                self.Actions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleNormalAction(AbstractModel):
    """规则引擎常规类型的动作

    """

    def __init__(self):
        r"""
        :param Action: 功能名称，功能名称填写规范可调用接口 [查询规则引擎的设置参数](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) 查看。
        :type Action: str
        :param Parameters: 参数。
        :type Parameters: list of RuleNormalActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleNormalActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleNormalActionParams(AbstractModel):
    """规则引擎条件常规动作参数

    """

    def __init__(self):
        r"""
        :param Name: 参数名称，参数填写规范可调用接口 [查询规则引擎的设置参数](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) 查看。
        :type Name: str
        :param Values: 参数值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleRewriteAction(AbstractModel):
    """规则引擎HTTP请求头/响应头类型的动作

    """

    def __init__(self):
        r"""
        :param Action: 功能名称，功能名称填写规范可调用接口 [查询规则引擎的设置参数](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) 查看。
        :type Action: str
        :param Parameters: 参数。
        :type Parameters: list of RuleRewriteActionParams
        """
        self.Action = None
        self.Parameters = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = RuleRewriteActionParams()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleRewriteActionParams(AbstractModel):
    """规则引擎条件 HTTP 请求/响应头操作动作参数。

    """

    def __init__(self):
        r"""
        :param Action: 功能参数名称，参数填写规范可调用接口 [查询规则引擎的设置参数](https://tcloud4api.woa.com/document/product/1657/79433?!preview&!document=1) 查看。现在只有三种取值：
<li> add：添加 HTTP 头部；</li>
<li> set：重写 HTTP 头部；</li>
<li> del：删除 HTTP 头部。</li>
        :type Action: str
        :param Name: 参数名称。
        :type Name: str
        :param Values: 参数值。
        :type Values: list of str
        """
        self.Action = None
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleSettingDetail(AbstractModel):
    """规则引擎规则详情

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID。
        :type RuleId: str
        :param RuleName: 规则名称，名称字符串长度 1~255。
        :type RuleName: str
        :param Status: 规则状态，取值有:
<li> enable: 启用； </li>
<li> disable: 未启用。 </li>
        :type Status: str
        :param Rules: 规则内容。
        :type Rules: list of RuleItem
        :param RulePriority: 规则优先级, 值越大优先级越高，最小为 1。
        :type RulePriority: int
        """
        self.RuleId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None
        self.RulePriority = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleItem()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RulePriority = params.get("RulePriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesProperties(AbstractModel):
    """规则引擎可应用于匹配请求的设置详细信息。

    """

    def __init__(self):
        r"""
        :param Name: 值为参数名称。
        :type Name: str
        :param Min: 数值参数的最小值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Min: int
        :param ChoicesValue: 参数值的可选值。
注意：若参数值为用户自定义则该数组为空数组。
        :type ChoicesValue: list of str
        :param Type: 参数值类型。
<li> CHOICE：参数值只能在 ChoicesValue 中选择； </li>
<li> TOGGLE：参数值为开关类型，可在 ChoicesValue 中选择；</li>
<li> OBJECT：参数值为对象类型，ChoiceProperties 为改对象类型关联的属性；</li>
<li> CUSTOM_NUM：参数值用户自定义，整型类型；</li>
<li> CUSTOM_STRING：参数值用户自定义，字符串类型。</li>注意：当参数类型为 OBJECT 类型时，请注意参考 [示例2 参数为 OBJECT 类型的创建](https://tcloud4api.woa.com/document/product/1657/79382?!preview&!document=1)
        :type Type: str
        :param Max: 数值参数的最大值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Max: int
        :param IsMultiple: 参数值是否支持多选或者填写多个。
        :type IsMultiple: bool
        :param IsAllowEmpty: 是否允许为空。
        :type IsAllowEmpty: bool
        :param ChoiceProperties: 该参数对应的关联配置参数，属于调用接口的必填参数。
注意：如果可选参数无特殊新增参数则该数组为空数组。
        :type ChoiceProperties: list of RuleChoicePropertiesItem
        :param ExtraParameter: <li> 为 NULL：无特殊参数，RuleAction 选择 NormalAction；</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraParameter: :class:`tencentcloud.teo.v20220106.models.RuleExtraParameter`
        """
        self.Name = None
        self.Min = None
        self.ChoicesValue = None
        self.Type = None
        self.Max = None
        self.IsMultiple = None
        self.IsAllowEmpty = None
        self.ChoiceProperties = None
        self.ExtraParameter = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Min = params.get("Min")
        self.ChoicesValue = params.get("ChoicesValue")
        self.Type = params.get("Type")
        self.Max = params.get("Max")
        self.IsMultiple = params.get("IsMultiple")
        self.IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ChoiceProperties") is not None:
            self.ChoiceProperties = []
            for item in params.get("ChoiceProperties"):
                obj = RuleChoicePropertiesItem()
                obj._deserialize(item)
                self.ChoiceProperties.append(obj)
        if params.get("ExtraParameter") is not None:
            self.ExtraParameter = RuleExtraParameter()
            self.ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesSettingAction(AbstractModel):
    """规则引擎可应用于匹配请求的设置列表及其详细信息

    """

    def __init__(self):
        r"""
        :param Action: 功能名称，取值有：
<li> 访问URL 重写（AccessUrlRedirect）；</li>
<li> 回源 URL 重写 （UpstreamUrlRedirect）；</li>
<li> 自定义错误页面
(ErrorPage)；</li>
<li> QUIC（QUIC）；</li>
<li> WebSocket （WebSocket）；</li>
<li> 视频拖拽（VideoSeek）；</li>
<li> Token 鉴权（Authentication）；</li>
<li> 自定义CacheKey（CacheKey）；</li>
<li> 节点缓存 TTL （Cache）；</li>
<li> 浏览器缓存 TTL（MaxAge）；</li>
<li> 离线缓存（OfflineCache）；</li>
<li> 智能加速（SmartRouting）；</li>
<li> 分片回源（RangeOriginPull）；</li>
<li> HTTP/2 回源（UpstreamHttp2）；</li>
<li> Host Header 重写（HostHeader）；</li>
<li> 强制 HTTPS（ForceRedirect）；</li>
<li> 回源 HTTPS（OriginPullProtocol）；</li>
<li> 缓存预刷新（CachePrefresh）；</li>
<li> 智能压缩（Compression）；</li>
<li> 修改 HTTP 请求头（RequestHeader）；</li>
<li> 修改HTTP响应头（ResponseHeader）;</li>
<li> 状态码缓存 TTL（StatusCodeCache）;</li>
<li> Hsts；</li>
<li> ClientIpHeader；</li>
<li> TlsVersion；</li>
<li> OcspStapling。</li>
        :type Action: str
        :param Properties: 参数信息。
        :type Properties: list of RulesProperties
        """
        self.Action = None
        self.Properties = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        if params.get("Properties") is not None:
            self.Properties = []
            for item in params.get("Properties"):
                obj = RulesProperties()
                obj._deserialize(item)
                self.Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param Key: 查询维度值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 查询维度下详细数据。
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
        :param Metric: 指标名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param Detail: 时序数据详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of TimingDataItem
        :param Max: 最大值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: int
        :param Avg: 平均值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Avg: float
        :param Sum: 数据总和。
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
        


class SecRuleRelatedInfo(AbstractModel):
    """安全规则（cc/waf/bot）相关信息

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID列表（99999为无效id）。
        :type RuleId: int
        :param Action: 执行动作（处置方式），取值有：
<li>trans ：通过 ；</li>
<li>alg ：算法挑战 ；</li>
<li>drop ：丢弃 ；</li>
<li>ban ：封禁源ip ；</li>
<li>redirect ：重定向 ；</li>
<li>page ：返回指定页面 ；</li>
<li>monitor ：观察 。</li>
        :type Action: str
        :param RiskLevel: 风险等级（waf日志中独有），取值有：
<li>high risk ：高危 ；</li>
<li>middle risk ：中危 ；</li>
<li>low risk ：低危 ；</li>
<li>unkonw ：未知 。</li>
        :type RiskLevel: str
        :param RuleLevel: 规则等级，取值有：
<li>normal  ：正常 。</li>
        :type RuleLevel: str
        :param Description: 规则描述。
        :type Description: str
        :param RuleTypeName: 规则类型名称。
        :type RuleTypeName: str
        """
        self.RuleId = None
        self.Action = None
        self.RiskLevel = None
        self.RuleLevel = None
        self.Description = None
        self.RuleTypeName = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Action = params.get("Action")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleLevel = params.get("RuleLevel")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityConfig(AbstractModel):
    """安全配置。

    """

    def __init__(self):
        r"""
        :param WafConfig: 托管规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WafConfig: :class:`tencentcloud.teo.v20220106.models.WafConfig`
        :param RateLimitConfig: 速率限制。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220106.models.RateLimitConfig`
        :param DdosConfig: DDoS配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DdosConfig: :class:`tencentcloud.teo.v20220106.models.DDoSConfig`
        :param AclConfig: 自定义规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AclConfig: :class:`tencentcloud.teo.v20220106.models.AclConfig`
        :param BotConfig: Bot配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type BotConfig: :class:`tencentcloud.teo.v20220106.models.BotConfig`
        :param SwitchConfig: 七层防护总开关。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchConfig: :class:`tencentcloud.teo.v20220106.models.SwitchConfig`
        :param IpTableConfig: 基础访问管控。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTableConfig: :class:`tencentcloud.teo.v20220106.models.IpTableConfig`
        :param ExceptConfig: 例外规则配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptConfig: :class:`tencentcloud.teo.v20220106.models.ExceptConfig`
        :param DropPageConfig: 自定义拦截页面配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropPageConfig: :class:`tencentcloud.teo.v20220106.models.DropPageConfig`
        """
        self.WafConfig = None
        self.RateLimitConfig = None
        self.DdosConfig = None
        self.AclConfig = None
        self.BotConfig = None
        self.SwitchConfig = None
        self.IpTableConfig = None
        self.ExceptConfig = None
        self.DropPageConfig = None


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
        if params.get("ExceptConfig") is not None:
            self.ExceptConfig = ExceptConfig()
            self.ExceptConfig._deserialize(params.get("ExceptConfig"))
        if params.get("DropPageConfig") is not None:
            self.DropPageConfig = DropPageConfig()
            self.DropPageConfig._deserialize(params.get("DropPageConfig"))
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
        :param CertId: 服务器证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Alias: 证书备注名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Type: 证书类型，取值有：
<li>default: 默认证书;</li>
<li>upload:用户上传;</li>
<li>managed:腾讯云托管。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书部署时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param Status: 部署状态，取值有：
<li>processing: 部署中;</li>
<li>deployed: 已部署。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param SignAlgo: 证书算法。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignAlgo: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Status = None
        self.SignAlgo = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Status = params.get("Status")
        self.SignAlgo = params.get("SignAlgo")
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
        :param Switch: 智能加速配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
        


class Sv(AbstractModel):
    """询价参数

    """

    def __init__(self):
        r"""
        :param Key: 询价参数键。
        :type Key: str
        :param Value: 询价参数值。
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
        


class SwitchConfig(AbstractModel):
    """功能总开关

    """

    def __init__(self):
        r"""
        :param WebSwitch: Web类型的安全总开关生效范围，Waf，自定义规则，速率限制。
1. on 开启
2. off 关闭
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
        :param Timestamp: 返回数据对应时间点，采用unix秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param Value: 具体数值
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
        :param Key: top查询维度值。
        :type Key: str
        :param Value: 查询具体数据。
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
        :param Name: 排序实体名。
        :type Name: str
        :param Count: 排序实体数量。
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
        :param Switch: http2回源配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
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
    """Waf配置。

    """

    def __init__(self):
        r"""
        :param Switch: WafConfig开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>开关仅与配置是否生效有关，即使为off（关闭），也可以正常修改配置的内容。
        :type Switch: str
        :param Level: 防护级别，取值有：
<li> loose：宽松；</li>
<li> normal：正常；</li>
<li> strict：严格；</li>
<li> stricter：超严格；</li>
<li> custom：自定义。</li>
        :type Level: str
        :param Mode: 全局WAF模式，取值有：
<li> block：阻断（全局阻断，但可对详细规则配置观察）；</li>
<li> observe：观察（无论详细规则配置什么，都为观察）。</li>
        :type Mode: str
        :param WafRules: 托管规则详细配置。
        :type WafRules: :class:`tencentcloud.teo.v20220106.models.WafRule`
        :param AiRule: AI规则引擎防护配置。
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
        :param Switch: 托管规则开关。 on为开启
        :type Switch: str
        :param BlockRuleIDs: 黑名单ID列表，将规则ID加入本参数列表中代表该ID关闭，即该规则ID不再生效。ID参考接口 [DescribeSecurityPolicyManagedRules](https://tcloud4api.woa.com/document/product/1657/76030?!preview&!document=1)。
        :type BlockRuleIDs: list of int
        :param ObserveRuleIDs: 观察模式ID列表，将规则ID加入本参数列表中代表该ID使用观察模式生效，即该规则ID进入观察模式。ID参考接口 [DescribeSecurityPolicyManagedRules](https://tcloud4api.woa.com/document/product/1657/76030?!preview&!document=1)。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObserveRuleIDs: list of int
        """
        self.Switch = None
        self.BlockRuleIDs = None
        self.ObserveRuleIDs = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockRuleIDs = params.get("BlockRuleIDs")
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
        :param List: 分组数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of WebLogs
        :param PageNo: 分页拉取的起始页号。最小值：1。
        :type PageNo: int
        :param PageSize: 分页拉取的最大返回结果数。最大值：1000。
        :type PageSize: int
        :param Pages: 总页数。
        :type Pages: int
        :param TotalSize: 总条数。
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
        :param AttackContent: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackContent: str
        :param AttackIp: 攻击源（客户端）Ip。
        :type AttackIp: str
        :param AttackType: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackType: str
        :param Domain: 受攻击子域名。
        :type Domain: str
        :param Msuuid: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msuuid: str
        :param RequestMethod: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestMethod: str
        :param RequestUri: URI
        :type RequestUri: str
        :param RiskLevel: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param RuleId: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param SipCountryCode: IP所在国家iso-3166中alpha-2编码，编码信息请参考[ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json)
        :type SipCountryCode: str
        :param EventId: 请求（事件）ID。
        :type EventId: str
        :param DisposalMethod: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisposalMethod: str
        :param HttpLog: http log。
        :type HttpLog: str
        :param Ua: 该字段已废弃。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ua: str
        :param AttackTime: 攻击时间，采用unix秒级时间戳。
        :type AttackTime: int
        :param RuleDetailList: 规则相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDetailList: list of SecRuleRelatedInfo
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
        self.RuleDetailList = None


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
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
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
        :param Switch: WebSocket 超时时间配置开关，取值有：
<li>on：使用Timeout作为WebSocket超时时间；</li>
<li>off：平台仍支持WebSocket连接，此时使用系统默认的15秒为超时时间。</li>
        :type Switch: str
        :param Timeout: 超时时间，单位为秒，最大超时时间120秒。
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
        :param Id: 站点ID。
        :type Id: str
        :param Name: 站点名称。
        :type Name: str
        :param OriginalNameServers: 站点当前使用的 NS 列表。
        :type OriginalNameServers: list of str
        :param NameServers: 腾讯云分配的 NS 列表。
        :type NameServers: list of str
        :param Status: 站点状态，取值有：
<li> active：NS 已切换； </li>
<li> pending：NS 未切换；</li>
<li> moved：NS 已切走；</li>
<li> deactivated：被封禁。 </li>
        :type Status: str
        :param Type: 站点接入方式，取值有
<li> full：NS 接入； </li>
<li> partial：CNAME 接入。</li>
        :type Type: str
        :param Paused: 站点是否关闭。
        :type Paused: bool
        :param CnameSpeedUp: 是否开启cname加速，取值有：
<li> enabled：开启；</li>
<li> disabled：关闭。</li>
        :type CnameSpeedUp: str
        :param CnameStatus: cname 接入状态，取值有：
<li> finished：站点已验证；</li>
<li> pending：站点验证中。</li>
        :type CnameStatus: str
        :param Tags: 资源标签列表。
        :type Tags: list of Tag
        :param Resources: 计费资源列表。
        :type Resources: list of Resource
        :param CreatedOn: 站点创建时间。
        :type CreatedOn: str
        :param ModifiedOn: 站点修改时间。
        :type ModifiedOn: str
        :param Area: 站点接入地域，取值为：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>
        :type Area: str
        """
        self.Id = None
        self.Name = None
        self.OriginalNameServers = None
        self.NameServers = None
        self.Status = None
        self.Type = None
        self.Paused = None
        self.CnameSpeedUp = None
        self.CnameStatus = None
        self.Tags = None
        self.Resources = None
        self.CreatedOn = None
        self.ModifiedOn = None
        self.Area = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.OriginalNameServers = params.get("OriginalNameServers")
        self.NameServers = params.get("NameServers")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Paused = params.get("Paused")
        self.CnameSpeedUp = params.get("CnameSpeedUp")
        self.CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
        self.Area = params.get("Area")
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
<li> name：站点名；</li>
<li> status：站点状态；</li>
<li> tagKey：标签键；</li>
<li> tagValue: 标签值。</li>
        :type Name: str
        :param Values: 过滤字段值。
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为name。模糊查询时，Values长度最大为1。默认为false。
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
        