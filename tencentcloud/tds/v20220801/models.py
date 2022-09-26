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
        