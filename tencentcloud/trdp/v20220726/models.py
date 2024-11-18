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


class AccountInfo(AbstractModel):
    """账号信息

    """

    def __init__(self):
        r"""
        :param _AccountType: 用户账号类型：
1-手机号；
2-IMEI；
3-IDFA；
100-SSID类型
        :type AccountType: int
        :param _UniversalAccount: 通用账号信息，当AccountType为1、2、3、100时必填
        :type UniversalAccount: :class:`tencentcloud.trdp.v20220726.models.UniversalAccountInfo`
        """
        self._AccountType = None
        self._UniversalAccount = None

    @property
    def AccountType(self):
        """用户账号类型：
1-手机号；
2-IMEI；
3-IDFA；
100-SSID类型
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def UniversalAccount(self):
        """通用账号信息，当AccountType为1、2、3、100时必填
        :rtype: :class:`tencentcloud.trdp.v20220726.models.UniversalAccountInfo`
        """
        return self._UniversalAccount

    @UniversalAccount.setter
    def UniversalAccount(self, UniversalAccount):
        self._UniversalAccount = UniversalAccount


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        if params.get("UniversalAccount") is not None:
            self._UniversalAccount = UniversalAccountInfo()
            self._UniversalAccount._deserialize(params.get("UniversalAccount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDetailInfo(AbstractModel):
    """设备详情

    """

    def __init__(self):
        r"""
        :param _MacAddress: mac地址或唯一设备标识
        :type MacAddress: str
        :param _Model: 手机型号
        :type Model: str
        :param _OsSystem: 操作系统(unknown，android，ios，windows)
        :type OsSystem: str
        :param _OsSystemVersion: 操作系统版本
        :type OsSystemVersion: str
        :param _BidFloor: 竞价底价
        :type BidFloor: int
        :param _DeviceVersion: 设备版本
        :type DeviceVersion: str
        :param _Maker: 设备制造商
        :type Maker: str
        :param _DeviceType: 设备类型（PHONE,TABLET）
        :type DeviceType: str
        :param _Carrier: 运营商；-1: 获取失败，0: 其他，1: 移动，2: 联通，3: 电信，4: 铁通
        :type Carrier: str
        :param _AccessMode: 入网方式(wifi,5g,4g,3g,2g)
        :type AccessMode: str
        :param _PhoneChipInfo: 手机芯片信息
        :type PhoneChipInfo: str
        :param _CpuModel: CPU 型号
        :type CpuModel: str
        :param _CpuCore: CPU 核数
        :type CpuCore: str
        :param _Memory: 内存容量，单位转换为 GB
        :type Memory: str
        :param _Language: 系统语言
        :type Language: str
        :param _Volume: 手机音量
        :type Volume: str
        :param _BatteryPower: 电池电量
        :type BatteryPower: str
        :param _ResolutionWidth: 屏幕分辨率宽，保留整数
        :type ResolutionWidth: int
        :param _ResolutionHeight: 屏幕分辨率高，保留整数
        :type ResolutionHeight: int
        :param _Ua: 浏览器类型
        :type Ua: str
        :param _App: 客户端应用
        :type App: str
        :param _AppPackageName: 应用包名
        :type AppPackageName: str
        :param _SerialNumber: 设备序列号
Android设备
        :type SerialNumber: str
        :param _MobileCountryAndNetworkCode: netOperator MCC+MNC
Android设备
        :type MobileCountryAndNetworkCode: str
        :param _VendorId: 设备品牌 “华为”“oppo”“小米”
Android设备
        :type VendorId: str
        :param _AndroidApiLevel: Android API等级
Android设备
        :type AndroidApiLevel: str
        :param _Brightness: 屏幕亮度
Android设备
        :type Brightness: str
        :param _BluetoothAddress: 蓝牙地址
Android设备
        :type BluetoothAddress: str
        :param _BaseBandVersion: 基带版本
Android设备
        :type BaseBandVersion: str
        :param _KernelVersion: kernel 版本
Android设备
        :type KernelVersion: str
        :param _Storage: 存储容量，单位转换为 GB
Android设备
        :type Storage: str
        :param _PackageName: 软件包名
Android设备
        :type PackageName: str
        :param _AppVersion: app 版本号
Android设备
        :type AppVersion: str
        :param _AppName: app 显示名称
Android设备
        :type AppName: str
        :param _IsDebug: 是否 debug；0 为正常模式，1 为 debug 模式；其他值无效
Android设备
        :type IsDebug: str
        :param _IsRoot: 是否越狱；0 为正常，1 为越狱；其他值无效
Android设备
        :type IsRoot: str
        :param _IsProxy: 是否启动代理；0 为未开启，1 为开启；其他值无效
Android设备
        :type IsProxy: str
        :param _IsEmulator: 是否模拟器；0 为未开启，1 为开启；其他值无效
Android设备
        :type IsEmulator: str
        :param _ChargeStatus: 充电状态；1-不在充电，2-USB充电，3-电源充电
Android设备
        :type ChargeStatus: str
        :param _NetworkType: 网络类型：2G/3G/4G/5G/Wi-Fi/WWAN/other
Android设备
        :type NetworkType: str
        :param _WifiMac: Wi-Fi MAC地址
Android设备
        :type WifiMac: str
        :param _DeviceName: 设备名称 "xxx 的 iPhone"，"xxx's IPhone" 等等
IOS设备
        :type DeviceName: str
        :param _StartupTime: 开机时间
IOS设备
        :type StartupTime: str
        :param _Lon: 所在经度
        :type Lon: str
        :param _Lat: 所在纬度
        :type Lat: str
        """
        self._MacAddress = None
        self._Model = None
        self._OsSystem = None
        self._OsSystemVersion = None
        self._BidFloor = None
        self._DeviceVersion = None
        self._Maker = None
        self._DeviceType = None
        self._Carrier = None
        self._AccessMode = None
        self._PhoneChipInfo = None
        self._CpuModel = None
        self._CpuCore = None
        self._Memory = None
        self._Language = None
        self._Volume = None
        self._BatteryPower = None
        self._ResolutionWidth = None
        self._ResolutionHeight = None
        self._Ua = None
        self._App = None
        self._AppPackageName = None
        self._SerialNumber = None
        self._MobileCountryAndNetworkCode = None
        self._VendorId = None
        self._AndroidApiLevel = None
        self._Brightness = None
        self._BluetoothAddress = None
        self._BaseBandVersion = None
        self._KernelVersion = None
        self._Storage = None
        self._PackageName = None
        self._AppVersion = None
        self._AppName = None
        self._IsDebug = None
        self._IsRoot = None
        self._IsProxy = None
        self._IsEmulator = None
        self._ChargeStatus = None
        self._NetworkType = None
        self._WifiMac = None
        self._DeviceName = None
        self._StartupTime = None
        self._Lon = None
        self._Lat = None

    @property
    def MacAddress(self):
        """mac地址或唯一设备标识
        :rtype: str
        """
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def Model(self):
        """手机型号
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def OsSystem(self):
        """操作系统(unknown，android，ios，windows)
        :rtype: str
        """
        return self._OsSystem

    @OsSystem.setter
    def OsSystem(self, OsSystem):
        self._OsSystem = OsSystem

    @property
    def OsSystemVersion(self):
        """操作系统版本
        :rtype: str
        """
        return self._OsSystemVersion

    @OsSystemVersion.setter
    def OsSystemVersion(self, OsSystemVersion):
        self._OsSystemVersion = OsSystemVersion

    @property
    def BidFloor(self):
        """竞价底价
        :rtype: int
        """
        return self._BidFloor

    @BidFloor.setter
    def BidFloor(self, BidFloor):
        self._BidFloor = BidFloor

    @property
    def DeviceVersion(self):
        """设备版本
        :rtype: str
        """
        return self._DeviceVersion

    @DeviceVersion.setter
    def DeviceVersion(self, DeviceVersion):
        self._DeviceVersion = DeviceVersion

    @property
    def Maker(self):
        """设备制造商
        :rtype: str
        """
        return self._Maker

    @Maker.setter
    def Maker(self, Maker):
        self._Maker = Maker

    @property
    def DeviceType(self):
        """设备类型（PHONE,TABLET）
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Carrier(self):
        """运营商；-1: 获取失败，0: 其他，1: 移动，2: 联通，3: 电信，4: 铁通
        :rtype: str
        """
        return self._Carrier

    @Carrier.setter
    def Carrier(self, Carrier):
        self._Carrier = Carrier

    @property
    def AccessMode(self):
        """入网方式(wifi,5g,4g,3g,2g)
        :rtype: str
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def PhoneChipInfo(self):
        """手机芯片信息
        :rtype: str
        """
        return self._PhoneChipInfo

    @PhoneChipInfo.setter
    def PhoneChipInfo(self, PhoneChipInfo):
        self._PhoneChipInfo = PhoneChipInfo

    @property
    def CpuModel(self):
        """CPU 型号
        :rtype: str
        """
        return self._CpuModel

    @CpuModel.setter
    def CpuModel(self, CpuModel):
        self._CpuModel = CpuModel

    @property
    def CpuCore(self):
        """CPU 核数
        :rtype: str
        """
        return self._CpuCore

    @CpuCore.setter
    def CpuCore(self, CpuCore):
        self._CpuCore = CpuCore

    @property
    def Memory(self):
        """内存容量，单位转换为 GB
        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Language(self):
        """系统语言
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def Volume(self):
        """手机音量
        :rtype: str
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def BatteryPower(self):
        """电池电量
        :rtype: str
        """
        return self._BatteryPower

    @BatteryPower.setter
    def BatteryPower(self, BatteryPower):
        self._BatteryPower = BatteryPower

    @property
    def ResolutionWidth(self):
        """屏幕分辨率宽，保留整数
        :rtype: int
        """
        return self._ResolutionWidth

    @ResolutionWidth.setter
    def ResolutionWidth(self, ResolutionWidth):
        self._ResolutionWidth = ResolutionWidth

    @property
    def ResolutionHeight(self):
        """屏幕分辨率高，保留整数
        :rtype: int
        """
        return self._ResolutionHeight

    @ResolutionHeight.setter
    def ResolutionHeight(self, ResolutionHeight):
        self._ResolutionHeight = ResolutionHeight

    @property
    def Ua(self):
        """浏览器类型
        :rtype: str
        """
        return self._Ua

    @Ua.setter
    def Ua(self, Ua):
        self._Ua = Ua

    @property
    def App(self):
        """客户端应用
        :rtype: str
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App

    @property
    def AppPackageName(self):
        """应用包名
        :rtype: str
        """
        return self._AppPackageName

    @AppPackageName.setter
    def AppPackageName(self, AppPackageName):
        self._AppPackageName = AppPackageName

    @property
    def SerialNumber(self):
        """设备序列号
Android设备
        :rtype: str
        """
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def MobileCountryAndNetworkCode(self):
        """netOperator MCC+MNC
Android设备
        :rtype: str
        """
        return self._MobileCountryAndNetworkCode

    @MobileCountryAndNetworkCode.setter
    def MobileCountryAndNetworkCode(self, MobileCountryAndNetworkCode):
        self._MobileCountryAndNetworkCode = MobileCountryAndNetworkCode

    @property
    def VendorId(self):
        """设备品牌 “华为”“oppo”“小米”
Android设备
        :rtype: str
        """
        return self._VendorId

    @VendorId.setter
    def VendorId(self, VendorId):
        self._VendorId = VendorId

    @property
    def AndroidApiLevel(self):
        """Android API等级
Android设备
        :rtype: str
        """
        return self._AndroidApiLevel

    @AndroidApiLevel.setter
    def AndroidApiLevel(self, AndroidApiLevel):
        self._AndroidApiLevel = AndroidApiLevel

    @property
    def Brightness(self):
        """屏幕亮度
Android设备
        :rtype: str
        """
        return self._Brightness

    @Brightness.setter
    def Brightness(self, Brightness):
        self._Brightness = Brightness

    @property
    def BluetoothAddress(self):
        """蓝牙地址
Android设备
        :rtype: str
        """
        return self._BluetoothAddress

    @BluetoothAddress.setter
    def BluetoothAddress(self, BluetoothAddress):
        self._BluetoothAddress = BluetoothAddress

    @property
    def BaseBandVersion(self):
        """基带版本
Android设备
        :rtype: str
        """
        return self._BaseBandVersion

    @BaseBandVersion.setter
    def BaseBandVersion(self, BaseBandVersion):
        self._BaseBandVersion = BaseBandVersion

    @property
    def KernelVersion(self):
        """kernel 版本
Android设备
        :rtype: str
        """
        return self._KernelVersion

    @KernelVersion.setter
    def KernelVersion(self, KernelVersion):
        self._KernelVersion = KernelVersion

    @property
    def Storage(self):
        """存储容量，单位转换为 GB
Android设备
        :rtype: str
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage

    @property
    def PackageName(self):
        """软件包名
Android设备
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def AppVersion(self):
        """app 版本号
Android设备
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def AppName(self):
        """app 显示名称
Android设备
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def IsDebug(self):
        """是否 debug；0 为正常模式，1 为 debug 模式；其他值无效
Android设备
        :rtype: str
        """
        return self._IsDebug

    @IsDebug.setter
    def IsDebug(self, IsDebug):
        self._IsDebug = IsDebug

    @property
    def IsRoot(self):
        """是否越狱；0 为正常，1 为越狱；其他值无效
Android设备
        :rtype: str
        """
        return self._IsRoot

    @IsRoot.setter
    def IsRoot(self, IsRoot):
        self._IsRoot = IsRoot

    @property
    def IsProxy(self):
        """是否启动代理；0 为未开启，1 为开启；其他值无效
Android设备
        :rtype: str
        """
        return self._IsProxy

    @IsProxy.setter
    def IsProxy(self, IsProxy):
        self._IsProxy = IsProxy

    @property
    def IsEmulator(self):
        """是否模拟器；0 为未开启，1 为开启；其他值无效
Android设备
        :rtype: str
        """
        return self._IsEmulator

    @IsEmulator.setter
    def IsEmulator(self, IsEmulator):
        self._IsEmulator = IsEmulator

    @property
    def ChargeStatus(self):
        """充电状态；1-不在充电，2-USB充电，3-电源充电
Android设备
        :rtype: str
        """
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def NetworkType(self):
        """网络类型：2G/3G/4G/5G/Wi-Fi/WWAN/other
Android设备
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def WifiMac(self):
        """Wi-Fi MAC地址
Android设备
        :rtype: str
        """
        return self._WifiMac

    @WifiMac.setter
    def WifiMac(self, WifiMac):
        self._WifiMac = WifiMac

    @property
    def DeviceName(self):
        """设备名称 "xxx 的 iPhone"，"xxx's IPhone" 等等
IOS设备
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def StartupTime(self):
        """开机时间
IOS设备
        :rtype: str
        """
        return self._StartupTime

    @StartupTime.setter
    def StartupTime(self, StartupTime):
        self._StartupTime = StartupTime

    @property
    def Lon(self):
        """所在经度
        :rtype: str
        """
        return self._Lon

    @Lon.setter
    def Lon(self, Lon):
        self._Lon = Lon

    @property
    def Lat(self):
        """所在纬度
        :rtype: str
        """
        return self._Lat

    @Lat.setter
    def Lat(self, Lat):
        self._Lat = Lat


    def _deserialize(self, params):
        self._MacAddress = params.get("MacAddress")
        self._Model = params.get("Model")
        self._OsSystem = params.get("OsSystem")
        self._OsSystemVersion = params.get("OsSystemVersion")
        self._BidFloor = params.get("BidFloor")
        self._DeviceVersion = params.get("DeviceVersion")
        self._Maker = params.get("Maker")
        self._DeviceType = params.get("DeviceType")
        self._Carrier = params.get("Carrier")
        self._AccessMode = params.get("AccessMode")
        self._PhoneChipInfo = params.get("PhoneChipInfo")
        self._CpuModel = params.get("CpuModel")
        self._CpuCore = params.get("CpuCore")
        self._Memory = params.get("Memory")
        self._Language = params.get("Language")
        self._Volume = params.get("Volume")
        self._BatteryPower = params.get("BatteryPower")
        self._ResolutionWidth = params.get("ResolutionWidth")
        self._ResolutionHeight = params.get("ResolutionHeight")
        self._Ua = params.get("Ua")
        self._App = params.get("App")
        self._AppPackageName = params.get("AppPackageName")
        self._SerialNumber = params.get("SerialNumber")
        self._MobileCountryAndNetworkCode = params.get("MobileCountryAndNetworkCode")
        self._VendorId = params.get("VendorId")
        self._AndroidApiLevel = params.get("AndroidApiLevel")
        self._Brightness = params.get("Brightness")
        self._BluetoothAddress = params.get("BluetoothAddress")
        self._BaseBandVersion = params.get("BaseBandVersion")
        self._KernelVersion = params.get("KernelVersion")
        self._Storage = params.get("Storage")
        self._PackageName = params.get("PackageName")
        self._AppVersion = params.get("AppVersion")
        self._AppName = params.get("AppName")
        self._IsDebug = params.get("IsDebug")
        self._IsRoot = params.get("IsRoot")
        self._IsProxy = params.get("IsProxy")
        self._IsEmulator = params.get("IsEmulator")
        self._ChargeStatus = params.get("ChargeStatus")
        self._NetworkType = params.get("NetworkType")
        self._WifiMac = params.get("WifiMac")
        self._DeviceName = params.get("DeviceName")
        self._StartupTime = params.get("StartupTime")
        self._Lon = params.get("Lon")
        self._Lat = params.get("Lat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceFingerprintInfo(AbstractModel):
    """设备指纹信息

    """

    def __init__(self):
        r"""
        :param _DeviceToken: 设备指纹Token
        :type DeviceToken: str
        :param _SdkChannel: 设备指纹的客户端SDK对应渠道
        :type SdkChannel: str
        """
        self._DeviceToken = None
        self._SdkChannel = None

    @property
    def DeviceToken(self):
        """设备指纹Token
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def SdkChannel(self):
        """设备指纹的客户端SDK对应渠道
        :rtype: str
        """
        return self._SdkChannel

    @SdkChannel.setter
    def SdkChannel(self, SdkChannel):
        self._SdkChannel = SdkChannel


    def _deserialize(self, params):
        self._DeviceToken = params.get("DeviceToken")
        self._SdkChannel = params.get("SdkChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateUserRiskRequest(AbstractModel):
    """EvaluateUserRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Account: 账号信息
        :type Account: :class:`tencentcloud.trdp.v20220726.models.AccountInfo`
        :param _User: 用户信息
        :type User: :class:`tencentcloud.trdp.v20220726.models.UserInfo`
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _DeviceFingerprint: 设备指纹信息
        :type DeviceFingerprint: :class:`tencentcloud.trdp.v20220726.models.DeviceFingerprintInfo`
        :param _SceneCode: 场景Code，不传默认活动防刷；
e_activity_antirush；活动防刷场景
e_login_protection；登录保护场景
e_register_protection：注册保护场景
        :type SceneCode: str
        :param _DeviceDetail: 设备详情
        :type DeviceDetail: :class:`tencentcloud.trdp.v20220726.models.DeviceDetailInfo`
        :param _Marketing: 营销信息
        :type Marketing: :class:`tencentcloud.trdp.v20220726.models.MarketingInfo`
        """
        self._Account = None
        self._User = None
        self._ModelId = None
        self._DeviceFingerprint = None
        self._SceneCode = None
        self._DeviceDetail = None
        self._Marketing = None

    @property
    def Account(self):
        """账号信息
        :rtype: :class:`tencentcloud.trdp.v20220726.models.AccountInfo`
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def User(self):
        """用户信息
        :rtype: :class:`tencentcloud.trdp.v20220726.models.UserInfo`
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def ModelId(self):
        """模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def DeviceFingerprint(self):
        """设备指纹信息
        :rtype: :class:`tencentcloud.trdp.v20220726.models.DeviceFingerprintInfo`
        """
        return self._DeviceFingerprint

    @DeviceFingerprint.setter
    def DeviceFingerprint(self, DeviceFingerprint):
        self._DeviceFingerprint = DeviceFingerprint

    @property
    def SceneCode(self):
        """场景Code，不传默认活动防刷；
e_activity_antirush；活动防刷场景
e_login_protection；登录保护场景
e_register_protection：注册保护场景
        :rtype: str
        """
        return self._SceneCode

    @SceneCode.setter
    def SceneCode(self, SceneCode):
        self._SceneCode = SceneCode

    @property
    def DeviceDetail(self):
        """设备详情
        :rtype: :class:`tencentcloud.trdp.v20220726.models.DeviceDetailInfo`
        """
        return self._DeviceDetail

    @DeviceDetail.setter
    def DeviceDetail(self, DeviceDetail):
        self._DeviceDetail = DeviceDetail

    @property
    def Marketing(self):
        """营销信息
        :rtype: :class:`tencentcloud.trdp.v20220726.models.MarketingInfo`
        """
        return self._Marketing

    @Marketing.setter
    def Marketing(self, Marketing):
        self._Marketing = Marketing


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self._Account = AccountInfo()
            self._Account._deserialize(params.get("Account"))
        if params.get("User") is not None:
            self._User = UserInfo()
            self._User._deserialize(params.get("User"))
        self._ModelId = params.get("ModelId")
        if params.get("DeviceFingerprint") is not None:
            self._DeviceFingerprint = DeviceFingerprintInfo()
            self._DeviceFingerprint._deserialize(params.get("DeviceFingerprint"))
        self._SceneCode = params.get("SceneCode")
        if params.get("DeviceDetail") is not None:
            self._DeviceDetail = DeviceDetailInfo()
            self._DeviceDetail._deserialize(params.get("DeviceDetail"))
        if params.get("Marketing") is not None:
            self._Marketing = MarketingInfo()
            self._Marketing._deserialize(params.get("Marketing"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateUserRiskResponse(AbstractModel):
    """EvaluateUserRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EvaluationResult: 评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :type EvaluationResult: :class:`tencentcloud.trdp.v20220726.models.EvaluationResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EvaluationResult = None
        self._RequestId = None

    @property
    def EvaluationResult(self):
        """评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trdp.v20220726.models.EvaluationResult`
        """
        return self._EvaluationResult

    @EvaluationResult.setter
    def EvaluationResult(self, EvaluationResult):
        self._EvaluationResult = EvaluationResult

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EvaluationResult") is not None:
            self._EvaluationResult = EvaluationResult()
            self._EvaluationResult._deserialize(params.get("EvaluationResult"))
        self._RequestId = params.get("RequestId")


class EvaluationResult(AbstractModel):
    """评估结果

    """

    def __init__(self):
        r"""
        :param _SSID: SSID值
        :type SSID: str
        :param _Score: 风险价值分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        :param _RiskLabels: 风险标签，请参考官网风险类型
账号风险
1 账号信用低 账号近期存在因恶意被处罚历史，网络低活跃，被举报等因素
11 疑似低活跃账号 账号活跃度与正常用户有差异
2 垃圾账号 疑似批量注册小号，近期存在严重违规或大量举报
21 疑似小号 账号有疑似线上养号，小号等行为
22 疑似违规账号 账号曾有违规行为、曾被举报过、曾因违规被处罚过等
3 无效账号 送检账号参数无法成功解析，请检查微信 Openid 是否有误/Appid与QQopenid无法关联/微信Openid权限是否有开通/手机号是否为中国大陆手机号
4 黑名单 该账号在业务侧有过拉黑记录
5 白名单 业务自行有添加过白名单记录
行为风险
101 批量操作存在 IP/设备/环境等因素的聚集性异常
1011 疑似 IP 属性聚集 出现 IP 聚集
1012 疑似设备属性聚集 出现设备聚集
102 自动机 疑似自动机批量请求
103 恶意行为-网赚 疑似网赚
104 微信登录态无效 检查 WeChatAccessToken 参数，是否已经失效
201 环境风险 环境异常 操作 IP/设备/环境存在异常。当前 IP 为非常用 IP 或恶意 IP 段
2011 疑似非常用 IP 请求 当前请求 IP 非该账号常用 IP
2012 疑似 IP 异常 使用 idc 机房 IP 或使用代理 IP 或使用恶意 IP 等
205 非公网有效IP 传进来的 IP 地址为内网 IP 地址或者 IP 保留地址
设备风险
206 设备异常 该设备存在异常的使用行为
2061 疑似非常用设备 当前请求的设备非该账号常用设备
2062 疑似虚拟设备 请求设备为模拟器、脚本、云设备等虚拟设备
2063 疑似群控设备 请求设备为猫池、手机墙等群控设备
10201 设备处于开发者模式 来源于Android
10202 设备疑似 Root 来源于Android
10203 疑似应用被注 来源于Android
10204 疑似应用被重打包 来源于Android
10205 疑似使用 hook 技术 来源于Android
10206 疑似应用被双开 来源于Android
10207 疑似设备存在风险进程 来源于Android
10208 疑似伪造地理位置 来源于Android
10209 疑似使用 VPN 软件 来源于Android
10210 疑似使用代理软件 来源于Android
10211 疑似设备处于调试模式 来源于Android
10212 疑似高危 ROM 来源于Android
10213 疑似检测到系统劫持 来源于Android
10003 疑似模拟器 来源于Android
10301 疑似主流模拟器 来源于Android
10302 疑似云模拟器 来源于Android
10303 疑似开发板设备 来源于Android
10004 疑似群控设备风险 来源于Android
10401 疑似使用自动化软件 来源于Android
10402 疑似群控自动化操作 来源于Android
10501 疑似参数异常-IMEI 来源于Android
10502 疑似参数异常-FP 来源于Android
10504 疑似参数异常-IMSI 来源于Android
10801 疑似存在刷量安装应用的行为 来源于Android
10901 疑似多账号异常 来源于Android
11001 疑似设备参数篡改 来源于Android
11002 疑似存在风险软件 来源于Android
11003 疑似应用被调试 来源于Android
11100 疑似云真机 来源于Android
25001 设备疑似越狱 来源于IOS
25004 进程疑似有注入文件 来源于IOS
25005 疑似使用代理软件 来源于IOS
25006 疑似使用 VPN 软件 来源于IOS
25007 疑似被 Hook 来源于IOS
25008 疑似进程被调试 来源于IOS
25009 疑似多开 来源于IOS
25010 疑似改机 来源于IOS
25011 疑似应用二次打包 来源于IOS
25012 疑似模拟器 来源于IOS
25013 疑似云真机 来源于IOS
25014 疑似云模拟器 来源于IOS
25015 疑似伪造地理位置 来源于IOS
25016 疑似使用自动化脚本 来源于IOS
25017 疑似群控自动化操作 来源于IOS
30001 疑似虚拟浏览器 来源于H5
30002 疑似安装作弊插件 来源于H5
30003 疑似浏览器参数遭篡改 来源于H5
30004 疑似 JS 代码被篡改 来源于H5
30005 疑似 JS 被调试 来源于H5
30006 Cookies 被禁用 来源于H5
40001 疑似伪造地理位置 来源于小程序
40002 疑似被调试 来源于小程序
40003 疑似模拟器 来源于小程序
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLabels: list of int
        """
        self._SSID = None
        self._Score = None
        self._RiskLabels = None

    @property
    def SSID(self):
        """SSID值
        :rtype: str
        """
        return self._SSID

    @SSID.setter
    def SSID(self, SSID):
        self._SSID = SSID

    @property
    def Score(self):
        """风险价值分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def RiskLabels(self):
        """风险标签，请参考官网风险类型
账号风险
1 账号信用低 账号近期存在因恶意被处罚历史，网络低活跃，被举报等因素
11 疑似低活跃账号 账号活跃度与正常用户有差异
2 垃圾账号 疑似批量注册小号，近期存在严重违规或大量举报
21 疑似小号 账号有疑似线上养号，小号等行为
22 疑似违规账号 账号曾有违规行为、曾被举报过、曾因违规被处罚过等
3 无效账号 送检账号参数无法成功解析，请检查微信 Openid 是否有误/Appid与QQopenid无法关联/微信Openid权限是否有开通/手机号是否为中国大陆手机号
4 黑名单 该账号在业务侧有过拉黑记录
5 白名单 业务自行有添加过白名单记录
行为风险
101 批量操作存在 IP/设备/环境等因素的聚集性异常
1011 疑似 IP 属性聚集 出现 IP 聚集
1012 疑似设备属性聚集 出现设备聚集
102 自动机 疑似自动机批量请求
103 恶意行为-网赚 疑似网赚
104 微信登录态无效 检查 WeChatAccessToken 参数，是否已经失效
201 环境风险 环境异常 操作 IP/设备/环境存在异常。当前 IP 为非常用 IP 或恶意 IP 段
2011 疑似非常用 IP 请求 当前请求 IP 非该账号常用 IP
2012 疑似 IP 异常 使用 idc 机房 IP 或使用代理 IP 或使用恶意 IP 等
205 非公网有效IP 传进来的 IP 地址为内网 IP 地址或者 IP 保留地址
设备风险
206 设备异常 该设备存在异常的使用行为
2061 疑似非常用设备 当前请求的设备非该账号常用设备
2062 疑似虚拟设备 请求设备为模拟器、脚本、云设备等虚拟设备
2063 疑似群控设备 请求设备为猫池、手机墙等群控设备
10201 设备处于开发者模式 来源于Android
10202 设备疑似 Root 来源于Android
10203 疑似应用被注 来源于Android
10204 疑似应用被重打包 来源于Android
10205 疑似使用 hook 技术 来源于Android
10206 疑似应用被双开 来源于Android
10207 疑似设备存在风险进程 来源于Android
10208 疑似伪造地理位置 来源于Android
10209 疑似使用 VPN 软件 来源于Android
10210 疑似使用代理软件 来源于Android
10211 疑似设备处于调试模式 来源于Android
10212 疑似高危 ROM 来源于Android
10213 疑似检测到系统劫持 来源于Android
10003 疑似模拟器 来源于Android
10301 疑似主流模拟器 来源于Android
10302 疑似云模拟器 来源于Android
10303 疑似开发板设备 来源于Android
10004 疑似群控设备风险 来源于Android
10401 疑似使用自动化软件 来源于Android
10402 疑似群控自动化操作 来源于Android
10501 疑似参数异常-IMEI 来源于Android
10502 疑似参数异常-FP 来源于Android
10504 疑似参数异常-IMSI 来源于Android
10801 疑似存在刷量安装应用的行为 来源于Android
10901 疑似多账号异常 来源于Android
11001 疑似设备参数篡改 来源于Android
11002 疑似存在风险软件 来源于Android
11003 疑似应用被调试 来源于Android
11100 疑似云真机 来源于Android
25001 设备疑似越狱 来源于IOS
25004 进程疑似有注入文件 来源于IOS
25005 疑似使用代理软件 来源于IOS
25006 疑似使用 VPN 软件 来源于IOS
25007 疑似被 Hook 来源于IOS
25008 疑似进程被调试 来源于IOS
25009 疑似多开 来源于IOS
25010 疑似改机 来源于IOS
25011 疑似应用二次打包 来源于IOS
25012 疑似模拟器 来源于IOS
25013 疑似云真机 来源于IOS
25014 疑似云模拟器 来源于IOS
25015 疑似伪造地理位置 来源于IOS
25016 疑似使用自动化脚本 来源于IOS
25017 疑似群控自动化操作 来源于IOS
30001 疑似虚拟浏览器 来源于H5
30002 疑似安装作弊插件 来源于H5
30003 疑似浏览器参数遭篡改 来源于H5
30004 疑似 JS 代码被篡改 来源于H5
30005 疑似 JS 被调试 来源于H5
30006 Cookies 被禁用 来源于H5
40001 疑似伪造地理位置 来源于小程序
40002 疑似被调试 来源于小程序
40003 疑似模拟器 来源于小程序
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._RiskLabels

    @RiskLabels.setter
    def RiskLabels(self, RiskLabels):
        self._RiskLabels = RiskLabels


    def _deserialize(self, params):
        self._SSID = params.get("SSID")
        self._Score = params.get("Score")
        self._RiskLabels = params.get("RiskLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MarketingInfo(AbstractModel):
    """营销信息

    """

    def __init__(self):
        r"""
        :param _DeliveryMode: 投放模式（0=PDB，1=PD，2=RTB，10=其他）
        :type DeliveryMode: int
        :param _AdvertisingType: 广告位类型 （0=前贴片，1=开屏广告，2=网页头部广告、3=网页中部广告、4=网页底部广告、5=悬浮广告、10=其它）
        :type AdvertisingType: int
        :param _FullScreen: 是否全屏插广告（0-否，1-是）
        :type FullScreen: int
        :param _AdvertisingSpaceWidth: 广告位宽度
        :type AdvertisingSpaceWidth: int
        :param _AdvertisingSpaceHeight: 广告位高度
        :type AdvertisingSpaceHeight: int
        :param _Url: 网址
        :type Url: str
        """
        self._DeliveryMode = None
        self._AdvertisingType = None
        self._FullScreen = None
        self._AdvertisingSpaceWidth = None
        self._AdvertisingSpaceHeight = None
        self._Url = None

    @property
    def DeliveryMode(self):
        """投放模式（0=PDB，1=PD，2=RTB，10=其他）
        :rtype: int
        """
        return self._DeliveryMode

    @DeliveryMode.setter
    def DeliveryMode(self, DeliveryMode):
        self._DeliveryMode = DeliveryMode

    @property
    def AdvertisingType(self):
        """广告位类型 （0=前贴片，1=开屏广告，2=网页头部广告、3=网页中部广告、4=网页底部广告、5=悬浮广告、10=其它）
        :rtype: int
        """
        return self._AdvertisingType

    @AdvertisingType.setter
    def AdvertisingType(self, AdvertisingType):
        self._AdvertisingType = AdvertisingType

    @property
    def FullScreen(self):
        """是否全屏插广告（0-否，1-是）
        :rtype: int
        """
        return self._FullScreen

    @FullScreen.setter
    def FullScreen(self, FullScreen):
        self._FullScreen = FullScreen

    @property
    def AdvertisingSpaceWidth(self):
        """广告位宽度
        :rtype: int
        """
        return self._AdvertisingSpaceWidth

    @AdvertisingSpaceWidth.setter
    def AdvertisingSpaceWidth(self, AdvertisingSpaceWidth):
        self._AdvertisingSpaceWidth = AdvertisingSpaceWidth

    @property
    def AdvertisingSpaceHeight(self):
        """广告位高度
        :rtype: int
        """
        return self._AdvertisingSpaceHeight

    @AdvertisingSpaceHeight.setter
    def AdvertisingSpaceHeight(self, AdvertisingSpaceHeight):
        self._AdvertisingSpaceHeight = AdvertisingSpaceHeight

    @property
    def Url(self):
        """网址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._DeliveryMode = params.get("DeliveryMode")
        self._AdvertisingType = params.get("AdvertisingType")
        self._FullScreen = params.get("FullScreen")
        self._AdvertisingSpaceWidth = params.get("AdvertisingSpaceWidth")
        self._AdvertisingSpaceHeight = params.get("AdvertisingSpaceHeight")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UniversalAccountInfo(AbstractModel):
    """通用账号信息

    """

    def __init__(self):
        r"""
        :param _AccountId: 账号值：
当账户类型为1时，填入手机号，如135****3695；
当账户类型为2、3或100时，填入对应的值。
        :type AccountId: str
        """
        self._AccountId = None

    @property
    def AccountId(self):
        """账号值：
当账户类型为1时，填入手机号，如135****3695；
当账户类型为2、3或100时，填入对应的值。
        :rtype: str
        """
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _Ip: 用户外网IP地址
        :type Ip: str
        :param _ChannelSource: 来源渠道编码
        :type ChannelSource: str
        :param _Platform: 用户登录平台。1：Android 2：iOS 3：H5 4：小程序
        :type Platform: int
        :param _Name: 姓名
        :type Name: str
        :param _Age: 年龄
        :type Age: int
        :param _Gender: 性别：
male（男）
female（女）
        :type Gender: str
        :param _ResidentIdentityCard: 身份证号
        :type ResidentIdentityCard: str
        :param _Email: 邮箱地址
        :type Email: str
        :param _Address: 用户地址
        :type Address: str
        :param _Nickname: 用户昵称
        :type Nickname: str
        """
        self._Ip = None
        self._ChannelSource = None
        self._Platform = None
        self._Name = None
        self._Age = None
        self._Gender = None
        self._ResidentIdentityCard = None
        self._Email = None
        self._Address = None
        self._Nickname = None

    @property
    def Ip(self):
        """用户外网IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def ChannelSource(self):
        """来源渠道编码
        :rtype: str
        """
        return self._ChannelSource

    @ChannelSource.setter
    def ChannelSource(self, ChannelSource):
        self._ChannelSource = ChannelSource

    @property
    def Platform(self):
        """用户登录平台。1：Android 2：iOS 3：H5 4：小程序
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Age(self):
        """年龄
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Gender(self):
        """性别：
male（男）
female（女）
        :rtype: str
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def ResidentIdentityCard(self):
        """身份证号
        :rtype: str
        """
        return self._ResidentIdentityCard

    @ResidentIdentityCard.setter
    def ResidentIdentityCard(self, ResidentIdentityCard):
        self._ResidentIdentityCard = ResidentIdentityCard

    @property
    def Email(self):
        """邮箱地址
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Address(self):
        """用户地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Nickname(self):
        """用户昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._ChannelSource = params.get("ChannelSource")
        self._Platform = params.get("Platform")
        self._Name = params.get("Name")
        self._Age = params.get("Age")
        self._Gender = params.get("Gender")
        self._ResidentIdentityCard = params.get("ResidentIdentityCard")
        self._Email = params.get("Email")
        self._Address = params.get("Address")
        self._Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        