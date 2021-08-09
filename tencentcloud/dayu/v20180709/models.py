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


class BaradData(AbstractModel):
    """巴拉多返回的数据

    """

    def __init__(self):
        """
        :param MetricName: 指标名（connum表示TCP活跃连接数；
new_conn表示新建TCP连接数；
inactive_conn表示非活跃连接数;
intraffic表示入流量；
outtraffic表示出流量；
alltraffic表示出流量和入流量之和；
inpkg表示入包速率；
outpkg表示出包速率；）\n        :type MetricName: str\n        :param Data: 值数组\n        :type Data: list of float\n        :param Count: 值数组的大小\n        :type Count: int\n        """
        self.MetricName = None
        self.Data = None
        self.Count = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundIpInfo(AbstractModel):
    """高防包绑定IP对象

    """

    def __init__(self):
        """
        :param Ip: IP地址\n        :type Ip: str\n        :param BizType: 绑定的产品分类，取值[public（CVM、CLB产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]\n        :type BizType: str\n        :param DeviceType: 产品分类下的子类型，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]\n        :type DeviceType: str\n        :param InstanceId: IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*); 如果绑定的是托管IP没有对应的资源实例ID，请填写"none";\n        :type InstanceId: str\n        :param IspCode: 运营商，0：电信；1：联通；2：移动；5：BGP\n        :type IspCode: int\n        """
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IspCode = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IspCode = params.get("IspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCAlarmThreshold(AbstractModel):
    """CC告警阈值

    """

    def __init__(self):
        """
        :param AlarmThreshold: CC告警阈值\n        :type AlarmThreshold: int\n        """
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCEventRecord(AbstractModel):
    """CC攻击事件记录

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Vip: 资源的IP\n        :type Vip: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        :param ReqQps: 总请求QPS峰值\n        :type ReqQps: int\n        :param DropQps: 攻击QPS峰值\n        :type DropQps: int\n        :param AttackStatus: 攻击状态，取值[0（攻击中）, 1（攻击结束）]\n        :type AttackStatus: int\n        :param ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceName: str\n        :param DomainList: 域名列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainList: str\n        :param UriList: uri列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UriList: str\n        :param AttackipList: 攻击源列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttackipList: str\n        """
        self.Business = None
        self.Id = None
        self.Vip = None
        self.StartTime = None
        self.EndTime = None
        self.ReqQps = None
        self.DropQps = None
        self.AttackStatus = None
        self.ResourceName = None
        self.DomainList = None
        self.UriList = None
        self.AttackipList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Vip = params.get("Vip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReqQps = params.get("ReqQps")
        self.DropQps = params.get("DropQps")
        self.AttackStatus = params.get("AttackStatus")
        self.ResourceName = params.get("ResourceName")
        self.DomainList = params.get("DomainList")
        self.UriList = params.get("UriList")
        self.AttackipList = params.get("AttackipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCFrequencyRule(AbstractModel):
    """CC的访问频率控制规则

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: CC的访问频率控制规则ID\n        :type CCFrequencyRuleId: str\n        :param Uri: URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；\n        :type Uri: str\n        :param UserAgent: User-Agent字符串，长度不超过80\n        :type UserAgent: str\n        :param Cookie: Cookie字符串，长度不超过40\n        :type Cookie: str\n        :param Mode: 匹配规则，取值["include"(前缀匹配)，"equal"(完全匹配)]\n        :type Mode: str\n        :param Period: 统计周期，单位秒，取值[10, 30, 60]\n        :type Period: int\n        :param ReqNumber: 访问次数，取值[1-10000]\n        :type ReqNumber: int\n        :param Act: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]\n        :type Act: str\n        :param ExeDuration: 执行时间，单位秒，取值[1-900]\n        :type ExeDuration: int\n        """
        self.CCFrequencyRuleId = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None


    def _deserialize(self, params):
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPolicy(AbstractModel):
    """cc自定义规则

    """

    def __init__(self):
        """
        :param Name: 策略名称\n        :type Name: str\n        :param Smode: 匹配模式，取值[matching(匹配模式), speedlimit(限速模式)]\n        :type Smode: str\n        :param SetId: 策略id\n        :type SetId: str\n        :param Frequency: 每分钟限制的次数\n        :type Frequency: int\n        :param ExeMode: 执行策略模式，拦截或者验证码，取值[alg（验证码）, drop（拦截）]\n        :type ExeMode: str\n        :param Switch: 生效开关\n        :type Switch: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param RuleList: 规则列表\n        :type RuleList: list of CCRule\n        :param IpList: IP列表，如果不填时，请传空数组但不能为null；\n        :type IpList: list of str\n        :param Protocol: cc防护类型，取值[http，https]\n        :type Protocol: str\n        :param RuleId: 可选字段，表示HTTPS的CC防护域名对应的转发规则ID;\n        :type RuleId: str\n        :param Domain: HTTPS的CC防护域名\n        :type Domain: str\n        """
        self.Name = None
        self.Smode = None
        self.SetId = None
        self.Frequency = None
        self.ExeMode = None
        self.Switch = None
        self.CreateTime = None
        self.RuleList = None
        self.IpList = None
        self.Protocol = None
        self.RuleId = None
        self.Domain = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Smode = params.get("Smode")
        self.SetId = params.get("SetId")
        self.Frequency = params.get("Frequency")
        self.ExeMode = params.get("ExeMode")
        self.Switch = params.get("Switch")
        self.CreateTime = params.get("CreateTime")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = CCRule()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.IpList = params.get("IpList")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRule(AbstractModel):
    """cc自定义策略配置的规则

    """

    def __init__(self):
        """
        :param Skey: 规则的key, 可以为host、cgi、ua、referer\n        :type Skey: str\n        :param Operator: 规则的条件，可以为include、not_include、equal\n        :type Operator: str\n        :param Value: 规则的值，长度小于31字节\n        :type Value: str\n        """
        self.Skey = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRuleConfig(AbstractModel):
    """7层CC自定义规则

    """

    def __init__(self):
        """
        :param Period: 统计周期，单位秒，取值[10, 30, 60]\n        :type Period: int\n        :param ReqNumber: 访问次数，取值[1-10000]\n        :type ReqNumber: int\n        :param Action: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]\n        :type Action: str\n        :param ExeDuration: 执行时间，单位秒，取值[1-900]\n        :type ExeDuration: int\n        """
        self.Period = None
        self.ReqNumber = None
        self.Action = None
        self.ExeDuration = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Action = params.get("Action")
        self.ExeDuration = params.get("ExeDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdRequest(AbstractModel):
    """CreateBasicDDoSAlarmThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（basic表示DDoS基础防护）\n        :type Business: str\n        :param Method: =get表示读取告警阈值；=set表示设置告警阈值；\n        :type Method: str\n        :param AlarmType: 可选，告警阈值类型，1-入流量，2-清洗流量；当Method为set时必须填写；\n        :type AlarmType: int\n        :param AlarmThreshold: 可选，告警阈值，当Method为set时必须填写；当设置阈值为0时表示清除告警阈值配置；\n        :type AlarmThreshold: int\n        """
        self.Business = None
        self.Method = None
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdResponse(AbstractModel):
    """CreateBasicDDoSAlarmThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param AlarmThreshold: 当存在告警阈值配置时，返回告警阈值大于0，当不存在告警配置时，返回告警阈值为0；\n        :type AlarmThreshold: int\n        :param AlarmType: 告警阈值类型，1-入流量，2-清洗流量；当AlarmThreshold大于0时有效；\n        :type AlarmType: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AlarmThreshold = None
        self.AlarmType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.AlarmType = params.get("AlarmType")
        self.RequestId = params.get("RequestId")


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param BoundDevList: 绑定到资源实例的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要绑定的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；\n        :type BoundDevList: list of BoundIpInfo\n        :param UnBoundDevList: 与资源实例解绑的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要解绑的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；\n        :type UnBoundDevList: list of BoundIpInfo\n        :param CopyPolicy: 已弃用，不填\n        :type CopyPolicy: str\n        """
        self.Business = None
        self.Id = None
        self.BoundDevList = None
        self.UnBoundDevList = None
        self.CopyPolicy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("BoundDevList") is not None:
            self.BoundDevList = []
            for item in params.get("BoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.BoundDevList.append(obj)
        if params.get("UnBoundDevList") is not None:
            self.UnBoundDevList = []
            for item in params.get("UnBoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.UnBoundDevList.append(obj)
        self.CopyPolicy = params.get("CopyPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateCCFrequencyRulesRequest(AbstractModel):
    """CreateCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleId: 7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）\n        :type RuleId: str\n        :param Mode: 匹配规则，取值["include"(前缀匹配)，"equal"(完全匹配)]\n        :type Mode: str\n        :param Period: 统计周期，单位秒，取值[10, 30, 60]\n        :type Period: int\n        :param ReqNumber: 访问次数，取值[1-10000]\n        :type ReqNumber: int\n        :param Act: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]\n        :type Act: str\n        :param ExeDuration: 执行时间，单位秒，取值[1-900]\n        :type ExeDuration: int\n        :param Uri: URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；\n        :type Uri: str\n        :param UserAgent: User-Agent字符串，长度不超过80\n        :type UserAgent: str\n        :param Cookie: Cookie字符串，长度不超过40\n        :type Cookie: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCFrequencyRulesResponse(AbstractModel):
    """CreateCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: CC防护的访问频率控制规则ID\n        :type CCFrequencyRuleId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CCFrequencyRuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.RequestId = params.get("RequestId")


class CreateCCSelfDefinePolicyRequest(AbstractModel):
    """CreateCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Policy: CC策略描述\n        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`\n        """
        self.Business = None
        self.Id = None
        self.Policy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Policy") is not None:
            self.Policy = CCPolicy()
            self.Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCSelfDefinePolicyResponse(AbstractModel):
    """CreateCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateDDoSPolicyCaseRequest(AbstractModel):
    """CreateDDoSPolicyCase请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param CaseName: 策略场景名，字符串长度小于64\n        :type CaseName: str\n        :param PlatformTypes: 开发平台，取值[PC（PC客户端）， MOBILE（移动端）， TV（电视端）， SERVER（主机）]\n        :type PlatformTypes: list of str\n        :param AppType: 细分品类，取值[WEB（网站）， GAME（游戏）， APP（应用）， OTHER（其他）]\n        :type AppType: str\n        :param AppProtocols: 应用协议，取值[tcp（TCP协议），udp（UDP协议），icmp（ICMP协议），all（其他协议）]\n        :type AppProtocols: list of str\n        :param TcpSportStart: TCP业务起始端口，取值(0, 65535]\n        :type TcpSportStart: str\n        :param TcpSportEnd: TCP业务结束端口，取值(0, 65535]，必须大于等于TCP业务起始端口\n        :type TcpSportEnd: str\n        :param UdpSportStart: UDP业务起始端口，取值范围(0, 65535]\n        :type UdpSportStart: str\n        :param UdpSportEnd: UDP业务结束端口，取值范围(0, 65535)，必须大于等于UDP业务起始端口\n        :type UdpSportEnd: str\n        :param HasAbroad: 是否有海外客户，取值[no（没有）, yes（有）]\n        :type HasAbroad: str\n        :param HasInitiateTcp: 是否会主动对外发起TCP请求，取值[no（不会）, yes（会）]\n        :type HasInitiateTcp: str\n        :param HasInitiateUdp: 是否会主动对外发起UDP业务请求，取值[no（不会）, yes（会）]\n        :type HasInitiateUdp: str\n        :param PeerTcpPort: 主动发起TCP请求的端口，取值范围(0, 65535]\n        :type PeerTcpPort: str\n        :param PeerUdpPort: 主动发起UDP请求的端口，取值范围(0, 65535]\n        :type PeerUdpPort: str\n        :param TcpFootprint: TCP载荷的固定特征码，字符串长度小于512\n        :type TcpFootprint: str\n        :param UdpFootprint: UDP载荷的固定特征码，字符串长度小于512\n        :type UdpFootprint: str\n        :param WebApiUrl: Web业务的API的URL\n        :type WebApiUrl: list of str\n        :param MinTcpPackageLen: TCP业务报文长度最小值，取值范围(0, 1500)\n        :type MinTcpPackageLen: str\n        :param MaxTcpPackageLen: TCP业务报文长度最大值，取值范围(0, 1500)，必须大于等于TCP业务报文长度最小值\n        :type MaxTcpPackageLen: str\n        :param MinUdpPackageLen: UDP业务报文长度最小值，取值范围(0, 1500)\n        :type MinUdpPackageLen: str\n        :param MaxUdpPackageLen: UDP业务报文长度最大值，取值范围(0, 1500)，必须大于等于UDP业务报文长度最小值\n        :type MaxUdpPackageLen: str\n        :param HasVPN: 是否有VPN业务，取值[no（没有）, yes（有）]\n        :type HasVPN: str\n        :param TcpPortList: TCP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000\n        :type TcpPortList: str\n        :param UdpPortList: UDP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000\n        :type UdpPortList: str\n        """
        self.Business = None
        self.CaseName = None
        self.PlatformTypes = None
        self.AppType = None
        self.AppProtocols = None
        self.TcpSportStart = None
        self.TcpSportEnd = None
        self.UdpSportStart = None
        self.UdpSportEnd = None
        self.HasAbroad = None
        self.HasInitiateTcp = None
        self.HasInitiateUdp = None
        self.PeerTcpPort = None
        self.PeerUdpPort = None
        self.TcpFootprint = None
        self.UdpFootprint = None
        self.WebApiUrl = None
        self.MinTcpPackageLen = None
        self.MaxTcpPackageLen = None
        self.MinUdpPackageLen = None
        self.MaxUdpPackageLen = None
        self.HasVPN = None
        self.TcpPortList = None
        self.UdpPortList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CaseName = params.get("CaseName")
        self.PlatformTypes = params.get("PlatformTypes")
        self.AppType = params.get("AppType")
        self.AppProtocols = params.get("AppProtocols")
        self.TcpSportStart = params.get("TcpSportStart")
        self.TcpSportEnd = params.get("TcpSportEnd")
        self.UdpSportStart = params.get("UdpSportStart")
        self.UdpSportEnd = params.get("UdpSportEnd")
        self.HasAbroad = params.get("HasAbroad")
        self.HasInitiateTcp = params.get("HasInitiateTcp")
        self.HasInitiateUdp = params.get("HasInitiateUdp")
        self.PeerTcpPort = params.get("PeerTcpPort")
        self.PeerUdpPort = params.get("PeerUdpPort")
        self.TcpFootprint = params.get("TcpFootprint")
        self.UdpFootprint = params.get("UdpFootprint")
        self.WebApiUrl = params.get("WebApiUrl")
        self.MinTcpPackageLen = params.get("MinTcpPackageLen")
        self.MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self.MinUdpPackageLen = params.get("MinUdpPackageLen")
        self.MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self.HasVPN = params.get("HasVPN")
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyCaseResponse(AbstractModel):
    """CreateDDoSPolicyCase返回参数结构体

    """

    def __init__(self):
        """
        :param SceneId: 策略场景ID\n        :type SceneId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SceneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SceneId = params.get("SceneId")
        self.RequestId = params.get("RequestId")


class CreateDDoSPolicyRequest(AbstractModel):
    """CreateDDoSPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param DropOptions: 协议禁用，必须填写且数组长度必须为1\n        :type DropOptions: list of DDoSPolicyDropOption\n        :param Name: 策略名称\n        :type Name: str\n        :param PortLimits: 端口禁用，当没有禁用端口时填空数组\n        :type PortLimits: list of DDoSPolicyPortLimit\n        :param IpAllowDenys: 请求源IP黑白名单，当没有IP黑白名单时填空数组\n        :type IpAllowDenys: list of IpBlackWhite\n        :param PacketFilters: 报文过滤，当没有报文过滤时填空数组\n        :type PacketFilters: list of DDoSPolicyPacketFilter\n        :param WaterPrint: 水印策略参数，当没有启用水印功能时填空数组，最多只能传一条水印策略（即数组大小不超过1）\n        :type WaterPrint: list of WaterPrintPolicy\n        """
        self.Business = None
        self.DropOptions = None
        self.Name = None
        self.PortLimits = None
        self.IpAllowDenys = None
        self.PacketFilters = None
        self.WaterPrint = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        if params.get("DropOptions") is not None:
            self.DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self.DropOptions.append(obj)
        self.Name = params.get("Name")
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self.IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyResponse(AbstractModel):
    """CreateDDoSPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID\n        :type PolicyId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateInstanceNameRequest(AbstractModel):
    """CreateInstanceName请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Name: 资源实例名称，长度不超过32个字符\n        :type Name: str\n        """
        self.Business = None
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNameResponse(AbstractModel):
    """CreateInstanceName返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL4HealthConfigRequest(AbstractModel):
    """CreateL4HealthConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param HealthConfig: 四层健康检查配置数组\n        :type HealthConfig: list of L4HealthConfig\n        """
        self.Business = None
        self.Id = None
        self.HealthConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4HealthConfigResponse(AbstractModel):
    """CreateL4HealthConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL4RulesRequest(AbstractModel):
    """CreateL4Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Rules: 规则列表\n        :type Rules: list of L4RuleEntry\n        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4RulesResponse(AbstractModel):
    """CreateL4Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7CCRuleRequest(AbstractModel):
    """CreateL7CCRule请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Method: 操作码，取值[query(表示查询)，add(表示添加)，del(表示删除)]\n        :type Method: str\n        :param RuleId: 7层转发规则ID，例如：rule-0000001\n        :type RuleId: str\n        :param RuleConfig: 7层CC自定义规则参数，当操作码为query时，可以不用填写；当操作码为add或del时，必须填写，且数组长度只能为1；\n        :type RuleConfig: list of CCRuleConfig\n        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.RuleId = None
        self.RuleConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.RuleId = params.get("RuleId")
        if params.get("RuleConfig") is not None:
            self.RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self.RuleConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7CCRuleResponse(AbstractModel):
    """CreateL7CCRule返回参数结构体

    """

    def __init__(self):
        """
        :param RuleConfig: 7层CC自定义规则参数，当没有开启CC自定义规则时，返回空数组\n        :type RuleConfig: list of CCRuleConfig\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RuleConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleConfig") is not None:
            self.RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self.RuleConfig.append(obj)
        self.RequestId = params.get("RequestId")


class CreateL7HealthConfigRequest(AbstractModel):
    """CreateL7HealthConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param HealthConfig: 七层健康检查配置数组\n        :type HealthConfig: list of L7HealthConfig\n        """
        self.Business = None
        self.Id = None
        self.HealthConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7HealthConfigResponse(AbstractModel):
    """CreateL7HealthConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RuleCertRequest(AbstractModel):
    """CreateL7RuleCert请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源实例ID，例如高防IP实例的ID，高防IP专业版实例的ID\n        :type Id: str\n        :param RuleId: 规则ID\n        :type RuleId: str\n        :param CertType: 证书类型，当为协议为HTTPS协议时必须填，取值[2(腾讯云托管证书)]\n        :type CertType: int\n        :param SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID\n        :type SSLId: str\n        :param Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)\n        :type Cert: str\n        :param PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)\n        :type PrivateKey: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RuleCertResponse(AbstractModel):
    """CreateL7RuleCert返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RulesRequest(AbstractModel):
    """CreateL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Rules: 规则列表\n        :type Rules: list of L7RuleEntry\n        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RulesUploadRequest(AbstractModel):
    """CreateL7RulesUpload请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Rules: 规则列表\n        :type Rules: list of L7RuleEntry\n        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesUploadResponse(AbstractModel):
    """CreateL7RulesUpload返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateNetReturnRequest(AbstractModel):
    """CreateNetReturn请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetReturnResponse(AbstractModel):
    """CreateNetReturn返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNewL4RulesRequest(AbstractModel):
    """CreateNewL4Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 高防产品代号：bgpip\n        :type Business: str\n        :param IdList: 添加规则资源列表\n        :type IdList: list of str\n        :param VipList: 添加规则IP列表\n        :type VipList: list of str\n        :param Rules: 规则列表\n        :type Rules: list of L4RuleEntry\n        """
        self.Business = None
        self.IdList = None
        self.VipList = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        self.VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL4RulesResponse(AbstractModel):
    """CreateNewL4Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateNewL7RulesRequest(AbstractModel):
    """CreateNewL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param IdList: 资源ID列表\n        :type IdList: list of str\n        :param VipList: 资源IP列表\n        :type VipList: list of str\n        :param Rules: 规则列表\n        :type Rules: list of L7RuleEntry\n        """
        self.Business = None
        self.IdList = None
        self.VipList = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        self.VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesResponse(AbstractModel):
    """CreateNewL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateNewL7RulesUploadRequest(AbstractModel):
    """CreateNewL7RulesUpload请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param IdList: 资源ID列表\n        :type IdList: list of str\n        :param VipList: 资源IP列表\n        :type VipList: list of str\n        :param Rules: 规则列表\n        :type Rules: list of L7RuleEntry\n        """
        self.Business = None
        self.IdList = None
        self.VipList = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        self.VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesUploadResponse(AbstractModel):
    """CreateNewL7RulesUpload返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateUnblockIpRequest(AbstractModel):
    """CreateUnblockIp请求参数结构体

    """

    def __init__(self):
        """
        :param Ip: IP\n        :type Ip: str\n        :param ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）\n        :type ActionType: str\n        """
        self.Ip = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUnblockIpResponse(AbstractModel):
    """CreateUnblockIp返回参数结构体

    """

    def __init__(self):
        """
        :param Ip: IP\n        :type Ip: str\n        :param ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）\n        :type ActionType: str\n        :param UnblockTime: 解封时间（预计解封时间）\n        :type UnblockTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Ip = None
        self.ActionType = None
        self.UnblockTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ActionType = params.get("ActionType")
        self.UnblockTime = params.get("UnblockTime")
        self.RequestId = params.get("RequestId")


class DDoSAlarmThreshold(AbstractModel):
    """DDoS告警阈值

    """

    def __init__(self):
        """
        :param AlarmType: 告警阈值类型，1-入流量，2-清洗流量\n        :type AlarmType: int\n        :param AlarmThreshold: 告警阈值，大于0（目前排定的值）\n        :type AlarmThreshold: int\n        """
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackSourceRecord(AbstractModel):
    """攻击源信息

    """

    def __init__(self):
        """
        :param SrcIp: 攻击源ip\n        :type SrcIp: str\n        :param Province: 省份（国内有效，不包含港澳台）\n        :type Province: str\n        :param Nation: 国家\n        :type Nation: str\n        :param PacketSum: 累计攻击包量\n        :type PacketSum: int\n        :param PacketLen: 累计攻击流量\n        :type PacketLen: int\n        """
        self.SrcIp = None
        self.Province = None
        self.Nation = None
        self.PacketSum = None
        self.PacketLen = None


    def _deserialize(self, params):
        self.SrcIp = params.get("SrcIp")
        self.Province = params.get("Province")
        self.Nation = params.get("Nation")
        self.PacketSum = params.get("PacketSum")
        self.PacketLen = params.get("PacketLen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSEventRecord(AbstractModel):
    """DDoS攻击事件记录

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Vip: 资源的IP\n        :type Vip: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        :param Mbps: 攻击最大带宽\n        :type Mbps: int\n        :param Pps: 攻击最大包速率\n        :type Pps: int\n        :param AttackType: 攻击类型\n        :type AttackType: str\n        :param BlockFlag: 是否被封堵，取值[1（是），0（否），2（无效值）]\n        :type BlockFlag: int\n        :param OverLoad: 是否超过弹性防护峰值，取值取值[yes(是)，no(否)，空字符串（未知值）]\n        :type OverLoad: str\n        :param AttackStatus: 攻击状态，取值[0（攻击中）, 1（攻击结束）]\n        :type AttackStatus: int\n        :param ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceName: str\n        :param EventId: 攻击事件Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type EventId: str\n        """
        self.Business = None
        self.Id = None
        self.Vip = None
        self.StartTime = None
        self.EndTime = None
        self.Mbps = None
        self.Pps = None
        self.AttackType = None
        self.BlockFlag = None
        self.OverLoad = None
        self.AttackStatus = None
        self.ResourceName = None
        self.EventId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Vip = params.get("Vip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.AttackType = params.get("AttackType")
        self.BlockFlag = params.get("BlockFlag")
        self.OverLoad = params.get("OverLoad")
        self.AttackStatus = params.get("AttackStatus")
        self.ResourceName = params.get("ResourceName")
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyDropOption(AbstractModel):
    """DDoS高级策略的禁用协议选项

    """

    def __init__(self):
        """
        :param DropTcp: 禁用TCP协议，取值范围[0,1]\n        :type DropTcp: int\n        :param DropUdp: 禁用UDP协议，取值范围[0,1]\n        :type DropUdp: int\n        :param DropIcmp: 禁用ICMP协议，取值范围[0,1]\n        :type DropIcmp: int\n        :param DropOther: 禁用其他协议，取值范围[0,1]\n        :type DropOther: int\n        :param DropAbroad: 拒绝海外流量，取值范围[0,1]\n        :type DropAbroad: int\n        :param CheckSyncConn: 空连接防护，取值范围[0,1]\n        :type CheckSyncConn: int\n        :param SdNewLimit: 基于来源IP及目的IP的新建连接抑制，取值范围[0,4294967295]\n        :type SdNewLimit: int\n        :param DstNewLimit: 基于目的IP的新建连接抑制，取值范围[0,4294967295]\n        :type DstNewLimit: int\n        :param SdConnLimit: 基于来源IP及目的IP的并发连接抑制，取值范围[0,4294967295]\n        :type SdConnLimit: int\n        :param DstConnLimit: 基于目的IP的并发连接抑制，取值范围[0,4294967295]\n        :type DstConnLimit: int\n        :param BadConnThreshold: 基于连接抑制触发阈值，取值范围[0,4294967295]\n        :type BadConnThreshold: int\n        :param NullConnEnable: 异常连接检测条件，空连接防护开关，，取值范围[0,1]\n        :type NullConnEnable: int\n        :param ConnTimeout: 异常连接检测条件，连接超时，，取值范围[0,65535]\n        :type ConnTimeout: int\n        :param SynRate: 异常连接检测条件，syn占比ack百分比，，取值范围[0,100]\n        :type SynRate: int\n        :param SynLimit: 异常连接检测条件，syn阈值，取值范围[0,100]\n        :type SynLimit: int\n        :param DTcpMbpsLimit: tcp限速，取值范围[0,4294967295]\n        :type DTcpMbpsLimit: int\n        :param DUdpMbpsLimit: udp限速，取值范围[0,4294967295]\n        :type DUdpMbpsLimit: int\n        :param DIcmpMbpsLimit: icmp限速，取值范围[0,4294967295]\n        :type DIcmpMbpsLimit: int\n        :param DOtherMbpsLimit: other协议限速，取值范围[0,4294967295]\n        :type DOtherMbpsLimit: int\n        """
        self.DropTcp = None
        self.DropUdp = None
        self.DropIcmp = None
        self.DropOther = None
        self.DropAbroad = None
        self.CheckSyncConn = None
        self.SdNewLimit = None
        self.DstNewLimit = None
        self.SdConnLimit = None
        self.DstConnLimit = None
        self.BadConnThreshold = None
        self.NullConnEnable = None
        self.ConnTimeout = None
        self.SynRate = None
        self.SynLimit = None
        self.DTcpMbpsLimit = None
        self.DUdpMbpsLimit = None
        self.DIcmpMbpsLimit = None
        self.DOtherMbpsLimit = None


    def _deserialize(self, params):
        self.DropTcp = params.get("DropTcp")
        self.DropUdp = params.get("DropUdp")
        self.DropIcmp = params.get("DropIcmp")
        self.DropOther = params.get("DropOther")
        self.DropAbroad = params.get("DropAbroad")
        self.CheckSyncConn = params.get("CheckSyncConn")
        self.SdNewLimit = params.get("SdNewLimit")
        self.DstNewLimit = params.get("DstNewLimit")
        self.SdConnLimit = params.get("SdConnLimit")
        self.DstConnLimit = params.get("DstConnLimit")
        self.BadConnThreshold = params.get("BadConnThreshold")
        self.NullConnEnable = params.get("NullConnEnable")
        self.ConnTimeout = params.get("ConnTimeout")
        self.SynRate = params.get("SynRate")
        self.SynLimit = params.get("SynLimit")
        self.DTcpMbpsLimit = params.get("DTcpMbpsLimit")
        self.DUdpMbpsLimit = params.get("DUdpMbpsLimit")
        self.DIcmpMbpsLimit = params.get("DIcmpMbpsLimit")
        self.DOtherMbpsLimit = params.get("DOtherMbpsLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPacketFilter(AbstractModel):
    """DDoS高级策略的报文过滤项

    """

    def __init__(self):
        """
        :param Protocol: 协议，取值范围[tcp,udp,icmp,all]\n        :type Protocol: str\n        :param SportStart: 开始源端口，取值范围[0,65535]\n        :type SportStart: int\n        :param SportEnd: 结束源端口，取值范围[0,65535]\n        :type SportEnd: int\n        :param DportStart: 开始目的端口，取值范围[0,65535]\n        :type DportStart: int\n        :param DportEnd: 结束目的端口，取值范围[0,65535]\n        :type DportEnd: int\n        :param PktlenMin: 最小包长，取值范围[0,1500]\n        :type PktlenMin: int\n        :param PktlenMax: 最大包长，取值范围[0,1500]\n        :type PktlenMax: int\n        :param MatchBegin: 是否检测载荷，取值范围[
begin_l3(IP头)
begin_l4(TCP头)
begin_l5(载荷)
no_match(不检测)
]\n        :type MatchBegin: str\n        :param MatchType: 是否是正则表达式，取值范围[sunday(表示关键字),pcre(表示正则表达式)]\n        :type MatchType: str\n        :param Str: 关键字或正则表达式\n        :type Str: str\n        :param Depth: 检测深度，取值范围[0,1500]\n        :type Depth: int\n        :param Offset: 检测偏移量，取值范围[0,1500]\n        :type Offset: int\n        :param IsNot: 是否包括，取值范围[0(表示不包含),1(表示包含)]\n        :type IsNot: int\n        :param Action: 策略动作，取值范围[drop，drop_black，drop_rst，drop_black_rst，transmit]\n        :type Action: str\n        """
        self.Protocol = None
        self.SportStart = None
        self.SportEnd = None
        self.DportStart = None
        self.DportEnd = None
        self.PktlenMin = None
        self.PktlenMax = None
        self.MatchBegin = None
        self.MatchType = None
        self.Str = None
        self.Depth = None
        self.Offset = None
        self.IsNot = None
        self.Action = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.SportStart = params.get("SportStart")
        self.SportEnd = params.get("SportEnd")
        self.DportStart = params.get("DportStart")
        self.DportEnd = params.get("DportEnd")
        self.PktlenMin = params.get("PktlenMin")
        self.PktlenMax = params.get("PktlenMax")
        self.MatchBegin = params.get("MatchBegin")
        self.MatchType = params.get("MatchType")
        self.Str = params.get("Str")
        self.Depth = params.get("Depth")
        self.Offset = params.get("Offset")
        self.IsNot = params.get("IsNot")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPortLimit(AbstractModel):
    """DDoS高级策略的禁用端口

    """

    def __init__(self):
        """
        :param Protocol: 协议，取值范围[tcp,udp,all]\n        :type Protocol: str\n        :param DPortStart: 开始目的端口，取值范围[0,65535]\n        :type DPortStart: int\n        :param DPortEnd: 结束目的端口，取值范围[0,65535]，要求大于等于开始目的端口\n        :type DPortEnd: int\n        :param SPortStart: 开始源端口，取值范围[0,65535]
注意：此字段可能返回 null，表示取不到有效值。\n        :type SPortStart: int\n        :param SPortEnd: 结束源端口，取值范围[0,65535]，要求大于等于开始源端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type SPortEnd: int\n        :param Action: 执行动作，取值[drop(丢弃) ，transmit(转发)]
注意：此字段可能返回 null，表示取不到有效值。\n        :type Action: str\n        :param Kind: 禁用端口类型，取值[0（目的端口范围禁用）， 1（源端口范围禁用）， 2（目的和源端口范围同时禁用）]
注意：此字段可能返回 null，表示取不到有效值。\n        :type Kind: int\n        """
        self.Protocol = None
        self.DPortStart = None
        self.DPortEnd = None
        self.SPortStart = None
        self.SPortEnd = None
        self.Action = None
        self.Kind = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.DPortStart = params.get("DPortStart")
        self.DPortEnd = params.get("DPortEnd")
        self.SPortStart = params.get("SPortStart")
        self.SPortEnd = params.get("SPortEnd")
        self.Action = params.get("Action")
        self.Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosPolicy(AbstractModel):
    """DDoS高级策略

    """

    def __init__(self):
        """
        :param Resources: 策略绑定的资源\n        :type Resources: list of ResourceIp\n        :param DropOptions: 禁用协议\n        :type DropOptions: :class:`tencentcloud.dayu.v20180709.models.DDoSPolicyDropOption`\n        :param PortLimits: 禁用端口\n        :type PortLimits: list of DDoSPolicyPortLimit\n        :param PacketFilters: 报文过滤\n        :type PacketFilters: list of DDoSPolicyPacketFilter\n        :param IpBlackWhiteLists: 黑白IP名单\n        :type IpBlackWhiteLists: list of IpBlackWhite\n        :param PolicyId: 策略ID\n        :type PolicyId: str\n        :param PolicyName: 策略名称\n        :type PolicyName: str\n        :param CreateTime: 策略创建时间\n        :type CreateTime: str\n        :param WaterPrint: 水印策略参数，最多只有一个，当没有水印策略时数组为空\n        :type WaterPrint: list of WaterPrintPolicy\n        :param WaterKey: 水印密钥，最多只有2个，当没有水印策略时数组为空\n        :type WaterKey: list of WaterPrintKey\n        :param BoundResources: 策略绑定的资源实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type BoundResources: list of str\n        :param SceneId: 策略所属的策略场景
注意：此字段可能返回 null，表示取不到有效值。\n        :type SceneId: str\n        """
        self.Resources = None
        self.DropOptions = None
        self.PortLimits = None
        self.PacketFilters = None
        self.IpBlackWhiteLists = None
        self.PolicyId = None
        self.PolicyName = None
        self.CreateTime = None
        self.WaterPrint = None
        self.WaterKey = None
        self.BoundResources = None
        self.SceneId = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = ResourceIp()
                obj._deserialize(item)
                self.Resources.append(obj)
        if params.get("DropOptions") is not None:
            self.DropOptions = DDoSPolicyDropOption()
            self.DropOptions._deserialize(params.get("DropOptions"))
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("IpBlackWhiteLists") is not None:
            self.IpBlackWhiteLists = []
            for item in params.get("IpBlackWhiteLists"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpBlackWhiteLists.append(obj)
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.CreateTime = params.get("CreateTime")
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)
        if params.get("WaterKey") is not None:
            self.WaterKey = []
            for item in params.get("WaterKey"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self.WaterKey.append(obj)
        self.BoundResources = params.get("BoundResources")
        self.SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesRequest(AbstractModel):
    """DeleteCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param CCFrequencyRuleId: CC防护的访问频率控制规则ID\n        :type CCFrequencyRuleId: str\n        """
        self.Business = None
        self.CCFrequencyRuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesResponse(AbstractModel):
    """DeleteCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteCCSelfDefinePolicyRequest(AbstractModel):
    """DeleteCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param SetId: 策略ID\n        :type SetId: str\n        """
        self.Business = None
        self.Id = None
        self.SetId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCSelfDefinePolicyResponse(AbstractModel):
    """DeleteCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteDDoSPolicyCaseRequest(AbstractModel):
    """DeleteDDoSPolicyCase请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param SceneId: 策略场景ID\n        :type SceneId: str\n        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyCaseResponse(AbstractModel):
    """DeleteDDoSPolicyCase返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteDDoSPolicyRequest(AbstractModel):
    """DeleteDDoSPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param PolicyId: 策略ID\n        :type PolicyId: str\n        """
        self.Business = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyResponse(AbstractModel):
    """DeleteDDoSPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteL4RulesRequest(AbstractModel):
    """DeleteL4Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleIdList: 规则ID列表\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL4RulesResponse(AbstractModel):
    """DeleteL4Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    """DeleteL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleIdList: 规则ID列表\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteNewL4RulesRequest(AbstractModel):
    """DeleteNewL4Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Rule: 删除接口结构体\n        :type Rule: list of L4DelRule\n        """
        self.Business = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = L4DelRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNewL4RulesResponse(AbstractModel):
    """DeleteNewL4Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteNewL7RulesRequest(AbstractModel):
    """DeleteNewL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP)\n        :type Business: str\n        :param Rule: 删除规则列表\n        :type Rule: list of L4DelRule\n        """
        self.Business = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = L4DelRule()
                obj._deserialize(item)
                self.Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNewL7RulesResponse(AbstractModel):
    """DeleteNewL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DescribeActionLogRequest(AbstractModel):
    """DescribeActionLog请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Filter: 搜索值，只支持资源ID或用户UIN\n        :type Filter: str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        """
        self.StartTime = None
        self.EndTime = None
        self.Business = None
        self.Filter = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Business = params.get("Business")
        self.Filter = params.get("Filter")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionLogResponse(AbstractModel):
    """DescribeActionLog返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param Data: 记录数组\n        :type Data: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBGPIPL7RuleMaxCntRequest(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBGPIPL7RuleMaxCntResponse(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 高防IP最多可添加的7层规则数量\n        :type Count: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeBaradDataRequest(AbstractModel):
    """DescribeBaradData请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param MetricName: 指标名，取值：
connum表示TCP活跃连接数；
new_conn表示新建TCP连接数；
inactive_conn表示非活跃连接数;
intraffic表示入流量；
outtraffic表示出流量；
alltraffic表示出流量和入流量之和；
inpkg表示入包速率；
outpkg表示出包速率；\n        :type MetricName: str\n        :param Period: 统计时间粒度，单位秒（300表示5分钟；3600表示小时；86400表示天）\n        :type Period: int\n        :param StartTime: 统计开始时间，秒部分保持为0，分钟部分为5的倍数\n        :type StartTime: str\n        :param EndTime: 统计结束时间，秒部分保持为0，分钟部分为5的倍数\n        :type EndTime: str\n        :param Statistics: 统计方式，取值：
max表示最大值；
min表示最小值；
avg表示均值；\n        :type Statistics: str\n        :param ProtocolPort: 协议端口数组\n        :type ProtocolPort: list of ProtocolPort\n        :param Ip: 资源实例下的IP，只有当Business=net(高防IP专业版)时才必须填写资源的一个IP（因为高防IP专业版资源实例有多个IP，才需要指定）；\n        :type Ip: str\n        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Statistics = None
        self.ProtocolPort = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Statistics = params.get("Statistics")
        if params.get("ProtocolPort") is not None:
            self.ProtocolPort = []
            for item in params.get("ProtocolPort"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPort.append(obj)
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaradDataResponse(AbstractModel):
    """DescribeBaradData返回参数结构体

    """

    def __init__(self):
        """
        :param DataList: 返回指标的值\n        :type DataList: list of BaradData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DataList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = BaradData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBasicCCThresholdRequest(AbstractModel):
    """DescribeBasicCCThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param BasicIp: 查询的IP地址，取值如：1.1.1.1\n        :type BasicIp: str\n        :param BasicRegion: 查询IP所属地域，取值如：gz、bj、sh、hk等地域缩写\n        :type BasicRegion: str\n        :param BasicBizType: 专区类型，取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。\n        :type BasicBizType: str\n        :param BasicDeviceType: 设备类型，取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel.\n        :type BasicDeviceType: str\n        :param BasicIpInstance: 可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）\n        :type BasicIpInstance: str\n        :param BasicIspCode: 可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）\n        :type BasicIspCode: int\n        """
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicIpInstance = None
        self.BasicIspCode = None


    def _deserialize(self, params):
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicCCThresholdResponse(AbstractModel):
    """DescribeBasicCCThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param CCEnable: CC启动开关（0:关闭；1:开启）\n        :type CCEnable: int\n        :param CCThreshold: CC防护阈值\n        :type CCThreshold: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CCEnable = None
        self.CCThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.RequestId = params.get("RequestId")


class DescribeBasicDeviceThresholdRequest(AbstractModel):
    """DescribeBasicDeviceThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param BasicIp: 查询的IP地址，取值如：1.1.1.1\n        :type BasicIp: str\n        :param BasicRegion: 查询IP所属地域，取值如：gz、bj、sh、hk等地域缩写\n        :type BasicRegion: str\n        :param BasicBizType: 专区类型，取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。\n        :type BasicBizType: str\n        :param BasicDeviceType: 设备类型，取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel.\n        :type BasicDeviceType: str\n        :param BasicCheckFlag: 有效性检查，取值为1\n        :type BasicCheckFlag: int\n        :param BasicIpInstance: 可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）\n        :type BasicIpInstance: str\n        :param BasicIspCode: 可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）\n        :type BasicIspCode: int\n        """
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicCheckFlag = None
        self.BasicIpInstance = None
        self.BasicIspCode = None


    def _deserialize(self, params):
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicCheckFlag = params.get("BasicCheckFlag")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDeviceThresholdResponse(AbstractModel):
    """DescribeBasicDeviceThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param Threshold: 返回黑洞封堵值\n        :type Threshold: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Threshold = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.RequestId = params.get("RequestId")


class DescribeBizHttpStatusRequest(AbstractModel):
    """DescribeBizHttpStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Id: 资源Id\n        :type Id: str\n        :param Period: 统计周期，可取值300，1800，3600， 21600，86400，单位秒\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param Statistics: 统计方式，仅支持sum\n        :type Statistics: str\n        :param ProtoInfo: 协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效\n        :type ProtoInfo: list of ProtocolPort\n        :param Domain: 特定域名查询\n        :type Domain: str\n        """
        self.Business = None
        self.Id = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Statistics = None
        self.ProtoInfo = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Statistics = params.get("Statistics")
        if params.get("ProtoInfo") is not None:
            self.ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtoInfo.append(obj)
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizHttpStatusResponse(AbstractModel):
    """DescribeBizHttpStatus返回参数结构体

    """

    def __init__(self):
        """
        :param HttpStatusMap: 业务流量http状态码统计数据\n        :type HttpStatusMap: :class:`tencentcloud.dayu.v20180709.models.HttpStatusMap`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.HttpStatusMap = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HttpStatusMap") is not None:
            self.HttpStatusMap = HttpStatusMap()
            self.HttpStatusMap._deserialize(params.get("HttpStatusMap"))
        self.RequestId = params.get("RequestId")


class DescribeBizTrendRequest(AbstractModel):
    """DescribeBizTrend请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param Period: 统计周期，可取值300，1800，3600，21600，86400，单位秒\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param Statistics: 统计方式，可取值max, min, avg, sum, 如统计纬度是流量速率或包量速率，仅可取值max\n        :type Statistics: str\n        :param MetricName: 统计纬度，可取值connum, new_conn, inactive_conn, intraffic, outtraffic, inpkg, outpkg, qps\n        :type MetricName: str\n        :param ProtoInfo: 协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效\n        :type ProtoInfo: list of ProtocolPort\n        :param Domain: 统计纬度为qps时，可选特定域名查询\n        :type Domain: str\n        """
        self.Business = None
        self.Id = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Statistics = None
        self.MetricName = None
        self.ProtoInfo = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Statistics = params.get("Statistics")
        self.MetricName = params.get("MetricName")
        if params.get("ProtoInfo") is not None:
            self.ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtoInfo.append(obj)
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizTrendResponse(AbstractModel):
    """DescribeBizTrend返回参数结构体

    """

    def __init__(self):
        """
        :param DataList: 曲线图各个时间点的值\n        :type DataList: list of float\n        :param MetricName: 统计纬度\n        :type MetricName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DataList = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataList = params.get("DataList")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeCCAlarmThresholdRequest(AbstractModel):
    """DescribeCCAlarmThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）\n        :type Business: str\n        :param RsId: 资源ID,字符串类型\n        :type RsId: str\n        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCAlarmThresholdResponse(AbstractModel):
    """DescribeCCAlarmThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param CCAlarmThreshold: CC告警阈值\n        :type CCAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.CCAlarmThreshold`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CCAlarmThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCAlarmThreshold") is not None:
            self.CCAlarmThreshold = CCAlarmThreshold()
            self.CCAlarmThreshold._deserialize(params.get("CCAlarmThreshold"))
        self.RequestId = params.get("RequestId")


class DescribeCCEvListRequest(AbstractModel):
    """DescribeCCEvList请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param IpList: 资源实例的IP，当business不为basic时，如果IpList不为空则Id也必须不能为空；\n        :type IpList: list of str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        """
        self.Business = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.IpList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCEvListResponse(AbstractModel):
    """DescribeCCEvList返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（shield表示棋牌盾；bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param IpList: 资源实例的IP列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpList: list of str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Data: CC攻击事件列表\n        :type Data: list of CCEventRecord\n        :param Total: 总记录数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.IpList = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CCEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCCFrequencyRulesRequest(AbstractModel):
    """DescribeCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleId: 7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；当填写时表示获取转发规则的访问频率控制规则；\n        :type RuleId: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCFrequencyRulesResponse(AbstractModel):
    """DescribeCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        """
        :param CCFrequencyRuleList: 访问频率控制规则列表\n        :type CCFrequencyRuleList: list of CCFrequencyRule\n        :param CCFrequencyRuleStatus: 访问频率控制规则开关状态，取值[on(开启)，off(关闭)]\n        :type CCFrequencyRuleStatus: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CCFrequencyRuleList = None
        self.CCFrequencyRuleStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCFrequencyRuleList") is not None:
            self.CCFrequencyRuleList = []
            for item in params.get("CCFrequencyRuleList"):
                obj = CCFrequencyRule()
                obj._deserialize(item)
                self.CCFrequencyRuleList.append(obj)
        self.CCFrequencyRuleStatus = params.get("CCFrequencyRuleStatus")
        self.RequestId = params.get("RequestId")


class DescribeCCIpAllowDenyRequest(AbstractModel):
    """DescribeCCIpAllowDeny请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Type: 黑或白名单，取值[white(白名单)，black(黑名单)]
注意：此数组只能有一个值，不能同时获取黑名单和白名单\n        :type Type: list of str\n        :param Limit: 分页参数\n        :type Limit: int\n        :param Offset: 分页参数\n        :type Offset: int\n        :param Protocol: 可选，代表HTTP协议或HTTPS协议的CC防护，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；\n        :type Protocol: str\n        """
        self.Business = None
        self.Id = None
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCIpAllowDenyResponse(AbstractModel):
    """DescribeCCIpAllowDeny返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 该字段被RecordList字段替代了，请不要使用\n        :type Data: list of KeyValue\n        :param Total: 记录数\n        :type Total: int\n        :param RecordList: 返回黑/白名单的记录，
"Key":"ip"时，"Value":值表示ip;
"Key":"domain"时， "Value":值表示域名;
"Key":"type"时，"Value":值表示黑白名单类型(white为白名单，block为黑名单);
"Key":"protocol"时，"Value":值表示CC防护的协议(http或https);\n        :type RecordList: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.Total = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCSelfDefinePolicyRequest(AbstractModel):
    """DescribeCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgp高防包；bgp-multip共享包）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Limit: 拉取的条数\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        """
        self.Business = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCSelfDefinePolicyResponse(AbstractModel):
    """DescribeCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 自定义规则总数\n        :type Total: int\n        :param Policys: 策略列表\n        :type Policys: list of CCPolicy\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.Policys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Policys") is not None:
            self.Policys = []
            for item in params.get("Policys"):
                obj = CCPolicy()
                obj._deserialize(item)
                self.Policys.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))]\n        :type MetricName: str\n        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）\n        :type Id: str\n        :param Domain: 域名，可选\n        :type Domain: str\n        """
        self.Business = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Id: 资源ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))]\n        :type MetricName: str\n        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param Data: 值数组\n        :type Data: list of int non-negative\n        :param Count: 值个数\n        :type Count: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeCCUrlAllowRequest(AbstractModel):
    """DescribeCCUrlAllow请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Type: 黑或白名单，取值[white(白名单)]，目前只支持白名单
注意：此数组只能有一个值，且只能为white\n        :type Type: list of str\n        :param Limit: 分页参数\n        :type Limit: int\n        :param Offset: 分页参数\n        :type Offset: int\n        :param Protocol: 可选，代表HTTP协议或HTTPS协议的CC防护，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；\n        :type Protocol: str\n        """
        self.Business = None
        self.Id = None
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCUrlAllowResponse(AbstractModel):
    """DescribeCCUrlAllow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 该字段被RecordList字段替代了，请不要使用\n        :type Data: list of KeyValue\n        :param Total: 记录总数\n        :type Total: int\n        :param RecordList: 返回黑/白名单的记录，
"Key":"url"时，"Value":值表示URL;
"Key":"domain"时， "Value":值表示域名;
"Key":"type"时，"Value":值表示黑白名单类型(white为白名单，block为黑名单);
"Key":"protocol"时，"Value":值表示CC的防护类型(HTTP防护或HTTPS域名防护);\n        :type RecordList: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.Total = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAlarmThresholdRequest(AbstractModel):
    """DescribeDDoSAlarmThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）\n        :type Business: str\n        :param RsId: 资源ID,字符串类型\n        :type RsId: str\n        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAlarmThresholdResponse(AbstractModel):
    """DescribeDDoSAlarmThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param DDoSAlarmThreshold: DDoS告警阈值\n        :type DDoSAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.DDoSAlarmThreshold`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DDoSAlarmThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DDoSAlarmThreshold") is not None:
            self.DDoSAlarmThreshold = DDoSAlarmThreshold()
            self.DDoSAlarmThreshold._deserialize(params.get("DDoSAlarmThreshold"))
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackIPRegionMapRequest(AbstractModel):
    """DescribeDDoSAttackIPRegionMap请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间，最大可统计的时间范围是半年；\n        :type EndTime: str\n        :param IpList: 指定资源的特定IP的攻击源，可选\n        :type IpList: list of str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackIPRegionMapResponse(AbstractModel):
    """DescribeDDoSAttackIPRegionMap返回参数结构体

    """

    def __init__(self):
        """
        :param NationCount: 全球地域分布数据\n        :type NationCount: list of KeyValueRecord\n        :param ProvinceCount: 国内省份地域分布数据\n        :type ProvinceCount: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NationCount = None
        self.ProvinceCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NationCount") is not None:
            self.NationCount = []
            for item in params.get("NationCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.NationCount.append(obj)
        if params.get("ProvinceCount") is not None:
            self.ProvinceCount = []
            for item in params.get("ProvinceCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ProvinceCount.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackSourceRequest(AbstractModel):
    """DescribeDDoSAttackSource请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 起始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        :param IpList: 获取指定资源的特定ip的攻击源，可选\n        :type IpList: list of str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackSourceResponse(AbstractModel):
    """DescribeDDoSAttackSource返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总攻击源条数\n        :type Total: int\n        :param AttackSourceList: 攻击源列表\n        :type AttackSourceList: list of DDoSAttackSourceRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.AttackSourceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AttackSourceList") is not None:
            self.AttackSourceList = []
            for item in params.get("AttackSourceList"):
                obj = DDoSAttackSourceRecord()
                obj._deserialize(item)
                self.AttackSourceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSCountRequest(AbstractModel):
    """DescribeDDoSCount请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]\n        :type MetricName: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSCountResponse(AbstractModel):
    """DescribeDDoSCount返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]\n        :type MetricName: str\n        :param Data: Key-Value值数组，Key说明如下，
当MetricName为traffic时：
key为"TcpKBSum"，表示TCP报文流量，单位KB
key为"UdpKBSum"，表示UDP报文流量，单位KB
key为"IcmpKBSum"，表示ICMP报文流量，单位KB
key为"OtherKBSum"，表示其他报文流量，单位KB

当MetricName为pkg时：
key为"TcpPacketSum"，表示TCP报文个数，单位个
key为"UdpPacketSum"，表示UDP报文个数，单位个
key为"IcmpPacketSum"，表示ICMP报文个数，单位个
key为"OtherPacketSum"，表示其他报文个数，单位个

当MetricName为classnum时：
key的值表示攻击事件类型，其中Key为"UNKNOWNFLOOD"，表示未知的攻击事件\n        :type Data: list of KeyValue\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSDefendStatusRequest(AbstractModel):
    """DescribeDDoSDefendStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（basic表示基础防护；bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源实例ID，只有当Business不是基础防护时才需要填写此字段；\n        :type Id: str\n        :param Ip: 基础防护的IP，只有当Business为基础防护时才需要填写此字段；\n        :type Ip: str\n        :param BizType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]\n        :type BizType: str\n        :param DeviceType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]\n        :type DeviceType: str\n        :param InstanceId: 只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);\n        :type InstanceId: str\n        :param IPRegion: 只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：
"bj":     华北地区(北京)
"cd":     西南地区(成都)
"cq":     西南地区(重庆)
"gz":     华南地区(广州)
"gzopen": 华南地区(广州Open)
"hk":     中国香港
"kr":     东南亚地区(首尔)
"sh":     华东地区(上海)
"shjr":   华东地区(上海金融)
"szjr":   华南地区(深圳金融)
"sg":     东南亚地区(新加坡)
"th":     东南亚地区(泰国)
"de":     欧洲地区(德国)
"usw":    美国西部（硅谷）
"ca":     北美地区(多伦多)
"jp":     日本
"hzec":   杭州
"in":     印度
"use":    美东地区（弗吉尼亚）
"ru":     俄罗斯
"tpe":    中国台湾
"nj":     南京\n        :type IPRegion: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSDefendStatusResponse(AbstractModel):
    """DescribeDDoSDefendStatus返回参数结构体

    """

    def __init__(self):
        """
        :param DefendStatus: 防护状态，为0表示防护处于关闭状态，为1表示防护处于开启状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type DefendStatus: int\n        :param UndefendExpire: 防护临时关闭的过期时间，当防护状态为开启时此字段为空；
注意：此字段可能返回 null，表示取不到有效值。\n        :type UndefendExpire: str\n        :param ShowFlag: 控制台功能展示字段，为1表示控制台功能展示，为0表示控制台功能隐藏
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShowFlag: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DefendStatus = None
        self.UndefendExpire = None
        self.ShowFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DefendStatus = params.get("DefendStatus")
        self.UndefendExpire = params.get("UndefendExpire")
        self.ShowFlag = params.get("ShowFlag")
        self.RequestId = params.get("RequestId")


class DescribeDDoSEvInfoRequest(AbstractModel):
    """DescribeDDoSEvInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvInfoResponse(AbstractModel):
    """DescribeDDoSEvInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        :param TcpPacketSum: TCP报文攻击包数\n        :type TcpPacketSum: int\n        :param TcpKBSum: TCP报文攻击流量，单位KB\n        :type TcpKBSum: int\n        :param UdpPacketSum: UDP报文攻击包数\n        :type UdpPacketSum: int\n        :param UdpKBSum: UDP报文攻击流量，单位KB\n        :type UdpKBSum: int\n        :param IcmpPacketSum: ICMP报文攻击包数\n        :type IcmpPacketSum: int\n        :param IcmpKBSum: ICMP报文攻击流量，单位KB\n        :type IcmpKBSum: int\n        :param OtherPacketSum: 其他报文攻击包数\n        :type OtherPacketSum: int\n        :param OtherKBSum: 其他报文攻击流量，单位KB\n        :type OtherKBSum: int\n        :param TotalTraffic: 累计攻击流量，单位KB\n        :type TotalTraffic: int\n        :param Mbps: 攻击流量带宽峰值\n        :type Mbps: int\n        :param Pps: 攻击包速率峰值\n        :type Pps: int\n        :param PcapUrl: PCAP文件下载链接\n        :type PcapUrl: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.TcpPacketSum = None
        self.TcpKBSum = None
        self.UdpPacketSum = None
        self.UdpKBSum = None
        self.IcmpPacketSum = None
        self.IcmpKBSum = None
        self.OtherPacketSum = None
        self.OtherKBSum = None
        self.TotalTraffic = None
        self.Mbps = None
        self.Pps = None
        self.PcapUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TcpPacketSum = params.get("TcpPacketSum")
        self.TcpKBSum = params.get("TcpKBSum")
        self.UdpPacketSum = params.get("UdpPacketSum")
        self.UdpKBSum = params.get("UdpKBSum")
        self.IcmpPacketSum = params.get("IcmpPacketSum")
        self.IcmpKBSum = params.get("IcmpKBSum")
        self.OtherPacketSum = params.get("OtherPacketSum")
        self.OtherKBSum = params.get("OtherKBSum")
        self.TotalTraffic = params.get("TotalTraffic")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.PcapUrl = params.get("PcapUrl")
        self.RequestId = params.get("RequestId")


class DescribeDDoSEvListRequest(AbstractModel):
    """DescribeDDoSEvList请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）\n        :type Id: str\n        :param IpList: 资源的IP\n        :type IpList: list of str\n        :param OverLoad: 是否超过弹性防护峰值，取值[yes(是)，no(否)]，填写空字符串时表示不进行过滤\n        :type OverLoad: str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        """
        self.Business = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.IpList = None
        self.OverLoad = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.OverLoad = params.get("OverLoad")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvListResponse(AbstractModel):
    """DescribeDDoSEvList返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param IpList: 资源的IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpList: list of str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Data: DDoS攻击事件列表\n        :type Data: list of DDoSEventRecord\n        :param Total: 总记录数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.IpList = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDDoSIpLogRequest(AbstractModel):
    """DescribeDDoSIpLog请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSIpLogResponse(AbstractModel):
    """DescribeDDoSIpLog返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        :param Data: IP攻击日志，KeyValue数组，Key-Value取值说明：
Key为"LogTime"时，Value值为IP日志时间
Key为"LogMessage"时，Value值为Ip日志内容\n        :type Data: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetCountRequest(AbstractModel):
    """DescribeDDoSNetCount请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]\n        :type MetricName: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetCountResponse(AbstractModel):
    """DescribeDDoSNetCount返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]\n        :type MetricName: str\n        :param Data: Key-Value值数组，Key说明如下，
当MetricName为traffic时：
key为"TcpKBSum"，表示TCP报文流量，单位KB
key为"UdpKBSum"，表示UDP报文流量，单位KB
key为"IcmpKBSum"，表示ICMP报文流量，单位KB
key为"OtherKBSum"，表示其他报文流量，单位KB

当MetricName为pkg时：
key为"TcpPacketSum"，表示TCP报文个数，单位个
key为"UdpPacketSum"，表示UDP报文个数，单位个
key为"IcmpPacketSum"，表示ICMP报文个数，单位个
key为"OtherPacketSum"，表示其他报文个数，单位个

当MetricName为classnum时：
key的值表示攻击事件类型，其中Key为"UNKNOWNFLOOD"，表示未知的攻击事件\n        :type Data: list of KeyValue\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetEvInfoRequest(AbstractModel):
    """DescribeDDoSNetEvInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvInfoResponse(AbstractModel):
    """DescribeDDoSNetEvInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        :param TcpPacketSum: TCP报文攻击包数\n        :type TcpPacketSum: int\n        :param TcpKBSum: TCP报文攻击流量，单位KB\n        :type TcpKBSum: int\n        :param UdpPacketSum: UDP报文攻击包数\n        :type UdpPacketSum: int\n        :param UdpKBSum: UDP报文攻击流量，单位KB\n        :type UdpKBSum: int\n        :param IcmpPacketSum: ICMP报文攻击包数\n        :type IcmpPacketSum: int\n        :param IcmpKBSum: ICMP报文攻击流量，单位KB\n        :type IcmpKBSum: int\n        :param OtherPacketSum: 其他报文攻击包数\n        :type OtherPacketSum: int\n        :param OtherKBSum: 其他报文攻击流量，单位KB\n        :type OtherKBSum: int\n        :param TotalTraffic: 累计攻击流量，单位KB\n        :type TotalTraffic: int\n        :param Mbps: 攻击流量带宽峰值\n        :type Mbps: int\n        :param Pps: 攻击包速率峰值\n        :type Pps: int\n        :param PcapUrl: PCAP文件下载链接\n        :type PcapUrl: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.TcpPacketSum = None
        self.TcpKBSum = None
        self.UdpPacketSum = None
        self.UdpKBSum = None
        self.IcmpPacketSum = None
        self.IcmpKBSum = None
        self.OtherPacketSum = None
        self.OtherKBSum = None
        self.TotalTraffic = None
        self.Mbps = None
        self.Pps = None
        self.PcapUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TcpPacketSum = params.get("TcpPacketSum")
        self.TcpKBSum = params.get("TcpKBSum")
        self.UdpPacketSum = params.get("UdpPacketSum")
        self.UdpKBSum = params.get("UdpKBSum")
        self.IcmpPacketSum = params.get("IcmpPacketSum")
        self.IcmpKBSum = params.get("IcmpKBSum")
        self.OtherPacketSum = params.get("OtherPacketSum")
        self.OtherKBSum = params.get("OtherKBSum")
        self.TotalTraffic = params.get("TotalTraffic")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.PcapUrl = params.get("PcapUrl")
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetEvListRequest(AbstractModel):
    """DescribeDDoSNetEvList请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvListResponse(AbstractModel):
    """DescribeDDoSNetEvList返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Data: DDoS攻击事件列表\n        :type Data: list of DDoSEventRecord\n        :param Total: 总记录数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetIpLogRequest(AbstractModel):
    """DescribeDDoSNetIpLog请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetIpLogResponse(AbstractModel):
    """DescribeDDoSNetIpLog返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param StartTime: 攻击开始时间\n        :type StartTime: str\n        :param EndTime: 攻击结束时间\n        :type EndTime: str\n        :param Data: IP攻击日志，KeyValue数组，Key-Value取值说明：
Key为"LogTime"时，Value值为IP日志时间
Key为"LogMessage"时，Value值为Ip日志内容\n        :type Data: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetTrendRequest(AbstractModel):
    """DescribeDDoSNetTrend请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]\n        :type MetricName: str\n        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetTrendResponse(AbstractModel):
    """DescribeDDoSNetTrend返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]\n        :type MetricName: str\n        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param Data: 值数组\n        :type Data: list of int non-negative\n        :param Count: 值个数\n        :type Count: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 可选字段，资源ID，如果填写则表示该资源绑定的DDoS高级策略\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
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
        """
        :param DDosPolicyList: DDoS高级策略列表\n        :type DDosPolicyList: list of DDosPolicy\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DDosPolicyList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DDosPolicyList") is not None:
            self.DDosPolicyList = []
            for item in params.get("DDosPolicyList"):
                obj = DDosPolicy()
                obj._deserialize(item)
                self.DDosPolicyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Ip: 资源实例的IP\n        :type Ip: str\n        :param MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]\n        :type MetricName: str\n        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）\n        :type Id: str\n        """
        self.Business = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend返回参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）\n        :type Business: str\n        :param Id: 资源ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param Ip: 资源的IP\n        :type Ip: str\n        :param MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]\n        :type MetricName: str\n        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]\n        :type Period: int\n        :param StartTime: 统计开始时间\n        :type StartTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param Data: 值数组，攻击流量带宽单位为Mbps，包速率单位为pps\n        :type Data: list of int non-negative\n        :param Count: 值个数\n        :type Count: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeDDoSUsedStatisRequest(AbstractModel):
    """DescribeDDoSUsedStatis请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSUsedStatisResponse(AbstractModel):
    """DescribeDDoSUsedStatis返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 字段值，如下：
Days：高防资源使用天数
Attacks：DDoS防护次数\n        :type Data: list of KeyValue\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIPProductInfoRequest(AbstractModel):
    """DescribeIPProductInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包）\n        :type Business: str\n        :param IpList: IP列表\n        :type IpList: list of str\n        """
        self.Business = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPProductInfoResponse(AbstractModel):
    """DescribeIPProductInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 云产品信息列表，如果没有查询到则返回空数组，值说明如下：
Key为ProductName时，value表示云产品实例的名称；
Key为ProductInstanceId时，value表示云产品实例的ID；
Key为ProductType时，value表示的是云产品的类型（cvm表示云主机、clb表示负载均衡）;
Key为IP时，value表示云产品实例的IP；\n        :type Data: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInsurePacksRequest(AbstractModel):
    """DescribeInsurePacks请求参数结构体

    """

    def __init__(self):
        """
        :param IdList: 可选字段，保险包套餐ID，当要获取指定ID（例如insure-000000xe）的保险包套餐时请填写此字段；\n        :type IdList: list of str\n        """
        self.IdList = None


    def _deserialize(self, params):
        self.IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInsurePacksResponse(AbstractModel):
    """DescribeInsurePacks返回参数结构体

    """

    def __init__(self):
        """
        :param InsurePacks: 保险包套餐列表\n        :type InsurePacks: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InsurePacks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InsurePacks") is not None:
            self.InsurePacks = []
            for item in params.get("InsurePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.InsurePacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpBlockListRequest(AbstractModel):
    """DescribeIpBlockList请求参数结构体

    """


class DescribeIpBlockListResponse(AbstractModel):
    """DescribeIpBlockList返回参数结构体

    """

    def __init__(self):
        """
        :param List: IP封堵列表\n        :type List: list of IpBlockData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = IpBlockData()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpUnBlockListRequest(AbstractModel):
    """DescribeIpUnBlockList请求参数结构体

    """

    def __init__(self):
        """
        :param BeginTime: 开始时间\n        :type BeginTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Ip: IP（不为空时，进行IP过滤）\n        :type Ip: str\n        :param Paging: 分页参数（不为空时，进行分页查询），此字段后面会弃用，请用Limit和Offset字段代替；\n        :type Paging: :class:`tencentcloud.dayu.v20180709.models.Paging`\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        """
        self.BeginTime = None
        self.EndTime = None
        self.Ip = None
        self.Paging = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")
        if params.get("Paging") is not None:
            self.Paging = Paging()
            self.Paging._deserialize(params.get("Paging"))
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpUnBlockListResponse(AbstractModel):
    """DescribeIpUnBlockList返回参数结构体

    """

    def __init__(self):
        """
        :param BeginTime: 开始时间\n        :type BeginTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param List: IP解封记录\n        :type List: list of IpUnBlockData\n        :param Total: 总记录数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BeginTime = None
        self.EndTime = None
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = IpUnBlockData()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeL4HealthConfigRequest(AbstractModel):
    """DescribeL4HealthConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleIdList: 规则ID数组，当导出所有规则的健康检查配置则不填或填空数组；\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4HealthConfigResponse(AbstractModel):
    """DescribeL4HealthConfig返回参数结构体

    """

    def __init__(self):
        """
        :param HealthConfig: 四层健康检查配置数组\n        :type HealthConfig: list of L4HealthConfig\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.HealthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4RulesErrHealthRequest(AbstractModel):
    """DescribeL4RulesErrHealth请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4RulesErrHealthResponse(AbstractModel):
    """DescribeL4RulesErrHealth返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 异常规则的总数\n        :type Total: int\n        :param ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP，多个IP用","分割\n        :type ErrHealths: list of KeyValue\n        :param ExtErrHealths: 异常规则列表(提供更多的错误相关信息)，返回值说明:
Key值为RuleId时，Value值为规则ID；
Key值为Protocol时，Value值为规则的转发协议；
Key值为VirtualPort时，Value值为规则的转发端口；
Key值为ErrMessage时，Value值为健康检查异常信息；
健康检查异常信息的格式为"SourceIp:1.1.1.1|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6" 多个源IP的错误信息用，分割,
SourceIp表示源站IP，SourcePort表示源站端口，AbnormalStatTime表示异常时间，AbnormalReason表示异常原因，Interval表示检查周期，CheckNum表示检查次数，FailNum表示失败次数；\n        :type ExtErrHealths: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.ErrHealths = None
        self.ExtErrHealths = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        if params.get("ExtErrHealths") is not None:
            self.ExtErrHealths = []
            for item in params.get("ExtErrHealths"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ExtErrHealths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7HealthConfigRequest(AbstractModel):
    """DescribeL7HealthConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleIdList: 规则ID数组，当导出所有规则的健康检查配置则不填或填空数组；\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7HealthConfigResponse(AbstractModel):
    """DescribeL7HealthConfig返回参数结构体

    """

    def __init__(self):
        """
        :param HealthConfig: 七层健康检查配置数组\n        :type HealthConfig: list of L7HealthConfig\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.HealthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNewL4RulesErrHealthRequest(AbstractModel):
    """DescribeNewL4RulesErrHealth请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param RuleIdList: 规则ID列表\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL4RulesErrHealthResponse(AbstractModel):
    """DescribeNewL4RulesErrHealth返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 异常规则的总数\n        :type Total: int\n        :param ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP，多个IP用","分割\n        :type ErrHealths: list of KeyValue\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.ErrHealths = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNewL4RulesRequest(AbstractModel):
    """DescribeNewL4Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Ip: 指定IP查询\n        :type Ip: str\n        :param VirtualPort: 指定高防IP端口查询\n        :type VirtualPort: int\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        """
        self.Business = None
        self.Ip = None
        self.VirtualPort = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.VirtualPort = params.get("VirtualPort")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL4RulesResponse(AbstractModel):
    """DescribeNewL4Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 转发规则列表\n        :type Rules: list of NewL4RuleEntry\n        :param Total: 总规则数\n        :type Total: int\n        :param Healths: 四层健康检查配置列表\n        :type Healths: list of L4RuleHealth\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = NewL4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNewL7RulesErrHealthRequest(AbstractModel):
    """DescribeNewL7RulesErrHealth请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP)\n        :type Business: str\n        :param RuleIdList: 规则Id列表\n        :type RuleIdList: list of str\n        """
        self.Business = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesErrHealthResponse(AbstractModel):
    """DescribeNewL7RulesErrHealth返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 异常规则的总数\n        :type Total: int\n        :param ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP及错误信息，多个IP用","分割\n        :type ErrHealths: list of KeyValue\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.ErrHealths = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePackIndexRequest(AbstractModel):
    """DescribePackIndex请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示高防包；net表示高防IP专业版）\n        :type Business: str\n        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackIndexResponse(AbstractModel):
    """DescribePackIndex返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 字段值，如下：
TotalPackCount：资源数
AttackPackCount：清洗中的资源数
BlockPackCount：封堵中的资源数
ExpiredPackCount：过期的资源数
ExpireingPackCount：即将过期的资源数
IsolatePackCount：隔离中的资源数\n        :type Data: list of KeyValue\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePcapRequest(AbstractModel):
    """DescribePcap请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param StartTime: 攻击事件的开始时间，格式为"2018-08-28 07:00:00"\n        :type StartTime: str\n        :param EndTime: 攻击事件的结束时间，格式为"2018-08-28 07:02:00"\n        :type EndTime: str\n        :param Ip: 资源的IP，只有当Business为net时才需要填写资源实例下的IP；\n        :type Ip: str\n        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePcapResponse(AbstractModel):
    """DescribePcap返回参数结构体

    """

    def __init__(self):
        """
        :param PcapUrlList: pcap包的下载链接列表，无pcap包时为空数组；\n        :type PcapUrlList: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PcapUrlList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PcapUrlList = params.get("PcapUrlList")
        self.RequestId = params.get("RequestId")


class DescribePolicyCaseRequest(AbstractModel):
    """DescribePolicyCase请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param SceneId: 策略场景ID\n        :type SceneId: str\n        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyCaseResponse(AbstractModel):
    """DescribePolicyCase返回参数结构体

    """

    def __init__(self):
        """
        :param CaseList: 策略场景列表\n        :type CaseList: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CaseList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CaseList") is not None:
            self.CaseList = []
            for item in params.get("CaseList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.CaseList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResIpListRequest(AbstractModel):
    """DescribeResIpList请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param IdList: 资源ID, 如果不填，则获取用户所有资源的IP\n        :type IdList: list of str\n        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResIpListResponse(AbstractModel):
    """DescribeResIpList返回参数结构体

    """

    def __init__(self):
        """
        :param Resource: 资源的IP列表\n        :type Resource: list of ResourceIp\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Resource = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self.Resource = []
            for item in params.get("Resource"):
                obj = ResourceIp()
                obj._deserialize(item)
                self.Resource.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceListRequest(AbstractModel):
    """DescribeResourceList请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param RegionList: 地域码搜索，可选，当不指定地域时空数组，当指定地域时，填地域码。例如：["gz", "sh"]\n        :type RegionList: list of str\n        :param Line: 线路搜索，可选，只有当获取高防IP资源列表是可以选填，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]，当获取其他产品时请填空数组；\n        :type Line: list of int non-negative\n        :param IdList: 资源ID搜索，可选，当不为空数组时表示获取指定资源的资源列表；\n        :type IdList: list of str\n        :param Name: 资源名称搜索，可选，当不为空字符串时表示按名称搜索资源；\n        :type Name: str\n        :param IpList: IP搜索列表，可选，当不为空时表示按照IP搜索资源；\n        :type IpList: list of str\n        :param Status: 资源状态搜索列表，可选，取值为[0（运行中）, 1（清洗中）, 2（封堵中）]，当填空数组时不进行状态搜索；\n        :type Status: list of int non-negative\n        :param Expire: 即将到期搜索；可选，取值为[0（不搜索），1（搜索即将到期的资源）]\n        :type Expire: int\n        :param OderBy: 排序字段，可选\n        :type OderBy: list of OrderBy\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        :param CName: 高防IP专业版资源的CNAME，可选，只对高防IP专业版资源列表有效；\n        :type CName: str\n        :param Domain: 高防IP专业版资源的域名，可选，只对高防IP专业版资源列表有效；\n        :type Domain: str\n        """
        self.Business = None
        self.RegionList = None
        self.Line = None
        self.IdList = None
        self.Name = None
        self.IpList = None
        self.Status = None
        self.Expire = None
        self.OderBy = None
        self.Limit = None
        self.Offset = None
        self.CName = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RegionList = params.get("RegionList")
        self.Line = params.get("Line")
        self.IdList = params.get("IdList")
        self.Name = params.get("Name")
        self.IpList = params.get("IpList")
        self.Status = params.get("Status")
        self.Expire = params.get("Expire")
        if params.get("OderBy") is not None:
            self.OderBy = []
            for item in params.get("OderBy"):
                obj = OrderBy()
                obj._deserialize(item)
                self.OderBy.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.CName = params.get("CName")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceListResponse(AbstractModel):
    """DescribeResourceList返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总记录数\n        :type Total: int\n        :param ServicePacks: 资源记录列表，返回Key值说明：
"Key": "CreateTime" 表示资源实例购买时间
"Key": "Region" 表示资源实例的地域
"Key": "BoundIP" 表示独享包实例绑定的IP
"Key": "Id" 表示资源实例的ID
"Key": "CCEnabled" 表示资源实例的CC防护开关状态
"Key": "DDoSThreshold" 表示资源实例的DDoS的清洗阈值	
"Key": "BoundStatus" 表示独享包或共享包实例的绑定IP操作状态(绑定中或绑定完成)
"Key": "Type" 此字段弃用
"Key": "ElasticLimit" 表示资源实例的弹性防护值
"Key": "DDoSAI" 表示资源实例的DDoS AI防护开关
"Key": "OverloadCount" 表示资源实例受到超过弹性防护值的次数
"Key": "Status" 表示资源实例的状态(idle:运行中, attacking:攻击中, blocking:封堵中, isolate:隔离中)
"Key": "Lbid" 此字段弃用
"Key": "ShowFlag" 此字段弃用
"Key": "Expire" 表示资源实例的过期时间
"Key": "CCThreshold" 表示资源实例的CC防护触发阈值
"Key": "AutoRenewFlag" 表示资源实例的自动续费是否开启
"Key": "IspCode" 表示独享包或共享包的线路(0-电信, 1-联通, 2-移动, 5-BGP)
"Key": "PackType" 表示套餐包类型
"Key": "PackId" 表示套餐包ID
"Key": "Name" 表示资源实例的名称
"Key": "Locked" 此字段弃用
"Key": "IpDDoSLevel" 表示资源实例的防护等级(low-宽松, middle-正常, high-严格)
"Key": "DefendStatus" 表示资源实例的DDoS防护状态(防护开启或临时关闭)
"Key": "UndefendExpire" 表示资源实例的DDoS防护临时关闭结束时间
"Key": "Tgw" 表示资源实例是否是新资源
"Key": "Bandwidth" 表示资源实例的保底防护值，只针对高防包和高防IP
"Key": "DdosMax" 表示资源实例的保底防护值，只针对高防IP专业版
"Key": "GFBandwidth" 表示资源实例的保底业务带宽，只针对高防IP
"Key": "ServiceBandwidth" 表示资源实例的保底业务带宽，只针对高防IP专业版\n        :type ServicePacks: list of KeyValueRecord\n        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.ServicePacks = None
        self.Business = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ServicePacks") is not None:
            self.ServicePacks = []
            for item in params.get("ServicePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ServicePacks.append(obj)
        self.Business = params.get("Business")
        self.RequestId = params.get("RequestId")


class DescribeRuleSetsRequest(AbstractModel):
    """DescribeRuleSets请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param IdList: 资源ID列表\n        :type IdList: list of str\n        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleSetsResponse(AbstractModel):
    """DescribeRuleSets返回参数结构体

    """

    def __init__(self):
        """
        :param L4RuleSets: 规则记录数数组，取值说明:
Key值为"Id"时，Value表示资源ID
Key值为"RuleIdList"时，Value值表示资源的规则ID，多个规则ID用","分割
Key值为"RuleNameList"时，Value值表示资源的规则名，多个规则名用","分割
Key值为"RuleNum"时，Value值表示资源的规则数\n        :type L4RuleSets: list of KeyValueRecord\n        :param L7RuleSets: 规则记录数数组，取值说明:
Key值为"Id"时，Value表示资源ID
Key值为"RuleIdList"时，Value值表示资源的规则ID，多个规则ID用","分割
Key值为"RuleNameList"时，Value值表示资源的规则名，多个规则名用","分割
Key值为"RuleNum"时，Value值表示资源的规则数\n        :type L7RuleSets: list of KeyValueRecord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.L4RuleSets = None
        self.L7RuleSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("L4RuleSets") is not None:
            self.L4RuleSets = []
            for item in params.get("L4RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.L4RuleSets.append(obj)
        if params.get("L7RuleSets") is not None:
            self.L7RuleSets = []
            for item in params.get("L7RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.L7RuleSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSchedulingDomainListRequest(AbstractModel):
    """DescribeSchedulingDomainList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        :param Domain: 可选，筛选特定的域名\n        :type Domain: str\n        """
        self.Limit = None
        self.Offset = None
        self.Domain = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSchedulingDomainListResponse(AbstractModel):
    """DescribeSchedulingDomainList返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 调度域名总数\n        :type Total: int\n        :param DomainList: 调度域名列表信息\n        :type DomainList: list of SchedulingDomain\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = SchedulingDomain()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecIndexRequest(AbstractModel):
    """DescribeSecIndex请求参数结构体

    """


class DescribeSecIndexResponse(AbstractModel):
    """DescribeSecIndex返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 字段值，如下：
AttackIpCount：受攻击的IP数
AttackCount：攻击次数
BlockCount：封堵次数
MaxMbps：攻击峰值Mbps
IpNum：统计的IP数据\n        :type Data: list of KeyValue\n        :param BeginDate: 本月开始时间\n        :type BeginDate: str\n        :param EndDate: 本月结束时间\n        :type EndDate: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.BeginDate = None
        self.EndDate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.RequestId = params.get("RequestId")


class DescribeSourceIpSegmentRequest(AbstractModel):
    """DescribeSourceIpSegment请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceIpSegmentResponse(AbstractModel):
    """DescribeSourceIpSegment返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 回源IP段，多个用"；"分隔\n        :type Data: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeTransmitStatisRequest(AbstractModel):
    """DescribeTransmitStatis请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版；bgp表示独享包；bgp-multip表示共享包）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param MetricName: 指标名，取值：
traffic表示流量带宽；
pkg表示包速率；\n        :type MetricName: str\n        :param Period: 统计时间粒度（300表示5分钟；3600表示小时；86400表示天）\n        :type Period: int\n        :param StartTime: 统计开始时间，秒部分保持为0，分钟部分为5的倍数\n        :type StartTime: str\n        :param EndTime: 统计结束时间，秒部分保持为0，分钟部分为5的倍数\n        :type EndTime: str\n        :param IpList: 资源的IP（当Business为bgp-multip时必填，且仅支持一个IP）；当不填写时，默认统计资源实例的所有IP；资源实例有多个IP（比如高防IP专业版）时，统计方式是求和；\n        :type IpList: list of str\n        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTransmitStatisResponse(AbstractModel):
    """DescribeTransmitStatis返回参数结构体

    """

    def __init__(self):
        """
        :param InDataList: 当MetricName=traffic时，表示入流量带宽，单位bps；
当MetricName=pkg时，表示入包速率，单位pps；\n        :type InDataList: list of float\n        :param OutDataList: 当MetricName=traffic时，表示出流量带宽，单位bps；
当MetricName=pkg时，表示出包速率，单位pps；\n        :type OutDataList: list of float\n        :param MetricName: 指标名：
traffic表示流量带宽；
pkg表示包速率；\n        :type MetricName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InDataList = None
        self.OutDataList = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InDataList = params.get("InDataList")
        self.OutDataList = params.get("OutDataList")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeUnBlockStatisRequest(AbstractModel):
    """DescribeUnBlockStatis请求参数结构体

    """


class DescribeUnBlockStatisResponse(AbstractModel):
    """DescribeUnBlockStatis返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 解封总配额数\n        :type Total: int\n        :param Used: 已使用次数\n        :type Used: int\n        :param BeginTime: 统计起始时间\n        :type BeginTime: str\n        :param EndTime: 统计结束时间\n        :type EndTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.Used = None
        self.BeginTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribleL4RulesRequest(AbstractModel):
    """DescribleL4Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleIdList: 规则ID，可选参数，填写后获取指定的规则\n        :type RuleIdList: list of str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL4RulesResponse(AbstractModel):
    """DescribleL4Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 转发规则列表\n        :type Rules: list of L4RuleEntry\n        :param Total: 总规则数\n        :type Total: int\n        :param Healths: 健康检查配置列表\n        :type Healths: list of L4RuleHealth\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleL7RulesRequest(AbstractModel):
    """DescribleL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleIdList: 规则ID，可选参数，填写后获取指定的规则\n        :type RuleIdList: list of str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        :param Domain: 域名搜索，选填，当需要搜索域名请填写\n        :type Domain: str\n        :param ProtocolList: 转发协议搜索，选填，取值[http, https, http/https]\n        :type ProtocolList: list of str\n        :param StatusList: 状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]\n        :type StatusList: list of int non-negative\n        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None
        self.Limit = None
        self.Offset = None
        self.Domain = None
        self.ProtocolList = None
        self.StatusList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")
        self.ProtocolList = params.get("ProtocolList")
        self.StatusList = params.get("StatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL7RulesResponse(AbstractModel):
    """DescribleL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 转发规则列表\n        :type Rules: list of L7RuleEntry\n        :param Total: 总规则数\n        :type Total: int\n        :param Healths: 健康检查配置列表\n        :type Healths: list of L7RuleHealth\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleNewL7RulesRequest(AbstractModel):
    """DescribleNewL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Limit: 一页条数，填0表示不分页\n        :type Limit: int\n        :param Offset: 页起始偏移，取值为(页码-1)*一页条数\n        :type Offset: int\n        :param Domain: 域名搜索，选填，当需要搜索域名请填写\n        :type Domain: str\n        :param ProtocolList: 转发协议搜索，选填，取值[http, https, http/https]\n        :type ProtocolList: list of str\n        :param StatusList: 状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]\n        :type StatusList: list of int non-negative\n        :param Ip: IP搜索，选填，当需要搜索IP请填写\n        :type Ip: str\n        """
        self.Business = None
        self.Limit = None
        self.Offset = None
        self.Domain = None
        self.ProtocolList = None
        self.StatusList = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")
        self.ProtocolList = params.get("ProtocolList")
        self.StatusList = params.get("StatusList")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleNewL7RulesResponse(AbstractModel):
    """DescribleNewL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 转发规则列表\n        :type Rules: list of NewL7RuleEntry\n        :param Total: 总规则数\n        :type Total: int\n        :param Healths: 健康检查配置列表\n        :type Healths: list of L7RuleHealth\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = NewL7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleRegionCountRequest(AbstractModel):
    """DescribleRegionCount请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；）\n        :type Business: str\n        :param LineList: 根据线路统计，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]；只对高防IP产品有效，其他产品此字段忽略\n        :type LineList: list of int non-negative\n        """
        self.Business = None
        self.LineList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleRegionCountResponse(AbstractModel):
    """DescribleRegionCount返回参数结构体

    """

    def __init__(self):
        """
        :param RegionList: 地域资源实例数\n        :type RegionList: list of RegionInstanceCount\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInstanceCount()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class HttpStatusMap(AbstractModel):
    """业务流量的http状态码聚合数据

    """

    def __init__(self):
        """
        :param Http2xx: http2xx状态码\n        :type Http2xx: list of float\n        :param Http3xx: http3xx状态码\n        :type Http3xx: list of float\n        :param Http404: http404状态码\n        :type Http404: list of float\n        :param Http4xx: http4xx状态码\n        :type Http4xx: list of float\n        :param Http5xx: http5xx状态码\n        :type Http5xx: list of float\n        :param SourceHttp2xx: http2xx回源状态码\n        :type SourceHttp2xx: list of float\n        :param SourceHttp3xx: http3xx回源状态码\n        :type SourceHttp3xx: list of float\n        :param SourceHttp404: http404回源状态码\n        :type SourceHttp404: list of float\n        :param SourceHttp4xx: http4xx回源状态码\n        :type SourceHttp4xx: list of float\n        :param SourceHttp5xx: http5xx回源状态码\n        :type SourceHttp5xx: list of float\n        """
        self.Http2xx = None
        self.Http3xx = None
        self.Http404 = None
        self.Http4xx = None
        self.Http5xx = None
        self.SourceHttp2xx = None
        self.SourceHttp3xx = None
        self.SourceHttp404 = None
        self.SourceHttp4xx = None
        self.SourceHttp5xx = None


    def _deserialize(self, params):
        self.Http2xx = params.get("Http2xx")
        self.Http3xx = params.get("Http3xx")
        self.Http404 = params.get("Http404")
        self.Http4xx = params.get("Http4xx")
        self.Http5xx = params.get("Http5xx")
        self.SourceHttp2xx = params.get("SourceHttp2xx")
        self.SourceHttp3xx = params.get("SourceHttp3xx")
        self.SourceHttp404 = params.get("SourceHttp404")
        self.SourceHttp4xx = params.get("SourceHttp4xx")
        self.SourceHttp5xx = params.get("SourceHttp5xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlackWhite(AbstractModel):
    """黑白IP

    """

    def __init__(self):
        """
        :param Ip: IP地址\n        :type Ip: str\n        :param Type: 黑白类型，取值范围[black，white]\n        :type Type: str\n        """
        self.Ip = None
        self.Type = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlockData(AbstractModel):
    """IP封堵记录

    """

    def __init__(self):
        """
        :param Ip: IP\n        :type Ip: str\n        :param Status: 状态（Blocked：被封堵；UnBlocking：解封中；UnBlockFailed：解封失败）\n        :type Status: str\n        :param BlockTime: 封堵时间\n        :type BlockTime: str\n        :param UnBlockTime: 解封时间（预计解封时间）\n        :type UnBlockTime: str\n        :param ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）\n        :type ActionType: str\n        """
        self.Ip = None
        self.Status = None
        self.BlockTime = None
        self.UnBlockTime = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Status = params.get("Status")
        self.BlockTime = params.get("BlockTime")
        self.UnBlockTime = params.get("UnBlockTime")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpUnBlockData(AbstractModel):
    """IP解封记录

    """

    def __init__(self):
        """
        :param Ip: IP\n        :type Ip: str\n        :param BlockTime: 封堵时间\n        :type BlockTime: str\n        :param UnBlockTime: 解封时间（实际解封时间）\n        :type UnBlockTime: str\n        :param ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）\n        :type ActionType: str\n        """
        self.Ip = None
        self.BlockTime = None
        self.UnBlockTime = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BlockTime = params.get("BlockTime")
        self.UnBlockTime = params.get("UnBlockTime")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """字段值，K-V形式

    """

    def __init__(self):
        """
        :param Key: 字段名称\n        :type Key: str\n        :param Value: 字段取值\n        :type Value: str\n        """
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
        


class KeyValueRecord(AbstractModel):
    """KeyValue记录

    """

    def __init__(self):
        """
        :param Record: 一条记录的Key-Value数组\n        :type Record: list of KeyValue\n        """
        self.Record = None


    def _deserialize(self, params):
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Record.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4DelRule(AbstractModel):
    """删除l4规则接口

    """

    def __init__(self):
        """
        :param Id: 资源Id\n        :type Id: str\n        :param Ip: 资源IP\n        :type Ip: str\n        :param RuleIdList: 规则Id\n        :type RuleIdList: list of str\n        """
        self.Id = None
        self.Ip = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4HealthConfig(AbstractModel):
    """四层健康检查配置

    """

    def __init__(self):
        """
        :param Protocol: 转发协议，取值[TCP, UDP]\n        :type Protocol: str\n        :param VirtualPort: 转发端口\n        :type VirtualPort: int\n        :param Enable: =1表示开启；=0表示关闭\n        :type Enable: int\n        :param TimeOut: 响应超时时间，单位秒\n        :type TimeOut: int\n        :param Interval: 检测间隔时间，单位秒\n        :type Interval: int\n        :param KickNum: 不健康阈值，单位次\n        :type KickNum: int\n        :param AliveNum: 健康阈值，单位次\n        :type AliveNum: int\n        :param KeepTime: 会话保持时间，单位秒\n        :type KeepTime: int\n        """
        self.Protocol = None
        self.VirtualPort = None
        self.Enable = None
        self.TimeOut = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.KeepTime = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.Enable = params.get("Enable")
        self.TimeOut = params.get("TimeOut")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.KeepTime = params.get("KeepTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleEntry(AbstractModel):
    """L4规则

    """

    def __init__(self):
        """
        :param Protocol: 转发协议，取值[TCP, UDP]\n        :type Protocol: str\n        :param VirtualPort: 转发端口\n        :type VirtualPort: int\n        :param SourcePort: 源站端口\n        :type SourcePort: int\n        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]\n        :type SourceType: int\n        :param KeepTime: 会话保持时间，单位秒\n        :type KeepTime: int\n        :param SourceList: 回源列表\n        :type SourceList: list of L4RuleSource\n        :param LbType: 负载均衡方式，取值[1(加权轮询)，2(源IP hash)]\n        :type LbType: int\n        :param KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]；\n        :type KeepEnable: int\n        :param RuleId: 规则ID\n        :type RuleId: str\n        :param RuleName: 规则描述\n        :type RuleName: str\n        :param RemoveSwitch: 移除水印状态，取值[0(关闭)，1(开启)]\n        :type RemoveSwitch: int\n        """
        self.Protocol = None
        self.VirtualPort = None
        self.SourcePort = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.RuleName = None
        self.RemoveSwitch = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.SourcePort = params.get("SourcePort")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RemoveSwitch = params.get("RemoveSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleHealth(AbstractModel):
    """规则健康检查参数

    """

    def __init__(self):
        """
        :param RuleId: 规则ID\n        :type RuleId: str\n        :param Enable: =1表示开启；=0表示关闭\n        :type Enable: int\n        :param TimeOut: 响应超时时间，单位秒\n        :type TimeOut: int\n        :param Interval: 检测间隔时间，单位秒，必须要大于响应超时时间\n        :type Interval: int\n        :param KickNum: 不健康阈值，单位次\n        :type KickNum: int\n        :param AliveNum: 健康阈值，单位次\n        :type AliveNum: int\n        """
        self.RuleId = None
        self.Enable = None
        self.TimeOut = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Enable = params.get("Enable")
        self.TimeOut = params.get("TimeOut")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleSource(AbstractModel):
    """L4规则回源列表

    """

    def __init__(self):
        """
        :param Source: 回源IP或域名\n        :type Source: str\n        :param Weight: 权重值，取值[0,100]\n        :type Weight: int\n        """
        self.Source = None
        self.Weight = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7HealthConfig(AbstractModel):
    """七层健康检查配置

    """

    def __init__(self):
        """
        :param Protocol: 转发协议，取值[http, https, http/https]\n        :type Protocol: str\n        :param Domain: 转发域名\n        :type Domain: str\n        :param Enable: =1表示开启；=0表示关闭\n        :type Enable: int\n        :param Interval: 检测间隔时间，单位秒\n        :type Interval: int\n        :param KickNum: 异常判定次数，单位次\n        :type KickNum: int\n        :param AliveNum: 健康判定次数，单位次\n        :type AliveNum: int\n        :param Method: 健康检查探测方法，可选HEAD或GET，默认为HEAD\n        :type Method: str\n        :param StatusCode: 健康检查判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和\n        :type StatusCode: int\n        :param Url: 检查目录的URL，默认为/\n        :type Url: str\n        """
        self.Protocol = None
        self.Domain = None
        self.Enable = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.Method = None
        self.StatusCode = None
        self.Url = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.Enable = params.get("Enable")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        """
        :param Protocol: 转发协议，取值[http, https]\n        :type Protocol: str\n        :param Domain: 转发域名\n        :type Domain: str\n        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]\n        :type SourceType: int\n        :param KeepTime: 会话保持时间，单位秒\n        :type KeepTime: int\n        :param SourceList: 回源列表\n        :type SourceList: list of L4RuleSource\n        :param LbType: 负载均衡方式，取值[1(加权轮询)]\n        :type LbType: int\n        :param KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]\n        :type KeepEnable: int\n        :param RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；\n        :type RuleId: str\n        :param CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0\n        :type CertType: int\n        :param SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID\n        :type SSLId: str\n        :param Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)\n        :type Cert: str\n        :param PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)\n        :type PrivateKey: str\n        :param RuleName: 规则描述\n        :type RuleName: str\n        :param Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]\n        :type Status: int\n        :param CCStatus: cc防护状态，取值[0(关闭), 1(开启)]\n        :type CCStatus: int\n        :param CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]\n        :type CCEnable: int\n        :param CCThreshold: HTTPS协议的CC防护阈值\n        :type CCThreshold: int\n        :param CCLevel: HTTPS协议的CC防护等级\n        :type CCLevel: str\n        :param HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type HttpsToHttpEnable: int\n        :param VirtualPort: 接入端口值
注意：此字段可能返回 null，表示取不到有效值。\n        :type VirtualPort: int\n        """
        self.Protocol = None
        self.Domain = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None
        self.RuleName = None
        self.Status = None
        self.CCStatus = None
        self.CCEnable = None
        self.CCThreshold = None
        self.CCLevel = None
        self.HttpsToHttpEnable = None
        self.VirtualPort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.CCStatus = params.get("CCStatus")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.CCLevel = params.get("CCLevel")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self.VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleHealth(AbstractModel):
    """L7规则健康检查参数

    """

    def __init__(self):
        """
        :param RuleId: 规则ID\n        :type RuleId: str\n        :param Enable: =1表示开启；=0表示关闭\n        :type Enable: int\n        :param Interval: 检测间隔时间，单位秒\n        :type Interval: int\n        :param KickNum: 不健康阈值，单位次\n        :type KickNum: int\n        :param AliveNum: 健康阈值，单位次\n        :type AliveNum: int\n        :param Method: HTTP请求方式，取值[HEAD,GET]\n        :type Method: str\n        :param StatusCode: 健康检查判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和\n        :type StatusCode: int\n        :param Url: 检查目录的URL，默认为/\n        :type Url: str\n        :param Status: 配置状态，0： 正常，1：配置中，2：配置失败\n        :type Status: int\n        """
        self.RuleId = None
        self.Enable = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.Method = None
        self.StatusCode = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Enable = params.get("Enable")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdRequest(AbstractModel):
    """ModifyCCAlarmThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）\n        :type Business: str\n        :param RsId: 资源ID,字符串类型\n        :type RsId: str\n        :param AlarmThreshold: 告警阈值，大于0（目前排定的值），后台设置默认值为1000\n        :type AlarmThreshold: int\n        :param IpList: 资源关联的IP列表，高防包未绑定时，传空数组，高防IP专业版传多个IP的数据\n        :type IpList: list of str\n        """
        self.Business = None
        self.RsId = None
        self.AlarmThreshold = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdResponse(AbstractModel):
    """ModifyCCAlarmThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesRequest(AbstractModel):
    """ModifyCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param CCFrequencyRuleId: CC的访问频率控制规则ID\n        :type CCFrequencyRuleId: str\n        :param Mode: 匹配规则，取值["include"(前缀匹配)，"equal"(完全匹配)]\n        :type Mode: str\n        :param Period: 统计周期，单位秒，取值[10, 30, 60]\n        :type Period: int\n        :param ReqNumber: 访问次数，取值[1-10000]\n        :type ReqNumber: int\n        :param Act: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]\n        :type Act: str\n        :param ExeDuration: 执行时间，单位秒，取值[1-900]\n        :type ExeDuration: int\n        :param Uri: URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；\n        :type Uri: str\n        :param UserAgent: User-Agent字符串，长度不超过80\n        :type UserAgent: str\n        :param Cookie: Cookie字符串，长度不超过40\n        :type Cookie: str\n        """
        self.Business = None
        self.CCFrequencyRuleId = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesResponse(AbstractModel):
    """ModifyCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesStatusRequest(AbstractModel):
    """ModifyCCFrequencyRulesStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleId: 7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）\n        :type RuleId: str\n        :param Method: 开启或关闭，取值["on"(开启)，"off"(关闭)]\n        :type Method: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesStatusResponse(AbstractModel):
    """ModifyCCFrequencyRulesStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCHostProtectionRequest(AbstractModel):
    """ModifyCCHostProtection请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleId: 规则ID\n        :type RuleId: str\n        :param Method: 开启/关闭CC域名防护，取值[open(表示开启)，close(表示关闭)]\n        :type Method: str\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCHostProtectionResponse(AbstractModel):
    """ModifyCCHostProtection返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCIpAllowDenyRequest(AbstractModel):
    """ModifyCCIpAllowDeny请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Method: add表示添加，delete表示删除\n        :type Method: str\n        :param Type: 黑/白名单类型；取值[white(白名单)，black(黑名单)]\n        :type Type: str\n        :param IpList: 黑/白名单的IP数组\n        :type IpList: list of str\n        :param Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写Domain和RuleId字段；\n        :type Protocol: str\n        :param Domain: 可选字段，表示HTTPS协议的7层转发规则域名（通过获取7层转发规则接口可以获取域名），只有当Protocol字段为https时才必须填写此字段；\n        :type Domain: str\n        :param RuleId: 可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID），
当Method为delete时，不用填写此字段；\n        :type RuleId: str\n        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.Type = None
        self.IpList = None
        self.Protocol = None
        self.Domain = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.Type = params.get("Type")
        self.IpList = params.get("IpList")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCIpAllowDenyResponse(AbstractModel):
    """ModifyCCIpAllowDeny返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCLevelRequest(AbstractModel):
    """ModifyCCLevel请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Level: CC防护等级，取值[default(正常), loose(宽松), strict(严格)];\n        :type Level: str\n        :param Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写RuleId字段；\n        :type Protocol: str\n        :param RuleId: 表示7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；\n        :type RuleId: str\n        """
        self.Business = None
        self.Id = None
        self.Level = None
        self.Protocol = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Level = params.get("Level")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelResponse(AbstractModel):
    """ModifyCCLevel返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCPolicySwitchRequest(AbstractModel):
    """ModifyCCPolicySwitch请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param SetId: 策略ID\n        :type SetId: str\n        :param Switch: 开关状态\n        :type Switch: int\n        """
        self.Business = None
        self.Id = None
        self.SetId = None
        self.Switch = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPolicySwitchResponse(AbstractModel):
    """ModifyCCPolicySwitch返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCSelfDefinePolicyRequest(AbstractModel):
    """ModifyCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param SetId: 策略ID\n        :type SetId: str\n        :param Policy: CC策略描述\n        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`\n        """
        self.Business = None
        self.Id = None
        self.SetId = None
        self.Policy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        if params.get("Policy") is not None:
            self.Policy = CCPolicy()
            self.Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCSelfDefinePolicyResponse(AbstractModel):
    """ModifyCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCThresholdRequest(AbstractModel):
    """ModifyCCThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示基础防护）\n        :type Business: str\n        :param Threshold: CC防护阈值，取值(0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);
当Business为高防IP、高防IP专业版时，其CC防护最大阈值跟资源的保底防护带宽有关，对应关系如下：
  保底带宽: 最大C防护阈值
  10:  20000,
  20:  40000,
  30:  70000,
  40:  100000,
  50:  150000,
  60:  200000,
  80:  250000,
  100: 300000,\n        :type Threshold: int\n        :param Id: 资源ID\n        :type Id: str\n        :param Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写RuleId字段；\n        :type Protocol: str\n        :param RuleId: 可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；
当Protocol=https时必须填写；\n        :type RuleId: str\n        :param BasicIp: 查询的IP地址（仅基础防护提供），取值如：1.1.1.1\n        :type BasicIp: str\n        :param BasicRegion: 查询IP所属地域（仅基础防护提供），取值如：gz、bj、sh、hk等地域缩写\n        :type BasicRegion: str\n        :param BasicBizType: 专区类型（仅基础防护提供），取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。\n        :type BasicBizType: str\n        :param BasicDeviceType: 设备类型（仅基础防护提供），取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel.\n        :type BasicDeviceType: str\n        :param BasicIpInstance: 仅基础防护提供。可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）\n        :type BasicIpInstance: str\n        :param BasicIspCode: 仅基础防护提供。可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）\n        :type BasicIspCode: int\n        :param Domain: 可选字段，当协议取值HTTPS时，必填\n        :type Domain: str\n        """
        self.Business = None
        self.Threshold = None
        self.Id = None
        self.Protocol = None
        self.RuleId = None
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicIpInstance = None
        self.BasicIspCode = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Threshold = params.get("Threshold")
        self.Id = params.get("Id")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCThresholdResponse(AbstractModel):
    """ModifyCCThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCUrlAllowRequest(AbstractModel):
    """ModifyCCUrlAllow请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Method: =add表示添加，=delete表示删除\n        :type Method: str\n        :param Type: 黑/白名单类型；取值[white(白名单)]\n        :type Type: str\n        :param UrlList: URL数组，URL格式如下：
http://域名/cgi
https://域名/cgi\n        :type UrlList: list of str\n        :param Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写Domain和RuleId字段；\n        :type Protocol: str\n        :param Domain: 可选字段，表示HTTPS协议的7层转发规则域名（通过获取7层转发规则接口可以获取域名），只有当Protocol字段为https时才必须填写此字段；\n        :type Domain: str\n        :param RuleId: 可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID），当添加并且Protocol=https时必须填写；
当Method为delete时，可以不用填写此字段；\n        :type RuleId: str\n        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.Type = None
        self.UrlList = None
        self.Protocol = None
        self.Domain = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.Type = params.get("Type")
        self.UrlList = params.get("UrlList")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCUrlAllowResponse(AbstractModel):
    """ModifyCCUrlAllow返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSAIStatusRequest(AbstractModel):
    """ModifyDDoSAIStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Method: =get表示读取AI防护状态；=set表示修改AI防护状态；\n        :type Method: str\n        :param DDoSAI: AI防护状态，取值[on，off]；当Method=set时必填；\n        :type DDoSAI: str\n        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSAI = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSAI = params.get("DDoSAI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAIStatusResponse(AbstractModel):
    """ModifyDDoSAIStatus返回参数结构体

    """

    def __init__(self):
        """
        :param DDoSAI: AI防护状态，取值[on，off]\n        :type DDoSAI: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DDoSAI = None
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DDoSAI = params.get("DDoSAI")
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class ModifyDDoSAlarmThresholdRequest(AbstractModel):
    """ModifyDDoSAlarmThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）\n        :type Business: str\n        :param RsId: 资源ID,字符串类型\n        :type RsId: str\n        :param AlarmType: 告警阈值类型，0-未设置，1-入流量，2-清洗流量\n        :type AlarmType: int\n        :param AlarmThreshold: 告警阈值，大于0（目前暂定的值）\n        :type AlarmThreshold: int\n        :param IpList: 资源关联的IP列表，高防包未绑定时，传空数组，高防IP专业版传多个IP的数据\n        :type IpList: list of str\n        """
        self.Business = None
        self.RsId = None
        self.AlarmType = None
        self.AlarmThreshold = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAlarmThresholdResponse(AbstractModel):
    """ModifyDDoSAlarmThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSDefendStatusRequest(AbstractModel):
    """ModifyDDoSDefendStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版；basic表示基础防护）\n        :type Business: str\n        :param Status: 防护状态值，取值[0（关闭），1（开启）]\n        :type Status: int\n        :param Hour: 关闭时长，单位小时，取值[0，1，2，3，4，5，6]；当Status=0表示关闭时，Hour必须大于0；\n        :type Hour: int\n        :param Id: 资源ID；当Business不是基础防护时必须填写此字段；\n        :type Id: str\n        :param Ip: 基础防护的IP，只有当Business为基础防护时才需要填写此字段；\n        :type Ip: str\n        :param BizType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]\n        :type BizType: str\n        :param DeviceType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]\n        :type DeviceType: str\n        :param InstanceId: 只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);\n        :type InstanceId: str\n        :param IPRegion: 只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：
"bj":     华北地区(北京)
"cd":     西南地区(成都)
"cq":     西南地区(重庆)
"gz":     华南地区(广州)
"gzopen": 华南地区(广州Open)
"hk":     中国香港
"kr":     东南亚地区(首尔)
"sh":     华东地区(上海)
"shjr":   华东地区(上海金融)
"szjr":   华南地区(深圳金融)
"sg":     东南亚地区(新加坡)
"th":     东南亚地区(泰国)
"de":     欧洲地区(德国)
"usw":    美国西部（硅谷）
"ca":     北美地区(多伦多)
"jp":     日本
"hzec":   杭州
"in":     印度
"use":    美东地区（弗吉尼亚）
"ru":     俄罗斯
"tpe":    中国台湾
"nj":     南京\n        :type IPRegion: str\n        """
        self.Business = None
        self.Status = None
        self.Hour = None
        self.Id = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Status = params.get("Status")
        self.Hour = params.get("Hour")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSDefendStatusResponse(AbstractModel):
    """ModifyDDoSDefendStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSLevelRequest(AbstractModel):
    """ModifyDDoSLevel请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Method: =get表示读取防护等级；=set表示修改防护等级\n        :type Method: str\n        :param DDoSLevel: 防护等级，取值[low,middle,high]；当Method=set时必填\n        :type DDoSLevel: str\n        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSLevel = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSLevel = params.get("DDoSLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 资源ID\n        :type Id: str\n        :param DDoSLevel: 防护等级，取值[low,middle,high]\n        :type DDoSLevel: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Id = None
        self.DDoSLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DDoSLevel = params.get("DDoSLevel")
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyCaseRequest(AbstractModel):
    """ModifyDDoSPolicyCase请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param SceneId: 策略场景ID\n        :type SceneId: str\n        :param PlatformTypes: 开发平台，取值[PC（PC客户端）， MOBILE（移动端）， TV（电视端）， SERVER（主机）]\n        :type PlatformTypes: list of str\n        :param AppType: 细分品类，取值[WEB（网站）， GAME（游戏）， APP（应用）， OTHER（其他）]\n        :type AppType: str\n        :param AppProtocols: 应用协议，取值[tcp（TCP协议），udp（UDP协议），icmp（ICMP协议），all（其他协议）]\n        :type AppProtocols: list of str\n        :param TcpSportStart: TCP业务起始端口，取值(0, 65535]\n        :type TcpSportStart: str\n        :param TcpSportEnd: TCP业务结束端口，取值(0, 65535]，必须大于等于TCP业务起始端口\n        :type TcpSportEnd: str\n        :param UdpSportStart: UDP业务起始端口，取值范围(0, 65535]\n        :type UdpSportStart: str\n        :param UdpSportEnd: UDP业务结束端口，取值范围(0, 65535)，必须大于等于UDP业务起始端口\n        :type UdpSportEnd: str\n        :param HasAbroad: 是否有海外客户，取值[no（没有）, yes（有）]\n        :type HasAbroad: str\n        :param HasInitiateTcp: 是否会主动对外发起TCP请求，取值[no（不会）, yes（会）]\n        :type HasInitiateTcp: str\n        :param HasInitiateUdp: 是否会主动对外发起UDP业务请求，取值[no（不会）, yes（会）]\n        :type HasInitiateUdp: str\n        :param PeerTcpPort: 主动发起TCP请求的端口，取值范围(0, 65535]\n        :type PeerTcpPort: str\n        :param PeerUdpPort: 主动发起UDP请求的端口，取值范围(0, 65535]\n        :type PeerUdpPort: str\n        :param TcpFootprint: TCP载荷的固定特征码，字符串长度小于512\n        :type TcpFootprint: str\n        :param UdpFootprint: UDP载荷的固定特征码，字符串长度小于512\n        :type UdpFootprint: str\n        :param WebApiUrl: Web业务的API的URL\n        :type WebApiUrl: list of str\n        :param MinTcpPackageLen: TCP业务报文长度最小值，取值范围(0, 1500)\n        :type MinTcpPackageLen: str\n        :param MaxTcpPackageLen: TCP业务报文长度最大值，取值范围(0, 1500)，必须大于等于TCP业务报文长度最小值\n        :type MaxTcpPackageLen: str\n        :param MinUdpPackageLen: UDP业务报文长度最小值，取值范围(0, 1500)\n        :type MinUdpPackageLen: str\n        :param MaxUdpPackageLen: UDP业务报文长度最大值，取值范围(0, 1500)，必须大于等于UDP业务报文长度最小值\n        :type MaxUdpPackageLen: str\n        :param HasVPN: 是否有VPN业务，取值[no（没有）, yes（有）]\n        :type HasVPN: str\n        :param TcpPortList: TCP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000\n        :type TcpPortList: str\n        :param UdpPortList: UDP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000\n        :type UdpPortList: str\n        """
        self.Business = None
        self.SceneId = None
        self.PlatformTypes = None
        self.AppType = None
        self.AppProtocols = None
        self.TcpSportStart = None
        self.TcpSportEnd = None
        self.UdpSportStart = None
        self.UdpSportEnd = None
        self.HasAbroad = None
        self.HasInitiateTcp = None
        self.HasInitiateUdp = None
        self.PeerTcpPort = None
        self.PeerUdpPort = None
        self.TcpFootprint = None
        self.UdpFootprint = None
        self.WebApiUrl = None
        self.MinTcpPackageLen = None
        self.MaxTcpPackageLen = None
        self.MinUdpPackageLen = None
        self.MaxUdpPackageLen = None
        self.HasVPN = None
        self.TcpPortList = None
        self.UdpPortList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")
        self.PlatformTypes = params.get("PlatformTypes")
        self.AppType = params.get("AppType")
        self.AppProtocols = params.get("AppProtocols")
        self.TcpSportStart = params.get("TcpSportStart")
        self.TcpSportEnd = params.get("TcpSportEnd")
        self.UdpSportStart = params.get("UdpSportStart")
        self.UdpSportEnd = params.get("UdpSportEnd")
        self.HasAbroad = params.get("HasAbroad")
        self.HasInitiateTcp = params.get("HasInitiateTcp")
        self.HasInitiateUdp = params.get("HasInitiateUdp")
        self.PeerTcpPort = params.get("PeerTcpPort")
        self.PeerUdpPort = params.get("PeerUdpPort")
        self.TcpFootprint = params.get("TcpFootprint")
        self.UdpFootprint = params.get("UdpFootprint")
        self.WebApiUrl = params.get("WebApiUrl")
        self.MinTcpPackageLen = params.get("MinTcpPackageLen")
        self.MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self.MinUdpPackageLen = params.get("MinUdpPackageLen")
        self.MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self.HasVPN = params.get("HasVPN")
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyCaseResponse(AbstractModel):
    """ModifyDDoSPolicyCase返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyNameRequest(AbstractModel):
    """ModifyDDoSPolicyName请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param PolicyId: 策略ID\n        :type PolicyId: str\n        :param Name: 策略名称\n        :type Name: str\n        """
        self.Business = None
        self.PolicyId = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyNameResponse(AbstractModel):
    """ModifyDDoSPolicyName返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param PolicyId: 策略ID\n        :type PolicyId: str\n        :param DropOptions: 协议禁用，必须填写且数组长度必须为1\n        :type DropOptions: list of DDoSPolicyDropOption\n        :param PortLimits: 端口禁用，当没有禁用端口时填空数组\n        :type PortLimits: list of DDoSPolicyPortLimit\n        :param IpAllowDenys: IP黑白名单，当没有IP黑白名单时填空数组\n        :type IpAllowDenys: list of IpBlackWhite\n        :param PacketFilters: 报文过滤，当没有报文过滤时填空数组\n        :type PacketFilters: list of DDoSPolicyPacketFilter\n        :param WaterPrint: 水印策略参数，当没有启用水印功能时填空数组，最多只能传一条水印策略（即数组大小不超过1）\n        :type WaterPrint: list of WaterPrintPolicy\n        """
        self.Business = None
        self.PolicyId = None
        self.DropOptions = None
        self.PortLimits = None
        self.IpAllowDenys = None
        self.PacketFilters = None
        self.WaterPrint = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        if params.get("DropOptions") is not None:
            self.DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self.DropOptions.append(obj)
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self.IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)
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
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSSwitchRequest(AbstractModel):
    """ModifyDDoSSwitch请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（basic表示基础防护）\n        :type Business: str\n        :param Method: =get表示读取DDoS防护状态；=set表示修改DDoS防护状态；\n        :type Method: str\n        :param Ip: 基础防护的IP，只有当Business为基础防护时才需要填写此字段；\n        :type Ip: str\n        :param BizType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]\n        :type BizType: str\n        :param DeviceType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]\n        :type DeviceType: str\n        :param InstanceId: 只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);\n        :type InstanceId: str\n        :param IPRegion: 只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：
"bj":     华北地区(北京)
"cd":     西南地区(成都)
"cq":     西南地区(重庆)
"gz":     华南地区(广州)
"gzopen": 华南地区(广州Open)
"hk":     中国香港
"kr":     东南亚地区(首尔)
"sh":     华东地区(上海)
"shjr":   华东地区(上海金融)
"szjr":   华南地区(深圳金融)
"sg":     东南亚地区(新加坡)
"th":     东南亚地区(泰国)
"de":     欧洲地区(德国)
"usw":    美国西部（硅谷）
"ca":     北美地区(多伦多)
"jp":     日本
"hzec":   杭州
"in":     印度
"use":    美东地区（弗吉尼亚）
"ru":     俄罗斯
"tpe":    中国台湾
"nj":     南京\n        :type IPRegion: str\n        :param Status: 可选字段，防护状态值，取值[0（关闭），1（开启）]；当Method为get时可以不填写此字段；\n        :type Status: int\n        """
        self.Business = None
        self.Method = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None
        self.Status = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSSwitchResponse(AbstractModel):
    """ModifyDDoSSwitch返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 当前防护状态值，取值[0（关闭），1（开启）]\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyDDoSThresholdRequest(AbstractModel):
    """ModifyDDoSThreshold请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Threshold: DDoS清洗阈值，取值[0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
当设置值为0时，表示采用默认值；\n        :type Threshold: int\n        """
        self.Business = None
        self.Id = None
        self.Threshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSWaterKeyRequest(AbstractModel):
    """ModifyDDoSWaterKey请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param PolicyId: 策略ID\n        :type PolicyId: str\n        :param Method: 密钥操作，取值：[add（添加），delete（删除），open（开启），close（关闭），get（获取密钥）]\n        :type Method: str\n        :param KeyId: 密钥ID，当添加密钥操作时可以不填或填0，其他操作时必须填写；\n        :type KeyId: int\n        """
        self.Business = None
        self.PolicyId = None
        self.Method = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSWaterKeyResponse(AbstractModel):
    """ModifyDDoSWaterKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyList: 水印密钥列表\n        :type KeyList: list of WaterPrintKey\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyList") is not None:
            self.KeyList = []
            for item in params.get("KeyList"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self.KeyList.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyElasticLimitRequest(AbstractModel):
    """ModifyElasticLimit请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Limit: 弹性防护阈值，取值[0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]\n        :type Limit: int\n        """
        self.Business = None
        self.Id = None
        self.Limit = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyElasticLimitResponse(AbstractModel):
    """ModifyElasticLimit返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4HealthRequest(AbstractModel):
    """ModifyL4Health请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Healths: 健康检查参数数组\n        :type Healths: list of L4RuleHealth\n        """
        self.Business = None
        self.Id = None
        self.Healths = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4HealthResponse(AbstractModel):
    """ModifyL4Health返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4KeepTimeRequest(AbstractModel):
    """ModifyL4KeepTime请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param RuleId: 规则ID\n        :type RuleId: str\n        :param KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]\n        :type KeepEnable: int\n        :param KeepTime: 会话保持时间，单位秒\n        :type KeepTime: int\n        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.KeepEnable = None
        self.KeepTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.KeepEnable = params.get("KeepEnable")
        self.KeepTime = params.get("KeepTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4KeepTimeResponse(AbstractModel):
    """ModifyL4KeepTime返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4RulesRequest(AbstractModel):
    """ModifyL4Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Rule: 规则\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L4RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4RulesResponse(AbstractModel):
    """ModifyL4Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL7RulesRequest(AbstractModel):
    """ModifyL7Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Rule: 规则\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L7RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7RulesResponse(AbstractModel):
    """ModifyL7Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyNetReturnSwitchRequest(AbstractModel):
    """ModifyNetReturnSwitch请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源实例ID\n        :type Id: str\n        :param Status: Status 表示回切开关，0: 关闭， 1:打开\n        :type Status: int\n        :param Hour: 回切时长，单位：小时，取值[0,1,2,3,4,5,6;]当status=1时必选填写Hour>0\n        :type Hour: int\n        """
        self.Business = None
        self.Id = None
        self.Status = None
        self.Hour = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Hour = params.get("Hour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetReturnSwitchResponse(AbstractModel):
    """ModifyNetReturnSwitch返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNewDomainRulesRequest(AbstractModel):
    """ModifyNewDomainRules请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Rule: 域名转发规则\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.NewL7RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = NewL7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewDomainRulesResponse(AbstractModel):
    """ModifyNewDomainRules返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyNewL4RuleRequest(AbstractModel):
    """ModifyNewL4Rule请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param Rule: 转发规则\n        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`\n        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L4RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewL4RuleResponse(AbstractModel):
    """ModifyNewL4Rule返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyResBindDDoSPolicyRequest(AbstractModel):
    """ModifyResBindDDoSPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）\n        :type Business: str\n        :param Id: 资源ID\n        :type Id: str\n        :param PolicyId: 策略ID\n        :type PolicyId: str\n        :param Method: 绑定或解绑，bind表示绑定策略，unbind表示解绑策略\n        :type Method: str\n        """
        self.Business = None
        self.Id = None
        self.PolicyId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResBindDDoSPolicyResponse(AbstractModel):
    """ModifyResBindDDoSPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyResourceRenewFlagRequest(AbstractModel):
    """ModifyResourceRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版；shield表示棋牌盾；bgp表示独享包；bgp-multip表示共享包；insurance表示保险包；staticpack表示三网套餐包）\n        :type Business: str\n        :param Id: 资源Id\n        :type Id: str\n        :param RenewFlag: 自动续费标记（0手动续费；1自动续费；2到期不续费）\n        :type RenewFlag: int\n        """
        self.Business = None
        self.Id = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceRenewFlagResponse(AbstractModel):
    """ModifyResourceRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param Success: 成功码\n        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class NewL4RuleEntry(AbstractModel):
    """四层规则结构体

    """

    def __init__(self):
        """
        :param Protocol: 转发协议，取值[TCP, UDP]\n        :type Protocol: str\n        :param VirtualPort: 转发端口\n        :type VirtualPort: int\n        :param SourcePort: 源站端口\n        :type SourcePort: int\n        :param KeepTime: 会话保持时间，单位秒\n        :type KeepTime: int\n        :param SourceList: 回源列表\n        :type SourceList: list of L4RuleSource\n        :param LbType: 负载均衡方式，取值[1(加权轮询)，2(源IP hash)]\n        :type LbType: int\n        :param KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]；\n        :type KeepEnable: int\n        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]\n        :type SourceType: int\n        :param RuleId: 规则ID\n        :type RuleId: str\n        :param RuleName: 规则描述\n        :type RuleName: str\n        :param RemoveSwitch: 移除水印状态，取值[0(关闭)，1(开启)]\n        :type RemoveSwitch: int\n        :param ModifyTime: 规则修改时间\n        :type ModifyTime: str\n        :param Region: 对应地区信息\n        :type Region: int\n        :param Ip: 绑定资源IP信息\n        :type Ip: str\n        :param Id: 绑定资源Id信息\n        :type Id: str\n        """
        self.Protocol = None
        self.VirtualPort = None
        self.SourcePort = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.SourceType = None
        self.RuleId = None
        self.RuleName = None
        self.RemoveSwitch = None
        self.ModifyTime = None
        self.Region = None
        self.Ip = None
        self.Id = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.SourcePort = params.get("SourcePort")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.SourceType = params.get("SourceType")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RemoveSwitch = params.get("RemoveSwitch")
        self.ModifyTime = params.get("ModifyTime")
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewL7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        """
        :param Protocol: 转发协议，取值[http, https]\n        :type Protocol: str\n        :param Domain: 转发域名\n        :type Domain: str\n        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]\n        :type SourceType: int\n        :param KeepTime: 会话保持时间，单位秒\n        :type KeepTime: int\n        :param SourceList: 回源列表\n        :type SourceList: list of L4RuleSource\n        :param LbType: 负载均衡方式，取值[1(加权轮询)]\n        :type LbType: int\n        :param KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]\n        :type KeepEnable: int\n        :param RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；\n        :type RuleId: str\n        :param CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0\n        :type CertType: int\n        :param SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID\n        :type SSLId: str\n        :param Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)\n        :type Cert: str\n        :param PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)\n        :type PrivateKey: str\n        :param RuleName: 规则描述\n        :type RuleName: str\n        :param Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]\n        :type Status: int\n        :param CCStatus: cc防护状态，取值[0(关闭), 1(开启)]\n        :type CCStatus: int\n        :param CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]\n        :type CCEnable: int\n        :param CCThreshold: HTTPS协议的CC防护阈值\n        :type CCThreshold: int\n        :param CCLevel: HTTPS协议的CC防护等级\n        :type CCLevel: str\n        :param Region: 区域码\n        :type Region: int\n        :param Id: 资源Id\n        :type Id: str\n        :param Ip: 资源Ip\n        :type Ip: str\n        :param ModifyTime: 修改时间\n        :type ModifyTime: str\n        :param HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭\n        :type HttpsToHttpEnable: int\n        :param VirtualPort: 接入端口值
注意：此字段可能返回 null，表示取不到有效值。\n        :type VirtualPort: int\n        """
        self.Protocol = None
        self.Domain = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None
        self.RuleName = None
        self.Status = None
        self.CCStatus = None
        self.CCEnable = None
        self.CCThreshold = None
        self.CCLevel = None
        self.Region = None
        self.Id = None
        self.Ip = None
        self.ModifyTime = None
        self.HttpsToHttpEnable = None
        self.VirtualPort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.CCStatus = params.get("CCStatus")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.CCLevel = params.get("CCLevel")
        self.Region = params.get("Region")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.ModifyTime = params.get("ModifyTime")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self.VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderBy(AbstractModel):
    """排序字段

    """

    def __init__(self):
        """
        :param Field: 排序字段名称，取值[
bandwidth（带宽），
overloadCount（超峰值次数）
]\n        :type Field: str\n        :param Order: 升降序，取值为[asc（升序），（升序），desc（降序）， DESC（降序）]\n        :type Order: str\n        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """分页索引

    """

    def __init__(self):
        """
        :param Offset: 起始位置\n        :type Offset: int\n        :param Limit: 数量\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolPort(AbstractModel):
    """Protocol、Port参数

    """

    def __init__(self):
        """
        :param Protocol: 协议（tcp；udp）\n        :type Protocol: str\n        :param Port: 端口\n        :type Port: int\n        """
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstanceCount(AbstractModel):
    """地域资源实例数

    """

    def __init__(self):
        """
        :param Region: 地域码\n        :type Region: str\n        :param RegionV3: 地域码（新规范）\n        :type RegionV3: str\n        :param Count: 资源实例数\n        :type Count: int\n        """
        self.Region = None
        self.RegionV3 = None
        self.Count = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionV3 = params.get("RegionV3")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIp(AbstractModel):
    """资源的IP数组

    """

    def __init__(self):
        """
        :param Id: 资源ID\n        :type Id: str\n        :param IpList: 资源的IP数组\n        :type IpList: list of str\n        """
        self.Id = None
        self.IpList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingDomain(AbstractModel):
    """调度域名信息

    """

    def __init__(self):
        """
        :param Domain: 调度域名\n        :type Domain: str\n        :param BGPIpList: BGP线路IP列表\n        :type BGPIpList: list of str\n        :param CTCCIpList: 电信线路IP列表\n        :type CTCCIpList: list of str\n        :param CUCCIpList: 联通线路IP列表\n        :type CUCCIpList: list of str\n        :param CMCCIpList: 移动线路IP列表\n        :type CMCCIpList: list of str\n        :param OverseaIpList: 海外线路IP列表\n        :type OverseaIpList: list of str\n        :param Method: 调度方式，当前仅支持优先级, 取值为priority\n        :type Method: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param TTL: ttl\n        :type TTL: int\n        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifyTime: str\n        """
        self.Domain = None
        self.BGPIpList = None
        self.CTCCIpList = None
        self.CUCCIpList = None
        self.CMCCIpList = None
        self.OverseaIpList = None
        self.Method = None
        self.CreateTime = None
        self.TTL = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.BGPIpList = params.get("BGPIpList")
        self.CTCCIpList = params.get("CTCCIpList")
        self.CUCCIpList = params.get("CUCCIpList")
        self.CMCCIpList = params.get("CMCCIpList")
        self.OverseaIpList = params.get("OverseaIpList")
        self.Method = params.get("Method")
        self.CreateTime = params.get("CreateTime")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCode(AbstractModel):
    """操作返回码，只用于返回成功的情况

    """

    def __init__(self):
        """
        :param Code: 成功/错误码\n        :type Code: str\n        :param Message: 描述\n        :type Message: str\n        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintKey(AbstractModel):
    """水印Key

    """

    def __init__(self):
        """
        :param KeyId: 水印KeyID\n        :type KeyId: str\n        :param KeyContent: 水印Key值\n        :type KeyContent: str\n        :param KeyVersion: 水印Key的版本号\n        :type KeyVersion: str\n        :param OpenStatus: 是否开启，取值[0（没有开启），1（已开启）]\n        :type OpenStatus: int\n        :param CreateTime: 密钥生成时间\n        :type CreateTime: str\n        """
        self.KeyId = None
        self.KeyContent = None
        self.KeyVersion = None
        self.OpenStatus = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyContent = params.get("KeyContent")
        self.KeyVersion = params.get("KeyVersion")
        self.OpenStatus = params.get("OpenStatus")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintPolicy(AbstractModel):
    """水印策略参数

    """

    def __init__(self):
        """
        :param TcpPortList: TCP端口段，例如["2000-3000","3500-4000"]\n        :type TcpPortList: list of str\n        :param UdpPortList: UDP端口段，例如["2000-3000","3500-4000"]\n        :type UdpPortList: list of str\n        :param Offset: 水印偏移量，取值范围[0, 100)\n        :type Offset: int\n        :param RemoveSwitch: 是否自动剥离，取值[0（不自动剥离），1（自动剥离）]\n        :type RemoveSwitch: int\n        :param OpenStatus: 是否开启，取值[0（没有开启），1（已开启）]\n        :type OpenStatus: int\n        """
        self.TcpPortList = None
        self.UdpPortList = None
        self.Offset = None
        self.RemoveSwitch = None
        self.OpenStatus = None


    def _deserialize(self, params):
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")
        self.Offset = params.get("Offset")
        self.RemoveSwitch = params.get("RemoveSwitch")
        self.OpenStatus = params.get("OpenStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        