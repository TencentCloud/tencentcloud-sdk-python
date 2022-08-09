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
        :param AccountType: 账号类型
        :type AccountType: str
        :param Uid: uid值
        :type Uid: str
        :param UserIp: 用户的真实外网 IP。若填入非外网有效ip，会返回level=0的风控结果，risktype中会有205的风险码返回作为标识
        :type UserIp: str
        :param PostTime: 用户操作时间戳。
        :type PostTime: str
        :param AppIdU: accountType 是QQ开放账号时，该参数必填，表示 QQ 开放平台分配给网站或应用的 AppID，用来唯一标识网站或应用。
        :type AppIdU: str
        :param NickName: 昵称，UTF-8 编码。
        :type NickName: str
        :param PhoneNumber: 手机号
        :type PhoneNumber: str
        :param EmailAddress: 用户邮箱地址。
        :type EmailAddress: str
        :param RegisterTime: 注册时间戳。
        :type RegisterTime: str
        :param RegisterIp: 注册来源的外网 IP。
        :type RegisterIp: str
        :param CookieHash: 用户 HTTP 请求中的 cookie 进行2次 hash 的值，只要保证相同 cookie 的 hash 值一致即可。
        :type CookieHash: str
        :param Address: 地址。
        :type Address: str
        :param LoginSource: 登录来源：
0：其他。
1：PC 网页。
2：移动页面。
3：App。
4：微信公众号。
        :type LoginSource: str
        :param LoginType: 登录方式：
0：其他。
1：手动账号密码输入。
2：动态短信密码登录。
3：二维码扫描登录。
        :type LoginType: str
        :param LoginSpend: 登录耗时，单位：秒。
        :type LoginSpend: str
        :param RootId: 用户操作的目的 ID，如点赞等，该字段就是被点赞的消息 ID，如果是投票，则为被投号码的 ID。
        :type RootId: str
        :param Referer: 用户 HTTP 请求的 referer 值。
        :type Referer: str
        :param JumpUrl: 登录成功后跳转页面。
        :type JumpUrl: str
        :param UserAgent: 用户 HTTP 请求的 userAgent。
        :type UserAgent: str
        :param XForwardedFor: 用户 HTTP 请求中的 x_forward_for。
        :type XForwardedFor: str
        :param MouseClickCount: 用户操作过程中鼠标单击次数。
        :type MouseClickCount: str
        :param KeyboardClickCount: 用户操作过程中键盘单击次数。
        :type KeyboardClickCount: str
        :param MacAddress: MAC 地址或设备唯一标识。
        :type MacAddress: str
        :param VendorId: 手机制造商 ID，如果手机注册，请带上此信息。
        :type VendorId: str
        :param Imei: 手机设备号。支持以下格式：
1.imei明文
2.idfa明文,
3.imei小写后MD5值小写
4.idfa大写后MD5值小写
        :type Imei: str
        :param AppVersion: App 客户端版本。
        :type AppVersion: str
        :param BusinessId: 业务 ID 网站或应用在多个业务中使用此服务，通过此 ID 区分统计数据。
        :type BusinessId: str
        :param WxSubType: 1：微信公众号。
2：微信小程序。
        :type WxSubType: str
        :param RandNum: Token 签名随机数，WxSubType为微信小程序时必填，建议16个字符。
        :type RandNum: str
        :param WxToken: token
        :type WxToken: str
        :param CheckDevice: 是否识别设备异常：
0：不识别。
1：识别。
        :type CheckDevice: str
        """
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
        r"""
        :param PostTime: 操作时间戳，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: str
        :param UserIp: 用户操作的真实外网 IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param Level: 0：表示无恶意。
1 - 4：恶意等级由低到高。
        :type Level: int
        :param RiskType: 风险类型。

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
        :param AssociateAccount: accountType是QQ或微信开放账号时，用于标识QQ或微信用户登录后关联业务自身的账号ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param Uid: uid值
注意：此字段可能返回 null，表示取不到有效值。
        :type Uid: str
        :param RootId: 用户操作的目的ID 
比如：点赞，该字段就是被点 赞的消息 id，如果是投票，就是被投号码的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RootId: str
        :param CodeDesc: 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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