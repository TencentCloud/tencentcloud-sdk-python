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
        """
        :param AccountType: 用户账号类型（默认开通 QQ 开放账号、手机号，手机 MD5 账号类型查询。如需使用微信开放账号，则需要 提交工单 由腾讯云进行资格审核，审核通过后方可正常使用微信开放账号）：
1：QQ开放账号。
2：微信开放账号。
4：手机号（暂仅支持国内手机号）。
8：设备号（imei/imeiMD5/idfa/idfaMd5）。
0：其他。
10004：手机号MD5（标准中国大陆手机号11位，MD5后取32位小写值）\n        :type AccountType: int\n        :param QQAccount: QQ账号信息，AccountType是1时，该字段必填。\n        :type QQAccount: :class:`tencentcloud.aa.v20200224.models.QQAccountInfo`\n        :param WeChatAccount: 微信账号信息，AccountType是2时，该字段必填。\n        :type WeChatAccount: :class:`tencentcloud.aa.v20200224.models.WeChatAccountInfo`\n        :param OtherAccount: 其它账号信息，AccountType是0、4、8或10004时，该字段必填。\n        :type OtherAccount: :class:`tencentcloud.aa.v20200224.models.OtherAccountInfo`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CrowdAntiRushInfo(AbstractModel):
    """网赚防刷相关参数

    """

    def __init__(self):
        """
        :param SponsorOpenId: 助力场景建议填写：活动发起人微信OpenID。\n        :type SponsorOpenId: str\n        :param SponsorDeviceNumber: 助力场景建议填写：发起人设备号。\n        :type SponsorDeviceNumber: str\n        :param SponsorPhone: 助力场景建议填写：发起人手机号。\n        :type SponsorPhone: str\n        :param SponsorIp: 助力场景建议填写：发起人IP。\n        :type SponsorIp: str\n        :param CampaignUrl: 助力场景建议填写：活动链接。\n        :type CampaignUrl: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputActivityAntiRushAdvanced(AbstractModel):
    """活动防刷高级版业务入参。

    """

    def __init__(self):
        """
        :param Account: 账号信息。\n        :type Account: :class:`tencentcloud.aa.v20200224.models.AccountInfo`\n        :param UserIp: 用户IP（外网有效IP地址）。\n        :type UserIp: str\n        :param PostTime: 用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）。\n        :type PostTime: int\n        :param Sponsor: 可选填写。详情请跳转至SponsorInfo查看。\n        :type Sponsor: :class:`tencentcloud.aa.v20200224.models.SponsorInfo`\n        :param OnlineScam: 可选填写。详情请跳转至OnlineScamInfo查看。\n        :type OnlineScam: :class:`tencentcloud.aa.v20200224.models.OnlineScamInfo`\n        :param BusinessId: 业务ID。网站或应用在多个业务中使用此服务，通过此ID区分统计数据。\n        :type BusinessId: int\n        :param Nickname: 昵称，UTF-8 编码。\n        :type Nickname: str\n        :param EmailAddress: 用户邮箱地址（非系统自动生成）。\n        :type EmailAddress: str\n        :param CheckDevice: 是否识别设备异常：
0：不识别。
1：识别。\n        :type CheckDevice: int\n        :param CookieHash: 用户HTTP请求中的Cookie进行2次hash的值，只要保证相同Cookie的hash值一致即可。\n        :type CookieHash: str\n        :param Referer: 用户HTTP请求的Referer值。\n        :type Referer: str\n        :param UserAgent: 用户HTTP请求的User-Agent值。\n        :type UserAgent: str\n        :param XForwardedFor: 用户HTTP请求的X-Forwarded-For值。\n        :type XForwardedFor: str\n        :param MacAddress: MAC地址或设备唯一标识。\n        :type MacAddress: str\n        :param VendorId: 手机制造商ID，如果手机注册，请带上此信息。\n        :type VendorId: str\n        """
        self.Account = None
        self.UserIp = None
        self.PostTime = None
        self.Sponsor = None
        self.OnlineScam = None
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


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self.Account = AccountInfo()
            self.Account._deserialize(params.get("Account"))
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        if params.get("Sponsor") is not None:
            self.Sponsor = SponsorInfo()
            self.Sponsor._deserialize(params.get("Sponsor"))
        if params.get("OnlineScam") is not None:
            self.OnlineScam = OnlineScamInfo()
            self.OnlineScam._deserialize(params.get("OnlineScam"))
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputDetails(AbstractModel):
    """入参的详细参数信息

    """

    def __init__(self):
        """
        :param FieldName: 字段名称\n        :type FieldName: str\n        :param FieldValue: 字段值\n        :type FieldValue: str\n        """
        self.FieldName = None
        self.FieldValue = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.FieldValue = params.get("FieldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputManageMarketingRisk(AbstractModel):
    """营销风控入参

    """

    def __init__(self):
        """
        :param Account: 账号信息。\n        :type Account: :class:`tencentcloud.aa.v20200224.models.AccountInfo`\n        :param UserIp: 登录来源的外网IP\n        :type UserIp: str\n        :param PostTime: 用户操作时间戳，单位秒（格林威治时间精确到秒，如1501590972）。\n        :type PostTime: int\n        :param SceneType: 场景类型。(后续不再支持，请使用SceneCode字段)
1：活动防刷
2：登录保护
3：注册保护
4：活动防刷高级版（网赚）\n        :type SceneType: int\n        :param UserId: 用户唯一标识。\n        :type UserId: str\n        :param DeviceToken: 设备指纹token。\n        :type DeviceToken: str\n        :param DeviceBusinessId: 设备指纹BusinessId\n        :type DeviceBusinessId: int\n        :param BusinessId: 业务ID。网站或应用在多个业务中使用此服务，通过此ID区分统计数据。\n        :type BusinessId: int\n        :param Nickname: 昵称，UTF-8 编码。\n        :type Nickname: str\n        :param EmailAddress: 用户邮箱地址（非系统自动生成）。\n        :type EmailAddress: str\n        :param CheckDevice: 是否识别设备异常：
0：不识别。
1：识别。\n        :type CheckDevice: int\n        :param CookieHash: 用户HTTP请求中的Cookie进行2次hash的值，只要保证相同Cookie的hash值一致即可。\n        :type CookieHash: str\n        :param Referer: 用户HTTP请求的Referer值。\n        :type Referer: str\n        :param UserAgent: 用户HTTP请求的User-Agent值。\n        :type UserAgent: str\n        :param XForwardedFor: 用户HTTP请求的X-Forwarded-For值。\n        :type XForwardedFor: str\n        :param MacAddress: MAC地址或设备唯一标识。\n        :type MacAddress: str\n        :param CrowdAntiRush: 网赚防刷相关信息。SceneType为4时填写。\n        :type CrowdAntiRush: :class:`tencentcloud.aa.v20200224.models.CrowdAntiRushInfo`\n        :param SceneCode: 场景Code，控制台上获取\n        :type SceneCode: str\n        :param Details: 详细信息\n        :type Details: list of InputDetails\n        :param DeviceType: 设备类型：
1：Android
2：IOS\n        :type DeviceType: int\n        """
        self.Account = None
        self.UserIp = None
        self.PostTime = None
        self.SceneType = None
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
        self.CrowdAntiRush = None
        self.SceneCode = None
        self.Details = None
        self.DeviceType = None


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self.Account = AccountInfo()
            self.Account._deserialize(params.get("Account"))
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        self.SceneType = params.get("SceneType")
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
        if params.get("CrowdAntiRush") is not None:
            self.CrowdAntiRush = CrowdAntiRushInfo()
            self.CrowdAntiRush._deserialize(params.get("CrowdAntiRush"))
        self.SceneCode = params.get("SceneCode")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = InputDetails()
                obj._deserialize(item)
                self.Details.append(obj)
        self.DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageMarketingRiskRequest(AbstractModel):
    """ManageMarketingRisk请求参数结构体

    """

    def __init__(self):
        """
        :param BusinessSecurityData: 业务入参\n        :type BusinessSecurityData: :class:`tencentcloud.aa.v20200224.models.InputManageMarketingRisk`\n        """
        self.BusinessSecurityData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = InputManageMarketingRisk()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageMarketingRiskResponse(AbstractModel):
    """ManageMarketingRisk返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 业务出参
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.aa.v20200224.models.OutputManageMarketingRisk`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ContentLabel: 内容标签。\n        :type ContentLabel: str\n        :param ContentRiskLevel: 内容风险等级：
0：正常。
1：可疑。\n        :type ContentRiskLevel: int\n        :param ContentType: 内容产生形式：
0：对话。
1：广播。\n        :type ContentType: int\n        :param FraudType: 诈骗账号类型：
1：11位手机号。
2：QQ账号。\n        :type FraudType: int\n        :param FraudAccount: 诈骗账号，手机号或QQ账号。\n        :type FraudAccount: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注：imeiMd5 加密方式为：imei 明文小写后，进行 MD5 加密，加密后取小写值。IdfaMd5 加密方式为：idfa 明文大写后，进行 MD5 加密，加密后取小写值。\n        :type AccountId: str\n        :param MobilePhone: 手机号，若 AccountType 是4（手机号）、或10004（手机号 MD5），则无需重复填写，否则填入对应的手机号（如13123456789）。\n        :type MobilePhone: str\n        :param DeviceId: 用户设备号。若 AccountType 是8（设备号），则无需重复填写，否则填入对应的设备号。\n        :type DeviceId: str\n        """
        self.AccountId = None
        self.MobilePhone = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.MobilePhone = params.get("MobilePhone")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputActivityAntiRushAdvanced(AbstractModel):
    """活动防刷高级版业务出参。

    """

    def __init__(self):
        """
        :param Code: 返回码。0表示成功，非0标识失败错误码。\n        :type Code: int\n        :param Message: UTF-8编码，出错消息。\n        :type Message: str\n        :param Value: 服务调用结果。\n        :type Value: :class:`tencentcloud.aa.v20200224.models.OutputActivityAntiRushAdvancedValue`\n        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = OutputActivityAntiRushAdvancedValue()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputActivityAntiRushAdvancedValue(AbstractModel):
    """活动防刷高级版业务出参。

    """

    def __init__(self):
        """
        :param UserId: 账号ID。对应输入参数：
AccountType是1时，对应QQ的OpenID。
AccountType是2时，对应微信的OpenID/UnionID。
AccountType是4时，对应手机号。
AccountType是8时，对应imei、idfa、imeiMD5或者idfaMD5。
AccountType是0时，对应账号信息。
AccountType是10004时，对应手机号的MD5。\n        :type UserId: str\n        :param PostTime: 操作时间戳，单位秒（对应输入参数）。\n        :type PostTime: int\n        :param AssociateAccount: AccountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号ID（对应输入参数）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssociateAccount: str\n        :param UserIp: 操作来源的外网IP（对应输入参数）。\n        :type UserIp: str\n        :param Level: 风险值：
0：表示无恶意。
1～4：恶意等级由低到高。\n        :type Level: int\n        :param RiskType: 风险类型，详情请参见下文RiskType详细说明。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RiskType: list of int\n        """
        self.UserId = None
        self.PostTime = None
        self.AssociateAccount = None
        self.UserIp = None
        self.Level = None
        self.RiskType = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.PostTime = params.get("PostTime")
        self.AssociateAccount = params.get("AssociateAccount")
        self.UserIp = params.get("UserIp")
        self.Level = params.get("Level")
        self.RiskType = params.get("RiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRisk(AbstractModel):
    """影响风控出参

    """

    def __init__(self):
        """
        :param Code: 返回码。0表示成功，非0标识失败错误码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Message: UTF-8编码，出错消息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        :param Value: 业务详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: :class:`tencentcloud.aa.v20200224.models.OutputManageMarketingRiskValue`\n        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = OutputManageMarketingRiskValue()
            self.Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRiskValue(AbstractModel):
    """营销风控出参值

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
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserId: str\n        :param PostTime: 操作时间戳，单位秒（对应输入参数）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostTime: int\n        :param AssociateAccount: 对应输入参数，AccountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssociateAccount: str\n        :param UserIp: 操作来源的外网IP（对应输入参数）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserIp: str\n        :param RiskLevel: 风险值
pass : 无恶意
review：需要人工审核
reject：拒绝，高风险恶意
注意：此字段可能返回 null，表示取不到有效值。\n        :type RiskLevel: str\n        :param RiskType: 风险类型，请参考官网风险类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type RiskType: list of int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QQAccountInfo(AbstractModel):
    """QQ账号信息。

    """

    def __init__(self):
        """
        :param QQOpenId: QQ的OpenID。\n        :type QQOpenId: str\n        :param AppIdUser: QQ分配给网站或应用的AppId，用来唯一标识网站或应用。\n        :type AppIdUser: str\n        :param AssociateAccount: 用于标识QQ用户登录后所关联业务自身的账号ID。\n        :type AssociateAccount: str\n        :param MobilePhone: 账号绑定的手机号。\n        :type MobilePhone: str\n        :param DeviceId: 用户设备号。\n        :type DeviceId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityAntiRushAdvancedRequest(AbstractModel):
    """QueryActivityAntiRushAdvanced请求参数结构体

    """

    def __init__(self):
        """
        :param BusinessSecurityData: 业务入参\n        :type BusinessSecurityData: :class:`tencentcloud.aa.v20200224.models.InputActivityAntiRushAdvanced`\n        """
        self.BusinessSecurityData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = InputActivityAntiRushAdvanced()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityAntiRushAdvancedResponse(AbstractModel):
    """QueryActivityAntiRushAdvanced返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 结果信息\n        :type Data: :class:`tencentcloud.aa.v20200224.models.OutputActivityAntiRushAdvanced`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputActivityAntiRushAdvanced()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class QueryActivityAntiRushRequest(AbstractModel):
    """QueryActivityAntiRush请求参数结构体

    """

    def __init__(self):
        """
        :param AccountType: 用户账号类型（默认开通 QQ 开放账号、手机号，手机 MD5 账号类型查询。如需使用微信开放账号，则需要 提交工单 由腾讯云进行资格审核，审核通过后方可正常使用微信开放账号）：
1：QQ 开放帐号。
2：微信开放账号。
4：手机号。
0：其他。
10004：手机号 MD5。\n        :type AccountType: str\n        :param Uid: 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。\n        :type Uid: str\n        :param UserIp: 用户的真实外网 IP。若填入非外网有效ip，会返回level=0的风控结果，risktype中会有205的风险码返回作为标识\n        :type UserIp: str\n        :param PostTime: 用户操作时间戳。\n        :type PostTime: str\n        :param AppIdU: accountType 是QQ开放账号时，该参数必填，表示 QQ 开放平台分配给网站或应用的 AppID，用来唯一标识网站或应用。\n        :type AppIdU: str\n        :param NickName: 昵称，UTF-8 编码。\n        :type NickName: str\n        :param PhoneNumber: 手机号。若 accountType 选4（手机号）、或10004（手机号 MD5），则无需重复填写。否则填入对应的手机号（如15912345687）。accountType为1或2时，该字段支持MD5值；\n        :type PhoneNumber: str\n        :param EmailAddress: 用户邮箱地址。\n        :type EmailAddress: str\n        :param RegisterTime: 注册时间戳。\n        :type RegisterTime: str\n        :param RegisterIp: 注册来源的外网 IP。\n        :type RegisterIp: str\n        :param CookieHash: 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。\n        :type CookieHash: str\n        :param Address: 地址。\n        :type Address: str\n        :param LoginSource: 登录来源：
0：其他。
1：PC 网页。
2：移动页面。
3：App。
4：微信公众号。\n        :type LoginSource: str\n        :param LoginType: 登录方式：
0：其他。
1：手动账号密码输入。
2：动态短信密码登录。
3：二维码扫描登录。\n        :type LoginType: str\n        :param LoginSpend: 登录耗时，单位：秒。\n        :type LoginSpend: str\n        :param RootId: 用户操作的目的 ID，如点赞等，该字段就是被点赞的消息 ID，如果是投票，则为被投号码的 ID。\n        :type RootId: str\n        :param Referer: 用户 HTTP 请求的 referer 值。\n        :type Referer: str\n        :param JumpUrl: 登录成功后跳转页面。\n        :type JumpUrl: str\n        :param UserAgent: 用户 HTTP 请求的 userAgent。\n        :type UserAgent: str\n        :param XForwardedFor: 用户 HTTP 请求中的 x_forward_for。\n        :type XForwardedFor: str\n        :param MouseClickCount: 用户操作过程中鼠标单击次数。\n        :type MouseClickCount: str\n        :param KeyboardClickCount: 用户操作过程中键盘单击次数。\n        :type KeyboardClickCount: str\n        :param MacAddress: MAC 地址或设备唯一标识。\n        :type MacAddress: str\n        :param VendorId: 手机制造商 ID，如果手机注册，请带上此信息。\n        :type VendorId: str\n        :param Imei: 手机设备号。支持以下格式：
1.imei明文
2.idfa明文,
3.imei小写后MD5值小写
4.idfa大写后MD5值小写\n        :type Imei: str\n        :param AppVersion: App 客户端版本。\n        :type AppVersion: str\n        :param BusinessId: 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。\n        :type BusinessId: str\n        :param WxSubType: 1：微信公众号。
2：微信小程序。\n        :type WxSubType: str\n        :param RandNum: Token 签名随机数，WxSubType为微信小程序时必填，建议16个字符。\n        :type RandNum: str\n        :param WxToken: 如果 accountType为2而且wxSubType有填，该字段必选，否则不需要填写；
如果是微信小程序（WxSubType=2），该字段为以ssesion_key为key去签名随机数radnNum得到的值（ hmac_sha256签名算法）；如果是微信公众号或第三方登录，则为授权的access_token（网页版本的access_Token,而且获取token的scope字段必需填写snsapi_userinfo；）\n        :type WxToken: str\n        :param CheckDevice: 是否识别设备异常：
0：不识别。
1：识别。\n        :type CheckDevice: str\n        """
        self.AccountType = None
        self.Uid = None
        self.UserIp = None
        self.PostTime = None
        self.AppIdU = None
        self.NickName = None
        self.PhoneNumber = None
        self.EmailAddress = None
        self.RegisterTime = None
        self.RegisterIp = None
        self.CookieHash = None
        self.Address = None
        self.LoginSource = None
        self.LoginType = None
        self.LoginSpend = None
        self.RootId = None
        self.Referer = None
        self.JumpUrl = None
        self.UserAgent = None
        self.XForwardedFor = None
        self.MouseClickCount = None
        self.KeyboardClickCount = None
        self.MacAddress = None
        self.VendorId = None
        self.Imei = None
        self.AppVersion = None
        self.BusinessId = None
        self.WxSubType = None
        self.RandNum = None
        self.WxToken = None
        self.CheckDevice = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        self.AppIdU = params.get("AppIdU")
        self.NickName = params.get("NickName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.EmailAddress = params.get("EmailAddress")
        self.RegisterTime = params.get("RegisterTime")
        self.RegisterIp = params.get("RegisterIp")
        self.CookieHash = params.get("CookieHash")
        self.Address = params.get("Address")
        self.LoginSource = params.get("LoginSource")
        self.LoginType = params.get("LoginType")
        self.LoginSpend = params.get("LoginSpend")
        self.RootId = params.get("RootId")
        self.Referer = params.get("Referer")
        self.JumpUrl = params.get("JumpUrl")
        self.UserAgent = params.get("UserAgent")
        self.XForwardedFor = params.get("XForwardedFor")
        self.MouseClickCount = params.get("MouseClickCount")
        self.KeyboardClickCount = params.get("KeyboardClickCount")
        self.MacAddress = params.get("MacAddress")
        self.VendorId = params.get("VendorId")
        self.Imei = params.get("Imei")
        self.AppVersion = params.get("AppVersion")
        self.BusinessId = params.get("BusinessId")
        self.WxSubType = params.get("WxSubType")
        self.RandNum = params.get("RandNum")
        self.WxToken = params.get("WxToken")
        self.CheckDevice = params.get("CheckDevice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityAntiRushResponse(AbstractModel):
    """QueryActivityAntiRush返回参数结构体

    """

    def __init__(self):
        """
        :param PostTime: 操作时间戳，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostTime: str\n        :param UserIp: 用户操作的真实外网 IP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserIp: str\n        :param Level: 0：表示无恶意。
1 - 4：恶意等级由低到高。\n        :type Level: int\n        :param RiskType: 风险类型。

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
206，设备异常，该设备存在异常的使用行为\n        :type RiskType: list of int\n        :param AssociateAccount: accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssociateAccount: str\n        :param Uid: 用户ID 
accountType不同对应不同的用户ID。如果是QQ或微信用户则填入对应的openId
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uid: str\n        :param RootId: 用户操作的目的ID 
比如：点赞，该字段就是被点 赞的消息 id，如果是投票，就是被投号码的 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RootId: str\n        :param CodeDesc: 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CodeDesc: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PostTime = None
        self.UserIp = None
        self.Level = None
        self.RiskType = None
        self.AssociateAccount = None
        self.Uid = None
        self.RootId = None
        self.CodeDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostTime = params.get("PostTime")
        self.UserIp = params.get("UserIp")
        self.Level = params.get("Level")
        self.RiskType = params.get("RiskType")
        self.AssociateAccount = params.get("AssociateAccount")
        self.Uid = params.get("Uid")
        self.RootId = params.get("RootId")
        self.CodeDesc = params.get("CodeDesc")
        self.RequestId = params.get("RequestId")


class SponsorInfo(AbstractModel):
    """助力场景信息

    """

    def __init__(self):
        """
        :param SponsorOpenId: 助力场景建议填写：活动发起人微信OpenID。\n        :type SponsorOpenId: str\n        :param SponsorDeviceId: 助力场景建议填写：发起人设备号。\n        :type SponsorDeviceId: str\n        :param SponsorPhone: 助力场景建议填写：发起人手机号。\n        :type SponsorPhone: str\n        :param SponsorIp: 助力场景建议填写：发起人IP。\n        :type SponsorIp: str\n        :param CampaignUrl: 助力场景建议填写：活动链接。\n        :type CampaignUrl: str\n        """
        self.SponsorOpenId = None
        self.SponsorDeviceId = None
        self.SponsorPhone = None
        self.SponsorIp = None
        self.CampaignUrl = None


    def _deserialize(self, params):
        self.SponsorOpenId = params.get("SponsorOpenId")
        self.SponsorDeviceId = params.get("SponsorDeviceId")
        self.SponsorPhone = params.get("SponsorPhone")
        self.SponsorIp = params.get("SponsorIp")
        self.CampaignUrl = params.get("CampaignUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeChatAccountInfo(AbstractModel):
    """微信账号信息。

    """

    def __init__(self):
        """
        :param WeChatOpenId: 微信的OpenID/UnionID 。\n        :type WeChatOpenId: str\n        :param WeChatSubType: 微信开放账号类型：
1：微信公众号/微信第三方登录。
2：微信小程序。\n        :type WeChatSubType: int\n        :param RandStr: 随机串。如果WeChatSubType是2，该字段必填。Token签名随机数，建议16个字符。\n        :type RandStr: str\n        :param WeChatAccessToken: 如果WeChatSubType是1，填入授权的access_token（注意：不是普通access_token，详情请参阅官方说明文档。获取网页版本的access_token时，scope字段必需填写snsapi_userinfo。
如果WeChatSubType是2，填入以session_key为密钥签名随机数RandStr（hmac_sha256签名算法）得到的字符串。\n        :type WeChatAccessToken: str\n        :param AssociateAccount: 用于标识微信用户登录后所关联业务自身的账号ID。\n        :type AssociateAccount: str\n        :param MobilePhone: 账号绑定的手机号。\n        :type MobilePhone: str\n        :param DeviceId: 用户设备号。\n        :type DeviceId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        