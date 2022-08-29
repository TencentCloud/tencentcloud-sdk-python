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


class BankCard2EVerificationRequest(AbstractModel):
    """BankCard2EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 姓名
        :type Name: str
        :param BankCard: 银行卡
        :type BankCard: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.Name = None
        self.BankCard = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCard2EVerificationResponse(AbstractModel):
    """BankCard2EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码
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
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class BankCard4EVerificationRequest(AbstractModel):
    """BankCard4EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 姓名
        :type Name: str
        :param BankCard: 银行卡
        :type BankCard: str
        :param Phone: 手机号码
        :type Phone: str
        :param IdCard: 开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。
        :type IdCard: str
        :param CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。
目前默认为0：身份证，其他证件类型暂不支持。
        :type CertType: int
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号、银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.Name = None
        self.BankCard = None
        self.Phone = None
        self.IdCard = None
        self.CertType = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")
        self.Phone = params.get("Phone")
        self.IdCard = params.get("IdCard")
        self.CertType = params.get("CertType")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCard4EVerificationResponse(AbstractModel):
    """BankCard4EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码
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
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class BankCardVerificationRequest(AbstractModel):
    """BankCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param BankCard: 银行卡
        :type BankCard: str
        :param CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。
目前默认：0 身份证，其他证件类型需求可以添加[腾讯云人脸核身小助手](https://cloud.tencent.com/document/product/1007/56130)进行确认。
        :type CertType: int
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.BankCard = None
        self.CertType = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")
        self.CertType = params.get("CertType")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardVerificationResponse(AbstractModel):
    """BankCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码
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
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class ChargeDetail(AbstractModel):
    """计费详情

    """

    def __init__(self):
        r"""
        :param ReqTime: 一比一时间时间戳，13位。
        :type ReqTime: str
        :param Seq: 一比一请求的唯一标记。
        :type Seq: str
        :param Idcard: 一比一时使用的、脱敏后的身份证号。
        :type Idcard: str
        :param Name: 一比一时使用的、脱敏后的姓名。
        :type Name: str
        :param Sim: 一比一的相似度。0-100，保留2位小数。
        :type Sim: str
        :param IsNeedCharge: 本次详情是否收费。
        :type IsNeedCharge: bool
        :param ChargeType: 收费类型，比对、核身、混合部署。
        :type ChargeType: str
        :param ErrorCode: 本次活体一比一最终结果。
        :type ErrorCode: str
        :param ErrorMessage: 本次活体一比一最终结果描述。
        :type ErrorMessage: str
        """
        self.ReqTime = None
        self.Seq = None
        self.Idcard = None
        self.Name = None
        self.Sim = None
        self.IsNeedCharge = None
        self.ChargeType = None
        self.ErrorCode = None
        self.ErrorMessage = None


    def _deserialize(self, params):
        self.ReqTime = params.get("ReqTime")
        self.Seq = params.get("Seq")
        self.Idcard = params.get("Idcard")
        self.Name = params.get("Name")
        self.Sim = params.get("Sim")
        self.IsNeedCharge = params.get("IsNeedCharge")
        self.ChargeType = params.get("ChargeType")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCardInformationRequest(AbstractModel):
    """CheckBankCardInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param BankCard: 银行卡号。
        :type BankCard: str
        :param Encryption: 敏感数据加密信息。对传入信息（银行卡号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.BankCard = None
        self.Encryption = None


    def _deserialize(self, params):
        self.BankCard = params.get("BankCard")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCardInformationResponse(AbstractModel):
    """CheckBankCardInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 查询成功
-1: 未查到信息
不收费结果码
-2：验证中心服务繁忙
-3：银行卡不存在
        :type Result: str
        :param Description: 业务结果描述
        :type Description: str
        :param AccountBank: 开户行
        :type AccountBank: str
        :param AccountType: 卡性质：1. 借记卡；2. 贷记卡；3. 预付费卡；4. 准贷记卡
        :type AccountType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.AccountBank = None
        self.AccountType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.AccountBank = params.get("AccountBank")
        self.AccountType = params.get("AccountType")
        self.RequestId = params.get("RequestId")


class CheckEidTokenStatusRequest(AbstractModel):
    """CheckEidTokenStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EidToken: E证通流程的唯一标识，调用GetEidToken接口时生成。
        :type EidToken: str
        """
        self.EidToken = None


    def _deserialize(self, params):
        self.EidToken = params.get("EidToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckEidTokenStatusResponse(AbstractModel):
    """CheckEidTokenStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 枚举：
init：token未验证
doing: 验证中
finished: 验证完成
timeout: token已超时
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CheckIdCardInformationRequest(AbstractModel):
    """CheckIdCardInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageBase64: 身份证人像面的 Base64 值
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
ImageBase64、ImageUrl二者必须提供其中之一。若都提供了，则按照ImageUrl>ImageBase64的优先级使用参数。
        :type ImageBase64: str
        :param ImageUrl: 身份证人像面的 Url 地址
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Config: 以下可选字段均为bool 类型，默认false：
CopyWarn，复印件告警
BorderCheckWarn，边框和框内遮挡告警
ReshootWarn，翻拍告警
DetectPsWarn，PS检测告警
TempIdWarn，临时身份证告警
Quality，图片质量告警（评价图片模糊程度）

SDK 设置方式参考：
Config = Json.stringify({"CopyWarn":true,"ReshootWarn":true})
API 3.0 Explorer 设置方式参考：
Config = {"CopyWarn":true,"ReshootWarn":true}
        :type Config: str
        :param IsEncrypt: 是否需要对返回中的敏感信息进行加密。默认false。
其中敏感信息包括：Response.IdNum、Response.Name
        :type IsEncrypt: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Config = None
        self.IsEncrypt = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")
        self.IsEncrypt = params.get("IsEncrypt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIdCardInformationResponse(AbstractModel):
    """CheckIdCardInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param Name: 姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param Nation: 民族
        :type Nation: str
        :param Birth: 出生日期
        :type Birth: str
        :param Address: 地址
        :type Address: str
        :param IdNum: 身份证号
        :type IdNum: str
        :param Portrait: 身份证头像照片的base64编码，如果抠图失败会拿整张身份证做比对并返回空。
        :type Portrait: str
        :param Warnings: 告警信息，当在Config中配置了告警信息会停止人像比对，Result返回错误（FailedOperation.OcrWarningOccurred）并有此告警信息，Code 告警码列表和释义：

-9101 身份证边框不完整告警，
-9102 身份证复印件告警，
-9103 身份证翻拍告警，
-9105 身份证框内遮挡告警，
-9104 临时身份证告警，
-9106 身份证 PS 告警。
-8001 图片模糊告警
多个会 |  隔开如 "-9101|-9106|-9104"
        :type Warnings: str
        :param Quality: 图片质量分数，当请求Config中配置图片模糊告警该参数才有意义，取值范围（0～100），目前默认阈值是50分，低于50分会触发模糊告警。
        :type Quality: float
        :param Encryption: 敏感数据加密信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Sim = None
        self.Result = None
        self.Description = None
        self.Name = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.IdNum = None
        self.Portrait = None
        self.Warnings = None
        self.Quality = None
        self.Encryption = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdNum = params.get("IdNum")
        self.Portrait = params.get("Portrait")
        self.Warnings = params.get("Warnings")
        self.Quality = params.get("Quality")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        self.RequestId = params.get("RequestId")


class CheckIdNameDateRequest(AbstractModel):
    """CheckIdNameDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 姓名
        :type Name: str
        :param IdCard: 身份证号
        :type IdCard: str
        :param ValidityBegin: 身份证有效期开始时间，格式：YYYYMMDD。如：20210701
        :type ValidityBegin: str
        :param ValidityEnd: 身份证有效期到期时间，格式：YYYYMMDD，长期用“00000000”代替；如：20210701
        :type ValidityEnd: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.Name = None
        self.IdCard = None
        self.ValidityBegin = None
        self.ValidityEnd = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IdCard = params.get("IdCard")
        self.ValidityBegin = params.get("ValidityBegin")
        self.ValidityEnd = params.get("ValidityEnd")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIdNameDateResponse(AbstractModel):
    """CheckIdNameDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
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
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class CheckPhoneAndNameRequest(AbstractModel):
    """CheckPhoneAndName请求参数结构体

    """

    def __init__(self):
        r"""
        :param Mobile: ⼿机号
        :type Mobile: str
        :param Name: 姓名
        :type Name: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.Mobile = None
        self.Name = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")
        self.Name = params.get("Name")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckPhoneAndNameResponse(AbstractModel):
    """CheckPhoneAndName返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 验证结果一致
1: 验证结果不一致
不收费结果码：
-1:查无记录
-2:引擎未知错误
-3:引擎服务异常
        :type Result: str
        :param Description: 业务结果描述
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DetectAuthRequest(AbstractModel):
    """DetectAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请添加[腾讯云人脸核身小助手](https://cloud.tencent.com/document/product/1007/56130)进行咨询。
        :type RuleId: str
        :param TerminalType: 本接口不需要传递此参数。
        :type TerminalType: str
        :param IdCard: 身份标识（未使用OCR服务时，必须传入）。
规则：a-zA-Z0-9组合。最长长度32位。
        :type IdCard: str
        :param Name: 姓名。（未使用OCR服务时，必须传入）最长长度32位。中文请使用UTF-8编码。
        :type Name: str
        :param RedirectUrl: 认证结束后重定向的回调链接地址。最长长度1024位。
        :type RedirectUrl: str
        :param Extra: 透传字段，在获取验证结果时返回。
        :type Extra: str
        :param ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param IntentionVerifyText: 意愿核身使用的文案，若未使用意愿核身功能，该字段无需传入。默认为空，最长可接受120的字符串长度。
        :type IntentionVerifyText: str
        :param IntentionQuestions: 意愿核身过程中播报文本/问题、用户朗读/回答的文本，当前支持一个播报文本+回答文本。
        :type IntentionQuestions: list of IntentionQuestion
        """
        self.RuleId = None
        self.TerminalType = None
        self.IdCard = None
        self.Name = None
        self.RedirectUrl = None
        self.Extra = None
        self.ImageBase64 = None
        self.Encryption = None
        self.IntentionVerifyText = None
        self.IntentionQuestions = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.TerminalType = params.get("TerminalType")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.RedirectUrl = params.get("RedirectUrl")
        self.Extra = params.get("Extra")
        self.ImageBase64 = params.get("ImageBase64")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        self.IntentionVerifyText = params.get("IntentionVerifyText")
        if params.get("IntentionQuestions") is not None:
            self.IntentionQuestions = []
            for item in params.get("IntentionQuestions"):
                obj = IntentionQuestion()
                obj._deserialize(item)
                self.IntentionQuestions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectAuthResponse(AbstractModel):
    """DetectAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 用于发起核身流程的URL，仅微信H5场景使用。
        :type Url: str
        :param BizToken: 一次核身流程的标识，有效时间为7,200秒；
完成核身后，可用该标识获取验证结果信息。
        :type BizToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.BizToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.BizToken = params.get("BizToken")
        self.RequestId = params.get("RequestId")


class DetectDetail(AbstractModel):
    """活体一比一详情

    """

    def __init__(self):
        r"""
        :param ReqTime: 请求时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReqTime: str
        :param Seq: 本次活体一比一请求的唯一标记。
注意：此字段可能返回 null，表示取不到有效值。
        :type Seq: str
        :param Idcard: 参与本次活体一比一的身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type Idcard: str
        :param Name: 参与本次活体一比一的姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Sim: 本次活体一比一的相似度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sim: str
        :param IsNeedCharge: 本次活体一比一是否收费
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNeedCharge: bool
        :param Errcode: 本次活体一比一最终结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Errcode: int
        :param Errmsg: 本次活体一比一最终结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Errmsg: str
        :param Livestatus: 本次活体结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Livestatus: int
        :param Livemsg: 本次活体结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Livemsg: str
        :param Comparestatus: 本次一比一结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param Comparemsg: 本次一比一结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        :param CompareLibType: 比对库源类型。包括：
公安商业库；
业务方自有库（用户上传照片、客户的混合库、混合部署库）；
二次验证库；
人工审核库；
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareLibType: str
        """
        self.ReqTime = None
        self.Seq = None
        self.Idcard = None
        self.Name = None
        self.Sim = None
        self.IsNeedCharge = None
        self.Errcode = None
        self.Errmsg = None
        self.Livestatus = None
        self.Livemsg = None
        self.Comparestatus = None
        self.Comparemsg = None
        self.CompareLibType = None


    def _deserialize(self, params):
        self.ReqTime = params.get("ReqTime")
        self.Seq = params.get("Seq")
        self.Idcard = params.get("Idcard")
        self.Name = params.get("Name")
        self.Sim = params.get("Sim")
        self.IsNeedCharge = params.get("IsNeedCharge")
        self.Errcode = params.get("Errcode")
        self.Errmsg = params.get("Errmsg")
        self.Livestatus = params.get("Livestatus")
        self.Livemsg = params.get("Livemsg")
        self.Comparestatus = params.get("Comparestatus")
        self.Comparemsg = params.get("Comparemsg")
        self.CompareLibType = params.get("CompareLibType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoBestFrame(AbstractModel):
    """核身最佳帧信息

    """

    def __init__(self):
        r"""
        :param BestFrame: 活体比对最佳帧Base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: str
        :param BestFrames: 自截帧Base64编码数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrames: list of str
        """
        self.BestFrame = None
        self.BestFrames = None


    def _deserialize(self, params):
        self.BestFrame = params.get("BestFrame")
        self.BestFrames = params.get("BestFrames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoIdCardData(AbstractModel):
    """核身身份证图片信息

    """

    def __init__(self):
        r"""
        :param OcrFront: OCR正面照片的base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrFront: str
        :param OcrBack: OCR反面照片的base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrBack: str
        :param ProcessedFrontImage: 旋转裁边后的正面照片base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedFrontImage: str
        :param ProcessedBackImage: 旋转裁边后的背面照片base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedBackImage: str
        :param Avatar: 身份证正面人像图base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param WarnInfos: 身份证人像面告警码，开启身份证告警功能后才会返回，返回数组中可能出现的告警码如下：
-9100 身份证有效日期不合法告警，
-9101 身份证边框不完整告警，
-9102 身份证复印件告警，
-9103 身份证翻拍告警，
-9105 身份证框内遮挡告警，
-9104 临时身份证告警，
-9106 身份证 PS 告警，
-9107 身份证反光告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type WarnInfos: list of int
        :param BackWarnInfos: 身份证国徽面告警码，开启身份证告警功能后才会返回，返回数组中可能出现的告警码如下：
-9100 身份证有效日期不合法告警，
-9101 身份证边框不完整告警，
-9102 身份证复印件告警，
-9103 身份证翻拍告警，
-9105 身份证框内遮挡告警，
-9104 临时身份证告警，
-9106 身份证 PS 告警，
-9107 身份证反光告警。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackWarnInfos: list of int
        """
        self.OcrFront = None
        self.OcrBack = None
        self.ProcessedFrontImage = None
        self.ProcessedBackImage = None
        self.Avatar = None
        self.WarnInfos = None
        self.BackWarnInfos = None


    def _deserialize(self, params):
        self.OcrFront = params.get("OcrFront")
        self.OcrBack = params.get("OcrBack")
        self.ProcessedFrontImage = params.get("ProcessedFrontImage")
        self.ProcessedBackImage = params.get("ProcessedBackImage")
        self.Avatar = params.get("Avatar")
        self.WarnInfos = params.get("WarnInfos")
        self.BackWarnInfos = params.get("BackWarnInfos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoText(AbstractModel):
    """核身文本信息

    """

    def __init__(self):
        r"""
        :param ErrCode: 本次流程最终验证结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param ErrMsg: 本次流程最终验证结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param IdCard: 本次验证使用的身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param Name: 本次验证使用的姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param OcrNation: Ocr识别结果。民族。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrNation: str
        :param OcrAddress: Ocr识别结果。家庭住址。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrAddress: str
        :param OcrBirth: Ocr识别结果。生日。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrBirth: str
        :param OcrAuthority: Ocr识别结果。签发机关。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrAuthority: str
        :param OcrValidDate: Ocr识别结果。有效日期。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrValidDate: str
        :param OcrName: Ocr识别结果。姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrName: str
        :param OcrIdCard: Ocr识别结果。身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrIdCard: str
        :param OcrGender: Ocr识别结果。性别。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrGender: str
        :param LiveStatus: 本次流程最终活体结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStatus: int
        :param LiveMsg: 本次流程最终活体结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveMsg: str
        :param Comparestatus: 本次流程最终一比一结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param Comparemsg: 本次流程最终一比一结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        :param Sim: 本次流程活体一比一的分数，取值范围 [0.00, 100.00]。相似度大于等于70时才判断为同一人，也可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
注意：此字段可能返回 null，表示取不到有效值。
        :type Sim: str
        :param Location: 地理位置经纬度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param Extra: Auth接口带入额外信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param LivenessDetail: 本次流程进行的活体一比一流水。
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessDetail: list of DetectDetail
        :param Mobile: 手机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        :param CompareLibType: 本次流程最终比对库源类型。包括：
权威库；
业务方自有库（用户上传照片、客户的混合库、混合部署库）；
二次验证库；
人工审核库；
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareLibType: str
        """
        self.ErrCode = None
        self.ErrMsg = None
        self.IdCard = None
        self.Name = None
        self.OcrNation = None
        self.OcrAddress = None
        self.OcrBirth = None
        self.OcrAuthority = None
        self.OcrValidDate = None
        self.OcrName = None
        self.OcrIdCard = None
        self.OcrGender = None
        self.LiveStatus = None
        self.LiveMsg = None
        self.Comparestatus = None
        self.Comparemsg = None
        self.Sim = None
        self.Location = None
        self.Extra = None
        self.LivenessDetail = None
        self.Mobile = None
        self.CompareLibType = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.OcrNation = params.get("OcrNation")
        self.OcrAddress = params.get("OcrAddress")
        self.OcrBirth = params.get("OcrBirth")
        self.OcrAuthority = params.get("OcrAuthority")
        self.OcrValidDate = params.get("OcrValidDate")
        self.OcrName = params.get("OcrName")
        self.OcrIdCard = params.get("OcrIdCard")
        self.OcrGender = params.get("OcrGender")
        self.LiveStatus = params.get("LiveStatus")
        self.LiveMsg = params.get("LiveMsg")
        self.Comparestatus = params.get("Comparestatus")
        self.Comparemsg = params.get("Comparemsg")
        self.Sim = params.get("Sim")
        self.Location = params.get("Location")
        self.Extra = params.get("Extra")
        if params.get("LivenessDetail") is not None:
            self.LivenessDetail = []
            for item in params.get("LivenessDetail"):
                obj = DetectDetail()
                obj._deserialize(item)
                self.LivenessDetail.append(obj)
        self.Mobile = params.get("Mobile")
        self.CompareLibType = params.get("CompareLibType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectInfoVideoData(AbstractModel):
    """核身视频信息

    """

    def __init__(self):
        r"""
        :param LivenessVideo: 活体视频的base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessVideo: str
        """
        self.LivenessVideo = None


    def _deserialize(self, params):
        self.LivenessVideo = params.get("LivenessVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EidInfo(AbstractModel):
    """Eid出参，包括商户方用户的标识和加密的用户姓名身份证信息。

    """

    def __init__(self):
        r"""
        :param EidCode: 商户方 appeIDcode 的数字证书
        :type EidCode: str
        :param EidSign: Eid中心针对商户方EidCode的电子签名
        :type EidSign: str
        :param DesKey: 商户方公钥加密的会话密钥的base64字符串，[指引详见](https://cloud.tencent.com/document/product/1007/63370)
        :type DesKey: str
        :param UserInfo: 会话密钥sm2加密后的base64字符串，[指引详见](https://cloud.tencent.com/document/product/1007/63370)
        :type UserInfo: str
        """
        self.EidCode = None
        self.EidSign = None
        self.DesKey = None
        self.UserInfo = None


    def _deserialize(self, params):
        self.EidCode = params.get("EidCode")
        self.EidSign = params.get("EidSign")
        self.DesKey = params.get("DesKey")
        self.UserInfo = params.get("UserInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptedPhoneVerificationRequest(AbstractModel):
    """EncryptedPhoneVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号，加密方式以EncryptionMode为准
        :type IdCard: str
        :param Name: 姓名，加密方式以EncryptionMode为准
        :type Name: str
        :param Phone: 手机号，加密方式以EncryptionMode为准
        :type Phone: str
        :param EncryptionMode: 敏感信息的加密方式，目前支持明文、MD5和SHA256加密传输，参数取值：

0：明文，不加密
1:   使用MD5加密
2:   使用SHA256
        :type EncryptionMode: str
        """
        self.IdCard = None
        self.Name = None
        self.Phone = None
        self.EncryptionMode = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        self.EncryptionMode = params.get("EncryptionMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptedPhoneVerificationResponse(AbstractModel):
    """EncryptedPhoneVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码:
【收费结果码】
0:   三要素信息一致
-4:  三要素信息不一致

【不收费结果码】
-7: 身份证号码有误
-8: 参数错误
-9: 没有记录
-11: 验证中心服务繁忙
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class Encryption(AbstractModel):
    """敏感数据加密

    """

    def __init__(self):
        r"""
        :param EncryptList: 在使用加密服务时，填入要被加密的字段。本接口中可填入加密后的一个或多个字段
        :type EncryptList: list of str
        :param CiphertextBlob: 有加密需求的用户，接入传入kms的CiphertextBlob，关于数据加密可查阅<a href="https://cloud.tencent.com/document/product/1007/47180">数据加密</a> 文档。
        :type CiphertextBlob: str
        :param Iv: 有加密需求的用户，传入CBC加密的初始向量（客户自定义字符串，长度16字符）。
        :type Iv: str
        :param Algorithm: 加密使用的算法（支持'AES-256-CBC'、'SM4-GCM'），不传默认为'AES-256-CBC'
        :type Algorithm: str
        :param TagList: SM4-GCM算法生成的消息摘要（校验消息完整性时使用）
        :type TagList: list of str
        """
        self.EncryptList = None
        self.CiphertextBlob = None
        self.Iv = None
        self.Algorithm = None
        self.TagList = None


    def _deserialize(self, params):
        self.EncryptList = params.get("EncryptList")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.Iv = params.get("Iv")
        self.Algorithm = params.get("Algorithm")
        self.TagList = params.get("TagList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetActionSequenceRequest(AbstractModel):
    """GetActionSequence请求参数结构体

    """

    def __init__(self):
        r"""
        :param ActionType: 默认不需要使用
        :type ActionType: str
        """
        self.ActionType = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetActionSequenceResponse(AbstractModel):
    """GetActionSequence返回参数结构体

    """

    def __init__(self):
        r"""
        :param ActionSequence: 动作顺序(2,1 or 1,2) 。1代表张嘴，2代表闭眼。
        :type ActionSequence: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ActionSequence = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActionSequence = params.get("ActionSequence")
        self.RequestId = params.get("RequestId")


class GetDetectInfoEnhancedRequest(AbstractModel):
    """GetDetectInfoEnhanced请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizToken: 人脸核身流程的标识，调用DetectAuth接口时生成。
        :type BizToken: str
        :param RuleId: 用于细分客户使用场景，由腾讯侧在线下对接时分配。
        :type RuleId: str
        :param InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证信息；3：视频最佳截图信息）。
如 13表示拉取文本类、视频最佳截图信息。
默认值：0
        :type InfoType: str
        :param BestFramesCount: 从活体视频中截取一定张数的最佳帧（仅部分服务支持，若需使用请与慧眼小助手沟通）。默认为0，最大为10，超出10的最多只给10张。（InfoType需要包含3）
        :type BestFramesCount: int
        :param IsCutIdCardImage: 是否对身份证照片进行裁边。默认为false。（InfoType需要包含2）
        :type IsCutIdCardImage: bool
        :param IsNeedIdCardAvatar: 是否需要从身份证中抠出头像。默认为false。（InfoType需要包含2）
        :type IsNeedIdCardAvatar: bool
        :param IsEncrypt: 已弃用。
        :type IsEncrypt: bool
        :param Encryption: 是否需要对返回中的敏感信息进行加密。仅指定加密算法Algorithm即可，其余字段传入默认值。其中敏感信息包括：Response.Text.IdCard、Response.Text.Name、Response.Text.OcrIdCard、Response.Text.OcrName
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.BizToken = None
        self.RuleId = None
        self.InfoType = None
        self.BestFramesCount = None
        self.IsCutIdCardImage = None
        self.IsNeedIdCardAvatar = None
        self.IsEncrypt = None
        self.Encryption = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        self.RuleId = params.get("RuleId")
        self.InfoType = params.get("InfoType")
        self.BestFramesCount = params.get("BestFramesCount")
        self.IsCutIdCardImage = params.get("IsCutIdCardImage")
        self.IsNeedIdCardAvatar = params.get("IsNeedIdCardAvatar")
        self.IsEncrypt = params.get("IsEncrypt")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDetectInfoEnhancedResponse(AbstractModel):
    """GetDetectInfoEnhanced返回参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 文本类信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.faceid.v20180301.models.DetectInfoText`
        :param IdCardData: 身份证照片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoIdCardData`
        :param BestFrame: 最佳帧信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.DetectInfoBestFrame`
        :param VideoData: 视频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoVideoData`
        :param Encryption: 敏感数据加密信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        :param IntentionVerifyData: 意愿核身相关信息。若未使用意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyData: :class:`tencentcloud.faceid.v20180301.models.IntentionVerifyData`
        :param IntentionQuestionResult: 意愿核身问答模式结果。若未使用该意愿核身功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionQuestionResult: :class:`tencentcloud.faceid.v20180301.models.IntentionQuestionResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Text = None
        self.IdCardData = None
        self.BestFrame = None
        self.VideoData = None
        self.Encryption = None
        self.IntentionVerifyData = None
        self.IntentionQuestionResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self.Text = DetectInfoText()
            self.Text._deserialize(params.get("Text"))
        if params.get("IdCardData") is not None:
            self.IdCardData = DetectInfoIdCardData()
            self.IdCardData._deserialize(params.get("IdCardData"))
        if params.get("BestFrame") is not None:
            self.BestFrame = DetectInfoBestFrame()
            self.BestFrame._deserialize(params.get("BestFrame"))
        if params.get("VideoData") is not None:
            self.VideoData = DetectInfoVideoData()
            self.VideoData._deserialize(params.get("VideoData"))
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        if params.get("IntentionVerifyData") is not None:
            self.IntentionVerifyData = IntentionVerifyData()
            self.IntentionVerifyData._deserialize(params.get("IntentionVerifyData"))
        if params.get("IntentionQuestionResult") is not None:
            self.IntentionQuestionResult = IntentionQuestionResult()
            self.IntentionQuestionResult._deserialize(params.get("IntentionQuestionResult"))
        self.RequestId = params.get("RequestId")


class GetDetectInfoRequest(AbstractModel):
    """GetDetectInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizToken: 人脸核身流程的标识，调用DetectAuth接口时生成。
        :type BizToken: str
        :param RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请加慧眼小助手微信（faceid001）进行咨询。
        :type RuleId: str
        :param InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证正反面；3：视频最佳截图照片；4：视频）。
如 134表示拉取文本类、视频最佳截图照片、视频。
默认值：0
        :type InfoType: str
        """
        self.BizToken = None
        self.RuleId = None
        self.InfoType = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        self.RuleId = params.get("RuleId")
        self.InfoType = params.get("InfoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDetectInfoResponse(AbstractModel):
    """GetDetectInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param DetectInfo: JSON字符串。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetectInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DetectInfo = params.get("DetectInfo")
        self.RequestId = params.get("RequestId")


class GetEidResultRequest(AbstractModel):
    """GetEidResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param EidToken: E证通流程的唯一标识，调用GetEidToken接口时生成。
        :type EidToken: str
        :param InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证信息；3：最佳截图信息；5：意愿核身朗读模式相关结果；6：意愿核身问答模式相关结果）。
如 13表示拉取文本类、最佳截图信息。
默认值：0
        :type InfoType: str
        :param BestFramesCount: 从活体视频中截取一定张数的最佳帧。默认为0，最大为3，超出3的最多只给3张。（InfoType需要包含3）
        :type BestFramesCount: int
        """
        self.EidToken = None
        self.InfoType = None
        self.BestFramesCount = None


    def _deserialize(self, params):
        self.EidToken = params.get("EidToken")
        self.InfoType = params.get("InfoType")
        self.BestFramesCount = params.get("BestFramesCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEidResultResponse(AbstractModel):
    """GetEidResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 文本类信息。（基于对敏感信息的保护，验证使用的姓名和身份证号统一通过加密后从Eidinfo参数中返回，如需获取请在控制台申请返回身份信息，详见[E证通获取实名信息指引](https://cloud.tencent.com/document/product/1007/63370)）
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.faceid.v20180301.models.DetectInfoText`
        :param IdCardData: 身份证照片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoIdCardData`
        :param BestFrame: 最佳帧信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.DetectInfoBestFrame`
        :param EidInfo: Eid信息。（包括商户下用户唯一标识以及加密后的姓名、身份证号信息。解密方式详见[E证通获取实名信息指引](https://cloud.tencent.com/document/product/1007/63370)）
注意：此字段可能返回 null，表示取不到有效值。
        :type EidInfo: :class:`tencentcloud.faceid.v20180301.models.EidInfo`
        :param IntentionVerifyData: 意愿核身朗读模式相关信息。若未使用意愿核身朗读功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyData: :class:`tencentcloud.faceid.v20180301.models.IntentionVerifyData`
        :param IntentionQuestionResult: 意愿核身问答模式相关信息。若未使用意愿核身问答模式功能，该字段返回值可以不处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionQuestionResult: :class:`tencentcloud.faceid.v20180301.models.IntentionQuestionResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Text = None
        self.IdCardData = None
        self.BestFrame = None
        self.EidInfo = None
        self.IntentionVerifyData = None
        self.IntentionQuestionResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self.Text = DetectInfoText()
            self.Text._deserialize(params.get("Text"))
        if params.get("IdCardData") is not None:
            self.IdCardData = DetectInfoIdCardData()
            self.IdCardData._deserialize(params.get("IdCardData"))
        if params.get("BestFrame") is not None:
            self.BestFrame = DetectInfoBestFrame()
            self.BestFrame._deserialize(params.get("BestFrame"))
        if params.get("EidInfo") is not None:
            self.EidInfo = EidInfo()
            self.EidInfo._deserialize(params.get("EidInfo"))
        if params.get("IntentionVerifyData") is not None:
            self.IntentionVerifyData = IntentionVerifyData()
            self.IntentionVerifyData._deserialize(params.get("IntentionVerifyData"))
        if params.get("IntentionQuestionResult") is not None:
            self.IntentionQuestionResult = IntentionQuestionResult()
            self.IntentionQuestionResult._deserialize(params.get("IntentionQuestionResult"))
        self.RequestId = params.get("RequestId")


class GetEidTokenConfig(AbstractModel):
    """获取token时的的配置

    """

    def __init__(self):
        r"""
        :param InputType: 姓名身份证输入方式。
1：传身份证正反面OCR   
2：传身份证正面OCR  
3：用户手动输入  
4：客户后台传入  
默认1
注：使用OCR时仅支持用户修改结果中的姓名
        :type InputType: str
        :param UseIntentionVerify: 是否使用意愿核身，默认不使用。注意：如开启使用，则计费标签按【意愿核身】计费标签计价；如不开启，则计费标签按【E证通】计费标签计价，价格详见：[价格说明](https://cloud.tencent.com/document/product/1007/56804)。
        :type UseIntentionVerify: bool
        :param IntentionMode: 意愿核身模式。枚举值：1( 朗读模式)，2（问答模式） 。默认值1
        :type IntentionMode: str
        :param IntentionVerifyText: 意愿核身朗读模式使用的文案，若未使用意愿核身朗读功能，该字段无需传入。默认为空，最长可接受120的字符串长度。
        :type IntentionVerifyText: str
        :param IntentionQuestions: 意愿核身问答模式的配置列表。当前仅支持一个问答。
        :type IntentionQuestions: list of IntentionQuestion
        """
        self.InputType = None
        self.UseIntentionVerify = None
        self.IntentionMode = None
        self.IntentionVerifyText = None
        self.IntentionQuestions = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        self.UseIntentionVerify = params.get("UseIntentionVerify")
        self.IntentionMode = params.get("IntentionMode")
        self.IntentionVerifyText = params.get("IntentionVerifyText")
        if params.get("IntentionQuestions") is not None:
            self.IntentionQuestions = []
            for item in params.get("IntentionQuestions"):
                obj = IntentionQuestion()
                obj._deserialize(item)
                self.IntentionQuestions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEidTokenRequest(AbstractModel):
    """GetEidToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: EID商户id，字段长度最长50位。
        :type MerchantId: str
        :param IdCard: 身份标识（未使用OCR服务时，必须传入）。
规则：a-zA-Z0-9组合。最长长度32位。
        :type IdCard: str
        :param Name: 姓名。（未使用OCR服务时，必须传入）最长长度32位。中文请使用UTF-8编码。
        :type Name: str
        :param Extra: 透传字段，在获取验证结果时返回。最长长度1024位。
        :type Extra: str
        :param Config: 小程序模式配置，包括如何传入姓名身份证的配置，以及是否使用意愿核身。
        :type Config: :class:`tencentcloud.faceid.v20180301.models.GetEidTokenConfig`
        :param RedirectUrl: 最长长度1024位。用户从Url中进入核身认证结束后重定向的回调链接地址。EidToken会在该链接的query参数中。
        :type RedirectUrl: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.MerchantId = None
        self.IdCard = None
        self.Name = None
        self.Extra = None
        self.Config = None
        self.RedirectUrl = None
        self.Encryption = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Extra = params.get("Extra")
        if params.get("Config") is not None:
            self.Config = GetEidTokenConfig()
            self.Config._deserialize(params.get("Config"))
        self.RedirectUrl = params.get("RedirectUrl")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEidTokenResponse(AbstractModel):
    """GetEidToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param EidToken: 一次核身流程的标识，有效时间为600秒；
完成核身后，可用该标识获取验证结果信息。
        :type EidToken: str
        :param Url: 发起核身流程的URL，用于H5场景核身。
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EidToken = None
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EidToken = params.get("EidToken")
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class GetFaceIdResultRequest(AbstractModel):
    """GetFaceIdResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param FaceIdToken: SDK人脸核身流程的标识，调用GetFaceIdToken接口时生成。
        :type FaceIdToken: str
        :param IsNeedVideo: 是否需要拉取视频，默认false不需要
        :type IsNeedVideo: bool
        :param IsNeedBestFrame: 是否需要拉取截帧，默认false不需要
        :type IsNeedBestFrame: bool
        """
        self.FaceIdToken = None
        self.IsNeedVideo = None
        self.IsNeedBestFrame = None


    def _deserialize(self, params):
        self.FaceIdToken = params.get("FaceIdToken")
        self.IsNeedVideo = params.get("IsNeedVideo")
        self.IsNeedBestFrame = params.get("IsNeedBestFrame")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFaceIdResultResponse(AbstractModel):
    """GetFaceIdResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Result: 业务核验结果，参考https://cloud.tencent.com/document/product/1007/47912
        :type Result: str
        :param Description: 业务核验描述
        :type Description: str
        :param Similarity: 相似度，0-100，数值越大相似度越高
        :type Similarity: float
        :param VideoBase64: 用户核验的视频base64，如果选择了使用cos，返回完整cos地址如https://bucket.cos.ap-guangzhou.myqcloud.com/objectKey
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoBase64: str
        :param BestFrameBase64: 用户核验视频的截帧base64，如果选择了使用cos，返回完整cos地址如https://bucket.cos.ap-guangzhou.myqcloud.com/objectKey
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Extra: 获取token时透传的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param DeviceInfoTag: 设备风险标签，仅错误码返回1007（设备疑似被劫持）时返回风险标签。标签说明：
202、5001：设备疑似被Root
203、5004：设备疑似被注入
205：设备疑似被Hook
206：设备疑似虚拟运行环境
5007、1005：设备疑似摄像头被劫持
8000：设备疑似存在异常篡改行为
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceInfoTag: str
        :param RiskInfoTag: 行为风险标签，仅错误码返回1007（设备疑似被劫持）时返回风险标签。标签说明：
02：攻击风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskInfoTag: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdCard = None
        self.Name = None
        self.Result = None
        self.Description = None
        self.Similarity = None
        self.VideoBase64 = None
        self.BestFrameBase64 = None
        self.Extra = None
        self.DeviceInfoTag = None
        self.RiskInfoTag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Similarity = params.get("Similarity")
        self.VideoBase64 = params.get("VideoBase64")
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Extra = params.get("Extra")
        self.DeviceInfoTag = params.get("DeviceInfoTag")
        self.RiskInfoTag = params.get("RiskInfoTag")
        self.RequestId = params.get("RequestId")


class GetFaceIdTokenRequest(AbstractModel):
    """GetFaceIdToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompareLib: 本地上传照片(LOCAL)、商业库(BUSINESS)
        :type CompareLib: str
        :param IdCard: CompareLib为商业库时必传。
        :type IdCard: str
        :param Name: CompareLib为商业库库时必传。
        :type Name: str
        :param ImageBase64: CompareLib为上传照片比对时必传，Base64后图片最大8MB。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param Meta: SDK中生成的Meta字符串
        :type Meta: str
        :param Extra: 透传参数 1000长度字符串
        :type Extra: str
        :param UseCos: 默认为false，设置该参数为true后，核身过程中的视频图片将会存储在人脸核身控制台授权cos的bucket中，拉取结果时会返回对应资源完整cos地址。开通地址见https://console.cloud.tencent.com/faceid/cos
【注意】选择该参数为true后将不返回base64数据，请根据接入情况谨慎修改。
        :type UseCos: bool
        """
        self.CompareLib = None
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.Meta = None
        self.Extra = None
        self.UseCos = None


    def _deserialize(self, params):
        self.CompareLib = params.get("CompareLib")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.Meta = params.get("Meta")
        self.Extra = params.get("Extra")
        self.UseCos = params.get("UseCos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFaceIdTokenResponse(AbstractModel):
    """GetFaceIdToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param FaceIdToken: 有效期 10分钟。只能完成1次核身。
        :type FaceIdToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceIdToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceIdToken = params.get("FaceIdToken")
        self.RequestId = params.get("RequestId")


class GetLiveCodeRequest(AbstractModel):
    """GetLiveCode请求参数结构体

    """


class GetLiveCodeResponse(AbstractModel):
    """GetLiveCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param LiveCode: 数字验证码，如：1234
        :type LiveCode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LiveCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LiveCode = params.get("LiveCode")
        self.RequestId = params.get("RequestId")


class GetRealNameAuthResultRequest(AbstractModel):
    """GetRealNameAuthResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param AuthToken: 实名认证凭证
        :type AuthToken: str
        """
        self.AuthToken = None


    def _deserialize(self, params):
        self.AuthToken = params.get("AuthToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRealNameAuthResultResponse(AbstractModel):
    """GetRealNameAuthResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultType: 认证结果码，收费情况如下：

收费码：
0:  姓名和身份证号一致
-1: 姓名和身份证号不一致
-2: 姓名和微信实名姓名不一致

不收费码：
-3: 微信号未实名
        :type ResultType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultType = params.get("ResultType")
        self.RequestId = params.get("RequestId")


class GetRealNameAuthTokenRequest(AbstractModel):
    """GetRealNameAuthToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 姓名
        :type Name: str
        :param IDCard: 身份证号
        :type IDCard: str
        :param CallbackURL: 回调地址。实名认证完成后，将会重定向到这个地址通知认证发起方。仅支持http或https协议。
        :type CallbackURL: str
        """
        self.Name = None
        self.IDCard = None
        self.CallbackURL = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IDCard = params.get("IDCard")
        self.CallbackURL = params.get("CallbackURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRealNameAuthTokenResponse(AbstractModel):
    """GetRealNameAuthToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param AuthToken: 查询实名认证结果的唯一凭证
        :type AuthToken: str
        :param RedirectURL: 实名认证授权地址，认证发起方需要重定向到这个地址获取认证用户的授权，仅能在微信环境下打开。
        :type RedirectURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuthToken = None
        self.RedirectURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuthToken = params.get("AuthToken")
        self.RedirectURL = params.get("RedirectURL")
        self.RequestId = params.get("RequestId")


class GetWeChatBillDetailsRequest(AbstractModel):
    """GetWeChatBillDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param Date: 拉取的日期（YYYY-MM-DD）。最大可追溯到365天前。当天6点后才能拉取前一天的数据。
        :type Date: str
        :param Cursor: 游标。用于分页，取第一页时传0，取后续页面时，传入本接口响应中返回的NextCursor字段的值。
        :type Cursor: int
        :param RuleId: 需要拉取账单详情业务对应的RuleId。不传会返回所有RuleId数据。默认为空字符串。
        :type RuleId: str
        """
        self.Date = None
        self.Cursor = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Cursor = params.get("Cursor")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWeChatBillDetailsResponse(AbstractModel):
    """GetWeChatBillDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param HasNextPage: 是否还有下一页。该字段为true时，需要将NextCursor的值作为入参Cursor继续调用本接口。
        :type HasNextPage: bool
        :param NextCursor: 下一页的游标。用于分页。
        :type NextCursor: int
        :param WeChatBillDetails: 数据
        :type WeChatBillDetails: list of WeChatBillDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HasNextPage = None
        self.NextCursor = None
        self.WeChatBillDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HasNextPage = params.get("HasNextPage")
        self.NextCursor = params.get("NextCursor")
        if params.get("WeChatBillDetails") is not None:
            self.WeChatBillDetails = []
            for item in params.get("WeChatBillDetails"):
                obj = WeChatBillDetail()
                obj._deserialize(item)
                self.WeChatBillDetails.append(obj)
        self.RequestId = params.get("RequestId")


class IdCardOCRVerificationRequest(AbstractModel):
    """IdCardOCRVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
姓名和身份证号、ImageBase64、ImageUrl三者必须提供其中之一。若都提供了，则按照姓名和身份证号>ImageBase64>ImageUrl的优先级使用参数。
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param ImageBase64: 身份证人像面的 Base64 值
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param ImageUrl: 身份证人像面的 Url 地址
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdCardOCRVerificationResponse(AbstractModel):
    """IdCardOCRVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
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
        :param Description: 业务结果描述。
        :type Description: str
        :param Name: 用于验证的姓名
        :type Name: str
        :param IdCard: 用于验证的身份证号
        :type IdCard: str
        :param Sex: OCR得到的性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param Nation: OCR得到的民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Nation: str
        :param Birth: OCR得到的生日
注意：此字段可能返回 null，表示取不到有效值。
        :type Birth: str
        :param Address: OCR得到的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.Name = None
        self.IdCard = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.IdCard = params.get("IdCard")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.RequestId = params.get("RequestId")


class IdCardVerificationRequest(AbstractModel):
    """IdCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdCardVerificationResponse(AbstractModel):
    """IdCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
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
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class ImageRecognitionRequest(AbstractModel):
    """ImageRecognition请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名。中文请使用UTF-8编码。
        :type Name: str
        :param ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param Optional: 本接口不需要传递此参数。
        :type Optional: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.Optional = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.Optional = params.get("Optional")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRecognitionResponse(AbstractModel):
    """ImageRecognition返回参数结构体

    """

    def __init__(self):
        r"""
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Sim = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class IntentionQuestion(AbstractModel):
    """意愿核身过程中播报的问题文本、用户回答的标准文本。

    """

    def __init__(self):
        r"""
        :param Question: 系统播报的问题文本，问题最大长度为150个字符。
        :type Question: str
        :param Answers: 用户答案的标准文本列表，用于识别用户回答的语音与标准文本是否一致。列表长度最大为50，单个答案长度限制10个字符。
        :type Answers: list of str
        """
        self.Question = None
        self.Answers = None


    def _deserialize(self, params):
        self.Question = params.get("Question")
        self.Answers = params.get("Answers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionQuestionResult(AbstractModel):
    """意愿核身问答模式结果

    """

    def __init__(self):
        r"""
        :param FinalResultCode: 意愿核身最终结果：
0：认证通过，-1：认证未通过，-2：浏览器内核不兼容，无法进行意愿校验
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalResultCode: str
        :param Video: 视频base64（其中包含全程问题和回答音频，mp4格式）
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: str
        :param ScreenShot: 屏幕截图base64列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ScreenShot: list of str
        :param ResultCode: 和答案匹配结果列表
0：成功，-1：不匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: list of str
        :param AsrResult: 回答问题语音识别结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrResult: list of str
        :param Audios: 答案录音音频
注意：此字段可能返回 null，表示取不到有效值。
        :type Audios: list of str
        """
        self.FinalResultCode = None
        self.Video = None
        self.ScreenShot = None
        self.ResultCode = None
        self.AsrResult = None
        self.Audios = None


    def _deserialize(self, params):
        self.FinalResultCode = params.get("FinalResultCode")
        self.Video = params.get("Video")
        self.ScreenShot = params.get("ScreenShot")
        self.ResultCode = params.get("ResultCode")
        self.AsrResult = params.get("AsrResult")
        self.Audios = params.get("Audios")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentionVerifyData(AbstractModel):
    """意愿核身相关结果

    """

    def __init__(self):
        r"""
        :param IntentionVerifyVideo: 意愿确认环节中录制的视频（base64）。若不存在则为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyVideo: str
        :param AsrResult: 意愿确认环节中用户语音转文字的识别结果。若不存在则为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrResult: str
        :param ErrorCode: 意愿确认环节的结果码。当该结果码为0时，语音朗读的视频与语音识别结果才会返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: int
        :param ErrorMessage: 意愿确认环节的结果信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param IntentionVerifyBestFrame: 意愿确认环节中录制视频的最佳帧（base64）。若不存在则为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentionVerifyBestFrame: str
        :param AsrResultSimilarity: 本次流程用户语音与传入文本比对的相似度分值，取值范围 [0.00, 100.00]。只有配置了相似度阈值后才进行语音校验并返回相似度分值。
注意：此字段可能返回 null，表示取不到有效值。
        :type AsrResultSimilarity: str
        """
        self.IntentionVerifyVideo = None
        self.AsrResult = None
        self.ErrorCode = None
        self.ErrorMessage = None
        self.IntentionVerifyBestFrame = None
        self.AsrResultSimilarity = None


    def _deserialize(self, params):
        self.IntentionVerifyVideo = params.get("IntentionVerifyVideo")
        self.AsrResult = params.get("AsrResult")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        self.IntentionVerifyBestFrame = params.get("IntentionVerifyBestFrame")
        self.AsrResultSimilarity = params.get("AsrResultSimilarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessCompareRequest(AbstractModel):
    """LivenessCompare请求参数结构体

    """

    def __init__(self):
        r"""
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ImageBase64: 用于人脸比对的照片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。

图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageBase64。
        :type ImageBase64: str
        :param ImageUrl: 用于人脸比对照片的URL地址；图片下载后经Base64编码后的数据大小不超过3M，仅支持jpg、png格式。

图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageBase64。

图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param ValidateData: 数字模式传参：传数字验证码，验证码需先调用<a href="https://cloud.tencent.com/document/product/1007/31821">获取数字验证码接口</a>得到；
动作模式传参：传动作顺序，动作顺序需先调用<a href="https://cloud.tencent.com/document/product/1007/31822">获取动作顺序接口</a>得到；
静默模式传参：空。
        :type ValidateData: str
        :param Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围2-10
}
        :type Optional: str
        :param VideoBase64: 用于活体检测的视频，视频的Base64值；
Base64编码后的大小不超过8M，支持mp4、avi、flv格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。

视频的 VideoUrl、VideoBase64 必须提供一个，如果都提供，只使用 VideoBase64。
        :type VideoBase64: str
        :param VideoUrl: 用于活体检测的视频Url 地址。视频下载后经Base64编码后不超过 8M，视频下载耗时不超过4S，支持mp4、avi、flv格式。

视频的 VideoUrl、VideoBase64 必须提供一个，如果都提供，只使用 VideoBase64。

建议视频存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议视频存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type VideoUrl: str
        """
        self.LivenessType = None
        self.ImageBase64 = None
        self.ImageUrl = None
        self.ValidateData = None
        self.Optional = None
        self.VideoBase64 = None
        self.VideoUrl = None


    def _deserialize(self, params):
        self.LivenessType = params.get("LivenessType")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")
        self.VideoBase64 = params.get("VideoBase64")
        self.VideoUrl = params.get("VideoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessCompareResponse(AbstractModel):
    """LivenessCompare返回参数结构体

    """

    def __init__(self):
        r"""
        :param BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）。
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param BestFrameList: 最佳截图列表，仅在配置了返回多张最佳截图时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")


class LivenessRecognitionRequest(AbstractModel):
    """LivenessRecognition请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名。中文请使用UTF-8编码。
        :type Name: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过8M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param VideoUrl: 用于活体检测的视频Url 地址。视频下载后经Base64编码不超过 8M，视频下载耗时不超过4S，支持mp4、avi、flv格式。

视频的 VideoUrl、VideoBase64 必须提供一个，如果都提供，只使用 VideoBase64。

建议视频存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议视频存储于腾讯云。非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type VideoUrl: str
        :param ValidateData: 数字模式传参：传数字验证码，验证码需先调用<a href="https://cloud.tencent.com/document/product/1007/31821">获取数字验证码接口</a>得到；
动作模式传参：传动作顺序，动作顺序需先调用<a href="https://cloud.tencent.com/document/product/1007/31822">获取动作顺序接口</a>得到；
静默模式传参：空。
        :type ValidateData: str
        :param Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围2-10
}
        :type Optional: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.LivenessType = None
        self.VideoBase64 = None
        self.VideoUrl = None
        self.ValidateData = None
        self.Optional = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.LivenessType = params.get("LivenessType")
        self.VideoBase64 = params.get("VideoBase64")
        self.VideoUrl = params.get("VideoUrl")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessRecognitionResponse(AbstractModel):
    """LivenessRecognition返回参数结构体

    """

    def __init__(self):
        r"""
        :param BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param BestFrameList: 最佳截图列表，仅在配置了返回多张最佳截图时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")


class LivenessRequest(AbstractModel):
    """Liveness请求参数结构体

    """

    def __init__(self):
        r"""
        :param VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过8M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：不需要传递此参数。
        :type ValidateData: str
        :param Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围1-10
}
        :type Optional: str
        """
        self.VideoBase64 = None
        self.LivenessType = None
        self.ValidateData = None
        self.Optional = None


    def _deserialize(self, params):
        self.VideoBase64 = params.get("VideoBase64")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessResponse(AbstractModel):
    """Liveness返回参数结构体

    """

    def __init__(self):
        r"""
        :param BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param BestFrameList: 最佳最佳截图列表，仅在配置了返回多张最佳截图时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")


class MinorsVerificationRequest(AbstractModel):
    """MinorsVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 参与校验的参数类型。
0：使用手机号进行校验；
1：使用姓名与身份证号进行校验。
        :type Type: str
        :param Mobile: 手机号，11位数字，
特别提示：
手机号验证只限制在腾讯健康守护可信模型覆盖的数据范围内，与手机号本身在运营商是否实名无关联，不在范围会提示“手机号未实名”，建议客户与传入姓名和身份证号信息组合使用。
        :type Mobile: str
        :param IdCard: 身份证号码。
        :type IdCard: str
        :param Name: 姓名。
        :type Name: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.Type = None
        self.Mobile = None
        self.IdCard = None
        self.Name = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Mobile = params.get("Mobile")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MinorsVerificationResponse(AbstractModel):
    """MinorsVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 结果码，收费情况如下。
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
        :param Description: 业务结果描述。
        :type Description: str
        :param AgeRange: 该字段的值为年龄区间。格式为[a,b)，
[0,8)表示年龄小于8周岁区间，不包括8岁；
[8,16)表示年龄8-16周岁区间，不包括16岁；
[16,18)表示年龄16-18周岁区间，不包括18岁；
[18,+)表示年龄大于18周岁。
        :type AgeRange: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.AgeRange = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.AgeRange = params.get("AgeRange")
        self.RequestId = params.get("RequestId")


class MobileNetworkTimeVerificationRequest(AbstractModel):
    """MobileNetworkTimeVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Mobile: 手机号码
        :type Mobile: str
        :param Encryption: 敏感数据加密信息。对传入信息（手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.Mobile = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MobileNetworkTimeVerificationResponse(AbstractModel):
    """MobileNetworkTimeVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 成功
-2: 手机号不存在
-3: 手机号存在，但无法查询到在网时长
不收费结果码：
-1: 手机号格式不正确
-4: 验证中心服务繁忙
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param Range: 在网时长区间。
格式为(a,b]，表示在网时长在a个月以上，b个月以下。若b为+时表示没有上限。
        :type Range: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.Range = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Range = params.get("Range")
        self.RequestId = params.get("RequestId")


class MobileStatusRequest(AbstractModel):
    """MobileStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Mobile: 手机号码
        :type Mobile: str
        :param Encryption: 敏感数据加密信息。对传入信息（手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.Mobile = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MobileStatusResponse(AbstractModel):
    """MobileStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0：成功
不收费结果码：
-1：未查询到结果
-2：手机号格式不正确
-3：验证中心服务繁忙
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param StatusCode: 状态码：
0：正常
1：停机
2：销号
3：空号
4：不在网
99：未知状态
        :type StatusCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.StatusCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.StatusCode = params.get("StatusCode")
        self.RequestId = params.get("RequestId")


class ParseNfcDataRequest(AbstractModel):
    """ParseNfcData请求参数结构体

    """

    def __init__(self):
        r"""
        :param ReqId: 前端SDK返回
        :type ReqId: str
        """
        self.ReqId = None


    def _deserialize(self, params):
        self.ReqId = params.get("ReqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseNfcDataResponse(AbstractModel):
    """ParseNfcData返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultCode: 0为首次查询成功，-1为查询失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultCode: str
        :param IdNum: 身份证号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdNum: str
        :param Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Picture: 照片
注意：此字段可能返回 null，表示取不到有效值。
        :type Picture: str
        :param BirthDate: 出生日期
注意：此字段可能返回 null，表示取不到有效值。
        :type BirthDate: str
        :param BeginTime: 有效期起始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: str
        :param EndTime: 有效期结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Address: 住址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Nation: 民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Nation: str
        :param Sex: 性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param IdType: 身份证 01 中国护照 03 军官证 04 武警证 05 港澳通行证 06 台胞证 07 外国护照 08 士兵证 09 临时身份证 10 户口本 11 警官证 12 外国人永久居留证 13 港澳台居民居住证 14 回乡证 15 大陆居民来往台湾通行证 16 其他证件 99
注意：此字段可能返回 null，表示取不到有效值。
        :type IdType: str
        :param EnName: 英文姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type EnName: str
        :param SigningOrganization: 签发机关
注意：此字段可能返回 null，表示取不到有效值。
        :type SigningOrganization: str
        :param OtherIdNum: 港澳台居民居住证，通行证号码
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherIdNum: str
        :param Nationality: 旅行证件国籍
注意：此字段可能返回 null，表示取不到有效值。
        :type Nationality: str
        :param PersonalNumber: 旅行证件机读区第二行 29~42 位
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonalNumber: str
        :param CheckMRTD: 旅行证件类的核验结果。JSON格式如下：
{"result_issuer ":"签发者证书合法性验证结果 ","result_pape r":"证件安全对象合法性验证 结果 ","result_data" :"防数据篡改验证结果 ","result_chip" :"防证书件芯片被复制验证结果"} 
 0:验证通过，1: 验证不通过，2: 未验证，3:部分通过，当4项核验结果都为0时，表示证件为真
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckMRTD: str
        :param ImageA: 身份证照片面合成图片
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageA: str
        :param ImageB: 身份证国徽面合成图片
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageB: str
        :param ResultDescription: 对result code的结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultDescription: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCode = None
        self.IdNum = None
        self.Name = None
        self.Picture = None
        self.BirthDate = None
        self.BeginTime = None
        self.EndTime = None
        self.Address = None
        self.Nation = None
        self.Sex = None
        self.IdType = None
        self.EnName = None
        self.SigningOrganization = None
        self.OtherIdNum = None
        self.Nationality = None
        self.PersonalNumber = None
        self.CheckMRTD = None
        self.ImageA = None
        self.ImageB = None
        self.ResultDescription = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCode = params.get("ResultCode")
        self.IdNum = params.get("IdNum")
        self.Name = params.get("Name")
        self.Picture = params.get("Picture")
        self.BirthDate = params.get("BirthDate")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Address = params.get("Address")
        self.Nation = params.get("Nation")
        self.Sex = params.get("Sex")
        self.IdType = params.get("IdType")
        self.EnName = params.get("EnName")
        self.SigningOrganization = params.get("SigningOrganization")
        self.OtherIdNum = params.get("OtherIdNum")
        self.Nationality = params.get("Nationality")
        self.PersonalNumber = params.get("PersonalNumber")
        self.CheckMRTD = params.get("CheckMRTD")
        self.ImageA = params.get("ImageA")
        self.ImageB = params.get("ImageB")
        self.ResultDescription = params.get("ResultDescription")
        self.RequestId = params.get("RequestId")


class PhoneVerificationCMCCRequest(AbstractModel):
    """PhoneVerificationCMCC请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Phone: 手机号
        :type Phone: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.Phone = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationCMCCResponse(AbstractModel):
    """PhoneVerificationCMCC返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 认证通过
-4: 信息不一致（手机号已实名，但姓名和身份证号与实名信息不一致）
不收费结果码：
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-10: 认证未通过
-11: 验证中心服务繁忙
        :type Result: str
        :param Isp: 运营商名称。
取值范围为["移动","联通","电信",""]
        :type Isp: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Isp = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Isp = params.get("Isp")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class PhoneVerificationCTCCRequest(AbstractModel):
    """PhoneVerificationCTCC请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Phone: 手机号
        :type Phone: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.Phone = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationCTCCResponse(AbstractModel):
    """PhoneVerificationCTCC返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 认证通过
-4: 信息不一致（手机号已实名，但姓名和身份证号与实名信息不一致）
不收费结果码：
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-10: 认证未通过
-11: 验证中心服务繁忙
        :type Result: str
        :param Isp: 运营商名称。
取值范围为["移动","联通","电信",""]
        :type Isp: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Isp = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Isp = params.get("Isp")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class PhoneVerificationCUCCRequest(AbstractModel):
    """PhoneVerificationCUCC请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Phone: 手机号
        :type Phone: str
        :param Encryption: 敏感数据加密信息。对传入信息（姓名、身份证号、手机号）有加密需求的用户可使用此参数，详情请点击左侧链接。
        :type Encryption: :class:`tencentcloud.faceid.v20180301.models.Encryption`
        """
        self.IdCard = None
        self.Name = None
        self.Phone = None
        self.Encryption = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        if params.get("Encryption") is not None:
            self.Encryption = Encryption()
            self.Encryption._deserialize(params.get("Encryption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationCUCCResponse(AbstractModel):
    """PhoneVerificationCUCC返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 认证通过
-4: 信息不一致（手机号已实名，但姓名和身份证号与实名信息不一致）
不收费结果码：
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-10: 认证未通过
-11: 验证中心服务繁忙
        :type Result: str
        :param Isp: 运营商名称。
取值范围为["移动","联通","电信",""]
        :type Isp: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Isp = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Isp = params.get("Isp")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class PhoneVerificationRequest(AbstractModel):
    """PhoneVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Phone: 手机号
        :type Phone: str
        :param CiphertextBlob: 有加密需求的用户，传入kms的CiphertextBlob，关于数据加密可查阅 <a href="https://cloud.tencent.com/document/product/1007/47180">数据加密</a> 文档。
        :type CiphertextBlob: str
        :param EncryptList: 在使用加密服务时，填入要被加密的字段。本接口中可填入加密后的IdCard，Name，Phone中的一个或多个。
        :type EncryptList: list of str
        :param Iv: 有加密需求的用户，传入CBC加密的初始向量。
        :type Iv: str
        """
        self.IdCard = None
        self.Name = None
        self.Phone = None
        self.CiphertextBlob = None
        self.EncryptList = None
        self.Iv = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.EncryptList = params.get("EncryptList")
        self.Iv = params.get("Iv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneVerificationResponse(AbstractModel):
    """PhoneVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 认证结果码:
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
        :param Description: 业务结果描述。
        :type Description: str
        :param Isp: 运营商名称。
取值范围为["","移动","电信","联通"]
        :type Isp: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.Isp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Isp = params.get("Isp")
        self.RequestId = params.get("RequestId")


class WeChatBillDetail(AbstractModel):
    """账单详情

    """

    def __init__(self):
        r"""
        :param BizToken: token
        :type BizToken: str
        :param ChargeCount: 本token收费次数
        :type ChargeCount: int
        :param ChargeDetails: 本token计费详情
        :type ChargeDetails: list of ChargeDetail
        :param RuleId: 业务RuleId
        :type RuleId: str
        """
        self.BizToken = None
        self.ChargeCount = None
        self.ChargeDetails = None
        self.RuleId = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        self.ChargeCount = params.get("ChargeCount")
        if params.get("ChargeDetails") is not None:
            self.ChargeDetails = []
            for item in params.get("ChargeDetails"):
                obj = ChargeDetail()
                obj._deserialize(item)
                self.ChargeDetails.append(obj)
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        