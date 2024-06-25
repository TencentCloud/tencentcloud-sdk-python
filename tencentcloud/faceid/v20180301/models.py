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


class AttackRiskDetail(AbstractModel):
    """疑似攻击风险详情

    """

    def __init__(self):
        r"""
        :param _Type: 疑似的攻击痕迹类型
SuspectedSpoofingAttack：翻拍攻击
SuspectedSynthesisImage：疑似合成图片
SuspectedSynthesisVideo：疑似合成视频
SuspectedeAnomalyAttack：人脸特征疑似非真人
SuspectedAdversarialAttack：疑似对抗样本攻击
SuspectedBlackIndustry：疑似黑产攻击
SuspectedWatermark：疑似存在水印
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCard2EVerificationRequest(AbstractModel):
    """BankCard2EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _BankCard: 银行卡
        :type BankCard: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._Name = None
        self._BankCard = None
        self._Encryption = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BankCard(self):
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._BankCard = params.get("BankCard")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCard2EVerificationResponse(AbstractModel):
    """BankCard2EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码
计费结果码：
  '0': '认证通过'
  '-1': '认证未通过'
 '-4': '持卡人信息有误'
  '-5': '未开通无卡支付'
  '-6': '此卡被没收'
  '-7': '无效卡号'
  '-8': '此卡无对应发卡行'
  '-9': '该卡未初始化或睡眠卡'
  '-10': '作弊卡、吞卡'
  '-11': '此卡已挂失'
  '-12': '该卡已过期'
  '-13': '受限制的卡'
  '-14': '密码错误次数超限'
  '-15': '发卡行不支持此交易'
不计费结果码：
  '-2': '姓名校验不通过'
  '-3': '银行卡号码有误'
  '-16': '验证中心服务繁忙'
  '-17': '验证次数超限，请次日重试'

        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class BankCard4EVerificationRequest(AbstractModel):
    """BankCard4EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _BankCard: 银行卡
        :type BankCard: str
        :param _Phone: 手机号码
        :type Phone: str
        :param _IdCard: 开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。
        :type IdCard: str
        :param _CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。
目前默认为0：身份证，其他证件类型暂不支持。
        :type CertType: int
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号、银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._Name = None
        self._BankCard = None
        self._Phone = None
        self._IdCard = None
        self._CertType = None
        self._Encryption = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BankCard(self):
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._BankCard = params.get("BankCard")
        self._Phone = params.get("Phone")
        self._IdCard = params.get("IdCard")
        self._CertType = params.get("CertType")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCard4EVerificationResponse(AbstractModel):
    """BankCard4EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码
收费结果码：
'0': '认证通过'
'-1': '认证未通过'
'-6': '持卡人信息有误'
'-7': '未开通无卡支付'
'-8': '此卡被没收'
'-9': '无效卡号'
'-10': '此卡无对应发卡行'
'-11': '该卡未初始化或睡眠卡'
'-12': '作弊卡、吞卡'
'-13': '此卡已挂失'
'-14': '该卡已过期'
'-15': '受限制的卡'
'-16': '密码错误次数超限'
'-17': '发卡行不支持此交易'
不收费结果码：
'-2': '姓名校验不通过'
'-3': '身份证号码有误'
'-4': '银行卡号码有误'
'-5': '手机号码不合法'
'-18': '验证中心服务繁忙'
'-19': '验证次数超限，请次日重试'
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class BankCardVerificationRequest(AbstractModel):
    """BankCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _BankCard: 银行卡
        :type BankCard: str
        :param _CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。
目前默认：0 身份证，其他证件类型暂不支持。
        :type CertType: int
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._BankCard = None
        self._CertType = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BankCard(self):
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._BankCard = params.get("BankCard")
        self._CertType = params.get("CertType")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardVerificationResponse(AbstractModel):
    """BankCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码
收费结果码：
'0': '认证通过'
'-1': '认证未通过'
'-5': '持卡人信息有误'
'-6': '未开通无卡支付'
'-7': '此卡被没收'
'-8': '无效卡号'
'-9': '此卡无对应发卡行'
'-10': '该卡未初始化或睡眠卡'
'-11': '作弊卡、吞卡'
'-12': '此卡已挂失'
'-13': '该卡已过期'
'-14': '受限制的卡'
'-15': '密码错误次数超限'
'-16': '发卡行不支持此交易'
不收费结果码：
'-2': '姓名校验不通过'
'-3': '身份证号码有误'
'-4': '银行卡号码有误'
'-17': '验证中心服务繁忙'
'-18': '验证次数超限，请次日重试'
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class ChargeDetail(AbstractModel):
    """计费详情

    """

    def __init__(self):
        r"""
        :param _ReqTime: 一比一时间时间戳，13位。
        :type ReqTime: str
        :param _Seq: 一比一请求的唯一标记。
        :type Seq: str
        :param _IdCard: 一比一时使用的、脱敏后的身份证号。
        :type IdCard: str
        :param _Idcard: 已废弃。请使用“IdCard”字段
        :type Idcard: str
        :param _Name: 一比一时使用的、脱敏后的姓名。
        :type Name: str
        :param _Sim: 一比一的相似度。0-100，保留2位小数。
        :type Sim: str
        :param _IsNeedCharge: 本次详情是否收费。
        :type IsNeedCharge: bool
        :param _ChargeType: 收费类型，比对、核身、混合部署。
        :type ChargeType: str
        :param _ErrorCode: 本次活体一比一最终结果。
        :type ErrorCode: str
        :param _ErrorMessage: 本次活体一比一最终结果描述。
        :type ErrorMessage: str
        """
        self._ReqTime = None
        self._Seq = None
        self._IdCard = None
        self._Idcard = None
        self._Name = None
        self._Sim = None
        self._IsNeedCharge = None
        self._ChargeType = None
        self._ErrorCode = None
        self._ErrorMessage = None

    @property
    def ReqTime(self):
        return self._ReqTime

    @ReqTime.setter
    def ReqTime(self, ReqTime):
        self._ReqTime = ReqTime

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Idcard(self):
        warnings.warn("parameter `Idcard` is deprecated", DeprecationWarning) 

        return self._Idcard

    @Idcard.setter
    def Idcard(self, Idcard):
        warnings.warn("parameter `Idcard` is deprecated", DeprecationWarning) 

        self._Idcard = Idcard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def IsNeedCharge(self):
        return self._IsNeedCharge

    @IsNeedCharge.setter
    def IsNeedCharge(self, IsNeedCharge):
        self._IsNeedCharge = IsNeedCharge

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._ReqTime = params.get("ReqTime")
        self._Seq = params.get("Seq")
        self._IdCard = params.get("IdCard")
        self._Idcard = params.get("Idcard")
        self._Name = params.get("Name")
        self._Sim = params.get("Sim")
        self._IsNeedCharge = params.get("IsNeedCharge")
        self._ChargeType = params.get("ChargeType")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCardInformationRequest(AbstractModel):
    """CheckBankCardInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BankCard: 银行卡号。
        :type BankCard: str
        :param _Encryption: 敏感数据加密信息。对传入信息（银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._BankCard = None
        self._Encryption = None

    @property
    def BankCard(self):
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._BankCard = params.get("BankCard")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCardInformationResponse(AbstractModel):
    """CheckBankCardInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 查询成功
-1: 未查到信息
不收费结果码：
-2：验证中心服务繁忙
-3：银行卡不存在
        :type Result: str
        :param _Description: 业务结果描述
        :type Description: str
        :param _AccountBank: 开户行
        :type AccountBank: str
        :param _AccountType: 卡性质：1. 借记卡；2. 贷记卡；3. 预付费卡；4. 准贷记卡
        :type AccountType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._AccountBank = None
        self._AccountType = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AccountBank(self):
        return self._AccountBank

    @AccountBank.setter
    def AccountBank(self, AccountBank):
        self._AccountBank = AccountBank

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._AccountBank = params.get("AccountBank")
        self._AccountType = params.get("AccountType")
        self._RequestId = params.get("RequestId")


class CheckEidTokenStatusRequest(AbstractModel):
    """CheckEidTokenStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EidToken: E证通流程的唯一标识，调用GetEidToken接口时生成。
        :type EidToken: str
        """
        self._EidToken = None

    @property
    def EidToken(self):
        return self._EidToken

    @EidToken.setter
    def EidToken(self, EidToken):
        self._EidToken = EidToken


    def _deserialize(self, params):
        self._EidToken = params.get("EidToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckEidTokenStatusResponse(AbstractModel):
    """CheckEidTokenStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 枚举：
init：token未验证
doing: 验证中
finished: 验证完成
timeout: token已超时
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CheckIdCardInformationRequest(AbstractModel):
    """CheckIdCardInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageBase64: 身份证人像面的 Base64 值
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
ImageBase64、ImageUrl二者必须提供其中之一。若都提供了，则按照ImageUrl>ImageBase64的优先级使用参数。
        :type ImageBase64: str
        :param _ImageUrl: 身份证人像面的 Url 地址
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Config: 以下可选字段均为bool 类型，默认false：
CopyWarn，复印件告警
BorderCheckWarn，边框和框内遮挡告警
ReshootWarn，翻拍告警
DetectPsWarn，PS检测告警（疑似存在PS痕迹）
TempIdWarn，临时身份证告警
Quality，图片质量告警（评价图片模糊程度）

SDK 设置方式参考：
Config = Json.stringify({"CopyWarn":true,"ReshootWarn":true})
API 3.0 Explorer 设置方式参考：
Config = {"CopyWarn":true,"ReshootWarn":true}
        :type Config: str
        :param _IsEncrypt: 是否需要对返回中的敏感信息进行加密。默认false。
其中敏感信息包括：Response.IdNum、Response.Name
        :type IsEncrypt: bool
        """
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Config = None
        self._IsEncrypt = None

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def IsEncrypt(self):
        return self._IsEncrypt

    @IsEncrypt.setter
    def IsEncrypt(self, IsEncrypt):
        self._IsEncrypt = IsEncrypt


    def _deserialize(self, params):
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Config = params.get("Config")
        self._IsEncrypt = params.get("IsEncrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIdCardInformationResponse(AbstractModel):
    """CheckIdCardInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param _Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _Name: 姓名
        :type Name: str
        :param _Sex: 性别
        :type Sex: str
        :param _Nation: 民族
        :type Nation: str
        :param _Birth: 出生日期
        :type Birth: str
        :param _Address: 地址
        :type Address: str
        :param _IdNum: 身份证号
        :type IdNum: str
        :param _Portrait: 身份证头像照片的base64编码，如果抠图失败会拿整张身份证做比对并返回空。
        :type Portrait: str
        :param _Warnings: 告警信息，当在Config中配置了告警信息会停止人像比对，Result返回错误（FailedOperation.OcrWarningOccurred）并有此告警信息，Code 告警码列表和释义：

-9101 身份证边框不完整告警，
-9102 身份证复印件告警，
-9103 身份证翻拍告警，
-9105 身份证框内遮挡告警，
-9104 临时身份证告警，
-9106 身份证 PS 告警（疑似存在PS痕迹）。
-8001 图片模糊告警
多个会 |  隔开如 "-9101|-9106|-9104"
        :type Warnings: str
        :param _Quality: 图片质量分数，当请求Config中配置图片模糊告警该参数才有意义，取值范围（0～100），目前默认阈值是50分，低于50分会触发模糊告警。
        :type Quality: float
        :param _Encryption: 敏感数据加密信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Sim = None
        self._Result = None
        self._Description = None
        self._Name = None
        self._Sex = None
        self._Nation = None
        self._Birth = None
        self._Address = None
        self._IdNum = None
        self._Portrait = None
        self._Warnings = None
        self._Quality = None
        self._Encryption = None
        self._RequestId = None

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def Birth(self):
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IdNum(self):
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Portrait(self):
        return self._Portrait

    @Portrait.setter
    def Portrait(self, Portrait):
        self._Portrait = Portrait

    @property
    def Warnings(self):
        return self._Warnings

    @Warnings.setter
    def Warnings(self, Warnings):
        self._Warnings = Warnings

    @property
    def Quality(self):
        return self._Quality

    @Quality.setter
    def Quality(self, Quality):
        self._Quality = Quality

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Sim = params.get("Sim")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._Sex = params.get("Sex")
        self._Nation = params.get("Nation")
        self._Birth = params.get("Birth")
        self._Address = params.get("Address")
        self._IdNum = params.get("IdNum")
        self._Portrait = params.get("Portrait")
        self._Warnings = params.get("Warnings")
        self._Quality = params.get("Quality")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        self._RequestId = params.get("RequestId")


class CheckIdNameDateRequest(AbstractModel):
    """CheckIdNameDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _ValidityBegin: 身份证有效期开始时间，格式：YYYYMMDD。如：20210701
        :type ValidityBegin: str
        :param _ValidityEnd: 身份证有效期到期时间，格式：YYYYMMDD，长期用“00000000”代替；如：20210701
        :type ValidityEnd: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._Name = None
        self._IdCard = None
        self._ValidityBegin = None
        self._ValidityEnd = None
        self._Encryption = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def ValidityBegin(self):
        return self._ValidityBegin

    @ValidityBegin.setter
    def ValidityBegin(self, ValidityBegin):
        self._ValidityBegin = ValidityBegin

    @property
    def ValidityEnd(self):
        return self._ValidityEnd

    @ValidityEnd.setter
    def ValidityEnd(self, ValidityEnd):
        self._ValidityEnd = ValidityEnd

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IdCard = params.get("IdCard")
        self._ValidityBegin = params.get("ValidityBegin")
        self._ValidityEnd = params.get("ValidityEnd")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIdNameDateResponse(AbstractModel):
    """CheckIdNameDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 一致
-1: 不一致
不收费结果码：
-2: 非法身份证号（长度、校验位等不正确）
-3: 非法姓名（长度、格式等不正确）
-4: 非法有效期（长度、格式等不正确）
-5: 身份信息无效
-6: 证件库服务异常
-7: 证件库中无此身份证记录
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckPhoneAndNameRequest(AbstractModel):
    """CheckPhoneAndName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mobile: ⼿机号
        :type Mobile: str
        :param _Name: 姓名
        :type Name: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._Mobile = None
        self._Name = None
        self._Encryption = None

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Mobile = params.get("Mobile")
        self._Name = params.get("Name")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckPhoneAndNameResponse(AbstractModel):
    """CheckPhoneAndName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 验证结果一致
1: 验证结果不一致
不收费结果码：
-1:查无记录
-2:引擎未知错误
-3:引擎服务异常
-4:姓名校验不通过
-5:手机号码不合法
        :type Result: str
        :param _Description: 业务结果描述
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DetectAIFakeFacesRequest(AbstractModel):
    """DetectAIFakeFaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceInput: 传入需要进行检测的带有人脸的图片或视频，使用base64编码的形式。

图片的Base64值：
建议整体图像480x640的分辨率，脸部 大小 100X100 以上；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。

视频的Base64值：
Base64编码后的大小不超过8M，支持mp4、avi、flv格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
视频时长最大支持20s，建议时长2～5s。
建议视频分辨率为480x640，帧率在25fps~30fps之间。
        :type FaceInput: str
        :param _FaceInputType: 传入的类型
1- 传入的是图片类型
2- 传入的是视频类型
其他 - 返回错误码InvalidParameter
        :type FaceInputType: int
        """
        self._FaceInput = None
        self._FaceInputType = None

    @property
    def FaceInput(self):
        return self._FaceInput

    @FaceInput.setter
    def FaceInput(self, FaceInput):
        self._FaceInput = FaceInput

    @property
    def FaceInputType(self):
        return self._FaceInputType

    @FaceInputType.setter
    def FaceInputType(self, FaceInputType):
        self._FaceInputType = FaceInputType


    def _deserialize(self, params):
        self._FaceInput = params.get("FaceInput")
        self._FaceInputType = params.get("FaceInputType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectAIFakeFacesResponse(AbstractModel):
    """DetectAIFakeFaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttackRiskLevel: 检测到的图片是否存在攻击：
Low：无攻击风险
Mid：中度疑似攻击
High：高度疑似攻击
        :type AttackRiskLevel: str
        :param _AttackRiskDetailList: 检测到疑似的攻击痕迹列表
说明：未检测到攻击痕迹时，返回空数组
此出参仅作为结果判断的参考，实际应用仍建议使用AttackRiskLevel的结果。
        :type AttackRiskDetailList: list of AttackRiskDetail
        :param _ExtraInfo: 额外信息
        :type ExtraInfo: :class:`tencentcloud.faceid.v20180301.models.ExtraInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttackRiskLevel = None
        self._AttackRiskDetailList = None
        self._ExtraInfo = None
        self._RequestId = None

    @property
    def AttackRiskLevel(self):
        return self._AttackRiskLevel

    @AttackRiskLevel.setter
    def AttackRiskLevel(self, AttackRiskLevel):
        self._AttackRiskLevel = AttackRiskLevel

    @property
    def AttackRiskDetailList(self):
        return self._AttackRiskDetailList

    @AttackRiskDetailList.setter
    def AttackRiskDetailList(self, AttackRiskDetailList):
        self._AttackRiskDetailList = AttackRiskDetailList

    @property
    def ExtraInfo(self):
        return self._ExtraInfo

    @ExtraInfo.setter
    def ExtraInfo(self, ExtraInfo):
        self._ExtraInfo = ExtraInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AttackRiskLevel = params.get("AttackRiskLevel")
        if params.get("AttackRiskDetailList") is not None:
            self._AttackRiskDetailList = []
            for item in params.get("AttackRiskDetailList"):
                obj = AttackRiskDetail()
                obj._deserialize(item)
                self._AttackRiskDetailList.append(obj)
        if params.get("ExtraInfo") is not None:
            self._ExtraInfo = ExtraInfo()
            self._ExtraInfo._deserialize(params.get("ExtraInfo"))
        self._RequestId = params.get("RequestId")


class DetectAuthRequest(AbstractModel):
    """DetectAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请添加[腾讯云人脸核身小助手](https://cloud.tencent.com/document/product/1007/56130)进行咨询。
        :type RuleId: str
        :param _TerminalType: 本接口不需要传递此参数。
        :type TerminalType: str
        :param _IdCard: 身份标识（是否必传基于[控制台](https://console.cloud.tencent.com/faceid/access)申请业务流程时配置的提示）。
规则：a-z，A-Z，0-9组合。最长长度32位。
        :type IdCard: str
        :param _Name: 姓名。（是否必传基于[控制台](https://console.cloud.tencent.com/faceid/access)申请业务流程时配置的提示）。
最长长度32位。中文请使用UTF-8编码。
        :type Name: str
        :param _RedirectUrl: 认证结束后重定向的回调链接地址。最长长度1024位。
        :type RedirectUrl: str
        :param _Extra: 透传字段，在获取验证结果时返回。
        :type Extra: str
        :param _ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param _IntentionVerifyText: 意愿核身（朗读模式）使用的文案，若未使用意愿核身（朗读模式），则该字段无需传入。默认为空，最长可接受120的字符串长度。
        :type IntentionVerifyText: str
        :param _IntentionQuestions: 意愿核身语音问答模式（即语音播报+语音回答）使用的文案，包括：系统语音播报的文本、需要核验的标准文本。当前仅支持1轮问答。
        :type IntentionQuestions: list of IntentionQuestion
        :param _Config: RuleId相关配置
        :type Config: :class:`tencentcloud.faceid.v20180301.models.RuleIdConfig`
        :param _IntentionActions: 意愿核身（点头确认模式）使用的文案，若未使用意愿核身（点头确认模式），则该字段无需传入。当前仅支持一个提示文本。
        :type IntentionActions: list of IntentionActionConfig
        """
        self._RuleId = None
        self._TerminalType = None
        self._IdCard = None
        self._Name = None
        self._RedirectUrl = None
        self._Extra = None
        self._ImageBase64 = None
        self._Encryption = None
        self._IntentionVerifyText = None
        self._IntentionQuestions = None
        self._Config = None
        self._IntentionActions = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TerminalType(self):
        return self._TerminalType

    @TerminalType.setter
    def TerminalType(self, TerminalType):
        self._TerminalType = TerminalType

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def IntentionVerifyText(self):
        return self._IntentionVerifyText

    @IntentionVerifyText.setter
    def IntentionVerifyText(self, IntentionVerifyText):
        self._IntentionVerifyText = IntentionVerifyText

    @property
    def IntentionQuestions(self):
        return self._IntentionQuestions

    @IntentionQuestions.setter
    def IntentionQuestions(self, IntentionQuestions):
        self._IntentionQuestions = IntentionQuestions

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def IntentionActions(self):
        return self._IntentionActions

    @IntentionActions.setter
    def IntentionActions(self, IntentionActions):
        self._IntentionActions = IntentionActions


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._TerminalType = params.get("TerminalType")
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._RedirectUrl = params.get("RedirectUrl")
        self._Extra = params.get("Extra")
        self._ImageBase64 = params.get("ImageBase64")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        self._IntentionVerifyText = params.get("IntentionVerifyText")
        if params.get("IntentionQuestions") is not None:
            self._IntentionQuestions = []
            for item in params.get("IntentionQuestions"):
                obj = IntentionQuestion()
                obj._deserialize(item)
                self._IntentionQuestions.append(obj)
        if params.get("Config") is not None:
            self._Config = RuleIdConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("IntentionActions") is not None:
            self._IntentionActions = []
            for item in params.get("IntentionActions"):
                obj = IntentionActionConfig()
                obj._deserialize(item)
                self._IntentionActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectAuthResponse(AbstractModel):
    """DetectAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 用于发起核身流程的URL，仅微信H5场景使用。
        :type Url: str
        :param _BizToken: 一次核身流程的标识，有效时间为7,200秒；
完成核身后，可用该标识获取验证结果信息。
        :type BizToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._BizToken = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._BizToken = params.get("BizToken")
        self._RequestId = params.get("RequestId")


class DetectDetail(AbstractModel):
    """活体一比一详情

    """

    def __init__(self):
        r"""
        :param _ReqTime: 请求时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReqTime: str
        :param _Seq: 本次活体一比一请求的唯一标记。
注意：此字段可能返回 null，表示取不到有效值。
        :type Seq: str
        :param _Idcard: 参与本次活体一比一的身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type Idcard: str
        :param _Name: 参与本次活体一比一的姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Sim: 本次活体一比一的相似度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sim: str
        :param _IsNeedCharge: 本次活体一比一是否收费
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNeedCharge: bool
        :param _Errcode: 本次活体一比一最终结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Errcode: int
        :param _Errmsg: 本次活体一比一最终结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Errmsg: str
        :param _Livestatus: 本次活体结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Livestatus: int
        :param _Livemsg: 本次活体结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Livemsg: str
        :param _Comparestatus: 本次一比一结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param _Comparemsg: 本次一比一结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        :param _CompareLibType: 比对库源类型。包括：
公安商业库；
业务方自有库（用户上传照片、客户的混合库、混合部署库）；
二次验证库；
人工审核库；
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareLibType: str
        :param _LivenessMode: 枚举活体检测类型：
0：未知
1：数字活体
2：动作活体
3：静默活体
4：一闪活体（动作+光线）
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessMode: int
        """
        self._ReqTime = None
        self._Seq = None
        self._Idcard = None
        self._Name = None
        self._Sim = None
        self._IsNeedCharge = None
        self._Errcode = None
        self._Errmsg = None
        self._Livestatus = None
        self._Livemsg = None
        self._Comparestatus = None
        self._Comparemsg = None
        self._CompareLibType = None
        self._LivenessMode = None

    @property
    def ReqTime(self):
        return self._ReqTime

    @ReqTime.setter
    def ReqTime(self, ReqTime):
        self._ReqTime = ReqTime

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def Idcard(self):
        return self._Idcard

    @Idcard.setter
    def Idcard(self, Idcard):
        self._Idcard = Idcard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def IsNeedCharge(self):
        return self._IsNeedCharge

    @IsNeedCharge.setter
    def IsNeedCharge(self, IsNeedCharge):
        self._IsNeedCharge = IsNeedCharge

    @property
    def Errcode(self):
        return self._Errcode

    @Errcode.setter
    def Errcode(self, Errcode):
        self._Errcode = Errcode

    @property
    def Errmsg(self):
        return self._Errmsg

    @Errmsg.setter
    def Errmsg(self, Errmsg):
        self._Errmsg = Errmsg

    @property
    def Livestatus(self):
        return self._Livestatus

    @Livestatus.setter
    def Livestatus(self, Livestatus):
        self._Livestatus = Livestatus

    @property
    def Livemsg(self):
        return self._Livemsg

    @Livemsg.setter
    def Livemsg(self, Livemsg):
        self._Livemsg = Livemsg

    @property
    def Comparestatus(self):
        return self._Comparestatus

    @Comparestatus.setter
    def Comparestatus(self, Comparestatus):
        self._Comparestatus = Comparestatus

    @property
    def Comparemsg(self):
        return self._Comparemsg

    @Comparemsg.setter
    def Comparemsg(self, Comparemsg):
        self._Comparemsg = Comparemsg

    @property
    def CompareLibType(self):
        return self._CompareLibType

    @CompareLibType.setter
    def CompareLibType(self, CompareLibType):
        self._CompareLibType = CompareLibType

    @property
    def LivenessMode(self):
        return self._LivenessMode

    @LivenessMode.setter
    def LivenessMode(self, LivenessMode):
        self._LivenessMode = LivenessMode


    def _deserialize(self, params):
        self._ReqTime = params.get("ReqTime")
        self._Seq = params.get("Seq")
        self._Idcard = params.get("Idcard")
        self._Name = params.get("Name")
        self._Sim = params.get("Sim")
        self._IsNeedCharge = params.get("IsNeedCharge")
        self._Errcode = params.get("Errcode")
        self._Errmsg = params.get("Errmsg")
        self._Livestatus = params.get("Livestatus")
        self._Livemsg = params.get("Livemsg")
        self._Comparestatus = params.get("Comparestatus")
        self._Comparemsg = params.get("Comparemsg")
        self._CompareLibType = params.get("CompareLibType")
        self._LivenessMode = params.get("LivenessMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoBestFrame(AbstractModel):
    """核身最佳帧信息

    """

    def __init__(self):
        r"""
        :param _BestFrame: 活体比对最佳帧Base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: str
        :param _BestFrames: 自截帧Base64编码数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrames: list of str
        """
        self._BestFrame = None
        self._BestFrames = None

    @property
    def BestFrame(self):
        return self._BestFrame

    @BestFrame.setter
    def BestFrame(self, BestFrame):
        self._BestFrame = BestFrame

    @property
    def BestFrames(self):
        return self._BestFrames

    @BestFrames.setter
    def BestFrames(self, BestFrames):
        self._BestFrames = BestFrames


    def _deserialize(self, params):
        self._BestFrame = params.get("BestFrame")
        self._BestFrames = params.get("BestFrames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoIdCardData(AbstractModel):
    """核身身份证图片信息

    """

    def __init__(self):
        r"""
        :param _OcrFront: OCR正面照片的base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrFront: str
        :param _OcrBack: OCR反面照片的base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrBack: str
        :param _ProcessedFrontImage: 旋转裁边后的正面照片base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedFrontImage: str
        :param _ProcessedBackImage: 旋转裁边后的背面照片base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedBackImage: str
        :param _Avatar: 身份证正面人像图base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _WarnInfos: 身份证人像面告警码，开启身份证告警功能后才会返回，返回数组中可能出现的告警码如下：
-9100 身份证有效日期不合法告警，
-9101 身份证边框不完整告警，
-9102 身份证复印件告警，
-9103 身份证翻拍告警，
-9105 身份证框内遮挡告警，
-9104 临时身份证告警，
-9106 身份证 PS 告警（疑似存在PS痕迹），
-9107 身份证反光告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnInfos: list of int
        :param _BackWarnInfos: 身份证国徽面告警码，开启身份证告警功能后才会返回，返回数组中可能出现的告警码如下：
-9100 身份证有效日期不合法告警，
-9101 身份证边框不完整告警，
-9102 身份证复印件告警，
-9103 身份证翻拍告警，
-9105 身份证框内遮挡告警，
-9104 临时身份证告警，
-9106 身份证 PS 告警（疑似存在PS痕迹），
-9107 身份证反光告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackWarnInfos: list of int
        """
        self._OcrFront = None
        self._OcrBack = None
        self._ProcessedFrontImage = None
        self._ProcessedBackImage = None
        self._Avatar = None
        self._WarnInfos = None
        self._BackWarnInfos = None

    @property
    def OcrFront(self):
        return self._OcrFront

    @OcrFront.setter
    def OcrFront(self, OcrFront):
        self._OcrFront = OcrFront

    @property
    def OcrBack(self):
        return self._OcrBack

    @OcrBack.setter
    def OcrBack(self, OcrBack):
        self._OcrBack = OcrBack

    @property
    def ProcessedFrontImage(self):
        return self._ProcessedFrontImage

    @ProcessedFrontImage.setter
    def ProcessedFrontImage(self, ProcessedFrontImage):
        self._ProcessedFrontImage = ProcessedFrontImage

    @property
    def ProcessedBackImage(self):
        return self._ProcessedBackImage

    @ProcessedBackImage.setter
    def ProcessedBackImage(self, ProcessedBackImage):
        self._ProcessedBackImage = ProcessedBackImage

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def WarnInfos(self):
        return self._WarnInfos

    @WarnInfos.setter
    def WarnInfos(self, WarnInfos):
        self._WarnInfos = WarnInfos

    @property
    def BackWarnInfos(self):
        return self._BackWarnInfos

    @BackWarnInfos.setter
    def BackWarnInfos(self, BackWarnInfos):
        self._BackWarnInfos = BackWarnInfos


    def _deserialize(self, params):
        self._OcrFront = params.get("OcrFront")
        self._OcrBack = params.get("OcrBack")
        self._ProcessedFrontImage = params.get("ProcessedFrontImage")
        self._ProcessedBackImage = params.get("ProcessedBackImage")
        self._Avatar = params.get("Avatar")
        self._WarnInfos = params.get("WarnInfos")
        self._BackWarnInfos = params.get("BackWarnInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoText(AbstractModel):
    """核身文本信息

    """

    def __init__(self):
        r"""
        :param _ErrCode: 本次流程最终验证结果。0为成功（仅包含活体人脸核身结果，不包含意愿核身结果）
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param _ErrMsg: 本次流程最终验证结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _IdCard: 本次验证使用的身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param _UseIDType: 用户认证时使用的证件号码类型：
0：二代身份证的证件号码
1：港澳台居住证的证件号码
2：其他（核验使用的证件号码非合法身份号码）
注意：此字段可能返回 null，表示取不到有效值。
        :type UseIDType: int
        :param _Name: 本次验证使用的姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _OcrNation: 身份校验环节识别结果：民族。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrNation: str
        :param _OcrAddress: 身份校验环节识别结果：家庭住址。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrAddress: str
        :param _OcrBirth: 身份校验环节识别结果：生日。格式为：YYYY/M/D
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrBirth: str
        :param _OcrAuthority: 身份校验环节识别结果：签发机关。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrAuthority: str
        :param _OcrValidDate: 身份校验环节识别结果：有效日期。格式为：YYYY.MM.DD-YYYY.MM.DD
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrValidDate: str
        :param _OcrName: 身份校验环节识别结果：姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrName: str
        :param _OcrIdCard: 身份校验环节识别结果：身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrIdCard: str
        :param _OcrGender: 身份校验环节识别结果：性别。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrGender: str
        :param _IdInfoFrom: 身份校验环节采用的信息上传方式。
取值有"NFC"、"OCR"、"手动输入"、"其他"
注意：此字段可能返回 null，表示取不到有效值。
        :type IdInfoFrom: str
        :param _LiveStatus: 本次流程最终活体结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStatus: int
        :param _LiveMsg: 本次流程最终活体结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveMsg: str
        :param _Comparestatus: 本次流程最终一比一结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param _Comparemsg: 本次流程最终一比一结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        :param _Sim: 本次流程活体一比一的分数，取值范围 [0.00, 100.00]。相似度大于等于70时才判断为同一人，也可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
注意：此字段可能返回 null，表示取不到有效值。
        :type Sim: str
        :param _Location: 地理位置经纬度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param _Extra: Auth接口带入额外信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _LivenessDetail: 本次流程进行的活体一比一流水。
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessDetail: list of DetectDetail
        :param _Mobile: 手机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        :param _CompareLibType: 本次流程最终比对库源类型。包括：
权威库；
业务方自有库（用户上传照片、客户的混合库、混合部署库）；
二次验证库；
人工审核库；
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareLibType: str
        :param _LivenessMode: 本次流程最终活体类型。包括：
0：未知
1：数字活体
2：动作活体
3：静默活体
4：一闪活体（动作+光线）
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessMode: int
        :param _NFCRequestIds: nfc重复计费requestId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NFCRequestIds: list of str
        :param _NFCBillingCounts: nfc重复计费计数
注意：此字段可能返回 null，表示取不到有效值。
        :type NFCBillingCounts: int
        :param _PassNo: 港澳台居住证通行证号码
注意：此字段可能返回 null，表示取不到有效值。
        :type PassNo: str
        :param _VisaNum: 港澳台居住证签发次数
注意：此字段可能返回 null，表示取不到有效值。
        :type VisaNum: str
        """
        self._ErrCode = None
        self._ErrMsg = None
        self._IdCard = None
        self._UseIDType = None
        self._Name = None
        self._OcrNation = None
        self._OcrAddress = None
        self._OcrBirth = None
        self._OcrAuthority = None
        self._OcrValidDate = None
        self._OcrName = None
        self._OcrIdCard = None
        self._OcrGender = None
        self._IdInfoFrom = None
        self._LiveStatus = None
        self._LiveMsg = None
        self._Comparestatus = None
        self._Comparemsg = None
        self._Sim = None
        self._Location = None
        self._Extra = None
        self._LivenessDetail = None
        self._Mobile = None
        self._CompareLibType = None
        self._LivenessMode = None
        self._NFCRequestIds = None
        self._NFCBillingCounts = None
        self._PassNo = None
        self._VisaNum = None

    @property
    def ErrCode(self):
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def UseIDType(self):
        return self._UseIDType

    @UseIDType.setter
    def UseIDType(self, UseIDType):
        self._UseIDType = UseIDType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OcrNation(self):
        return self._OcrNation

    @OcrNation.setter
    def OcrNation(self, OcrNation):
        self._OcrNation = OcrNation

    @property
    def OcrAddress(self):
        return self._OcrAddress

    @OcrAddress.setter
    def OcrAddress(self, OcrAddress):
        self._OcrAddress = OcrAddress

    @property
    def OcrBirth(self):
        return self._OcrBirth

    @OcrBirth.setter
    def OcrBirth(self, OcrBirth):
        self._OcrBirth = OcrBirth

    @property
    def OcrAuthority(self):
        return self._OcrAuthority

    @OcrAuthority.setter
    def OcrAuthority(self, OcrAuthority):
        self._OcrAuthority = OcrAuthority

    @property
    def OcrValidDate(self):
        return self._OcrValidDate

    @OcrValidDate.setter
    def OcrValidDate(self, OcrValidDate):
        self._OcrValidDate = OcrValidDate

    @property
    def OcrName(self):
        return self._OcrName

    @OcrName.setter
    def OcrName(self, OcrName):
        self._OcrName = OcrName

    @property
    def OcrIdCard(self):
        return self._OcrIdCard

    @OcrIdCard.setter
    def OcrIdCard(self, OcrIdCard):
        self._OcrIdCard = OcrIdCard

    @property
    def OcrGender(self):
        return self._OcrGender

    @OcrGender.setter
    def OcrGender(self, OcrGender):
        self._OcrGender = OcrGender

    @property
    def IdInfoFrom(self):
        return self._IdInfoFrom

    @IdInfoFrom.setter
    def IdInfoFrom(self, IdInfoFrom):
        self._IdInfoFrom = IdInfoFrom

    @property
    def LiveStatus(self):
        return self._LiveStatus

    @LiveStatus.setter
    def LiveStatus(self, LiveStatus):
        self._LiveStatus = LiveStatus

    @property
    def LiveMsg(self):
        return self._LiveMsg

    @LiveMsg.setter
    def LiveMsg(self, LiveMsg):
        self._LiveMsg = LiveMsg

    @property
    def Comparestatus(self):
        return self._Comparestatus

    @Comparestatus.setter
    def Comparestatus(self, Comparestatus):
        self._Comparestatus = Comparestatus

    @property
    def Comparemsg(self):
        return self._Comparemsg

    @Comparemsg.setter
    def Comparemsg(self, Comparemsg):
        self._Comparemsg = Comparemsg

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def LivenessDetail(self):
        return self._LivenessDetail

    @LivenessDetail.setter
    def LivenessDetail(self, LivenessDetail):
        self._LivenessDetail = LivenessDetail

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def CompareLibType(self):
        return self._CompareLibType

    @CompareLibType.setter
    def CompareLibType(self, CompareLibType):
        self._CompareLibType = CompareLibType

    @property
    def LivenessMode(self):
        return self._LivenessMode

    @LivenessMode.setter
    def LivenessMode(self, LivenessMode):
        self._LivenessMode = LivenessMode

    @property
    def NFCRequestIds(self):
        return self._NFCRequestIds

    @NFCRequestIds.setter
    def NFCRequestIds(self, NFCRequestIds):
        self._NFCRequestIds = NFCRequestIds

    @property
    def NFCBillingCounts(self):
        return self._NFCBillingCounts

    @NFCBillingCounts.setter
    def NFCBillingCounts(self, NFCBillingCounts):
        self._NFCBillingCounts = NFCBillingCounts

    @property
    def PassNo(self):
        return self._PassNo

    @PassNo.setter
    def PassNo(self, PassNo):
        self._PassNo = PassNo

    @property
    def VisaNum(self):
        return self._VisaNum

    @VisaNum.setter
    def VisaNum(self, VisaNum):
        self._VisaNum = VisaNum


    def _deserialize(self, params):
        self._ErrCode = params.get("ErrCode")
        self._ErrMsg = params.get("ErrMsg")
        self._IdCard = params.get("IdCard")
        self._UseIDType = params.get("UseIDType")
        self._Name = params.get("Name")
        self._OcrNation = params.get("OcrNation")
        self._OcrAddress = params.get("OcrAddress")
        self._OcrBirth = params.get("OcrBirth")
        self._OcrAuthority = params.get("OcrAuthority")
        self._OcrValidDate = params.get("OcrValidDate")
        self._OcrName = params.get("OcrName")
        self._OcrIdCard = params.get("OcrIdCard")
        self._OcrGender = params.get("OcrGender")
        self._IdInfoFrom = params.get("IdInfoFrom")
        self._LiveStatus = params.get("LiveStatus")
        self._LiveMsg = params.get("LiveMsg")
        self._Comparestatus = params.get("Comparestatus")
        self._Comparemsg = params.get("Comparemsg")
        self._Sim = params.get("Sim")
        self._Location = params.get("Location")
        self._Extra = params.get("Extra")
        if params.get("LivenessDetail") is not None:
            self._LivenessDetail = []
            for item in params.get("LivenessDetail"):
                obj = DetectDetail()
                obj._deserialize(item)
                self._LivenessDetail.append(obj)
        self._Mobile = params.get("Mobile")
        self._CompareLibType = params.get("CompareLibType")
        self._LivenessMode = params.get("LivenessMode")
        self._NFCRequestIds = params.get("NFCRequestIds")
        self._NFCBillingCounts = params.get("NFCBillingCounts")
        self._PassNo = params.get("PassNo")
        self._VisaNum = params.get("VisaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoVideoData(AbstractModel):
    """核身视频信息

    """

    def __init__(self):
        r"""
        :param _LivenessVideo: 活体视频的base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessVideo: str
        """
        self._LivenessVideo = None

    @property
    def LivenessVideo(self):
        return self._LivenessVideo

    @LivenessVideo.setter
    def LivenessVideo(self, LivenessVideo):
        self._LivenessVideo = LivenessVideo


    def _deserialize(self, params):
        self._LivenessVideo = params.get("LivenessVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EidInfo(AbstractModel):
    """Eid出参，包括商户方用户的标识和加密的用户姓名身份证信息。

    """

    def __init__(self):
        r"""
        :param _EidCode: 商户方 appeIDcode 的数字证书
        :type EidCode: str
        :param _EidSign: Eid中心针对商户方EidCode的电子签名
        :type EidSign: str
        :param _DesKey: 商户方公钥加密的会话密钥的base64字符串，[指引详见](https://cloud.tencent.com/document/product/1007/63370)
        :type DesKey: str
        :param _UserInfo: 会话密钥sm2加密后的base64字符串，[指引详见](https://cloud.tencent.com/document/product/1007/63370)
        :type UserInfo: str
        """
        self._EidCode = None
        self._EidSign = None
        self._DesKey = None
        self._UserInfo = None

    @property
    def EidCode(self):
        return self._EidCode

    @EidCode.setter
    def EidCode(self, EidCode):
        self._EidCode = EidCode

    @property
    def EidSign(self):
        return self._EidSign

    @EidSign.setter
    def EidSign(self, EidSign):
        self._EidSign = EidSign

    @property
    def DesKey(self):
        return self._DesKey

    @DesKey.setter
    def DesKey(self, DesKey):
        self._DesKey = DesKey

    @property
    def UserInfo(self):
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo


    def _deserialize(self, params):
        self._EidCode = params.get("EidCode")
        self._EidSign = params.get("EidSign")
        self._DesKey = params.get("DesKey")
        self._UserInfo = params.get("UserInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptedPhoneVerificationRequest(AbstractModel):
    """EncryptedPhoneVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号，加密方式以EncryptionMode为准
        :type IdCard: str
        :param _Name: 姓名，加密方式以EncryptionMode为准
        :type Name: str
        :param _Phone: 手机号，加密方式以EncryptionMode为准
        :type Phone: str
        :param _EncryptionMode: 敏感信息的加密方式，目前支持明文、MD5和SHA256加密传输，参数取值：

0：明文，不加密
1：使用MD5加密
2：使用SHA256
3：使用SM3加密
        :type EncryptionMode: str
        """
        self._IdCard = None
        self._Name = None
        self._Phone = None
        self._EncryptionMode = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def EncryptionMode(self):
        return self._EncryptionMode

    @EncryptionMode.setter
    def EncryptionMode(self, EncryptionMode):
        self._EncryptionMode = EncryptionMode


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        self._EncryptionMode = params.get("EncryptionMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptedPhoneVerificationResponse(AbstractModel):
    """EncryptedPhoneVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码:
【收费结果码】
0:   三要素信息一致
-4:  三要素信息不一致

【不收费结果码】
-7: 身份证号码有误
-8: 参数错误
-9: 没有记录
-11: 验证中心服务繁忙
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _ISP: 运营商名称。
取值范围为["移动","联通","电信",""]
        :type ISP: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._ISP = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ISP(self):
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._ISP = params.get("ISP")
        self._RequestId = params.get("RequestId")


class Encryption(AbstractModel):
    """敏感数据加密

    """

    def __init__(self):
        r"""
        :param _EncryptList: 在使用加密服务时，填入要被加密的字段。本接口中可填入加密后的一个或多个字段
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptList: list of str
        :param _CiphertextBlob: 有加密需求的用户，接入传入kms的CiphertextBlob，关于数据加密可查阅<a href="https://cloud.tencent.com/document/product/1007/47180">数据加密</a> 文档。
注意：此字段可能返回 null，表示取不到有效值。
        :type CiphertextBlob: str
        :param _Iv: 有加密需求的用户，传入CBC加密的初始向量（客户自定义字符串，长度16字符）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Iv: str
        :param _Algorithm: 加密使用的算法（支持'AES-256-CBC'、'SM4-GCM'），不传默认为'AES-256-CBC'
注意：此字段可能返回 null，表示取不到有效值。
        :type Algorithm: str
        :param _TagList: SM4-GCM算法生成的消息摘要（校验消息完整性时使用）
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of str
        """
        self._EncryptList = None
        self._CiphertextBlob = None
        self._Iv = None
        self._Algorithm = None
        self._TagList = None

    @property
    def EncryptList(self):
        return self._EncryptList

    @EncryptList.setter
    def EncryptList(self, EncryptList):
        self._EncryptList = EncryptList

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def Iv(self):
        return self._Iv

    @Iv.setter
    def Iv(self, Iv):
        self._Iv = Iv

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._EncryptList = params.get("EncryptList")
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._Iv = params.get("Iv")
        self._Algorithm = params.get("Algorithm")
        self._TagList = params.get("TagList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraInfo(AbstractModel):
    """额外的详细信息

    """

    def __init__(self):
        r"""
        :param _RetrievalLivenessExtraInfo: 命中模板的详细信息，仅返回命中的相似度最高的模板信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RetrievalLivenessExtraInfo: list of RetrievalLivenessExtraInfo
        """
        self._RetrievalLivenessExtraInfo = None

    @property
    def RetrievalLivenessExtraInfo(self):
        return self._RetrievalLivenessExtraInfo

    @RetrievalLivenessExtraInfo.setter
    def RetrievalLivenessExtraInfo(self, RetrievalLivenessExtraInfo):
        self._RetrievalLivenessExtraInfo = RetrievalLivenessExtraInfo


    def _deserialize(self, params):
        if params.get("RetrievalLivenessExtraInfo") is not None:
            self._RetrievalLivenessExtraInfo = []
            for item in params.get("RetrievalLivenessExtraInfo"):
                obj = RetrievalLivenessExtraInfo()
                obj._deserialize(item)
                self._RetrievalLivenessExtraInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetActionSequenceRequest(AbstractModel):
    """GetActionSequence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionType: 默认不需要使用
        :type ActionType: str
        """
        self._ActionType = None

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetActionSequenceResponse(AbstractModel):
    """GetActionSequence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ActionSequence: 动作顺序(2,1 or 1,2) 。1代表张嘴，2代表闭眼。
        :type ActionSequence: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ActionSequence = None
        self._RequestId = None

    @property
    def ActionSequence(self):
        return self._ActionSequence

    @ActionSequence.setter
    def ActionSequence(self, ActionSequence):
        self._ActionSequence = ActionSequence

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActionSequence = params.get("ActionSequence")
        self._RequestId = params.get("RequestId")


class GetDetectInfoEnhancedRequest(AbstractModel):
    """GetDetectInfoEnhanced请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizToken: 人脸核身流程的标识，调用DetectAuth接口时生成。
        :type BizToken: str
        :param _RuleId: 用于细分客户使用场景，由腾讯侧在线下对接时分配。
        :type RuleId: str
        :param _InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证信息；3：视频最佳截图信息）。
如 13表示拉取文本类、视频最佳截图信息。
默认值：0
        :type InfoType: str
        :param _BestFramesCount: 从活体视频中截取一定张数的最佳帧（仅部分服务支持，若需使用请与慧眼小助手沟通）。默认为0，最大为10，超出10的最多只给10张。（InfoType需要包含3）
        :type BestFramesCount: int
        :param _IsCutIdCardImage: 是否对身份证照片进行裁边。默认为false。（InfoType需要包含2）
        :type IsCutIdCardImage: bool
        :param _IsNeedIdCardAvatar: 是否需要从身份证中抠出头像。默认为false。（InfoType需要包含2）
        :type IsNeedIdCardAvatar: bool
        :param _IsEncrypt: 已弃用。
        :type IsEncrypt: bool
        :param _Encryption: 是否需要对返回中的敏感信息进行加密。仅指定加密算法Algorithm即可，其余字段传入默认值。其中敏感信息包括：Response.Text.IdCard、Response.Text.Name、Response.Text.OcrIdCard、Response.Text.OcrName
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param _IsEncryptResponse: 是否对回包整体进行加密
        :type IsEncryptResponse: bool
        """
        self._BizToken = None
        self._RuleId = None
        self._InfoType = None
        self._BestFramesCount = None
        self._IsCutIdCardImage = None
        self._IsNeedIdCardAvatar = None
        self._IsEncrypt = None
        self._Encryption = None
        self._IsEncryptResponse = None

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def InfoType(self):
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType

    @property
    def BestFramesCount(self):
        return self._BestFramesCount

    @BestFramesCount.setter
    def BestFramesCount(self, BestFramesCount):
        self._BestFramesCount = BestFramesCount

    @property
    def IsCutIdCardImage(self):
        return self._IsCutIdCardImage

    @IsCutIdCardImage.setter
    def IsCutIdCardImage(self, IsCutIdCardImage):
        self._IsCutIdCardImage = IsCutIdCardImage

    @property
    def IsNeedIdCardAvatar(self):
        return self._IsNeedIdCardAvatar

    @IsNeedIdCardAvatar.setter
    def IsNeedIdCardAvatar(self, IsNeedIdCardAvatar):
        self._IsNeedIdCardAvatar = IsNeedIdCardAvatar

    @property
    def IsEncrypt(self):
        return self._IsEncrypt

    @IsEncrypt.setter
    def IsEncrypt(self, IsEncrypt):
        self._IsEncrypt = IsEncrypt

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def IsEncryptResponse(self):
        return self._IsEncryptResponse

    @IsEncryptResponse.setter
    def IsEncryptResponse(self, IsEncryptResponse):
        self._IsEncryptResponse = IsEncryptResponse


    def _deserialize(self, params):
        self._BizToken = params.get("BizToken")
        self._RuleId = params.get("RuleId")
        self._InfoType = params.get("InfoType")
        self._BestFramesCount = params.get("BestFramesCount")
        self._IsCutIdCardImage = params.get("IsCutIdCardImage")
        self._IsNeedIdCardAvatar = params.get("IsNeedIdCardAvatar")
        self._IsEncrypt = params.get("IsEncrypt")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        self._IsEncryptResponse = params.get("IsEncryptResponse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDetectInfoEnhancedResponse(AbstractModel):
    """GetDetectInfoEnhanced返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 文本类信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.faceid.v20180301.models.DetectInfoText`
        :param _IdCardData: 身份证照片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoIdCardData`
        :param _BestFrame: 最佳帧信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.DetectInfoBestFrame`
        :param _VideoData: 视频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoVideoData`
        :param _Encryption: 敏感数据加密信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param _IntentionVerifyData: 意愿核身朗读模式结果信息。若未使用意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyData: :class:`tencentcloud.faceid.v20180301.models.IntentionVerifyData`
        :param _IntentionQuestionResult: 意愿核身问答模式结果。若未使用该意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionQuestionResult: :class:`tencentcloud.faceid.v20180301.models.IntentionQuestionResult`
        :param _IntentionActionResult: 意愿核身点头确认模式的结果信息，若未使用该意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionActionResult: :class:`tencentcloud.faceid.v20180301.models.IntentionActionResult`
        :param _EncryptedBody: 加密后的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptedBody: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Text = None
        self._IdCardData = None
        self._BestFrame = None
        self._VideoData = None
        self._Encryption = None
        self._IntentionVerifyData = None
        self._IntentionQuestionResult = None
        self._IntentionActionResult = None
        self._EncryptedBody = None
        self._RequestId = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def IdCardData(self):
        return self._IdCardData

    @IdCardData.setter
    def IdCardData(self, IdCardData):
        self._IdCardData = IdCardData

    @property
    def BestFrame(self):
        return self._BestFrame

    @BestFrame.setter
    def BestFrame(self, BestFrame):
        self._BestFrame = BestFrame

    @property
    def VideoData(self):
        return self._VideoData

    @VideoData.setter
    def VideoData(self, VideoData):
        self._VideoData = VideoData

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def IntentionVerifyData(self):
        return self._IntentionVerifyData

    @IntentionVerifyData.setter
    def IntentionVerifyData(self, IntentionVerifyData):
        self._IntentionVerifyData = IntentionVerifyData

    @property
    def IntentionQuestionResult(self):
        return self._IntentionQuestionResult

    @IntentionQuestionResult.setter
    def IntentionQuestionResult(self, IntentionQuestionResult):
        self._IntentionQuestionResult = IntentionQuestionResult

    @property
    def IntentionActionResult(self):
        return self._IntentionActionResult

    @IntentionActionResult.setter
    def IntentionActionResult(self, IntentionActionResult):
        self._IntentionActionResult = IntentionActionResult

    @property
    def EncryptedBody(self):
        return self._EncryptedBody

    @EncryptedBody.setter
    def EncryptedBody(self, EncryptedBody):
        self._EncryptedBody = EncryptedBody

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self._Text = DetectInfoText()
            self._Text._deserialize(params.get("Text"))
        if params.get("IdCardData") is not None:
            self._IdCardData = DetectInfoIdCardData()
            self._IdCardData._deserialize(params.get("IdCardData"))
        if params.get("BestFrame") is not None:
            self._BestFrame = DetectInfoBestFrame()
            self._BestFrame._deserialize(params.get("BestFrame"))
        if params.get("VideoData") is not None:
            self._VideoData = DetectInfoVideoData()
            self._VideoData._deserialize(params.get("VideoData"))
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        if params.get("IntentionVerifyData") is not None:
            self._IntentionVerifyData = IntentionVerifyData()
            self._IntentionVerifyData._deserialize(params.get("IntentionVerifyData"))
        if params.get("IntentionQuestionResult") is not None:
            self._IntentionQuestionResult = IntentionQuestionResult()
            self._IntentionQuestionResult._deserialize(params.get("IntentionQuestionResult"))
        if params.get("IntentionActionResult") is not None:
            self._IntentionActionResult = IntentionActionResult()
            self._IntentionActionResult._deserialize(params.get("IntentionActionResult"))
        self._EncryptedBody = params.get("EncryptedBody")
        self._RequestId = params.get("RequestId")


class GetDetectInfoRequest(AbstractModel):
    """GetDetectInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizToken: 人脸核身流程的标识，调用DetectAuth接口时生成。
        :type BizToken: str
        :param _RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请加慧眼小助手微信（faceid001）进行咨询。
        :type RuleId: str
        :param _InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证正反面；3：视频最佳截图照片；4：视频）。
如 134表示拉取文本类、视频最佳截图照片、视频。
默认值：0
        :type InfoType: str
        """
        self._BizToken = None
        self._RuleId = None
        self._InfoType = None

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def InfoType(self):
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType


    def _deserialize(self, params):
        self._BizToken = params.get("BizToken")
        self._RuleId = params.get("RuleId")
        self._InfoType = params.get("InfoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDetectInfoResponse(AbstractModel):
    """GetDetectInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DetectInfo: JSON字符串。
{
  // 文本类信息
  "Text": {
    "ErrCode": null,      // 本次核身最终结果。0为成功
    "ErrMsg": null,       // 本次核身最终结果信息描述。
    "IdCard": "",         // 本次核身最终获得的身份证号。
    "Name": "",           // 本次核身最终获得的姓名。
    "OcrNation": null,    // ocr阶段获取的民族
    "OcrAddress": null,   // ocr阶段获取的地址
    "OcrBirth": null,     // ocr阶段获取的出生信息
    "OcrAuthority": null, // ocr阶段获取的证件签发机关
    "OcrValidDate": null, // ocr阶段获取的证件有效期
    "OcrName": null,      // ocr阶段获取的姓名
    "OcrIdCard": null,    // ocr阶段获取的身份证号
    "OcrGender": null,    // ocr阶段获取的性别
    "LiveStatus": null,   // 活体检测阶段的错误码。0为成功
    "LiveMsg": null,      // 活体检测阶段的错误信息
    "Comparestatus": null,// 一比一阶段的错误码。0为成功
    "Comparemsg": null,   // 一比一阶段的错误信息
    "Sim": null, // 比对相似度
    "Location": null, // 地理位置信息
    "Extra": "",          // DetectAuth结果传进来的Extra信息
    "Detail": {           // 活体一比一信息详情
      "LivenessData": [
            {
              ErrCode: null, // 活体比对验证错误码
              ErrMsg: null, // 活体比对验证错误描述
              ReqTime: null, // 活体验证时间戳
              IdCard: null, // 验证身份证号
              Name: null // 验证姓名
            }
      ]
    }
  },
  // 身份证正反面照片Base64
  "IdCardData": {
    "OcrFront": null,
    "OcrBack": null
  },
  // 视频最佳帧截图Base64
  "BestFrame": {
    "BestFrame": null
  },
  // 活体视频Base64
  "VideoData": {
    "LivenessVideo": null
  }
}
        :type DetectInfo: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DetectInfo = None
        self._RequestId = None

    @property
    def DetectInfo(self):
        return self._DetectInfo

    @DetectInfo.setter
    def DetectInfo(self, DetectInfo):
        self._DetectInfo = DetectInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DetectInfo = params.get("DetectInfo")
        self._RequestId = params.get("RequestId")


class GetEidResultRequest(AbstractModel):
    """GetEidResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EidToken: E证通流程的唯一标识，调用GetEidToken接口时生成。
        :type EidToken: str
        :param _InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证信息；3：最佳截图信息；5：意愿核身朗读模式相关结果；6：意愿核身问答模式相关结果）。
如 13表示拉取文本类、最佳截图信息。
默认值：0
        :type InfoType: str
        :param _BestFramesCount: 从活体视频中截取一定张数的最佳帧。默认为0，最大为3，超出3的最多只给3张。（InfoType需要包含3）
        :type BestFramesCount: int
        :param _IsCutIdCardImage: 是否对身份证照片进行裁边。默认为false。（InfoType需要包含2）
        :type IsCutIdCardImage: bool
        :param _IsNeedIdCardAvatar: 是否需要从身份证中抠出头像。默认为false。（InfoType需要包含2）
        :type IsNeedIdCardAvatar: bool
        """
        self._EidToken = None
        self._InfoType = None
        self._BestFramesCount = None
        self._IsCutIdCardImage = None
        self._IsNeedIdCardAvatar = None

    @property
    def EidToken(self):
        return self._EidToken

    @EidToken.setter
    def EidToken(self, EidToken):
        self._EidToken = EidToken

    @property
    def InfoType(self):
        return self._InfoType

    @InfoType.setter
    def InfoType(self, InfoType):
        self._InfoType = InfoType

    @property
    def BestFramesCount(self):
        return self._BestFramesCount

    @BestFramesCount.setter
    def BestFramesCount(self, BestFramesCount):
        self._BestFramesCount = BestFramesCount

    @property
    def IsCutIdCardImage(self):
        return self._IsCutIdCardImage

    @IsCutIdCardImage.setter
    def IsCutIdCardImage(self, IsCutIdCardImage):
        self._IsCutIdCardImage = IsCutIdCardImage

    @property
    def IsNeedIdCardAvatar(self):
        return self._IsNeedIdCardAvatar

    @IsNeedIdCardAvatar.setter
    def IsNeedIdCardAvatar(self, IsNeedIdCardAvatar):
        self._IsNeedIdCardAvatar = IsNeedIdCardAvatar


    def _deserialize(self, params):
        self._EidToken = params.get("EidToken")
        self._InfoType = params.get("InfoType")
        self._BestFramesCount = params.get("BestFramesCount")
        self._IsCutIdCardImage = params.get("IsCutIdCardImage")
        self._IsNeedIdCardAvatar = params.get("IsNeedIdCardAvatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEidResultResponse(AbstractModel):
    """GetEidResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 文本类信息。（基于对敏感信息的保护，验证使用的姓名和身份证号统一通过加密后从Eidinfo参数中返回，如需获取请在控制台申请返回身份信息，详见[E证通获取实名信息指引](https://cloud.tencent.com/document/product/1007/63370)）
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.faceid.v20180301.models.DetectInfoText`
        :param _IdCardData: 身份证照片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoIdCardData`
        :param _BestFrame: 最佳帧信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.DetectInfoBestFrame`
        :param _EidInfo: Eid信息。（包括商户下用户唯一标识以及加密后的姓名、身份证号信息。解密方式详见[E证通获取实名信息指引](https://cloud.tencent.com/document/product/1007/63370)）
注意：此字段可能返回 null，表示取不到有效值。
        :type EidInfo: :class:`tencentcloud.faceid.v20180301.models.EidInfo`
        :param _IntentionVerifyData: 意愿核身朗读模式相关信息。若未使用意愿核身朗读功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyData: :class:`tencentcloud.faceid.v20180301.models.IntentionVerifyData`
        :param _IntentionQuestionResult: 意愿核身问答模式相关信息。若未使用意愿核身问答模式功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionQuestionResult: :class:`tencentcloud.faceid.v20180301.models.IntentionQuestionResult`
        :param _IntentionActionResult: 意愿核身点头确认模式的结果信息，若未使用该意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionActionResult: :class:`tencentcloud.faceid.v20180301.models.IntentionActionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Text = None
        self._IdCardData = None
        self._BestFrame = None
        self._EidInfo = None
        self._IntentionVerifyData = None
        self._IntentionQuestionResult = None
        self._IntentionActionResult = None
        self._RequestId = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def IdCardData(self):
        return self._IdCardData

    @IdCardData.setter
    def IdCardData(self, IdCardData):
        self._IdCardData = IdCardData

    @property
    def BestFrame(self):
        return self._BestFrame

    @BestFrame.setter
    def BestFrame(self, BestFrame):
        self._BestFrame = BestFrame

    @property
    def EidInfo(self):
        return self._EidInfo

    @EidInfo.setter
    def EidInfo(self, EidInfo):
        self._EidInfo = EidInfo

    @property
    def IntentionVerifyData(self):
        return self._IntentionVerifyData

    @IntentionVerifyData.setter
    def IntentionVerifyData(self, IntentionVerifyData):
        self._IntentionVerifyData = IntentionVerifyData

    @property
    def IntentionQuestionResult(self):
        return self._IntentionQuestionResult

    @IntentionQuestionResult.setter
    def IntentionQuestionResult(self, IntentionQuestionResult):
        self._IntentionQuestionResult = IntentionQuestionResult

    @property
    def IntentionActionResult(self):
        return self._IntentionActionResult

    @IntentionActionResult.setter
    def IntentionActionResult(self, IntentionActionResult):
        self._IntentionActionResult = IntentionActionResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self._Text = DetectInfoText()
            self._Text._deserialize(params.get("Text"))
        if params.get("IdCardData") is not None:
            self._IdCardData = DetectInfoIdCardData()
            self._IdCardData._deserialize(params.get("IdCardData"))
        if params.get("BestFrame") is not None:
            self._BestFrame = DetectInfoBestFrame()
            self._BestFrame._deserialize(params.get("BestFrame"))
        if params.get("EidInfo") is not None:
            self._EidInfo = EidInfo()
            self._EidInfo._deserialize(params.get("EidInfo"))
        if params.get("IntentionVerifyData") is not None:
            self._IntentionVerifyData = IntentionVerifyData()
            self._IntentionVerifyData._deserialize(params.get("IntentionVerifyData"))
        if params.get("IntentionQuestionResult") is not None:
            self._IntentionQuestionResult = IntentionQuestionResult()
            self._IntentionQuestionResult._deserialize(params.get("IntentionQuestionResult"))
        if params.get("IntentionActionResult") is not None:
            self._IntentionActionResult = IntentionActionResult()
            self._IntentionActionResult._deserialize(params.get("IntentionActionResult"))
        self._RequestId = params.get("RequestId")


class GetEidTokenConfig(AbstractModel):
    """获取token时的配置

    """

    def __init__(self):
        r"""
        :param _InputType: 姓名身份证输入方式。
1：传身份证正反面OCR   
2：传身份证正面OCR  
3：用户手动输入  
4：客户后台传入  
默认1
注：使用OCR时仅支持用户修改结果中的姓名
        :type InputType: str
        :param _UseIntentionVerify: 是否使用意愿核身，默认不使用。注意：如开启使用，则计费标签按【意愿核身】计费标签计价；如不开启，则计费标签按【E证通】计费标签计价，价格详见：[价格说明](https://cloud.tencent.com/document/product/1007/56804)。
        :type UseIntentionVerify: bool
        :param _IntentionMode: 意愿核身模式。枚举值：1( 语音朗读模式)，2（语音问答模式） ，3（点头确认模式）。默认值为1。
        :type IntentionMode: str
        :param _IntentionVerifyText: 意愿核身朗读模式使用的文案，若未使用意愿核身朗读功能，该字段无需传入。默认为空，最长可接受120的字符串长度。
        :type IntentionVerifyText: str
        :param _IntentionQuestions: 意愿核身问答模式的配置列表。当前仅支持一个问答。
        :type IntentionQuestions: list of IntentionQuestion
        :param _IntentionActions: 意愿核身（点头确认模式）使用的文案，若未使用意愿核身（点头确认模式），则该字段无需传入。默认为空，最长可接受150的字符串长度。
        :type IntentionActions: list of IntentionActionConfig
        :param _IntentionRecognition: 意愿核身过程中识别用户的回答意图，开启后除了IntentionQuestions的Answers列表中的标准回答会通过，近似意图的回答也会通过，默认开启。
        :type IntentionRecognition: bool
        :param _IsSupportHMTResidentPermitOCR: 是否支持港澳台居住证识别
        :type IsSupportHMTResidentPermitOCR: bool
        :param _MouthOpenRecognition: 用户语音回答过程中是否开启张嘴识别检测，默认不开启，仅在意愿核身问答模式中使用。
        :type MouthOpenRecognition: bool
        """
        self._InputType = None
        self._UseIntentionVerify = None
        self._IntentionMode = None
        self._IntentionVerifyText = None
        self._IntentionQuestions = None
        self._IntentionActions = None
        self._IntentionRecognition = None
        self._IsSupportHMTResidentPermitOCR = None
        self._MouthOpenRecognition = None

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def UseIntentionVerify(self):
        return self._UseIntentionVerify

    @UseIntentionVerify.setter
    def UseIntentionVerify(self, UseIntentionVerify):
        self._UseIntentionVerify = UseIntentionVerify

    @property
    def IntentionMode(self):
        return self._IntentionMode

    @IntentionMode.setter
    def IntentionMode(self, IntentionMode):
        self._IntentionMode = IntentionMode

    @property
    def IntentionVerifyText(self):
        return self._IntentionVerifyText

    @IntentionVerifyText.setter
    def IntentionVerifyText(self, IntentionVerifyText):
        self._IntentionVerifyText = IntentionVerifyText

    @property
    def IntentionQuestions(self):
        return self._IntentionQuestions

    @IntentionQuestions.setter
    def IntentionQuestions(self, IntentionQuestions):
        self._IntentionQuestions = IntentionQuestions

    @property
    def IntentionActions(self):
        return self._IntentionActions

    @IntentionActions.setter
    def IntentionActions(self, IntentionActions):
        self._IntentionActions = IntentionActions

    @property
    def IntentionRecognition(self):
        return self._IntentionRecognition

    @IntentionRecognition.setter
    def IntentionRecognition(self, IntentionRecognition):
        self._IntentionRecognition = IntentionRecognition

    @property
    def IsSupportHMTResidentPermitOCR(self):
        return self._IsSupportHMTResidentPermitOCR

    @IsSupportHMTResidentPermitOCR.setter
    def IsSupportHMTResidentPermitOCR(self, IsSupportHMTResidentPermitOCR):
        self._IsSupportHMTResidentPermitOCR = IsSupportHMTResidentPermitOCR

    @property
    def MouthOpenRecognition(self):
        return self._MouthOpenRecognition

    @MouthOpenRecognition.setter
    def MouthOpenRecognition(self, MouthOpenRecognition):
        self._MouthOpenRecognition = MouthOpenRecognition


    def _deserialize(self, params):
        self._InputType = params.get("InputType")
        self._UseIntentionVerify = params.get("UseIntentionVerify")
        self._IntentionMode = params.get("IntentionMode")
        self._IntentionVerifyText = params.get("IntentionVerifyText")
        if params.get("IntentionQuestions") is not None:
            self._IntentionQuestions = []
            for item in params.get("IntentionQuestions"):
                obj = IntentionQuestion()
                obj._deserialize(item)
                self._IntentionQuestions.append(obj)
        if params.get("IntentionActions") is not None:
            self._IntentionActions = []
            for item in params.get("IntentionActions"):
                obj = IntentionActionConfig()
                obj._deserialize(item)
                self._IntentionActions.append(obj)
        self._IntentionRecognition = params.get("IntentionRecognition")
        self._IsSupportHMTResidentPermitOCR = params.get("IsSupportHMTResidentPermitOCR")
        self._MouthOpenRecognition = params.get("MouthOpenRecognition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEidTokenRequest(AbstractModel):
    """GetEidToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MerchantId: EID商户id，字段长度最长50位。
        :type MerchantId: str
        :param _IdCard: 身份标识（未使用OCR服务时，必须传入）。
规则：a-z，A-Z，0-9组合。最长长度32位。
        :type IdCard: str
        :param _Name: 姓名。（未使用OCR服务时，必须传入）最长长度32位。中文请使用UTF-8编码。
        :type Name: str
        :param _Extra: 透传字段，在获取验证结果时返回。最长长度1024位。
        :type Extra: str
        :param _Config: 小程序模式配置，包括如何传入姓名身份证的配置，以及是否使用意愿核身。
        :type Config: :class:`tencentcloud.faceid.v20180301.models.GetEidTokenConfig`
        :param _RedirectUrl: 最长长度1024位。用户从Url中进入核身认证结束后重定向的回调链接地址。EidToken会在该链接的query参数中。
        :type RedirectUrl: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._MerchantId = None
        self._IdCard = None
        self._Name = None
        self._Extra = None
        self._Config = None
        self._RedirectUrl = None
        self._Encryption = None

    @property
    def MerchantId(self):
        return self._MerchantId

    @MerchantId.setter
    def MerchantId(self, MerchantId):
        self._MerchantId = MerchantId

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._MerchantId = params.get("MerchantId")
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._Extra = params.get("Extra")
        if params.get("Config") is not None:
            self._Config = GetEidTokenConfig()
            self._Config._deserialize(params.get("Config"))
        self._RedirectUrl = params.get("RedirectUrl")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEidTokenResponse(AbstractModel):
    """GetEidToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EidToken: 一次核身流程的标识，有效时间为600秒；
完成核身后，可用该标识获取验证结果信息。
        :type EidToken: str
        :param _Url: 发起核身流程的URL，用于H5场景核身。
        :type Url: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EidToken = None
        self._Url = None
        self._RequestId = None

    @property
    def EidToken(self):
        return self._EidToken

    @EidToken.setter
    def EidToken(self, EidToken):
        self._EidToken = EidToken

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EidToken = params.get("EidToken")
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class GetFaceIdResultRequest(AbstractModel):
    """GetFaceIdResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceIdToken: SDK人脸核身流程的标识，调用GetFaceIdToken接口时生成。
        :type FaceIdToken: str
        :param _IsNeedVideo: 是否需要拉取视频，默认false不需要
        :type IsNeedVideo: bool
        :param _IsNeedBestFrame: 是否需要拉取截帧，默认false不需要
        :type IsNeedBestFrame: bool
        """
        self._FaceIdToken = None
        self._IsNeedVideo = None
        self._IsNeedBestFrame = None

    @property
    def FaceIdToken(self):
        return self._FaceIdToken

    @FaceIdToken.setter
    def FaceIdToken(self, FaceIdToken):
        self._FaceIdToken = FaceIdToken

    @property
    def IsNeedVideo(self):
        return self._IsNeedVideo

    @IsNeedVideo.setter
    def IsNeedVideo(self, IsNeedVideo):
        self._IsNeedVideo = IsNeedVideo

    @property
    def IsNeedBestFrame(self):
        return self._IsNeedBestFrame

    @IsNeedBestFrame.setter
    def IsNeedBestFrame(self, IsNeedBestFrame):
        self._IsNeedBestFrame = IsNeedBestFrame


    def _deserialize(self, params):
        self._FaceIdToken = params.get("FaceIdToken")
        self._IsNeedVideo = params.get("IsNeedVideo")
        self._IsNeedBestFrame = params.get("IsNeedBestFrame")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFaceIdResultResponse(AbstractModel):
    """GetFaceIdResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _Result: 业务核验结果，参考https://cloud.tencent.com/document/product/1007/47912
        :type Result: str
        :param _Description: 业务核验描述
        :type Description: str
        :param _Similarity: 相似度，0-100，数值越大相似度越高
        :type Similarity: float
        :param _VideoBase64: 用户核验的视频base64，如果选择了使用cos，返回完整cos地址如https://bucket.cos.ap-guangzhou.myqcloud.com/objectKey
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoBase64: str
        :param _BestFrameBase64: 用户核验视频的截帧base64，如果选择了使用cos，返回完整cos地址如https://bucket.cos.ap-guangzhou.myqcloud.com/objectKey
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param _Extra: 获取token时透传的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _DeviceInfoTag: plus版：描述当前请求所在设备的风险标签，详情如下：
01-设备疑似被Root/设备疑似越狱
02-设备疑似被注入
03-设备疑似为模拟器
04-设备疑似存在风险操作
05-摄像头疑似被劫持
06-疑似黑产设备
null-无设备风险
增强版：此字段不生效，默认为null
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceInfoTag: str
        :param _RiskInfoTag: 行为风险标签，仅错误码返回1007（设备疑似被劫持）时返回风险标签。标签说明：
02：攻击风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfoTag: str
        :param _LivenessInfoTag: plus版：描述当前请求活体阶段被拒绝的详细原因，详情如下：01-用户全程闭眼02-用户未完成指定动作03-疑似翻拍攻击04-疑似合成图片05-疑似合成视频06-疑似合成动作07-疑似黑产模板08-疑似存在水印09-反光校验未通过10-最佳帧校验未通过11-人脸质量过差12-人脸距离不匹配13-疑似对抗样本攻击null-无增强版：此字段不生效，默认为null
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessInfoTag: str
        :param _DeviceInfoLevel: plus版：描述当前请求所在设备的风险等级，共4级，详情如下：
1 - 安全
2 - 低风险
3 - 中风险
4 - 高危
null - 未获取到风险等级
增强版：此字段不生效，默认为null
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceInfoLevel: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdCard = None
        self._Name = None
        self._Result = None
        self._Description = None
        self._Similarity = None
        self._VideoBase64 = None
        self._BestFrameBase64 = None
        self._Extra = None
        self._DeviceInfoTag = None
        self._RiskInfoTag = None
        self._LivenessInfoTag = None
        self._DeviceInfoLevel = None
        self._RequestId = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def VideoBase64(self):
        return self._VideoBase64

    @VideoBase64.setter
    def VideoBase64(self, VideoBase64):
        self._VideoBase64 = VideoBase64

    @property
    def BestFrameBase64(self):
        return self._BestFrameBase64

    @BestFrameBase64.setter
    def BestFrameBase64(self, BestFrameBase64):
        self._BestFrameBase64 = BestFrameBase64

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def DeviceInfoTag(self):
        return self._DeviceInfoTag

    @DeviceInfoTag.setter
    def DeviceInfoTag(self, DeviceInfoTag):
        self._DeviceInfoTag = DeviceInfoTag

    @property
    def RiskInfoTag(self):
        return self._RiskInfoTag

    @RiskInfoTag.setter
    def RiskInfoTag(self, RiskInfoTag):
        self._RiskInfoTag = RiskInfoTag

    @property
    def LivenessInfoTag(self):
        return self._LivenessInfoTag

    @LivenessInfoTag.setter
    def LivenessInfoTag(self, LivenessInfoTag):
        self._LivenessInfoTag = LivenessInfoTag

    @property
    def DeviceInfoLevel(self):
        return self._DeviceInfoLevel

    @DeviceInfoLevel.setter
    def DeviceInfoLevel(self, DeviceInfoLevel):
        self._DeviceInfoLevel = DeviceInfoLevel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Similarity = params.get("Similarity")
        self._VideoBase64 = params.get("VideoBase64")
        self._BestFrameBase64 = params.get("BestFrameBase64")
        self._Extra = params.get("Extra")
        self._DeviceInfoTag = params.get("DeviceInfoTag")
        self._RiskInfoTag = params.get("RiskInfoTag")
        self._LivenessInfoTag = params.get("LivenessInfoTag")
        self._DeviceInfoLevel = params.get("DeviceInfoLevel")
        self._RequestId = params.get("RequestId")


class GetFaceIdRiskInfoRequest(AbstractModel):
    """GetFaceIdRiskInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceIdToken: SDK人脸核身流程的标识，调用GetFaceidRiskInfoToken接口时生成。
        :type FaceIdToken: str
        """
        self._FaceIdToken = None

    @property
    def FaceIdToken(self):
        return self._FaceIdToken

    @FaceIdToken.setter
    def FaceIdToken(self, FaceIdToken):
        self._FaceIdToken = FaceIdToken


    def _deserialize(self, params):
        self._FaceIdToken = params.get("FaceIdToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFaceIdRiskInfoResponse(AbstractModel):
    """GetFaceIdRiskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceInfoTag: 描述当前请求所在设备的风险标签，详情如下： 01-设备疑似被Root/设备疑似越狱 02-设备疑似被注入 03-设备疑似为模拟器 04-设备疑似存在风险操作 05-摄像头疑似被劫持 06-疑似黑产设备
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceInfoTag: str
        :param _DeviceInfoLevel: 描述当前请求所在设备的风险等级，共4级，详情如下： 1 - 低风险 2 - 中风险 3 - 高风险 4 - 攻击 ，-1表示未获取到风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceInfoLevel: int
        :param _OpenId: 设备id标识
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _CameraInfoLevel: 描述当前请求所在设备的相机指纹风险等级，共4级，详情如下： 1 - 低风险 2 - 中风险 3 - 高风险 4 - 攻击 ，-1表示未获取到风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type CameraInfoLevel: int
        :param _CameraInfoTag: 描述当前请求所在设备的相机指纹风险标签，详情如下： 01-设备疑似被Root/设备疑似越狱 02-设备疑似被注入 03-设备疑似为模拟器 04-设备疑似存在风险操作 05-摄像头疑似被劫持 06-疑似黑产设备，空表示没有相机指纹风险
注意：此字段可能返回 null，表示取不到有效值。
        :type CameraInfoTag: str
        :param _Extra: 获取token时透传的信息	
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceInfoTag = None
        self._DeviceInfoLevel = None
        self._OpenId = None
        self._CameraInfoLevel = None
        self._CameraInfoTag = None
        self._Extra = None
        self._RequestId = None

    @property
    def DeviceInfoTag(self):
        return self._DeviceInfoTag

    @DeviceInfoTag.setter
    def DeviceInfoTag(self, DeviceInfoTag):
        self._DeviceInfoTag = DeviceInfoTag

    @property
    def DeviceInfoLevel(self):
        return self._DeviceInfoLevel

    @DeviceInfoLevel.setter
    def DeviceInfoLevel(self, DeviceInfoLevel):
        self._DeviceInfoLevel = DeviceInfoLevel

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def CameraInfoLevel(self):
        return self._CameraInfoLevel

    @CameraInfoLevel.setter
    def CameraInfoLevel(self, CameraInfoLevel):
        self._CameraInfoLevel = CameraInfoLevel

    @property
    def CameraInfoTag(self):
        return self._CameraInfoTag

    @CameraInfoTag.setter
    def CameraInfoTag(self, CameraInfoTag):
        self._CameraInfoTag = CameraInfoTag

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceInfoTag = params.get("DeviceInfoTag")
        self._DeviceInfoLevel = params.get("DeviceInfoLevel")
        self._OpenId = params.get("OpenId")
        self._CameraInfoLevel = params.get("CameraInfoLevel")
        self._CameraInfoTag = params.get("CameraInfoTag")
        self._Extra = params.get("Extra")
        self._RequestId = params.get("RequestId")


class GetFaceIdTokenRequest(AbstractModel):
    """GetFaceIdToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompareLib: 本地上传照片(LOCAL)、商业库(BUSINESS)
        :type CompareLib: str
        :param _IdCard: CompareLib为商业库时必传。
        :type IdCard: str
        :param _Name: CompareLib为商业库时必传。
        :type Name: str
        :param _ImageBase64: CompareLib为上传照片比对时必传，Base64后图片最大8MB。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param _Meta: SDK中生成的Meta字符串
        :type Meta: str
        :param _Extra: 透传参数 1000长度字符串
        :type Extra: str
        :param _UseCos: 默认为false，设置该参数为true后，核身过程中的视频图片将会存储在人脸核身控制台授权cos的bucket中，拉取结果时会返回对应资源完整cos地址。开通地址见https://console.cloud.tencent.com/faceid/cos
【注意】选择该参数为true后将不返回base64数据，请根据接入情况谨慎修改。
        :type UseCos: bool
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param _RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请添加腾讯云人脸核身小助手进行咨询。
示例值：1
        :type RuleId: str
        """
        self._CompareLib = None
        self._IdCard = None
        self._Name = None
        self._ImageBase64 = None
        self._Meta = None
        self._Extra = None
        self._UseCos = None
        self._Encryption = None
        self._RuleId = None

    @property
    def CompareLib(self):
        return self._CompareLib

    @CompareLib.setter
    def CompareLib(self, CompareLib):
        self._CompareLib = CompareLib

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Meta(self):
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def UseCos(self):
        return self._UseCos

    @UseCos.setter
    def UseCos(self, UseCos):
        self._UseCos = UseCos

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._CompareLib = params.get("CompareLib")
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._ImageBase64 = params.get("ImageBase64")
        self._Meta = params.get("Meta")
        self._Extra = params.get("Extra")
        self._UseCos = params.get("UseCos")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFaceIdTokenResponse(AbstractModel):
    """GetFaceIdToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceIdToken: 有效期 10分钟。只能完成1次核身。
        :type FaceIdToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceIdToken = None
        self._RequestId = None

    @property
    def FaceIdToken(self):
        return self._FaceIdToken

    @FaceIdToken.setter
    def FaceIdToken(self, FaceIdToken):
        self._FaceIdToken = FaceIdToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceIdToken = params.get("FaceIdToken")
        self._RequestId = params.get("RequestId")


class GetFaceidRiskInfoTokenRequest(AbstractModel):
    """GetFaceidRiskInfoToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Meta: SDK中生成的Meta字符串
        :type Meta: str
        :param _Extra: 透传参数 1000长度字符串
        :type Extra: str
        """
        self._Meta = None
        self._Extra = None

    @property
    def Meta(self):
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra


    def _deserialize(self, params):
        self._Meta = params.get("Meta")
        self._Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFaceidRiskInfoTokenResponse(AbstractModel):
    """GetFaceidRiskInfoToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceIdToken: 有效期 10分钟。只能完成1次核身。
        :type FaceIdToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceIdToken = None
        self._RequestId = None

    @property
    def FaceIdToken(self):
        return self._FaceIdToken

    @FaceIdToken.setter
    def FaceIdToken(self, FaceIdToken):
        self._FaceIdToken = FaceIdToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceIdToken = params.get("FaceIdToken")
        self._RequestId = params.get("RequestId")


class GetLiveCodeRequest(AbstractModel):
    """GetLiveCode请求参数结构体

    """


class GetLiveCodeResponse(AbstractModel):
    """GetLiveCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LiveCode: 数字验证码，如：1234
        :type LiveCode: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LiveCode = None
        self._RequestId = None

    @property
    def LiveCode(self):
        return self._LiveCode

    @LiveCode.setter
    def LiveCode(self, LiveCode):
        self._LiveCode = LiveCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LiveCode = params.get("LiveCode")
        self._RequestId = params.get("RequestId")


class GetWeChatBillDetailsRequest(AbstractModel):
    """GetWeChatBillDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Date: 拉取的日期（YYYY-MM-DD）。最大可追溯到365天前。当天6点后才能拉取前一天的数据。
        :type Date: str
        :param _Cursor: 游标。用于分页，取第一页时传0，取后续页面时，传入本接口响应中返回的NextCursor字段的值。
        :type Cursor: int
        :param _RuleId: 需要拉取账单详情业务对应的RuleId。不传会返回所有RuleId数据。默认为空字符串。
        :type RuleId: str
        """
        self._Date = None
        self._Cursor = None
        self._RuleId = None

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Cursor = params.get("Cursor")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWeChatBillDetailsResponse(AbstractModel):
    """GetWeChatBillDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HasNextPage: 是否还有下一页。该字段为true时，需要将NextCursor的值作为入参Cursor继续调用本接口。
        :type HasNextPage: bool
        :param _NextCursor: 下一页的游标。用于分页。
        :type NextCursor: int
        :param _WeChatBillDetails: 数据
        :type WeChatBillDetails: list of WeChatBillDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HasNextPage = None
        self._NextCursor = None
        self._WeChatBillDetails = None
        self._RequestId = None

    @property
    def HasNextPage(self):
        return self._HasNextPage

    @HasNextPage.setter
    def HasNextPage(self, HasNextPage):
        self._HasNextPage = HasNextPage

    @property
    def NextCursor(self):
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def WeChatBillDetails(self):
        return self._WeChatBillDetails

    @WeChatBillDetails.setter
    def WeChatBillDetails(self, WeChatBillDetails):
        self._WeChatBillDetails = WeChatBillDetails

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HasNextPage = params.get("HasNextPage")
        self._NextCursor = params.get("NextCursor")
        if params.get("WeChatBillDetails") is not None:
            self._WeChatBillDetails = []
            for item in params.get("WeChatBillDetails"):
                obj = WeChatBillDetail()
                obj._deserialize(item)
                self._WeChatBillDetails.append(obj)
        self._RequestId = params.get("RequestId")


class IdCardOCRVerificationRequest(AbstractModel):
    """IdCardOCRVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
姓名和身份证号、ImageBase64、ImageUrl三者必须提供其中之一。若都提供了，则按照姓名和身份证号>ImageBase64>ImageUrl的优先级使用参数。
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _ImageBase64: 身份证人像面的 Base64 值
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param _ImageUrl: 身份证人像面的 Url 地址
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdCardOCRVerificationResponse(AbstractModel):
    """IdCardOCRVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 姓名和身份证号一致
-1: 姓名和身份证号不一致
不收费结果码：
-2: 非法身份证号（长度、校验位等不正确）
-3: 非法姓名（长度、格式等不正确）
-4: 证件库服务异常
-5: 证件库中无此身份证记录
-6: 权威比对系统升级中，请稍后再试
-7: 认证次数超过当日限制
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _Name: 用于验证的姓名
        :type Name: str
        :param _IdCard: 用于验证的身份证号
        :type IdCard: str
        :param _Sex: OCR得到的性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param _Nation: OCR得到的民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Nation: str
        :param _Birth: OCR得到的生日
注意：此字段可能返回 null，表示取不到有效值。
        :type Birth: str
        :param _Address: OCR得到的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._Name = None
        self._IdCard = None
        self._Sex = None
        self._Nation = None
        self._Birth = None
        self._Address = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def Birth(self):
        return self._Birth

    @Birth.setter
    def Birth(self, Birth):
        self._Birth = Birth

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._IdCard = params.get("IdCard")
        self._Sex = params.get("Sex")
        self._Nation = params.get("Nation")
        self._Birth = params.get("Birth")
        self._Address = params.get("Address")
        self._RequestId = params.get("RequestId")


class IdCardVerificationRequest(AbstractModel):
    """IdCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdCardVerificationResponse(AbstractModel):
    """IdCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 姓名和身份证号一致
-1: 姓名和身份证号不一致
不收费结果码：
-2: 非法身份证号（长度、校验位等不正确）
-3: 非法姓名（长度、格式等不正确）
-4: 证件库服务异常
-5: 证件库中无此身份证记录
-6: 权威比对系统升级中，请稍后再试
-7: 认证次数超过当日限制
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class ImageRecognitionRequest(AbstractModel):
    """ImageRecognition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名。中文请使用UTF-8编码。
        :type Name: str
        :param _ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param _Optional: 本接口不需要传递此参数。
        :type Optional: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._ImageBase64 = None
        self._Optional = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Optional(self):
        return self._Optional

    @Optional.setter
    def Optional(self, Optional):
        self._Optional = Optional

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._ImageBase64 = params.get("ImageBase64")
        self._Optional = params.get("Optional")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRecognitionResponse(AbstractModel):
    """ImageRecognition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param _Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Sim = None
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Sim = params.get("Sim")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class ImageRecognitionV2Request(AbstractModel):
    """ImageRecognitionV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名。中文请使用UTF-8编码。
        :type Name: str
        :param _ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param _Optional: 本接口不需要传递此参数。
        :type Optional: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._ImageBase64 = None
        self._Optional = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Optional(self):
        return self._Optional

    @Optional.setter
    def Optional(self, Optional):
        self._Optional = Optional

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._ImageBase64 = params.get("ImageBase64")
        self._Optional = params.get("Optional")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRecognitionV2Response(AbstractModel):
    """ImageRecognitionV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param _Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Sim = None
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Sim = params.get("Sim")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class IntentionActionConfig(AbstractModel):
    """意愿核身（点头确认模式）配置

    """

    def __init__(self):
        r"""
        :param _Text: 点头确认模式下，系统语音播报使用的问题文本，问题最大长度为150个字符。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionActionResult(AbstractModel):
    """意愿核身点头确认模式结果

    """

    def __init__(self):
        r"""
        :param _FinalResultDetailCode: 意愿核身错误码：
0: "成功"       
-1: "参数错误"    
-2: "系统异常"    
-101: "请保持人脸在框内"    
-102: "检测到多张人脸"   
-103: "人脸检测失败"   
-104: "人脸检测不完整"   
-105: "请勿遮挡眼睛"    
-106: "请勿遮挡嘴巴"     
-107: "请勿遮挡鼻子"     
-201: "人脸比对相似度低"    
-202: "人脸比对失败"    
-301: "意愿核验不通过"   
-800: "前端不兼容错误"    
-801: "用户未授权摄像头和麦克风权限"   
-802: "核验流程异常中断，请勿切屏或进行其他操作"   
-803: "用户主动关闭链接/异常断开链接"   
-998: "系统数据异常"   
-999: "系统未知错误，请联系人工核实"   
若在人脸核身过程失败、未进入意愿确认过程，则该参数返回为空，请参考人脸核身错误码结果（DetectInfoText.ErrCode)
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalResultDetailCode: int
        :param _FinalResultMessage: 意愿核身错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalResultMessage: str
        :param _Details: 意愿核身结果详细数据，与每段点头确认过程一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of IntentionActionResultDetail
        """
        self._FinalResultDetailCode = None
        self._FinalResultMessage = None
        self._Details = None

    @property
    def FinalResultDetailCode(self):
        return self._FinalResultDetailCode

    @FinalResultDetailCode.setter
    def FinalResultDetailCode(self, FinalResultDetailCode):
        self._FinalResultDetailCode = FinalResultDetailCode

    @property
    def FinalResultMessage(self):
        return self._FinalResultMessage

    @FinalResultMessage.setter
    def FinalResultMessage(self, FinalResultMessage):
        self._FinalResultMessage = FinalResultMessage

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._FinalResultDetailCode = params.get("FinalResultDetailCode")
        self._FinalResultMessage = params.get("FinalResultMessage")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = IntentionActionResultDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionActionResultDetail(AbstractModel):
    """意愿核身点头确认模式结果详细数据

    """

    def __init__(self):
        r"""
        :param _Video: 视频base64编码（其中包含全程提示文本和点头音频，mp4格式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: str
        :param _ScreenShot: 屏幕截图base64编码列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ScreenShot: list of str
        """
        self._Video = None
        self._ScreenShot = None

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def ScreenShot(self):
        return self._ScreenShot

    @ScreenShot.setter
    def ScreenShot(self, ScreenShot):
        self._ScreenShot = ScreenShot


    def _deserialize(self, params):
        self._Video = params.get("Video")
        self._ScreenShot = params.get("ScreenShot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionQuestion(AbstractModel):
    """意愿核身过程中播报的问题文本、用户回答的标准文本。

    """

    def __init__(self):
        r"""
        :param _Question: 当选择语音问答模式时，系统自动播报的问题文本，最大长度为150个字符。
        :type Question: str
        :param _Answers: 当选择语音问答模式时，用于判断用户回答是否通过的标准答案列表，传入后可自动判断用户回答文本是否在标准文本列表中。列表长度最大为50，单个答案长度限制10个字符。
        :type Answers: list of str
        """
        self._Question = None
        self._Answers = None

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answers(self):
        return self._Answers

    @Answers.setter
    def Answers(self, Answers):
        self._Answers = Answers


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._Answers = params.get("Answers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionQuestionResult(AbstractModel):
    """意愿核身问答模式结果

    """

    def __init__(self):
        r"""
        :param _FinalResultDetailCode: 意愿核身错误码：
0: "成功"       
-1: "参数错误"    
-2: "系统异常"    
-101: "请保持人脸在框内"    
-102: "检测到多张人脸"   
-103: "人脸检测失败"   
-104: "人脸检测不完整"   
-105: "请勿遮挡眼睛"    
-106: "请勿遮挡嘴巴"     
-107: "请勿遮挡鼻子"     
-201: "人脸比对相似度低"    
-202: "人脸比对失败"    
-301: "意愿核验不通过"       
-302: "用户回答阶段未检测到张嘴动作"  
-800: "前端不兼容错误"    
-801: "用户未授权摄像头和麦克风权限"   
-802: "核验流程异常中断，请勿切屏或进行其他操作"   
-803: "用户主动关闭链接/异常断开链接"   
-998: "系统数据异常"   
-999: "系统未知错误，请联系人工核实"   
若在人脸核身过程失败、未进入意愿确认过程，则该参数返回为空，请参考人脸核身错误码结果（DetectInfoText.ErrCode)
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalResultDetailCode: int
        :param _FinalResultMessage: 意愿核身错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalResultMessage: str
        :param _Video: 视频base64（其中包含全程问题和回答音频，mp4格式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: str
        :param _ScreenShot: 屏幕截图base64列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ScreenShot: list of str
        :param _ResultCode: 和答案匹配结果列表
0：成功，-1：不匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: list of str
        :param _AsrResult: 回答问题语音识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrResult: list of str
        :param _Audios: 答案录音音频
注意：此字段可能返回 null，表示取不到有效值。
        :type Audios: list of str
        :param _FinalResultCode: 意愿核身最终结果：
0：认证通过，-1：认证未通过，-2：浏览器内核不兼容，无法进行意愿校验。建议使用“FinalResultDetailCode”参数获取详细的错误码信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalResultCode: str
        """
        self._FinalResultDetailCode = None
        self._FinalResultMessage = None
        self._Video = None
        self._ScreenShot = None
        self._ResultCode = None
        self._AsrResult = None
        self._Audios = None
        self._FinalResultCode = None

    @property
    def FinalResultDetailCode(self):
        return self._FinalResultDetailCode

    @FinalResultDetailCode.setter
    def FinalResultDetailCode(self, FinalResultDetailCode):
        self._FinalResultDetailCode = FinalResultDetailCode

    @property
    def FinalResultMessage(self):
        return self._FinalResultMessage

    @FinalResultMessage.setter
    def FinalResultMessage(self, FinalResultMessage):
        self._FinalResultMessage = FinalResultMessage

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def ScreenShot(self):
        return self._ScreenShot

    @ScreenShot.setter
    def ScreenShot(self, ScreenShot):
        self._ScreenShot = ScreenShot

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def AsrResult(self):
        return self._AsrResult

    @AsrResult.setter
    def AsrResult(self, AsrResult):
        self._AsrResult = AsrResult

    @property
    def Audios(self):
        return self._Audios

    @Audios.setter
    def Audios(self, Audios):
        self._Audios = Audios

    @property
    def FinalResultCode(self):
        return self._FinalResultCode

    @FinalResultCode.setter
    def FinalResultCode(self, FinalResultCode):
        self._FinalResultCode = FinalResultCode


    def _deserialize(self, params):
        self._FinalResultDetailCode = params.get("FinalResultDetailCode")
        self._FinalResultMessage = params.get("FinalResultMessage")
        self._Video = params.get("Video")
        self._ScreenShot = params.get("ScreenShot")
        self._ResultCode = params.get("ResultCode")
        self._AsrResult = params.get("AsrResult")
        self._Audios = params.get("Audios")
        self._FinalResultCode = params.get("FinalResultCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionVerifyData(AbstractModel):
    """意愿核身相关结果

    """

    def __init__(self):
        r"""
        :param _IntentionVerifyVideo: 意愿确认环节中录制的视频（base64）。若不存在则为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyVideo: str
        :param _AsrResult: 意愿确认环节中用户语音转文字的识别结果。若不存在则为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrResult: str
        :param _ErrorCode: 意愿确认环节的结果码。当该结果码为0时，语音朗读的视频与语音识别结果才会返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: int
        :param _ErrorMessage: 意愿确认环节的结果信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _IntentionVerifyBestFrame: 意愿确认环节中录制视频的最佳帧（base64）。若不存在则为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyBestFrame: str
        :param _AsrResultSimilarity: 本次流程用户语音与传入文本比对的相似度分值，取值范围 [0.00, 100.00]。只有配置了相似度阈值后才进行语音校验并返回相似度分值。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrResultSimilarity: str
        """
        self._IntentionVerifyVideo = None
        self._AsrResult = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._IntentionVerifyBestFrame = None
        self._AsrResultSimilarity = None

    @property
    def IntentionVerifyVideo(self):
        return self._IntentionVerifyVideo

    @IntentionVerifyVideo.setter
    def IntentionVerifyVideo(self, IntentionVerifyVideo):
        self._IntentionVerifyVideo = IntentionVerifyVideo

    @property
    def AsrResult(self):
        return self._AsrResult

    @AsrResult.setter
    def AsrResult(self, AsrResult):
        self._AsrResult = AsrResult

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def IntentionVerifyBestFrame(self):
        return self._IntentionVerifyBestFrame

    @IntentionVerifyBestFrame.setter
    def IntentionVerifyBestFrame(self, IntentionVerifyBestFrame):
        self._IntentionVerifyBestFrame = IntentionVerifyBestFrame

    @property
    def AsrResultSimilarity(self):
        warnings.warn("parameter `AsrResultSimilarity` is deprecated", DeprecationWarning) 

        return self._AsrResultSimilarity

    @AsrResultSimilarity.setter
    def AsrResultSimilarity(self, AsrResultSimilarity):
        warnings.warn("parameter `AsrResultSimilarity` is deprecated", DeprecationWarning) 

        self._AsrResultSimilarity = AsrResultSimilarity


    def _deserialize(self, params):
        self._IntentionVerifyVideo = params.get("IntentionVerifyVideo")
        self._AsrResult = params.get("AsrResult")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._IntentionVerifyBestFrame = params.get("IntentionVerifyBestFrame")
        self._AsrResultSimilarity = params.get("AsrResultSimilarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessCompareRequest(AbstractModel):
    """LivenessCompare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param _ImageBase64: 用于人脸比对的照片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。

图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageBase64。
        :type ImageBase64: str
        :param _ImageUrl: 用于人脸比对照片的URL地址；图片下载后经Base64编码后的数据大小不超过3M，仅支持jpg、png格式。

图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageBase64。

图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param _ValidateData: 数字模式传参：传数字验证码，验证码需先调用<a href="https://cloud.tencent.com/document/product/1007/31821">获取数字验证码接口</a>得到；
动作模式传参：传动作顺序，动作顺序需先调用<a href="https://cloud.tencent.com/document/product/1007/31822">获取动作顺序接口</a>得到；
静默模式传参：空。
        :type ValidateData: str
        :param _Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围2-10
}
        :type Optional: str
        :param _VideoBase64: 用于活体检测的视频，视频的Base64值；
Base64编码后的大小不超过8M，支持mp4、avi、flv格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。

视频的 VideoUrl、VideoBase64 必须提供一个，如果都提供，只使用 VideoBase64。
        :type VideoBase64: str
        :param _VideoUrl: 用于活体检测的视频Url 地址。视频下载后经Base64编码后不超过 8M，视频下载耗时不超过4S，支持mp4、avi、flv格式。

视频的 VideoUrl、VideoBase64 必须提供一个，如果都提供，只使用 VideoBase64。

建议视频存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议视频存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type VideoUrl: str
        """
        self._LivenessType = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._ValidateData = None
        self._Optional = None
        self._VideoBase64 = None
        self._VideoUrl = None

    @property
    def LivenessType(self):
        return self._LivenessType

    @LivenessType.setter
    def LivenessType(self, LivenessType):
        self._LivenessType = LivenessType

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ValidateData(self):
        return self._ValidateData

    @ValidateData.setter
    def ValidateData(self, ValidateData):
        self._ValidateData = ValidateData

    @property
    def Optional(self):
        return self._Optional

    @Optional.setter
    def Optional(self, Optional):
        self._Optional = Optional

    @property
    def VideoBase64(self):
        return self._VideoBase64

    @VideoBase64.setter
    def VideoBase64(self, VideoBase64):
        self._VideoBase64 = VideoBase64

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl


    def _deserialize(self, params):
        self._LivenessType = params.get("LivenessType")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._ValidateData = params.get("ValidateData")
        self._Optional = params.get("Optional")
        self._VideoBase64 = params.get("VideoBase64")
        self._VideoUrl = params.get("VideoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessCompareResponse(AbstractModel):
    """LivenessCompare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param _Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）。
        :type Sim: float
        :param _Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _BestFrameList: 最佳截图列表，仅在配置了返回多张最佳截图时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BestFrameBase64 = None
        self._Sim = None
        self._Result = None
        self._Description = None
        self._BestFrameList = None
        self._RequestId = None

    @property
    def BestFrameBase64(self):
        return self._BestFrameBase64

    @BestFrameBase64.setter
    def BestFrameBase64(self, BestFrameBase64):
        self._BestFrameBase64 = BestFrameBase64

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def BestFrameList(self):
        return self._BestFrameList

    @BestFrameList.setter
    def BestFrameList(self, BestFrameList):
        self._BestFrameList = BestFrameList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BestFrameBase64 = params.get("BestFrameBase64")
        self._Sim = params.get("Sim")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._BestFrameList = params.get("BestFrameList")
        self._RequestId = params.get("RequestId")


class LivenessRecognitionRequest(AbstractModel):
    """LivenessRecognition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名。中文请使用UTF-8编码。
        :type Name: str
        :param _LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param _VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过8M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param _VideoUrl: 用于活体检测的视频Url 地址。视频下载后经Base64编码不超过 8M，视频下载耗时不超过4S，支持mp4、avi、flv格式。

视频的 VideoUrl、VideoBase64 必须提供一个，如果都提供，只使用 VideoBase64。

建议视频存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议视频存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type VideoUrl: str
        :param _ValidateData: 数字模式传参：传数字验证码，验证码需先调用<a href="https://cloud.tencent.com/document/product/1007/31821">获取数字验证码接口</a>得到；
动作模式传参：传动作顺序，动作顺序需先调用<a href="https://cloud.tencent.com/document/product/1007/31822">获取动作顺序接口</a>得到；
静默模式传参：空。
        :type ValidateData: str
        :param _Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围2-10
}
        :type Optional: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._LivenessType = None
        self._VideoBase64 = None
        self._VideoUrl = None
        self._ValidateData = None
        self._Optional = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LivenessType(self):
        return self._LivenessType

    @LivenessType.setter
    def LivenessType(self, LivenessType):
        self._LivenessType = LivenessType

    @property
    def VideoBase64(self):
        return self._VideoBase64

    @VideoBase64.setter
    def VideoBase64(self, VideoBase64):
        self._VideoBase64 = VideoBase64

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def ValidateData(self):
        return self._ValidateData

    @ValidateData.setter
    def ValidateData(self, ValidateData):
        self._ValidateData = ValidateData

    @property
    def Optional(self):
        return self._Optional

    @Optional.setter
    def Optional(self, Optional):
        self._Optional = Optional

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._LivenessType = params.get("LivenessType")
        self._VideoBase64 = params.get("VideoBase64")
        self._VideoUrl = params.get("VideoUrl")
        self._ValidateData = params.get("ValidateData")
        self._Optional = params.get("Optional")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessRecognitionResponse(AbstractModel):
    """LivenessRecognition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param _Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param _Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _BestFrameList: 最佳截图列表，仅在配置了返回多张最佳截图时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BestFrameBase64 = None
        self._Sim = None
        self._Result = None
        self._Description = None
        self._BestFrameList = None
        self._RequestId = None

    @property
    def BestFrameBase64(self):
        return self._BestFrameBase64

    @BestFrameBase64.setter
    def BestFrameBase64(self, BestFrameBase64):
        self._BestFrameBase64 = BestFrameBase64

    @property
    def Sim(self):
        return self._Sim

    @Sim.setter
    def Sim(self, Sim):
        self._Sim = Sim

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def BestFrameList(self):
        return self._BestFrameList

    @BestFrameList.setter
    def BestFrameList(self, BestFrameList):
        self._BestFrameList = BestFrameList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BestFrameBase64 = params.get("BestFrameBase64")
        self._Sim = params.get("Sim")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._BestFrameList = params.get("BestFrameList")
        self._RequestId = params.get("RequestId")


class LivenessRequest(AbstractModel):
    """Liveness请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过8M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param _LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param _ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：不需要传递此参数。
        :type ValidateData: str
        :param _Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围1-10
}
        :type Optional: str
        """
        self._VideoBase64 = None
        self._LivenessType = None
        self._ValidateData = None
        self._Optional = None

    @property
    def VideoBase64(self):
        return self._VideoBase64

    @VideoBase64.setter
    def VideoBase64(self, VideoBase64):
        self._VideoBase64 = VideoBase64

    @property
    def LivenessType(self):
        return self._LivenessType

    @LivenessType.setter
    def LivenessType(self, LivenessType):
        self._LivenessType = LivenessType

    @property
    def ValidateData(self):
        return self._ValidateData

    @ValidateData.setter
    def ValidateData(self, ValidateData):
        self._ValidateData = ValidateData

    @property
    def Optional(self):
        return self._Optional

    @Optional.setter
    def Optional(self, Optional):
        self._Optional = Optional


    def _deserialize(self, params):
        self._VideoBase64 = params.get("VideoBase64")
        self._LivenessType = params.get("LivenessType")
        self._ValidateData = params.get("ValidateData")
        self._Optional = params.get("Optional")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessResponse(AbstractModel):
    """Liveness返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param _Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _BestFrameList: 最佳最佳截图列表，仅在配置了返回多张最佳截图时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BestFrameBase64 = None
        self._Result = None
        self._Description = None
        self._BestFrameList = None
        self._RequestId = None

    @property
    def BestFrameBase64(self):
        return self._BestFrameBase64

    @BestFrameBase64.setter
    def BestFrameBase64(self, BestFrameBase64):
        self._BestFrameBase64 = BestFrameBase64

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def BestFrameList(self):
        return self._BestFrameList

    @BestFrameList.setter
    def BestFrameList(self, BestFrameList):
        self._BestFrameList = BestFrameList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BestFrameBase64 = params.get("BestFrameBase64")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._BestFrameList = params.get("BestFrameList")
        self._RequestId = params.get("RequestId")


class MinorsVerificationRequest(AbstractModel):
    """MinorsVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 参与校验的参数类型。
0：使用手机号进行校验；
1：使用姓名与身份证号进行校验。
        :type Type: str
        :param _Mobile: 手机号，11位数字，
特别提示：
手机号验证只限制在腾讯健康守护可信模型覆盖的数据范围内，与手机号本身在运营商是否实名无关联，不在范围会提示“手机号未实名”，建议客户与传入姓名和身份证号信息组合使用。
        :type Mobile: str
        :param _IdCard: 身份证号码。
        :type IdCard: str
        :param _Name: 姓名。
        :type Name: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._Type = None
        self._Mobile = None
        self._IdCard = None
        self._Name = None
        self._Encryption = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Mobile = params.get("Mobile")
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MinorsVerificationResponse(AbstractModel):
    """MinorsVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 结果码，收费情况如下。
收费结果码：
0: 成年
-1: 未成年
-3: 姓名和身份证号不一致

不收费结果码：
-2: 未查询到手机号信息
-4: 非法身份证号（长度、校验位等不正确）
-5: 非法姓名（长度、格式等不正确）
-6: 权威数据源服务异常
-7: 未查询到身份信息
-8: 权威数据源升级中，请稍后再试
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _AgeRange: 该字段的值为年龄区间。格式为[a,b)，
[0,8)表示年龄小于8周岁区间，不包括8岁；
[8,16)表示年龄8-16周岁区间，不包括16岁；
[16,18)表示年龄16-18周岁区间，不包括18岁；
[18,+)表示年龄大于18周岁。
        :type AgeRange: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._AgeRange = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AgeRange(self):
        return self._AgeRange

    @AgeRange.setter
    def AgeRange(self, AgeRange):
        self._AgeRange = AgeRange

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._AgeRange = params.get("AgeRange")
        self._RequestId = params.get("RequestId")


class MobileNetworkTimeVerificationRequest(AbstractModel):
    """MobileNetworkTimeVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mobile: 手机号码
        :type Mobile: str
        :param _Encryption: 敏感数据加密信息。对传入信息（手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._Mobile = None
        self._Encryption = None

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Mobile = params.get("Mobile")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MobileNetworkTimeVerificationResponse(AbstractModel):
    """MobileNetworkTimeVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 成功
-2: 手机号不存在
-3: 手机号存在，但无法查询到在网时长
不收费结果码：
-1: 手机号格式不正确
-4: 验证中心服务繁忙
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _Range: 在网时长区间。
格式为(a,b]，表示在网时长在a个月以上，b个月以下。若b为+时表示没有上限。
        :type Range: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._Range = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Range(self):
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Range = params.get("Range")
        self._RequestId = params.get("RequestId")


class MobileStatusRequest(AbstractModel):
    """MobileStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mobile: 手机号码
        :type Mobile: str
        :param _Encryption: 敏感数据加密信息。对传入信息（手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._Mobile = None
        self._Encryption = None

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Mobile = params.get("Mobile")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MobileStatusResponse(AbstractModel):
    """MobileStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0：成功
不收费结果码：
-1：未查询到结果
-2：手机号格式不正确
-3：验证中心服务繁忙
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _StatusCode: 状态码：
0：正常
1：停机
2：销号
3：空号
4：不在网
99：未知状态
        :type StatusCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._StatusCode = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._StatusCode = params.get("StatusCode")
        self._RequestId = params.get("RequestId")


class ParseNfcDataRequest(AbstractModel):
    """ParseNfcData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReqId: 前端SDK返回
        :type ReqId: str
        """
        self._ReqId = None

    @property
    def ReqId(self):
        return self._ReqId

    @ReqId.setter
    def ReqId(self, ReqId):
        self._ReqId = ReqId


    def _deserialize(self, params):
        self._ReqId = params.get("ReqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseNfcDataResponse(AbstractModel):
    """ParseNfcData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: 0为首次查询成功，-1为查询失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param _IdNum: 身份证号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdNum: str
        :param _Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Picture: 照片
注意：此字段可能返回 null，表示取不到有效值。
        :type Picture: str
        :param _BirthDate: 出生日期
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthDate: str
        :param _BeginTime: 有效期起始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param _EndTime: 有效期结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Address: 住址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param _Nation: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Nation: str
        :param _Sex: 性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param _IdType: 身份证 01 中国护照 03 军官证 04 武警证 05 港澳通行证 06 台胞证 07 外国护照 08 士兵证 09 临时身份证 10 户口本 11 警官证 12 外国人永久居留证 13 港澳台居民居住证 14 回乡证 15 大陆居民来往台湾通行证 16 其他证件 99
注意：此字段可能返回 null，表示取不到有效值。
        :type IdType: str
        :param _EnName: 英文姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type EnName: str
        :param _SigningOrganization: 签发机关
注意：此字段可能返回 null，表示取不到有效值。
        :type SigningOrganization: str
        :param _OtherIdNum: 港澳台居民居住证，通行证号码
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherIdNum: str
        :param _Nationality: 旅行证件国籍
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param _PersonalNumber: 旅行证件机读区第二行 29~42 位
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalNumber: str
        :param _CheckMRTD: 旅行证件类的核验结果。JSON格式如下：
{"result_issuer ":"签发者证书合法性验证结果 ","result_pape r":"证件安全对象合法性验证 结果 ","result_data" :"防数据篡改验证结果 ","result_chip" :"防证书件芯片被复制验证结果"} 
 0:验证通过，1: 验证不通过，2: 未验证，3:部分通过，当4项核验结果都为0时，表示证件为真
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckMRTD: str
        :param _ImageA: 身份证照片面合成图片
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageA: str
        :param _ImageB: 身份证国徽面合成图片
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageB: str
        :param _ResultDescription: 对result code的结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultDescription: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._IdNum = None
        self._Name = None
        self._Picture = None
        self._BirthDate = None
        self._BeginTime = None
        self._EndTime = None
        self._Address = None
        self._Nation = None
        self._Sex = None
        self._IdType = None
        self._EnName = None
        self._SigningOrganization = None
        self._OtherIdNum = None
        self._Nationality = None
        self._PersonalNumber = None
        self._CheckMRTD = None
        self._ImageA = None
        self._ImageB = None
        self._ResultDescription = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def IdNum(self):
        return self._IdNum

    @IdNum.setter
    def IdNum(self, IdNum):
        self._IdNum = IdNum

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Picture(self):
        return self._Picture

    @Picture.setter
    def Picture(self, Picture):
        self._Picture = Picture

    @property
    def BirthDate(self):
        return self._BirthDate

    @BirthDate.setter
    def BirthDate(self, BirthDate):
        self._BirthDate = BirthDate

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def Sex(self):
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def IdType(self):
        return self._IdType

    @IdType.setter
    def IdType(self, IdType):
        self._IdType = IdType

    @property
    def EnName(self):
        return self._EnName

    @EnName.setter
    def EnName(self, EnName):
        self._EnName = EnName

    @property
    def SigningOrganization(self):
        return self._SigningOrganization

    @SigningOrganization.setter
    def SigningOrganization(self, SigningOrganization):
        self._SigningOrganization = SigningOrganization

    @property
    def OtherIdNum(self):
        return self._OtherIdNum

    @OtherIdNum.setter
    def OtherIdNum(self, OtherIdNum):
        self._OtherIdNum = OtherIdNum

    @property
    def Nationality(self):
        return self._Nationality

    @Nationality.setter
    def Nationality(self, Nationality):
        self._Nationality = Nationality

    @property
    def PersonalNumber(self):
        return self._PersonalNumber

    @PersonalNumber.setter
    def PersonalNumber(self, PersonalNumber):
        self._PersonalNumber = PersonalNumber

    @property
    def CheckMRTD(self):
        return self._CheckMRTD

    @CheckMRTD.setter
    def CheckMRTD(self, CheckMRTD):
        self._CheckMRTD = CheckMRTD

    @property
    def ImageA(self):
        return self._ImageA

    @ImageA.setter
    def ImageA(self, ImageA):
        self._ImageA = ImageA

    @property
    def ImageB(self):
        return self._ImageB

    @ImageB.setter
    def ImageB(self, ImageB):
        self._ImageB = ImageB

    @property
    def ResultDescription(self):
        return self._ResultDescription

    @ResultDescription.setter
    def ResultDescription(self, ResultDescription):
        self._ResultDescription = ResultDescription

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._IdNum = params.get("IdNum")
        self._Name = params.get("Name")
        self._Picture = params.get("Picture")
        self._BirthDate = params.get("BirthDate")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Address = params.get("Address")
        self._Nation = params.get("Nation")
        self._Sex = params.get("Sex")
        self._IdType = params.get("IdType")
        self._EnName = params.get("EnName")
        self._SigningOrganization = params.get("SigningOrganization")
        self._OtherIdNum = params.get("OtherIdNum")
        self._Nationality = params.get("Nationality")
        self._PersonalNumber = params.get("PersonalNumber")
        self._CheckMRTD = params.get("CheckMRTD")
        self._ImageA = params.get("ImageA")
        self._ImageB = params.get("ImageB")
        self._ResultDescription = params.get("ResultDescription")
        self._RequestId = params.get("RequestId")


class PhoneVerificationCMCCRequest(AbstractModel):
    """PhoneVerificationCMCC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _Phone: 手机号
        :type Phone: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._Phone = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationCMCCResponse(AbstractModel):
    """PhoneVerificationCMCC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 认证通过
-4: 信息不一致（手机号已实名，但姓名和身份证号与实名信息不一致）
不收费结果码：
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-11: 验证中心服务繁忙
        :type Result: str
        :param _Isp: 运营商名称。
取值范围为["移动","联通","电信",""]
        :type Isp: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Isp = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Isp = params.get("Isp")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class PhoneVerificationCTCCRequest(AbstractModel):
    """PhoneVerificationCTCC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _Phone: 手机号
        :type Phone: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._Phone = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationCTCCResponse(AbstractModel):
    """PhoneVerificationCTCC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 认证通过
-4: 信息不一致（手机号已实名，但姓名和身份证号与实名信息不一致）
不收费结果码：
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-11: 验证中心服务繁忙
        :type Result: str
        :param _Isp: 运营商名称。
取值范围为["移动","联通","电信",""]
        :type Isp: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Isp = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Isp = params.get("Isp")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class PhoneVerificationCUCCRequest(AbstractModel):
    """PhoneVerificationCUCC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _Phone: 手机号
        :type Phone: str
        :param _Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self._IdCard = None
        self._Name = None
        self._Phone = None
        self._Encryption = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Encryption(self):
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        if params.get("Encryption") is not None:
            self._Encryption = Encryption()
            self._Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationCUCCResponse(AbstractModel):
    """PhoneVerificationCUCC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码，收费情况如下。
收费结果码：
0: 认证通过
-4: 信息不一致（手机号已实名，但姓名和身份证号与实名信息不一致）
不收费结果码：
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-11: 验证中心服务繁忙
        :type Result: str
        :param _Isp: 运营商名称。
取值范围为["移动","联通","电信",""]
        :type Isp: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Isp = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Isp = params.get("Isp")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class PhoneVerificationRequest(AbstractModel):
    """PhoneVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdCard: 身份证号
        :type IdCard: str
        :param _Name: 姓名
        :type Name: str
        :param _Phone: 手机号
        :type Phone: str
        :param _VerifyMode: 验证模式（详版/简版）。简版与详版价格不一致，详见[价格说明](https://cloud.tencent.com/document/product/1007/84321)。

枚举值：0（简版），1（详版）。默认值为0。
        :type VerifyMode: str
        :param _CiphertextBlob: 有加密需求的用户，传入kms的CiphertextBlob，关于数据加密可查阅 <a href="https://cloud.tencent.com/document/product/1007/47180">数据加密</a> 文档。
        :type CiphertextBlob: str
        :param _EncryptList: 在使用加密服务时，填入要被加密的字段。本接口中可填入加密后的IdCard，Name，Phone中的一个或多个。
        :type EncryptList: list of str
        :param _Iv: 有加密需求的用户，传入CBC加密的初始向量。
        :type Iv: str
        """
        self._IdCard = None
        self._Name = None
        self._Phone = None
        self._VerifyMode = None
        self._CiphertextBlob = None
        self._EncryptList = None
        self._Iv = None

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, IdCard):
        self._IdCard = IdCard

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def VerifyMode(self):
        return self._VerifyMode

    @VerifyMode.setter
    def VerifyMode(self, VerifyMode):
        self._VerifyMode = VerifyMode

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def EncryptList(self):
        return self._EncryptList

    @EncryptList.setter
    def EncryptList(self, EncryptList):
        self._EncryptList = EncryptList

    @property
    def Iv(self):
        return self._Iv

    @Iv.setter
    def Iv(self, Iv):
        self._Iv = Iv


    def _deserialize(self, params):
        self._IdCard = params.get("IdCard")
        self._Name = params.get("Name")
        self._Phone = params.get("Phone")
        self._VerifyMode = params.get("VerifyMode")
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._EncryptList = params.get("EncryptList")
        self._Iv = params.get("Iv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationResponse(AbstractModel):
    """PhoneVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 认证结果码:
收费结果码
0: 三要素信息一致
-4: 三要素信息不一致
不收费结果码
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-11: 验证中心服务繁忙
        :type Result: str
        :param _Description: 业务结果描述。
        :type Description: str
        :param _Isp: 运营商名称。
取值范围为["","移动","电信","联通"]
        :type Isp: str
        :param _ResultDetail: 业务结果详细信息。（当VerifyMode配置"详版"，且Result为"-4: 三要素信息不一致"时返回）
枚举值：
PhoneIdCardMismatch：手机号码与姓名一致，与身份证号不一致；
PhoneNameMismatch：手机号码身份证号一致，与姓名不一致；
PhoneNameIdCardMismatch：手机号码与姓名和身份证号均不一致；
NameIdCardMismatch：姓名和身份证号不一致；
OtherMismatch：其他不一致；
        :type ResultDetail: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._Isp = None
        self._ResultDetail = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def ResultDetail(self):
        return self._ResultDetail

    @ResultDetail.setter
    def ResultDetail(self, ResultDetail):
        self._ResultDetail = ResultDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Isp = params.get("Isp")
        self._ResultDetail = params.get("ResultDetail")
        self._RequestId = params.get("RequestId")


class RetrievalLivenessExtraInfo(AbstractModel):
    """模版检索详细信息

    """

    def __init__(self):
        r"""
        :param _HitGroup: 命中的模版类型，其中Common-公共库；Auto-自动聚类库；Owner-自建模版库
注意：此字段可能返回 null，表示取不到有效值。
        :type HitGroup: str
        :param _SimilarityScore: 命中的相似度
注意：此字段可能返回 null，表示取不到有效值。
        :type SimilarityScore: float
        :param _HitTemplate: 命中的模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type HitTemplate: str
        """
        self._HitGroup = None
        self._SimilarityScore = None
        self._HitTemplate = None

    @property
    def HitGroup(self):
        return self._HitGroup

    @HitGroup.setter
    def HitGroup(self, HitGroup):
        self._HitGroup = HitGroup

    @property
    def SimilarityScore(self):
        return self._SimilarityScore

    @SimilarityScore.setter
    def SimilarityScore(self, SimilarityScore):
        self._SimilarityScore = SimilarityScore

    @property
    def HitTemplate(self):
        return self._HitTemplate

    @HitTemplate.setter
    def HitTemplate(self, HitTemplate):
        self._HitTemplate = HitTemplate


    def _deserialize(self, params):
        self._HitGroup = params.get("HitGroup")
        self._SimilarityScore = params.get("SimilarityScore")
        self._HitTemplate = params.get("HitTemplate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleIdConfig(AbstractModel):
    """RuleId相关配置

    """

    def __init__(self):
        r"""
        :param _IntentionRecognition: 意愿核身过程中识别用户的回答意图，开启后除了IntentionQuestions的Answers列表中的标准回答会通过，近似意图的回答也会通过，默认开启。
        :type IntentionRecognition: bool
        :param _IntentionType: 意愿核身类型，默认为0：
0：问答模式，DetectAuth接口需要传入IntentionQuestions字段；
1：点头模式，DetectAuth接口需要传入IntentionActions字段；
        :type IntentionType: int
        :param _MouthOpenRecognition: 用户语音回答过程中是否开启张嘴识别检测，默认不开启，仅在意愿核身问答模式中使用。
        :type MouthOpenRecognition: bool
        """
        self._IntentionRecognition = None
        self._IntentionType = None
        self._MouthOpenRecognition = None

    @property
    def IntentionRecognition(self):
        return self._IntentionRecognition

    @IntentionRecognition.setter
    def IntentionRecognition(self, IntentionRecognition):
        self._IntentionRecognition = IntentionRecognition

    @property
    def IntentionType(self):
        return self._IntentionType

    @IntentionType.setter
    def IntentionType(self, IntentionType):
        self._IntentionType = IntentionType

    @property
    def MouthOpenRecognition(self):
        return self._MouthOpenRecognition

    @MouthOpenRecognition.setter
    def MouthOpenRecognition(self, MouthOpenRecognition):
        self._MouthOpenRecognition = MouthOpenRecognition


    def _deserialize(self, params):
        self._IntentionRecognition = params.get("IntentionRecognition")
        self._IntentionType = params.get("IntentionType")
        self._MouthOpenRecognition = params.get("MouthOpenRecognition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeChatBillDetail(AbstractModel):
    """账单详情

    """

    def __init__(self):
        r"""
        :param _BizToken: token
        :type BizToken: str
        :param _ChargeCount: 本token收费次数
        :type ChargeCount: int
        :param _ChargeDetails: 本token计费详情
        :type ChargeDetails: list of ChargeDetail
        :param _RuleId: 业务RuleId
        :type RuleId: str
        """
        self._BizToken = None
        self._ChargeCount = None
        self._ChargeDetails = None
        self._RuleId = None

    @property
    def BizToken(self):
        return self._BizToken

    @BizToken.setter
    def BizToken(self, BizToken):
        self._BizToken = BizToken

    @property
    def ChargeCount(self):
        return self._ChargeCount

    @ChargeCount.setter
    def ChargeCount(self, ChargeCount):
        self._ChargeCount = ChargeCount

    @property
    def ChargeDetails(self):
        return self._ChargeDetails

    @ChargeDetails.setter
    def ChargeDetails(self, ChargeDetails):
        self._ChargeDetails = ChargeDetails

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._BizToken = params.get("BizToken")
        self._ChargeCount = params.get("ChargeCount")
        if params.get("ChargeDetails") is not None:
            self._ChargeDetails = []
            for item in params.get("ChargeDetails"):
                obj = ChargeDetail()
                obj._deserialize(item)
                self._ChargeDetails.append(obj)
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        