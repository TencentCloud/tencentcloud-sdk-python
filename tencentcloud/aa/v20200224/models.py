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


class QueryActivityAntiRushRequest(AbstractModel):
    """QueryActivityAntiRush请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 账号类型
        :type AccountType: str
        :param _Uid: uid值
        :type Uid: str
        :param _UserIp: 用户的真实外网 IP。若填入非外网有效ip，会返回level=0的风控结果，risktype中会有205的风险码返回作为标识
        :type UserIp: str
        :param _PostTime: 用户操作时间戳。
        :type PostTime: str
        :param _AppIdU: accountType 是QQ开放账号时，该参数必填，表示 QQ 开放平台分配给网站或应用的 AppID，用来唯一标识网站或应用。
        :type AppIdU: str
        :param _NickName: 昵称，UTF-8 编码。
        :type NickName: str
        :param _PhoneNumber: 手机号
        :type PhoneNumber: str
        :param _EmailAddress: 用户邮箱地址。
        :type EmailAddress: str
        :param _RegisterTime: 注册时间戳。
        :type RegisterTime: str
        :param _RegisterIp: 注册来源的外网 IP。
        :type RegisterIp: str
        :param _CookieHash: 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。
        :type CookieHash: str
        :param _Address: 地址。
        :type Address: str
        :param _LoginSource: 登录来源：
0：其他。
1：PC 网页。
2：移动页面。
3：App。
4：微信公众号。
        :type LoginSource: str
        :param _LoginType: 登录方式：
0：其他。
1：手动账号密码输入。
2：动态短信密码登录。
3：二维码扫描登录。
        :type LoginType: str
        :param _LoginSpend: 登录耗时，单位：秒。
        :type LoginSpend: str
        :param _RootId: 用户操作的目的 ID，如点赞等，该字段就是被点赞的消息 ID，如果是投票，则为被投号码的 ID。
        :type RootId: str
        :param _Referer: 用户 HTTP 请求的 referer 值。
        :type Referer: str
        :param _JumpUrl: 登录成功后跳转页面。
        :type JumpUrl: str
        :param _UserAgent: 用户 HTTP 请求的 userAgent。
        :type UserAgent: str
        :param _XForwardedFor: 用户 HTTP 请求中的 x_forward_for。
        :type XForwardedFor: str
        :param _MouseClickCount: 用户操作过程中鼠标单击次数。
        :type MouseClickCount: str
        :param _KeyboardClickCount: 用户操作过程中键盘单击次数。
        :type KeyboardClickCount: str
        :param _MacAddress: MAC 地址或设备唯一标识。
        :type MacAddress: str
        :param _VendorId: 手机制造商 ID，如果手机注册，请带上此信息。
        :type VendorId: str
        :param _Imei: 手机设备号。支持以下格式：
1.imei明文
2.idfa明文,
3.imei小写后MD5值小写
4.idfa大写后MD5值小写
        :type Imei: str
        :param _AppVersion: App 客户端版本。
        :type AppVersion: str
        :param _BusinessId: 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。
        :type BusinessId: str
        :param _WxSubType: 1：微信公众号。
2：微信小程序。
        :type WxSubType: str
        :param _RandNum: Token 签名随机数，WxSubType为微信小程序时必填，建议16个字符。
        :type RandNum: str
        :param _WxToken: token
        :type WxToken: str
        :param _CheckDevice: 是否识别设备异常：
0：不识别。
1：识别。
        :type CheckDevice: str
        """
        self._AccountType = None
        self._Uid = None
        self._UserIp = None
        self._PostTime = None
        self._AppIdU = None
        self._NickName = None
        self._PhoneNumber = None
        self._EmailAddress = None
        self._RegisterTime = None
        self._RegisterIp = None
        self._CookieHash = None
        self._Address = None
        self._LoginSource = None
        self._LoginType = None
        self._LoginSpend = None
        self._RootId = None
        self._Referer = None
        self._JumpUrl = None
        self._UserAgent = None
        self._XForwardedFor = None
        self._MouseClickCount = None
        self._KeyboardClickCount = None
        self._MacAddress = None
        self._VendorId = None
        self._Imei = None
        self._AppVersion = None
        self._BusinessId = None
        self._WxSubType = None
        self._RandNum = None
        self._WxToken = None
        self._CheckDevice = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def AppIdU(self):
        return self._AppIdU

    @AppIdU.setter
    def AppIdU(self, AppIdU):
        self._AppIdU = AppIdU

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def EmailAddress(self):
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def RegisterTime(self):
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def RegisterIp(self):
        return self._RegisterIp

    @RegisterIp.setter
    def RegisterIp(self, RegisterIp):
        self._RegisterIp = RegisterIp

    @property
    def CookieHash(self):
        return self._CookieHash

    @CookieHash.setter
    def CookieHash(self, CookieHash):
        self._CookieHash = CookieHash

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def LoginSource(self):
        return self._LoginSource

    @LoginSource.setter
    def LoginSource(self, LoginSource):
        self._LoginSource = LoginSource

    @property
    def LoginType(self):
        return self._LoginType

    @LoginType.setter
    def LoginType(self, LoginType):
        self._LoginType = LoginType

    @property
    def LoginSpend(self):
        return self._LoginSpend

    @LoginSpend.setter
    def LoginSpend(self, LoginSpend):
        self._LoginSpend = LoginSpend

    @property
    def RootId(self):
        return self._RootId

    @RootId.setter
    def RootId(self, RootId):
        self._RootId = RootId

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def JumpUrl(self):
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def XForwardedFor(self):
        return self._XForwardedFor

    @XForwardedFor.setter
    def XForwardedFor(self, XForwardedFor):
        self._XForwardedFor = XForwardedFor

    @property
    def MouseClickCount(self):
        return self._MouseClickCount

    @MouseClickCount.setter
    def MouseClickCount(self, MouseClickCount):
        self._MouseClickCount = MouseClickCount

    @property
    def KeyboardClickCount(self):
        return self._KeyboardClickCount

    @KeyboardClickCount.setter
    def KeyboardClickCount(self, KeyboardClickCount):
        self._KeyboardClickCount = KeyboardClickCount

    @property
    def MacAddress(self):
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def VendorId(self):
        return self._VendorId

    @VendorId.setter
    def VendorId(self, VendorId):
        self._VendorId = VendorId

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def WxSubType(self):
        return self._WxSubType

    @WxSubType.setter
    def WxSubType(self, WxSubType):
        self._WxSubType = WxSubType

    @property
    def RandNum(self):
        return self._RandNum

    @RandNum.setter
    def RandNum(self, RandNum):
        self._RandNum = RandNum

    @property
    def WxToken(self):
        return self._WxToken

    @WxToken.setter
    def WxToken(self, WxToken):
        self._WxToken = WxToken

    @property
    def CheckDevice(self):
        return self._CheckDevice

    @CheckDevice.setter
    def CheckDevice(self, CheckDevice):
        self._CheckDevice = CheckDevice


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Uid = params.get("Uid")
        self._UserIp = params.get("UserIp")
        self._PostTime = params.get("PostTime")
        self._AppIdU = params.get("AppIdU")
        self._NickName = params.get("NickName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._EmailAddress = params.get("EmailAddress")
        self._RegisterTime = params.get("RegisterTime")
        self._RegisterIp = params.get("RegisterIp")
        self._CookieHash = params.get("CookieHash")
        self._Address = params.get("Address")
        self._LoginSource = params.get("LoginSource")
        self._LoginType = params.get("LoginType")
        self._LoginSpend = params.get("LoginSpend")
        self._RootId = params.get("RootId")
        self._Referer = params.get("Referer")
        self._JumpUrl = params.get("JumpUrl")
        self._UserAgent = params.get("UserAgent")
        self._XForwardedFor = params.get("XForwardedFor")
        self._MouseClickCount = params.get("MouseClickCount")
        self._KeyboardClickCount = params.get("KeyboardClickCount")
        self._MacAddress = params.get("MacAddress")
        self._VendorId = params.get("VendorId")
        self._Imei = params.get("Imei")
        self._AppVersion = params.get("AppVersion")
        self._BusinessId = params.get("BusinessId")
        self._WxSubType = params.get("WxSubType")
        self._RandNum = params.get("RandNum")
        self._WxToken = params.get("WxToken")
        self._CheckDevice = params.get("CheckDevice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityAntiRushResponse(AbstractModel):
    """QueryActivityAntiRush返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PostTime: 操作时间戳，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: str
        :param _UserIp: 用户操作的真实外网 IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param _Level: 0：表示无恶意。
1 - 4：恶意等级由低到高。
        :type Level: int
        :param _RiskType: 风险类型。

账号风险：

1，账号信用低，账号近期存在因恶意被处罚历史，网络低活跃，被举报等因素；
2，垃圾账号，疑似批量注册小号，近期存在严重违规或大量举报；
3，无效账号，送检账号参数无法成功解析，请检查微信openid是否有误 ，QQopenid是否与appidU对应，手机号是否有误。
4，黑名单，该账号在业务侧有过拉黑记录
5，白名单，该账号在业务侧有过加白名单记录

行为风险：
101，批量操作，存在ip/设备/环境等因素的聚集性异常；
102，自动机，疑似自动机批量请求；
104，微信登录态无效，检查wxToken参数，是否已经失效；

环境风险：
201，环境异常，操作ip/设备/环境存在异常。当前ip为非常用ip或恶意ip段；
205，非公网有效ip，传进来的IP地址为内网ip地址或者ip保留地址；
206，设备异常，该设备存在异常的使用行为
        :type RiskType: list of int
        :param _AssociateAccount: accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param _Uid: uid值
注意：此字段可能返回 null，表示取不到有效值。
        :type Uid: str
        :param _RootId: 用户操作的目的ID 
比如：点赞，该字段就是被点 赞的消息 id，如果是投票，就是被投号码的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RootId: str
        :param _CodeDesc: 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PostTime = None
        self._UserIp = None
        self._Level = None
        self._RiskType = None
        self._AssociateAccount = None
        self._Uid = None
        self._RootId = None
        self._CodeDesc = None
        self._RequestId = None

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RiskType(self):
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def RootId(self):
        return self._RootId

    @RootId.setter
    def RootId(self, RootId):
        self._RootId = RootId

    @property
    def CodeDesc(self):
        return self._CodeDesc

    @CodeDesc.setter
    def CodeDesc(self, CodeDesc):
        self._CodeDesc = CodeDesc

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PostTime = params.get("PostTime")
        self._UserIp = params.get("UserIp")
        self._Level = params.get("Level")
        self._RiskType = params.get("RiskType")
        self._AssociateAccount = params.get("AssociateAccount")
        self._Uid = params.get("Uid")
        self._RootId = params.get("RootId")
        self._CodeDesc = params.get("CodeDesc")
        self._RequestId = params.get("RequestId")