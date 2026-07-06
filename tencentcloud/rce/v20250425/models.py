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


class IpLocationInfo(AbstractModel):
    r"""IP地理位置信息

    """

    def __init__(self):
        r"""
        :param _Country: <p>IP地址所属国家</p>
        :type Country: str
        :param _Region: <p>IP地址所属省份</p>
        :type Region: str
        :param _City: <p>IP地址所属城市</p>
        :type City: str
        :param _District: <p>IP地址所属地区</p>
        :type District: str
        :param _Longitude: <p>IP地址的经度</p>
        :type Longitude: str
        :param _Latitude: <p>IP地址的纬度</p>
        :type Latitude: str
        :param _Timezone: <p>IP地址所属时区</p>
        :type Timezone: str
        :param _ZipCode: <p>IP地址的邮政编码</p>
        :type ZipCode: str
        """
        self._Country = None
        self._Region = None
        self._City = None
        self._District = None
        self._Longitude = None
        self._Latitude = None
        self._Timezone = None
        self._ZipCode = None

    @property
    def Country(self):
        r"""<p>IP地址所属国家</p>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Region(self):
        r"""<p>IP地址所属省份</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def City(self):
        r"""<p>IP地址所属城市</p>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        r"""<p>IP地址所属地区</p>
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Longitude(self):
        r"""<p>IP地址的经度</p>
        :rtype: str
        """
        return self._Longitude

    @Longitude.setter
    def Longitude(self, Longitude):
        self._Longitude = Longitude

    @property
    def Latitude(self):
        r"""<p>IP地址的纬度</p>
        :rtype: str
        """
        return self._Latitude

    @Latitude.setter
    def Latitude(self, Latitude):
        self._Latitude = Latitude

    @property
    def Timezone(self):
        r"""<p>IP地址所属时区</p>
        :rtype: str
        """
        return self._Timezone

    @Timezone.setter
    def Timezone(self, Timezone):
        self._Timezone = Timezone

    @property
    def ZipCode(self):
        r"""<p>IP地址的邮政编码</p>
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode


    def _deserialize(self, params):
        self._Country = params.get("Country")
        self._Region = params.get("Region")
        self._City = params.get("City")
        self._District = params.get("District")
        self._Longitude = params.get("Longitude")
        self._Latitude = params.get("Latitude")
        self._Timezone = params.get("Timezone")
        self._ZipCode = params.get("ZipCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpNetworkInfo(AbstractModel):
    r"""IP基础网络信息

    """

    def __init__(self):
        r"""
        :param _ISP: <p>互联网服务提供商</p>
        :type ISP: str
        :param _ASN: <p>自治系统号</p>
        :type ASN: str
        :param _Organization: <p>IP注册组织名称</p>
        :type Organization: str
        :param _IsReserved: <p>是否保留IP</p>
        :type IsReserved: bool
        :param _IsGateway: <p>是否网关IP</p>
        :type IsGateway: bool
        :param _IsAnycast: <p>是否任播网络</p>
        :type IsAnycast: bool
        :param _IsMobile: <p>是否移动网络</p>
        :type IsMobile: bool
        :param _IsDynamic: <p>是否动态IP</p>
        :type IsDynamic: bool
        :param _IsEgress: <p>是否网络出口</p>
        :type IsEgress: bool
        :param _IsDNS: <p>是否域名解析</p>
        :type IsDNS: bool
        :param _IsEducation: <p>是否教育机构</p>
        :type IsEducation: bool
        :param _IsInstitution: <p>是否组织机构</p>
        :type IsInstitution: bool
        :param _IsCompany: <p>是否企业专线</p>
        :type IsCompany: bool
        :param _IsResidence: <p>是否家用宽带</p>
        :type IsResidence: bool
        :param _IsCloudService: <p>是否云服务</p>
        :type IsCloudService: bool
        :param _IsInfrastructure: <p>是否基础设施</p>
        :type IsInfrastructure: bool
        :param _IsMXServer: <p>是否邮箱服务</p>
        :type IsMXServer: bool
        """
        self._ISP = None
        self._ASN = None
        self._Organization = None
        self._IsReserved = None
        self._IsGateway = None
        self._IsAnycast = None
        self._IsMobile = None
        self._IsDynamic = None
        self._IsEgress = None
        self._IsDNS = None
        self._IsEducation = None
        self._IsInstitution = None
        self._IsCompany = None
        self._IsResidence = None
        self._IsCloudService = None
        self._IsInfrastructure = None
        self._IsMXServer = None

    @property
    def ISP(self):
        r"""<p>互联网服务提供商</p>
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def ASN(self):
        r"""<p>自治系统号</p>
        :rtype: str
        """
        return self._ASN

    @ASN.setter
    def ASN(self, ASN):
        self._ASN = ASN

    @property
    def Organization(self):
        r"""<p>IP注册组织名称</p>
        :rtype: str
        """
        return self._Organization

    @Organization.setter
    def Organization(self, Organization):
        self._Organization = Organization

    @property
    def IsReserved(self):
        r"""<p>是否保留IP</p>
        :rtype: bool
        """
        return self._IsReserved

    @IsReserved.setter
    def IsReserved(self, IsReserved):
        self._IsReserved = IsReserved

    @property
    def IsGateway(self):
        r"""<p>是否网关IP</p>
        :rtype: bool
        """
        return self._IsGateway

    @IsGateway.setter
    def IsGateway(self, IsGateway):
        self._IsGateway = IsGateway

    @property
    def IsAnycast(self):
        r"""<p>是否任播网络</p>
        :rtype: bool
        """
        return self._IsAnycast

    @IsAnycast.setter
    def IsAnycast(self, IsAnycast):
        self._IsAnycast = IsAnycast

    @property
    def IsMobile(self):
        r"""<p>是否移动网络</p>
        :rtype: bool
        """
        return self._IsMobile

    @IsMobile.setter
    def IsMobile(self, IsMobile):
        self._IsMobile = IsMobile

    @property
    def IsDynamic(self):
        r"""<p>是否动态IP</p>
        :rtype: bool
        """
        return self._IsDynamic

    @IsDynamic.setter
    def IsDynamic(self, IsDynamic):
        self._IsDynamic = IsDynamic

    @property
    def IsEgress(self):
        r"""<p>是否网络出口</p>
        :rtype: bool
        """
        return self._IsEgress

    @IsEgress.setter
    def IsEgress(self, IsEgress):
        self._IsEgress = IsEgress

    @property
    def IsDNS(self):
        r"""<p>是否域名解析</p>
        :rtype: bool
        """
        return self._IsDNS

    @IsDNS.setter
    def IsDNS(self, IsDNS):
        self._IsDNS = IsDNS

    @property
    def IsEducation(self):
        r"""<p>是否教育机构</p>
        :rtype: bool
        """
        return self._IsEducation

    @IsEducation.setter
    def IsEducation(self, IsEducation):
        self._IsEducation = IsEducation

    @property
    def IsInstitution(self):
        r"""<p>是否组织机构</p>
        :rtype: bool
        """
        return self._IsInstitution

    @IsInstitution.setter
    def IsInstitution(self, IsInstitution):
        self._IsInstitution = IsInstitution

    @property
    def IsCompany(self):
        r"""<p>是否企业专线</p>
        :rtype: bool
        """
        return self._IsCompany

    @IsCompany.setter
    def IsCompany(self, IsCompany):
        self._IsCompany = IsCompany

    @property
    def IsResidence(self):
        r"""<p>是否家用宽带</p>
        :rtype: bool
        """
        return self._IsResidence

    @IsResidence.setter
    def IsResidence(self, IsResidence):
        self._IsResidence = IsResidence

    @property
    def IsCloudService(self):
        r"""<p>是否云服务</p>
        :rtype: bool
        """
        return self._IsCloudService

    @IsCloudService.setter
    def IsCloudService(self, IsCloudService):
        self._IsCloudService = IsCloudService

    @property
    def IsInfrastructure(self):
        r"""<p>是否基础设施</p>
        :rtype: bool
        """
        return self._IsInfrastructure

    @IsInfrastructure.setter
    def IsInfrastructure(self, IsInfrastructure):
        self._IsInfrastructure = IsInfrastructure

    @property
    def IsMXServer(self):
        r"""<p>是否邮箱服务</p>
        :rtype: bool
        """
        return self._IsMXServer

    @IsMXServer.setter
    def IsMXServer(self, IsMXServer):
        self._IsMXServer = IsMXServer


    def _deserialize(self, params):
        self._ISP = params.get("ISP")
        self._ASN = params.get("ASN")
        self._Organization = params.get("Organization")
        self._IsReserved = params.get("IsReserved")
        self._IsGateway = params.get("IsGateway")
        self._IsAnycast = params.get("IsAnycast")
        self._IsMobile = params.get("IsMobile")
        self._IsDynamic = params.get("IsDynamic")
        self._IsEgress = params.get("IsEgress")
        self._IsDNS = params.get("IsDNS")
        self._IsEducation = params.get("IsEducation")
        self._IsInstitution = params.get("IsInstitution")
        self._IsCompany = params.get("IsCompany")
        self._IsResidence = params.get("IsResidence")
        self._IsCloudService = params.get("IsCloudService")
        self._IsInfrastructure = params.get("IsInfrastructure")
        self._IsMXServer = params.get("IsMXServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageIPPortraitRiskInput(AbstractModel):
    r"""业务入参

    """

    def __init__(self):
        r"""
        :param _UserIp: <p>用户公网ip（仅支持IPv4）</p>
        :type UserIp: str
        :param _Channel: <p>渠道号<br>1：pc<br>2：H5<br>3：app<br>4：ott</p>
        :type Channel: int
        """
        self._UserIp = None
        self._Channel = None

    @property
    def UserIp(self):
        r"""<p>用户公网ip（仅支持IPv4）</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Channel(self):
        r"""<p>渠道号<br>1：pc<br>2：H5<br>3：app<br>4：ott</p>
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageIPPortraitRiskOutput(AbstractModel):
    r"""IP画像出参

    """

    def __init__(self):
        r"""
        :param _Code: <p>错误码，0 表示成功，非0表示失败错误码。<br>0：成功<br>1002：参数错误<br>6000：系统内部错误</p>
        :type Code: int
        :param _Message: <p>返回消息</p>
        :type Message: str
        :param _Value: <p>结果</p>
        :type Value: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskValueOutput`
        """
        self._Code = None
        self._Message = None
        self._Value = None

    @property
    def Code(self):
        r"""<p>错误码，0 表示成功，非0表示失败错误码。<br>0：成功<br>1002：参数错误<br>6000：系统内部错误</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>返回消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Value(self):
        r"""<p>结果</p>
        :rtype: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskValueOutput`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Value") is not None:
            self._Value = ManageIPPortraitRiskValueOutput()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageIPPortraitRiskRequest(AbstractModel):
    r"""ManageIPPortraitRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PostTime: 请求秒级时间戳
        :type PostTime: int
        :param _BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskInput`
        """
        self._PostTime = None
        self._BusinessSecurityData = None

    @property
    def PostTime(self):
        r"""请求秒级时间戳
        :rtype: int
        """
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def BusinessSecurityData(self):
        r"""业务入参
        :rtype: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskInput`
        """
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData


    def _deserialize(self, params):
        self._PostTime = params.get("PostTime")
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = ManageIPPortraitRiskInput()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageIPPortraitRiskResponse(AbstractModel):
    r"""ManageIPPortraitRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 出参
        :type Data: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskOutput`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""出参
        :rtype: :class:`tencentcloud.rce.v20250425.models.ManageIPPortraitRiskOutput`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ManageIPPortraitRiskOutput()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ManageIPPortraitRiskValueOutput(AbstractModel):
    r"""业务出参

    """

    def __init__(self):
        r"""
        :param _UserIp: <p>对应的IP</p>
        :type UserIp: str
        :param _RiskScore: <p>返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高</p>
        :type RiskScore: int
        :param _RiskType: <p>风险类型<br>730001：垃圾邮件，当前IP存在未经用户请求或同意，大量发送的广告、欺诈或推广信息，通常通过邮件、短信或社交消息传播。<br>730002：恶意行为，当前IP存在破坏、窃取、干扰或未授权访问为目的的故意行为。<br>730003：恶意工具，当前IP关联用于实施恶意行为的软件或脚本，如病毒、木马、勒索软件、漏洞利用工具等。<br>730004：匿名IP，通过代理、Tor网络等技术手段隐藏真实来源的IP地址，存在逃避定位或实施攻击风险。<br>730005：开放端口，网络上处于开放状态的服务入口，若配置不当或存在漏洞。<br>730006：养号，当前IP存在通过模拟正常操作（如登录、浏览）维护和提升账号的活跃度与可信度行为。<br>730007：IDC，互联网数据中心，可能被黑客利用来托管恶意服务或发动攻击。<br>730008：晒号，当前IP在公开或地下论坛展示、交易非法获取的各类账号（如游戏、社交、金融账号）的行为。<br>730009：盗号，当前IP存在通过钓鱼、撞库、木马等手段，非法获取他人账号的登录凭证（用户名、密码等）行为。<br>730010：代理，作为中间节点转发网络流量，可用于隐藏真实IP、绕过地域限制。<br>730011：扫描，使用工具自动探测目标网络或系统的开放端口、服务、漏洞等。<br>730012：秒拨，当前IP通过不断重新拨号以快速切换IP地址，常被用于绕过基于IP的频率限制或封禁。<br>730013：爬虫，自动抓取网络信息的脚本或程序。<br>730014：VPN 虚拟专用网络。<br>730015：僵尸网络，当前IP由攻击者通过恶意软件控制的、大规模联网设备（如电脑、IoT设备）集群，可能被用于发动DDoS攻击、发送垃圾邮件等。<br>730016：网络攻击，当前IP存在对计算机系统、网络或数据的任何进攻行为。</p>
        :type RiskType: list of int
        :param _IpLocation: <p>IP地理位置信息</p>
        :type IpLocation: :class:`tencentcloud.rce.v20250425.models.IpLocationInfo`
        :param _IpNetwork: <p>IP基础网络信息</p>
        :type IpNetwork: :class:`tencentcloud.rce.v20250425.models.IpNetworkInfo`
        """
        self._UserIp = None
        self._RiskScore = None
        self._RiskType = None
        self._IpLocation = None
        self._IpNetwork = None

    @property
    def UserIp(self):
        r"""<p>对应的IP</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def RiskScore(self):
        r"""<p>返回风险等级, 0 - 4，0代表无风险，数值越大，风险越高</p>
        :rtype: int
        """
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskType(self):
        r"""<p>风险类型<br>730001：垃圾邮件，当前IP存在未经用户请求或同意，大量发送的广告、欺诈或推广信息，通常通过邮件、短信或社交消息传播。<br>730002：恶意行为，当前IP存在破坏、窃取、干扰或未授权访问为目的的故意行为。<br>730003：恶意工具，当前IP关联用于实施恶意行为的软件或脚本，如病毒、木马、勒索软件、漏洞利用工具等。<br>730004：匿名IP，通过代理、Tor网络等技术手段隐藏真实来源的IP地址，存在逃避定位或实施攻击风险。<br>730005：开放端口，网络上处于开放状态的服务入口，若配置不当或存在漏洞。<br>730006：养号，当前IP存在通过模拟正常操作（如登录、浏览）维护和提升账号的活跃度与可信度行为。<br>730007：IDC，互联网数据中心，可能被黑客利用来托管恶意服务或发动攻击。<br>730008：晒号，当前IP在公开或地下论坛展示、交易非法获取的各类账号（如游戏、社交、金融账号）的行为。<br>730009：盗号，当前IP存在通过钓鱼、撞库、木马等手段，非法获取他人账号的登录凭证（用户名、密码等）行为。<br>730010：代理，作为中间节点转发网络流量，可用于隐藏真实IP、绕过地域限制。<br>730011：扫描，使用工具自动探测目标网络或系统的开放端口、服务、漏洞等。<br>730012：秒拨，当前IP通过不断重新拨号以快速切换IP地址，常被用于绕过基于IP的频率限制或封禁。<br>730013：爬虫，自动抓取网络信息的脚本或程序。<br>730014：VPN 虚拟专用网络。<br>730015：僵尸网络，当前IP由攻击者通过恶意软件控制的、大规模联网设备（如电脑、IoT设备）集群，可能被用于发动DDoS攻击、发送垃圾邮件等。<br>730016：网络攻击，当前IP存在对计算机系统、网络或数据的任何进攻行为。</p>
        :rtype: list of int
        """
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def IpLocation(self):
        r"""<p>IP地理位置信息</p>
        :rtype: :class:`tencentcloud.rce.v20250425.models.IpLocationInfo`
        """
        return self._IpLocation

    @IpLocation.setter
    def IpLocation(self, IpLocation):
        self._IpLocation = IpLocation

    @property
    def IpNetwork(self):
        r"""<p>IP基础网络信息</p>
        :rtype: :class:`tencentcloud.rce.v20250425.models.IpNetworkInfo`
        """
        return self._IpNetwork

    @IpNetwork.setter
    def IpNetwork(self, IpNetwork):
        self._IpNetwork = IpNetwork


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        self._RiskScore = params.get("RiskScore")
        self._RiskType = params.get("RiskType")
        if params.get("IpLocation") is not None:
            self._IpLocation = IpLocationInfo()
            self._IpLocation._deserialize(params.get("IpLocation"))
        if params.get("IpNetwork") is not None:
            self._IpNetwork = IpNetworkInfo()
            self._IpNetwork._deserialize(params.get("IpNetwork"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        