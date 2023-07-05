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


class AntiFraudCryptoFilter(AbstractModel):
    """AntiFraudCryptoFilter – 业务入参

    """

    def __init__(self):
        r"""
        :param _CryptoType: 约定用入参，默认不涉及默认BusinessSecurityData 与BusinessCrptoData 不传
        :type CryptoType: str
        :param _CryptoContent: 约定用入参，默认不涉及
        :type CryptoContent: str
        """
        self._CryptoType = None
        self._CryptoContent = None

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
        self._CryptoType = params.get("CryptoType")
        self._CryptoContent = params.get("CryptoContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AntiFraudFilter(AbstractModel):
    """AntiFraudFilter – 业务入参

    """

    def __init__(self):
        r"""
        :param _CustomerUin: 业务方账号 ID
        :type CustomerUin: str
        :param _CustomerAppid: 业务方APPID
        :type CustomerAppid: str
        :param _IdNumber: 身份证号
注 1：下方 idCryptoType 为指定
加密方式
注 2：若 idNumber 加密则必传加
密方式
        :type IdNumber: str
        :param _PhoneNumber: 手机号码（注：不需要带国家代码
例如：13430421011）
注 1：下方 phoneCryptoType 为
指定加密方式:
注 2：若 phoneNumber 加密则必
传加密方式
        :type PhoneNumber: str
        :param _Scene: 业务场景 ID
        :type Scene: str
        :param _CustomerSubUin: 默认不使用，业务方子
账号，若接口使用密钥对应是子账
号则必填
        :type CustomerSubUin: str
        :param _Authorization: 已获取约定标识则传 1；
用于基于特定需求而传的标识字段
注：有约定则是必传，若未传则查
询接口失败
        :type Authorization: str
        :param _Name: 姓名
注 ：不支持加密
        :type Name: str
        :param _BankCardNumber: 银行卡号
        :type BankCardNumber: str
        :param _UserIp: 用户请求来源 IP
        :type UserIp: str
        :param _Imei: 国际移动设备识别码
        :type Imei: str
        :param _Idfa: ios 系统广告标示符
        :type Idfa: str
        :param _EmailAddress: 用户邮箱地址
        :type EmailAddress: str
        :param _Address: 用户住址
        :type Address: str
        :param _Mac: MAC 地址
        :type Mac: str
        :param _Imsi: 国际移动用户识别码
        :type Imsi: str
        :param _AccountType: 关联的腾讯帐号 QQ：1；
开放帐号微信： 2；
        :type AccountType: str
        :param _Uid: 可选的 QQ 或微信 openid
        :type Uid: str
        :param _AppIdU: qq 或微信分配给网站或应用的
appid，用来唯一标识网站或应用
        :type AppIdU: str
        :param _WifiMac: ＷＩＦＩＭＡＣ
        :type WifiMac: str
        :param _WifiSSID: WIFI 服务集标识
        :type WifiSSID: str
        :param _WifiBSSID: WIFI-BSSID
        :type WifiBSSID: str
        :param _ExtensionId: 拓展字段类型 ID
注：默认不填写，需要时天御侧将
提供
        :type ExtensionId: str
        :param _ExtensionIn: 拓展字段内容
注：默认不填，需要时天御侧将提
供
        :type ExtensionIn: str
        :param _BusinessId: 业务 ID，默认不传
        :type BusinessId: str
        :param _IdCryptoType: 身份证加密类型
0：不加密（默认值）
1：md5
2：sha256
3：SM3
注：若 idNumber 加密则必传加密
方式
        :type IdCryptoType: str
        :param _PhoneCryptoType: 手机号加密类型
0：不加密（默认值）
1：md5,
2：sha256
3：SM3
注：若 phoneNumber 加密则必传
加密方式
        :type PhoneCryptoType: str
        :param _NameCryptoType: 姓名加密类型：——注：已经不支持加
密，该字段存在是为了兼容可能历史客户
版本；
0：不加密（默认值）
1：md5
        :type NameCryptoType: str
        :param _OldResponseType: 是否使用旧回包
        :type OldResponseType: str
        """
        self._CustomerUin = None
        self._CustomerAppid = None
        self._IdNumber = None
        self._PhoneNumber = None
        self._Scene = None
        self._CustomerSubUin = None
        self._Authorization = None
        self._Name = None
        self._BankCardNumber = None
        self._UserIp = None
        self._Imei = None
        self._Idfa = None
        self._EmailAddress = None
        self._Address = None
        self._Mac = None
        self._Imsi = None
        self._AccountType = None
        self._Uid = None
        self._AppIdU = None
        self._WifiMac = None
        self._WifiSSID = None
        self._WifiBSSID = None
        self._ExtensionId = None
        self._ExtensionIn = None
        self._BusinessId = None
        self._IdCryptoType = None
        self._PhoneCryptoType = None
        self._NameCryptoType = None
        self._OldResponseType = None

    @property
    def CustomerUin(self):
        return self._CustomerUin

    @CustomerUin.setter
    def CustomerUin(self, CustomerUin):
        self._CustomerUin = CustomerUin

    @property
    def CustomerAppid(self):
        return self._CustomerAppid

    @CustomerAppid.setter
    def CustomerAppid(self, CustomerAppid):
        self._CustomerAppid = CustomerAppid

    @property
    def IdNumber(self):
        return self._IdNumber

    @IdNumber.setter
    def IdNumber(self, IdNumber):
        self._IdNumber = IdNumber

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def CustomerSubUin(self):
        return self._CustomerSubUin

    @CustomerSubUin.setter
    def CustomerSubUin(self, CustomerSubUin):
        self._CustomerSubUin = CustomerSubUin

    @property
    def Authorization(self):
        return self._Authorization

    @Authorization.setter
    def Authorization(self, Authorization):
        self._Authorization = Authorization

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BankCardNumber(self):
        return self._BankCardNumber

    @BankCardNumber.setter
    def BankCardNumber(self, BankCardNumber):
        self._BankCardNumber = BankCardNumber

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Idfa(self):
        return self._Idfa

    @Idfa.setter
    def Idfa(self, Idfa):
        self._Idfa = Idfa

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
    def Mac(self):
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def Imsi(self):
        return self._Imsi

    @Imsi.setter
    def Imsi(self, Imsi):
        self._Imsi = Imsi

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
    def AppIdU(self):
        return self._AppIdU

    @AppIdU.setter
    def AppIdU(self, AppIdU):
        self._AppIdU = AppIdU

    @property
    def WifiMac(self):
        return self._WifiMac

    @WifiMac.setter
    def WifiMac(self, WifiMac):
        self._WifiMac = WifiMac

    @property
    def WifiSSID(self):
        return self._WifiSSID

    @WifiSSID.setter
    def WifiSSID(self, WifiSSID):
        self._WifiSSID = WifiSSID

    @property
    def WifiBSSID(self):
        return self._WifiBSSID

    @WifiBSSID.setter
    def WifiBSSID(self, WifiBSSID):
        self._WifiBSSID = WifiBSSID

    @property
    def ExtensionId(self):
        return self._ExtensionId

    @ExtensionId.setter
    def ExtensionId(self, ExtensionId):
        self._ExtensionId = ExtensionId

    @property
    def ExtensionIn(self):
        return self._ExtensionIn

    @ExtensionIn.setter
    def ExtensionIn(self, ExtensionIn):
        self._ExtensionIn = ExtensionIn

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def IdCryptoType(self):
        return self._IdCryptoType

    @IdCryptoType.setter
    def IdCryptoType(self, IdCryptoType):
        self._IdCryptoType = IdCryptoType

    @property
    def PhoneCryptoType(self):
        return self._PhoneCryptoType

    @PhoneCryptoType.setter
    def PhoneCryptoType(self, PhoneCryptoType):
        self._PhoneCryptoType = PhoneCryptoType

    @property
    def NameCryptoType(self):
        return self._NameCryptoType

    @NameCryptoType.setter
    def NameCryptoType(self, NameCryptoType):
        self._NameCryptoType = NameCryptoType

    @property
    def OldResponseType(self):
        return self._OldResponseType

    @OldResponseType.setter
    def OldResponseType(self, OldResponseType):
        self._OldResponseType = OldResponseType


    def _deserialize(self, params):
        self._CustomerUin = params.get("CustomerUin")
        self._CustomerAppid = params.get("CustomerAppid")
        self._IdNumber = params.get("IdNumber")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Scene = params.get("Scene")
        self._CustomerSubUin = params.get("CustomerSubUin")
        self._Authorization = params.get("Authorization")
        self._Name = params.get("Name")
        self._BankCardNumber = params.get("BankCardNumber")
        self._UserIp = params.get("UserIp")
        self._Imei = params.get("Imei")
        self._Idfa = params.get("Idfa")
        self._EmailAddress = params.get("EmailAddress")
        self._Address = params.get("Address")
        self._Mac = params.get("Mac")
        self._Imsi = params.get("Imsi")
        self._AccountType = params.get("AccountType")
        self._Uid = params.get("Uid")
        self._AppIdU = params.get("AppIdU")
        self._WifiMac = params.get("WifiMac")
        self._WifiSSID = params.get("WifiSSID")
        self._WifiBSSID = params.get("WifiBSSID")
        self._ExtensionId = params.get("ExtensionId")
        self._ExtensionIn = params.get("ExtensionIn")
        self._BusinessId = params.get("BusinessId")
        self._IdCryptoType = params.get("IdCryptoType")
        self._PhoneCryptoType = params.get("PhoneCryptoType")
        self._NameCryptoType = params.get("NameCryptoType")
        self._OldResponseType = params.get("OldResponseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AntiFraudRecord(AbstractModel):
    """反欺诈查询结果

    """

    def __init__(self):
        r"""
        :param _Code: 公共错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _CodeDesc: 业务侧错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param _Message: 业务侧错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Found: 表示该条记录能否查到：1 为能查到；-1 为查不到，此时 RiskScore 返回-1；
注意：此字段可能返回 null，表示取不到有效值。
        :type Found: str
        :param _IdFound: 表示该条记录中的身份 ID 能否查到
1 为能查到
-1 为查不到
注意：此字段可能返回 null，表示取不到有效值。
        :type IdFound: str
        :param _RiskScore: 当可查到时，返回 0~100 区间，值越高 欺诈可
能性越大。
当查不到时（即 found=-1），返回-1
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskScore: str
        :param _RiskInfo: 扩展字段，对风险类型的说明。扩展字段并非必
然出现。
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of SimpleKindRiskDetail
        :param _OtherModelScores: 默认出现，提供模型版本号说明及多模型返回需
要时用到；
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherModelScores: list of OtherModelScoresDetail
        :param _PostTime: 表示请求时间，标准 sunix 时间戳，非必然出现
注意：此字段可能返回 null，表示取不到有效值。
        :type PostTime: str
        :param _ExtensionOut: 拓展字段，非必然出现，和 ExtensionIn 对应；
注：非必然出现，需要返回时天御侧将说明；
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionOut: str
        """
        self._Code = None
        self._CodeDesc = None
        self._Message = None
        self._Found = None
        self._IdFound = None
        self._RiskScore = None
        self._RiskInfo = None
        self._OtherModelScores = None
        self._PostTime = None
        self._ExtensionOut = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeDesc(self):
        return self._CodeDesc

    @CodeDesc.setter
    def CodeDesc(self, CodeDesc):
        self._CodeDesc = CodeDesc

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Found(self):
        return self._Found

    @Found.setter
    def Found(self, Found):
        self._Found = Found

    @property
    def IdFound(self):
        return self._IdFound

    @IdFound.setter
    def IdFound(self, IdFound):
        self._IdFound = IdFound

    @property
    def RiskScore(self):
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskInfo(self):
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

    @property
    def OtherModelScores(self):
        return self._OtherModelScores

    @OtherModelScores.setter
    def OtherModelScores(self, OtherModelScores):
        self._OtherModelScores = OtherModelScores

    @property
    def PostTime(self):
        return self._PostTime

    @PostTime.setter
    def PostTime(self, PostTime):
        self._PostTime = PostTime

    @property
    def ExtensionOut(self):
        return self._ExtensionOut

    @ExtensionOut.setter
    def ExtensionOut(self, ExtensionOut):
        self._ExtensionOut = ExtensionOut


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._CodeDesc = params.get("CodeDesc")
        self._Message = params.get("Message")
        self._Found = params.get("Found")
        self._IdFound = params.get("IdFound")
        self._RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self._RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = SimpleKindRiskDetail()
                obj._deserialize(item)
                self._RiskInfo.append(obj)
        if params.get("OtherModelScores") is not None:
            self._OtherModelScores = []
            for item in params.get("OtherModelScores"):
                obj = OtherModelScoresDetail()
                obj._deserialize(item)
                self._OtherModelScores.append(obj)
        self._PostTime = params.get("PostTime")
        self._ExtensionOut = params.get("ExtensionOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiFraudRequest(AbstractModel):
    """DescribeAntiFraud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 原始业务入参(二选一）
        :type BusinessSecurityData: :class:`tencentcloud.af.v20200226.models.FinanceAntiFraudFilter`
        :param _BusinessCryptoData: 密文业务入参(二选一）
        :type BusinessCryptoData: :class:`tencentcloud.af.v20200226.models.FinanceAntiFraudCryptoFilter`
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
            self._BusinessSecurityData = FinanceAntiFraudFilter()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        if params.get("BusinessCryptoData") is not None:
            self._BusinessCryptoData = FinanceAntiFraudCryptoFilter()
            self._BusinessCryptoData._deserialize(params.get("BusinessCryptoData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAntiFraudResponse(AbstractModel):
    """DescribeAntiFraud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.af.v20200226.models.FinanceAntiFraudRecord`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
            self._Data = FinanceAntiFraudRecord()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class FinanceAntiFraudCryptoFilter(AbstractModel):
    """借贷反欺诈密文业务入参

    """

    def __init__(self):
        r"""
        :param _CryptoType: 值1定义：AES加密方式[加密模式ECB；填充格式pkcs7padding；秘钥16字节即128位
        :type CryptoType: str
        :param _CryptoContent: 业务字段BusinessSecurityData的json数据格式，采用CryptoType相应的加密方式计算后得到的bash64编码内容。比如对{"PhoneNumber":"13430420001","IdNumber":"420115199501010001","BankCardNumber":"6214000100010001"}包体做加密。
        :type CryptoContent: str
        """
        self._CryptoType = None
        self._CryptoContent = None

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
        self._CryptoType = params.get("CryptoType")
        self._CryptoContent = params.get("CryptoContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanceAntiFraudFilter(AbstractModel):
    """借贷反欺诈原始业务入参

    """

    def __init__(self):
        r"""
        :param _PhoneNumber: 电话号码(五选二)
        :type PhoneNumber: str
        :param _IdNumber: 身份证Id(五选二) 参数详细定义请加微信：TYXGJ-01
        :type IdNumber: str
        :param _BankCardNumber: 银行卡号(五选二)
        :type BankCardNumber: str
        :param _UserIp: 用户请求来源 IP(五选二)
        :type UserIp: str
        :param _Imei: 国际移动设备识别码(五选二)
        :type Imei: str
        :param _Idfa: ios 系统广告标示符(五选二)
        :type Idfa: str
        :param _Scene: 业务场景ID，需要找技术对接
        :type Scene: str
        :param _Name: 姓名
        :type Name: str
        :param _EmailAddress: 用户邮箱地址
        :type EmailAddress: str
        :param _Address: 用户住址
        :type Address: str
        :param _Mac: MAC 地址
        :type Mac: str
        :param _Imsi: 国际移动用户识别码
        :type Imsi: str
        :param _AccountType: 1：关联的腾讯帐号QQ；2：开放帐号微信
        :type AccountType: str
        :param _Uid: 可选的 QQ 或微信 openid
        :type Uid: str
        :param _AppIdU: qq 或微信分配给网站或应用的 appid，用来唯一标识网站或应用
        :type AppIdU: str
        :param _WifiMac: WIFI MAC
        :type WifiMac: str
        :param _WifiSSID: WIFI 服务集标识
        :type WifiSSID: str
        :param _WifiBSSID: WIFI-BSSID
        :type WifiBSSID: str
        :param _BusinessId: 业务 ID，在多个业务中使用此服务，通过此ID 区分统计数据
        :type BusinessId: str
        :param _PhoneCryptoType: 手机号加密类型 0：不加密（默认值）；1：md5；2：sha256；3：SM3
        :type PhoneCryptoType: str
        :param _IdCryptoType: 身份证Id加密类型 0：不加密（默认值）；1：md5；2：sha256；3：SM3
        :type IdCryptoType: str
        :param _NameCryptoType: 姓名加密类型 0：不加密（默认值）；1：md5；2：sha256；3：SM3
        :type NameCryptoType: str
        """
        self._PhoneNumber = None
        self._IdNumber = None
        self._BankCardNumber = None
        self._UserIp = None
        self._Imei = None
        self._Idfa = None
        self._Scene = None
        self._Name = None
        self._EmailAddress = None
        self._Address = None
        self._Mac = None
        self._Imsi = None
        self._AccountType = None
        self._Uid = None
        self._AppIdU = None
        self._WifiMac = None
        self._WifiSSID = None
        self._WifiBSSID = None
        self._BusinessId = None
        self._PhoneCryptoType = None
        self._IdCryptoType = None
        self._NameCryptoType = None

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def IdNumber(self):
        return self._IdNumber

    @IdNumber.setter
    def IdNumber(self, IdNumber):
        self._IdNumber = IdNumber

    @property
    def BankCardNumber(self):
        return self._BankCardNumber

    @BankCardNumber.setter
    def BankCardNumber(self, BankCardNumber):
        self._BankCardNumber = BankCardNumber

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Idfa(self):
        return self._Idfa

    @Idfa.setter
    def Idfa(self, Idfa):
        self._Idfa = Idfa

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Mac(self):
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def Imsi(self):
        return self._Imsi

    @Imsi.setter
    def Imsi(self, Imsi):
        self._Imsi = Imsi

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
    def AppIdU(self):
        return self._AppIdU

    @AppIdU.setter
    def AppIdU(self, AppIdU):
        self._AppIdU = AppIdU

    @property
    def WifiMac(self):
        return self._WifiMac

    @WifiMac.setter
    def WifiMac(self, WifiMac):
        self._WifiMac = WifiMac

    @property
    def WifiSSID(self):
        return self._WifiSSID

    @WifiSSID.setter
    def WifiSSID(self, WifiSSID):
        self._WifiSSID = WifiSSID

    @property
    def WifiBSSID(self):
        return self._WifiBSSID

    @WifiBSSID.setter
    def WifiBSSID(self, WifiBSSID):
        self._WifiBSSID = WifiBSSID

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def PhoneCryptoType(self):
        return self._PhoneCryptoType

    @PhoneCryptoType.setter
    def PhoneCryptoType(self, PhoneCryptoType):
        self._PhoneCryptoType = PhoneCryptoType

    @property
    def IdCryptoType(self):
        return self._IdCryptoType

    @IdCryptoType.setter
    def IdCryptoType(self, IdCryptoType):
        self._IdCryptoType = IdCryptoType

    @property
    def NameCryptoType(self):
        return self._NameCryptoType

    @NameCryptoType.setter
    def NameCryptoType(self, NameCryptoType):
        self._NameCryptoType = NameCryptoType


    def _deserialize(self, params):
        self._PhoneNumber = params.get("PhoneNumber")
        self._IdNumber = params.get("IdNumber")
        self._BankCardNumber = params.get("BankCardNumber")
        self._UserIp = params.get("UserIp")
        self._Imei = params.get("Imei")
        self._Idfa = params.get("Idfa")
        self._Scene = params.get("Scene")
        self._Name = params.get("Name")
        self._EmailAddress = params.get("EmailAddress")
        self._Address = params.get("Address")
        self._Mac = params.get("Mac")
        self._Imsi = params.get("Imsi")
        self._AccountType = params.get("AccountType")
        self._Uid = params.get("Uid")
        self._AppIdU = params.get("AppIdU")
        self._WifiMac = params.get("WifiMac")
        self._WifiSSID = params.get("WifiSSID")
        self._WifiBSSID = params.get("WifiBSSID")
        self._BusinessId = params.get("BusinessId")
        self._PhoneCryptoType = params.get("PhoneCryptoType")
        self._IdCryptoType = params.get("IdCryptoType")
        self._NameCryptoType = params.get("NameCryptoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanceAntiFraudRecord(AbstractModel):
    """借贷反欺查询返回结果出参

    """

    def __init__(self):
        r"""
        :param _Found: 表示该条记录能否查到：1为能查到，-1为查不到
注意：此字段可能返回 null，表示取不到有效值。
        :type Found: str
        :param _IdFound: 表示该条Id能否查到：1为能查到，-1为查不到
注意：此字段可能返回 null，表示取不到有效值。
        :type IdFound: str
        :param _RiskScore: 评分0~100;值越高 欺诈可能性越大
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskScore: str
        :param _RiskInfo: 扩展字段，对风险类型的说明
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfo: list of RiskDetailInfo
        :param _OtherModelScores: 多模型返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherModelScores: list of FinanceOtherModelScores
        :param _Code: 业务侧错误码。成功时返回0，错误时返回非0值
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Message: 业务侧错误信息。成功时返回Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._Found = None
        self._IdFound = None
        self._RiskScore = None
        self._RiskInfo = None
        self._OtherModelScores = None
        self._Code = None
        self._Message = None

    @property
    def Found(self):
        return self._Found

    @Found.setter
    def Found(self, Found):
        self._Found = Found

    @property
    def IdFound(self):
        return self._IdFound

    @IdFound.setter
    def IdFound(self, IdFound):
        self._IdFound = IdFound

    @property
    def RiskScore(self):
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskInfo(self):
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

    @property
    def OtherModelScores(self):
        return self._OtherModelScores

    @OtherModelScores.setter
    def OtherModelScores(self, OtherModelScores):
        self._OtherModelScores = OtherModelScores

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


    def _deserialize(self, params):
        self._Found = params.get("Found")
        self._IdFound = params.get("IdFound")
        self._RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self._RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskDetailInfo()
                obj._deserialize(item)
                self._RiskInfo.append(obj)
        if params.get("OtherModelScores") is not None:
            self._OtherModelScores = []
            for item in params.get("OtherModelScores"):
                obj = FinanceOtherModelScores()
                obj._deserialize(item)
                self._OtherModelScores.append(obj)
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FinanceOtherModelScores(AbstractModel):
    """借贷反欺返回结果出参中的多模型返回结果

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID序号
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _ModelScore: 模型ID序号对应的评分结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelScore: str
        """
        self._ModelId = None
        self._ModelScore = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelScore(self):
        return self._ModelScore

    @ModelScore.setter
    def ModelScore(self, ModelScore):
        self._ModelScore = ModelScore


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ModelScore = params.get("ModelScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAntiFraudRequest(AbstractModel):
    """GetAntiFraud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessSecurityData: 默认不传，约定用原始业务
入参(二选一BusinessSecurityData 或
BusinessCryptoData)。
        :type BusinessSecurityData: :class:`tencentcloud.af.v20200226.models.AntiFraudFilter`
        :param _BusinessCryptoData: 默认不传，约定用密文业务
入参(二选一
BusinessSecurityData 或
BusinessCryptoData)。
        :type BusinessCryptoData: :class:`tencentcloud.af.v20200226.models.AntiFraudCryptoFilter`
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
            self._BusinessSecurityData = AntiFraudFilter()
            self._BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))
        if params.get("BusinessCryptoData") is not None:
            self._BusinessCryptoData = AntiFraudCryptoFilter()
            self._BusinessCryptoData._deserialize(params.get("BusinessCryptoData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAntiFraudResponse(AbstractModel):
    """GetAntiFraud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 反欺诈评分接口结果
        :type Data: :class:`tencentcloud.af.v20200226.models.AntiFraudRecord`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
            self._Data = AntiFraudRecord()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class OtherModelScoresDetail(AbstractModel):
    """扩展字段，对多模型返回结果的说明，被如下接口引用：GetAntiFraud。

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型版本号；默认顺序为 0、1、2、3、…其中：0=主模型，跟 RiskScore 保持一致；
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _ModelScore: 模型版本对应的评分结果；Found=1 时：模型版本对应的评分结果，0~100 分
区间；Found=-1（未查到）时：全部模型结果返回-1
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelScore: str
        """
        self._ModelId = None
        self._ModelScore = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelScore(self):
        return self._ModelScore

    @ModelScore.setter
    def ModelScore(self, ModelScore):
        self._ModelScore = ModelScore


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ModelScore = params.get("ModelScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAntiFraudRequest(AbstractModel):
    """QueryAntiFraud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PhoneNumber: 电话号码(五选二)
        :type PhoneNumber: str
        :param _IdNumber: Id(五选二)
        :type IdNumber: str
        :param _BankCardNumber: 银行卡号(五选二)
        :type BankCardNumber: str
        :param _UserIp: 用户请求来源 IP(五选二)
        :type UserIp: str
        :param _Imei: 国际移动设备识别码(五选二)
        :type Imei: str
        :param _Idfa: ios 系统广告标示符(五选二)
        :type Idfa: str
        :param _Scene: 业务场景 ID，需要找技术对接
        :type Scene: str
        :param _Name: 姓名
        :type Name: str
        :param _EmailAddress: 用户邮箱地址
        :type EmailAddress: str
        :param _Address: 用户住址
        :type Address: str
        :param _Mac: MAC 地址
        :type Mac: str
        :param _Imsi: 国际移动用户识别码
        :type Imsi: str
        :param _AccountType: 关联的腾讯帐号 QQ：1；
开放帐号微信： 2；
        :type AccountType: str
        :param _Uid: 可选的 QQ 或微信 openid
        :type Uid: str
        :param _AppIdU: qq 或微信分配给网站或应用的 appid，用来
唯一标识网站或应用
        :type AppIdU: str
        :param _WifiMac: WIFI MAC
        :type WifiMac: str
        :param _WifiSSID: WIFI 服务集标识
        :type WifiSSID: str
        :param _WifiBSSID: WIFI-BSSID
        :type WifiBSSID: str
        :param _BusinessId: 业务 ID，在多个业务中使用此服务，通过此
ID 区分统计数据
        :type BusinessId: str
        :param _IdCryptoType: Id加密类型
0：不加密（默认值）
1：md5
2：sha256
3：SM3
        :type IdCryptoType: str
        :param _PhoneCryptoType: 手机号加密类型
0：不加密（默认值）
1：md5, 2：sha256
3：SM3
        :type PhoneCryptoType: str
        :param _NameCryptoType: 姓名加密类型
0：不加密（默认值）
1：md5
2：sha256
3：SM3
        :type NameCryptoType: str
        """
        self._PhoneNumber = None
        self._IdNumber = None
        self._BankCardNumber = None
        self._UserIp = None
        self._Imei = None
        self._Idfa = None
        self._Scene = None
        self._Name = None
        self._EmailAddress = None
        self._Address = None
        self._Mac = None
        self._Imsi = None
        self._AccountType = None
        self._Uid = None
        self._AppIdU = None
        self._WifiMac = None
        self._WifiSSID = None
        self._WifiBSSID = None
        self._BusinessId = None
        self._IdCryptoType = None
        self._PhoneCryptoType = None
        self._NameCryptoType = None

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def IdNumber(self):
        return self._IdNumber

    @IdNumber.setter
    def IdNumber(self, IdNumber):
        self._IdNumber = IdNumber

    @property
    def BankCardNumber(self):
        return self._BankCardNumber

    @BankCardNumber.setter
    def BankCardNumber(self, BankCardNumber):
        self._BankCardNumber = BankCardNumber

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def Imei(self):
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Idfa(self):
        return self._Idfa

    @Idfa.setter
    def Idfa(self, Idfa):
        self._Idfa = Idfa

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Mac(self):
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def Imsi(self):
        return self._Imsi

    @Imsi.setter
    def Imsi(self, Imsi):
        self._Imsi = Imsi

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
    def AppIdU(self):
        return self._AppIdU

    @AppIdU.setter
    def AppIdU(self, AppIdU):
        self._AppIdU = AppIdU

    @property
    def WifiMac(self):
        return self._WifiMac

    @WifiMac.setter
    def WifiMac(self, WifiMac):
        self._WifiMac = WifiMac

    @property
    def WifiSSID(self):
        return self._WifiSSID

    @WifiSSID.setter
    def WifiSSID(self, WifiSSID):
        self._WifiSSID = WifiSSID

    @property
    def WifiBSSID(self):
        return self._WifiBSSID

    @WifiBSSID.setter
    def WifiBSSID(self, WifiBSSID):
        self._WifiBSSID = WifiBSSID

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def IdCryptoType(self):
        return self._IdCryptoType

    @IdCryptoType.setter
    def IdCryptoType(self, IdCryptoType):
        self._IdCryptoType = IdCryptoType

    @property
    def PhoneCryptoType(self):
        return self._PhoneCryptoType

    @PhoneCryptoType.setter
    def PhoneCryptoType(self, PhoneCryptoType):
        self._PhoneCryptoType = PhoneCryptoType

    @property
    def NameCryptoType(self):
        return self._NameCryptoType

    @NameCryptoType.setter
    def NameCryptoType(self, NameCryptoType):
        self._NameCryptoType = NameCryptoType


    def _deserialize(self, params):
        self._PhoneNumber = params.get("PhoneNumber")
        self._IdNumber = params.get("IdNumber")
        self._BankCardNumber = params.get("BankCardNumber")
        self._UserIp = params.get("UserIp")
        self._Imei = params.get("Imei")
        self._Idfa = params.get("Idfa")
        self._Scene = params.get("Scene")
        self._Name = params.get("Name")
        self._EmailAddress = params.get("EmailAddress")
        self._Address = params.get("Address")
        self._Mac = params.get("Mac")
        self._Imsi = params.get("Imsi")
        self._AccountType = params.get("AccountType")
        self._Uid = params.get("Uid")
        self._AppIdU = params.get("AppIdU")
        self._WifiMac = params.get("WifiMac")
        self._WifiSSID = params.get("WifiSSID")
        self._WifiBSSID = params.get("WifiBSSID")
        self._BusinessId = params.get("BusinessId")
        self._IdCryptoType = params.get("IdCryptoType")
        self._PhoneCryptoType = params.get("PhoneCryptoType")
        self._NameCryptoType = params.get("NameCryptoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAntiFraudResponse(AbstractModel):
    """QueryAntiFraud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Found: 表示该条记录能否查到：1为能查到，-1为查不到
        :type Found: int
        :param _IdFound: 表示该条Id能否查到：1为能查到，-1为查不到
        :type IdFound: int
        :param _RiskScore: 0~100;值越高 欺诈可能性越大
        :type RiskScore: int
        :param _RiskInfo: 扩展字段，对风险类型的说明
        :type RiskInfo: list of RiskDetail
        :param _CodeDesc: 业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Found = None
        self._IdFound = None
        self._RiskScore = None
        self._RiskInfo = None
        self._CodeDesc = None
        self._RequestId = None

    @property
    def Found(self):
        return self._Found

    @Found.setter
    def Found(self, Found):
        self._Found = Found

    @property
    def IdFound(self):
        return self._IdFound

    @IdFound.setter
    def IdFound(self, IdFound):
        self._IdFound = IdFound

    @property
    def RiskScore(self):
        return self._RiskScore

    @RiskScore.setter
    def RiskScore(self, RiskScore):
        self._RiskScore = RiskScore

    @property
    def RiskInfo(self):
        return self._RiskInfo

    @RiskInfo.setter
    def RiskInfo(self, RiskInfo):
        self._RiskInfo = RiskInfo

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
        self._Found = params.get("Found")
        self._IdFound = params.get("IdFound")
        self._RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self._RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskDetail()
                obj._deserialize(item)
                self._RiskInfo.append(obj)
        self._CodeDesc = params.get("CodeDesc")
        self._RequestId = params.get("RequestId")


class RiskDetail(AbstractModel):
    """扩展字段，对风险类型的说明

    """

    def __init__(self):
        r"""
        :param _RiskCode: 风险码 参数详细定义请加微信：TYXGJ-01
        :type RiskCode: int
        """
        self._RiskCode = None

    @property
    def RiskCode(self):
        return self._RiskCode

    @RiskCode.setter
    def RiskCode(self, RiskCode):
        self._RiskCode = RiskCode


    def _deserialize(self, params):
        self._RiskCode = params.get("RiskCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetailInfo(AbstractModel):
    """金融借贷反欺诈 风险码输出类型

    """

    def __init__(self):
        r"""
        :param _RiskCode: 风险码
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCode: str
        :param _RiskValue: 风险码对应的风险值
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskValue: str
        """
        self._RiskCode = None
        self._RiskValue = None

    @property
    def RiskCode(self):
        return self._RiskCode

    @RiskCode.setter
    def RiskCode(self, RiskCode):
        self._RiskCode = RiskCode

    @property
    def RiskValue(self):
        return self._RiskValue

    @RiskValue.setter
    def RiskValue(self, RiskValue):
        self._RiskValue = RiskValue


    def _deserialize(self, params):
        self._RiskCode = params.get("RiskCode")
        self._RiskValue = params.get("RiskValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleKindRiskDetail(AbstractModel):
    """扩展字段，对风险类型的说明

    """

    def __init__(self):
        r"""
        :param _RiskCode: 风险码
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCode: str
        :param _RiskCodeValue: 风险码详情
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCodeValue: str
        """
        self._RiskCode = None
        self._RiskCodeValue = None

    @property
    def RiskCode(self):
        return self._RiskCode

    @RiskCode.setter
    def RiskCode(self, RiskCode):
        self._RiskCode = RiskCode

    @property
    def RiskCodeValue(self):
        return self._RiskCodeValue

    @RiskCodeValue.setter
    def RiskCodeValue(self, RiskCodeValue):
        self._RiskCodeValue = RiskCodeValue


    def _deserialize(self, params):
        self._RiskCode = params.get("RiskCode")
        self._RiskCodeValue = params.get("RiskCodeValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        