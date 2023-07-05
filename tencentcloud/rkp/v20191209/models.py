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
        :param _OpenId: devid
        :type OpenId: str
        :param _RiskScore: 风险值
        :type RiskScore: int
        :param _RiskInfo: 风险详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of RiskDetail
        :param _Probability: 概率值
        :type Probability: float
        """
        self._OpenId = None
        self._RiskScore = None
        self._RiskInfo = None
        self._Probability = None

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def RiskScore(self):
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskInfo(self):
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

    @property
    def Probability(self):
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._OpenId = params.get("OpenId")
        self._RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self._RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskDetail()
                obj._deserialize(item)
                self._RiskInfo.append(obj)
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpenIdRequest(AbstractModel):
    """GetOpenId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceToken: dev临时token，通过sdk接口获取
        :type DeviceToken: str
        :param _BusinessId: 业务ID
        :type BusinessId: int
        :param _BusinessUserId: 业务侧账号体系下的用户ID
        :type BusinessUserId: str
        :param _Platform: 平台：0-Android， 1-iOS， 2-web
        :type Platform: int
        :param _Option: 选项
        :type Option: str
        """
        self._DeviceToken = None
        self._BusinessId = None
        self._BusinessUserId = None
        self._Platform = None
        self._Option = None

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def BusinessUserId(self):
        return self._BusinessUserId

    @BusinessUserId.setter
    def BusinessUserId(self, BusinessUserId):
        self._BusinessUserId = BusinessUserId

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        self._BusinessId = params.get("BusinessId")
        self._BusinessUserId = params.get("BusinessUserId")
        self._Platform = params.get("Platform")
        self._Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetOpenIdResponse(AbstractModel):
    """GetOpenId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OpenId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _RiskInfo: 设备风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of RiskInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OpenId = None
        self._RiskInfo = None
        self._RequestId = None

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def RiskInfo(self):
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OpenId = params.get("OpenId")
        if params.get("RiskInfo") is not None:
            self._RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskInfo()
                obj._deserialize(item)
                self._RiskInfo.append(obj)
        self._RequestId = params.get("RequestId")


class GetTokenRequest(AbstractModel):
    """GetToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID
        :type BusinessId: int
        :param _Scene: 业务子场景
        :type Scene: int
        :param _BusinessUserId: 业务侧账号体系下的用户ID
        :type BusinessUserId: str
        :param _AppClientIp: 用户侧的IP
        :type AppClientIp: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: int
        :param _OldToken: 上一个token
        :type OldToken: str
        """
        self._BusinessId = None
        self._Scene = None
        self._BusinessUserId = None
        self._AppClientIp = None
        self._ExpireTime = None
        self._OldToken = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def BusinessUserId(self):
        return self._BusinessUserId

    @BusinessUserId.setter
    def BusinessUserId(self, BusinessUserId):
        self._BusinessUserId = BusinessUserId

    @property
    def AppClientIp(self):
        return self._AppClientIp

    @AppClientIp.setter
    def AppClientIp(self, AppClientIp):
        self._AppClientIp = AppClientIp

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def OldToken(self):
        return self._OldToken

    @OldToken.setter
    def OldToken(self, OldToken):
        self._OldToken = OldToken


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._Scene = params.get("Scene")
        self._BusinessUserId = params.get("BusinessUserId")
        self._AppClientIp = params.get("AppClientIp")
        self._ExpireTime = params.get("ExpireTime")
        self._OldToken = params.get("OldToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTokenResponse(AbstractModel):
    """GetToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: 返回token
        :type Token: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class QueryDevAndRiskRequest(AbstractModel):
    """QueryDevAndRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DevType: 设备类型 0表示Android， 1表示IOS
        :type DevType: int
        :param _Imei: Android Imei号
        :type Imei: str
        :param _Mac: Mac地址
        :type Mac: str
        :param _Aid: android  Aid
        :type Aid: str
        :param _Cid: Android Cid
        :type Cid: str
        :param _Imsi: 手机Imsi
        :type Imsi: str
        :param _Df: Df 磁盘分区信息
        :type Df: str
        :param _KernelVer: 内核版本
        :type KernelVer: str
        :param _Storage: 存储大小
        :type Storage: str
        :param _Dfp: 设备驱动指纹
        :type Dfp: str
        :param _BootTime: 启动时间
        :type BootTime: str
        :param _Resolution: 分辨率 水平*垂直 格式
        :type Resolution: str
        :param _RingList: 铃声列表
        :type RingList: str
        :param _FontList: 字体列表
        :type FontList: str
        :param _SensorList: 传感器列表
        :type SensorList: str
        :param _CpuType: CPU型号
        :type CpuType: str
        :param _Battery: 电池容量
        :type Battery: str
        :param _Oaid: 信通院广告ID
        :type Oaid: str
        :param _Idfa: IOS 广告ID
        :type Idfa: str
        :param _Idfv: IOS 应用ID
        :type Idfv: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _IphoneModel: IOS手机型号
        :type IphoneModel: str
        :param _Fingerprint: Android 指纹
        :type Fingerprint: str
        :param _SerialId: Android序列号
        :type SerialId: str
        """
        self._DevType = None
        self._Imei = None
        self._Mac = None
        self._Aid = None
        self._Cid = None
        self._Imsi = None
        self._Df = None
        self._KernelVer = None
        self._Storage = None
        self._Dfp = None
        self._BootTime = None
        self._Resolution = None
        self._RingList = None
        self._FontList = None
        self._SensorList = None
        self._CpuType = None
        self._Battery = None
        self._Oaid = None
        self._Idfa = None
        self._Idfv = None
        self._DeviceName = None
        self._IphoneModel = None
        self._Fingerprint = None
        self._SerialId = None

    @property
    def DevType(self):
        return self._DevType

    @DevType.setter
    def DevType(self, DevType):
        self._DevType = DevType

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Mac(self):
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def Aid(self):
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid

    @property
    def Cid(self):
        return self._Cid

    @Cid.setter
    def Cid(self, Cid):
        self._Cid = Cid

    @property
    def Imsi(self):
        return self._Imsi

    @Imsi.setter
    def Imsi(self, Imsi):
        self._Imsi = Imsi

    @property
    def Df(self):
        return self._Df

    @Df.setter
    def Df(self, Df):
        self._Df = Df

    @property
    def KernelVer(self):
        return self._KernelVer

    @KernelVer.setter
    def KernelVer(self, KernelVer):
        self._KernelVer = KernelVer

    @property
    def Storage(self):
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def Dfp(self):
        return self._Dfp

    @Dfp.setter
    def Dfp(self, Dfp):
        self._Dfp = Dfp

    @property
    def BootTime(self):
        return self._BootTime

    @BootTime.setter
    def BootTime(self, BootTime):
        self._BootTime = BootTime

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def RingList(self):
        return self._RingList

    @RingList.setter
    def RingList(self, RingList):
        self._RingList = RingList

    @property
    def FontList(self):
        return self._FontList

    @FontList.setter
    def FontList(self, FontList):
        self._FontList = FontList

    @property
    def SensorList(self):
        return self._SensorList

    @SensorList.setter
    def SensorList(self, SensorList):
        self._SensorList = SensorList

    @property
    def CpuType(self):
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Battery(self):
        return self._Battery

    @Battery.setter
    def Battery(self, Battery):
        self._Battery = Battery

    @property
    def Oaid(self):
        return self._Oaid

    @Oaid.setter
    def Oaid(self, Oaid):
        self._Oaid = Oaid

    @property
    def Idfa(self):
        return self._Idfa

    @Idfa.setter
    def Idfa(self, Idfa):
        self._Idfa = Idfa

    @property
    def Idfv(self):
        return self._Idfv

    @Idfv.setter
    def Idfv(self, Idfv):
        self._Idfv = Idfv

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def IphoneModel(self):
        return self._IphoneModel

    @IphoneModel.setter
    def IphoneModel(self, IphoneModel):
        self._IphoneModel = IphoneModel

    @property
    def Fingerprint(self):
        return self._Fingerprint

    @Fingerprint.setter
    def Fingerprint(self, Fingerprint):
        self._Fingerprint = Fingerprint

    @property
    def SerialId(self):
        return self._SerialId

    @SerialId.setter
    def SerialId(self, SerialId):
        self._SerialId = SerialId


    def _deserialize(self, params):
        self._DevType = params.get("DevType")
        self._Imei = params.get("Imei")
        self._Mac = params.get("Mac")
        self._Aid = params.get("Aid")
        self._Cid = params.get("Cid")
        self._Imsi = params.get("Imsi")
        self._Df = params.get("Df")
        self._KernelVer = params.get("KernelVer")
        self._Storage = params.get("Storage")
        self._Dfp = params.get("Dfp")
        self._BootTime = params.get("BootTime")
        self._Resolution = params.get("Resolution")
        self._RingList = params.get("RingList")
        self._FontList = params.get("FontList")
        self._SensorList = params.get("SensorList")
        self._CpuType = params.get("CpuType")
        self._Battery = params.get("Battery")
        self._Oaid = params.get("Oaid")
        self._Idfa = params.get("Idfa")
        self._Idfv = params.get("Idfv")
        self._DeviceName = params.get("DeviceName")
        self._IphoneModel = params.get("IphoneModel")
        self._Fingerprint = params.get("Fingerprint")
        self._SerialId = params.get("SerialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDevAndRiskResponse(AbstractModel):
    """QueryDevAndRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Found: 是否查得
        :type Found: int
        :param _AllCnt: 匹配数量级别
注意：此字段可能返回 null，表示取不到有效值。
        :type AllCnt: int
        :param _Matches: 匹配到的设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Matches: list of DevInfoQ
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Found = None
        self._AllCnt = None
        self._Matches = None
        self._RequestId = None

    @property
    def Found(self):
        return self._Found

    @Found.setter
    def Found(self, Found):
        self._Found = Found

    @property
    def AllCnt(self):
        return self._AllCnt

    @AllCnt.setter
    def AllCnt(self, AllCnt):
        self._AllCnt = AllCnt

    @property
    def Matches(self):
        return self._Matches

    @Matches.setter
    def Matches(self, Matches):
        self._Matches = Matches

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Found = params.get("Found")
        self._AllCnt = params.get("AllCnt")
        if params.get("Matches") is not None:
            self._Matches = []
            for item in params.get("Matches"):
                obj = DevInfoQ()
                obj._deserialize(item)
                self._Matches.append(obj)
        self._RequestId = params.get("RequestId")


class RiskDetail(AbstractModel):
    """风险详情

    """

    def __init__(self):
        r"""
        :param _RiskCode: 风险码
        :type RiskCode: int
        :param _RiskCodeValue: 风险详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCodeValue: str
        """
        self._RiskCode = None
        self._RiskCodeValue = None

    @property
    def RiskCode(self):
        return self._RiskCode

    @RiskCode.setter
    def RiskCode(self, RiskCode):
        self._RiskCode = RiskCode

    @property
    def RiskCodeValue(self):
        return self._RiskCodeValue

    @RiskCodeValue.setter
    def RiskCodeValue(self, RiskCodeValue):
        self._RiskCodeValue = RiskCodeValue


    def _deserialize(self, params):
        self._RiskCode = params.get("RiskCode")
        self._RiskCodeValue = params.get("RiskCodeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskInfo(AbstractModel):
    """风险信息

    """

    def __init__(self):
        r"""
        :param _Key: 风险码
        :type Key: int
        :param _Value: 风险详情
注意：此字段可能返回 null，表示取不到有效值。
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
        