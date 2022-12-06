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
        :param DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        """
        self.DeviceToken = None


    def _deserialize(self, params):
        self.DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFraudBaseResponse(AbstractModel):
    """DescribeFraudBase返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppVersion: App版本信息
        :type AppVersion: str
        :param Brand: 品牌
        :type Brand: str
        :param ClientIp: 客户端IP
        :type ClientIp: str
        :param Model: 机型
        :type Model: str
        :param NetworkType: 网络类型
        :type NetworkType: str
        :param PackageName: 应用包名
        :type PackageName: str
        :param Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param SystemVersion: 系统版本
        :type SystemVersion: str
        :param SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param RiskInfos: 实时风险信息
        :type RiskInfos: list of RiskInfo
        :param HistRiskInfos: 离线风险信息
        :type HistRiskInfos: list of RiskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppVersion = None
        self.Brand = None
        self.ClientIp = None
        self.Model = None
        self.NetworkType = None
        self.PackageName = None
        self.Platform = None
        self.SystemVersion = None
        self.SdkBuildNo = None
        self.RiskInfos = None
        self.HistRiskInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppVersion = params.get("AppVersion")
        self.Brand = params.get("Brand")
        self.ClientIp = params.get("ClientIp")
        self.Model = params.get("Model")
        self.NetworkType = params.get("NetworkType")
        self.PackageName = params.get("PackageName")
        self.Platform = params.get("Platform")
        self.SystemVersion = params.get("SystemVersion")
        self.SdkBuildNo = params.get("SdkBuildNo")
        if params.get("RiskInfos") is not None:
            self.RiskInfos = []
            for item in params.get("RiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.RiskInfos.append(obj)
        if params.get("HistRiskInfos") is not None:
            self.HistRiskInfos = []
            for item in params.get("HistRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.HistRiskInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFraudPremiumRequest(AbstractModel):
    """DescribeFraudPremium请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        """
        self.DeviceToken = None


    def _deserialize(self, params):
        self.DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFraudPremiumResponse(AbstractModel):
    """DescribeFraudPremium返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppVersion: App版本信息
        :type AppVersion: str
        :param Brand: 品牌
        :type Brand: str
        :param ClientIp: 客户端IP
        :type ClientIp: str
        :param Model: 机型
        :type Model: str
        :param NetworkType: 网络类型
        :type NetworkType: str
        :param PackageName: 应用包名
        :type PackageName: str
        :param Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param SystemVersion: 系统版本
        :type SystemVersion: str
        :param SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param RiskInfos: 实时风险信息
        :type RiskInfos: list of RiskInfo
        :param HistRiskInfos: 离线风险信息
        :type HistRiskInfos: list of RiskInfo
        :param Openid: 设备匿名标识
        :type Openid: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppVersion = None
        self.Brand = None
        self.ClientIp = None
        self.Model = None
        self.NetworkType = None
        self.PackageName = None
        self.Platform = None
        self.SystemVersion = None
        self.SdkBuildNo = None
        self.RiskInfos = None
        self.HistRiskInfos = None
        self.Openid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppVersion = params.get("AppVersion")
        self.Brand = params.get("Brand")
        self.ClientIp = params.get("ClientIp")
        self.Model = params.get("Model")
        self.NetworkType = params.get("NetworkType")
        self.PackageName = params.get("PackageName")
        self.Platform = params.get("Platform")
        self.SystemVersion = params.get("SystemVersion")
        self.SdkBuildNo = params.get("SdkBuildNo")
        if params.get("RiskInfos") is not None:
            self.RiskInfos = []
            for item in params.get("RiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.RiskInfos.append(obj)
        if params.get("HistRiskInfos") is not None:
            self.HistRiskInfos = []
            for item in params.get("HistRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.HistRiskInfos.append(obj)
        self.Openid = params.get("Openid")
        self.RequestId = params.get("RequestId")


class DescribeFraudUltimateRequest(AbstractModel):
    """DescribeFraudUltimate请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        :param SceneCode: 使用场景。目前仅支持login-登录场景、register-注册场景
        :type SceneCode: str
        :param UserId: 用户唯一标识
        :type UserId: str
        :param EventTime: 事件时间戳（毫秒）
        :type EventTime: int
        :param ElapsedTime: 事件耗时（毫秒），例如进入登录界面到点击登录按钮耗时
        :type ElapsedTime: int
        :param WeChatOpenId: 微信的OpenId
        :type WeChatOpenId: str
        :param PhoneNumber: 手机号码（注：不需要带国家代码 例如：13430421011）。可以传入原文或MD5
        :type PhoneNumber: str
        :param ClientIP: 客户端IP
        :type ClientIP: str
        :param QQOpenId: QQ的OpenId
        :type QQOpenId: str
        """
        self.DeviceToken = None
        self.SceneCode = None
        self.UserId = None
        self.EventTime = None
        self.ElapsedTime = None
        self.WeChatOpenId = None
        self.PhoneNumber = None
        self.ClientIP = None
        self.QQOpenId = None


    def _deserialize(self, params):
        self.DeviceToken = params.get("DeviceToken")
        self.SceneCode = params.get("SceneCode")
        self.UserId = params.get("UserId")
        self.EventTime = params.get("EventTime")
        self.ElapsedTime = params.get("ElapsedTime")
        self.WeChatOpenId = params.get("WeChatOpenId")
        self.PhoneNumber = params.get("PhoneNumber")
        self.ClientIP = params.get("ClientIP")
        self.QQOpenId = params.get("QQOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFraudUltimateResponse(AbstractModel):
    """DescribeFraudUltimate返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppVersion: App版本信息
        :type AppVersion: str
        :param Brand: 品牌
        :type Brand: str
        :param ClientIp: 客户端IP
        :type ClientIp: str
        :param Model: 机型
        :type Model: str
        :param NetworkType: 网络类型
        :type NetworkType: str
        :param PackageName: 应用包名
        :type PackageName: str
        :param Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param SystemVersion: 系统版本
        :type SystemVersion: str
        :param SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param RiskInfos: 实时风险信息
        :type RiskInfos: list of RiskInfo
        :param HistRiskInfos: 离线风险信息
        :type HistRiskInfos: list of RiskInfo
        :param Openid: 设备匿名标识
        :type Openid: str
        :param SceneRiskInfos: 场景风险信息
        :type SceneRiskInfos: list of RiskInfo
        :param SuggestionLevel: 建议等级。1-极差，2-较差，3-中等，4-良好，5-优秀
        :type SuggestionLevel: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppVersion = None
        self.Brand = None
        self.ClientIp = None
        self.Model = None
        self.NetworkType = None
        self.PackageName = None
        self.Platform = None
        self.SystemVersion = None
        self.SdkBuildNo = None
        self.RiskInfos = None
        self.HistRiskInfos = None
        self.Openid = None
        self.SceneRiskInfos = None
        self.SuggestionLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppVersion = params.get("AppVersion")
        self.Brand = params.get("Brand")
        self.ClientIp = params.get("ClientIp")
        self.Model = params.get("Model")
        self.NetworkType = params.get("NetworkType")
        self.PackageName = params.get("PackageName")
        self.Platform = params.get("Platform")
        self.SystemVersion = params.get("SystemVersion")
        self.SdkBuildNo = params.get("SdkBuildNo")
        if params.get("RiskInfos") is not None:
            self.RiskInfos = []
            for item in params.get("RiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.RiskInfos.append(obj)
        if params.get("HistRiskInfos") is not None:
            self.HistRiskInfos = []
            for item in params.get("HistRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.HistRiskInfos.append(obj)
        self.Openid = params.get("Openid")
        if params.get("SceneRiskInfos") is not None:
            self.SceneRiskInfos = []
            for item in params.get("SceneRiskInfos"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.SceneRiskInfos.append(obj)
        self.SuggestionLevel = params.get("SuggestionLevel")
        self.RequestId = params.get("RequestId")


class DescribeTrustedIDRequest(AbstractModel):
    """DescribeTrustedID请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceToken: 客户端通过SDK获取的设备Token
        :type DeviceToken: str
        """
        self.DeviceToken = None


    def _deserialize(self, params):
        self.DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrustedIDResponse(AbstractModel):
    """DescribeTrustedID返回参数结构体

    """

    def __init__(self):
        r"""
        :param Openid: 设备匿名标识
        :type Openid: str
        :param AppVersion: App版本信息
        :type AppVersion: str
        :param Brand: 品牌
        :type Brand: str
        :param ClientIp: 客户端IP
        :type ClientIp: str
        :param Model: 机型
        :type Model: str
        :param NetworkType: 网络类型
        :type NetworkType: str
        :param PackageName: 应用包名
        :type PackageName: str
        :param Platform: 平台（2-Android，3-iOS，4-H5，5-微信小程序）
        :type Platform: str
        :param SystemVersion: 系统版本
        :type SystemVersion: str
        :param SdkBuildNo: SDK版本号
        :type SdkBuildNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Openid = None
        self.AppVersion = None
        self.Brand = None
        self.ClientIp = None
        self.Model = None
        self.NetworkType = None
        self.PackageName = None
        self.Platform = None
        self.SystemVersion = None
        self.SdkBuildNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Openid = params.get("Openid")
        self.AppVersion = params.get("AppVersion")
        self.Brand = params.get("Brand")
        self.ClientIp = params.get("ClientIp")
        self.Model = params.get("Model")
        self.NetworkType = params.get("NetworkType")
        self.PackageName = params.get("PackageName")
        self.Platform = params.get("Platform")
        self.SystemVersion = params.get("SystemVersion")
        self.SdkBuildNo = params.get("SdkBuildNo")
        self.RequestId = params.get("RequestId")


class RiskInfo(AbstractModel):
    """风险信息

    """

    def __init__(self):
        r"""
        :param Type: 风险类型
        :type Type: int
        :param Level: 风险等级
        :type Level: int
        """
        self.Type = None
        self.Level = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        