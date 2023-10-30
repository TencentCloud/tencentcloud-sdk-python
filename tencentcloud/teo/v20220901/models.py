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
        :param _Switch: 是否开启中国大陆加速优化配置，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccelerateType(AbstractModel):
    """加速类型

    """

    def __init__(self):
        r"""
        :param _Switch: 加速开关。取值范围：
<li> on：打开;</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccelerationDomain(AbstractModel):
    """加速域名

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _DomainName: 加速域名名称。
        :type DomainName: str
        :param _DomainStatus: 加速域名状态，取值有：
<li>online：已生效；</li>
<li>process：部署中；</li>
<li>offline：已停用；</li>
<li>forbidden：已封禁；</li>
<li>init：未生效，待激活站点；</li>
        :type DomainStatus: str
        :param _OriginDetail: 源站信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginDetail: :class:`tencentcloud.teo.v20220901.models.OriginDetail`
        :param _OriginProtocol: 回源协议，取值有：
<li>FOLLOW: 协议跟随；</li>
<li>HTTP: HTTP协议回源；</li>
<li>HTTPS: HTTPS协议回源。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginProtocol: str
        :param _HttpOriginPort: HTTP回源端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpOriginPort: int
        :param _HttpsOriginPort: HTTPS回源端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpsOriginPort: int
        :param _IPv6Status: IPv6状态，取值有：
<li>follow：遵循站点IPv6配置；</li>
<li>on：开启状态；</li>
<li>off：关闭状态。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Status: str
        :param _Cname: CNAME 地址。
        :type Cname: str
        :param _IdentificationStatus: 加速域名归属权验证状态，取值有： <li>pending：待验证；</li> <li>finished：已完成验证。</li>	
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentificationStatus: str
        :param _CreatedOn: 创建时间。
        :type CreatedOn: str
        :param _ModifiedOn: 修改时间。
        :type ModifiedOn: str
        :param _OwnershipVerification: 当域名需要进行归属权验证才能继续提供服务时，该对象会携带对应验证方式所需要的信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        :param _Certificate: 域名证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.teo.v20220901.models.AccelerationDomainCertificate`
        """
        self._ZoneId = None
        self._DomainName = None
        self._DomainStatus = None
        self._OriginDetail = None
        self._OriginProtocol = None
        self._HttpOriginPort = None
        self._HttpsOriginPort = None
        self._IPv6Status = None
        self._Cname = None
        self._IdentificationStatus = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._OwnershipVerification = None
        self._Certificate = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DomainStatus(self):
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus

    @property
    def OriginDetail(self):
        return self._OriginDetail

    @OriginDetail.setter
    def OriginDetail(self, OriginDetail):
        self._OriginDetail = OriginDetail

    @property
    def OriginProtocol(self):
        return self._OriginProtocol

    @OriginProtocol.setter
    def OriginProtocol(self, OriginProtocol):
        self._OriginProtocol = OriginProtocol

    @property
    def HttpOriginPort(self):
        return self._HttpOriginPort

    @HttpOriginPort.setter
    def HttpOriginPort(self, HttpOriginPort):
        self._HttpOriginPort = HttpOriginPort

    @property
    def HttpsOriginPort(self):
        return self._HttpsOriginPort

    @HttpsOriginPort.setter
    def HttpsOriginPort(self, HttpsOriginPort):
        self._HttpsOriginPort = HttpsOriginPort

    @property
    def IPv6Status(self):
        return self._IPv6Status

    @IPv6Status.setter
    def IPv6Status(self, IPv6Status):
        self._IPv6Status = IPv6Status

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def IdentificationStatus(self):
        return self._IdentificationStatus

    @IdentificationStatus.setter
    def IdentificationStatus(self, IdentificationStatus):
        self._IdentificationStatus = IdentificationStatus

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainName = params.get("DomainName")
        self._DomainStatus = params.get("DomainStatus")
        if params.get("OriginDetail") is not None:
            self._OriginDetail = OriginDetail()
            self._OriginDetail._deserialize(params.get("OriginDetail"))
        self._OriginProtocol = params.get("OriginProtocol")
        self._HttpOriginPort = params.get("HttpOriginPort")
        self._HttpsOriginPort = params.get("HttpsOriginPort")
        self._IPv6Status = params.get("IPv6Status")
        self._Cname = params.get("Cname")
        self._IdentificationStatus = params.get("IdentificationStatus")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        if params.get("Certificate") is not None:
            self._Certificate = AccelerationDomainCertificate()
            self._Certificate._deserialize(params.get("Certificate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccelerationDomainCertificate(AbstractModel):
    """加速域名所对应的证书信息。

    """

    def __init__(self):
        r"""
        :param _Mode: 配置证书的模式，取值有： <li>disable：不配置证书；</li> <li>eofreecert：配置 EdgeOne 免费证书；</li> <li>sslcert：配置 SSL 证书。</li>
        :type Mode: str
        :param _List: 证书列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of CertificateInfo
        """
        self._Mode = None
        self._List = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = CertificateInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclCondition(AbstractModel):
    """精准防护条件

    """

    def __init__(self):
        r"""
        :param _MatchFrom: 匹配字段，取值有：
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
<li>header_seq：请求头顺序，仅bot自定义规则可用；</li>
<li>hdr：请求正文，仅Web防护自定义规则可用。</li>
        :type MatchFrom: str
        :param _MatchParam: 匹配字符串。当 MatchFrom 为 header 时，可以填入 header 的 key 作为参数。
        :type MatchParam: str
        :param _Operator: 匹配关系，取值有：
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
        :param _MatchContent: 匹配内容。
        :type MatchContent: str
        """
        self._MatchFrom = None
        self._MatchParam = None
        self._Operator = None
        self._MatchContent = None

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchParam(self):
        return self._MatchParam

    @MatchParam.setter
    def MatchParam(self, MatchParam):
        self._MatchParam = MatchParam

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._MatchFrom = params.get("MatchFrom")
        self._MatchParam = params.get("MatchParam")
        self._Operator = params.get("Operator")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclConfig(AbstractModel):
    """ACL配置

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param _AclUserRules: 用户自定义规则。
        :type AclUserRules: list of AclUserRule
        :param _Customizes: 托管定制规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Customizes: list of AclUserRule
        """
        self._Switch = None
        self._AclUserRules = None
        self._Customizes = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AclUserRules(self):
        return self._AclUserRules

    @AclUserRules.setter
    def AclUserRules(self, AclUserRules):
        self._AclUserRules = AclUserRules

    @property
    def Customizes(self):
        return self._Customizes

    @Customizes.setter
    def Customizes(self, Customizes):
        self._Customizes = Customizes


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("AclUserRules") is not None:
            self._AclUserRules = []
            for item in params.get("AclUserRules"):
                obj = AclUserRule()
                obj._deserialize(item)
                self._AclUserRules.append(obj)
        if params.get("Customizes") is not None:
            self._Customizes = []
            for item in params.get("Customizes"):
                obj = AclUserRule()
                obj._deserialize(item)
                self._Customizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclUserRule(AbstractModel):
    """用户自定义规则

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名。
        :type RuleName: str
        :param _Action: 处罚动作，取值有：
<li>trans：放行；</li>
<li>drop：拦截；</li>
<li>monitor：观察；</li>
<li>ban：IP 封禁；</li>
<li>redirect：重定向；</li>
<li>page：指定页面；</li>
<li>alg：JavaScript 挑战。</li>
        :type Action: str
        :param _RuleStatus: 规则状态，取值有：
<li>on：生效；</li>
<li>off：失效。</li>
        :type RuleStatus: str
        :param _AclConditions: 自定义规则。
        :type AclConditions: list of AclCondition
        :param _RulePriority: 规则优先级，取值范围0-100。
        :type RulePriority: int
        :param _RuleID: 规则 Id。仅出参使用。
        :type RuleID: int
        :param _UpdateTime: 更新时间。仅出参使用。
        :type UpdateTime: str
        :param _PunishTime: ip 封禁的惩罚时间。Action 是 ban 时必填，且不能为空，取值范围0-2天。
        :type PunishTime: int
        :param _PunishTimeUnit: ip 封禁的惩罚时间单位，取值有：
<li>second：秒；</li>
<li>minutes：分；</li>
<li>hour：小时。</li>默认为 second。
        :type PunishTimeUnit: str
        :param _Name: 自定义返回页面的名称。Action 是 page 时必填，且不能为空。	
        :type Name: str
        :param _PageId: 自定义返回页面的实例 Id。默认为0，代表使用系统默认拦截页面。该参数已废弃。
        :type PageId: int
        :param _CustomResponseId: 自定义响应 Id。该 Id 可通过查询自定义错误页列表接口获取。默认值为default，使用系统默认页面。Action 是 page 时必填，且不能为空。	
        :type CustomResponseId: str
        :param _ResponseCode: 自定义返回页面的响应码。Action 是 page 时必填，且不能为空，取值: 100~600，不支持 3xx 响应码。默认值：567。
        :type ResponseCode: int
        :param _RedirectUrl: 重定向时候的地址。Action 是 redirect 时必填，且不能为空。	
        :type RedirectUrl: str
        """
        self._RuleName = None
        self._Action = None
        self._RuleStatus = None
        self._AclConditions = None
        self._RulePriority = None
        self._RuleID = None
        self._UpdateTime = None
        self._PunishTime = None
        self._PunishTimeUnit = None
        self._Name = None
        self._PageId = None
        self._CustomResponseId = None
        self._ResponseCode = None
        self._RedirectUrl = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def AclConditions(self):
        return self._AclConditions

    @AclConditions.setter
    def AclConditions(self, AclConditions):
        self._AclConditions = AclConditions

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def PunishTime(self):
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def PunishTimeUnit(self):
        return self._PunishTimeUnit

    @PunishTimeUnit.setter
    def PunishTimeUnit(self, PunishTimeUnit):
        self._PunishTimeUnit = PunishTimeUnit

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId

    @property
    def ResponseCode(self):
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self._AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AclConditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        self._PunishTime = params.get("PunishTime")
        self._PunishTimeUnit = params.get("PunishTimeUnit")
        self._Name = params.get("Name")
        self._PageId = params.get("PageId")
        self._CustomResponseId = params.get("CustomResponseId")
        self._ResponseCode = params.get("ResponseCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Action(AbstractModel):
    """规则引擎功能项操作，对于一种功能只对应下面三种类型的其中一种，RuleAction 数组中的每一项只能是其中一个类型，更多功能项的填写规范可调用接口 [查询规则引擎的设置参数](https://cloud.tencent.com/document/product/1552/80618) 查看。

    """

    def __init__(self):
        r"""
        :param _NormalAction: 常规功能操作，选择该类型的功能项有：
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
        :param _RewriteAction: 带有请求头/响应头的功能操作，选择该类型的功能项有：
<li> 修改 HTTP 请求头（RequestHeader）；</li>
<li> 修改HTTP响应头（ResponseHeader）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type RewriteAction: :class:`tencentcloud.teo.v20220901.models.RewriteAction`
        :param _CodeAction: 带有状态码的功能操作，选择该类型的功能项有：
<li> 自定义错误页面（ErrorPage）；</li>
<li> 状态码缓存 TTL（StatusCodeCache）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeAction: :class:`tencentcloud.teo.v20220901.models.CodeAction`
        """
        self._NormalAction = None
        self._RewriteAction = None
        self._CodeAction = None

    @property
    def NormalAction(self):
        return self._NormalAction

    @NormalAction.setter
    def NormalAction(self, NormalAction):
        self._NormalAction = NormalAction

    @property
    def RewriteAction(self):
        return self._RewriteAction

    @RewriteAction.setter
    def RewriteAction(self, RewriteAction):
        self._RewriteAction = RewriteAction

    @property
    def CodeAction(self):
        return self._CodeAction

    @CodeAction.setter
    def CodeAction(self, CodeAction):
        self._CodeAction = CodeAction


    def _deserialize(self, params):
        if params.get("NormalAction") is not None:
            self._NormalAction = NormalAction()
            self._NormalAction._deserialize(params.get("NormalAction"))
        if params.get("RewriteAction") is not None:
            self._RewriteAction = RewriteAction()
            self._RewriteAction._deserialize(params.get("RewriteAction"))
        if params.get("CodeAction") is not None:
            self._CodeAction = CodeAction()
            self._CodeAction._deserialize(params.get("CodeAction"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedFilter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询，支持模糊查询。例如过滤ID、名称、状态等。
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        :param _Fuzzy: 是否启用模糊查询。
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Fuzzy = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Fuzzy(self):
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRule(AbstractModel):
    """AI规则引擎防护

    """

    def __init__(self):
        r"""
        :param _Mode: AI规则引擎状态，取值有：
<li> smart_status_close：关闭；</li>
<li> smart_status_open：拦截处置；</li>
<li> smart_status_observe：观察处置。</li>
        :type Mode: str
        """
        self._Mode = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectJS(AbstractModel):
    """Bot主动特征识别客户端行为校验。

    """

    def __init__(self):
        r"""
        :param _Name: 操作名称。
        :type Name: str
        :param _WorkLevel: 工作量证明 (proof_Of-Work)校验强度，默认low，取值有：
<li>low：低；</li>
<li>middle：中；</li>
<li>high：高。</li>
        :type WorkLevel: str
        :param _ExecuteMode: 执行方式，js延迟执行的时间。单位为ms，默认500，取值：0～1000。
        :type ExecuteMode: int
        :param _InvalidStatTime: 客户端末启用JS（末完成检测）统计周期。单位为秒，默认10，取值：5～3600。
        :type InvalidStatTime: int
        :param _InvalidThreshold: 客户端末启用JS（末完成检测）触发阈值。单位为次，默认300，取值：1～100000000。
        :type InvalidThreshold: int
        :param _AlgDetectResults: Bot主动特征识别客户端行为校验结果。
        :type AlgDetectResults: list of AlgDetectResult
        """
        self._Name = None
        self._WorkLevel = None
        self._ExecuteMode = None
        self._InvalidStatTime = None
        self._InvalidThreshold = None
        self._AlgDetectResults = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def WorkLevel(self):
        return self._WorkLevel

    @WorkLevel.setter
    def WorkLevel(self, WorkLevel):
        self._WorkLevel = WorkLevel

    @property
    def ExecuteMode(self):
        return self._ExecuteMode

    @ExecuteMode.setter
    def ExecuteMode(self, ExecuteMode):
        self._ExecuteMode = ExecuteMode

    @property
    def InvalidStatTime(self):
        return self._InvalidStatTime

    @InvalidStatTime.setter
    def InvalidStatTime(self, InvalidStatTime):
        self._InvalidStatTime = InvalidStatTime

    @property
    def InvalidThreshold(self):
        return self._InvalidThreshold

    @InvalidThreshold.setter
    def InvalidThreshold(self, InvalidThreshold):
        self._InvalidThreshold = InvalidThreshold

    @property
    def AlgDetectResults(self):
        return self._AlgDetectResults

    @AlgDetectResults.setter
    def AlgDetectResults(self, AlgDetectResults):
        self._AlgDetectResults = AlgDetectResults


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._WorkLevel = params.get("WorkLevel")
        self._ExecuteMode = params.get("ExecuteMode")
        self._InvalidStatTime = params.get("InvalidStatTime")
        self._InvalidThreshold = params.get("InvalidThreshold")
        if params.get("AlgDetectResults") is not None:
            self._AlgDetectResults = []
            for item in params.get("AlgDetectResults"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self._AlgDetectResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectResult(AbstractModel):
    """Bot主动特征识别校验结果。

    """

    def __init__(self):
        r"""
        :param _Result: 校验结果，取值有：
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
        :param _Action: 处罚动作，取值有：
<li>drop：拦截；</li>
<li>monitor：观察；</li>
<li>silence：静默；</li>
<li>shortdelay：（短时间）等待后响应；</li>
<li>longdelay：（长时间）等待后响应。</li>
        :type Action: str
        """
        self._Result = None
        self._Action = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectRule(AbstractModel):
    """Bot主动特征识别规则。

    """

    def __init__(self):
        r"""
        :param _RuleID: 规则id。
        :type RuleID: int
        :param _RuleName: 规则名。
        :type RuleName: str
        :param _Switch: 规则开关。
        :type Switch: str
        :param _AlgConditions: 自定义规则。
        :type AlgConditions: list of AclCondition
        :param _AlgDetectSession: Cookie校验和会话行为分析。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgDetectSession: :class:`tencentcloud.teo.v20220901.models.AlgDetectSession`
        :param _AlgDetectJS: 客户端行为校验。
        :type AlgDetectJS: list of AlgDetectJS
        :param _UpdateTime: 更新时间。仅出参使用。
        :type UpdateTime: str
        """
        self._RuleID = None
        self._RuleName = None
        self._Switch = None
        self._AlgConditions = None
        self._AlgDetectSession = None
        self._AlgDetectJS = None
        self._UpdateTime = None

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AlgConditions(self):
        return self._AlgConditions

    @AlgConditions.setter
    def AlgConditions(self, AlgConditions):
        self._AlgConditions = AlgConditions

    @property
    def AlgDetectSession(self):
        return self._AlgDetectSession

    @AlgDetectSession.setter
    def AlgDetectSession(self, AlgDetectSession):
        self._AlgDetectSession = AlgDetectSession

    @property
    def AlgDetectJS(self):
        return self._AlgDetectJS

    @AlgDetectJS.setter
    def AlgDetectJS(self, AlgDetectJS):
        self._AlgDetectJS = AlgDetectJS

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._RuleID = params.get("RuleID")
        self._RuleName = params.get("RuleName")
        self._Switch = params.get("Switch")
        if params.get("AlgConditions") is not None:
            self._AlgConditions = []
            for item in params.get("AlgConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AlgConditions.append(obj)
        if params.get("AlgDetectSession") is not None:
            self._AlgDetectSession = AlgDetectSession()
            self._AlgDetectSession._deserialize(params.get("AlgDetectSession"))
        if params.get("AlgDetectJS") is not None:
            self._AlgDetectJS = []
            for item in params.get("AlgDetectJS"):
                obj = AlgDetectJS()
                obj._deserialize(item)
                self._AlgDetectJS.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlgDetectSession(AbstractModel):
    """Cookie校验与会话跟踪。

    """

    def __init__(self):
        r"""
        :param _Name: 操作名称。
        :type Name: str
        :param _DetectMode: 校验方式，默认update_detect，取值有：
<li>detect：仅校验；</li>
<li>update_detect：更新Cookie并校验。</li>
        :type DetectMode: str
        :param _SessionAnalyzeSwitch: 会话速率和周期特征校验开关，默认off，取值有：
<li>off：关闭；</li>
<li>on：打开。</li>
        :type SessionAnalyzeSwitch: str
        :param _InvalidStatTime: 校验结果为未携带Cookie或Cookie已过期的统计周期。单位为秒，默认10，取值：5～3600。
        :type InvalidStatTime: int
        :param _InvalidThreshold: 校验结果为未携带Cookie或Cookie已过期的触发阈值。单位为次，默认300，取值：1～100000000。
        :type InvalidThreshold: int
        :param _AlgDetectResults: Cookie校验校验结果。
        :type AlgDetectResults: list of AlgDetectResult
        :param _SessionBehaviors: 会话速率和周期特征校验结果。
        :type SessionBehaviors: list of AlgDetectResult
        """
        self._Name = None
        self._DetectMode = None
        self._SessionAnalyzeSwitch = None
        self._InvalidStatTime = None
        self._InvalidThreshold = None
        self._AlgDetectResults = None
        self._SessionBehaviors = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DetectMode(self):
        return self._DetectMode

    @DetectMode.setter
    def DetectMode(self, DetectMode):
        self._DetectMode = DetectMode

    @property
    def SessionAnalyzeSwitch(self):
        return self._SessionAnalyzeSwitch

    @SessionAnalyzeSwitch.setter
    def SessionAnalyzeSwitch(self, SessionAnalyzeSwitch):
        self._SessionAnalyzeSwitch = SessionAnalyzeSwitch

    @property
    def InvalidStatTime(self):
        return self._InvalidStatTime

    @InvalidStatTime.setter
    def InvalidStatTime(self, InvalidStatTime):
        self._InvalidStatTime = InvalidStatTime

    @property
    def InvalidThreshold(self):
        return self._InvalidThreshold

    @InvalidThreshold.setter
    def InvalidThreshold(self, InvalidThreshold):
        self._InvalidThreshold = InvalidThreshold

    @property
    def AlgDetectResults(self):
        return self._AlgDetectResults

    @AlgDetectResults.setter
    def AlgDetectResults(self, AlgDetectResults):
        self._AlgDetectResults = AlgDetectResults

    @property
    def SessionBehaviors(self):
        return self._SessionBehaviors

    @SessionBehaviors.setter
    def SessionBehaviors(self, SessionBehaviors):
        self._SessionBehaviors = SessionBehaviors


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DetectMode = params.get("DetectMode")
        self._SessionAnalyzeSwitch = params.get("SessionAnalyzeSwitch")
        self._InvalidStatTime = params.get("InvalidStatTime")
        self._InvalidThreshold = params.get("InvalidThreshold")
        if params.get("AlgDetectResults") is not None:
            self._AlgDetectResults = []
            for item in params.get("AlgDetectResults"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self._AlgDetectResults.append(obj)
        if params.get("SessionBehaviors") is not None:
            self._SessionBehaviors = []
            for item in params.get("SessionBehaviors"):
                obj = AlgDetectResult()
                obj._deserialize(item)
                self._SessionBehaviors.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AliasDomain(AbstractModel):
    """别称域名信息。

    """

    def __init__(self):
        r"""
        :param _AliasName: 别称域名名称。
        :type AliasName: str
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _TargetName: 目标域名名称。
        :type TargetName: str
        :param _Status: 别称域名状态，取值有：
<li> active：已生效； </li>
<li> pending：部署中；</li>
<li> conflict：被找回。 </li>
<li> stop：已停用；</li>
        :type Status: str
        :param _ForbidMode: 封禁模式，取值有：
<li> 0：未封禁； </li>
<li> 11：合规封禁；</li>
<li> 14：未备案封禁。</li>
        :type ForbidMode: int
        :param _CreatedOn: 别称域名创建时间。
        :type CreatedOn: str
        :param _ModifiedOn: 别称域名修改时间。
        :type ModifiedOn: str
        """
        self._AliasName = None
        self._ZoneId = None
        self._TargetName = None
        self._Status = None
        self._ForbidMode = None
        self._CreatedOn = None
        self._ModifiedOn = None

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TargetName(self):
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ForbidMode(self):
        return self._ForbidMode

    @ForbidMode.setter
    def ForbidMode(self, ForbidMode):
        self._ForbidMode = ForbidMode

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn


    def _deserialize(self, params):
        self._AliasName = params.get("AliasName")
        self._ZoneId = params.get("ZoneId")
        self._TargetName = params.get("TargetName")
        self._Status = params.get("Status")
        self._ForbidMode = params.get("ForbidMode")
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxy(AbstractModel):
    """应用代理实例

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _ZoneName: 站点名称。
        :type ZoneName: str
        :param _ProxyId: 代理ID。
        :type ProxyId: str
        :param _ProxyName: 当ProxyType=hostname时，表示域名或子域名；
当ProxyType=instance时，表示代理名称。
        :type ProxyName: str
        :param _ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>
        :type ProxyType: str
        :param _PlatType: 调度模式，取值有：
<li>ip：表示Anycast IP调度；</li>
<li>domain：表示CNAME调度。</li>
        :type PlatType: str
        :param _Area: 加速区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
默认值：overseas
        :type Area: str
        :param _SecurityType: 是否开启安全，取值有：
<li>0：关闭安全；</li>
<li>1：开启安全。</li>
        :type SecurityType: int
        :param _AccelerateType: 是否开启加速，取值有：
<li>0：关闭加速；</li>
<li>1：开启加速。</li>
        :type AccelerateType: int
        :param _SessionPersistTime: 会话保持时间。
        :type SessionPersistTime: int
        :param _Status: 状态，取值有：
<li>online：启用；</li>
<li>offline：停用；</li>
<li>progress：部署中；</li>
<li>stopping：停用中；</li>
<li>fail：部署失败/停用失败。</li>
        :type Status: str
        :param _BanStatus: 封禁状态，取值有：
<li>banned：已封禁;</li>
<li>banning：封禁中；</li>
<li>recover：已解封；</li>
<li>recovering：解封禁中。</li>
        :type BanStatus: str
        :param _ScheduleValue: 调度信息。
        :type ScheduleValue: list of str
        :param _HostId: 当ProxyType=hostname时：
表示代理加速唯一标识。
        :type HostId: str
        :param _Ipv6: Ipv6访问配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _ApplicationProxyRules: 规则列表。
        :type ApplicationProxyRules: list of ApplicationProxyRule
        :param _AccelerateMainland: 中国大陆加速优化配置。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self._ZoneId = None
        self._ZoneName = None
        self._ProxyId = None
        self._ProxyName = None
        self._ProxyType = None
        self._PlatType = None
        self._Area = None
        self._SecurityType = None
        self._AccelerateType = None
        self._SessionPersistTime = None
        self._Status = None
        self._BanStatus = None
        self._ScheduleValue = None
        self._HostId = None
        self._Ipv6 = None
        self._UpdateTime = None
        self._ApplicationProxyRules = None
        self._AccelerateMainland = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def PlatType(self):
        return self._PlatType

    @PlatType.setter
    def PlatType(self, PlatType):
        self._PlatType = PlatType

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SecurityType(self):
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def AccelerateType(self):
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BanStatus(self):
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def ScheduleValue(self):
        return self._ScheduleValue

    @ScheduleValue.setter
    def ScheduleValue(self, ScheduleValue):
        self._ScheduleValue = ScheduleValue

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ApplicationProxyRules(self):
        return self._ApplicationProxyRules

    @ApplicationProxyRules.setter
    def ApplicationProxyRules(self, ApplicationProxyRules):
        self._ApplicationProxyRules = ApplicationProxyRules

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._ProxyType = params.get("ProxyType")
        self._PlatType = params.get("PlatType")
        self._Area = params.get("Area")
        self._SecurityType = params.get("SecurityType")
        self._AccelerateType = params.get("AccelerateType")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._Status = params.get("Status")
        self._BanStatus = params.get("BanStatus")
        self._ScheduleValue = params.get("ScheduleValue")
        self._HostId = params.get("HostId")
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        self._UpdateTime = params.get("UpdateTime")
        if params.get("ApplicationProxyRules") is not None:
            self._ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._ApplicationProxyRules.append(obj)
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationProxyRule(AbstractModel):
    """应用代理规则

    """

    def __init__(self):
        r"""
        :param _Proto: 协议，取值有：
<li>TCP：TCP协议；</li>
<li>UDP：UDP协议。</li>
        :type Proto: str
        :param _Port: 端口，支持格式：
<li>单个端口，如：80。</li>
<li>端口段，如：81-82。表示81，82两个端口。</li>
注意：一条规则最多可填写20个端口。
        :type Port: list of str
        :param _OriginType: 源站类型，取值有：
<li>custom：手动添加；</li>
<li>origins：源站组。</li>
        :type OriginType: str
        :param _OriginValue: 源站信息：
<li>当 OriginType 为 custom 时，表示一个或多个源站，如`["8.8.8.8","9.9.9.9"]` 或 `OriginValue=["test.com"]`；</li>
<li>当 OriginType 为 origins 时，要求有且仅有一个元素，表示源站组ID，如`["origin-537f5b41-162a-11ed-abaa-525400c5da15"]`。</li>
        :type OriginValue: list of str
        :param _RuleId: 规则ID。
        :type RuleId: str
        :param _Status: 状态，取值有：
<li>online：启用；</li>
<li>offline：停用；</li>
<li>progress：部署中；</li>
<li>stopping：停用中；</li>
<li>fail：部署失败/停用失败。</li>
        :type Status: str
        :param _ForwardClientIp: 传递客户端IP，取值有：
<li>TOA：TOA（仅Proto=TCP时可选）；</li>
<li>PPV1：Proxy Protocol传递，协议版本V1（仅Proto=TCP时可选）；</li>
<li>PPV2：Proxy Protocol传递，协议版本V2；</li>
<li>OFF：不传递。</li>默认值：OFF。
        :type ForwardClientIp: str
        :param _SessionPersist: 是否开启会话保持，取值有：
<li>true：开启；</li>
<li>false：关闭。</li>默认值：false。
        :type SessionPersist: bool
        :param _SessionPersistTime: 会话保持的时间，只有当SessionPersist为true时，该值才会生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionPersistTime: int
        :param _OriginPort: 源站端口，支持格式：
<li>单端口，如：80。</li>
<li>端口段：81-82，表示81，82两个端口。</li>
        :type OriginPort: str
        :param _RuleTag: 规则标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTag: str
        """
        self._Proto = None
        self._Port = None
        self._OriginType = None
        self._OriginValue = None
        self._RuleId = None
        self._Status = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._OriginPort = None
        self._RuleTag = None

    @property
    def Proto(self):
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ForwardClientIp(self):
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def OriginPort(self):
        return self._OriginPort

    @OriginPort.setter
    def OriginPort(self, OriginPort):
        self._OriginPort = OriginPort

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._OriginPort = params.get("OriginPort")
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AscriptionInfo(AbstractModel):
    """站点归属信息

    """

    def __init__(self):
        r"""
        :param _Subdomain: 主机记录。
        :type Subdomain: str
        :param _RecordType: 记录类型。
        :type RecordType: str
        :param _RecordValue: 记录值。
        :type RecordValue: str
        """
        self._Subdomain = None
        self._RecordType = None
        self._RecordValue = None

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecurityTemplateToEntityRequest(AbstractModel):
    """BindSecurityTemplateToEntity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 需要绑定或解绑的策略模板所属站点 ID。
        :type ZoneId: str
        :param _Entities: 绑定至策略模板（或者从策略模板解绑）的域名列表。
        :type Entities: list of str
        :param _Operate: 绑定或解绑操作选项，取值有：
<li>bind：绑定域名至策略模板；</li>
<li>unbind-keep-policy：将域名从策略模板解绑，解绑时保留当前策略；</li>
<li>unbind-use-default：将域名从策略模板解绑，并使用默认空白策略。</li>注意：解绑操作当前仅支持单个域名解绑。即：当 Operate 参数取值为 unbind-keep-policy 或 unbind-use-default 时，Entities 参数列表仅支持填写一个域名。
        :type Operate: str
        :param _TemplateId: 指定绑定或解绑的策略模板 ID 。
        :type TemplateId: str
        :param _OverWrite: 如指定的域名已经绑定了策略模板，是否替换该模板。支持下列取值：
<li>true： 替换域名当前绑定的模板；</li>
<li>false：不替换域名当前绑定的模板。</li>注意：当选择不替换已有策略模板时，若指定域名已经绑定策略模板，API 将返回错误。
        :type OverWrite: bool
        """
        self._ZoneId = None
        self._Entities = None
        self._Operate = None
        self._TemplateId = None
        self._OverWrite = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Entities(self):
        return self._Entities

    @Entities.setter
    def Entities(self, Entities):
        self._Entities = Entities

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def OverWrite(self):
        return self._OverWrite

    @OverWrite.setter
    def OverWrite(self, OverWrite):
        self._OverWrite = OverWrite


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Entities = params.get("Entities")
        self._Operate = params.get("Operate")
        self._TemplateId = params.get("TemplateId")
        self._OverWrite = params.get("OverWrite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecurityTemplateToEntityResponse(AbstractModel):
    """BindSecurityTemplateToEntity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BindZoneToPlanRequest(AbstractModel):
    """BindZoneToPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 未绑定套餐的站点ID。
        :type ZoneId: str
        :param _PlanId: 待绑定的目标套餐ID。
        :type PlanId: str
        """
        self._ZoneId = None
        self._PlanId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindZoneToPlanResponse(AbstractModel):
    """BindZoneToPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BotConfig(AbstractModel):
    """安全Bot配置

    """

    def __init__(self):
        r"""
        :param _Switch: bot开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _BotManagedRule: 通用详细基础规则。如果为null，默认使用历史配置。
        :type BotManagedRule: :class:`tencentcloud.teo.v20220901.models.BotManagedRule`
        :param _BotPortraitRule: 用户画像规则。如果为null，默认使用历史配置。
        :type BotPortraitRule: :class:`tencentcloud.teo.v20220901.models.BotPortraitRule`
        :param _IntelligenceRule: Bot智能分析。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntelligenceRule: :class:`tencentcloud.teo.v20220901.models.IntelligenceRule`
        :param _BotUserRules: Bot自定义规则。如果为null，默认使用历史配置。
        :type BotUserRules: list of BotUserRule
        :param _AlgDetectRule: Bot主动特征识别规则。
        :type AlgDetectRule: list of AlgDetectRule
        :param _Customizes: Bot托管定制策略，入参可不填，仅出参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Customizes: list of BotUserRule
        """
        self._Switch = None
        self._BotManagedRule = None
        self._BotPortraitRule = None
        self._IntelligenceRule = None
        self._BotUserRules = None
        self._AlgDetectRule = None
        self._Customizes = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BotManagedRule(self):
        return self._BotManagedRule

    @BotManagedRule.setter
    def BotManagedRule(self, BotManagedRule):
        self._BotManagedRule = BotManagedRule

    @property
    def BotPortraitRule(self):
        return self._BotPortraitRule

    @BotPortraitRule.setter
    def BotPortraitRule(self, BotPortraitRule):
        self._BotPortraitRule = BotPortraitRule

    @property
    def IntelligenceRule(self):
        return self._IntelligenceRule

    @IntelligenceRule.setter
    def IntelligenceRule(self, IntelligenceRule):
        self._IntelligenceRule = IntelligenceRule

    @property
    def BotUserRules(self):
        return self._BotUserRules

    @BotUserRules.setter
    def BotUserRules(self, BotUserRules):
        self._BotUserRules = BotUserRules

    @property
    def AlgDetectRule(self):
        return self._AlgDetectRule

    @AlgDetectRule.setter
    def AlgDetectRule(self, AlgDetectRule):
        self._AlgDetectRule = AlgDetectRule

    @property
    def Customizes(self):
        return self._Customizes

    @Customizes.setter
    def Customizes(self, Customizes):
        self._Customizes = Customizes


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("BotManagedRule") is not None:
            self._BotManagedRule = BotManagedRule()
            self._BotManagedRule._deserialize(params.get("BotManagedRule"))
        if params.get("BotPortraitRule") is not None:
            self._BotPortraitRule = BotPortraitRule()
            self._BotPortraitRule._deserialize(params.get("BotPortraitRule"))
        if params.get("IntelligenceRule") is not None:
            self._IntelligenceRule = IntelligenceRule()
            self._IntelligenceRule._deserialize(params.get("IntelligenceRule"))
        if params.get("BotUserRules") is not None:
            self._BotUserRules = []
            for item in params.get("BotUserRules"):
                obj = BotUserRule()
                obj._deserialize(item)
                self._BotUserRules.append(obj)
        if params.get("AlgDetectRule") is not None:
            self._AlgDetectRule = []
            for item in params.get("AlgDetectRule"):
                obj = AlgDetectRule()
                obj._deserialize(item)
                self._AlgDetectRule.append(obj)
        if params.get("Customizes") is not None:
            self._Customizes = []
            for item in params.get("Customizes"):
                obj = BotUserRule()
                obj._deserialize(item)
                self._Customizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotExtendAction(AbstractModel):
    """Bot扩展处置方式，多处置动作组合。

    """

    def __init__(self):
        r"""
        :param _Action: 处置动作，取值有：
<li>monitor：观察；</li>
<li>alg：JavaScript挑战；</li>
<li>captcha：托管挑战；</li>
<li>random：随机，按照ExtendActions分配处置动作和比例；</li>
<li>silence：静默；</li>
<li>shortdelay：短时响应；</li>
<li>longdelay：长时响应。</li>
        :type Action: str
        :param _Percent: 处置方式的触发概率，范围0-100。
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        """
        self._Action = None
        self._Percent = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotManagedRule(AbstractModel):
    """Bot 规则，下列规则ID可参考接口 DescribeBotManagedRules返回的ID信息

    """

    def __init__(self):
        r"""
        :param _Action: 触发规则后的处置方式，取值有：
<li>drop：拦截；</li>
<li>trans：放行；</li>
<li>alg：Javascript挑战；</li>
<li>monitor：观察。</li>
        :type Action: str
        :param _RuleID: 本规则的ID。仅出参使用。
        :type RuleID: int
        :param _TransManagedIds: 放行的规则ID。默认所有规则不配置放行。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransManagedIds: list of int
        :param _AlgManagedIds: JS挑战的规则ID。默认所有规则不配置JS挑战。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param _CapManagedIds: 数字验证码的规则ID。默认所有规则不配置数字验证码。
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param _MonManagedIds: 观察的规则ID。默认所有规则不配置观察。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param _DropManagedIds: 拦截的规则ID。默认所有规则不配置拦截。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        """
        self._Action = None
        self._RuleID = None
        self._TransManagedIds = None
        self._AlgManagedIds = None
        self._CapManagedIds = None
        self._MonManagedIds = None
        self._DropManagedIds = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def TransManagedIds(self):
        return self._TransManagedIds

    @TransManagedIds.setter
    def TransManagedIds(self, TransManagedIds):
        self._TransManagedIds = TransManagedIds

    @property
    def AlgManagedIds(self):
        return self._AlgManagedIds

    @AlgManagedIds.setter
    def AlgManagedIds(self, AlgManagedIds):
        self._AlgManagedIds = AlgManagedIds

    @property
    def CapManagedIds(self):
        return self._CapManagedIds

    @CapManagedIds.setter
    def CapManagedIds(self, CapManagedIds):
        self._CapManagedIds = CapManagedIds

    @property
    def MonManagedIds(self):
        return self._MonManagedIds

    @MonManagedIds.setter
    def MonManagedIds(self, MonManagedIds):
        self._MonManagedIds = MonManagedIds

    @property
    def DropManagedIds(self):
        return self._DropManagedIds

    @DropManagedIds.setter
    def DropManagedIds(self, DropManagedIds):
        self._DropManagedIds = DropManagedIds


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._RuleID = params.get("RuleID")
        self._TransManagedIds = params.get("TransManagedIds")
        self._AlgManagedIds = params.get("AlgManagedIds")
        self._CapManagedIds = params.get("CapManagedIds")
        self._MonManagedIds = params.get("MonManagedIds")
        self._DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotPortraitRule(AbstractModel):
    """bot 用户画像规则

    """

    def __init__(self):
        r"""
        :param _Switch: 本功能的开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _RuleID: 本规则的ID。仅出参使用。
        :type RuleID: int
        :param _AlgManagedIds: JS挑战的规则ID。默认所有规则不配置JS挑战。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgManagedIds: list of int
        :param _CapManagedIds: 数字验证码的规则ID。默认所有规则不配置数字验证码。
注意：此字段可能返回 null，表示取不到有效值。
        :type CapManagedIds: list of int
        :param _MonManagedIds: 观察的规则ID。默认所有规则不配置观察。
注意：此字段可能返回 null，表示取不到有效值。
        :type MonManagedIds: list of int
        :param _DropManagedIds: 拦截的规则ID。默认所有规则不配置拦截。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropManagedIds: list of int
        """
        self._Switch = None
        self._RuleID = None
        self._AlgManagedIds = None
        self._CapManagedIds = None
        self._MonManagedIds = None
        self._DropManagedIds = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def AlgManagedIds(self):
        return self._AlgManagedIds

    @AlgManagedIds.setter
    def AlgManagedIds(self, AlgManagedIds):
        self._AlgManagedIds = AlgManagedIds

    @property
    def CapManagedIds(self):
        return self._CapManagedIds

    @CapManagedIds.setter
    def CapManagedIds(self, CapManagedIds):
        self._CapManagedIds = CapManagedIds

    @property
    def MonManagedIds(self):
        return self._MonManagedIds

    @MonManagedIds.setter
    def MonManagedIds(self, MonManagedIds):
        self._MonManagedIds = MonManagedIds

    @property
    def DropManagedIds(self):
        return self._DropManagedIds

    @DropManagedIds.setter
    def DropManagedIds(self, DropManagedIds):
        self._DropManagedIds = DropManagedIds


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleID = params.get("RuleID")
        self._AlgManagedIds = params.get("AlgManagedIds")
        self._CapManagedIds = params.get("CapManagedIds")
        self._MonManagedIds = params.get("MonManagedIds")
        self._DropManagedIds = params.get("DropManagedIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotUserRule(AbstractModel):
    """Bot自定义规则

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名，只能以英文字符，数字，下划线组合，且不能以下划线开头。
        :type RuleName: str
        :param _Action: 处置动作，取值有：
<li>drop：拦截；</li>
<li>monitor：观察；</li>
<li>trans：放行；</li>
<li>redirect：重定向；</li>
<li>page：指定页面；</li>
<li>alg：JavaScript 挑战；</li>
<li>captcha：托管挑战；</li>
<li>random：随机处置；</li>
<li>silence：静默；</li>
<li>shortdelay：短时响应；</li>
<li>longdelay：长时响应。</li>
        :type Action: str
        :param _RuleStatus: 规则状态，取值有：
<li>on：生效；</li>
<li>off：不生效。</li>默认 on 生效。
        :type RuleStatus: str
        :param _AclConditions: 规则详情。
        :type AclConditions: list of AclCondition
        :param _RulePriority: 规则权重，取值范围0-100。
        :type RulePriority: int
        :param _RuleID: 规则 Id。仅出参使用。
        :type RuleID: int
        :param _ExtendActions: 随机处置的处置方式及占比，非随机处置可不填暂不支持。
        :type ExtendActions: list of BotExtendAction
        :param _FreqFields: 过滤词，取值有：
<li>sip：客户端 ip。</li>
默认为空字符串。
        :type FreqFields: list of str
        :param _UpdateTime: 更新时间。仅出参使用。
        :type UpdateTime: str
        :param _FreqScope: 统计范围。取值有：
<li>source_to_eo：（响应）源站到 EdgeOne；</li>
<li>client_to_eo：（请求）客户端到 EdgeOne。</li>
默认为 source_to_eo。
        :type FreqScope: list of str
        :param _Name: 自定义返回页面的名称。Action 是 page 时必填，且不能为空。
        :type Name: str
        :param _CustomResponseId: 自定义响应 Id。该 Id 可通过查询自定义错误页列表接口获取。默认值为default，使用系统默认页面。Action 是 page 时必填，且不能为空。	
        :type CustomResponseId: str
        :param _ResponseCode: 自定义返回页面的响应码。Action 是 page 时必填，且不能为空，取值: 100~600，不支持 3xx 响应码。默认值：567。
        :type ResponseCode: int
        :param _RedirectUrl: 重定向时候的地址。Action 是 redirect 时必填，且不能为空。
        :type RedirectUrl: str
        """
        self._RuleName = None
        self._Action = None
        self._RuleStatus = None
        self._AclConditions = None
        self._RulePriority = None
        self._RuleID = None
        self._ExtendActions = None
        self._FreqFields = None
        self._UpdateTime = None
        self._FreqScope = None
        self._Name = None
        self._CustomResponseId = None
        self._ResponseCode = None
        self._RedirectUrl = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def AclConditions(self):
        return self._AclConditions

    @AclConditions.setter
    def AclConditions(self, AclConditions):
        self._AclConditions = AclConditions

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def ExtendActions(self):
        return self._ExtendActions

    @ExtendActions.setter
    def ExtendActions(self, ExtendActions):
        self._ExtendActions = ExtendActions

    @property
    def FreqFields(self):
        return self._FreqFields

    @FreqFields.setter
    def FreqFields(self, FreqFields):
        self._FreqFields = FreqFields

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def FreqScope(self):
        return self._FreqScope

    @FreqScope.setter
    def FreqScope(self, FreqScope):
        self._FreqScope = FreqScope

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId

    @property
    def ResponseCode(self):
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self._AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AclConditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        if params.get("ExtendActions") is not None:
            self._ExtendActions = []
            for item in params.get("ExtendActions"):
                obj = BotExtendAction()
                obj._deserialize(item)
                self._ExtendActions.append(obj)
        self._FreqFields = params.get("FreqFields")
        self._UpdateTime = params.get("UpdateTime")
        self._FreqScope = params.get("FreqScope")
        self._Name = params.get("Name")
        self._CustomResponseId = params.get("CustomResponseId")
        self._ResponseCode = params.get("ResponseCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CC(AbstractModel):
    """cc配置项。

    """

    def __init__(self):
        r"""
        :param _Switch: Waf开关，取值为：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        """
        self._Switch = None
        self._PolicyId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """缓存时间设置

    """

    def __init__(self):
        r"""
        :param _Switch: 缓存配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _CacheTime: 缓存过期时间设置。
单位为秒，最大可设置为 365 天。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        :param _IgnoreCacheControl: 是否开启强制缓存，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        """
        self._Switch = None
        self._CacheTime = None
        self._IgnoreCacheControl = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def IgnoreCacheControl(self):
        warnings.warn("parameter `IgnoreCacheControl` is deprecated", DeprecationWarning) 

        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        warnings.warn("parameter `IgnoreCacheControl` is deprecated", DeprecationWarning) 

        self._IgnoreCacheControl = IgnoreCacheControl


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CacheTime = params.get("CacheTime")
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """缓存规则配置。

    """

    def __init__(self):
        r"""
        :param _Cache: 缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.teo.v20220901.models.Cache`
        :param _NoCache: 不缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCache: :class:`tencentcloud.teo.v20220901.models.NoCache`
        :param _FollowOrigin: 遵循源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: :class:`tencentcloud.teo.v20220901.models.FollowOrigin`
        """
        self._Cache = None
        self._NoCache = None
        self._FollowOrigin = None

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def NoCache(self):
        return self._NoCache

    @NoCache.setter
    def NoCache(self, NoCache):
        self._NoCache = NoCache

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self._NoCache = NoCache()
            self._NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self._FollowOrigin = FollowOrigin()
            self._FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """缓存键配置。

    """

    def __init__(self):
        r"""
        :param _FullUrlCache: 是否开启全路径缓存，取值有：
<li>on：开启全路径缓存（即关闭参数忽略）；</li>
<li>off：关闭全路径缓存（即开启参数忽略）。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FullUrlCache: str
        :param _IgnoreCase: 是否忽略大小写缓存，取值有：
<li>on：忽略；</li>
<li>off：不忽略。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param _QueryString: CacheKey 中包含请求参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.teo.v20220901.models.QueryString`
        """
        self._FullUrlCache = None
        self._IgnoreCase = None
        self._QueryString = None

    @property
    def FullUrlCache(self):
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache

    @property
    def IgnoreCase(self):
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString


    def _deserialize(self, params):
        self._FullUrlCache = params.get("FullUrlCache")
        self._IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self._QueryString = QueryString()
            self._QueryString._deserialize(params.get("QueryString"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CachePrefresh(AbstractModel):
    """缓存预刷新

    """

    def __init__(self):
        r"""
        :param _Switch: 缓存预刷新配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _Percent: 缓存预刷新百分比，取值范围：1-99。
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        """
        self._Switch = None
        self._Percent = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfo(AbstractModel):
    """https 服务端证书配置

    """

    def __init__(self):
        r"""
        :param _CertId: 服务器证书 ID。
        :type CertId: str
        :param _Alias: 证书备注名。
        :type Alias: str
        :param _Type: 证书类型，取值有：
<li>default：默认证书；</li>
<li>upload：用户上传；</li>
<li>managed：腾讯云托管。</li>
        :type Type: str
        :param _ExpireTime: 证书过期时间。
        :type ExpireTime: str
        :param _DeployTime: 证书部署时间。
        :type DeployTime: str
        :param _SignAlgo: 签名算法。
        :type SignAlgo: str
        :param _Status: 证书状态，取值有：
<li>deployed：已部署；</li>
<li>processing：部署中；</li>
<li>applying：申请中；</li>
<li>failed：申请失败；</li>
<li>issued：绑定失败。</li>
        :type Status: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._DeployTime = None
        self._SignAlgo = None
        self._Status = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def SignAlgo(self):
        return self._SignAlgo

    @SignAlgo.setter
    def SignAlgo(self, SignAlgo):
        self._SignAlgo = SignAlgo

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._SignAlgo = params.get("SignAlgo")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCnameStatusRequest(AbstractModel):
    """CheckCnameStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _RecordNames: 加速域名列表。
        :type RecordNames: list of str
        """
        self._ZoneId = None
        self._RecordNames = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordNames(self):
        return self._RecordNames

    @RecordNames.setter
    def RecordNames(self, RecordNames):
        self._RecordNames = RecordNames


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordNames = params.get("RecordNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCnameStatusResponse(AbstractModel):
    """CheckCnameStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CnameStatus: 加速域名 CNAME 状态信息列表。
        :type CnameStatus: list of CnameStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CnameStatus = None
        self._RequestId = None

    @property
    def CnameStatus(self):
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CnameStatus") is not None:
            self._CnameStatus = []
            for item in params.get("CnameStatus"):
                obj = CnameStatus()
                obj._deserialize(item)
                self._CnameStatus.append(obj)
        self._RequestId = params.get("RequestId")


class ClientIpCountry(AbstractModel):
    """回源时携带客户端IP所属地域信息，值的格式为ISO-3166-1两位字母代码。

    """

    def __init__(self):
        r"""
        :param _Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _HeaderName: 存放客户端 IP 所属地域信息的请求头名称，当 Switch=on 时有效。
为空则使用默认值：EO-Client-IPCountry。
        :type HeaderName: str
        """
        self._Switch = None
        self._HeaderName = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientIpHeader(AbstractModel):
    """存储客户端请求IP的头部信息配置

    """

    def __init__(self):
        r"""
        :param _Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _HeaderName: 回源时，存放客户端 IP 的请求头名称。
为空则使用默认值：X-Forwarded-IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderName: str
        """
        self._Switch = None
        self._HeaderName = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CnameStatus(AbstractModel):
    """CNAME 状态

    """

    def __init__(self):
        r"""
        :param _RecordName: 记录名称。
        :type RecordName: str
        :param _Cname: CNAME 地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param _Status: Cname状态信息，取值有：
<li>active：生效；</li>
<li>moved：不生效。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._RecordName = None
        self._Cname = None
        self._Status = None

    @property
    def RecordName(self):
        return self._RecordName

    @RecordName.setter
    def RecordName(self, RecordName):
        self._RecordName = RecordName

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RecordName = params.get("RecordName")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeAction(AbstractModel):
    """规则引擎带有状态码的动作

    """

    def __init__(self):
        r"""
        :param _Action: 功能名称，功能名称填写规范可调用接口 [查询规则引擎的设置参数](https://cloud.tencent.com/document/product/1552/80618) 查看。
        :type Action: str
        :param _Parameters: 操作参数。
        :type Parameters: list of RuleCodeActionParams
        """
        self._Action = None
        self._Parameters = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = RuleCodeActionParams()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """智能压缩配置。

    """

    def __init__(self):
        r"""
        :param _Switch: 智能压缩配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _Algorithms: 支持的压缩算法列表，取值有：
<li>brotli：brotli算法；</li>
<li>gzip：gzip算法。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Algorithms: list of str
        """
        self._Switch = None
        self._Algorithms = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Algorithms(self):
        return self._Algorithms

    @Algorithms.setter
    def Algorithms(self, Algorithms):
        self._Algorithms = Algorithms


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Algorithms = params.get("Algorithms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerationDomainRequest(AbstractModel):
    """CreateAccelerationDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 加速域名所属站点 ID。
        :type ZoneId: str
        :param _DomainName: 加速域名。
        :type DomainName: str
        :param _OriginInfo: 源站信息。
        :type OriginInfo: :class:`tencentcloud.teo.v20220901.models.OriginInfo`
        :param _OriginProtocol: 回源协议，取值有：
<li>FOLLOW: 协议跟随；</li>
<li>HTTP: HTTP协议回源；</li>
<li>HTTPS: HTTPS协议回源。</li>
<li>不填默认为： FOLLOW。</li>
        :type OriginProtocol: str
        :param _HttpOriginPort: HTTP回源端口，取值为1-65535，当OriginProtocol=FOLLOW/HTTP时生效, 不填默认为80。
        :type HttpOriginPort: int
        :param _HttpsOriginPort: HTTPS回源端口，取值为1-65535，当OriginProtocol=FOLLOW/HTTPS时生效，不填默认为443。
        :type HttpsOriginPort: int
        :param _IPv6Status: IPv6状态，取值有：
<li>follow：遵循站点IPv6配置；</li>
<li>on：开启状态；</li>
<li>off：关闭状态。</li>
<li>不填默认为：follow。</li>
        :type IPv6Status: str
        """
        self._ZoneId = None
        self._DomainName = None
        self._OriginInfo = None
        self._OriginProtocol = None
        self._HttpOriginPort = None
        self._HttpsOriginPort = None
        self._IPv6Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def OriginInfo(self):
        return self._OriginInfo

    @OriginInfo.setter
    def OriginInfo(self, OriginInfo):
        self._OriginInfo = OriginInfo

    @property
    def OriginProtocol(self):
        return self._OriginProtocol

    @OriginProtocol.setter
    def OriginProtocol(self, OriginProtocol):
        self._OriginProtocol = OriginProtocol

    @property
    def HttpOriginPort(self):
        return self._HttpOriginPort

    @HttpOriginPort.setter
    def HttpOriginPort(self, HttpOriginPort):
        self._HttpOriginPort = HttpOriginPort

    @property
    def HttpsOriginPort(self):
        return self._HttpsOriginPort

    @HttpsOriginPort.setter
    def HttpsOriginPort(self, HttpsOriginPort):
        self._HttpsOriginPort = HttpsOriginPort

    @property
    def IPv6Status(self):
        return self._IPv6Status

    @IPv6Status.setter
    def IPv6Status(self, IPv6Status):
        self._IPv6Status = IPv6Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainName = params.get("DomainName")
        if params.get("OriginInfo") is not None:
            self._OriginInfo = OriginInfo()
            self._OriginInfo._deserialize(params.get("OriginInfo"))
        self._OriginProtocol = params.get("OriginProtocol")
        self._HttpOriginPort = params.get("HttpOriginPort")
        self._HttpsOriginPort = params.get("HttpsOriginPort")
        self._IPv6Status = params.get("IPv6Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerationDomainResponse(AbstractModel):
    """CreateAccelerationDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnershipVerification: 当您的站点未进行归属权验证时，您可通过该参数返回的信息单独对域名进行归属权校验。详情参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789)。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OwnershipVerification = None
        self._RequestId = None

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        self._RequestId = params.get("RequestId")


class CreateAliasDomainRequest(AbstractModel):
    """CreateAliasDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _AliasName: 别称域名名称。
        :type AliasName: str
        :param _TargetName: 目标域名名称。
        :type TargetName: str
        :param _CertType: 证书配置，取值有：
<li> none：不配置；</li>
<li> hosting：SSL托管证书。</li>默认取值为 none。
        :type CertType: str
        :param _CertId: 当 CertType 取值为 hosting 时需填入相应证书 ID。
        :type CertId: list of str
        """
        self._ZoneId = None
        self._AliasName = None
        self._TargetName = None
        self._CertType = None
        self._CertId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def TargetName(self):
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._AliasName = params.get("AliasName")
        self._TargetName = params.get("TargetName")
        self._CertType = params.get("CertType")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasDomainResponse(AbstractModel):
    """CreateAliasDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateApplicationProxyRequest(AbstractModel):
    """CreateApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _ProxyName: 当 ProxyType=hostname 时，表示域名或子域名；
当 ProxyType=instance 时，表示代理名称。
        :type ProxyName: str
        :param _PlatType: 调度模式，取值有：
<li>ip：表示Anycast IP调度；</li>
<li>domain：表示CNAME调度。</li>
        :type PlatType: str
        :param _SecurityType: 是否开启安全，取值有：
<li>0：关闭安全；</li>
<li>1：开启安全。</li>
        :type SecurityType: int
        :param _AccelerateType: 是否开启加速，取值有：
<li>0：关闭加速；</li>
<li>1：开启加速。</li>
        :type AccelerateType: int
        :param _ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>不填写使用默认值instance。
        :type ProxyType: str
        :param _SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒。
不填写使用默认值600。
        :type SessionPersistTime: int
        :param _Ipv6: Ipv6 访问配置。
不填写表示关闭 Ipv6 访问。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _ApplicationProxyRules: 规则详细信息。
不填写则不创建规则。
        :type ApplicationProxyRules: list of ApplicationProxyRule
        :param _AccelerateMainland: 中国大陆加速优化配置。不填写表示关闭中国大陆加速优化。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self._ZoneId = None
        self._ProxyName = None
        self._PlatType = None
        self._SecurityType = None
        self._AccelerateType = None
        self._ProxyType = None
        self._SessionPersistTime = None
        self._Ipv6 = None
        self._ApplicationProxyRules = None
        self._AccelerateMainland = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def PlatType(self):
        return self._PlatType

    @PlatType.setter
    def PlatType(self, PlatType):
        self._PlatType = PlatType

    @property
    def SecurityType(self):
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def AccelerateType(self):
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def ApplicationProxyRules(self):
        return self._ApplicationProxyRules

    @ApplicationProxyRules.setter
    def ApplicationProxyRules(self, ApplicationProxyRules):
        self._ApplicationProxyRules = ApplicationProxyRules

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyName = params.get("ProxyName")
        self._PlatType = params.get("PlatType")
        self._SecurityType = params.get("SecurityType")
        self._AccelerateType = params.get("AccelerateType")
        self._ProxyType = params.get("ProxyType")
        self._SessionPersistTime = params.get("SessionPersistTime")
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ApplicationProxyRules") is not None:
            self._ApplicationProxyRules = []
            for item in params.get("ApplicationProxyRules"):
                obj = ApplicationProxyRule()
                obj._deserialize(item)
                self._ApplicationProxyRules.append(obj)
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyResponse(AbstractModel):
    """CreateApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 新增的四层代理应用ID。
        :type ProxyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyId = None
        self._RequestId = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._RequestId = params.get("RequestId")


class CreateApplicationProxyRuleRequest(AbstractModel):
    """CreateApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _ProxyId: 代理ID。
        :type ProxyId: str
        :param _Proto: 协议，取值有：
<li>TCP：TCP协议；</li>
<li>UDP：UDP协议。</li>
        :type Proto: str
        :param _Port: 端口，支持格式：
<li>80：80端口；</li>
<li>81-90：81至90端口。</li>
        :type Port: list of str
        :param _OriginType: 源站类型，取值有：
<li>custom：手动添加；</li>
<li>origins：源站组。</li>
        :type OriginType: str
        :param _OriginValue: 源站信息：
<li>当 OriginType 为 custom 时，表示一个或多个源站，如`["8.8.8.8","9.9.9.9"]` 或 `OriginValue=["test.com"]`；</li>
<li>当 OriginType 为 origins 时，要求有且仅有一个元素，表示源站组ID，如`["origin-537f5b41-162a-11ed-abaa-525400c5da15"]`。</li>
        :type OriginValue: list of str
        :param _ForwardClientIp: 传递客户端IP，取值有：
<li>TOA：TOA（仅Proto=TCP时可选）；</li>
<li>PPV1：Proxy Protocol传递，协议版本V1（仅Proto=TCP时可选）；</li>
<li>PPV2：Proxy Protocol传递，协议版本V2；</li>
<li>OFF：不传递。</li>默认值：OFF。
        :type ForwardClientIp: str
        :param _SessionPersist: 是否开启会话保持，取值有：
<li>true：开启；</li>
<li>false：关闭。</li>默认值：false。
        :type SessionPersist: bool
        :param _SessionPersistTime: 会话保持的时间，只有当SessionPersist为true时，该值才会生效。
        :type SessionPersistTime: int
        :param _OriginPort: 源站端口，支持格式：
<li>单端口：80；</li>
<li>端口段：81-90，81至90端口。</li>
        :type OriginPort: str
        :param _RuleTag: 规则标签。默认值为空字符串。
        :type RuleTag: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Proto = None
        self._Port = None
        self._OriginType = None
        self._OriginValue = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._OriginPort = None
        self._RuleTag = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Proto(self):
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def OriginValue(self):
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def ForwardClientIp(self):
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def OriginPort(self):
        return self._OriginPort

    @OriginPort.setter
    def OriginPort(self, OriginPort):
        self._OriginPort = OriginPort

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._OriginType = params.get("OriginType")
        self._OriginValue = params.get("OriginValue")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._OriginPort = params.get("OriginPort")
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationProxyRuleResponse(AbstractModel):
    """CreateApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateOriginGroupRequest(AbstractModel):
    """CreateOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID
        :type ZoneId: str
        :param _Name: 源站组名称，可输入1 - 200个字符，允许的字符为 a - z, A - Z, 0 - 9, _, - 。
        :type Name: str
        :param _Type: 源站组类型，此参数必填，取值有：
<li>GENERAL：通用型源站组，仅支持添加 IP/域名 源站，可以被域名服务、规则引擎、四层代理、通用型负载均衡、HTTP 专用型负载均衡引用；</li>
<li>HTTP： HTTP 专用型源站组，支持添加 IP/域名、对象存储源站作为源站，无法被四层代理引用，仅支持被添加加速域名、规则引擎-修改源站、HTTP 专用型负载均衡引用。</li>
        :type Type: str
        :param _Records: 源站记录信息，此参数必填。
        :type Records: list of OriginRecord
        :param _HostHeader: 回源 Host Header，仅 Type = HTTP 时传入生效，规则引擎修改 Host Header 配置优先级高于源站组的 Host Header。
        :type HostHeader: str
        """
        self._ZoneId = None
        self._Name = None
        self._Type = None
        self._Records = None
        self._HostHeader = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def HostHeader(self):
        return self._HostHeader

    @HostHeader.setter
    def HostHeader(self, HostHeader):
        self._HostHeader = HostHeader


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOriginGroupResponse(AbstractModel):
    """CreateOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginGroupId: 源站组ID。
        :type OriginGroupId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginGroupId = None
        self._RequestId = None

    @property
    def OriginGroupId(self):
        return self._OriginGroupId

    @OriginGroupId.setter
    def OriginGroupId(self, OriginGroupId):
        self._OriginGroupId = OriginGroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OriginGroupId = params.get("OriginGroupId")
        self._RequestId = params.get("RequestId")


class CreatePlanForZoneRequest(AbstractModel):
    """CreatePlanForZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _PlanType: 所要购买套餐的类型，取值有：
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
        self._ZoneId = None
        self._PlanType = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PlanType(self):
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePlanForZoneResponse(AbstractModel):
    """CreatePlanForZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceNames: 购买的资源名字列表。
        :type ResourceNames: list of str
        :param _DealNames: 购买的订单号列表。
        :type DealNames: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceNames = None
        self._DealNames = None
        self._RequestId = None

    @property
    def ResourceNames(self):
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames

    @property
    def DealNames(self):
        return self._DealNames

    @DealNames.setter
    def DealNames(self, DealNames):
        self._DealNames = DealNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceNames = params.get("ResourceNames")
        self._DealNames = params.get("DealNames")
        self._RequestId = params.get("RequestId")


class CreatePrefetchTaskRequest(AbstractModel):
    """CreatePrefetchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Targets: 要预热的资源列表，每个元素格式类似如下:
http://www.example.com/example.txt。
注意：提交任务数受计费套餐配额限制，请查看 [EO计费套餐](https://cloud.tencent.com/document/product/1552/77380)。
        :type Targets: list of str
        :param _EncodeUrl: 是否对url进行encode，若内容含有非 ASCII 字符集的字符，请开启此开关进行编码转换（编码规则遵循 RFC3986）。
        :type EncodeUrl: bool
        :param _Headers: 附带的http头部信息。
        :type Headers: list of Header
        """
        self._ZoneId = None
        self._Targets = None
        self._EncodeUrl = None
        self._Headers = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EncodeUrl(self):
        return self._EncodeUrl

    @EncodeUrl.setter
    def EncodeUrl(self, EncodeUrl):
        self._EncodeUrl = EncodeUrl

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Targets = params.get("Targets")
        self._EncodeUrl = params.get("EncodeUrl")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrefetchTaskResponse(AbstractModel):
    """CreatePrefetchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        :param _FailedList: 失败的任务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._FailedList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def FailedList(self):
        return self._FailedList

    @FailedList.setter
    def FailedList(self, FailedList):
        self._FailedList = FailedList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self._FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self._FailedList.append(obj)
        self._RequestId = params.get("RequestId")


class CreatePurgeTaskRequest(AbstractModel):
    """CreatePurgeTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Type: 节点缓存清除类型，取值有：
<li>purge_url：URL刷新；</li>
<li>purge_prefix：目录刷新；</li>
<li>purge_host：Hostname 刷新；</li>
<li>purge_all：站点下全部缓存刷新；</li>
<li>purge_cache_tag：cache-tag 刷新。</li>缓存清除类型详情请查看[清除缓存](https://cloud.tencent.com/document/product/1552/70759)。
        :type Type: str
        :param _Method: 节点缓存清除方法，针对目录刷新、Hostname刷新以及刷新全部缓存 类型有效，取值有：<li> invalidate：仅刷新目录下产生了更新的资源；</li><li> delete：无论目录下资源是否更新都刷新节点资源。</li>注意：使用目录刷新时，默认值： invalidate。
        :type Method: str
        :param _Targets: 要清除缓存的资源列表。每个元素格式依据清除缓存类型而定，可参考接口示例。<li>EO 默认针对内容含有非 ASCII 字符集的字符进行转义，编码规则遵循 RFC3986；</li><li>单次提交的任务数受计费套餐配额限制，请查看 [EO计费套餐](https://cloud.tencent.com/document/product/1552/77380)。</li>
        :type Targets: list of str
        :param _EncodeUrl: 若有编码转换，仅清除编码转换后匹配的资源。
若内容含有非 ASCII 字符集的字符，请开启此开关进行编码转换（编码规则遵循 RFC3986）。
        :type EncodeUrl: bool
        """
        self._ZoneId = None
        self._Type = None
        self._Method = None
        self._Targets = None
        self._EncodeUrl = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def EncodeUrl(self):
        warnings.warn("parameter `EncodeUrl` is deprecated", DeprecationWarning) 

        return self._EncodeUrl

    @EncodeUrl.setter
    def EncodeUrl(self, EncodeUrl):
        warnings.warn("parameter `EncodeUrl` is deprecated", DeprecationWarning) 

        self._EncodeUrl = EncodeUrl


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        self._Method = params.get("Method")
        self._Targets = params.get("Targets")
        self._EncodeUrl = params.get("EncodeUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePurgeTaskResponse(AbstractModel):
    """CreatePurgeTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        :param _FailedList: 失败的任务列表及原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedList: list of FailReason
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._FailedList = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def FailedList(self):
        return self._FailedList

    @FailedList.setter
    def FailedList(self, FailedList):
        self._FailedList = FailedList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("FailedList") is not None:
            self._FailedList = []
            for item in params.get("FailedList"):
                obj = FailReason()
                obj._deserialize(item)
                self._FailedList.append(obj)
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _RuleName: 规则名称，名称字符串长度 1～255。
        :type RuleName: str
        :param _Status: 规则状态，取值有：
<li> enable: 启用； </li>
<li> disable: 未启用。</li>
        :type Status: str
        :param _Rules: 规则内容。
        :type Rules: list of Rule
        :param _Tags: 规则标签。
        :type Tags: list of str
        """
        self._ZoneId = None
        self._RuleName = None
        self._Status = None
        self._Rules = None
        self._Tags = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Tags = params.get("Tags")
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
        :param _RuleId: 规则 ID。
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateSecurityIPGroupRequest(AbstractModel):
    """CreateSecurityIPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 Id。
        :type ZoneId: str
        :param _IPGroup: IP 组信息。
        :type IPGroup: :class:`tencentcloud.teo.v20220901.models.IPGroup`
        """
        self._ZoneId = None
        self._IPGroup = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IPGroup(self):
        return self._IPGroup

    @IPGroup.setter
    def IPGroup(self, IPGroup):
        self._IPGroup = IPGroup


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("IPGroup") is not None:
            self._IPGroup = IPGroup()
            self._IPGroup._deserialize(params.get("IPGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityIPGroupResponse(AbstractModel):
    """CreateSecurityIPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: IP 组 Id。
        :type GroupId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateSharedCNAMERequest(AbstractModel):
    """CreateSharedCNAME请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 共享 CNAME 所属站点的 ID。	
        :type ZoneId: str
        :param _SharedCNAMEPrefix: 共享 CNAME 前缀。请输入合法的域名前缀，例如"test-api"、"test-api.com"，限制输入 50 个字符。

共享 CNAME 完整格式为：<自定义前缀>+<zoneid中的12位随机字符串>+"share.eo.dnse[0-5].com"。

例如前缀传入 example.com，EO 会为您创建共享 CNAME：example.com.sai2ig51kaa5.share.eo.dnse2.com
        :type SharedCNAMEPrefix: str
        :param _Description: 描述。可输入 1-50 个任意字符。
        :type Description: str
        """
        self._ZoneId = None
        self._SharedCNAMEPrefix = None
        self._Description = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SharedCNAMEPrefix(self):
        return self._SharedCNAMEPrefix

    @SharedCNAMEPrefix.setter
    def SharedCNAMEPrefix(self, SharedCNAMEPrefix):
        self._SharedCNAMEPrefix = SharedCNAMEPrefix

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._SharedCNAMEPrefix = params.get("SharedCNAMEPrefix")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSharedCNAMEResponse(AbstractModel):
    """CreateSharedCNAME返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SharedCNAME: 共享 CNAME。格式为：<自定义前缀>+<ZoneId中的12位随机字符串>+"share.eo.dnse[0-5].com"
        :type SharedCNAME: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SharedCNAME = None
        self._RequestId = None

    @property
    def SharedCNAME(self):
        return self._SharedCNAME

    @SharedCNAME.setter
    def SharedCNAME(self, SharedCNAME):
        self._SharedCNAME = SharedCNAME

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SharedCNAME = params.get("SharedCNAME")
        self._RequestId = params.get("RequestId")


class CreateZoneRequest(AbstractModel):
    """CreateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 站点接入类型。该参数取值如下，不填写时默认为 partial：
<li>partial：CNAME 接入；</li>
<li> full：NS 接入；</li>
<li>noDomainAccess：无域名接入。</li>
        :type Type: str
        :param _ZoneName: 站点名称。CNAME/NS 接入的时，请传入二级域名（example.com）作为站点名称；无域名接入时，该值请保留为空。
        :type ZoneName: str
        :param _Area: Type 取值为 partial/full 时，七层域名的加速区域。以下为该参数取值，不填写时该值默认为 overseas。Type 取值为 noDomainAccess 时该值请保留为空：
<li> global: 全球可用区；</li>
<li> mainland: 中国大陆可用区；</li>
<li> overseas: 全球可用区（不含中国大陆）。</li>
        :type Area: str
        :param _PlanId: 待绑定的目标套餐 ID。当您账号下已存在套餐时，可以填写此参数，直接将站点绑定至该套餐。若您当前没有可绑定的套餐时，请前往控制台购买套餐完成站点创建。
        :type PlanId: str
        :param _AliasZoneName: 同名站点标识。限制输入数字、英文、- 和 _ 组合，长度 20 个字符以内。详情参考 [同名站点标识](https://cloud.tencent.com/document/product/1552/70202)，无此使用场景时，该字段保留为空即可。
        :type AliasZoneName: str
        :param _Tags: 标签。该参数用于对站点进行分权限管控、分账。需要先前往 [标签控制台](https://console.cloud.tencent.com/tag/taglist) 创建对应的标签才可以在此处传入对应的标签键和标签值。
        :type Tags: list of Tag
        :param _AllowDuplicates: 是否允许重复接入。
<li> true：允许重复接入；</li>
<li> false：不允许重复接入。</li>不填写使用默认值false。
        :type AllowDuplicates: bool
        :param _JumpStart: 是否跳过站点现有的DNS记录扫描。默认值：false。
        :type JumpStart: bool
        """
        self._Type = None
        self._ZoneName = None
        self._Area = None
        self._PlanId = None
        self._AliasZoneName = None
        self._Tags = None
        self._AllowDuplicates = None
        self._JumpStart = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def AliasZoneName(self):
        return self._AliasZoneName

    @AliasZoneName.setter
    def AliasZoneName(self, AliasZoneName):
        self._AliasZoneName = AliasZoneName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AllowDuplicates(self):
        warnings.warn("parameter `AllowDuplicates` is deprecated", DeprecationWarning) 

        return self._AllowDuplicates

    @AllowDuplicates.setter
    def AllowDuplicates(self, AllowDuplicates):
        warnings.warn("parameter `AllowDuplicates` is deprecated", DeprecationWarning) 

        self._AllowDuplicates = AllowDuplicates

    @property
    def JumpStart(self):
        warnings.warn("parameter `JumpStart` is deprecated", DeprecationWarning) 

        return self._JumpStart

    @JumpStart.setter
    def JumpStart(self, JumpStart):
        warnings.warn("parameter `JumpStart` is deprecated", DeprecationWarning) 

        self._JumpStart = JumpStart


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ZoneName = params.get("ZoneName")
        self._Area = params.get("Area")
        self._PlanId = params.get("PlanId")
        self._AliasZoneName = params.get("AliasZoneName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AllowDuplicates = params.get("AllowDuplicates")
        self._JumpStart = params.get("JumpStart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateZoneResponse(AbstractModel):
    """CreateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _OwnershipVerification: 站点归属权验证信息。站点完成创建后，您还需要完成归属权校验，站点才能正常服务。

Type = partial 时，您需要参考 [站点/域名归属权验证](https://cloud.tencent.com/document/product/1552/70789) 前往您的域名解析服务商添加 TXT 记录或者前往根域名服务器添加文件，再调用接口 [VerifyOwnership]() 完成验证；

Type = full 时，您需要参考 [修改 DNS 服务器](https://cloud.tencent.com/document/product/1552/90452) 切换 DNS 服务器即可，可通过接口 [VerifyOwnership]() 查询 DNS 是否切换成功；

Type = noDomainAccess 时，该值为空，不需要进行任何操作。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._OwnershipVerification = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        self._RequestId = params.get("RequestId")


class DDoS(AbstractModel):
    """DDoS配置

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackEvent(AbstractModel):
    """DDoS攻击事件对象

    """

    def __init__(self):
        r"""
        :param _EventId: 事件ID。
        :type EventId: str
        :param _AttackType: 攻击类型(对应交互事件名称)。
        :type AttackType: str
        :param _AttackStatus: 攻击状态。
        :type AttackStatus: int
        :param _AttackMaxBandWidth: 攻击最大带宽。
        :type AttackMaxBandWidth: int
        :param _AttackPacketMaxRate: 攻击包速率峰值。
        :type AttackPacketMaxRate: int
        :param _AttackStartTime: 攻击开始时间，单位为s。
        :type AttackStartTime: int
        :param _AttackEndTime: 攻击结束时间，单位为s。
        :type AttackEndTime: int
        :param _PolicyId: DDoS策略组ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _ZoneId: 站点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _Area: 攻击事件所属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param _DDoSBlockData: 封禁解封信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DDoSBlockData: list of DDoSBlockData
        """
        self._EventId = None
        self._AttackType = None
        self._AttackStatus = None
        self._AttackMaxBandWidth = None
        self._AttackPacketMaxRate = None
        self._AttackStartTime = None
        self._AttackEndTime = None
        self._PolicyId = None
        self._ZoneId = None
        self._Area = None
        self._DDoSBlockData = None

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def AttackMaxBandWidth(self):
        return self._AttackMaxBandWidth

    @AttackMaxBandWidth.setter
    def AttackMaxBandWidth(self, AttackMaxBandWidth):
        self._AttackMaxBandWidth = AttackMaxBandWidth

    @property
    def AttackPacketMaxRate(self):
        return self._AttackPacketMaxRate

    @AttackPacketMaxRate.setter
    def AttackPacketMaxRate(self, AttackPacketMaxRate):
        self._AttackPacketMaxRate = AttackPacketMaxRate

    @property
    def AttackStartTime(self):
        return self._AttackStartTime

    @AttackStartTime.setter
    def AttackStartTime(self, AttackStartTime):
        self._AttackStartTime = AttackStartTime

    @property
    def AttackEndTime(self):
        return self._AttackEndTime

    @AttackEndTime.setter
    def AttackEndTime(self, AttackEndTime):
        self._AttackEndTime = AttackEndTime

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def DDoSBlockData(self):
        return self._DDoSBlockData

    @DDoSBlockData.setter
    def DDoSBlockData(self, DDoSBlockData):
        self._DDoSBlockData = DDoSBlockData


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._AttackType = params.get("AttackType")
        self._AttackStatus = params.get("AttackStatus")
        self._AttackMaxBandWidth = params.get("AttackMaxBandWidth")
        self._AttackPacketMaxRate = params.get("AttackPacketMaxRate")
        self._AttackStartTime = params.get("AttackStartTime")
        self._AttackEndTime = params.get("AttackEndTime")
        self._PolicyId = params.get("PolicyId")
        self._ZoneId = params.get("ZoneId")
        self._Area = params.get("Area")
        if params.get("DDoSBlockData") is not None:
            self._DDoSBlockData = []
            for item in params.get("DDoSBlockData"):
                obj = DDoSBlockData()
                obj._deserialize(item)
                self._DDoSBlockData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSBlockData(AbstractModel):
    """DDoS封禁解封信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，采用unix时间戳。
        :type StartTime: int
        :param _EndTime: 结束时间，采用unix时间戳, 为0表示还处于封禁中。
        :type EndTime: int
        :param _BlockArea: 封禁受影响区域。
        :type BlockArea: str
        """
        self._StartTime = None
        self._EndTime = None
        self._BlockArea = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BlockArea(self):
        return self._BlockArea

    @BlockArea.setter
    def BlockArea(self, BlockArea):
        self._BlockArea = BlockArea


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._BlockArea = params.get("BlockArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultServerCertInfo(AbstractModel):
    """https 服务端证书配置

    """

    def __init__(self):
        r"""
        :param _CertId: 服务器证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _Alias: 证书备注名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Type: 证书类型，取值有：
<li>default: 默认证书;</li>
<li>upload:用户上传;</li>
<li>managed:腾讯云托管。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _EffectiveTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectiveTime: str
        :param _CommonName: 证书公用名。
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        :param _SubjectAltName: 证书SAN域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param _Status: 部署状态，取值有：
<li>processing: 部署中；</li>
<li>deployed: 已部署；</li>
<li>failed: 部署失败。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Message: Status为失败时,此字段返回失败原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _SignAlgo: 证书算法。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignAlgo: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._EffectiveTime = None
        self._CommonName = None
        self._SubjectAltName = None
        self._Status = None
        self._Message = None
        self._SignAlgo = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def EffectiveTime(self):
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def CommonName(self):
        return self._CommonName

    @CommonName.setter
    def CommonName(self, CommonName):
        self._CommonName = CommonName

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def SignAlgo(self):
        return self._SignAlgo

    @SignAlgo.setter
    def SignAlgo(self, SignAlgo):
        self._SignAlgo = SignAlgo


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._EffectiveTime = params.get("EffectiveTime")
        self._CommonName = params.get("CommonName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._SignAlgo = params.get("SignAlgo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerationDomainsRequest(AbstractModel):
    """DeleteAccelerationDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param _DomainNames: 需要删除的加速域名ID列表。
        :type DomainNames: list of str
        :param _Force: 是否强制删除。当域名存在关联资源（如马甲域名、流量调度功能）时，是否强制删除该域名，取值有：
<li> true：删除该域名及所有关联资源；</li>
<li> false：当该加速域名存在关联资源时，不允许删除。</li>不填写，默认值为：false。
        :type Force: bool
        """
        self._ZoneId = None
        self._DomainNames = None
        self._Force = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainNames(self):
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainNames = params.get("DomainNames")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerationDomainsResponse(AbstractModel):
    """DeleteAccelerationDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAliasDomainRequest(AbstractModel):
    """DeleteAliasDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _AliasNames: 待删除别称域名名称。如果为空，则不执行删除操作。
        :type AliasNames: list of str
        """
        self._ZoneId = None
        self._AliasNames = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasNames(self):
        return self._AliasNames

    @AliasNames.setter
    def AliasNames(self, AliasNames):
        self._AliasNames = AliasNames


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasDomainResponse(AbstractModel):
    """DeleteAliasDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteApplicationProxyRequest(AbstractModel):
    """DeleteApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _ProxyId: 代理ID。
        :type ProxyId: str
        """
        self._ZoneId = None
        self._ProxyId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyResponse(AbstractModel):
    """DeleteApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteApplicationProxyRuleRequest(AbstractModel):
    """DeleteApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _ProxyId: 代理ID。
        :type ProxyId: str
        :param _RuleId: 规则ID。
        :type RuleId: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationProxyRuleResponse(AbstractModel):
    """DeleteApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteOriginGroupRequest(AbstractModel):
    """DeleteOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _GroupId: 源站组ID，此参数必填。
        :type GroupId: str
        """
        self._ZoneId = None
        self._GroupId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOriginGroupResponse(AbstractModel):
    """DeleteOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRulesRequest(AbstractModel):
    """DeleteRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _RuleIds: 指定删除的规则 ID 列表。
        :type RuleIds: list of str
        """
        self._ZoneId = None
        self._RuleIds = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRulesResponse(AbstractModel):
    """DeleteRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSecurityIPGroupRequest(AbstractModel):
    """DeleteSecurityIPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 Id。
        :type ZoneId: str
        :param _GroupId: IP 组 Id。
        :type GroupId: int
        """
        self._ZoneId = None
        self._GroupId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityIPGroupResponse(AbstractModel):
    """DeleteSecurityIPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteZoneRequest(AbstractModel):
    """DeleteZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteZoneResponse(AbstractModel):
    """DeleteZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccelerationDomainsRequest(AbstractModel):
    """DescribeAccelerationDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 加速域名所属站点 ID。
        :type ZoneId: str
        :param _Offset: 分页查询偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认值：20，上限：200。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values 的上限为 20。该参数不填写时，返回当前 zone-id 下所有域名信息。详细的过滤条件如下：
<li>domain-name：按照加速域名进行过滤；</li>
<li>origin-type：按照源站类型进行过滤；</li>
<li>origin：按照主源站地址进行过滤；</li>
<li>backup-origin： 按照备用源站地址进行过滤；</li>
<li>domain-cname：按照 CNAME 进行过滤；</li>
<li>share-cname：按照共享 CNAME 进行过滤；</li>
        :type Filters: list of AdvancedFilter
        :param _Order: 可根据该字段对返回结果进行排序，取值有：
<li>created_on：加速域名创建时间；</li>
<li>domain-name：加速域名。</li>不填写时，默认对返回结果按照 domain-name 排序。
        :type Order: str
        :param _Direction: 排序方向，如果是字段值为数字，则根据数字大小排序；如果字段值为文本，则根据 ascill 码的大小排序。取值有：
<li>asc：升序排列；</li>
<li>desc：降序排列。</li>不填写使用默认值 asc。
        :type Direction: str
        :param _Match: 匹配方式，取值有：
<li>all：返回匹配所有查询条件的加速域名；</li>
<li>any：返回匹配任意一个查询条件的加速域名。</li>不填写时默认值为 all。
        :type Match: str
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._Direction = None
        self._Match = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Match(self):
        return self._Match

    @Match.setter
    def Match(self, Match):
        self._Match = Match


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._Direction = params.get("Direction")
        self._Match = params.get("Match")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccelerationDomainsResponse(AbstractModel):
    """DescribeAccelerationDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合查询条件的加速域名个数。
        :type TotalCount: int
        :param _AccelerationDomains: 符合查询条件的所有加速域名的信息。
        :type AccelerationDomains: list of AccelerationDomain
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccelerationDomains = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccelerationDomains(self):
        return self._AccelerationDomains

    @AccelerationDomains.setter
    def AccelerationDomains(self, AccelerationDomains):
        self._AccelerationDomains = AccelerationDomains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccelerationDomains") is not None:
            self._AccelerationDomains = []
            for item in params.get("AccelerationDomains"):
                obj = AccelerationDomain()
                obj._deserialize(item)
                self._AccelerationDomains.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAliasDomainsRequest(AbstractModel):
    """DescribeAliasDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param _Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>target-name<br>   按照【<strong>目标域名名称</strong>】进行过滤。<br>   类型：String<br>   必选：否</li><li>alias-name<br>   按照【<strong>别称域名名称</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>模糊查询时仅支持过滤字段名为alias-name。
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAliasDomainsResponse(AbstractModel):
    """DescribeAliasDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的别称域名个数。
        :type TotalCount: int
        :param _AliasDomains: 别称域名详细信息列表。
        :type AliasDomains: list of AliasDomain
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AliasDomains = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AliasDomains(self):
        return self._AliasDomains

    @AliasDomains.setter
    def AliasDomains(self, AliasDomains):
        self._AliasDomains = AliasDomains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AliasDomains") is not None:
            self._AliasDomains = []
            for item in params.get("AliasDomains"):
                obj = AliasDomain()
                obj._deserialize(item)
                self._AliasDomains.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationProxiesRequest(AbstractModel):
    """DescribeApplicationProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询偏移量。默认为0。
        :type Offset: int
        :param _Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：<li>proxy-id<br>   按照【<strong>代理ID</strong>】进行过滤。代理ID形如：proxy-ev2sawbwfd。<br>   类型：String<br>   必选：否</li><li>zone-id<br>   按照【<strong>站点ID</strong>】进行过滤。站点ID形如：zone-vawer2vadg。<br>   类型：String<br>   必选：否</li><li>rule-tag<br>   按照【<strong>规则标签</strong>】对应用代理下的规则进行过滤。规则标签形如：rule-service-1。<br>   类型：String<br>   必选：否</li>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationProxiesResponse(AbstractModel):
    """DescribeApplicationProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationProxies: 应用代理列表。
        :type ApplicationProxies: list of ApplicationProxy
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationProxies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApplicationProxies(self):
        return self._ApplicationProxies

    @ApplicationProxies.setter
    def ApplicationProxies(self, ApplicationProxies):
        self._ApplicationProxies = ApplicationProxies

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplicationProxies") is not None:
            self._ApplicationProxies = []
            for item in params.get("ApplicationProxies"):
                obj = ApplicationProxy()
                obj._deserialize(item)
                self._ApplicationProxies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAvailablePlansRequest(AbstractModel):
    """DescribeAvailablePlans请求参数结构体

    """


class DescribeAvailablePlansResponse(AbstractModel):
    """DescribeAvailablePlans返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanInfo: 当前账户可购买套餐类型及相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PlanInfo: list of PlanInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanInfo = None
        self._RequestId = None

    @property
    def PlanInfo(self):
        return self._PlanInfo

    @PlanInfo.setter
    def PlanInfo(self, PlanInfo):
        self._PlanInfo = PlanInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlanInfo") is not None:
            self._PlanInfo = []
            for item in params.get("PlanInfo"):
                obj = PlanInfo()
                obj._deserialize(item)
                self._PlanInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeContentQuotaRequest(AbstractModel):
    """DescribeContentQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentQuotaResponse(AbstractModel):
    """DescribeContentQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PurgeQuota: 刷新相关配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type PurgeQuota: list of Quota
        :param _PrefetchQuota: 预热相关配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrefetchQuota: list of Quota
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PurgeQuota = None
        self._PrefetchQuota = None
        self._RequestId = None

    @property
    def PurgeQuota(self):
        return self._PurgeQuota

    @PurgeQuota.setter
    def PurgeQuota(self, PurgeQuota):
        self._PurgeQuota = PurgeQuota

    @property
    def PrefetchQuota(self):
        return self._PrefetchQuota

    @PrefetchQuota.setter
    def PrefetchQuota(self, PrefetchQuota):
        self._PrefetchQuota = PrefetchQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PurgeQuota") is not None:
            self._PurgeQuota = []
            for item in params.get("PurgeQuota"):
                obj = Quota()
                obj._deserialize(item)
                self._PurgeQuota.append(obj)
        if params.get("PrefetchQuota") is not None:
            self._PrefetchQuota = []
            for item in params.get("PrefetchQuota"):
                obj = Quota()
                obj._deserialize(item)
                self._PrefetchQuota.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackDataRequest(AbstractModel):
    """DescribeDDoSAttackData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricNames: 统计指标列表，取值有：
<li>ddos_attackMaxBandwidth：攻击带宽峰值；</li>
<li>ddos_attackMaxPackageRate：攻击包速率峰值 ；</li>
<li>ddos_attackBandwidth：攻击带宽曲线；</li>
<li>ddos_attackPackageRate：攻击包速率曲线。</li>
        :type MetricNames: list of str
        :param _ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param _PolicyIds: DDoS策略组ID列表，不填默认选择全部策略ID。
        :type PolicyIds: list of int
        :param _Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间与结束时间的间隔自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._PolicyIds = None
        self._Interval = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._PolicyIds = params.get("PolicyIds")
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackDataResponse(AbstractModel):
    """DescribeDDoSAttackData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: DDoS攻击数据内容列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of SecEntry
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackEventRequest(AbstractModel):
    """DescribeDDoSAttackEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _PolicyIds: ddos策略组集合，不填默认选择全部策略。
        :type PolicyIds: list of int
        :param _ZoneIds: 站点集合，此参数必填，不填默认查询为空。
        :type ZoneIds: list of str
        :param _Limit: 分页查询的限制数目，默认值为20，最大查询条目为1000。
        :type Limit: int
        :param _Offset: 分页的偏移量，默认值为0。
        :type Offset: int
        :param _ShowDetail: 是否展示详细信息。
        :type ShowDetail: bool
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据；</li>不填默认取值为global。
        :type Area: str
        :param _OrderBy: 排序字段，取值有：
<li>MaxBandWidth：带宽峰值；</li>
<li>AttackStartTime：攻击开始时间。</li>不填默认值为：AttackStartTime。
        :type OrderBy: str
        :param _OrderType: 排序方式，取值有：
<li>asc：升序方式；</li>
<li>desc：降序方式。</li>不填默认值为：desc。
        :type OrderType: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PolicyIds = None
        self._ZoneIds = None
        self._Limit = None
        self._Offset = None
        self._ShowDetail = None
        self._Area = None
        self._OrderBy = None
        self._OrderType = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ShowDetail(self):
        return self._ShowDetail

    @ShowDetail.setter
    def ShowDetail(self, ShowDetail):
        self._ShowDetail = ShowDetail

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PolicyIds = params.get("PolicyIds")
        self._ZoneIds = params.get("ZoneIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ShowDetail = params.get("ShowDetail")
        self._Area = params.get("Area")
        self._OrderBy = params.get("OrderBy")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackEventResponse(AbstractModel):
    """DescribeDDoSAttackEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: DDOS攻击事件数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DDoSAttackEvent
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSAttackEvent()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackTopDataRequest(AbstractModel):
    """DescribeDDoSAttackTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricName: 查询的统计指标，取值有：
<li>ddos_attackFlux_protocol：按各协议的攻击流量排行；</li>
<li>ddos_attackPackageNum_protocol：按各协议的攻击包量排行；</li>
<li>ddos_attackNum_attackType：按各攻击类型的攻击数量排行；</li>
<li>ddos_attackNum_sregion：按攻击源地区的攻击数量排行；</li>
<li>ddos_attackFlux_sip：按攻击源IP的攻击数量排行；</li>
<li>ddos_attackFlux_sregion：按攻击源地区的攻击数量排行。</li>
        :type MetricName: str
        :param _ZoneIds: 站点ID集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param _PolicyIds: DDoS策略组ID集合，不填默认选择全部策略ID。
        :type PolicyIds: list of int
        :param _AttackType: 攻击类型，取值有：
<li>flood：洪泛攻击；</li>
<li>icmpFlood：icmp洪泛攻击；</li>
<li>all：所有的攻击类型。</li>不填默认为all，表示查询全部攻击类型。
        :type AttackType: str
        :param _ProtocolType: 协议类型，取值有：
<li>tcp：tcp协议；</li>
<li>udp：udp协议；</li>
<li>all：所有的协议类型。</li>不填默认为all，表示查询所有协议。
        :type ProtocolType: str
        :param _Port: 端口号。
        :type Port: int
        :param _Limit: 查询前多少个数据，不填默认默认为10， 表示查询前top 10的数据。
        :type Limit: int
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据。</li>不填将根据用户所在地智能选择地区。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._ZoneIds = None
        self._PolicyIds = None
        self._AttackType = None
        self._ProtocolType = None
        self._Port = None
        self._Limit = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def PolicyIds(self):
        return self._PolicyIds

    @PolicyIds.setter
    def PolicyIds(self, PolicyIds):
        self._PolicyIds = PolicyIds

    @property
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def ProtocolType(self):
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._ZoneIds = params.get("ZoneIds")
        self._PolicyIds = params.get("PolicyIds")
        self._AttackType = params.get("AttackType")
        self._ProtocolType = params.get("ProtocolType")
        self._Port = params.get("Port")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackTopDataResponse(AbstractModel):
    """DescribeDDoSAttackTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: DDoS攻击Top数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopEntry
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopEntry()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDefaultCertificatesRequest(AbstractModel):
    """DescribeDefaultCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，Filters.Values的上限为5。详细的过滤条件如下：
<li>zone-id<br>   按照【<strong>站点ID</strong>】进行过滤。站点ID形如：zone-xxx。<br>   类型：String<br>   必选：是 </li>
        :type Filters: list of Filter
        :param _Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param _Limit: 分页查询限制数目。默认值：20，最大值：100。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultCertificatesResponse(AbstractModel):
    """DescribeDefaultCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 证书总数。
        :type TotalCount: int
        :param _DefaultServerCertInfo: 默认证书列表。
        :type DefaultServerCertInfo: list of DefaultServerCertInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DefaultServerCertInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DefaultServerCertInfo(self):
        return self._DefaultServerCertInfo

    @DefaultServerCertInfo.setter
    def DefaultServerCertInfo(self, DefaultServerCertInfo):
        self._DefaultServerCertInfo = DefaultServerCertInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DefaultServerCertInfo") is not None:
            self._DefaultServerCertInfo = []
            for item in params.get("DefaultServerCertInfo"):
                obj = DefaultServerCertInfo()
                obj._deserialize(item)
                self._DefaultServerCertInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostsSettingRequest(AbstractModel):
    """DescribeHostsSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _Offset: 分页查询偏移量。默认值： 0，最小值：0。
        :type Offset: int
        :param _Limit: 分页查询限制数目。默认值： 100，最大值：1000。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>host<br>   按照【<strong>域名</strong>】进行过滤。<br>   类型：string<br>   必选：否</li>
        :type Filters: list of Filter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostsSettingResponse(AbstractModel):
    """DescribeHostsSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetailHosts: 域名列表。
        :type DetailHosts: list of DetailHost
        :param _TotalNumber: 域名数量。
        :type TotalNumber: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetailHosts = None
        self._TotalNumber = None
        self._RequestId = None

    @property
    def DetailHosts(self):
        return self._DetailHosts

    @DetailHosts.setter
    def DetailHosts(self, DetailHosts):
        self._DetailHosts = DetailHosts

    @property
    def TotalNumber(self):
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DetailHosts") is not None:
            self._DetailHosts = []
            for item in params.get("DetailHosts"):
                obj = DetailHost()
                obj._deserialize(item)
                self._DetailHosts.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeIdentificationsRequest(AbstractModel):
    """DescribeIdentifications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>zone-name<br>   按照【<strong>站点名称</strong>】进行过滤。<br>   类型：String<br>   必选：是</li>
        :type Filters: list of Filter
        :param _Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param _Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdentificationsResponse(AbstractModel):
    """DescribeIdentifications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的站点个数。
        :type TotalCount: int
        :param _Identifications: 站点验证信息列表。
        :type Identifications: list of Identification
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Identifications = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Identifications(self):
        return self._Identifications

    @Identifications.setter
    def Identifications(self, Identifications):
        self._Identifications = Identifications

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Identifications") is not None:
            self._Identifications = []
            for item in params.get("Identifications"):
                obj = Identification()
                obj._deserialize(item)
                self._Identifications.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOriginGroupRequest(AbstractModel):
    """DescribeOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID，此参数必填。
        :type ZoneId: str
        :param _Offset: 分页查询偏移量，不填默认为0。
        :type Offset: int
        :param _Limit: 分页查询限制数目，不填默认为20，取值：1-1000。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>origin-group-id<br>   按照【<strong>源站组ID</strong>】进行过滤。源站组ID形如：origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a<br>   模糊查询：不支持</li><li>origin-group-name<br>   按照【<strong>源站组名称</strong>】进行过滤<br>   模糊查询：支持。使用模糊查询时，仅支持填写一个源站组名称</li>
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginGroupResponse(AbstractModel):
    """DescribeOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数。
        :type TotalCount: int
        :param _OriginGroups: 源站组信息。
        :type OriginGroups: list of OriginGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._OriginGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OriginGroups(self):
        return self._OriginGroups

    @OriginGroups.setter
    def OriginGroups(self, OriginGroups):
        self._OriginGroups = OriginGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("OriginGroups") is not None:
            self._OriginGroups = []
            for item in params.get("OriginGroups"):
                obj = OriginGroup()
                obj._deserialize(item)
                self._OriginGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOriginProtectionRequest(AbstractModel):
    """DescribeOriginProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneIds: 查询的站点集合，不填默认查询所有站点。
        :type ZoneIds: list of str
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>need-update<br>   按照【<strong>站点是否需要更新源站防护IP白名单</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   true：需要更新<br>   false：无需更新<br></li>
<li>plan-support<br>   按照【<strong>站点套餐是否支持源站防护</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   true：支持<br>   false：不支持<br></li>
        :type Filters: list of Filter
        :param _Offset: 分页查询偏移量，默认为0。
        :type Offset: int
        :param _Limit: 分页查询限制数目。默认值：20，最大值：1000。
        :type Limit: int
        """
        self._ZoneIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginProtectionResponse(AbstractModel):
    """DescribeOriginProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OriginProtectionInfo: 源站防护信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginProtectionInfo: list of OriginProtectionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OriginProtectionInfo = None
        self._RequestId = None

    @property
    def OriginProtectionInfo(self):
        return self._OriginProtectionInfo

    @OriginProtectionInfo.setter
    def OriginProtectionInfo(self, OriginProtectionInfo):
        self._OriginProtectionInfo = OriginProtectionInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OriginProtectionInfo") is not None:
            self._OriginProtectionInfo = []
            for item in params.get("OriginProtectionInfo"):
                obj = OriginProtectionInfo()
                obj._deserialize(item)
                self._OriginProtectionInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOverviewL7DataRequest(AbstractModel):
    """DescribeOverviewL7Data请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricNames: 查询的指标，取值有：
<li>l7Flow_outFlux: Edegone响应流量；</li>
<li>l7Flow_inFlux: Edgeone请求流量；</li>
<li>l7Flow_outBandwidth: Edegone响应带宽；</li>
<li>l7Flow_inBandwidth: Edegone请求带宽；</li>
<li>l7Flow_hit_outFlux: 缓存命中流量；</li>
<li>l7Flow_request: 访问请求数；</li>
<li>l7Flow_flux: 访问请求上行+下行流量；</li>
<li>l7Flow_bandwidth：访问请求上行+下行带宽。</li>
        :type MetricNames: list of str
        :param _ZoneIds: 站点集合。
若不填写，默认选择全部站点，且最多只能查询近30天的数据；若填写，则可查询站点绑定套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>。
        :type ZoneIds: list of str
        :param _Domains: 查询的域名集合，不填默认查询所有子域名。
        :type Domains: list of str
        :param _Protocol: 查询的协议类型，取值有：
<li>http: http协议；</li>
<li>https: https协议；</li>
<li>http2: http2协议；</li>
<li>all:  所有协议。</li>不填默认为all，此参数暂未生效。
        :type Protocol: str
        :param _Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param _Filters: 过滤条件，详细的过滤条件Key值如下：
<li>socket<br>   按照【<strong>HTTP协议类型</strong>】进行过滤。<br>   对应的Value可选项如下：<br>   HTTP：HTTP 协议；<br>   HTTPS：HTTPS协议；<br>   QUIC：QUIC协议。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。</li>
        :type Filters: list of QueryCondition
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Domains = None
        self._Protocol = None
        self._Interval = None
        self._Filters = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._Protocol = params.get("Protocol")
        self._Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewL7DataResponse(AbstractModel):
    """DescribeOverviewL7Data返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 七层监控类时序流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrefetchTasksRequest(AbstractModel):
    """DescribePrefetchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间。
        :type StartTime: str
        :param _EndTime: 查询结束时间。
        :type EndTime: str
        :param _Offset: 分页查询偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认值：20，上限：1000。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>zone-id<br>   按照【<strong>站点 ID</strong>】进行过滤。zone-id形如：zone-1379afjk91u32h，暂不支持多值。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>job-id<br>   按照【<strong>任务ID</strong>】进行过滤。job-id形如：1379afjk91u32h，暂不支持多值。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>target<br>   按照【<strong>目标资源信息</strong>】进行过滤。target形如：http://www.qq.com/1.txt，暂不支持多值。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>domains<br>   按照【<strong>域名</strong>】进行过滤。domains形如：www.qq.com。<br>   类型：String<br>   必选：否。<br>   模糊查询：不支持。</li><li>statuses<br>   按照【<strong>任务状态</strong>】进行过滤。<br>   必选：否<br>   模糊查询：不支持。<br>   可选项：<br>   processing：处理中<br>   success：成功<br>   failed：失败<br>   timeout：超时</li>
        :type Filters: list of AdvancedFilter
        """
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrefetchTasksResponse(AbstractModel):
    """DescribePrefetchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该查询条件总共条目数。
        :type TotalCount: int
        :param _Tasks: 任务结果列表。
        :type Tasks: list of Task
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 字段已废弃，请使用Filters中的zone-id。
        :type ZoneId: str
        :param _StartTime: 查询起始时间。
        :type StartTime: str
        :param _EndTime: 查询结束时间。
        :type EndTime: str
        :param _Offset: 分页查询偏移量，默认为0。
        :type Offset: int
        :param _Limit: 分页查限制数目，默认值：20，最大值：1000。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：<li>zone-id<br>   按照【<strong>站点 ID</strong>】进行过滤。zone-id形如：zone-xxx，暂不支持多值<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>job-id<br>   按照【<strong>任务ID</strong>】进行过滤。job-id形如：1379afjk91u32h，暂不支持多值。<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>target<br>   按照【<strong>目标资源信息</strong>】进行过滤，target形如：http://www.qq.com/1.txt或者tag1，暂不支持多值<br>   类型：String<br>   必选：否<br>   模糊查询：不支持</li><li>domains<br>   按照【<strong>域名</strong>】进行过滤，domains形如：www.qq.com<br>   类型：String<br>   必选：否<br>   模糊查询：不支持。</li><li>statuses<br>   按照【<strong>任务状态</strong>】进行过滤<br>   必选：否<br>   模糊查询：不支持。<br>   可选项：<br>   processing：处理中<br>   success：成功<br>   failed：失败<br>   timeout：超时</li><li>type<br>   按照【<strong>清除缓存类型</strong>】进行过滤，暂不支持多值。<br>   类型：String<br>   必选：否<br>   模糊查询：不支持<br>   可选项：<br>   purge_url：URL<br>   purge_prefix：前缀<br>   purge_all：全部缓存内容<br>   purge_host：Hostname<br>   purge_cache_tag：CacheTag</li>
        :type Filters: list of AdvancedFilter
        """
        self._ZoneId = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该查询条件总共条目数。
        :type TotalCount: int
        :param _Tasks: 任务结果列表。
        :type Tasks: list of Task
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tasks = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Filters: 过滤条件，Filters.Values的上限为20。详细的过滤条件如下：
<li>rule-id<br>   按照【<strong>规则ID</strong>】进行过滤。<br>   类型：string<br>   必选：否</li>
        :type Filters: list of Filter
        """
        self._ZoneId = None
        self._Filters = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _RuleItems: 规则列表，按规则执行顺序从先往后排序。
        :type RuleItems: list of RuleItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._RuleItems = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleItems(self):
        return self._RuleItems

    @RuleItems.setter
    def RuleItems(self, RuleItems):
        self._RuleItems = RuleItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("RuleItems") is not None:
            self._RuleItems = []
            for item in params.get("RuleItems"):
                obj = RuleItem()
                obj._deserialize(item)
                self._RuleItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesSettingRequest(AbstractModel):
    """DescribeRulesSetting请求参数结构体

    """


class DescribeRulesSettingResponse(AbstractModel):
    """DescribeRulesSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Actions: 规则引擎可应用匹配请求的设置列表及其详细建议配置信息。
        :type Actions: list of RulesSettingAction
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Actions = None
        self._RequestId = None

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RulesSettingAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityTemplateBindingsRequest(AbstractModel):
    """DescribeSecurityTemplateBindings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 要查询的站点 ID。
        :type ZoneId: str
        :param _TemplateId: 要查询的策略模板 ID。
        :type TemplateId: list of str
        """
        self._ZoneId = None
        self._TemplateId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityTemplateBindingsResponse(AbstractModel):
    """DescribeSecurityTemplateBindings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityTemplate: 指定策略模板的绑定关系列表。

当某个站点中的域名包含在指定策略模板的绑定关系中时，绑定关系列表 `TemplateScope` 中会包含该站点的 `ZoneId`，和该站点下的和该策略模板有关的域名绑定关系。

注意：当没有任何域名正在绑定或已经绑定到指定策略模板时，绑定关系为空。即：返回结构体中，`TemplateScope` 数组长度为 0。

绑定关系中，同一域名可能在 `EntityStatus` 列表中重复出现，并标记为不同 `Status` 。例如，正在被绑定到其他策略模板的域名，会同时标记为 `online` 和 `pending` 。
        :type SecurityTemplate: list of SecurityTemplateBinding
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityTemplate = None
        self._RequestId = None

    @property
    def SecurityTemplate(self):
        return self._SecurityTemplate

    @SecurityTemplate.setter
    def SecurityTemplate(self, SecurityTemplate):
        self._SecurityTemplate = SecurityTemplate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SecurityTemplate") is not None:
            self._SecurityTemplate = []
            for item in params.get("SecurityTemplate"):
                obj = SecurityTemplateBinding()
                obj._deserialize(item)
                self._SecurityTemplate.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimingL4DataRequest(AbstractModel):
    """DescribeTimingL4Data请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricNames: 查询指标，取值有：
<li>l4Flow_connections: 访问连接数；</li>
<li>l4Flow_flux: 访问总流量；</li>
<li>l4Flow_inFlux: 访问入流量；</li>
<li>l4Flow_outFlux: 访问出流量；</li>
<li> l4Flow_outPkt: 访问出包量。</li>
        :type MetricNames: list of str
        :param _ZoneIds: 站点集合。
若不填写，默认选择全部站点，且最多只能查询近30天的数据；
若填写，则可查询站点绑定套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>。
        :type ZoneIds: list of str
        :param _ProxyIds: 四层实例列表, 不填表示选择全部实例。
        :type ProxyIds: list of str
        :param _Interval: 查询时间粒度，取值有：
<li>min: 1分钟 ；</li>
<li>5min: 5分钟 ；</li>
<li>hour: 1小时 ；</li>
<li>day: 1天 。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param _Filters: 过滤条件，详细的过滤条件Key值如下：
<li>ruleId<br>   按照【<strong>转发规则ID</strong>】进行过滤。</li>
<li>proxyId<br>   按照【<strong>四层代理实例ID</strong>】进行过滤。</li>
        :type Filters: list of QueryCondition
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._ProxyIds = None
        self._Interval = None
        self._Filters = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._ProxyIds = params.get("ProxyIds")
        self._Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL4DataResponse(AbstractModel):
    """DescribeTimingL4Data返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 四层时序流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimingL7AnalysisDataRequest(AbstractModel):
    """DescribeTimingL7AnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricNames: 指标列表，取值有:
<li>l7Flow_outFlux: Edgeone响应流量；</li>
<li>l7Flow_inFlux: Edgeone请求流量；</li>
<li>l7Flow_outBandwidth: Edgeone响应带宽；</li>
<li>l7Flow_inBandwidth：Edgeone请求带宽；</li>
<li>l7Flow_request: 访问请求数；</li>
<li>l7Flow_flux: 访问请求上行+下行流量；</li>
<li>l7Flow_bandwidth：访问请求上行+下行带宽。</li>
        :type MetricNames: list of str
        :param _ZoneIds: 站点集合。
若不填写，默认选择全部站点，且最多只能查询近30天的数据；若填写，则可查询站点绑定套餐支持的<a href="https://cloud.tencent.com/document/product/1552/77380#edgeone-.E5.A5.97.E9.A4.90">数据分析最大查询范围</a>。
        :type ZoneIds: list of str
        :param _Interval: 查询时间粒度，取值有：
<li>min: 1分钟；</li>
<li>5min: 5分钟；</li>
<li>hour: 1小时；</li>
<li>day: 1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：1小时范围内以min粒度查询，2天范围内以5min粒度查询，7天范围内以hour粒度查询，超过7天以day粒度查询。
        :type Interval: str
        :param _Filters: 过滤条件，详细的过滤条件Key值如下：
<li>country<br>   按照【<strong>国家/地区</strong>】进行过滤，国家/地区遵循 <a href="https://baike.baidu.com/item/ISO%203166-1/5269555">ISO 3166</a> 规范。</li>
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
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Interval = None
        self._Filters = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        self._Interval = params.get("Interval")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7AnalysisDataResponse(AbstractModel):
    """DescribeTimingL7AnalysisData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 时序流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTimingL7CacheDataRequest(AbstractModel):
    """DescribeTimingL7CacheData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricNames: 查询的指标，取值有：
<li>l7Cache_outFlux：响应流量；</li>
<li>l7Cache_request：响应请求数；</li>
<li> l7Cache_outBandwidth：响应带宽。</li>
        :type MetricNames: list of str
        :param _ZoneIds: 站点集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param _Filters: 过滤条件，详细的过滤条件如下：
<li>domain<br>   按照【<strong>子域名</strong>】进行过滤，子域名形如： test.example.com。<br>   类型：String<br>   必选：否</li>
<li>url<br>   按照【<strong>URL</strong>】进行过滤，此参数只支持30天的时间范围，URL形如：/content。<br>   类型：String<br>   必选：否</li>
<li>resourceType<br>   按照【<strong>资源类型</strong>】进行过滤，此参数只支持30天的时间范围，资源类型形如：jpg，png。<br>   类型：String<br>   必选：否</li>
<li>cacheType<br>   按照【<strong>缓存类型</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   hit：命中缓存；<br>   dynamic：资源不可缓存；<br>   miss：未命中缓存。</li>
<li>statusCode<br>   按照【<strong>状态码</strong>】进行过滤，此参数只支持30天的时间范围。<br>   类型：String<br>   必选：否<br>   可选项：<br>   1XX：1xx类型的状态码；<br>   100：100状态码；<br>   101：101状态码；<br>   102：102状态码；<br>   2XX：2xx类型的状态码；<br>   200：200状态码；<br>   201：201状态码；<br>   202：202状态码；<br>   203：203状态码；<br>   204：204状态码；<br>   100：100状态码；<br>   206：206状态码；<br>   207：207状态码；<br>   3XX：3xx类型的状态码；<br>   300：300状态码；<br>   301：301状态码；<br>   302：302状态码；<br>   303：303状态码；<br>   304：304状态码；<br>   305：305状态码；<br>   307：307状态码；<br>   4XX：4xx类型的状态码；<br>   400：400状态码；<br>   401：401状态码；<br>   402：402状态码；<br>   403：403状态码；<br>   404：404状态码；<br>   405：405状态码；<br>   406：406状态码；<br>   407：407状态码；<br>   408：408状态码；<br>   409：409状态码；<br>   410：410状态码；<br>   411：411状态码；<br>   412：412状态码；<br>   412：413状态码；<br>   414：414状态码；<br>   415：415状态码；<br>   416：416状态码；<br>   417：417状态码；<br>   422：422状态码；<br>   423：423状态码；<br>   424：424状态码；<br>   426：426状态码；<br>   451：451状态码；<br>   5XX：5xx类型的状态码；<br>   500：500状态码；<br>   501：501状态码；<br>   502：502状态码；<br>   503：503状态码；<br>   504：504状态码；<br>   505：505状态码；<br>   506：506状态码；<br>   507：507状态码；<br>   510：510状态码；<br>   514：514状态码；<br>   544：544状态码。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
        :type Filters: list of QueryCondition
        :param _Interval: 查询时间粒度，可选的值有：
<li>min：1分钟的时间粒度；</li>
<li>5min：5分钟的时间粒度；</li>
<li>hour：1小时的时间粒度；</li>
<li>day：1天的时间粒度。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._ZoneIds = None
        self._Filters = None
        self._Interval = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._ZoneIds = params.get("ZoneIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTimingL7CacheDataResponse(AbstractModel):
    """DescribeTimingL7CacheData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 七层缓存分析时序类流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TimingDataRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimingDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopL7AnalysisDataRequest(AbstractModel):
    """DescribeTopL7AnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricName: 查询的指标，取值有：
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
        :param _ZoneIds: 站点集合，此参数必填，不填默认查询为空。
        :type ZoneIds: list of str
        :param _Limit: 查询前多少个数据，最大值为1000，不填默认默认为: 10， 表示查询前top10的数据。
        :type Limit: int
        :param _Filters: 过滤条件，详细的过滤条件Key值如下：
<li>country<br>   按照【<strong>国家/地区</strong>】进行过滤，国家/地区遵循 <a href="https://baike.baidu.com/item/ISO%203166-1/5269555">ISO 3166</a> 规范。</li>
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
        :param _Interval: 查询时间粒度，取值有：
<li>min：1分钟；</li>
<li>5min：5分钟；</li>
<li>hour：1小时；</li>
<li>day：1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._ZoneIds = None
        self._Limit = None
        self._Filters = None
        self._Interval = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._ZoneIds = params.get("ZoneIds")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7AnalysisDataResponse(AbstractModel):
    """DescribeTopL7AnalysisData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 七层流量前topN数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopDataRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopL7CacheDataRequest(AbstractModel):
    """DescribeTopL7CacheData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _MetricName: 查询的指标，取值有：
<li> l7Cache_outFlux_domain：host/域名；</li>
<li> l7Cache_outFlux_url：url地址；</li>
<li> l7Cache_outFlux_resourceType：资源类型；</li>
<li> l7Cache_outFlux_statusCode：状态码。</li>
        :type MetricName: str
        :param _ZoneIds: 站点id集合，不填默认选择全部站点。
        :type ZoneIds: list of str
        :param _Limit: 查询前多少个数据，最大值为1000，不填默认默认为10， 表示查询前top 10的数据。
        :type Limit: int
        :param _Filters: 过滤条件，详细的过滤条件如下：
<li>domain<br>   按照【<strong>子域名</strong>】进行过滤，子域名形如： test.example.com。<br>   类型：String<br>   必选：否</li>
<li>url<br>   按照【<strong>URL</strong>】进行过滤，此参数只支持30天的时间范围，URL形如：/content。<br>   类型：String<br>   必选：否</li>
<li>resourceType<br>   按照【<strong>资源类型</strong>】进行过滤，此参数只支持30天的时间范围，资源类型形如：jpg，png。<br>   类型：String<br>   必选：否</li>
<li>cacheType<br>   按照【<strong>缓存类型</strong>】进行过滤。<br>   类型：String<br>   必选：否<br>   可选项：<br>   hit：命中缓存；<br>   dynamic：资源不可缓存；<br>   miss：未命中缓存。</li>
<li>statusCode<br>   按照【<strong>状态码</strong>】进行过滤，此参数只支持30天的时间范围。<br>   类型：String<br>   必选：否<br>   可选项：<br>   1XX：1xx类型的状态码；<br>   100：100状态码；<br>   101：101状态码；<br>   102：102状态码；<br>   2XX：2xx类型的状态码；<br>   200：200状态码；<br>   201：201状态码；<br>   202：202状态码；<br>   203：203状态码；<br>   204：204状态码；<br>   100：100状态码；<br>   206：206状态码；<br>   207：207状态码；<br>   3XX：3xx类型的状态码；<br>   300：300状态码；<br>   301：301状态码；<br>   302：302状态码；<br>   303：303状态码；<br>   304：304状态码；<br>   305：305状态码；<br>   307：307状态码；<br>   4XX：4xx类型的状态码；<br>   400：400状态码；<br>   401：401状态码；<br>   402：402状态码；<br>   403：403状态码；<br>   404：404状态码；<br>   405：405状态码；<br>   406：406状态码；<br>   407：407状态码；<br>   408：408状态码；<br>   409：409状态码；<br>   410：410状态码；<br>   411：411状态码；<br>   412：412状态码；<br>   412：413状态码；<br>   414：414状态码；<br>   415：415状态码；<br>   416：416状态码；<br>   417：417状态码；<br>   422：422状态码；<br>   423：423状态码；<br>   424：424状态码；<br>   426：426状态码；<br>   451：451状态码；<br>   5XX：5xx类型的状态码；<br>   500：500状态码；<br>   501：501状态码；<br>   502：502状态码；<br>   503：503状态码；<br>   504：504状态码；<br>   505：505状态码；<br>   506：506状态码；<br>   507：507状态码；<br>   510：510状态码；<br>   514：514状态码；<br>   544：544状态码。</li>
<li>tagKey<br>   按照【<strong>标签Key</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>tagValue<br>   按照【<strong>标签Value</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
        :type Filters: list of QueryCondition
        :param _Interval: 查询时间粒度，取值有：
<li>min: 1分钟；</li>
<li>5min: 5分钟；</li>
<li>hour: 1小时；</li>
<li>day: 1天。</li>不填将根据开始时间跟结束时间的间距自动推算粒度，具体为：一小时范围内以min粒度查询，两天范围内以5min粒度查询，七天范围内以hour粒度查询，超过七天以day粒度查询。
        :type Interval: str
        :param _Area: 数据归属地区，取值有：
<li>overseas：全球（除中国大陆地区）数据；</li>
<li>mainland：中国大陆地区数据；</li>
<li>global：全球数据。</li>不填默认取值为global。
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._ZoneIds = None
        self._Limit = None
        self._Filters = None
        self._Interval = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._ZoneIds = params.get("ZoneIds")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryCondition()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Interval = params.get("Interval")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopL7CacheDataResponse(AbstractModel):
    """DescribeTopL7CacheData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 七层缓存TopN流量数据列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TopDataRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopDataRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneSettingRequest(AbstractModel):
    """DescribeZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneSettingResponse(AbstractModel):
    """DescribeZoneSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneSetting: 站点配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneSetting: :class:`tencentcloud.teo.v20220901.models.ZoneSetting`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneSetting = None
        self._RequestId = None

    @property
    def ZoneSetting(self):
        return self._ZoneSetting

    @ZoneSetting.setter
    def ZoneSetting(self, ZoneSetting):
        self._ZoneSetting = ZoneSetting

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ZoneSetting") is not None:
            self._ZoneSetting = ZoneSetting()
            self._ZoneSetting._deserialize(params.get("ZoneSetting"))
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询偏移量。默认值：0。
        :type Offset: int
        :param _Limit: 分页查询限制数目。默认值：20，最大值：100。
        :type Limit: int
        :param _Filters: 过滤条件，Filters.Values 的上限为 20。该参数不填写时，返回当前 appid 下有权限的所有站点信息。详细的过滤条件如下：
<li>zone-name：按照站点名称进行过滤；</li><li>zone-id：按照站点 ID进行过滤。站点 ID 形如：zone-2noz78a8ev6k；</li><li>status：按照站点状态进行过滤；</li><li>tag-key：按照标签键进行过滤；</li><li>tag-value： 按照标签值进行过滤。</li>模糊查询时仅支持过滤字段名为 zone-name。
        :type Filters: list of AdvancedFilter
        :param _Order: 可根据该字段对返回结果进行排序，取值有：
<li> type：接入类型；</li>
<li> area：加速区域；</li>
<li> create-time：创建时间；</li>
<li> zone-name：站点名称；</li>
<li> use-time：最近使用时间；</li>
<li> active-status：生效状态。</li>不填写时对返回结果默认按照 create-time 排序。
        :type Order: str
        :param _Direction: 排序方向，如果是字段值为数字，则根据数字大小排序；如果字段值为文本，则根据 ascill 码的大小排序。取值有：
<li> asc：从小到大排序；</li>
<li> desc：从大到小排序。</li>不填写使用默认值 desc。
        :type Direction: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._Direction = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = AdvancedFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的站点个数。
        :type TotalCount: int
        :param _Zones: 站点详细信息。
        :type Zones: list of Zone
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Zones = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RequestId = params.get("RequestId")


class DetailHost(AbstractModel):
    """域名配置信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _Status: 加速服务状态，取值为：
<li> process：部署中；</li>
<li> online：已启动；</li>
<li> offline：已关闭。</li>
        :type Status: str
        :param _Host: 域名。
        :type Host: str
        :param _ZoneName: 站点名称。
        :type ZoneName: str
        :param _Cname: 分配的Cname域名
        :type Cname: str
        :param _Id: 资源ID。
        :type Id: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Lock: 锁状态。
        :type Lock: int
        :param _Mode: 域名状态类型。
        :type Mode: int
        :param _Area: 域名加速地域，取值有：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>
        :type Area: str
        :param _AccelerateType: 加速类型配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccelerateType: :class:`tencentcloud.teo.v20220901.models.AccelerateType`
        :param _Https: Https配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param _CacheConfig: 缓存配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param _Origin: 源站配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param _SecurityType: 安全类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityType: :class:`tencentcloud.teo.v20220901.models.SecurityType`
        :param _CacheKey: 缓存键配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param _Compression: 智能压缩配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param _Waf: Waf防护配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Waf: :class:`tencentcloud.teo.v20220901.models.Waf`
        :param _CC: CC防护配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type CC: :class:`tencentcloud.teo.v20220901.models.CC`
        :param _DDoS: DDoS防护配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DDoS: :class:`tencentcloud.teo.v20220901.models.DDoS`
        :param _SmartRouting: 智能路由配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param _Ipv6: Ipv6访问配置项。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _ClientIpCountry: 回源时是否携带客户端IP所属地域信息的配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        """
        self._ZoneId = None
        self._Status = None
        self._Host = None
        self._ZoneName = None
        self._Cname = None
        self._Id = None
        self._InstanceId = None
        self._Lock = None
        self._Mode = None
        self._Area = None
        self._AccelerateType = None
        self._Https = None
        self._CacheConfig = None
        self._Origin = None
        self._SecurityType = None
        self._CacheKey = None
        self._Compression = None
        self._Waf = None
        self._CC = None
        self._DDoS = None
        self._SmartRouting = None
        self._Ipv6 = None
        self._ClientIpCountry = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Lock(self):
        return self._Lock

    @Lock.setter
    def Lock(self, Lock):
        self._Lock = Lock

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AccelerateType(self):
        return self._AccelerateType

    @AccelerateType.setter
    def AccelerateType(self, AccelerateType):
        self._AccelerateType = AccelerateType

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SecurityType(self):
        return self._SecurityType

    @SecurityType.setter
    def SecurityType(self, SecurityType):
        self._SecurityType = SecurityType

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def Waf(self):
        return self._Waf

    @Waf.setter
    def Waf(self, Waf):
        self._Waf = Waf

    @property
    def CC(self):
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def DDoS(self):
        return self._DDoS

    @DDoS.setter
    def DDoS(self, DDoS):
        self._DDoS = DDoS

    @property
    def SmartRouting(self):
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def ClientIpCountry(self):
        return self._ClientIpCountry

    @ClientIpCountry.setter
    def ClientIpCountry(self, ClientIpCountry):
        self._ClientIpCountry = ClientIpCountry


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        self._Host = params.get("Host")
        self._ZoneName = params.get("ZoneName")
        self._Cname = params.get("Cname")
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._Lock = params.get("Lock")
        self._Mode = params.get("Mode")
        self._Area = params.get("Area")
        if params.get("AccelerateType") is not None:
            self._AccelerateType = AccelerateType()
            self._AccelerateType._deserialize(params.get("AccelerateType"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SecurityType") is not None:
            self._SecurityType = SecurityType()
            self._SecurityType._deserialize(params.get("SecurityType"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("Waf") is not None:
            self._Waf = Waf()
            self._Waf._deserialize(params.get("Waf"))
        if params.get("CC") is not None:
            self._CC = CC()
            self._CC._deserialize(params.get("CC"))
        if params.get("DDoS") is not None:
            self._DDoS = DDoS()
            self._DDoS._deserialize(params.get("DDoS"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self._ClientIpCountry = ClientIpCountry()
            self._ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiffIPWhitelist(AbstractModel):
    """最新IP白名单列表相比于当前IP白名单列表的区别

    """

    def __init__(self):
        r"""
        :param _LatestIPWhitelist: 最新IP白名单列表。
        :type LatestIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _AddedIPWhitelist: 最新IP白名单列表相比于当前IP白名单列表，新增部分。
        :type AddedIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _RemovedIPWhitelist: 最新IP白名单列表相比于当前IP白名单列表，删减部分。
        :type RemovedIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _NoChangeIPWhitelist: 最新IP白名单列表相比于当前IP白名单列表，不变部分。
        :type NoChangeIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        """
        self._LatestIPWhitelist = None
        self._AddedIPWhitelist = None
        self._RemovedIPWhitelist = None
        self._NoChangeIPWhitelist = None

    @property
    def LatestIPWhitelist(self):
        return self._LatestIPWhitelist

    @LatestIPWhitelist.setter
    def LatestIPWhitelist(self, LatestIPWhitelist):
        self._LatestIPWhitelist = LatestIPWhitelist

    @property
    def AddedIPWhitelist(self):
        return self._AddedIPWhitelist

    @AddedIPWhitelist.setter
    def AddedIPWhitelist(self, AddedIPWhitelist):
        self._AddedIPWhitelist = AddedIPWhitelist

    @property
    def RemovedIPWhitelist(self):
        return self._RemovedIPWhitelist

    @RemovedIPWhitelist.setter
    def RemovedIPWhitelist(self, RemovedIPWhitelist):
        self._RemovedIPWhitelist = RemovedIPWhitelist

    @property
    def NoChangeIPWhitelist(self):
        return self._NoChangeIPWhitelist

    @NoChangeIPWhitelist.setter
    def NoChangeIPWhitelist(self, NoChangeIPWhitelist):
        self._NoChangeIPWhitelist = NoChangeIPWhitelist


    def _deserialize(self, params):
        if params.get("LatestIPWhitelist") is not None:
            self._LatestIPWhitelist = IPWhitelist()
            self._LatestIPWhitelist._deserialize(params.get("LatestIPWhitelist"))
        if params.get("AddedIPWhitelist") is not None:
            self._AddedIPWhitelist = IPWhitelist()
            self._AddedIPWhitelist._deserialize(params.get("AddedIPWhitelist"))
        if params.get("RemovedIPWhitelist") is not None:
            self._RemovedIPWhitelist = IPWhitelist()
            self._RemovedIPWhitelist._deserialize(params.get("RemovedIPWhitelist"))
        if params.get("NoChangeIPWhitelist") is not None:
            self._NoChangeIPWhitelist = IPWhitelist()
            self._NoChangeIPWhitelist._deserialize(params.get("NoChangeIPWhitelist"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DnsVerification(AbstractModel):
    """CNAME 接入，使用 DNS 解析验证时所需的信息。

    """

    def __init__(self):
        r"""
        :param _Subdomain: 主机记录。
        :type Subdomain: str
        :param _RecordType: 记录类型。
        :type RecordType: str
        :param _RecordValue: 记录值。
        :type RecordValue: str
        """
        self._Subdomain = None
        self._RecordType = None
        self._RecordValue = None

    @property
    def Subdomain(self):
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        self._Subdomain = Subdomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue


    def _deserialize(self, params):
        self._Subdomain = params.get("Subdomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsRequest(AbstractModel):
    """DownloadL4Logs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _ZoneIds: 站点集合，此参数必填，不填默认查询为空。
        :type ZoneIds: list of str
        :param _ProxyIds: 四层实例 ID 集合。
        :type ProxyIds: list of str
        :param _Limit: 分页查询的限制数目，默认值为 20，最大查询条目为 300。
        :type Limit: int
        :param _Offset: 分页的偏移量，默认值为 0。
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._ZoneIds = None
        self._ProxyIds = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ZoneIds = params.get("ZoneIds")
        self._ProxyIds = params.get("ProxyIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL4LogsResponse(AbstractModel):
    """DownloadL4Logs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 四层离线日志数据列表。
        :type Data: list of L4OfflineLog
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = L4OfflineLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DownloadL7LogsRequest(AbstractModel):
    """DownloadL7Logs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间。
        :type StartTime: str
        :param _EndTime: 结束时间。
        :type EndTime: str
        :param _ZoneIds: 站点集合，此参数必填，不填默认查询为空。
        :type ZoneIds: list of str
        :param _Domains: 子域名集合，不填默认选择全部子域名。
        :type Domains: list of str
        :param _Limit: 分页查询的限制数目，默认值为 20，最大查询条目为 300。
        :type Limit: int
        :param _Offset: 分页的偏移量，默认值为 0。
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._ZoneIds = None
        self._Domains = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ZoneIds = params.get("ZoneIds")
        self._Domains = params.get("Domains")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadL7LogsResponse(AbstractModel):
    """DownloadL7Logs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果的总条数。
        :type TotalCount: int
        :param _Data: 七层离线日志数据列表。
        :type Data: list of L7OfflineLog
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = L7OfflineLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DropPageConfig(AbstractModel):
    """拦截页面的总体配置，用于配置各个模块的拦截后行为。

    """

    def __init__(self):
        r"""
        :param _Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _WafDropPageDetail: Waf(托管规则)模块的拦截页面配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WafDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        :param _AclDropPageDetail: 自定义页面的拦截页面配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AclDropPageDetail: :class:`tencentcloud.teo.v20220901.models.DropPageDetail`
        """
        self._Switch = None
        self._WafDropPageDetail = None
        self._AclDropPageDetail = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def WafDropPageDetail(self):
        return self._WafDropPageDetail

    @WafDropPageDetail.setter
    def WafDropPageDetail(self, WafDropPageDetail):
        self._WafDropPageDetail = WafDropPageDetail

    @property
    def AclDropPageDetail(self):
        return self._AclDropPageDetail

    @AclDropPageDetail.setter
    def AclDropPageDetail(self, AclDropPageDetail):
        self._AclDropPageDetail = AclDropPageDetail


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("WafDropPageDetail") is not None:
            self._WafDropPageDetail = DropPageDetail()
            self._WafDropPageDetail._deserialize(params.get("WafDropPageDetail"))
        if params.get("AclDropPageDetail") is not None:
            self._AclDropPageDetail = DropPageDetail()
            self._AclDropPageDetail._deserialize(params.get("AclDropPageDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropPageDetail(AbstractModel):
    """拦截页面的配置信息

    """

    def __init__(self):
        r"""
        :param _PageId: 拦截页面的唯一 Id。系统默认包含一个自带拦截页面，Id 值为0。
该 Id 可通过创建拦截页面接口进行上传获取。如传入0，代表使用系统默认拦截页面。该参数已废弃。
        :type PageId: int
        :param _StatusCode: 拦截页面的 HTTP 状态码。状态码取值：100～600，不支持 3xx 状态码。托管规则拦截页面默认：566，安全防护（除托管规则外）拦截页面默认：567.
        :type StatusCode: int
        :param _Name: 页面文件名或 url。
        :type Name: str
        :param _Type: 页面的类型，取值有：
<li>page：指定页面。</li>

        :type Type: str
        :param _CustomResponseId: 自定义响应 Id。该 Id 可通过查询自定义错误页列表接口获取。默认值为default，使用系统默认页面。Type 类型是 page 时必填，且不能为空。
        :type CustomResponseId: str
        """
        self._PageId = None
        self._StatusCode = None
        self._Name = None
        self._Type = None
        self._CustomResponseId = None

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId


    def _deserialize(self, params):
        self._PageId = params.get("PageId")
        self._StatusCode = params.get("StatusCode")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CustomResponseId = params.get("CustomResponseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityStatus(AbstractModel):
    """安全实例状态。

    """

    def __init__(self):
        r"""
        :param _Entity: 实例名，现在只有子域名。
        :type Entity: str
        :param _Status: 实例配置下发状态，取值有：
<li>online：配置已生效；</li><li>fail：配置失败；</li><li> process：配置下发中。</li>
        :type Status: str
        :param _Message: 实例配置下发信息提示。
        :type Message: str
        """
        self._Entity = None
        self._Status = None
        self._Message = None

    @property
    def Entity(self):
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Entity = params.get("Entity")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptConfig(AbstractModel):
    """例外规则，用于配置需要跳过特定场景的规则

    """

    def __init__(self):
        r"""
        :param _Switch: 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _ExceptUserRules: 例外规则详情。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptUserRules: list of ExceptUserRule
        """
        self._Switch = None
        self._ExceptUserRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ExceptUserRules(self):
        return self._ExceptUserRules

    @ExceptUserRules.setter
    def ExceptUserRules(self, ExceptUserRules):
        self._ExceptUserRules = ExceptUserRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("ExceptUserRules") is not None:
            self._ExceptUserRules = []
            for item in params.get("ExceptUserRules"):
                obj = ExceptUserRule()
                obj._deserialize(item)
                self._ExceptUserRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRule(AbstractModel):
    """例外规则的配置，包含生效的条件，生效的范围。

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称，不可使用中文。
        :type RuleName: str
        :param _Action: 规则的处置方式，当前仅支持skip：跳过全部托管规则。
        :type Action: str
        :param _RuleStatus: 规则生效状态，取值有：
<li>on：生效；</li>
<li>off：失效。</li>
        :type RuleStatus: str
        :param _RuleID: 规则ID。仅出参使用。默认由底层生成。
        :type RuleID: int
        :param _UpdateTime: 更新时间，如果为null，默认由底层按当前时间生成。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _ExceptUserRuleConditions: 匹配条件。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptUserRuleConditions: list of ExceptUserRuleCondition
        :param _ExceptUserRuleScope: 规则生效的范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptUserRuleScope: :class:`tencentcloud.teo.v20220901.models.ExceptUserRuleScope`
        :param _RulePriority: 优先级，取值范围0-100。如果为null，默认由底层设置为0。
        :type RulePriority: int
        """
        self._RuleName = None
        self._Action = None
        self._RuleStatus = None
        self._RuleID = None
        self._UpdateTime = None
        self._ExceptUserRuleConditions = None
        self._ExceptUserRuleScope = None
        self._RulePriority = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExceptUserRuleConditions(self):
        return self._ExceptUserRuleConditions

    @ExceptUserRuleConditions.setter
    def ExceptUserRuleConditions(self, ExceptUserRuleConditions):
        self._ExceptUserRuleConditions = ExceptUserRuleConditions

    @property
    def ExceptUserRuleScope(self):
        return self._ExceptUserRuleScope

    @ExceptUserRuleScope.setter
    def ExceptUserRuleScope(self, ExceptUserRuleScope):
        self._ExceptUserRuleScope = ExceptUserRuleScope

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._RuleStatus = params.get("RuleStatus")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("ExceptUserRuleConditions") is not None:
            self._ExceptUserRuleConditions = []
            for item in params.get("ExceptUserRuleConditions"):
                obj = ExceptUserRuleCondition()
                obj._deserialize(item)
                self._ExceptUserRuleConditions.append(obj)
        if params.get("ExceptUserRuleScope") is not None:
            self._ExceptUserRuleScope = ExceptUserRuleScope()
            self._ExceptUserRuleScope._deserialize(params.get("ExceptUserRuleScope"))
        self._RulePriority = params.get("RulePriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleCondition(AbstractModel):
    """例外规则生效的具体条件。

    """

    def __init__(self):
        r"""
        :param _MatchFrom: 匹配项，取值有：
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
        :param _MatchParam: 匹配项的参数。仅当 MatchFrom 为 header 时，可以使用本参数，值可填入 header 的 key 作为参数。
        :type MatchParam: str
        :param _Operator: 匹配操作符，取值有：
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
        :param _MatchContent: 匹配值。
        :type MatchContent: str
        """
        self._MatchFrom = None
        self._MatchParam = None
        self._Operator = None
        self._MatchContent = None

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchParam(self):
        return self._MatchParam

    @MatchParam.setter
    def MatchParam(self, MatchParam):
        self._MatchParam = MatchParam

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._MatchFrom = params.get("MatchFrom")
        self._MatchParam = params.get("MatchParam")
        self._Operator = params.get("Operator")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExceptUserRuleScope(AbstractModel):
    """例外规则的生效范围。

    """

    def __init__(self):
        r"""
        :param _Type: 例外规则类型。其中complete模式代表全量数据进行例外，partial模式代表可选择指定模块指定字段进行例外，该字段取值有：
<li>complete：完全跳过模式；</li>
<li>partial：部分跳过模式。</li>
        :type Type: str
        :param _Modules: 生效的模块，该字段取值有：
<li>waf：托管规则；</li>
<li>rate：速率限制；</li>
<li>acl：自定义规则；</li>
<li>cc：cc攻击防护；</li>
<li>bot：Bot防护。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Modules: list of str
        :param _PartialModules: 跳过部分规则ID的例外规则详情。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type PartialModules: list of PartialModule
        :param _SkipConditions: 跳过具体字段不去扫描的例外规则详情。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipConditions: list of SkipCondition
        """
        self._Type = None
        self._Modules = None
        self._PartialModules = None
        self._SkipConditions = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Modules(self):
        return self._Modules

    @Modules.setter
    def Modules(self, Modules):
        self._Modules = Modules

    @property
    def PartialModules(self):
        return self._PartialModules

    @PartialModules.setter
    def PartialModules(self, PartialModules):
        self._PartialModules = PartialModules

    @property
    def SkipConditions(self):
        return self._SkipConditions

    @SkipConditions.setter
    def SkipConditions(self, SkipConditions):
        self._SkipConditions = SkipConditions


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Modules = params.get("Modules")
        if params.get("PartialModules") is not None:
            self._PartialModules = []
            for item in params.get("PartialModules"):
                obj = PartialModule()
                obj._deserialize(item)
                self._PartialModules.append(obj)
        if params.get("SkipConditions") is not None:
            self._SkipConditions = []
            for item in params.get("SkipConditions"):
                obj = SkipCondition()
                obj._deserialize(item)
                self._SkipConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailReason(AbstractModel):
    """失败原因

    """

    def __init__(self):
        r"""
        :param _Reason: 失败原因。
        :type Reason: str
        :param _Targets: 处理失败的资源列表。
        :type Targets: list of str
        """
        self._Reason = None
        self._Targets = None

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._Targets = params.get("Targets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileAscriptionInfo(AbstractModel):
    """站点归属权校验——文件校验信息。

    """

    def __init__(self):
        r"""
        :param _IdentifyPath: 文件校验目录。
        :type IdentifyPath: str
        :param _IdentifyContent: 文件校验内容。
        :type IdentifyContent: str
        """
        self._IdentifyPath = None
        self._IdentifyContent = None

    @property
    def IdentifyPath(self):
        return self._IdentifyPath

    @IdentifyPath.setter
    def IdentifyPath(self, IdentifyPath):
        self._IdentifyPath = IdentifyPath

    @property
    def IdentifyContent(self):
        return self._IdentifyContent

    @IdentifyContent.setter
    def IdentifyContent(self, IdentifyContent):
        self._IdentifyContent = IdentifyContent


    def _deserialize(self, params):
        self._IdentifyPath = params.get("IdentifyPath")
        self._IdentifyContent = params.get("IdentifyContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileVerification(AbstractModel):
    """CNAME 接入，使用文件验证时所需的信息。

    """

    def __init__(self):
        r"""
        :param _Path: EdgeOne 后台服务器将通过 Scheme + Host + URL Path 的格式（例如 https://www.example.com/.well-known/teo-verification/z12h416twn.txt）获取文件验证信息。该字段为您需要创建的 URL Path 部分。
        :type Path: str
        :param _Content: 验证文件的内容。该字段的内容需要您填写至 Path 字段返回的 txt 文件中。
        :type Content: str
        """
        self._Path = None
        self._Content = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等。
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirstPartConfig(AbstractModel):
    """慢速攻击的首段包配置。

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _StatTime: 首段包的统计时长，单位是秒，即期望首段包的统计时长是多少，默认5秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatTime: int
        """
        self._Switch = None
        self._StatTime = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def StatTime(self):
        return self._StatTime

    @StatTime.setter
    def StatTime(self, StatTime):
        self._StatTime = StatTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._StatTime = params.get("StatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowOrigin(AbstractModel):
    """缓存遵循源站配置

    """

    def __init__(self):
        r"""
        :param _Switch: 遵循源站配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _DefaultCacheTime: 源站未返回 Cache-Control 头时, 设置默认的缓存时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCacheTime: int
        :param _DefaultCache: 源站未返回 Cache-Control 头时, 设置缓存/不缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCache: str
        :param _DefaultCacheStrategy: 源站未返回 Cache-Control 头时, 使用/不使用默认缓存策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultCacheStrategy: str
        """
        self._Switch = None
        self._DefaultCacheTime = None
        self._DefaultCache = None
        self._DefaultCacheStrategy = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def DefaultCacheTime(self):
        return self._DefaultCacheTime

    @DefaultCacheTime.setter
    def DefaultCacheTime(self, DefaultCacheTime):
        self._DefaultCacheTime = DefaultCacheTime

    @property
    def DefaultCache(self):
        return self._DefaultCache

    @DefaultCache.setter
    def DefaultCache(self, DefaultCache):
        self._DefaultCache = DefaultCache

    @property
    def DefaultCacheStrategy(self):
        return self._DefaultCacheStrategy

    @DefaultCacheStrategy.setter
    def DefaultCacheStrategy(self, DefaultCacheStrategy):
        self._DefaultCacheStrategy = DefaultCacheStrategy


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._DefaultCacheTime = params.get("DefaultCacheTime")
        self._DefaultCache = params.get("DefaultCache")
        self._DefaultCacheStrategy = params.get("DefaultCacheStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """访问协议强制https跳转配置

    """

    def __init__(self):
        r"""
        :param _Switch: 访问强制跳转配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _RedirectStatusCode: 重定向状态码，取值有：
<li>301：301跳转；</li>
<li>302：302跳转。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        """
        self._Switch = None
        self._RedirectStatusCode = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectStatusCode(self):
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Grpc(AbstractModel):
    """Grpc配置项

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启 Grpc 配置，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Header(AbstractModel):
    """刷新预热附带的头部信息

    """

    def __init__(self):
        r"""
        :param _Name: HTTP头部名称。
        :type Name: str
        :param _Value: HTTP头部值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """Hsts配置

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _MaxAge: MaxAge 数值。单位为秒，最大值为1天。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: int
        :param _IncludeSubDomains: 是否包含子域名，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeSubDomains: str
        :param _Preload: 是否开启预加载，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Preload: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None
        self._Preload = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        return self._IncludeSubDomains

    @IncludeSubDomains.setter
    def IncludeSubDomains(self, IncludeSubDomains):
        self._IncludeSubDomains = IncludeSubDomains

    @property
    def Preload(self):
        return self._Preload

    @Preload.setter
    def Preload(self, Preload):
        self._Preload = Preload


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxAge = params.get("MaxAge")
        self._IncludeSubDomains = params.get("IncludeSubDomains")
        self._Preload = params.get("Preload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """域名 https 加速配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Http2: http2 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param _OcspStapling: OCSP 配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param _TlsVersion: Tls 版本设置，取值有：
<li>TLSv1：TLSv1版本；</li>
<li>TLSV1.1：TLSv1.1版本；</li>
<li>TLSV1.2：TLSv1.2版本；</li>
<li>TLSv1.3：TLSv1.3版本。</li>修改时必须开启连续的版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type TlsVersion: list of str
        :param _Hsts: HSTS 配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.teo.v20220901.models.Hsts`
        :param _CertInfo: 证书配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: list of ServerCertInfo
        :param _ApplyType: 申请类型，取值有：
<li>apply：托管EdgeOne；</li>
<li>none：不托管EdgeOne。</li>不填，默认取值为none。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyType: str
        :param _CipherSuite: 密码套件，取值有：
<li>loose-v2023：提供最高的兼容性，安全性一般，支持 TLS 1.0-1.3 密码套件；</li>
<li>general-v2023：提供较高的兼容性，安全性中等，支持 TLS 1.2-1.3 密码套件；</li>
<li>strict-v2023：提供最高的安全性能，禁用所有含不安全隐患的加密套件，支持 TLS 1.2-1.3 密码套件。
注意：此字段可能返回 null，表示取不到有效值。
        :type CipherSuite: str
        """
        self._Http2 = None
        self._OcspStapling = None
        self._TlsVersion = None
        self._Hsts = None
        self._CertInfo = None
        self._ApplyType = None
        self._CipherSuite = None

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def TlsVersion(self):
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion

    @property
    def Hsts(self):
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts

    @property
    def CertInfo(self):
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def ApplyType(self):
        return self._ApplyType

    @ApplyType.setter
    def ApplyType(self, ApplyType):
        self._ApplyType = ApplyType

    @property
    def CipherSuite(self):
        return self._CipherSuite

    @CipherSuite.setter
    def CipherSuite(self, CipherSuite):
        self._CipherSuite = CipherSuite


    def _deserialize(self, params):
        self._Http2 = params.get("Http2")
        self._OcspStapling = params.get("OcspStapling")
        self._TlsVersion = params.get("TlsVersion")
        if params.get("Hsts") is not None:
            self._Hsts = Hsts()
            self._Hsts._deserialize(params.get("Hsts"))
        if params.get("CertInfo") is not None:
            self._CertInfo = []
            for item in params.get("CertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self._CertInfo.append(obj)
        self._ApplyType = params.get("ApplyType")
        self._CipherSuite = params.get("CipherSuite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPGroup(AbstractModel):
    """IP 网段组

    """

    def __init__(self):
        r"""
        :param _GroupId: 组 Id，创建时填 0 即可。
        :type GroupId: int
        :param _Name: 组名称。
        :type Name: str
        :param _Content: IP 组内容，可以填入 IP 及 IP 掩码。
        :type Content: list of str
        """
        self._GroupId = None
        self._Name = None
        self._Content = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPWhitelist(AbstractModel):
    """源站防护IP白名单

    """

    def __init__(self):
        r"""
        :param _IPv4: IPv4列表。
        :type IPv4: list of str
        :param _IPv6: IPv6列表。
        :type IPv6: list of str
        """
        self._IPv4 = None
        self._IPv6 = None

    @property
    def IPv4(self):
        return self._IPv4

    @IPv4.setter
    def IPv4(self, IPv4):
        self._IPv4 = IPv4

    @property
    def IPv6(self):
        return self._IPv6

    @IPv6.setter
    def IPv6(self, IPv6):
        self._IPv6 = IPv6


    def _deserialize(self, params):
        self._IPv4 = params.get("IPv4")
        self._IPv6 = params.get("IPv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identification(AbstractModel):
    """站点验证信息

    """

    def __init__(self):
        r"""
        :param _ZoneName: 站点名称。
        :type ZoneName: str
        :param _Domain: 验证子域名。验证站点时，该值为空。验证子域名是为具体子域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Status: 验证状态，取值有：
<li> pending：验证中；</li>
<li> finished：验证完成。</li>
        :type Status: str
        :param _Ascription: 站点归属权校验：Dns校验信息。
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param _OriginalNameServers: 域名当前的 NS 记录。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalNameServers: list of str
        :param _FileAscription: 站点归属权校验：文件校验信息。
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        """
        self._ZoneName = None
        self._Domain = None
        self._Status = None
        self._Ascription = None
        self._OriginalNameServers = None
        self._FileAscription = None

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ascription(self):
        return self._Ascription

    @Ascription.setter
    def Ascription(self, Ascription):
        self._Ascription = Ascription

    @property
    def OriginalNameServers(self):
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def FileAscription(self):
        return self._FileAscription

    @FileAscription.setter
    def FileAscription(self, FileAscription):
        self._FileAscription = FileAscription


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        if params.get("Ascription") is not None:
            self._Ascription = AscriptionInfo()
            self._Ascription._deserialize(params.get("Ascription"))
        self._OriginalNameServers = params.get("OriginalNameServers")
        if params.get("FileAscription") is not None:
            self._FileAscription = FileAscriptionInfo()
            self._FileAscription._deserialize(params.get("FileAscription"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneRequest(AbstractModel):
    """IdentifyZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneName: 站点名称。
        :type ZoneName: str
        :param _Domain: 站点下的子域名。如果验证站点下的子域名，则传该值，否则为空。

        :type Domain: str
        """
        self._ZoneName = None
        self._Domain = None

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentifyZoneResponse(AbstractModel):
    """IdentifyZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ascription: 站点归属校验：Dns校验信息。
        :type Ascription: :class:`tencentcloud.teo.v20220901.models.AscriptionInfo`
        :param _FileAscription: 站点归属权校验：文件校验信息。
        :type FileAscription: :class:`tencentcloud.teo.v20220901.models.FileAscriptionInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ascription = None
        self._FileAscription = None
        self._RequestId = None

    @property
    def Ascription(self):
        return self._Ascription

    @Ascription.setter
    def Ascription(self, Ascription):
        self._Ascription = Ascription

    @property
    def FileAscription(self):
        return self._FileAscription

    @FileAscription.setter
    def FileAscription(self, FileAscription):
        self._FileAscription = FileAscription

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ascription") is not None:
            self._Ascription = AscriptionInfo()
            self._Ascription._deserialize(params.get("Ascription"))
        if params.get("FileAscription") is not None:
            self._FileAscription = FileAscriptionInfo()
            self._FileAscription._deserialize(params.get("FileAscription"))
        self._RequestId = params.get("RequestId")


class ImageOptimize(AbstractModel):
    """图片优化配置。

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceRule(AbstractModel):
    """智能分析规则

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _IntelligenceRuleItems: 规则详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntelligenceRuleItems: list of IntelligenceRuleItem
        """
        self._Switch = None
        self._IntelligenceRuleItems = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def IntelligenceRuleItems(self):
        return self._IntelligenceRuleItems

    @IntelligenceRuleItems.setter
    def IntelligenceRuleItems(self, IntelligenceRuleItems):
        self._IntelligenceRuleItems = IntelligenceRuleItems


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("IntelligenceRuleItems") is not None:
            self._IntelligenceRuleItems = []
            for item in params.get("IntelligenceRuleItems"):
                obj = IntelligenceRuleItem()
                obj._deserialize(item)
                self._IntelligenceRuleItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceRuleItem(AbstractModel):
    """Bot智能分析规则详情

    """

    def __init__(self):
        r"""
        :param _Label: 智能分析标签，取值有：
<li>evil_bot：恶意bot；</li>
<li>suspect_bot：疑似bot；</li>
<li>good_bot：良好bot；</li>
<li>normal：正常请求。</li>
        :type Label: str
        :param _Action: 触发智能分析标签对应的处置方式，取值有：
<li>drop：拦截；</li>
<li>trans：放行；</li>
<li>alg：Javascript挑战；</li>
<li>captcha：数字验证码；</li>
<li>monitor：观察。</li>
        :type Action: str
        """
        self._Label = None
        self._Action = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableConfig(AbstractModel):
    """IP黑白名单及IP区域控制配置

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭；</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _IpTableRules: 基础管控规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTableRules: list of IpTableRule
        """
        self._Switch = None
        self._IpTableRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def IpTableRules(self):
        return self._IpTableRules

    @IpTableRules.setter
    def IpTableRules(self, IpTableRules):
        self._IpTableRules = IpTableRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("IpTableRules") is not None:
            self._IpTableRules = []
            for item in params.get("IpTableRules"):
                obj = IpTableRule()
                obj._deserialize(item)
                self._IpTableRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpTableRule(AbstractModel):
    """IP黑白名单详细规则

    """

    def __init__(self):
        r"""
        :param _Action: 动作，取值有：
<li> drop：拦截；</li>
<li> trans：放行；</li>
<li> monitor：观察。</li>
        :type Action: str
        :param _MatchFrom: 根据类型匹配，取值有：
<li>ip：对ip进行匹配；</li>
<li>area：对ip所属地区匹配。</li>
        :type MatchFrom: str
        :param _Operator: 规则的匹配方式，默认为空代表等于。
取值有：
<li> is_emty：配置为空；</li>
<li> not_exists：配置为不存在；</li>
<li> include：包含；</li>
<li> not_include：不包含；</li>
<li> equal：等于；</li>
<li> not_equal：不等于。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _RuleID: 规则id。仅出参使用。
        :type RuleID: int
        :param _UpdateTime: 更新时间。仅出参使用。
        :type UpdateTime: str
        :param _Status: 规则启用状态，当返回为null时，为启用。取值有：
<li> on：启用；</li>
<li> off：未启用。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _RuleName: 规则名。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _MatchContent: 匹配内容。当 Operator为is_emty 或not_exists时，此值允许为空。
        :type MatchContent: str
        """
        self._Action = None
        self._MatchFrom = None
        self._Operator = None
        self._RuleID = None
        self._UpdateTime = None
        self._Status = None
        self._RuleName = None
        self._MatchContent = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._MatchFrom = params.get("MatchFrom")
        self._Operator = params.get("Operator")
        self._RuleID = params.get("RuleID")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._RuleName = params.get("RuleName")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """Ipv6访问配置

    """

    def __init__(self):
        r"""
        :param _Switch: Ipv6 访问功能配置，取值有：
<li>on：开启Ipv6访问功能；</li>
<li>off：关闭Ipv6访问功能。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4OfflineLog(AbstractModel):
    """离线日志详细信息

    """

    def __init__(self):
        r"""
        :param _ProxyId: 四层代理实例 ID。
        :type ProxyId: str
        :param _Area: 日志所属区域，取值有：
<li>mainland：中国大陆境内;</li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        :param _LogPacketName: 离线日志数据包名。
        :type LogPacketName: str
        :param _Url: 离线日志下载地址。
        :type Url: str
        :param _LogTime: 日志打包时间，此参数已经废弃。
        :type LogTime: int
        :param _LogStartTime: 日志打包开始时间。
        :type LogStartTime: str
        :param _LogEndTime: 日志打包结束时间。
        :type LogEndTime: str
        :param _Size: 日志大小，单位为 Byte。
        :type Size: int
        """
        self._ProxyId = None
        self._Area = None
        self._LogPacketName = None
        self._Url = None
        self._LogTime = None
        self._LogStartTime = None
        self._LogEndTime = None
        self._Size = None

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogPacketName(self):
        return self._LogPacketName

    @LogPacketName.setter
    def LogPacketName(self, LogPacketName):
        self._LogPacketName = LogPacketName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LogTime(self):
        return self._LogTime

    @LogTime.setter
    def LogTime(self, LogTime):
        self._LogTime = LogTime

    @property
    def LogStartTime(self):
        return self._LogStartTime

    @LogStartTime.setter
    def LogStartTime(self, LogStartTime):
        self._LogStartTime = LogStartTime

    @property
    def LogEndTime(self):
        return self._LogEndTime

    @LogEndTime.setter
    def LogEndTime(self, LogEndTime):
        self._LogEndTime = LogEndTime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._Area = params.get("Area")
        self._LogPacketName = params.get("LogPacketName")
        self._Url = params.get("Url")
        self._LogTime = params.get("LogTime")
        self._LogStartTime = params.get("LogStartTime")
        self._LogEndTime = params.get("LogEndTime")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7OfflineLog(AbstractModel):
    """七层离线日志详细信息。

    """

    def __init__(self):
        r"""
        :param _Domain: 离线日志域名。
        :type Domain: str
        :param _Area: 日志所属区域，取值有：
<li>mainland：中国大陆境内; </li>
<li>overseas：全球（不含中国大陆）。</li>
        :type Area: str
        :param _LogPacketName: 离线日志数据包名。	
        :type LogPacketName: str
        :param _Url: 离线日志下载地址。	
        :type Url: str
        :param _LogTime: 日志打包时间，此参数已经废弃。
        :type LogTime: int
        :param _LogStartTime: 日志打包开始时间。
        :type LogStartTime: str
        :param _LogEndTime: 日志打包结束时间。
        :type LogEndTime: str
        :param _Size: 日志原始大小，单位 Byte。
        :type Size: int
        """
        self._Domain = None
        self._Area = None
        self._LogPacketName = None
        self._Url = None
        self._LogTime = None
        self._LogStartTime = None
        self._LogEndTime = None
        self._Size = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogPacketName(self):
        return self._LogPacketName

    @LogPacketName.setter
    def LogPacketName(self, LogPacketName):
        self._LogPacketName = LogPacketName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def LogTime(self):
        return self._LogTime

    @LogTime.setter
    def LogTime(self, LogTime):
        self._LogTime = LogTime

    @property
    def LogStartTime(self):
        return self._LogStartTime

    @LogStartTime.setter
    def LogStartTime(self, LogStartTime):
        self._LogStartTime = LogStartTime

    @property
    def LogEndTime(self):
        return self._LogEndTime

    @LogEndTime.setter
    def LogEndTime(self, LogEndTime):
        self._LogEndTime = LogEndTime

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Area = params.get("Area")
        self._LogPacketName = params.get("LogPacketName")
        self._Url = params.get("Url")
        self._LogTime = params.get("LogTime")
        self._LogStartTime = params.get("LogStartTime")
        self._LogEndTime = params.get("LogEndTime")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """浏览器缓存规则配置，用于设置 MaxAge 默认值，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _FollowOrigin: 是否遵循源站，取值有：
<li>on：遵循源站，忽略MaxAge 时间设置；</li>
<li>off：不遵循源站，使用MaxAge 时间设置。</li>
        :type FollowOrigin: str
        :param _MaxAgeTime: MaxAge 时间设置，单位秒，最大365天。
注意：时间为0，即不缓存。
        :type MaxAgeTime: int
        """
        self._FollowOrigin = None
        self._MaxAgeTime = None

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin

    @property
    def MaxAgeTime(self):
        return self._MaxAgeTime

    @MaxAgeTime.setter
    def MaxAgeTime(self, MaxAgeTime):
        self._MaxAgeTime = MaxAgeTime


    def _deserialize(self, params):
        self._FollowOrigin = params.get("FollowOrigin")
        self._MaxAgeTime = params.get("MaxAgeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainRequest(AbstractModel):
    """ModifyAccelerationDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param _DomainName: 加速域名名称。
        :type DomainName: str
        :param _OriginInfo: 源站信息。
        :type OriginInfo: :class:`tencentcloud.teo.v20220901.models.OriginInfo`
        :param _OriginProtocol: 回源协议，取值有：
<li>FOLLOW: 协议跟随；</li>
<li>HTTP: HTTP协议回源；</li>
<li>HTTPS: HTTPS协议回源。</li>
<li>不填保持原有配置。</li>
        :type OriginProtocol: str
        :param _HttpOriginPort: HTTP回源端口，取值为1-65535，当OriginProtocol=FOLLOW/HTTP时生效, 不填保持原有配置。
        :type HttpOriginPort: int
        :param _HttpsOriginPort: HTTPS回源端口，取值为1-65535，当OriginProtocol=FOLLOW/HTTPS时生效，不填保持原有配置。
        :type HttpsOriginPort: int
        :param _IPv6Status: IPv6状态，取值有：
<li>follow：遵循站点IPv6配置；</li>
<li>on：开启状态；</li>
<li>off：关闭状态。</li>
<li>不填保持原有配置。</li>
        :type IPv6Status: str
        """
        self._ZoneId = None
        self._DomainName = None
        self._OriginInfo = None
        self._OriginProtocol = None
        self._HttpOriginPort = None
        self._HttpsOriginPort = None
        self._IPv6Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def OriginInfo(self):
        return self._OriginInfo

    @OriginInfo.setter
    def OriginInfo(self, OriginInfo):
        self._OriginInfo = OriginInfo

    @property
    def OriginProtocol(self):
        return self._OriginProtocol

    @OriginProtocol.setter
    def OriginProtocol(self, OriginProtocol):
        self._OriginProtocol = OriginProtocol

    @property
    def HttpOriginPort(self):
        return self._HttpOriginPort

    @HttpOriginPort.setter
    def HttpOriginPort(self, HttpOriginPort):
        self._HttpOriginPort = HttpOriginPort

    @property
    def HttpsOriginPort(self):
        return self._HttpsOriginPort

    @HttpsOriginPort.setter
    def HttpsOriginPort(self, HttpsOriginPort):
        self._HttpsOriginPort = HttpsOriginPort

    @property
    def IPv6Status(self):
        return self._IPv6Status

    @IPv6Status.setter
    def IPv6Status(self, IPv6Status):
        self._IPv6Status = IPv6Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainName = params.get("DomainName")
        if params.get("OriginInfo") is not None:
            self._OriginInfo = OriginInfo()
            self._OriginInfo._deserialize(params.get("OriginInfo"))
        self._OriginProtocol = params.get("OriginProtocol")
        self._HttpOriginPort = params.get("HttpOriginPort")
        self._HttpsOriginPort = params.get("HttpsOriginPort")
        self._IPv6Status = params.get("IPv6Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainResponse(AbstractModel):
    """ModifyAccelerationDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAccelerationDomainStatusesRequest(AbstractModel):
    """ModifyAccelerationDomainStatuses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 加速域名所属站点ID。
        :type ZoneId: str
        :param _DomainNames: 要执行状态变更的加速域名列表。
        :type DomainNames: list of str
        :param _Status: 加速域名状态，取值有：
<li>online：启用；</li>
<li>offline：停用。</li>
        :type Status: str
        :param _Force: 是否强制停用。当域名存在关联资源（如马甲域名、流量调度功能）时，是否强制停用该域名，取值有：
<li> true：停用该域名及所有关联资源；</li>
<li> false：当该加速域名存在关联资源时，不允许停用。</li>不填写，默认值为：false。
        :type Force: bool
        """
        self._ZoneId = None
        self._DomainNames = None
        self._Status = None
        self._Force = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def DomainNames(self):
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._DomainNames = params.get("DomainNames")
        self._Status = params.get("Status")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerationDomainStatusesResponse(AbstractModel):
    """ModifyAccelerationDomainStatuses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAliasDomainRequest(AbstractModel):
    """ModifyAliasDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _AliasName: 别称域名名称。
        :type AliasName: str
        :param _TargetName: 目标域名名称。
        :type TargetName: str
        :param _CertType: 证书配置，取值有：
<li> none：不配置；</li>
<li> hosting：SSL托管证书；</li>
<li> apply：申请免费证书。</li>不填写保持原有配置。
        :type CertType: str
        :param _CertId: 当 CertType 取值为 hosting 时填入相应证书 ID。
        :type CertId: list of str
        """
        self._ZoneId = None
        self._AliasName = None
        self._TargetName = None
        self._CertType = None
        self._CertId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def TargetName(self):
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._AliasName = params.get("AliasName")
        self._TargetName = params.get("TargetName")
        self._CertType = params.get("CertType")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainResponse(AbstractModel):
    """ModifyAliasDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAliasDomainStatusRequest(AbstractModel):
    """ModifyAliasDomainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Paused: 别称域名状态，取值有：
<li> false：开启别称域名；</li>
<li> true：关闭别称域名。</li>
        :type Paused: bool
        :param _AliasNames: 待修改状态的别称域名名称。如果为空，则不执行修改状态操作。
        :type AliasNames: list of str
        """
        self._ZoneId = None
        self._Paused = None
        self._AliasNames = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Paused(self):
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused

    @property
    def AliasNames(self):
        return self._AliasNames

    @AliasNames.setter
    def AliasNames(self, AliasNames):
        self._AliasNames = AliasNames


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Paused = params.get("Paused")
        self._AliasNames = params.get("AliasNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAliasDomainStatusResponse(AbstractModel):
    """ModifyAliasDomainStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyApplicationProxyRequest(AbstractModel):
    """ModifyApplicationProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _ProxyId: 代理 ID。
        :type ProxyId: str
        :param _ProxyName: 当 ProxyType=hostname 时，表示域名或子域名；
当 ProxyType=instance 时，表示代理名称。
        :type ProxyName: str
        :param _SessionPersistTime: 会话保持时间，取值范围：30-3600，单位：秒。
不填写保持原有配置。
        :type SessionPersistTime: int
        :param _ProxyType: 四层代理模式，取值有：
<li>hostname：表示子域名模式；</li>
<li>instance：表示实例模式。</li>不填写保持原有配置。
        :type ProxyType: str
        :param _Ipv6: Ipv6 访问配置，不填写保持原有配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _AccelerateMainland: 中国大陆加速优化配置。 不填写表示保持原有配置。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        """
        self._ZoneId = None
        self._ProxyId = None
        self._ProxyName = None
        self._SessionPersistTime = None
        self._ProxyType = None
        self._Ipv6 = None
        self._AccelerateMainland = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def ProxyType(self):
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._ProxyType = params.get("ProxyType")
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyResponse(AbstractModel):
    """ModifyApplicationProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleRequest(AbstractModel):
    """ModifyApplicationProxyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _ProxyId: 代理ID。
        :type ProxyId: str
        :param _RuleId: 规则ID。
        :type RuleId: str
        :param _OriginType: 源站类型，取值有：
<li>custom：手动添加；</li>
<li>origins：源站组。</li>不填保持原有值。
        :type OriginType: str
        :param _Port: 端口，支持格式：
<li>80：80端口；</li>
<li>81-90：81至90端口。</li>
        :type Port: list of str
        :param _Proto: 协议，取值有：
<li>TCP：TCP协议；</li>
<li>UDP：UDP协议。</li>不填保持原有值。
        :type Proto: str
        :param _OriginValue: 源站信息：
<li>当 OriginType 为 custom 时，表示一个或多个源站，如`["8.8.8.8","9.9.9.9"]` 或 `OriginValue=["test.com"]`；</li>
<li>当 OriginType 为 origins 时，要求有且仅有一个元素，表示源站组ID，如`["origin-537f5b41-162a-11ed-abaa-525400c5da15"]`。</li>

不填保持原有值。
        :type OriginValue: list of str
        :param _ForwardClientIp: 传递客户端IP，取值有：
<li>TOA：TOA（仅Proto=TCP时可选）；</li>
<li>PPV1：Proxy Protocol传递，协议版本V1（仅Proto=TCP时可选）；</li>
<li>PPV2：Proxy Protocol传递，协议版本V2；</li>
<li>OFF：不传递。</li>不填保持原有值。
        :type ForwardClientIp: str
        :param _SessionPersist: 是否开启会话保持，取值有：
<li>true：开启；</li>
<li>false：关闭。</li>不填为false。
        :type SessionPersist: bool
        :param _SessionPersistTime: 会话保持的时间，只有当SessionPersist为true时，该值才会生效。
        :type SessionPersistTime: int
        :param _OriginPort: 源站端口，支持格式：
<li>单端口：80；</li>
<li>端口段：81-90，81至90端口。</li>
        :type OriginPort: str
        :param _RuleTag: 规则标签。不填保持原有值。
        :type RuleTag: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None
        self._OriginType = None
        self._Port = None
        self._Proto = None
        self._OriginValue = None
        self._ForwardClientIp = None
        self._SessionPersist = None
        self._SessionPersistTime = None
        self._OriginPort = None
        self._RuleTag = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Proto(self):
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

    @property
    def OriginValue(self):
        return self._OriginValue

    @OriginValue.setter
    def OriginValue(self, OriginValue):
        self._OriginValue = OriginValue

    @property
    def ForwardClientIp(self):
        return self._ForwardClientIp

    @ForwardClientIp.setter
    def ForwardClientIp(self, ForwardClientIp):
        self._ForwardClientIp = ForwardClientIp

    @property
    def SessionPersist(self):
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def SessionPersistTime(self):
        return self._SessionPersistTime

    @SessionPersistTime.setter
    def SessionPersistTime(self, SessionPersistTime):
        self._SessionPersistTime = SessionPersistTime

    @property
    def OriginPort(self):
        return self._OriginPort

    @OriginPort.setter
    def OriginPort(self, OriginPort):
        self._OriginPort = OriginPort

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        self._OriginType = params.get("OriginType")
        self._Port = params.get("Port")
        self._Proto = params.get("Proto")
        self._OriginValue = params.get("OriginValue")
        self._ForwardClientIp = params.get("ForwardClientIp")
        self._SessionPersist = params.get("SessionPersist")
        self._SessionPersistTime = params.get("SessionPersistTime")
        self._OriginPort = params.get("OriginPort")
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleResponse(AbstractModel):
    """ModifyApplicationProxyRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyApplicationProxyRuleStatusRequest(AbstractModel):
    """ModifyApplicationProxyRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _ProxyId: 代理ID。
        :type ProxyId: str
        :param _RuleId: 规则ID。
        :type RuleId: str
        :param _Status: 状态，取值有：
<li>offline: 停用；</li>
<li>online: 启用。</li>
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._RuleId = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyRuleStatusResponse(AbstractModel):
    """ModifyApplicationProxyRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyApplicationProxyStatusRequest(AbstractModel):
    """ModifyApplicationProxyStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _ProxyId: 代理ID。
        :type ProxyId: str
        :param _Status: 状态，取值有：
<li>offline: 停用；</li>
<li>online: 启用。</li>
        :type Status: str
        """
        self._ZoneId = None
        self._ProxyId = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ProxyId(self):
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ProxyId = params.get("ProxyId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationProxyStatusResponse(AbstractModel):
    """ModifyApplicationProxyStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyHostsCertificateRequest(AbstractModel):
    """ModifyHostsCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Hosts: 需要修改证书配置的加速域名。
        :type Hosts: list of str
        :param _Mode: 配置证书的模式，取值有：
<li>disable：不配置证书；</li>
<li>eofreecert：配置 EdgeOne 免费证书；</li>
<li>sslcert：配置 SSL 证书。</li>不填时默认取值为 disable。
        :type Mode: str
        :param _ServerCertInfo: SSL 证书配置，本参数仅在 mode = sslcert 时生效，传入对应证书的 CertId 即可。您可以前往 [SSL 证书列表](https://console.cloud.tencent.com/certoverview) 查看 CertId。
        :type ServerCertInfo: list of ServerCertInfo
        :param _ApplyType: 托管类型，取值有：
<li>none：不托管EO；</li>
<li>apply：托管EO</li>
不填，默认取值为none。
        :type ApplyType: str
        """
        self._ZoneId = None
        self._Hosts = None
        self._Mode = None
        self._ServerCertInfo = None
        self._ApplyType = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ServerCertInfo(self):
        return self._ServerCertInfo

    @ServerCertInfo.setter
    def ServerCertInfo(self, ServerCertInfo):
        self._ServerCertInfo = ServerCertInfo

    @property
    def ApplyType(self):
        warnings.warn("parameter `ApplyType` is deprecated", DeprecationWarning) 

        return self._ApplyType

    @ApplyType.setter
    def ApplyType(self, ApplyType):
        warnings.warn("parameter `ApplyType` is deprecated", DeprecationWarning) 

        self._ApplyType = ApplyType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Hosts = params.get("Hosts")
        self._Mode = params.get("Mode")
        if params.get("ServerCertInfo") is not None:
            self._ServerCertInfo = []
            for item in params.get("ServerCertInfo"):
                obj = ServerCertInfo()
                obj._deserialize(item)
                self._ServerCertInfo.append(obj)
        self._ApplyType = params.get("ApplyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsCertificateResponse(AbstractModel):
    """ModifyHostsCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyOriginGroupRequest(AbstractModel):
    """ModifyOriginGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID
        :type ZoneId: str
        :param _GroupId: 源站组 ID，此参数必填。
        :type GroupId: str
        :param _Name: 源站组名称，不填保持原有配置，可输入1 - 200个字符，允许的字符为 a - z, A - Z, 0 - 9, _, - 。	
        :type Name: str
        :param _Type: 源站组类型，取值有：
<li>GENERAL：通用型源站组，仅支持添加 IP/域名 源站，可以被域名服务、规则引擎、四层代理、通用型负载均衡引用；</li>
<li>HTTP： HTTP专用型源站组，支持添加 IP/域名、对象存储源站，无法被四层代理引用。</li>不填保持原有配置。
        :type Type: str
        :param _Records: 源站记录信息，不填保持原有配置。
        :type Records: list of OriginRecord
        :param _HostHeader: 回源 Host Header，仅 Type = HTTP 时生效， 不填或者填空表示不配置回源Host，规则引擎修改 Host Header 配置优先级高于源站组的 Host Header。
        :type HostHeader: str
        """
        self._ZoneId = None
        self._GroupId = None
        self._Name = None
        self._Type = None
        self._Records = None
        self._HostHeader = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def HostHeader(self):
        return self._HostHeader

    @HostHeader.setter
    def HostHeader(self, HostHeader):
        self._HostHeader = HostHeader


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._HostHeader = params.get("HostHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOriginGroupResponse(AbstractModel):
    """ModifyOriginGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _RuleName: 规则名称，字符串名称长度 1~255。
        :type RuleName: str
        :param _Rules: 规则内容。
        :type Rules: list of Rule
        :param _RuleId: 规则 ID。
        :type RuleId: str
        :param _Status: 规则状态，取值有：
<li> enable: 启用； </li>
<li> disable: 未启用。</li>
        :type Status: str
        :param _Tags: 规则标签。
        :type Tags: list of str
        """
        self._ZoneId = None
        self._RuleName = None
        self._Rules = None
        self._RuleId = None
        self._Status = None
        self._Tags = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RuleName = params.get("RuleName")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RuleId = params.get("RuleId")
        self._Status = params.get("Status")
        self._Tags = params.get("Tags")
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
        :param _RuleId: 规则 ID。
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class ModifySecurityIPGroupRequest(AbstractModel):
    """ModifySecurityIPGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 Id。
        :type ZoneId: str
        :param _IPGroup: IP 组配置。
        :type IPGroup: :class:`tencentcloud.teo.v20220901.models.IPGroup`
        :param _Mode: 操作类型，取值有：
<li> append: 向 IPGroup 中追加 Content 参数中内容；</li>
<li> remove: 从 IPGroup 中删除 Content 参数中内容；</li>
<li> update: 全量替换 IPGroup 内容，并可修改 IPGroup 名称。 </li>
        :type Mode: str
        """
        self._ZoneId = None
        self._IPGroup = None
        self._Mode = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def IPGroup(self):
        return self._IPGroup

    @IPGroup.setter
    def IPGroup(self, IPGroup):
        self._IPGroup = IPGroup

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("IPGroup") is not None:
            self._IPGroup = IPGroup()
            self._IPGroup._deserialize(params.get("IPGroup"))
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityIPGroupResponse(AbstractModel):
    """ModifySecurityIPGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySecurityPolicyRequest(AbstractModel):
    """ModifySecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点Id。
        :type ZoneId: str
        :param _SecurityConfig: 安全配置。
        :type SecurityConfig: :class:`tencentcloud.teo.v20220901.models.SecurityConfig`
        :param _Entity: 子域名/应用名。当使用Entity时可不填写TemplateId，否则必须填写TemplateId。
        :type Entity: str
        :param _TemplateId: 模板策略id。当使用模板Id时可不填Entity，否则必须填写Entity。
        :type TemplateId: str
        """
        self._ZoneId = None
        self._SecurityConfig = None
        self._Entity = None
        self._TemplateId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SecurityConfig(self):
        return self._SecurityConfig

    @SecurityConfig.setter
    def SecurityConfig(self, SecurityConfig):
        self._SecurityConfig = SecurityConfig

    @property
    def Entity(self):
        return self._Entity

    @Entity.setter
    def Entity(self, Entity):
        self._Entity = Entity

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("SecurityConfig") is not None:
            self._SecurityConfig = SecurityConfig()
            self._SecurityConfig._deserialize(params.get("SecurityConfig"))
        self._Entity = params.get("Entity")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyResponse(AbstractModel):
    """ModifySecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyZoneRequest(AbstractModel):
    """ModifyZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Type: 站点接入方式，取值有：
<li> full：NS 接入；</li>
<li> partial：CNAME 接入，如果站点当前是无域名接入，仅支持切换到CNAME接入。</li>不填写保持原有配置。
        :type Type: str
        :param _VanityNameServers: 自定义站点信息，以替代系统默认分配的名称服务器。不填写保持原有配置。当站点是无域名接入方式时不允许传此参数。
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param _AliasZoneName: 站点别名。数字、英文、-和_组合，限制20个字符。
        :type AliasZoneName: str
        :param _Area: 站点接入地域，取值有：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>当站点是无域名接入方式时，不允许传此参数。
        :type Area: str
        :param _ZoneName: 站点名称。仅当站点由无域名接入方式切换到CNAME接入方式的场景下有效。
        :type ZoneName: str
        """
        self._ZoneId = None
        self._Type = None
        self._VanityNameServers = None
        self._AliasZoneName = None
        self._Area = None
        self._ZoneName = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VanityNameServers(self):
        return self._VanityNameServers

    @VanityNameServers.setter
    def VanityNameServers(self, VanityNameServers):
        self._VanityNameServers = VanityNameServers

    @property
    def AliasZoneName(self):
        return self._AliasZoneName

    @AliasZoneName.setter
    def AliasZoneName(self, AliasZoneName):
        self._AliasZoneName = AliasZoneName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Type = params.get("Type")
        if params.get("VanityNameServers") is not None:
            self._VanityNameServers = VanityNameServers()
            self._VanityNameServers._deserialize(params.get("VanityNameServers"))
        self._AliasZoneName = params.get("AliasZoneName")
        self._Area = params.get("Area")
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneResponse(AbstractModel):
    """ModifyZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyZoneSettingRequest(AbstractModel):
    """ModifyZoneSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 待变更的站点 ID。
        :type ZoneId: str
        :param _CacheConfig: 缓存过期时间配置。
不填写表示保持原有配置。
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param _CacheKey: 节点缓存键配置。
不填写表示保持原有配置。
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param _MaxAge: 浏览器缓存配置。
不填写表示保持原有配置。
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param _OfflineCache: 离线缓存配置。
不填写表示保持原有配置。
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param _Quic: Quic 访问配置。
不填写表示保持原有配置。
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param _PostMaxSize: Post 请求传输配置。
不填写表示保持原有配置。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param _Compression: 智能压缩配置。
不填写表示保持原有配置。
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param _UpstreamHttp2: Http2 回源配置。
不填写表示保持原有配置。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param _ForceRedirect: 访问协议强制 Https 跳转配置。
不填写表示保持原有配置。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param _Https: Https 加速配置。
不填写表示保持原有配置。
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param _Origin: 源站配置。
不填写表示保持原有配置。
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param _SmartRouting: 智能加速配置。
不填写表示保持原有配置。
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param _WebSocket: WebSocket 配置。
不填写表示保持原有配置。
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param _ClientIpHeader: 客户端 IP 回源请求头配置。
不填写表示保持原有配置。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param _CachePrefresh: 缓存预刷新配置。
不填写表示保持原有配置。
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param _Ipv6: Ipv6 访问配置。
不填写表示保持原有配置。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _ClientIpCountry: 回源时是否携带客户端 IP 所属地域信息的配置。
不填写表示保持原有配置。
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        :param _Grpc: Grpc 协议支持配置。
不填写表示保持原有配置。
        :type Grpc: :class:`tencentcloud.teo.v20220901.models.Grpc`
        :param _ImageOptimize: 图片优化配置。
不填写表示关闭。
        :type ImageOptimize: :class:`tencentcloud.teo.v20220901.models.ImageOptimize`
        :param _StandardDebug: 标准 Debug 配置。
        :type StandardDebug: :class:`tencentcloud.teo.v20220901.models.StandardDebug`
        """
        self._ZoneId = None
        self._CacheConfig = None
        self._CacheKey = None
        self._MaxAge = None
        self._OfflineCache = None
        self._Quic = None
        self._PostMaxSize = None
        self._Compression = None
        self._UpstreamHttp2 = None
        self._ForceRedirect = None
        self._Https = None
        self._Origin = None
        self._SmartRouting = None
        self._WebSocket = None
        self._ClientIpHeader = None
        self._CachePrefresh = None
        self._Ipv6 = None
        self._ClientIpCountry = None
        self._Grpc = None
        self._ImageOptimize = None
        self._StandardDebug = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def OfflineCache(self):
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def PostMaxSize(self):
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def UpstreamHttp2(self):
        return self._UpstreamHttp2

    @UpstreamHttp2.setter
    def UpstreamHttp2(self, UpstreamHttp2):
        self._UpstreamHttp2 = UpstreamHttp2

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SmartRouting(self):
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def ClientIpHeader(self):
        return self._ClientIpHeader

    @ClientIpHeader.setter
    def ClientIpHeader(self, ClientIpHeader):
        self._ClientIpHeader = ClientIpHeader

    @property
    def CachePrefresh(self):
        return self._CachePrefresh

    @CachePrefresh.setter
    def CachePrefresh(self, CachePrefresh):
        self._CachePrefresh = CachePrefresh

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def ClientIpCountry(self):
        return self._ClientIpCountry

    @ClientIpCountry.setter
    def ClientIpCountry(self, ClientIpCountry):
        self._ClientIpCountry = ClientIpCountry

    @property
    def Grpc(self):
        return self._Grpc

    @Grpc.setter
    def Grpc(self, Grpc):
        self._Grpc = Grpc

    @property
    def ImageOptimize(self):
        return self._ImageOptimize

    @ImageOptimize.setter
    def ImageOptimize(self, ImageOptimize):
        self._ImageOptimize = ImageOptimize

    @property
    def StandardDebug(self):
        return self._StandardDebug

    @StandardDebug.setter
    def StandardDebug(self, StandardDebug):
        self._StandardDebug = StandardDebug


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostMaxSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self._UpstreamHttp2 = UpstreamHttp2()
            self._UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self._ClientIpHeader = ClientIpHeader()
            self._ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self._CachePrefresh = CachePrefresh()
            self._CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("ClientIpCountry") is not None:
            self._ClientIpCountry = ClientIpCountry()
            self._ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        if params.get("Grpc") is not None:
            self._Grpc = Grpc()
            self._Grpc._deserialize(params.get("Grpc"))
        if params.get("ImageOptimize") is not None:
            self._ImageOptimize = ImageOptimize()
            self._ImageOptimize._deserialize(params.get("ImageOptimize"))
        if params.get("StandardDebug") is not None:
            self._StandardDebug = StandardDebug()
            self._StandardDebug._deserialize(params.get("StandardDebug"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneSettingResponse(AbstractModel):
    """ModifyZoneSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyZoneStatusRequest(AbstractModel):
    """ModifyZoneStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _Paused: 站点状态，取值有：
<li> false：开启站点；</li>
<li> true：关闭站点。</li>
        :type Paused: bool
        """
        self._ZoneId = None
        self._Paused = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Paused(self):
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Paused = params.get("Paused")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyZoneStatusResponse(AbstractModel):
    """ModifyZoneStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NoCache(AbstractModel):
    """不缓存配置

    """

    def __init__(self):
        r"""
        :param _Switch: 不缓存配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalAction(AbstractModel):
    """规则引擎常规类型的动作

    """

    def __init__(self):
        r"""
        :param _Action: 功能名称，功能名称填写规范可调用接口 [查询规则引擎的设置参数](https://cloud.tencent.com/document/product/1552/80618) 查看。
        :type Action: str
        :param _Parameters: 参数。
        :type Parameters: list of RuleNormalActionParams
        """
        self._Action = None
        self._Parameters = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = RuleNormalActionParams()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NsVerification(AbstractModel):
    """NS 接入，切换 DNS 服务器所需的信息。

    """

    def __init__(self):
        r"""
        :param _NameServers: NS 接入时，分配给用户的 DNS 服务器地址，需要将域名的 NameServer 切换至该地址。
        :type NameServers: list of str
        """
        self._NameServers = None

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers


    def _deserialize(self, params):
        self._NameServers = params.get("NameServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineCache(AbstractModel):
    """离线缓存是否开启

    """

    def __init__(self):
        r"""
        :param _Switch: 离线缓存是否开启，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """源站配置。

    """

    def __init__(self):
        r"""
        :param _Origins: 主源站列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origins: list of str
        :param _BackupOrigins: 备源站列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOrigins: list of str
        :param _OriginPullProtocol: 回源协议配置，取值有：
<li>http：强制 http 回源；</li>
<li>follow：协议跟随回源；</li>
<li>https：强制 https 回源。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param _CosPrivateAccess: 源站为腾讯云 COS 时，是否为私有访问 bucket，取值有：
<li>on：私有访问；</li>
<li>off：公共访问。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPrivateAccess: str
        """
        self._Origins = None
        self._BackupOrigins = None
        self._OriginPullProtocol = None
        self._CosPrivateAccess = None

    @property
    def Origins(self):
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def BackupOrigins(self):
        return self._BackupOrigins

    @BackupOrigins.setter
    def BackupOrigins(self, BackupOrigins):
        self._BackupOrigins = BackupOrigins

    @property
    def OriginPullProtocol(self):
        return self._OriginPullProtocol

    @OriginPullProtocol.setter
    def OriginPullProtocol(self, OriginPullProtocol):
        self._OriginPullProtocol = OriginPullProtocol

    @property
    def CosPrivateAccess(self):
        return self._CosPrivateAccess

    @CosPrivateAccess.setter
    def CosPrivateAccess(self, CosPrivateAccess):
        self._CosPrivateAccess = CosPrivateAccess


    def _deserialize(self, params):
        self._Origins = params.get("Origins")
        self._BackupOrigins = params.get("BackupOrigins")
        self._OriginPullProtocol = params.get("OriginPullProtocol")
        self._CosPrivateAccess = params.get("CosPrivateAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginDetail(AbstractModel):
    """加速域名源站信息。

    """

    def __init__(self):
        r"""
        :param _OriginType: 源站类型，取值有：
<li>IP_DOMAIN：IPV4、IPV6或域名类型源站；</li>
<li>COS：COS源。</li>
<li>ORIGIN_GROUP：源站组类型源站。</li>
<li>AWS_S3：AWS S3对象存储源站。</li>
        :type OriginType: str
        :param _Origin: 源站地址，当OriginType参数指定为ORIGIN_GROUP时，该参数填写源站组ID，其他情况下填写源站地址。
        :type Origin: str
        :param _BackupOrigin: 备用源站组ID，该参数在OriginType参数指定为ORIGIN_GROUP时生效，为空表示不使用备用源站。
        :type BackupOrigin: str
        :param _OriginGroupName: 主源源站组名称，当OriginType参数指定为ORIGIN_GROUP时该参数生效。
        :type OriginGroupName: str
        :param _BackOriginGroupName: 备用源站源站组名称，当OriginType参数指定为ORIGIN_GROUP，且用户指定了被用源站时该参数生效。
        :type BackOriginGroupName: str
        :param _PrivateAccess: 指定是否允许访问私有对象存储源站。当源站类型OriginType=COS或AWS_S3时有效 取值有：
<li>on：使用私有鉴权；</li>
<li>off：不使用私有鉴权。</li>
不填写，默认值为off。
        :type PrivateAccess: str
        :param _PrivateParameters: 私有鉴权使用参数，当源站类型PrivateAccess=on时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateParameters: list of PrivateParameter
        """
        self._OriginType = None
        self._Origin = None
        self._BackupOrigin = None
        self._OriginGroupName = None
        self._BackOriginGroupName = None
        self._PrivateAccess = None
        self._PrivateParameters = None

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def BackupOrigin(self):
        return self._BackupOrigin

    @BackupOrigin.setter
    def BackupOrigin(self, BackupOrigin):
        self._BackupOrigin = BackupOrigin

    @property
    def OriginGroupName(self):
        return self._OriginGroupName

    @OriginGroupName.setter
    def OriginGroupName(self, OriginGroupName):
        self._OriginGroupName = OriginGroupName

    @property
    def BackOriginGroupName(self):
        return self._BackOriginGroupName

    @BackOriginGroupName.setter
    def BackOriginGroupName(self, BackOriginGroupName):
        self._BackOriginGroupName = BackOriginGroupName

    @property
    def PrivateAccess(self):
        return self._PrivateAccess

    @PrivateAccess.setter
    def PrivateAccess(self, PrivateAccess):
        self._PrivateAccess = PrivateAccess

    @property
    def PrivateParameters(self):
        return self._PrivateParameters

    @PrivateParameters.setter
    def PrivateParameters(self, PrivateParameters):
        self._PrivateParameters = PrivateParameters


    def _deserialize(self, params):
        self._OriginType = params.get("OriginType")
        self._Origin = params.get("Origin")
        self._BackupOrigin = params.get("BackupOrigin")
        self._OriginGroupName = params.get("OriginGroupName")
        self._BackOriginGroupName = params.get("BackOriginGroupName")
        self._PrivateAccess = params.get("PrivateAccess")
        if params.get("PrivateParameters") is not None:
            self._PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self._PrivateParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroup(AbstractModel):
    """源站组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 源站组ID。
        :type GroupId: str
        :param _Name: 源站组名称。
        :type Name: str
        :param _Type: 源站组类型，取值有：
<li>GENERAL：通用型源站组；</li>
<li>HTTP： HTTP专用型源站组。</li>
        :type Type: str
        :param _Records: 源站记录信息。
        :type Records: list of OriginRecord
        :param _References: 源站组被引用实例列表。	
        :type References: list of OriginGroupReference
        :param _CreateTime: 源站组创建时间。
        :type CreateTime: str
        :param _UpdateTime: 源站组更新时间。
        :type UpdateTime: str
        """
        self._GroupId = None
        self._Name = None
        self._Type = None
        self._Records = None
        self._References = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = OriginRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = OriginGroupReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginGroupReference(AbstractModel):
    """源站组引用服务。

    """

    def __init__(self):
        r"""
        :param _InstanceType: 引用服务类型，取值有：
<li>AccelerationDomain: 加速域名；</li>
<li>RuleEngine: 规则引擎；</li>
<li>Loadbalance: 负载均衡；</li>
<li>ApplicationProxy: 四层代理。</li>
        :type InstanceType: str
        :param _InstanceId: 引用类型的实例ID。
        :type InstanceId: str
        :param _InstanceName: 应用类型的实例名称。
        :type InstanceName: str
        """
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginInfo(AbstractModel):
    """加速域名源站信息。

    """

    def __init__(self):
        r"""
        :param _OriginType: 源站类型，取值有：
<li>IP_DOMAIN：IPV4、IPV6 或域名类型源站；</li>
<li>COS：COS 源；</li>
<li>ORIGIN_GROUP：源站组类型源站；</li>
<li>AWS_S3：S3兼容对象存储源站；</li>
<li>LB: 负载均衡类型源站；</li>
<li>SPACE：EdgeOne Shield Space 存储。</li>  
        :type OriginType: str
        :param _Origin: 源站地址，当 OriginType 参数指定为 ORIGIN_GROUP 时，该参数填写源站组 ID，其他情况下填写源站地址。
        :type Origin: str
        :param _BackupOrigin: 备用源站组 ID，该参数在 OriginType 参数指定为 ORIGIN_GROUP 时生效，为空表示不使用备用源站。
        :type BackupOrigin: str
        :param _PrivateAccess: 指定是否允许访问私有对象存储源站，当源站类型 OriginType=COS 或 AWS_S3 时有效，取值有：
<li>on：使用私有鉴权；</li>
<li>off：不使用私有鉴权。</li>默认值：off。
        :type PrivateAccess: str
        :param _PrivateParameters: 私有鉴权使用参数，当源站类型 PrivateAccess=on 时有效。
        :type PrivateParameters: list of PrivateParameter
        """
        self._OriginType = None
        self._Origin = None
        self._BackupOrigin = None
        self._PrivateAccess = None
        self._PrivateParameters = None

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def BackupOrigin(self):
        return self._BackupOrigin

    @BackupOrigin.setter
    def BackupOrigin(self, BackupOrigin):
        self._BackupOrigin = BackupOrigin

    @property
    def PrivateAccess(self):
        return self._PrivateAccess

    @PrivateAccess.setter
    def PrivateAccess(self, PrivateAccess):
        self._PrivateAccess = PrivateAccess

    @property
    def PrivateParameters(self):
        return self._PrivateParameters

    @PrivateParameters.setter
    def PrivateParameters(self, PrivateParameters):
        self._PrivateParameters = PrivateParameters


    def _deserialize(self, params):
        self._OriginType = params.get("OriginType")
        self._Origin = params.get("Origin")
        self._BackupOrigin = params.get("BackupOrigin")
        self._PrivateAccess = params.get("PrivateAccess")
        if params.get("PrivateParameters") is not None:
            self._PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self._PrivateParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginProtectionInfo(AbstractModel):
    """源站防护信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
        :type ZoneId: str
        :param _Hosts: 域名列表。
        :type Hosts: list of str
        :param _ProxyIds: 代理ID列表。
        :type ProxyIds: list of str
        :param _CurrentIPWhitelist: 当前版本的IP白名单。
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentIPWhitelist: :class:`tencentcloud.teo.v20220901.models.IPWhitelist`
        :param _NeedUpdate: 该站点是否需要更新源站白名单，取值有：
<li>true ：需要更新IP白名单 ；</li>
<li>false ：无需更新IP白名单。</li>
        :type NeedUpdate: bool
        :param _Status: 源站防护状态，取值有：
<li>online ：源站防护启用中 ；</li>
<li>offline ：源站防护已停用 ；</li>
<li>nonactivate ：源站防护未激活，仅在从未使用过源站防护功能的站点调用中返回。</li>
        :type Status: str
        :param _PlanSupport: 站点套餐是否支持源站防护，取值有：
<li>true ：支持 ；</li>
<li>false ：不支持。</li>
        :type PlanSupport: bool
        :param _DiffIPWhitelist: 最新IP白名单与当前IP白名单的对比。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiffIPWhitelist: :class:`tencentcloud.teo.v20220901.models.DiffIPWhitelist`
        """
        self._ZoneId = None
        self._Hosts = None
        self._ProxyIds = None
        self._CurrentIPWhitelist = None
        self._NeedUpdate = None
        self._Status = None
        self._PlanSupport = None
        self._DiffIPWhitelist = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def ProxyIds(self):
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def CurrentIPWhitelist(self):
        return self._CurrentIPWhitelist

    @CurrentIPWhitelist.setter
    def CurrentIPWhitelist(self, CurrentIPWhitelist):
        self._CurrentIPWhitelist = CurrentIPWhitelist

    @property
    def NeedUpdate(self):
        return self._NeedUpdate

    @NeedUpdate.setter
    def NeedUpdate(self, NeedUpdate):
        self._NeedUpdate = NeedUpdate

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PlanSupport(self):
        return self._PlanSupport

    @PlanSupport.setter
    def PlanSupport(self, PlanSupport):
        self._PlanSupport = PlanSupport

    @property
    def DiffIPWhitelist(self):
        return self._DiffIPWhitelist

    @DiffIPWhitelist.setter
    def DiffIPWhitelist(self, DiffIPWhitelist):
        self._DiffIPWhitelist = DiffIPWhitelist


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Hosts = params.get("Hosts")
        self._ProxyIds = params.get("ProxyIds")
        if params.get("CurrentIPWhitelist") is not None:
            self._CurrentIPWhitelist = IPWhitelist()
            self._CurrentIPWhitelist._deserialize(params.get("CurrentIPWhitelist"))
        self._NeedUpdate = params.get("NeedUpdate")
        self._Status = params.get("Status")
        self._PlanSupport = params.get("PlanSupport")
        if params.get("DiffIPWhitelist") is not None:
            self._DiffIPWhitelist = DiffIPWhitelist()
            self._DiffIPWhitelist._deserialize(params.get("DiffIPWhitelist"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginRecord(AbstractModel):
    """源站组记录

    """

    def __init__(self):
        r"""
        :param _Record: 源站记录值，不包含端口信息，可以为：IPv4，IPv6，域名格式。
        :type Record: str
        :param _Type: 源站类型，取值有：
<li>IP_DOMAIN：IPV4、IPV6、域名类型源站；</li>
<li>COS：COS源。</li>
<li>AWS_S3：AWS S3对象存储源站。</li>
        :type Type: str
        :param _RecordId: 源站记录ID。
        :type RecordId: str
        :param _Weight: 源站权重，取值为0-100, 不填表示不设置权重，由系统自由调度，填0表示权重为0, 流量将不会调度到此源站。
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _Private: 是否私有鉴权，当源站类型 RecordType=COS/AWS_S3 时生效，取值有：
<li>true：使用私有鉴权；</li>
<li>false：不使用私有鉴权。</li>不填写，默认值为：false。

        :type Private: bool
        :param _PrivateParameters: 私有鉴权参数，当源站类型Private=true时有效。
        :type PrivateParameters: list of PrivateParameter
        """
        self._Record = None
        self._Type = None
        self._RecordId = None
        self._Weight = None
        self._Private = None
        self._PrivateParameters = None

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Private(self):
        return self._Private

    @Private.setter
    def Private(self, Private):
        self._Private = Private

    @property
    def PrivateParameters(self):
        return self._PrivateParameters

    @PrivateParameters.setter
    def PrivateParameters(self, PrivateParameters):
        self._PrivateParameters = PrivateParameters


    def _deserialize(self, params):
        self._Record = params.get("Record")
        self._Type = params.get("Type")
        self._RecordId = params.get("RecordId")
        self._Weight = params.get("Weight")
        self._Private = params.get("Private")
        if params.get("PrivateParameters") is not None:
            self._PrivateParameters = []
            for item in params.get("PrivateParameters"):
                obj = PrivateParameter()
                obj._deserialize(item)
                self._PrivateParameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OwnershipVerification(AbstractModel):
    """该结构体表示各种场景、模式下，用于验证用户对站点域名的归属权内容。

    """

    def __init__(self):
        r"""
        :param _DnsVerification: CNAME 接入，使用 DNS 解析验证时所需的信息。详情参考 [站点/域名归属权验证
](https://cloud.tencent.com/document/product/1552/70789#7af6ecf8-afca-4e35-8811-b5797ed1bde5)。
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsVerification: :class:`tencentcloud.teo.v20220901.models.DnsVerification`
        :param _FileVerification: CNAME 接入，使用文件验证时所需的信息。详情参考 [站点/域名归属权验证
](https://cloud.tencent.com/document/product/1552/70789#7af6ecf8-afca-4e35-8811-b5797ed1bde5)。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileVerification: :class:`tencentcloud.teo.v20220901.models.FileVerification`
        :param _NsVerification: NS 接入，切换 DNS 服务器所需的信息。详情参考 [修改 DNS 服务器](https://cloud.tencent.com/document/product/1552/90452)。
注意：此字段可能返回 null，表示取不到有效值。
        :type NsVerification: :class:`tencentcloud.teo.v20220901.models.NsVerification`
        """
        self._DnsVerification = None
        self._FileVerification = None
        self._NsVerification = None

    @property
    def DnsVerification(self):
        return self._DnsVerification

    @DnsVerification.setter
    def DnsVerification(self, DnsVerification):
        self._DnsVerification = DnsVerification

    @property
    def FileVerification(self):
        return self._FileVerification

    @FileVerification.setter
    def FileVerification(self, FileVerification):
        self._FileVerification = FileVerification

    @property
    def NsVerification(self):
        return self._NsVerification

    @NsVerification.setter
    def NsVerification(self, NsVerification):
        self._NsVerification = NsVerification


    def _deserialize(self, params):
        if params.get("DnsVerification") is not None:
            self._DnsVerification = DnsVerification()
            self._DnsVerification._deserialize(params.get("DnsVerification"))
        if params.get("FileVerification") is not None:
            self._FileVerification = FileVerification()
            self._FileVerification._deserialize(params.get("FileVerification"))
        if params.get("NsVerification") is not None:
            self._NsVerification = NsVerification()
            self._NsVerification._deserialize(params.get("NsVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartialModule(AbstractModel):
    """例外规则的详细模块配置。

    """

    def __init__(self):
        r"""
        :param _Module: 模块名称，取值为：
<li>waf：托管规则。</li>
        :type Module: str
        :param _Include: 模块下的需要例外的具体规则ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Include: list of int
        """
        self._Module = None
        self._Include = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Include(self):
        return self._Include

    @Include.setter
    def Include(self, Include):
        self._Include = Include


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Include = params.get("Include")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanInfo(AbstractModel):
    """edgeone套餐信息

    """

    def __init__(self):
        r"""
        :param _Currency: 结算货币类型，取值有：
<li> CNY ：人民币结算； </li>
<li> USD ：美元结算。</li>
        :type Currency: str
        :param _Flux: 套餐所含流量，该流量数值为安全加速流量，内容加速流量和智能加速流量的总和（单位：字节）。
        :type Flux: int
        :param _Frequency: 结算周期，取值有：
<li> y ：按年结算； </li>
<li> m ：按月结算；</li>
<li> h ：按小时结算； </li>
<li> M ：按分钟结算；</li>
<li> s ：按秒结算。 </li>
        :type Frequency: str
        :param _PlanType: 套餐类型，取值有：
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
        :param _Price: 套餐价格（单位：分）。
        :type Price: float
        :param _Request: 套餐所含请求次数，该请求次数为安全加速请求次数。（单位：次）。
        :type Request: int
        :param _SiteNumber: 套餐所能绑定的站点个数。
        :type SiteNumber: int
        :param _Area: 套餐加速区域类型，取值有：
<li> mainland ：中国大陆； </li>
<li> overseas ：全球（不包括中国大陆）；</li>
<li> global ：全球（包括中国大陆）。 </li>
        :type Area: str
        """
        self._Currency = None
        self._Flux = None
        self._Frequency = None
        self._PlanType = None
        self._Price = None
        self._Request = None
        self._SiteNumber = None
        self._Area = None

    @property
    def Currency(self):
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Flux(self):
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def PlanType(self):
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def Request(self):
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def SiteNumber(self):
        return self._SiteNumber

    @SiteNumber.setter
    def SiteNumber(self, SiteNumber):
        self._SiteNumber = SiteNumber

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Currency = params.get("Currency")
        self._Flux = params.get("Flux")
        self._Frequency = params.get("Frequency")
        self._PlanType = params.get("PlanType")
        self._Price = params.get("Price")
        self._Request = params.get("Request")
        self._SiteNumber = params.get("SiteNumber")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostMaxSize(AbstractModel):
    """POST请求上传文件流式传输最大限制

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启 POST 请求上传文件限制，平台默认为限制为32MB，取值有：
<li>on：开启限制；</li>
<li>off：关闭限制。</li>
        :type Switch: str
        :param _MaxSize: 最大限制，取值在1MB和500MB之间。单位字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self._Switch = None
        self._MaxSize = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateParameter(AbstractModel):
    """对象存储源站记录私有鉴权参数

    """

    def __init__(self):
        r"""
        :param _Name: 私有鉴权参数名称，取值有：
<li>AccessKeyId：鉴权参数Access Key ID；</li>
<li>SecretAccessKey：鉴权参数Secret Access Key；</li>
<li>SignatureVersion：鉴权版本，v2或者v4；</li>
<li>Region：存储桶地域。</li>
        :type Name: str
        :param _Value: 私有鉴权参数值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCondition(AbstractModel):
    """查询条件

    """

    def __init__(self):
        r"""
        :param _Key: 筛选条件的key。
        :type Key: str
        :param _Operator: 查询条件操作符，操作类型有：
<li>equals: 等于；</li>
<li>notEquals: 不等于；</li>
<li>include: 包含；</li>
<li>notInclude: 不包含; </li>
<li>startWith: 开始的值是value；</li>
<li>notStartWith: 不以value的值开始；</li>
<li>endWith: 结尾是value值；</li>
<li>notEndWith: 不以value的值结尾。</li>
        :type Operator: str
        :param _Value: 筛选条件的值。
        :type Value: list of str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryString(AbstractModel):
    """CacheKey中包含请求参数

    """

    def __init__(self):
        r"""
        :param _Switch: CacheKey是否由QueryString组成，取值有：
<li>on：是；</li>
<li>off：否。</li>
        :type Switch: str
        :param _Action: CacheKey使用QueryString的方式，取值有：
<li>includeCustom：使用部分url参数；</li>
<li>excludeCustom：排除部分url参数。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _Value: 使用/排除的url参数数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
        self._Switch = None
        self._Action = None
        self._Value = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """Quic配置项

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启 Quic 配置，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """刷新/预热 可用量及配额

    """

    def __init__(self):
        r"""
        :param _Batch: 单次批量提交配额上限。
        :type Batch: int
        :param _Daily: 每日提交配额上限。
        :type Daily: int
        :param _DailyAvailable: 每日剩余的可提交配额。
        :type DailyAvailable: int
        :param _Type: 刷新预热缓存类型，取值有：
<li> purge_prefix：按前缀刷新；</li>
<li> purge_url：按URL刷新；</li>
<li> purge_host：按Hostname刷新；</li>
<li> purge_all：刷新全部缓存内容；</li>
<li> purge_cache_tag：按CacheTag刷新；</li><li> prefetch_url：按URL预热。</li>
        :type Type: str
        """
        self._Batch = None
        self._Daily = None
        self._DailyAvailable = None
        self._Type = None

    @property
    def Batch(self):
        return self._Batch

    @Batch.setter
    def Batch(self, Batch):
        self._Batch = Batch

    @property
    def Daily(self):
        return self._Daily

    @Daily.setter
    def Daily(self, Daily):
        self._Daily = Daily

    @property
    def DailyAvailable(self):
        return self._DailyAvailable

    @DailyAvailable.setter
    def DailyAvailable(self, DailyAvailable):
        self._DailyAvailable = DailyAvailable

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Batch = params.get("Batch")
        self._Daily = params.get("Daily")
        self._DailyAvailable = params.get("DailyAvailable")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitConfig(AbstractModel):
    """速率限制规则

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _RateLimitUserRules: 速率限制-用户规则列表。如果为null，默认使用历史配置。
        :type RateLimitUserRules: list of RateLimitUserRule
        :param _RateLimitTemplate: 速率限制模板功能。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitTemplate: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplate`
        :param _RateLimitIntelligence: 智能客户端过滤。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitIntelligence: :class:`tencentcloud.teo.v20220901.models.RateLimitIntelligence`
        :param _RateLimitCustomizes: 速率限制-托管定制规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitCustomizes: list of RateLimitUserRule
        """
        self._Switch = None
        self._RateLimitUserRules = None
        self._RateLimitTemplate = None
        self._RateLimitIntelligence = None
        self._RateLimitCustomizes = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RateLimitUserRules(self):
        return self._RateLimitUserRules

    @RateLimitUserRules.setter
    def RateLimitUserRules(self, RateLimitUserRules):
        self._RateLimitUserRules = RateLimitUserRules

    @property
    def RateLimitTemplate(self):
        return self._RateLimitTemplate

    @RateLimitTemplate.setter
    def RateLimitTemplate(self, RateLimitTemplate):
        self._RateLimitTemplate = RateLimitTemplate

    @property
    def RateLimitIntelligence(self):
        return self._RateLimitIntelligence

    @RateLimitIntelligence.setter
    def RateLimitIntelligence(self, RateLimitIntelligence):
        self._RateLimitIntelligence = RateLimitIntelligence

    @property
    def RateLimitCustomizes(self):
        return self._RateLimitCustomizes

    @RateLimitCustomizes.setter
    def RateLimitCustomizes(self, RateLimitCustomizes):
        self._RateLimitCustomizes = RateLimitCustomizes


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RateLimitUserRules") is not None:
            self._RateLimitUserRules = []
            for item in params.get("RateLimitUserRules"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self._RateLimitUserRules.append(obj)
        if params.get("RateLimitTemplate") is not None:
            self._RateLimitTemplate = RateLimitTemplate()
            self._RateLimitTemplate._deserialize(params.get("RateLimitTemplate"))
        if params.get("RateLimitIntelligence") is not None:
            self._RateLimitIntelligence = RateLimitIntelligence()
            self._RateLimitIntelligence._deserialize(params.get("RateLimitIntelligence"))
        if params.get("RateLimitCustomizes") is not None:
            self._RateLimitCustomizes = []
            for item in params.get("RateLimitCustomizes"):
                obj = RateLimitUserRule()
                obj._deserialize(item)
                self._RateLimitCustomizes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitIntelligence(AbstractModel):
    """智能客户端过滤

    """

    def __init__(self):
        r"""
        :param _Switch: 功能开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _Action: 执行动作，取值有：
<li>monitor：观察；</li>
<li>alg：挑战。</li>
        :type Action: str
        :param _RuleId: 规则id，仅出参使用。
        :type RuleId: int
        """
        self._Switch = None
        self._Action = None
        self._RuleId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplate(AbstractModel):
    """速率限制模板

    """

    def __init__(self):
        r"""
        :param _Mode: 模板等级名称，取值有：
<li>sup_loose：超级宽松；</li>
<li>loose：宽松；</li>
<li>emergency：紧急；</li>
<li>normal：适中；</li>
<li>strict：严格；</li>
<li>close：关闭，仅精准速率限制生效。</li>
        :type Mode: str
        :param _Action: 模板处置方式，取值有：
<li>alg：JavaScript挑战；</li>
<li>monitor：观察。</li>不填写默认取alg。
        :type Action: str
        :param _RateLimitTemplateDetail: 模板值详情。仅出参返回。
        :type RateLimitTemplateDetail: :class:`tencentcloud.teo.v20220901.models.RateLimitTemplateDetail`
        """
        self._Mode = None
        self._Action = None
        self._RateLimitTemplateDetail = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RateLimitTemplateDetail(self):
        return self._RateLimitTemplateDetail

    @RateLimitTemplateDetail.setter
    def RateLimitTemplateDetail(self, RateLimitTemplateDetail):
        self._RateLimitTemplateDetail = RateLimitTemplateDetail


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Action = params.get("Action")
        if params.get("RateLimitTemplateDetail") is not None:
            self._RateLimitTemplateDetail = RateLimitTemplateDetail()
            self._RateLimitTemplateDetail._deserialize(params.get("RateLimitTemplateDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitTemplateDetail(AbstractModel):
    """模板当前详细配置

    """

    def __init__(self):
        r"""
        :param _Mode: 模板等级名称，取值有：
<li>sup_loose：超级宽松；</li>
<li>loose：宽松；</li>
<li>emergency：紧急；</li>
<li>normal：适中；</li>
<li>strict：严格；</li>
<li>close：关闭，仅精准速率限制生效。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param _ID: 唯一id。
        :type ID: int
        :param _Action: 模板处置方式，取值有：
<li>alg：JavaScript挑战；</li>
<li>monitor：观察。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _PunishTime: 惩罚时间，取值范围0-2天，单位秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishTime: int
        :param _Threshold: 统计阈值，单位是次，取值范围0-4294967294。
        :type Threshold: int
        :param _Period: 统计周期，取值范围0-120秒。
        :type Period: int
        """
        self._Mode = None
        self._ID = None
        self._Action = None
        self._PunishTime = None
        self._Threshold = None
        self._Period = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PunishTime(self):
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._ID = params.get("ID")
        self._Action = params.get("Action")
        self._PunishTime = params.get("PunishTime")
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitUserRule(AbstractModel):
    """RateLimit规则

    """

    def __init__(self):
        r"""
        :param _Threshold: 速率限制统计阈值，单位是次，取值范围0-4294967294。
        :type Threshold: int
        :param _Period: 速率限制统计时间，取值范围 10/20/30/40/50/60 单位是秒。
        :type Period: int
        :param _RuleName: 规则名，只能以英文字符，数字，下划线组合，且不能以下划线开头。
        :type RuleName: str
        :param _Action: 处置动作，取值有： <li>monitor：观察；</li> <li>drop：拦截；</li><li> redirect：重定向；</li><li> page：指定页面；</li><li>alg：JavaScript 挑战。</li>	
        :type Action: str
        :param _PunishTime: 惩罚时长，0-2天。
        :type PunishTime: int
        :param _PunishTimeUnit: 处罚时长单位，取值有：
<li>second：秒；</li>
<li>minutes：分钟；</li>
<li>hour：小时。</li>
        :type PunishTimeUnit: str
        :param _RuleStatus: 规则状态，取值有：
<li>on：生效；</li>
<li>off：不生效。</li>默认 on 生效。
        :type RuleStatus: str
        :param _AclConditions: 规则详情。
        :type AclConditions: list of AclCondition
        :param _RulePriority: 规则权重，取值范围0-100。
        :type RulePriority: int
        :param _RuleID: 规则 Id。仅出参使用。
        :type RuleID: int
        :param _FreqFields: 过滤词，取值有：
<li>sip：客户端 ip。</li>
默认为空字符串。
        :type FreqFields: list of str
        :param _UpdateTime: 更新时间。仅出参使用。修改时默认为当前时间。
        :type UpdateTime: str
        :param _FreqScope: 统计范围。取值有：
<li>source_to_eo：（响应）源站到  EdgeOne；</li>
<li>client_to_eo：（请求）客户端到  EdgeOne。</li>
默认为 source_to_eo。
        :type FreqScope: list of str
        :param _Name: 自定义返回页面的名称。Action 是 page 时必填，且不能为空。
        :type Name: str
        :param _CustomResponseId: 自定义响应 Id。该 Id 可通过查询自定义错误页列表接口获取。默认值为default，使用系统默认页面。Action 是 page 时必填，且不能为空。	
        :type CustomResponseId: str
        :param _ResponseCode: 自定义返回页面的响应码。Action 是 page 时必填，且不能为空，取值: 100~600，不支持 3xx 响应码。默认值：567。
        :type ResponseCode: int
        :param _RedirectUrl: 重定向时候的地址。Action 是 redirect 时必填，且不能为空。
        :type RedirectUrl: str
        """
        self._Threshold = None
        self._Period = None
        self._RuleName = None
        self._Action = None
        self._PunishTime = None
        self._PunishTimeUnit = None
        self._RuleStatus = None
        self._AclConditions = None
        self._RulePriority = None
        self._RuleID = None
        self._FreqFields = None
        self._UpdateTime = None
        self._FreqScope = None
        self._Name = None
        self._CustomResponseId = None
        self._ResponseCode = None
        self._RedirectUrl = None

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PunishTime(self):
        return self._PunishTime

    @PunishTime.setter
    def PunishTime(self, PunishTime):
        self._PunishTime = PunishTime

    @property
    def PunishTimeUnit(self):
        return self._PunishTimeUnit

    @PunishTimeUnit.setter
    def PunishTimeUnit(self, PunishTimeUnit):
        self._PunishTimeUnit = PunishTimeUnit

    @property
    def RuleStatus(self):
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def AclConditions(self):
        return self._AclConditions

    @AclConditions.setter
    def AclConditions(self, AclConditions):
        self._AclConditions = AclConditions

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def RuleID(self):
        return self._RuleID

    @RuleID.setter
    def RuleID(self, RuleID):
        self._RuleID = RuleID

    @property
    def FreqFields(self):
        return self._FreqFields

    @FreqFields.setter
    def FreqFields(self, FreqFields):
        self._FreqFields = FreqFields

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def FreqScope(self):
        return self._FreqScope

    @FreqScope.setter
    def FreqScope(self, FreqScope):
        self._FreqScope = FreqScope

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CustomResponseId(self):
        return self._CustomResponseId

    @CustomResponseId.setter
    def CustomResponseId(self, CustomResponseId):
        self._CustomResponseId = CustomResponseId

    @property
    def ResponseCode(self):
        return self._ResponseCode

    @ResponseCode.setter
    def ResponseCode(self, ResponseCode):
        self._ResponseCode = ResponseCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._Threshold = params.get("Threshold")
        self._Period = params.get("Period")
        self._RuleName = params.get("RuleName")
        self._Action = params.get("Action")
        self._PunishTime = params.get("PunishTime")
        self._PunishTimeUnit = params.get("PunishTimeUnit")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("AclConditions") is not None:
            self._AclConditions = []
            for item in params.get("AclConditions"):
                obj = AclCondition()
                obj._deserialize(item)
                self._AclConditions.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._RuleID = params.get("RuleID")
        self._FreqFields = params.get("FreqFields")
        self._UpdateTime = params.get("UpdateTime")
        self._FreqScope = params.get("FreqScope")
        self._Name = params.get("Name")
        self._CustomResponseId = params.get("CustomResponseId")
        self._ResponseCode = params.get("ResponseCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """计费资源

    """

    def __init__(self):
        r"""
        :param _Id: 资源 ID。
        :type Id: str
        :param _PayMode: 付费模式，取值有：
<li>0：后付费。</li>
        :type PayMode: int
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _EnableTime: 生效时间。
        :type EnableTime: str
        :param _ExpireTime: 失效时间。
        :type ExpireTime: str
        :param _Status: 套餐状态，取值有：
<li>normal：正常；</li>
<li>isolated：隔离；</li>
<li>destroyed：销毁。</li>
        :type Status: str
        :param _Sv: 询价参数。
        :type Sv: list of Sv
        :param _AutoRenewFlag: 是否自动续费，取值有：
<li>0：默认状态；</li>
<li>1：自动续费；</li>
<li>2：不自动续费。</li>
        :type AutoRenewFlag: int
        :param _PlanId: 套餐关联资源 ID。
        :type PlanId: str
        :param _Area: 地域，取值有：
<li>mainland：国内；</li>
<li>overseas：海外。</li>
<li>global：全球。</li>
        :type Area: str
        :param _Group: 资源类型，取值有：
<li>plan：套餐类型；</li>
<li>pay-as-you-go：后付费类型。</li>
<li>value-added：增值服务类型。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: str
        :param _ZoneNumber: 当前资源绑定的站点数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneNumber: int
        """
        self._Id = None
        self._PayMode = None
        self._CreateTime = None
        self._EnableTime = None
        self._ExpireTime = None
        self._Status = None
        self._Sv = None
        self._AutoRenewFlag = None
        self._PlanId = None
        self._Area = None
        self._Group = None
        self._ZoneNumber = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableTime(self):
        return self._EnableTime

    @EnableTime.setter
    def EnableTime(self, EnableTime):
        self._EnableTime = EnableTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Sv(self):
        return self._Sv

    @Sv.setter
    def Sv(self, Sv):
        self._Sv = Sv

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def ZoneNumber(self):
        return self._ZoneNumber

    @ZoneNumber.setter
    def ZoneNumber(self, ZoneNumber):
        self._ZoneNumber = ZoneNumber


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PayMode = params.get("PayMode")
        self._CreateTime = params.get("CreateTime")
        self._EnableTime = params.get("EnableTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Status = params.get("Status")
        if params.get("Sv") is not None:
            self._Sv = []
            for item in params.get("Sv"):
                obj = Sv()
                obj._deserialize(item)
                self._Sv.append(obj)
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PlanId = params.get("PlanId")
        self._Area = params.get("Area")
        self._Group = params.get("Group")
        self._ZoneNumber = params.get("ZoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewriteAction(AbstractModel):
    """规则引擎HTTP请求头/响应头类型的动作

    """

    def __init__(self):
        r"""
        :param _Action: 功能名称，功能名称填写规范可调用接口 [查询规则引擎的设置参数](https://cloud.tencent.com/document/product/1552/80618) 查看。
        :type Action: str
        :param _Parameters: 参数。
        :type Parameters: list of RuleRewriteActionParams
        """
        self._Action = None
        self._Parameters = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = RuleRewriteActionParams()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """规则引擎规则项，Conditions 数组内多个项的关系为 或，内层 Conditions 列表内多个项的关系为 且。

    """

    def __init__(self):
        r"""
        :param _Actions: 执行的功能。
        :type Actions: list of Action
        :param _Conditions: 执行功能判断条件。
注意：满足该数组内任意一项条件，功能即可执行。
        :type Conditions: list of RuleAndConditions
        :param _SubRules: 嵌套规则。
        :type SubRules: list of SubRuleItem
        """
        self._Actions = None
        self._Conditions = None
        self._SubRules = None

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def SubRules(self):
        return self._SubRules

    @SubRules.setter
    def SubRules(self, SubRules):
        self._SubRules = SubRules


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("SubRules") is not None:
            self._SubRules = []
            for item in params.get("SubRules"):
                obj = SubRuleItem()
                obj._deserialize(item)
                self._SubRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAndConditions(AbstractModel):
    """规则引擎条件且关系条件列表

    """

    def __init__(self):
        r"""
        :param _Conditions: 规则引擎条件，该数组内所有项全部满足即判断该条件满足。
        :type Conditions: list of RuleCondition
        """
        self._Conditions = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleChoicePropertiesItem(AbstractModel):
    """规则引擎可应用于匹配请求的设置详细信息，可选参数配置项

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称。
        :type Name: str
        :param _Type: 参数值类型。
<li> CHOICE：参数值只能在 ChoicesValue 中选择； </li>
<li> TOGGLE：参数值为开关类型，可在 ChoicesValue 中选择；</li>
<li> CUSTOM_NUM：参数值用户自定义，整型类型；</li>
<li> CUSTOM_STRING：参数值用户自定义，字符串类型。</li>
        :type Type: str
        :param _ChoicesValue: 参数值的可选值。
注意：若参数值为用户自定义则该数组为空数组。
        :type ChoicesValue: list of str
        :param _Min: 数值参数的最小值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Min: int
        :param _Max: 数值参数的最大值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Max: int
        :param _IsMultiple: 参数值是否支持多选或者填写多个。
        :type IsMultiple: bool
        :param _IsAllowEmpty: 是否允许为空。
        :type IsAllowEmpty: bool
        :param _ExtraParameter: 特殊参数。
<li> 为 NULL：RuleAction 选择 NormalAction；</li>
<li> 成员参数 Id 为 Action：RuleAction 选择 RewirteAction；</li>
<li> 成员参数 Id 为 StatusCode：RuleAction 选择 CodeAction。</li>
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self._Name = None
        self._Type = None
        self._ChoicesValue = None
        self._Min = None
        self._Max = None
        self._IsMultiple = None
        self._IsAllowEmpty = None
        self._ExtraParameter = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ChoicesValue(self):
        return self._ChoicesValue

    @ChoicesValue.setter
    def ChoicesValue(self, ChoicesValue):
        self._ChoicesValue = ChoicesValue

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def IsMultiple(self):
        return self._IsMultiple

    @IsMultiple.setter
    def IsMultiple(self, IsMultiple):
        self._IsMultiple = IsMultiple

    @property
    def IsAllowEmpty(self):
        return self._IsAllowEmpty

    @IsAllowEmpty.setter
    def IsAllowEmpty(self, IsAllowEmpty):
        self._IsAllowEmpty = IsAllowEmpty

    @property
    def ExtraParameter(self):
        return self._ExtraParameter

    @ExtraParameter.setter
    def ExtraParameter(self, ExtraParameter):
        self._ExtraParameter = ExtraParameter


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._ChoicesValue = params.get("ChoicesValue")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._IsMultiple = params.get("IsMultiple")
        self._IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ExtraParameter") is not None:
            self._ExtraParameter = RuleExtraParameter()
            self._ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCodeActionParams(AbstractModel):
    """规则引擎条件使用StatusCode字段动作参数

    """

    def __init__(self):
        r"""
        :param _StatusCode: 状态 Code。
        :type StatusCode: int
        :param _Name: 参数名称，参数填写规范可调用接口 [查询规则引擎的设置参数](https://cloud.tencent.com/document/product/1552/80618) 查看。
        :type Name: str
        :param _Values: 参数值。
        :type Values: list of str
        """
        self._StatusCode = None
        self._Name = None
        self._Values = None

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._StatusCode = params.get("StatusCode")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    """规则引擎条件参数

    """

    def __init__(self):
        r"""
        :param _Operator: 运算符，取值有：
<li> equal: 等于； </li>
<li> notequal: 不等于；</li>
<li> exist: 存在； </li>
<li> notexist: 不存在。</li>
        :type Operator: str
        :param _Target: 匹配类型，取值有： <li> filename：文件名； </li> <li> extension：文件后缀； </li> <li> host：HOST； </li> <li> full_url：URL Full，当前站点下完整 URL 路径，必须包含 HTTP 协议，Host 和 路径； </li> <li> url：URL Path，当前站点下 URL 路径的请求； </li><li>client_country：客户端国家/地区；</li> <li> query_string：查询字符串，当前站点下请求URL的查询字符串； </li> <li> request_header：HTTP请求头部。 </li>
        :type Target: str
        :param _Values: 对应匹配类型的参数值，仅在匹配类型为查询字符串或HTTP请求头并且运算符取值为存在或不存在时允许传空数组，对应匹配类型有：
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
        :param _IgnoreCase: 是否忽略参数值的大小写，默认值为 false。
        :type IgnoreCase: bool
        :param _Name: 对应匹配类型的参数名称，在 Target 值为以下取值时有效，有效时值不能为空：
<li> query_string（查询字符串）: 当前站点下URL请求中查询字符串的参数名称，例如lang=cn&version=1中的lang和version； </li>
<li> request_header（HTTP 请求头）: HTTP请求头部字段名，例如Accept-Language:zh-CN,zh;q=0.9中的Accept-Language。 </li>
        :type Name: str
        :param _IgnoreNameCase: 是否忽略参数名称的大小写，默认值为 false。
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreNameCase: bool
        """
        self._Operator = None
        self._Target = None
        self._Values = None
        self._IgnoreCase = None
        self._Name = None
        self._IgnoreNameCase = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def IgnoreCase(self):
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IgnoreNameCase(self):
        warnings.warn("parameter `IgnoreNameCase` is deprecated", DeprecationWarning) 

        return self._IgnoreNameCase

    @IgnoreNameCase.setter
    def IgnoreNameCase(self, IgnoreNameCase):
        warnings.warn("parameter `IgnoreNameCase` is deprecated", DeprecationWarning) 

        self._IgnoreNameCase = IgnoreNameCase


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        self._Target = params.get("Target")
        self._Values = params.get("Values")
        self._IgnoreCase = params.get("IgnoreCase")
        self._Name = params.get("Name")
        self._IgnoreNameCase = params.get("IgnoreNameCase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleExtraParameter(AbstractModel):
    """规则引擎参数详情信息，特殊参数类型。

    """

    def __init__(self):
        r"""
        :param _Id: 参数名，取值有：
<li> Action：修改 HTTP 头部所需参数，RuleAction 选择 RewirteAction；</li>
<li> StatusCode：状态码相关功能所需参数，RuleAction 选择 CodeAction。</li>
        :type Id: str
        :param _Type: 参数值类型。
<li> CHOICE：参数值只能在 Values 中选择； </li>
<li> CUSTOM_NUM：参数值用户自定义，整型类型；</li>
<li> CUSTOM_STRING：参数值用户自定义，字符串类型。</li>
        :type Type: str
        :param _Choices: 可选参数值。
注意：当 Id 的值为 StatusCode 时数组中的值为整型，填写参数值时请填写字符串的整型数值。
        :type Choices: list of str
        """
        self._Id = None
        self._Type = None
        self._Choices = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Choices(self):
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Choices = params.get("Choices")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleItem(AbstractModel):
    """规则引擎规则详情

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID。
        :type RuleId: str
        :param _RuleName: 规则名称，名称字符串长度 1~255。
        :type RuleName: str
        :param _Status: 规则状态，取值有:
<li> enable: 启用； </li>
<li> disable: 未启用。 </li>
        :type Status: str
        :param _Rules: 规则内容。
        :type Rules: list of Rule
        :param _RulePriority: 规则优先级, 值越大优先级越高，最小为 1。
        :type RulePriority: int
        :param _Tags: 规则标签。
        :type Tags: list of str
        """
        self._RuleId = None
        self._RuleName = None
        self._Status = None
        self._Rules = None
        self._RulePriority = None
        self._Tags = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RulePriority(self):
        return self._RulePriority

    @RulePriority.setter
    def RulePriority(self, RulePriority):
        self._RulePriority = RulePriority

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RulePriority = params.get("RulePriority")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleNormalActionParams(AbstractModel):
    """规则引擎条件常规动作参数

    """

    def __init__(self):
        r"""
        :param _Name: 参数名称，参数填写规范可调用接口 [查询规则引擎的设置参数](https://cloud.tencent.com/document/product/1552/80618) 查看。
        :type Name: str
        :param _Values: 参数值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleRewriteActionParams(AbstractModel):
    """规则引擎条件 HTTP 请求/响应头操作动作参数。

    """

    def __init__(self):
        r"""
        :param _Action: 功能参数名称，参数填写规范可调用接口 [查询规则引擎的设置参数](https://cloud.tencent.com/document/product/1552/80618) 查看。现在只有三种取值：
<li> add：添加 HTTP 头部；</li>
<li> set：重写 HTTP 头部；</li>
<li> del：删除 HTTP 头部。</li>
        :type Action: str
        :param _Name: 参数名称。
        :type Name: str
        :param _Values: 参数值。
        :type Values: list of str
        """
        self._Action = None
        self._Name = None
        self._Values = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesProperties(AbstractModel):
    """规则引擎可应用于匹配请求的设置详细信息。

    """

    def __init__(self):
        r"""
        :param _Name: 值为参数名称。
        :type Name: str
        :param _Min: 数值参数的最小值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Min: int
        :param _ChoicesValue: 参数值的可选值。
注意：若参数值为用户自定义则该数组为空数组。
        :type ChoicesValue: list of str
        :param _Type: 参数值类型。
<li> CHOICE：参数值只能在 ChoicesValue 中选择； </li>
<li> TOGGLE：参数值为开关类型，可在 ChoicesValue 中选择；</li>
<li> OBJECT：参数值为对象类型，ChoiceProperties 为改对象类型关联的属性；</li>
<li> CUSTOM_NUM：参数值用户自定义，整型类型；</li>
<li> CUSTOM_STRING：参数值用户自定义，字符串类型。</li>注意：当参数类型为 OBJECT 类型时，请注意参考 [示例2 参数为 OBJECT 类型的创建](https://cloud.tencent.com/document/product/1552/80622#.E7.A4.BA.E4.BE.8B2-.E5.8F.82.E6.95.B0.E4.B8.BA-OBJECT-.E7.B1.BB.E5.9E.8B.E7.9A.84.E5.88.9B.E5.BB.BA)
        :type Type: str
        :param _Max: 数值参数的最大值，非数值参数或 Min 和 Max 值都为 0 则此项无意义。
        :type Max: int
        :param _IsMultiple: 参数值是否支持多选或者填写多个。
        :type IsMultiple: bool
        :param _IsAllowEmpty: 是否允许为空。
        :type IsAllowEmpty: bool
        :param _ChoiceProperties: 该参数对应的关联配置参数，属于调用接口的必填参数。
注意：如果可选参数无特殊新增参数则该数组为空数组。
        :type ChoiceProperties: list of RuleChoicePropertiesItem
        :param _ExtraParameter: <li> 为 NULL：无特殊参数，RuleAction 选择 NormalAction；</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraParameter: :class:`tencentcloud.teo.v20220901.models.RuleExtraParameter`
        """
        self._Name = None
        self._Min = None
        self._ChoicesValue = None
        self._Type = None
        self._Max = None
        self._IsMultiple = None
        self._IsAllowEmpty = None
        self._ChoiceProperties = None
        self._ExtraParameter = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def ChoicesValue(self):
        return self._ChoicesValue

    @ChoicesValue.setter
    def ChoicesValue(self, ChoicesValue):
        self._ChoicesValue = ChoicesValue

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def IsMultiple(self):
        return self._IsMultiple

    @IsMultiple.setter
    def IsMultiple(self, IsMultiple):
        self._IsMultiple = IsMultiple

    @property
    def IsAllowEmpty(self):
        return self._IsAllowEmpty

    @IsAllowEmpty.setter
    def IsAllowEmpty(self, IsAllowEmpty):
        self._IsAllowEmpty = IsAllowEmpty

    @property
    def ChoiceProperties(self):
        return self._ChoiceProperties

    @ChoiceProperties.setter
    def ChoiceProperties(self, ChoiceProperties):
        self._ChoiceProperties = ChoiceProperties

    @property
    def ExtraParameter(self):
        return self._ExtraParameter

    @ExtraParameter.setter
    def ExtraParameter(self, ExtraParameter):
        self._ExtraParameter = ExtraParameter


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Min = params.get("Min")
        self._ChoicesValue = params.get("ChoicesValue")
        self._Type = params.get("Type")
        self._Max = params.get("Max")
        self._IsMultiple = params.get("IsMultiple")
        self._IsAllowEmpty = params.get("IsAllowEmpty")
        if params.get("ChoiceProperties") is not None:
            self._ChoiceProperties = []
            for item in params.get("ChoiceProperties"):
                obj = RuleChoicePropertiesItem()
                obj._deserialize(item)
                self._ChoiceProperties.append(obj)
        if params.get("ExtraParameter") is not None:
            self._ExtraParameter = RuleExtraParameter()
            self._ExtraParameter._deserialize(params.get("ExtraParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RulesSettingAction(AbstractModel):
    """规则引擎可应用于匹配请求的设置列表及其详细信息

    """

    def __init__(self):
        r"""
        :param _Action: 功能名称，取值有：
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
        :param _Properties: 参数信息。
        :type Properties: list of RulesProperties
        """
        self._Action = None
        self._Properties = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Properties(self):
        return self._Properties

    @Properties.setter
    def Properties(self, Properties):
        self._Properties = Properties


    def _deserialize(self, params):
        self._Action = params.get("Action")
        if params.get("Properties") is not None:
            self._Properties = []
            for item in params.get("Properties"):
                obj = RulesProperties()
                obj._deserialize(item)
                self._Properties.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntry(AbstractModel):
    """安全数据Entry返回值

    """

    def __init__(self):
        r"""
        :param _Key: 查询维度值。
        :type Key: str
        :param _Value: 查询维度下详细数据。
        :type Value: list of SecEntryValue
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = SecEntryValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecEntryValue(AbstractModel):
    """安全数据维度值信息

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名称。
        :type Metric: str
        :param _Detail: 时序数据详情。
        :type Detail: list of TimingDataItem
        :param _Max: 最大值。
        :type Max: int
        :param _Avg: 平均值。
        :type Avg: float
        :param _Sum: 数据总和。
        :type Sum: float
        """
        self._Metric = None
        self._Detail = None
        self._Max = None
        self._Avg = None
        self._Sum = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Avg(self):
        return self._Avg

    @Avg.setter
    def Avg(self, Avg):
        self._Avg = Avg

    @property
    def Sum(self):
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        self._Max = params.get("Max")
        self._Avg = params.get("Avg")
        self._Sum = params.get("Sum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityConfig(AbstractModel):
    """安全配置

    """

    def __init__(self):
        r"""
        :param _WafConfig: 托管规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WafConfig: :class:`tencentcloud.teo.v20220901.models.WafConfig`
        :param _RateLimitConfig: 速率限制。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitConfig: :class:`tencentcloud.teo.v20220901.models.RateLimitConfig`
        :param _AclConfig: 自定义规则。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AclConfig: :class:`tencentcloud.teo.v20220901.models.AclConfig`
        :param _BotConfig: Bot配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type BotConfig: :class:`tencentcloud.teo.v20220901.models.BotConfig`
        :param _SwitchConfig: 七层防护总开关。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchConfig: :class:`tencentcloud.teo.v20220901.models.SwitchConfig`
        :param _IpTableConfig: 基础访问管控。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpTableConfig: :class:`tencentcloud.teo.v20220901.models.IpTableConfig`
        :param _ExceptConfig: 例外规则配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExceptConfig: :class:`tencentcloud.teo.v20220901.models.ExceptConfig`
        :param _DropPageConfig: 自定义拦截页面配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DropPageConfig: :class:`tencentcloud.teo.v20220901.models.DropPageConfig`
        :param _TemplateConfig: 模板配置。此处仅出参数使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateConfig: :class:`tencentcloud.teo.v20220901.models.TemplateConfig`
        :param _SlowPostConfig: 慢速攻击配置。如果为null，默认使用历史配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowPostConfig: :class:`tencentcloud.teo.v20220901.models.SlowPostConfig`
        """
        self._WafConfig = None
        self._RateLimitConfig = None
        self._AclConfig = None
        self._BotConfig = None
        self._SwitchConfig = None
        self._IpTableConfig = None
        self._ExceptConfig = None
        self._DropPageConfig = None
        self._TemplateConfig = None
        self._SlowPostConfig = None

    @property
    def WafConfig(self):
        return self._WafConfig

    @WafConfig.setter
    def WafConfig(self, WafConfig):
        self._WafConfig = WafConfig

    @property
    def RateLimitConfig(self):
        return self._RateLimitConfig

    @RateLimitConfig.setter
    def RateLimitConfig(self, RateLimitConfig):
        self._RateLimitConfig = RateLimitConfig

    @property
    def AclConfig(self):
        return self._AclConfig

    @AclConfig.setter
    def AclConfig(self, AclConfig):
        self._AclConfig = AclConfig

    @property
    def BotConfig(self):
        return self._BotConfig

    @BotConfig.setter
    def BotConfig(self, BotConfig):
        self._BotConfig = BotConfig

    @property
    def SwitchConfig(self):
        return self._SwitchConfig

    @SwitchConfig.setter
    def SwitchConfig(self, SwitchConfig):
        self._SwitchConfig = SwitchConfig

    @property
    def IpTableConfig(self):
        return self._IpTableConfig

    @IpTableConfig.setter
    def IpTableConfig(self, IpTableConfig):
        self._IpTableConfig = IpTableConfig

    @property
    def ExceptConfig(self):
        return self._ExceptConfig

    @ExceptConfig.setter
    def ExceptConfig(self, ExceptConfig):
        self._ExceptConfig = ExceptConfig

    @property
    def DropPageConfig(self):
        return self._DropPageConfig

    @DropPageConfig.setter
    def DropPageConfig(self, DropPageConfig):
        self._DropPageConfig = DropPageConfig

    @property
    def TemplateConfig(self):
        return self._TemplateConfig

    @TemplateConfig.setter
    def TemplateConfig(self, TemplateConfig):
        self._TemplateConfig = TemplateConfig

    @property
    def SlowPostConfig(self):
        return self._SlowPostConfig

    @SlowPostConfig.setter
    def SlowPostConfig(self, SlowPostConfig):
        self._SlowPostConfig = SlowPostConfig


    def _deserialize(self, params):
        if params.get("WafConfig") is not None:
            self._WafConfig = WafConfig()
            self._WafConfig._deserialize(params.get("WafConfig"))
        if params.get("RateLimitConfig") is not None:
            self._RateLimitConfig = RateLimitConfig()
            self._RateLimitConfig._deserialize(params.get("RateLimitConfig"))
        if params.get("AclConfig") is not None:
            self._AclConfig = AclConfig()
            self._AclConfig._deserialize(params.get("AclConfig"))
        if params.get("BotConfig") is not None:
            self._BotConfig = BotConfig()
            self._BotConfig._deserialize(params.get("BotConfig"))
        if params.get("SwitchConfig") is not None:
            self._SwitchConfig = SwitchConfig()
            self._SwitchConfig._deserialize(params.get("SwitchConfig"))
        if params.get("IpTableConfig") is not None:
            self._IpTableConfig = IpTableConfig()
            self._IpTableConfig._deserialize(params.get("IpTableConfig"))
        if params.get("ExceptConfig") is not None:
            self._ExceptConfig = ExceptConfig()
            self._ExceptConfig._deserialize(params.get("ExceptConfig"))
        if params.get("DropPageConfig") is not None:
            self._DropPageConfig = DropPageConfig()
            self._DropPageConfig._deserialize(params.get("DropPageConfig"))
        if params.get("TemplateConfig") is not None:
            self._TemplateConfig = TemplateConfig()
            self._TemplateConfig._deserialize(params.get("TemplateConfig"))
        if params.get("SlowPostConfig") is not None:
            self._SlowPostConfig = SlowPostConfig()
            self._SlowPostConfig._deserialize(params.get("SlowPostConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityTemplateBinding(AbstractModel):
    """安全策略模板的绑定关系。

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID
        :type TemplateId: str
        :param _TemplateScope: 模板绑定状态。
        :type TemplateScope: list of TemplateScope
        """
        self._TemplateId = None
        self._TemplateScope = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateScope(self):
        return self._TemplateScope

    @TemplateScope.setter
    def TemplateScope(self, TemplateScope):
        self._TemplateScope = TemplateScope


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("TemplateScope") is not None:
            self._TemplateScope = []
            for item in params.get("TemplateScope"):
                obj = TemplateScope()
                obj._deserialize(item)
                self._TemplateScope.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityType(AbstractModel):
    """安全类型配置项。

    """

    def __init__(self):
        r"""
        :param _Switch: 安全类型开关，取值为：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCertInfo(AbstractModel):
    """https 服务端证书配置

    """

    def __init__(self):
        r"""
        :param _CertId: 服务器证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _Alias: 证书备注名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Type: 证书类型，取值有：
<li>default：默认证书；</li>
<li>upload：用户上传；</li>
<li>managed：腾讯云托管。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _DeployTime: 证书部署时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param _SignAlgo: 签名算法。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignAlgo: str
        :param _CommonName: 证书归属域名名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonName: str
        """
        self._CertId = None
        self._Alias = None
        self._Type = None
        self._ExpireTime = None
        self._DeployTime = None
        self._SignAlgo = None
        self._CommonName = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def SignAlgo(self):
        return self._SignAlgo

    @SignAlgo.setter
    def SignAlgo(self, SignAlgo):
        self._SignAlgo = SignAlgo

    @property
    def CommonName(self):
        return self._CommonName

    @CommonName.setter
    def CommonName(self, CommonName):
        self._CommonName = CommonName


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._SignAlgo = params.get("SignAlgo")
        self._CommonName = params.get("CommonName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkipCondition(AbstractModel):
    """例外规则的跳过匹配条件，即在例外时根据本匹配条件，略过指定字段及内容。

    """

    def __init__(self):
        r"""
        :param _Type: 例外跳过类型，取值为：
<li>header_fields：HTTP请求Header；</li>
<li>cookie：HTTP请求Cookie；</li>
<li>query_string：HTTP请求URL中的Query参数；</li>
<li>uri：HTTP请求URI；</li>
<li>body_raw：HTTP请求Body；</li>
<li>body_json： JSON格式的HTTP Body。</li>
        :type Type: str
        :param _Selector: 选择跳过的字段，取值为：
<li>args：uri 下选择 query 参数: ?name1=jack&age=12；</li>
<li>path：uri 下选择部分路径：/path/to/resource.jpg；</li>
<li>full：uri 下选择完整路径：example.com/path/to/resource.jpg?name1=jack&age=12；</li>
<li>upload_filename：分段文件名，即分段传输文件时；</li>
<li>keys：所有的Key；</li>
<li>values：匹配Key对应的值；</li>
<li>key_value：匹配Key及匹配Value。</li>
        :type Selector: str
        :param _MatchFromType: 匹配Key所使用的匹配方式，取值为：
<li>equal：精准匹配，等于；</li>
<li>wildcard：通配符匹配，支持 * 通配。</li>
        :type MatchFromType: str
        :param _MatchFrom: 匹配Key的值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchFrom: list of str
        :param _MatchContentType: 匹配Content所使用的匹配方式，取值为：
<li>equal：精准匹配，等于；</li>
<li>wildcard：通配符匹配，支持 * 通配。</li>
        :type MatchContentType: str
        :param _MatchContent: 匹配Value的值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchContent: list of str
        """
        self._Type = None
        self._Selector = None
        self._MatchFromType = None
        self._MatchFrom = None
        self._MatchContentType = None
        self._MatchContent = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Selector(self):
        return self._Selector

    @Selector.setter
    def Selector(self, Selector):
        self._Selector = Selector

    @property
    def MatchFromType(self):
        return self._MatchFromType

    @MatchFromType.setter
    def MatchFromType(self, MatchFromType):
        self._MatchFromType = MatchFromType

    @property
    def MatchFrom(self):
        return self._MatchFrom

    @MatchFrom.setter
    def MatchFrom(self, MatchFrom):
        self._MatchFrom = MatchFrom

    @property
    def MatchContentType(self):
        return self._MatchContentType

    @MatchContentType.setter
    def MatchContentType(self, MatchContentType):
        self._MatchContentType = MatchContentType

    @property
    def MatchContent(self):
        return self._MatchContent

    @MatchContent.setter
    def MatchContent(self, MatchContent):
        self._MatchContent = MatchContent


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Selector = params.get("Selector")
        self._MatchFromType = params.get("MatchFromType")
        self._MatchFrom = params.get("MatchFrom")
        self._MatchContentType = params.get("MatchContentType")
        self._MatchContent = params.get("MatchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowPostConfig(AbstractModel):
    """慢速攻击配置。

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _FirstPartConfig: 首包配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstPartConfig: :class:`tencentcloud.teo.v20220901.models.FirstPartConfig`
        :param _SlowRateConfig: 基础配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowRateConfig: :class:`tencentcloud.teo.v20220901.models.SlowRateConfig`
        :param _Action: 慢速攻击的处置动作，取值有：
<li>monitor：观察；</li>
<li>drop：拦截。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _RuleId: 本规则的Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        """
        self._Switch = None
        self._FirstPartConfig = None
        self._SlowRateConfig = None
        self._Action = None
        self._RuleId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FirstPartConfig(self):
        return self._FirstPartConfig

    @FirstPartConfig.setter
    def FirstPartConfig(self, FirstPartConfig):
        self._FirstPartConfig = FirstPartConfig

    @property
    def SlowRateConfig(self):
        return self._SlowRateConfig

    @SlowRateConfig.setter
    def SlowRateConfig(self, SlowRateConfig):
        self._SlowRateConfig = SlowRateConfig

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("FirstPartConfig") is not None:
            self._FirstPartConfig = FirstPartConfig()
            self._FirstPartConfig._deserialize(params.get("FirstPartConfig"))
        if params.get("SlowRateConfig") is not None:
            self._SlowRateConfig = SlowRateConfig()
            self._SlowRateConfig._deserialize(params.get("SlowRateConfig"))
        self._Action = params.get("Action")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlowRateConfig(AbstractModel):
    """慢速攻击的基础配置。

    """

    def __init__(self):
        r"""
        :param _Switch: 开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _Interval: 统计的间隔，单位是秒，即在首段包传输结束后，将数据传输轴按照本参数切分，每个分片独立计算慢速攻击。
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: int
        :param _Threshold: 统计时应用的速率阈值，单位是bps，即如果本分片中的传输速率没达到本参数的值，则判定为慢速攻击，应用慢速攻击的处置方式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Threshold: int
        """
        self._Switch = None
        self._Interval = None
        self._Threshold = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Interval = params.get("Interval")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartRouting(AbstractModel):
    """智能加速配置

    """

    def __init__(self):
        r"""
        :param _Switch: 智能加速配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardDebug(AbstractModel):
    """支持标准debug结构体

    """

    def __init__(self):
        r"""
        :param _Switch: Debug 功能开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        :param _AllowClientIPList: 允许的客户端来源。支持填写 IPV4 以及 IPV6 的 IP/IP 段，不填则表示允许任意客户端 IP。
        :type AllowClientIPList: list of str
        :param _ExpireTime: Debug 功能到期时间。超出设置的时间，则功能失效。
        :type ExpireTime: str
        """
        self._Switch = None
        self._AllowClientIPList = None
        self._ExpireTime = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AllowClientIPList(self):
        return self._AllowClientIPList

    @AllowClientIPList.setter
    def AllowClientIPList(self, AllowClientIPList):
        self._AllowClientIPList = AllowClientIPList

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AllowClientIPList = params.get("AllowClientIPList")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRule(AbstractModel):
    """嵌套规则信息。

    """

    def __init__(self):
        r"""
        :param _Conditions: 执行功能判断条件。
注意：满足该数组内任意一项条件，功能即可执行。
        :type Conditions: list of RuleAndConditions
        :param _Actions: 执行的功能。
        :type Actions: list of Action
        """
        self._Conditions = None
        self._Actions = None

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleAndConditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self._Actions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubRuleItem(AbstractModel):
    """规则引擎嵌套规则

    """

    def __init__(self):
        r"""
        :param _Rules: 嵌套规则信息。
        :type Rules: list of SubRule
        :param _Tags: 规则标签。
        :type Tags: list of str
        """
        self._Rules = None
        self._Tags = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SubRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sv(AbstractModel):
    """询价参数

    """

    def __init__(self):
        r"""
        :param _Key: 询价参数键。
        :type Key: str
        :param _Value: 询价参数值。
        :type Value: str
        :param _Pack: 询价参数映射的配额，取值有：
<li>zone：站点数；</li>
<li>custom-rule：自定义规则数；</li>
<li>rate-limiting-rule：速率限制规则数；</li>
<li>l4-proxy-instance：四层代理实例数。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type Pack: str
        :param _InstanceId: 询价参数映射的四层代理实例Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ProtectionSpecs: 询价参数对应的防护等级。
取值有： <li> cm_30G：中国大陆加速区域保底防护30Gbps；</li><li> cm_60G：中国大陆加速区域保底防护60Gbps；</li><li> cm_100G：中国大陆加速区域保底防护100Gbps；</li><li> anycast_300G：全球加速区域（除中国大陆）Anycast联防300Gbps；</li><li> anycast_unlimited：全球加速区域（除中国大陆）Anycast无上限全力防护；</li><li> cm_30G_anycast_300G：中国大陆加速区域保底防护30Gbps，全球加速区域（除中国大陆）Anycast联防300Gbps；</li><li> cm_30G_anycast_unlimited：中国大陆加速区域保底防护30Gbps，全球加速区域（除中国大陆）Anycast无上限全力防护；</li><li> cm_60G_anycast_300G：中国大陆加速区域保底防护60Gbps，全球加速区域（除中国大陆）Anycast联防300Gbps；</li><li> cm_60G_anycast_unlimited：中国大陆加速区域保底防护60Gbps，全球加速区域（除中国大陆）Anycast无上限全力防护；</li><li> cm_100G_anycast_300G：中国大陆加速区域保底防护100Gbps，全球加速区域（除中国大陆）Anycast联防300Gbps；</li><li> cm_100G_anycast_unlimited：中国大陆加速区域保底防护100Gbps，全球加速区域（除中国大陆）Anycast无上限全力防护。</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectionSpecs: str
        """
        self._Key = None
        self._Value = None
        self._Pack = None
        self._InstanceId = None
        self._ProtectionSpecs = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Pack(self):
        return self._Pack

    @Pack.setter
    def Pack(self, Pack):
        self._Pack = Pack

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProtectionSpecs(self):
        return self._ProtectionSpecs

    @ProtectionSpecs.setter
    def ProtectionSpecs(self, ProtectionSpecs):
        self._ProtectionSpecs = ProtectionSpecs


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Pack = params.get("Pack")
        self._InstanceId = params.get("InstanceId")
        self._ProtectionSpecs = params.get("ProtectionSpecs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchConfig(AbstractModel):
    """功能总开关

    """

    def __init__(self):
        r"""
        :param _WebSwitch: Web类型的安全总开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>不影响DDoS与Bot的开关。
        :type WebSwitch: str
        """
        self._WebSwitch = None

    @property
    def WebSwitch(self):
        return self._WebSwitch

    @WebSwitch.setter
    def WebSwitch(self, WebSwitch):
        self._WebSwitch = WebSwitch


    def _deserialize(self, params):
        self._WebSwitch = params.get("WebSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签配置

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class Task(AbstractModel):
    """内容管理任务结果

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        :param _Status: 状态。
        :type Status: str
        :param _Target: 资源。
        :type Target: str
        :param _Type: 任务类型。
        :type Type: str
        :param _CreateTime: 任务创建时间。
        :type CreateTime: str
        :param _UpdateTime: 任务完成时间。
        :type UpdateTime: str
        """
        self._JobId = None
        self._Status = None
        self._Target = None
        self._Type = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._Status = params.get("Status")
        self._Target = params.get("Target")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateConfig(AbstractModel):
    """安全模板配置

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID。
        :type TemplateId: str
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        """
        self._TemplateId = None
        self._TemplateName = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateScope(AbstractModel):
    """安全模板绑定域名状态

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _EntityStatus: 实例状态列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EntityStatus: list of EntityStatus
        """
        self._ZoneId = None
        self._EntityStatus = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EntityStatus(self):
        return self._EntityStatus

    @EntityStatus.setter
    def EntityStatus(self, EntityStatus):
        self._EntityStatus = EntityStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("EntityStatus") is not None:
            self._EntityStatus = []
            for item in params.get("EntityStatus"):
                obj = EntityStatus()
                obj._deserialize(item)
                self._EntityStatus.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataItem(AbstractModel):
    """统计曲线数据项

    """

    def __init__(self):
        r"""
        :param _Timestamp: 返回数据对应时间点，采用unix秒级时间戳。
        :type Timestamp: int
        :param _Value: 具体数值。
        :type Value: int
        """
        self._Timestamp = None
        self._Value = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingDataRecord(AbstractModel):
    """时序数据信息

    """

    def __init__(self):
        r"""
        :param _TypeKey: 查询维度值。
        :type TypeKey: str
        :param _TypeValue: 详细时序数据。
        :type TypeValue: list of TimingTypeValue
        """
        self._TypeKey = None
        self._TypeValue = None

    @property
    def TypeKey(self):
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey

    @property
    def TypeValue(self):
        return self._TypeValue

    @TypeValue.setter
    def TypeValue(self, TypeValue):
        self._TypeValue = TypeValue


    def _deserialize(self, params):
        self._TypeKey = params.get("TypeKey")
        if params.get("TypeValue") is not None:
            self._TypeValue = []
            for item in params.get("TypeValue"):
                obj = TimingTypeValue()
                obj._deserialize(item)
                self._TypeValue.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingTypeValue(AbstractModel):
    """时序类型详细数据

    """

    def __init__(self):
        r"""
        :param _Sum: 数据和。
        :type Sum: int
        :param _Max: 最大值。
        :type Max: int
        :param _Avg: 平均值。
        :type Avg: int
        :param _MetricName: 指标名。
        :type MetricName: str
        :param _Detail: 详细数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: list of TimingDataItem
        """
        self._Sum = None
        self._Max = None
        self._Avg = None
        self._MetricName = None
        self._Detail = None

    @property
    def Sum(self):
        return self._Sum

    @Sum.setter
    def Sum(self, Sum):
        self._Sum = Sum

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def Avg(self):
        return self._Avg

    @Avg.setter
    def Avg(self, Avg):
        self._Avg = Avg

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Sum = params.get("Sum")
        self._Max = params.get("Max")
        self._Avg = params.get("Avg")
        self._MetricName = params.get("MetricName")
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = TimingDataItem()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDataRecord(AbstractModel):
    """Top类数据记录

    """

    def __init__(self):
        r"""
        :param _TypeKey: 查询维度值。
        :type TypeKey: str
        :param _DetailData: top数据排行。
        :type DetailData: list of TopDetailData
        """
        self._TypeKey = None
        self._DetailData = None

    @property
    def TypeKey(self):
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey

    @property
    def DetailData(self):
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._TypeKey = params.get("TypeKey")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """Top数据的详细信息

    """

    def __init__(self):
        r"""
        :param _Key: 字段名。
        :type Key: str
        :param _Value: 字段值。
        :type Value: int
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class TopEntry(AbstractModel):
    """TopN的Entry数据

    """

    def __init__(self):
        r"""
        :param _Key: top查询维度值。
        :type Key: str
        :param _Value: 查询具体数据。
        :type Value: list of TopEntryValue
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        if params.get("Value") is not None:
            self._Value = []
            for item in params.get("Value"):
                obj = TopEntryValue()
                obj._deserialize(item)
                self._Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopEntryValue(AbstractModel):
    """TopN数据Entry

    """

    def __init__(self):
        r"""
        :param _Name: 排序实体名。
        :type Name: str
        :param _Count: 排序实体数量。
        :type Count: int
        """
        self._Name = None
        self._Count = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHttp2(AbstractModel):
    """Http2回源配置

    """

    def __init__(self):
        r"""
        :param _Switch: http2 回源配置开关，取值有：
<li>on：开启；</li>
<li>off：关闭。</li>
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServers(AbstractModel):
    """自定义 nameservers

    """

    def __init__(self):
        r"""
        :param _Switch: 自定义 ns 开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param _Servers: 自定义 ns 列表。
        :type Servers: list of str
        """
        self._Switch = None
        self._Servers = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Servers(self):
        return self._Servers

    @Servers.setter
    def Servers(self, Servers):
        self._Servers = Servers


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Servers = params.get("Servers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VanityNameServersIps(AbstractModel):
    """自定义名字服务器 IP 信息

    """

    def __init__(self):
        r"""
        :param _Name: 自定义名字服务器名称。
        :type Name: str
        :param _IPv4: 自定义名字服务器 IPv4 地址。
        :type IPv4: str
        """
        self._Name = None
        self._IPv4 = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IPv4(self):
        return self._IPv4

    @IPv4.setter
    def IPv4(self, IPv4):
        self._IPv4 = IPv4


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IPv4 = params.get("IPv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyOwnershipRequest(AbstractModel):
    """VerifyOwnership请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 站点或者加速域名。
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyOwnershipResponse(AbstractModel):
    """VerifyOwnership返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 归属权验证结果。
<li>success：验证成功；</li>
<li>fail：验证失败。</li>
        :type Status: str
        :param _Result: 当验证结果为不通过时，该字段会返回原因，协助您排查问题。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Result = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class Waf(AbstractModel):
    """无

    """

    def __init__(self):
        r"""
        :param _Switch: Waf开关，取值为：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        """
        self._Switch = None
        self._PolicyId = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafConfig(AbstractModel):
    """Waf配置。

    """

    def __init__(self):
        r"""
        :param _Switch: WafConfig开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>开关仅与配置是否生效有关，即使为off（关闭），也可以正常修改配置的内容。
        :type Switch: str
        :param _Level: 上一次设置的防护级别，取值有：
<li> loose：宽松；</li>
<li> normal：正常；</li>
<li> strict：严格；</li>
<li> stricter：超严格；</li>
<li> custom：自定义。</li>
        :type Level: str
        :param _Mode: 全局WAF模式，取值有：
<li> block：阻断（全局阻断，但可对详细规则配置观察）；</li>
<li> observe：观察（无论详细规则配置什么，都为观察）。</li>
        :type Mode: str
        :param _WafRule: 托管规则详细配置。如果为null，默认使用历史配置。
        :type WafRule: :class:`tencentcloud.teo.v20220901.models.WafRule`
        :param _AiRule: AI规则引擎防护配置。如果为null，默认使用历史配置。
        :type AiRule: :class:`tencentcloud.teo.v20220901.models.AiRule`
        """
        self._Switch = None
        self._Level = None
        self._Mode = None
        self._WafRule = None
        self._AiRule = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def WafRule(self):
        return self._WafRule

    @WafRule.setter
    def WafRule(self, WafRule):
        self._WafRule = WafRule

    @property
    def AiRule(self):
        return self._AiRule

    @AiRule.setter
    def AiRule(self, AiRule):
        self._AiRule = AiRule


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Level = params.get("Level")
        self._Mode = params.get("Mode")
        if params.get("WafRule") is not None:
            self._WafRule = WafRule()
            self._WafRule._deserialize(params.get("WafRule"))
        if params.get("AiRule") is not None:
            self._AiRule = AiRule()
            self._AiRule._deserialize(params.get("AiRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafRule(AbstractModel):
    """Waf规则

    """

    def __init__(self):
        r"""
        :param _Switch: 托管规则开关，取值有：
<li> on：开启；</li>
<li> off：关闭。</li>
        :type Switch: str
        :param _BlockRuleIDs: 黑名单ID列表，将规则ID加入本参数列表中代表该ID关闭，即该规则ID不再生效。
        :type BlockRuleIDs: list of int
        :param _ObserveRuleIDs: 观察模式ID列表，将规则ID加入本参数列表中代表该ID使用观察模式生效，即该规则ID进入观察模式。
        :type ObserveRuleIDs: list of int
        """
        self._Switch = None
        self._BlockRuleIDs = None
        self._ObserveRuleIDs = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BlockRuleIDs(self):
        return self._BlockRuleIDs

    @BlockRuleIDs.setter
    def BlockRuleIDs(self, BlockRuleIDs):
        self._BlockRuleIDs = BlockRuleIDs

    @property
    def ObserveRuleIDs(self):
        return self._ObserveRuleIDs

    @ObserveRuleIDs.setter
    def ObserveRuleIDs(self, ObserveRuleIDs):
        self._ObserveRuleIDs = ObserveRuleIDs


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._BlockRuleIDs = params.get("BlockRuleIDs")
        self._ObserveRuleIDs = params.get("ObserveRuleIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket配置

    """

    def __init__(self):
        r"""
        :param _Switch: WebSocket 超时时间配置开关，取值有：
<li>on：使用Timeout作为WebSocket超时时间；</li>
<li>off：平台仍支持WebSocket连接，此时使用系统默认的15秒为超时时间。</li>
        :type Switch: str
        :param _Timeout: 超时时间，单位为秒，最大超时时间120秒。
        :type Timeout: int
        """
        self._Switch = None
        self._Timeout = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    """站点信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 站点 ID。
        :type ZoneId: str
        :param _ZoneName: 站点名称。
        :type ZoneName: str
        :param _OriginalNameServers: 站点当前使用的 NS 列表。
        :type OriginalNameServers: list of str
        :param _NameServers: 腾讯云分配的 NS 列表。
        :type NameServers: list of str
        :param _Status: 站点状态，取值有：
<li> active：NS 已切换； </li>
<li> pending：NS 未切换；</li>
<li> moved：NS 已切走；</li>
<li> deactivated：被封禁。 </li>
<li> initializing：待绑定套餐。 </li>
        :type Status: str
        :param _Type: 站点接入方式，取值有：
<li> full：NS 接入；</li>
<li> partial：CNAME 接入；</li>
<li> noDomainAccess：无域名接入；</li>
        :type Type: str
        :param _Paused: 站点是否关闭。
        :type Paused: bool
        :param _CnameSpeedUp: 是否开启 CNAME 加速，取值有：
<li> enabled：开启；</li>
<li> disabled：关闭。</li>
        :type CnameSpeedUp: str
        :param _CnameStatus: CNAME 接入状态，取值有：
<li> finished：站点已验证；</li>
<li> pending：站点验证中。</li>
        :type CnameStatus: str
        :param _Tags: 资源标签列表。
        :type Tags: list of Tag
        :param _Resources: 计费资源列表。
        :type Resources: list of Resource
        :param _CreatedOn: 站点创建时间。
        :type CreatedOn: str
        :param _ModifiedOn: 站点修改时间。
        :type ModifiedOn: str
        :param _Area: 站点接入地域，取值有：
<li> global：全球；</li>
<li> mainland：中国大陆；</li>
<li> overseas：境外区域。</li>
        :type Area: str
        :param _VanityNameServers: 用户自定义 NS 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServers: :class:`tencentcloud.teo.v20220901.models.VanityNameServers`
        :param _VanityNameServersIps: 用户自定义 NS IP 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VanityNameServersIps: list of VanityNameServersIps
        :param _ActiveStatus: 展示状态，取值有：
<li> active：已启用；</li>
<li> inactive：未生效；</li>
<li> paused：已停用。</li>
        :type ActiveStatus: str
        :param _AliasZoneName: 站点别名。数字、英文、-和_组合，限制20个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasZoneName: str
        :param _IsFake: 是否伪站点，取值有：
<li> 0：非伪站点；</li>
<li> 1：伪站点。</li>
        :type IsFake: int
        :param _LockStatus: 锁定状态，取值有：<li> enable：正常，允许进行修改操作；</li><li> disable：锁定中，不允许进行修改操作；</li><li> plan_migrate：套餐迁移中，不允许进行修改操作。</li>
        :type LockStatus: str
        :param _OwnershipVerification: 归属权验证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnershipVerification: :class:`tencentcloud.teo.v20220901.models.OwnershipVerification`
        """
        self._ZoneId = None
        self._ZoneName = None
        self._OriginalNameServers = None
        self._NameServers = None
        self._Status = None
        self._Type = None
        self._Paused = None
        self._CnameSpeedUp = None
        self._CnameStatus = None
        self._Tags = None
        self._Resources = None
        self._CreatedOn = None
        self._ModifiedOn = None
        self._Area = None
        self._VanityNameServers = None
        self._VanityNameServersIps = None
        self._ActiveStatus = None
        self._AliasZoneName = None
        self._IsFake = None
        self._LockStatus = None
        self._OwnershipVerification = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def OriginalNameServers(self):
        return self._OriginalNameServers

    @OriginalNameServers.setter
    def OriginalNameServers(self, OriginalNameServers):
        self._OriginalNameServers = OriginalNameServers

    @property
    def NameServers(self):
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Paused(self):
        return self._Paused

    @Paused.setter
    def Paused(self, Paused):
        self._Paused = Paused

    @property
    def CnameSpeedUp(self):
        return self._CnameSpeedUp

    @CnameSpeedUp.setter
    def CnameSpeedUp(self, CnameSpeedUp):
        self._CnameSpeedUp = CnameSpeedUp

    @property
    def CnameStatus(self):
        return self._CnameStatus

    @CnameStatus.setter
    def CnameStatus(self, CnameStatus):
        self._CnameStatus = CnameStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def ModifiedOn(self):
        return self._ModifiedOn

    @ModifiedOn.setter
    def ModifiedOn(self, ModifiedOn):
        self._ModifiedOn = ModifiedOn

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VanityNameServers(self):
        return self._VanityNameServers

    @VanityNameServers.setter
    def VanityNameServers(self, VanityNameServers):
        self._VanityNameServers = VanityNameServers

    @property
    def VanityNameServersIps(self):
        return self._VanityNameServersIps

    @VanityNameServersIps.setter
    def VanityNameServersIps(self, VanityNameServersIps):
        self._VanityNameServersIps = VanityNameServersIps

    @property
    def ActiveStatus(self):
        return self._ActiveStatus

    @ActiveStatus.setter
    def ActiveStatus(self, ActiveStatus):
        self._ActiveStatus = ActiveStatus

    @property
    def AliasZoneName(self):
        return self._AliasZoneName

    @AliasZoneName.setter
    def AliasZoneName(self, AliasZoneName):
        self._AliasZoneName = AliasZoneName

    @property
    def IsFake(self):
        return self._IsFake

    @IsFake.setter
    def IsFake(self, IsFake):
        self._IsFake = IsFake

    @property
    def LockStatus(self):
        return self._LockStatus

    @LockStatus.setter
    def LockStatus(self, LockStatus):
        self._LockStatus = LockStatus

    @property
    def OwnershipVerification(self):
        return self._OwnershipVerification

    @OwnershipVerification.setter
    def OwnershipVerification(self, OwnershipVerification):
        self._OwnershipVerification = OwnershipVerification


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._OriginalNameServers = params.get("OriginalNameServers")
        self._NameServers = params.get("NameServers")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Paused = params.get("Paused")
        self._CnameSpeedUp = params.get("CnameSpeedUp")
        self._CnameStatus = params.get("CnameStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self._Resources.append(obj)
        self._CreatedOn = params.get("CreatedOn")
        self._ModifiedOn = params.get("ModifiedOn")
        self._Area = params.get("Area")
        if params.get("VanityNameServers") is not None:
            self._VanityNameServers = VanityNameServers()
            self._VanityNameServers._deserialize(params.get("VanityNameServers"))
        if params.get("VanityNameServersIps") is not None:
            self._VanityNameServersIps = []
            for item in params.get("VanityNameServersIps"):
                obj = VanityNameServersIps()
                obj._deserialize(item)
                self._VanityNameServersIps.append(obj)
        self._ActiveStatus = params.get("ActiveStatus")
        self._AliasZoneName = params.get("AliasZoneName")
        self._IsFake = params.get("IsFake")
        self._LockStatus = params.get("LockStatus")
        if params.get("OwnershipVerification") is not None:
            self._OwnershipVerification = OwnershipVerification()
            self._OwnershipVerification._deserialize(params.get("OwnershipVerification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneSetting(AbstractModel):
    """站点配置。

    """

    def __init__(self):
        r"""
        :param _ZoneName: 站点名称。
        :type ZoneName: str
        :param _Area: 站点加速区域信息，取值有：
<li> mainland：中国境内加速；</li>
<li> overseas：中国境外加速。</li>
        :type Area: str
        :param _CacheKey: 节点缓存键配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.teo.v20220901.models.CacheKey`
        :param _Quic: Quic访问配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Quic: :class:`tencentcloud.teo.v20220901.models.Quic`
        :param _PostMaxSize: POST请求传输配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostMaxSize: :class:`tencentcloud.teo.v20220901.models.PostMaxSize`
        :param _Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.teo.v20220901.models.Compression`
        :param _UpstreamHttp2: Http2回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHttp2: :class:`tencentcloud.teo.v20220901.models.UpstreamHttp2`
        :param _ForceRedirect: 访问协议强制Https跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.teo.v20220901.models.ForceRedirect`
        :param _CacheConfig: 缓存过期时间配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheConfig: :class:`tencentcloud.teo.v20220901.models.CacheConfig`
        :param _Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.teo.v20220901.models.Origin`
        :param _SmartRouting: 智能加速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartRouting: :class:`tencentcloud.teo.v20220901.models.SmartRouting`
        :param _MaxAge: 浏览器缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.teo.v20220901.models.MaxAge`
        :param _OfflineCache: 离线缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineCache: :class:`tencentcloud.teo.v20220901.models.OfflineCache`
        :param _WebSocket: WebSocket配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSocket: :class:`tencentcloud.teo.v20220901.models.WebSocket`
        :param _ClientIpHeader: 客户端IP回源请求头配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpHeader: :class:`tencentcloud.teo.v20220901.models.ClientIpHeader`
        :param _CachePrefresh: 缓存预刷新配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CachePrefresh: :class:`tencentcloud.teo.v20220901.models.CachePrefresh`
        :param _Ipv6: Ipv6访问配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.teo.v20220901.models.Ipv6`
        :param _Https: Https 加速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.teo.v20220901.models.Https`
        :param _ClientIpCountry: 回源时是否携带客户端IP所属地域信息的配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIpCountry: :class:`tencentcloud.teo.v20220901.models.ClientIpCountry`
        :param _Grpc: Grpc协议支持配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Grpc: :class:`tencentcloud.teo.v20220901.models.Grpc`
        :param _ImageOptimize: 图片优化相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageOptimize: :class:`tencentcloud.teo.v20220901.models.ImageOptimize`
        :param _AccelerateMainland: 中国大陆加速优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccelerateMainland: :class:`tencentcloud.teo.v20220901.models.AccelerateMainland`
        :param _StandardDebug: 标准 Debug 配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type StandardDebug: :class:`tencentcloud.teo.v20220901.models.StandardDebug`
        """
        self._ZoneName = None
        self._Area = None
        self._CacheKey = None
        self._Quic = None
        self._PostMaxSize = None
        self._Compression = None
        self._UpstreamHttp2 = None
        self._ForceRedirect = None
        self._CacheConfig = None
        self._Origin = None
        self._SmartRouting = None
        self._MaxAge = None
        self._OfflineCache = None
        self._WebSocket = None
        self._ClientIpHeader = None
        self._CachePrefresh = None
        self._Ipv6 = None
        self._Https = None
        self._ClientIpCountry = None
        self._Grpc = None
        self._ImageOptimize = None
        self._AccelerateMainland = None
        self._StandardDebug = None

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def PostMaxSize(self):
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def UpstreamHttp2(self):
        return self._UpstreamHttp2

    @UpstreamHttp2.setter
    def UpstreamHttp2(self, UpstreamHttp2):
        self._UpstreamHttp2 = UpstreamHttp2

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def SmartRouting(self):
        return self._SmartRouting

    @SmartRouting.setter
    def SmartRouting(self, SmartRouting):
        self._SmartRouting = SmartRouting

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def OfflineCache(self):
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def ClientIpHeader(self):
        return self._ClientIpHeader

    @ClientIpHeader.setter
    def ClientIpHeader(self, ClientIpHeader):
        self._ClientIpHeader = ClientIpHeader

    @property
    def CachePrefresh(self):
        return self._CachePrefresh

    @CachePrefresh.setter
    def CachePrefresh(self, CachePrefresh):
        self._CachePrefresh = CachePrefresh

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def ClientIpCountry(self):
        return self._ClientIpCountry

    @ClientIpCountry.setter
    def ClientIpCountry(self, ClientIpCountry):
        self._ClientIpCountry = ClientIpCountry

    @property
    def Grpc(self):
        return self._Grpc

    @Grpc.setter
    def Grpc(self, Grpc):
        self._Grpc = Grpc

    @property
    def ImageOptimize(self):
        return self._ImageOptimize

    @ImageOptimize.setter
    def ImageOptimize(self, ImageOptimize):
        self._ImageOptimize = ImageOptimize

    @property
    def AccelerateMainland(self):
        return self._AccelerateMainland

    @AccelerateMainland.setter
    def AccelerateMainland(self, AccelerateMainland):
        self._AccelerateMainland = AccelerateMainland

    @property
    def StandardDebug(self):
        return self._StandardDebug

    @StandardDebug.setter
    def StandardDebug(self, StandardDebug):
        self._StandardDebug = StandardDebug


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._Area = params.get("Area")
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostMaxSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("UpstreamHttp2") is not None:
            self._UpstreamHttp2 = UpstreamHttp2()
            self._UpstreamHttp2._deserialize(params.get("UpstreamHttp2"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("SmartRouting") is not None:
            self._SmartRouting = SmartRouting()
            self._SmartRouting._deserialize(params.get("SmartRouting"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("ClientIpHeader") is not None:
            self._ClientIpHeader = ClientIpHeader()
            self._ClientIpHeader._deserialize(params.get("ClientIpHeader"))
        if params.get("CachePrefresh") is not None:
            self._CachePrefresh = CachePrefresh()
            self._CachePrefresh._deserialize(params.get("CachePrefresh"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("ClientIpCountry") is not None:
            self._ClientIpCountry = ClientIpCountry()
            self._ClientIpCountry._deserialize(params.get("ClientIpCountry"))
        if params.get("Grpc") is not None:
            self._Grpc = Grpc()
            self._Grpc._deserialize(params.get("Grpc"))
        if params.get("ImageOptimize") is not None:
            self._ImageOptimize = ImageOptimize()
            self._ImageOptimize._deserialize(params.get("ImageOptimize"))
        if params.get("AccelerateMainland") is not None:
            self._AccelerateMainland = AccelerateMainland()
            self._AccelerateMainland._deserialize(params.get("AccelerateMainland"))
        if params.get("StandardDebug") is not None:
            self._StandardDebug = StandardDebug()
            self._StandardDebug._deserialize(params.get("StandardDebug"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        