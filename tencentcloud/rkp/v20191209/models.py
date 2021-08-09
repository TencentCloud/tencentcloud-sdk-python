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


class DevInfoQ(AbstractModel):
    """设备信息

    """

    def __init__(self):
        """
        :param OpenId: devid\n        :type OpenId: str\n        :param RiskScore: 风险值\n        :type RiskScore: int\n        :param RiskInfo: 风险详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type RiskInfo: list of RiskDetail\n        :param Probability: 概率值\n        :type Probability: float\n        """
        self.OpenId = None
        self.RiskScore = None
        self.RiskInfo = None
        self.Probability = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self.RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskDetail()
                obj._deserialize(item)
                self.RiskInfo.append(obj)
        self.Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpenIdRequest(AbstractModel):
    """GetOpenId请求参数结构体

    """

    def __init__(self):
        """
        :param DeviceToken: dev临时token，通过sdk接口获取\n        :type DeviceToken: str\n        :param BusinessId: 业务ID\n        :type BusinessId: int\n        :param BusinessUserId: 业务侧账号体系下的用户ID\n        :type BusinessUserId: str\n        :param Platform: 平台：0-Android， 1-iOS， 2-web\n        :type Platform: int\n        :param Option: 选项\n        :type Option: str\n        """
        self.DeviceToken = None
        self.BusinessId = None
        self.BusinessUserId = None
        self.Platform = None
        self.Option = None


    def _deserialize(self, params):
        self.DeviceToken = params.get("DeviceToken")
        self.BusinessId = params.get("BusinessId")
        self.BusinessUserId = params.get("BusinessUserId")
        self.Platform = params.get("Platform")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpenIdResponse(AbstractModel):
    """GetOpenId返回参数结构体

    """

    def __init__(self):
        """
        :param OpenId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type OpenId: str\n        :param RiskInfo: 设备风险
注意：此字段可能返回 null，表示取不到有效值。\n        :type RiskInfo: list of RiskInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OpenId = None
        self.RiskInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        if params.get("RiskInfo") is not None:
            self.RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskInfo()
                obj._deserialize(item)
                self.RiskInfo.append(obj)
        self.RequestId = params.get("RequestId")


class GetTokenRequest(AbstractModel):
    """GetToken请求参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 业务ID\n        :type BusinessId: int\n        :param Scene: 业务子场景\n        :type Scene: int\n        :param BusinessUserId: 业务侧账号体系下的用户ID\n        :type BusinessUserId: str\n        :param AppClientIp: 用户侧的IP\n        :type AppClientIp: str\n        :param ExpireTime: 过期时间\n        :type ExpireTime: int\n        :param OldToken: 上一个token\n        :type OldToken: str\n        """
        self.BusinessId = None
        self.Scene = None
        self.BusinessUserId = None
        self.AppClientIp = None
        self.ExpireTime = None
        self.OldToken = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.Scene = params.get("Scene")
        self.BusinessUserId = params.get("BusinessUserId")
        self.AppClientIp = params.get("AppClientIp")
        self.ExpireTime = params.get("ExpireTime")
        self.OldToken = params.get("OldToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTokenResponse(AbstractModel):
    """GetToken返回参数结构体

    """

    def __init__(self):
        """
        :param Token: 返回token\n        :type Token: str\n        :param ExpireTime: 过期时间\n        :type ExpireTime: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Token = None
        self.ExpireTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.ExpireTime = params.get("ExpireTime")
        self.RequestId = params.get("RequestId")


class QueryDevAndRiskRequest(AbstractModel):
    """QueryDevAndRisk请求参数结构体

    """

    def __init__(self):
        """
        :param DevType: 设备类型 0表示Android， 1表示IOS\n        :type DevType: int\n        :param Imei: Android Imei号\n        :type Imei: str\n        :param Mac: Mac地址\n        :type Mac: str\n        :param Aid: android  Aid\n        :type Aid: str\n        :param Cid: Android Cid\n        :type Cid: str\n        :param Imsi: 手机Imsi\n        :type Imsi: str\n        :param Df: Df 磁盘分区信息\n        :type Df: str\n        :param KernelVer: 内核版本\n        :type KernelVer: str\n        :param Storage: 存储大小\n        :type Storage: str\n        :param Dfp: 设备驱动指纹\n        :type Dfp: str\n        :param BootTime: 启动时间\n        :type BootTime: str\n        :param Resolution: 分辨率 水平*垂直 格式\n        :type Resolution: str\n        :param RingList: 铃声列表\n        :type RingList: str\n        :param FontList: 字体列表\n        :type FontList: str\n        :param SensorList: 传感器列表\n        :type SensorList: str\n        :param CpuType: CPU型号\n        :type CpuType: str\n        :param Battery: 电池容量\n        :type Battery: str\n        :param Oaid: 信通院广告ID\n        :type Oaid: str\n        :param Idfa: IOS 广告ID\n        :type Idfa: str\n        :param Idfv: IOS 应用ID\n        :type Idfv: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param IphoneModel: IOS手机型号\n        :type IphoneModel: str\n        :param Fingerprint: Android 指纹\n        :type Fingerprint: str\n        :param SerialId: Android序列号\n        :type SerialId: str\n        """
        self.DevType = None
        self.Imei = None
        self.Mac = None
        self.Aid = None
        self.Cid = None
        self.Imsi = None
        self.Df = None
        self.KernelVer = None
        self.Storage = None
        self.Dfp = None
        self.BootTime = None
        self.Resolution = None
        self.RingList = None
        self.FontList = None
        self.SensorList = None
        self.CpuType = None
        self.Battery = None
        self.Oaid = None
        self.Idfa = None
        self.Idfv = None
        self.DeviceName = None
        self.IphoneModel = None
        self.Fingerprint = None
        self.SerialId = None


    def _deserialize(self, params):
        self.DevType = params.get("DevType")
        self.Imei = params.get("Imei")
        self.Mac = params.get("Mac")
        self.Aid = params.get("Aid")
        self.Cid = params.get("Cid")
        self.Imsi = params.get("Imsi")
        self.Df = params.get("Df")
        self.KernelVer = params.get("KernelVer")
        self.Storage = params.get("Storage")
        self.Dfp = params.get("Dfp")
        self.BootTime = params.get("BootTime")
        self.Resolution = params.get("Resolution")
        self.RingList = params.get("RingList")
        self.FontList = params.get("FontList")
        self.SensorList = params.get("SensorList")
        self.CpuType = params.get("CpuType")
        self.Battery = params.get("Battery")
        self.Oaid = params.get("Oaid")
        self.Idfa = params.get("Idfa")
        self.Idfv = params.get("Idfv")
        self.DeviceName = params.get("DeviceName")
        self.IphoneModel = params.get("IphoneModel")
        self.Fingerprint = params.get("Fingerprint")
        self.SerialId = params.get("SerialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDevAndRiskResponse(AbstractModel):
    """QueryDevAndRisk返回参数结构体

    """

    def __init__(self):
        """
        :param Found: 是否查得\n        :type Found: int\n        :param AllCnt: 匹配数量级别
注意：此字段可能返回 null，表示取不到有效值。\n        :type AllCnt: int\n        :param Matches: 匹配到的设备信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Matches: list of DevInfoQ\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Found = None
        self.AllCnt = None
        self.Matches = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Found = params.get("Found")
        self.AllCnt = params.get("AllCnt")
        if params.get("Matches") is not None:
            self.Matches = []
            for item in params.get("Matches"):
                obj = DevInfoQ()
                obj._deserialize(item)
                self.Matches.append(obj)
        self.RequestId = params.get("RequestId")


class RiskDetail(AbstractModel):
    """风险详情

    """

    def __init__(self):
        """
        :param RiskCode: 风险码\n        :type RiskCode: int\n        :param RiskCodeValue: 风险详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type RiskCodeValue: str\n        """
        self.RiskCode = None
        self.RiskCodeValue = None


    def _deserialize(self, params):
        self.RiskCode = params.get("RiskCode")
        self.RiskCodeValue = params.get("RiskCodeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskInfo(AbstractModel):
    """风险信息

    """

    def __init__(self):
        """
        :param Key: 风险码\n        :type Key: int\n        :param Value: 风险详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
        