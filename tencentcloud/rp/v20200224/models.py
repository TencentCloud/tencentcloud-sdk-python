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


class QueryRegisterProtectionRequest(AbstractModel):
    """QueryRegisterProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterIp: 注册来源的外网 IP。
        :type RegisterIp: str
        :param _Uid: 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。
        :type Uid: str
        :param _RegisterTime: 注册时间戳，单位：秒。
        :type RegisterTime: str
        :param _AccountType: 用户账号类型（QQ 开放帐号、微信开放账号需要 提交工单 由腾讯云进行资格审核）：
1：QQ 开放帐号。
2：微信开放账号。
4：手机号。
0：其他。
10004：手机号 MD5。
        :type AccountType: str
        :param _AppIdU: accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给网站或应用的 AppID，用来唯一标识网站或应用。
        :type AppIdU: str
        :param _AssociateAccount: accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。
        :type AssociateAccount: str
        :param _NickName: 昵称，UTF-8 编码。
        :type NickName: str
        :param _PhoneNumber: 手机号：国家代码-手机号， 如0086-15912345687（0086前不需要+号）。
        :type PhoneNumber: str
        :param _EmailAddress: 用户邮箱地址（非系统自动生成）。
        :type EmailAddress: str
        :param _Address: 地址。
        :type Address: str
        :param _CookieHash: 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。
        :type CookieHash: str
        :param _RegisterSource: 注册来源：
0：其他。
1：PC 网页。
2：移动页面。
3：App。
4：微信公众号。
        :type RegisterSource: str
        :param _Referer: 用户 HTTP 请求的 referer 值。
        :type Referer: str
        :param _JumpUrl: 注册成功后跳转页面。
        :type JumpUrl: str
        :param _UserAgent: 用户 HTTP 请求的 userAgent。
        :type UserAgent: str
        :param _XForwardedFor: 用户 HTTP 请求中的 x_forward_for。
        :type XForwardedFor: str
        :param _MouseClickCount: 用户操作过程中鼠标单击次数。
        :type MouseClickCount: str
        :param _KeyboardClickCount: 用户操作过程中键盘单击次数。
        :type KeyboardClickCount: str
        :param _Result: 注册结果：
0：失败。
1：成功。
        :type Result: str
        :param _Reason: 失败原因：
0：其他。
1：参数错误。
2：帐号冲突。
3：验证错误。
        :type Reason: str
        :param _RegisterSpend: 登录耗时，单位：秒。
        :type RegisterSpend: str
        :param _MacAddress: MAC 地址或设备唯一标识。
        :type MacAddress: str
        :param _VendorId: 手机制造商 ID，如果手机注册，请带上此信息。
        :type VendorId: str
        :param _AppVersion: App 客户端版本。
        :type AppVersion: str
        :param _Imei: 手机设备号。
        :type Imei: str
        :param _BusinessId: 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。
        :type BusinessId: str
        :param _WxSubType: 1：微信公众号。
2：微信小程序。
        :type WxSubType: str
        :param _RandNum: Token 签名随机数，微信小程序必填，建议16个字符。
        :type RandNum: str
        :param _WxToken: 如果是微信小程序，该字段为以 ssesion_key 为 key 去签名随机数 radnNum 得到的值（hmac_sha256签名算法）。
如果是微信公众号或第三方登录，则为授权的 access_token（注意：不是普通 access_token，具体看 微信官方文档）。
        :type WxToken: str
        """
        self._RegisterIp = None
        self._Uid = None
        self._RegisterTime = None
        self._AccountType = None
        self._AppIdU = None
        self._AssociateAccount = None
        self._NickName = None
        self._PhoneNumber = None
        self._EmailAddress = None
        self._Address = None
        self._CookieHash = None
        self._RegisterSource = None
        self._Referer = None
        self._JumpUrl = None
        self._UserAgent = None
        self._XForwardedFor = None
        self._MouseClickCount = None
        self._KeyboardClickCount = None
        self._Result = None
        self._Reason = None
        self._RegisterSpend = None
        self._MacAddress = None
        self._VendorId = None
        self._AppVersion = None
        self._Imei = None
        self._BusinessId = None
        self._WxSubType = None
        self._RandNum = None
        self._WxToken = None

    @property
    def RegisterIp(self):
        return self._RegisterIp

    @RegisterIp.setter
    def RegisterIp(self, RegisterIp):
        self._RegisterIp = RegisterIp

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def RegisterTime(self):
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def AppIdU(self):
        return self._AppIdU

    @AppIdU.setter
    def AppIdU(self, AppIdU):
        self._AppIdU = AppIdU

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

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
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def CookieHash(self):
        return self._CookieHash

    @CookieHash.setter
    def CookieHash(self, CookieHash):
        self._CookieHash = CookieHash

    @property
    def RegisterSource(self):
        return self._RegisterSource

    @RegisterSource.setter
    def RegisterSource(self, RegisterSource):
        self._RegisterSource = RegisterSource

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
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def RegisterSpend(self):
        return self._RegisterSpend

    @RegisterSpend.setter
    def RegisterSpend(self, RegisterSpend):
        self._RegisterSpend = RegisterSpend

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
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

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


    def _deserialize(self, params):
        self._RegisterIp = params.get("RegisterIp")
        self._Uid = params.get("Uid")
        self._RegisterTime = params.get("RegisterTime")
        self._AccountType = params.get("AccountType")
        self._AppIdU = params.get("AppIdU")
        self._AssociateAccount = params.get("AssociateAccount")
        self._NickName = params.get("NickName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._EmailAddress = params.get("EmailAddress")
        self._Address = params.get("Address")
        self._CookieHash = params.get("CookieHash")
        self._RegisterSource = params.get("RegisterSource")
        self._Referer = params.get("Referer")
        self._JumpUrl = params.get("JumpUrl")
        self._UserAgent = params.get("UserAgent")
        self._XForwardedFor = params.get("XForwardedFor")
        self._MouseClickCount = params.get("MouseClickCount")
        self._KeyboardClickCount = params.get("KeyboardClickCount")
        self._Result = params.get("Result")
        self._Reason = params.get("Reason")
        self._RegisterSpend = params.get("RegisterSpend")
        self._MacAddress = params.get("MacAddress")
        self._VendorId = params.get("VendorId")
        self._AppVersion = params.get("AppVersion")
        self._Imei = params.get("Imei")
        self._BusinessId = params.get("BusinessId")
        self._WxSubType = params.get("WxSubType")
        self._RandNum = params.get("RandNum")
        self._WxToken = params.get("WxToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRegisterProtectionResponse(AbstractModel):
    """QueryRegisterProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeDesc: 业务侧错误码，成功时返回 Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param _AssociateAccount: accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param _RegisterTime: 注册时间戳，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisterTime: str
        :param _Uid: 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Uid: str
        :param _RegisterIp: 注册来源的外网 IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisterIp: str
        :param _Level: 0：表示无恶意。
1 - 4：恶意等级由低到高。
        :type Level: int
        :param _RiskType: 风险类型。
        :type RiskType: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CodeDesc = None
        self._AssociateAccount = None
        self._RegisterTime = None
        self._Uid = None
        self._RegisterIp = None
        self._Level = None
        self._RiskType = None
        self._RequestId = None

    @property
    def CodeDesc(self):
        return self._CodeDesc

    @CodeDesc.setter
    def CodeDesc(self, CodeDesc):
        self._CodeDesc = CodeDesc

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

    @property
    def RegisterTime(self):
        return self._RegisterTime

    @RegisterTime.setter
    def RegisterTime(self, RegisterTime):
        self._RegisterTime = RegisterTime

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def RegisterIp(self):
        return self._RegisterIp

    @RegisterIp.setter
    def RegisterIp(self, RegisterIp):
        self._RegisterIp = RegisterIp

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CodeDesc = params.get("CodeDesc")
        self._AssociateAccount = params.get("AssociateAccount")
        self._RegisterTime = params.get("RegisterTime")
        self._Uid = params.get("Uid")
        self._RegisterIp = params.get("RegisterIp")
        self._Level = params.get("Level")
        self._RiskType = params.get("RiskType")
        self._RequestId = params.get("RequestId")