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


class DescribeFraudBaseRequest(AbstractModel):
    """DescribeFraudBase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        """
        self._DeviceToken = None

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFraudBaseResponse(AbstractModel):
    """DescribeFraudBase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppVersion: App版本信息
        :type AppVersion: str
        :param _Brand: 品牌
        :type Brand: str
        :param _ClientIp: 客户端IP
        :type ClientIp: str
        :param _Model: 机型
        :type Model: str
        :param _NetworkType: 网络类型
        :type NetworkType: str
        :param _PackageName: 应用包名
        :type PackageName: str
        :param _Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param _SystemVersion: 系统版本
        :type SystemVersion: str
        :param _SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param _RiskInfos: 实时风险信息
        :type RiskInfos: list of RiskInfo
        :param _HistRiskInfos: 离线风险信息
        :type HistRiskInfos: list of RiskInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppVersion = None
        self._Brand = None
        self._ClientIp = None
        self._Model = None
        self._NetworkType = None
        self._PackageName = None
        self._Platform = None
        self._SystemVersion = None
        self._SdkBuildNo = None
        self._RiskInfos = None
        self._HistRiskInfos = None
        self._RequestId = None

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SystemVersion(self):
        return self._SystemVersion

    @SystemVersion.setter
    def SystemVersion(self, SystemVersion):
        self._SystemVersion = SystemVersion

    @property
    def SdkBuildNo(self):
        return self._SdkBuildNo

    @SdkBuildNo.setter
    def SdkBuildNo(self, SdkBuildNo):
        self._SdkBuildNo = SdkBuildNo

    @property
    def RiskInfos(self):
        return self._RiskInfos

    @RiskInfos.setter
    def RiskInfos(self, RiskInfos):
        self._RiskInfos = RiskInfos

    @property
    def HistRiskInfos(self):
        return self._HistRiskInfos

    @HistRiskInfos.setter
    def HistRiskInfos(self, HistRiskInfos):
        self._HistRiskInfos = HistRiskInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppVersion = params.get("AppVersion")
        self._Brand = params.get("Brand")
        self._ClientIp = params.get("ClientIp")
        self._Model = params.get("Model")
        self._NetworkType = params.get("NetworkType")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._SystemVersion = params.get("SystemVersion")
        self._SdkBuildNo = params.get("SdkBuildNo")
        if params.get("RiskInfos") is not None:
            self._RiskInfos = []
            for item in params.get("RiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._RiskInfos.append(obj)
        if params.get("HistRiskInfos") is not None:
            self._HistRiskInfos = []
            for item in params.get("HistRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._HistRiskInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFraudPremiumRequest(AbstractModel):
    """DescribeFraudPremium请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        """
        self._DeviceToken = None

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFraudPremiumResponse(AbstractModel):
    """DescribeFraudPremium返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppVersion: App版本信息
        :type AppVersion: str
        :param _Brand: 品牌
        :type Brand: str
        :param _ClientIp: 客户端IP
        :type ClientIp: str
        :param _Model: 机型
        :type Model: str
        :param _NetworkType: 网络类型
        :type NetworkType: str
        :param _PackageName: 应用包名
        :type PackageName: str
        :param _Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param _SystemVersion: 系统版本
        :type SystemVersion: str
        :param _SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param _RiskInfos: 实时风险信息
        :type RiskInfos: list of RiskInfo
        :param _HistRiskInfos: 离线风险信息
        :type HistRiskInfos: list of RiskInfo
        :param _Openid: 设备匿名标识
        :type Openid: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppVersion = None
        self._Brand = None
        self._ClientIp = None
        self._Model = None
        self._NetworkType = None
        self._PackageName = None
        self._Platform = None
        self._SystemVersion = None
        self._SdkBuildNo = None
        self._RiskInfos = None
        self._HistRiskInfos = None
        self._Openid = None
        self._RequestId = None

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SystemVersion(self):
        return self._SystemVersion

    @SystemVersion.setter
    def SystemVersion(self, SystemVersion):
        self._SystemVersion = SystemVersion

    @property
    def SdkBuildNo(self):
        return self._SdkBuildNo

    @SdkBuildNo.setter
    def SdkBuildNo(self, SdkBuildNo):
        self._SdkBuildNo = SdkBuildNo

    @property
    def RiskInfos(self):
        return self._RiskInfos

    @RiskInfos.setter
    def RiskInfos(self, RiskInfos):
        self._RiskInfos = RiskInfos

    @property
    def HistRiskInfos(self):
        return self._HistRiskInfos

    @HistRiskInfos.setter
    def HistRiskInfos(self, HistRiskInfos):
        self._HistRiskInfos = HistRiskInfos

    @property
    def Openid(self):
        return self._Openid

    @Openid.setter
    def Openid(self, Openid):
        self._Openid = Openid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppVersion = params.get("AppVersion")
        self._Brand = params.get("Brand")
        self._ClientIp = params.get("ClientIp")
        self._Model = params.get("Model")
        self._NetworkType = params.get("NetworkType")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._SystemVersion = params.get("SystemVersion")
        self._SdkBuildNo = params.get("SdkBuildNo")
        if params.get("RiskInfos") is not None:
            self._RiskInfos = []
            for item in params.get("RiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._RiskInfos.append(obj)
        if params.get("HistRiskInfos") is not None:
            self._HistRiskInfos = []
            for item in params.get("HistRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._HistRiskInfos.append(obj)
        self._Openid = params.get("Openid")
        self._RequestId = params.get("RequestId")


class DescribeFraudUltimateRequest(AbstractModel):
    """DescribeFraudUltimate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        :param _SceneCode: 使用场景。目前仅支持login-登录场景、register-注册场景
        :type SceneCode: str
        :param _UserId: 用户唯一标识
        :type UserId: str
        :param _EventTime: 事件时间戳（毫秒）
        :type EventTime: int
        :param _ElapsedTime: 事件耗时（毫秒），例如进入登录界面到点击登录按钮耗时
        :type ElapsedTime: int
        :param _WeChatOpenId: 微信的OpenId
        :type WeChatOpenId: str
        :param _PhoneNumber: 手机号码（注：不需要带国家代码 例如：13430421011）。可以传入原文或MD5
        :type PhoneNumber: str
        :param _ClientIP: 客户端IP
        :type ClientIP: str
        :param _QQOpenId: QQ的OpenId
        :type QQOpenId: str
        """
        self._DeviceToken = None
        self._SceneCode = None
        self._UserId = None
        self._EventTime = None
        self._ElapsedTime = None
        self._WeChatOpenId = None
        self._PhoneNumber = None
        self._ClientIP = None
        self._QQOpenId = None

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def SceneCode(self):
        return self._SceneCode

    @SceneCode.setter
    def SceneCode(self, SceneCode):
        self._SceneCode = SceneCode

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def EventTime(self):
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def ElapsedTime(self):
        return self._ElapsedTime

    @ElapsedTime.setter
    def ElapsedTime(self, ElapsedTime):
        self._ElapsedTime = ElapsedTime

    @property
    def WeChatOpenId(self):
        return self._WeChatOpenId

    @WeChatOpenId.setter
    def WeChatOpenId(self, WeChatOpenId):
        self._WeChatOpenId = WeChatOpenId

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def ClientIP(self):
        return self._ClientIP

    @ClientIP.setter
    def ClientIP(self, ClientIP):
        self._ClientIP = ClientIP

    @property
    def QQOpenId(self):
        return self._QQOpenId

    @QQOpenId.setter
    def QQOpenId(self, QQOpenId):
        self._QQOpenId = QQOpenId


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        self._SceneCode = params.get("SceneCode")
        self._UserId = params.get("UserId")
        self._EventTime = params.get("EventTime")
        self._ElapsedTime = params.get("ElapsedTime")
        self._WeChatOpenId = params.get("WeChatOpenId")
        self._PhoneNumber = params.get("PhoneNumber")
        self._ClientIP = params.get("ClientIP")
        self._QQOpenId = params.get("QQOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFraudUltimateResponse(AbstractModel):
    """DescribeFraudUltimate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppVersion: App版本信息
        :type AppVersion: str
        :param _Brand: 品牌
        :type Brand: str
        :param _ClientIp: 客户端IP
        :type ClientIp: str
        :param _Model: 机型
        :type Model: str
        :param _NetworkType: 网络类型
        :type NetworkType: str
        :param _PackageName: 应用包名
        :type PackageName: str
        :param _Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param _SystemVersion: 系统版本
        :type SystemVersion: str
        :param _SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param _RiskInfos: 实时风险信息
        :type RiskInfos: list of RiskInfo
        :param _HistRiskInfos: 离线风险信息
        :type HistRiskInfos: list of RiskInfo
        :param _Openid: 设备匿名标识
        :type Openid: str
        :param _SceneRiskInfos: 场景风险信息
        :type SceneRiskInfos: list of RiskInfo
        :param _SuggestionLevel: 建议等级。1-极差，2-较差，3-中等，4-良好，5-优秀
        :type SuggestionLevel: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppVersion = None
        self._Brand = None
        self._ClientIp = None
        self._Model = None
        self._NetworkType = None
        self._PackageName = None
        self._Platform = None
        self._SystemVersion = None
        self._SdkBuildNo = None
        self._RiskInfos = None
        self._HistRiskInfos = None
        self._Openid = None
        self._SceneRiskInfos = None
        self._SuggestionLevel = None
        self._RequestId = None

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SystemVersion(self):
        return self._SystemVersion

    @SystemVersion.setter
    def SystemVersion(self, SystemVersion):
        self._SystemVersion = SystemVersion

    @property
    def SdkBuildNo(self):
        return self._SdkBuildNo

    @SdkBuildNo.setter
    def SdkBuildNo(self, SdkBuildNo):
        self._SdkBuildNo = SdkBuildNo

    @property
    def RiskInfos(self):
        return self._RiskInfos

    @RiskInfos.setter
    def RiskInfos(self, RiskInfos):
        self._RiskInfos = RiskInfos

    @property
    def HistRiskInfos(self):
        return self._HistRiskInfos

    @HistRiskInfos.setter
    def HistRiskInfos(self, HistRiskInfos):
        self._HistRiskInfos = HistRiskInfos

    @property
    def Openid(self):
        return self._Openid

    @Openid.setter
    def Openid(self, Openid):
        self._Openid = Openid

    @property
    def SceneRiskInfos(self):
        return self._SceneRiskInfos

    @SceneRiskInfos.setter
    def SceneRiskInfos(self, SceneRiskInfos):
        self._SceneRiskInfos = SceneRiskInfos

    @property
    def SuggestionLevel(self):
        return self._SuggestionLevel

    @SuggestionLevel.setter
    def SuggestionLevel(self, SuggestionLevel):
        self._SuggestionLevel = SuggestionLevel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppVersion = params.get("AppVersion")
        self._Brand = params.get("Brand")
        self._ClientIp = params.get("ClientIp")
        self._Model = params.get("Model")
        self._NetworkType = params.get("NetworkType")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._SystemVersion = params.get("SystemVersion")
        self._SdkBuildNo = params.get("SdkBuildNo")
        if params.get("RiskInfos") is not None:
            self._RiskInfos = []
            for item in params.get("RiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._RiskInfos.append(obj)
        if params.get("HistRiskInfos") is not None:
            self._HistRiskInfos = []
            for item in params.get("HistRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._HistRiskInfos.append(obj)
        self._Openid = params.get("Openid")
        if params.get("SceneRiskInfos") is not None:
            self._SceneRiskInfos = []
            for item in params.get("SceneRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._SceneRiskInfos.append(obj)
        self._SuggestionLevel = params.get("SuggestionLevel")
        self._RequestId = params.get("RequestId")


class DescribeTrustedIDRequest(AbstractModel):
    """DescribeTrustedID请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        """
        self._DeviceToken = None

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrustedIDResponse(AbstractModel):
    """DescribeTrustedID返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Openid: 设备匿名标识
        :type Openid: str
        :param _AppVersion: App版本信息
        :type AppVersion: str
        :param _Brand: 品牌
        :type Brand: str
        :param _ClientIp: 客户端IP
        :type ClientIp: str
        :param _Model: 机型
        :type Model: str
        :param _NetworkType: 网络类型
        :type NetworkType: str
        :param _PackageName: 应用包名
        :type PackageName: str
        :param _Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param _SystemVersion: 系统版本
        :type SystemVersion: str
        :param _SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Openid = None
        self._AppVersion = None
        self._Brand = None
        self._ClientIp = None
        self._Model = None
        self._NetworkType = None
        self._PackageName = None
        self._Platform = None
        self._SystemVersion = None
        self._SdkBuildNo = None
        self._RequestId = None

    @property
    def Openid(self):
        return self._Openid

    @Openid.setter
    def Openid(self, Openid):
        self._Openid = Openid

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def SystemVersion(self):
        return self._SystemVersion

    @SystemVersion.setter
    def SystemVersion(self, SystemVersion):
        self._SystemVersion = SystemVersion

    @property
    def SdkBuildNo(self):
        return self._SdkBuildNo

    @SdkBuildNo.setter
    def SdkBuildNo(self, SdkBuildNo):
        self._SdkBuildNo = SdkBuildNo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Openid = params.get("Openid")
        self._AppVersion = params.get("AppVersion")
        self._Brand = params.get("Brand")
        self._ClientIp = params.get("ClientIp")
        self._Model = params.get("Model")
        self._NetworkType = params.get("NetworkType")
        self._PackageName = params.get("PackageName")
        self._Platform = params.get("Platform")
        self._SystemVersion = params.get("SystemVersion")
        self._SdkBuildNo = params.get("SdkBuildNo")
        self._RequestId = params.get("RequestId")


class RiskInfo(AbstractModel):
    """风险信息

    """

    def __init__(self):
        r"""
        :param _Type: 风险类型
        :type Type: int
        :param _Level: 风险等级
        :type Level: int
        """
        self._Type = None
        self._Level = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        