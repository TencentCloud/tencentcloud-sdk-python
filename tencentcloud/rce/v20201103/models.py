# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AccountInfo(AbstractModel):
    """账号信息。

    """

    def __init__(self):
        """
        :param AccountType: 用户账号类型（默认开通 QQ 开放账号、手机号，手机 MD5 账号类型查询。如需使用微信开放账号，则需要 提交工单 由腾讯云进行资格审核，审核通过后方可正常使用微信开放账号）：
1：QQ开放账号。
2：微信开放账号。
4：手机号（暂仅支持国内手机号）。
8：设备号（imei/imeiMD5/idfa/idfaMD5）。
0：其他。
10004：支持手机号MD5加密和sha256加密；
标准中国大陆手机号11位，MD5加密后取长度32位小写字符串；例如：手机号13112345678的Md5加密结果为手"dafc728802534d51fbf85c70313a2bd2"
标准中国大陆手机号11位，sha256加密后取长度为64位的小写字符串；例如：手机号13112345678的sha256加密的结果为“9f46715cff1a9ac969ec01924111f7f3697a97ad98a4fd53e15a78d79d1f3551”
        :type AccountType: int
        :param QQAccount: QQ账号信息，AccountType是1时，该字段必填。
        :type QQAccount: :class:`tencentcloud.rce.v20201103.models.QQAccountInfo`
        :param WeChatAccount: 微信账号信息，AccountType是2时，该字段必填。
        :type WeChatAccount: :class:`tencentcloud.rce.v20201103.models.WeChatAccountInfo`
        :param OtherAccount: 其它账号信息，AccountType是0、4、8或10004时，该字段必填。
        :type OtherAccount: :class:`tencentcloud.rce.v20201103.models.OtherAccountInfo`
        """
        self.AccountType = None
        self.QQAccount = None
        self.WeChatAccount = None
        self.OtherAccount = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        if params.get("QQAccount") is not None:
            self.QQAccount = QQAccountInfo()
            self.QQAccount._deserialize(params.get("QQAccount"))
        if params.get("WeChatAccount") is not None:
            self.WeChatAccount = WeChatAccountInfo()
            self.WeChatAccount._deserialize(params.get("WeChatAccount"))
        if params.get("OtherAccount") is not None:
            self.OtherAccount = OtherAccountInfo()
            self.OtherAccount._deserialize(params.get("OtherAccount"))


class InputDetails(AbstractModel):
    """入参的详细参数信息

    """

    def __init__(self):
        """
        :param FieldName: 字段名称
        :type FieldName: str
        :param FieldValue: 字段值
        :type FieldValue: str
        """
        self.FieldName = None
        self.FieldValue = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.FieldValue = params.get("FieldValue")


class InputManageMarketingRisk(AbstractModel):
    """全栈式风控引擎入参

    """

    def __init__(self):
        """
        :param Account: 账号信息。
        :type Account: :class:`tencentcloud.rce.v20201103.models.AccountInfo`
        :param SceneCode: 场景code;
e_activity_antirush；活动防刷场景e_login_protection；登陆保护场景e_register_protection：注册保护场景
        :type SceneCode: str
        :param UserIp: 登录来源的外网IP
        :type UserIp: str
        :param PostTime: 用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）。
        :type PostTime: int
        :param UserId: 用户唯一标识。
        :type UserId: str
        :param DeviceToken: 设备指纹token。
        :type DeviceToken: str
        :param DeviceBusinessId: 设备指纹BusinessId
        :type DeviceBusinessId: int
        :param BusinessId: 业务ID。网站或应用在多个业务中使用此服务，通过此ID区分统计数据。
        :type BusinessId: int
        :param Nickname: 昵称，UTF-8 编码。
        :type Nickname: str
        :param EmailAddress: 用户邮箱地址（非系统自动生成）。
        :type EmailAddress: str
        :param CheckDevice: 是否识别设备异常：
0：不识别。
1：识别。
        :type CheckDevice: int
        :param CookieHash: 用户HTTP请求中的Cookie进行2次hash的值，只要保证相同Cookie的hash值一致即可。
        :type CookieHash: str
        :param Referer: 用户HTTP请求的Referer值。
        :type Referer: str
        :param UserAgent: 用户HTTP请求的User-Agent值。
        :type UserAgent: str
        :param XForwardedFor: 用户HTTP请求的X-Forwarded-For值。
        :type XForwardedFor: str
        :param MacAddress: MAC地址或设备唯一标识。
        :type MacAddress: str
        :param VendorId: 手机制造商ID，如果手机注册，请带上此信息。
        :type VendorId: str
        :param DeviceType: 设备类型：
1：Android
2：IOS
        :type DeviceType: int
        :param Details: 详细信息
FieldName 清单
Android serial_number String 否 设备序列号
Android carrier String 否 运营商；-1: 获取失败，0: 其他，1: 移动，2: 联通，3: 电信，4: 铁通
Android mcc_mnc String 否 netOperator MCC+MNC
Android model String 否 手机型号
Android os_system String 否 操作系统
Android vendor_id String 否 设备品牌 “华为”“oppo”“小米”
Android device_version String 否 设备版本
Android android_api_level String 否 安卓API等级
Android phone_chip_info String 否 手机芯片信息
Android resolution_w String 否 屏幕分辨率宽，保留整数
Android resolution_h String 否 屏幕分辨率高，保留整数
Android brightness String 否 屏幕亮度
Android bluetooth_address String 否 蓝牙地址
Android baseband_version String 否 基带版本
Android kernel_version String 否 kernel 版本
Android cpu_core String 否 CPU 核数
Android cpu_model String 否 CPU 型号
Android memory String 否 内存容量，单位转换为 GB
Android storage String 否 存储容量，单位转换为 GB
Android volume String 否 手机音量
Android battery_power String 否 电池电量
Android language String 否 语言
Android package_name String 否 软件包名
Android App_version String 否 App 版本号
Android App_name String 否 App 显示名称
Android is_debug String 否 是否 debug；0 为正常模式，1 为 debug 模式；其他值无效
Android is_root String 否 是否越狱；0 为正常，1 为越狱；其他值无效
Android is_proxy String 否 是否启动代理；0 为未开启，1 为开启；其他值无效
Android is_emulator String 否 是否模拟器；0 为未开启，1 为开启；其他值无效
Android charge_status String 否 充电状态；1-不在充电，2-USB充电，3-电源充电
Android network_type String 否 网络类型：2G/3G/4G/5G/WiFi/WWAN/other
Android wifi_mac String 否 WiFi MAC地址
IOS model String 否 机器型号 iPhone11
IOS memory String 否 内存容量，单位转换为 GB
IOS os_system String 否 操作系统
IOS device_version String 否 设备版本
IOS phone_chip_info String 否 手机芯片信息
IOS device_name String 否 设备名称 "xxx 的 iPhone"，"xxx's IPhone" 等等
IOS uptime String 否 开机时间
IOS language String 否 系统语言
IOS carrier String 否 运营商
IOS cpu_model String 否 CPU 型号
IOS cpu_core String 否 CPU 个数
IOS volume String 否 手机音量
IOS battery_power String 否 电池电量
IOS resolution_w String 否 屏幕分辨率宽，保留整数
IOS resolution_h String 否 屏幕分辨率高，保留整数
IOS package_name String 否 App 包名
IOS App_version String 否 App 版本号
IOS App_name String 否 App 显示名称
IOS is_debug String 否 是否 debug；0 为正常模式，1 为 debug 模式；其他值无效
IOS is_root String 否 是否越狱；0 为正常，1 为越狱；其他值无效
IOS is_proxy String 否 是否启动代理；0 为未开启，1 为开启；其他值无效
IOS is_emulator String 否 是否模拟器；0 为未开启，1 为开启；其他值无效
IOS charge_status String 否 充电状态；1-不在充电，2-USB充电，3-电源充电
IOS network_type String 否 网络类型：2G/3G/4G/5G/WiFi/WWAN/other
IOS wifi_mac String 否 WiFi MAC地址
其他 os_system String 否 操作系统
其他 browser String 否 浏览器信息
其他 from_url String 否 来源链接
        :type Details: list of InputDetails
        :param Sponsor: 可选填写。详情请跳转至SponsorInfo查看。
        :type Sponsor: :class:`tencentcloud.rce.v20201103.models.SponsorInfo`
        :param OnlineScam: 可选填写。详情请跳转至OnlineScamInfo查看。
        :type OnlineScam: :class:`tencentcloud.rce.v20201103.models.OnlineScamInfo`
        """
        self.Account = None
        self.SceneCode = None
        self.UserIp = None
        self.PostTime = None
        self.UserId = None
        self.DeviceToken = None
        self.DeviceBusinessId = None
        self.BusinessId = None
        self.Nickname = None
        self.EmailAddress = None
        self.CheckDevice = None
        self.CookieHash = None
        self.Referer = None
        self.UserAgent = None
        self.XForwardedFor = None
        self.MacAddress = None
        self.VendorId = None
        self.DeviceType = None
        self.Details = None
        self.Sponsor = None
        self.OnlineScam = None


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self.Account = AccountInfo()
            self.Account._deserialize(params.get("Account"))
        self.SceneCode = params.get("SceneCode")
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        self.UserId = params.get("UserId")
        self.DeviceToken = params.get("DeviceToken")
        self.DeviceBusinessId = params.get("DeviceBusinessId")
        self.BusinessId = params.get("BusinessId")
        self.Nickname = params.get("Nickname")
        self.EmailAddress = params.get("EmailAddress")
        self.CheckDevice = params.get("CheckDevice")
        self.CookieHash = params.get("CookieHash")
        self.Referer = params.get("Referer")
        self.UserAgent = params.get("UserAgent")
        self.XForwardedFor = params.get("XForwardedFor")
        self.MacAddress = params.get("MacAddress")
        self.VendorId = params.get("VendorId")
        self.DeviceType = params.get("DeviceType")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = InputDetails()
                obj._deserialize(item)
                self.Details.append(obj)
        if params.get("Sponsor") is not None:
            self.Sponsor = SponsorInfo()
            self.Sponsor._deserialize(params.get("Sponsor"))
        if params.get("OnlineScam") is not None:
            self.OnlineScam = OnlineScamInfo()
            self.OnlineScam._deserialize(params.get("OnlineScam"))


class ManageMarketingRiskRequest(AbstractModel):
    """ManageMarketingRisk请求参数结构体

    """

    def __init__(self):
        """
        :param BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.rce.v20201103.models.InputManageMarketingRisk`
        """
        self.BusinessSecurityData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = InputManageMarketingRisk()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))


class ManageMarketingRiskResponse(AbstractModel):
    """ManageMarketingRisk返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 业务出参
        :type Data: :class:`tencentcloud.rce.v20201103.models.OutputManageMarketingRisk`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputManageMarketingRisk()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class OnlineScamInfo(AbstractModel):
    """诈骗信息。

    """

    def __init__(self):
        """
        :param ContentLabel: 内容标签。
        :type ContentLabel: str
        :param ContentRiskLevel: 内容风险等级：
0：正常。
1：可疑。
        :type ContentRiskLevel: int
        :param ContentType: 内容产生形式：
0：对话。
1：广播。
        :type ContentType: int
        :param FraudType: 诈骗账号类型：
1：11位手机号。
2：QQ账号。
        :type FraudType: int
        :param FraudAccount: 诈骗账号，手机号或QQ账号。
        :type FraudAccount: str
        """
        self.ContentLabel = None
        self.ContentRiskLevel = None
        self.ContentType = None
        self.FraudType = None
        self.FraudAccount = None


    def _deserialize(self, params):
        self.ContentLabel = params.get("ContentLabel")
        self.ContentRiskLevel = params.get("ContentRiskLevel")
        self.ContentType = params.get("ContentType")
        self.FraudType = params.get("FraudType")
        self.FraudAccount = params.get("FraudAccount")


class OtherAccountInfo(AbstractModel):
    """其它账号信息。

    """

    def __init__(self):
        """
        :param AccountId: 其它账号信息：
AccountType是4时，填入真实的手机号（如13123456789）。
AccountType是8时，支持 imei、idfa、imeiMD5、idfaMD5 入参。
AccountType是0时，填入账号信息。
AccountType是10004时，填入手机号的MD5值。
注：imeiMd5 加密方式为：imei 明文小写后，进行 MD5 加密，加密后取小写值。IdfaMd5 加密方式为：idfa 明文大写后，进行 MD5 加密，加密后取小写值。
        :type AccountId: str
        :param MobilePhone: 手机号，若 AccountType 是4（手机号）、或10004（手机号 MD5），则无需重复填写，否则填入对应的手机号（如13123456789）。
        :type MobilePhone: str
        :param DeviceId: 用户设备号。若 AccountType 是8（设备号），则无需重复填写，否则填入对应的设备号。
        :type DeviceId: str
        """
        self.AccountId = None
        self.MobilePhone = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.MobilePhone = params.get("MobilePhone")
        self.DeviceId = params.get("DeviceId")


class OutputManageMarketingRisk(AbstractModel):
    """全栈式风控引擎出参

    """

    def __init__(self):
        """
        :param Code: 返回码。0表示成功，非0标识失败错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: UTF-8编码，出错消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 业务详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.rce.v20201103.models.OutputManageMarketingRiskValue`
        :param UUid: 控制台显示的req_id。
注意：此字段可能返回 null，表示取不到有效值。
        :type UUid: str
        """
        self.Code = None
        self.Message = None
        self.Value = None
        self.UUid = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = OutputManageMarketingRiskValue()
            self.Value._deserialize(params.get("Value"))
        self.UUid = params.get("UUid")


class OutputManageMarketingRiskValue(AbstractModel):
    """全栈式风控引擎出参值

    """

    def __init__(self):
        """
        :param UserId: 账号ID。对应输入参数：
AccountType是1时，对应QQ的OpenID。
AccountType是2时，对应微信的OpenID/UnionID。
AccountType是4时，对应手机号。
AccountType是8时，对应imei、idfa、imeiMD5或者idfaMD5。
AccountType是0时，对应账号信息。
AccountType是10004时，对应手机号的MD5。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param PostTime: 操作时间戳，单位秒（对应输入参数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: int
        :param AssociateAccount: 对应输入参数，AccountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param UserIp: 操作来源的外网IP（对应输入参数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param RiskLevel: 风险值
pass : 无恶意
review：需要人工审核
reject：拒绝，高风险恶意
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param RiskType: 风险类型，请参考官网风险类型
账号风险 
1 账号信用低,账号近期存在因恶意被处罚历史，网络低活跃，被举报等因素
11 疑似 低活跃账号,账号活跃度与正常用户有差异
2 垃圾账号 疑似批量注册小号，近期存在严重违规或大量举报
21 疑似小号 账号有疑似线上养号，小号等行为
22 疑似违规账号 账号曾有违规行为、曾被举报过、曾因违规被处罚过等
3 无效账号 送检账号参数无法成功解析，请检查微信 openid 是否有误/appid与QQopenid无法关联/微信openid权限是否有开通/手机号是否为中国大陆手机号；
4 黑名单 该账号在业务侧有过拉黑记录
5 白名单 业务自行有添加过白名单记录
行为风险 
101 批量操作 存在 ip/设备/环境等因素的聚集性异常
1011 疑似 IP 属性聚集，出现 IP 聚集
1012 疑似 设备属性聚集 出现设备聚集
102 自动机 疑似自动机批量请求
103 恶意行为-网赚 疑似网赚
104 微信登录态无效 检查 WeChatAccessToken 参数，是否已经失效；
201 环境风险 环境异常 操作 ip/设备/环境存在异常。当前 ip 为非常用 ip 或恶意 ip 段
2011 疑似 非常用IP 请求 当前请求 IP 非该账号常用 IP
2012 疑似 IP 异常 使用 idc 机房 ip 或 使用代理 ip 或 使用恶意 ip 等
205 非公网有效ip 传进来的 IP 地址为内网 ip 地址或者 ip 保留地址；
设备风险
206  设备异常 该设备存在异常的使用行为
2061 疑似 非常用设备 当前请求的设备非该账号常用设备
2062 疑似 虚拟设备 请求设备为模拟器、脚本、云设备等虚拟设备
2063 疑似 群控设备 请求设备为猫池、手机墙等群控设备
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskType: list of int
        """
        self.UserId = None
        self.PostTime = None
        self.AssociateAccount = None
        self.UserIp = None
        self.RiskLevel = None
        self.RiskType = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.PostTime = params.get("PostTime")
        self.AssociateAccount = params.get("AssociateAccount")
        self.UserIp = params.get("UserIp")
        self.RiskLevel = params.get("RiskLevel")
        self.RiskType = params.get("RiskType")


class QQAccountInfo(AbstractModel):
    """QQ账号信息。

    """

    def __init__(self):
        """
        :param QQOpenId: QQ的OpenID。
        :type QQOpenId: str
        :param AppIdUser: QQ分配给网站或应用的AppId，用来唯一标识网站或应用。
        :type AppIdUser: str
        :param AssociateAccount: 用于标识QQ用户登录后所关联业务自身的账号ID。
        :type AssociateAccount: str
        :param MobilePhone: 账号绑定的手机号。
        :type MobilePhone: str
        :param DeviceId: 用户设备号。
        :type DeviceId: str
        """
        self.QQOpenId = None
        self.AppIdUser = None
        self.AssociateAccount = None
        self.MobilePhone = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.QQOpenId = params.get("QQOpenId")
        self.AppIdUser = params.get("AppIdUser")
        self.AssociateAccount = params.get("AssociateAccount")
        self.MobilePhone = params.get("MobilePhone")
        self.DeviceId = params.get("DeviceId")


class SponsorInfo(AbstractModel):
    """网赚防刷相关参数

    """

    def __init__(self):
        """
        :param SponsorOpenId: 助力场景建议填写：活动发起人微信OpenID。
        :type SponsorOpenId: str
        :param SponsorDeviceNumber: 助力场景建议填写：发起人设备号。
        :type SponsorDeviceNumber: str
        :param SponsorPhone: 助力场景建议填写：发起人手机号。
        :type SponsorPhone: str
        :param SponsorIp: 助力场景建议填写：发起人IP。
        :type SponsorIp: str
        :param CampaignUrl: 助力场景建议填写：活动链接。
        :type CampaignUrl: str
        """
        self.SponsorOpenId = None
        self.SponsorDeviceNumber = None
        self.SponsorPhone = None
        self.SponsorIp = None
        self.CampaignUrl = None


    def _deserialize(self, params):
        self.SponsorOpenId = params.get("SponsorOpenId")
        self.SponsorDeviceNumber = params.get("SponsorDeviceNumber")
        self.SponsorPhone = params.get("SponsorPhone")
        self.SponsorIp = params.get("SponsorIp")
        self.CampaignUrl = params.get("CampaignUrl")


class WeChatAccountInfo(AbstractModel):
    """微信账号信息。

    """

    def __init__(self):
        """
        :param WeChatOpenId: 微信的OpenID/UnionID 。
        :type WeChatOpenId: str
        :param WeChatSubType: 微信开放账号类型：
1：微信公众号/微信第三方登录。
2：微信小程序。
        :type WeChatSubType: int
        :param RandStr: 随机串。如果WeChatSubType是2，该字段必填。Token签名随机数，建议16个字符。
        :type RandStr: str
        :param WeChatAccessToken: 如果WeChatSubType是1，填入授权的access_token（注意：不是普通access_token，详情请参阅官方说明文档。获取网页版本的access_token时，scope字段必需填写snsapi_userinfo。
如果WeChatSubType是2，填入以session_key为密钥签名随机数RandStr（hmac_sha256签名算法）得到的字符串。
        :type WeChatAccessToken: str
        :param AssociateAccount: 用于标识微信用户登录后所关联业务自身的账号ID。
        :type AssociateAccount: str
        :param MobilePhone: 账号绑定的手机号。
        :type MobilePhone: str
        :param DeviceId: 用户设备号。
        :type DeviceId: str
        """
        self.WeChatOpenId = None
        self.WeChatSubType = None
        self.RandStr = None
        self.WeChatAccessToken = None
        self.AssociateAccount = None
        self.MobilePhone = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.WeChatOpenId = params.get("WeChatOpenId")
        self.WeChatSubType = params.get("WeChatSubType")
        self.RandStr = params.get("RandStr")
        self.WeChatAccessToken = params.get("WeChatAccessToken")
        self.AssociateAccount = params.get("AssociateAccount")
        self.MobilePhone = params.get("MobilePhone")
        self.DeviceId = params.get("DeviceId")