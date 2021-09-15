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


class DescribeAntiFraudRequest(AbstractModel):
    """DescribeAntiFraud请求参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessSecurityData: 原始业务入参(二选一）
        :type BusinessSecurityData: :class:`tencentcloud.af.v20200226.models.FinanceAntiFraudFilter`
        :param BusinessCryptoData: 密文业务入参(二选一）
        :type BusinessCryptoData: :class:`tencentcloud.af.v20200226.models.FinanceAntiFraudCryptoFilter`
        """
        self.BusinessSecurityData = None
        self.BusinessCryptoData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = FinanceAntiFraudFilter()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        if params.get("BusinessCryptoData") is not None:
            self.BusinessCryptoData = FinanceAntiFraudCryptoFilter()
            self.BusinessCryptoData._deserialize(params.get("BusinessCryptoData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiFraudResponse(AbstractModel):
    """DescribeAntiFraud返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.af.v20200226.models.FinanceAntiFraudRecord`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = FinanceAntiFraudRecord()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class FinanceAntiFraudCryptoFilter(AbstractModel):
    """借贷反欺诈密文业务入参

    """

    def __init__(self):
        r"""
        :param CryptoType: 值1定义：AES加密方式[加密模式ECB；填充格式pkcs7padding；秘钥16字节即128位
        :type CryptoType: str
        :param CryptoContent: 业务字段BusinessSecurityData的json数据格式，采用CryptoType相应的加密方式计算后得到的bash64编码内容。比如对{"PhoneNumber":"13430420001","IdNumber":"420115199501010001","BankCardNumber":"6214000100010001"}包体做加密。
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
        


class FinanceAntiFraudFilter(AbstractModel):
    """借贷反欺诈原始业务入参

    """

    def __init__(self):
        r"""
        :param PhoneNumber: 电话号码(五选二)
        :type PhoneNumber: str
        :param IdNumber: 身份证Id(五选二) 参数详细定义请加微信：TYXGJ-01
        :type IdNumber: str
        :param BankCardNumber: 银行卡号(五选二)
        :type BankCardNumber: str
        :param UserIp: 用户请求来源 IP(五选二)
        :type UserIp: str
        :param Imei: 国际移动设备识别码(五选二)
        :type Imei: str
        :param Idfa: ios 系统广告标示符(五选二)
        :type Idfa: str
        :param Scene: 业务场景ID，需要找技术对接
        :type Scene: str
        :param Name: 姓名
        :type Name: str
        :param EmailAddress: 用户邮箱地址
        :type EmailAddress: str
        :param Address: 用户住址
        :type Address: str
        :param Mac: MAC 地址
        :type Mac: str
        :param Imsi: 国际移动用户识别码
        :type Imsi: str
        :param AccountType: 1：关联的腾讯帐号QQ；2：开放帐号微信
        :type AccountType: str
        :param Uid: 可选的 QQ 或微信 openid
        :type Uid: str
        :param AppIdU: qq 或微信分配给网站或应用的 appid，用来唯一标识网站或应用
        :type AppIdU: str
        :param WifiMac: WIFI MAC
        :type WifiMac: str
        :param WifiSSID: WIFI 服务集标识
        :type WifiSSID: str
        :param WifiBSSID: WIFI-BSSID
        :type WifiBSSID: str
        :param BusinessId: 业务 ID，在多个业务中使用此服务，通过此ID 区分统计数据
        :type BusinessId: str
        :param PhoneCryptoType: 手机号加密类型 0：不加密（默认值）；1：md5；2：sha256；3：SM3
        :type PhoneCryptoType: str
        :param IdCryptoType: 身份证Id加密类型 0：不加密（默认值）；1：md5；2：sha256；3：SM3
        :type IdCryptoType: str
        :param NameCryptoType: 姓名加密类型 0：不加密（默认值）；1：md5；2：sha256；3：SM3
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
        self.Mac = None
        self.Imsi = None
        self.AccountType = None
        self.Uid = None
        self.AppIdU = None
        self.WifiMac = None
        self.WifiSSID = None
        self.WifiBSSID = None
        self.BusinessId = None
        self.PhoneCryptoType = None
        self.IdCryptoType = None
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
        self.Mac = params.get("Mac")
        self.Imsi = params.get("Imsi")
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.AppIdU = params.get("AppIdU")
        self.WifiMac = params.get("WifiMac")
        self.WifiSSID = params.get("WifiSSID")
        self.WifiBSSID = params.get("WifiBSSID")
        self.BusinessId = params.get("BusinessId")
        self.PhoneCryptoType = params.get("PhoneCryptoType")
        self.IdCryptoType = params.get("IdCryptoType")
        self.NameCryptoType = params.get("NameCryptoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanceAntiFraudRecord(AbstractModel):
    """借贷反欺查询返回结果出参

    """

    def __init__(self):
        r"""
        :param Found: 表示该条记录能否查到：1为能查到，-1为查不到
注意：此字段可能返回 null，表示取不到有效值。
        :type Found: str
        :param IdFound: 表示该条Id能否查到：1为能查到，-1为查不到
注意：此字段可能返回 null，表示取不到有效值。
        :type IdFound: str
        :param RiskScore: 评分0~100;值越高 欺诈可能性越大
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskScore: str
        :param RiskInfo: 扩展字段，对风险类型的说明
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of RiskDetailInfo
        :param OtherModelScores: 多模型返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherModelScores: list of FinanceOtherModelScores
        :param Code: 业务侧错误码。成功时返回0，错误时返回非0值
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Message: 业务侧错误信息。成功时返回Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.Found = None
        self.IdFound = None
        self.RiskScore = None
        self.RiskInfo = None
        self.OtherModelScores = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Found = params.get("Found")
        self.IdFound = params.get("IdFound")
        self.RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self.RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskDetailInfo()
                obj._deserialize(item)
                self.RiskInfo.append(obj)
        if params.get("OtherModelScores") is not None:
            self.OtherModelScores = []
            for item in params.get("OtherModelScores"):
                obj = FinanceOtherModelScores()
                obj._deserialize(item)
                self.OtherModelScores.append(obj)
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanceOtherModelScores(AbstractModel):
    """借贷反欺返回结果出参中的多模型返回结果

    """

    def __init__(self):
        r"""
        :param ModelId: 模型ID序号
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param ModelScore: 模型ID序号对应的评分结果
注意：此字段可能返回 null，表示取不到有效值。
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
        


class QueryAntiFraudRequest(AbstractModel):
    """QueryAntiFraud请求参数结构体

    """

    def __init__(self):
        r"""
        :param PhoneNumber: 电话号码(五选二)
        :type PhoneNumber: str
        :param IdNumber: Id(五选二)
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
        :param Mac: MAC 地址
        :type Mac: str
        :param Imsi: 国际移动用户识别码
        :type Imsi: str
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
        self.Mac = None
        self.Imsi = None
        self.AccountType = None
        self.Uid = None
        self.AppIdU = None
        self.WifiMac = None
        self.WifiSSID = None
        self.WifiBSSID = None
        self.BusinessId = None
        self.IdCryptoType = None
        self.PhoneCryptoType = None
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
        self.Mac = params.get("Mac")
        self.Imsi = params.get("Imsi")
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.AppIdU = params.get("AppIdU")
        self.WifiMac = params.get("WifiMac")
        self.WifiSSID = params.get("WifiSSID")
        self.WifiBSSID = params.get("WifiBSSID")
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
        


class QueryAntiFraudResponse(AbstractModel):
    """QueryAntiFraud返回参数结构体

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
        :param RiskCode: 风险码 参数详细定义请加微信：TYXGJ-01
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
        


class RiskDetailInfo(AbstractModel):
    """金融借贷反欺诈 风险码输出类型

    """

    def __init__(self):
        r"""
        :param RiskCode: 风险码
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCode: str
        :param RiskValue: 风险码对应的风险值
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskValue: str
        """
        self.RiskCode = None
        self.RiskValue = None


    def _deserialize(self, params):
        self.RiskCode = params.get("RiskCode")
        self.RiskValue = params.get("RiskValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        