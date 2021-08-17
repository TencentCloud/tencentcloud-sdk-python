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


class QueryAntiFraudVipRequest(AbstractModel):
    """QueryAntiFraudVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param PhoneNumber: 电话号码(五选二)
        :type PhoneNumber: str
        :param IdNumber: Id号(五选二)
        :type IdNumber: str
        :param BankCardNumber: 银行卡号(五选二)
        :type BankCardNumber: str
        :param UserIp: 用户请求来源 IP(五选二)
        :type UserIp: str
        :param Imei: 国际移动设备识别码(五选二)
        :type Imei: str
        :param Idfa: ios 系统广告标示符(五选二)
        :type Idfa: str
        :param Scene: 业务场景 ID，需要找技术对接
        :type Scene: str
        :param Name: 姓名
        :type Name: str
        :param EmailAddress: 用户邮箱地址
        :type EmailAddress: str
        :param Address: 用户住址
        :type Address: str
        :param AccountType: 关联的腾讯帐号 QQ：1；
开放帐号微信： 2；
        :type AccountType: str
        :param Uid: 可选的 QQ 或微信 openid
        :type Uid: str
        :param AppIdU: qq 或微信分配给网站或应用的 appid，用来
唯一标识网站或应用
        :type AppIdU: str
        :param WifiMac: WIFI MAC
        :type WifiMac: str
        :param WifiSSID: WIFI 服务集标识
        :type WifiSSID: str
        :param WifiBSSID: WIFI-BSSID
        :type WifiBSSID: str
        :param BusinessId: 业务 ID，在多个业务中使用此服务，通过此
ID 区分统计数据
        :type BusinessId: str
        :param IdCryptoType: Id加密类型
0：不加密（默认值）
1：md5
2：sha256
3：SM3
        :type IdCryptoType: str
        :param PhoneCryptoType: 手机号加密类型
0：不加密（默认值）
1：md5, 2：sha256
3：SM3
        :type PhoneCryptoType: str
        :param Mac: MAC 地址
        :type Mac: str
        :param Imsi: 国际移动用户识别码
        :type Imsi: str
        :param NameCryptoType: 姓名加密类型
0：不加密（默认值）
1：md5
2：sha256
3：SM3
        :type NameCryptoType: str
        """
        self.PhoneNumber = None
        self.IdNumber = None
        self.BankCardNumber = None
        self.UserIp = None
        self.Imei = None
        self.Idfa = None
        self.Scene = None
        self.Name = None
        self.EmailAddress = None
        self.Address = None
        self.AccountType = None
        self.Uid = None
        self.AppIdU = None
        self.WifiMac = None
        self.WifiSSID = None
        self.WifiBSSID = None
        self.BusinessId = None
        self.IdCryptoType = None
        self.PhoneCryptoType = None
        self.Mac = None
        self.Imsi = None
        self.NameCryptoType = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        self.IdNumber = params.get("IdNumber")
        self.BankCardNumber = params.get("BankCardNumber")
        self.UserIp = params.get("UserIp")
        self.Imei = params.get("Imei")
        self.Idfa = params.get("Idfa")
        self.Scene = params.get("Scene")
        self.Name = params.get("Name")
        self.EmailAddress = params.get("EmailAddress")
        self.Address = params.get("Address")
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.AppIdU = params.get("AppIdU")
        self.WifiMac = params.get("WifiMac")
        self.WifiSSID = params.get("WifiSSID")
        self.WifiBSSID = params.get("WifiBSSID")
        self.BusinessId = params.get("BusinessId")
        self.IdCryptoType = params.get("IdCryptoType")
        self.PhoneCryptoType = params.get("PhoneCryptoType")
        self.Mac = params.get("Mac")
        self.Imsi = params.get("Imsi")
        self.NameCryptoType = params.get("NameCryptoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAntiFraudVipResponse(AbstractModel):
    """QueryAntiFraudVip返回参数结构体

    """

    def __init__(self):
        r"""
        :param Found: 表示该条记录能否查到：1为能查到，-1为查不到
        :type Found: int
        :param IdFound: 表示该条Id能否查到：1为能查到，-1为查不到
        :type IdFound: int
        :param RiskScore: 0~100;值越高 欺诈可能性越大
        :type RiskScore: int
        :param RiskInfo: 扩展字段，对风险类型的说明
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of RiskDetail
        :param CodeDesc: 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Found = None
        self.IdFound = None
        self.RiskScore = None
        self.RiskInfo = None
        self.CodeDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Found = params.get("Found")
        self.IdFound = params.get("IdFound")
        self.RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self.RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskDetail()
                obj._deserialize(item)
                self.RiskInfo.append(obj)
        self.CodeDesc = params.get("CodeDesc")
        self.RequestId = params.get("RequestId")


class RiskDetail(AbstractModel):
    """扩展字段，对风险类型的说明

    """

    def __init__(self):
        r"""
        :param RiskCode: 风险码
        :type RiskCode: int
        """
        self.RiskCode = None


    def _deserialize(self, params):
        self.RiskCode = params.get("RiskCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        