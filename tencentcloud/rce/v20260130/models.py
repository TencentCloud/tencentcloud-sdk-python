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


class AssessEnvironmentRiskRequest(AbstractModel):
    r"""AssessEnvironmentRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserIp: <p>客户端 IP 地址</p>
        :type UserIp: str
        """
        self._UserIp = None

    @property
    def UserIp(self):
        r"""<p>客户端 IP 地址</p>
        :rtype: str
        """
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp


    def _deserialize(self, params):
        self._UserIp = params.get("UserIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssessEnvironmentRiskResponse(AbstractModel):
    r"""AssessEnvironmentRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>环境风险评估返回结果</p>
        :type Data: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>环境风险评估返回结果</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.AssessEnvironmentRiskRsp`
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
            self._Data = AssessEnvironmentRiskRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AssessEnvironmentRiskRsp(AbstractModel):
    r"""环境风险评估返回结果

    """

    def __init__(self):
        r"""
        :param _Score: <p>环境风险分信息</p>
        :type Score: :class:`tencentcloud.rce.v20260130.models.DataScore`
        :param _Environment: <p>环境基础信息</p>
        :type Environment: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        self._Score = None
        self._Environment = None

    @property
    def Score(self):
        r"""<p>环境风险分信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.DataScore`
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Environment(self):
        r"""<p>环境基础信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.Environment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        if params.get("Score") is not None:
            self._Score = DataScore()
            self._Score._deserialize(params.get("Score"))
        if params.get("Environment") is not None:
            self._Environment = Environment()
            self._Environment._deserialize(params.get("Environment"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataScore(AbstractModel):
    r"""风险分信息

    """

    def __init__(self):
        r"""
        :param _RiskLevel: <p>风险等级</p>
        :type RiskLevel: int
        :param _RiskLabels: <p>风险标签</p>
        :type RiskLabels: list of RiskLabel
        """
        self._RiskLevel = None
        self._RiskLabels = None

    @property
    def RiskLevel(self):
        r"""<p>风险等级</p>
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskLabels(self):
        r"""<p>风险标签</p>
        :rtype: list of RiskLabel
        """
        return self._RiskLabels

    @RiskLabels.setter
    def RiskLabels(self, RiskLabels):
        self._RiskLabels = RiskLabels


    def _deserialize(self, params):
        self._RiskLevel = params.get("RiskLevel")
        if params.get("RiskLabels") is not None:
            self._RiskLabels = []
            for item in params.get("RiskLabels"):
                obj = RiskLabel()
                obj._deserialize(item)
                self._RiskLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    r"""环境基础信息

    """

    def __init__(self):
        r"""
        :param _Location: <p>IP地理位置信息</p>
        :type Location: :class:`tencentcloud.rce.v20260130.models.IPLocation`
        :param _Network: <p>IP基础网络信息</p>
        :type Network: :class:`tencentcloud.rce.v20260130.models.IPNetwork`
        """
        self._Location = None
        self._Network = None

    @property
    def Location(self):
        r"""<p>IP地理位置信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.IPLocation`
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Network(self):
        r"""<p>IP基础网络信息</p>
        :rtype: :class:`tencentcloud.rce.v20260130.models.IPNetwork`
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network


    def _deserialize(self, params):
        if params.get("Location") is not None:
            self._Location = IPLocation()
            self._Location._deserialize(params.get("Location"))
        if params.get("Network") is not None:
            self._Network = IPNetwork()
            self._Network._deserialize(params.get("Network"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPLocation(AbstractModel):
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
        


class IPNetwork(AbstractModel):
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
        


class RiskLabel(AbstractModel):
    r"""风险标签

    """

    def __init__(self):
        r"""
        :param _Id: <p>风险ID</p>
        :type Id: str
        :param _Reason: <p>风险描述</p>
        :type Reason: str
        """
        self._Id = None
        self._Reason = None

    @property
    def Id(self):
        r"""<p>风险ID</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Reason(self):
        r"""<p>风险描述</p>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        