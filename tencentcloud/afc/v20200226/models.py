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


class AntiFraudVipCryptoFilter(AbstractModel):
    """AntiFraudVipCryptoFilter– 业务入参

    """

    def __init__(self):
        r"""
        :param CryptoType: 约定用入参，默认不涉及默认BusinessSecurityData 与BusinessCrptoData 不传
        :type CryptoType: str
        :param CryptoContent: 约定用入参，默认不涉及
        :type CryptoContent: str
        """
        self.CryptoType = None
        self.CryptoContent = None


    def _deserialize(self, params):
        self.CryptoType = params.get("CryptoType")
        self.CryptoContent = params.get("CryptoContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AntiFraudVipFilter(AbstractModel):
    """AntiFraudVipFilter– 业务入参

    """

    def __init__(self):
        r"""
        :param CustomerUin: 业务方账号 ID
        :type CustomerUin: str
        :param CustomerAppid: 业务方APPID
        :type CustomerAppid: str
        :param IdNumber: 身份证号
注 1：下方 idCryptoType 为指定
加密方式
注 2：若 idNumber 加密则必传加
密方式
        :type IdNumber: str
        :param PhoneNumber: 手机号码（注：不需要带国家代码
例如：13430421011）
注 1：下方 phoneCryptoType 为
指定加密方式:
注 2：若 phoneNumber 加密则必
传加密方式
        :type PhoneNumber: str
        :param Scene: 业务场景 ID
        :type Scene: str
        :param CustomerSubUin: 默认不使用，业务方子
账号，若接口使用密钥对应是子账
号则必填
        :type CustomerSubUin: str
        :param Authorization: 已获取约定标识则传 1；
用于基于特定需求而传的标识字段
注：有约定则是必传，若未传则查
询接口失败
        :type Authorization: str
        :param Name: 姓名
注 ：不支持加密
        :type Name: str
        :param BankCardNumber: 银行卡号
        :type BankCardNumber: str
        :param UserIp: 用户请求来源 IP
        :type UserIp: str
        :param Imei: 国际移动设备识别码
        :type Imei: str
        :param Idfa: ios 系统广告标示符
        :type Idfa: str
        :param EmailAddress: 用户邮箱地址
        :type EmailAddress: str
        :param Address: 用户住址
        :type Address: str
        :param Mac: MAC 地址
        :type Mac: str
        :param Imsi: 国际移动用户识别码
        :type Imsi: str
        :param AccountType: 关联的腾讯帐号 QQ：1；
开放帐号微信： 2；
        :type AccountType: str
        :param Uid: 可选的 QQ 或微信 openid
        :type Uid: str
        :param AppIdU: qq 或微信分配给网站或应用的
appid，用来唯一标识网站或应用
        :type AppIdU: str
        :param WifiMac: ＷＩＦＩＭＡＣ
        :type WifiMac: str
        :param WifiSSID: WIFI 服务集标识
        :type WifiSSID: str
        :param WifiBSSID: WIFI-BSSID
        :type WifiBSSID: str
        :param ExtensionId: 拓展字段类型 ID
注：默认不填写，需要时天御侧将
提供
        :type ExtensionId: str
        :param ExtensionIn: 拓展字段内容
注：默认不填，需要时天御侧将提
供
        :type ExtensionIn: str
        :param BusinessId: 业务 ID，默认不传
        :type BusinessId: str
        :param IdCryptoType: 身份证加密类型
0：不加密（默认值）
1：md5
2：sha256
3：SM3
注：若 idNumber 加密则必传加密
方式
        :type IdCryptoType: str
        :param PhoneCryptoType: 手机号加密类型
0：不加密（默认值）
1：md5,
2：sha256
3：SM3
注：若 phoneNumber 加密则必传
加密方式
        :type PhoneCryptoType: str
        :param NameCryptoType: 姓名加密类型：——注：已经不支持加
密，该字段存在是为了兼容可能历史客户
版本；
0：不加密（默认值）
1：md5
        :type NameCryptoType: str
        """
        self.CustomerUin = None
        self.CustomerAppid = None
        self.IdNumber = None
        self.PhoneNumber = None
        self.Scene = None
        self.CustomerSubUin = None
        self.Authorization = None
        self.Name = None
        self.BankCardNumber = None
        self.UserIp = None
        self.Imei = None
        self.Idfa = None
        self.EmailAddress = None
        self.Address = None
        self.Mac = None
        self.Imsi = None
        self.AccountType = None
        self.Uid = None
        self.AppIdU = None
        self.WifiMac = None
        self.WifiSSID = None
        self.WifiBSSID = None
        self.ExtensionId = None
        self.ExtensionIn = None
        self.BusinessId = None
        self.IdCryptoType = None
        self.PhoneCryptoType = None
        self.NameCryptoType = None


    def _deserialize(self, params):
        self.CustomerUin = params.get("CustomerUin")
        self.CustomerAppid = params.get("CustomerAppid")
        self.IdNumber = params.get("IdNumber")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Scene = params.get("Scene")
        self.CustomerSubUin = params.get("CustomerSubUin")
        self.Authorization = params.get("Authorization")
        self.Name = params.get("Name")
        self.BankCardNumber = params.get("BankCardNumber")
        self.UserIp = params.get("UserIp")
        self.Imei = params.get("Imei")
        self.Idfa = params.get("Idfa")
        self.EmailAddress = params.get("EmailAddress")
        self.Address = params.get("Address")
        self.Mac = params.get("Mac")
        self.Imsi = params.get("Imsi")
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.AppIdU = params.get("AppIdU")
        self.WifiMac = params.get("WifiMac")
        self.WifiSSID = params.get("WifiSSID")
        self.WifiBSSID = params.get("WifiBSSID")
        self.ExtensionId = params.get("ExtensionId")
        self.ExtensionIn = params.get("ExtensionIn")
        self.BusinessId = params.get("BusinessId")
        self.IdCryptoType = params.get("IdCryptoType")
        self.PhoneCryptoType = params.get("PhoneCryptoType")
        self.NameCryptoType = params.get("NameCryptoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AntiFraudVipRecord(AbstractModel):
    """反欺诈VIP查询结果

    """

    def __init__(self):
        r"""
        :param Code: 公共错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param CodeDesc: 业务侧错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param Message: 业务侧错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Found: 表示该条记录能否查到：1 为能查到；-1 为查不到，此时 RiskScore 返回-1；
注意：此字段可能返回 null，表示取不到有效值。
        :type Found: str
        :param IdFound: 表示该条记录中的身份 ID 能否查到
1 为能查到
-1 为查不到
注意：此字段可能返回 null，表示取不到有效值。
        :type IdFound: str
        :param RiskScore: 当可查到时，返回 0~100 区间，值越高 欺诈可
能性越大。
当查不到时（即 found=-1），返回-1
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskScore: str
        :param RiskInfo: 扩展字段，对风险类型的说明。扩展字段并非必
然出现。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of SimpleKindRiskDetail
        :param OtherModelScores: 默认出现，提供模型版本号说明及多模型返回需
要时用到；
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherModelScores: list of OtherModelScores
        :param PostTime: 表示请求时间，标准 sunix 时间戳，非必然出现
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: str
        :param ExtensionOut: 拓展字段，非必然出现，和 ExtensionIn 对应；
注：非必然出现，需要返回时天御侧将说明；
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionOut: str
        """
        self.Code = None
        self.CodeDesc = None
        self.Message = None
        self.Found = None
        self.IdFound = None
        self.RiskScore = None
        self.RiskInfo = None
        self.OtherModelScores = None
        self.PostTime = None
        self.ExtensionOut = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.CodeDesc = params.get("CodeDesc")
        self.Message = params.get("Message")
        self.Found = params.get("Found")
        self.IdFound = params.get("IdFound")
        self.RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self.RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = SimpleKindRiskDetail()
                obj._deserialize(item)
                self.RiskInfo.append(obj)
        if params.get("OtherModelScores") is not None:
            self.OtherModelScores = []
            for item in params.get("OtherModelScores"):
                obj = OtherModelScores()
                obj._deserialize(item)
                self.OtherModelScores.append(obj)
        self.PostTime = params.get("PostTime")
        self.ExtensionOut = params.get("ExtensionOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAntiFraudVipRequest(AbstractModel):
    """GetAntiFraudVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessSecurityData: 默认不传，约定用原始业务
入参(二选一BusinessSecurityData 或
BusinessCryptoData)。
        :type BusinessSecurityData: :class:`tencentcloud.afc.v20200226.models.AntiFraudVipFilter`
        :param BusinessCryptoData: 默认不传，约定用密文业务
入参(二选一
BusinessSecurityData 或
BusinessCryptoData)。
        :type BusinessCryptoData: :class:`tencentcloud.afc.v20200226.models.AntiFraudVipCryptoFilter`
        """
        self.BusinessSecurityData = None
        self.BusinessCryptoData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = AntiFraudVipFilter()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        if params.get("BusinessCryptoData") is not None:
            self.BusinessCryptoData = AntiFraudVipCryptoFilter()
            self.BusinessCryptoData._deserialize(params.get("BusinessCryptoData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAntiFraudVipResponse(AbstractModel):
    """GetAntiFraudVip返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 反欺诈评分接口结果
        :type Data: :class:`tencentcloud.afc.v20200226.models.AntiFraudVipRecord`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AntiFraudVipRecord()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class OtherModelScores(AbstractModel):
    """扩展字段，包含多个模型的结果

    """

    def __init__(self):
        r"""
        :param ModelId: 模型类型
        :type ModelId: str
        :param ModelScore: 该模型评分
        :type ModelScore: str
        """
        self.ModelId = None
        self.ModelScore = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ModelScore = params.get("ModelScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class SimpleKindRiskDetail(AbstractModel):
    """扩展字段，对风险类型的说明

    """

    def __init__(self):
        r"""
        :param RiskCode: 风险码
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCode: str
        :param RiskCodeValue: 风险码详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCodeValue: str
        """
        self.RiskCode = None
        self.RiskCodeValue = None


    def _deserialize(self, params):
        self.RiskCode = params.get("RiskCode")
        self.RiskCodeValue = params.get("RiskCodeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        