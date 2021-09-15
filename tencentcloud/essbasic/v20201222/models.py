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


class Address(AbstractModel):
    """此结构体 (Address) 用于描述住址或通讯地址。

    """

    def __init__(self):
        r"""
        :param Province: 省份
        :type Province: str
        :param City: 城市
        :type City: str
        :param County: 区县
        :type County: str
        :param Details: 详细地址
        :type Details: str
        :param Country: 国家，默认中国
        :type Country: str
        """
        self.Province = None
        self.City = None
        self.County = None
        self.Details = None
        self.Country = None


    def _deserialize(self, params):
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.County = params.get("County")
        self.Details = params.get("Details")
        self.Country = params.get("Country")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveFlowRequest(AbstractModel):
    """ArchiveFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 流程ID
        :type FlowId: str
        """
        self.Caller = None
        self.FlowId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveFlowResponse(AbstractModel):
    """ArchiveFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Caller(AbstractModel):
    """此结构体 (Caller) 用于描述调用方属性。

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用号
        :type ApplicationId: str
        :param SubOrganizationId: 下属机构ID
        :type SubOrganizationId: str
        :param OperatorId: 经办人的用户ID
        :type OperatorId: str
        """
        self.ApplicationId = None
        self.SubOrganizationId = None
        self.OperatorId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.OperatorId = params.get("OperatorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowRequest(AbstractModel):
    """CancelFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 流程ID
        :type FlowId: str
        :param CancelMessage: 撤销原因
        :type CancelMessage: str
        """
        self.Caller = None
        self.FlowId = None
        self.CancelMessage = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        self.CancelMessage = params.get("CancelMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowResponse(AbstractModel):
    """CancelFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CatalogApprovers(AbstractModel):
    """目录流程参与者

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
        :type FlowId: str
        :param Approvers: 参与者列表
        :type Approvers: list of FlowApproverInfo
        """
        self.FlowId = None
        self.Approvers = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self.Approvers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CatalogComponents(AbstractModel):
    """目录流程签署区

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
        :type FlowId: str
        :param SignComponents: 签署区列表
        :type SignComponents: list of Component
        :param SignId: 签署任务ID
        :type SignId: str
        """
        self.FlowId = None
        self.SignComponents = None
        self.SignId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard2EVerificationRequest(AbstractModel):
    """CheckBankCard2EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param BankCard: 银行卡号
        :type BankCard: str
        :param Name: 姓名
        :type Name: str
        """
        self.Caller = None
        self.BankCard = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.BankCard = params.get("BankCard")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard2EVerificationResponse(AbstractModel):
    """CheckBankCard2EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 检测结果
计费结果码：
  0:  认证通过
  1:  认证未通过
  2:  持卡人信息有误
  3:  未开通无卡支付
  4:  此卡被没收
  5:  无效卡号
  6:  此卡无对应发卡行
  7:  该卡未初始化或睡眠卡
  8:  作弊卡、吞卡
  9:  此卡已挂失
  10: 该卡已过期
  11: 受限制的卡
  12: 密码错误次数超限
  13: 发卡行不支持此交易
不收费结果码:
  101: 姓名校验不通过
  102: 银行卡号码有误
  103: 验证中心服务繁忙
  104: 身份证号码有误
  105: 手机号码不合法
        :type Result: int
        :param Description: 结果描述; 未通过时必选
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


class CheckBankCard3EVerificationRequest(AbstractModel):
    """CheckBankCard3EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param BankCard: 银行卡号
        :type BankCard: str
        :param Name: 姓名
        :type Name: str
        :param IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self.Caller = None
        self.BankCard = None
        self.Name = None
        self.IdCardNumber = None
        self.IdCardType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.BankCard = params.get("BankCard")
        self.Name = params.get("Name")
        self.IdCardNumber = params.get("IdCardNumber")
        self.IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard3EVerificationResponse(AbstractModel):
    """CheckBankCard3EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 检测结果
计费结果码：
  0:  认证通过
  1:  认证未通过
  2:  持卡人信息有误
  3:  未开通无卡支付
  4:  此卡被没收
  5:  无效卡号
  6:  此卡无对应发卡行
  7:  该卡未初始化或睡眠卡
  8:  作弊卡、吞卡
  9:  此卡已挂失
  10: 该卡已过期
  11: 受限制的卡
  12: 密码错误次数超限
  13: 发卡行不支持此交易
不收费结果码:
  101: 姓名校验不通过
  102: 银行卡号码有误
  103: 验证中心服务繁忙
  104: 身份证号码有误
  105: 手机号码不合法
        :type Result: int
        :param Description: 结果描述; 未通过时必选
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


class CheckBankCard4EVerificationRequest(AbstractModel):
    """CheckBankCard4EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param BankCard: 银行卡号
        :type BankCard: str
        :param Name: 姓名
        :type Name: str
        :param IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param Mobile: 手机号
        :type Mobile: str
        :param IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self.Caller = None
        self.BankCard = None
        self.Name = None
        self.IdCardNumber = None
        self.Mobile = None
        self.IdCardType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.BankCard = params.get("BankCard")
        self.Name = params.get("Name")
        self.IdCardNumber = params.get("IdCardNumber")
        self.Mobile = params.get("Mobile")
        self.IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard4EVerificationResponse(AbstractModel):
    """CheckBankCard4EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 检测结果
计费结果码：
  0:  认证通过
  1:  认证未通过
  2:  持卡人信息有误
  3:  未开通无卡支付
  4:  此卡被没收
  5:  无效卡号
  6:  此卡无对应发卡行
  7:  该卡未初始化或睡眠卡
  8:  作弊卡、吞卡
  9:  此卡已挂失
  10: 该卡已过期
  11: 受限制的卡
  12: 密码错误次数超限
  13: 发卡行不支持此交易
不收费结果码:
  101: 姓名校验不通过
  102: 银行卡号码有误
  103: 验证中心服务繁忙
  104: 身份证号码有误
  105: 手机号码不合法
        :type Result: int
        :param Description: 结果描述; 未通过时必选
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


class CheckBankCardVerificationRequest(AbstractModel):
    """CheckBankCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param BankCard: 银行卡号
        :type BankCard: str
        :param Name: 姓名
        :type Name: str
        :param IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param Mobile: 手机号
        :type Mobile: str
        :param IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self.Caller = None
        self.BankCard = None
        self.Name = None
        self.IdCardNumber = None
        self.Mobile = None
        self.IdCardType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.BankCard = params.get("BankCard")
        self.Name = params.get("Name")
        self.IdCardNumber = params.get("IdCardNumber")
        self.Mobile = params.get("Mobile")
        self.IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCardVerificationResponse(AbstractModel):
    """CheckBankCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 检测结果
计费结果码：
  0:  认证通过
  1:  认证未通过
  2:  持卡人信息有误
  3:  未开通无卡支付
  4:  此卡被没收
  5:  无效卡号
  6:  此卡无对应发卡行
  7:  该卡未初始化或睡眠卡
  8:  作弊卡、吞卡
  9:  此卡已挂失
  10: 该卡已过期
  11: 受限制的卡
  12: 密码错误次数超限
  13: 发卡行不支持此交易
不收费结果码:
  101: 姓名校验不通过
  102: 银行卡号码有误
  103: 验证中心服务繁忙
  104: 身份证号码有误
  105: 手机号码不合法
        :type Result: int
        :param Description: 结果描述; 未通过时必选
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


class CheckFaceIdentifyRequest(AbstractModel):
    """CheckFaceIdentify请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param VerifyChannel: 人脸核身渠道; 必选; WEIXINAPP:腾讯电子签小程序,FACEID:腾讯电子签慧眼,None:白名单中的客户直接通过
        :type VerifyChannel: str
        :param VerifyResult: 核身订单号; 必选; 对于WEIXINAPP,直接取响应的{VerifyResult};对于FACEID,使用{WbAppId}:{OrderNo}拼接
        :type VerifyResult: str
        :param Name: 要对比的姓名; 可选; 未填写时对比caller.OperatorId的实名信息
        :type Name: str
        :param IdCardNumber: 要对比的身份证号码; 可选; 未填写时对比caller.OperatorId的实名信息
        :type IdCardNumber: str
        :param GetPhoto: 是否取认证时的照片
        :type GetPhoto: bool
        """
        self.Caller = None
        self.VerifyChannel = None
        self.VerifyResult = None
        self.Name = None
        self.IdCardNumber = None
        self.GetPhoto = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.VerifyChannel = params.get("VerifyChannel")
        self.VerifyResult = params.get("VerifyResult")
        self.Name = params.get("Name")
        self.IdCardNumber = params.get("IdCardNumber")
        self.GetPhoto = params.get("GetPhoto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckFaceIdentifyResponse(AbstractModel):
    """CheckFaceIdentify返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 核身结果; 0:通过,1:不通过
        :type Result: int
        :param Description: 核身结果描述
        :type Description: str
        :param ChannelName: 渠道名
        :type ChannelName: str
        :param VerifiedOn: 认证通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifiedOn: int
        :param SerialNumber: 核身流水号
        :type SerialNumber: str
        :param VerifyServerIp: 渠道核身服务器IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyServerIp: str
        :param PhotoFileName: 核身照片文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type PhotoFileName: str
        :param PhotoFileData: 核身照片内容base64(文件格式见文件名后缀,一般为jpg)
注意：此字段可能返回 null，表示取不到有效值。
        :type PhotoFileData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.ChannelName = None
        self.VerifiedOn = None
        self.SerialNumber = None
        self.VerifyServerIp = None
        self.PhotoFileName = None
        self.PhotoFileData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.ChannelName = params.get("ChannelName")
        self.VerifiedOn = params.get("VerifiedOn")
        self.SerialNumber = params.get("SerialNumber")
        self.VerifyServerIp = params.get("VerifyServerIp")
        self.PhotoFileName = params.get("PhotoFileName")
        self.PhotoFileData = params.get("PhotoFileData")
        self.RequestId = params.get("RequestId")


class CheckIdCardVerificationRequest(AbstractModel):
    """CheckIdCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Name: 姓名
        :type Name: str
        :param IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self.Caller = None
        self.Name = None
        self.IdCardNumber = None
        self.IdCardType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Name = params.get("Name")
        self.IdCardNumber = params.get("IdCardNumber")
        self.IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIdCardVerificationResponse(AbstractModel):
    """CheckIdCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 检测结果; 
收费错误码:
  0: 通过,
  1: 姓名和身份证号不一致,
免费错误码:
  101: 非法身份证号(长度,格式等不正确),
  102: 非法姓名(长度,格式等不正确),
  103: 验证平台异常,
  104: 证件库中无此身份证记录
        :type Result: int
        :param Description: 结果描述; 未通过时必选
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


class CheckMobileAndNameRequest(AbstractModel):
    """CheckMobileAndName请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Mobile: 手机号
        :type Mobile: str
        :param Name: 姓名
        :type Name: str
        """
        self.Caller = None
        self.Mobile = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Mobile = params.get("Mobile")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckMobileAndNameResponse(AbstractModel):
    """CheckMobileAndName返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 检测结果
计费结果码：
  0:  验证结果一致
  1:  手机号未实名
  2:  姓名和手机号不一致
  3:  信息不一致(手机号已实名,但姓名和身份证号与实名信息不一致)
不收费结果码:
  101: 查无记录
  102: 非法姓名(长度,格式等不正确)
  103: 非法手机号(长度,格式等不正确)
  104: 非法身份证号(长度,校验位等不正确)
  105: 认证未通过
  106: 验证平台异常
        :type Result: int
        :param Description: 结果描述; 未通过时必选
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


class CheckMobileVerificationRequest(AbstractModel):
    """CheckMobileVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Mobile: 手机号
        :type Mobile: str
        :param Name: 姓名
        :type Name: str
        :param IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self.Caller = None
        self.Mobile = None
        self.Name = None
        self.IdCardNumber = None
        self.IdCardType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Mobile = params.get("Mobile")
        self.Name = params.get("Name")
        self.IdCardNumber = params.get("IdCardNumber")
        self.IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckMobileVerificationResponse(AbstractModel):
    """CheckMobileVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 检测结果
计费结果码：
  0:  验证结果一致
  1:  手机号未实名
  2:  姓名和手机号不一致
  3:  信息不一致(手机号已实名,但姓名和身份证号与实名信息不一致)
不收费结果码:
  101: 查无记录
  102: 非法姓名(长度,格式等不正确)
  103: 非法手机号(长度,格式等不正确)
  104: 非法身份证号(长度,校验位等不正确)
  105: 认证未通过
  106: 验证平台异常
        :type Result: int
        :param Description: 结果描述; 未通过时必选
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


class CheckVerifyCodeMatchFlowIdRequest(AbstractModel):
    """CheckVerifyCodeMatchFlowId请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Mobile: 手机号
        :type Mobile: str
        :param VerifyCode: 验证码
        :type VerifyCode: str
        :param FlowId: 流程(目录) id
        :type FlowId: str
        """
        self.Caller = None
        self.Mobile = None
        self.VerifyCode = None
        self.FlowId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Mobile = params.get("Mobile")
        self.VerifyCode = params.get("VerifyCode")
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckVerifyCodeMatchFlowIdResponse(AbstractModel):
    """CheckVerifyCodeMatchFlowId返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: true: 验证码正确，false: 验证码错误
        :type Success: bool
        :param Result: 0: 验证码正确 1:验证码错误或过期 2:验证码错误 3:验证码和流程不匹配 4:验证码输入错误超过次数 5:内部错误
6:参数错误
        :type Result: int
        :param Description: 结果描述
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Success = params.get("Success")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class Component(AbstractModel):
    """此结构体 (Component) 用于描述控件属性。

    """

    def __init__(self):
        r"""
        :param ComponentId: 控件编号

注：
当GenerateMode=3时，通过"^"来决定是否使用关键字整词匹配能力。
例：
当GenerateMode=3时，如果传入关键字"^甲方签署^"，则会在PDF文件中有且仅有"甲方签署"关键字的地方进行对应操作。
如传入的关键字为"甲方签署"，则PDF文件中每个出现关键字的位置都会执行相应操作。
        :type ComponentId: str
        :param ComponentType: 如果是Component控件类型，则可选的字段为：
TEXT - 普通文本控件；
DATE - 普通日期控件；
SELECT- 勾选框控件；
如果是SignComponent控件类型，则可选的字段为
SIGN_SEAL- 签署印章控件；
SIGN_DATE- 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
        :type ComponentType: str
        :param ComponentName: 控件名称
        :type ComponentName: str
        :param ComponentRequired: 定义控件是否为必填项，默认为false
        :type ComponentRequired: bool
        :param FileIndex: 控件所属文件的序号 (模板中的resourceId排列序号)
        :type FileIndex: int
        :param GenerateMode: 控件生成的方式：
0 - 普通控件
1 - 表单域
2 - html 控件
3 - 关键字
        :type GenerateMode: int
        :param ComponentWidth: 参数控件宽度，单位px
        :type ComponentWidth: float
        :param ComponentHeight: 参数控件高度，单位px
        :type ComponentHeight: float
        :param ComponentPage: 参数控件所在页码
        :type ComponentPage: int
        :param ComponentPosX: 参数控件X位置，单位px
        :type ComponentPosX: float
        :param ComponentPosY: 参数控件Y位置，单位px
        :type ComponentPosY: float
        :param ComponentExtra: 参数控件样式
        :type ComponentExtra: str
        :param ComponentValue: 印章ID，如果是手写签名则为jpg或png格式的base64图片

SIGN_SEAL控件,可以用ORG_DEFAULT_SEAL表示主企业的默认印章
SIGN_SEAL控件,可以用SUBORG_DEFAULT_SEAL表示子企业的默认印章
SIGN_SEAL控件,可以用USER_DEFAULT_SEAL表示个人默认印章
        :type ComponentValue: str
        :param SealOperate: 如果是SIGN_SEAL类型的签署控件, 参数标识H5签署界面是否在该签署区上进行放置展示, 1为放置,其他为不放置
        :type SealOperate: int
        :param GenerateExtra: 不同GenerateMode对应的额外信息
        :type GenerateExtra: str
        """
        self.ComponentId = None
        self.ComponentType = None
        self.ComponentName = None
        self.ComponentRequired = None
        self.FileIndex = None
        self.GenerateMode = None
        self.ComponentWidth = None
        self.ComponentHeight = None
        self.ComponentPage = None
        self.ComponentPosX = None
        self.ComponentPosY = None
        self.ComponentExtra = None
        self.ComponentValue = None
        self.SealOperate = None
        self.GenerateExtra = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")
        self.ComponentType = params.get("ComponentType")
        self.ComponentName = params.get("ComponentName")
        self.ComponentRequired = params.get("ComponentRequired")
        self.FileIndex = params.get("FileIndex")
        self.GenerateMode = params.get("GenerateMode")
        self.ComponentWidth = params.get("ComponentWidth")
        self.ComponentHeight = params.get("ComponentHeight")
        self.ComponentPage = params.get("ComponentPage")
        self.ComponentPosX = params.get("ComponentPosX")
        self.ComponentPosY = params.get("ComponentPosY")
        self.ComponentExtra = params.get("ComponentExtra")
        self.ComponentValue = params.get("ComponentValue")
        self.SealOperate = params.get("SealOperate")
        self.GenerateExtra = params.get("GenerateExtra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentSeal(AbstractModel):
    """此结构体 (ComponentSeal) 用于描述“签署区ID”到“印章ID”的映射。

    """

    def __init__(self):
        r"""
        :param ComponentId: 签署区ID
        :type ComponentId: str
        :param SealId: 印章ID
        :type SealId: str
        """
        self.ComponentId = None
        self.SealId = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")
        self.SealId = params.get("SealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFaceIdSignRequest(AbstractModel):
    """CreateFaceIdSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Values: 除api_ticket之外的其它要参与签名的参数值,包括UserId
        :type Values: list of str
        """
        self.Caller = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFaceIdSignResponse(AbstractModel):
    """CreateFaceIdSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param Sign: 慧眼API签名
        :type Sign: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Sign = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Sign = params.get("Sign")
        self.RequestId = params.get("RequestId")


class CreateFlowByFilesRequest(AbstractModel):
    """CreateFlowByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowInfo: 流程创建信息
        :type FlowInfo: :class:`tencentcloud.essbasic.v20201222.models.FlowInfo`
        :param FileIds: 文件资源列表 (支持多文件)
        :type FileIds: list of str
        :param CustomId: 自定义流程id
        :type CustomId: str
        """
        self.Caller = None
        self.FlowInfo = None
        self.FileIds = None
        self.CustomId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        if params.get("FlowInfo") is not None:
            self.FlowInfo = FlowInfo()
            self.FlowInfo._deserialize(params.get("FlowInfo"))
        self.FileIds = params.get("FileIds")
        self.CustomId = params.get("CustomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowByFilesResponse(AbstractModel):
    """CreateFlowByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程ID
        :type FlowId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateH5FaceIdUrlRequest(AbstractModel):
    """CreateH5FaceIdUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param WbAppId: 慧眼业务ID; 不填写时后台使用Caller反查
        :type WbAppId: str
        :param Name: 姓名; 可选(未通过实名认证的用户必选)
        :type Name: str
        :param IdCardType: 用户证件类型; 可选; 默认ID_CARD:中国居民身份证
        :type IdCardType: str
        :param IdCardNumber: 用户证件号; 可选(未通过实名认证的用户必选)
        :type IdCardNumber: str
        :param JumpUrl: H5人脸核身完成后回调的第三方Url; 可选; 不需要做Encode, 跳转的参数: ?code=XX&orderNo=XX&liveRate=xx, code=0表示成功,orderNo为订单号,liveRate为百分制活体检测得分
        :type JumpUrl: str
        :param JumpType: 参数值为"1":直接跳转到url回调地址; 可选; 其他值:跳转提供的结果页面
        :type JumpType: str
        :param OpenFrom: browser:表示在浏览器启动刷脸, app:表示在App里启动刷脸,默认值为browser; 可选
        :type OpenFrom: str
        :param RedirectType: 跳转类型; 可选; 参数值为"1"时,刷脸页面使用replace方式跳转,不在浏览器history中留下记录;不传或其他值则正常跳转
        :type RedirectType: str
        """
        self.Caller = None
        self.WbAppId = None
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.JumpUrl = None
        self.JumpType = None
        self.OpenFrom = None
        self.RedirectType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.WbAppId = params.get("WbAppId")
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.JumpUrl = params.get("JumpUrl")
        self.JumpType = params.get("JumpType")
        self.OpenFrom = params.get("OpenFrom")
        self.RedirectType = params.get("RedirectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateH5FaceIdUrlResponse(AbstractModel):
    """CreateH5FaceIdUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 跳转到人脸核身页面的链接
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class CreatePreviewSignUrlRequest(AbstractModel):
    """CreatePreviewSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Deadline: URL过期时间戳
        :type Deadline: int
        :param CatalogId: 目录ID。当 SignUrlType 为 CATALOG 时必填
        :type CatalogId: str
        :param FlowId: 流程ID。当 SignUrlType 为 FLOW 时必填
        :type FlowId: str
        :param SignUrlType: 签署链接类型：
1. FLOW - 单流程签署 (默认) 
2. CATALOG - 目录签署
        :type SignUrlType: str
        """
        self.Caller = None
        self.Deadline = None
        self.CatalogId = None
        self.FlowId = None
        self.SignUrlType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Deadline = params.get("Deadline")
        self.CatalogId = params.get("CatalogId")
        self.FlowId = params.get("FlowId")
        self.SignUrlType = params.get("SignUrlType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePreviewSignUrlResponse(AbstractModel):
    """CreatePreviewSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param PreviewSignUrl: 合同预览URL
        :type PreviewSignUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PreviewSignUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreviewSignUrl = params.get("PreviewSignUrl")
        self.RequestId = params.get("RequestId")


class CreateSealRequest(AbstractModel):
    """CreateSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param SealType: 印章类型：
1. PERSONAL - 个人私章
2. OFFICIAL - 公章
3. SPECIAL_FINANCIAL - 财务专用章
4. CONTRACT - 合同专用章
5. LEGAL_REPRESENTATIVE - 法定代表人章
6. SPECIAL_NATIONWIDE_INVOICE - 发票专用章
7. OTHER-其他
        :type SealType: str
        :param SealName: 印章名称
        :type SealName: str
        :param SourceIp: 请求创建印章的客户端IP
        :type SourceIp: str
        :param Image: 印章图片，base64编码（与FileId参数二选一，同时传入参数时优先使用Image参数）
        :type Image: str
        :param FileId: 印章文件图片ID（与Image参数二选一，同时传入参数时优先使用Image参数）
        :type FileId: str
        :param UserId: 需要创建印章的用户ID
        :type UserId: str
        :param IsDefault: 是否是默认印章 true：是，false：否
        :type IsDefault: bool
        """
        self.Caller = None
        self.SealType = None
        self.SealName = None
        self.SourceIp = None
        self.Image = None
        self.FileId = None
        self.UserId = None
        self.IsDefault = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.SealType = params.get("SealType")
        self.SealName = params.get("SealName")
        self.SourceIp = params.get("SourceIp")
        self.Image = params.get("Image")
        self.FileId = params.get("FileId")
        self.UserId = params.get("UserId")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealResponse(AbstractModel):
    """CreateSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param SealId: 电子印章Id
        :type SealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealId = params.get("SealId")
        self.RequestId = params.get("RequestId")


class CreateServerFlowSignRequest(AbstractModel):
    """CreateServerFlowSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 流程ID
        :type FlowId: str
        :param SignComponents: 签署区域信息
        :type SignComponents: list of Component
        :param SourceIp: 客户端IP
        :type SourceIp: str
        """
        self.Caller = None
        self.FlowId = None
        self.SignComponents = None
        self.SourceIp = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.SourceIp = params.get("SourceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerFlowSignResponse(AbstractModel):
    """CreateServerFlowSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param SignStatus: 任务状态：
0：失败
1：成功
        :type SignStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignStatus = params.get("SignStatus")
        self.RequestId = params.get("RequestId")


class CreateSignUrlRequest(AbstractModel):
    """CreateSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param UserId: 签署人ID
        :type UserId: str
        :param Deadline: 文件签署截止时间戳
        :type Deadline: int
        :param CatalogId: 目录ID。当 SignUrlType 为 CATALOG 时必填
        :type CatalogId: str
        :param FlowId: 流程ID。当 SignUrlType 为 FLOW 时必填
        :type FlowId: str
        :param SignUrlType: 签署链接类型：
1. FLOW - 单流程签署 (默认) 
2. CATALOG - 目录签署
        :type SignUrlType: str
        :param SignId: 发送流程或目录时生成的签署任务ID
        :type SignId: str
        """
        self.Caller = None
        self.UserId = None
        self.Deadline = None
        self.CatalogId = None
        self.FlowId = None
        self.SignUrlType = None
        self.SignId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.UserId = params.get("UserId")
        self.Deadline = params.get("Deadline")
        self.CatalogId = params.get("CatalogId")
        self.FlowId = params.get("FlowId")
        self.SignUrlType = params.get("SignUrlType")
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignUrlResponse(AbstractModel):
    """CreateSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param SignUrl: 合同签署链接
        :type SignUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignUrl = params.get("SignUrl")
        self.RequestId = params.get("RequestId")


class CreateSubOrganizationAndSealRequest(AbstractModel):
    """CreateSubOrganizationAndSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Name: 机构名称全称
        :type Name: str
        :param IdCardType: 机构证件号码类型可选值：
1. USCC - 统一社会信用代码
2. BIZREGISTNO - 营业执照注册号
        :type IdCardType: str
        :param IdCardNumber: 机构证件号码
        :type IdCardNumber: str
        :param OrganizationType: 机构类型可选值：
1. ENTERPRISE - 企业
2. INDIVIDUALBIZ - 个体工商户
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :type OrganizationType: str
        :param LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param LegalIdCardType: 机构法人/经营者证件类型可选值：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type LegalIdCardType: str
        :param LegalIdCardNumber: 机构法人/经营者证件号码；
OrganizationType 为 ENTERPRISE时，INDIVIDUALBIZ 时必填，其他情况选填
        :type LegalIdCardNumber: str
        :param VerifyClientIp: 实名认证的客户端IP/请求生成企业印章的客户端Ip
        :type VerifyClientIp: str
        :param Email: 机构电子邮箱
        :type Email: str
        :param IdCardFileType: 机构证件文件类型可选值：
1. USCCFILE - 统一社会信用代码证书
2. LICENSEFILE - 营业执照
        :type IdCardFileType: str
        :param BizLicenseFile: 机构证件照片文件，base64编码，支持jpg、jpeg、png格式
        :type BizLicenseFile: str
        :param BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param ContactName: 组织联系人姓名
        :type ContactName: str
        :param VerifyServerIp: 实名认证的服务器IP
        :type VerifyServerIp: str
        :param ContactAddress: 企业联系地址
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        :param SealName: 电子印章名称
        :type SealName: str
        :param SealType: 印章类型：默认: CONTRACT
1. OFFICIAL-公章
2. SPECIAL_FINANCIAL-财务专用章
3. CONTRACT-合同专用章
4. LEGAL_REPRESENTATIVE-法定代表人章
5. SPECIAL_NATIONWIDE_INVOICE-发票专用章
6. OTHER-其他
        :type SealType: str
        :param SealHorizontalText: 企业印章横向文字，最多可填8个汉字（可为空，默认为"电子签名专用章"）
        :type SealHorizontalText: str
        :param OpenId: 机构在第三方的唯一标识，32位以内标识符
        :type OpenId: str
        :param UseOpenId: 是否使用OpenId作为数据主键，如果为true，请确保OpenId在当前应用号唯一
        :type UseOpenId: bool
        """
        self.Caller = None
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.OrganizationType = None
        self.LegalName = None
        self.LegalIdCardType = None
        self.LegalIdCardNumber = None
        self.VerifyClientIp = None
        self.Email = None
        self.IdCardFileType = None
        self.BizLicenseFile = None
        self.BizLicenseFileName = None
        self.LegalMobile = None
        self.ContactName = None
        self.VerifyServerIp = None
        self.ContactAddress = None
        self.SealName = None
        self.SealType = None
        self.SealHorizontalText = None
        self.OpenId = None
        self.UseOpenId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.OrganizationType = params.get("OrganizationType")
        self.LegalName = params.get("LegalName")
        self.LegalIdCardType = params.get("LegalIdCardType")
        self.LegalIdCardNumber = params.get("LegalIdCardNumber")
        self.VerifyClientIp = params.get("VerifyClientIp")
        self.Email = params.get("Email")
        self.IdCardFileType = params.get("IdCardFileType")
        self.BizLicenseFile = params.get("BizLicenseFile")
        self.BizLicenseFileName = params.get("BizLicenseFileName")
        self.LegalMobile = params.get("LegalMobile")
        self.ContactName = params.get("ContactName")
        self.VerifyServerIp = params.get("VerifyServerIp")
        if params.get("ContactAddress") is not None:
            self.ContactAddress = Address()
            self.ContactAddress._deserialize(params.get("ContactAddress"))
        self.SealName = params.get("SealName")
        self.SealType = params.get("SealType")
        self.SealHorizontalText = params.get("SealHorizontalText")
        self.OpenId = params.get("OpenId")
        self.UseOpenId = params.get("UseOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubOrganizationAndSealResponse(AbstractModel):
    """CreateSubOrganizationAndSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubOrganizationId: 子机构在电子文件签署平台唯一标识
        :type SubOrganizationId: str
        :param SealId: 电子印章ID
        :type SealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubOrganizationId = None
        self.SealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.SealId = params.get("SealId")
        self.RequestId = params.get("RequestId")


class CreateSubOrganizationRequest(AbstractModel):
    """CreateSubOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param IdCardType: 机构证件号码类型可选值：
1. USCC - 统一社会信用代码
2. BIZREGISTNO - 营业执照注册号
        :type IdCardType: str
        :param IdCardNumber: 机构证件号码
        :type IdCardNumber: str
        :param OrganizationType: 机构类型可选值：
1. ENTERPRISE - 企业
2. INDIVIDUALBIZ - 个体工商户
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :type OrganizationType: str
        :param LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param LegalIdCardType: 机构法人/经营者证件类型可选值：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type LegalIdCardType: str
        :param LegalIdCardNumber: 机构法人/经营者证件号码；
OrganizationType 为 ENTERPRISE时，INDIVIDUALBIZ 时必填，其他情况选填
        :type LegalIdCardNumber: str
        :param Name: 机构名称全称
        :type Name: str
        :param OpenId: 机构在第三方的唯一标识，32位以内标识符
        :type OpenId: str
        :param UseOpenId: 是否使用OpenId作为数据主键，如果为true，请确保OpenId在当前应用号唯一
        :type UseOpenId: bool
        :param IdCardFileType: 机构证件文件类型可选值：
1. USCCFILE - 统一社会信用代码证书
2. LICENSEFILE - 营业执照
        :type IdCardFileType: str
        :param BizLicenseFile: 机构证件照片文件，base64编码，支持jpg、jpeg、png格式
        :type BizLicenseFile: str
        :param BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param ContactName: 组织联系人姓名
        :type ContactName: str
        :param VerifyClientIp: 实名认证的客户端IP
        :type VerifyClientIp: str
        :param VerifyServerIp: 实名认证的服务器IP
        :type VerifyServerIp: str
        :param ContactAddress: 企业联系地址
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        :param Email: 机构电子邮箱
        :type Email: str
        """
        self.Caller = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.OrganizationType = None
        self.LegalName = None
        self.LegalIdCardType = None
        self.LegalIdCardNumber = None
        self.Name = None
        self.OpenId = None
        self.UseOpenId = None
        self.IdCardFileType = None
        self.BizLicenseFile = None
        self.BizLicenseFileName = None
        self.LegalMobile = None
        self.ContactName = None
        self.VerifyClientIp = None
        self.VerifyServerIp = None
        self.ContactAddress = None
        self.Email = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.OrganizationType = params.get("OrganizationType")
        self.LegalName = params.get("LegalName")
        self.LegalIdCardType = params.get("LegalIdCardType")
        self.LegalIdCardNumber = params.get("LegalIdCardNumber")
        self.Name = params.get("Name")
        self.OpenId = params.get("OpenId")
        self.UseOpenId = params.get("UseOpenId")
        self.IdCardFileType = params.get("IdCardFileType")
        self.BizLicenseFile = params.get("BizLicenseFile")
        self.BizLicenseFileName = params.get("BizLicenseFileName")
        self.LegalMobile = params.get("LegalMobile")
        self.ContactName = params.get("ContactName")
        self.VerifyClientIp = params.get("VerifyClientIp")
        self.VerifyServerIp = params.get("VerifyServerIp")
        if params.get("ContactAddress") is not None:
            self.ContactAddress = Address()
            self.ContactAddress._deserialize(params.get("ContactAddress"))
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubOrganizationResponse(AbstractModel):
    """CreateSubOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubOrganizationId: 子机构ID
        :type SubOrganizationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubOrganizationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.RequestId = params.get("RequestId")


class CreateUserAndSealRequest(AbstractModel):
    """CreateUserAndSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param OpenId: 第三方平台唯一标识，要求应用内OpenId唯一
        :type OpenId: str
        :param Name: 用户姓名
        :type Name: str
        :param IdCardType: 用户证件类型：
1. ID_CARD - 居民身份证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type IdCardType: str
        :param IdCardNumber: 用户证件号
        :type IdCardNumber: str
        :param SourceIp: 请求生成个人印章的客户端IP
        :type SourceIp: str
        :param Mobile: 用户手机号码，不要求唯一
        :type Mobile: str
        :param Email: 用户邮箱，不要求唯一
        :type Email: str
        :param SealName: 默认印章名称
        :type SealName: str
        :param UseOpenId: 是否以OpenId作为UserId (为true时将直接以OpenId生成腾讯电子签平台的UserId)
        :type UseOpenId: bool
        """
        self.Caller = None
        self.OpenId = None
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.SourceIp = None
        self.Mobile = None
        self.Email = None
        self.SealName = None
        self.UseOpenId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.OpenId = params.get("OpenId")
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.SourceIp = params.get("SourceIp")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SealName = params.get("SealName")
        self.UseOpenId = params.get("UseOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserAndSealResponse(AbstractModel):
    """CreateUserAndSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户唯一标识，按应用号隔离
        :type UserId: str
        :param SealId: 默认印章ID
        :type SealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.SealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.SealId = params.get("SealId")
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param OpenId: 第三方平台唯一标识；要求应用内OpenId唯一; len<=32
        :type OpenId: str
        :param Name: 用户姓名
        :type Name: str
        :param IdCardType: 用户证件类型：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type IdCardType: str
        :param IdCardNumber: 用户证件号
        :type IdCardNumber: str
        :param UseOpenId: 是否以OpenId作为UserId (为true时将直接以OpenId生成腾讯电子签平台的UserId)
        :type UseOpenId: bool
        :param Email: 用户邮箱，不要求唯一
        :type Email: str
        :param Mobile: 用户手机号码，不要求唯一
        :type Mobile: str
        """
        self.Caller = None
        self.OpenId = None
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.UseOpenId = None
        self.Email = None
        self.Mobile = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.OpenId = params.get("OpenId")
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.UseOpenId = params.get("UseOpenId")
        self.Email = params.get("Email")
        self.Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID，按应用号隔离
        :type UserId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")


class CustomFileIdMap(AbstractModel):
    """<自定义Id,文件id>映射对象

    """

    def __init__(self):
        r"""
        :param CustomId: 用户自定义ID
        :type CustomId: str
        :param FileId: 文件id
        :type FileId: str
        """
        self.CustomId = None
        self.FileId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomFlowIdMap(AbstractModel):
    """自定义流程id映射关系

    """

    def __init__(self):
        r"""
        :param CustomId: 自定义id
        :type CustomId: str
        :param FlowId: 流程id
        :type FlowId: str
        """
        self.CustomId = None
        self.FlowId = None


    def _deserialize(self, params):
        self.CustomId = params.get("CustomId")
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSealRequest(AbstractModel):
    """DeleteSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param SealId: 印章ID
        :type SealId: str
        :param SourceIp: 请求删除印章的客户端IP
        :type SourceIp: str
        :param UserId: 用户唯一标识，默认为空时删除企业印章，如非空则删除个人印章
        :type UserId: str
        """
        self.Caller = None
        self.SealId = None
        self.SourceIp = None
        self.UserId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.SealId = params.get("SealId")
        self.SourceIp = params.get("SourceIp")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSealResponse(AbstractModel):
    """DeleteSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCatalogApproversRequest(AbstractModel):
    """DescribeCatalogApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param CatalogId: 目录ID
        :type CatalogId: str
        :param UserId: 查询指定用户是否为参与者,为空表示查询所有参与者
        :type UserId: str
        """
        self.Caller = None
        self.CatalogId = None
        self.UserId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.CatalogId = params.get("CatalogId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCatalogApproversResponse(AbstractModel):
    """DescribeCatalogApprovers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Approvers: 参与者列表
        :type Approvers: list of CatalogApprovers
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Approvers = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = CatalogApprovers()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCatalogSignComponentsRequest(AbstractModel):
    """DescribeCatalogSignComponents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param CatalogId: 目录ID
        :type CatalogId: str
        """
        self.Caller = None
        self.CatalogId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.CatalogId = params.get("CatalogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCatalogSignComponentsResponse(AbstractModel):
    """DescribeCatalogSignComponents返回参数结构体

    """

    def __init__(self):
        r"""
        :param SignComponents: 签署区列表
        :type SignComponents: list of CatalogComponents
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignComponents = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = CatalogComponents()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomFlowIdsByFlowIdRequest(AbstractModel):
    """DescribeCustomFlowIdsByFlowId请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowIds: 流程 id 列表，最多同时查询 10 个流程 id
        :type FlowIds: list of str
        """
        self.Caller = None
        self.FlowIds = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowIds = params.get("FlowIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomFlowIdsByFlowIdResponse(AbstractModel):
    """DescribeCustomFlowIdsByFlowId返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomIdList: 自定义流程 id 映射列表
        :type CustomIdList: list of CustomFlowIdMap
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomIdList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomIdList") is not None:
            self.CustomIdList = []
            for item in params.get("CustomIdList"):
                obj = CustomFlowIdMap()
                obj._deserialize(item)
                self.CustomIdList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomFlowIdsRequest(AbstractModel):
    """DescribeCustomFlowIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param CustomIds: 自定义 id 列表，最多同时查询 10 个自定义 id
        :type CustomIds: list of str
        """
        self.Caller = None
        self.CustomIds = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.CustomIds = params.get("CustomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomFlowIdsResponse(AbstractModel):
    """DescribeCustomFlowIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomIdList: 自定义流程 id 映射列表
        :type CustomIdList: list of CustomFlowIdMap
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomIdList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomIdList") is not None:
            self.CustomIdList = []
            for item in params.get("CustomIdList"):
                obj = CustomFlowIdMap()
                obj._deserialize(item)
                self.CustomIdList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFaceIdPhotosRequest(AbstractModel):
    """DescribeFaceIdPhotos请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param WbAppId: 慧眼业务ID
        :type WbAppId: str
        :param OrderNumbers: 订单号(orderNo); 限制在3个或以内
        :type OrderNumbers: list of str
        """
        self.Caller = None
        self.WbAppId = None
        self.OrderNumbers = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.WbAppId = params.get("WbAppId")
        self.OrderNumbers = params.get("OrderNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFaceIdPhotosResponse(AbstractModel):
    """DescribeFaceIdPhotos返回参数结构体

    """

    def __init__(self):
        r"""
        :param Photos: 照片信息列表
        :type Photos: list of FaceIdPhoto
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Photos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Photos") is not None:
            self.Photos = []
            for item in params.get("Photos"):
                obj = FaceIdPhoto()
                obj._deserialize(item)
                self.Photos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFaceIdResultsRequest(AbstractModel):
    """DescribeFaceIdResults请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param WbAppId: 慧眼业务ID
        :type WbAppId: str
        :param OrderNumbers: 订单号(orderNo); 限制在3个或以内
        :type OrderNumbers: list of str
        :param FileType: 1:视频+照片,2:照片,3:视频,0（或其他数字）:无; 可选
        :type FileType: int
        """
        self.Caller = None
        self.WbAppId = None
        self.OrderNumbers = None
        self.FileType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.WbAppId = params.get("WbAppId")
        self.OrderNumbers = params.get("OrderNumbers")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFaceIdResultsResponse(AbstractModel):
    """DescribeFaceIdResults返回参数结构体

    """

    def __init__(self):
        r"""
        :param Results: 核身结果列表
        :type Results: list of FaceIdResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = FaceIdResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFileIdsByCustomIdsRequest(AbstractModel):
    """DescribeFileIdsByCustomIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息, OrganizationId必填
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param CustomIds: 用户自定义ID
        :type CustomIds: list of str
        """
        self.Caller = None
        self.CustomIds = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.CustomIds = params.get("CustomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileIdsByCustomIdsResponse(AbstractModel):
    """DescribeFileIdsByCustomIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param CustomIdList: <自定义Id,文件id>数组
        :type CustomIdList: list of CustomFileIdMap
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomIdList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomIdList") is not None:
            self.CustomIdList = []
            for item in params.get("CustomIdList"):
                obj = CustomFileIdMap()
                obj._deserialize(item)
                self.CustomIdList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFileUrlsRequest(AbstractModel):
    """DescribeFileUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param BusinessIds: 业务编号数组，如模板编号、文档编号、印章编号、流程编号、目录编号
        :type BusinessIds: list of str
        :param BusinessType: 业务类型：
1. TEMPLATE - 模板
2. SEAL - 印章
3. FLOW - 流程
4.CATALOG - 目录
        :type BusinessType: str
        :param FileName: 下载后的文件命名，只有FileType为“ZIP”时生效
        :type FileName: str
        :param ResourceOffset: 单个业务ID多个资源情况下，指定资源起始偏移量
        :type ResourceOffset: int
        :param ResourceLimit: 单个业务ID多个资源情况下，指定资源数量
        :type ResourceLimit: int
        :param FileType: 文件类型，支持"JPG", "PDF","ZIP"等，默认为上传的文件类型
        :type FileType: str
        """
        self.Caller = None
        self.BusinessIds = None
        self.BusinessType = None
        self.FileName = None
        self.ResourceOffset = None
        self.ResourceLimit = None
        self.FileType = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.BusinessIds = params.get("BusinessIds")
        self.BusinessType = params.get("BusinessType")
        self.FileName = params.get("FileName")
        self.ResourceOffset = params.get("ResourceOffset")
        self.ResourceLimit = params.get("ResourceLimit")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileUrlsResponse(AbstractModel):
    """DescribeFileUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrls: 文件下载URL数组
        :type FileUrls: list of FileUrl
        :param TotalCount: URL数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileUrls = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileUrls") is not None:
            self.FileUrls = []
            for item in params.get("FileUrls"):
                obj = FileUrl()
                obj._deserialize(item)
                self.FileUrls.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFlowApproversRequest(AbstractModel):
    """DescribeFlowApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 需要查询的流程ID
        :type FlowId: str
        :param UserId: 需要查询的用户ID，为空则默认查询所有用户信息
        :type UserId: str
        :param SignId: 需要查询的签署ID，为空则不按签署ID过滤
        :type SignId: str
        """
        self.Caller = None
        self.FlowId = None
        self.UserId = None
        self.SignId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        self.UserId = params.get("UserId")
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowApproversResponse(AbstractModel):
    """DescribeFlowApprovers返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程编号
        :type FlowId: str
        :param Approvers: 流程参与者信息
        :type Approvers: list of FlowApproverInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.Approvers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowFilesRequest(AbstractModel):
    """DescribeFlowFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 需要查询的流程ID
        :type FlowId: str
        """
        self.Caller = None
        self.FlowId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowFilesResponse(AbstractModel):
    """DescribeFlowFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程编号
        :type FlowId: str
        :param FlowFileInfos: 流程文件列表
        :type FlowFileInfos: list of FlowFileInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.FlowFileInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("FlowFileInfos") is not None:
            self.FlowFileInfos = []
            for item in params.get("FlowFileInfos"):
                obj = FlowFileInfo()
                obj._deserialize(item)
                self.FlowFileInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 需要查询的流程ID
        :type FlowId: str
        """
        self.Caller = None
        self.FlowId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Creator: 流程创建者信息
        :type Creator: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 流程编号
        :type FlowId: str
        :param FlowName: 流程名称
        :type FlowName: str
        :param FlowDescription: 流程描述
        :type FlowDescription: str
        :param FlowType: 流程的类型: ”劳务合同“,”租赁合同“,”销售合同“,”其他“
        :type FlowType: str
        :param FlowStatus: 流程状态：
0-创建；
1-签署中；
2-拒签；
3-撤回；
4-签完存档完成；
5-已过期；
6-已销毁
7-签署完成未归档
        :type FlowStatus: int
        :param CreatedOn: 流程创建时间
        :type CreatedOn: int
        :param UpdatedOn: 流程完成时间
        :type UpdatedOn: int
        :param Deadline: 流程截止日期
        :type Deadline: int
        :param CallbackUrl: 回调地址
        :type CallbackUrl: str
        :param FlowMessage: 流程中止原因
        :type FlowMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Creator = None
        self.FlowId = None
        self.FlowName = None
        self.FlowDescription = None
        self.FlowType = None
        self.FlowStatus = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.Deadline = None
        self.CallbackUrl = None
        self.FlowMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Creator") is not None:
            self.Creator = Caller()
            self.Creator._deserialize(params.get("Creator"))
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        self.FlowDescription = params.get("FlowDescription")
        self.FlowType = params.get("FlowType")
        self.FlowStatus = params.get("FlowStatus")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.Deadline = params.get("Deadline")
        self.CallbackUrl = params.get("CallbackUrl")
        self.FlowMessage = params.get("FlowMessage")
        self.RequestId = params.get("RequestId")


class DescribeSealsRequest(AbstractModel):
    """DescribeSeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param SealIds: 印章ID列表
        :type SealIds: list of str
        :param UserId: 用户唯一标识
        :type UserId: str
        """
        self.Caller = None
        self.SealIds = None
        self.UserId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.SealIds = params.get("SealIds")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSealsResponse(AbstractModel):
    """DescribeSeals返回参数结构体

    """

    def __init__(self):
        r"""
        :param Seals: 印章信息
        :type Seals: list of Seal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Seals = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Seals") is not None:
            self.Seals = []
            for item in params.get("Seals"):
                obj = Seal()
                obj._deserialize(item)
                self.Seals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubOrganizationsRequest(AbstractModel):
    """DescribeSubOrganizations请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param SubOrganizationIds: 子机构ID数组
        :type SubOrganizationIds: list of str
        """
        self.Caller = None
        self.SubOrganizationIds = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.SubOrganizationIds = params.get("SubOrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubOrganizationsResponse(AbstractModel):
    """DescribeSubOrganizations返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubOrganizationInfos: 子机构信息列表
        :type SubOrganizationInfos: list of SubOrganizationDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubOrganizationInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubOrganizationInfos") is not None:
            self.SubOrganizationInfos = []
            for item in params.get("SubOrganizationInfos"):
                obj = SubOrganizationDetail()
                obj._deserialize(item)
                self.SubOrganizationInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    """DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param UserIds: UserId列表，最多支持100个UserId
        :type UserIds: list of str
        """
        self.Caller = None
        self.UserIds = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersResponse(AbstractModel):
    """DescribeUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Users: 用户信息查询结果
        :type Users: list of UserDescribe
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = UserDescribe()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyFlowFileRequest(AbstractModel):
    """DestroyFlowFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 流程ID
        :type FlowId: str
        """
        self.Caller = None
        self.FlowId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyFlowFileResponse(AbstractModel):
    """DestroyFlowFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FaceIdPhoto(AbstractModel):
    """此结构体 (FaceIdPhoto) 用于描述慧眼人脸核身照片信息。

    """

    def __init__(self):
        r"""
        :param Result: 核身结果：
0 - 通过；
1 - 未通过
        :type Result: int
        :param Description: 核身失败描述
        :type Description: str
        :param Photo: 照片数据 (base64编码, 一般为JPG或PNG)
        :type Photo: str
        :param OrderNumber: 订单号 (orderNo)
        :type OrderNumber: str
        """
        self.Result = None
        self.Description = None
        self.Photo = None
        self.OrderNumber = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Photo = params.get("Photo")
        self.OrderNumber = params.get("OrderNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceIdResult(AbstractModel):
    """此结构体 (FaceIdResult) 用于描述慧眼人脸核身结果。

    """

    def __init__(self):
        r"""
        :param Result: 核身结果：
0 - 通过；
1 - 未通过
        :type Result: int
        :param Description: 核身失败描述
        :type Description: str
        :param OrderNumber: 订单号 (orderNo)
        :type OrderNumber: str
        :param Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param IdCardType: 身份证件类型： 
ID_CARD - 居民身份证
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardType: str
        :param IdCardNumber: 身份证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardNumber: str
        :param LiveRate: 活体检测得分 (百分制)
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveRate: int
        :param Similarity: 人脸检测得分 (百分制)
注意：此字段可能返回 null，表示取不到有效值。
        :type Similarity: float
        :param OccurredTime: 刷脸时间 (UNIX时间戳)
注意：此字段可能返回 null，表示取不到有效值。
        :type OccurredTime: int
        :param Photo: 照片数据 (base64编码, 一般为JPG或PNG)
注意：此字段可能返回 null，表示取不到有效值。
        :type Photo: str
        :param Video: 视频数据 (base64编码, 一般为MP4)
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: str
        """
        self.Result = None
        self.Description = None
        self.OrderNumber = None
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.LiveRate = None
        self.Similarity = None
        self.OccurredTime = None
        self.Photo = None
        self.Video = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.OrderNumber = params.get("OrderNumber")
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.LiveRate = params.get("LiveRate")
        self.Similarity = params.get("Similarity")
        self.OccurredTime = params.get("OccurredTime")
        self.Photo = params.get("Photo")
        self.Video = params.get("Video")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileUrl(AbstractModel):
    """此结构体 (FileUrl) 用于描述下载文件的URL信息。

    """

    def __init__(self):
        r"""
        :param Url: 下载文件的URL
        :type Url: str
        :param Option: 下载文件的附加信息
        :type Option: str
        :param Index: 下载文件所属的资源序号
        :type Index: int
        :param FlowId: 目录业务下，文件对应的流程
        :type FlowId: str
        """
        self.Url = None
        self.Option = None
        self.Index = None
        self.FlowId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Option = params.get("Option")
        self.Index = params.get("Index")
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverInfo(AbstractModel):
    """此结构体 (FlowApproverInfo) 用于描述流程参与者信息。

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        :param VerifyChannel: 认证方式：
WEIXINAPP - 微信小程序；
FACEID - 慧眼 (默认)；
VERIFYCODE - 验证码；
THIRD - 第三方 (暂不支持)
        :type VerifyChannel: list of str
        :param ApproveStatus: 签署状态：
0 - 待签署；
1- 已签署；
2 - 拒绝；
3 - 过期未处理；
4 - 流程已撤回,
12-审核中,
13-审核驳回
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveStatus: int
        :param ApproveMessage: 拒签/签署/审核驳回原因
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMessage: str
        :param ApproveTime: 签约时间的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveTime: int
        :param SubOrganizationId: 签署企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubOrganizationId: str
        :param JumpUrl: 签署完成后跳转的URL
注意：此字段可能返回 null，表示取不到有效值。
        :type JumpUrl: str
        :param ComponentSeals: 用户签署区ID到印章ID的映射集合
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentSeals: list of ComponentSeal
        :param IsFullText: 签署前置条件：是否强制用户全文阅读，即阅读到待签署文档的最后一页。默认FALSE
        :type IsFullText: bool
        :param PreReadTime: 签署前置条件：强制阅读时长，页面停留时长不足则不允许签署。默认不限制
        :type PreReadTime: int
        :param Mobile: 签署人手机号，脱敏显示
        :type Mobile: str
        :param Deadline: 签署链接截止时间，默认签署流程发起后7天失效
        :type Deadline: int
        :param IsLastApprover: 是否为最后一个签署人, 若为最后一人，则其签署完成后自动归档
        :type IsLastApprover: bool
        :param SmsTemplate: 短信模板
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsTemplate: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        :param IdCardNumber: 身份证号，脱敏显示
        :type IdCardNumber: str
        :param Name: 用户姓名
        :type Name: str
        :param CanOffLine: 是否支持线下核身
        :type CanOffLine: bool
        :param IdCardType: 证件号码类型：ID_CARD - 身份证，PASSPORT - 护照，MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证; 暂不支持用于电子签自有平台实名认证，MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证; 暂不支持用于电子签自有平台实名认证，HOUSEHOLD_REGISTER - 户口本; 暂不支持用于电子签自有平台实名认证，TEMP_ID_CARD - 临时居民身份证; 暂不支持用于电子签自有平台实名认证
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardType: str
        :param CallbackUrl: 签署回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        :param SignId: 签署任务ID，标识每一次的流程发送
注意：此字段可能返回 null，表示取不到有效值。
        :type SignId: str
        """
        self.UserId = None
        self.VerifyChannel = None
        self.ApproveStatus = None
        self.ApproveMessage = None
        self.ApproveTime = None
        self.SubOrganizationId = None
        self.JumpUrl = None
        self.ComponentSeals = None
        self.IsFullText = None
        self.PreReadTime = None
        self.Mobile = None
        self.Deadline = None
        self.IsLastApprover = None
        self.SmsTemplate = None
        self.IdCardNumber = None
        self.Name = None
        self.CanOffLine = None
        self.IdCardType = None
        self.CallbackUrl = None
        self.SignId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.VerifyChannel = params.get("VerifyChannel")
        self.ApproveStatus = params.get("ApproveStatus")
        self.ApproveMessage = params.get("ApproveMessage")
        self.ApproveTime = params.get("ApproveTime")
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.JumpUrl = params.get("JumpUrl")
        if params.get("ComponentSeals") is not None:
            self.ComponentSeals = []
            for item in params.get("ComponentSeals"):
                obj = ComponentSeal()
                obj._deserialize(item)
                self.ComponentSeals.append(obj)
        self.IsFullText = params.get("IsFullText")
        self.PreReadTime = params.get("PreReadTime")
        self.Mobile = params.get("Mobile")
        self.Deadline = params.get("Deadline")
        self.IsLastApprover = params.get("IsLastApprover")
        if params.get("SmsTemplate") is not None:
            self.SmsTemplate = SmsTemplate()
            self.SmsTemplate._deserialize(params.get("SmsTemplate"))
        self.IdCardNumber = params.get("IdCardNumber")
        self.Name = params.get("Name")
        self.CanOffLine = params.get("CanOffLine")
        self.IdCardType = params.get("IdCardType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowFileInfo(AbstractModel):
    """此结构体 (FlowFileInfo) 用于描述流程文档信息。

    """

    def __init__(self):
        r"""
        :param FileIndex: 文件序号
        :type FileIndex: int
        :param FileType: 文件类型
        :type FileType: str
        :param FileMd5: 文件的MD5码
        :type FileMd5: str
        :param FileName: 文件名
        :type FileName: str
        :param FileSize: 文件大小，单位为Byte
        :type FileSize: int
        :param CreatedOn: 文件创建时间戳
        :type CreatedOn: int
        :param Url: 文件的下载地址
        :type Url: str
        """
        self.FileIndex = None
        self.FileType = None
        self.FileMd5 = None
        self.FileName = None
        self.FileSize = None
        self.CreatedOn = None
        self.Url = None


    def _deserialize(self, params):
        self.FileIndex = params.get("FileIndex")
        self.FileType = params.get("FileType")
        self.FileMd5 = params.get("FileMd5")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.CreatedOn = params.get("CreatedOn")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowInfo(AbstractModel):
    """此结构体 (FlowInfo) 用于描述流程信息。

    """

    def __init__(self):
        r"""
        :param FlowName: 合同名字
        :type FlowName: str
        :param Deadline: 签署截止时间戳，超过有效签署时间则该签署流程失败
        :type Deadline: int
        :param FlowDescription: 合同描述
        :type FlowDescription: str
        :param FlowType: 合同类型：
1. “劳务”
2. “销售”
3. “租赁”
4. “其他”
        :type FlowType: str
        :param CallbackUrl: 回调地址
        :type CallbackUrl: str
        :param UserData: 用户自定义数据
        :type UserData: str
        """
        self.FlowName = None
        self.Deadline = None
        self.FlowDescription = None
        self.FlowType = None
        self.CallbackUrl = None
        self.UserData = None


    def _deserialize(self, params):
        self.FlowName = params.get("FlowName")
        self.Deadline = params.get("Deadline")
        self.FlowDescription = params.get("FlowDescription")
        self.FlowType = params.get("FlowType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.UserData = params.get("UserData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateOrganizationSealRequest(AbstractModel):
    """GenerateOrganizationSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param SealType: 印章类型：
OFFICIAL-公章
SPECIAL_FINANCIAL-财务专用章
CONTRACT-合同专用章
LEGAL_REPRESENTATIVE-法定代表人章
SPECIAL_NATIONWIDE_INVOICE-发票专用章
OTHER-其他
        :type SealType: str
        :param SourceIp: 请求生成企业印章的客户端Ip
        :type SourceIp: str
        :param SealName: 电子印章名称
        :type SealName: str
        :param SealHorizontalText: 企业印章横向文字，最多可填8个汉字（可不填，默认为"电子签名专用章"）
        :type SealHorizontalText: str
        :param IsDefault: 是否是默认印章 true：是，false：否
        :type IsDefault: bool
        """
        self.Caller = None
        self.SealType = None
        self.SourceIp = None
        self.SealName = None
        self.SealHorizontalText = None
        self.IsDefault = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.SealType = params.get("SealType")
        self.SourceIp = params.get("SourceIp")
        self.SealName = params.get("SealName")
        self.SealHorizontalText = params.get("SealHorizontalText")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateOrganizationSealResponse(AbstractModel):
    """GenerateOrganizationSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param SealId: 电子印章Id
        :type SealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealId = params.get("SealId")
        self.RequestId = params.get("RequestId")


class GenerateUserSealRequest(AbstractModel):
    """GenerateUserSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param UserId: 用户ID
        :type UserId: str
        :param SourceIp: 请求生成个人印章的客户端IP
        :type SourceIp: str
        :param SealName: 电子印章名称
        :type SealName: str
        :param IsDefault: 是否是默认印章 true：是，false：否
        :type IsDefault: bool
        """
        self.Caller = None
        self.UserId = None
        self.SourceIp = None
        self.SealName = None
        self.IsDefault = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.UserId = params.get("UserId")
        self.SourceIp = params.get("SourceIp")
        self.SealName = params.get("SealName")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateUserSealResponse(AbstractModel):
    """GenerateUserSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param SealId: 电子印章Id
        :type SealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealId = params.get("SealId")
        self.RequestId = params.get("RequestId")


class ModifyOrganizationDefaultSealRequest(AbstractModel):
    """ModifyOrganizationDefaultSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param SealId: 重新指定的默认印章ID
        :type SealId: str
        :param SourceIp: 请求重新指定企业默认印章的客户端IP
        :type SourceIp: str
        """
        self.Caller = None
        self.SealId = None
        self.SourceIp = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.SealId = params.get("SealId")
        self.SourceIp = params.get("SourceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrganizationDefaultSealResponse(AbstractModel):
    """ModifyOrganizationDefaultSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySealRequest(AbstractModel):
    """ModifySeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param SourceIp: 请求更新印章的客户端IP
        :type SourceIp: str
        :param SealId: 电子印章ID。若为空，则修改个人/机构的默认印章。
        :type SealId: str
        :param SealName: 电子印章名称
        :type SealName: str
        :param Image: 印章图片，base64编码（与FileId参数二选一，同时传入参数时优先使用Image参数）
        :type Image: str
        :param FileId: 印章图片文件ID（与Image参数二选一，同时传入参数时优先使用Image参数）
        :type FileId: str
        :param UserId: 需要更新印章的用户ID
        :type UserId: str
        """
        self.Caller = None
        self.SourceIp = None
        self.SealId = None
        self.SealName = None
        self.Image = None
        self.FileId = None
        self.UserId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.SourceIp = params.get("SourceIp")
        self.SealId = params.get("SealId")
        self.SealName = params.get("SealName")
        self.Image = params.get("Image")
        self.FileId = params.get("FileId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySealResponse(AbstractModel):
    """ModifySeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubOrganizationInfoRequest(AbstractModel):
    """ModifySubOrganizationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息，该接口 SubOrganizationId 字段与 OpenId 字段二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param OpenId: 机构在第三方的唯一标识，32位定长字符串，与 Caller 中 SubOrgnizationId 二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :type OpenId: str
        :param Name: 机构名称全称，修改后机构状态将变为未实名，需要调用实名接口重新实名。
        :type Name: str
        :param OrganizationType: 机构类型可选值：
1. ENTERPRISE - 企业；
2. INDIVIDUALBIZ - 个体工商户；
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :type OrganizationType: str
        :param BizLicenseFile: 机构证件照片文件，base64编码。支持jpg，jpeg，png格式；如果传值，则重新上传文件后，机构状态将变为未实名，需要调用实名接口重新实名。
        :type BizLicenseFile: str
        :param BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param LegalIdCardType: 机构法人/经营者证件类型，可选值：ID_CARD - 居民身份证。OrganizationType 为 ENTERPRISE、INDIVIDUALBIZ 时，此项必填，其他情况选填。
        :type LegalIdCardType: str
        :param LegalIdCardNumber: 机构法人/经营者证件号码。OrganizationType 为 ENTERPRISE、INDIVIDUALBIZ 时，此项必填，其他情况选填
        :type LegalIdCardNumber: str
        :param LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param ContactName: 组织联系人姓名
        :type ContactName: str
        :param ContactAddress: 企业联系地址
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        :param Email: 机构电子邮箱
        :type Email: str
        """
        self.Caller = None
        self.OpenId = None
        self.Name = None
        self.OrganizationType = None
        self.BizLicenseFile = None
        self.BizLicenseFileName = None
        self.LegalName = None
        self.LegalIdCardType = None
        self.LegalIdCardNumber = None
        self.LegalMobile = None
        self.ContactName = None
        self.ContactAddress = None
        self.Email = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.OpenId = params.get("OpenId")
        self.Name = params.get("Name")
        self.OrganizationType = params.get("OrganizationType")
        self.BizLicenseFile = params.get("BizLicenseFile")
        self.BizLicenseFileName = params.get("BizLicenseFileName")
        self.LegalName = params.get("LegalName")
        self.LegalIdCardType = params.get("LegalIdCardType")
        self.LegalIdCardNumber = params.get("LegalIdCardNumber")
        self.LegalMobile = params.get("LegalMobile")
        self.ContactName = params.get("ContactName")
        if params.get("ContactAddress") is not None:
            self.ContactAddress = Address()
            self.ContactAddress._deserialize(params.get("ContactAddress"))
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubOrganizationInfoResponse(AbstractModel):
    """ModifySubOrganizationInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubOrganizationId: 子机构ID
        :type SubOrganizationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubOrganizationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.RequestId = params.get("RequestId")


class ModifyUserDefaultSealRequest(AbstractModel):
    """ModifyUserDefaultSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param UserId: 用户唯一标识，需要重新指定默认印章的用户ID
        :type UserId: str
        :param SealId: 重新指定的默认印章ID
        :type SealId: str
        :param SourceIp: 请求重新指定个人默认印章的客户端IP
        :type SourceIp: str
        """
        self.Caller = None
        self.UserId = None
        self.SealId = None
        self.SourceIp = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.UserId = params.get("UserId")
        self.SealId = params.get("SealId")
        self.SourceIp = params.get("SourceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserDefaultSealResponse(AbstractModel):
    """ModifyUserDefaultSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param OpenId: 第三方平台用户唯一标识; OpenId 和 UserId 二选一填写, 两个都不为空则优先使用UserId
        :type OpenId: str
        :param UserId: 腾讯电子签平台用户唯一标识; OpenId 和 UserId 二选一填写, 两个都不为空则优先使用UserId
        :type UserId: str
        :param Mobile: 用户手机号码，不要求唯一
        :type Mobile: str
        :param Email: 用户邮箱，不要求唯一
        :type Email: str
        :param Name: 用户姓名
        :type Name: str
        """
        self.Caller = None
        self.OpenId = None
        self.UserId = None
        self.Mobile = None
        self.Email = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.OpenId = params.get("OpenId")
        self.UserId = params.get("UserId")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    """ModifyUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 腾讯电子签平台用户唯一标识
        :type UserId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")


class RejectFlowRequest(AbstractModel):
    """RejectFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 流程编号
        :type FlowId: str
        :param VerifyResult: 意愿确认票据。
1. VerifyChannel 为 WEIXINAPP，使用响应的VerifyResult；
2. VerifyChannel 为 FACEID时，使用OrderNo；
3. VerifyChannel 为 VERIFYCODE，使用短信验证码
4. VerifyChannel 为 NONE，传空值
（注：普通情况下，VerifyResult不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyResult: str
        :param VerifyChannel: 意愿确认渠道：
1. WEIXINAPP - 微信小程序
2. FACEID - 慧眼 (默认) 
3. VERIFYCODE - 验证码
4. THIRD - 第三方 (暂不支持)
5. NONE - 无需电子签系统验证
（注：普通情况下，VerifyChannel不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyChannel: str
        :param SourceIp: 客户端来源IP
        :type SourceIp: str
        :param RejectMessage: 拒签原因
        :type RejectMessage: str
        :param SignId: 签署参与者编号
        :type SignId: str
        """
        self.Caller = None
        self.FlowId = None
        self.VerifyResult = None
        self.VerifyChannel = None
        self.SourceIp = None
        self.RejectMessage = None
        self.SignId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        self.VerifyResult = params.get("VerifyResult")
        self.VerifyChannel = params.get("VerifyChannel")
        self.SourceIp = params.get("SourceIp")
        self.RejectMessage = params.get("RejectMessage")
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectFlowResponse(AbstractModel):
    """RejectFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Seal(AbstractModel):
    """此结构体 (Seal) 用于描述电子印章的信息。

    """

    def __init__(self):
        r"""
        :param SealId: 电子印章ID
        :type SealId: str
        :param SealName: 电子印章名称
        :type SealName: str
        :param SealType: 电子印章类型
        :type SealType: str
        :param SealSource: 电子印章来源：
CREATE - 通过图片上传
GENERATE - 通过文字生成
        :type SealSource: str
        :param Creator: 电子印章创建者
        :type Creator: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param CreatedOn: 电子印章创建时间戳
        :type CreatedOn: int
        :param UserId: 电子印章所有人
        :type UserId: str
        :param FileUrl: 电子印章URL
        :type FileUrl: :class:`tencentcloud.essbasic.v20201222.models.FileUrl`
        :param DefaultSeal: 是否为默认印章，false-非默认，true-默认
        :type DefaultSeal: bool
        """
        self.SealId = None
        self.SealName = None
        self.SealType = None
        self.SealSource = None
        self.Creator = None
        self.CreatedOn = None
        self.UserId = None
        self.FileUrl = None
        self.DefaultSeal = None


    def _deserialize(self, params):
        self.SealId = params.get("SealId")
        self.SealName = params.get("SealName")
        self.SealType = params.get("SealType")
        self.SealSource = params.get("SealSource")
        if params.get("Creator") is not None:
            self.Creator = Caller()
            self.Creator._deserialize(params.get("Creator"))
        self.CreatedOn = params.get("CreatedOn")
        self.UserId = params.get("UserId")
        if params.get("FileUrl") is not None:
            self.FileUrl = FileUrl()
            self.FileUrl._deserialize(params.get("FileUrl"))
        self.DefaultSeal = params.get("DefaultSeal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendFlowRequest(AbstractModel):
    """SendFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 需要推送合同的流程ID
        :type FlowId: str
        :param UserId: 签署人用户ID
        :type UserId: str
        :param SignComponents: 签署控件信息 (支持添加多个控件)
        :type SignComponents: list of Component
        :param Mobile: 签署人手机号 (如果选择短信验证码签署，则此字段必填)
        :type Mobile: str
        :param SubOrganizationId: 签署人对应的子机构ID，个人签署者此字段不填
        :type SubOrganizationId: str
        :param VerifyChannel: 签名后校验方式：
1. WEIXINAPP - 微信小程序；
2. FACEID - 慧眼 (默认) ；
3. VERIFYCODE - 验证码；
4. NONE - 无。此选项为白名单参数，暂不支持公开调用。如需开通权限，请通过客户经理或邮件至e-contract@tencent.com与我们联系；
5. THIRD - 第三方 (暂不支持)
        :type VerifyChannel: list of str
        :param Deadline: 签署链接失效截止时间，默认为7天
        :type Deadline: int
        :param IsLastApprover: 是否为最后一个签署人。若为最后一人，本次签署完成以后自动归档。
        :type IsLastApprover: bool
        :param JumpUrl: 签署完成后，前端跳转的URL
        :type JumpUrl: str
        :param SmsTemplate: 短信模板。默认使用腾讯电子签官方短信模板，如有自定义需求，请通过客户经理或邮件至e-contract@tencent.com与我们联系。
        :type SmsTemplate: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        :param IsFullText: 签署前置条件：是否要全文阅读，默认否
        :type IsFullText: bool
        :param PreReadTime: 签署前置条件：强制用户阅读待签署文件时长，默认不限制
        :type PreReadTime: int
        :param CanOffLine: 当前参与者是否支持线下核身,默认为不支持
        :type CanOffLine: bool
        :param CallbackUrl: 签署任务的回调地址
        :type CallbackUrl: str
        """
        self.Caller = None
        self.FlowId = None
        self.UserId = None
        self.SignComponents = None
        self.Mobile = None
        self.SubOrganizationId = None
        self.VerifyChannel = None
        self.Deadline = None
        self.IsLastApprover = None
        self.JumpUrl = None
        self.SmsTemplate = None
        self.IsFullText = None
        self.PreReadTime = None
        self.CanOffLine = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        self.UserId = params.get("UserId")
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.Mobile = params.get("Mobile")
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.VerifyChannel = params.get("VerifyChannel")
        self.Deadline = params.get("Deadline")
        self.IsLastApprover = params.get("IsLastApprover")
        self.JumpUrl = params.get("JumpUrl")
        if params.get("SmsTemplate") is not None:
            self.SmsTemplate = SmsTemplate()
            self.SmsTemplate._deserialize(params.get("SmsTemplate"))
        self.IsFullText = params.get("IsFullText")
        self.PreReadTime = params.get("PreReadTime")
        self.CanOffLine = params.get("CanOffLine")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendFlowResponse(AbstractModel):
    """SendFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param SignId: 签署任务ID，标识每一次的流程发送
        :type SignId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.RequestId = params.get("RequestId")


class SendFlowUrlRequest(AbstractModel):
    """SendFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 需要推送合同的流程ID
        :type FlowId: str
        :param UserId: 签署人ID
        :type UserId: str
        :param SignComponents: 签署控件信息 (支持添加多个控件)
        :type SignComponents: list of Component
        :param Mobile: 签署人手机号 (如果选择短信验证码签署，则此字段必填)
        :type Mobile: str
        :param SubOrganizationId: 签署人对应的子机构ID，个人签署者此字段不填
        :type SubOrganizationId: str
        :param VerifyChannel: 签名后校验方式：
1. WEIXINAPP - 微信小程序；
2. FACEID - 慧眼 (默认) ；
3. VERIFYCODE - 验证码；
4. NONE - 无。此选项为白名单参数，暂不支持公开调用。如需开通权限，请通过客户经理或邮件至e-contract@tencent.com与我们联系；
5. THIRD - 第三方 (暂不支持)
6. OFFLINE - 线下人工审核
        :type VerifyChannel: list of str
        :param Deadline: 签署链接失效截止时间，默认为7天
        :type Deadline: int
        :param IsLastApprover: 是否为最后一个签署人。若为最后一人，本次签署完成以后自动归档
        :type IsLastApprover: bool
        :param JumpUrl: 签署完成后，前端跳转的url
        :type JumpUrl: str
        :param SmsTemplate: 短信模板
默认使用腾讯电子签官方短信模板，如有自定义需求，请通过客户经理或邮件至e-contract@tencent.com与我们联系。
        :type SmsTemplate: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        :param IsFullText: 签署前置条件：是否要全文阅读，默认否
        :type IsFullText: bool
        :param PreReadTime: 签署前置条件：强制用户阅读待签署文件时长，默认不限制
        :type PreReadTime: int
        :param CanOffLine: 当前参与者是否支持线下核身,默认为不支持
        :type CanOffLine: bool
        :param CallbackUrl: 签署任务的回调地址
        :type CallbackUrl: str
        """
        self.Caller = None
        self.FlowId = None
        self.UserId = None
        self.SignComponents = None
        self.Mobile = None
        self.SubOrganizationId = None
        self.VerifyChannel = None
        self.Deadline = None
        self.IsLastApprover = None
        self.JumpUrl = None
        self.SmsTemplate = None
        self.IsFullText = None
        self.PreReadTime = None
        self.CanOffLine = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        self.UserId = params.get("UserId")
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.Mobile = params.get("Mobile")
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.VerifyChannel = params.get("VerifyChannel")
        self.Deadline = params.get("Deadline")
        self.IsLastApprover = params.get("IsLastApprover")
        self.JumpUrl = params.get("JumpUrl")
        if params.get("SmsTemplate") is not None:
            self.SmsTemplate = SmsTemplate()
            self.SmsTemplate._deserialize(params.get("SmsTemplate"))
        self.IsFullText = params.get("IsFullText")
        self.PreReadTime = params.get("PreReadTime")
        self.CanOffLine = params.get("CanOffLine")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendFlowUrlResponse(AbstractModel):
    """SendFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param SignId: 签署任务ID，标识每一次的流程发送
        :type SignId: str
        :param SignUrl: 签署链接
        :type SignUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignId = None
        self.SignUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignUrl = params.get("SignUrl")
        self.RequestId = params.get("RequestId")


class SendSignInnerVerifyCodeRequest(AbstractModel):
    """SendSignInnerVerifyCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param Mobile: 手机号
        :type Mobile: str
        :param VerifyType: 验证码类型，取值(SIGN)
        :type VerifyType: str
        :param UserId: 用户 id
        :type UserId: str
        :param VerifyTemplateId: 模板 id
        :type VerifyTemplateId: str
        :param VerifySign: 签名
        :type VerifySign: str
        :param FlowId: 流程(目录) id
        :type FlowId: str
        :param CheckThreeElementResult: 三要素检测结果
        :type CheckThreeElementResult: int
        """
        self.Caller = None
        self.Mobile = None
        self.VerifyType = None
        self.UserId = None
        self.VerifyTemplateId = None
        self.VerifySign = None
        self.FlowId = None
        self.CheckThreeElementResult = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.Mobile = params.get("Mobile")
        self.VerifyType = params.get("VerifyType")
        self.UserId = params.get("UserId")
        self.VerifyTemplateId = params.get("VerifyTemplateId")
        self.VerifySign = params.get("VerifySign")
        self.FlowId = params.get("FlowId")
        self.CheckThreeElementResult = params.get("CheckThreeElementResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSignInnerVerifyCodeResponse(AbstractModel):
    """SendSignInnerVerifyCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: true: 验证码正确，false: 验证码错误
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class SignFlowRequest(AbstractModel):
    """SignFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param FlowId: 流程编号
        :type FlowId: str
        :param VerifyResult: 意愿确认票据。
1. VerifyChannel 为 WEIXINAPP，使用响应的VerifyResult；
2. VerifyChannel 为 FACEID时，使用OrderNo；
3. VerifyChannel 为 VERIFYCODE，使用短信验证码
4. VerifyChannel 为 NONE，传空值
（注：普通情况下，VerifyResult不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyResult: str
        :param VerifyChannel: 意愿确认渠道：
1. WEIXINAPP - 微信小程序
2. FACEID - 慧眼 (默认) 
3. VERIFYCODE - 验证码
4. THIRD - 第三方 (暂不支持)
5. NONE - 无需电子签系统验证
（注：普通情况下，VerifyChannel不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyChannel: str
        :param SourceIp: 客户端来源IP
        :type SourceIp: str
        :param SignSeals: 签署内容
        :type SignSeals: list of SignSeal
        :param ApproveMessage: 签署备注
        :type ApproveMessage: str
        :param SignId: 签署参与者编号
        :type SignId: str
        """
        self.Caller = None
        self.FlowId = None
        self.VerifyResult = None
        self.VerifyChannel = None
        self.SourceIp = None
        self.SignSeals = None
        self.ApproveMessage = None
        self.SignId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.FlowId = params.get("FlowId")
        self.VerifyResult = params.get("VerifyResult")
        self.VerifyChannel = params.get("VerifyChannel")
        self.SourceIp = params.get("SourceIp")
        if params.get("SignSeals") is not None:
            self.SignSeals = []
            for item in params.get("SignSeals"):
                obj = SignSeal()
                obj._deserialize(item)
                self.SignSeals.append(obj)
        self.ApproveMessage = params.get("ApproveMessage")
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignFlowResponse(AbstractModel):
    """SignFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 签署任务状态。签署成功 - SUCCESS、提交审核 - REVIEW
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class SignSeal(AbstractModel):
    """此结构体 (SignSeal) 用于描述签名/印章信息。

    """

    def __init__(self):
        r"""
        :param ComponentId: 签署控件ID
        :type ComponentId: str
        :param SignType: 签署印章类型:
SIGN_SIGNATURE - 签名
SIGN_SEAL - 印章
SIGN_DATE - 日期
SIGN_IMAGE - 图片
        :type SignType: str
        :param FileIndex: 合同文件ID
        :type FileIndex: int
        :param SealId: 印章ID，仅当 SignType 为 SIGN_SEAL 时必填
        :type SealId: str
        :param SealContent: 签名内容，仅当 SignType 为SIGN_SIGNATURE或SIGN_IMAGE 时必填，base64编码
        :type SealContent: str
        """
        self.ComponentId = None
        self.SignType = None
        self.FileIndex = None
        self.SealId = None
        self.SealContent = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")
        self.SignType = params.get("SignType")
        self.FileIndex = params.get("FileIndex")
        self.SealId = params.get("SealId")
        self.SealContent = params.get("SealContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsTemplate(AbstractModel):
    """此结构体 (SmsTemplate) 用于描述短信模板。

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID，必须填写已审核通过的模板ID。模板ID可登录短信控制台查看。
        :type TemplateId: str
        :param Sign: 短信签名内容，使用UTF-8编码，必须填写已审核通过的签名，签名信息可登录短信控制台查看。
        :type Sign: str
        """
        self.TemplateId = None
        self.Sign = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Sign = params.get("Sign")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubOrganizationDetail(AbstractModel):
    """此结构体 (SubOrganizationDetail) 用于描述子机构或子企业的详情信息。

    """

    def __init__(self):
        r"""
        :param Id: 组织ID
        :type Id: str
        :param Name: 机构名称全称
        :type Name: str
        :param Email: 机构电子邮箱
        :type Email: str
        :param IdCardType: 机构证件号码类型
        :type IdCardType: str
        :param IdCardNumber: 机构证件号码
        :type IdCardNumber: str
        :param OrganizationType: 机构类型
        :type OrganizationType: str
        :param IdCardFileType: 机构证件文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardFileType: str
        :param BizLicenseFile: 机构证件照片文件，base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type BizLicenseFile: str
        :param BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param LegalIdCardType: 机构法人/经营者证件类型
        :type LegalIdCardType: str
        :param LegalIdCardNumber: 机构法人/经营者证件号码
        :type LegalIdCardNumber: str
        :param LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param ContactName: 组织联系人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactName: str
        :param VerifyStatus: 机构实名状态
        :type VerifyStatus: str
        :param VerifiedOn: 机构通过实名时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifiedOn: int
        :param CreatedOn: 机构创建时间
        :type CreatedOn: int
        :param UpdatedOn: 机构更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: int
        :param VerifyClientIp: 实名认证的客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyClientIp: str
        :param VerifyServerIp: 实名认证的服务器IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyServerIp: str
        :param ContactAddress: 企业联系地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        """
        self.Id = None
        self.Name = None
        self.Email = None
        self.IdCardType = None
        self.IdCardNumber = None
        self.OrganizationType = None
        self.IdCardFileType = None
        self.BizLicenseFile = None
        self.BizLicenseFileName = None
        self.LegalName = None
        self.LegalIdCardType = None
        self.LegalIdCardNumber = None
        self.LegalMobile = None
        self.ContactName = None
        self.VerifyStatus = None
        self.VerifiedOn = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.VerifyClientIp = None
        self.VerifyServerIp = None
        self.ContactAddress = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Email = params.get("Email")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        self.OrganizationType = params.get("OrganizationType")
        self.IdCardFileType = params.get("IdCardFileType")
        self.BizLicenseFile = params.get("BizLicenseFile")
        self.BizLicenseFileName = params.get("BizLicenseFileName")
        self.LegalName = params.get("LegalName")
        self.LegalIdCardType = params.get("LegalIdCardType")
        self.LegalIdCardNumber = params.get("LegalIdCardNumber")
        self.LegalMobile = params.get("LegalMobile")
        self.ContactName = params.get("ContactName")
        self.VerifyStatus = params.get("VerifyStatus")
        self.VerifiedOn = params.get("VerifiedOn")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.VerifyClientIp = params.get("VerifyClientIp")
        self.VerifyServerIp = params.get("VerifyServerIp")
        if params.get("ContactAddress") is not None:
            self.ContactAddress = Address()
            self.ContactAddress._deserialize(params.get("ContactAddress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFile(AbstractModel):
    """此结构体 (UploadFile) 用于描述多文件上传的文件信息。

    """

    def __init__(self):
        r"""
        :param FileBody: Base64编码后的文件内容
        :type FileBody: str
        :param FileName: 文件名
        :type FileName: str
        """
        self.FileBody = None
        self.FileName = None


    def _deserialize(self, params):
        self.FileBody = params.get("FileBody")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesRequest(AbstractModel):
    """UploadFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param BusinessType: 文件对应业务类型，用于区分文件存储路径：
1. TEMPLATE - 模版； 文件类型：.pdf/.html
2. DOCUMENT - 签署过程及签署后的合同文档 文件类型：.pdf/.html
3. FLOW - 签署过程 文件类型：.pdf/.html
4. SEAL - 印章； 文件类型：.jpg/.jpeg/.png
5. BUSINESSLICENSE - 营业执照 文件类型：.jpg/.jpeg/.png
6. IDCARD - 身份证 文件类型：.jpg/.jpeg/.png
        :type BusinessType: str
        :param FileInfos: 上传文件内容数组，最多支持20个文件
        :type FileInfos: list of UploadFile
        :param FileUrls: 上传文件链接数组，最多支持20个URL
        :type FileUrls: list of str
        :param CoverRect: 是否将pdf灰色矩阵置白
true--是，处理置白
false--否，不处理
        :type CoverRect: bool
        :param FileType: 特殊文件类型需要指定文件类型：
HTML-- .html文件
        :type FileType: str
        :param CustomIds: 用户自定义ID数组，与上传文件一一对应
        :type CustomIds: list of str
        """
        self.Caller = None
        self.BusinessType = None
        self.FileInfos = None
        self.FileUrls = None
        self.CoverRect = None
        self.FileType = None
        self.CustomIds = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.BusinessType = params.get("BusinessType")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = UploadFile()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        self.FileUrls = params.get("FileUrls")
        self.CoverRect = params.get("CoverRect")
        self.FileType = params.get("FileType")
        self.CustomIds = params.get("CustomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesResponse(AbstractModel):
    """UploadFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileIds: 文件id数组
        :type FileIds: list of str
        :param TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileIds = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class UserDescribe(AbstractModel):
    """此结构体 (UserDescribe) 用于描述个人帐号查询结果。

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        :param Mobile: 手机号，隐藏中间4位数字，用*代替
        :type Mobile: str
        :param CreatedOn: 注册时间点 (UNIX时间戳)
        :type CreatedOn: int
        :param VerifyStatus: 实名认证状态：
0 - 未实名；
1 - 通过实名
        :type VerifyStatus: int
        :param Name: 真实姓名
        :type Name: str
        :param VerifiedOn: 实名认证通过时间 (UNIX时间戳)
        :type VerifiedOn: int
        :param IdCardType: 身份证件类型; 
ID_CARD - 居民身份证；
PASSPORT - 护照；
MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证；
MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证；
HOUSEHOLD_REGISTER - 户口本；
TEMP_ID_CARD - 临时居民身份证
        :type IdCardType: str
        :param IdCardNumber: 身份证件号码 (脱敏)
        :type IdCardNumber: str
        """
        self.UserId = None
        self.Mobile = None
        self.CreatedOn = None
        self.VerifyStatus = None
        self.Name = None
        self.VerifiedOn = None
        self.IdCardType = None
        self.IdCardNumber = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Mobile = params.get("Mobile")
        self.CreatedOn = params.get("CreatedOn")
        self.VerifyStatus = params.get("VerifyStatus")
        self.Name = params.get("Name")
        self.VerifiedOn = params.get("VerifiedOn")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySubOrganizationRequest(AbstractModel):
    """VerifySubOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息，该接口SubOrganizationId必填
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param OpenId: 机构在第三方的唯一标识，32位定长字符串，与 Caller 中 SubOrgnizationId 二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :type OpenId: str
        """
        self.Caller = None
        self.OpenId = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySubOrganizationResponse(AbstractModel):
    """VerifySubOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubOrganizationId: 子机构ID
        :type SubOrganizationId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubOrganizationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubOrganizationId = params.get("SubOrganizationId")
        self.RequestId = params.get("RequestId")


class VerifyUserRequest(AbstractModel):
    """VerifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param UserId: 电子签平台用户ID
        :type UserId: str
        :param CertificateRequired: 是否需要下发个人长效证书，默认为false
注：如您有下发个人长效证书需求，请提前邮件至e-contract@oa.com进行申请。
        :type CertificateRequired: bool
        """
        self.Caller = None
        self.UserId = None
        self.CertificateRequired = None


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        self.UserId = params.get("UserId")
        self.CertificateRequired = params.get("CertificateRequired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyUserResponse(AbstractModel):
    """VerifyUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 电子签平台用户ID
        :type UserId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")