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


class AccelerateMainland(AbstractModel):
    """中国大陆加速优化配置。

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启中国大陆加速优化配置，取值有：
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
        


class AccelerateType(AbstractModel):
    """加速类型

    """

    def __init__(self):
        r"""
        :param Switch: 加速开关。取值范围：
<li> on：打开;</li>
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
        


class AccelerationDomain(AbstractModel):
    """加速域名

    """

    def __init__(self):
        r"""
        :param OriginDetail: 源站信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginDetail: :class:`tencentcloud.teo.v20220901.models.OriginDetail`
        :param CreatedOn: 创建时间。
        :type CreatedOn: str
        :param DomainName: 加速域名名称。
        :type DomainName: str
        :param ModifiedOn: 修改时间。
        :type ModifiedOn: str
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param DomainStatus: 加速域名状态，取值有：
<li>online：已生效；</li>
<li>process：部署中；</li>
<li>offline：已停用；</li>
<li>forbidden：已封禁；</li>
<li>init：未生效，待激活站点；</li>
        :type DomainStatus: str
        :param Cname: CNAME 地址。
        :type Cname: str
        :param IdentificationStatus: 加速域名归属权验证状态，取值有： <li>pending：待验证；</li> <li>finished：已完成验证。</li>	
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentificationStatus: str
        """
        self.OriginDetail = None
        self.CreatedOn = None
        self.DomainName = None
        self.ModifiedOn = None
        self.ZoneId = None
        self.DomainStatus = None
        self.Cname = None
        self.IdentificationStatus = None


    def _deserialize(self, params):
        if params.get("OriginDetail") is not None:
            self.OriginDetail = OriginDetail()
            self.OriginDetail._deserialize(params.get("OriginDetail"))
        self.CreatedOn = params.get("CreatedOn")
        self.DomainName = params.get("DomainName")
        self.ModifiedOn = params.get("ModifiedOn")
        self.ZoneId = params.get("ZoneId")
        self.DomainStatus = params.get("DomainStatus")
        self.Cname = params.get("Cname")
        self.IdentificationStatus = params.get("IdentificationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclCondition(AbstractModel):
    """精准防护条件

    """

    def __init__(self):
        r"""
        :param MatchFrom: 匹配字段，取值有：
<li>host：请求域名；</li>
<li>sip：客户端IP；</li>
<li>ua：User-Agent；</li>
<li>cookie：会话 Cookie；</li>
<li>cgi：CGI 脚本；</li>
<li>xff：XFF 扩展头部；</li>
<li>url：请求 URL；</li>
<li>accept：请求内容类型；</li>
<li>method：请求方式；</li>
<li>header：请求头部；</li>
<li>app_proto：应用层协议；</li>
<li>sip_proto：网络层协议；</li>
<li>uabot：UA 特征规则，仅bot自定义规则可用；</li>
<li>idcid：IDC 规则，仅bot自定义规则可用；</li>
<li>sipbot：搜索引擎规则，仅bot自定义规则可用；</li>
<li>portrait：画像分析，仅bot自定义规则可用；</li>
<li>header_seq：请求头顺序，仅bot自定义规则可用。</li>
        :type MatchFrom: str
        :param MatchParam: 匹配字符串。当 MatchFrom 为 header 时，可以填入 header 的 key 作为参数。
        :type MatchParam: str
        :param Operator: 匹配关系，取值有：
<li>equal：字符串等于；</li>
<li>not_equal：数值不等于；</li>
<li>include：字符包含；</li>
<li>not_include：字符不包含；</li>
<li>match：ip匹配；</li>
<li>not_match：ip不匹配；</li>
<li>include_area：地域包含；</li>
<li>is_empty：存在字段但值为空；</li>
<li>not_exists：不存在关键字段；</li>
<li>regexp：正则匹配；</li>
<li>len_gt：数值大于；</li>
<li>len_lt：数值小于；</li>
<li>len_eq：数值等于；</li>
<li>match_prefix：前缀匹配；</li>
<li>match_suffix：后缀匹配；</li>
<li>wildcard：通配符。</li>
        :type Operator: str
        :param MatchContent: 匹配内容。
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
        


class AclConfig(AbstractModel):
    """ACL配置

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param AclUserRules: 用户自定义规则。
        :type AclUserRules: list of AclUserRule
        :param Customizes: 托管定制规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Customizes: list of AclUserRule
        """
        self.Switch = None
        self.AclUserRules = None
        self.Customizes = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("AclUserRules") is not None:
            self.AclUserRules = []
            for item in params.get("AclUserRules"):
                obj = AclUserRule()
                obj._deserialize(item)
                self.AclUserRules.append(obj)
        if params.get("Customizes") is not None:
            self.Customizes = []
            for item in params.get("Customizes"):
                obj = AclUserRule()
                obj._deserialize(item)
                self.Customizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclUserRule(AbstractModel):
    """用户自定义规则

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名。
        :type RuleName: str
        :param Action: 处罚动作，取值有：
<li>trans：放行；</li>
<li>drop：拦截；</li>
<li>monitor：观察；</li>
<li>ban：IP封禁；</li>
<li>redirect：重定向；</li>
<li>page：指定页面；</li>
<li>alg：Javascript挑战。</li>
        :type Action: str
        :param RuleStatus: 规则状态，取值有：
<li>on：生效；</li>
<li>off：失效。</li>
        :type RuleStatus: str
        :param AclConditions: 自定义规则。
        :type AclConditions: list of AclCondition
        :param RulePriority: 规则优先级，取值范围0-100。
        :type RulePriority: int
        :param RuleID: 规则Id。仅出参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param UpdateTime: 更新时间。仅出参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param PunishTime: ip封禁的惩罚时间，取值范围0-2天。默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param PunishTimeUnit: ip封禁的惩罚时间单位，取值有：
<li>second：秒；</li>
<li>minutes：分；</li>
<li>hour：小时。</li>默认为second。
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTimeUnit: str
        :param Name: 自定义返回页面的名称。默认为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param PageId: 自定义返回页面的实例id。默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: int
        :param RedirectUrl: 重定向时候的地址，必须为本用户接入的站点子域名。默认为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param ResponseCode: 重定向时候的返回码。默认为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseCode: int
        """
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.AclConditions = None
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
        if params.get("AclConditions") is not None:
            self.AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self.AclConditions.append(obj)
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
        


class Action(AbstractModel):
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
<li> SslTlsSecureConf；</li>
<li> OcspStapling；</li>
<li> HTTP/2 访问（Http2）；</li>
<li> 回源跟随重定向(UpstreamFollowRedirect)；</li>
<li> 修改源站(Origin)。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalAction: :class:`tencentcloud.teo.v20220901.models.NormalAction`
        :param RewriteAction: 带有请求头/响应头的功能操作，选择该类型的功能项有：
<li> 修改 HTTP 请求头（RequestHeader）；</li>
<li> 修改HTTP响应头（ResponseHeader）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteAction: :class:`tencentcloud.teo.v20220901.models.RewriteAction`
        :param CodeAction: 带有状态码的功能操作，选择该类型的功能项有：
<li> 自定义错误页面（ErrorPage）；</li>
<li> 状态码缓存 TTL（StatusCodeCache）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeAction: :class:`tencentcloud.teo.v20220901.models.CodeAction`
        """
        self.NormalAction = None
        self.RewriteAction = None
        self.CodeAction = None


    def _deserialize(self, params):
        if params.get("NormalAction") is not None:
            self.NormalAction = NormalAction()
            self.NormalAction._deserialize(params.get("NormalAction"))
        if params.get("RewriteAction") is not None:
            self.RewriteAction = RewriteAction()
            self.RewriteAction._deserialize(params.get("RewriteAction"))
        if params.get("CodeAction") is not None:
            self.CodeAction = CodeAction()
            self.CodeAction._deserialize(params.get("CodeAction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedFilter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询，支持模糊查询。例如过滤ID、名称、状态等。
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        :param Fuzzy: 是否启用模糊查询。
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
        


class AiRule(AbstractModel):
    """AI规则引擎防护

    """

    def __init__(self):
        r"""
        :param Mode: AI规则引擎状态，取值有：
<li> smart_status_close：关闭；</li>
<li> smart_status_open：拦截处置；</li>
<li> smart_status_observe：观察处置。</li>
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
        


class AlgDetectJS(AbstractModel):
    """Bot主动特征识别客户端行为校验。

    """

    def __init__(self):
        r"""
        :param Name: 操作名称。
        :type Name: str
        :param WorkLevel: 工作量证明 (proof_Of-Work)校验强度，默认low，取值有：
<li>low：低；</li>
<li>middle：中；</li>
<li>high：高。</li>
        :type WorkLevel: str
        :param ExecuteMode: 执行方式，js延迟执行的时间。单位为ms，默认500，取值：0～1000。
        :type ExecuteMode: int
        :param InvalidStatTime: 客户端末启用JS（末完成检测）统计周期。单位为秒，默认10，取值：5～3600。
        :type InvalidStatTime: int
        :param InvalidThreshold: 客户端末启用JS（末完成检测）触发阈值。单位为次，默认300，取值：1～100000000。
        :type InvalidThreshold: int
        :param AlgDetectResults: Bot主动特征识别客户端行为校验结果。
        :type AlgDetectResults: list of AlgDetectResult
        """
        self.Name = None
        self.WorkLevel = None
        self.ExecuteMode = None
        self.InvalidStatTime = None
        self.InvalidThreshold = None
        self.AlgDetectResults = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.WorkLevel = params.get("WorkLevel")
        self.ExecuteMode = params.get("ExecuteMode")
        self.InvalidStatTime = params.get("InvalidStatTime")
        self.InvalidThreshold = params.get("InvalidThreshold")
        if params.get("AlgDetectResults") is not None:
            self.AlgDetectResults = []
            for item in params.get("AlgDetectResults"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self.AlgDetectResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectResult(AbstractModel):
    """Bot主动特征识别校验结果。

    """

    def __init__(self):
        r"""
        :param Result: 校验结果，取值有：
<li>invalid：不合法Cookie；</li>
<li>cookie_empty：末携带Cookie或Cookie己过期；</li>
<li>js_empty：客户端末启用JS（末完成检测）；</li>
<li>low：会话速率和周期特征校验低风险；</li>
<li>middle：会话速率和周期特征校验中风险；</li>
<li>high：会话速率和周期特征校验高风险；</li>
<li>timeout：检测超时时长；</li>
<li>not_browser：不合法浏览器；</li>
<li>is_bot：Bot客户端。</li>
        :type Result: str
        :param Action: 处罚动作，取值有：
<li>drop：拦截；</li>
<li>monitor：观察；</li>
<li>silence：静默；</li>
<li>shortdelay：（短时间）等待后响应；</li>
<li>longdelay：（长时间）等待后响应。</li>
        :type Action: str
        """
        self.Result = None
        self.Action = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectRule(AbstractModel):
    """Bot主动特征识别规则。

    """

    def __init__(self):
        r"""
        :param RuleID: 规则id。
        :type RuleID: int
        :param RuleName: 规则名。
        :type RuleName: str
        :param Switch: 规则开关。
        :type Switch: str
        :param AlgConditions: 自定义规则。
        :type AlgConditions: list of AclCondition
        :param AlgDetectSession: Cookie校验和会话行为分析。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgDetectSession: :class:`tencentcloud.teo.v20220901.models.AlgDetectSession`
        :param AlgDetectJS: 客户端行为校验。
        :type AlgDetectJS: list of AlgDetectJS
        :param UpdateTime: 更新时间。仅出参使用。
        :type UpdateTime: str
        """
        self.RuleID = None
        self.RuleName = None
        self.Switch = None
        self.AlgConditions = None
        self.AlgDetectSession = None
        self.AlgDetectJS = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RuleID = params.get("RuleID")
        self.RuleName = params.get("RuleName")
        self.Switch = params.get("Switch")
        if params.get("AlgConditions") is not None:
            self.AlgConditions = []
            for item in params.get("AlgConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self.AlgConditions.append(obj)
        if params.get("AlgDetectSession") is not None:
            self.AlgDetectSession = AlgDetectSession()
            self.AlgDetectSession._deserialize(params.get("AlgDetectSession"))
        if params.get("AlgDetectJS") is not None:
            self.AlgDetectJS = []
            for item in params.get("AlgDetectJS"):
                obj = AlgDetectJS()
                obj._deserialize(item)
                self.AlgDetectJS.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectSession(AbstractModel):
    """Cookie校验与会话跟踪。

    """

    def __init__(self):
        r"""
        :param Name: 操作名称。
        :type Name: str
        :param DetectMode: 校验方式，默认update_detect，取值有：
<li>detect：仅校验；</li>
<li>update_detect：更新Cookie并校验。</li>
        :type DetectMode: str
        :param SessionAnalyzeSwitch: 会话速率和周期特征校验开关，默认off，取值有：
<li>off：关闭；</li>
<li>on：打开。</li>
        :type SessionAnalyzeSwitch: str
        :param InvalidStatTime: 校验结果为未携带Cookie或Cookie已过期的统计周期。单位为秒，默认10，取值：5～3600。
        :type InvalidStatTime: int
        :param InvalidThreshold: 校验结果为未携带Cookie或Cookie已过期的触发阈值。单位为次，默认300，取值：1～100000000。
        :type InvalidThreshold: int
        :param AlgDetectResults: Cookie校验校验结果。
        :type AlgDetectResults: list of AlgDetectResult
        :param SessionBehaviors: 会话速率和周期特征校验结果。
        :type SessionBehaviors: list of AlgDetectResult
        """
        self.Name = None
        self.DetectMode = None
        self.SessionAnalyzeSwitch = None
        self.InvalidStatTime = None
        self.InvalidThreshold = None
        self.AlgDetectResults = None
        self.SessionBehaviors = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DetectMode = params.get("DetectMode")
        self.SessionAnalyzeSwitch = params.get("SessionAnalyzeSwitch")
        self.InvalidStatTime = params.get("InvalidStatTime")
        self.InvalidThreshold = params.get("InvalidThreshold")
        if params.get("AlgDetectResults") is not None:
            self.AlgDetectResults = []
            for item in params.get("AlgDetectResults"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self.AlgDetectResults.append(obj)
        if params.get("SessionBehaviors") is not None:
            self.SessionBehaviors = []
            for item in params.get("SessionBehaviors"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self.SessionBehaviors.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AliasDomain(AbstractModel):
    """别称域名信息。

    """

    def __init__(self):
        r"""
        :param AliasName: 别称域名名称。
        :type AliasName: str
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param TargetName: 目标域名名称。
        :type TargetName: str
        :param Status: 别称域名状态，取值有：
<li> active：已生效； </li>
<li> pending：部署中；</li>
<li> conflict：被找回。 </li>
<li> stop：已停用；</li>
        :type Status: str
        :param ForbidMode: 封禁模式，取值有：
<li> 0：未封禁； </li>
<li> 11：合规封禁；</li>
<li> 14：未备案封禁。</li>
        :type ForbidMode: int
        :param CreatedOn: 别称域名创建时间。
        :type CreatedOn: str
        :param ModifiedOn: 别称域名修改时间。
        :type ModifiedOn: str
        """
        self.AliasName = None
        self.ZoneId = None
        self.TargetName = None
        self.Status = None
        self.ForbidMode = None
        self.CreatedOn = None
        self.ModifiedOn = None


    def _deserialize(self, params):
        self.AliasName = params.get("AliasName")
        self.ZoneId = params.get("ZoneId")
        self.TargetName = params.get("TargetName")
        self.Status = params.get("Status")
        self.ForbidMode = params.get("ForbidMode")
        self.CreatedOn = params.get("CreatedOn")
        self.ModifiedOn = params.get("ModifiedOn")
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param ProxyName: 当ProxyType=hostname时，表示域名或子域名；
当ProxyType=instance时，表示代理名称。
        :type ProxyName: str
        :param ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>
        :type ProxyType: str
        :param PlatType: 调度模式，取值有：
<li>ip：表示Anycast IP调度；</li>
<li>domain：表示CNAME调度。</li>
        :type PlatType: str
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
默认值：overseas
        :type Area: str
        :param SecurityType: 是否开启安全，取值有：
<li>0：关闭安全；</li>
<li>1：开启安全。</li>
        :type SecurityType: int
        :param AccelerateType: 是否开启加速，取值有：
<li>0：关闭加速；</li>
<li>1：开启加速。</li>
        :type AccelerateType: int
        :param SessionPersistTime: 会话保持时间。
        :type SessionPersistTime: int
        :param Status: 状态，取值有：
<li>online：启用；</li>
<li>offline：停用；</li>
<li>progress：部署中；</li>
<li>stopping：停用中；</li>
<li>fail：部署失败/停用失败。</li>
        :type Status: str
        :param BanStatus: 封禁状态，取值有：
<li>banned：已封禁;</li>
<li>banning：封禁中；</li>
<li>recover：已解封；</li>
<li>recovering：解封禁中。</li>
        :type BanStatus: str
        :param ScheduleValue: 调度信息。
        :type ScheduleValue: list of str
        :param HostId: 当ProxyType=hostname时：
表示代理加速唯一标识。
        :type HostId: str
        :param Ipv6: Ipv6访问配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        :param ApplicationProxyRules: 规则列表。
        :type ApplicationProxyRules: list of ApplicationProxyRule
        :param AccelerateMainland: 中国大陆加速优化配置。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self.ZoneId = None
        self.ZoneName = None
        self.ProxyId = None
        self.ProxyName = None
        self.ProxyType = None
        self.PlatType = None
        self.Area = None
        self.SecurityType = None
        self.AccelerateType = None
        self.SessionPersistTime = None
        self.Status = None
        self.BanStatus = None
        self.ScheduleValue = None
        self.HostId = None
        self.Ipv6 = None
        self.UpdateTime = None
        self.ApplicationProxyRules = None
        self.AccelerateMainland = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.ProxyType = params.get("ProxyType")
        self.PlatType = params.get("PlatType")
        self.Area = params.get("Area")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.Status = params.get("Status")
        self.BanStatus = params.get("BanStatus")
        self.ScheduleValue = params.get("ScheduleValue")
        self.HostId = params.get("HostId")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        self.UpdateTime = params.get("UpdateTime")
        if params.get("ApplicationProxyRules") is not None:
            self.ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.ApplicationProxyRules.append(obj)
        if params.get("AccelerateMainland") is not None:
            self.AccelerateMainland = AccelerateMainland()
            self.AccelerateMainland._deserialize(params.get("AccelerateMainland"))
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
<li>单个端口，如：80。</li>
<li>端口段，如：81-82。表示81，82两个端口。</li>
注意：一条规则最多可填写20个端口。
        :type Port: list of str
        :param OriginType: 源站类型，取值有：
<li>custom：手动添加；</li>
<li>origins：源站组。</li>
        :type OriginType: str
        :param OriginValue: 源站信息：
<li>当 OriginType 为 custom 时，表示一个或多个源站，如`["8.8.8.8","9.9.9.9"]` 或 `OriginValue=["test.com"]`；</li>
<li>当 OriginType 为 origins 时，要求有且仅有一个元素，表示源站组ID，如`["origin-537f5b41-162a-11ed-abaa-525400c5da15"]`。</li>
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
<li>OFF：不传递。</li>默认值：OFF。
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持，取值有：
<li>true：开启；</li>
<li>false：关闭。</li>默认值：false。
        :type SessionPersist: bool
        :param OriginPort: 源站端口，支持格式：
<li>单端口，如：80。</li>
<li>端口段：81-82，表示81，82两个端口。</li>
        :type OriginPort: str
        """
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.RuleId = None
        self.Status = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.OriginPort = None


    def _deserialize(self, params):
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.OriginPort = params.get("OriginPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AscriptionInfo(AbstractModel):
    """站点归属信息

    """

    def __init__(self):
        r"""
        :param Subdomain: 主机记录。
        :type Subdomain: str
        :param RecordType: 记录类型。
        :type RecordType: str
        :param RecordValue: 记录值。
        :type RecordValue: str
        """
        self.Subdomain = None
        self.RecordType = None
        self.RecordValue = None


    def _deserialize(self, params):
        self.Subdomain = params.get("Subdomain")
        self.RecordType = params.get("RecordType")
        self.RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindZoneToPlanRequest(AbstractModel):
    """BindZoneToPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 未绑定套餐的站点ID。
        :type ZoneId: str
        :param PlanId: 待绑定的目标套餐ID。
        :type PlanId: str
        """
        self.ZoneId = None
        self.PlanId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindZoneToPlanResponse(AbstractModel):
    """BindZoneToPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BotConfig(AbstractModel):
    """安全Bot配置

    """

    def __init__(self):
        r"""
        :param Switch: bot开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param BotManagedRule: 通用详细基础规则。如果为null，默认使用历史配置。
        :type BotManagedRule: :class:`tencentcloud.teo.v20220901.models.BotManagedRule`
        :param BotPortraitRule: 用户画像规则。如果为null，默认使用历史配置。
        :type BotPortraitRule: :class:`tencentcloud.teo.v20220901.models.BotPortraitRule`
        :param IntelligenceRule: Bot智能分析。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntelligenceRule: :class:`tencentcloud.teo.v20220901.models.IntelligenceRule`
        :param BotUserRules: Bot自定义规则。如果为null，默认使用历史配置。
        :type BotUserRules: list of BotUserRule
        :param AlgDetectRule: Bot主动特征识别规则。
        :type AlgDetectRule: list of AlgDetectRule
        :param Customizes: Bot托管定制策略，入参可不填，仅出参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Customizes: list of BotUserRule
        """
        self.Switch = None
        self.BotManagedRule = None
        self.BotPortraitRule = None
        self.IntelligenceRule = None
        self.BotUserRules = None
        self.AlgDetectRule = None
        self.Customizes = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("BotManagedRule") is not None:
            self.BotManagedRule = BotManagedRule()
            self.BotManagedRule._deserialize(params.get("BotManagedRule"))
        if params.get("BotPortraitRule") is not None:
            self.BotPortraitRule = BotPortraitRule()
            self.BotPortraitRule._deserialize(params.get("BotPortraitRule"))
        if params.get("IntelligenceRule") is not None:
            self.IntelligenceRule = IntelligenceRule()
            self.IntelligenceRule._deserialize(params.get("IntelligenceRule"))
        if params.get("BotUserRules") is not None:
            self.BotUserRules = []
            for item in params.get("BotUserRules"):
                obj = BotUserRule()
                obj._deserialize(item)
                self.BotUserRules.append(obj)
        if params.get("AlgDetectRule") is not None:
            self.AlgDetectRule = []
            for item in params.get("AlgDetectRule"):
                obj = AlgDetectRule()
                obj._deserialize(item)
                self.AlgDetectRule.append(obj)
        if params.get("Customizes") is not None:
            self.Customizes = []
            for item in params.get("Customizes"):
                obj = BotUserRule()
                obj._deserialize(item)
                self.Customizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotExtendAction(AbstractModel):
    """Bot扩展处置方式，多处置动作组合。

    """

    def __init__(self):
        r"""
        :param Action: 处置动作，取值有：
<li>monitor：观察；</li>
<li>alg：JavaScript挑战；</li>
<li>captcha：托管挑战；</li>
<li>random：随机，按照ExtendActions分配处置动作和比例；</li>
<li>silence：静默；</li>
<li>shortdelay：短时响应；</li>
<li>longdelay：长时响应。</li>
        :type Action: str
        :param Percent: 处置方式的触发概率，范围0-100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        """
        self.Action = None
        self.Percent = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Percent = params.get("Percent")
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
        :param Action: 触发规则后的处置方式，取值有：
<li>drop：拦截；</li>
<li>trans：放行；</li>
<li>alg：Javascript挑战；</li>
<li>monitor：观察。</li>
        :type Action: str
        :param RuleID: 本规则的ID。仅出参使用。
        :type RuleID: int
        :param TransManagedIds: 放行的规则ID。默认所有规则不配置放行。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransManagedIds: list of int
        :param AlgManagedIds: JS挑战的规则ID。默认所有规则不配置JS挑战。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param CapManagedIds: 数字验证码的规则ID。默认所有规则不配置数字验证码。
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param MonManagedIds: 观察的规则ID。默认所有规则不配置观察。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param DropManagedIds: 拦截的规则ID。默认所有规则不配置拦截。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        """
        self.Action = None
        self.RuleID = None
        self.TransManagedIds = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.RuleID = params.get("RuleID")
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
        


class BotPortraitRule(AbstractModel):
    """bot 用户画像规则

    """

    def __init__(self):
        r"""
        :param Switch: 本功能的开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param RuleID: 本规则的ID。仅出参使用。
        :type RuleID: int
        :param AlgManagedIds: JS挑战的规则ID。默认所有规则不配置JS挑战。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param CapManagedIds: 数字验证码的规则ID。默认所有规则不配置数字验证码。
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param MonManagedIds: 观察的规则ID。默认所有规则不配置观察。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param DropManagedIds: 拦截的规则ID。默认所有规则不配置拦截。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        """
        self.Switch = None
        self.RuleID = None
        self.AlgManagedIds = None
        self.CapManagedIds = None
        self.MonManagedIds = None
        self.DropManagedIds = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RuleID = params.get("RuleID")
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
        


class BotUserRule(AbstractModel):
    """Bot自定义规则

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名，只能以英文字符，数字，下划线组合，且不能以下划线开头。
        :type RuleName: str
        :param Action: 处置动作，取值有：
<li>drop：拦截；</li>
<li>monitor：观察；</li>
<li>trans：放行；</li>
<li>alg：JavaScript挑战；</li>
<li>captcha：托管挑战；</li>
<li>random：随机处置；</li>
<li>silence：静默；</li>
<li>shortdelay：短时响应；</li>
<li>longdelay：长时响应。</li>
        :type Action: str
        :param RuleStatus: 规则状态，取值有：
<li>on：生效；</li>
<li>off：不生效。</li>默认on生效。
        :type RuleStatus: str
        :param AclConditions: 规则详情。
        :type AclConditions: list of AclCondition
        :param RulePriority: 规则权重，取值范围0-100。
        :type RulePriority: int
        :param RuleID: 规则id。仅出参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param ExtendActions: 随机处置的处置方式及占比，非随机处置可不填暂不支持。
        :type ExtendActions: list of BotExtendAction
        :param FreqFields: 过滤词，取值有：
<li>sip：客户端ip。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreqFields: list of str
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FreqScope: 统计范围，字段为null时，代表source_to_eo。取值有：
<li>source_to_eo：（响应）源站到EdgeOne。</li>
<li>client_to_eo：（请求）客户端到EdgeOne；</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreqScope: list of str
        """
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.AclConditions = None
        self.RulePriority = None
        self.RuleID = None
        self.ExtendActions = None
        self.FreqFields = None
        self.UpdateTime = None
        self.FreqScope = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self.AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self.AclConditions.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.RuleID = params.get("RuleID")
        if params.get("ExtendActions") is not None:
            self.ExtendActions = []
            for item in params.get("ExtendActions"):
                obj = BotExtendAction()
                obj._deserialize(item)
                self.ExtendActions.append(obj)
        self.FreqFields = params.get("FreqFields")
        self.UpdateTime = params.get("UpdateTime")
        self.FreqScope = params.get("FreqScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CC(AbstractModel):
    """cc配置项。

    """

    def __init__(self):
        r"""
        :param Switch: Waf开关，取值为：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param PolicyId: 策略ID。
        :type PolicyId: int
        """
        self.Switch = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
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
        


class CacheConfig(AbstractModel):
    """缓存规则配置。

    """

    def __init__(self):
        r"""
        :param Cache: 缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220901.models.Cache`
        :param NoCache: 不缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCache: :class:`tencentcloud.teo.v20220901.models.NoCache`
        :param FollowOrigin: 遵循源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: :class:`tencentcloud.teo.v20220901.models.FollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = NoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = FollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """缓存键配置。

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
        :param QueryString: CacheKey 中包含请求参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.teo.v20220901.models.QueryString`
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
        


class CheckCertificateRequest(AbstractModel):
    """CheckCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Certificate: 证书内容。
        :type Certificate: str
        :param PrivateKey: 私钥内容。
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


class ClientIpCountry(AbstractModel):
    """回源时携带客户端IP所属地域信息，值的格式为ISO-3166-1两位字母代码。

    """

    def __init__(self):
        r"""
        :param Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param HeaderName: 存放客户端 IP 所属地域信息的请求头名称，当 Switch=on 时有效。
为空则使用默认值：EO-Client-IPCountry。
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
        


class ClientIpHeader(AbstractModel):
    """存储客户端请求IP的头部信息配置

    """

    def __init__(self):
        r"""
        :param Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param HeaderName: 回源时，存放客户端 IP 的请求头名称。
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
        


class ClientRule(AbstractModel):
    """客户端规则信息

    """

    def __init__(self):
        r"""
        :param ClientIp: 客户端ip。
        :type ClientIp: str
        :param RuleType: 规则类型。
        :type RuleType: str
        :param RuleId: 规则id。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param Description: 规则描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param IpStatus: 封禁状态，取值有：
<li>block ：封禁 ；</li>
<li>allow ：放行 。</li>
        :type IpStatus: str
        :param BlockTime: 封禁时间，采用unix秒级时间戳。
        :type BlockTime: int
        :param Id: 每条数据的唯一标识id。
        :type Id: str
        """
        self.ClientIp = None
        self.RuleType = None
        self.RuleId = None
        self.Description = None
        self.IpStatus = None
        self.BlockTime = None
        self.Id = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.RuleType = params.get("RuleType")
        self.RuleId = params.get("RuleId")
        self.Description = params.get("Description")
        self.IpStatus = params.get("IpStatus")
        self.BlockTime = params.get("BlockTime")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogTopicInfo(AbstractModel):
    """日志任务主题信息

    """

    def __init__(self):
        r"""
        :param TaskName: 任务名。
        :type TaskName: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param LogSetId: 日志集ID。
        :type LogSetId: str
        :param TopicId: 日志主题ID。
        :type TopicId: str
        :param EntityType: 任务类型。
        :type EntityType: str
        :param Period: 任务主题保存时间。
        :type Period: int
        :param Enabled: 任务主题是否开启。
        :type Enabled: bool
        :param Deleted: 任务主题是否异常。
        :type Deleted: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param Target: 推送目标地址,取值有：
<li>cls: 推送到cls；</li>
<li>custom_enpoint: 自定义推送地址。</li>
        :type Target: str
        :param LogSetRegion: 日志集所属地区。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetRegion: str
        :param ZoneId: 站点id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        :param LogSetType: 推送任务类型，取值有：
<li>cls：推送到cls；</li>
<li>custom_endpoint：推送到自定义接口。</li>
        :type LogSetType: str
        """
        self.TaskName = None
        self.ZoneName = None
        self.LogSetId = None
        self.TopicId = None
        self.EntityType = None
        self.Period = None
        self.Enabled = None
        self.Deleted = None
        self.CreateTime = None
        self.Target = None
        self.LogSetRegion = None
        self.ZoneId = None
        self.Area = None
        self.LogSetType = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.ZoneName = params.get("ZoneName")
        self.LogSetId = params.get("LogSetId")
        self.TopicId = params.get("TopicId")
        self.EntityType = params.get("EntityType")
        self.Period = params.get("Period")
        self.Enabled = params.get("Enabled")
        self.Deleted = params.get("Deleted")
        self.CreateTime = params.get("CreateTime")
        self.Target = params.get("Target")
        self.LogSetRegion = params.get("LogSetRegion")
        self.ZoneId = params.get("ZoneId")
        self.Area = params.get("Area")
        self.LogSetType = params.get("LogSetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeAction(AbstractModel):
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
        


class Compression(AbstractModel):
    """智能压缩配置。

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
        


class CreateAccelerationDomainRequest(AbstractModel):
    """CreateAccelerationDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param DomainName: 加速域名名称。
        :type DomainName: str
        :param OriginInfo: 源站信息。
        :type OriginInfo: :class:`tencentcloud.teo.v20220901.models.OriginInfo`
        """
        self.ZoneId = None
        self.DomainName = None
        self.OriginInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.DomainName = params.get("DomainName")
        if params.get("OriginInfo") is not None:
            self.OriginInfo = OriginInfo()
            self.OriginInfo._deserialize(params.get("OriginInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerationDomainResponse(AbstractModel):
    """CreateAccelerationDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAliasDomainRequest(AbstractModel):
    """CreateAliasDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param AliasName: 别称域名名称。
        :type AliasName: str
        :param TargetName: 目标域名名称。
        :type TargetName: str
        :param CertType: 证书配置，取值有：
<li> none：不配置；</li>
<li> hosting：SSL托管证书。</li>默认取值为 none。
        :type CertType: str
        :param CertId: 当 CertType 取值为 hosting 时需填入相应证书 ID。
        :type CertId: list of str
        """
        self.ZoneId = None
        self.AliasName = None
        self.TargetName = None
        self.CertType = None
        self.CertId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.AliasName = params.get("AliasName")
        self.TargetName = params.get("TargetName")
        self.CertType = params.get("CertType")
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasDomainResponse(AbstractModel):
    """CreateAliasDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param ProxyName: 当 ProxyType=hostname 时，表示域名或子域名；
当 ProxyType=instance 时，表示代理名称。
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
        :param ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>不填写使用默认值instance。
        :type ProxyType: str
        :param SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒。
不填写使用默认值600。
        :type SessionPersistTime: int
        :param Ipv6: Ipv6 访问配置。
不填写表示关闭 Ipv6 访问。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ApplicationProxyRules: 规则详细信息。
不填写则不创建规则。
        :type ApplicationProxyRules: list of ApplicationProxyRule
        :param AccelerateMainland: 中国大陆加速优化配置。不填写表示关闭中国大陆加速优化。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self.ZoneId = None
        self.ProxyName = None
        self.PlatType = None
        self.SecurityType = None
        self.AccelerateType = None
        self.ProxyType = None
        self.SessionPersistTime = None
        self.Ipv6 = None
        self.ApplicationProxyRules = None
        self.AccelerateMainland = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyName = params.get("ProxyName")
        self.PlatType = params.get("PlatType")
        self.SecurityType = params.get("SecurityType")
        self.AccelerateType = params.get("AccelerateType")
        self.ProxyType = params.get("ProxyType")
        self.SessionPersistTime = params.get("SessionPersistTime")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ApplicationProxyRules") is not None:
            self.ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self.ApplicationProxyRules.append(obj)
        if params.get("AccelerateMainland") is not None:
            self.AccelerateMainland = AccelerateMainland()
            self.AccelerateMainland._deserialize(params.get("AccelerateMainland"))
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param Proto: 协议，取值有：
<li>TCP：TCP协议；</li>
<li>UDP：UDP协议。</li>
        :type Proto: str
        :param Port: 端口，支持格式：
<li>80：80端口；</li>
<li>81-90：81至90端口。</li>
        :type Port: list of str
        :param OriginType: 源站类型，取值有：
<li>custom：手动添加；</li>
<li>origins：源站组。</li>
        :type OriginType: str
        :param OriginValue: 源站信息：
<li>当 OriginType 为 custom 时，表示一个或多个源站，如`["8.8.8.8","9.9.9.9"]` 或 `OriginValue=["test.com"]`；</li>
<li>当 OriginType 为 origins 时，要求有且仅有一个元素，表示源站组ID，如`["origin-537f5b41-162a-11ed-abaa-525400c5da15"]`。</li>
        :type OriginValue: list of str
        :param ForwardClientIp: 传递客户端IP，取值有：
<li>TOA：TOA（仅Proto=TCP时可选）；</li>
<li>PPV1：Proxy Protocol传递，协议版本V1（仅Proto=TCP时可选）；</li>
<li>PPV2：Proxy Protocol传递，协议版本V2；</li>
<li>OFF：不传递。</li>默认值：OFF。
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持，取值有：
<li>true：开启；</li>
<li>false：关闭。</li>默认值：false。
        :type SessionPersist: bool
        :param OriginPort: 源站端口，支持格式：
<li>单端口：80；</li>
<li>端口段：81-90，81至90端口。</li>
        :type OriginPort: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.Proto = None
        self.Port = None
        self.OriginType = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.OriginPort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.OriginType = params.get("OriginType")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.OriginPort = params.get("OriginPort")
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


class CreateCredentialRequest(AbstractModel):
    """CreateCredential请求参数结构体

    """


class CreateCredentialResponse(AbstractModel):
    """CreateCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOriginGroupRequest(AbstractModel):
    """CreateOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param OriginType: 源站类型，取值有：
<li>self：自有源站；</li>
<li>third_party：第三方源站；</li>
<li>cos：腾讯云COS源站。</li>
        :type OriginType: str
        :param OriginGroupName: 源站组名称。
        :type OriginGroupName: str
        :param ConfigurationType: 源站配置类型，当OriginType=self时，取值有：
<li>area：按区域配置；</li>
<li>weight： 按权重配置；</li>
<li>proto： 按HTTP协议配置。</li>当OriginType=third_party/cos时放空。
        :type ConfigurationType: str
        :param OriginRecords: 源站记录信息。
        :type OriginRecords: list of OriginRecord
        :param HostHeader: 回源Host，仅当OriginType=self时可以设置。
        :type HostHeader: str
        """
        self.ZoneId = None
        self.OriginType = None
        self.OriginGroupName = None
        self.ConfigurationType = None
        self.OriginRecords = None
        self.HostHeader = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OriginType = params.get("OriginType")
        self.OriginGroupName = params.get("OriginGroupName")
        self.ConfigurationType = params.get("ConfigurationType")
        if params.get("OriginRecords") is not None:
            self.OriginRecords = []
            for item in params.get("OriginRecords"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.OriginRecords.append(obj)
        self.HostHeader = params.get("HostHeader")
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
        :param OriginGroupId: 源站组ID。
        :type OriginGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginGroupId = params.get("OriginGroupId")
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
<li> sta_global ：全球内容分发网络（包括中国大陆）标准版套餐； </li>
<li> sta_global_with_bot ：全球内容分发网络（包括中国大陆）标准版套餐附带bot管理；</li>
<li> ent: 全球内容分发网络（不包括中国大陆）企业版套餐； </li>
<li> ent_with_bot: 全球内容分发网络（不包括中国大陆）企业版套餐附带bot管理；</li>
<li> ent_cm: 中国大陆内容分发网络企业版套餐； </li>
<li> ent_cm_with_bot: 中国大陆内容分发网络企业版套餐附带bot管理。</li>
<li> ent_global ：全球内容分发网络（包括中国大陆）企业版套餐； </li>
<li> ent_global_with_bot ：全球内容分发网络（包括中国大陆）企业版套餐附带bot管理。</li>当前账户可购买套餐类型请以<a href="https://cloud.tencent.com/document/product/1552/80606">DescribeAvailablePlans</a>返回为准。
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
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Targets: 要预热的资源列表，每个元素格式类似如下:
http://www.example.com/example.txt。
        :type Targets: list of str
        :param EncodeUrl: 是否对url进行encode，若内容含有非 ASCII 字符集的字符，请开启此开关进行编码转换（编码规则遵循 RFC3986）。
        :type EncodeUrl: bool
        :param Headers: 附带的http头部信息。
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
        :param JobId: 任务 ID。
        :type JobId: str
        :param FailedList: 失败的任务列表。
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param Type: 清除缓存类型，取值有：
<li>purge_url：URL；</li>
<li>purge_prefix：前缀；</li>
<li>purge_host：Hostname；</li>
<li>purge_all：全部缓存；</li>
<li>purge_cache_tag：cache-tag刷新。</li>
        :type Type: str
        :param Targets: 要清除缓存的资源列表，每个元素格式依据Type而定：
1) Type = purge_host 时：
形如：www.example.com 或 foo.bar.example.com。
2) Type = purge_prefix 时：
形如：http://www.example.com/example。
3) Type = purge_url 时：
形如：https://www.example.com/example.jpg。
4）Type = purge_all 时：
Targets可为空，不需要填写。
5）Type = purge_cache_tag 时：
形如：tag1。
        :type Targets: list of str
        :param EncodeUrl: 若有编码转换，仅清除编码转换后匹配的资源。
若内容含有非 ASCII 字符集的字符，请开启此开关进行编码转换（编码规则遵循 RFC3986）。
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
        :param JobId: 任务ID。
        :type JobId: str
        :param FailedList: 失败的任务列表及原因。
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


class CreateReplayTaskRequest(AbstractModel):
    """CreateReplayTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 重放任务的 ID 列表。
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReplayTaskResponse(AbstractModel):
    """CreateReplayTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param JobId: 此次任务ID。
        :type JobId: str
        :param FailedList: 失败的任务列表及原因。
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
        :type Rules: list of Rule
        :param Tags: 规则标签。
        :type Tags: list of str
        """
        self.ZoneId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None
        self.Tags = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Tags = params.get("Tags")
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


class CreateSecurityIPGroupRequest(AbstractModel):
    """CreateSecurityIPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 Id。
        :type ZoneId: str
        :param IPGroup: IP 组信息。
        :type IPGroup: :class:`tencentcloud.teo.v20220901.models.IPGroup`
        """
        self.ZoneId = None
        self.IPGroup = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("IPGroup") is not None:
            self.IPGroup = IPGroup()
            self.IPGroup._deserialize(params.get("IPGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityIPGroupResponse(AbstractModel):
    """CreateSecurityIPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: IP 组 Id。
        :type GroupId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateSpeedTestingRequest(AbstractModel):
    """CreateSpeedTesting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Host: 拨测子域名。
        :type Host: str
        """
        self.ZoneId = None
        self.Host = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSpeedTestingResponse(AbstractModel):
    """CreateSpeedTesting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param Type: 接入方式，取值有：
<li> full：NS接入；</li>
<li> partial：CNAME接入，请先调用认证站点API（IdentifyZone）进行站点归属权校验，校验通过后继续调用本接口创建站点。</li>不填写使用默认值full。
        :type Type: str
        :param JumpStart: 是否跳过站点现有的DNS记录扫描。默认值：false。
        :type JumpStart: bool
        :param Tags: 资源标签。
        :type Tags: list of Tag
        :param AllowDuplicates: 是否允许重复接入。
<li> true：允许重复接入；</li>
<li> false：不允许重复接入。</li>不填写使用默认值false。
        :type AllowDuplicates: bool
        :param AliasZoneName: 站点别名。数字、英文、-和_组合，限制20个字符。
        :type AliasZoneName: str
        """
        self.ZoneName = None
        self.Type = None
        self.JumpStart = None
        self.Tags = None
        self.AllowDuplicates = None
        self.AliasZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Type = params.get("Type")
        self.JumpStart = params.get("JumpStart")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AllowDuplicates = params.get("AllowDuplicates")
        self.AliasZoneName = params.get("AliasZoneName")
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


class DDoS(AbstractModel):
    """DDoS配置

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
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
        


class DDoSAttackEvent(AbstractModel):
    """DDoS攻击事件对象

    """

    def __init__(self):
        r"""
        :param EventId: 事件ID。
        :type EventId: str
        :param AttackType: 攻击类型(对应交互事件名称)。
        :type AttackType: str
        :param AttackStatus: 攻击状态。
        :type AttackStatus: int
        :param AttackMaxBandWidth: 攻击最大带宽。
        :type AttackMaxBandWidth: int
        :param AttackPacketMaxRate: 攻击包速率峰值。
        :type AttackPacketMaxRate: int
        :param AttackStartTime: 攻击开始时间，单位为s。
        :type AttackStartTime: int
        :param AttackEndTime: 攻击结束时间，单位为s。
        :type AttackEndTime: int
        :param PolicyId: DDoS策略组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param ZoneId: 站点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param Area: 攻击事件所属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param DDoSBlockData: 封禁解封信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DDoSBlockData: list of DDoSBlockData
        """
        self.EventId = None
        self.AttackType = None
        self.AttackStatus = None
        self.AttackMaxBandWidth = None
        self.AttackPacketMaxRate = None
        self.AttackStartTime = None
        self.AttackEndTime = None
        self.PolicyId = None
        self.ZoneId = None
        self.Area = None
        self.DDoSBlockData = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AttackType = params.get("AttackType")
        self.AttackStatus = params.get("AttackStatus")
        self.AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self.AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self.AttackStartTime = params.get("AttackStartTime")
        self.AttackEndTime = params.get("AttackEndTime")
        self.PolicyId = params.get("PolicyId")
        self.ZoneId = params.get("ZoneId")
        self.Area = params.get("Area")
        if params.get("DDoSBlockData") is not None:
            self.DDoSBlockData = []
            for item in params.get("DDoSBlockData"):
                obj = DDoSBlockData()
                obj._deserialize(item)
                self.DDoSBlockData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSBlockData(AbstractModel):
    """DDoS封禁解封信息

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间，采用unix时间戳。
        :type StartTime: int
        :param EndTime: 结束时间，采用unix时间戳, 为0表示还处于封禁中。
        :type EndTime: int
        :param BlockArea: 封禁受影响区域。
        :type BlockArea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.BlockArea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.BlockArea = params.get("BlockArea")
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
        :param EffectiveTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectiveTime: str
        :param CommonName: 证书公用名。
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        :param SubjectAltName: 证书SAN域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param Status: 部署状态，取值有：
<li>processing: 部署中；</li>
<li>deployed: 已部署；</li>
<li>failed: 部署失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Message: Status为失败时,此字段返回失败原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param SignAlgo: 证书算法。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignAlgo: str
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
        self.SignAlgo = None


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
        self.SignAlgo = params.get("SignAlgo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerationDomainsRequest(AbstractModel):
    """DeleteAccelerationDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param DomainNames: 需要删除的加速域名ID列表。
        :type DomainNames: list of str
        :param Force: 是否强制删除。当域名存在关联资源（如马甲域名、流量调度功能）时，是否强制删除该域名，取值有：
<li> true：删除该域名及所有关联资源；</li>
<li> false：当该加速域名存在关联资源时，不允许删除。</li>不填写，默认值为：false。
        :type Force: bool
        """
        self.ZoneId = None
        self.DomainNames = None
        self.Force = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.DomainNames = params.get("DomainNames")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerationDomainsResponse(AbstractModel):
    """DeleteAccelerationDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAliasDomainRequest(AbstractModel):
    """DeleteAliasDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param AliasNames: 待删除别称域名名称。如果为空，则不执行删除操作。
        :type AliasNames: list of str
        """
        self.ZoneId = None
        self.AliasNames = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasDomainResponse(AbstractModel):
    """DeleteAliasDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 代理ID。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param RuleId: 规则ID。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOriginGroupRequest(AbstractModel):
    """DeleteOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param OriginGroupId: 源站组ID。
        :type OriginGroupId: str
        """
        self.ZoneId = None
        self.OriginGroupId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OriginGroupId = params.get("OriginGroupId")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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


class DeleteSecurityIPGroupRequest(AbstractModel):
    """DeleteSecurityIPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 Id。
        :type ZoneId: str
        :param GroupId: IP 组 Id。
        :type GroupId: int
        """
        self.ZoneId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityIPGroupResponse(AbstractModel):
    """DeleteSecurityIPGroup返回参数结构体

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
        :param ZoneId: 站点 ID。
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
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccelerationDomainsRequest(AbstractModel):
    """DescribeAccelerationDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>domain-name<br>   按照【<strong>加速域名名称</strong>】进行过滤。<br>   类型：String<br>   必选：否
<li>origin-type<br>   按照【<strong>源站类型</strong>】进行过滤。<br>   类型：String<br>   必选：否
<li>origin<br>   按照【<strong>主源站地址</strong>】进行过滤。<br>   类型：String<br>   必选：否
<li>backup-origin<br>   按照【<strong>备用源站地址</strong>】进行过滤。<br>   类型：String<br>   必选：否
<li>domain-cname<br>   按照【<strong>加速CNAME名</strong>】进行过滤。<br>   类型：String<br>   必选：否
<li>share-cname<br>   按照【<strong>共享CNAME名</strong>】进行过滤。<br>   类型：String<br>   必选：否
        :type Filters: list of AdvancedFilter
        :param Direction: 列表排序方式，取值有：
<li>asc：升序排列；</li>
<li>desc：降序排列。</li>默认值为asc。
        :type Direction: str
        :param Match: 匹配方式，取值有：
<li>all：返回匹配所有查询条件的加速域名；</li>
<li>any：返回匹配任意一个查询条件的加速域名。</li>默认值为all。
        :type Match: str
        :param Limit: 分页查询限制数目，默认值：20，上限：200。
        :type Limit: int
        :param Offset: 分页查询偏移量，默认为 0。
        :type Offset: int
        :param Order: 排序依据，取值有：
<li>created_on：加速域名创建时间；</li>
<li>domain-name：加速域名名称；</li>
</li>默认根据domain-name属性排序。
        :type Order: str
        """
        self.ZoneId = None
        self.Filters = None
        self.Direction = None
        self.Match = None
        self.Limit = None
        self.Offset = None
        self.Order = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Direction = params.get("Direction")
        self.Match = params.get("Match")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccelerationDomainsResponse(AbstractModel):
    """DescribeAccelerationDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 加速域名总数。
        :type TotalCount: int
        :param AccelerationDomains: 加速域名列表。
        :type AccelerationDomains: list of AccelerationDomain
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccelerationDomains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccelerationDomains") is not None:
            self.AccelerationDomains = []
            for item in params.get("AccelerationDomains"):
                obj = AccelerationDomain()
                obj._deserialize(item)
                self.AccelerationDomains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddableEntityListRequest(AbstractModel):
    """DescribeAddableEntityList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param EntityType: 推送数据类型，取值有:
<li>domain：七层加速日志；</li>
<li>application：四层加速日志；</li>
<li>web-rateLiming：速率限制日志；</li>
<li>web-attack：web攻击防护日志；</li>
<li>web-rule：自定义规则日志；</li>
<li>web-bot：Bot管理日志。</li>
        :type EntityType: str
        :param Area: 服务区域，取值有：
<li>mainland：中国大陆境内；</li>
<li>overseas：全球（不含中国大陆）。</li>若为国内站账号，则默认取值为mainland；若为国际站账号，则默认取值为overseas。
        :type Area: str
        """
        self.ZoneId = None
        self.EntityType = None
        self.Area = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.EntityType = params.get("EntityType")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddableEntityListResponse(AbstractModel):
    """DescribeAddableEntityList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param EntityList: 可添加的实体列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EntityList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EntityList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.EntityList = params.get("EntityList")
        self.RequestId = params.get("RequestId")


class DescribeAliasDomainsRequest(AbstractModel):
    """DescribeAliasDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>target-name<br>   按照【<strong>目标域名名称</strong>】进行过滤。<br>   类型：String<br>   必选：否</li><li>alias-name<br>   按照【<strong>别称域名名称</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>模糊查询时仅支持过滤字段名为alias-name。
        :type Filters: list of AdvancedFilter
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAliasDomainsResponse(AbstractModel):
    """DescribeAliasDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的别称域名个数。
        :type TotalCount: int
        :param AliasDomains: 别称域名详细信息列表。
        :type AliasDomains: list of AliasDomain
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AliasDomains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AliasDomains") is not None:
            self.AliasDomains = []
            for item in params.get("AliasDomains"):
                obj = AliasDomain()
                obj._deserialize(item)
                self.AliasDomains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeApplicationProxiesRequest(AbstractModel):
    """DescribeApplicationProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页查询偏移量。默认为0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：<li>proxy-id<br>   按照【<strong>代理ID</strong>】进行过滤。代理ID形如：proxy-ev2sawbwfd。<br>   类型：String<br>   必选：否</li><li>zone-id<br>   按照【<strong>站点ID</strong>】进行过滤。站点ID形如：zone-vawer2vadg。<br>   类型：String<br>   必选：否</li>
        :type Filters: list of Filter
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
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxiesResponse(AbstractModel):
    """DescribeApplicationProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationProxies: 应用代理列表。
        :type ApplicationProxies: list of ApplicationProxy
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationProxies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ApplicationProxies") is not None:
            self.ApplicationProxies = []
            for item in params.get("ApplicationProxies"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self.ApplicationProxies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAvailablePlansRequest(AbstractModel):
    """DescribeAvailablePlans请求参数结构体

    """


class DescribeAvailablePlansResponse(AbstractModel):
    """DescribeAvailablePlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param PlanInfo: 当前账户可购买套餐类型及相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanInfo: list of PlanInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlanInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlanInfo") is not None:
            self.PlanInfo = []
            for item in params.get("PlanInfo"):
                obj = PlanInfo()
                obj._deserialize(item)
                self.PlanInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClientRuleListRequest(AbstractModel):
    """DescribeClientRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 查询的站点ID.
        :type ZoneId: str
        :param Domain: 查询的子域名。
        :type Domain: str
        :param RuleType: 规则类型，取值有：
<li>acl：自定义规则；</li>
<li>rate：限速规则。</li>不填表示查询所有规则。
        :type RuleType: str
        :param RuleId: 规则ID。
        :type RuleId: int
        :param SourceClientIp: 客户端IP。
        :type SourceClientIp: str
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.ZoneId = None
        self.Domain = None
        self.RuleType = None
        self.RuleId = None
        self.SourceClientIp = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Domain = params.get("Domain")
        self.RuleType = params.get("RuleType")
        self.RuleId = params.get("RuleId")
        self.SourceClientIp = params.get("SourceClientIp")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientRuleListResponse(AbstractModel):
    """DescribeClientRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 封禁客户端数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ClientRule
        :param TotalCount: 查询结果的总条数。
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
                obj = ClientRule()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeContentQuotaRequest(AbstractModel):
    """DescribeContentQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
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
        


class DescribeContentQuotaResponse(AbstractModel):
    """DescribeContentQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param PurgeQuota: 刷新相关配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type PurgeQuota: list of Quota
        :param PrefetchQuota: 预热相关配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrefetchQuota: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PurgeQuota = None
        self.PrefetchQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurgeQuota") is not None:
            self.PurgeQuota = []
            for item in params.get("PurgeQuota"):
                obj = Quota()
                obj._deserialize(item)
                self.PurgeQuota.append(obj)
        if params.get("PrefetchQuota") is not None:
            self.PrefetchQuota = []
            for item in params.get("PrefetchQuota"):
                obj = Quota()
                obj._deserialize(item)
                self.PrefetchQuota.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackDataRequest(AbstractModel):
    """DescribeDDoSAttackData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 统计指标列表，取值有：
<li>ddos_attackMaxBandwidth：攻击带宽峰值；</li>
<li>ddos_attackMaxPackageRate：攻击包速率峰值 ；</li>
<li>ddos_attackBandwidth：攻击带宽曲线；</li>
<li>ddos_attackPackageRate：攻击包速率曲线。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param PolicyIds: DDoS策略组ID列表，不填默认选择全部策略ID。
        :type PolicyIds: list of int
        :param Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间与结束时间的间隔自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackDataResponse(AbstractModel):
    """DescribeDDoSAttackData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: DDoS攻击数据内容列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
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
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackEventRequest(AbstractModel):
    """DescribeDDoSAttackEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param PolicyIds: ddos策略组集合，不填默认选择全部策略。
        :type PolicyIds: list of int
        :param ZoneIds: 站点集合，此参数必填，不填默认查询为空。
        :type ZoneIds: list of str
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param ShowDetail: 是否展示详细信息。
        :type ShowDetail: bool
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据；</li>不填默认取值为global。
        :type Area: str
        :param OrderBy: 排序字段，取值有：
<li>MaxBandWidth：带宽峰值；</li>
<li>AttackStartTime：攻击开始时间。</li>不填默认值为：AttackStartTime。
        :type OrderBy: str
        :param OrderType: 排序方式，取值有：
<li>asc：升序方式；</li>
<li>desc：降序方式。</li>不填默认值为：desc。
        :type OrderType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PolicyIds = None
        self.ZoneIds = None
        self.Limit = None
        self.Offset = None
        self.ShowDetail = None
        self.Area = None
        self.OrderBy = None
        self.OrderType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PolicyIds = params.get("PolicyIds")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ShowDetail = params.get("ShowDetail")
        self.Area = params.get("Area")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackEventResponse(AbstractModel):
    """DescribeDDoSAttackEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDOS攻击事件数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DDoSAttackEvent
        :param TotalCount: 查询结果的总条数。
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
                obj = DDoSAttackEvent()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackTopDataRequest(AbstractModel):
    """DescribeDDoSAttackTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricName: 查询的统计指标，取值有：
<li>ddos_attackFlux_protocol：按各协议的攻击流量排行；</li>
<li>ddos_attackPackageNum_protocol：按各协议的攻击包量排行；</li>
<li>ddos_attackNum_attackType：按各攻击类型的攻击数量排行；</li>
<li>ddos_attackNum_sregion：按攻击源地区的攻击数量排行；</li>
<li>ddos_attackFlux_sip：按攻击源IP的攻击数量排行；</li>
<li>ddos_attackFlux_sregion：按攻击源地区的攻击数量排行。</li>
        :type MetricName: str
        :param ZoneIds: 站点ID集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param PolicyIds: DDoS策略组ID集合，不填默认选择全部策略ID。
        :type PolicyIds: list of int
        :param AttackType: 攻击类型，取值有：
<li>flood：洪泛攻击；</li>
<li>icmpFlood：icmp洪泛攻击；</li>
<li>all：所有的攻击类型。</li>不填默认为all，表示查询全部攻击类型。
        :type AttackType: str
        :param ProtocolType: 协议类型，取值有：
<li>tcp：tcp协议；</li>
<li>udp：udp协议；</li>
<li>all：所有的协议类型。</li>不填默认为all，表示查询所有协议。
        :type ProtocolType: str
        :param Port: 端口号。
        :type Port: int
        :param Limit: 查询前多少个数据，不填默认默认为10， 表示查询前top 10的数据。
        :type Limit: int
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.PolicyIds = None
        self.AttackType = None
        self.ProtocolType = None
        self.Port = None
        self.Limit = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.PolicyIds = params.get("PolicyIds")
        self.AttackType = params.get("AttackType")
        self.ProtocolType = params.get("ProtocolType")
        self.Port = params.get("Port")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackTopDataResponse(AbstractModel):
    """DescribeDDoSAttackTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: DDoS攻击Top数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopEntry
        :param TotalCount: 查询结果的总条数。
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
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件，Filters.Values的上限为5。详细的过滤条件如下：
<li>zone-id<br>   按照【<strong>站点ID</strong>】进行过滤。站点ID形如：zone-xxx。<br>   类型：String<br>   必选：是 </li>
        :type Filters: list of Filter
        :param Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：20，最大值：100。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        :param TotalCount: 证书总数。
        :type TotalCount: int
        :param DefaultServerCertInfo: 默认证书列表。
        :type DefaultServerCertInfo: list of DefaultServerCertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DefaultServerCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DefaultServerCertInfo") is not None:
            self.DefaultServerCertInfo = []
            for item in params.get("DefaultServerCertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self.DefaultServerCertInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDnsDataRequest(AbstractModel):
    """DescribeDnsData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>zone<br>   按照【<strong>站点名称</strong>】进行过滤。站点名称形如：tencent.com<br>   类型：String<br>   必选：否，仅支持填写一个站点
<li>host<br>   按照【<strong>域名</strong>】进行过滤。域名形如：test.tencent.com<br>   类型：String<br>   必选：否，仅支持填写一个域名
<li>type<br>   按照【<strong>DNS解析类型</strong>】进行过滤<br>   类型：String<br>   必选：否<br>   可选项：<br>   A：A记录<br>   AAAA：AAAA记录<br>   CNAME：CNAME记录<br>   MX：MX记录<br>   TXT：TXT记录<br>   NS：NS记录<br>   SRV：SRV记录<br>   CAA：CAA记录
<li>code<br>   按照【<strong>DNS解析状态码</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   NoError：成功<br>   NXDomain：请求域不存在<br>   NotImp：不支持的请求类型<br>   Refused：域名服务器因为策略的原因拒绝执行请求
<li>area<br>   按照【<strong>DNS解析地域</strong>】进行过滤。<br>   类型：String<br>   必选：否。<br>   可选项：<br>   亚洲：Asia<br>   欧洲：Europe<br>   非洲：Africa<br>   大洋洲：Oceania<br>   美洲：Americas
        :type Filters: list of Filter
        :param Interval: 时间粒度，取值有：
<li>min：1分钟粒度；</li>
<li>5min：5分钟粒度；</li>
<li>hour：1小时粒度；</li>
<li>day：天粒度。</li>不填写，默认值为：min。
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
                obj = Filter()
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
        :param Data: 统计数据。
        :type Data: list of DnsData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DnsData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param Offset: 分页查询偏移量。默认值： 0，最小值：0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值： 100，最大值：1000。
        :type Limit: int
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>host<br>   按照【<strong>域名</strong>】进行过滤。<br>   类型：string<br>   必选：否</li>
        :type Filters: list of Filter
        """
        self.ZoneId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param DetailHosts: 域名列表。
        :type DetailHosts: list of DetailHost
        :param TotalNumber: 域名数量。
        :type TotalNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetailHosts = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailHosts") is not None:
            self.DetailHosts = []
            for item in params.get("DetailHosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self.DetailHosts.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIdentificationsRequest(AbstractModel):
    """DescribeIdentifications请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>zone-name<br>   按照【<strong>站点名称</strong>】进行过滤。<br>   类型：String<br>   必选：是</li>
        :type Filters: list of Filter
        :param Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationsResponse(AbstractModel):
    """DescribeIdentifications返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的站点个数。
        :type TotalCount: int
        :param Identifications: 站点验证信息列表。
        :type Identifications: list of Identification
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Identifications = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Identifications") is not None:
            self.Identifications = []
            for item in params.get("Identifications"):
                obj = Identification()
                obj._deserialize(item)
                self.Identifications.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogSetsRequest(AbstractModel):
    """DescribeLogSets请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogSetRegion: 日志集所属的地域。
        :type LogSetRegion: str
        :param LogSetId: 日志集ID。
        :type LogSetId: str
        :param LogSetName: 日志集名称。
        :type LogSetName: str
        """
        self.LogSetRegion = None
        self.LogSetId = None
        self.LogSetName = None


    def _deserialize(self, params):
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetId = params.get("LogSetId")
        self.LogSetName = params.get("LogSetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogSetsResponse(AbstractModel):
    """DescribeLogSets返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogSetList: 日志集列表数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetList: list of LogSetInfo
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogSetList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogSetList") is not None:
            self.LogSetList = []
            for item in params.get("LogSetList"):
                obj = LogSetInfo()
                obj._deserialize(item)
                self.LogSetList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLogTopicTasksRequest(AbstractModel):
    """DescribeLogTopicTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        """
        self.ZoneId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogTopicTasksResponse(AbstractModel):
    """DescribeLogTopicTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopicList: 推送任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicList: list of ClsLogTopicInfo
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ClsLogTopicInfo()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeOriginGroupRequest(AbstractModel):
    """DescribeOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页查询偏移量，默认为0。
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为10，取值：1-1000。
        :type Limit: int
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>zone-id<br>   按照【<strong>站点ID</strong>】进行过滤。站点ID形如：zone-20hzkd4rdmy0<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>origin-group-id<br>   按照【<strong>源站组ID</strong>】进行过滤。源站组ID形如：origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>origin-group-name<br>   按照【<strong>源站组名称</strong>】进行过滤<br>   类型：String<br>   必选：否<br>   模糊查询：支持。使用模糊查询时，仅支持填写一个源站组名称</li>
        :type Filters: list of AdvancedFilter
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
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param OriginGroups: 源站组信息。
        :type OriginGroups: list of OriginGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OriginGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OriginGroups") is not None:
            self.OriginGroups = []
            for item in params.get("OriginGroups"):
                obj = OriginGroup()
                obj._deserialize(item)
                self.OriginGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOriginProtectionRequest(AbstractModel):
    """DescribeOriginProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneIds: 查询的站点集合，不填默认查询所有站点。
        :type ZoneIds: list of str
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>need-update<br>   按照【<strong>站点是否需要更新源站防护IP白名单</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   true：需要更新<br>   false：无需更新<br></li>
<li>plan-support<br>   按照【<strong>站点套餐是否支持源站防护</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   true：支持<br>   false：不支持<br></li>
        :type Filters: list of Filter
        :param Offset: 分页查询偏移量，默认为0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        """
        self.ZoneIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginProtectionResponse(AbstractModel):
    """DescribeOriginProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param OriginProtectionInfo: 源站防护信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginProtectionInfo: list of OriginProtectionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginProtectionInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OriginProtectionInfo") is not None:
            self.OriginProtectionInfo = []
            for item in params.get("OriginProtectionInfo"):
                obj = OriginProtectionInfo()
                obj._deserialize(item)
                self.OriginProtectionInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 查询的指标，取值有：
<li>l7Flow_outFlux: Edegone响应流量；</li>
<li>l7Flow_inFlux: Edgeone请求流量；</li>
<li>l7Flow_outBandwidth: Edegone响应带宽；</li>
<li>l7Flow_inBandwidth: Edegone请求带宽；</li>
<li>l7Flow_hit_outFlux: 缓存命中流量；</li>
<li>l7Flow_request: 访问请求数；</li>
<li>l7Flow_flux: 访问请求上行+下行流量；</li>
<li>l7Flow_bandwidth：访问请求上行+下行带宽。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合。
若不填写，默认选择全部站点，且最多只能查询近30天的数据；若填写，则可查询站点绑定套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>。
        :type ZoneIds: list of str
        :param Domains: 查询的域名集合，不填默认查询所有子域名。
        :type Domains: list of str
        :param Protocol: 查询的协议类型，取值有：
<li>http: http协议；</li>
<li>https: https协议；</li>
<li>http2: http2协议；</li>
<li>all:  所有协议。</li>不填默认为all，此参数暂未生效。
        :type Protocol: str
        :param Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param Filters: 过滤条件，详细的过滤条件Key值如下：
<li>socket<br>   按照【<strong>HTTP协议类型</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP：HTTP 协议；<br>   HTTPS：HTTPS协议；<br>   QUIC：QUIC协议。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。</li>
        :type Filters: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.Protocol = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Protocol = params.get("Protocol")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: 七层监控类时序流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
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
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询起始时间。
        :type StartTime: str
        :param EndTime: 查询结束时间。
        :type EndTime: str
        :param Offset: 分页查询偏移量，默认为 0。
        :type Offset: int
        :param Limit: 分页查询限制数目，默认值：20，上限：1000。
        :type Limit: int
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>zone-id<br>   按照【<strong>站点 ID</strong>】进行过滤。zone-id形如：zone-1379afjk91u32h，暂不支持多值。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>job-id<br>   按照【<strong>任务ID</strong>】进行过滤。job-id形如：1379afjk91u32h，暂不支持多值。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>target<br>   按照【<strong>目标资源信息</strong>】进行过滤。target形如：http://www.qq.com/1.txt，暂不支持多值。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>domains<br>   按照【<strong>域名</strong>】进行过滤。domains形如：www.qq.com。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>statuses<br>   按照【<strong>任务状态</strong>】进行过滤。<br>   必选：否<br>   模糊查询：不支持。<br>   可选项：<br>   processing：处理中<br>   success：成功<br>   failed：失败<br>   timeout：超时</li>
        :type Filters: list of AdvancedFilter
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        :param TotalCount: 该查询条件总共条目数。
        :type TotalCount: int
        :param Tasks: 任务结果列表。
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
        :param ZoneId: 字段已废弃，请使用Filters中的zone-id。
        :type ZoneId: str
        :param StartTime: 查询起始时间。
        :type StartTime: str
        :param EndTime: 查询结束时间。
        :type EndTime: str
        :param Offset: 分页查询偏移量，默认为0。
        :type Offset: int
        :param Limit: 分页查限制数目，默认值：20，最大值：1000。
        :type Limit: int
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：<li>zone-id<br>   按照【<strong>站点 ID</strong>】进行过滤。zone-id形如：zone-xxx，暂不支持多值<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>job-id<br>   按照【<strong>任务ID</strong>】进行过滤。job-id形如：1379afjk91u32h，暂不支持多值。<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>target<br>   按照【<strong>目标资源信息</strong>】进行过滤，target形如：http://www.qq.com/1.txt或者tag1，暂不支持多值<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>domains<br>   按照【<strong>域名</strong>】进行过滤，domains形如：www.qq.com<br>   类型：String<br>   必选：否<br>   模糊查询：不支持。</li><li>statuses<br>   按照【<strong>任务状态</strong>】进行过滤<br>   必选：否<br>   模糊查询：不支持。<br>   可选项：<br>   processing：处理中<br>   success：成功<br>   failed：失败<br>   timeout：超时</li><li>type<br>   按照【<strong>清除缓存类型</strong>】进行过滤，暂不支持多值。<br>   类型：String<br>   必选：否<br>   模糊查询：不支持<br>   可选项：<br>   purge_url：URL<br>   purge_prefix：前缀<br>   purge_all：全部缓存内容<br>   purge_host：Hostname<br>   purge_cache_tag：CacheTag</li>
        :type Filters: list of AdvancedFilter
        """
        self.ZoneId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        :param TotalCount: 该查询条件总共条目数。
        :type TotalCount: int
        :param Tasks: 任务结果列表。
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
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>rule-id<br>   按照【<strong>规则ID</strong>】进行过滤。<br>   类型：string<br>   必选：否</li>
        :type Filters: list of Filter
        """
        self.ZoneId = None
        self.Filters = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
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
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param RuleItems: 规则列表，按规则执行顺序从先往后排序。
        :type RuleItems: list of RuleItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneId = None
        self.RuleItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("RuleItems") is not None:
            self.RuleItems = []
            for item in params.get("RuleItems"):
                obj = RuleItem()
                obj._deserialize(item)
                self.RuleItems.append(obj)
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


class DescribeSingleL7AnalysisDataRequest(AbstractModel):
    """DescribeSingleL7AnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 查询的指标，取值有:
<li> l7Flow_singleIpRequest：独立IP请求数。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合。
若不填写，默认选择全部站点，且最多只能查询近30天的数据；
若填写，则可查询站点绑定套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>。
        :type ZoneIds: list of str
        :param Filters: 过滤条件，详细的过滤条件Key值如下：
<li>country<br>   按照【<strong>国家/地区</strong>】进行过滤，国家/地区遵循<a href="https://zh.wikipedia.org/wiki/ISO_3166-1">ISO 3166</a>规范。</li>
<li>domain<br>   按照【<strong>子域名</strong>】进行过滤，子域名形如： test.example.com。</li>
<li>protocol<br>   按照【<strong>HTTP协议版本</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP/1.0：HTTP 1.0；<br>   HTTP/1.1：HTTP 1.1；<br>   HTTP/2.0：HTTP 2.0；<br>   HTTP/3.0：HTTP 3.0；<br>   WebSocket：WebSocket。</li>
<li>socket<br>   按照【<strong>HTTP协议类型</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP：HTTP 协议；<br>   HTTPS：HTTPS协议；<br>   QUIC：QUIC协议。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。</li>
        :type Filters: list of QueryCondition
        :param Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天;。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSingleL7AnalysisDataResponse(AbstractModel):
    """DescribeSingleL7AnalysisData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: 单值流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SingleDataRecord
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
                obj = SingleDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSpeedTestingDetailsRequest(AbstractModel):
    """DescribeSpeedTestingDetails请求参数结构体

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
        


class DescribeSpeedTestingDetailsResponse(AbstractModel):
    """DescribeSpeedTestingDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpeedTestingDetailData: 分地域拨测统计数据。
        :type SpeedTestingDetailData: :class:`tencentcloud.teo.v20220901.models.SpeedTestingDetailData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpeedTestingDetailData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpeedTestingDetailData") is not None:
            self.SpeedTestingDetailData = SpeedTestingDetailData()
            self.SpeedTestingDetailData._deserialize(params.get("SpeedTestingDetailData"))
        self.RequestId = params.get("RequestId")


class DescribeSpeedTestingMetricDataRequest(AbstractModel):
    """DescribeSpeedTestingMetricData请求参数结构体

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
        


class DescribeSpeedTestingMetricDataResponse(AbstractModel):
    """DescribeSpeedTestingMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpeedTestingMetricData: 站点拨测维度数据。
        :type SpeedTestingMetricData: :class:`tencentcloud.teo.v20220901.models.SpeedTestingMetricData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpeedTestingMetricData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpeedTestingMetricData") is not None:
            self.SpeedTestingMetricData = SpeedTestingMetricData()
            self.SpeedTestingMetricData._deserialize(params.get("SpeedTestingMetricData"))
        self.RequestId = params.get("RequestId")


class DescribeSpeedTestingQuotaRequest(AbstractModel):
    """DescribeSpeedTestingQuota请求参数结构体

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
        


class DescribeSpeedTestingQuotaResponse(AbstractModel):
    """DescribeSpeedTestingQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpeedTestingQuota: 配额数据。
        :type SpeedTestingQuota: :class:`tencentcloud.teo.v20220901.models.SpeedTestingQuota`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpeedTestingQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpeedTestingQuota") is not None:
            self.SpeedTestingQuota = SpeedTestingQuota()
            self.SpeedTestingQuota._deserialize(params.get("SpeedTestingQuota"))
        self.RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 查询指标，取值有：
<li>l4Flow_connections: 访问连接数；</li>
<li>l4Flow_flux: 访问总流量；</li>
<li>l4Flow_inFlux: 访问入流量；</li>
<li>l4Flow_outFlux: 访问出流量；</li>
<li> l4Flow_outPkt: 访问出包量。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合。
若不填写，默认选择全部站点，且最多只能查询近30天的数据；
若填写，则可查询站点绑定套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>。
        :type ZoneIds: list of str
        :param ProxyIds: 四层实例列表, 不填表示选择全部实例。
        :type ProxyIds: list of str
        :param Interval: 查询时间粒度，取值有：
<li>min: 1分钟 ；</li>
<li>5min: 5分钟 ；</li>
<li>hour: 1小时 ；</li>
<li>day: 1天 。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param Filters: 过滤条件，详细的过滤条件Key值如下：
<li>ruleId<br>   按照【<strong>转发规则ID</strong>】进行过滤。</li>
<li>proxyId<br>   按照【<strong>四层代理实例ID</strong>】进行过滤。</li>
        :type Filters: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.ProxyIds = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.ProxyIds = params.get("ProxyIds")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
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
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: 四层时序流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
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
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimingL7AnalysisDataRequest(AbstractModel):
    """DescribeTimingL7AnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 指标列表，取值有:
<li>l7Flow_outFlux: Edgeone响应流量；</li>
<li>l7Flow_inFlux: Edgeone请求流量；</li>
<li>l7Flow_outBandwidth: Edgeone响应带宽；</li>
<li>l7Flow_inBandwidth：Edgeone请求带宽；</li>
<li>l7Flow_request: 访问请求数；</li>
<li>l7Flow_flux: 访问请求上行+下行流量；</li>
<li>l7Flow_bandwidth：访问请求上行+下行带宽。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合。
若不填写，默认选择全部站点，且最多只能查询近30天的数据；若填写，则可查询站点绑定套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>。
        :type ZoneIds: list of str
        :param Interval: 查询时间粒度，取值有：
<li>min: 1分钟；</li>
<li>5min: 5分钟；</li>
<li>hour: 1小时；</li>
<li>day: 1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param Filters: 过滤条件，详细的过滤条件Key值如下：
<li>country<br>   按照【<strong>国家/地区</strong>】进行过滤，国家/地区遵循<a href="https://zh.wikipedia.org/wiki/ISO_3166-1">ISO 3166</a>规范。</li>
<li>province<br>   按照【<strong>省份</strong>】进行过滤，此参数只支持服务区域为中国大陆。</li>
<li>isp<br>   按照【<strong>运营商</strong>】进行过滤，此参数只支持服务区域为中国大陆。<br>   对应的Value可选项如下：<br>   2：中国电信；<br>   26：中国联通；<br>   1046：中国移动；<br>   3947：中国铁通；<br>   38：教育网；<br>   43：长城宽带；<br>   0：其他运营商。</li>
<li>domain<br>   按照【<strong>子域名</strong>】进行过滤，子域名形如： test.example.com。</li>
<li>url<br>   按照【<strong>URL Path</strong>】进行过滤，URL Path形如：/content或/content/test.jpg。<br>   若只填写url参数，则最多可查询近30天的数据；<br>   若同时填写url+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。</li>
<li>referer<br>   按照【<strong>Referer头信息</strong>】进行过滤, Referer形如：example.com。<br>   若只填写referer参数，则最多可查询近30天的数据；<br>   若同时填写referer+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。</li>
<li>resourceType<br>   按照【<strong>资源类型</strong>】进行过滤，资源类型一般是文件后缀，形如: .jpg, .css。<br>   若只填写resourceType参数，则最多可查询近30天的数据；<br>   若同时填写resourceType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。</li>
<li>protocol<br>   按照【<strong>HTTP协议版本</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP/1.0：HTTP 1.0；<br>   HTTP/1.1：HTTP 1.1；<br>   HTTP/2.0：HTTP 2.0；<br>   HTTP/3.0：HTTP 3.0；<br>   WebSocket：WebSocket。</li>
<li>socket<br>   按照【<strong>HTTP协议类型</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP：HTTP 协议；<br>   HTTPS：HTTPS协议；<br>   QUIC：QUIC协议。</li>
<li>statusCode<br>   按照【<strong>状态码</strong>】进行过滤。<br>   若只填写statusCode参数，则最多可查询近30天的数据；<br>   若同时填写statusCode+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应的Value可选项如下：<br>   1XX：1xx类型的状态码；<br>   100：100状态码；<br>   101：101状态码；<br>   102：102状态码；<br>   2XX：2xx类型的状态码；<br>   200：200状态码；<br>   201：201状态码；<br>   202：202状态码；<br>   203：203状态码；<br>   204：204状态码；<br>   205：205状态码；<br>   206：206状态码；<br>   207：207状态码；<br>   3XX：3xx类型的状态码；<br>   300：300状态码；<br>   301：301状态码；<br>   302：302状态码；<br>   303：303状态码；<br>   304：304状态码；<br>   305：305状态码；<br>   307：307状态码；<br>   4XX：4xx类型的状态码；<br>   400：400状态码；<br>   401：401状态码；<br>   402：402状态码；<br>   403：403状态码；<br>   404：404状态码；<br>   405：405状态码；<br>   406：406状态码；<br>   407：407状态码；<br>   408：408状态码；<br>   409：409状态码；<br>   410：410状态码；<br>   411：411状态码；<br>   412：412状态码；<br>   412：413状态码；<br>   414：414状态码；<br>   415：415状态码；<br>   416：416状态码；<br>   417：417状态码；<br>   422：422状态码；<br>   423：423状态码；<br>   424：424状态码；<br>   426：426状态码；<br>   451：451状态码；<br>   5XX：5xx类型的状态码；<br>   500：500状态码；<br>   501：501状态码；<br>   502：502状态码；<br>   503：503状态码；<br>   504：504状态码；<br>   505：505状态码；<br>   506：506状态码；<br>   507：507状态码；<br>   510：510状态码；<br>   514：514状态码；<br>   544：544状态码。</li>
<li>browserType<br>   按照【<strong>浏览器类型</strong>】进行过滤。<br>   若只填写browserType参数，则最多可查询近30天的数据；<br>   若同时填写browserType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   Firefox：Firefox浏览器；<br>   Chrome：Chrome浏览器；<br>   Safari：Safari浏览器；<br>   Other：其他浏览器类型；<br>   Empty：浏览器类型为空；<br>   Bot：搜索引擎爬虫；<br>   MicrosoftEdge：MicrosoftEdge浏览器；<br>   IE：IE浏览器；<br>   Opera：Opera浏览器；<br>   QQBrowser：QQ浏览器；<br>   LBBrowser：LB浏览器；<br>   MaxthonBrowser：Maxthon浏览器；<br>   SouGouBrowser：搜狗浏览器；<br>   BIDUBrowser：百度浏览器；<br>   TaoBrowser：淘浏览器；<br>   UBrowser：UC浏览器。</li>
<li>deviceType<br>   按照【<strong>设备类型</strong>】进行过滤。<br>   若只填写deviceType参数，则最多可查询近30天的数据；<br>   若同时填写deviceType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   TV：TV设备；<br>   Tablet：Tablet设备；<br>   Mobile：Mobile设备；<br>   Desktop：Desktop设备；<br>   Other：其他设备类型；<br>   Empty：设备类型为空。</li>
<li>operatingSystemType<br>   按照【<strong>操作系统类型</strong>】进行过滤。<br>   若只填写operatingSystemType参数，则最多可查询近30天的数据；<br>   若同时填写operatingSystemType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   Linux：Linux操作系统；<br>   MacOS：MacOs操作系统；<br>   Android：Android操作系统；<br>   IOS：IOS操作系统；<br>   Windows：Windows操作系统；<br>   NetBSD：NetBSD；<br>   ChromiumOS：ChromiumOS；<br>   Bot：搜索引擎爬虫；<br>   Other：其他类型的操作系统；<br>   Empty：操作系统为空。</li>
<li>tlsVersion<br>   按照【<strong>TLS版本</strong>】进行过滤。<br>   若只填写tlsVersion参数，则最多可查询近30天的数据；<br>   若同时填写tlsVersion+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   TLS1.0：TLS 1.0；<br>   TLS1.1：TLS 1.1；<br>   TLS1.2：TLS 1.2；<br>   TLS1.3：TLS 1.3。</li>
<li>ipVersion<br>   按照【<strong>IP版本</strong>】进行过滤。<br>   对应Value的可选项如下：<br>   4：Ipv4；<br>   6：Ipv6。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。</li>
        :type Filters: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
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
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: 时序流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
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
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 查询的指标，取值有：
<li>l7Cache_outFlux：响应流量；</li>
<li>l7Cache_request：响应请求数；</li>
<li> l7Cache_outBandwidth：响应带宽。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Filters: 过滤条件，详细的过滤条件如下：
<li>domain<br>   按照【<strong>子域名</strong>】进行过滤，子域名形如： test.example.com。<br>   类型：String<br>   必选：否</li>
<li>url<br>   按照【<strong>URL</strong>】进行过滤，此参数只支持30天的时间范围，URL形如：/content。<br>   类型：String<br>   必选：否</li>
<li>resourceType<br>   按照【<strong>资源类型</strong>】进行过滤，此参数只支持30天的时间范围，资源类型形如：jpg，png。<br>   类型：String<br>   必选：否</li>
<li>cacheType<br>   按照【<strong>缓存类型</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   hit：命中缓存；<br>   dynamic：资源不可缓存；<br>   miss：未命中缓存。</li>
<li>statusCode<br>   按照【<strong>状态码</strong>】进行过滤，此参数只支持30天的时间范围。<br>   类型：String<br>   必选：否<br>   可选项：<br>   1XX：1xx类型的状态码；<br>   100：100状态码；<br>   101：101状态码；<br>   102：102状态码；<br>   2XX：2xx类型的状态码；<br>   200：200状态码；<br>   201：201状态码；<br>   202：202状态码；<br>   203：203状态码；<br>   204：204状态码；<br>   100：100状态码；<br>   206：206状态码；<br>   207：207状态码；<br>   3XX：3xx类型的状态码；<br>   300：300状态码；<br>   301：301状态码；<br>   302：302状态码；<br>   303：303状态码；<br>   304：304状态码；<br>   305：305状态码；<br>   307：307状态码；<br>   4XX：4xx类型的状态码；<br>   400：400状态码；<br>   401：401状态码；<br>   402：402状态码；<br>   403：403状态码；<br>   404：404状态码；<br>   405：405状态码；<br>   406：406状态码；<br>   407：407状态码；<br>   408：408状态码；<br>   409：409状态码；<br>   410：410状态码；<br>   411：411状态码；<br>   412：412状态码；<br>   412：413状态码；<br>   414：414状态码；<br>   415：415状态码；<br>   416：416状态码；<br>   417：417状态码；<br>   422：422状态码；<br>   423：423状态码；<br>   424：424状态码；<br>   426：426状态码；<br>   451：451状态码；<br>   5XX：5xx类型的状态码；<br>   500：500状态码；<br>   501：501状态码；<br>   502：502状态码；<br>   503：503状态码；<br>   504：504状态码；<br>   505：505状态码；<br>   506：506状态码；<br>   507：507状态码；<br>   510：510状态码；<br>   514：514状态码；<br>   544：544状态码。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
        :type Filters: list of QueryCondition
        :param Interval: 查询时间粒度，可选的值有：
<li>min：1分钟的时间粒度；</li>
<li>5min：5分钟的时间粒度；</li>
<li>hour：1小时的时间粒度；</li>
<li>day：1天的时间粒度。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
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
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: 七层缓存分析时序类流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
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
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTimingL7SourceDataRequest(AbstractModel):
    """DescribeTimingL7SourceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 指标列表，取值有:
<li>l7Flow_outFlux_hy: Edgeone请求流量；</li>
<li>l7Flow_outBandwidth_hy: Edgeone请求带宽；</li>
<li>l7Flow_inFlux_hy: 源站响应流量；</li>
<li>l7Flow_inBandwidth_hy: 源站响应带宽；</li>
<li>l7Flow_request_hy: 回源请求数；</li>
        :type MetricNames: list of str
        :param ZoneIds: 待查询的站点列表，此参数必填。
        :type ZoneIds: list of str
        :param Interval: 查询时间粒度，取值有：
<li>min: 1分钟；</li>
<li>5min: 5分钟；</li>
<li>hour: 1小时；</li>
<li>day: 1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param Filters: 过滤条件，详细的过滤条件如下：
<li>domain<br>   按照【<strong>回源Host</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>origin<br>   按照【<strong>源站</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>originGroup<br>   按照【<strong>源站组</strong>】进行过滤，源站组形如：origin-xxxxx。<br>   类型：String<br>   必选：否</li>
<li>flowType<br>   按照【<strong>源站响应类型</strong>】进行过滤，优先级高于 MetricNames.N 参数。<br>   类型：String<br>   必选：否<br>   可选项：<br>   inFlow：源站响应流量，对应MetricNames中l7Flow_inFlux_hy、l7Flow_inBandwidth_hy、l7Flow_request_hy三个指标；<br>   outFlow：EdgeOne请求流量，对应MetricNames中l7Flow_outFlux_hy、l7Flow_outBandwidth_hy、l7Flow_request_hy三个指标。</li>
        :type Filters: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Interval = None
        self.Filters = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7SourceDataResponse(AbstractModel):
    """DescribeTimingL7SourceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param TimingDataRecords: 时序流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimingDataRecords: list of TimingDataRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TimingDataRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TimingDataRecords") is not None:
            self.TimingDataRecords = []
            for item in params.get("TimingDataRecords"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self.TimingDataRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricName: 查询的指标，取值有：
<li> l7Flow_outFlux_country：按国家/地区维度统计流量指标；</li>
<li> l7Flow_outFlux_statusCode：按状态码维度统计流量指标；</li>
<li> l7Flow_outFlux_domain：按域名维度统计流量指标；</li>
<li> l7Flow_outFlux_url：按URL维度统计流量指标; </li>
<li> l7Flow_outFlux_resourceType：按资源类型维度统计流量指标；</li>
<li> l7Flow_outFlux_sip：按客户端的源IP维度统计流量指标；</li>
<li> l7Flow_outFlux_referers：按refer信息维度统计流量指标；</li>
<li> l7Flow_outFlux_ua_device：按设备类型维度统计流量指标; </li>
<li> l7Flow_outFlux_ua_browser：按浏览器类型维度统计流量指标；</li>
<li> l7Flow_outFlux_us_os：按操作系统类型维度统计流量指标；</li>
<li> l7Flow_request_country：按国家/地区维度统计请求数指标；</li>
<li> l7Flow_request_statusCode：按状态码维度统计请求数指标；</li>
<li> l7Flow_request_domain：按域名维度统计请求数指标；</li>
<li> l7Flow_request_url：按URL维度统计请求数指标; </li>
<li> l7Flow_request_resourceType：按资源类型维度统计请求数指标；</li>
<li> l7Flow_request_sip：按客户端的源IP维度统计请求数指标；</li>
<li> l7Flow_request_referer：按refer信息维度统计请求数指标；</li>
<li> l7Flow_request_ua_device：按设备类型维度统计请求数指标; </li>
<li> l7Flow_request_ua_browser：按浏览器类型维度统计请求数指标；</li>
<li> l7Flow_request_us_os：按操作系统类型维度统计请求数指标。</li>

        :type MetricName: str
        :param ZoneIds: 站点集合，此参数必填，不填默认查询为空。
        :type ZoneIds: list of str
        :param Limit: 查询前多少个数据，最大值为1000，不填默认默认为: 10， 表示查询前top10的数据。
        :type Limit: int
        :param Filters: 过滤条件，详细的过滤条件Key值如下：
<li>country<br>   按照【<strong>国家/地区</strong>】进行过滤，国家/地区遵循<a href="https://zh.wikipedia.org/wiki/ISO_3166-1">ISO 3166</a>规范。</li>
<li>province<br>   按照【<strong>省份</strong>】进行过滤，此参数只支持服务区域为中国大陆。</li>
<li>isp<br>   按照【<strong>运营商</strong>】进行过滤，此参数只支持服务区域为中国大陆。<br>   对应的Value可选项如下：<br>   2：中国电信；<br>   26：中国联通；<br>   1046：中国移动；<br>   3947：中国铁通；<br>   38：教育网；<br>   43：长城宽带；<br>   0：其他运营商。</li>
<li>domain<br>   按照【<strong>子域名</strong>】进行过滤，子域名形如： test.example.com。</li>
<li>url<br>   按照【<strong>URL Path</strong>】进行过滤，URL Path形如：/content或/content/test.jpg。<br>   若只填写url参数，则最多可查询近30天的数据；<br>   若同时填写url+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。</li>
<li>referer<br>   按照【<strong>Referer头信息</strong>】进行过滤, Referer形如：example.com。<br>   若只填写referer参数，则最多可查询近30天的数据；<br>   若同时填写referer+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。</li>
<li>resourceType<br>   按照【<strong>资源类型</strong>】进行过滤，资源类型一般是文件后缀，形如: .jpg, .css。<br>   若只填写resourceType参数，则最多可查询近30天的数据；<br>   若同时填写resourceType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。</li>
<li>protocol<br>   按照【<strong>HTTP协议版本</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP/1.0：HTTP 1.0；<br>   HTTP/1.1：HTTP 1.1；<br>   HTTP/2.0：HTTP 2.0；<br>   HTTP/3.0：HTTP 3.0；<br>   WebSocket：WebSocket。</li>
<li>socket<br>   按照【<strong>HTTP协议类型</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP：HTTP 协议；<br>   HTTPS：HTTPS协议；<br>   QUIC：QUIC协议。</li>
<li>statusCode<br>   按照【<strong>状态码</strong>】进行过滤。<br>   若只填写statusCode参数，则最多可查询近30天的数据；<br>   若同时填写statusCode+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应的Value可选项如下：<br>   1XX：1xx类型的状态码；<br>   100：100状态码；<br>   101：101状态码；<br>   102：102状态码；<br>   2XX：2xx类型的状态码；<br>   200：200状态码；<br>   201：201状态码；<br>   202：202状态码；<br>   203：203状态码；<br>   204：204状态码；<br>   205：205状态码；<br>   206：206状态码；<br>   207：207状态码；<br>   3XX：3xx类型的状态码；<br>   300：300状态码；<br>   301：301状态码；<br>   302：302状态码；<br>   303：303状态码；<br>   304：304状态码；<br>   305：305状态码；<br>   307：307状态码；<br>   4XX：4xx类型的状态码；<br>   400：400状态码；<br>   401：401状态码；<br>   402：402状态码；<br>   403：403状态码；<br>   404：404状态码；<br>   405：405状态码；<br>   406：406状态码；<br>   407：407状态码；<br>   408：408状态码；<br>   409：409状态码；<br>   410：410状态码；<br>   411：411状态码；<br>   412：412状态码；<br>   412：413状态码；<br>   414：414状态码；<br>   415：415状态码；<br>   416：416状态码；<br>   417：417状态码；<br>   422：422状态码；<br>   423：423状态码；<br>   424：424状态码；<br>   426：426状态码；<br>   451：451状态码；<br>   5XX：5xx类型的状态码；<br>   500：500状态码；<br>   501：501状态码；<br>   502：502状态码；<br>   503：503状态码；<br>   504：504状态码；<br>   505：505状态码；<br>   506：506状态码；<br>   507：507状态码；<br>   510：510状态码；<br>   514：514状态码；<br>   544：544状态码。</li>
<li>browserType<br>   按照【<strong>浏览器类型</strong>】进行过滤。<br>   若只填写browserType参数，则最多可查询近30天的数据；<br>   若同时填写browserType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   Firefox：Firefox浏览器；<br>   Chrome：Chrome浏览器；<br>   Safari：Safari浏览器；<br>   Other：其他浏览器类型；<br>   Empty：浏览器类型为空；<br>   Bot：搜索引擎爬虫；<br>   MicrosoftEdge：MicrosoftEdge浏览器；<br>   IE：IE浏览器；<br>   Opera：Opera浏览器；<br>   QQBrowser：QQ浏览器；<br>   LBBrowser：LB浏览器；<br>   MaxthonBrowser：Maxthon浏览器；<br>   SouGouBrowser：搜狗浏览器；<br>   BIDUBrowser：百度浏览器；<br>   TaoBrowser：淘浏览器；<br>   UBrowser：UC浏览器。</li>
<li>deviceType<br>   按照【<strong>设备类型</strong>】进行过滤。<br>   若只填写deviceType参数，则最多可查询近30天的数据；<br>   若同时填写deviceType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   TV：TV设备；<br>   Tablet：Tablet设备；<br>   Mobile：Mobile设备；<br>   Desktop：Desktop设备；<br>   Other：其他设备类型；<br>   Empty：设备类型为空。</li>
<li>operatingSystemType<br>   按照【<strong>操作系统类型</strong>】进行过滤。<br>   若只填写operatingSystemType参数，则最多可查询近30天的数据；<br>   若同时填写operatingSystemType+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   Linux：Linux操作系统；<br>   MacOS：MacOs操作系统；<br>   Android：Android操作系统；<br>   IOS：IOS操作系统；<br>   Windows：Windows操作系统；<br>   NetBSD：NetBSD；<br>   ChromiumOS：ChromiumOS；<br>   Bot：搜索引擎爬虫；<br>   Other：其他类型的操作系统；<br>   Empty：操作系统为空。</li>
<li>tlsVersion<br>   按照【<strong>TLS版本</strong>】进行过滤。<br>   若只填写tlsVersion参数，则最多可查询近30天的数据；<br>   若同时填写tlsVersion+Zonelds参数，则支持的查询数据范围为套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>与30天两者中的较小值。<br>   对应Value的可选项如下：<br>   TLS1.0：TLS 1.0；<br>   TLS1.1：TLS 1.1；<br>   TLS1.2：TLS 1.2；<br>   TLS1.3：TLS 1.3。</li>
<li>ipVersion<br>   按照【<strong>IP版本</strong>】进行过滤。<br>   对应Value的可选项如下：<br>   4：Ipv4；<br>   6：Ipv6。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。</li>
        :type Filters: list of QueryCondition
        :param Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Limit = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
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
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: 七层流量前topN数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopDataRecord
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
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricName: 查询的指标，取值有：
<li> l7Cache_outFlux_domain：host/域名；</li>
<li> l7Cache_outFlux_url：url地址；</li>
<li> l7Cache_outFlux_resourceType：资源类型；</li>
<li> l7Cache_outFlux_statusCode：状态码。</li>
        :type MetricName: str
        :param ZoneIds: 站点id集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Limit: 查询前多少个数据，最大值为1000，不填默认默认为10， 表示查询前top 10的数据。
        :type Limit: int
        :param Filters: 过滤条件，详细的过滤条件如下：
<li>domain<br>   按照【<strong>子域名</strong>】进行过滤，子域名形如： test.example.com。<br>   类型：String<br>   必选：否</li>
<li>url<br>   按照【<strong>URL</strong>】进行过滤，此参数只支持30天的时间范围，URL形如：/content。<br>   类型：String<br>   必选：否</li>
<li>resourceType<br>   按照【<strong>资源类型</strong>】进行过滤，此参数只支持30天的时间范围，资源类型形如：jpg，png。<br>   类型：String<br>   必选：否</li>
<li>cacheType<br>   按照【<strong>缓存类型</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   hit：命中缓存；<br>   dynamic：资源不可缓存；<br>   miss：未命中缓存。</li>
<li>statusCode<br>   按照【<strong>状态码</strong>】进行过滤，此参数只支持30天的时间范围。<br>   类型：String<br>   必选：否<br>   可选项：<br>   1XX：1xx类型的状态码；<br>   100：100状态码；<br>   101：101状态码；<br>   102：102状态码；<br>   2XX：2xx类型的状态码；<br>   200：200状态码；<br>   201：201状态码；<br>   202：202状态码；<br>   203：203状态码；<br>   204：204状态码；<br>   100：100状态码；<br>   206：206状态码；<br>   207：207状态码；<br>   3XX：3xx类型的状态码；<br>   300：300状态码；<br>   301：301状态码；<br>   302：302状态码；<br>   303：303状态码；<br>   304：304状态码；<br>   305：305状态码；<br>   307：307状态码；<br>   4XX：4xx类型的状态码；<br>   400：400状态码；<br>   401：401状态码；<br>   402：402状态码；<br>   403：403状态码；<br>   404：404状态码；<br>   405：405状态码；<br>   406：406状态码；<br>   407：407状态码；<br>   408：408状态码；<br>   409：409状态码；<br>   410：410状态码；<br>   411：411状态码；<br>   412：412状态码；<br>   412：413状态码；<br>   414：414状态码；<br>   415：415状态码；<br>   416：416状态码；<br>   417：417状态码；<br>   422：422状态码；<br>   423：423状态码；<br>   424：424状态码；<br>   426：426状态码；<br>   451：451状态码；<br>   5XX：5xx类型的状态码；<br>   500：500状态码；<br>   501：501状态码；<br>   502：502状态码；<br>   503：503状态码；<br>   504：504状态码；<br>   505：505状态码；<br>   506：506状态码；<br>   507：507状态码；<br>   510：510状态码；<br>   514：514状态码；<br>   544：544状态码。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
        :type Filters: list of QueryCondition
        :param Interval: 查询时间粒度，取值有：
<li>min: 1分钟；</li>
<li>5min: 5分钟；</li>
<li>hour: 1小时；</li>
<li>day: 1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.ZoneIds = None
        self.Limit = None
        self.Filters = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.ZoneIds = params.get("ZoneIds")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Interval = params.get("Interval")
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
        :param TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param Data: 七层缓存TopN流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopDataRecord
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
                obj = TopDataRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesDataRequest(AbstractModel):
    """DescribeWebManagedRulesData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 统计指标列表，取值有：
<li>waf_interceptNum：waf拦截次数。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 子域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param QueryCondition: 筛选条件，key可选的值有：
<li>action：执行动作。</li>
        :type QueryCondition: list of QueryCondition
        :param Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Interval = params.get("Interval")
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
        :param Data: WAF攻击的时序数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param TotalCount: 查询结果的总条数。
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
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesHitRuleDetailRequest(AbstractModel):
    """DescribeWebManagedRulesHitRuleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 子域名列表，不填默认选择全部全部子域名。
        :type Domains: list of str
        :param Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天 。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param QueryCondition: 筛选条件，key可选的值有：
<li>action ：执行动作 。</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebManagedRulesHitRuleDetailResponse(AbstractModel):
    """DescribeWebManagedRulesHitRuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 命中规则的详细列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecHitRuleInfo
        :param TotalCount: 查询结果的总条数。
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
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebManagedRulesLogRequest(AbstractModel):
    """DescribeWebManagedRulesLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param QueryCondition: 筛选条件，key可选的值有：
<li>attackType：攻击类型；</li>
<li>riskLevel：风险等级；</li>
<li>action：执行动作（处置方式）；</li>
<li>ruleId：规则id；</li>
<li>sipCountryCode：ip所在国家；</li>
<li>attackIp：攻击ip；</li>
<li>realClientIp：真实客户端ip；</li>
<li>oriDomain：被攻击的子域名；</li>
<li>eventId：事件id；</li>
<li>ua：用户代理；</li>
<li>requestMethod：请求方法；</li>
<li>uri：统一资源标识符。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        :param Data: Web攻击日志数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of WebLogs
        :param TotalCount: 查询结果的总条数。
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
                obj = WebLogs()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionClientIpListRequest(AbstractModel):
    """DescribeWebProtectionClientIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param Interval: 查询的时间粒度，支持的粒度有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param QueryCondition: 筛选条件，key可选的值有：
<li>action：执行动作。</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Interval = params.get("Interval")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionClientIpListResponse(AbstractModel):
    """DescribeWebProtectionClientIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: CC防护客户端（攻击源）ip信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecClientIp
        :param TotalCount: 查询结果的总条数。
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
                obj = SecClientIp()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionDataRequest(AbstractModel):
    """DescribeWebProtectionData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricNames: 统计指标，取值有：
<li>ccRate_interceptNum：速率限制规则限制次数；</li>
<li>ccAcl_interceptNum：自定义规则拦截次数。</li>
        :type MetricNames: list of str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param Interval: 查询时间粒度，支持的时间粒度有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param QueryCondition: 筛选条件，key可选的值有：
<li>action：执行动作。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.ZoneIds = None
        self.Domains = None
        self.Interval = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.ZoneIds = params.get("ZoneIds")
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
        


class DescribeWebProtectionDataResponse(AbstractModel):
    """DescribeWebProtectionData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: CC防护时序数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param TotalCount: 查询结果的总条数。
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
                obj = SecEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionHitRuleDetailRequest(AbstractModel):
    """DescribeWebProtectionHitRuleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param EntityType: 所属规则数据类型，支持的规则有：
<li>rate：限速规则；</li>
<li>acl：自定义规则。</li>
        :type EntityType: str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 域名列表，不填默认选择全部子域名。
        :type Domains: list of str
        :param QueryCondition: 筛选条件，key可选的值有：
<li>action：执行动作。</li>
        :type QueryCondition: list of QueryCondition
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param Interval: 查询时间粒度，支持的时间粒度有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.EntityType = None
        self.ZoneIds = None
        self.Domains = None
        self.QueryCondition = None
        self.Limit = None
        self.Offset = None
        self.Interval = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EntityType = params.get("EntityType")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        if params.get("QueryCondition") is not None:
            self.QueryCondition = []
            for item in params.get("QueryCondition"):
                obj = QueryCondition()
                obj._deserialize(item)
                self.QueryCondition.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Interval = params.get("Interval")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebProtectionHitRuleDetailResponse(AbstractModel):
    """DescribeWebProtectionHitRuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: cc防护命中规则列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecHitRuleInfo
        :param TotalCount: 查询结果的总条数。
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
                obj = SecHitRuleInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebProtectionTopDataRequest(AbstractModel):
    """DescribeWebProtectionTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param MetricName: 统计指标列表，取值有：
<li>ccRate_requestNum_url：速率限制规则请求次数url分布排行；</li>
<li>ccRate_cipRequestNum_region：速率限制规则请求次数区域客户端ip分布排行；</li>
<li>ccAcl_requestNum_url：自定义规则请求次数url分布排行；</li>
<li>ccAcl_requestNum_cip：自定义规则请求次数客户端ip分布排行；</li>
<li>ccAcl_cipRequestNum_region：自定义规则请求次数客户端区域分布排行。</li>
        :type MetricName: str
        :param Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param Limit: 查询前多少个数据，不填默认默认为10， 表示查询前top 10的数据。
        :type Limit: int
        :param QueryCondition: 筛选条件，key可选的值有：
<li>action：执行动作 。</li>
        :type QueryCondition: list of QueryCondition
        :param Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Interval = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.QueryCondition = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Interval = params.get("Interval")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
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
        


class DescribeWebProtectionTopDataResponse(AbstractModel):
    """DescribeWebProtectionTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: CC防护的TopN数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopEntry
        :param TotalCount: 查询结果的总条数。
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
                obj = TopEntry()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
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
        :param ZoneSetting: 站点配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneSetting: :class:`tencentcloud.teo.v20220901.models.ZoneSetting`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZoneSetting = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ZoneSetting") is not None:
            self.ZoneSetting = ZoneSetting()
            self.ZoneSetting._deserialize(params.get("ZoneSetting"))
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        :param Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>zone-name<br>   按照【<strong>站点名称</strong>】进行过滤。<br>   类型：String<br>   必选：否</li><li>zone-id<br>   按照【<strong>站点ID</strong>】进行过滤。站点ID形如：zone-xxx。<br>   类型：String<br>   必选：否</li><li>status<br>   按照【<strong>站点状态</strong>】进行过滤。<br>   类型：String<br>   必选：否</li><li>tag-key<br>   按照【<strong>标签键</strong>】进行过滤。<br>   类型：String<br>   必选：否</li><li>tag-value<br>   按照【<strong>标签值</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>模糊查询时仅支持过滤字段名为zone-name。
        :type Filters: list of AdvancedFilter
        :param Order: 排序字段，取值有：
<li> type：接入类型；</li>
<li> area：加速区域；</li>
<li> create-time：创建时间；</li>
<li> zone-name：站点名称；</li>
<li> use-time：最近使用时间；</li>
<li> active-status：生效状态。</li>不填写使用默认值create-time。
        :type Order: str
        :param Direction: 排序方向，取值有：
<li> asc：从小到大排序；</li>
<li> desc：从大到小排序。</li>不填写使用默认值desc。
        :type Direction: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Order = None
        self.Direction = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.Direction = params.get("Direction")
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param Status: 加速服务状态，取值为：
<li> process：部署中；</li>
<li> online：已启动；</li>
<li> offline：已关闭。</li>
        :type Status: str
        :param Host: 域名。
        :type Host: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param Cname: 分配的Cname域名
        :type Cname: str
        :param Id: 资源ID。
        :type Id: str
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param Lock: 锁状态。
        :type Lock: int
        :param Mode: 域名状态类型。
        :type Mode: int
        :param Area: 域名加速地域，取值有：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>
        :type Area: str
        :param AccelerateType: 加速类型配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccelerateType: :class:`tencentcloud.teo.v20220901.models.AccelerateType`
        :param Https: Https配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param CacheConfig: 缓存配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param Origin: 源站配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SecurityType: 安全类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityType: :class:`tencentcloud.teo.v20220901.models.SecurityType`
        :param CacheKey: 缓存键配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param Compression: 智能压缩配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param Waf: Waf防护配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Waf: :class:`tencentcloud.teo.v20220901.models.Waf`
        :param CC: CC防护配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type CC: :class:`tencentcloud.teo.v20220901.models.CC`
        :param DDoS: DDoS防护配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DDoS: :class:`tencentcloud.teo.v20220901.models.DDoS`
        :param SmartRouting: 智能路由配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param Ipv6: Ipv6访问配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ClientIpCountry: 回源时是否携带客户端IP所属地域信息的配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self.ZoneId = None
        self.Status = None
        self.Host = None
        self.ZoneName = None
        self.Cname = None
        self.Id = None
        self.InstanceId = None
        self.Lock = None
        self.Mode = None
        self.Area = None
        self.AccelerateType = None
        self.Https = None
        self.CacheConfig = None
        self.Origin = None
        self.SecurityType = None
        self.CacheKey = None
        self.Compression = None
        self.Waf = None
        self.CC = None
        self.DDoS = None
        self.SmartRouting = None
        self.Ipv6 = None
        self.ClientIpCountry = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.Host = params.get("Host")
        self.ZoneName = params.get("ZoneName")
        self.Cname = params.get("Cname")
        self.Id = params.get("Id")
        self.InstanceId = params.get("InstanceId")
        self.Lock = params.get("Lock")
        self.Mode = params.get("Mode")
        self.Area = params.get("Area")
        if params.get("AccelerateType") is not None:
            self.AccelerateType = AccelerateType()
            self.AccelerateType._deserialize(params.get("AccelerateType"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("SecurityType") is not None:
            self.SecurityType = SecurityType()
            self.SecurityType._deserialize(params.get("SecurityType"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("Waf") is not None:
            self.Waf = Waf()
            self.Waf._deserialize(params.get("Waf"))
        if params.get("CC") is not None:
            self.CC = CC()
            self.CC._deserialize(params.get("CC"))
        if params.get("DDoS") is not None:
            self.DDoS = DDoS()
            self.DDoS._deserialize(params.get("DDoS"))
        if params.get("SmartRouting") is not None:
            self.SmartRouting = SmartRouting()
            self.SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiffIPWhitelist(AbstractModel):
    """最新IP白名单列表相比于当前IP白名单列表的区别

    """

    def __init__(self):
        r"""
        :param LatestIPWhitelist: 最新IP白名单列表。
        :type LatestIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param AddedIPWhitelist: 最新IP白名单列表相比于当前IP白名单列表，新增部分。
        :type AddedIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param RemovedIPWhitelist: 最新IP白名单列表相比于当前IP白名单列表，删减部分。
        :type RemovedIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param NoChangeIPWhitelist: 最新IP白名单列表相比于当前IP白名单列表，不变部分。
        :type NoChangeIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        """
        self.LatestIPWhitelist = None
        self.AddedIPWhitelist = None
        self.RemovedIPWhitelist = None
        self.NoChangeIPWhitelist = None


    def _deserialize(self, params):
        if params.get("LatestIPWhitelist") is not None:
            self.LatestIPWhitelist = IPWhitelist()
            self.LatestIPWhitelist._deserialize(params.get("LatestIPWhitelist"))
        if params.get("AddedIPWhitelist") is not None:
            self.AddedIPWhitelist = IPWhitelist()
            self.AddedIPWhitelist._deserialize(params.get("AddedIPWhitelist"))
        if params.get("RemovedIPWhitelist") is not None:
            self.RemovedIPWhitelist = IPWhitelist()
            self.RemovedIPWhitelist._deserialize(params.get("RemovedIPWhitelist"))
        if params.get("NoChangeIPWhitelist") is not None:
            self.NoChangeIPWhitelist = IPWhitelist()
            self.NoChangeIPWhitelist._deserialize(params.get("NoChangeIPWhitelist"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistrictStatistics(AbstractModel):
    """拨测分地域统计数据

    """

    def __init__(self):
        r"""
        :param Alpha2: ISO 3166-2 国家/地区简写，详情请参考[ISO 3166-2](https://zh.m.wikipedia.org/zh-hans/ISO_3166-2)。
        :type Alpha2: str
        :param LoadTime: 整体拨测用时，单位ms。
        :type LoadTime: int
        """
        self.Alpha2 = None
        self.LoadTime = None


    def _deserialize(self, params):
        self.Alpha2 = params.get("Alpha2")
        self.LoadTime = params.get("LoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsData(AbstractModel):
    """Dns统计曲线数据项

    """

    def __init__(self):
        r"""
        :param Time: 时间。
        :type Time: str
        :param Value: 数值。
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
        


class DownloadL4LogsRequest(AbstractModel):
    """DownloadL4Logs请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param ProxyIds: 四层实例ID集合。
        :type ProxyIds: list of str
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.ProxyIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.ProxyIds = params.get("ProxyIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsResponse(AbstractModel):
    """DownloadL4Logs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 四层离线日志数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of L4OfflineLog
        :param TotalCount: 查询结果的总条数。
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
                obj = L4OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间。
        :type StartTime: str
        :param EndTime: 结束时间。
        :type EndTime: str
        :param ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param Domains: 子域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ZoneIds = None
        self.Domains = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Domains = params.get("Domains")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        :param Data: 七层离线日志数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of L7OfflineLog
        :param TotalCount: 查询结果的总条数。
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
                obj = L7OfflineLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DropPageConfig(AbstractModel):
    """拦截页面的总体配置，用于配置各个模块的拦截后行为。

    """

    def __init__(self):
        r"""
        :param Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param WafDropPageDetail: Waf(托管规则)模块的拦截页面配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WafDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        :param AclDropPageDetail: 自定义页面的拦截页面配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AclDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        """
        self.Switch = None
        self.WafDropPageDetail = None
        self.AclDropPageDetail = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("WafDropPageDetail") is not None:
            self.WafDropPageDetail = DropPageDetail()
            self.WafDropPageDetail._deserialize(params.get("WafDropPageDetail"))
        if params.get("AclDropPageDetail") is not None:
            self.AclDropPageDetail = DropPageDetail()
            self.AclDropPageDetail._deserialize(params.get("AclDropPageDetail"))
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
该Id可通过创建拦截页面接口进行上传获取。如传入0，代表使用系统默认拦截页面。
        :type PageId: int
        :param StatusCode: 拦截页面的HTTP状态码。状态码范围是100-600。
        :type StatusCode: int
        :param Name: 页面文件名或url。
        :type Name: str
        :param Type: 页面的类型，取值有：
<li> file：页面文件内容；</li>
<li> url：上传的url地址。</li>
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
        :param Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param ExceptUserRules: 例外规则详情。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptUserRules: list of ExceptUserRule
        """
        self.Switch = None
        self.ExceptUserRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("ExceptUserRules") is not None:
            self.ExceptUserRules = []
            for item in params.get("ExceptUserRules"):
                obj = ExceptUserRule()
                obj._deserialize(item)
                self.ExceptUserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRule(AbstractModel):
    """例外规则的配置，包含生效的条件，生效的范围。

    """

    def __init__(self):
        r"""
        :param RuleName: 规则名称，不可使用中文。
        :type RuleName: str
        :param Action: 规则的处置方式，当前仅支持skip：跳过全部托管规则。
        :type Action: str
        :param RuleStatus: 规则生效状态，取值有：
<li>on：生效；</li>
<li>off：失效。</li>
        :type RuleStatus: str
        :param RuleID: 规则ID。仅出参使用。默认由底层生成。
        :type RuleID: int
        :param UpdateTime: 更新时间，如果为null，默认由底层按当前时间生成。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ExceptUserRuleConditions: 匹配条件。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptUserRuleConditions: list of ExceptUserRuleCondition
        :param ExceptUserRuleScope: 规则生效的范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptUserRuleScope: :class:`tencentcloud.teo.v20220901.models.ExceptUserRuleScope`
        :param RulePriority: 优先级，取值范围0-100。如果为null，默认由底层设置为0。
        :type RulePriority: int
        """
        self.RuleName = None
        self.Action = None
        self.RuleStatus = None
        self.RuleID = None
        self.UpdateTime = None
        self.ExceptUserRuleConditions = None
        self.ExceptUserRuleScope = None
        self.RulePriority = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.RuleStatus = params.get("RuleStatus")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("ExceptUserRuleConditions") is not None:
            self.ExceptUserRuleConditions = []
            for item in params.get("ExceptUserRuleConditions"):
                obj = ExceptUserRuleCondition()
                obj._deserialize(item)
                self.ExceptUserRuleConditions.append(obj)
        if params.get("ExceptUserRuleScope") is not None:
            self.ExceptUserRuleScope = ExceptUserRuleScope()
            self.ExceptUserRuleScope._deserialize(params.get("ExceptUserRuleScope"))
        self.RulePriority = params.get("RulePriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleCondition(AbstractModel):
    """例外规则生效的具体条件。

    """

    def __init__(self):
        r"""
        :param MatchFrom: 匹配项，取值有：
<li>host：请求域名；</li>
<li>sip：客户端IP；</li>
<li>ua：User-Agent；</li>
<li>cookie：会话 Cookie；</li>
<li>cgi：CGI 脚本；</li>
<li>xff：XFF 扩展头部；</li>
<li>url：请求 URL；</li>
<li>accept：请求内容类型；</li>
<li>method：请求方式；</li>
<li>header：请求头部；</li>
<li>sip_proto：网络层协议。</li>
        :type MatchFrom: str
        :param MatchParam: 匹配项的参数。仅当 MatchFrom 为 header 时，可以使用本参数，值可填入 header 的 key 作为参数。
        :type MatchParam: str
        :param Operator: 匹配操作符，取值有：
<li>equal：字符串等于；</li>
<li>not_equal：数值不等于；</li>
<li>include：字符包含；</li>
<li>not_include：字符不包含；</li>
<li>match：ip匹配；</li>
<li>not_match：ip不匹配；</li>
<li>include_area：地域包含；</li>
<li>is_empty：存在字段但值为空；</li>
<li>not_exists：不存在关键字段；</li>
<li>regexp：正则匹配；</li>
<li>len_gt：数值大于；</li>
<li>len_lt：数值小于；</li>
<li>len_eq：数值等于；</li>
<li>match_prefix：前缀匹配；</li>
<li>match_suffix：后缀匹配；</li>
<li>wildcard：通配符。</li>
        :type Operator: str
        :param MatchContent: 匹配值。
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
    """例外规则的生效范围。

    """

    def __init__(self):
        r"""
        :param Type: 例外规则类型。其中complete模式代表全量数据进行例外，partial模式代表可选择指定模块指定字段进行例外，该字段取值有：
<li>complete：完全跳过模式；</li>
<li>partial：部分跳过模式。</li>
        :type Type: str
        :param Modules: 生效的模块，该字段取值有：
<li>waf：托管规则；</li>
<li>rate：速率限制；</li>
<li>acl：自定义规则；</li>
<li>cc：cc攻击防护；</li>
<li>bot：Bot防护。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Modules: list of str
        :param PartialModules: 跳过部分规则ID的例外规则详情。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type PartialModules: list of PartialModule
        :param SkipConditions: 跳过具体字段不去扫描的例外规则详情。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipConditions: list of SkipCondition
        """
        self.Type = None
        self.Modules = None
        self.PartialModules = None
        self.SkipConditions = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Modules = params.get("Modules")
        if params.get("PartialModules") is not None:
            self.PartialModules = []
            for item in params.get("PartialModules"):
                obj = PartialModule()
                obj._deserialize(item)
                self.PartialModules.append(obj)
        if params.get("SkipConditions") is not None:
            self.SkipConditions = []
            for item in params.get("SkipConditions"):
                obj = SkipCondition()
                obj._deserialize(item)
                self.SkipConditions.append(obj)
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
        :param Reason: 失败原因。
        :type Reason: str
        :param Targets: 处理失败的资源列表。
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
        


class FileAscriptionInfo(AbstractModel):
    """站点归属权校验——文件校验信息。

    """

    def __init__(self):
        r"""
        :param IdentifyPath: 文件校验目录。
        :type IdentifyPath: str
        :param IdentifyContent: 文件校验内容。
        :type IdentifyContent: str
        """
        self.IdentifyPath = None
        self.IdentifyContent = None


    def _deserialize(self, params):
        self.IdentifyPath = params.get("IdentifyPath")
        self.IdentifyContent = params.get("IdentifyContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等。
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
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
        


class FirstPartConfig(AbstractModel):
    """慢速攻击的首段包配置。

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param StatTime: 首段包的统计时长，单位是秒，即期望首段包的统计时长是多少，默认5秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatTime: int
        """
        self.Switch = None
        self.StatTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.StatTime = params.get("StatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowOrigin(AbstractModel):
    """缓存遵循源站配置

    """

    def __init__(self):
        r"""
        :param Switch: 遵循源站配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param DefaultCacheTime: 源站未返回 Cache-Control 头时, 设置默认的缓存时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCacheTime: int
        :param DefaultCache: 源站未返回 Cache-Control 头时, 设置缓存/不缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCache: str
        :param DefaultCacheStrategy: 源站未返回 Cache-Control 头时, 使用/不使用默认缓存策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCacheStrategy: str
        """
        self.Switch = None
        self.DefaultCacheTime = None
        self.DefaultCache = None
        self.DefaultCacheStrategy = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.DefaultCacheTime = params.get("DefaultCacheTime")
        self.DefaultCache = params.get("DefaultCache")
        self.DefaultCacheStrategy = params.get("DefaultCacheStrategy")
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
        


class Grpc(AbstractModel):
    """Grpc配置项

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启 Grpc 配置，取值有：
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
        


class Header(AbstractModel):
    """刷新预热附带的头部信息

    """

    def __init__(self):
        r"""
        :param Name: HTTP头部名称。
        :type Name: str
        :param Value: HTTP头部值。
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
        


class Hsts(AbstractModel):
    """Hsts配置

    """

    def __init__(self):
        r"""
        :param Switch: 是否开启，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param MaxAge: MaxAge 数值。单位为秒，最大值为1天。
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
        :param TlsVersion: Tls 版本设置，取值有：
<li>TLSv1：TLSv1版本；</li>
<li>TLSV1.1：TLSv1.1版本；</li>
<li>TLSV1.2：TLSv1.2版本；</li>
<li>TLSv1.3：TLSv1.3版本。</li>修改时必须开启连续的版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type TlsVersion: list of str
        :param Hsts: HSTS 配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.teo.v20220901.models.Hsts`
        :param CertInfo: 证书配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: list of ServerCertInfo
        :param ApplyType: 申请类型，取值有：
<li>apply：托管EdgeOne；</li>
<li>none：不托管EdgeOne。</li>不填，默认取值为none。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyType: str
        :param CipherSuite: 密码套件，取值有：
<li>loose-v2023：提供最高的兼容性，安全性一般，支持 TLS 1.0-1.3 密码套件；</li>
<li>general-v2023：提供较高的兼容性，安全性中等，支持 TLS 1.2-1.3 密码套件；</li>
<li>strict-v2023：提供最高的安全性能，禁用所有含不安全隐患的加密套件，支持 TLS 1.2-1.3 密码套件。
注意：此字段可能返回 null，表示取不到有效值。
        :type CipherSuite: str
        """
        self.Http2 = None
        self.OcspStapling = None
        self.TlsVersion = None
        self.Hsts = None
        self.CertInfo = None
        self.ApplyType = None
        self.CipherSuite = None


    def _deserialize(self, params):
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
        if params.get("CertInfo") is not None:
            self.CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.CertInfo.append(obj)
        self.ApplyType = params.get("ApplyType")
        self.CipherSuite = params.get("CipherSuite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPGroup(AbstractModel):
    """IP 网段组

    """

    def __init__(self):
        r"""
        :param GroupId: 组 Id，创建时填 0 即可。
        :type GroupId: int
        :param Name: 组名称。
        :type Name: str
        :param Content: IP 组内容，可以填入 IP 及 IP 掩码。
        :type Content: list of str
        """
        self.GroupId = None
        self.Name = None
        self.Content = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Name = params.get("Name")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPWhitelist(AbstractModel):
    """源站防护IP白名单

    """

    def __init__(self):
        r"""
        :param IPv4: IPv4列表。
        :type IPv4: list of str
        :param IPv6: IPv6列表。
        :type IPv6: list of str
        """
        self.IPv4 = None
        self.IPv6 = None


    def _deserialize(self, params):
        self.IPv4 = params.get("IPv4")
        self.IPv6 = params.get("IPv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identification(AbstractModel):
    """站点验证信息

    """

    def __init__(self):
        r"""
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param Domain: 验证子域名。验证站点时，该值为空。验证子域名是为具体子域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Status: 验证状态，取值有：
<li> pending：验证中；</li>
<li> finished：验证完成。</li>
        :type Status: str
        :param Ascription: 站点归属权校验：Dns校验信息。
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param OriginalNameServers: 域名当前的 NS 记录。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalNameServers: list of str
        :param FileAscription: 站点归属权校验：文件校验信息。
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        """
        self.ZoneName = None
        self.Domain = None
        self.Status = None
        self.Ascription = None
        self.OriginalNameServers = None
        self.FileAscription = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Domain = params.get("Domain")
        self.Status = params.get("Status")
        if params.get("Ascription") is not None:
            self.Ascription = AscriptionInfo()
            self.Ascription._deserialize(params.get("Ascription"))
        self.OriginalNameServers = params.get("OriginalNameServers")
        if params.get("FileAscription") is not None:
            self.FileAscription = FileAscriptionInfo()
            self.FileAscription._deserialize(params.get("FileAscription"))
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
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param Domain: 站点下的子域名。如果验证站点下的子域名，则传该值，否则为空。

        :type Domain: str
        """
        self.ZoneName = None
        self.Domain = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Domain = params.get("Domain")
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
        :param Ascription: 站点归属校验：Dns校验信息。
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param FileAscription: 站点归属权校验：文件校验信息。
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ascription = None
        self.FileAscription = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ascription") is not None:
            self.Ascription = AscriptionInfo()
            self.Ascription._deserialize(params.get("Ascription"))
        if params.get("FileAscription") is not None:
            self.FileAscription = FileAscriptionInfo()
            self.FileAscription._deserialize(params.get("FileAscription"))
        self.RequestId = params.get("RequestId")


class ImageOptimize(AbstractModel):
    """图片优化配置。

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
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
        


class IntelligenceRule(AbstractModel):
    """智能分析规则

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param IntelligenceRuleItems: 规则详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntelligenceRuleItems: list of IntelligenceRuleItem
        """
        self.Switch = None
        self.IntelligenceRuleItems = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("IntelligenceRuleItems") is not None:
            self.IntelligenceRuleItems = []
            for item in params.get("IntelligenceRuleItems"):
                obj = IntelligenceRuleItem()
                obj._deserialize(item)
                self.IntelligenceRuleItems.append(obj)
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
        :param Label: 智能分析标签，取值有：
<li>evil_bot：恶意bot；</li>
<li>suspect_bot：疑似bot；</li>
<li>good_bot：良好bot；</li>
<li>normal：正常请求。</li>
        :type Label: str
        :param Action: 触发智能分析标签对应的处置方式，取值有：
<li>drop：拦截；</li>
<li>trans：放行；</li>
<li>alg：Javascript挑战；</li>
<li>captcha：数字验证码；</li>
<li>monitor：观察。</li>
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
        :param Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭；</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param IpTableRules: 基础管控规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTableRules: list of IpTableRule
        """
        self.Switch = None
        self.IpTableRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("IpTableRules") is not None:
            self.IpTableRules = []
            for item in params.get("IpTableRules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self.IpTableRules.append(obj)
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
        :param Action: 动作，取值有：
<li> drop：拦截；</li>
<li> trans：放行；</li>
<li> monitor：观察。</li>
        :type Action: str
        :param MatchFrom: 根据类型匹配，取值有：
<li>ip：对ip进行匹配；</li>
<li>area：对ip所属地区匹配。</li>
        :type MatchFrom: str
        :param Operator: 规则的匹配方式，默认为空代表等于。
取值有：
<li> is_emty：配置为空；</li>
<li> not_exists：配置为不存在；</li>
<li> include：包含；</li>
<li> not_include：不包含；</li>
<li> equal：等于；</li>
<li> not_equal：不等于。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param RuleID: 规则id。仅出参使用。
        :type RuleID: int
        :param UpdateTime: 更新时间。仅出参使用。
        :type UpdateTime: str
        :param Status: 规则启用状态，当返回为null时，为启用。取值有：
<li> on：启用；</li>
<li> off：未启用。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RuleName: 规则名。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param MatchContent: 匹配内容。当 Operator为is_emty 或not_exists时，此值允许为空。
        :type MatchContent: str
        """
        self.Action = None
        self.MatchFrom = None
        self.Operator = None
        self.RuleID = None
        self.UpdateTime = None
        self.Status = None
        self.RuleName = None
        self.MatchContent = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.MatchFrom = params.get("MatchFrom")
        self.Operator = params.get("Operator")
        self.RuleID = params.get("RuleID")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.RuleName = params.get("RuleName")
        self.MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """Ipv6访问配置

    """

    def __init__(self):
        r"""
        :param Switch: Ipv6 访问功能配置，取值有：
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
        


class L4OfflineLog(AbstractModel):
    """离线日志详细信息

    """

    def __init__(self):
        r"""
        :param LogTime: 日志打包开始时间。
        :type LogTime: int
        :param ProxyId: 四层实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param Size: 原始大小 单位byte。
        :type Size: int
        :param Url: 下载地址。
        :type Url: str
        :param LogPacketName: 日志数据包名。
        :type LogPacketName: str
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        """
        self.LogTime = None
        self.ProxyId = None
        self.Size = None
        self.Url = None
        self.LogPacketName = None
        self.Area = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.ProxyId = params.get("ProxyId")
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
        


class L7OfflineLog(AbstractModel):
    """离线日志详细信息

    """

    def __init__(self):
        r"""
        :param LogTime: 日志打包开始时间。
        :type LogTime: int
        :param Domain: 子域名。
        :type Domain: str
        :param Size: 原始大小，单位byte。
        :type Size: int
        :param Url: 下载地址。
        :type Url: str
        :param LogPacketName: 日志数据包名。
        :type LogPacketName: str
        :param Area: 加速区域，取值有：
<li>mainland：中国大陆境内; </li>
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
        


class LogSetInfo(AbstractModel):
    """日志集基本信息

    """

    def __init__(self):
        r"""
        :param LogSetRegion: 日志集所属地区。
        :type LogSetRegion: str
        :param LogSetName: 日志集名
        :type LogSetName: str
        :param LogSetId: 日志集Id
        :type LogSetId: str
        :param Deleted: 该日志集是否已被删除, 可选的值有：
<li>no: 日志集没有被删除；</li>
<li>yes: 日志集已经被删除；</li>
        :type Deleted: str
        """
        self.LogSetRegion = None
        self.LogSetName = None
        self.LogSetId = None
        self.Deleted = None


    def _deserialize(self, params):
        self.LogSetRegion = params.get("LogSetRegion")
        self.LogSetName = params.get("LogSetName")
        self.LogSetId = params.get("LogSetId")
        self.Deleted = params.get("Deleted")
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
        


class ModifyAccelerationDomainRequest(AbstractModel):
    """ModifyAccelerationDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param DomainName: 加速域名名称。
        :type DomainName: str
        :param OriginInfo: 源站信息。
        :type OriginInfo: :class:`tencentcloud.teo.v20220901.models.OriginInfo`
        """
        self.ZoneId = None
        self.DomainName = None
        self.OriginInfo = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.DomainName = params.get("DomainName")
        if params.get("OriginInfo") is not None:
            self.OriginInfo = OriginInfo()
            self.OriginInfo._deserialize(params.get("OriginInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainResponse(AbstractModel):
    """ModifyAccelerationDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccelerationDomainStatusesRequest(AbstractModel):
    """ModifyAccelerationDomainStatuses请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param DomainNames: 要执行状态变更的加速域名列表。
        :type DomainNames: list of str
        :param Status: 加速域名状态，取值有：
<li>online：启用；</li>
<li>offline：停用。</li>
        :type Status: str
        :param Force: 是否强制停用。当域名存在关联资源（如马甲域名、流量调度功能）时，是否强制停用该域名，取值有：
<li> true：停用该域名及所有关联资源；</li>
<li> false：当该加速域名存在关联资源时，不允许停用。</li>不填写，默认值为：false。
        :type Force: bool
        """
        self.ZoneId = None
        self.DomainNames = None
        self.Status = None
        self.Force = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.DomainNames = params.get("DomainNames")
        self.Status = params.get("Status")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainStatusesResponse(AbstractModel):
    """ModifyAccelerationDomainStatuses返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAliasDomainRequest(AbstractModel):
    """ModifyAliasDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param AliasName: 别称域名名称。
        :type AliasName: str
        :param TargetName: 目标域名名称。
        :type TargetName: str
        :param CertType: 证书配置，取值有：
<li> none：不配置；</li>
<li> hosting：SSL托管证书；</li>
<li> apply：申请免费证书。</li>不填写保持原有配置。
        :type CertType: str
        :param CertId: 当 CertType 取值为 hosting 时填入相应证书 ID。
        :type CertId: list of str
        """
        self.ZoneId = None
        self.AliasName = None
        self.TargetName = None
        self.CertType = None
        self.CertId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.AliasName = params.get("AliasName")
        self.TargetName = params.get("TargetName")
        self.CertType = params.get("CertType")
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainResponse(AbstractModel):
    """ModifyAliasDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAliasDomainStatusRequest(AbstractModel):
    """ModifyAliasDomainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Paused: 别称域名状态，取值有：
<li> false：开启别称域名；</li>
<li> true：关闭别称域名。</li>
        :type Paused: bool
        :param AliasNames: 待修改状态的别称域名名称。如果为空，则不执行修改状态操作。
        :type AliasNames: list of str
        """
        self.ZoneId = None
        self.Paused = None
        self.AliasNames = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Paused = params.get("Paused")
        self.AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainStatusResponse(AbstractModel):
    """ModifyAliasDomainStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param ProxyId: 代理 ID。
        :type ProxyId: str
        :param ProxyName: 当 ProxyType=hostname 时，表示域名或子域名；
当 ProxyType=instance 时，表示代理名称。
        :type ProxyName: str
        :param SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒。
不填写保持原有配置。
        :type SessionPersistTime: int
        :param ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>不填写保持原有配置。
        :type ProxyType: str
        :param Ipv6: Ipv6 访问配置，不填写保持原有配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param AccelerateMainland: 中国大陆加速优化配置。 不填写表示保持原有配置。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self.ZoneId = None
        self.ProxyId = None
        self.ProxyName = None
        self.SessionPersistTime = None
        self.ProxyType = None
        self.Ipv6 = None
        self.AccelerateMainland = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        self.SessionPersistTime = params.get("SessionPersistTime")
        self.ProxyType = params.get("ProxyType")
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("AccelerateMainland") is not None:
            self.AccelerateMainland = AccelerateMainland()
            self.AccelerateMainland._deserialize(params.get("AccelerateMainland"))
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param RuleId: 规则ID。
        :type RuleId: str
        :param OriginType: 源站类型，取值有：
<li>custom：手动添加；</li>
<li>origins：源站组。</li>不填保持原有值。
        :type OriginType: str
        :param Port: 端口，支持格式：
<li>80：80端口；</li>
<li>81-90：81至90端口。</li>
        :type Port: list of str
        :param Proto: 协议，取值有：
<li>TCP：TCP协议；</li>
<li>UDP：UDP协议。</li>不填保持原有值。
        :type Proto: str
        :param OriginValue: 源站信息：
<li>当 OriginType 为 custom 时，表示一个或多个源站，如`["8.8.8.8","9.9.9.9"]` 或 `OriginValue=["test.com"]`；</li>
<li>当 OriginType 为 origins 时，要求有且仅有一个元素，表示源站组ID，如`["origin-537f5b41-162a-11ed-abaa-525400c5da15"]`。</li>

不填保持原有值。
        :type OriginValue: list of str
        :param ForwardClientIp: 传递客户端IP，取值有：
<li>TOA：TOA（仅Proto=TCP时可选）；</li>
<li>PPV1：Proxy Protocol传递，协议版本V1（仅Proto=TCP时可选）；</li>
<li>PPV2：Proxy Protocol传递，协议版本V2；</li>
<li>OFF：不传递。</li>不填保持原有值。
        :type ForwardClientIp: str
        :param SessionPersist: 是否开启会话保持，取值有：
<li>true：开启；</li>
<li>false：关闭。</li>不填为false。
        :type SessionPersist: bool
        :param OriginPort: 源站端口，支持格式：
<li>单端口：80；</li>
<li>端口段：81-90，81至90端口。</li>
        :type OriginPort: str
        """
        self.ZoneId = None
        self.ProxyId = None
        self.RuleId = None
        self.OriginType = None
        self.Port = None
        self.Proto = None
        self.OriginValue = None
        self.ForwardClientIp = None
        self.SessionPersist = None
        self.OriginPort = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ProxyId = params.get("ProxyId")
        self.RuleId = params.get("RuleId")
        self.OriginType = params.get("OriginType")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")
        self.OriginValue = params.get("OriginValue")
        self.ForwardClientIp = params.get("ForwardClientIp")
        self.SessionPersist = params.get("SessionPersist")
        self.OriginPort = params.get("OriginPort")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param RuleId: 规则ID。
        :type RuleId: str
        :param Status: 状态，取值有：
<li>offline: 停用；</li>
<li>online: 启用。</li>
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ProxyId: 代理ID。
        :type ProxyId: str
        :param Status: 状态，取值有：
<li>offline: 停用；</li>
<li>online: 启用。</li>
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDefaultCertificateRequest(AbstractModel):
    """ModifyDefaultCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param CertId: 默认证书ID。
        :type CertId: str
        :param Status: 证书状态，取值有：
<li>deployed ：部署证书；</li>
<li>disabled ：禁用证书。</li>失败状态下重新deployed即可重试。
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


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Hosts: 本次变更的域名列表。
        :type Hosts: list of str
        :param ServerCertInfo: 证书信息, 只需要传入 CertId 即可, 如果为空, 则使用默认证书。
        :type ServerCertInfo: list of ServerCertInfo
        :param ApplyType: 托管类型，取值有：
<li>apply：托管EO；</li>
<li>none：不托管EO；</li>不填，默认取值为apply。
        :type ApplyType: str
        """
        self.ZoneId = None
        self.Hosts = None
        self.ServerCertInfo = None
        self.ApplyType = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
        if params.get("ServerCertInfo") is not None:
            self.ServerCertInfo = []
            for item in params.get("ServerCertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self.ServerCertInfo.append(obj)
        self.ApplyType = params.get("ApplyType")
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


class ModifyOriginGroupRequest(AbstractModel):
    """ModifyOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param OriginGroupId: 源站组ID。
        :type OriginGroupId: str
        :param OriginType: 源站类型，取值有：
<li>self：自有源站；</li>
<li>third_party：第三方源站；</li>
<li>cos：腾讯云COS源站。</li>
        :type OriginType: str
        :param OriginGroupName: 源站组名称。
        :type OriginGroupName: str
        :param ConfigurationType: 源站配置类型，当OriginType=self时，取值有：
<li>area：按区域配置；</li>
<li>weight： 按权重配置；</li>
<li>proto： 按HTTP协议配置。</li>当OriginType=third_party/cos时放空。
        :type ConfigurationType: str
        :param OriginRecords: 源站记录信息。
        :type OriginRecords: list of OriginRecord
        :param HostHeader: 回源Host，仅当OriginType=self时可以设置。
不填写，表示使用已有配置。
        :type HostHeader: str
        """
        self.ZoneId = None
        self.OriginGroupId = None
        self.OriginType = None
        self.OriginGroupName = None
        self.ConfigurationType = None
        self.OriginRecords = None
        self.HostHeader = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.OriginGroupId = params.get("OriginGroupId")
        self.OriginType = params.get("OriginType")
        self.OriginGroupName = params.get("OriginGroupName")
        self.ConfigurationType = params.get("ConfigurationType")
        if params.get("OriginRecords") is not None:
            self.OriginRecords = []
            for item in params.get("OriginRecords"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.OriginRecords.append(obj)
        self.HostHeader = params.get("HostHeader")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :type Rules: list of Rule
        :param RuleId: 规则 ID。
        :type RuleId: str
        :param Status: 规则状态，取值有：
<li> enable: 启用； </li>
<li> disable: 未启用。</li>
        :type Status: str
        :param Tags: 规则标签。
        :type Tags: list of str
        """
        self.ZoneId = None
        self.RuleName = None
        self.Rules = None
        self.RuleId = None
        self.Status = None
        self.Tags = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleName = params.get("RuleName")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RuleId = params.get("RuleId")
        self.Status = params.get("Status")
        self.Tags = params.get("Tags")
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


class ModifySecurityIPGroupRequest(AbstractModel):
    """ModifySecurityIPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 Id。
        :type ZoneId: str
        :param IPGroup: IP 组配置。
        :type IPGroup: :class:`tencentcloud.teo.v20220901.models.IPGroup`
        :param Mode: 操作类型，取值有：
<li> append: 向 IPGroup 中追加 Content 参数中内容；</li>
<li> remove: 从 IPGroup 中删除 Content 参数中内容；</li>
<li> update: 全量替换 IPGroup 内容，并可修改 IPGroup 名称。 </li>
        :type Mode: str
        """
        self.ZoneId = None
        self.IPGroup = None
        self.Mode = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("IPGroup") is not None:
            self.IPGroup = IPGroup()
            self.IPGroup._deserialize(params.get("IPGroup"))
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityIPGroupResponse(AbstractModel):
    """ModifySecurityIPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点Id。
        :type ZoneId: str
        :param SecurityConfig: 安全配置。
        :type SecurityConfig: :class:`tencentcloud.teo.v20220901.models.SecurityConfig`
        :param Entity: 子域名/应用名。当使用Entity时可不填写TemplateId，否则必须填写TemplateId。
        :type Entity: str
        :param TemplateId: 模板策略id。当使用模板Id时可不填Entity，否则必须填写Entity。
        :type TemplateId: str
        """
        self.ZoneId = None
        self.SecurityConfig = None
        self.Entity = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("SecurityConfig") is not None:
            self.SecurityConfig = SecurityConfig()
            self.SecurityConfig._deserialize(params.get("SecurityConfig"))
        self.Entity = params.get("Entity")
        self.TemplateId = params.get("TemplateId")
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


class ModifySecurityWafGroupPolicyRequest(AbstractModel):
    """ModifySecurityWafGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点Id。当使用ZoneId和Entity时可不填写TemplateId，否则必须填写TemplateId。
        :type ZoneId: str
        :param Entity: 子域名。当使用ZoneId和Entity时可不填写TemplateId，否则必须填写TemplateId。
        :type Entity: str
        :param Switch: 总开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>不填默认为上次的配置。
        :type Switch: str
        :param Level: 规则等级，取值有：
<li> loose：宽松；</li>
<li> normal：正常；</li>
<li> strict：严格；</li>
<li> stricter：超严格；</li>
<li> custom：自定义。</li>不填默认为上次的配置。
        :type Level: str
        :param Mode: 处置方式，取值有：
<li> block：阻断；</li>
<li> observe：观察。</li>不填默认为上次的配置。
        :type Mode: str
        :param WafRules: 托管规则。不填默认为上次的配置。
        :type WafRules: :class:`tencentcloud.teo.v20220901.models.WafRule`
        :param AiRule: AI引擎模式。不填默认为上次的配置。
        :type AiRule: :class:`tencentcloud.teo.v20220901.models.AiRule`
        :param WafGroups: 托管规则等级组。不填默认为上次的配置。
        :type WafGroups: list of WafGroup
        :param TemplateId: 模板Id。当使用模板Id时可不填ZoneId和Entity，否则必须填写ZoneId和Entity。
        :type TemplateId: str
        """
        self.ZoneId = None
        self.Entity = None
        self.Switch = None
        self.Level = None
        self.Mode = None
        self.WafRules = None
        self.AiRule = None
        self.WafGroups = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Entity = params.get("Entity")
        self.Switch = params.get("Switch")
        self.Level = params.get("Level")
        self.Mode = params.get("Mode")
        if params.get("WafRules") is not None:
            self.WafRules = WafRule()
            self.WafRules._deserialize(params.get("WafRules"))
        if params.get("AiRule") is not None:
            self.AiRule = AiRule()
            self.AiRule._deserialize(params.get("AiRule"))
        if params.get("WafGroups") is not None:
            self.WafGroups = []
            for item in params.get("WafGroups"):
                obj = WafGroup()
                obj._deserialize(item)
                self.WafGroups.append(obj)
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityWafGroupPolicyResponse(AbstractModel):
    """ModifySecurityWafGroupPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Type: 站点接入方式，取值有：
<li> full：NS 接入；</li>
<li> partial：CNAME 接入。</li>不填写保持原有配置。
        :type Type: str
        :param VanityNameServers: 自定义站点信息，以替代系统默认分配的名称服务器。不填写保持原有配置。
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param AliasZoneName: 站点别名。数字、英文、-和_组合，限制20个字符。
        :type AliasZoneName: str
        """
        self.ZoneId = None
        self.Type = None
        self.VanityNameServers = None
        self.AliasZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        self.AliasZoneName = params.get("AliasZoneName")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 待变更的站点 ID。
        :type ZoneId: str
        :param CacheConfig: 缓存过期时间配置。
不填写表示保持原有配置。
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param CacheKey: 节点缓存键配置。
不填写表示保持原有配置。
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param MaxAge: 浏览器缓存配置。
不填写表示保持原有配置。
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param OfflineCache: 离线缓存配置。
不填写表示保持原有配置。
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param Quic: Quic 访问配置。
不填写表示保持原有配置。
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param PostMaxSize: Post 请求传输配置。
不填写表示保持原有配置。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param Compression: 智能压缩配置。
不填写表示保持原有配置。
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param UpstreamHttp2: Http2 回源配置。
不填写表示保持原有配置。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制 Https 跳转配置。
不填写表示保持原有配置。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param Https: Https 加速配置。
不填写表示保持原有配置。
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param Origin: 源站配置。
不填写表示保持原有配置。
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SmartRouting: 智能加速配置。
不填写表示保持原有配置。
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param WebSocket: WebSocket 配置。
不填写表示保持原有配置。
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param ClientIpHeader: 客户端 IP 回源请求头配置。
不填写表示保持原有配置。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param CachePrefresh: 缓存预刷新配置。
不填写表示保持原有配置。
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param Ipv6: Ipv6 访问配置。
不填写表示保持原有配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param ClientIpCountry: 回源时是否携带客户端 IP 所属地域信息的配置。
不填写表示保持原有配置。
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        :param Grpc: Grpc 协议支持配置。
不填写表示保持原有配置。
        :type Grpc: :class:`tencentcloud.teo.v20220901.models.Grpc`
        :param ImageOptimize: 图片优化配置。
不填写表示关闭。
        :type ImageOptimize: :class:`tencentcloud.teo.v20220901.models.ImageOptimize`
        """
        self.ZoneId = None
        self.CacheConfig = None
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
        self.ClientIpCountry = None
        self.Grpc = None
        self.ImageOptimize = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
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
            self.ClientIpHeader = ClientIpHeader()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        if params.get("Grpc") is not None:
            self.Grpc = Grpc()
            self.Grpc._deserialize(params.get("Grpc"))
        if params.get("ImageOptimize") is not None:
            self.ImageOptimize = ImageOptimize()
            self.ImageOptimize._deserialize(params.get("ImageOptimize"))
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param Paused: 站点状态，取值有：
<li> false：开启站点；</li>
<li> true：关闭站点。</li>
        :type Paused: bool
        """
        self.ZoneId = None
        self.Paused = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NoCache(AbstractModel):
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
        


class NormalAction(AbstractModel):
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
        


class OptimizeAction(AbstractModel):
    """站点拨测优化建议

    """

    def __init__(self):
        r"""
        :param Name: 站点性能优化配置项，取值有：
<li>Http2；</li>
<li>Http3；</li>
<li>Brotli。</li>
        :type Name: str
        :param Connectivity: 网络环境。
        :type Connectivity: str
        :param Value: 开启配置项后，预估性能优化效果，单位ms。
        :type Value: int
        :param Ratio: 开启配置项后，预估性能提升比例，单位%。
        :type Ratio: int
        """
        self.Name = None
        self.Connectivity = None
        self.Value = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Connectivity = params.get("Connectivity")
        self.Value = params.get("Value")
        self.Ratio = params.get("Ratio")
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
<li>https：强制 https 回源。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param CosPrivateAccess: 源站为腾讯云 COS 时，是否为私有访问 bucket，取值有：
<li>on：私有访问；</li>
<li>off：公共访问。</li>
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
        


class OriginDetail(AbstractModel):
    """加速域名源站信息。

    """

    def __init__(self):
        r"""
        :param OriginType: 源站类型，取值有：
<li>IP_DOMAIN：IPV4、IPV6或域名类型源站；</li>
<li>COS：COS源。</li>
<li>ORIGIN_GROUP：源站组类型源站。</li>
<li>AWS_S3：AWS S3对象存储源站。</li>
        :type OriginType: str
        :param Origin: 源站地址，当OriginType参数指定为ORIGIN_GROUP时，该参数填写源站组ID，其他情况下填写源站地址。
        :type Origin: str
        :param BackupOrigin: 备用源站组ID，该参数在OriginType参数指定为ORIGIN_GROUP时生效，为空表示不使用备用源站。
        :type BackupOrigin: str
        :param OriginGroupName: 主源源站组名称，当OriginType参数指定为ORIGIN_GROUP时该参数生效。
        :type OriginGroupName: str
        :param BackOriginGroupName: 备用源站源站组名称，当OriginType参数指定为ORIGIN_GROUP，且用户指定了被用源站时该参数生效。
        :type BackOriginGroupName: str
        :param PrivateAccess: 指定是否允许访问私有对象存储源站。当源站类型OriginType=COS或AWS_S3时有效 取值有：
<li>on：使用私有鉴权；</li>
<li>off：不使用私有鉴权。</li>
不填写，默认值为off。
        :type PrivateAccess: str
        :param PrivateParameters: 私有鉴权使用参数，当源站类型PrivateAccess=on时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateParameters: list of PrivateParameter
        """
        self.OriginType = None
        self.Origin = None
        self.BackupOrigin = None
        self.OriginGroupName = None
        self.BackOriginGroupName = None
        self.PrivateAccess = None
        self.PrivateParameters = None


    def _deserialize(self, params):
        self.OriginType = params.get("OriginType")
        self.Origin = params.get("Origin")
        self.BackupOrigin = params.get("BackupOrigin")
        self.OriginGroupName = params.get("OriginGroupName")
        self.BackOriginGroupName = params.get("BackOriginGroupName")
        self.PrivateAccess = params.get("PrivateAccess")
        if params.get("PrivateParameters") is not None:
            self.PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self.PrivateParameters.append(obj)
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param OriginGroupId: 源站组ID。
        :type OriginGroupId: str
        :param OriginType: 源站类型，取值有：
<li>self：自有源站；</li>
<li>third_party：第三方源站；</li>
<li>cos：腾讯云COS源站。</li>
        :type OriginType: str
        :param OriginGroupName: 源站组名称。
        :type OriginGroupName: str
        :param ConfigurationType: 源站配置类型，当OriginType=self时，取值有：
<li>area：按区域配置；</li>
<li>weight： 按权重配置。</li>
<li>proto： 按HTTP协议配置。</li>当OriginType=third_party/cos时放空。
        :type ConfigurationType: str
        :param OriginRecords: 源站记录信息。
        :type OriginRecords: list of OriginRecord
        :param UpdateTime: 源站组更新时间。
        :type UpdateTime: str
        :param HostHeader: 当OriginType=self时，表示回源Host。
注意：此字段可能返回 null，表示取不到有效值。
        :type HostHeader: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.OriginGroupId = None
        self.OriginType = None
        self.OriginGroupName = None
        self.ConfigurationType = None
        self.OriginRecords = None
        self.UpdateTime = None
        self.HostHeader = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.OriginGroupId = params.get("OriginGroupId")
        self.OriginType = params.get("OriginType")
        self.OriginGroupName = params.get("OriginGroupName")
        self.ConfigurationType = params.get("ConfigurationType")
        if params.get("OriginRecords") is not None:
            self.OriginRecords = []
            for item in params.get("OriginRecords"):
                obj = OriginRecord()
                obj._deserialize(item)
                self.OriginRecords.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginInfo(AbstractModel):
    """加速域名源站信息。

    """

    def __init__(self):
        r"""
        :param OriginType: 源站类型，取值有：
<li>IP_DOMAIN：IPV4、IPV6或域名类型源站；</li>
<li>COS：COS源。</li>
<li>ORIGIN_GROUP：源站组类型源站。</li>
<li>AWS_S3：AWS S3对象存储源站。</li>
        :type OriginType: str
        :param Origin: 源站地址，当OriginType参数指定为ORIGIN_GROUP时，该参数填写源站组ID，其他情况下填写源站地址。
        :type Origin: str
        :param BackupOrigin: 备用源站组ID，该参数在OriginType参数指定为ORIGIN_GROUP时生效，为空表示不使用备用源站。
        :type BackupOrigin: str
        :param PrivateAccess: 指定是否允许访问私有对象存储源站，当源站类型OriginType=COS或AWS_S3时有效，取值有：
<li>on：使用私有鉴权；</li>
<li>off：不使用私有鉴权。</li>不填写，默认值为：off。
        :type PrivateAccess: str
        :param PrivateParameters: 私有鉴权使用参数，当源站类型PrivateAccess=on时有效。
        :type PrivateParameters: list of PrivateParameter
        """
        self.OriginType = None
        self.Origin = None
        self.BackupOrigin = None
        self.PrivateAccess = None
        self.PrivateParameters = None


    def _deserialize(self, params):
        self.OriginType = params.get("OriginType")
        self.Origin = params.get("Origin")
        self.BackupOrigin = params.get("BackupOrigin")
        self.PrivateAccess = params.get("PrivateAccess")
        if params.get("PrivateParameters") is not None:
            self.PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self.PrivateParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginProtectionInfo(AbstractModel):
    """源站防护信息

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param Hosts: 域名列表。
        :type Hosts: list of str
        :param ProxyIds: 代理ID列表。
        :type ProxyIds: list of str
        :param CurrentIPWhitelist: 当前版本的IP白名单。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param NeedUpdate: 该站点是否需要更新源站白名单，取值有：
<li>true ：需要更新IP白名单 ；</li>
<li>false ：无需更新IP白名单。</li>
        :type NeedUpdate: bool
        :param Status: 源站防护状态，取值有：
<li>online ：源站防护启用中 ；</li>
<li>offline ：源站防护已停用 ；</li>
<li>nonactivate ：源站防护未激活，仅在从未使用过源站防护功能的站点调用中返回。</li>
        :type Status: str
        :param PlanSupport: 站点套餐是否支持源站防护，取值有：
<li>true ：支持 ；</li>
<li>false ：不支持。</li>
        :type PlanSupport: bool
        :param DiffIPWhitelist: 最新IP白名单与当前IP白名单的对比。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiffIPWhitelist: :class:`tencentcloud.teo.v20220901.models.DiffIPWhitelist`
        """
        self.ZoneId = None
        self.Hosts = None
        self.ProxyIds = None
        self.CurrentIPWhitelist = None
        self.NeedUpdate = None
        self.Status = None
        self.PlanSupport = None
        self.DiffIPWhitelist = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Hosts = params.get("Hosts")
        self.ProxyIds = params.get("ProxyIds")
        if params.get("CurrentIPWhitelist") is not None:
            self.CurrentIPWhitelist = IPWhitelist()
            self.CurrentIPWhitelist._deserialize(params.get("CurrentIPWhitelist"))
        self.NeedUpdate = params.get("NeedUpdate")
        self.Status = params.get("Status")
        self.PlanSupport = params.get("PlanSupport")
        if params.get("DiffIPWhitelist") is not None:
            self.DiffIPWhitelist = DiffIPWhitelist()
            self.DiffIPWhitelist._deserialize(params.get("DiffIPWhitelist"))
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
        :param Record: 源站记录值，不包含端口信息，可以为：IPv4，IPv6，域名格式。
        :type Record: str
        :param RecordId: 源站记录ID。
        :type RecordId: str
        :param Port: 源站端口，取值范围：[1-65535]。
        :type Port: int
        :param Weight: 当源站配置类型ConfigurationType=weight时，表示权重。
不配置权重信息时，所有源站组记录统一填写为0或者不填写，表示多个源站轮询回源。
配置权重信息时，取值为[1-100]，多个源站权重总和应为100，表示多个源站按照权重回源。
当源站配置类型ConfigurationType=proto时，表示权重。
不配置权重信息时，所有源站组记录统一填写为0或者不填写，表示多个源站轮询回源。
配置权重信息时，取值为[1-100]，源站组内Proto相同的多个源站权重总和应为100，表示多个源站按照权重回源。
        :type Weight: int
        :param Proto: 当源站配置类型ConfigurationType=proto时，表示源站的协议类型，将按照客户端请求协议回到相应的源站，取值有：
<li>http：HTTP协议源站；</li>
<li>https：HTTPS协议源站。</li>
        :type Proto: str
        :param Area: 当源站配置类型ConfigurationType=area时，表示区域，为空表示全部地区。取值为iso-3166中alpha-2编码或者大洲区域代码。大洲区域代码取值为：
<li>Asia：亚洲；</li>
<li>Europe：欧洲；</li>
<li>Africa：非洲；</li>
<li>Oceania：大洋洲；</li>
<li>Americas：美洲。</li>源站组记录中，至少需要有一项为全部地区。
        :type Area: list of str
        :param Private: 当源站类型OriginType=third_part时有效
是否私有鉴权，取值有：
<li>true：使用私有鉴权；</li>
<li>false：不使用私有鉴权。</li>不填写，默认值为：false。
        :type Private: bool
        :param PrivateParameters: 当源站类型Private=true时有效，表示私有鉴权使用参数。
        :type PrivateParameters: list of PrivateParameter
        """
        self.Record = None
        self.RecordId = None
        self.Port = None
        self.Weight = None
        self.Proto = None
        self.Area = None
        self.Private = None
        self.PrivateParameters = None


    def _deserialize(self, params):
        self.Record = params.get("Record")
        self.RecordId = params.get("RecordId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Proto = params.get("Proto")
        self.Area = params.get("Area")
        self.Private = params.get("Private")
        if params.get("PrivateParameters") is not None:
            self.PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self.PrivateParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartialModule(AbstractModel):
    """例外规则的详细模块配置。

    """

    def __init__(self):
        r"""
        :param Module: 模块名称，取值为：
<li>waf：托管规则。</li>
        :type Module: str
        :param Include: 模块下的需要例外的具体规则ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Include: list of int
        """
        self.Module = None
        self.Include = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Include = params.get("Include")
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
        :param Flux: 套餐所含流量，该流量数值为安全加速流量，内容加速流量和智能加速流量的总和（单位：字节）。
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
<li> sta_global ：全球内容分发网络（包括中国大陆）标准版套餐； </li>
<li> sta_global_with_bot ：全球内容分发网络（包括中国大陆）标准版套餐附带bot管理；</li>
<li> ent ：全球内容分发网络（不包括中国大陆）企业版套餐； </li>
<li> ent_with_bot ： 全球内容分发网络（不包括中国大陆）企业版套餐附带bot管理；</li>
<li> ent_cm ：中国大陆内容分发网络企业版套餐； </li>
<li> ent_cm_with_bot ：中国大陆内容分发网络企业版套餐附带bot管理；</li>
<li> ent_global ：全球内容分发网络（包括中国大陆）企业版套餐； </li>
<li> ent_global_with_bot ：全球内容分发网络（包括中国大陆）企业版套餐附带bot管理。</li>
        :type PlanType: str
        :param Price: 套餐价格（单位：分）。
        :type Price: float
        :param Request: 套餐所含请求次数，该请求次数为安全加速请求次数。（单位：次）。
        :type Request: int
        :param SiteNumber: 套餐所能绑定的站点个数。
        :type SiteNumber: int
        :param Area: 套餐加速区域类型，取值有：
<li> mainland ：中国大陆； </li>
<li> overseas ：全球（不包括中国大陆）；</li>
<li> global ：全球（包括中国大陆）。 </li>
        :type Area: str
        """
        self.Currency = None
        self.Flux = None
        self.Frequency = None
        self.PlanType = None
        self.Price = None
        self.Request = None
        self.SiteNumber = None
        self.Area = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Flux = params.get("Flux")
        self.Frequency = params.get("Frequency")
        self.PlanType = params.get("PlanType")
        self.Price = params.get("Price")
        self.Request = params.get("Request")
        self.SiteNumber = params.get("SiteNumber")
        self.Area = params.get("Area")
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
        :param Switch: 是否开启 POST 请求上传文件限制，平台默认为限制为32MB，取值有：
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
        


class PrivateParameter(AbstractModel):
    """源站记录私有鉴权参数

    """

    def __init__(self):
        r"""
        :param Name: 私有鉴权参数名称，取值有：
<li>AccessKeyId：鉴权参数Access Key ID；</li>
<li>SecretAccessKey：鉴权参数Secret Access Key。</li>
        :type Name: str
        :param Value: 私有鉴权参数值。
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
        


class QueryCondition(AbstractModel):
    """查询条件

    """

    def __init__(self):
        r"""
        :param Key: 筛选条件的key。
        :type Key: str
        :param Operator: 查询条件操作符，操作类型有：
<li>equals: 等于；</li>
<li>notEquals: 不等于；</li>
<li>include: 包含；</li>
<li>notInclude: 不包含; </li>
<li>startWith: 开始的值是value；</li>
<li>notStartWith: 不以value的值开始；</li>
<li>endWith: 结尾是value值；</li>
<li>notEndWith: 不以value的值结尾。</li>
        :type Operator: str
        :param Value: 筛选条件的值。
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
        :param Switch: 是否开启 Quic 配置，取值有：
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
        


class Quota(AbstractModel):
    """刷新/预热 可用量及配额

    """

    def __init__(self):
        r"""
        :param Batch: 单次批量提交配额上限。
        :type Batch: int
        :param Daily: 每日提交配额上限。
        :type Daily: int
        :param DailyAvailable: 每日剩余的可提交配额。
        :type DailyAvailable: int
        :param Type: 刷新预热缓存类型，取值有：
<li> purge_prefix：按前缀刷新；</li>
<li> purge_url：按URL刷新；</li>
<li> purge_host：按Hostname刷新；</li>
<li> purge_all：刷新全部缓存内容；</li>
<li> purge_cache_tag：按CacheTag刷新；</li><li> prefetch_url：按URL预热。</li>
        :type Type: str
        """
        self.Batch = None
        self.Daily = None
        self.DailyAvailable = None
        self.Type = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Daily = params.get("Daily")
        self.DailyAvailable = params.get("DailyAvailable")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitConfig(AbstractModel):
    """速率限制规则

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param RateLimitUserRules: 速率限制-用户规则列表。如果为null，默认使用历史配置。
        :type RateLimitUserRules: list of RateLimitUserRule
        :param RateLimitTemplate: 速率限制模板功能。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitTemplate: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplate`
        :param RateLimitIntelligence: 智能客户端过滤。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitIntelligence: :class:`tencentcloud.teo.v20220901.models.RateLimitIntelligence`
        :param RateLimitCustomizes: 速率限制-托管定制规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitCustomizes: list of RateLimitUserRule
        """
        self.Switch = None
        self.RateLimitUserRules = None
        self.RateLimitTemplate = None
        self.RateLimitIntelligence = None
        self.RateLimitCustomizes = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("RateLimitUserRules") is not None:
            self.RateLimitUserRules = []
            for item in params.get("RateLimitUserRules"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self.RateLimitUserRules.append(obj)
        if params.get("RateLimitTemplate") is not None:
            self.RateLimitTemplate = RateLimitTemplate()
            self.RateLimitTemplate._deserialize(params.get("RateLimitTemplate"))
        if params.get("RateLimitIntelligence") is not None:
            self.RateLimitIntelligence = RateLimitIntelligence()
            self.RateLimitIntelligence._deserialize(params.get("RateLimitIntelligence"))
        if params.get("RateLimitCustomizes") is not None:
            self.RateLimitCustomizes = []
            for item in params.get("RateLimitCustomizes"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self.RateLimitCustomizes.append(obj)
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
        :param Switch: 功能开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param Action: 执行动作，取值有：
<li>monitor：观察；</li>
<li>alg：挑战。</li>
        :type Action: str
        :param RuleId: 规则id，仅出参使用。
        :type RuleId: int
        """
        self.Switch = None
        self.Action = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        self.RuleId = params.get("RuleId")
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
        :param Mode: 模板等级名称，取值有：
<li>sup_loose：超级宽松；</li>
<li>loose：宽松；</li>
<li>emergency：紧急；</li>
<li>normal：适中；</li>
<li>strict：严格；</li>
<li>close：关闭，仅精准速率限制生效。</li>
        :type Mode: str
        :param Action: 模板处置方式，取值有：
<li>alg：JavaScript挑战；</li>
<li>monitor：观察。</li>不填写默认取alg。
        :type Action: str
        :param RateLimitTemplateDetail: 模板值详情。仅出参返回。
        :type RateLimitTemplateDetail: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplateDetail`
        """
        self.Mode = None
        self.Action = None
        self.RateLimitTemplateDetail = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Action = params.get("Action")
        if params.get("RateLimitTemplateDetail") is not None:
            self.RateLimitTemplateDetail = RateLimitTemplateDetail()
            self.RateLimitTemplateDetail._deserialize(params.get("RateLimitTemplateDetail"))
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
        :param Mode: 模板等级名称，取值有：
<li>sup_loose：超级宽松；</li>
<li>loose：宽松；</li>
<li>emergency：紧急；</li>
<li>normal：适中；</li>
<li>strict：严格；</li>
<li>close：关闭，仅精准速率限制生效。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param ID: 唯一id。
        :type ID: int
        :param Action: 模板处置方式，取值有：
<li>alg：JavaScript挑战；</li>
<li>monitor：观察。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param PunishTime: 惩罚时间，取值范围0-2天，单位秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param Threshold: 统计阈值，单位是次，取值范围0-4294967294。
        :type Threshold: int
        :param Period: 统计周期，取值范围0-120秒。
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
        :param Threshold: 速率限制统计阈值，单位是次，取值范围0-4294967294。
        :type Threshold: int
        :param Period: 速率限制统计时间，取值范围 10/20/30/40/50/60 单位是秒。
        :type Period: int
        :param RuleName: 规则名，只能以英文字符，数字，下划线组合，且不能以下划线开头。
        :type RuleName: str
        :param Action: 处置动作，取值有：
<li>monitor：观察；</li>
<li>drop：拦截；</li>
<li>alg：JavaScript挑战。</li>
        :type Action: str
        :param PunishTime: 惩罚时长，0-2天。
        :type PunishTime: int
        :param PunishTimeUnit: 处罚时长单位，取值有：
<li>second：秒；</li>
<li>minutes：分钟；</li>
<li>hour：小时。</li>
        :type PunishTimeUnit: str
        :param RuleStatus: 规则状态，取值有：
<li>on：生效；</li>
<li>off：不生效。</li>默认on生效。
        :type RuleStatus: str
        :param AclConditions: 规则详情。
        :type AclConditions: list of AclCondition
        :param RulePriority: 规则权重，取值范围0-100。
        :type RulePriority: int
        :param RuleID: 规则id。仅出参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleID: int
        :param FreqFields: 过滤词，取值有：
<li>sip：客户端ip。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreqFields: list of str
        :param UpdateTime: 更新时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FreqScope: 统计范围，字段为null时，代表source_to_eo。取值有：
<li>source_to_eo：（响应）源站到EdgeOne。</li>
<li>client_to_eo：（请求）客户端到EdgeOne；</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreqScope: list of str
        """
        self.Threshold = None
        self.Period = None
        self.RuleName = None
        self.Action = None
        self.PunishTime = None
        self.PunishTimeUnit = None
        self.RuleStatus = None
        self.AclConditions = None
        self.RulePriority = None
        self.RuleID = None
        self.FreqFields = None
        self.UpdateTime = None
        self.FreqScope = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        self.RuleName = params.get("RuleName")
        self.Action = params.get("Action")
        self.PunishTime = params.get("PunishTime")
        self.PunishTimeUnit = params.get("PunishTimeUnit")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self.AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self.AclConditions.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.RuleID = params.get("RuleID")
        self.FreqFields = params.get("FreqFields")
        self.UpdateTime = params.get("UpdateTime")
        self.FreqScope = params.get("FreqScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimAliasDomainRequest(AbstractModel):
    """ReclaimAliasDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点 ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        """
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReclaimAliasDomainResponse(AbstractModel):
    """ReclaimAliasDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReclaimZoneRequest(AbstractModel):
    """ReclaimZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ZoneName: 站点名称。
        :type ZoneName: str
        """
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
<li>global：全球。</li>
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
        


class RewriteAction(AbstractModel):
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
        


class Rule(AbstractModel):
    """规则引擎规则项，Conditions 数组内多个项的关系为 或，内层 Conditions 列表内多个项的关系为 且。

    """

    def __init__(self):
        r"""
        :param Actions: 执行的功能。
        :type Actions: list of Action
        :param Conditions: 执行功能判断条件。
注意：满足该数组内任意一项条件，功能即可执行。
        :type Conditions: list of RuleAndConditions
        :param SubRules: 嵌套规则。
        :type SubRules: list of SubRuleItem
        """
        self.Actions = None
        self.Conditions = None
        self.SubRules = None


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("SubRules") is not None:
            self.SubRules = []
            for item in params.get("SubRules"):
                obj = SubRuleItem()
                obj._deserialize(item)
                self.SubRules.append(obj)
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
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
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
<li> notequal: 不等于；</li>
<li> exist: 存在； </li>
<li> notexist: 不存在。</li>
        :type Operator: str
        :param Target: 匹配类型，取值有：
<li> filename：文件名； </li>
<li> extension：文件后缀； </li>
<li> host：HOST； </li>
<li> full_url：URL Full，当前站点下完整 URL 路径，必须包含 HTTP 协议，Host 和 路径； </li>
<li> url：URL Path，当前站点下 URL 路径的请求； </li><li>client_country：客户端国家/地区；</li>
<li> query_string：查询字符串，当前站点下请求URL的查询字符串； </li>
<li> request_header：HTTP请求头部。 </li>
        :type Target: str
        :param Values: 对应匹配类型的参数值，仅在匹配类型为查询字符串或HTTP请求头并且运算符取值为存在或不存在时允许传空数组，对应匹配类型有：
<li> 文件后缀：jpg、txt等文件后缀；</li>
<li> 文件名称：例如 foo.jpg 中的 foo；</li>
<li> 全部（站点任意请求）： all； </li>
<li> HOST：当前站点下的 host ，例如www.maxx55.com；</li>
<li> URL Path：当前站点下 URL 路径的请求，例如：/example；</li>
<li> URL Full：当前站点下完整 URL 请求，必须包含 HTTP 协议，Host 和 路径，例如：https://www.maxx55.cn/example；</li>
<li> 客户端国家/地区：符合ISO3166标准的国家/地区标识；</li>
<li> 查询字符串: 当前站点下URL请求中查询字符串的参数值，例如lang=cn&version=1中的cn和1； </li>
<li> HTTP 请求头: HTTP请求头部字段值，例如Accept-Language:zh-CN,zh;q=0.9中的zh-CN,zh;q=0.9。 </li>
        :type Values: list of str
        :param IgnoreCase: 是否忽略参数值的大小写，默认值为 false。
        :type IgnoreCase: bool
        :param Name: 对应匹配类型的参数名称，在 Target 值为以下取值时有效，有效时值不能为空：
<li> query_string（查询字符串）: 当前站点下URL请求中查询字符串的参数名称，例如lang=cn&version=1中的lang和version； </li>
<li> request_header（HTTP 请求头）: HTTP请求头部字段名，例如Accept-Language:zh-CN,zh;q=0.9中的Accept-Language。 </li>
        :type Name: str
        :param IgnoreNameCase: 是否忽略参数名称的大小写，默认值为 false。
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreNameCase: bool
        """
        self.Operator = None
        self.Target = None
        self.Values = None
        self.IgnoreCase = None
        self.Name = None
        self.IgnoreNameCase = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Target = params.get("Target")
        self.Values = params.get("Values")
        self.IgnoreCase = params.get("IgnoreCase")
        self.Name = params.get("Name")
        self.IgnoreNameCase = params.get("IgnoreNameCase")
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
        :type Choices: list of str
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
        


class RuleItem(AbstractModel):
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
        :type Rules: list of Rule
        :param RulePriority: 规则优先级, 值越大优先级越高，最小为 1。
        :type RulePriority: int
        :param Tags: 规则标签。
        :type Tags: list of str
        """
        self.RuleId = None
        self.RuleName = None
        self.Status = None
        self.Rules = None
        self.RulePriority = None
        self.Tags = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RulePriority = params.get("RulePriority")
        self.Tags = params.get("Tags")
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
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
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
        


class SecClientIp(AbstractModel):
    """客户端ip信息

    """

    def __init__(self):
        r"""
        :param ClientIp: 客户端ip。
        :type ClientIp: str
        :param RequestMaxQps: 最大qps。
        :type RequestMaxQps: int
        :param RequestNum: 请求数。
        :type RequestNum: int
        """
        self.ClientIp = None
        self.RequestMaxQps = None
        self.RequestNum = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.RequestMaxQps = params.get("RequestMaxQps")
        self.RequestNum = params.get("RequestNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntry(AbstractModel):
    """安全数据Entry返回值

    """

    def __init__(self):
        r"""
        :param Key: 查询维度值。
        :type Key: str
        :param Value: 查询维度下详细数据。
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
    """安全数据维度值信息

    """

    def __init__(self):
        r"""
        :param Metric: 指标名称。
        :type Metric: str
        :param Detail: 时序数据详情。
        :type Detail: list of TimingDataItem
        :param Max: 最大值。
        :type Max: int
        :param Avg: 平均值。
        :type Avg: float
        :param Sum: 数据总和。
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
        


class SecHitRuleInfo(AbstractModel):
    """命中规则信息

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param RuleId: 规则ID。
        :type RuleId: int
        :param RuleTypeName: 规则类型名称。
        :type RuleTypeName: str
        :param HitTime: 命中时间，采用unix秒级时间戳。
        :type HitTime: int
        :param RequestNum: 请求数。
        :type RequestNum: int
        :param Description: 规则描述。
        :type Description: str
        :param Domain: 子域名。
        :type Domain: str
        :param Action: 执行动作（处置方式），取值有：
<li>trans ：通过 ；</li>
<li>alg ：算法挑战 ；</li>
<li>drop ：丢弃 ；</li>
<li>ban ：封禁源ip ；</li>
<li>redirect ：重定向 ；</li>
<li>page ：返回指定页面 ；</li>
<li>monitor ：观察 。</li>
        :type Action: str
        :param BotLabel: Bot标签，取值有:
<li>evil_bot：恶意Bot；</li>
<li>suspect_bot：疑似Bot；</li>
<li>good_bot：正常Bot；</li>
<li>normal：正常请求；</li>
<li>none：未分类。</li>
        :type BotLabel: str
        :param RuleEnabled: 规则是否启用。
        :type RuleEnabled: bool
        :param AlarmEnabled: 规则是否启用监控告警。
        :type AlarmEnabled: bool
        :param RuleDeleted: 规则是否存在，取值有：
<li>true: 规则不存在；</li>
<li>false: 规则存在。</li>
        :type RuleDeleted: bool
        """
        self.ZoneId = None
        self.RuleId = None
        self.RuleTypeName = None
        self.HitTime = None
        self.RequestNum = None
        self.Description = None
        self.Domain = None
        self.Action = None
        self.BotLabel = None
        self.RuleEnabled = None
        self.AlarmEnabled = None
        self.RuleDeleted = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.RuleId = params.get("RuleId")
        self.RuleTypeName = params.get("RuleTypeName")
        self.HitTime = params.get("HitTime")
        self.RequestNum = params.get("RequestNum")
        self.Description = params.get("Description")
        self.Domain = params.get("Domain")
        self.Action = params.get("Action")
        self.BotLabel = params.get("BotLabel")
        self.RuleEnabled = params.get("RuleEnabled")
        self.AlarmEnabled = params.get("AlarmEnabled")
        self.RuleDeleted = params.get("RuleDeleted")
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
        :param RuleId: 规则ID。
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
        :param AttackContent: 攻击内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackContent: str
        :param RuleType: 规则类型，取值有：
<li>waf: 托管规则；</li>
<li>acl：自定义规则；</li>
<li>rate：速率限制规则；</li>
<li>bot：bot防护规则。</li>
        :type RuleType: str
        :param RuleEnabled: 规则是否开启。
        :type RuleEnabled: bool
        :param RuleDeleted: 规则是否存在，取值有：
<li>true: 规则不存在；</li>
<li>false: 规则存在。</li>
        :type RuleDeleted: bool
        :param AlarmEnabled: 规则是否启用监控告警。
        :type AlarmEnabled: bool
        """
        self.RuleId = None
        self.Action = None
        self.RiskLevel = None
        self.RuleLevel = None
        self.Description = None
        self.RuleTypeName = None
        self.AttackContent = None
        self.RuleType = None
        self.RuleEnabled = None
        self.RuleDeleted = None
        self.AlarmEnabled = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Action = params.get("Action")
        self.RiskLevel = params.get("RiskLevel")
        self.RuleLevel = params.get("RuleLevel")
        self.Description = params.get("Description")
        self.RuleTypeName = params.get("RuleTypeName")
        self.AttackContent = params.get("AttackContent")
        self.RuleType = params.get("RuleType")
        self.RuleEnabled = params.get("RuleEnabled")
        self.RuleDeleted = params.get("RuleDeleted")
        self.AlarmEnabled = params.get("AlarmEnabled")
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
        :param WafConfig: 托管规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WafConfig: :class:`tencentcloud.teo.v20220901.models.WafConfig`
        :param RateLimitConfig: 速率限制。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220901.models.RateLimitConfig`
        :param AclConfig: 自定义规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AclConfig: :class:`tencentcloud.teo.v20220901.models.AclConfig`
        :param BotConfig: Bot配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type BotConfig: :class:`tencentcloud.teo.v20220901.models.BotConfig`
        :param SwitchConfig: 七层防护总开关。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchConfig: :class:`tencentcloud.teo.v20220901.models.SwitchConfig`
        :param IpTableConfig: 基础访问管控。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTableConfig: :class:`tencentcloud.teo.v20220901.models.IpTableConfig`
        :param ExceptConfig: 例外规则配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptConfig: :class:`tencentcloud.teo.v20220901.models.ExceptConfig`
        :param DropPageConfig: 自定义拦截页面配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropPageConfig: :class:`tencentcloud.teo.v20220901.models.DropPageConfig`
        :param TemplateConfig: 模板配置。此处仅出参数使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateConfig: :class:`tencentcloud.teo.v20220901.models.TemplateConfig`
        :param SlowPostConfig: 慢速攻击配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowPostConfig: :class:`tencentcloud.teo.v20220901.models.SlowPostConfig`
        """
        self.WafConfig = None
        self.RateLimitConfig = None
        self.AclConfig = None
        self.BotConfig = None
        self.SwitchConfig = None
        self.IpTableConfig = None
        self.ExceptConfig = None
        self.DropPageConfig = None
        self.TemplateConfig = None
        self.SlowPostConfig = None


    def _deserialize(self, params):
        if params.get("WafConfig") is not None:
            self.WafConfig = WafConfig()
            self.WafConfig._deserialize(params.get("WafConfig"))
        if params.get("RateLimitConfig") is not None:
            self.RateLimitConfig = RateLimitConfig()
            self.RateLimitConfig._deserialize(params.get("RateLimitConfig"))
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
        if params.get("TemplateConfig") is not None:
            self.TemplateConfig = TemplateConfig()
            self.TemplateConfig._deserialize(params.get("TemplateConfig"))
        if params.get("SlowPostConfig") is not None:
            self.SlowPostConfig = SlowPostConfig()
            self.SlowPostConfig._deserialize(params.get("SlowPostConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityType(AbstractModel):
    """安全类型配置项。

    """

    def __init__(self):
        r"""
        :param Switch: 安全类型开关，取值为：
<li> on：开启；</li>
<li> off：关闭。</li>
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
<li>default：默认证书；</lil>
<li>upload：用户上传；</li>
<li>managed：腾讯云托管。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书部署时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param SignAlgo: 签名算法。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignAlgo: str
        :param CommonName: 证书归属域名名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        """
        self.CertId = None
        self.Alias = None
        self.Type = None
        self.ExpireTime = None
        self.DeployTime = None
        self.SignAlgo = None
        self.CommonName = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.Alias = params.get("Alias")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.SignAlgo = params.get("SignAlgo")
        self.CommonName = params.get("CommonName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleDataRecord(AbstractModel):
    """单值类数据记录

    """

    def __init__(self):
        r"""
        :param TypeKey: 查询维度值。
        :type TypeKey: str
        :param TypeValue: 查询维度下具体指标值。
        :type TypeValue: list of SingleTypeValue
        """
        self.TypeKey = None
        self.TypeValue = None


    def _deserialize(self, params):
        self.TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self.TypeValue = []
            for item in params.get("TypeValue"):
                obj = SingleTypeValue()
                obj._deserialize(item)
                self.TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleTypeValue(AbstractModel):
    """单值指标数据

    """

    def __init__(self):
        r"""
        :param MetricName: 指标名。
        :type MetricName: str
        :param DetailData: 指标值。
        :type DetailData: int
        """
        self.MetricName = None
        self.DetailData = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.DetailData = params.get("DetailData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCondition(AbstractModel):
    """例外规则的跳过匹配条件，即在例外时根据本匹配条件，略过指定字段及内容。

    """

    def __init__(self):
        r"""
        :param Type: 例外跳过类型，取值为：
<li>header_fields：HTTP请求Header；</li>
<li>cookie：HTTP请求Cookie；</li>
<li>query_string：HTTP请求URL中的Query参数；</li>
<li>uri：HTTP请求URI；</li>
<li>body_raw：HTTP请求Body；</li>
<li>body_json： JSON格式的HTTP Body。</li>
        :type Type: str
        :param Selector: 选择跳过的字段，取值为：
<li>args：uri 下选择 query 参数: ?name1=jack&age=12；</li>
<li>path：uri 下选择部分路径：/path/to/resource.jpg；</li>
<li>full：uri 下选择完整路径：example.com/path/to/resource.jpg?name1=jack&age=12；</li>
<li>upload_filename：分段文件名，即分段传输文件时；</li>
<li>keys：所有的Key；</li>
<li>values：匹配Key对应的值；</li>
<li>key_value：匹配Key及匹配Value。</li>
        :type Selector: str
        :param MatchFromType: 匹配Key所使用的匹配方式，取值为：
<li>equal：精准匹配，等于；</li>
<li>wildcard：通配符匹配，支持 * 通配。</li>
        :type MatchFromType: str
        :param MatchFrom: 匹配Key的值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchFrom: list of str
        :param MatchContentType: 匹配Content所使用的匹配方式，取值为：
<li>equal：精准匹配，等于；</li>
<li>wildcard：通配符匹配，支持 * 通配。</li>
        :type MatchContentType: str
        :param MatchContent: 匹配Value的值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchContent: list of str
        """
        self.Type = None
        self.Selector = None
        self.MatchFromType = None
        self.MatchFrom = None
        self.MatchContentType = None
        self.MatchContent = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Selector = params.get("Selector")
        self.MatchFromType = params.get("MatchFromType")
        self.MatchFrom = params.get("MatchFrom")
        self.MatchContentType = params.get("MatchContentType")
        self.MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowPostConfig(AbstractModel):
    """慢速攻击配置。

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param FirstPartConfig: 首包配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstPartConfig: :class:`tencentcloud.teo.v20220901.models.FirstPartConfig`
        :param SlowRateConfig: 基础配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowRateConfig: :class:`tencentcloud.teo.v20220901.models.SlowRateConfig`
        :param Action: 慢速攻击的处置动作，取值有：
<li>monitor：观察；</li>
<li>drop：拦截。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param RuleId: 本规则的Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        """
        self.Switch = None
        self.FirstPartConfig = None
        self.SlowRateConfig = None
        self.Action = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("FirstPartConfig") is not None:
            self.FirstPartConfig = FirstPartConfig()
            self.FirstPartConfig._deserialize(params.get("FirstPartConfig"))
        if params.get("SlowRateConfig") is not None:
            self.SlowRateConfig = SlowRateConfig()
            self.SlowRateConfig._deserialize(params.get("SlowRateConfig"))
        self.Action = params.get("Action")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowRateConfig(AbstractModel):
    """慢速攻击的基础配置。

    """

    def __init__(self):
        r"""
        :param Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param Interval: 统计的间隔，单位是秒，即在首段包传输结束后，将数据传输轴按照本参数切分，每个分片独立计算慢速攻击。
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: int
        :param Threshold: 统计时应用的速率阈值，单位是bps，即如果本分片中的传输速率没达到本参数的值，则判定为慢速攻击，应用慢速攻击的处置方式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: int
        """
        self.Switch = None
        self.Interval = None
        self.Threshold = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Interval = params.get("Interval")
        self.Threshold = params.get("Threshold")
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
        


class SpeedTestingConfig(AbstractModel):
    """站点拨测配置

    """

    def __init__(self):
        r"""
        :param TaskType: 任务类型，取值有：
<li>1：页面性能;</li>
<li>2：文件上传;</li>
<li>3：文件下载;</li>
<li>4：端口性能;</li>
<li>5：网络质量;</li>
<li>6：音视频体验。</li>
        :type TaskType: int
        :param Url: 拨测 url。
        :type Url: str
        :param UA: 拨测 UA。
        :type UA: str
        :param Connectivity: 网络类型。
        :type Connectivity: str
        """
        self.TaskType = None
        self.Url = None
        self.UA = None
        self.Connectivity = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Url = params.get("Url")
        self.UA = params.get("UA")
        self.Connectivity = params.get("Connectivity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingDetailData(AbstractModel):
    """拨测详细数据，包括各地域性能数据。

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param DistrictStatistics: 地域性能数据。
        :type DistrictStatistics: list of DistrictStatistics
        """
        self.ZoneId = None
        self.ZoneName = None
        self.DistrictStatistics = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("DistrictStatistics") is not None:
            self.DistrictStatistics = []
            for item in params.get("DistrictStatistics"):
                obj = DistrictStatistics()
                obj._deserialize(item)
                self.DistrictStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingInfo(AbstractModel):
    """拨测结果信息

    """

    def __init__(self):
        r"""
        :param StatusCode: 任务状态，取值有：
<li> 200：任务完成;</li>
<li> 100：任务进行中；</li>
<li> 503: 任务失败。</li>
        :type StatusCode: int
        :param TestId: 拨测任务 ID。
        :type TestId: str
        :param SpeedTestingConfig: 拨测任务配置。
        :type SpeedTestingConfig: :class:`tencentcloud.teo.v20220901.models.SpeedTestingConfig`
        :param SpeedTestingStatistics: 拨测任务统计结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type SpeedTestingStatistics: :class:`tencentcloud.teo.v20220901.models.SpeedTestingStatistics`
        """
        self.StatusCode = None
        self.TestId = None
        self.SpeedTestingConfig = None
        self.SpeedTestingStatistics = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.TestId = params.get("TestId")
        if params.get("SpeedTestingConfig") is not None:
            self.SpeedTestingConfig = SpeedTestingConfig()
            self.SpeedTestingConfig._deserialize(params.get("SpeedTestingConfig"))
        if params.get("SpeedTestingStatistics") is not None:
            self.SpeedTestingStatistics = SpeedTestingStatistics()
            self.SpeedTestingStatistics._deserialize(params.get("SpeedTestingStatistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingMetricData(AbstractModel):
    """不同维度的测速数据。

    """

    def __init__(self):
        r"""
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param OriginSpeedTestingInfo: 源站拨测信息。
        :type OriginSpeedTestingInfo: list of SpeedTestingInfo
        :param ProxySpeedTestingInfo: EO 拨测信息。
        :type ProxySpeedTestingInfo: list of SpeedTestingInfo
        :param SpeedTestingStatus: 站点状态。
        :type SpeedTestingStatus: :class:`tencentcloud.teo.v20220901.models.SpeedTestingStatus`
        :param OptimizeAction: 优化建议。
        :type OptimizeAction: list of OptimizeAction
        :param ProxyLoadTime: EO 整体性能，单位ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyLoadTime: int
        :param OriginLoadTime: 源站整体性能，单位ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginLoadTime: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.OriginSpeedTestingInfo = None
        self.ProxySpeedTestingInfo = None
        self.SpeedTestingStatus = None
        self.OptimizeAction = None
        self.ProxyLoadTime = None
        self.OriginLoadTime = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("OriginSpeedTestingInfo") is not None:
            self.OriginSpeedTestingInfo = []
            for item in params.get("OriginSpeedTestingInfo"):
                obj = SpeedTestingInfo()
                obj._deserialize(item)
                self.OriginSpeedTestingInfo.append(obj)
        if params.get("ProxySpeedTestingInfo") is not None:
            self.ProxySpeedTestingInfo = []
            for item in params.get("ProxySpeedTestingInfo"):
                obj = SpeedTestingInfo()
                obj._deserialize(item)
                self.ProxySpeedTestingInfo.append(obj)
        if params.get("SpeedTestingStatus") is not None:
            self.SpeedTestingStatus = SpeedTestingStatus()
            self.SpeedTestingStatus._deserialize(params.get("SpeedTestingStatus"))
        if params.get("OptimizeAction") is not None:
            self.OptimizeAction = []
            for item in params.get("OptimizeAction"):
                obj = OptimizeAction()
                obj._deserialize(item)
                self.OptimizeAction.append(obj)
        self.ProxyLoadTime = params.get("ProxyLoadTime")
        self.OriginLoadTime = params.get("OriginLoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingQuota(AbstractModel):
    """拨测配额数据。

    """

    def __init__(self):
        r"""
        :param TotalTestRuns: 站点总拨测次数。
        :type TotalTestRuns: int
        :param AvailableTestRuns: 站点剩余可用拨测次数。
        :type AvailableTestRuns: int
        """
        self.TotalTestRuns = None
        self.AvailableTestRuns = None


    def _deserialize(self, params):
        self.TotalTestRuns = params.get("TotalTestRuns")
        self.AvailableTestRuns = params.get("AvailableTestRuns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingStatistics(AbstractModel):
    """拨测统计结果

    """

    def __init__(self):
        r"""
        :param FirstContentfulPaint: 首屏时间，单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstContentfulPaint: int
        :param FirstMeaningfulPaint: 首屏完全渲染时间，单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstMeaningfulPaint: int
        :param OverallDownloadSpeed: 整体下载速度，单位 KB/s。
注意：此字段可能返回 null，表示取不到有效值。
        :type OverallDownloadSpeed: float
        :param RenderTime: 渲染时间，单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenderTime: int
        :param DocumentFinishTime: 文档完成时间, 单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentFinishTime: int
        :param TcpConnectionTime: 基础文档TCP连接时间，单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type TcpConnectionTime: int
        :param ResponseTime: 基础文档服务器响应时间，单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTime: int
        :param FileDownloadTime: 基础文档下载时间，单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileDownloadTime: int
        :param LoadTime: 整体性能，测试总时间，单位 ms。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadTime: int
        """
        self.FirstContentfulPaint = None
        self.FirstMeaningfulPaint = None
        self.OverallDownloadSpeed = None
        self.RenderTime = None
        self.DocumentFinishTime = None
        self.TcpConnectionTime = None
        self.ResponseTime = None
        self.FileDownloadTime = None
        self.LoadTime = None


    def _deserialize(self, params):
        self.FirstContentfulPaint = params.get("FirstContentfulPaint")
        self.FirstMeaningfulPaint = params.get("FirstMeaningfulPaint")
        self.OverallDownloadSpeed = params.get("OverallDownloadSpeed")
        self.RenderTime = params.get("RenderTime")
        self.DocumentFinishTime = params.get("DocumentFinishTime")
        self.TcpConnectionTime = params.get("TcpConnectionTime")
        self.ResponseTime = params.get("ResponseTime")
        self.FileDownloadTime = params.get("FileDownloadTime")
        self.LoadTime = params.get("LoadTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedTestingStatus(AbstractModel):
    """拨测任务状态信息

    """

    def __init__(self):
        r"""
        :param Url: 拨测 url。
        :type Url: str
        :param Tls: 拨测 url 是否使用 https。
        :type Tls: bool
        :param CreatedOn: 任务创建时间。
        :type CreatedOn: str
        :param StatusCode: 任务状态，取值有：
<li> 200：任务完成;</li>
<li> 100：任务进行中。</li>
<li> 503: 任务失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCode: int
        :param UA: 拨测 UA。
注意：此字段可能返回 null，表示取不到有效值。
        :type UA: str
        :param Connectivity: 网络环境。
注意：此字段可能返回 null，表示取不到有效值。
        :type Connectivity: str
        :param Reachable: 是否可达，取值：
<li> true：可达；</li>
<li> false：不可达。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Reachable: bool
        :param TimedOut: 是否超时，取值：
<li> true：超时；</li>
<li> false：不超时。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimedOut: bool
        """
        self.Url = None
        self.Tls = None
        self.CreatedOn = None
        self.StatusCode = None
        self.UA = None
        self.Connectivity = None
        self.Reachable = None
        self.TimedOut = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Tls = params.get("Tls")
        self.CreatedOn = params.get("CreatedOn")
        self.StatusCode = params.get("StatusCode")
        self.UA = params.get("UA")
        self.Connectivity = params.get("Connectivity")
        self.Reachable = params.get("Reachable")
        self.TimedOut = params.get("TimedOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRule(AbstractModel):
    """嵌套规则信息。

    """

    def __init__(self):
        r"""
        :param Conditions: 执行功能判断条件。
注意：满足该数组内任意一项条件，功能即可执行。
        :type Conditions: list of RuleAndConditions
        :param Actions: 执行的功能。
        :type Actions: list of Action
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
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRuleItem(AbstractModel):
    """规则引擎嵌套规则

    """

    def __init__(self):
        r"""
        :param Rules: 嵌套规则信息。
        :type Rules: list of SubRule
        :param Tags: 规则标签。
        :type Tags: list of str
        """
        self.Rules = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = SubRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Tags = params.get("Tags")
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
        :param WebSwitch: Web类型的安全总开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>不影响DDoS与Bot的开关。
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
        :param TagKey: 标签键。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值。
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
        :param JobId: 任务 ID。
        :type JobId: str
        :param Status: 状态。
        :type Status: str
        :param Target: 资源。
        :type Target: str
        :param Type: 任务类型。
        :type Type: str
        :param CreateTime: 任务创建时间。
        :type CreateTime: str
        :param UpdateTime: 任务完成时间。
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
        


class TemplateConfig(AbstractModel):
    """安全模板配置

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID。
        :type TemplateId: str
        :param TemplateName: 模板名称。
        :type TemplateName: str
        """
        self.TemplateId = None
        self.TemplateName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
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
        :param Timestamp: 返回数据对应时间点，采用unix秒级时间戳。
        :type Timestamp: int
        :param Value: 具体数值。
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
    """时序数据信息

    """

    def __init__(self):
        r"""
        :param TypeKey: 查询维度值。
        :type TypeKey: str
        :param TypeValue: 详细时序数据。
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
        :param Sum: 数据和。
        :type Sum: int
        :param Max: 最大值。
        :type Max: int
        :param Avg: 平均值。
        :type Avg: int
        :param MetricName: 指标名。
        :type MetricName: str
        :param Detail: 详细数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of TimingDataItem
        """
        self.Sum = None
        self.Max = None
        self.Avg = None
        self.MetricName = None
        self.Detail = None


    def _deserialize(self, params):
        self.Sum = params.get("Sum")
        self.Max = params.get("Max")
        self.Avg = params.get("Avg")
        self.MetricName = params.get("MetricName")
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
    """Top类数据记录

    """

    def __init__(self):
        r"""
        :param TypeKey: 查询维度值。
        :type TypeKey: str
        :param DetailData: top数据排行。
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
    """Top数据的详细信息

    """

    def __init__(self):
        r"""
        :param Key: 字段名。
        :type Key: str
        :param Value: 字段值。
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
        


class TopEntry(AbstractModel):
    """TopN的Entry数据

    """

    def __init__(self):
        r"""
        :param Key: top查询维度值。
        :type Key: str
        :param Value: 查询具体数据。
        :type Value: list of TopEntryValue
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = TopEntryValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopEntryValue(AbstractModel):
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
        


class UpdateOriginProtectionIPWhitelistRequest(AbstractModel):
    """UpdateOriginProtectionIPWhitelist请求参数结构体

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
        


class UpdateOriginProtectionIPWhitelistResponse(AbstractModel):
    """UpdateOriginProtectionIPWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpstreamHttp2(AbstractModel):
    """Http2回源配置

    """

    def __init__(self):
        r"""
        :param Switch: http2 回源配置开关，取值有：
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
        :param Switch: 自定义 ns 开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param Servers: 自定义 ns 列表。
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
        :param Name: 自定义名字服务器名称。
        :type Name: str
        :param IPv4: 自定义名字服务器 IPv4 地址。
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
        


class Waf(AbstractModel):
    """无

    """

    def __init__(self):
        r"""
        :param Switch: Waf开关，取值为：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param PolicyId: 策略ID。
        :type PolicyId: int
        """
        self.Switch = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.PolicyId = params.get("PolicyId")
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
        :param Level: 上一次设置的防护级别，取值有：
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
        :param WafRule: 托管规则详细配置。如果为null，默认使用历史配置。
        :type WafRule: :class:`tencentcloud.teo.v20220901.models.WafRule`
        :param AiRule: AI规则引擎防护配置。如果为null，默认使用历史配置。
        :type AiRule: :class:`tencentcloud.teo.v20220901.models.AiRule`
        """
        self.Switch = None
        self.Level = None
        self.Mode = None
        self.WafRule = None
        self.AiRule = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Level = params.get("Level")
        self.Mode = params.get("Mode")
        if params.get("WafRule") is not None:
            self.WafRule = WafRule()
            self.WafRule._deserialize(params.get("WafRule"))
        if params.get("AiRule") is not None:
            self.AiRule = AiRule()
            self.AiRule._deserialize(params.get("AiRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafGroup(AbstractModel):
    """Waf托管规则组

    """

    def __init__(self):
        r"""
        :param Action: 执行动作，取值有：
<li> block：阻断；</li>
<li> observe：观察。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param Level: 防护级别，取值有：
<li> loose：宽松；</li>
<li> normal：正常；</li>
<li> strict：严格；</li>
<li> stricter：超严格；</li>
<li> custom：自定义。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: str
        :param TypeId: 规则类型id。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeId: int
        """
        self.Action = None
        self.Level = None
        self.TypeId = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Level = params.get("Level")
        self.TypeId = params.get("TypeId")
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
        :param Switch: 托管规则开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param BlockRuleIDs: 黑名单ID列表，将规则ID加入本参数列表中代表该ID关闭，即该规则ID不再生效。
        :type BlockRuleIDs: list of int
        :param ObserveRuleIDs: 观察模式ID列表，将规则ID加入本参数列表中代表该ID使用观察模式生效，即该规则ID进入观察模式。
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
        


class WebLogs(AbstractModel):
    """web攻击日志

    """

    def __init__(self):
        r"""
        :param EventId: 请求（事件）ID。
        :type EventId: str
        :param HttpLog: http 日志内容。
        :type HttpLog: str
        :param Domain: 受攻击子域名。
        :type Domain: str
        :param AttackIp: 攻击源（客户端）Ip。
        :type AttackIp: str
        :param SipCountryCode: IP所在国家iso-3166中alpha-2编码，编码信息请参考[ISO-3166](https://git.woa.com/edgeone/iso-3166/blob/master/all/all.json)
        :type SipCountryCode: str
        :param RealClientIp: 真实客户端Ip。
        :type RealClientIp: str
        :param RealClientIpCountryCode: 真实客户端Ip所在国家iso-3166中alpha-2编码。
        :type RealClientIpCountryCode: str
        :param AttackTime: 攻击时间，采用unix秒级时间戳。
        :type AttackTime: int
        :param RequestUri: 请求地址。
        :type RequestUri: str
        :param ReqMethod: 请求类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReqMethod: str
        :param RuleDetailList: 规则相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleDetailList: list of SecRuleRelatedInfo
        :param AttackContent: 攻击内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackContent: str
        :param Area: 日志所属区域。
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        """
        self.EventId = None
        self.HttpLog = None
        self.Domain = None
        self.AttackIp = None
        self.SipCountryCode = None
        self.RealClientIp = None
        self.RealClientIpCountryCode = None
        self.AttackTime = None
        self.RequestUri = None
        self.ReqMethod = None
        self.RuleDetailList = None
        self.AttackContent = None
        self.Area = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.HttpLog = params.get("HttpLog")
        self.Domain = params.get("Domain")
        self.AttackIp = params.get("AttackIp")
        self.SipCountryCode = params.get("SipCountryCode")
        self.RealClientIp = params.get("RealClientIp")
        self.RealClientIpCountryCode = params.get("RealClientIpCountryCode")
        self.AttackTime = params.get("AttackTime")
        self.RequestUri = params.get("RequestUri")
        self.ReqMethod = params.get("ReqMethod")
        if params.get("RuleDetailList") is not None:
            self.RuleDetailList = []
            for item in params.get("RuleDetailList"):
                obj = SecRuleRelatedInfo()
                obj._deserialize(item)
                self.RuleDetailList.append(obj)
        self.AttackContent = params.get("AttackContent")
        self.Area = params.get("Area")
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
        :param ZoneId: 站点ID。
        :type ZoneId: str
        :param ZoneName: 站点名称。
        :type ZoneName: str
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
        :param CnameSpeedUp: 是否开启 CNAME 加速，取值有：
<li> enabled：开启；</li>
<li> disabled：关闭。</li>
        :type CnameSpeedUp: str
        :param CnameStatus: CNAME 接入状态，取值有：
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
        :param Area: 站点接入地域，取值有：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>
        :type Area: str
        :param VanityNameServers: 用户自定义 NS 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param VanityNameServersIps: 用户自定义 NS IP 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServersIps: list of VanityNameServersIps
        :param ActiveStatus: 展示状态，取值有：
<li> active：已启用；</li>
<li> inactive：未生效；</li>
<li> paused：已停用。</li>
        :type ActiveStatus: str
        :param AliasZoneName: 站点别名。数字、英文、-和_组合，限制20个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasZoneName: str
        :param IsFake: 是否伪站点，取值有：
<li> 0：非伪站点；</li>
<li> 1：伪站点。</li>
        :type IsFake: int
        :param LockStatus: 锁定状态，取值有：<li> enable：正常，允许进行修改操作；</li><li> disable：锁定中，不允许进行修改操作。</li>
        :type LockStatus: str
        """
        self.ZoneId = None
        self.ZoneName = None
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
        self.VanityNameServers = None
        self.VanityNameServersIps = None
        self.ActiveStatus = None
        self.AliasZoneName = None
        self.IsFake = None
        self.LockStatus = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
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
        if params.get("VanityNameServers") is not None:
            self.VanityNameServers = VanityNameServers()
            self.VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self.VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self.VanityNameServersIps.append(obj)
        self.ActiveStatus = params.get("ActiveStatus")
        self.AliasZoneName = params.get("AliasZoneName")
        self.IsFake = params.get("IsFake")
        self.LockStatus = params.get("LockStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSetting(AbstractModel):
    """站点配置。

    """

    def __init__(self):
        r"""
        :param ZoneName: 站点名称。
        :type ZoneName: str
        :param Area: 站点加速区域信息，取值有：
<li> mainland：中国境内加速；</li>
<li> overseas：中国境外加速。</li>
        :type Area: str
        :param CacheKey: 节点缓存键配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param Quic: Quic访问配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param PostMaxSize: POST请求传输配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param UpstreamHttp2: Http2回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param ForceRedirect: 访问协议强制Https跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param CacheConfig: 缓存过期时间配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param SmartRouting: 智能加速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param MaxAge: 浏览器缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param OfflineCache: 离线缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param WebSocket: WebSocket配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param ClientIpHeader: 客户端IP回源请求头配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param CachePrefresh: 缓存预刷新配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param Ipv6: Ipv6访问配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param Https: Https 加速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param ClientIpCountry: 回源时是否携带客户端IP所属地域信息的配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        :param Grpc: Grpc协议支持配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Grpc: :class:`tencentcloud.teo.v20220901.models.Grpc`
        :param ImageOptimize: 图片优化相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageOptimize: :class:`tencentcloud.teo.v20220901.models.ImageOptimize`
        :param AccelerateMainland: 中国大陆加速优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self.ZoneName = None
        self.Area = None
        self.CacheKey = None
        self.Quic = None
        self.PostMaxSize = None
        self.Compression = None
        self.UpstreamHttp2 = None
        self.ForceRedirect = None
        self.CacheConfig = None
        self.Origin = None
        self.SmartRouting = None
        self.MaxAge = None
        self.OfflineCache = None
        self.WebSocket = None
        self.ClientIpHeader = None
        self.CachePrefresh = None
        self.Ipv6 = None
        self.Https = None
        self.ClientIpCountry = None
        self.Grpc = None
        self.ImageOptimize = None
        self.AccelerateMainland = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.Area = params.get("Area")
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
        if params.get("CacheConfig") is not None:
            self.CacheConfig = CacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
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
            self.ClientIpHeader = ClientIpHeader()
            self.ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self.CachePrefresh = CachePrefresh()
            self.CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ClientIpCountry") is not None:
            self.ClientIpCountry = ClientIpCountry()
            self.ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        if params.get("Grpc") is not None:
            self.Grpc = Grpc()
            self.Grpc._deserialize(params.get("Grpc"))
        if params.get("ImageOptimize") is not None:
            self.ImageOptimize = ImageOptimize()
            self.ImageOptimize._deserialize(params.get("ImageOptimize"))
        if params.get("AccelerateMainland") is not None:
            self.AccelerateMainland = AccelerateMainland()
            self.AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        