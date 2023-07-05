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
        r"""
        :param _MetricName: 指标名（connum表示TCP活跃连接数；
new_conn表示新建TCP连接数；
inactive_conn表示非活跃连接数;
intraffic表示入流量；
outtraffic表示出流量；
alltraffic表示出流量和入流量之和；
inpkg表示入包速率；
outpkg表示出包速率；）
        :type MetricName: str
        :param _Data: 值数组
        :type Data: list of float
        :param _Count: 值数组的大小
        :type Count: int
        """
        self._MetricName = None
        self._Data = None
        self._Count = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundIpInfo(AbstractModel):
    """高防包绑定IP对象

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _BizType: 绑定的产品分类，取值[public（CVM、CLB产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]
        :type BizType: str
        :param _DeviceType: 产品分类下的子类型，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]
        :type DeviceType: str
        :param _InstanceId: IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*); 如果绑定的是托管IP没有对应的资源实例ID，请填写"none";
        :type InstanceId: str
        :param _IspCode: 运营商，0：电信；1：联通；2：移动；5：BGP
        :type IspCode: int
        """
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._IspCode = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IspCode(self):
        return self._IspCode

    @IspCode.setter
    def IspCode(self, IspCode):
        self._IspCode = IspCode


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._IspCode = params.get("IspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCAlarmThreshold(AbstractModel):
    """CC告警阈值

    """

    def __init__(self):
        r"""
        :param _AlarmThreshold: CC告警阈值
        :type AlarmThreshold: int
        """
        self._AlarmThreshold = None

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold


    def _deserialize(self, params):
        self._AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCEventRecord(AbstractModel):
    """CC攻击事件记录

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Vip: 资源的IP
        :type Vip: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        :param _ReqQps: 总请求QPS峰值
        :type ReqQps: int
        :param _DropQps: 攻击QPS峰值
        :type DropQps: int
        :param _AttackStatus: 攻击状态，取值[0（攻击中）, 1（攻击结束）]
        :type AttackStatus: int
        :param _ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _DomainList: 域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: str
        :param _UriList: uri列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UriList: str
        :param _AttackipList: 攻击源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackipList: str
        """
        self._Business = None
        self._Id = None
        self._Vip = None
        self._StartTime = None
        self._EndTime = None
        self._ReqQps = None
        self._DropQps = None
        self._AttackStatus = None
        self._ResourceName = None
        self._DomainList = None
        self._UriList = None
        self._AttackipList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

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
    def ReqQps(self):
        return self._ReqQps

    @ReqQps.setter
    def ReqQps(self, ReqQps):
        self._ReqQps = ReqQps

    @property
    def DropQps(self):
        return self._DropQps

    @DropQps.setter
    def DropQps(self, DropQps):
        self._DropQps = DropQps

    @property
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def UriList(self):
        return self._UriList

    @UriList.setter
    def UriList(self, UriList):
        self._UriList = UriList

    @property
    def AttackipList(self):
        return self._AttackipList

    @AttackipList.setter
    def AttackipList(self, AttackipList):
        self._AttackipList = AttackipList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReqQps = params.get("ReqQps")
        self._DropQps = params.get("DropQps")
        self._AttackStatus = params.get("AttackStatus")
        self._ResourceName = params.get("ResourceName")
        self._DomainList = params.get("DomainList")
        self._UriList = params.get("UriList")
        self._AttackipList = params.get("AttackipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCFrequencyRule(AbstractModel):
    """CC的访问频率控制规则

    """

    def __init__(self):
        r"""
        :param _CCFrequencyRuleId: CC的访问频率控制规则ID
        :type CCFrequencyRuleId: str
        :param _Uri: URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；
        :type Uri: str
        :param _UserAgent: User-Agent字符串，长度不超过80
        :type UserAgent: str
        :param _Cookie: Cookie字符串，长度不超过40
        :type Cookie: str
        :param _Mode: 匹配规则，取值["include"(前缀匹配)，"equal"(完全匹配)]
        :type Mode: str
        :param _Period: 统计周期，单位秒，取值[10, 30, 60]
        :type Period: int
        :param _ReqNumber: 访问次数，取值[1-10000]
        :type ReqNumber: int
        :param _Act: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]
        :type Act: str
        :param _ExeDuration: 执行时间，单位秒，取值[1-900]
        :type ExeDuration: int
        """
        self._CCFrequencyRuleId = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None
        self._Mode = None
        self._Period = None
        self._ReqNumber = None
        self._Act = None
        self._ExeDuration = None

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Cookie(self):
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Act(self):
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration


    def _deserialize(self, params):
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self._Uri = params.get("Uri")
        self._UserAgent = params.get("UserAgent")
        self._Cookie = params.get("Cookie")
        self._Mode = params.get("Mode")
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Act = params.get("Act")
        self._ExeDuration = params.get("ExeDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPolicy(AbstractModel):
    """cc自定义规则

    """

    def __init__(self):
        r"""
        :param _Name: 策略名称
        :type Name: str
        :param _Smode: 匹配模式，取值[matching(匹配模式), speedlimit(限速模式)]
        :type Smode: str
        :param _SetId: 策略id
        :type SetId: str
        :param _Frequency: 每分钟限制的次数
        :type Frequency: int
        :param _ExeMode: 执行策略模式，拦截或者验证码，取值[alg（验证码）, drop（拦截）]
        :type ExeMode: str
        :param _Switch: 生效开关
        :type Switch: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _RuleList: 规则列表
        :type RuleList: list of CCRule
        :param _IpList: IP列表，如果不填时，请传空数组但不能为null；
        :type IpList: list of str
        :param _Protocol: cc防护类型，取值[http，https]
        :type Protocol: str
        :param _RuleId: 可选字段，表示HTTPS的CC防护域名对应的转发规则ID;
        :type RuleId: str
        :param _Domain: HTTPS的CC防护域名
        :type Domain: str
        """
        self._Name = None
        self._Smode = None
        self._SetId = None
        self._Frequency = None
        self._ExeMode = None
        self._Switch = None
        self._CreateTime = None
        self._RuleList = None
        self._IpList = None
        self._Protocol = None
        self._RuleId = None
        self._Domain = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Smode(self):
        return self._Smode

    @Smode.setter
    def Smode(self, Smode):
        self._Smode = Smode

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Frequency(self):
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def ExeMode(self):
        return self._ExeMode

    @ExeMode.setter
    def ExeMode(self, ExeMode):
        self._ExeMode = ExeMode

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RuleList(self):
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Smode = params.get("Smode")
        self._SetId = params.get("SetId")
        self._Frequency = params.get("Frequency")
        self._ExeMode = params.get("ExeMode")
        self._Switch = params.get("Switch")
        self._CreateTime = params.get("CreateTime")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = CCRule()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._IpList = params.get("IpList")
        self._Protocol = params.get("Protocol")
        self._RuleId = params.get("RuleId")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRule(AbstractModel):
    """cc自定义策略配置的规则

    """

    def __init__(self):
        r"""
        :param _Skey: 规则的key, 可以为host、cgi、ua、referer
        :type Skey: str
        :param _Operator: 规则的条件，可以为include、not_include、equal
        :type Operator: str
        :param _Value: 规则的值，长度小于31字节
        :type Value: str
        """
        self._Skey = None
        self._Operator = None
        self._Value = None

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

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
        self._Skey = params.get("Skey")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCRuleConfig(AbstractModel):
    """7层CC自定义规则

    """

    def __init__(self):
        r"""
        :param _Period: 统计周期，单位秒，取值[10, 30, 60]
        :type Period: int
        :param _ReqNumber: 访问次数，取值[1-10000]
        :type ReqNumber: int
        :param _Action: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]
        :type Action: str
        :param _ExeDuration: 执行时间，单位秒，取值[1-900]
        :type ExeDuration: int
        """
        self._Period = None
        self._ReqNumber = None
        self._Action = None
        self._ExeDuration = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Action = params.get("Action")
        self._ExeDuration = params.get("ExeDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdRequest(AbstractModel):
    """CreateBasicDDoSAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（basic表示DDoS基础防护）
        :type Business: str
        :param _Method: =get表示读取告警阈值；=set表示设置告警阈值；
        :type Method: str
        :param _AlarmType: 可选，告警阈值类型，1-入流量，2-清洗流量；当Method为set时必须填写；
        :type AlarmType: int
        :param _AlarmThreshold: 可选，告警阈值，当Method为set时必须填写；当设置阈值为0时表示清除告警阈值配置；
        :type AlarmThreshold: int
        """
        self._Business = None
        self._Method = None
        self._AlarmType = None
        self._AlarmThreshold = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Method = params.get("Method")
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicDDoSAlarmThresholdResponse(AbstractModel):
    """CreateBasicDDoSAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmThreshold: 当存在告警阈值配置时，返回告警阈值大于0，当不存在告警配置时，返回告警阈值为0；
        :type AlarmThreshold: int
        :param _AlarmType: 告警阈值类型，1-入流量，2-清洗流量；当AlarmThreshold大于0时有效；
        :type AlarmType: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmThreshold = None
        self._AlarmType = None
        self._RequestId = None

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AlarmThreshold = params.get("AlarmThreshold")
        self._AlarmType = params.get("AlarmType")
        self._RequestId = params.get("RequestId")


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _BoundDevList: 绑定到资源实例的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要绑定的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :type BoundDevList: list of BoundIpInfo
        :param _UnBoundDevList: 与资源实例解绑的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要解绑的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :type UnBoundDevList: list of BoundIpInfo
        :param _CopyPolicy: 已弃用，不填
        :type CopyPolicy: str
        """
        self._Business = None
        self._Id = None
        self._BoundDevList = None
        self._UnBoundDevList = None
        self._CopyPolicy = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BoundDevList(self):
        return self._BoundDevList

    @BoundDevList.setter
    def BoundDevList(self, BoundDevList):
        self._BoundDevList = BoundDevList

    @property
    def UnBoundDevList(self):
        return self._UnBoundDevList

    @UnBoundDevList.setter
    def UnBoundDevList(self, UnBoundDevList):
        self._UnBoundDevList = UnBoundDevList

    @property
    def CopyPolicy(self):
        return self._CopyPolicy

    @CopyPolicy.setter
    def CopyPolicy(self, CopyPolicy):
        self._CopyPolicy = CopyPolicy


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("BoundDevList") is not None:
            self._BoundDevList = []
            for item in params.get("BoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self._BoundDevList.append(obj)
        if params.get("UnBoundDevList") is not None:
            self._UnBoundDevList = []
            for item in params.get("UnBoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self._UnBoundDevList.append(obj)
        self._CopyPolicy = params.get("CopyPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateCCFrequencyRulesRequest(AbstractModel):
    """CreateCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleId: 7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）
        :type RuleId: str
        :param _Mode: 匹配规则，取值["include"(前缀匹配)，"equal"(完全匹配)]
        :type Mode: str
        :param _Period: 统计周期，单位秒，取值[10, 30, 60]
        :type Period: int
        :param _ReqNumber: 访问次数，取值[1-10000]
        :type ReqNumber: int
        :param _Act: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]
        :type Act: str
        :param _ExeDuration: 执行时间，单位秒，取值[1-900]
        :type ExeDuration: int
        :param _Uri: URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；
        :type Uri: str
        :param _UserAgent: User-Agent字符串，长度不超过80
        :type UserAgent: str
        :param _Cookie: Cookie字符串，长度不超过40
        :type Cookie: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._Mode = None
        self._Period = None
        self._ReqNumber = None
        self._Act = None
        self._ExeDuration = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Act(self):
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Cookie(self):
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._Mode = params.get("Mode")
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Act = params.get("Act")
        self._ExeDuration = params.get("ExeDuration")
        self._Uri = params.get("Uri")
        self._UserAgent = params.get("UserAgent")
        self._Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCFrequencyRulesResponse(AbstractModel):
    """CreateCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CCFrequencyRuleId: CC防护的访问频率控制规则ID
        :type CCFrequencyRuleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CCFrequencyRuleId = None
        self._RequestId = None

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self._RequestId = params.get("RequestId")


class CreateCCSelfDefinePolicyRequest(AbstractModel):
    """CreateCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Policy: CC策略描述
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self._Business = None
        self._Id = None
        self._Policy = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Policy") is not None:
            self._Policy = CCPolicy()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCSelfDefinePolicyResponse(AbstractModel):
    """CreateCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateDDoSPolicyCaseRequest(AbstractModel):
    """CreateDDoSPolicyCase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _CaseName: 策略场景名，字符串长度小于64
        :type CaseName: str
        :param _PlatformTypes: 开发平台，取值[PC（PC客户端）， MOBILE（移动端）， TV（电视端）， SERVER（主机）]
        :type PlatformTypes: list of str
        :param _AppType: 细分品类，取值[WEB（网站）， GAME（游戏）， APP（应用）， OTHER（其他）]
        :type AppType: str
        :param _AppProtocols: 应用协议，取值[tcp（TCP协议），udp（UDP协议），icmp（ICMP协议），all（其他协议）]
        :type AppProtocols: list of str
        :param _TcpSportStart: TCP业务起始端口，取值(0, 65535]
        :type TcpSportStart: str
        :param _TcpSportEnd: TCP业务结束端口，取值(0, 65535]，必须大于等于TCP业务起始端口
        :type TcpSportEnd: str
        :param _UdpSportStart: UDP业务起始端口，取值范围(0, 65535]
        :type UdpSportStart: str
        :param _UdpSportEnd: UDP业务结束端口，取值范围(0, 65535)，必须大于等于UDP业务起始端口
        :type UdpSportEnd: str
        :param _HasAbroad: 是否有海外客户，取值[no（没有）, yes（有）]
        :type HasAbroad: str
        :param _HasInitiateTcp: 是否会主动对外发起TCP请求，取值[no（不会）, yes（会）]
        :type HasInitiateTcp: str
        :param _HasInitiateUdp: 是否会主动对外发起UDP业务请求，取值[no（不会）, yes（会）]
        :type HasInitiateUdp: str
        :param _PeerTcpPort: 主动发起TCP请求的端口，取值范围(0, 65535]
        :type PeerTcpPort: str
        :param _PeerUdpPort: 主动发起UDP请求的端口，取值范围(0, 65535]
        :type PeerUdpPort: str
        :param _TcpFootprint: TCP载荷的固定特征码，字符串长度小于512
        :type TcpFootprint: str
        :param _UdpFootprint: UDP载荷的固定特征码，字符串长度小于512
        :type UdpFootprint: str
        :param _WebApiUrl: Web业务的API的URL
        :type WebApiUrl: list of str
        :param _MinTcpPackageLen: TCP业务报文长度最小值，取值范围(0, 1500)
        :type MinTcpPackageLen: str
        :param _MaxTcpPackageLen: TCP业务报文长度最大值，取值范围(0, 1500)，必须大于等于TCP业务报文长度最小值
        :type MaxTcpPackageLen: str
        :param _MinUdpPackageLen: UDP业务报文长度最小值，取值范围(0, 1500)
        :type MinUdpPackageLen: str
        :param _MaxUdpPackageLen: UDP业务报文长度最大值，取值范围(0, 1500)，必须大于等于UDP业务报文长度最小值
        :type MaxUdpPackageLen: str
        :param _HasVPN: 是否有VPN业务，取值[no（没有）, yes（有）]
        :type HasVPN: str
        :param _TcpPortList: TCP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000
        :type TcpPortList: str
        :param _UdpPortList: UDP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000
        :type UdpPortList: str
        """
        self._Business = None
        self._CaseName = None
        self._PlatformTypes = None
        self._AppType = None
        self._AppProtocols = None
        self._TcpSportStart = None
        self._TcpSportEnd = None
        self._UdpSportStart = None
        self._UdpSportEnd = None
        self._HasAbroad = None
        self._HasInitiateTcp = None
        self._HasInitiateUdp = None
        self._PeerTcpPort = None
        self._PeerUdpPort = None
        self._TcpFootprint = None
        self._UdpFootprint = None
        self._WebApiUrl = None
        self._MinTcpPackageLen = None
        self._MaxTcpPackageLen = None
        self._MinUdpPackageLen = None
        self._MaxUdpPackageLen = None
        self._HasVPN = None
        self._TcpPortList = None
        self._UdpPortList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CaseName(self):
        return self._CaseName

    @CaseName.setter
    def CaseName(self, CaseName):
        self._CaseName = CaseName

    @property
    def PlatformTypes(self):
        return self._PlatformTypes

    @PlatformTypes.setter
    def PlatformTypes(self, PlatformTypes):
        self._PlatformTypes = PlatformTypes

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppProtocols(self):
        return self._AppProtocols

    @AppProtocols.setter
    def AppProtocols(self, AppProtocols):
        self._AppProtocols = AppProtocols

    @property
    def TcpSportStart(self):
        return self._TcpSportStart

    @TcpSportStart.setter
    def TcpSportStart(self, TcpSportStart):
        self._TcpSportStart = TcpSportStart

    @property
    def TcpSportEnd(self):
        return self._TcpSportEnd

    @TcpSportEnd.setter
    def TcpSportEnd(self, TcpSportEnd):
        self._TcpSportEnd = TcpSportEnd

    @property
    def UdpSportStart(self):
        return self._UdpSportStart

    @UdpSportStart.setter
    def UdpSportStart(self, UdpSportStart):
        self._UdpSportStart = UdpSportStart

    @property
    def UdpSportEnd(self):
        return self._UdpSportEnd

    @UdpSportEnd.setter
    def UdpSportEnd(self, UdpSportEnd):
        self._UdpSportEnd = UdpSportEnd

    @property
    def HasAbroad(self):
        return self._HasAbroad

    @HasAbroad.setter
    def HasAbroad(self, HasAbroad):
        self._HasAbroad = HasAbroad

    @property
    def HasInitiateTcp(self):
        return self._HasInitiateTcp

    @HasInitiateTcp.setter
    def HasInitiateTcp(self, HasInitiateTcp):
        self._HasInitiateTcp = HasInitiateTcp

    @property
    def HasInitiateUdp(self):
        return self._HasInitiateUdp

    @HasInitiateUdp.setter
    def HasInitiateUdp(self, HasInitiateUdp):
        self._HasInitiateUdp = HasInitiateUdp

    @property
    def PeerTcpPort(self):
        return self._PeerTcpPort

    @PeerTcpPort.setter
    def PeerTcpPort(self, PeerTcpPort):
        self._PeerTcpPort = PeerTcpPort

    @property
    def PeerUdpPort(self):
        return self._PeerUdpPort

    @PeerUdpPort.setter
    def PeerUdpPort(self, PeerUdpPort):
        self._PeerUdpPort = PeerUdpPort

    @property
    def TcpFootprint(self):
        return self._TcpFootprint

    @TcpFootprint.setter
    def TcpFootprint(self, TcpFootprint):
        self._TcpFootprint = TcpFootprint

    @property
    def UdpFootprint(self):
        return self._UdpFootprint

    @UdpFootprint.setter
    def UdpFootprint(self, UdpFootprint):
        self._UdpFootprint = UdpFootprint

    @property
    def WebApiUrl(self):
        return self._WebApiUrl

    @WebApiUrl.setter
    def WebApiUrl(self, WebApiUrl):
        self._WebApiUrl = WebApiUrl

    @property
    def MinTcpPackageLen(self):
        return self._MinTcpPackageLen

    @MinTcpPackageLen.setter
    def MinTcpPackageLen(self, MinTcpPackageLen):
        self._MinTcpPackageLen = MinTcpPackageLen

    @property
    def MaxTcpPackageLen(self):
        return self._MaxTcpPackageLen

    @MaxTcpPackageLen.setter
    def MaxTcpPackageLen(self, MaxTcpPackageLen):
        self._MaxTcpPackageLen = MaxTcpPackageLen

    @property
    def MinUdpPackageLen(self):
        return self._MinUdpPackageLen

    @MinUdpPackageLen.setter
    def MinUdpPackageLen(self, MinUdpPackageLen):
        self._MinUdpPackageLen = MinUdpPackageLen

    @property
    def MaxUdpPackageLen(self):
        return self._MaxUdpPackageLen

    @MaxUdpPackageLen.setter
    def MaxUdpPackageLen(self, MaxUdpPackageLen):
        self._MaxUdpPackageLen = MaxUdpPackageLen

    @property
    def HasVPN(self):
        return self._HasVPN

    @HasVPN.setter
    def HasVPN(self, HasVPN):
        self._HasVPN = HasVPN

    @property
    def TcpPortList(self):
        return self._TcpPortList

    @TcpPortList.setter
    def TcpPortList(self, TcpPortList):
        self._TcpPortList = TcpPortList

    @property
    def UdpPortList(self):
        return self._UdpPortList

    @UdpPortList.setter
    def UdpPortList(self, UdpPortList):
        self._UdpPortList = UdpPortList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._CaseName = params.get("CaseName")
        self._PlatformTypes = params.get("PlatformTypes")
        self._AppType = params.get("AppType")
        self._AppProtocols = params.get("AppProtocols")
        self._TcpSportStart = params.get("TcpSportStart")
        self._TcpSportEnd = params.get("TcpSportEnd")
        self._UdpSportStart = params.get("UdpSportStart")
        self._UdpSportEnd = params.get("UdpSportEnd")
        self._HasAbroad = params.get("HasAbroad")
        self._HasInitiateTcp = params.get("HasInitiateTcp")
        self._HasInitiateUdp = params.get("HasInitiateUdp")
        self._PeerTcpPort = params.get("PeerTcpPort")
        self._PeerUdpPort = params.get("PeerUdpPort")
        self._TcpFootprint = params.get("TcpFootprint")
        self._UdpFootprint = params.get("UdpFootprint")
        self._WebApiUrl = params.get("WebApiUrl")
        self._MinTcpPackageLen = params.get("MinTcpPackageLen")
        self._MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self._MinUdpPackageLen = params.get("MinUdpPackageLen")
        self._MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self._HasVPN = params.get("HasVPN")
        self._TcpPortList = params.get("TcpPortList")
        self._UdpPortList = params.get("UdpPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyCaseResponse(AbstractModel):
    """CreateDDoSPolicyCase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneId: 策略场景ID
        :type SceneId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SceneId = None
        self._RequestId = None

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._RequestId = params.get("RequestId")


class CreateDDoSPolicyRequest(AbstractModel):
    """CreateDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _DropOptions: 协议禁用，必须填写且数组长度必须为1
        :type DropOptions: list of DDoSPolicyDropOption
        :param _Name: 策略名称
        :type Name: str
        :param _PortLimits: 端口禁用，当没有禁用端口时填空数组
        :type PortLimits: list of DDoSPolicyPortLimit
        :param _IpAllowDenys: 请求源IP黑白名单，当没有IP黑白名单时填空数组
        :type IpAllowDenys: list of IpBlackWhite
        :param _PacketFilters: 报文过滤，当没有报文过滤时填空数组
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param _WaterPrint: 水印策略参数，当没有启用水印功能时填空数组，最多只能传一条水印策略（即数组大小不超过1）
        :type WaterPrint: list of WaterPrintPolicy
        """
        self._Business = None
        self._DropOptions = None
        self._Name = None
        self._PortLimits = None
        self._IpAllowDenys = None
        self._PacketFilters = None
        self._WaterPrint = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def DropOptions(self):
        return self._DropOptions

    @DropOptions.setter
    def DropOptions(self, DropOptions):
        self._DropOptions = DropOptions

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PortLimits(self):
        return self._PortLimits

    @PortLimits.setter
    def PortLimits(self, PortLimits):
        self._PortLimits = PortLimits

    @property
    def IpAllowDenys(self):
        return self._IpAllowDenys

    @IpAllowDenys.setter
    def IpAllowDenys(self, IpAllowDenys):
        self._IpAllowDenys = IpAllowDenys

    @property
    def PacketFilters(self):
        return self._PacketFilters

    @PacketFilters.setter
    def PacketFilters(self, PacketFilters):
        self._PacketFilters = PacketFilters

    @property
    def WaterPrint(self):
        return self._WaterPrint

    @WaterPrint.setter
    def WaterPrint(self, WaterPrint):
        self._WaterPrint = WaterPrint


    def _deserialize(self, params):
        self._Business = params.get("Business")
        if params.get("DropOptions") is not None:
            self._DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self._DropOptions.append(obj)
        self._Name = params.get("Name")
        if params.get("PortLimits") is not None:
            self._PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self._PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self._IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self._IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self._PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self._PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self._WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self._WaterPrint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSPolicyResponse(AbstractModel):
    """CreateDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateInstanceNameRequest(AbstractModel):
    """CreateInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Name: 资源实例名称，长度不超过32个字符
        :type Name: str
        """
        self._Business = None
        self._Id = None
        self._Name = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceNameResponse(AbstractModel):
    """CreateInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL4HealthConfigRequest(AbstractModel):
    """CreateL4HealthConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _HealthConfig: 四层健康检查配置数组
        :type HealthConfig: list of L4HealthConfig
        """
        self._Business = None
        self._Id = None
        self._HealthConfig = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4HealthConfigResponse(AbstractModel):
    """CreateL4HealthConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL4RulesRequest(AbstractModel):
    """CreateL4Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rules: 规则列表
        :type Rules: list of L4RuleEntry
        """
        self._Business = None
        self._Id = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL4RulesResponse(AbstractModel):
    """CreateL4Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7CCRuleRequest(AbstractModel):
    """CreateL7CCRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Method: 操作码，取值[query(表示查询)，add(表示添加)，del(表示删除)]
        :type Method: str
        :param _RuleId: 7层转发规则ID，例如：rule-0000001
        :type RuleId: str
        :param _RuleConfig: 7层CC自定义规则参数，当操作码为query时，可以不用填写；当操作码为add或del时，必须填写，且数组长度只能为1；
        :type RuleConfig: list of CCRuleConfig
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._RuleId = None
        self._RuleConfig = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleConfig(self):
        return self._RuleConfig

    @RuleConfig.setter
    def RuleConfig(self, RuleConfig):
        self._RuleConfig = RuleConfig


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._RuleId = params.get("RuleId")
        if params.get("RuleConfig") is not None:
            self._RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self._RuleConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7CCRuleResponse(AbstractModel):
    """CreateL7CCRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleConfig: 7层CC自定义规则参数，当没有开启CC自定义规则时，返回空数组
        :type RuleConfig: list of CCRuleConfig
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleConfig = None
        self._RequestId = None

    @property
    def RuleConfig(self):
        return self._RuleConfig

    @RuleConfig.setter
    def RuleConfig(self, RuleConfig):
        self._RuleConfig = RuleConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RuleConfig") is not None:
            self._RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self._RuleConfig.append(obj)
        self._RequestId = params.get("RequestId")


class CreateL7HealthConfigRequest(AbstractModel):
    """CreateL7HealthConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _HealthConfig: 七层健康检查配置数组
        :type HealthConfig: list of L7HealthConfig
        """
        self._Business = None
        self._Id = None
        self._HealthConfig = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7HealthConfigResponse(AbstractModel):
    """CreateL7HealthConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7RuleCertRequest(AbstractModel):
    """CreateL7RuleCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源实例ID，例如高防IP实例的ID，高防IP专业版实例的ID
        :type Id: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _CertType: 证书类型，当为协议为HTTPS协议时必须填，取值[2(腾讯云托管证书)]
        :type CertType: int
        :param _SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param _Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param _PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RuleCertResponse(AbstractModel):
    """CreateL7RuleCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7RulesRequest(AbstractModel):
    """CreateL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rules: 规则列表
        :type Rules: list of L7RuleEntry
        """
        self._Business = None
        self._Id = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateL7RulesUploadRequest(AbstractModel):
    """CreateL7RulesUpload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rules: 规则列表
        :type Rules: list of L7RuleEntry
        """
        self._Business = None
        self._Id = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RulesUploadResponse(AbstractModel):
    """CreateL7RulesUpload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateNetReturnRequest(AbstractModel):
    """CreateNetReturn请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetReturnResponse(AbstractModel):
    """CreateNetReturn返回参数结构体

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


class CreateNewL4RulesRequest(AbstractModel):
    """CreateNewL4Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 高防产品代号：bgpip
        :type Business: str
        :param _IdList: 添加规则资源列表
        :type IdList: list of str
        :param _VipList: 添加规则IP列表
        :type VipList: list of str
        :param _Rules: 规则列表
        :type Rules: list of L4RuleEntry
        """
        self._Business = None
        self._IdList = None
        self._VipList = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def VipList(self):
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        self._VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL4RulesResponse(AbstractModel):
    """CreateNewL4Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateNewL7RulesRequest(AbstractModel):
    """CreateNewL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _IdList: 资源ID列表
        :type IdList: list of str
        :param _VipList: 资源IP列表
        :type VipList: list of str
        :param _Rules: 规则列表
        :type Rules: list of L7RuleEntry
        """
        self._Business = None
        self._IdList = None
        self._VipList = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def VipList(self):
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        self._VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesResponse(AbstractModel):
    """CreateNewL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateNewL7RulesUploadRequest(AbstractModel):
    """CreateNewL7RulesUpload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _IdList: 资源ID列表
        :type IdList: list of str
        :param _VipList: 资源IP列表
        :type VipList: list of str
        :param _Rules: 规则列表
        :type Rules: list of L7RuleEntry
        """
        self._Business = None
        self._IdList = None
        self._VipList = None
        self._Rules = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def VipList(self):
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        self._VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesUploadResponse(AbstractModel):
    """CreateNewL7RulesUpload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateUnblockIpRequest(AbstractModel):
    """CreateUnblockIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）
        :type ActionType: str
        """
        self._Ip = None
        self._ActionType = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUnblockIpResponse(AbstractModel):
    """CreateUnblockIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）
        :type ActionType: str
        :param _UnblockTime: 解封时间（预计解封时间）
        :type UnblockTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ip = None
        self._ActionType = None
        self._UnblockTime = None
        self._RequestId = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def UnblockTime(self):
        return self._UnblockTime

    @UnblockTime.setter
    def UnblockTime(self, UnblockTime):
        self._UnblockTime = UnblockTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._ActionType = params.get("ActionType")
        self._UnblockTime = params.get("UnblockTime")
        self._RequestId = params.get("RequestId")


class DDoSAlarmThreshold(AbstractModel):
    """DDoS告警阈值

    """

    def __init__(self):
        r"""
        :param _AlarmType: 告警阈值类型，1-入流量，2-清洗流量
        :type AlarmType: int
        :param _AlarmThreshold: 告警阈值，大于0（目前排定的值）
        :type AlarmThreshold: int
        """
        self._AlarmType = None
        self._AlarmThreshold = None

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold


    def _deserialize(self, params):
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackSourceRecord(AbstractModel):
    """攻击源信息

    """

    def __init__(self):
        r"""
        :param _SrcIp: 攻击源ip
        :type SrcIp: str
        :param _Province: 省份（国内有效，不包含港澳台）
        :type Province: str
        :param _Nation: 国家
        :type Nation: str
        :param _PacketSum: 累计攻击包量
        :type PacketSum: int
        :param _PacketLen: 累计攻击流量
        :type PacketLen: int
        """
        self._SrcIp = None
        self._Province = None
        self._Nation = None
        self._PacketSum = None
        self._PacketLen = None

    @property
    def SrcIp(self):
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def Province(self):
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def PacketSum(self):
        return self._PacketSum

    @PacketSum.setter
    def PacketSum(self, PacketSum):
        self._PacketSum = PacketSum

    @property
    def PacketLen(self):
        return self._PacketLen

    @PacketLen.setter
    def PacketLen(self, PacketLen):
        self._PacketLen = PacketLen


    def _deserialize(self, params):
        self._SrcIp = params.get("SrcIp")
        self._Province = params.get("Province")
        self._Nation = params.get("Nation")
        self._PacketSum = params.get("PacketSum")
        self._PacketLen = params.get("PacketLen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSEventRecord(AbstractModel):
    """DDoS攻击事件记录

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Vip: 资源的IP
        :type Vip: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        :param _Mbps: 攻击最大带宽
        :type Mbps: int
        :param _Pps: 攻击最大包速率
        :type Pps: int
        :param _AttackType: 攻击类型
        :type AttackType: str
        :param _BlockFlag: 是否被封堵，取值[1（是），0（否），2（无效值）]
        :type BlockFlag: int
        :param _OverLoad: 是否超过弹性防护峰值，取值取值[yes(是)，no(否)，空字符串（未知值）]
        :type OverLoad: str
        :param _AttackStatus: 攻击状态，取值[0（攻击中）, 1（攻击结束）]
        :type AttackStatus: int
        :param _ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _EventId: 攻击事件Id
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        """
        self._Business = None
        self._Id = None
        self._Vip = None
        self._StartTime = None
        self._EndTime = None
        self._Mbps = None
        self._Pps = None
        self._AttackType = None
        self._BlockFlag = None
        self._OverLoad = None
        self._AttackStatus = None
        self._ResourceName = None
        self._EventId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

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
    def Mbps(self):
        return self._Mbps

    @Mbps.setter
    def Mbps(self, Mbps):
        self._Mbps = Mbps

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def BlockFlag(self):
        return self._BlockFlag

    @BlockFlag.setter
    def BlockFlag(self, BlockFlag):
        self._BlockFlag = BlockFlag

    @property
    def OverLoad(self):
        return self._OverLoad

    @OverLoad.setter
    def OverLoad(self, OverLoad):
        self._OverLoad = OverLoad

    @property
    def AttackStatus(self):
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._AttackType = params.get("AttackType")
        self._BlockFlag = params.get("BlockFlag")
        self._OverLoad = params.get("OverLoad")
        self._AttackStatus = params.get("AttackStatus")
        self._ResourceName = params.get("ResourceName")
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyDropOption(AbstractModel):
    """DDoS高级策略的禁用协议选项

    """

    def __init__(self):
        r"""
        :param _DropTcp: 禁用TCP协议，取值范围[0,1]
        :type DropTcp: int
        :param _DropUdp: 禁用UDP协议，取值范围[0,1]
        :type DropUdp: int
        :param _DropIcmp: 禁用ICMP协议，取值范围[0,1]
        :type DropIcmp: int
        :param _DropOther: 禁用其他协议，取值范围[0,1]
        :type DropOther: int
        :param _DropAbroad: 拒绝海外流量，取值范围[0,1]
        :type DropAbroad: int
        :param _CheckSyncConn: 空连接防护，取值范围[0,1]
        :type CheckSyncConn: int
        :param _SdNewLimit: 基于来源IP及目的IP的新建连接抑制，取值范围[0,4294967295]
        :type SdNewLimit: int
        :param _DstNewLimit: 基于目的IP的新建连接抑制，取值范围[0,4294967295]
        :type DstNewLimit: int
        :param _SdConnLimit: 基于来源IP及目的IP的并发连接抑制，取值范围[0,4294967295]
        :type SdConnLimit: int
        :param _DstConnLimit: 基于目的IP的并发连接抑制，取值范围[0,4294967295]
        :type DstConnLimit: int
        :param _BadConnThreshold: 基于连接抑制触发阈值，取值范围[0,4294967295]
        :type BadConnThreshold: int
        :param _NullConnEnable: 异常连接检测条件，空连接防护开关，，取值范围[0,1]
        :type NullConnEnable: int
        :param _ConnTimeout: 异常连接检测条件，连接超时，，取值范围[0,65535]
        :type ConnTimeout: int
        :param _SynRate: 异常连接检测条件，syn占比ack百分比，，取值范围[0,100]
        :type SynRate: int
        :param _SynLimit: 异常连接检测条件，syn阈值，取值范围[0,100]
        :type SynLimit: int
        :param _DTcpMbpsLimit: tcp限速，取值范围[0,4294967295]
        :type DTcpMbpsLimit: int
        :param _DUdpMbpsLimit: udp限速，取值范围[0,4294967295]
        :type DUdpMbpsLimit: int
        :param _DIcmpMbpsLimit: icmp限速，取值范围[0,4294967295]
        :type DIcmpMbpsLimit: int
        :param _DOtherMbpsLimit: other协议限速，取值范围[0,4294967295]
        :type DOtherMbpsLimit: int
        """
        self._DropTcp = None
        self._DropUdp = None
        self._DropIcmp = None
        self._DropOther = None
        self._DropAbroad = None
        self._CheckSyncConn = None
        self._SdNewLimit = None
        self._DstNewLimit = None
        self._SdConnLimit = None
        self._DstConnLimit = None
        self._BadConnThreshold = None
        self._NullConnEnable = None
        self._ConnTimeout = None
        self._SynRate = None
        self._SynLimit = None
        self._DTcpMbpsLimit = None
        self._DUdpMbpsLimit = None
        self._DIcmpMbpsLimit = None
        self._DOtherMbpsLimit = None

    @property
    def DropTcp(self):
        return self._DropTcp

    @DropTcp.setter
    def DropTcp(self, DropTcp):
        self._DropTcp = DropTcp

    @property
    def DropUdp(self):
        return self._DropUdp

    @DropUdp.setter
    def DropUdp(self, DropUdp):
        self._DropUdp = DropUdp

    @property
    def DropIcmp(self):
        return self._DropIcmp

    @DropIcmp.setter
    def DropIcmp(self, DropIcmp):
        self._DropIcmp = DropIcmp

    @property
    def DropOther(self):
        return self._DropOther

    @DropOther.setter
    def DropOther(self, DropOther):
        self._DropOther = DropOther

    @property
    def DropAbroad(self):
        return self._DropAbroad

    @DropAbroad.setter
    def DropAbroad(self, DropAbroad):
        self._DropAbroad = DropAbroad

    @property
    def CheckSyncConn(self):
        return self._CheckSyncConn

    @CheckSyncConn.setter
    def CheckSyncConn(self, CheckSyncConn):
        self._CheckSyncConn = CheckSyncConn

    @property
    def SdNewLimit(self):
        return self._SdNewLimit

    @SdNewLimit.setter
    def SdNewLimit(self, SdNewLimit):
        self._SdNewLimit = SdNewLimit

    @property
    def DstNewLimit(self):
        return self._DstNewLimit

    @DstNewLimit.setter
    def DstNewLimit(self, DstNewLimit):
        self._DstNewLimit = DstNewLimit

    @property
    def SdConnLimit(self):
        return self._SdConnLimit

    @SdConnLimit.setter
    def SdConnLimit(self, SdConnLimit):
        self._SdConnLimit = SdConnLimit

    @property
    def DstConnLimit(self):
        return self._DstConnLimit

    @DstConnLimit.setter
    def DstConnLimit(self, DstConnLimit):
        self._DstConnLimit = DstConnLimit

    @property
    def BadConnThreshold(self):
        return self._BadConnThreshold

    @BadConnThreshold.setter
    def BadConnThreshold(self, BadConnThreshold):
        self._BadConnThreshold = BadConnThreshold

    @property
    def NullConnEnable(self):
        return self._NullConnEnable

    @NullConnEnable.setter
    def NullConnEnable(self, NullConnEnable):
        self._NullConnEnable = NullConnEnable

    @property
    def ConnTimeout(self):
        return self._ConnTimeout

    @ConnTimeout.setter
    def ConnTimeout(self, ConnTimeout):
        self._ConnTimeout = ConnTimeout

    @property
    def SynRate(self):
        return self._SynRate

    @SynRate.setter
    def SynRate(self, SynRate):
        self._SynRate = SynRate

    @property
    def SynLimit(self):
        return self._SynLimit

    @SynLimit.setter
    def SynLimit(self, SynLimit):
        self._SynLimit = SynLimit

    @property
    def DTcpMbpsLimit(self):
        return self._DTcpMbpsLimit

    @DTcpMbpsLimit.setter
    def DTcpMbpsLimit(self, DTcpMbpsLimit):
        self._DTcpMbpsLimit = DTcpMbpsLimit

    @property
    def DUdpMbpsLimit(self):
        return self._DUdpMbpsLimit

    @DUdpMbpsLimit.setter
    def DUdpMbpsLimit(self, DUdpMbpsLimit):
        self._DUdpMbpsLimit = DUdpMbpsLimit

    @property
    def DIcmpMbpsLimit(self):
        return self._DIcmpMbpsLimit

    @DIcmpMbpsLimit.setter
    def DIcmpMbpsLimit(self, DIcmpMbpsLimit):
        self._DIcmpMbpsLimit = DIcmpMbpsLimit

    @property
    def DOtherMbpsLimit(self):
        return self._DOtherMbpsLimit

    @DOtherMbpsLimit.setter
    def DOtherMbpsLimit(self, DOtherMbpsLimit):
        self._DOtherMbpsLimit = DOtherMbpsLimit


    def _deserialize(self, params):
        self._DropTcp = params.get("DropTcp")
        self._DropUdp = params.get("DropUdp")
        self._DropIcmp = params.get("DropIcmp")
        self._DropOther = params.get("DropOther")
        self._DropAbroad = params.get("DropAbroad")
        self._CheckSyncConn = params.get("CheckSyncConn")
        self._SdNewLimit = params.get("SdNewLimit")
        self._DstNewLimit = params.get("DstNewLimit")
        self._SdConnLimit = params.get("SdConnLimit")
        self._DstConnLimit = params.get("DstConnLimit")
        self._BadConnThreshold = params.get("BadConnThreshold")
        self._NullConnEnable = params.get("NullConnEnable")
        self._ConnTimeout = params.get("ConnTimeout")
        self._SynRate = params.get("SynRate")
        self._SynLimit = params.get("SynLimit")
        self._DTcpMbpsLimit = params.get("DTcpMbpsLimit")
        self._DUdpMbpsLimit = params.get("DUdpMbpsLimit")
        self._DIcmpMbpsLimit = params.get("DIcmpMbpsLimit")
        self._DOtherMbpsLimit = params.get("DOtherMbpsLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPacketFilter(AbstractModel):
    """DDoS高级策略的报文过滤项

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议，取值范围[tcp,udp,icmp,all]
        :type Protocol: str
        :param _SportStart: 开始源端口，取值范围[0,65535]
        :type SportStart: int
        :param _SportEnd: 结束源端口，取值范围[0,65535]
        :type SportEnd: int
        :param _DportStart: 开始目的端口，取值范围[0,65535]
        :type DportStart: int
        :param _DportEnd: 结束目的端口，取值范围[0,65535]
        :type DportEnd: int
        :param _PktlenMin: 最小包长，取值范围[0,1500]
        :type PktlenMin: int
        :param _PktlenMax: 最大包长，取值范围[0,1500]
        :type PktlenMax: int
        :param _MatchBegin: 是否检测载荷，取值范围[
begin_l3(IP头)
begin_l4(TCP头)
begin_l5(载荷)
no_match(不检测)
]
        :type MatchBegin: str
        :param _MatchType: 是否是正则表达式，取值范围[sunday(表示关键字),pcre(表示正则表达式)]
        :type MatchType: str
        :param _Str: 关键字或正则表达式
        :type Str: str
        :param _Depth: 检测深度，取值范围[0,1500]
        :type Depth: int
        :param _Offset: 检测偏移量，取值范围[0,1500]
        :type Offset: int
        :param _IsNot: 是否包括，取值范围[0(表示不包含),1(表示包含)]
        :type IsNot: int
        :param _Action: 策略动作，取值范围[drop，drop_black，drop_rst，drop_black_rst，transmit]
        :type Action: str
        """
        self._Protocol = None
        self._SportStart = None
        self._SportEnd = None
        self._DportStart = None
        self._DportEnd = None
        self._PktlenMin = None
        self._PktlenMax = None
        self._MatchBegin = None
        self._MatchType = None
        self._Str = None
        self._Depth = None
        self._Offset = None
        self._IsNot = None
        self._Action = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SportStart(self):
        return self._SportStart

    @SportStart.setter
    def SportStart(self, SportStart):
        self._SportStart = SportStart

    @property
    def SportEnd(self):
        return self._SportEnd

    @SportEnd.setter
    def SportEnd(self, SportEnd):
        self._SportEnd = SportEnd

    @property
    def DportStart(self):
        return self._DportStart

    @DportStart.setter
    def DportStart(self, DportStart):
        self._DportStart = DportStart

    @property
    def DportEnd(self):
        return self._DportEnd

    @DportEnd.setter
    def DportEnd(self, DportEnd):
        self._DportEnd = DportEnd

    @property
    def PktlenMin(self):
        return self._PktlenMin

    @PktlenMin.setter
    def PktlenMin(self, PktlenMin):
        self._PktlenMin = PktlenMin

    @property
    def PktlenMax(self):
        return self._PktlenMax

    @PktlenMax.setter
    def PktlenMax(self, PktlenMax):
        self._PktlenMax = PktlenMax

    @property
    def MatchBegin(self):
        return self._MatchBegin

    @MatchBegin.setter
    def MatchBegin(self, MatchBegin):
        self._MatchBegin = MatchBegin

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def Str(self):
        return self._Str

    @Str.setter
    def Str(self, Str):
        self._Str = Str

    @property
    def Depth(self):
        return self._Depth

    @Depth.setter
    def Depth(self, Depth):
        self._Depth = Depth

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def IsNot(self):
        return self._IsNot

    @IsNot.setter
    def IsNot(self, IsNot):
        self._IsNot = IsNot

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._SportStart = params.get("SportStart")
        self._SportEnd = params.get("SportEnd")
        self._DportStart = params.get("DportStart")
        self._DportEnd = params.get("DportEnd")
        self._PktlenMin = params.get("PktlenMin")
        self._PktlenMax = params.get("PktlenMax")
        self._MatchBegin = params.get("MatchBegin")
        self._MatchType = params.get("MatchType")
        self._Str = params.get("Str")
        self._Depth = params.get("Depth")
        self._Offset = params.get("Offset")
        self._IsNot = params.get("IsNot")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSPolicyPortLimit(AbstractModel):
    """DDoS高级策略的禁用端口

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议，取值范围[tcp,udp,all]
        :type Protocol: str
        :param _DPortStart: 开始目的端口，取值范围[0,65535]
        :type DPortStart: int
        :param _DPortEnd: 结束目的端口，取值范围[0,65535]，要求大于等于开始目的端口
        :type DPortEnd: int
        :param _SPortStart: 开始源端口，取值范围[0,65535]
注意：此字段可能返回 null，表示取不到有效值。
        :type SPortStart: int
        :param _SPortEnd: 结束源端口，取值范围[0,65535]，要求大于等于开始源端口
注意：此字段可能返回 null，表示取不到有效值。
        :type SPortEnd: int
        :param _Action: 执行动作，取值[drop(丢弃) ，transmit(转发)]
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _Kind: 禁用端口类型，取值[0（目的端口范围禁用）， 1（源端口范围禁用）， 2（目的和源端口范围同时禁用）]
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: int
        """
        self._Protocol = None
        self._DPortStart = None
        self._DPortEnd = None
        self._SPortStart = None
        self._SPortEnd = None
        self._Action = None
        self._Kind = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def DPortStart(self):
        return self._DPortStart

    @DPortStart.setter
    def DPortStart(self, DPortStart):
        self._DPortStart = DPortStart

    @property
    def DPortEnd(self):
        return self._DPortEnd

    @DPortEnd.setter
    def DPortEnd(self, DPortEnd):
        self._DPortEnd = DPortEnd

    @property
    def SPortStart(self):
        return self._SPortStart

    @SPortStart.setter
    def SPortStart(self, SPortStart):
        self._SPortStart = SPortStart

    @property
    def SPortEnd(self):
        return self._SPortEnd

    @SPortEnd.setter
    def SPortEnd(self, SPortEnd):
        self._SPortEnd = SPortEnd

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._DPortStart = params.get("DPortStart")
        self._DPortEnd = params.get("DPortEnd")
        self._SPortStart = params.get("SPortStart")
        self._SPortEnd = params.get("SPortEnd")
        self._Action = params.get("Action")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDosPolicy(AbstractModel):
    """DDoS高级策略

    """

    def __init__(self):
        r"""
        :param _Resources: 策略绑定的资源
        :type Resources: list of ResourceIp
        :param _DropOptions: 禁用协议
        :type DropOptions: :class:`tencentcloud.dayu.v20180709.models.DDoSPolicyDropOption`
        :param _PortLimits: 禁用端口
        :type PortLimits: list of DDoSPolicyPortLimit
        :param _PacketFilters: 报文过滤
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param _IpBlackWhiteLists: 黑白IP名单
        :type IpBlackWhiteLists: list of IpBlackWhite
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _CreateTime: 策略创建时间
        :type CreateTime: str
        :param _WaterPrint: 水印策略参数，最多只有一个，当没有水印策略时数组为空
        :type WaterPrint: list of WaterPrintPolicy
        :param _WaterKey: 水印密钥，最多只有2个，当没有水印策略时数组为空
        :type WaterKey: list of WaterPrintKey
        :param _BoundResources: 策略绑定的资源实例
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundResources: list of str
        :param _SceneId: 策略所属的策略场景
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneId: str
        """
        self._Resources = None
        self._DropOptions = None
        self._PortLimits = None
        self._PacketFilters = None
        self._IpBlackWhiteLists = None
        self._PolicyId = None
        self._PolicyName = None
        self._CreateTime = None
        self._WaterPrint = None
        self._WaterKey = None
        self._BoundResources = None
        self._SceneId = None

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def DropOptions(self):
        return self._DropOptions

    @DropOptions.setter
    def DropOptions(self, DropOptions):
        self._DropOptions = DropOptions

    @property
    def PortLimits(self):
        return self._PortLimits

    @PortLimits.setter
    def PortLimits(self, PortLimits):
        self._PortLimits = PortLimits

    @property
    def PacketFilters(self):
        return self._PacketFilters

    @PacketFilters.setter
    def PacketFilters(self, PacketFilters):
        self._PacketFilters = PacketFilters

    @property
    def IpBlackWhiteLists(self):
        return self._IpBlackWhiteLists

    @IpBlackWhiteLists.setter
    def IpBlackWhiteLists(self, IpBlackWhiteLists):
        self._IpBlackWhiteLists = IpBlackWhiteLists

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def WaterPrint(self):
        return self._WaterPrint

    @WaterPrint.setter
    def WaterPrint(self, WaterPrint):
        self._WaterPrint = WaterPrint

    @property
    def WaterKey(self):
        return self._WaterKey

    @WaterKey.setter
    def WaterKey(self, WaterKey):
        self._WaterKey = WaterKey

    @property
    def BoundResources(self):
        return self._BoundResources

    @BoundResources.setter
    def BoundResources(self, BoundResources):
        self._BoundResources = BoundResources

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceIp()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("DropOptions") is not None:
            self._DropOptions = DDoSPolicyDropOption()
            self._DropOptions._deserialize(params.get("DropOptions"))
        if params.get("PortLimits") is not None:
            self._PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self._PortLimits.append(obj)
        if params.get("PacketFilters") is not None:
            self._PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self._PacketFilters.append(obj)
        if params.get("IpBlackWhiteLists") is not None:
            self._IpBlackWhiteLists = []
            for item in params.get("IpBlackWhiteLists"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self._IpBlackWhiteLists.append(obj)
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._CreateTime = params.get("CreateTime")
        if params.get("WaterPrint") is not None:
            self._WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self._WaterPrint.append(obj)
        if params.get("WaterKey") is not None:
            self._WaterKey = []
            for item in params.get("WaterKey"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self._WaterKey.append(obj)
        self._BoundResources = params.get("BoundResources")
        self._SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesRequest(AbstractModel):
    """DeleteCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _CCFrequencyRuleId: CC防护的访问频率控制规则ID
        :type CCFrequencyRuleId: str
        """
        self._Business = None
        self._CCFrequencyRuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCFrequencyRulesResponse(AbstractModel):
    """DeleteCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteCCSelfDefinePolicyRequest(AbstractModel):
    """DeleteCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _SetId: 策略ID
        :type SetId: str
        """
        self._Business = None
        self._Id = None
        self._SetId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._SetId = params.get("SetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCSelfDefinePolicyResponse(AbstractModel):
    """DeleteCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteDDoSPolicyCaseRequest(AbstractModel):
    """DeleteDDoSPolicyCase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _SceneId: 策略场景ID
        :type SceneId: str
        """
        self._Business = None
        self._SceneId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyCaseResponse(AbstractModel):
    """DeleteDDoSPolicyCase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteDDoSPolicyRequest(AbstractModel):
    """DeleteDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _PolicyId: 策略ID
        :type PolicyId: str
        """
        self._Business = None
        self._PolicyId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSPolicyResponse(AbstractModel):
    """DeleteDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteL4RulesRequest(AbstractModel):
    """DeleteL4Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleIdList: 规则ID列表
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL4RulesResponse(AbstractModel):
    """DeleteL4Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    """DeleteL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleIdList: 规则ID列表
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteNewL4RulesRequest(AbstractModel):
    """DeleteNewL4Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Rule: 删除接口结构体
        :type Rule: list of L4DelRule
        """
        self._Business = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        if params.get("Rule") is not None:
            self._Rule = []
            for item in params.get("Rule"):
                obj = L4DelRule()
                obj._deserialize(item)
                self._Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNewL4RulesResponse(AbstractModel):
    """DeleteNewL4Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DeleteNewL7RulesRequest(AbstractModel):
    """DeleteNewL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP)
        :type Business: str
        :param _Rule: 删除规则列表
        :type Rule: list of L4DelRule
        """
        self._Business = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        if params.get("Rule") is not None:
            self._Rule = []
            for item in params.get("Rule"):
                obj = L4DelRule()
                obj._deserialize(item)
                self._Rule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNewL7RulesResponse(AbstractModel):
    """DeleteNewL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class DescribeActionLogRequest(AbstractModel):
    """DescribeActionLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Filter: 搜索值，只支持资源ID或用户UIN
        :type Filter: str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Business = None
        self._Filter = None
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
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

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
        self._Business = params.get("Business")
        self._Filter = params.get("Filter")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeActionLogResponse(AbstractModel):
    """DescribeActionLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _Data: 记录数组
        :type Data: list of KeyValueRecord
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
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBGPIPL7RuleMaxCntRequest(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBGPIPL7RuleMaxCntResponse(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 高防IP最多可添加的7层规则数量
        :type Count: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._RequestId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeBaradDataRequest(AbstractModel):
    """DescribeBaradData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _MetricName: 指标名，取值：
connum表示TCP活跃连接数；
new_conn表示新建TCP连接数；
inactive_conn表示非活跃连接数;
intraffic表示入流量；
outtraffic表示出流量；
alltraffic表示出流量和入流量之和；
inpkg表示入包速率；
outpkg表示出包速率；
        :type MetricName: str
        :param _Period: 统计时间粒度，单位秒（300表示5分钟；3600表示小时；86400表示天）
        :type Period: int
        :param _StartTime: 统计开始时间，秒部分保持为0，分钟部分为5的倍数
        :type StartTime: str
        :param _EndTime: 统计结束时间，秒部分保持为0，分钟部分为5的倍数
        :type EndTime: str
        :param _Statistics: 统计方式，取值：
max表示最大值；
min表示最小值；
avg表示均值；
        :type Statistics: str
        :param _ProtocolPort: 协议端口数组
        :type ProtocolPort: list of ProtocolPort
        :param _Ip: 资源实例下的IP，只有当Business=net(高防IP专业版)时才必须填写资源的一个IP（因为高防IP专业版资源实例有多个IP，才需要指定）；
        :type Ip: str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Statistics = None
        self._ProtocolPort = None
        self._Ip = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def ProtocolPort(self):
        return self._ProtocolPort

    @ProtocolPort.setter
    def ProtocolPort(self, ProtocolPort):
        self._ProtocolPort = ProtocolPort

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Statistics = params.get("Statistics")
        if params.get("ProtocolPort") is not None:
            self._ProtocolPort = []
            for item in params.get("ProtocolPort"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtocolPort.append(obj)
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaradDataResponse(AbstractModel):
    """DescribeBaradData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataList: 返回指标的值
        :type DataList: list of BaradData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataList = None
        self._RequestId = None

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = BaradData()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBasicCCThresholdRequest(AbstractModel):
    """DescribeBasicCCThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicIp: 查询的IP地址，取值如：1.1.1.1
        :type BasicIp: str
        :param _BasicRegion: 查询IP所属地域，取值如：gz、bj、sh、hk等地域缩写
        :type BasicRegion: str
        :param _BasicBizType: 专区类型，取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。
        :type BasicBizType: str
        :param _BasicDeviceType: 设备类型，取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel.
        :type BasicDeviceType: str
        :param _BasicIpInstance: 可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）
        :type BasicIpInstance: str
        :param _BasicIspCode: 可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）
        :type BasicIspCode: int
        """
        self._BasicIp = None
        self._BasicRegion = None
        self._BasicBizType = None
        self._BasicDeviceType = None
        self._BasicIpInstance = None
        self._BasicIspCode = None

    @property
    def BasicIp(self):
        return self._BasicIp

    @BasicIp.setter
    def BasicIp(self, BasicIp):
        self._BasicIp = BasicIp

    @property
    def BasicRegion(self):
        return self._BasicRegion

    @BasicRegion.setter
    def BasicRegion(self, BasicRegion):
        self._BasicRegion = BasicRegion

    @property
    def BasicBizType(self):
        return self._BasicBizType

    @BasicBizType.setter
    def BasicBizType(self, BasicBizType):
        self._BasicBizType = BasicBizType

    @property
    def BasicDeviceType(self):
        return self._BasicDeviceType

    @BasicDeviceType.setter
    def BasicDeviceType(self, BasicDeviceType):
        self._BasicDeviceType = BasicDeviceType

    @property
    def BasicIpInstance(self):
        return self._BasicIpInstance

    @BasicIpInstance.setter
    def BasicIpInstance(self, BasicIpInstance):
        self._BasicIpInstance = BasicIpInstance

    @property
    def BasicIspCode(self):
        return self._BasicIspCode

    @BasicIspCode.setter
    def BasicIspCode(self, BasicIspCode):
        self._BasicIspCode = BasicIspCode


    def _deserialize(self, params):
        self._BasicIp = params.get("BasicIp")
        self._BasicRegion = params.get("BasicRegion")
        self._BasicBizType = params.get("BasicBizType")
        self._BasicDeviceType = params.get("BasicDeviceType")
        self._BasicIpInstance = params.get("BasicIpInstance")
        self._BasicIspCode = params.get("BasicIspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicCCThresholdResponse(AbstractModel):
    """DescribeBasicCCThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CCEnable: CC启动开关（0:关闭；1:开启）
        :type CCEnable: int
        :param _CCThreshold: CC防护阈值
        :type CCThreshold: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CCEnable = None
        self._CCThreshold = None
        self._RequestId = None

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._RequestId = params.get("RequestId")


class DescribeBasicDeviceThresholdRequest(AbstractModel):
    """DescribeBasicDeviceThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicIp: 查询的IP地址，取值如：1.1.1.1
        :type BasicIp: str
        :param _BasicRegion: 查询IP所属地域，取值如：gz、bj、sh、hk等地域缩写
        :type BasicRegion: str
        :param _BasicBizType: 专区类型，取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。
        :type BasicBizType: str
        :param _BasicDeviceType: 设备类型，取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel.
        :type BasicDeviceType: str
        :param _BasicCheckFlag: 有效性检查，取值为1
        :type BasicCheckFlag: int
        :param _BasicIpInstance: 可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）
        :type BasicIpInstance: str
        :param _BasicIspCode: 可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）
        :type BasicIspCode: int
        """
        self._BasicIp = None
        self._BasicRegion = None
        self._BasicBizType = None
        self._BasicDeviceType = None
        self._BasicCheckFlag = None
        self._BasicIpInstance = None
        self._BasicIspCode = None

    @property
    def BasicIp(self):
        return self._BasicIp

    @BasicIp.setter
    def BasicIp(self, BasicIp):
        self._BasicIp = BasicIp

    @property
    def BasicRegion(self):
        return self._BasicRegion

    @BasicRegion.setter
    def BasicRegion(self, BasicRegion):
        self._BasicRegion = BasicRegion

    @property
    def BasicBizType(self):
        return self._BasicBizType

    @BasicBizType.setter
    def BasicBizType(self, BasicBizType):
        self._BasicBizType = BasicBizType

    @property
    def BasicDeviceType(self):
        return self._BasicDeviceType

    @BasicDeviceType.setter
    def BasicDeviceType(self, BasicDeviceType):
        self._BasicDeviceType = BasicDeviceType

    @property
    def BasicCheckFlag(self):
        return self._BasicCheckFlag

    @BasicCheckFlag.setter
    def BasicCheckFlag(self, BasicCheckFlag):
        self._BasicCheckFlag = BasicCheckFlag

    @property
    def BasicIpInstance(self):
        return self._BasicIpInstance

    @BasicIpInstance.setter
    def BasicIpInstance(self, BasicIpInstance):
        self._BasicIpInstance = BasicIpInstance

    @property
    def BasicIspCode(self):
        return self._BasicIspCode

    @BasicIspCode.setter
    def BasicIspCode(self, BasicIspCode):
        self._BasicIspCode = BasicIspCode


    def _deserialize(self, params):
        self._BasicIp = params.get("BasicIp")
        self._BasicRegion = params.get("BasicRegion")
        self._BasicBizType = params.get("BasicBizType")
        self._BasicDeviceType = params.get("BasicDeviceType")
        self._BasicCheckFlag = params.get("BasicCheckFlag")
        self._BasicIpInstance = params.get("BasicIpInstance")
        self._BasicIspCode = params.get("BasicIspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDeviceThresholdResponse(AbstractModel):
    """DescribeBasicDeviceThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Threshold: 返回黑洞封堵值
        :type Threshold: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Threshold = None
        self._RequestId = None

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Threshold = params.get("Threshold")
        self._RequestId = params.get("RequestId")


class DescribeBizHttpStatusRequest(AbstractModel):
    """DescribeBizHttpStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Id: 资源Id
        :type Id: str
        :param _Period: 统计周期，可取值300，1800，3600， 21600，86400，单位秒
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Statistics: 统计方式，仅支持sum
        :type Statistics: str
        :param _ProtoInfo: 协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效
        :type ProtoInfo: list of ProtocolPort
        :param _Domain: 特定域名查询
        :type Domain: str
        """
        self._Business = None
        self._Id = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Statistics = None
        self._ProtoInfo = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def ProtoInfo(self):
        return self._ProtoInfo

    @ProtoInfo.setter
    def ProtoInfo(self, ProtoInfo):
        self._ProtoInfo = ProtoInfo

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Statistics = params.get("Statistics")
        if params.get("ProtoInfo") is not None:
            self._ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtoInfo.append(obj)
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizHttpStatusResponse(AbstractModel):
    """DescribeBizHttpStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HttpStatusMap: 业务流量http状态码统计数据
        :type HttpStatusMap: :class:`tencentcloud.dayu.v20180709.models.HttpStatusMap`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HttpStatusMap = None
        self._RequestId = None

    @property
    def HttpStatusMap(self):
        return self._HttpStatusMap

    @HttpStatusMap.setter
    def HttpStatusMap(self, HttpStatusMap):
        self._HttpStatusMap = HttpStatusMap

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HttpStatusMap") is not None:
            self._HttpStatusMap = HttpStatusMap()
            self._HttpStatusMap._deserialize(params.get("HttpStatusMap"))
        self._RequestId = params.get("RequestId")


class DescribeBizTrendRequest(AbstractModel):
    """DescribeBizTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _Period: 统计周期，可取值300，1800，3600，21600，86400，单位秒
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Statistics: 统计方式，可取值max, min, avg, sum, 如统计纬度是流量速率或包量速率，仅可取值max
        :type Statistics: str
        :param _MetricName: 统计纬度，可取值connum, new_conn, inactive_conn, intraffic, outtraffic, inpkg, outpkg, qps
        :type MetricName: str
        :param _ProtoInfo: 协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效
        :type ProtoInfo: list of ProtocolPort
        :param _Domain: 统计纬度为qps时，可选特定域名查询
        :type Domain: str
        """
        self._Business = None
        self._Id = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Statistics = None
        self._MetricName = None
        self._ProtoInfo = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def ProtoInfo(self):
        return self._ProtoInfo

    @ProtoInfo.setter
    def ProtoInfo(self, ProtoInfo):
        self._ProtoInfo = ProtoInfo

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Statistics = params.get("Statistics")
        self._MetricName = params.get("MetricName")
        if params.get("ProtoInfo") is not None:
            self._ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtoInfo.append(obj)
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizTrendResponse(AbstractModel):
    """DescribeBizTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataList: 曲线图各个时间点的值
        :type DataList: list of float
        :param _MetricName: 统计纬度
        :type MetricName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataList = None
        self._MetricName = None
        self._RequestId = None

    @property
    def DataList(self):
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataList = params.get("DataList")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeCCAlarmThresholdRequest(AbstractModel):
    """DescribeCCAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）
        :type Business: str
        :param _RsId: 资源ID,字符串类型
        :type RsId: str
        """
        self._Business = None
        self._RsId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCAlarmThresholdResponse(AbstractModel):
    """DescribeCCAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CCAlarmThreshold: CC告警阈值
        :type CCAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.CCAlarmThreshold`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CCAlarmThreshold = None
        self._RequestId = None

    @property
    def CCAlarmThreshold(self):
        return self._CCAlarmThreshold

    @CCAlarmThreshold.setter
    def CCAlarmThreshold(self, CCAlarmThreshold):
        self._CCAlarmThreshold = CCAlarmThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CCAlarmThreshold") is not None:
            self._CCAlarmThreshold = CCAlarmThreshold()
            self._CCAlarmThreshold._deserialize(params.get("CCAlarmThreshold"))
        self._RequestId = params.get("RequestId")


class DescribeCCEvListRequest(AbstractModel):
    """DescribeCCEvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _IpList: 资源实例的IP，当business不为basic时，如果IpList不为空则Id也必须不能为空；
        :type IpList: list of str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        """
        self._Business = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._IpList = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

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
        self._Business = params.get("Business")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCEvListResponse(AbstractModel):
    """DescribeCCEvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（shield表示棋牌盾；bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _IpList: 资源实例的IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpList: list of str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Data: CC攻击事件列表
        :type Data: list of CCEventRecord
        :param _Total: 总记录数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._IpList = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

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
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CCEventRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeCCFrequencyRulesRequest(AbstractModel):
    """DescribeCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleId: 7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；当填写时表示获取转发规则的访问频率控制规则；
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCFrequencyRulesResponse(AbstractModel):
    """DescribeCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CCFrequencyRuleList: 访问频率控制规则列表
        :type CCFrequencyRuleList: list of CCFrequencyRule
        :param _CCFrequencyRuleStatus: 访问频率控制规则开关状态，取值[on(开启)，off(关闭)]
        :type CCFrequencyRuleStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CCFrequencyRuleList = None
        self._CCFrequencyRuleStatus = None
        self._RequestId = None

    @property
    def CCFrequencyRuleList(self):
        return self._CCFrequencyRuleList

    @CCFrequencyRuleList.setter
    def CCFrequencyRuleList(self, CCFrequencyRuleList):
        self._CCFrequencyRuleList = CCFrequencyRuleList

    @property
    def CCFrequencyRuleStatus(self):
        return self._CCFrequencyRuleStatus

    @CCFrequencyRuleStatus.setter
    def CCFrequencyRuleStatus(self, CCFrequencyRuleStatus):
        self._CCFrequencyRuleStatus = CCFrequencyRuleStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CCFrequencyRuleList") is not None:
            self._CCFrequencyRuleList = []
            for item in params.get("CCFrequencyRuleList"):
                obj = CCFrequencyRule()
                obj._deserialize(item)
                self._CCFrequencyRuleList.append(obj)
        self._CCFrequencyRuleStatus = params.get("CCFrequencyRuleStatus")
        self._RequestId = params.get("RequestId")


class DescribeCCIpAllowDenyRequest(AbstractModel):
    """DescribeCCIpAllowDeny请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Type: 黑或白名单，取值[white(白名单)，black(黑名单)]
注意：此数组只能有一个值，不能同时获取黑名单和白名单
        :type Type: list of str
        :param _Limit: 分页参数
        :type Limit: int
        :param _Offset: 分页参数
        :type Offset: int
        :param _Protocol: 可选，代表HTTP协议或HTTPS协议的CC防护，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；
        :type Protocol: str
        """
        self._Business = None
        self._Id = None
        self._Type = None
        self._Limit = None
        self._Offset = None
        self._Protocol = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCIpAllowDenyResponse(AbstractModel):
    """DescribeCCIpAllowDeny返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 该字段被RecordList字段替代了，请不要使用
        :type Data: list of KeyValue
        :param _Total: 记录数
        :type Total: int
        :param _RecordList: 返回黑/白名单的记录，
"Key":"ip"时，"Value":值表示ip;
"Key":"domain"时， "Value":值表示域名;
"Key":"type"时，"Value":值表示黑白名单类型(white为白名单，block为黑名单);
"Key":"protocol"时，"Value":值表示CC防护的协议(http或https);
        :type RecordList: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RecordList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

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
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCSelfDefinePolicyRequest(AbstractModel):
    """DescribeCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgp高防包；bgp-multip共享包）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Limit: 拉取的条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._Business = None
        self._Id = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCSelfDefinePolicyResponse(AbstractModel):
    """DescribeCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 自定义规则总数
        :type Total: int
        :param _Policys: 策略列表
        :type Policys: list of CCPolicy
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Policys = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Policys(self):
        return self._Policys

    @Policys.setter
    def Policys(self, Policys):
        self._Policys = Policys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Policys") is not None:
            self._Policys = []
            for item in params.get("Policys"):
                obj = CCPolicy()
                obj._deserialize(item)
                self._Policys.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))]
        :type MetricName: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :type Id: str
        :param _Domain: 域名，可选
        :type Domain: str
        """
        self._Business = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Id: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))]
        :type MetricName: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Data: 值数组
        :type Data: list of int non-negative
        :param _Count: 值个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Count = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeCCUrlAllowRequest(AbstractModel):
    """DescribeCCUrlAllow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Type: 黑或白名单，取值[white(白名单)]，目前只支持白名单
注意：此数组只能有一个值，且只能为white
        :type Type: list of str
        :param _Limit: 分页参数
        :type Limit: int
        :param _Offset: 分页参数
        :type Offset: int
        :param _Protocol: 可选，代表HTTP协议或HTTPS协议的CC防护，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；
        :type Protocol: str
        """
        self._Business = None
        self._Id = None
        self._Type = None
        self._Limit = None
        self._Offset = None
        self._Protocol = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCUrlAllowResponse(AbstractModel):
    """DescribeCCUrlAllow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 该字段被RecordList字段替代了，请不要使用
        :type Data: list of KeyValue
        :param _Total: 记录总数
        :type Total: int
        :param _RecordList: 返回黑/白名单的记录，
"Key":"url"时，"Value":值表示URL;
"Key":"domain"时， "Value":值表示域名;
"Key":"type"时，"Value":值表示黑白名单类型(white为白名单，block为黑名单);
"Key":"protocol"时，"Value":值表示CC的防护类型(HTTP防护或HTTPS域名防护);
        :type RecordList: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RecordList = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RecordList(self):
        return self._RecordList

    @RecordList.setter
    def RecordList(self, RecordList):
        self._RecordList = RecordList

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
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("RecordList") is not None:
            self._RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._RecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAlarmThresholdRequest(AbstractModel):
    """DescribeDDoSAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）
        :type Business: str
        :param _RsId: 资源ID,字符串类型
        :type RsId: str
        """
        self._Business = None
        self._RsId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAlarmThresholdResponse(AbstractModel):
    """DescribeDDoSAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DDoSAlarmThreshold: DDoS告警阈值
        :type DDoSAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.DDoSAlarmThreshold`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DDoSAlarmThreshold = None
        self._RequestId = None

    @property
    def DDoSAlarmThreshold(self):
        return self._DDoSAlarmThreshold

    @DDoSAlarmThreshold.setter
    def DDoSAlarmThreshold(self, DDoSAlarmThreshold):
        self._DDoSAlarmThreshold = DDoSAlarmThreshold

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DDoSAlarmThreshold") is not None:
            self._DDoSAlarmThreshold = DDoSAlarmThreshold()
            self._DDoSAlarmThreshold._deserialize(params.get("DDoSAlarmThreshold"))
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackIPRegionMapRequest(AbstractModel):
    """DescribeDDoSAttackIPRegionMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间，最大可统计的时间范围是半年；
        :type EndTime: str
        :param _IpList: 指定资源的特定IP的攻击源，可选
        :type IpList: list of str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackIPRegionMapResponse(AbstractModel):
    """DescribeDDoSAttackIPRegionMap返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NationCount: 全球地域分布数据
        :type NationCount: list of KeyValueRecord
        :param _ProvinceCount: 国内省份地域分布数据
        :type ProvinceCount: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NationCount = None
        self._ProvinceCount = None
        self._RequestId = None

    @property
    def NationCount(self):
        return self._NationCount

    @NationCount.setter
    def NationCount(self, NationCount):
        self._NationCount = NationCount

    @property
    def ProvinceCount(self):
        return self._ProvinceCount

    @ProvinceCount.setter
    def ProvinceCount(self, ProvinceCount):
        self._ProvinceCount = ProvinceCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NationCount") is not None:
            self._NationCount = []
            for item in params.get("NationCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._NationCount.append(obj)
        if params.get("ProvinceCount") is not None:
            self._ProvinceCount = []
            for item in params.get("ProvinceCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._ProvinceCount.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSAttackSourceRequest(AbstractModel):
    """DescribeDDoSAttackSource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _IpList: 获取指定资源的特定ip的攻击源，可选
        :type IpList: list of str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSAttackSourceResponse(AbstractModel):
    """DescribeDDoSAttackSource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总攻击源条数
        :type Total: int
        :param _AttackSourceList: 攻击源列表
        :type AttackSourceList: list of DDoSAttackSourceRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AttackSourceList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AttackSourceList(self):
        return self._AttackSourceList

    @AttackSourceList.setter
    def AttackSourceList(self, AttackSourceList):
        self._AttackSourceList = AttackSourceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("AttackSourceList") is not None:
            self._AttackSourceList = []
            for item in params.get("AttackSourceList"):
                obj = DDoSAttackSourceRecord()
                obj._deserialize(item)
                self._AttackSourceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSCountRequest(AbstractModel):
    """DescribeDDoSCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]
        :type MetricName: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSCountResponse(AbstractModel):
    """DescribeDDoSCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]
        :type MetricName: str
        :param _Data: Key-Value值数组，Key说明如下，
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
key的值表示攻击事件类型，其中Key为"UNKNOWNFLOOD"，表示未知的攻击事件
        :type Data: list of KeyValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSDefendStatusRequest(AbstractModel):
    """DescribeDDoSDefendStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（basic表示基础防护；bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源实例ID，只有当Business不是基础防护时才需要填写此字段；
        :type Id: str
        :param _Ip: 基础防护的IP，只有当Business为基础防护时才需要填写此字段；
        :type Ip: str
        :param _BizType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]
        :type BizType: str
        :param _DeviceType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]
        :type DeviceType: str
        :param _InstanceId: 只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);
        :type InstanceId: str
        :param _IPRegion: 只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：
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
"nj":     南京
        :type IPRegion: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._IPRegion = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IPRegion(self):
        return self._IPRegion

    @IPRegion.setter
    def IPRegion(self, IPRegion):
        self._IPRegion = IPRegion


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._IPRegion = params.get("IPRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSDefendStatusResponse(AbstractModel):
    """DescribeDDoSDefendStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DefendStatus: 防护状态，为0表示防护处于关闭状态，为1表示防护处于开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DefendStatus: int
        :param _UndefendExpire: 防护临时关闭的过期时间，当防护状态为开启时此字段为空；
注意：此字段可能返回 null，表示取不到有效值。
        :type UndefendExpire: str
        :param _ShowFlag: 控制台功能展示字段，为1表示控制台功能展示，为0表示控制台功能隐藏
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowFlag: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DefendStatus = None
        self._UndefendExpire = None
        self._ShowFlag = None
        self._RequestId = None

    @property
    def DefendStatus(self):
        return self._DefendStatus

    @DefendStatus.setter
    def DefendStatus(self, DefendStatus):
        self._DefendStatus = DefendStatus

    @property
    def UndefendExpire(self):
        return self._UndefendExpire

    @UndefendExpire.setter
    def UndefendExpire(self, UndefendExpire):
        self._UndefendExpire = UndefendExpire

    @property
    def ShowFlag(self):
        return self._ShowFlag

    @ShowFlag.setter
    def ShowFlag(self, ShowFlag):
        self._ShowFlag = ShowFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DefendStatus = params.get("DefendStatus")
        self._UndefendExpire = params.get("UndefendExpire")
        self._ShowFlag = params.get("ShowFlag")
        self._RequestId = params.get("RequestId")


class DescribeDDoSEvInfoRequest(AbstractModel):
    """DescribeDDoSEvInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvInfoResponse(AbstractModel):
    """DescribeDDoSEvInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        :param _TcpPacketSum: TCP报文攻击包数
        :type TcpPacketSum: int
        :param _TcpKBSum: TCP报文攻击流量，单位KB
        :type TcpKBSum: int
        :param _UdpPacketSum: UDP报文攻击包数
        :type UdpPacketSum: int
        :param _UdpKBSum: UDP报文攻击流量，单位KB
        :type UdpKBSum: int
        :param _IcmpPacketSum: ICMP报文攻击包数
        :type IcmpPacketSum: int
        :param _IcmpKBSum: ICMP报文攻击流量，单位KB
        :type IcmpKBSum: int
        :param _OtherPacketSum: 其他报文攻击包数
        :type OtherPacketSum: int
        :param _OtherKBSum: 其他报文攻击流量，单位KB
        :type OtherKBSum: int
        :param _TotalTraffic: 累计攻击流量，单位KB
        :type TotalTraffic: int
        :param _Mbps: 攻击流量带宽峰值
        :type Mbps: int
        :param _Pps: 攻击包速率峰值
        :type Pps: int
        :param _PcapUrl: PCAP文件下载链接
        :type PcapUrl: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._TcpPacketSum = None
        self._TcpKBSum = None
        self._UdpPacketSum = None
        self._UdpKBSum = None
        self._IcmpPacketSum = None
        self._IcmpKBSum = None
        self._OtherPacketSum = None
        self._OtherKBSum = None
        self._TotalTraffic = None
        self._Mbps = None
        self._Pps = None
        self._PcapUrl = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def TcpPacketSum(self):
        return self._TcpPacketSum

    @TcpPacketSum.setter
    def TcpPacketSum(self, TcpPacketSum):
        self._TcpPacketSum = TcpPacketSum

    @property
    def TcpKBSum(self):
        return self._TcpKBSum

    @TcpKBSum.setter
    def TcpKBSum(self, TcpKBSum):
        self._TcpKBSum = TcpKBSum

    @property
    def UdpPacketSum(self):
        return self._UdpPacketSum

    @UdpPacketSum.setter
    def UdpPacketSum(self, UdpPacketSum):
        self._UdpPacketSum = UdpPacketSum

    @property
    def UdpKBSum(self):
        return self._UdpKBSum

    @UdpKBSum.setter
    def UdpKBSum(self, UdpKBSum):
        self._UdpKBSum = UdpKBSum

    @property
    def IcmpPacketSum(self):
        return self._IcmpPacketSum

    @IcmpPacketSum.setter
    def IcmpPacketSum(self, IcmpPacketSum):
        self._IcmpPacketSum = IcmpPacketSum

    @property
    def IcmpKBSum(self):
        return self._IcmpKBSum

    @IcmpKBSum.setter
    def IcmpKBSum(self, IcmpKBSum):
        self._IcmpKBSum = IcmpKBSum

    @property
    def OtherPacketSum(self):
        return self._OtherPacketSum

    @OtherPacketSum.setter
    def OtherPacketSum(self, OtherPacketSum):
        self._OtherPacketSum = OtherPacketSum

    @property
    def OtherKBSum(self):
        return self._OtherKBSum

    @OtherKBSum.setter
    def OtherKBSum(self, OtherKBSum):
        self._OtherKBSum = OtherKBSum

    @property
    def TotalTraffic(self):
        return self._TotalTraffic

    @TotalTraffic.setter
    def TotalTraffic(self, TotalTraffic):
        self._TotalTraffic = TotalTraffic

    @property
    def Mbps(self):
        return self._Mbps

    @Mbps.setter
    def Mbps(self, Mbps):
        self._Mbps = Mbps

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def PcapUrl(self):
        return self._PcapUrl

    @PcapUrl.setter
    def PcapUrl(self, PcapUrl):
        self._PcapUrl = PcapUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TcpPacketSum = params.get("TcpPacketSum")
        self._TcpKBSum = params.get("TcpKBSum")
        self._UdpPacketSum = params.get("UdpPacketSum")
        self._UdpKBSum = params.get("UdpKBSum")
        self._IcmpPacketSum = params.get("IcmpPacketSum")
        self._IcmpKBSum = params.get("IcmpKBSum")
        self._OtherPacketSum = params.get("OtherPacketSum")
        self._OtherKBSum = params.get("OtherKBSum")
        self._TotalTraffic = params.get("TotalTraffic")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._PcapUrl = params.get("PcapUrl")
        self._RequestId = params.get("RequestId")


class DescribeDDoSEvListRequest(AbstractModel):
    """DescribeDDoSEvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :type Id: str
        :param _IpList: 资源的IP
        :type IpList: list of str
        :param _OverLoad: 是否超过弹性防护峰值，取值[yes(是)，no(否)]，填写空字符串时表示不进行过滤
        :type OverLoad: str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        """
        self._Business = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._IpList = None
        self._OverLoad = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def OverLoad(self):
        return self._OverLoad

    @OverLoad.setter
    def OverLoad(self, OverLoad):
        self._OverLoad = OverLoad

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
        self._Business = params.get("Business")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._OverLoad = params.get("OverLoad")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSEvListResponse(AbstractModel):
    """DescribeDDoSEvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _IpList: 资源的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IpList: list of str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Data: DDoS攻击事件列表
        :type Data: list of DDoSEventRecord
        :param _Total: 总记录数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._IpList = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

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
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDDoSIpLogRequest(AbstractModel):
    """DescribeDDoSIpLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSIpLogResponse(AbstractModel):
    """DescribeDDoSIpLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        :param _Data: IP攻击日志，KeyValue数组，Key-Value取值说明：
Key为"LogTime"时，Value值为IP日志时间
Key为"LogMessage"时，Value值为Ip日志内容
        :type Data: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetCountRequest(AbstractModel):
    """DescribeDDoSNetCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]
        :type MetricName: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetCountResponse(AbstractModel):
    """DescribeDDoSNetCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[traffic（攻击协议流量, 单位KB）, pkg（攻击协议报文数）, classnum（攻击事件次数）]
        :type MetricName: str
        :param _Data: Key-Value值数组，Key说明如下，
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
key的值表示攻击事件类型，其中Key为"UNKNOWNFLOOD"，表示未知的攻击事件
        :type Data: list of KeyValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetEvInfoRequest(AbstractModel):
    """DescribeDDoSNetEvInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvInfoResponse(AbstractModel):
    """DescribeDDoSNetEvInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        :param _TcpPacketSum: TCP报文攻击包数
        :type TcpPacketSum: int
        :param _TcpKBSum: TCP报文攻击流量，单位KB
        :type TcpKBSum: int
        :param _UdpPacketSum: UDP报文攻击包数
        :type UdpPacketSum: int
        :param _UdpKBSum: UDP报文攻击流量，单位KB
        :type UdpKBSum: int
        :param _IcmpPacketSum: ICMP报文攻击包数
        :type IcmpPacketSum: int
        :param _IcmpKBSum: ICMP报文攻击流量，单位KB
        :type IcmpKBSum: int
        :param _OtherPacketSum: 其他报文攻击包数
        :type OtherPacketSum: int
        :param _OtherKBSum: 其他报文攻击流量，单位KB
        :type OtherKBSum: int
        :param _TotalTraffic: 累计攻击流量，单位KB
        :type TotalTraffic: int
        :param _Mbps: 攻击流量带宽峰值
        :type Mbps: int
        :param _Pps: 攻击包速率峰值
        :type Pps: int
        :param _PcapUrl: PCAP文件下载链接
        :type PcapUrl: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._TcpPacketSum = None
        self._TcpKBSum = None
        self._UdpPacketSum = None
        self._UdpKBSum = None
        self._IcmpPacketSum = None
        self._IcmpKBSum = None
        self._OtherPacketSum = None
        self._OtherKBSum = None
        self._TotalTraffic = None
        self._Mbps = None
        self._Pps = None
        self._PcapUrl = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def TcpPacketSum(self):
        return self._TcpPacketSum

    @TcpPacketSum.setter
    def TcpPacketSum(self, TcpPacketSum):
        self._TcpPacketSum = TcpPacketSum

    @property
    def TcpKBSum(self):
        return self._TcpKBSum

    @TcpKBSum.setter
    def TcpKBSum(self, TcpKBSum):
        self._TcpKBSum = TcpKBSum

    @property
    def UdpPacketSum(self):
        return self._UdpPacketSum

    @UdpPacketSum.setter
    def UdpPacketSum(self, UdpPacketSum):
        self._UdpPacketSum = UdpPacketSum

    @property
    def UdpKBSum(self):
        return self._UdpKBSum

    @UdpKBSum.setter
    def UdpKBSum(self, UdpKBSum):
        self._UdpKBSum = UdpKBSum

    @property
    def IcmpPacketSum(self):
        return self._IcmpPacketSum

    @IcmpPacketSum.setter
    def IcmpPacketSum(self, IcmpPacketSum):
        self._IcmpPacketSum = IcmpPacketSum

    @property
    def IcmpKBSum(self):
        return self._IcmpKBSum

    @IcmpKBSum.setter
    def IcmpKBSum(self, IcmpKBSum):
        self._IcmpKBSum = IcmpKBSum

    @property
    def OtherPacketSum(self):
        return self._OtherPacketSum

    @OtherPacketSum.setter
    def OtherPacketSum(self, OtherPacketSum):
        self._OtherPacketSum = OtherPacketSum

    @property
    def OtherKBSum(self):
        return self._OtherKBSum

    @OtherKBSum.setter
    def OtherKBSum(self, OtherKBSum):
        self._OtherKBSum = OtherKBSum

    @property
    def TotalTraffic(self):
        return self._TotalTraffic

    @TotalTraffic.setter
    def TotalTraffic(self, TotalTraffic):
        self._TotalTraffic = TotalTraffic

    @property
    def Mbps(self):
        return self._Mbps

    @Mbps.setter
    def Mbps(self, Mbps):
        self._Mbps = Mbps

    @property
    def Pps(self):
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def PcapUrl(self):
        return self._PcapUrl

    @PcapUrl.setter
    def PcapUrl(self, PcapUrl):
        self._PcapUrl = PcapUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TcpPacketSum = params.get("TcpPacketSum")
        self._TcpKBSum = params.get("TcpKBSum")
        self._UdpPacketSum = params.get("UdpPacketSum")
        self._UdpKBSum = params.get("UdpKBSum")
        self._IcmpPacketSum = params.get("IcmpPacketSum")
        self._IcmpKBSum = params.get("IcmpKBSum")
        self._OtherPacketSum = params.get("OtherPacketSum")
        self._OtherKBSum = params.get("OtherKBSum")
        self._TotalTraffic = params.get("TotalTraffic")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._PcapUrl = params.get("PcapUrl")
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetEvListRequest(AbstractModel):
    """DescribeDDoSNetEvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetEvListResponse(AbstractModel):
    """DescribeDDoSNetEvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Data: DDoS攻击事件列表
        :type Data: list of DDoSEventRecord
        :param _Total: 总记录数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetIpLogRequest(AbstractModel):
    """DescribeDDoSNetIpLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetIpLogResponse(AbstractModel):
    """DescribeDDoSNetIpLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _StartTime: 攻击开始时间
        :type StartTime: str
        :param _EndTime: 攻击结束时间
        :type EndTime: str
        :param _Data: IP攻击日志，KeyValue数组，Key-Value取值说明：
Key为"LogTime"时，Value值为IP日志时间
Key为"LogMessage"时，Value值为Ip日志内容
        :type Data: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSNetTrendRequest(AbstractModel):
    """DescribeDDoSNetTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSNetTrendResponse(AbstractModel):
    """DescribeDDoSNetTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Data: 值数组
        :type Data: list of int non-negative
        :param _Count: 值个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Count = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 可选字段，资源ID，如果填写则表示该资源绑定的DDoS高级策略
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSPolicyResponse(AbstractModel):
    """DescribeDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DDosPolicyList: DDoS高级策略列表
        :type DDosPolicyList: list of DDosPolicy
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DDosPolicyList = None
        self._RequestId = None

    @property
    def DDosPolicyList(self):
        return self._DDosPolicyList

    @DDosPolicyList.setter
    def DDosPolicyList(self, DDosPolicyList):
        self._DDosPolicyList = DDosPolicyList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DDosPolicyList") is not None:
            self._DDosPolicyList = []
            for item in params.get("DDosPolicyList"):
                obj = DDosPolicy()
                obj._deserialize(item)
                self._DDosPolicyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Ip: 资源实例的IP
        :type Ip: str
        :param _MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :type Id: str
        """
        self._Business = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Id: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Data: 值数组，攻击流量带宽单位为Mbps，包速率单位为pps
        :type Data: list of int non-negative
        :param _Count: 值个数
        :type Count: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Business = None
        self._Id = None
        self._Ip = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Count = None
        self._RequestId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeDDoSUsedStatisRequest(AbstractModel):
    """DescribeDDoSUsedStatis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        """
        self._Business = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSUsedStatisResponse(AbstractModel):
    """DescribeDDoSUsedStatis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 字段值，如下：
Days：高防资源使用天数
Attacks：DDoS防护次数
        :type Data: list of KeyValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIPProductInfoRequest(AbstractModel):
    """DescribeIPProductInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包）
        :type Business: str
        :param _IpList: IP列表
        :type IpList: list of str
        """
        self._Business = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPProductInfoResponse(AbstractModel):
    """DescribeIPProductInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 云产品信息列表，如果没有查询到则返回空数组，值说明如下：
Key为ProductName时，value表示云产品实例的名称；
Key为ProductInstanceId时，value表示云产品实例的ID；
Key为ProductType时，value表示的是云产品的类型（cvm表示云主机、clb表示负载均衡）;
Key为IP时，value表示云产品实例的IP；
        :type Data: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInsurePacksRequest(AbstractModel):
    """DescribeInsurePacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdList: 可选字段，保险包套餐ID，当要获取指定ID（例如insure-000000xe）的保险包套餐时请填写此字段；
        :type IdList: list of str
        """
        self._IdList = None

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInsurePacksResponse(AbstractModel):
    """DescribeInsurePacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InsurePacks: 保险包套餐列表
        :type InsurePacks: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InsurePacks = None
        self._RequestId = None

    @property
    def InsurePacks(self):
        return self._InsurePacks

    @InsurePacks.setter
    def InsurePacks(self, InsurePacks):
        self._InsurePacks = InsurePacks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InsurePacks") is not None:
            self._InsurePacks = []
            for item in params.get("InsurePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._InsurePacks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpBlockListRequest(AbstractModel):
    """DescribeIpBlockList请求参数结构体

    """


class DescribeIpBlockListResponse(AbstractModel):
    """DescribeIpBlockList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: IP封堵列表
        :type List: list of IpBlockData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = IpBlockData()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpUnBlockListRequest(AbstractModel):
    """DescribeIpUnBlockList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 开始时间
        :type BeginTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Ip: IP（不为空时，进行IP过滤）
        :type Ip: str
        :param _Paging: 分页参数（不为空时，进行分页查询），此字段后面会弃用，请用Limit和Offset字段代替；
        :type Paging: :class:`tencentcloud.dayu.v20180709.models.Paging`
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._Ip = None
        self._Paging = None
        self._Limit = None
        self._Offset = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Paging(self):
        return self._Paging

    @Paging.setter
    def Paging(self, Paging):
        self._Paging = Paging

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
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Ip = params.get("Ip")
        if params.get("Paging") is not None:
            self._Paging = Paging()
            self._Paging._deserialize(params.get("Paging"))
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpUnBlockListResponse(AbstractModel):
    """DescribeIpUnBlockList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 开始时间
        :type BeginTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _List: IP解封记录
        :type List: list of IpUnBlockData
        :param _Total: 总记录数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BeginTime = None
        self._EndTime = None
        self._List = None
        self._Total = None
        self._RequestId = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = IpUnBlockData()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeL4HealthConfigRequest(AbstractModel):
    """DescribeL4HealthConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleIdList: 规则ID数组，当导出所有规则的健康检查配置则不填或填空数组；
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4HealthConfigResponse(AbstractModel):
    """DescribeL4HealthConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthConfig: 四层健康检查配置数组
        :type HealthConfig: list of L4HealthConfig
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthConfig = None
        self._RequestId = None

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL4RulesErrHealthRequest(AbstractModel):
    """DescribeL4RulesErrHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL4RulesErrHealthResponse(AbstractModel):
    """DescribeL4RulesErrHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 异常规则的总数
        :type Total: int
        :param _ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP，多个IP用","分割
        :type ErrHealths: list of KeyValue
        :param _ExtErrHealths: 异常规则列表(提供更多的错误相关信息)，返回值说明:
Key值为RuleId时，Value值为规则ID；
Key值为Protocol时，Value值为规则的转发协议；
Key值为VirtualPort时，Value值为规则的转发端口；
Key值为ErrMessage时，Value值为健康检查异常信息；
健康检查异常信息的格式为"SourceIp:1.1.1.1|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6" 多个源IP的错误信息用，分割,
SourceIp表示源站IP，SourcePort表示源站端口，AbnormalStatTime表示异常时间，AbnormalReason表示异常原因，Interval表示检查周期，CheckNum表示检查次数，FailNum表示失败次数；
        :type ExtErrHealths: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ErrHealths = None
        self._ExtErrHealths = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ErrHealths(self):
        return self._ErrHealths

    @ErrHealths.setter
    def ErrHealths(self, ErrHealths):
        self._ErrHealths = ErrHealths

    @property
    def ExtErrHealths(self):
        return self._ExtErrHealths

    @ExtErrHealths.setter
    def ExtErrHealths(self, ExtErrHealths):
        self._ExtErrHealths = ExtErrHealths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self._ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ErrHealths.append(obj)
        if params.get("ExtErrHealths") is not None:
            self._ExtErrHealths = []
            for item in params.get("ExtErrHealths"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._ExtErrHealths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7HealthConfigRequest(AbstractModel):
    """DescribeL7HealthConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleIdList: 规则ID数组，当导出所有规则的健康检查配置则不填或填空数组；
        :type RuleIdList: list of str
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7HealthConfigResponse(AbstractModel):
    """DescribeL7HealthConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthConfig: 七层健康检查配置数组
        :type HealthConfig: list of L7HealthConfig
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthConfig = None
        self._RequestId = None

    @property
    def HealthConfig(self):
        return self._HealthConfig

    @HealthConfig.setter
    def HealthConfig(self, HealthConfig):
        self._HealthConfig = HealthConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self._HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self._HealthConfig.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNewL4RulesErrHealthRequest(AbstractModel):
    """DescribeNewL4RulesErrHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _RuleIdList: 规则ID列表
        :type RuleIdList: list of str
        """
        self._Business = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL4RulesErrHealthResponse(AbstractModel):
    """DescribeNewL4RulesErrHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 异常规则的总数
        :type Total: int
        :param _ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP，多个IP用","分割
        :type ErrHealths: list of KeyValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ErrHealths = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ErrHealths(self):
        return self._ErrHealths

    @ErrHealths.setter
    def ErrHealths(self, ErrHealths):
        self._ErrHealths = ErrHealths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self._ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ErrHealths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNewL4RulesRequest(AbstractModel):
    """DescribeNewL4Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Ip: 指定IP查询
        :type Ip: str
        :param _VirtualPort: 指定高防IP端口查询
        :type VirtualPort: int
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        """
        self._Business = None
        self._Ip = None
        self._VirtualPort = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

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
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._VirtualPort = params.get("VirtualPort")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL4RulesResponse(AbstractModel):
    """DescribeNewL4Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 转发规则列表
        :type Rules: list of NewL4RuleEntry
        :param _Total: 总规则数
        :type Total: int
        :param _Healths: 四层健康检查配置列表
        :type Healths: list of L4RuleHealth
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._Total = None
        self._Healths = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = NewL4RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNewL7RulesErrHealthRequest(AbstractModel):
    """DescribeNewL7RulesErrHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP)
        :type Business: str
        :param _RuleIdList: 规则Id列表
        :type RuleIdList: list of str
        """
        self._Business = None
        self._RuleIdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesErrHealthResponse(AbstractModel):
    """DescribeNewL7RulesErrHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 异常规则的总数
        :type Total: int
        :param _ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP及错误信息，多个IP用","分割
        :type ErrHealths: list of KeyValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ErrHealths = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ErrHealths(self):
        return self._ErrHealths

    @ErrHealths.setter
    def ErrHealths(self, ErrHealths):
        self._ErrHealths = ErrHealths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self._ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ErrHealths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePackIndexRequest(AbstractModel):
    """DescribePackIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示高防包；net表示高防IP专业版）
        :type Business: str
        """
        self._Business = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackIndexResponse(AbstractModel):
    """DescribePackIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 字段值，如下：
TotalPackCount：资源数
AttackPackCount：清洗中的资源数
BlockPackCount：封堵中的资源数
ExpiredPackCount：过期的资源数
ExpireingPackCount：即将过期的资源数
IsolatePackCount：隔离中的资源数
        :type Data: list of KeyValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePcapRequest(AbstractModel):
    """DescribePcap请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _StartTime: 攻击事件的开始时间，格式为"2018-08-28 07:00:00"
        :type StartTime: str
        :param _EndTime: 攻击事件的结束时间，格式为"2018-08-28 07:02:00"
        :type EndTime: str
        :param _Ip: 资源的IP，只有当Business为net时才需要填写资源实例下的IP；
        :type Ip: str
        """
        self._Business = None
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Ip = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePcapResponse(AbstractModel):
    """DescribePcap返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PcapUrlList: pcap包的下载链接列表，无pcap包时为空数组；
        :type PcapUrlList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PcapUrlList = None
        self._RequestId = None

    @property
    def PcapUrlList(self):
        return self._PcapUrlList

    @PcapUrlList.setter
    def PcapUrlList(self, PcapUrlList):
        self._PcapUrlList = PcapUrlList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PcapUrlList = params.get("PcapUrlList")
        self._RequestId = params.get("RequestId")


class DescribePolicyCaseRequest(AbstractModel):
    """DescribePolicyCase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _SceneId: 策略场景ID
        :type SceneId: str
        """
        self._Business = None
        self._SceneId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._SceneId = params.get("SceneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyCaseResponse(AbstractModel):
    """DescribePolicyCase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaseList: 策略场景列表
        :type CaseList: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaseList = None
        self._RequestId = None

    @property
    def CaseList(self):
        return self._CaseList

    @CaseList.setter
    def CaseList(self, CaseList):
        self._CaseList = CaseList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CaseList") is not None:
            self._CaseList = []
            for item in params.get("CaseList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._CaseList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResIpListRequest(AbstractModel):
    """DescribeResIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _IdList: 资源ID, 如果不填，则获取用户所有资源的IP
        :type IdList: list of str
        """
        self._Business = None
        self._IdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResIpListResponse(AbstractModel):
    """DescribeResIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Resource: 资源的IP列表
        :type Resource: list of ResourceIp
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Resource = None
        self._RequestId = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self._Resource = []
            for item in params.get("Resource"):
                obj = ResourceIp()
                obj._deserialize(item)
                self._Resource.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceListRequest(AbstractModel):
    """DescribeResourceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _RegionList: 地域码搜索，可选，当不指定地域时空数组，当指定地域时，填地域码。例如：["gz", "sh"]
        :type RegionList: list of str
        :param _Line: 线路搜索，可选，只有当获取高防IP资源列表是可以选填，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]，当获取其他产品时请填空数组；
        :type Line: list of int non-negative
        :param _IdList: 资源ID搜索，可选，当不为空数组时表示获取指定资源的资源列表；
        :type IdList: list of str
        :param _Name: 资源名称搜索，可选，当不为空字符串时表示按名称搜索资源；
        :type Name: str
        :param _IpList: IP搜索列表，可选，当不为空时表示按照IP搜索资源；
        :type IpList: list of str
        :param _Status: 资源状态搜索列表，可选，取值为[0（运行中）, 1（清洗中）, 2（封堵中）]，当填空数组时不进行状态搜索；
        :type Status: list of int non-negative
        :param _Expire: 即将到期搜索；可选，取值为[0（不搜索），1（搜索即将到期的资源）]
        :type Expire: int
        :param _OderBy: 排序字段，可选
        :type OderBy: list of OrderBy
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _CName: 高防IP专业版资源的CNAME，可选，只对高防IP专业版资源列表有效；
        :type CName: str
        :param _Domain: 高防IP专业版资源的域名，可选，只对高防IP专业版资源列表有效；
        :type Domain: str
        """
        self._Business = None
        self._RegionList = None
        self._Line = None
        self._IdList = None
        self._Name = None
        self._IpList = None
        self._Status = None
        self._Expire = None
        self._OderBy = None
        self._Limit = None
        self._Offset = None
        self._CName = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def Line(self):
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Expire(self):
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def OderBy(self):
        return self._OderBy

    @OderBy.setter
    def OderBy(self, OderBy):
        self._OderBy = OderBy

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
    def CName(self):
        return self._CName

    @CName.setter
    def CName(self, CName):
        self._CName = CName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RegionList = params.get("RegionList")
        self._Line = params.get("Line")
        self._IdList = params.get("IdList")
        self._Name = params.get("Name")
        self._IpList = params.get("IpList")
        self._Status = params.get("Status")
        self._Expire = params.get("Expire")
        if params.get("OderBy") is not None:
            self._OderBy = []
            for item in params.get("OderBy"):
                obj = OrderBy()
                obj._deserialize(item)
                self._OderBy.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CName = params.get("CName")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceListResponse(AbstractModel):
    """DescribeResourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总记录数
        :type Total: int
        :param _ServicePacks: 资源记录列表，返回Key值说明：
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
"Key": "ServiceBandwidth" 表示资源实例的保底业务带宽，只针对高防IP专业版
        :type ServicePacks: list of KeyValueRecord
        :param _Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ServicePacks = None
        self._Business = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ServicePacks(self):
        return self._ServicePacks

    @ServicePacks.setter
    def ServicePacks(self, ServicePacks):
        self._ServicePacks = ServicePacks

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ServicePacks") is not None:
            self._ServicePacks = []
            for item in params.get("ServicePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._ServicePacks.append(obj)
        self._Business = params.get("Business")
        self._RequestId = params.get("RequestId")


class DescribeRuleSetsRequest(AbstractModel):
    """DescribeRuleSets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _IdList: 资源ID列表
        :type IdList: list of str
        """
        self._Business = None
        self._IdList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleSetsResponse(AbstractModel):
    """DescribeRuleSets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _L4RuleSets: 规则记录数数组，取值说明:
Key值为"Id"时，Value表示资源ID
Key值为"RuleIdList"时，Value值表示资源的规则ID，多个规则ID用","分割
Key值为"RuleNameList"时，Value值表示资源的规则名，多个规则名用","分割
Key值为"RuleNum"时，Value值表示资源的规则数
        :type L4RuleSets: list of KeyValueRecord
        :param _L7RuleSets: 规则记录数数组，取值说明:
Key值为"Id"时，Value表示资源ID
Key值为"RuleIdList"时，Value值表示资源的规则ID，多个规则ID用","分割
Key值为"RuleNameList"时，Value值表示资源的规则名，多个规则名用","分割
Key值为"RuleNum"时，Value值表示资源的规则数
        :type L7RuleSets: list of KeyValueRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._L4RuleSets = None
        self._L7RuleSets = None
        self._RequestId = None

    @property
    def L4RuleSets(self):
        return self._L4RuleSets

    @L4RuleSets.setter
    def L4RuleSets(self, L4RuleSets):
        self._L4RuleSets = L4RuleSets

    @property
    def L7RuleSets(self):
        return self._L7RuleSets

    @L7RuleSets.setter
    def L7RuleSets(self, L7RuleSets):
        self._L7RuleSets = L7RuleSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("L4RuleSets") is not None:
            self._L4RuleSets = []
            for item in params.get("L4RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._L4RuleSets.append(obj)
        if params.get("L7RuleSets") is not None:
            self._L7RuleSets = []
            for item in params.get("L7RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self._L7RuleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSchedulingDomainListRequest(AbstractModel):
    """DescribeSchedulingDomainList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Domain: 可选，筛选特定的域名
        :type Domain: str
        """
        self._Limit = None
        self._Offset = None
        self._Domain = None

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
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSchedulingDomainListResponse(AbstractModel):
    """DescribeSchedulingDomainList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 调度域名总数
        :type Total: int
        :param _DomainList: 调度域名列表信息
        :type DomainList: list of SchedulingDomain
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DomainList = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = SchedulingDomain()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecIndexRequest(AbstractModel):
    """DescribeSecIndex请求参数结构体

    """


class DescribeSecIndexResponse(AbstractModel):
    """DescribeSecIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 字段值，如下：
AttackIpCount：受攻击的IP数
AttackCount：攻击次数
BlockCount：封堵次数
MaxMbps：攻击峰值Mbps
IpNum：统计的IP数据
        :type Data: list of KeyValue
        :param _BeginDate: 本月开始时间
        :type BeginDate: str
        :param _EndDate: 本月结束时间
        :type EndDate: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._BeginDate = None
        self._EndDate = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

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
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        self._RequestId = params.get("RequestId")


class DescribeSourceIpSegmentRequest(AbstractModel):
    """DescribeSourceIpSegment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        """
        self._Business = None
        self._Id = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceIpSegmentResponse(AbstractModel):
    """DescribeSourceIpSegment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 回源IP段，多个用"；"分隔
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeTransmitStatisRequest(AbstractModel):
    """DescribeTransmitStatis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版；bgp表示独享包；bgp-multip表示共享包）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _MetricName: 指标名，取值：
traffic表示流量带宽；
pkg表示包速率；
        :type MetricName: str
        :param _Period: 统计时间粒度（300表示5分钟；3600表示小时；86400表示天）
        :type Period: int
        :param _StartTime: 统计开始时间，秒部分保持为0，分钟部分为5的倍数
        :type StartTime: str
        :param _EndTime: 统计结束时间，秒部分保持为0，分钟部分为5的倍数
        :type EndTime: str
        :param _IpList: 资源的IP（当Business为bgp-multip时必填，且仅支持一个IP）；当不填写时，默认统计资源实例的所有IP；资源实例有多个IP（比如高防IP专业版）时，统计方式是求和；
        :type IpList: list of str
        """
        self._Business = None
        self._Id = None
        self._MetricName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

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
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTransmitStatisResponse(AbstractModel):
    """DescribeTransmitStatis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InDataList: 当MetricName=traffic时，表示入流量带宽，单位bps；
当MetricName=pkg时，表示入包速率，单位pps；
        :type InDataList: list of float
        :param _OutDataList: 当MetricName=traffic时，表示出流量带宽，单位bps；
当MetricName=pkg时，表示出包速率，单位pps；
        :type OutDataList: list of float
        :param _MetricName: 指标名：
traffic表示流量带宽；
pkg表示包速率；
        :type MetricName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InDataList = None
        self._OutDataList = None
        self._MetricName = None
        self._RequestId = None

    @property
    def InDataList(self):
        return self._InDataList

    @InDataList.setter
    def InDataList(self, InDataList):
        self._InDataList = InDataList

    @property
    def OutDataList(self):
        return self._OutDataList

    @OutDataList.setter
    def OutDataList(self, OutDataList):
        self._OutDataList = OutDataList

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InDataList = params.get("InDataList")
        self._OutDataList = params.get("OutDataList")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeUnBlockStatisRequest(AbstractModel):
    """DescribeUnBlockStatis请求参数结构体

    """


class DescribeUnBlockStatisResponse(AbstractModel):
    """DescribeUnBlockStatis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 解封总配额数
        :type Total: int
        :param _Used: 已使用次数
        :type Used: int
        :param _BeginTime: 统计起始时间
        :type BeginTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Used = None
        self._BeginTime = None
        self._EndTime = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._RequestId = params.get("RequestId")


class DescribleL4RulesRequest(AbstractModel):
    """DescribleL4Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleIdList: 规则ID，可选参数，填写后获取指定的规则
        :type RuleIdList: list of str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None
        self._Limit = None
        self._Offset = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList

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
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL4RulesResponse(AbstractModel):
    """DescribleL4Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 转发规则列表
        :type Rules: list of L4RuleEntry
        :param _Total: 总规则数
        :type Total: int
        :param _Healths: 健康检查配置列表
        :type Healths: list of L4RuleHealth
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._Total = None
        self._Healths = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribleL7RulesRequest(AbstractModel):
    """DescribleL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleIdList: 规则ID，可选参数，填写后获取指定的规则
        :type RuleIdList: list of str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Domain: 域名搜索，选填，当需要搜索域名请填写
        :type Domain: str
        :param _ProtocolList: 转发协议搜索，选填，取值[http, https, http/https]
        :type ProtocolList: list of str
        :param _StatusList: 状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type StatusList: list of int non-negative
        """
        self._Business = None
        self._Id = None
        self._RuleIdList = None
        self._Limit = None
        self._Offset = None
        self._Domain = None
        self._ProtocolList = None
        self._StatusList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList

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
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProtocolList(self):
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def StatusList(self):
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleIdList = params.get("RuleIdList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Domain = params.get("Domain")
        self._ProtocolList = params.get("ProtocolList")
        self._StatusList = params.get("StatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleL7RulesResponse(AbstractModel):
    """DescribleL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 转发规则列表
        :type Rules: list of L7RuleEntry
        :param _Total: 总规则数
        :type Total: int
        :param _Healths: 健康检查配置列表
        :type Healths: list of L7RuleHealth
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._Total = None
        self._Healths = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribleNewL7RulesRequest(AbstractModel):
    """DescribleNewL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Domain: 域名搜索，选填，当需要搜索域名请填写
        :type Domain: str
        :param _ProtocolList: 转发协议搜索，选填，取值[http, https, http/https]
        :type ProtocolList: list of str
        :param _StatusList: 状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type StatusList: list of int non-negative
        :param _Ip: IP搜索，选填，当需要搜索IP请填写
        :type Ip: str
        """
        self._Business = None
        self._Limit = None
        self._Offset = None
        self._Domain = None
        self._ProtocolList = None
        self._StatusList = None
        self._Ip = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

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
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProtocolList(self):
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def StatusList(self):
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Domain = params.get("Domain")
        self._ProtocolList = params.get("ProtocolList")
        self._StatusList = params.get("StatusList")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleNewL7RulesResponse(AbstractModel):
    """DescribleNewL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 转发规则列表
        :type Rules: list of NewL7RuleEntry
        :param _Total: 总规则数
        :type Total: int
        :param _Healths: 健康检查配置列表
        :type Healths: list of L7RuleHealth
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._Total = None
        self._Healths = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = NewL7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._RequestId = params.get("RequestId")


class DescribleRegionCountRequest(AbstractModel):
    """DescribleRegionCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；）
        :type Business: str
        :param _LineList: 根据线路统计，取值为[1（BGP线路），2（南京电信），3（南京联通），99（第三方合作线路）]；只对高防IP产品有效，其他产品此字段忽略
        :type LineList: list of int non-negative
        """
        self._Business = None
        self._LineList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def LineList(self):
        return self._LineList

    @LineList.setter
    def LineList(self, LineList):
        self._LineList = LineList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._LineList = params.get("LineList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribleRegionCountResponse(AbstractModel):
    """DescribleRegionCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionList: 地域资源实例数
        :type RegionList: list of RegionInstanceCount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionList = None
        self._RequestId = None

    @property
    def RegionList(self):
        return self._RegionList

    @RegionList.setter
    def RegionList(self, RegionList):
        self._RegionList = RegionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self._RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInstanceCount()
                obj._deserialize(item)
                self._RegionList.append(obj)
        self._RequestId = params.get("RequestId")


class HttpStatusMap(AbstractModel):
    """业务流量的http状态码聚合数据

    """

    def __init__(self):
        r"""
        :param _Http2xx: http2xx状态码
        :type Http2xx: list of float
        :param _Http3xx: http3xx状态码
        :type Http3xx: list of float
        :param _Http404: http404状态码
        :type Http404: list of float
        :param _Http4xx: http4xx状态码
        :type Http4xx: list of float
        :param _Http5xx: http5xx状态码
        :type Http5xx: list of float
        :param _SourceHttp2xx: http2xx回源状态码
        :type SourceHttp2xx: list of float
        :param _SourceHttp3xx: http3xx回源状态码
        :type SourceHttp3xx: list of float
        :param _SourceHttp404: http404回源状态码
        :type SourceHttp404: list of float
        :param _SourceHttp4xx: http4xx回源状态码
        :type SourceHttp4xx: list of float
        :param _SourceHttp5xx: http5xx回源状态码
        :type SourceHttp5xx: list of float
        """
        self._Http2xx = None
        self._Http3xx = None
        self._Http404 = None
        self._Http4xx = None
        self._Http5xx = None
        self._SourceHttp2xx = None
        self._SourceHttp3xx = None
        self._SourceHttp404 = None
        self._SourceHttp4xx = None
        self._SourceHttp5xx = None

    @property
    def Http2xx(self):
        return self._Http2xx

    @Http2xx.setter
    def Http2xx(self, Http2xx):
        self._Http2xx = Http2xx

    @property
    def Http3xx(self):
        return self._Http3xx

    @Http3xx.setter
    def Http3xx(self, Http3xx):
        self._Http3xx = Http3xx

    @property
    def Http404(self):
        return self._Http404

    @Http404.setter
    def Http404(self, Http404):
        self._Http404 = Http404

    @property
    def Http4xx(self):
        return self._Http4xx

    @Http4xx.setter
    def Http4xx(self, Http4xx):
        self._Http4xx = Http4xx

    @property
    def Http5xx(self):
        return self._Http5xx

    @Http5xx.setter
    def Http5xx(self, Http5xx):
        self._Http5xx = Http5xx

    @property
    def SourceHttp2xx(self):
        return self._SourceHttp2xx

    @SourceHttp2xx.setter
    def SourceHttp2xx(self, SourceHttp2xx):
        self._SourceHttp2xx = SourceHttp2xx

    @property
    def SourceHttp3xx(self):
        return self._SourceHttp3xx

    @SourceHttp3xx.setter
    def SourceHttp3xx(self, SourceHttp3xx):
        self._SourceHttp3xx = SourceHttp3xx

    @property
    def SourceHttp404(self):
        return self._SourceHttp404

    @SourceHttp404.setter
    def SourceHttp404(self, SourceHttp404):
        self._SourceHttp404 = SourceHttp404

    @property
    def SourceHttp4xx(self):
        return self._SourceHttp4xx

    @SourceHttp4xx.setter
    def SourceHttp4xx(self, SourceHttp4xx):
        self._SourceHttp4xx = SourceHttp4xx

    @property
    def SourceHttp5xx(self):
        return self._SourceHttp5xx

    @SourceHttp5xx.setter
    def SourceHttp5xx(self, SourceHttp5xx):
        self._SourceHttp5xx = SourceHttp5xx


    def _deserialize(self, params):
        self._Http2xx = params.get("Http2xx")
        self._Http3xx = params.get("Http3xx")
        self._Http404 = params.get("Http404")
        self._Http4xx = params.get("Http4xx")
        self._Http5xx = params.get("Http5xx")
        self._SourceHttp2xx = params.get("SourceHttp2xx")
        self._SourceHttp3xx = params.get("SourceHttp3xx")
        self._SourceHttp404 = params.get("SourceHttp404")
        self._SourceHttp4xx = params.get("SourceHttp4xx")
        self._SourceHttp5xx = params.get("SourceHttp5xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlackWhite(AbstractModel):
    """黑白IP

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _Type: 黑白类型，取值范围[black，white]
        :type Type: str
        """
        self._Ip = None
        self._Type = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlockData(AbstractModel):
    """IP封堵记录

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _Status: 状态（Blocked：被封堵；UnBlocking：解封中；UnBlockFailed：解封失败）
        :type Status: str
        :param _BlockTime: 封堵时间
        :type BlockTime: str
        :param _UnBlockTime: 解封时间（预计解封时间）
        :type UnBlockTime: str
        :param _ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）
        :type ActionType: str
        :param _ProtectFlag: 高防标记，0：非高防，1：高防
        :type ProtectFlag: int
        """
        self._Ip = None
        self._Status = None
        self._BlockTime = None
        self._UnBlockTime = None
        self._ActionType = None
        self._ProtectFlag = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BlockTime(self):
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def UnBlockTime(self):
        return self._UnBlockTime

    @UnBlockTime.setter
    def UnBlockTime(self, UnBlockTime):
        self._UnBlockTime = UnBlockTime

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProtectFlag(self):
        return self._ProtectFlag

    @ProtectFlag.setter
    def ProtectFlag(self, ProtectFlag):
        self._ProtectFlag = ProtectFlag


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Status = params.get("Status")
        self._BlockTime = params.get("BlockTime")
        self._UnBlockTime = params.get("UnBlockTime")
        self._ActionType = params.get("ActionType")
        self._ProtectFlag = params.get("ProtectFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpUnBlockData(AbstractModel):
    """IP解封记录

    """

    def __init__(self):
        r"""
        :param _Ip: IP
        :type Ip: str
        :param _BlockTime: 封堵时间
        :type BlockTime: str
        :param _UnBlockTime: 解封时间（实际解封时间）
        :type UnBlockTime: str
        :param _ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）
        :type ActionType: str
        """
        self._Ip = None
        self._BlockTime = None
        self._UnBlockTime = None
        self._ActionType = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BlockTime(self):
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def UnBlockTime(self):
        return self._UnBlockTime

    @UnBlockTime.setter
    def UnBlockTime(self, UnBlockTime):
        self._UnBlockTime = UnBlockTime

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._BlockTime = params.get("BlockTime")
        self._UnBlockTime = params.get("UnBlockTime")
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """字段值，K-V形式

    """

    def __init__(self):
        r"""
        :param _Key: 字段名称
        :type Key: str
        :param _Value: 字段取值
        :type Value: str
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
        


class KeyValueRecord(AbstractModel):
    """KeyValue记录

    """

    def __init__(self):
        r"""
        :param _Record: 一条记录的Key-Value数组
        :type Record: list of KeyValue
        """
        self._Record = None

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record


    def _deserialize(self, params):
        if params.get("Record") is not None:
            self._Record = []
            for item in params.get("Record"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Record.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4DelRule(AbstractModel):
    """删除l4规则接口

    """

    def __init__(self):
        r"""
        :param _Id: 资源Id
        :type Id: str
        :param _Ip: 资源IP
        :type Ip: str
        :param _RuleIdList: 规则Id
        :type RuleIdList: list of str
        """
        self._Id = None
        self._Ip = None
        self._RuleIdList = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def RuleIdList(self):
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4HealthConfig(AbstractModel):
    """四层健康检查配置

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[TCP, UDP]
        :type Protocol: str
        :param _VirtualPort: 转发端口
        :type VirtualPort: int
        :param _Enable: =1表示开启；=0表示关闭
        :type Enable: int
        :param _TimeOut: 响应超时时间，单位秒
        :type TimeOut: int
        :param _Interval: 检测间隔时间，单位秒
        :type Interval: int
        :param _KickNum: 不健康阈值，单位次
        :type KickNum: int
        :param _AliveNum: 健康阈值，单位次
        :type AliveNum: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        """
        self._Protocol = None
        self._VirtualPort = None
        self._Enable = None
        self._TimeOut = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None
        self._KeepTime = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._VirtualPort = params.get("VirtualPort")
        self._Enable = params.get("Enable")
        self._TimeOut = params.get("TimeOut")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        self._KeepTime = params.get("KeepTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleEntry(AbstractModel):
    """L4规则

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[TCP, UDP]
        :type Protocol: str
        :param _VirtualPort: 转发端口
        :type VirtualPort: int
        :param _SourcePort: 源站端口
        :type SourcePort: int
        :param _SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param _SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param _LbType: 负载均衡方式，取值[1(加权轮询)，2(源IP hash)]
        :type LbType: int
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]；
        :type KeepEnable: int
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _RuleName: 规则描述
        :type RuleName: str
        :param _RemoveSwitch: 移除水印状态，取值[0(关闭)，1(开启)]
        :type RemoveSwitch: int
        """
        self._Protocol = None
        self._VirtualPort = None
        self._SourcePort = None
        self._SourceType = None
        self._KeepTime = None
        self._SourceList = None
        self._LbType = None
        self._KeepEnable = None
        self._RuleId = None
        self._RuleName = None
        self._RemoveSwitch = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def SourcePort(self):
        return self._SourcePort

    @SourcePort.setter
    def SourcePort(self, SourcePort):
        self._SourcePort = SourcePort

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

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
    def RemoveSwitch(self):
        return self._RemoveSwitch

    @RemoveSwitch.setter
    def RemoveSwitch(self, RemoveSwitch):
        self._RemoveSwitch = RemoveSwitch


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._VirtualPort = params.get("VirtualPort")
        self._SourcePort = params.get("SourcePort")
        self._SourceType = params.get("SourceType")
        self._KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RemoveSwitch = params.get("RemoveSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleHealth(AbstractModel):
    """规则健康检查参数

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Enable: =1表示开启；=0表示关闭
        :type Enable: int
        :param _TimeOut: 响应超时时间，单位秒
        :type TimeOut: int
        :param _Interval: 检测间隔时间，单位秒，必须要大于响应超时时间
        :type Interval: int
        :param _KickNum: 不健康阈值，单位次
        :type KickNum: int
        :param _AliveNum: 健康阈值，单位次
        :type AliveNum: int
        """
        self._RuleId = None
        self._Enable = None
        self._TimeOut = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def TimeOut(self):
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Enable = params.get("Enable")
        self._TimeOut = params.get("TimeOut")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleSource(AbstractModel):
    """L4规则回源列表

    """

    def __init__(self):
        r"""
        :param _Source: 回源IP或域名
        :type Source: str
        :param _Weight: 权重值，取值[0,100]
        :type Weight: int
        """
        self._Source = None
        self._Weight = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7HealthConfig(AbstractModel):
    """七层健康检查配置

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[http, https, http/https]
        :type Protocol: str
        :param _Domain: 转发域名
        :type Domain: str
        :param _Enable: =1表示开启；=0表示关闭
        :type Enable: int
        :param _Interval: 检测间隔时间，单位秒
        :type Interval: int
        :param _KickNum: 异常判定次数，单位次
        :type KickNum: int
        :param _AliveNum: 健康判定次数，单位次
        :type AliveNum: int
        :param _Method: 健康检查探测方法，可选HEAD或GET，默认为HEAD
        :type Method: str
        :param _StatusCode: 健康检查判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :type StatusCode: int
        :param _Url: 检查目录的URL，默认为/
        :type Url: str
        """
        self._Protocol = None
        self._Domain = None
        self._Enable = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None
        self._Method = None
        self._StatusCode = None
        self._Url = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._Enable = params.get("Enable")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[http, https]
        :type Protocol: str
        :param _Domain: 转发域名
        :type Domain: str
        :param _SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param _SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param _LbType: 负载均衡方式，取值[1(加权轮询)]
        :type LbType: int
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param _RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :type RuleId: str
        :param _CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :type CertType: int
        :param _SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param _Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param _PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        :param _RuleName: 规则描述
        :type RuleName: str
        :param _Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type Status: int
        :param _CCStatus: cc防护状态，取值[0(关闭), 1(开启)]
        :type CCStatus: int
        :param _CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :type CCEnable: int
        :param _CCThreshold: HTTPS协议的CC防护阈值
        :type CCThreshold: int
        :param _CCLevel: HTTPS协议的CC防护等级
        :type CCLevel: str
        :param _HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpsToHttpEnable: int
        :param _VirtualPort: 接入端口值
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPort: int
        """
        self._Protocol = None
        self._Domain = None
        self._SourceType = None
        self._KeepTime = None
        self._SourceList = None
        self._LbType = None
        self._KeepEnable = None
        self._RuleId = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None
        self._RuleName = None
        self._Status = None
        self._CCStatus = None
        self._CCEnable = None
        self._CCThreshold = None
        self._CCLevel = None
        self._HttpsToHttpEnable = None
        self._VirtualPort = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

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
    def CCStatus(self):
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def CCLevel(self):
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def HttpsToHttpEnable(self):
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._SourceType = params.get("SourceType")
        self._KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._RuleId = params.get("RuleId")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        self._CCStatus = params.get("CCStatus")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._CCLevel = params.get("CCLevel")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleHealth(AbstractModel):
    """L7规则健康检查参数

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Enable: =1表示开启；=0表示关闭
        :type Enable: int
        :param _Interval: 检测间隔时间，单位秒
        :type Interval: int
        :param _KickNum: 不健康阈值，单位次
        :type KickNum: int
        :param _AliveNum: 健康阈值，单位次
        :type AliveNum: int
        :param _Method: HTTP请求方式，取值[HEAD,GET]
        :type Method: str
        :param _StatusCode: 健康检查判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :type StatusCode: int
        :param _Url: 检查目录的URL，默认为/
        :type Url: str
        :param _Status: 配置状态，0： 正常，1：配置中，2：配置失败
        :type Status: int
        """
        self._RuleId = None
        self._Enable = None
        self._Interval = None
        self._KickNum = None
        self._AliveNum = None
        self._Method = None
        self._StatusCode = None
        self._Url = None
        self._Status = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def KickNum(self):
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def AliveNum(self):
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Enable = params.get("Enable")
        self._Interval = params.get("Interval")
        self._KickNum = params.get("KickNum")
        self._AliveNum = params.get("AliveNum")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdRequest(AbstractModel):
    """ModifyCCAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）
        :type Business: str
        :param _RsId: 资源ID,字符串类型
        :type RsId: str
        :param _AlarmThreshold: 告警阈值，大于0（目前排定的值），后台设置默认值为1000
        :type AlarmThreshold: int
        :param _IpList: 资源关联的IP列表，高防包未绑定时，传空数组，高防IP专业版传多个IP的数据
        :type IpList: list of str
        """
        self._Business = None
        self._RsId = None
        self._AlarmThreshold = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        self._AlarmThreshold = params.get("AlarmThreshold")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCAlarmThresholdResponse(AbstractModel):
    """ModifyCCAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesRequest(AbstractModel):
    """ModifyCCFrequencyRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _CCFrequencyRuleId: CC的访问频率控制规则ID
        :type CCFrequencyRuleId: str
        :param _Mode: 匹配规则，取值["include"(前缀匹配)，"equal"(完全匹配)]
        :type Mode: str
        :param _Period: 统计周期，单位秒，取值[10, 30, 60]
        :type Period: int
        :param _ReqNumber: 访问次数，取值[1-10000]
        :type ReqNumber: int
        :param _Act: 执行动作，取值["alg"（人机识别）, "drop"（拦截）]
        :type Act: str
        :param _ExeDuration: 执行时间，单位秒，取值[1-900]
        :type ExeDuration: int
        :param _Uri: URI字符串，必须以/开头，例如/abc/a.php，长度不超过31；当URI=/时，匹配模式只能选择前缀匹配；
        :type Uri: str
        :param _UserAgent: User-Agent字符串，长度不超过80
        :type UserAgent: str
        :param _Cookie: Cookie字符串，长度不超过40
        :type Cookie: str
        """
        self._Business = None
        self._CCFrequencyRuleId = None
        self._Mode = None
        self._Period = None
        self._ReqNumber = None
        self._Act = None
        self._ExeDuration = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def CCFrequencyRuleId(self):
        return self._CCFrequencyRuleId

    @CCFrequencyRuleId.setter
    def CCFrequencyRuleId(self, CCFrequencyRuleId):
        self._CCFrequencyRuleId = CCFrequencyRuleId

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def ReqNumber(self):
        return self._ReqNumber

    @ReqNumber.setter
    def ReqNumber(self, ReqNumber):
        self._ReqNumber = ReqNumber

    @property
    def Act(self):
        return self._Act

    @Act.setter
    def Act(self, Act):
        self._Act = Act

    @property
    def ExeDuration(self):
        return self._ExeDuration

    @ExeDuration.setter
    def ExeDuration(self, ExeDuration):
        self._ExeDuration = ExeDuration

    @property
    def Uri(self):
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Cookie(self):
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self._Mode = params.get("Mode")
        self._Period = params.get("Period")
        self._ReqNumber = params.get("ReqNumber")
        self._Act = params.get("Act")
        self._ExeDuration = params.get("ExeDuration")
        self._Uri = params.get("Uri")
        self._UserAgent = params.get("UserAgent")
        self._Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesResponse(AbstractModel):
    """ModifyCCFrequencyRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesStatusRequest(AbstractModel):
    """ModifyCCFrequencyRulesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleId: 7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）
        :type RuleId: str
        :param _Method: 开启或关闭，取值["on"(开启)，"off"(关闭)]
        :type Method: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._Method = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCFrequencyRulesStatusResponse(AbstractModel):
    """ModifyCCFrequencyRulesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCHostProtectionRequest(AbstractModel):
    """ModifyCCHostProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Method: 开启/关闭CC域名防护，取值[open(表示开启)，close(表示关闭)]
        :type Method: str
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._Method = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCHostProtectionResponse(AbstractModel):
    """ModifyCCHostProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCIpAllowDenyRequest(AbstractModel):
    """ModifyCCIpAllowDeny请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Method: add表示添加，delete表示删除
        :type Method: str
        :param _Type: 黑/白名单类型；取值[white(白名单)，black(黑名单)]
        :type Type: str
        :param _IpList: 黑/白名单的IP数组
        :type IpList: list of str
        :param _Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写Domain和RuleId字段；
        :type Protocol: str
        :param _Domain: 可选字段，表示HTTPS协议的7层转发规则域名（通过获取7层转发规则接口可以获取域名），只有当Protocol字段为https时才必须填写此字段；
        :type Domain: str
        :param _RuleId: 可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID），
当Method为delete时，不用填写此字段；
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._Type = None
        self._IpList = None
        self._Protocol = None
        self._Domain = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._Type = params.get("Type")
        self._IpList = params.get("IpList")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCIpAllowDenyResponse(AbstractModel):
    """ModifyCCIpAllowDeny返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCLevelRequest(AbstractModel):
    """ModifyCCLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Level: CC防护等级，取值[default(正常), loose(宽松), strict(严格)];
        :type Level: str
        :param _Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写RuleId字段；
        :type Protocol: str
        :param _RuleId: 表示7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._Level = None
        self._Protocol = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Level = params.get("Level")
        self._Protocol = params.get("Protocol")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelResponse(AbstractModel):
    """ModifyCCLevel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCPolicySwitchRequest(AbstractModel):
    """ModifyCCPolicySwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _SetId: 策略ID
        :type SetId: str
        :param _Switch: 开关状态
        :type Switch: int
        """
        self._Business = None
        self._Id = None
        self._SetId = None
        self._Switch = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._SetId = params.get("SetId")
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPolicySwitchResponse(AbstractModel):
    """ModifyCCPolicySwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCSelfDefinePolicyRequest(AbstractModel):
    """ModifyCCSelfDefinePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _SetId: 策略ID
        :type SetId: str
        :param _Policy: CC策略描述
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self._Business = None
        self._Id = None
        self._SetId = None
        self._Policy = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._SetId = params.get("SetId")
        if params.get("Policy") is not None:
            self._Policy = CCPolicy()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCSelfDefinePolicyResponse(AbstractModel):
    """ModifyCCSelfDefinePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCThresholdRequest(AbstractModel):
    """ModifyCCThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示基础防护）
        :type Business: str
        :param _Threshold: CC防护阈值，取值(0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);
当Business为高防IP、高防IP专业版时，其CC防护最大阈值跟资源的保底防护带宽有关，对应关系如下：
  保底带宽: 最大C防护阈值
  10:  20000,
  20:  40000,
  30:  70000,
  40:  100000,
  50:  150000,
  60:  200000,
  80:  250000,
  100: 300000,
        :type Threshold: int
        :param _Id: 资源ID
        :type Id: str
        :param _Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写RuleId字段；
        :type Protocol: str
        :param _RuleId: 可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID）；
当Protocol=https时必须填写；
        :type RuleId: str
        :param _BasicIp: 查询的IP地址（仅基础防护提供），取值如：1.1.1.1
        :type BasicIp: str
        :param _BasicRegion: 查询IP所属地域（仅基础防护提供），取值如：gz、bj、sh、hk等地域缩写
        :type BasicRegion: str
        :param _BasicBizType: 专区类型（仅基础防护提供），取值如：公有云专区：public，黑石专区：bm, NAT服务器专区：nat，互联网通道：channel。
        :type BasicBizType: str
        :param _BasicDeviceType: 设备类型（仅基础防护提供），取值如：服务器：cvm，公有云负载均衡：clb，黑石负载均衡：lb，NAT服务器：nat，互联网通道：channel.
        :type BasicDeviceType: str
        :param _BasicIpInstance: 仅基础防护提供。可选，IPInstance Nat 网关（如果查询的设备类型是NAT服务器，需要传此参数，通过nat资源查询接口获取）
        :type BasicIpInstance: str
        :param _BasicIspCode: 仅基础防护提供。可选，运营商线路（如果查询的设备类型是NAT服务器，需要传此参数为5）
        :type BasicIspCode: int
        :param _Domain: 可选字段，当协议取值HTTPS时，必填
        :type Domain: str
        """
        self._Business = None
        self._Threshold = None
        self._Id = None
        self._Protocol = None
        self._RuleId = None
        self._BasicIp = None
        self._BasicRegion = None
        self._BasicBizType = None
        self._BasicDeviceType = None
        self._BasicIpInstance = None
        self._BasicIspCode = None
        self._Domain = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def BasicIp(self):
        return self._BasicIp

    @BasicIp.setter
    def BasicIp(self, BasicIp):
        self._BasicIp = BasicIp

    @property
    def BasicRegion(self):
        return self._BasicRegion

    @BasicRegion.setter
    def BasicRegion(self, BasicRegion):
        self._BasicRegion = BasicRegion

    @property
    def BasicBizType(self):
        return self._BasicBizType

    @BasicBizType.setter
    def BasicBizType(self, BasicBizType):
        self._BasicBizType = BasicBizType

    @property
    def BasicDeviceType(self):
        return self._BasicDeviceType

    @BasicDeviceType.setter
    def BasicDeviceType(self, BasicDeviceType):
        self._BasicDeviceType = BasicDeviceType

    @property
    def BasicIpInstance(self):
        return self._BasicIpInstance

    @BasicIpInstance.setter
    def BasicIpInstance(self, BasicIpInstance):
        self._BasicIpInstance = BasicIpInstance

    @property
    def BasicIspCode(self):
        return self._BasicIspCode

    @BasicIspCode.setter
    def BasicIspCode(self, BasicIspCode):
        self._BasicIspCode = BasicIspCode

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Threshold = params.get("Threshold")
        self._Id = params.get("Id")
        self._Protocol = params.get("Protocol")
        self._RuleId = params.get("RuleId")
        self._BasicIp = params.get("BasicIp")
        self._BasicRegion = params.get("BasicRegion")
        self._BasicBizType = params.get("BasicBizType")
        self._BasicDeviceType = params.get("BasicDeviceType")
        self._BasicIpInstance = params.get("BasicIpInstance")
        self._BasicIspCode = params.get("BasicIspCode")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCThresholdResponse(AbstractModel):
    """ModifyCCThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyCCUrlAllowRequest(AbstractModel):
    """ModifyCCUrlAllow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Method: =add表示添加，=delete表示删除
        :type Method: str
        :param _Type: 黑/白名单类型；取值[white(白名单)]
        :type Type: str
        :param _UrlList: URL数组，URL格式如下：
http://域名/cgi
https://域名/cgi
        :type UrlList: list of str
        :param _Protocol: 可选字段，代表CC防护类型，取值[http（HTTP协议的CC防护），https（HTTPS协议的CC防护）]；当不填时，默认为HTTP协议的CC防护；当填写https时还需要填写Domain和RuleId字段；
        :type Protocol: str
        :param _Domain: 可选字段，表示HTTPS协议的7层转发规则域名（通过获取7层转发规则接口可以获取域名），只有当Protocol字段为https时才必须填写此字段；
        :type Domain: str
        :param _RuleId: 可选字段，表示HTTPS协议的7层转发规则ID（通过获取7层转发规则接口可以获取规则ID），当添加并且Protocol=https时必须填写；
当Method为delete时，可以不用填写此字段；
        :type RuleId: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._Type = None
        self._UrlList = None
        self._Protocol = None
        self._Domain = None
        self._RuleId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UrlList(self):
        return self._UrlList

    @UrlList.setter
    def UrlList(self, UrlList):
        self._UrlList = UrlList

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._Type = params.get("Type")
        self._UrlList = params.get("UrlList")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCUrlAllowResponse(AbstractModel):
    """ModifyCCUrlAllow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSAIStatusRequest(AbstractModel):
    """ModifyDDoSAIStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Method: =get表示读取AI防护状态；=set表示修改AI防护状态；
        :type Method: str
        :param _DDoSAI: AI防护状态，取值[on，off]；当Method=set时必填；
        :type DDoSAI: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._DDoSAI = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DDoSAI(self):
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._DDoSAI = params.get("DDoSAI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAIStatusResponse(AbstractModel):
    """ModifyDDoSAIStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DDoSAI: AI防护状态，取值[on，off]
        :type DDoSAI: str
        :param _Id: 资源ID
        :type Id: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DDoSAI = None
        self._Id = None
        self._RequestId = None

    @property
    def DDoSAI(self):
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DDoSAI = params.get("DDoSAI")
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class ModifyDDoSAlarmThresholdRequest(AbstractModel):
    """ModifyDDoSAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP专业版）
        :type Business: str
        :param _RsId: 资源ID,字符串类型
        :type RsId: str
        :param _AlarmType: 告警阈值类型，0-未设置，1-入流量，2-清洗流量
        :type AlarmType: int
        :param _AlarmThreshold: 告警阈值，大于0（目前暂定的值）
        :type AlarmThreshold: int
        :param _IpList: 资源关联的IP列表，高防包未绑定时，传空数组，高防IP专业版传多个IP的数据
        :type IpList: list of str
        """
        self._Business = None
        self._RsId = None
        self._AlarmType = None
        self._AlarmThreshold = None
        self._IpList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RsId(self):
        return self._RsId

    @RsId.setter
    def RsId(self, RsId):
        self._RsId = RsId

    @property
    def AlarmType(self):
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RsId = params.get("RsId")
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSAlarmThresholdResponse(AbstractModel):
    """ModifyDDoSAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSDefendStatusRequest(AbstractModel):
    """ModifyDDoSDefendStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP专业版；basic表示基础防护）
        :type Business: str
        :param _Status: 防护状态值，取值[0（关闭），1（开启）]
        :type Status: int
        :param _Hour: 关闭时长，单位小时，取值[0，1，2，3，4，5，6]；当Status=0表示关闭时，Hour必须大于0；
        :type Hour: int
        :param _Id: 资源ID；当Business不是基础防护时必须填写此字段；
        :type Id: str
        :param _Ip: 基础防护的IP，只有当Business为基础防护时才需要填写此字段；
        :type Ip: str
        :param _BizType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]
        :type BizType: str
        :param _DeviceType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]
        :type DeviceType: str
        :param _InstanceId: 只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);
        :type InstanceId: str
        :param _IPRegion: 只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：
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
"nj":     南京
        :type IPRegion: str
        """
        self._Business = None
        self._Status = None
        self._Hour = None
        self._Id = None
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._IPRegion = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IPRegion(self):
        return self._IPRegion

    @IPRegion.setter
    def IPRegion(self, IPRegion):
        self._IPRegion = IPRegion


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Status = params.get("Status")
        self._Hour = params.get("Hour")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._IPRegion = params.get("IPRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSDefendStatusResponse(AbstractModel):
    """ModifyDDoSDefendStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSLevelRequest(AbstractModel):
    """ModifyDDoSLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Method: =get表示读取防护等级；=set表示修改防护等级
        :type Method: str
        :param _DDoSLevel: 防护等级，取值[low,middle,high]；当Method=set时必填
        :type DDoSLevel: str
        """
        self._Business = None
        self._Id = None
        self._Method = None
        self._DDoSLevel = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DDoSLevel(self):
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Method = params.get("Method")
        self._DDoSLevel = params.get("DDoSLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 资源ID
        :type Id: str
        :param _DDoSLevel: 防护等级，取值[low,middle,high]
        :type DDoSLevel: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._DDoSLevel = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DDoSLevel(self):
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DDoSLevel = params.get("DDoSLevel")
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyCaseRequest(AbstractModel):
    """ModifyDDoSPolicyCase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _SceneId: 策略场景ID
        :type SceneId: str
        :param _PlatformTypes: 开发平台，取值[PC（PC客户端）， MOBILE（移动端）， TV（电视端）， SERVER（主机）]
        :type PlatformTypes: list of str
        :param _AppType: 细分品类，取值[WEB（网站）， GAME（游戏）， APP（应用）， OTHER（其他）]
        :type AppType: str
        :param _AppProtocols: 应用协议，取值[tcp（TCP协议），udp（UDP协议），icmp（ICMP协议），all（其他协议）]
        :type AppProtocols: list of str
        :param _TcpSportStart: TCP业务起始端口，取值(0, 65535]
        :type TcpSportStart: str
        :param _TcpSportEnd: TCP业务结束端口，取值(0, 65535]，必须大于等于TCP业务起始端口
        :type TcpSportEnd: str
        :param _UdpSportStart: UDP业务起始端口，取值范围(0, 65535]
        :type UdpSportStart: str
        :param _UdpSportEnd: UDP业务结束端口，取值范围(0, 65535)，必须大于等于UDP业务起始端口
        :type UdpSportEnd: str
        :param _HasAbroad: 是否有海外客户，取值[no（没有）, yes（有）]
        :type HasAbroad: str
        :param _HasInitiateTcp: 是否会主动对外发起TCP请求，取值[no（不会）, yes（会）]
        :type HasInitiateTcp: str
        :param _HasInitiateUdp: 是否会主动对外发起UDP业务请求，取值[no（不会）, yes（会）]
        :type HasInitiateUdp: str
        :param _PeerTcpPort: 主动发起TCP请求的端口，取值范围(0, 65535]
        :type PeerTcpPort: str
        :param _PeerUdpPort: 主动发起UDP请求的端口，取值范围(0, 65535]
        :type PeerUdpPort: str
        :param _TcpFootprint: TCP载荷的固定特征码，字符串长度小于512
        :type TcpFootprint: str
        :param _UdpFootprint: UDP载荷的固定特征码，字符串长度小于512
        :type UdpFootprint: str
        :param _WebApiUrl: Web业务的API的URL
        :type WebApiUrl: list of str
        :param _MinTcpPackageLen: TCP业务报文长度最小值，取值范围(0, 1500)
        :type MinTcpPackageLen: str
        :param _MaxTcpPackageLen: TCP业务报文长度最大值，取值范围(0, 1500)，必须大于等于TCP业务报文长度最小值
        :type MaxTcpPackageLen: str
        :param _MinUdpPackageLen: UDP业务报文长度最小值，取值范围(0, 1500)
        :type MinUdpPackageLen: str
        :param _MaxUdpPackageLen: UDP业务报文长度最大值，取值范围(0, 1500)，必须大于等于UDP业务报文长度最小值
        :type MaxUdpPackageLen: str
        :param _HasVPN: 是否有VPN业务，取值[no（没有）, yes（有）]
        :type HasVPN: str
        :param _TcpPortList: TCP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000
        :type TcpPortList: str
        :param _UdpPortList: UDP业务端口列表，同时支持单个端口和端口段，字符串格式，例如：80,443,700-800,53,1000-3000
        :type UdpPortList: str
        """
        self._Business = None
        self._SceneId = None
        self._PlatformTypes = None
        self._AppType = None
        self._AppProtocols = None
        self._TcpSportStart = None
        self._TcpSportEnd = None
        self._UdpSportStart = None
        self._UdpSportEnd = None
        self._HasAbroad = None
        self._HasInitiateTcp = None
        self._HasInitiateUdp = None
        self._PeerTcpPort = None
        self._PeerUdpPort = None
        self._TcpFootprint = None
        self._UdpFootprint = None
        self._WebApiUrl = None
        self._MinTcpPackageLen = None
        self._MaxTcpPackageLen = None
        self._MinUdpPackageLen = None
        self._MaxUdpPackageLen = None
        self._HasVPN = None
        self._TcpPortList = None
        self._UdpPortList = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def SceneId(self):
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def PlatformTypes(self):
        return self._PlatformTypes

    @PlatformTypes.setter
    def PlatformTypes(self, PlatformTypes):
        self._PlatformTypes = PlatformTypes

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppProtocols(self):
        return self._AppProtocols

    @AppProtocols.setter
    def AppProtocols(self, AppProtocols):
        self._AppProtocols = AppProtocols

    @property
    def TcpSportStart(self):
        return self._TcpSportStart

    @TcpSportStart.setter
    def TcpSportStart(self, TcpSportStart):
        self._TcpSportStart = TcpSportStart

    @property
    def TcpSportEnd(self):
        return self._TcpSportEnd

    @TcpSportEnd.setter
    def TcpSportEnd(self, TcpSportEnd):
        self._TcpSportEnd = TcpSportEnd

    @property
    def UdpSportStart(self):
        return self._UdpSportStart

    @UdpSportStart.setter
    def UdpSportStart(self, UdpSportStart):
        self._UdpSportStart = UdpSportStart

    @property
    def UdpSportEnd(self):
        return self._UdpSportEnd

    @UdpSportEnd.setter
    def UdpSportEnd(self, UdpSportEnd):
        self._UdpSportEnd = UdpSportEnd

    @property
    def HasAbroad(self):
        return self._HasAbroad

    @HasAbroad.setter
    def HasAbroad(self, HasAbroad):
        self._HasAbroad = HasAbroad

    @property
    def HasInitiateTcp(self):
        return self._HasInitiateTcp

    @HasInitiateTcp.setter
    def HasInitiateTcp(self, HasInitiateTcp):
        self._HasInitiateTcp = HasInitiateTcp

    @property
    def HasInitiateUdp(self):
        return self._HasInitiateUdp

    @HasInitiateUdp.setter
    def HasInitiateUdp(self, HasInitiateUdp):
        self._HasInitiateUdp = HasInitiateUdp

    @property
    def PeerTcpPort(self):
        return self._PeerTcpPort

    @PeerTcpPort.setter
    def PeerTcpPort(self, PeerTcpPort):
        self._PeerTcpPort = PeerTcpPort

    @property
    def PeerUdpPort(self):
        return self._PeerUdpPort

    @PeerUdpPort.setter
    def PeerUdpPort(self, PeerUdpPort):
        self._PeerUdpPort = PeerUdpPort

    @property
    def TcpFootprint(self):
        return self._TcpFootprint

    @TcpFootprint.setter
    def TcpFootprint(self, TcpFootprint):
        self._TcpFootprint = TcpFootprint

    @property
    def UdpFootprint(self):
        return self._UdpFootprint

    @UdpFootprint.setter
    def UdpFootprint(self, UdpFootprint):
        self._UdpFootprint = UdpFootprint

    @property
    def WebApiUrl(self):
        return self._WebApiUrl

    @WebApiUrl.setter
    def WebApiUrl(self, WebApiUrl):
        self._WebApiUrl = WebApiUrl

    @property
    def MinTcpPackageLen(self):
        return self._MinTcpPackageLen

    @MinTcpPackageLen.setter
    def MinTcpPackageLen(self, MinTcpPackageLen):
        self._MinTcpPackageLen = MinTcpPackageLen

    @property
    def MaxTcpPackageLen(self):
        return self._MaxTcpPackageLen

    @MaxTcpPackageLen.setter
    def MaxTcpPackageLen(self, MaxTcpPackageLen):
        self._MaxTcpPackageLen = MaxTcpPackageLen

    @property
    def MinUdpPackageLen(self):
        return self._MinUdpPackageLen

    @MinUdpPackageLen.setter
    def MinUdpPackageLen(self, MinUdpPackageLen):
        self._MinUdpPackageLen = MinUdpPackageLen

    @property
    def MaxUdpPackageLen(self):
        return self._MaxUdpPackageLen

    @MaxUdpPackageLen.setter
    def MaxUdpPackageLen(self, MaxUdpPackageLen):
        self._MaxUdpPackageLen = MaxUdpPackageLen

    @property
    def HasVPN(self):
        return self._HasVPN

    @HasVPN.setter
    def HasVPN(self, HasVPN):
        self._HasVPN = HasVPN

    @property
    def TcpPortList(self):
        return self._TcpPortList

    @TcpPortList.setter
    def TcpPortList(self, TcpPortList):
        self._TcpPortList = TcpPortList

    @property
    def UdpPortList(self):
        return self._UdpPortList

    @UdpPortList.setter
    def UdpPortList(self, UdpPortList):
        self._UdpPortList = UdpPortList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._SceneId = params.get("SceneId")
        self._PlatformTypes = params.get("PlatformTypes")
        self._AppType = params.get("AppType")
        self._AppProtocols = params.get("AppProtocols")
        self._TcpSportStart = params.get("TcpSportStart")
        self._TcpSportEnd = params.get("TcpSportEnd")
        self._UdpSportStart = params.get("UdpSportStart")
        self._UdpSportEnd = params.get("UdpSportEnd")
        self._HasAbroad = params.get("HasAbroad")
        self._HasInitiateTcp = params.get("HasInitiateTcp")
        self._HasInitiateUdp = params.get("HasInitiateUdp")
        self._PeerTcpPort = params.get("PeerTcpPort")
        self._PeerUdpPort = params.get("PeerUdpPort")
        self._TcpFootprint = params.get("TcpFootprint")
        self._UdpFootprint = params.get("UdpFootprint")
        self._WebApiUrl = params.get("WebApiUrl")
        self._MinTcpPackageLen = params.get("MinTcpPackageLen")
        self._MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self._MinUdpPackageLen = params.get("MinUdpPackageLen")
        self._MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self._HasVPN = params.get("HasVPN")
        self._TcpPortList = params.get("TcpPortList")
        self._UdpPortList = params.get("UdpPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyCaseResponse(AbstractModel):
    """ModifyDDoSPolicyCase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyNameRequest(AbstractModel):
    """ModifyDDoSPolicyName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _Name: 策略名称
        :type Name: str
        """
        self._Business = None
        self._PolicyId = None
        self._Name = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyNameResponse(AbstractModel):
    """ModifyDDoSPolicyName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _DropOptions: 协议禁用，必须填写且数组长度必须为1
        :type DropOptions: list of DDoSPolicyDropOption
        :param _PortLimits: 端口禁用，当没有禁用端口时填空数组
        :type PortLimits: list of DDoSPolicyPortLimit
        :param _IpAllowDenys: IP黑白名单，当没有IP黑白名单时填空数组
        :type IpAllowDenys: list of IpBlackWhite
        :param _PacketFilters: 报文过滤，当没有报文过滤时填空数组
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param _WaterPrint: 水印策略参数，当没有启用水印功能时填空数组，最多只能传一条水印策略（即数组大小不超过1）
        :type WaterPrint: list of WaterPrintPolicy
        """
        self._Business = None
        self._PolicyId = None
        self._DropOptions = None
        self._PortLimits = None
        self._IpAllowDenys = None
        self._PacketFilters = None
        self._WaterPrint = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def DropOptions(self):
        return self._DropOptions

    @DropOptions.setter
    def DropOptions(self, DropOptions):
        self._DropOptions = DropOptions

    @property
    def PortLimits(self):
        return self._PortLimits

    @PortLimits.setter
    def PortLimits(self, PortLimits):
        self._PortLimits = PortLimits

    @property
    def IpAllowDenys(self):
        return self._IpAllowDenys

    @IpAllowDenys.setter
    def IpAllowDenys(self, IpAllowDenys):
        self._IpAllowDenys = IpAllowDenys

    @property
    def PacketFilters(self):
        return self._PacketFilters

    @PacketFilters.setter
    def PacketFilters(self, PacketFilters):
        self._PacketFilters = PacketFilters

    @property
    def WaterPrint(self):
        return self._WaterPrint

    @WaterPrint.setter
    def WaterPrint(self, WaterPrint):
        self._WaterPrint = WaterPrint


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        if params.get("DropOptions") is not None:
            self._DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self._DropOptions.append(obj)
        if params.get("PortLimits") is not None:
            self._PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self._PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self._IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self._IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self._PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self._PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self._WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self._WaterPrint.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSPolicyResponse(AbstractModel):
    """ModifyDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSSwitchRequest(AbstractModel):
    """ModifyDDoSSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（basic表示基础防护）
        :type Business: str
        :param _Method: =get表示读取DDoS防护状态；=set表示修改DDoS防护状态；
        :type Method: str
        :param _Ip: 基础防护的IP，只有当Business为基础防护时才需要填写此字段；
        :type Ip: str
        :param _BizType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品类型，取值[public（CVM产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]
        :type BizType: str
        :param _DeviceType: 只有当Business为基础防护时才需要填写此字段，IP所属的产品子类，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]
        :type DeviceType: str
        :param _InstanceId: 只有当Business为基础防护时才需要填写此字段，IP所属的资源实例ID，当绑定新IP时必须填写此字段；例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*);
        :type InstanceId: str
        :param _IPRegion: 只有当Business为基础防护时才需要填写此字段，表示IP所属的地域，取值：
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
"nj":     南京
        :type IPRegion: str
        :param _Status: 可选字段，防护状态值，取值[0（关闭），1（开启）]；当Method为get时可以不填写此字段；
        :type Status: int
        """
        self._Business = None
        self._Method = None
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._IPRegion = None
        self._Status = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IPRegion(self):
        return self._IPRegion

    @IPRegion.setter
    def IPRegion(self, IPRegion):
        self._IPRegion = IPRegion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Method = params.get("Method")
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._IPRegion = params.get("IPRegion")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSSwitchResponse(AbstractModel):
    """ModifyDDoSSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 当前防护状态值，取值[0（关闭），1（开启）]
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyDDoSThresholdRequest(AbstractModel):
    """ModifyDDoSThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Threshold: DDoS清洗阈值，取值[0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
当设置值为0时，表示采用默认值；
        :type Threshold: int
        """
        self._Business = None
        self._Id = None
        self._Threshold = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDDoSWaterKeyRequest(AbstractModel):
    """ModifyDDoSWaterKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _Method: 密钥操作，取值：[add（添加），delete（删除），open（开启），close（关闭），get（获取密钥）]
        :type Method: str
        :param _KeyId: 密钥ID，当添加密钥操作时可以不填或填0，其他操作时必须填写；
        :type KeyId: int
        """
        self._Business = None
        self._PolicyId = None
        self._Method = None
        self._KeyId = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._PolicyId = params.get("PolicyId")
        self._Method = params.get("Method")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSWaterKeyResponse(AbstractModel):
    """ModifyDDoSWaterKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyList: 水印密钥列表
        :type KeyList: list of WaterPrintKey
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyList = None
        self._RequestId = None

    @property
    def KeyList(self):
        return self._KeyList

    @KeyList.setter
    def KeyList(self, KeyList):
        self._KeyList = KeyList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyList") is not None:
            self._KeyList = []
            for item in params.get("KeyList"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self._KeyList.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyElasticLimitRequest(AbstractModel):
    """ModifyElasticLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Limit: 弹性防护阈值，取值[0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]
        :type Limit: int
        """
        self._Business = None
        self._Id = None
        self._Limit = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyElasticLimitResponse(AbstractModel):
    """ModifyElasticLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL4HealthRequest(AbstractModel):
    """ModifyL4Health请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Healths: 健康检查参数数组
        :type Healths: list of L4RuleHealth
        """
        self._Business = None
        self._Id = None
        self._Healths = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Healths(self):
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4HealthResponse(AbstractModel):
    """ModifyL4Health返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL4KeepTimeRequest(AbstractModel):
    """ModifyL4KeepTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        """
        self._Business = None
        self._Id = None
        self._RuleId = None
        self._KeepEnable = None
        self._KeepTime = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._KeepEnable = params.get("KeepEnable")
        self._KeepTime = params.get("KeepTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4KeepTimeResponse(AbstractModel):
    """ModifyL4KeepTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL4RulesRequest(AbstractModel):
    """ModifyL4Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = L4RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL4RulesResponse(AbstractModel):
    """ModifyL4Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyL7RulesRequest(AbstractModel):
    """ModifyL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L7RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = L7RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7RulesResponse(AbstractModel):
    """ModifyL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyNetReturnSwitchRequest(AbstractModel):
    """ModifyNetReturnSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _Status: Status 表示回切开关，0: 关闭， 1:打开
        :type Status: int
        :param _Hour: 回切时长，单位：小时，取值[0,1,2,3,4,5,6;]当status=1时必选填写Hour>0
        :type Hour: int
        """
        self._Business = None
        self._Id = None
        self._Status = None
        self._Hour = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Hour(self):
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Hour = params.get("Hour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetReturnSwitchResponse(AbstractModel):
    """ModifyNetReturnSwitch返回参数结构体

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


class ModifyNewDomainRulesRequest(AbstractModel):
    """ModifyNewDomainRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rule: 域名转发规则
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.NewL7RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = NewL7RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewDomainRulesResponse(AbstractModel):
    """ModifyNewDomainRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyNewL4RuleRequest(AbstractModel):
    """ModifyNewL4Rule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rule: 转发规则
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = L4RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewL4RuleResponse(AbstractModel):
    """ModifyNewL4Rule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyResBindDDoSPolicyRequest(AbstractModel):
    """ModifyResBindDDoSPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _Method: 绑定或解绑，bind表示绑定策略，unbind表示解绑策略
        :type Method: str
        """
        self._Business = None
        self._Id = None
        self._PolicyId = None
        self._Method = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PolicyId(self):
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._PolicyId = params.get("PolicyId")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResBindDDoSPolicyResponse(AbstractModel):
    """ModifyResBindDDoSPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyResourceRenewFlagRequest(AbstractModel):
    """ModifyResourceRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: 大禹子产品代号（bgpip表示高防IP；net表示高防IP专业版；shield表示棋牌盾；bgp表示独享包；bgp-multip表示共享包；insurance表示保险包；staticpack表示三网套餐包）
        :type Business: str
        :param _Id: 资源Id
        :type Id: str
        :param _RenewFlag: 自动续费标记（0手动续费；1自动续费；2到期不续费）
        :type RenewFlag: int
        """
        self._Business = None
        self._Id = None
        self._RenewFlag = None

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceRenewFlagResponse(AbstractModel):
    """ModifyResourceRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class NewL4RuleEntry(AbstractModel):
    """四层规则结构体

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[TCP, UDP]
        :type Protocol: str
        :param _VirtualPort: 转发端口
        :type VirtualPort: int
        :param _SourcePort: 源站端口
        :type SourcePort: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param _SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param _LbType: 负载均衡方式，取值[1(加权轮询)，2(源IP hash)]
        :type LbType: int
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]；
        :type KeepEnable: int
        :param _SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _RuleName: 规则描述
        :type RuleName: str
        :param _RemoveSwitch: 移除水印状态，取值[0(关闭)，1(开启)]
        :type RemoveSwitch: int
        :param _ModifyTime: 规则修改时间
        :type ModifyTime: str
        :param _Region: 对应地区信息
        :type Region: int
        :param _Ip: 绑定资源IP信息
        :type Ip: str
        :param _Id: 绑定资源Id信息
        :type Id: str
        """
        self._Protocol = None
        self._VirtualPort = None
        self._SourcePort = None
        self._KeepTime = None
        self._SourceList = None
        self._LbType = None
        self._KeepEnable = None
        self._SourceType = None
        self._RuleId = None
        self._RuleName = None
        self._RemoveSwitch = None
        self._ModifyTime = None
        self._Region = None
        self._Ip = None
        self._Id = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def SourcePort(self):
        return self._SourcePort

    @SourcePort.setter
    def SourcePort(self, SourcePort):
        self._SourcePort = SourcePort

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

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
    def RemoveSwitch(self):
        return self._RemoveSwitch

    @RemoveSwitch.setter
    def RemoveSwitch(self, RemoveSwitch):
        self._RemoveSwitch = RemoveSwitch

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._VirtualPort = params.get("VirtualPort")
        self._SourcePort = params.get("SourcePort")
        self._KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._SourceType = params.get("SourceType")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RemoveSwitch = params.get("RemoveSwitch")
        self._ModifyTime = params.get("ModifyTime")
        self._Region = params.get("Region")
        self._Ip = params.get("Ip")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewL7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[http, https]
        :type Protocol: str
        :param _Domain: 转发域名
        :type Domain: str
        :param _SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param _SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param _LbType: 负载均衡方式，取值[1(加权轮询)]
        :type LbType: int
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param _RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :type RuleId: str
        :param _CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :type CertType: int
        :param _SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param _Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param _PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        :param _RuleName: 规则描述
        :type RuleName: str
        :param _Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type Status: int
        :param _CCStatus: cc防护状态，取值[0(关闭), 1(开启)]
        :type CCStatus: int
        :param _CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :type CCEnable: int
        :param _CCThreshold: HTTPS协议的CC防护阈值
        :type CCThreshold: int
        :param _CCLevel: HTTPS协议的CC防护等级
        :type CCLevel: str
        :param _Region: 区域码
        :type Region: int
        :param _Id: 资源Id
        :type Id: str
        :param _Ip: 资源Ip
        :type Ip: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :type HttpsToHttpEnable: int
        :param _VirtualPort: 接入端口值
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPort: int
        """
        self._Protocol = None
        self._Domain = None
        self._SourceType = None
        self._KeepTime = None
        self._SourceList = None
        self._LbType = None
        self._KeepEnable = None
        self._RuleId = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None
        self._RuleName = None
        self._Status = None
        self._CCStatus = None
        self._CCEnable = None
        self._CCThreshold = None
        self._CCLevel = None
        self._Region = None
        self._Id = None
        self._Ip = None
        self._ModifyTime = None
        self._HttpsToHttpEnable = None
        self._VirtualPort = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def KeepTime(self):
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceList(self):
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def LbType(self):
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

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
    def CCStatus(self):
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def CCEnable(self):
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def CCLevel(self):
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def HttpsToHttpEnable(self):
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._SourceType = params.get("SourceType")
        self._KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._RuleId = params.get("RuleId")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        self._CCStatus = params.get("CCStatus")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._CCLevel = params.get("CCLevel")
        self._Region = params.get("Region")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._ModifyTime = params.get("ModifyTime")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderBy(AbstractModel):
    """排序字段

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段名称，取值[
bandwidth（带宽），
overloadCount（超峰值次数）
]
        :type Field: str
        :param _Order: 升降序，取值为[asc（升序），（升序），desc（降序）， DESC（降序）]
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """分页索引

    """

    def __init__(self):
        r"""
        :param _Offset: 起始位置
        :type Offset: int
        :param _Limit: 数量
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

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
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolPort(AbstractModel):
    """Protocol、Port参数

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议（tcp；udp）
        :type Protocol: str
        :param _Port: 端口
        :type Port: int
        """
        self._Protocol = None
        self._Port = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstanceCount(AbstractModel):
    """地域资源实例数

    """

    def __init__(self):
        r"""
        :param _Region: 地域码
        :type Region: str
        :param _RegionV3: 地域码（新规范）
        :type RegionV3: str
        :param _Count: 资源实例数
        :type Count: int
        """
        self._Region = None
        self._RegionV3 = None
        self._Count = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionV3(self):
        return self._RegionV3

    @RegionV3.setter
    def RegionV3(self, RegionV3):
        self._RegionV3 = RegionV3

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionV3 = params.get("RegionV3")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIp(AbstractModel):
    """资源的IP数组

    """

    def __init__(self):
        r"""
        :param _Id: 资源ID
        :type Id: str
        :param _IpList: 资源的IP数组
        :type IpList: list of str
        """
        self._Id = None
        self._IpList = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def IpList(self):
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingDomain(AbstractModel):
    """调度域名信息

    """

    def __init__(self):
        r"""
        :param _Domain: 调度域名
        :type Domain: str
        :param _BGPIpList: BGP线路IP列表
        :type BGPIpList: list of str
        :param _CTCCIpList: 电信线路IP列表
        :type CTCCIpList: list of str
        :param _CUCCIpList: 联通线路IP列表
        :type CUCCIpList: list of str
        :param _CMCCIpList: 移动线路IP列表
        :type CMCCIpList: list of str
        :param _OverseaIpList: 海外线路IP列表
        :type OverseaIpList: list of str
        :param _Method: 调度方式，当前仅支持优先级, 取值为priority
        :type Method: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _TTL: ttl
        :type TTL: int
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        """
        self._Domain = None
        self._BGPIpList = None
        self._CTCCIpList = None
        self._CUCCIpList = None
        self._CMCCIpList = None
        self._OverseaIpList = None
        self._Method = None
        self._CreateTime = None
        self._TTL = None
        self._Status = None
        self._ModifyTime = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def BGPIpList(self):
        return self._BGPIpList

    @BGPIpList.setter
    def BGPIpList(self, BGPIpList):
        self._BGPIpList = BGPIpList

    @property
    def CTCCIpList(self):
        return self._CTCCIpList

    @CTCCIpList.setter
    def CTCCIpList(self, CTCCIpList):
        self._CTCCIpList = CTCCIpList

    @property
    def CUCCIpList(self):
        return self._CUCCIpList

    @CUCCIpList.setter
    def CUCCIpList(self, CUCCIpList):
        self._CUCCIpList = CUCCIpList

    @property
    def CMCCIpList(self):
        return self._CMCCIpList

    @CMCCIpList.setter
    def CMCCIpList(self, CMCCIpList):
        self._CMCCIpList = CMCCIpList

    @property
    def OverseaIpList(self):
        return self._OverseaIpList

    @OverseaIpList.setter
    def OverseaIpList(self, OverseaIpList):
        self._OverseaIpList = OverseaIpList

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._BGPIpList = params.get("BGPIpList")
        self._CTCCIpList = params.get("CTCCIpList")
        self._CUCCIpList = params.get("CUCCIpList")
        self._CMCCIpList = params.get("CMCCIpList")
        self._OverseaIpList = params.get("OverseaIpList")
        self._Method = params.get("Method")
        self._CreateTime = params.get("CreateTime")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCode(AbstractModel):
    """操作返回码，只用于返回成功的情况

    """

    def __init__(self):
        r"""
        :param _Code: 成功/错误码
        :type Code: str
        :param _Message: 描述
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintKey(AbstractModel):
    """水印Key

    """

    def __init__(self):
        r"""
        :param _KeyId: 水印KeyID
        :type KeyId: str
        :param _KeyContent: 水印Key值
        :type KeyContent: str
        :param _KeyVersion: 水印Key的版本号
        :type KeyVersion: str
        :param _OpenStatus: 是否开启，取值[0（没有开启），1（已开启）]
        :type OpenStatus: int
        :param _CreateTime: 密钥生成时间
        :type CreateTime: str
        """
        self._KeyId = None
        self._KeyContent = None
        self._KeyVersion = None
        self._OpenStatus = None
        self._CreateTime = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyContent(self):
        return self._KeyContent

    @KeyContent.setter
    def KeyContent(self, KeyContent):
        self._KeyContent = KeyContent

    @property
    def KeyVersion(self):
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def OpenStatus(self):
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyContent = params.get("KeyContent")
        self._KeyVersion = params.get("KeyVersion")
        self._OpenStatus = params.get("OpenStatus")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintPolicy(AbstractModel):
    """水印策略参数

    """

    def __init__(self):
        r"""
        :param _TcpPortList: TCP端口段，例如["2000-3000","3500-4000"]
        :type TcpPortList: list of str
        :param _UdpPortList: UDP端口段，例如["2000-3000","3500-4000"]
        :type UdpPortList: list of str
        :param _Offset: 水印偏移量，取值范围[0, 100)
        :type Offset: int
        :param _RemoveSwitch: 是否自动剥离，取值[0（不自动剥离），1（自动剥离）]
        :type RemoveSwitch: int
        :param _OpenStatus: 是否开启，取值[0（没有开启），1（已开启）]
        :type OpenStatus: int
        """
        self._TcpPortList = None
        self._UdpPortList = None
        self._Offset = None
        self._RemoveSwitch = None
        self._OpenStatus = None

    @property
    def TcpPortList(self):
        return self._TcpPortList

    @TcpPortList.setter
    def TcpPortList(self, TcpPortList):
        self._TcpPortList = TcpPortList

    @property
    def UdpPortList(self):
        return self._UdpPortList

    @UdpPortList.setter
    def UdpPortList(self, UdpPortList):
        self._UdpPortList = UdpPortList

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def RemoveSwitch(self):
        return self._RemoveSwitch

    @RemoveSwitch.setter
    def RemoveSwitch(self, RemoveSwitch):
        self._RemoveSwitch = RemoveSwitch

    @property
    def OpenStatus(self):
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus


    def _deserialize(self, params):
        self._TcpPortList = params.get("TcpPortList")
        self._UdpPortList = params.get("UdpPortList")
        self._Offset = params.get("Offset")
        self._RemoveSwitch = params.get("RemoveSwitch")
        self._OpenStatus = params.get("OpenStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        