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
        r"""
        :param OpenId: devid
        :type OpenId: str
        :param RiskScore: 风险值
        :type RiskScore: int
        :param RiskInfo: 风险详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of RiskDetail
        :param Probability: 概率值
        :type Probability: float
        """
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
        r"""
        :param DeviceToken: dev临时token，通过sdk接口获取
        :type DeviceToken: str
        :param BusinessId: 业务ID
        :type BusinessId: int
        :param BusinessUserId: 业务侧账号体系下的用户ID
        :type BusinessUserId: str
        :param Platform: 平台：0-Android， 1-iOS， 2-web
        :type Platform: int
        :param Option: 选项
        :type Option: str
        """
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
        r"""
        :param OpenId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param RiskInfo: 设备风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of RiskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param BusinessId: 业务ID
        :type BusinessId: int
        :param Scene: 业务子场景
        :type Scene: int
        :param BusinessUserId: 业务侧账号体系下的用户ID
        :type BusinessUserId: str
        :param AppClientIp: 用户侧的IP
        :type AppClientIp: str
        :param ExpireTime: 过期时间
        :type ExpireTime: int
        :param OldToken: 上一个token
        :type OldToken: str
        """
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
        r"""
        :param Token: 返回token
        :type Token: str
        :param ExpireTime: 过期时间
        :type ExpireTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param DevType: 设备类型 0表示Android， 1表示IOS
        :type DevType: int
        :param Imei: Android Imei号
        :type Imei: str
        :param Mac: Mac地址
        :type Mac: str
        :param Aid: android  Aid
        :type Aid: str
        :param Cid: Android Cid
        :type Cid: str
        :param Imsi: 手机Imsi
        :type Imsi: str
        :param Df: Df 磁盘分区信息
        :type Df: str
        :param KernelVer: 内核版本
        :type KernelVer: str
        :param Storage: 存储大小
        :type Storage: str
        :param Dfp: 设备驱动指纹
        :type Dfp: str
        :param BootTime: 启动时间
        :type BootTime: str
        :param Resolution: 分辨率 水平*垂直 格式
        :type Resolution: str
        :param RingList: 铃声列表
        :type RingList: str
        :param FontList: 字体列表
        :type FontList: str
        :param SensorList: 传感器列表
        :type SensorList: str
        :param CpuType: CPU型号
        :type CpuType: str
        :param Battery: 电池容量
        :type Battery: str
        :param Oaid: 信通院广告ID
        :type Oaid: str
        :param Idfa: IOS 广告ID
        :type Idfa: str
        :param Idfv: IOS 应用ID
        :type Idfv: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param IphoneModel: IOS手机型号
        :type IphoneModel: str
        :param Fingerprint: Android 指纹
        :type Fingerprint: str
        :param SerialId: Android序列号
        :type SerialId: str
        """
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
        r"""
        :param Found: 是否查得
        :type Found: int
        :param AllCnt: 匹配数量级别
注意：此字段可能返回 null，表示取不到有效值。
        :type AllCnt: int
        :param Matches: 匹配到的设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Matches: list of DevInfoQ
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param RiskCode: 风险码
        :type RiskCode: int
        :param RiskCodeValue: 风险详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCodeValue: str
        """
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
        r"""
        :param Key: 风险码
        :type Key: int
        :param Value: 风险详情
注意：此字段可能返回 null，表示取不到有效值。
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
        