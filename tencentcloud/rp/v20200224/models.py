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
        """
        :param RegisterIp: 注册来源的外网 IP。\n        :type RegisterIp: str\n        :param Uid: 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。\n        :type Uid: str\n        :param RegisterTime: 注册时间戳，单位：秒。\n        :type RegisterTime: str\n        :param AccountType: 用户账号类型（QQ 开放帐号、微信开放账号需要 提交工单 由腾讯云进行资格审核）：
1：QQ 开放帐号。
2：微信开放账号。
4：手机号。
0：其他。
10004：手机号 MD5。\n        :type AccountType: str\n        :param AppIdU: accountType 是 QQ 或微信开放账号时，该参数必填，表示 QQ 或微信分配给网站或应用的 AppID，用来唯一标识网站或应用。\n        :type AppIdU: str\n        :param AssociateAccount: accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。\n        :type AssociateAccount: str\n        :param NickName: 昵称，UTF-8 编码。\n        :type NickName: str\n        :param PhoneNumber: 手机号：国家代码-手机号， 如0086-15912345687（0086前不需要+号）。\n        :type PhoneNumber: str\n        :param EmailAddress: 用户邮箱地址（非系统自动生成）。\n        :type EmailAddress: str\n        :param Address: 地址。\n        :type Address: str\n        :param CookieHash: 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。\n        :type CookieHash: str\n        :param RegisterSource: 注册来源：
0：其他。
1：PC 网页。
2：移动页面。
3：App。
4：微信公众号。\n        :type RegisterSource: str\n        :param Referer: 用户 HTTP 请求的 referer 值。\n        :type Referer: str\n        :param JumpUrl: 注册成功后跳转页面。\n        :type JumpUrl: str\n        :param UserAgent: 用户 HTTP 请求的 userAgent。\n        :type UserAgent: str\n        :param XForwardedFor: 用户 HTTP 请求中的 x_forward_for。\n        :type XForwardedFor: str\n        :param MouseClickCount: 用户操作过程中鼠标单击次数。\n        :type MouseClickCount: str\n        :param KeyboardClickCount: 用户操作过程中键盘单击次数。\n        :type KeyboardClickCount: str\n        :param Result: 注册结果：
0：失败。
1：成功。\n        :type Result: str\n        :param Reason: 失败原因：
0：其他。
1：参数错误。
2：帐号冲突。
3：验证错误。\n        :type Reason: str\n        :param RegisterSpend: 登录耗时，单位：秒。\n        :type RegisterSpend: str\n        :param MacAddress: MAC 地址或设备唯一标识。\n        :type MacAddress: str\n        :param VendorId: 手机制造商 ID，如果手机注册，请带上此信息。\n        :type VendorId: str\n        :param AppVersion: App 客户端版本。\n        :type AppVersion: str\n        :param Imei: 手机设备号。\n        :type Imei: str\n        :param BusinessId: 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。\n        :type BusinessId: str\n        :param WxSubType: 1：微信公众号。
2：微信小程序。\n        :type WxSubType: str\n        :param RandNum: Token 签名随机数，微信小程序必填，建议16个字符。\n        :type RandNum: str\n        :param WxToken: 如果是微信小程序，该字段为以 ssesion_key 为 key 去签名随机数 radnNum 得到的值（hmac_sha256签名算法）。
如果是微信公众号或第三方登录，则为授权的 access_token（注意：不是普通 access_token，具体看 微信官方文档）。\n        :type WxToken: str\n        """
        self.RegisterIp = None
        self.Uid = None
        self.RegisterTime = None
        self.AccountType = None
        self.AppIdU = None
        self.AssociateAccount = None
        self.NickName = None
        self.PhoneNumber = None
        self.EmailAddress = None
        self.Address = None
        self.CookieHash = None
        self.RegisterSource = None
        self.Referer = None
        self.JumpUrl = None
        self.UserAgent = None
        self.XForwardedFor = None
        self.MouseClickCount = None
        self.KeyboardClickCount = None
        self.Result = None
        self.Reason = None
        self.RegisterSpend = None
        self.MacAddress = None
        self.VendorId = None
        self.AppVersion = None
        self.Imei = None
        self.BusinessId = None
        self.WxSubType = None
        self.RandNum = None
        self.WxToken = None


    def _deserialize(self, params):
        self.RegisterIp = params.get("RegisterIp")
        self.Uid = params.get("Uid")
        self.RegisterTime = params.get("RegisterTime")
        self.AccountType = params.get("AccountType")
        self.AppIdU = params.get("AppIdU")
        self.AssociateAccount = params.get("AssociateAccount")
        self.NickName = params.get("NickName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.EmailAddress = params.get("EmailAddress")
        self.Address = params.get("Address")
        self.CookieHash = params.get("CookieHash")
        self.RegisterSource = params.get("RegisterSource")
        self.Referer = params.get("Referer")
        self.JumpUrl = params.get("JumpUrl")
        self.UserAgent = params.get("UserAgent")
        self.XForwardedFor = params.get("XForwardedFor")
        self.MouseClickCount = params.get("MouseClickCount")
        self.KeyboardClickCount = params.get("KeyboardClickCount")
        self.Result = params.get("Result")
        self.Reason = params.get("Reason")
        self.RegisterSpend = params.get("RegisterSpend")
        self.MacAddress = params.get("MacAddress")
        self.VendorId = params.get("VendorId")
        self.AppVersion = params.get("AppVersion")
        self.Imei = params.get("Imei")
        self.BusinessId = params.get("BusinessId")
        self.WxSubType = params.get("WxSubType")
        self.RandNum = params.get("RandNum")
        self.WxToken = params.get("WxToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRegisterProtectionResponse(AbstractModel):
    """QueryRegisterProtection返回参数结构体

    """

    def __init__(self):
        """
        :param CodeDesc: 业务侧错误码，成功时返回 Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CodeDesc: str\n        :param AssociateAccount: accountType 是 QQ 或微信开放账号时，用于标识 QQ 或微信用户登录后关联业务自身的账号 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssociateAccount: str\n        :param RegisterTime: 注册时间戳，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegisterTime: str\n        :param Uid: 用户 ID 不同的 accountType 对应不同的用户 ID。如果是 QQ，则填入对应的 openid，微信用户则填入对应的 openid/unionid，手机号则填入对应真实用户手机号（如13123456789）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uid: str\n        :param RegisterIp: 注册来源的外网 IP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegisterIp: str\n        :param Level: 0：表示无恶意。
1 - 4：恶意等级由低到高。\n        :type Level: int\n        :param RiskType: 风险类型。\n        :type RiskType: list of int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CodeDesc = None
        self.AssociateAccount = None
        self.RegisterTime = None
        self.Uid = None
        self.RegisterIp = None
        self.Level = None
        self.RiskType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeDesc = params.get("CodeDesc")
        self.AssociateAccount = params.get("AssociateAccount")
        self.RegisterTime = params.get("RegisterTime")
        self.Uid = params.get("Uid")
        self.RegisterIp = params.get("RegisterIp")
        self.Level = params.get("Level")
        self.RiskType = params.get("RiskType")
        self.RequestId = params.get("RequestId")