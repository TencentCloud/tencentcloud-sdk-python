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
        :param AccountType: 用户账号类型：
1-手机号；
2-IMEI；
3-IDFA；
100-SSID类型
        :type AccountType: int
        :param UniversalAccount: 通用账号信息，当AccountType为1、2、3、100时必填
        :type UniversalAccount: :class:`tencentcloud.trdp.v20220726.models.UniversalAccountInfo`
        """
        self.AccountType = None
        self.UniversalAccount = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        if params.get("UniversalAccount") is not None:
            self.UniversalAccount = UniversalAccountInfo()
            self.UniversalAccount._deserialize(params.get("UniversalAccount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDetailInfo(AbstractModel):
    """设备详情

    """

    def __init__(self):
        r"""
        :param MacAddress: mac地址或唯一设备标识
        :type MacAddress: str
        :param Model: 手机型号
        :type Model: str
        :param OsSystem: 操作系统(unknown，android，ios，windows)
        :type OsSystem: str
        :param OsSystemVersion: 操作系统版本
        :type OsSystemVersion: str
        :param BidFloor: 竞价底价
        :type BidFloor: int
        :param DeviceVersion: 设备版本
        :type DeviceVersion: str
        :param Maker: 设备制造商
        :type Maker: str
        :param DeviceType: 设备类型（PHONE,TABLET）
        :type DeviceType: str
        :param Carrier: 运营商；-1: 获取失败，0: 其他，1: 移动，2: 联通，3: 电信，4: 铁通
        :type Carrier: str
        :param AccessMode: 入网方式(wifi,5g,4g,3g,2g)
        :type AccessMode: str
        :param PhoneChipInfo: 手机芯片信息
        :type PhoneChipInfo: str
        :param CpuModel: CPU 型号
        :type CpuModel: str
        :param CpuCore: CPU 核数
        :type CpuCore: str
        :param Memory: 内存容量，单位转换为 GB
        :type Memory: str
        :param Language: 系统语言
        :type Language: str
        :param Volume: 手机音量
        :type Volume: str
        :param BatteryPower: 电池电量
        :type BatteryPower: str
        :param ResolutionWidth: 屏幕分辨率宽，保留整数
        :type ResolutionWidth: int
        :param ResolutionHeight: 屏幕分辨率高，保留整数
        :type ResolutionHeight: int
        :param Ua: 浏览器类型
        :type Ua: str
        :param App: 客户端应用
        :type App: str
        :param AppPackageName: 应用包名
        :type AppPackageName: str
        :param SerialNumber: 设备序列号
Android设备
        :type SerialNumber: str
        :param MobileCountryAndNetworkCode: netOperator MCC+MNC
Android设备
        :type MobileCountryAndNetworkCode: str
        :param VendorId: 设备品牌 “华为”“oppo”“小米”
Android设备
        :type VendorId: str
        :param AndroidApiLevel: Android API等级
Android设备
        :type AndroidApiLevel: str
        :param Brightness: 屏幕亮度
Android设备
        :type Brightness: str
        :param BluetoothAddress: 蓝牙地址
Android设备
        :type BluetoothAddress: str
        :param BaseBandVersion: 基带版本
Android设备
        :type BaseBandVersion: str
        :param KernelVersion: kernel 版本
Android设备
        :type KernelVersion: str
        :param Storage: 存储容量，单位转换为 GB
Android设备
        :type Storage: str
        :param PackageName: 软件包名
Android设备
        :type PackageName: str
        :param AppVersion: app 版本号
Android设备
        :type AppVersion: str
        :param AppName: app 显示名称
Android设备
        :type AppName: str
        :param IsDebug: 是否 debug；0 为正常模式，1 为 debug 模式；其他值无效
Android设备
        :type IsDebug: str
        :param IsRoot: 是否越狱；0 为正常，1 为越狱；其他值无效
Android设备
        :type IsRoot: str
        :param IsProxy: 是否启动代理；0 为未开启，1 为开启；其他值无效
Android设备
        :type IsProxy: str
        :param IsEmulator: 是否模拟器；0 为未开启，1 为开启；其他值无效
Android设备
        :type IsEmulator: str
        :param ChargeStatus: 充电状态；1-不在充电，2-USB充电，3-电源充电
Android设备
        :type ChargeStatus: str
        :param NetworkType: 网络类型：2G/3G/4G/5G/Wi-Fi/WWAN/other
Android设备
        :type NetworkType: str
        :param WifiMac: Wi-Fi MAC地址
Android设备
        :type WifiMac: str
        :param DeviceName: 设备名称 "xxx 的 iPhone"，"xxx's IPhone" 等等
IOS设备
        :type DeviceName: str
        :param StartupTime: 开机时间
IOS设备
        :type StartupTime: str
        :param Lon: 所在经度
        :type Lon: str
        :param Lat: 所在纬度
        :type Lat: str
        """
        self.MacAddress = None
        self.Model = None
        self.OsSystem = None
        self.OsSystemVersion = None
        self.BidFloor = None
        self.DeviceVersion = None
        self.Maker = None
        self.DeviceType = None
        self.Carrier = None
        self.AccessMode = None
        self.PhoneChipInfo = None
        self.CpuModel = None
        self.CpuCore = None
        self.Memory = None
        self.Language = None
        self.Volume = None
        self.BatteryPower = None
        self.ResolutionWidth = None
        self.ResolutionHeight = None
        self.Ua = None
        self.App = None
        self.AppPackageName = None
        self.SerialNumber = None
        self.MobileCountryAndNetworkCode = None
        self.VendorId = None
        self.AndroidApiLevel = None
        self.Brightness = None
        self.BluetoothAddress = None
        self.BaseBandVersion = None
        self.KernelVersion = None
        self.Storage = None
        self.PackageName = None
        self.AppVersion = None
        self.AppName = None
        self.IsDebug = None
        self.IsRoot = None
        self.IsProxy = None
        self.IsEmulator = None
        self.ChargeStatus = None
        self.NetworkType = None
        self.WifiMac = None
        self.DeviceName = None
        self.StartupTime = None
        self.Lon = None
        self.Lat = None


    def _deserialize(self, params):
        self.MacAddress = params.get("MacAddress")
        self.Model = params.get("Model")
        self.OsSystem = params.get("OsSystem")
        self.OsSystemVersion = params.get("OsSystemVersion")
        self.BidFloor = params.get("BidFloor")
        self.DeviceVersion = params.get("DeviceVersion")
        self.Maker = params.get("Maker")
        self.DeviceType = params.get("DeviceType")
        self.Carrier = params.get("Carrier")
        self.AccessMode = params.get("AccessMode")
        self.PhoneChipInfo = params.get("PhoneChipInfo")
        self.CpuModel = params.get("CpuModel")
        self.CpuCore = params.get("CpuCore")
        self.Memory = params.get("Memory")
        self.Language = params.get("Language")
        self.Volume = params.get("Volume")
        self.BatteryPower = params.get("BatteryPower")
        self.ResolutionWidth = params.get("ResolutionWidth")
        self.ResolutionHeight = params.get("ResolutionHeight")
        self.Ua = params.get("Ua")
        self.App = params.get("App")
        self.AppPackageName = params.get("AppPackageName")
        self.SerialNumber = params.get("SerialNumber")
        self.MobileCountryAndNetworkCode = params.get("MobileCountryAndNetworkCode")
        self.VendorId = params.get("VendorId")
        self.AndroidApiLevel = params.get("AndroidApiLevel")
        self.Brightness = params.get("Brightness")
        self.BluetoothAddress = params.get("BluetoothAddress")
        self.BaseBandVersion = params.get("BaseBandVersion")
        self.KernelVersion = params.get("KernelVersion")
        self.Storage = params.get("Storage")
        self.PackageName = params.get("PackageName")
        self.AppVersion = params.get("AppVersion")
        self.AppName = params.get("AppName")
        self.IsDebug = params.get("IsDebug")
        self.IsRoot = params.get("IsRoot")
        self.IsProxy = params.get("IsProxy")
        self.IsEmulator = params.get("IsEmulator")
        self.ChargeStatus = params.get("ChargeStatus")
        self.NetworkType = params.get("NetworkType")
        self.WifiMac = params.get("WifiMac")
        self.DeviceName = params.get("DeviceName")
        self.StartupTime = params.get("StartupTime")
        self.Lon = params.get("Lon")
        self.Lat = params.get("Lat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceFingerprintInfo(AbstractModel):
    """设备指纹信息

    """

    def __init__(self):
        r"""
        :param DeviceToken: 设备指纹Token
        :type DeviceToken: str
        :param SdkChannel: 设备指纹的客户端SDK对应渠道
        :type SdkChannel: str
        """
        self.DeviceToken = None
        self.SdkChannel = None


    def _deserialize(self, params):
        self.DeviceToken = params.get("DeviceToken")
        self.SdkChannel = params.get("SdkChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateUserRiskRequest(AbstractModel):
    """EvaluateUserRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param Account: 账号信息
        :type Account: :class:`tencentcloud.trdp.v20220726.models.AccountInfo`
        :param User: 用户信息
        :type User: :class:`tencentcloud.trdp.v20220726.models.UserInfo`
        :param ModelId: 模型ID
        :type ModelId: str
        :param DeviceFingerprint: 设备指纹信息
        :type DeviceFingerprint: :class:`tencentcloud.trdp.v20220726.models.DeviceFingerprintInfo`
        :param SceneCode: 场景Code，不传默认活动防刷；
e_activity_antirush；活动防刷场景
e_login_protection；登录保护场景
e_register_protection：注册保护场景
        :type SceneCode: str
        :param DeviceDetail: 设备详情
        :type DeviceDetail: :class:`tencentcloud.trdp.v20220726.models.DeviceDetailInfo`
        :param Marketing: 营销信息
        :type Marketing: :class:`tencentcloud.trdp.v20220726.models.MarketingInfo`
        """
        self.Account = None
        self.User = None
        self.ModelId = None
        self.DeviceFingerprint = None
        self.SceneCode = None
        self.DeviceDetail = None
        self.Marketing = None


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self.Account = AccountInfo()
            self.Account._deserialize(params.get("Account"))
        if params.get("User") is not None:
            self.User = UserInfo()
            self.User._deserialize(params.get("User"))
        self.ModelId = params.get("ModelId")
        if params.get("DeviceFingerprint") is not None:
            self.DeviceFingerprint = DeviceFingerprintInfo()
            self.DeviceFingerprint._deserialize(params.get("DeviceFingerprint"))
        self.SceneCode = params.get("SceneCode")
        if params.get("DeviceDetail") is not None:
            self.DeviceDetail = DeviceDetailInfo()
            self.DeviceDetail._deserialize(params.get("DeviceDetail"))
        if params.get("Marketing") is not None:
            self.Marketing = MarketingInfo()
            self.Marketing._deserialize(params.get("Marketing"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateUserRiskResponse(AbstractModel):
    """EvaluateUserRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param EvaluationResult: 评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :type EvaluationResult: :class:`tencentcloud.trdp.v20220726.models.EvaluationResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EvaluationResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EvaluationResult") is not None:
            self.EvaluationResult = EvaluationResult()
            self.EvaluationResult._deserialize(params.get("EvaluationResult"))
        self.RequestId = params.get("RequestId")


class EvaluationResult(AbstractModel):
    """评估结果

    """

    def __init__(self):
        r"""
        :param SSID: SSID值
        :type SSID: str
        :param Score: 风险价值分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        :param RiskLabels: 风险标签，请参考官网风险类型
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
        self.SSID = None
        self.Score = None
        self.RiskLabels = None


    def _deserialize(self, params):
        self.SSID = params.get("SSID")
        self.Score = params.get("Score")
        self.RiskLabels = params.get("RiskLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MarketingInfo(AbstractModel):
    """营销信息

    """

    def __init__(self):
        r"""
        :param DeliveryMode: 投放模式（0=PDB，1=PD，2=RTB，10=其他）
        :type DeliveryMode: int
        :param AdvertisingType: 广告位类型 （0=前贴片，1=开屏广告，2=网页头部广告、3=网页中部广告、4=网页底部广告、5=悬浮广告、10=其它）
        :type AdvertisingType: int
        :param FullScreen: 是否全屏插广告（0-否，1-是）
        :type FullScreen: int
        :param AdvertisingSpaceWidth: 广告位宽度
        :type AdvertisingSpaceWidth: int
        :param AdvertisingSpaceHeight: 广告位高度
        :type AdvertisingSpaceHeight: int
        :param Url: 网址
        :type Url: str
        """
        self.DeliveryMode = None
        self.AdvertisingType = None
        self.FullScreen = None
        self.AdvertisingSpaceWidth = None
        self.AdvertisingSpaceHeight = None
        self.Url = None


    def _deserialize(self, params):
        self.DeliveryMode = params.get("DeliveryMode")
        self.AdvertisingType = params.get("AdvertisingType")
        self.FullScreen = params.get("FullScreen")
        self.AdvertisingSpaceWidth = params.get("AdvertisingSpaceWidth")
        self.AdvertisingSpaceHeight = params.get("AdvertisingSpaceHeight")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UniversalAccountInfo(AbstractModel):
    """通用账号信息

    """

    def __init__(self):
        r"""
        :param AccountId: 账号值：
当账户类型为1时，填入手机号，如135****3695；
当账户类型为2、3或100时，填入对应的值。
        :type AccountId: str
        """
        self.AccountId = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param Ip: 用户外网IP地址
        :type Ip: str
        :param ChannelSource: 来源渠道编码
        :type ChannelSource: str
        :param Platform: 用户登录平台。1：Android 2：iOS 3：H5 4：小程序
        :type Platform: int
        :param Name: 姓名
        :type Name: str
        :param Age: 年龄
        :type Age: int
        :param Gender: 性别：
male（男）
female（女）
        :type Gender: str
        :param ResidentIdentityCard: 身份证号
        :type ResidentIdentityCard: str
        :param Email: 邮箱地址
        :type Email: str
        :param Address: 用户地址
        :type Address: str
        :param Nickname: 用户昵称
        :type Nickname: str
        """
        self.Ip = None
        self.ChannelSource = None
        self.Platform = None
        self.Name = None
        self.Age = None
        self.Gender = None
        self.ResidentIdentityCard = None
        self.Email = None
        self.Address = None
        self.Nickname = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ChannelSource = params.get("ChannelSource")
        self.Platform = params.get("Platform")
        self.Name = params.get("Name")
        self.Age = params.get("Age")
        self.Gender = params.get("Gender")
        self.ResidentIdentityCard = params.get("ResidentIdentityCard")
        self.Email = params.get("Email")
        self.Address = params.get("Address")
        self.Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        