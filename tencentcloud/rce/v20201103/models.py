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
    """账号信息。

    """

    def __init__(self):
        r"""
        :param _AccountType: 用户账号类型；默认开通QQOpenId、手机号MD5权限；如果需要使用微信OpenId入参，则需要"提交工单"或联系对接人进行资格审核，审核通过后方可正常使用微信开放账号。
1：QQ开放账号
2：微信开放账号
10004：手机号MD5，中国大陆11位手机号进行MD5加密，取32位小写值
10005：手机号SHA256，中国大陆11位手机号进行SHA256加密，取64位小写值
        :type AccountType: int
        :param _QQAccount: QQ账号信息，AccountType是"1"时，该字段必填。
        :type QQAccount: :class:`tencentcloud.rce.v20201103.models.QQAccountInfo`
        :param _WeChatAccount: 微信账号信息，AccountType是"2"时，该字段必填。
        :type WeChatAccount: :class:`tencentcloud.rce.v20201103.models.WeChatAccountInfo`
        :param _OtherAccount: 其它账号信息，AccountType是10004或10005时，该字段必填。
        :type OtherAccount: :class:`tencentcloud.rce.v20201103.models.OtherAccountInfo`
        """
        self._AccountType = None
        self._QQAccount = None
        self._WeChatAccount = None
        self._OtherAccount = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def QQAccount(self):
        return self._QQAccount

    @QQAccount.setter
    def QQAccount(self, QQAccount):
        self._QQAccount = QQAccount

    @property
    def WeChatAccount(self):
        return self._WeChatAccount

    @WeChatAccount.setter
    def WeChatAccount(self, WeChatAccount):
        self._WeChatAccount = WeChatAccount

    @property
    def OtherAccount(self):
        return self._OtherAccount

    @OtherAccount.setter
    def OtherAccount(self, OtherAccount):
        self._OtherAccount = OtherAccount


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        if params.get("QQAccount") is not None:
            self._QQAccount = QQAccountInfo()
            self._QQAccount._deserialize(params.get("QQAccount"))
        if params.get("WeChatAccount") is not None:
            self._WeChatAccount = WeChatAccountInfo()
            self._WeChatAccount._deserialize(params.get("WeChatAccount"))
        if params.get("OtherAccount") is not None:
            self._OtherAccount = OtherAccountInfo()
            self._OtherAccount._deserialize(params.get("OtherAccount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputCryptoManageMarketingRisk(AbstractModel):
    """全栈式风控引擎入参

    """

    def __init__(self):
        r"""
        :param _IsAuthorized: 是否授权：1已授权，否则未授权。
 调用全栈式风控引擎接口服务时，客户需先明确授权


        :type IsAuthorized: str
        :param _CryptoType: 加密类型：1AES加密

        :type CryptoType: str
        :param _CryptoContent: 加密内容，非空时接口采用加密模式。
        :type CryptoContent: str
        """
        self._IsAuthorized = None
        self._CryptoType = None
        self._CryptoContent = None

    @property
    def IsAuthorized(self):
        return self._IsAuthorized

    @IsAuthorized.setter
    def IsAuthorized(self, IsAuthorized):
        self._IsAuthorized = IsAuthorized

    @property
    def CryptoType(self):
        return self._CryptoType

    @CryptoType.setter
    def CryptoType(self, CryptoType):
        self._CryptoType = CryptoType

    @property
    def CryptoContent(self):
        return self._CryptoContent

    @CryptoContent.setter
    def CryptoContent(self, CryptoContent):
        self._CryptoContent = CryptoContent


    def _deserialize(self, params):
        self._IsAuthorized = params.get("IsAuthorized")
        self._CryptoType = params.get("CryptoType")
        self._CryptoContent = params.get("CryptoContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputDetails(AbstractModel):
    """入参的详细参数信息

    """

    def __init__(self):
        r"""
        :param _FieldName: 字段名称
        :type FieldName: str
        :param _FieldValue: 字段值
        :type FieldValue: str
        """
        self._FieldName = None
        self._FieldValue = None

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def FieldValue(self):
        return self._FieldValue

    @FieldValue.setter
    def FieldValue(self, FieldValue):
        self._FieldValue = FieldValue


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._FieldValue = params.get("FieldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputManageMarketingRisk(AbstractModel):
    """全栈式风控引擎入参

    """

    def __init__(self):
        r"""
        :param _Account: 用户账号类型；默认开通QQOpenId、手机号MD5权限；如果需要使用微信OpenId入参，则需要"提交工单"或联系对接人进行资格审核，审核通过后方可正常使用微信开放账号。
1：QQ开放账号
2：微信开放账号
10004：手机号MD5，中国大陆11位手机号进行MD5加密，取32位小写值
10005：手机号SHA256，中国大陆11位手机号进行SHA256加密，取64位小写值
        :type Account: :class:`tencentcloud.rce.v20201103.models.AccountInfo`
        :param _SceneCode: 场景码，用于识别和区分不同的业务场景，可在控制台上新建和管理
控制台链接：https://console.cloud.tencent.com/rce/risk/strategy/scene-root
活动防刷默认场景码：e_activity_antirush 
登录保护默认场景码：e_login_protection
注册保护默认场景码：e_register_protection
        :type SceneCode: str
        :param _UserIp: 用户外网ip（传入用户非外网ip会影响判断结果）。
        :type UserIp: str
        :param _PostTime: 用户操作时间戳，精确到秒。
        :type PostTime: int
        :param _UserId: 业务平台用户唯一标识，支持自定义。
        :type UserId: str
        :param _DeviceToken: 设备指纹DeviceToken值，集成设备指纹后获取；如果集成了相应的设备指纹，该字段必填。
        :type DeviceToken: str
        :param _DeviceBusinessId: 设备指纹 BusinessId。
        :type DeviceBusinessId: int
        :param _BusinessId: 业务ID。网站或应用在多个业务中使用此服务，通过此ID区分统计数据。
        :type BusinessId: int
        :param _Nickname: 昵称，UTF-8 编码。
        :type Nickname: str
        :param _EmailAddress: 用户邮箱地址。
        :type EmailAddress: str
        :param _CheckDevice: 是否识别设备异常：
0：不识别。
1：识别。
        :type CheckDevice: int
        :param _CookieHash: 用户HTTP请求中的Cookie进行2次hash的值，只要保证相同Cookie的hash值一致即可。
        :type CookieHash: str
        :param _Referer: 用户HTTP请求的Referer值。
        :type Referer: str
        :param _UserAgent: 用户HTTP请求的User-Agent值。
        :type UserAgent: str
        :param _XForwardedFor: 用户HTTP请求的X-Forwarded-For值。
        :type XForwardedFor: str
        :param _MacAddress: MAC地址或设备唯一标识。
        :type MacAddress: str
        :param _VendorId: 手机制造商ID，如果手机注册，请带上此信息。
        :type VendorId: str
        :param _DeviceType: 设备类型(已不推荐使用)。
        :type DeviceType: int
        :param _Details: 扩展字段。
        :type Details: list of InputDetails
        :param _Sponsor: 邀请助力场景相关信息。
        :type Sponsor: :class:`tencentcloud.rce.v20201103.models.SponsorInfo`
        :param _OnlineScam: 详情请跳转至OnlineScamInfo查看。
        :type OnlineScam: :class:`tencentcloud.rce.v20201103.models.OnlineScamInfo`
        :param _Platform: 1：Android
2：iOS
3：H5
4：小程序

        :type Platform: str
        """
        self._Account = None
        self._SceneCode = None
        self._UserIp = None
        self._PostTime = None
        self._UserId = None
        self._DeviceToken = None
        self._DeviceBusinessId = None
        self._BusinessId = None
        self._Nickname = None
        self._EmailAddress = None
        self._CheckDevice = None
        self._CookieHash = None
        self._Referer = None
        self._UserAgent = None
        self._XForwardedFor = None
        self._MacAddress = None
        self._VendorId = None
        self._DeviceType = None
        self._Details = None
        self._Sponsor = None
        self._OnlineScam = None
        self._Platform = None

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def SceneCode(self):
        return self._SceneCode

    @SceneCode.setter
    def SceneCode(self, SceneCode):
        self._SceneCode = SceneCode

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
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken

    @property
    def DeviceBusinessId(self):
        return self._DeviceBusinessId

    @DeviceBusinessId.setter
    def DeviceBusinessId(self, DeviceBusinessId):
        self._DeviceBusinessId = DeviceBusinessId

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def EmailAddress(self):
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def CheckDevice(self):
        return self._CheckDevice

    @CheckDevice.setter
    def CheckDevice(self, CheckDevice):
        self._CheckDevice = CheckDevice

    @property
    def CookieHash(self):
        return self._CookieHash

    @CookieHash.setter
    def CookieHash(self, CookieHash):
        self._CookieHash = CookieHash

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

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
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def Sponsor(self):
        return self._Sponsor

    @Sponsor.setter
    def Sponsor(self, Sponsor):
        self._Sponsor = Sponsor

    @property
    def OnlineScam(self):
        return self._OnlineScam

    @OnlineScam.setter
    def OnlineScam(self, OnlineScam):
        self._OnlineScam = OnlineScam

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self._Account = AccountInfo()
            self._Account._deserialize(params.get("Account"))
        self._SceneCode = params.get("SceneCode")
        self._UserIp = params.get("UserIp")
        self._PostTime = params.get("PostTime")
        self._UserId = params.get("UserId")
        self._DeviceToken = params.get("DeviceToken")
        self._DeviceBusinessId = params.get("DeviceBusinessId")
        self._BusinessId = params.get("BusinessId")
        self._Nickname = params.get("Nickname")
        self._EmailAddress = params.get("EmailAddress")
        self._CheckDevice = params.get("CheckDevice")
        self._CookieHash = params.get("CookieHash")
        self._Referer = params.get("Referer")
        self._UserAgent = params.get("UserAgent")
        self._XForwardedFor = params.get("XForwardedFor")
        self._MacAddress = params.get("MacAddress")
        self._VendorId = params.get("VendorId")
        self._DeviceType = params.get("DeviceType")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = InputDetails()
                obj._deserialize(item)
                self._Details.append(obj)
        if params.get("Sponsor") is not None:
            self._Sponsor = SponsorInfo()
            self._Sponsor._deserialize(params.get("Sponsor"))
        if params.get("OnlineScam") is not None:
            self._OnlineScam = OnlineScamInfo()
            self._OnlineScam._deserialize(params.get("OnlineScam"))
        self._Platform = params.get("Platform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageMarketingRiskRequest(AbstractModel):
    """ManageMarketingRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.rce.v20201103.models.InputManageMarketingRisk`
        :param _BusinessCryptoData: 业务入参
        :type BusinessCryptoData: :class:`tencentcloud.rce.v20201103.models.InputCryptoManageMarketingRisk`
        """
        self._BusinessSecurityData = None
        self._BusinessCryptoData = None

    @property
    def BusinessSecurityData(self):
        return self._BusinessSecurityData

    @BusinessSecurityData.setter
    def BusinessSecurityData(self, BusinessSecurityData):
        self._BusinessSecurityData = BusinessSecurityData

    @property
    def BusinessCryptoData(self):
        return self._BusinessCryptoData

    @BusinessCryptoData.setter
    def BusinessCryptoData(self, BusinessCryptoData):
        self._BusinessCryptoData = BusinessCryptoData


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self._BusinessSecurityData = InputManageMarketingRisk()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        if params.get("BusinessCryptoData") is not None:
            self._BusinessCryptoData = InputCryptoManageMarketingRisk()
            self._BusinessCryptoData._deserialize(params.get("BusinessCryptoData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageMarketingRiskResponse(AbstractModel):
    """ManageMarketingRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 业务出参
        :type Data: :class:`tencentcloud.rce.v20201103.models.OutputManageMarketingRisk`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = OutputManageMarketingRisk()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class OnlineScamInfo(AbstractModel):
    """诈骗信息。

    """

    def __init__(self):
        r"""
        :param _ContentLabel: 内容标签。
        :type ContentLabel: str
        :param _ContentRiskLevel: 内容风险等级：
0：正常。
1：可疑。
        :type ContentRiskLevel: int
        :param _ContentType: 内容产生形式：
0：对话。
1：广播。
        :type ContentType: int
        :param _FraudType: 类型
        :type FraudType: int
        :param _FraudAccount: 账号
        :type FraudAccount: str
        """
        self._ContentLabel = None
        self._ContentRiskLevel = None
        self._ContentType = None
        self._FraudType = None
        self._FraudAccount = None

    @property
    def ContentLabel(self):
        return self._ContentLabel

    @ContentLabel.setter
    def ContentLabel(self, ContentLabel):
        self._ContentLabel = ContentLabel

    @property
    def ContentRiskLevel(self):
        return self._ContentRiskLevel

    @ContentRiskLevel.setter
    def ContentRiskLevel(self, ContentRiskLevel):
        self._ContentRiskLevel = ContentRiskLevel

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def FraudType(self):
        return self._FraudType

    @FraudType.setter
    def FraudType(self, FraudType):
        self._FraudType = FraudType

    @property
    def FraudAccount(self):
        return self._FraudAccount

    @FraudAccount.setter
    def FraudAccount(self, FraudAccount):
        self._FraudAccount = FraudAccount


    def _deserialize(self, params):
        self._ContentLabel = params.get("ContentLabel")
        self._ContentRiskLevel = params.get("ContentRiskLevel")
        self._ContentType = params.get("ContentType")
        self._FraudType = params.get("FraudType")
        self._FraudAccount = params.get("FraudAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherAccountInfo(AbstractModel):
    """其它账号信息。

    """

    def __init__(self):
        r"""
        :param _AccountId: 其他账号信息；
AccountType是10004时，填入中国大陆标准11位手机号的MD5值
AccountType是10005时，填入中国大陆标准11位手机号的SHA256值
注释：
MD5手机号加密方式，使用中国大陆11位手机号进行MD5加密，加密后取32位小写值。
SHA256手机号加密方式，使用中国大陆11位手机号进行SHA256加密，加密后取64位小写值。
        :type AccountId: str
        :param _MobilePhone: 账号绑定的MD5或SHA256加密的手机号（该字段已不推荐使用）。
注释：支持标准中国大陆11位手机号MD5加密后位的32位小写字符串；
     支持标准中国大陆11位手机号SHA256加密后位的64位小写字符串。
        :type MobilePhone: str
        :param _DeviceId: 用户设备号（该字段已不推荐使用）。
        :type DeviceId: str
        """
        self._AccountId = None
        self._MobilePhone = None
        self._DeviceId = None

    @property
    def AccountId(self):
        return self._AccountId

    @AccountId.setter
    def AccountId(self, AccountId):
        self._AccountId = AccountId

    @property
    def MobilePhone(self):
        return self._MobilePhone

    @MobilePhone.setter
    def MobilePhone(self, MobilePhone):
        self._MobilePhone = MobilePhone

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._AccountId = params.get("AccountId")
        self._MobilePhone = params.get("MobilePhone")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRisk(AbstractModel):
    """全栈式风控引擎出参

    """

    def __init__(self):
        r"""
        :param _Code: 错误码，0 表示成功，非0表示失败错误码。
0：成功
1：错误
1002：参数错误
4300：未开通服务
4301：后端未创建对应产品
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Message: UTF-8编码，出错消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Value: 业务详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.rce.v20201103.models.OutputManageMarketingRiskValue`
        :param _UUid: 控制台显示的req_id。
注意：此字段可能返回 null，表示取不到有效值。
        :type UUid: str
        """
        self._Code = None
        self._Message = None
        self._Value = None
        self._UUid = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def UUid(self):
        return self._UUid

    @UUid.setter
    def UUid(self, UUid):
        self._UUid = UUid


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Value") is not None:
            self._Value = OutputManageMarketingRiskValue()
            self._Value._deserialize(params.get("Value"))
        self._UUid = params.get("UUid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRiskValue(AbstractModel):
    """全栈式风控引擎出参值

    """

    def __init__(self):
        r"""
        :param _UserId: 账号ID：对应输入参数。
当AccountType为1时，对应QQ的OpenId；
当AccountType为2时，对应微信的OpenId/UnionId；
当AccountType为10004时，对应手机号的MD5值；
当AccountType为10005时，对应手机号的SHA256值。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _PostTime: 操作时间戳，单位秒（对应输入参数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: int
        :param _AssociateAccount: 业务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param _UserIp: 操作来源的外网IP（对应输入参数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param _RiskLevel: 风险等级
pass：无恶意
review：低风险，需要人工审核
reject：高风险，建议拦截
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: str
        :param _RiskType: 风险类型，可能同时命中多个风险类型
1: 账号信用低，账号近期存在因恶意被处罚历史，网络低活跃，被举报等因素。
11: 疑似低活跃账号，账号活跃度与正常用户有差异。
2: 垃圾账号，疑似批量注册小号，近期存在严重违规或大量举报。
21: 疑似小号，账号有疑似线上养号，小号等行为。
22: 疑似违规账号，账号曾有违规行为、曾被举报过、曾因违规被处罚过等。
3: 无效账号，送检账号参数无法成功解析，请检查微信 OpenId 是否有误/AppId 与 QQ OpenId 无法关联/微信 OpenId 权限是否开通/手机号是否为中国大陆手机号；
4: 黑名单，该账号在业务侧有过拉黑记录。
5: 白名单，业务自行有添加过白名单记录。
101: 批量操作，存在 IP/设备/环境等因素的聚集性异常。
1011: 疑似 IP 属性聚集，出现 IP 聚集。
1012: 疑似设备属性聚集，出现设备聚集。
102: 自动机，疑似自动机批量请求。
103: 恶意行为-网赚，疑似网赚。
104: 微信登录态无效，检查 WeChatAccessToken 参数，是否已经失效。
201: 环境风险，环境异常操作 IP/设备/环境存在异常。当前 IP 为非常用 IP 或恶意 IP 段。
2011: 疑似非常用IP，请求当前请求 IP 非该账号常用 IP。
2012: 疑似 IP 异常，使用 IDC 机房 IP 或使用代理 IP 或使用恶意 IP 等。
205: 非公网有效 IP，传进来的 IP 地址为内网 IP 地址或者 IP 保留地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskType: list of int
        :param _ConstId: 设备指纹ID，如果集成了设备指纹，并传入了正确的DeviceToken和Platform，该字段正常输出；如果DeviceToken异常（校验不通过），则会在RiskType中返回"-1"标签，ConstId字段为空；如果没有集成设备指纹ConstId字段默认为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConstId: str
        :param _RiskInformation: 风险扩展数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInformation: str
        """
        self._UserId = None
        self._PostTime = None
        self._AssociateAccount = None
        self._UserIp = None
        self._RiskLevel = None
        self._RiskType = None
        self._ConstId = None
        self._RiskInformation = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskType(self):
        return self._RiskType

    @RiskType.setter
    def RiskType(self, RiskType):
        self._RiskType = RiskType

    @property
    def ConstId(self):
        return self._ConstId

    @ConstId.setter
    def ConstId(self, ConstId):
        self._ConstId = ConstId

    @property
    def RiskInformation(self):
        return self._RiskInformation

    @RiskInformation.setter
    def RiskInformation(self, RiskInformation):
        self._RiskInformation = RiskInformation


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PostTime = params.get("PostTime")
        self._AssociateAccount = params.get("AssociateAccount")
        self._UserIp = params.get("UserIp")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskType = params.get("RiskType")
        self._ConstId = params.get("ConstId")
        self._RiskInformation = params.get("RiskInformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QQAccountInfo(AbstractModel):
    """QQ账号信息。

    """

    def __init__(self):
        r"""
        :param _QQOpenId: QQ的OpenId。
        :type QQOpenId: str
        :param _AppIdUser: QQ分配给网站或应用的AppId，用来唯一标识网站或应用。
        :type AppIdUser: str
        :param _AssociateAccount: 用于标识QQ用户登录后所关联业务自身的账号ID。
        :type AssociateAccount: str
        :param _MobilePhone: 账号绑定的MD5或SHA256加密的手机号。
注释：支持标准中国大陆11位手机号MD5加密后位的32位小写字符串；
     支持标准中国大陆11位手机号SHA256加密后位的64位小写字符串。
        :type MobilePhone: str
        :param _DeviceId: 用户设备号（已不推荐使用）。

        :type DeviceId: str
        """
        self._QQOpenId = None
        self._AppIdUser = None
        self._AssociateAccount = None
        self._MobilePhone = None
        self._DeviceId = None

    @property
    def QQOpenId(self):
        return self._QQOpenId

    @QQOpenId.setter
    def QQOpenId(self, QQOpenId):
        self._QQOpenId = QQOpenId

    @property
    def AppIdUser(self):
        return self._AppIdUser

    @AppIdUser.setter
    def AppIdUser(self, AppIdUser):
        self._AppIdUser = AppIdUser

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

    @property
    def MobilePhone(self):
        return self._MobilePhone

    @MobilePhone.setter
    def MobilePhone(self, MobilePhone):
        self._MobilePhone = MobilePhone

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._QQOpenId = params.get("QQOpenId")
        self._AppIdUser = params.get("AppIdUser")
        self._AssociateAccount = params.get("AssociateAccount")
        self._MobilePhone = params.get("MobilePhone")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SponsorInfo(AbstractModel):
    """网赚防刷相关参数

    """

    def __init__(self):
        r"""
        :param _SponsorOpenId: 助力场景建议填写：活动发起人微信OpenId。
        :type SponsorOpenId: str
        :param _SponsorDeviceNumber: 助力场景建议填写：发起人设备号
        :type SponsorDeviceNumber: str
        :param _SponsorPhone: 助力场景建议填写：发起人的MD5手机号
        :type SponsorPhone: str
        :param _SponsorIp: 助力场景建议填写：发起人IP
        :type SponsorIp: str
        :param _CampaignUrl: 助力场景建议填写：活动链接
        :type CampaignUrl: str
        """
        self._SponsorOpenId = None
        self._SponsorDeviceNumber = None
        self._SponsorPhone = None
        self._SponsorIp = None
        self._CampaignUrl = None

    @property
    def SponsorOpenId(self):
        return self._SponsorOpenId

    @SponsorOpenId.setter
    def SponsorOpenId(self, SponsorOpenId):
        self._SponsorOpenId = SponsorOpenId

    @property
    def SponsorDeviceNumber(self):
        return self._SponsorDeviceNumber

    @SponsorDeviceNumber.setter
    def SponsorDeviceNumber(self, SponsorDeviceNumber):
        self._SponsorDeviceNumber = SponsorDeviceNumber

    @property
    def SponsorPhone(self):
        return self._SponsorPhone

    @SponsorPhone.setter
    def SponsorPhone(self, SponsorPhone):
        self._SponsorPhone = SponsorPhone

    @property
    def SponsorIp(self):
        return self._SponsorIp

    @SponsorIp.setter
    def SponsorIp(self, SponsorIp):
        self._SponsorIp = SponsorIp

    @property
    def CampaignUrl(self):
        return self._CampaignUrl

    @CampaignUrl.setter
    def CampaignUrl(self, CampaignUrl):
        self._CampaignUrl = CampaignUrl


    def _deserialize(self, params):
        self._SponsorOpenId = params.get("SponsorOpenId")
        self._SponsorDeviceNumber = params.get("SponsorDeviceNumber")
        self._SponsorPhone = params.get("SponsorPhone")
        self._SponsorIp = params.get("SponsorIp")
        self._CampaignUrl = params.get("CampaignUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeChatAccountInfo(AbstractModel):
    """微信账号信息。

    """

    def __init__(self):
        r"""
        :param _WeChatOpenId: 微信的OpenId/UnionId。
        :type WeChatOpenId: str
        :param _WeChatSubType: 微信开放账号类型：
1：微信公众号/微信第三方登录。
2：微信小程序。
        :type WeChatSubType: int
        :param _RandStr: 随机串。如果WeChatSubType是2，该字段必填。Token签名随机数，建议16个字符。
        :type RandStr: str
        :param _WeChatAccessToken: 如果WeChatSubType 是1，填入授权的 access_token（注意：不是普通 access_token，详情请参阅官方说明文档。获取网页版本的 access_token 时，scope 字段必需填写snsapi_userinfo
如果WeChatSubType是2，填入以session_key 为密钥签名随机数RandStr（hmac_sha256签名算法）得到的字符串。
        :type WeChatAccessToken: str
        :param _AssociateAccount: 用于标识微信用户登录后所关联业务自身的账号ID。
        :type AssociateAccount: str
        :param _MobilePhone: 账号绑定的MD5或SHA256加密的手机号。
注释：支持标准中国大陆11位手机号MD5加密后位的32位小写字符串；
     支持标准中国大陆11位手机号SHA256加密后位的64位小写字符串。
        :type MobilePhone: str
        :param _DeviceId: 用户设备号（已不推荐使用）。
        :type DeviceId: str
        """
        self._WeChatOpenId = None
        self._WeChatSubType = None
        self._RandStr = None
        self._WeChatAccessToken = None
        self._AssociateAccount = None
        self._MobilePhone = None
        self._DeviceId = None

    @property
    def WeChatOpenId(self):
        return self._WeChatOpenId

    @WeChatOpenId.setter
    def WeChatOpenId(self, WeChatOpenId):
        self._WeChatOpenId = WeChatOpenId

    @property
    def WeChatSubType(self):
        return self._WeChatSubType

    @WeChatSubType.setter
    def WeChatSubType(self, WeChatSubType):
        self._WeChatSubType = WeChatSubType

    @property
    def RandStr(self):
        return self._RandStr

    @RandStr.setter
    def RandStr(self, RandStr):
        self._RandStr = RandStr

    @property
    def WeChatAccessToken(self):
        return self._WeChatAccessToken

    @WeChatAccessToken.setter
    def WeChatAccessToken(self, WeChatAccessToken):
        self._WeChatAccessToken = WeChatAccessToken

    @property
    def AssociateAccount(self):
        return self._AssociateAccount

    @AssociateAccount.setter
    def AssociateAccount(self, AssociateAccount):
        self._AssociateAccount = AssociateAccount

    @property
    def MobilePhone(self):
        return self._MobilePhone

    @MobilePhone.setter
    def MobilePhone(self, MobilePhone):
        self._MobilePhone = MobilePhone

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._WeChatOpenId = params.get("WeChatOpenId")
        self._WeChatSubType = params.get("WeChatSubType")
        self._RandStr = params.get("RandStr")
        self._WeChatAccessToken = params.get("WeChatAccessToken")
        self._AssociateAccount = params.get("AssociateAccount")
        self._MobilePhone = params.get("MobilePhone")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        