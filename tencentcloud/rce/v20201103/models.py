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
        :param AccountType: 账号类型
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskAssessmentRequest(AbstractModel):
    """DescribeRiskAssessment请求参数结构体

    """


class DescribeRiskAssessmentResponse(AbstractModel):
    """DescribeRiskAssessment返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeRiskTrendsRequest(AbstractModel):
    """DescribeRiskTrends请求参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.rce.v20201103.models.InputFrontRisk`
        """
        self.BusinessSecurityData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = InputFrontRisk()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskTrendsResponse(AbstractModel):
    """DescribeRiskTrends返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 业务出参
        :type Data: :class:`tencentcloud.rce.v20201103.models.OutputFrontRiskData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputFrontRiskData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class InputCryptoManageMarketingRisk(AbstractModel):
    """全栈式风控引擎入参

    """

    def __init__(self):
        r"""
        :param IsAuthorized: 是否授权
        :type IsAuthorized: str
        :param CryptoType: 加密类型
        :type CryptoType: str
        :param CryptoContent: 加密内容
        :type CryptoContent: str
        """
        self.IsAuthorized = None
        self.CryptoType = None
        self.CryptoContent = None


    def _deserialize(self, params):
        self.IsAuthorized = params.get("IsAuthorized")
        self.CryptoType = params.get("CryptoType")
        self.CryptoContent = params.get("CryptoContent")
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputFrontRisk(AbstractModel):
    """风险趋势统计--入参

    """

    def __init__(self):
        r"""
        :param EventId: 事件ID
        :type EventId: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Type: 趋势类型
        :type Type: int
        :param CurrentStartTime: 当前开始时间
        :type CurrentStartTime: str
        :param CurrentEndTime: 当前结束时间
        :type CurrentEndTime: str
        """
        self.EventId = None
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.CurrentStartTime = None
        self.CurrentEndTime = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.CurrentStartTime = params.get("CurrentStartTime")
        self.CurrentEndTime = params.get("CurrentEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputManageMarketingRisk(AbstractModel):
    """全栈式风控引擎入参

    """

    def __init__(self):
        r"""
        :param Account: 账号信息。
        :type Account: :class:`tencentcloud.rce.v20201103.models.AccountInfo`
        :param SceneCode: 场景类型：场景SceneCode, 控制台上新建对应的场景并获取对应的值；
例如：e_register_protection_1521184361
控制台链接：https://console.cloud.tencent.com/rce/risk/sceneroot；
        :type SceneCode: str
        :param UserIp: 登录来源的外网IP
        :type UserIp: str
        :param PostTime: 时间戳
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
        :type Details: list of InputDetails
        :param Sponsor: 可选填写。详情请跳转至SponsorInfo查看。
        :type Sponsor: :class:`tencentcloud.rce.v20201103.models.SponsorInfo`
        :param OnlineScam: 可选填写。详情请跳转至OnlineScamInfo查看。
        :type OnlineScam: :class:`tencentcloud.rce.v20201103.models.OnlineScamInfo`
        :param Platform: 平台: 1android
        :type Platform: str
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
        self.Platform = None


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
        self.Platform = params.get("Platform")
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
        r"""
        :param BusinessSecurityData: 业务入参
        :type BusinessSecurityData: :class:`tencentcloud.rce.v20201103.models.InputManageMarketingRisk`
        :param BusinessCryptoData: 业务入参
        :type BusinessCryptoData: :class:`tencentcloud.rce.v20201103.models.InputCryptoManageMarketingRisk`
        """
        self.BusinessSecurityData = None
        self.BusinessCryptoData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = InputManageMarketingRisk()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        if params.get("BusinessCryptoData") is not None:
            self.BusinessCryptoData = InputCryptoManageMarketingRisk()
            self.BusinessCryptoData._deserialize(params.get("BusinessCryptoData"))
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
        r"""
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
        r"""
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
        :param FraudType: 类型
        :type FraudType: int
        :param FraudAccount: 账号
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
        r"""
        :param AccountId: id
        :type AccountId: str
        :param MobilePhone: 手机号
        :type MobilePhone: str
        :param DeviceId: id
        :type DeviceId: str
        """
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
        


class OutputFrontRisk(AbstractModel):
    """风险趋势统计出参，需要为数组

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of OutputFrontRiskValue
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = OutputFrontRiskValue()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputFrontRiskData(AbstractModel):
    """风险趋势统计--出参

    """

    def __init__(self):
        r"""
        :param Code: 返回码[0：成功；非0：标识失败错误码]。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: 出错消息[UTF-8编码]。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of OutputFrontRisk
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = OutputFrontRisk()
                obj._deserialize(item)
                self.Value.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputFrontRiskValue(AbstractModel):
    """风险趋势统计--值

    """

    def __init__(self):
        r"""
        :param Requests: 请求次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Requests: int
        :param Index: 日期标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: str
        """
        self.Requests = None
        self.Index = None


    def _deserialize(self, params):
        self.Requests = params.get("Requests")
        self.Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRisk(AbstractModel):
    """全栈式风控引擎出参

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputManageMarketingRiskValue(AbstractModel):
    """全栈式风控引擎出参值

    """

    def __init__(self):
        r"""
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
        :param ConstId: 唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConstId: str
        """
        self.UserId = None
        self.PostTime = None
        self.AssociateAccount = None
        self.UserIp = None
        self.RiskLevel = None
        self.RiskType = None
        self.ConstId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.PostTime = params.get("PostTime")
        self.AssociateAccount = params.get("AssociateAccount")
        self.UserIp = params.get("UserIp")
        self.RiskLevel = params.get("RiskLevel")
        self.RiskType = params.get("RiskType")
        self.ConstId = params.get("ConstId")
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SponsorInfo(AbstractModel):
    """网赚防刷相关参数

    """

    def __init__(self):
        r"""
        :param SponsorOpenId: OpenID
        :type SponsorOpenId: str
        :param SponsorDeviceNumber: 设备号
        :type SponsorDeviceNumber: str
        :param SponsorPhone: 手机号
        :type SponsorPhone: str
        :param SponsorIp: IP
        :type SponsorIp: str
        :param CampaignUrl: 链接
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
        r"""
        :param WeChatOpenId: 微信的OpenID/UnionID 。
        :type WeChatOpenId: str
        :param WeChatSubType: 微信开放账号类型：
1：微信公众号/微信第三方登录。
2：微信小程序。
        :type WeChatSubType: int
        :param RandStr: 随机串。如果WeChatSubType是2，该字段必填。Token签名随机数，建议16个字符。
        :type RandStr: str
        :param WeChatAccessToken: token
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        