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
        :param _Province: 省份
        :type Province: str
        :param _City: 城市
        :type City: str
        :param _County: 区县
        :type County: str
        :param _Details: 详细地址
        :type Details: str
        :param _Country: 国家，默认中国
        :type Country: str
        """
        self._Province = None
        self._City = None
        self._County = None
        self._Details = None
        self._Country = None

    @property
    def Province(self):
        """省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def County(self):
        """区县
        :rtype: str
        """
        return self._County

    @County.setter
    def County(self, County):
        self._County = County

    @property
    def Details(self):
        """详细地址
        :rtype: str
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def Country(self):
        """国家，默认中国
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country


    def _deserialize(self, params):
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._County = params.get("County")
        self._Details = params.get("Details")
        self._Country = params.get("Country")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveFlowRequest(AbstractModel):
    """ArchiveFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 流程ID
        :type FlowId: str
        """
        self._Caller = None
        self._FlowId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveFlowResponse(AbstractModel):
    """ArchiveFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Caller(AbstractModel):
    """此结构体 (Caller) 用于描述调用方属性。

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用号
        :type ApplicationId: str
        :param _SubOrganizationId: 下属机构ID
        :type SubOrganizationId: str
        :param _OperatorId: 经办人的用户ID
        :type OperatorId: str
        """
        self._ApplicationId = None
        self._SubOrganizationId = None
        self._OperatorId = None

    @property
    def ApplicationId(self):
        """应用号
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SubOrganizationId(self):
        """下属机构ID
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def OperatorId(self):
        """经办人的用户ID
        :rtype: str
        """
        return self._OperatorId

    @OperatorId.setter
    def OperatorId(self, OperatorId):
        self._OperatorId = OperatorId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._OperatorId = params.get("OperatorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowRequest(AbstractModel):
    """CancelFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _CancelMessage: 撤销原因
        :type CancelMessage: str
        """
        self._Caller = None
        self._FlowId = None
        self._CancelMessage = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def CancelMessage(self):
        """撤销原因
        :rtype: str
        """
        return self._CancelMessage

    @CancelMessage.setter
    def CancelMessage(self, CancelMessage):
        self._CancelMessage = CancelMessage


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        self._CancelMessage = params.get("CancelMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowResponse(AbstractModel):
    """CancelFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CatalogApprovers(AbstractModel):
    """目录流程参与者

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _Approvers: 参与者列表
        :type Approvers: list of FlowApproverInfo
        """
        self._FlowId = None
        self._Approvers = None

    @property
    def FlowId(self):
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Approvers(self):
        """参与者列表
        :rtype: list of FlowApproverInfo
        """
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self._Approvers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CatalogComponents(AbstractModel):
    """目录流程签署区

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _SignComponents: 签署区列表
        :type SignComponents: list of Component
        :param _SignId: 签署任务ID
        :type SignId: str
        """
        self._FlowId = None
        self._SignComponents = None
        self._SignId = None

    @property
    def FlowId(self):
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def SignComponents(self):
        """签署区列表
        :rtype: list of Component
        """
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def SignId(self):
        """签署任务ID
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard2EVerificationRequest(AbstractModel):
    """CheckBankCard2EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _BankCard: 银行卡号
        :type BankCard: str
        :param _Name: 姓名
        :type Name: str
        """
        self._Caller = None
        self._BankCard = None
        self._Name = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def BankCard(self):
        """银行卡号
        :rtype: str
        """
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._BankCard = params.get("BankCard")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard2EVerificationResponse(AbstractModel):
    """CheckBankCard2EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 检测结果
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
        :param _Description: 结果描述; 未通过时必选
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        """检测结果
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
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述; 未通过时必选
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckBankCard3EVerificationRequest(AbstractModel):
    """CheckBankCard3EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _BankCard: 银行卡号
        :type BankCard: str
        :param _Name: 姓名
        :type Name: str
        :param _IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param _IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self._Caller = None
        self._BankCard = None
        self._Name = None
        self._IdCardNumber = None
        self._IdCardType = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def BankCard(self):
        """银行卡号
        :rtype: str
        """
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        """身份证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def IdCardType(self):
        """身份证件类型; ID_CARD
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._BankCard = params.get("BankCard")
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard3EVerificationResponse(AbstractModel):
    """CheckBankCard3EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 检测结果
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
        :param _Description: 结果描述; 未通过时必选
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        """检测结果
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
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述; 未通过时必选
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckBankCard4EVerificationRequest(AbstractModel):
    """CheckBankCard4EVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _BankCard: 银行卡号
        :type BankCard: str
        :param _Name: 姓名
        :type Name: str
        :param _IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param _Mobile: 手机号
        :type Mobile: str
        :param _IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self._Caller = None
        self._BankCard = None
        self._Name = None
        self._IdCardNumber = None
        self._Mobile = None
        self._IdCardType = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def BankCard(self):
        """银行卡号
        :rtype: str
        """
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        """身份证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def Mobile(self):
        """手机号
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def IdCardType(self):
        """身份证件类型; ID_CARD
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._BankCard = params.get("BankCard")
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._Mobile = params.get("Mobile")
        self._IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCard4EVerificationResponse(AbstractModel):
    """CheckBankCard4EVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 检测结果
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
        :param _Description: 结果描述; 未通过时必选
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        """检测结果
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
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述; 未通过时必选
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckBankCardVerificationRequest(AbstractModel):
    """CheckBankCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _BankCard: 银行卡号
        :type BankCard: str
        :param _Name: 姓名
        :type Name: str
        :param _IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param _Mobile: 手机号
        :type Mobile: str
        :param _IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self._Caller = None
        self._BankCard = None
        self._Name = None
        self._IdCardNumber = None
        self._Mobile = None
        self._IdCardType = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def BankCard(self):
        """银行卡号
        :rtype: str
        """
        return self._BankCard

    @BankCard.setter
    def BankCard(self, BankCard):
        self._BankCard = BankCard

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        """身份证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def Mobile(self):
        """手机号
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def IdCardType(self):
        """身份证件类型; ID_CARD
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._BankCard = params.get("BankCard")
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._Mobile = params.get("Mobile")
        self._IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBankCardVerificationResponse(AbstractModel):
    """CheckBankCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 检测结果
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
        :param _Description: 结果描述; 未通过时必选
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        """检测结果
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
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述; 未通过时必选
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckFaceIdentifyRequest(AbstractModel):
    """CheckFaceIdentify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _VerifyChannel: 人脸核身渠道; 必选; WEIXINAPP:腾讯电子签小程序,FACEID:腾讯电子签慧眼,None:白名单中的客户直接通过
        :type VerifyChannel: str
        :param _VerifyResult: 核身订单号; 必选; 对于WEIXINAPP,直接取响应的{VerifyResult};对于FACEID,使用{WbAppId}:{OrderNo}拼接
        :type VerifyResult: str
        :param _Name: 要对比的姓名; 可选; 未填写时对比caller.OperatorId的实名信息
        :type Name: str
        :param _IdCardNumber: 要对比的身份证号码; 可选; 未填写时对比caller.OperatorId的实名信息
        :type IdCardNumber: str
        :param _GetPhoto: 是否取认证时的照片
        :type GetPhoto: bool
        """
        self._Caller = None
        self._VerifyChannel = None
        self._VerifyResult = None
        self._Name = None
        self._IdCardNumber = None
        self._GetPhoto = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def VerifyChannel(self):
        """人脸核身渠道; 必选; WEIXINAPP:腾讯电子签小程序,FACEID:腾讯电子签慧眼,None:白名单中的客户直接通过
        :rtype: str
        """
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def VerifyResult(self):
        """核身订单号; 必选; 对于WEIXINAPP,直接取响应的{VerifyResult};对于FACEID,使用{WbAppId}:{OrderNo}拼接
        :rtype: str
        """
        return self._VerifyResult

    @VerifyResult.setter
    def VerifyResult(self, VerifyResult):
        self._VerifyResult = VerifyResult

    @property
    def Name(self):
        """要对比的姓名; 可选; 未填写时对比caller.OperatorId的实名信息
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        """要对比的身份证号码; 可选; 未填写时对比caller.OperatorId的实名信息
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def GetPhoto(self):
        """是否取认证时的照片
        :rtype: bool
        """
        return self._GetPhoto

    @GetPhoto.setter
    def GetPhoto(self, GetPhoto):
        self._GetPhoto = GetPhoto


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._VerifyChannel = params.get("VerifyChannel")
        self._VerifyResult = params.get("VerifyResult")
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._GetPhoto = params.get("GetPhoto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckFaceIdentifyResponse(AbstractModel):
    """CheckFaceIdentify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 核身结果; 0:通过,1:不通过
        :type Result: int
        :param _Description: 核身结果描述
        :type Description: str
        :param _ChannelName: 渠道名
        :type ChannelName: str
        :param _VerifiedOn: 认证通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifiedOn: int
        :param _SerialNumber: 核身流水号
        :type SerialNumber: str
        :param _VerifyServerIp: 渠道核身服务器IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyServerIp: str
        :param _PhotoFileName: 核身照片文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type PhotoFileName: str
        :param _PhotoFileData: 核身照片内容base64(文件格式见文件名后缀,一般为jpg)
注意：此字段可能返回 null，表示取不到有效值。
        :type PhotoFileData: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._ChannelName = None
        self._VerifiedOn = None
        self._SerialNumber = None
        self._VerifyServerIp = None
        self._PhotoFileName = None
        self._PhotoFileData = None
        self._RequestId = None

    @property
    def Result(self):
        """核身结果; 0:通过,1:不通过
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """核身结果描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ChannelName(self):
        """渠道名
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def VerifiedOn(self):
        """认证通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VerifiedOn

    @VerifiedOn.setter
    def VerifiedOn(self, VerifiedOn):
        self._VerifiedOn = VerifiedOn

    @property
    def SerialNumber(self):
        """核身流水号
        :rtype: str
        """
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def VerifyServerIp(self):
        """渠道核身服务器IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyServerIp

    @VerifyServerIp.setter
    def VerifyServerIp(self, VerifyServerIp):
        self._VerifyServerIp = VerifyServerIp

    @property
    def PhotoFileName(self):
        """核身照片文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PhotoFileName

    @PhotoFileName.setter
    def PhotoFileName(self, PhotoFileName):
        self._PhotoFileName = PhotoFileName

    @property
    def PhotoFileData(self):
        """核身照片内容base64(文件格式见文件名后缀,一般为jpg)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PhotoFileData

    @PhotoFileData.setter
    def PhotoFileData(self, PhotoFileData):
        self._PhotoFileData = PhotoFileData

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._ChannelName = params.get("ChannelName")
        self._VerifiedOn = params.get("VerifiedOn")
        self._SerialNumber = params.get("SerialNumber")
        self._VerifyServerIp = params.get("VerifyServerIp")
        self._PhotoFileName = params.get("PhotoFileName")
        self._PhotoFileData = params.get("PhotoFileData")
        self._RequestId = params.get("RequestId")


class CheckIdCardVerificationRequest(AbstractModel):
    """CheckIdCardVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Name: 姓名
        :type Name: str
        :param _IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param _IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self._Caller = None
        self._Name = None
        self._IdCardNumber = None
        self._IdCardType = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        """身份证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def IdCardType(self):
        """身份证件类型; ID_CARD
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckIdCardVerificationResponse(AbstractModel):
    """CheckIdCardVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 检测结果; 
收费错误码:
  0: 通过,
  1: 姓名和身份证号不一致,
免费错误码:
  101: 非法身份证号(长度,格式等不正确),
  102: 非法姓名(长度,格式等不正确),
  103: 验证平台异常,
  104: 证件库中无此身份证记录
        :type Result: int
        :param _Description: 结果描述; 未通过时必选
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        """检测结果; 
收费错误码:
  0: 通过,
  1: 姓名和身份证号不一致,
免费错误码:
  101: 非法身份证号(长度,格式等不正确),
  102: 非法姓名(长度,格式等不正确),
  103: 验证平台异常,
  104: 证件库中无此身份证记录
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述; 未通过时必选
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckMobileAndNameRequest(AbstractModel):
    """CheckMobileAndName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Mobile: 手机号
        :type Mobile: str
        :param _Name: 姓名
        :type Name: str
        """
        self._Caller = None
        self._Mobile = None
        self._Name = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Mobile(self):
        """手机号
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Mobile = params.get("Mobile")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckMobileAndNameResponse(AbstractModel):
    """CheckMobileAndName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 检测结果
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
        :param _Description: 结果描述; 未通过时必选
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        """检测结果
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
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述; 未通过时必选
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckMobileVerificationRequest(AbstractModel):
    """CheckMobileVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Mobile: 手机号
        :type Mobile: str
        :param _Name: 姓名
        :type Name: str
        :param _IdCardNumber: 身份证件号码
        :type IdCardNumber: str
        :param _IdCardType: 身份证件类型; ID_CARD
        :type IdCardType: str
        """
        self._Caller = None
        self._Mobile = None
        self._Name = None
        self._IdCardNumber = None
        self._IdCardType = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Mobile(self):
        """手机号
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardNumber(self):
        """身份证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def IdCardType(self):
        """身份证件类型; ID_CARD
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Mobile = params.get("Mobile")
        self._Name = params.get("Name")
        self._IdCardNumber = params.get("IdCardNumber")
        self._IdCardType = params.get("IdCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckMobileVerificationResponse(AbstractModel):
    """CheckMobileVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 检测结果
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
        :param _Description: 结果描述; 未通过时必选
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Result(self):
        """检测结果
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
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述; 未通过时必选
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class CheckVerifyCodeMatchFlowIdRequest(AbstractModel):
    """CheckVerifyCodeMatchFlowId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Mobile: 手机号
        :type Mobile: str
        :param _VerifyCode: 验证码
        :type VerifyCode: str
        :param _FlowId: 流程(目录) id
        :type FlowId: str
        """
        self._Caller = None
        self._Mobile = None
        self._VerifyCode = None
        self._FlowId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Mobile(self):
        """手机号
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def VerifyCode(self):
        """验证码
        :rtype: str
        """
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode

    @property
    def FlowId(self):
        """流程(目录) id
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Mobile = params.get("Mobile")
        self._VerifyCode = params.get("VerifyCode")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckVerifyCodeMatchFlowIdResponse(AbstractModel):
    """CheckVerifyCodeMatchFlowId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: true: 验证码正确，false: 验证码错误
        :type Success: bool
        :param _Result: 0: 验证码正确 1:验证码错误或过期 2:验证码错误 3:验证码和流程不匹配 4:验证码输入错误超过次数 5:内部错误
6:参数错误
        :type Result: int
        :param _Description: 结果描述
        :type Description: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._Result = None
        self._Description = None
        self._RequestId = None

    @property
    def Success(self):
        """true: 验证码正确，false: 验证码错误
        :rtype: bool
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Result(self):
        """0: 验证码正确 1:验证码错误或过期 2:验证码错误 3:验证码和流程不匹配 4:验证码输入错误超过次数 5:内部错误
6:参数错误
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """结果描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Success = params.get("Success")
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class Component(AbstractModel):
    """此结构体 (Component) 用于描述控件属性。

    """

    def __init__(self):
        r"""
        :param _ComponentId: 控件编号

注：
当GenerateMode=3时，通过"^"来决定是否使用关键字整词匹配能力。
例：
当GenerateMode=3时，如果传入关键字"^甲方签署^"，则会在PDF文件中有且仅有"甲方签署"关键字的地方进行对应操作。
如传入的关键字为"甲方签署"，则PDF文件中每个出现关键字的位置都会执行相应操作。
        :type ComponentId: str
        :param _ComponentType: 如果是Component控件类型，则可选的字段为：
TEXT - 普通文本控件；
DATE - 普通日期控件；
SELECT- 勾选框控件；
如果是SignComponent控件类型，则可选的字段为
SIGN_SEAL- 签署印章控件；
SIGN_DATE- 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
        :type ComponentType: str
        :param _ComponentName: 控件名称
        :type ComponentName: str
        :param _ComponentRequired: 定义控件是否为必填项，默认为false
        :type ComponentRequired: bool
        :param _FileIndex: 控件所属文件的序号 (模板中的resourceId排列序号)
        :type FileIndex: int
        :param _GenerateMode: 控件生成的方式：
0 - 普通控件
1 - 表单域
2 - html 控件
3 - 关键字
        :type GenerateMode: int
        :param _ComponentWidth: 参数控件宽度，单位px
        :type ComponentWidth: float
        :param _ComponentHeight: 参数控件高度，单位px
        :type ComponentHeight: float
        :param _ComponentPage: 参数控件所在页码
        :type ComponentPage: int
        :param _ComponentPosX: 参数控件X位置，单位px
        :type ComponentPosX: float
        :param _ComponentPosY: 参数控件Y位置，单位px
        :type ComponentPosY: float
        :param _ComponentExtra: 参数控件样式
        :type ComponentExtra: str
        :param _ComponentValue: 印章ID，如果是手写签名则为jpg或png格式的base64图片

SIGN_SEAL控件,可以用ORG_DEFAULT_SEAL表示主企业的默认印章
SIGN_SEAL控件,可以用SUBORG_DEFAULT_SEAL表示子企业的默认印章
SIGN_SEAL控件,可以用USER_DEFAULT_SEAL表示个人默认印章
        :type ComponentValue: str
        :param _SealOperate: 如果是SIGN_SEAL类型的签署控件, 参数标识H5签署界面是否在该签署区上进行放置展示, 1为放置,其他为不放置
        :type SealOperate: int
        :param _GenerateExtra: 不同GenerateMode对应的额外信息
        :type GenerateExtra: str
        """
        self._ComponentId = None
        self._ComponentType = None
        self._ComponentName = None
        self._ComponentRequired = None
        self._FileIndex = None
        self._GenerateMode = None
        self._ComponentWidth = None
        self._ComponentHeight = None
        self._ComponentPage = None
        self._ComponentPosX = None
        self._ComponentPosY = None
        self._ComponentExtra = None
        self._ComponentValue = None
        self._SealOperate = None
        self._GenerateExtra = None

    @property
    def ComponentId(self):
        """控件编号

注：
当GenerateMode=3时，通过"^"来决定是否使用关键字整词匹配能力。
例：
当GenerateMode=3时，如果传入关键字"^甲方签署^"，则会在PDF文件中有且仅有"甲方签署"关键字的地方进行对应操作。
如传入的关键字为"甲方签署"，则PDF文件中每个出现关键字的位置都会执行相应操作。
        :rtype: str
        """
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def ComponentType(self):
        """如果是Component控件类型，则可选的字段为：
TEXT - 普通文本控件；
DATE - 普通日期控件；
SELECT- 勾选框控件；
如果是SignComponent控件类型，则可选的字段为
SIGN_SEAL- 签署印章控件；
SIGN_DATE- 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
        :rtype: str
        """
        return self._ComponentType

    @ComponentType.setter
    def ComponentType(self, ComponentType):
        self._ComponentType = ComponentType

    @property
    def ComponentName(self):
        """控件名称
        :rtype: str
        """
        return self._ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName):
        self._ComponentName = ComponentName

    @property
    def ComponentRequired(self):
        """定义控件是否为必填项，默认为false
        :rtype: bool
        """
        return self._ComponentRequired

    @ComponentRequired.setter
    def ComponentRequired(self, ComponentRequired):
        self._ComponentRequired = ComponentRequired

    @property
    def FileIndex(self):
        """控件所属文件的序号 (模板中的resourceId排列序号)
        :rtype: int
        """
        return self._FileIndex

    @FileIndex.setter
    def FileIndex(self, FileIndex):
        self._FileIndex = FileIndex

    @property
    def GenerateMode(self):
        """控件生成的方式：
0 - 普通控件
1 - 表单域
2 - html 控件
3 - 关键字
        :rtype: int
        """
        return self._GenerateMode

    @GenerateMode.setter
    def GenerateMode(self, GenerateMode):
        self._GenerateMode = GenerateMode

    @property
    def ComponentWidth(self):
        """参数控件宽度，单位px
        :rtype: float
        """
        return self._ComponentWidth

    @ComponentWidth.setter
    def ComponentWidth(self, ComponentWidth):
        self._ComponentWidth = ComponentWidth

    @property
    def ComponentHeight(self):
        """参数控件高度，单位px
        :rtype: float
        """
        return self._ComponentHeight

    @ComponentHeight.setter
    def ComponentHeight(self, ComponentHeight):
        self._ComponentHeight = ComponentHeight

    @property
    def ComponentPage(self):
        """参数控件所在页码
        :rtype: int
        """
        return self._ComponentPage

    @ComponentPage.setter
    def ComponentPage(self, ComponentPage):
        self._ComponentPage = ComponentPage

    @property
    def ComponentPosX(self):
        """参数控件X位置，单位px
        :rtype: float
        """
        return self._ComponentPosX

    @ComponentPosX.setter
    def ComponentPosX(self, ComponentPosX):
        self._ComponentPosX = ComponentPosX

    @property
    def ComponentPosY(self):
        """参数控件Y位置，单位px
        :rtype: float
        """
        return self._ComponentPosY

    @ComponentPosY.setter
    def ComponentPosY(self, ComponentPosY):
        self._ComponentPosY = ComponentPosY

    @property
    def ComponentExtra(self):
        """参数控件样式
        :rtype: str
        """
        return self._ComponentExtra

    @ComponentExtra.setter
    def ComponentExtra(self, ComponentExtra):
        self._ComponentExtra = ComponentExtra

    @property
    def ComponentValue(self):
        """印章ID，如果是手写签名则为jpg或png格式的base64图片

SIGN_SEAL控件,可以用ORG_DEFAULT_SEAL表示主企业的默认印章
SIGN_SEAL控件,可以用SUBORG_DEFAULT_SEAL表示子企业的默认印章
SIGN_SEAL控件,可以用USER_DEFAULT_SEAL表示个人默认印章
        :rtype: str
        """
        return self._ComponentValue

    @ComponentValue.setter
    def ComponentValue(self, ComponentValue):
        self._ComponentValue = ComponentValue

    @property
    def SealOperate(self):
        """如果是SIGN_SEAL类型的签署控件, 参数标识H5签署界面是否在该签署区上进行放置展示, 1为放置,其他为不放置
        :rtype: int
        """
        return self._SealOperate

    @SealOperate.setter
    def SealOperate(self, SealOperate):
        self._SealOperate = SealOperate

    @property
    def GenerateExtra(self):
        """不同GenerateMode对应的额外信息
        :rtype: str
        """
        return self._GenerateExtra

    @GenerateExtra.setter
    def GenerateExtra(self, GenerateExtra):
        self._GenerateExtra = GenerateExtra


    def _deserialize(self, params):
        self._ComponentId = params.get("ComponentId")
        self._ComponentType = params.get("ComponentType")
        self._ComponentName = params.get("ComponentName")
        self._ComponentRequired = params.get("ComponentRequired")
        self._FileIndex = params.get("FileIndex")
        self._GenerateMode = params.get("GenerateMode")
        self._ComponentWidth = params.get("ComponentWidth")
        self._ComponentHeight = params.get("ComponentHeight")
        self._ComponentPage = params.get("ComponentPage")
        self._ComponentPosX = params.get("ComponentPosX")
        self._ComponentPosY = params.get("ComponentPosY")
        self._ComponentExtra = params.get("ComponentExtra")
        self._ComponentValue = params.get("ComponentValue")
        self._SealOperate = params.get("SealOperate")
        self._GenerateExtra = params.get("GenerateExtra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComponentSeal(AbstractModel):
    """此结构体 (ComponentSeal) 用于描述“签署区ID”到“印章ID”的映射。

    """

    def __init__(self):
        r"""
        :param _ComponentId: 签署区ID
        :type ComponentId: str
        :param _SealId: 印章ID
        :type SealId: str
        """
        self._ComponentId = None
        self._SealId = None

    @property
    def ComponentId(self):
        """签署区ID
        :rtype: str
        """
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def SealId(self):
        """印章ID
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId


    def _deserialize(self, params):
        self._ComponentId = params.get("ComponentId")
        self._SealId = params.get("SealId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFaceIdSignRequest(AbstractModel):
    """CreateFaceIdSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Values: 除api_ticket之外的其它要参与签名的参数值,包括UserId
        :type Values: list of str
        """
        self._Caller = None
        self._Values = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Values(self):
        """除api_ticket之外的其它要参与签名的参数值,包括UserId
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFaceIdSignResponse(AbstractModel):
    """CreateFaceIdSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Sign: 慧眼API签名
        :type Sign: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Sign = None
        self._RequestId = None

    @property
    def Sign(self):
        """慧眼API签名
        :rtype: str
        """
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Sign = params.get("Sign")
        self._RequestId = params.get("RequestId")


class CreateFlowByFilesRequest(AbstractModel):
    """CreateFlowByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowInfo: 流程创建信息
        :type FlowInfo: :class:`tencentcloud.essbasic.v20201222.models.FlowInfo`
        :param _FileIds: 文件资源列表 (支持多文件)
        :type FileIds: list of str
        :param _CustomId: 自定义流程id
        :type CustomId: str
        """
        self._Caller = None
        self._FlowInfo = None
        self._FileIds = None
        self._CustomId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowInfo(self):
        """流程创建信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.FlowInfo`
        """
        return self._FlowInfo

    @FlowInfo.setter
    def FlowInfo(self, FlowInfo):
        self._FlowInfo = FlowInfo

    @property
    def FileIds(self):
        """文件资源列表 (支持多文件)
        :rtype: list of str
        """
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def CustomId(self):
        """自定义流程id
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        if params.get("FlowInfo") is not None:
            self._FlowInfo = FlowInfo()
            self._FlowInfo._deserialize(params.get("FlowInfo"))
        self._FileIds = params.get("FileIds")
        self._CustomId = params.get("CustomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowByFilesResponse(AbstractModel):
    """CreateFlowByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._RequestId = None

    @property
    def FlowId(self):
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")


class CreateH5FaceIdUrlRequest(AbstractModel):
    """CreateH5FaceIdUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _WbAppId: 慧眼业务ID; 不填写时后台使用Caller反查
        :type WbAppId: str
        :param _Name: 姓名; 可选(未通过实名认证的用户必选)
        :type Name: str
        :param _IdCardType: 用户证件类型; 可选; 默认ID_CARD:中国居民身份证
        :type IdCardType: str
        :param _IdCardNumber: 用户证件号; 可选(未通过实名认证的用户必选)
        :type IdCardNumber: str
        :param _JumpUrl: H5人脸核身完成后回调的第三方Url; 可选; 不需要做Encode, 跳转的参数: ?code=XX&orderNo=XX&liveRate=xx, code=0表示成功,orderNo为订单号,liveRate为百分制活体检测得分
        :type JumpUrl: str
        :param _JumpType: 参数值为"1":直接跳转到url回调地址; 可选; 其他值:跳转提供的结果页面
        :type JumpType: str
        :param _OpenFrom: browser:表示在浏览器启动刷脸, app:表示在App里启动刷脸,默认值为browser; 可选
        :type OpenFrom: str
        :param _RedirectType: 跳转类型; 可选; 参数值为"1"时,刷脸页面使用replace方式跳转,不在浏览器history中留下记录;不传或其他值则正常跳转
        :type RedirectType: str
        """
        self._Caller = None
        self._WbAppId = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._JumpUrl = None
        self._JumpType = None
        self._OpenFrom = None
        self._RedirectType = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def WbAppId(self):
        """慧眼业务ID; 不填写时后台使用Caller反查
        :rtype: str
        """
        return self._WbAppId

    @WbAppId.setter
    def WbAppId(self, WbAppId):
        self._WbAppId = WbAppId

    @property
    def Name(self):
        """姓名; 可选(未通过实名认证的用户必选)
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        """用户证件类型; 可选; 默认ID_CARD:中国居民身份证
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """用户证件号; 可选(未通过实名认证的用户必选)
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def JumpUrl(self):
        """H5人脸核身完成后回调的第三方Url; 可选; 不需要做Encode, 跳转的参数: ?code=XX&orderNo=XX&liveRate=xx, code=0表示成功,orderNo为订单号,liveRate为百分制活体检测得分
        :rtype: str
        """
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def JumpType(self):
        """参数值为"1":直接跳转到url回调地址; 可选; 其他值:跳转提供的结果页面
        :rtype: str
        """
        return self._JumpType

    @JumpType.setter
    def JumpType(self, JumpType):
        self._JumpType = JumpType

    @property
    def OpenFrom(self):
        """browser:表示在浏览器启动刷脸, app:表示在App里启动刷脸,默认值为browser; 可选
        :rtype: str
        """
        return self._OpenFrom

    @OpenFrom.setter
    def OpenFrom(self, OpenFrom):
        self._OpenFrom = OpenFrom

    @property
    def RedirectType(self):
        """跳转类型; 可选; 参数值为"1"时,刷脸页面使用replace方式跳转,不在浏览器history中留下记录;不传或其他值则正常跳转
        :rtype: str
        """
        return self._RedirectType

    @RedirectType.setter
    def RedirectType(self, RedirectType):
        self._RedirectType = RedirectType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._WbAppId = params.get("WbAppId")
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._JumpUrl = params.get("JumpUrl")
        self._JumpType = params.get("JumpType")
        self._OpenFrom = params.get("OpenFrom")
        self._RedirectType = params.get("RedirectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateH5FaceIdUrlResponse(AbstractModel):
    """CreateH5FaceIdUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 跳转到人脸核身页面的链接
        :type Url: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        """跳转到人脸核身页面的链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class CreatePreviewSignUrlRequest(AbstractModel):
    """CreatePreviewSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Deadline: URL过期时间戳
        :type Deadline: int
        :param _CatalogId: 目录ID。当 SignUrlType 为 CATALOG 时必填
        :type CatalogId: str
        :param _FlowId: 流程ID。当 SignUrlType 为 FLOW 时必填
        :type FlowId: str
        :param _SignUrlType: 签署链接类型：
1. FLOW - 单流程签署 (默认) 
2. CATALOG - 目录签署
        :type SignUrlType: str
        """
        self._Caller = None
        self._Deadline = None
        self._CatalogId = None
        self._FlowId = None
        self._SignUrlType = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Deadline(self):
        """URL过期时间戳
        :rtype: int
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def CatalogId(self):
        """目录ID。当 SignUrlType 为 CATALOG 时必填
        :rtype: str
        """
        return self._CatalogId

    @CatalogId.setter
    def CatalogId(self, CatalogId):
        self._CatalogId = CatalogId

    @property
    def FlowId(self):
        """流程ID。当 SignUrlType 为 FLOW 时必填
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def SignUrlType(self):
        """签署链接类型：
1. FLOW - 单流程签署 (默认) 
2. CATALOG - 目录签署
        :rtype: str
        """
        return self._SignUrlType

    @SignUrlType.setter
    def SignUrlType(self, SignUrlType):
        self._SignUrlType = SignUrlType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Deadline = params.get("Deadline")
        self._CatalogId = params.get("CatalogId")
        self._FlowId = params.get("FlowId")
        self._SignUrlType = params.get("SignUrlType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePreviewSignUrlResponse(AbstractModel):
    """CreatePreviewSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PreviewSignUrl: 合同预览URL
        :type PreviewSignUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PreviewSignUrl = None
        self._RequestId = None

    @property
    def PreviewSignUrl(self):
        """合同预览URL
        :rtype: str
        """
        return self._PreviewSignUrl

    @PreviewSignUrl.setter
    def PreviewSignUrl(self, PreviewSignUrl):
        self._PreviewSignUrl = PreviewSignUrl

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PreviewSignUrl = params.get("PreviewSignUrl")
        self._RequestId = params.get("RequestId")


class CreateSealRequest(AbstractModel):
    """CreateSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _SealType: 印章类型：
1. PERSONAL - 个人私章
2. OFFICIAL - 公章
3. SPECIAL_FINANCIAL - 财务专用章
4. CONTRACT - 合同专用章
5. LEGAL_REPRESENTATIVE - 法定代表人章
6. SPECIAL_NATIONWIDE_INVOICE - 发票专用章
7. OTHER-其他
        :type SealType: str
        :param _SealName: 印章名称
        :type SealName: str
        :param _SourceIp: 请求创建印章的客户端IP
        :type SourceIp: str
        :param _Image: 印章图片，base64编码（与FileId参数二选一，同时传入参数时优先使用Image参数）
        :type Image: str
        :param _FileId: 印章文件图片ID（与Image参数二选一，同时传入参数时优先使用Image参数）
        :type FileId: str
        :param _UserId: 需要创建印章的用户ID
        :type UserId: str
        :param _IsDefault: 是否是默认印章 true：是，false：否
        :type IsDefault: bool
        """
        self._Caller = None
        self._SealType = None
        self._SealName = None
        self._SourceIp = None
        self._Image = None
        self._FileId = None
        self._UserId = None
        self._IsDefault = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def SealType(self):
        """印章类型：
1. PERSONAL - 个人私章
2. OFFICIAL - 公章
3. SPECIAL_FINANCIAL - 财务专用章
4. CONTRACT - 合同专用章
5. LEGAL_REPRESENTATIVE - 法定代表人章
6. SPECIAL_NATIONWIDE_INVOICE - 发票专用章
7. OTHER-其他
        :rtype: str
        """
        return self._SealType

    @SealType.setter
    def SealType(self, SealType):
        self._SealType = SealType

    @property
    def SealName(self):
        """印章名称
        :rtype: str
        """
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def SourceIp(self):
        """请求创建印章的客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Image(self):
        """印章图片，base64编码（与FileId参数二选一，同时传入参数时优先使用Image参数）
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def FileId(self):
        """印章文件图片ID（与Image参数二选一，同时传入参数时优先使用Image参数）
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def UserId(self):
        """需要创建印章的用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsDefault(self):
        """是否是默认印章 true：是，false：否
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._SealType = params.get("SealType")
        self._SealName = params.get("SealName")
        self._SourceIp = params.get("SourceIp")
        self._Image = params.get("Image")
        self._FileId = params.get("FileId")
        self._UserId = params.get("UserId")
        self._IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealResponse(AbstractModel):
    """CreateSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealId: 电子印章Id
        :type SealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealId = None
        self._RequestId = None

    @property
    def SealId(self):
        """电子印章Id
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._RequestId = params.get("RequestId")


class CreateServerFlowSignRequest(AbstractModel):
    """CreateServerFlowSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 流程ID
        :type FlowId: str
        :param _SignComponents: 签署区域信息
        :type SignComponents: list of Component
        :param _SourceIp: 客户端IP
        :type SourceIp: str
        """
        self._Caller = None
        self._FlowId = None
        self._SignComponents = None
        self._SourceIp = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def SignComponents(self):
        """签署区域信息
        :rtype: list of Component
        """
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def SourceIp(self):
        """客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._SourceIp = params.get("SourceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerFlowSignResponse(AbstractModel):
    """CreateServerFlowSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignStatus: 任务状态：
0：失败
1：成功
        :type SignStatus: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignStatus = None
        self._RequestId = None

    @property
    def SignStatus(self):
        """任务状态：
0：失败
1：成功
        :rtype: int
        """
        return self._SignStatus

    @SignStatus.setter
    def SignStatus(self, SignStatus):
        self._SignStatus = SignStatus

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignStatus = params.get("SignStatus")
        self._RequestId = params.get("RequestId")


class CreateSignUrlRequest(AbstractModel):
    """CreateSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _UserId: 签署人ID
        :type UserId: str
        :param _Deadline: 文件签署截止时间戳
        :type Deadline: int
        :param _CatalogId: 目录ID。当 SignUrlType 为 CATALOG 时必填
        :type CatalogId: str
        :param _FlowId: 流程ID。当 SignUrlType 为 FLOW 时必填
        :type FlowId: str
        :param _SignUrlType: 签署链接类型：
1. FLOW - 单流程签署 (默认) 
2. CATALOG - 目录签署
        :type SignUrlType: str
        :param _SignId: 发送流程或目录时生成的签署任务ID
        :type SignId: str
        """
        self._Caller = None
        self._UserId = None
        self._Deadline = None
        self._CatalogId = None
        self._FlowId = None
        self._SignUrlType = None
        self._SignId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def UserId(self):
        """签署人ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Deadline(self):
        """文件签署截止时间戳
        :rtype: int
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def CatalogId(self):
        """目录ID。当 SignUrlType 为 CATALOG 时必填
        :rtype: str
        """
        return self._CatalogId

    @CatalogId.setter
    def CatalogId(self, CatalogId):
        self._CatalogId = CatalogId

    @property
    def FlowId(self):
        """流程ID。当 SignUrlType 为 FLOW 时必填
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def SignUrlType(self):
        """签署链接类型：
1. FLOW - 单流程签署 (默认) 
2. CATALOG - 目录签署
        :rtype: str
        """
        return self._SignUrlType

    @SignUrlType.setter
    def SignUrlType(self, SignUrlType):
        self._SignUrlType = SignUrlType

    @property
    def SignId(self):
        """发送流程或目录时生成的签署任务ID
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._UserId = params.get("UserId")
        self._Deadline = params.get("Deadline")
        self._CatalogId = params.get("CatalogId")
        self._FlowId = params.get("FlowId")
        self._SignUrlType = params.get("SignUrlType")
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSignUrlResponse(AbstractModel):
    """CreateSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignUrl: 合同签署链接
        :type SignUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignUrl = None
        self._RequestId = None

    @property
    def SignUrl(self):
        """合同签署链接
        :rtype: str
        """
        return self._SignUrl

    @SignUrl.setter
    def SignUrl(self, SignUrl):
        self._SignUrl = SignUrl

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignUrl = params.get("SignUrl")
        self._RequestId = params.get("RequestId")


class CreateSubOrganizationAndSealRequest(AbstractModel):
    """CreateSubOrganizationAndSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Name: 机构名称全称
        :type Name: str
        :param _IdCardType: 机构证件号码类型可选值：
1. USCC - 统一社会信用代码
2. BIZREGISTNO - 营业执照注册号
        :type IdCardType: str
        :param _IdCardNumber: 机构证件号码
        :type IdCardNumber: str
        :param _OrganizationType: 机构类型可选值：
1. ENTERPRISE - 企业
2. INDIVIDUALBIZ - 个体工商户
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :type OrganizationType: str
        :param _LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param _LegalIdCardType: 机构法人/经营者证件类型可选值：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type LegalIdCardType: str
        :param _LegalIdCardNumber: 机构法人/经营者证件号码；
OrganizationType 为 ENTERPRISE时，INDIVIDUALBIZ 时必填，其他情况选填
        :type LegalIdCardNumber: str
        :param _VerifyClientIp: 实名认证的客户端IP/请求生成企业印章的客户端Ip
        :type VerifyClientIp: str
        :param _Email: 机构电子邮箱
        :type Email: str
        :param _IdCardFileType: 机构证件文件类型可选值：
1. USCCFILE - 统一社会信用代码证书
2. LICENSEFILE - 营业执照
        :type IdCardFileType: str
        :param _BizLicenseFile: 机构证件照片文件，base64编码，支持jpg、jpeg、png格式
        :type BizLicenseFile: str
        :param _BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param _LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param _ContactName: 组织联系人姓名
        :type ContactName: str
        :param _VerifyServerIp: 实名认证的服务器IP
        :type VerifyServerIp: str
        :param _ContactAddress: 企业联系地址
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        :param _SealName: 电子印章名称
        :type SealName: str
        :param _SealType: 印章类型：默认: CONTRACT
1. OFFICIAL-公章
2. SPECIAL_FINANCIAL-财务专用章
3. CONTRACT-合同专用章
4. LEGAL_REPRESENTATIVE-法定代表人章
5. SPECIAL_NATIONWIDE_INVOICE-发票专用章
6. OTHER-其他
        :type SealType: str
        :param _SealHorizontalText: 企业印章横向文字，最多可填8个汉字（可为空，默认为"电子签名专用章"）
        :type SealHorizontalText: str
        :param _OpenId: 机构在第三方的唯一标识，32位以内标识符
        :type OpenId: str
        :param _UseOpenId: 是否使用OpenId作为数据主键，如果为true，请确保OpenId在当前应用号唯一
        :type UseOpenId: bool
        """
        self._Caller = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._OrganizationType = None
        self._LegalName = None
        self._LegalIdCardType = None
        self._LegalIdCardNumber = None
        self._VerifyClientIp = None
        self._Email = None
        self._IdCardFileType = None
        self._BizLicenseFile = None
        self._BizLicenseFileName = None
        self._LegalMobile = None
        self._ContactName = None
        self._VerifyServerIp = None
        self._ContactAddress = None
        self._SealName = None
        self._SealType = None
        self._SealHorizontalText = None
        self._OpenId = None
        self._UseOpenId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Name(self):
        """机构名称全称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        """机构证件号码类型可选值：
1. USCC - 统一社会信用代码
2. BIZREGISTNO - 营业执照注册号
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """机构证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def OrganizationType(self):
        """机构类型可选值：
1. ENTERPRISE - 企业
2. INDIVIDUALBIZ - 个体工商户
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :rtype: str
        """
        return self._OrganizationType

    @OrganizationType.setter
    def OrganizationType(self, OrganizationType):
        self._OrganizationType = OrganizationType

    @property
    def LegalName(self):
        """机构法人/经营者姓名
        :rtype: str
        """
        return self._LegalName

    @LegalName.setter
    def LegalName(self, LegalName):
        self._LegalName = LegalName

    @property
    def LegalIdCardType(self):
        """机构法人/经营者证件类型可选值：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :rtype: str
        """
        return self._LegalIdCardType

    @LegalIdCardType.setter
    def LegalIdCardType(self, LegalIdCardType):
        self._LegalIdCardType = LegalIdCardType

    @property
    def LegalIdCardNumber(self):
        """机构法人/经营者证件号码；
OrganizationType 为 ENTERPRISE时，INDIVIDUALBIZ 时必填，其他情况选填
        :rtype: str
        """
        return self._LegalIdCardNumber

    @LegalIdCardNumber.setter
    def LegalIdCardNumber(self, LegalIdCardNumber):
        self._LegalIdCardNumber = LegalIdCardNumber

    @property
    def VerifyClientIp(self):
        """实名认证的客户端IP/请求生成企业印章的客户端Ip
        :rtype: str
        """
        return self._VerifyClientIp

    @VerifyClientIp.setter
    def VerifyClientIp(self, VerifyClientIp):
        self._VerifyClientIp = VerifyClientIp

    @property
    def Email(self):
        """机构电子邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def IdCardFileType(self):
        """机构证件文件类型可选值：
1. USCCFILE - 统一社会信用代码证书
2. LICENSEFILE - 营业执照
        :rtype: str
        """
        return self._IdCardFileType

    @IdCardFileType.setter
    def IdCardFileType(self, IdCardFileType):
        self._IdCardFileType = IdCardFileType

    @property
    def BizLicenseFile(self):
        """机构证件照片文件，base64编码，支持jpg、jpeg、png格式
        :rtype: str
        """
        return self._BizLicenseFile

    @BizLicenseFile.setter
    def BizLicenseFile(self, BizLicenseFile):
        self._BizLicenseFile = BizLicenseFile

    @property
    def BizLicenseFileName(self):
        """机构证件照片文件名
        :rtype: str
        """
        return self._BizLicenseFileName

    @BizLicenseFileName.setter
    def BizLicenseFileName(self, BizLicenseFileName):
        self._BizLicenseFileName = BizLicenseFileName

    @property
    def LegalMobile(self):
        """机构法人/经营者/联系人手机号码
        :rtype: str
        """
        return self._LegalMobile

    @LegalMobile.setter
    def LegalMobile(self, LegalMobile):
        self._LegalMobile = LegalMobile

    @property
    def ContactName(self):
        """组织联系人姓名
        :rtype: str
        """
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def VerifyServerIp(self):
        """实名认证的服务器IP
        :rtype: str
        """
        return self._VerifyServerIp

    @VerifyServerIp.setter
    def VerifyServerIp(self, VerifyServerIp):
        self._VerifyServerIp = VerifyServerIp

    @property
    def ContactAddress(self):
        """企业联系地址
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Address`
        """
        return self._ContactAddress

    @ContactAddress.setter
    def ContactAddress(self, ContactAddress):
        self._ContactAddress = ContactAddress

    @property
    def SealName(self):
        """电子印章名称
        :rtype: str
        """
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def SealType(self):
        """印章类型：默认: CONTRACT
1. OFFICIAL-公章
2. SPECIAL_FINANCIAL-财务专用章
3. CONTRACT-合同专用章
4. LEGAL_REPRESENTATIVE-法定代表人章
5. SPECIAL_NATIONWIDE_INVOICE-发票专用章
6. OTHER-其他
        :rtype: str
        """
        return self._SealType

    @SealType.setter
    def SealType(self, SealType):
        self._SealType = SealType

    @property
    def SealHorizontalText(self):
        """企业印章横向文字，最多可填8个汉字（可为空，默认为"电子签名专用章"）
        :rtype: str
        """
        return self._SealHorizontalText

    @SealHorizontalText.setter
    def SealHorizontalText(self, SealHorizontalText):
        self._SealHorizontalText = SealHorizontalText

    @property
    def OpenId(self):
        """机构在第三方的唯一标识，32位以内标识符
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def UseOpenId(self):
        """是否使用OpenId作为数据主键，如果为true，请确保OpenId在当前应用号唯一
        :rtype: bool
        """
        return self._UseOpenId

    @UseOpenId.setter
    def UseOpenId(self, UseOpenId):
        self._UseOpenId = UseOpenId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._OrganizationType = params.get("OrganizationType")
        self._LegalName = params.get("LegalName")
        self._LegalIdCardType = params.get("LegalIdCardType")
        self._LegalIdCardNumber = params.get("LegalIdCardNumber")
        self._VerifyClientIp = params.get("VerifyClientIp")
        self._Email = params.get("Email")
        self._IdCardFileType = params.get("IdCardFileType")
        self._BizLicenseFile = params.get("BizLicenseFile")
        self._BizLicenseFileName = params.get("BizLicenseFileName")
        self._LegalMobile = params.get("LegalMobile")
        self._ContactName = params.get("ContactName")
        self._VerifyServerIp = params.get("VerifyServerIp")
        if params.get("ContactAddress") is not None:
            self._ContactAddress = Address()
            self._ContactAddress._deserialize(params.get("ContactAddress"))
        self._SealName = params.get("SealName")
        self._SealType = params.get("SealType")
        self._SealHorizontalText = params.get("SealHorizontalText")
        self._OpenId = params.get("OpenId")
        self._UseOpenId = params.get("UseOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubOrganizationAndSealResponse(AbstractModel):
    """CreateSubOrganizationAndSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubOrganizationId: 子机构在电子文件签署平台唯一标识
        :type SubOrganizationId: str
        :param _SealId: 电子印章ID
        :type SealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubOrganizationId = None
        self._SealId = None
        self._RequestId = None

    @property
    def SubOrganizationId(self):
        """子机构在电子文件签署平台唯一标识
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def SealId(self):
        """电子印章ID
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._SealId = params.get("SealId")
        self._RequestId = params.get("RequestId")


class CreateSubOrganizationRequest(AbstractModel):
    """CreateSubOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _IdCardType: 机构证件号码类型可选值：
1. USCC - 统一社会信用代码
2. BIZREGISTNO - 营业执照注册号
        :type IdCardType: str
        :param _IdCardNumber: 机构证件号码
        :type IdCardNumber: str
        :param _OrganizationType: 机构类型可选值：
1. ENTERPRISE - 企业
2. INDIVIDUALBIZ - 个体工商户
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :type OrganizationType: str
        :param _LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param _LegalIdCardType: 机构法人/经营者证件类型可选值：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type LegalIdCardType: str
        :param _LegalIdCardNumber: 机构法人/经营者证件号码；
OrganizationType 为 ENTERPRISE时，INDIVIDUALBIZ 时必填，其他情况选填
        :type LegalIdCardNumber: str
        :param _Name: 机构名称全称
        :type Name: str
        :param _OpenId: 机构在第三方的唯一标识，32位以内标识符
        :type OpenId: str
        :param _UseOpenId: 是否使用OpenId作为数据主键，如果为true，请确保OpenId在当前应用号唯一
        :type UseOpenId: bool
        :param _IdCardFileType: 机构证件文件类型可选值：
1. USCCFILE - 统一社会信用代码证书
2. LICENSEFILE - 营业执照
        :type IdCardFileType: str
        :param _BizLicenseFile: 机构证件照片文件，base64编码，支持jpg、jpeg、png格式
        :type BizLicenseFile: str
        :param _BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param _LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param _ContactName: 组织联系人姓名
        :type ContactName: str
        :param _VerifyClientIp: 实名认证的客户端IP
        :type VerifyClientIp: str
        :param _VerifyServerIp: 实名认证的服务器IP
        :type VerifyServerIp: str
        :param _ContactAddress: 企业联系地址
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        :param _Email: 机构电子邮箱
        :type Email: str
        """
        self._Caller = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._OrganizationType = None
        self._LegalName = None
        self._LegalIdCardType = None
        self._LegalIdCardNumber = None
        self._Name = None
        self._OpenId = None
        self._UseOpenId = None
        self._IdCardFileType = None
        self._BizLicenseFile = None
        self._BizLicenseFileName = None
        self._LegalMobile = None
        self._ContactName = None
        self._VerifyClientIp = None
        self._VerifyServerIp = None
        self._ContactAddress = None
        self._Email = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def IdCardType(self):
        """机构证件号码类型可选值：
1. USCC - 统一社会信用代码
2. BIZREGISTNO - 营业执照注册号
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """机构证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def OrganizationType(self):
        """机构类型可选值：
1. ENTERPRISE - 企业
2. INDIVIDUALBIZ - 个体工商户
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :rtype: str
        """
        return self._OrganizationType

    @OrganizationType.setter
    def OrganizationType(self, OrganizationType):
        self._OrganizationType = OrganizationType

    @property
    def LegalName(self):
        """机构法人/经营者姓名
        :rtype: str
        """
        return self._LegalName

    @LegalName.setter
    def LegalName(self, LegalName):
        self._LegalName = LegalName

    @property
    def LegalIdCardType(self):
        """机构法人/经营者证件类型可选值：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :rtype: str
        """
        return self._LegalIdCardType

    @LegalIdCardType.setter
    def LegalIdCardType(self, LegalIdCardType):
        self._LegalIdCardType = LegalIdCardType

    @property
    def LegalIdCardNumber(self):
        """机构法人/经营者证件号码；
OrganizationType 为 ENTERPRISE时，INDIVIDUALBIZ 时必填，其他情况选填
        :rtype: str
        """
        return self._LegalIdCardNumber

    @LegalIdCardNumber.setter
    def LegalIdCardNumber(self, LegalIdCardNumber):
        self._LegalIdCardNumber = LegalIdCardNumber

    @property
    def Name(self):
        """机构名称全称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OpenId(self):
        """机构在第三方的唯一标识，32位以内标识符
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def UseOpenId(self):
        """是否使用OpenId作为数据主键，如果为true，请确保OpenId在当前应用号唯一
        :rtype: bool
        """
        return self._UseOpenId

    @UseOpenId.setter
    def UseOpenId(self, UseOpenId):
        self._UseOpenId = UseOpenId

    @property
    def IdCardFileType(self):
        """机构证件文件类型可选值：
1. USCCFILE - 统一社会信用代码证书
2. LICENSEFILE - 营业执照
        :rtype: str
        """
        return self._IdCardFileType

    @IdCardFileType.setter
    def IdCardFileType(self, IdCardFileType):
        self._IdCardFileType = IdCardFileType

    @property
    def BizLicenseFile(self):
        """机构证件照片文件，base64编码，支持jpg、jpeg、png格式
        :rtype: str
        """
        return self._BizLicenseFile

    @BizLicenseFile.setter
    def BizLicenseFile(self, BizLicenseFile):
        self._BizLicenseFile = BizLicenseFile

    @property
    def BizLicenseFileName(self):
        """机构证件照片文件名
        :rtype: str
        """
        return self._BizLicenseFileName

    @BizLicenseFileName.setter
    def BizLicenseFileName(self, BizLicenseFileName):
        self._BizLicenseFileName = BizLicenseFileName

    @property
    def LegalMobile(self):
        """机构法人/经营者/联系人手机号码
        :rtype: str
        """
        return self._LegalMobile

    @LegalMobile.setter
    def LegalMobile(self, LegalMobile):
        self._LegalMobile = LegalMobile

    @property
    def ContactName(self):
        """组织联系人姓名
        :rtype: str
        """
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def VerifyClientIp(self):
        """实名认证的客户端IP
        :rtype: str
        """
        return self._VerifyClientIp

    @VerifyClientIp.setter
    def VerifyClientIp(self, VerifyClientIp):
        self._VerifyClientIp = VerifyClientIp

    @property
    def VerifyServerIp(self):
        """实名认证的服务器IP
        :rtype: str
        """
        return self._VerifyServerIp

    @VerifyServerIp.setter
    def VerifyServerIp(self, VerifyServerIp):
        self._VerifyServerIp = VerifyServerIp

    @property
    def ContactAddress(self):
        """企业联系地址
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Address`
        """
        return self._ContactAddress

    @ContactAddress.setter
    def ContactAddress(self, ContactAddress):
        self._ContactAddress = ContactAddress

    @property
    def Email(self):
        """机构电子邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._OrganizationType = params.get("OrganizationType")
        self._LegalName = params.get("LegalName")
        self._LegalIdCardType = params.get("LegalIdCardType")
        self._LegalIdCardNumber = params.get("LegalIdCardNumber")
        self._Name = params.get("Name")
        self._OpenId = params.get("OpenId")
        self._UseOpenId = params.get("UseOpenId")
        self._IdCardFileType = params.get("IdCardFileType")
        self._BizLicenseFile = params.get("BizLicenseFile")
        self._BizLicenseFileName = params.get("BizLicenseFileName")
        self._LegalMobile = params.get("LegalMobile")
        self._ContactName = params.get("ContactName")
        self._VerifyClientIp = params.get("VerifyClientIp")
        self._VerifyServerIp = params.get("VerifyServerIp")
        if params.get("ContactAddress") is not None:
            self._ContactAddress = Address()
            self._ContactAddress._deserialize(params.get("ContactAddress"))
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubOrganizationResponse(AbstractModel):
    """CreateSubOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubOrganizationId: 子机构ID
        :type SubOrganizationId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubOrganizationId = None
        self._RequestId = None

    @property
    def SubOrganizationId(self):
        """子机构ID
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._RequestId = params.get("RequestId")


class CreateUserAndSealRequest(AbstractModel):
    """CreateUserAndSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _OpenId: 第三方平台唯一标识，要求应用内OpenId唯一
        :type OpenId: str
        :param _Name: 用户姓名
        :type Name: str
        :param _IdCardType: 用户证件类型：
1. ID_CARD - 居民身份证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type IdCardType: str
        :param _IdCardNumber: 用户证件号
        :type IdCardNumber: str
        :param _SourceIp: 请求生成个人印章的客户端IP
        :type SourceIp: str
        :param _Mobile: 用户手机号码，不要求唯一
        :type Mobile: str
        :param _Email: 用户邮箱，不要求唯一
        :type Email: str
        :param _SealName: 默认印章名称
        :type SealName: str
        :param _UseOpenId: 是否以OpenId作为UserId (为true时将直接以OpenId生成腾讯电子签平台的UserId)
        :type UseOpenId: bool
        """
        self._Caller = None
        self._OpenId = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._SourceIp = None
        self._Mobile = None
        self._Email = None
        self._SealName = None
        self._UseOpenId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def OpenId(self):
        """第三方平台唯一标识，要求应用内OpenId唯一
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Name(self):
        """用户姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        """用户证件类型：
1. ID_CARD - 居民身份证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """用户证件号
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def SourceIp(self):
        """请求生成个人印章的客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def Mobile(self):
        """用户手机号码，不要求唯一
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        """用户邮箱，不要求唯一
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def SealName(self):
        """默认印章名称
        :rtype: str
        """
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def UseOpenId(self):
        """是否以OpenId作为UserId (为true时将直接以OpenId生成腾讯电子签平台的UserId)
        :rtype: bool
        """
        return self._UseOpenId

    @UseOpenId.setter
    def UseOpenId(self, UseOpenId):
        self._UseOpenId = UseOpenId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._OpenId = params.get("OpenId")
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._SourceIp = params.get("SourceIp")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._SealName = params.get("SealName")
        self._UseOpenId = params.get("UseOpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserAndSealResponse(AbstractModel):
    """CreateUserAndSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户唯一标识，按应用号隔离
        :type UserId: str
        :param _SealId: 默认印章ID
        :type SealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._SealId = None
        self._RequestId = None

    @property
    def UserId(self):
        """用户唯一标识，按应用号隔离
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SealId(self):
        """默认印章ID
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._SealId = params.get("SealId")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _OpenId: 第三方平台唯一标识；要求应用内OpenId唯一; len<=32
        :type OpenId: str
        :param _Name: 用户姓名
        :type Name: str
        :param _IdCardType: 用户证件类型：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :type IdCardType: str
        :param _IdCardNumber: 用户证件号
        :type IdCardNumber: str
        :param _UseOpenId: 是否以OpenId作为UserId (为true时将直接以OpenId生成腾讯电子签平台的UserId)
        :type UseOpenId: bool
        :param _Email: 用户邮箱，不要求唯一
        :type Email: str
        :param _Mobile: 用户手机号码，不要求唯一
        :type Mobile: str
        """
        self._Caller = None
        self._OpenId = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._UseOpenId = None
        self._Email = None
        self._Mobile = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def OpenId(self):
        """第三方平台唯一标识；要求应用内OpenId唯一; len<=32
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Name(self):
        """用户姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        """用户证件类型：
1. ID_CARD - 居民身份证
2. PASSPORT - 护照
3. MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证
4. MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证
5. HOUSEHOLD_REGISTER - 户口本
6. TEMP_ID_CARD - 临时居民身份证
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """用户证件号
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def UseOpenId(self):
        """是否以OpenId作为UserId (为true时将直接以OpenId生成腾讯电子签平台的UserId)
        :rtype: bool
        """
        return self._UseOpenId

    @UseOpenId.setter
    def UseOpenId(self, UseOpenId):
        self._UseOpenId = UseOpenId

    @property
    def Email(self):
        """用户邮箱，不要求唯一
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Mobile(self):
        """用户手机号码，不要求唯一
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._OpenId = params.get("OpenId")
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._UseOpenId = params.get("UseOpenId")
        self._Email = params.get("Email")
        self._Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID，按应用号隔离
        :type UserId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        """用户ID，按应用号隔离
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class CustomFileIdMap(AbstractModel):
    """<自定义Id,文件id>映射对象

    """

    def __init__(self):
        r"""
        :param _CustomId: 用户自定义ID
        :type CustomId: str
        :param _FileId: 文件id
        :type FileId: str
        """
        self._CustomId = None
        self._FileId = None

    @property
    def CustomId(self):
        """用户自定义ID
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def FileId(self):
        """文件id
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomFlowIdMap(AbstractModel):
    """自定义流程id映射关系

    """

    def __init__(self):
        r"""
        :param _CustomId: 自定义id
        :type CustomId: str
        :param _FlowId: 流程id
        :type FlowId: str
        """
        self._CustomId = None
        self._FlowId = None

    @property
    def CustomId(self):
        """自定义id
        :rtype: str
        """
        return self._CustomId

    @CustomId.setter
    def CustomId(self, CustomId):
        self._CustomId = CustomId

    @property
    def FlowId(self):
        """流程id
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._CustomId = params.get("CustomId")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSealRequest(AbstractModel):
    """DeleteSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _SealId: 印章ID
        :type SealId: str
        :param _SourceIp: 请求删除印章的客户端IP
        :type SourceIp: str
        :param _UserId: 用户唯一标识，默认为空时删除企业印章，如非空则删除个人印章
        :type UserId: str
        """
        self._Caller = None
        self._SealId = None
        self._SourceIp = None
        self._UserId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def SealId(self):
        """印章ID
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SourceIp(self):
        """请求删除印章的客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def UserId(self):
        """用户唯一标识，默认为空时删除企业印章，如非空则删除个人印章
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._SealId = params.get("SealId")
        self._SourceIp = params.get("SourceIp")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSealResponse(AbstractModel):
    """DeleteSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCatalogApproversRequest(AbstractModel):
    """DescribeCatalogApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _CatalogId: 目录ID
        :type CatalogId: str
        :param _UserId: 查询指定用户是否为参与者,为空表示查询所有参与者
        :type UserId: str
        """
        self._Caller = None
        self._CatalogId = None
        self._UserId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def CatalogId(self):
        """目录ID
        :rtype: str
        """
        return self._CatalogId

    @CatalogId.setter
    def CatalogId(self, CatalogId):
        self._CatalogId = CatalogId

    @property
    def UserId(self):
        """查询指定用户是否为参与者,为空表示查询所有参与者
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._CatalogId = params.get("CatalogId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCatalogApproversResponse(AbstractModel):
    """DescribeCatalogApprovers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Approvers: 参与者列表
        :type Approvers: list of CatalogApprovers
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Approvers = None
        self._RequestId = None

    @property
    def Approvers(self):
        """参与者列表
        :rtype: list of CatalogApprovers
        """
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = CatalogApprovers()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCatalogSignComponentsRequest(AbstractModel):
    """DescribeCatalogSignComponents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _CatalogId: 目录ID
        :type CatalogId: str
        """
        self._Caller = None
        self._CatalogId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def CatalogId(self):
        """目录ID
        :rtype: str
        """
        return self._CatalogId

    @CatalogId.setter
    def CatalogId(self, CatalogId):
        self._CatalogId = CatalogId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._CatalogId = params.get("CatalogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCatalogSignComponentsResponse(AbstractModel):
    """DescribeCatalogSignComponents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignComponents: 签署区列表
        :type SignComponents: list of CatalogComponents
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignComponents = None
        self._RequestId = None

    @property
    def SignComponents(self):
        """签署区列表
        :rtype: list of CatalogComponents
        """
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = CatalogComponents()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomFlowIdsByFlowIdRequest(AbstractModel):
    """DescribeCustomFlowIdsByFlowId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowIds: 流程 id 列表，最多同时查询 10 个流程 id
        :type FlowIds: list of str
        """
        self._Caller = None
        self._FlowIds = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowIds(self):
        """流程 id 列表，最多同时查询 10 个流程 id
        :rtype: list of str
        """
        return self._FlowIds

    @FlowIds.setter
    def FlowIds(self, FlowIds):
        self._FlowIds = FlowIds


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowIds = params.get("FlowIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomFlowIdsByFlowIdResponse(AbstractModel):
    """DescribeCustomFlowIdsByFlowId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomIdList: 自定义流程 id 映射列表
        :type CustomIdList: list of CustomFlowIdMap
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomIdList = None
        self._RequestId = None

    @property
    def CustomIdList(self):
        """自定义流程 id 映射列表
        :rtype: list of CustomFlowIdMap
        """
        return self._CustomIdList

    @CustomIdList.setter
    def CustomIdList(self, CustomIdList):
        self._CustomIdList = CustomIdList

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomIdList") is not None:
            self._CustomIdList = []
            for item in params.get("CustomIdList"):
                obj = CustomFlowIdMap()
                obj._deserialize(item)
                self._CustomIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCustomFlowIdsRequest(AbstractModel):
    """DescribeCustomFlowIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _CustomIds: 自定义 id 列表，最多同时查询 10 个自定义 id
        :type CustomIds: list of str
        """
        self._Caller = None
        self._CustomIds = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def CustomIds(self):
        """自定义 id 列表，最多同时查询 10 个自定义 id
        :rtype: list of str
        """
        return self._CustomIds

    @CustomIds.setter
    def CustomIds(self, CustomIds):
        self._CustomIds = CustomIds


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._CustomIds = params.get("CustomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomFlowIdsResponse(AbstractModel):
    """DescribeCustomFlowIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomIdList: 自定义流程 id 映射列表
        :type CustomIdList: list of CustomFlowIdMap
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomIdList = None
        self._RequestId = None

    @property
    def CustomIdList(self):
        """自定义流程 id 映射列表
        :rtype: list of CustomFlowIdMap
        """
        return self._CustomIdList

    @CustomIdList.setter
    def CustomIdList(self, CustomIdList):
        self._CustomIdList = CustomIdList

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomIdList") is not None:
            self._CustomIdList = []
            for item in params.get("CustomIdList"):
                obj = CustomFlowIdMap()
                obj._deserialize(item)
                self._CustomIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFaceIdPhotosRequest(AbstractModel):
    """DescribeFaceIdPhotos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _WbAppId: 慧眼业务ID
        :type WbAppId: str
        :param _OrderNumbers: 订单号(orderNo); 限制在3个或以内
        :type OrderNumbers: list of str
        """
        self._Caller = None
        self._WbAppId = None
        self._OrderNumbers = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def WbAppId(self):
        """慧眼业务ID
        :rtype: str
        """
        return self._WbAppId

    @WbAppId.setter
    def WbAppId(self, WbAppId):
        self._WbAppId = WbAppId

    @property
    def OrderNumbers(self):
        """订单号(orderNo); 限制在3个或以内
        :rtype: list of str
        """
        return self._OrderNumbers

    @OrderNumbers.setter
    def OrderNumbers(self, OrderNumbers):
        self._OrderNumbers = OrderNumbers


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._WbAppId = params.get("WbAppId")
        self._OrderNumbers = params.get("OrderNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFaceIdPhotosResponse(AbstractModel):
    """DescribeFaceIdPhotos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Photos: 照片信息列表
        :type Photos: list of FaceIdPhoto
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Photos = None
        self._RequestId = None

    @property
    def Photos(self):
        """照片信息列表
        :rtype: list of FaceIdPhoto
        """
        return self._Photos

    @Photos.setter
    def Photos(self, Photos):
        self._Photos = Photos

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Photos") is not None:
            self._Photos = []
            for item in params.get("Photos"):
                obj = FaceIdPhoto()
                obj._deserialize(item)
                self._Photos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFaceIdResultsRequest(AbstractModel):
    """DescribeFaceIdResults请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _WbAppId: 慧眼业务ID
        :type WbAppId: str
        :param _OrderNumbers: 订单号(orderNo); 限制在3个或以内
        :type OrderNumbers: list of str
        :param _FileType: 1:视频+照片,2:照片,3:视频,0（或其他数字）:无; 可选
        :type FileType: int
        """
        self._Caller = None
        self._WbAppId = None
        self._OrderNumbers = None
        self._FileType = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def WbAppId(self):
        """慧眼业务ID
        :rtype: str
        """
        return self._WbAppId

    @WbAppId.setter
    def WbAppId(self, WbAppId):
        self._WbAppId = WbAppId

    @property
    def OrderNumbers(self):
        """订单号(orderNo); 限制在3个或以内
        :rtype: list of str
        """
        return self._OrderNumbers

    @OrderNumbers.setter
    def OrderNumbers(self, OrderNumbers):
        self._OrderNumbers = OrderNumbers

    @property
    def FileType(self):
        """1:视频+照片,2:照片,3:视频,0（或其他数字）:无; 可选
        :rtype: int
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._WbAppId = params.get("WbAppId")
        self._OrderNumbers = params.get("OrderNumbers")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFaceIdResultsResponse(AbstractModel):
    """DescribeFaceIdResults返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 核身结果列表
        :type Results: list of FaceIdResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        """核身结果列表
        :rtype: list of FaceIdResult
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = FaceIdResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileIdsByCustomIdsRequest(AbstractModel):
    """DescribeFileIdsByCustomIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息, OrganizationId必填
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _CustomIds: 用户自定义ID
        :type CustomIds: list of str
        """
        self._Caller = None
        self._CustomIds = None

    @property
    def Caller(self):
        """调用方信息, OrganizationId必填
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def CustomIds(self):
        """用户自定义ID
        :rtype: list of str
        """
        return self._CustomIds

    @CustomIds.setter
    def CustomIds(self, CustomIds):
        self._CustomIds = CustomIds


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._CustomIds = params.get("CustomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileIdsByCustomIdsResponse(AbstractModel):
    """DescribeFileIdsByCustomIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomIdList: <自定义Id,文件id>数组
        :type CustomIdList: list of CustomFileIdMap
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomIdList = None
        self._RequestId = None

    @property
    def CustomIdList(self):
        """<自定义Id,文件id>数组
        :rtype: list of CustomFileIdMap
        """
        return self._CustomIdList

    @CustomIdList.setter
    def CustomIdList(self, CustomIdList):
        self._CustomIdList = CustomIdList

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CustomIdList") is not None:
            self._CustomIdList = []
            for item in params.get("CustomIdList"):
                obj = CustomFileIdMap()
                obj._deserialize(item)
                self._CustomIdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFileUrlsRequest(AbstractModel):
    """DescribeFileUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _BusinessIds: 业务编号数组，如模板编号、文档编号、印章编号、流程编号、目录编号
        :type BusinessIds: list of str
        :param _BusinessType: 业务类型：
1. TEMPLATE - 模板
2. SEAL - 印章
3. FLOW - 流程
4.CATALOG - 目录
        :type BusinessType: str
        :param _FileName: 下载后的文件命名，只有FileType为“ZIP”时生效
        :type FileName: str
        :param _ResourceOffset: 单个业务ID多个资源情况下，指定资源起始偏移量
        :type ResourceOffset: int
        :param _ResourceLimit: 单个业务ID多个资源情况下，指定资源数量
        :type ResourceLimit: int
        :param _FileType: 文件类型，支持"JPG", "PDF","ZIP"等，默认为上传的文件类型
        :type FileType: str
        """
        self._Caller = None
        self._BusinessIds = None
        self._BusinessType = None
        self._FileName = None
        self._ResourceOffset = None
        self._ResourceLimit = None
        self._FileType = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def BusinessIds(self):
        """业务编号数组，如模板编号、文档编号、印章编号、流程编号、目录编号
        :rtype: list of str
        """
        return self._BusinessIds

    @BusinessIds.setter
    def BusinessIds(self, BusinessIds):
        self._BusinessIds = BusinessIds

    @property
    def BusinessType(self):
        """业务类型：
1. TEMPLATE - 模板
2. SEAL - 印章
3. FLOW - 流程
4.CATALOG - 目录
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def FileName(self):
        """下载后的文件命名，只有FileType为“ZIP”时生效
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ResourceOffset(self):
        """单个业务ID多个资源情况下，指定资源起始偏移量
        :rtype: int
        """
        return self._ResourceOffset

    @ResourceOffset.setter
    def ResourceOffset(self, ResourceOffset):
        self._ResourceOffset = ResourceOffset

    @property
    def ResourceLimit(self):
        """单个业务ID多个资源情况下，指定资源数量
        :rtype: int
        """
        return self._ResourceLimit

    @ResourceLimit.setter
    def ResourceLimit(self, ResourceLimit):
        self._ResourceLimit = ResourceLimit

    @property
    def FileType(self):
        """文件类型，支持"JPG", "PDF","ZIP"等，默认为上传的文件类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._BusinessIds = params.get("BusinessIds")
        self._BusinessType = params.get("BusinessType")
        self._FileName = params.get("FileName")
        self._ResourceOffset = params.get("ResourceOffset")
        self._ResourceLimit = params.get("ResourceLimit")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileUrlsResponse(AbstractModel):
    """DescribeFileUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileUrls: 文件下载URL数组
        :type FileUrls: list of FileUrl
        :param _TotalCount: URL数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileUrls = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FileUrls(self):
        """文件下载URL数组
        :rtype: list of FileUrl
        """
        return self._FileUrls

    @FileUrls.setter
    def FileUrls(self, FileUrls):
        self._FileUrls = FileUrls

    @property
    def TotalCount(self):
        """URL数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileUrls") is not None:
            self._FileUrls = []
            for item in params.get("FileUrls"):
                obj = FileUrl()
                obj._deserialize(item)
                self._FileUrls.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFlowApproversRequest(AbstractModel):
    """DescribeFlowApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 需要查询的流程ID
        :type FlowId: str
        :param _UserId: 需要查询的用户ID，为空则默认查询所有用户信息
        :type UserId: str
        :param _SignId: 需要查询的签署ID，为空则不按签署ID过滤
        :type SignId: str
        """
        self._Caller = None
        self._FlowId = None
        self._UserId = None
        self._SignId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """需要查询的流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def UserId(self):
        """需要查询的用户ID，为空则默认查询所有用户信息
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SignId(self):
        """需要查询的签署ID，为空则不按签署ID过滤
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        self._UserId = params.get("UserId")
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowApproversResponse(AbstractModel):
    """DescribeFlowApprovers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程编号
        :type FlowId: str
        :param _Approvers: 流程参与者信息
        :type Approvers: list of FlowApproverInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._Approvers = None
        self._RequestId = None

    @property
    def FlowId(self):
        """流程编号
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Approvers(self):
        """流程参与者信息
        :rtype: list of FlowApproverInfo
        """
        return self._Approvers

    @Approvers.setter
    def Approvers(self, Approvers):
        self._Approvers = Approvers

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self._Approvers = []
            for item in params.get("Approvers"):
                obj = FlowApproverInfo()
                obj._deserialize(item)
                self._Approvers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowFilesRequest(AbstractModel):
    """DescribeFlowFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息; 必选
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 需要查询的流程ID
        :type FlowId: str
        """
        self._Caller = None
        self._FlowId = None

    @property
    def Caller(self):
        """调用方信息; 必选
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """需要查询的流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowFilesResponse(AbstractModel):
    """DescribeFlowFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程编号
        :type FlowId: str
        :param _FlowFileInfos: 流程文件列表
        :type FlowFileInfos: list of FlowFileInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._FlowFileInfos = None
        self._RequestId = None

    @property
    def FlowId(self):
        """流程编号
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowFileInfos(self):
        """流程文件列表
        :rtype: list of FlowFileInfo
        """
        return self._FlowFileInfos

    @FlowFileInfos.setter
    def FlowFileInfos(self, FlowFileInfos):
        self._FlowFileInfos = FlowFileInfos

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("FlowFileInfos") is not None:
            self._FlowFileInfos = []
            for item in params.get("FlowFileInfos"):
                obj = FlowFileInfo()
                obj._deserialize(item)
                self._FlowFileInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 需要查询的流程ID
        :type FlowId: str
        """
        self._Caller = None
        self._FlowId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """需要查询的流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Creator: 流程创建者信息
        :type Creator: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 流程编号
        :type FlowId: str
        :param _FlowName: 流程名称
        :type FlowName: str
        :param _FlowDescription: 流程描述
        :type FlowDescription: str
        :param _FlowType: 流程的类型: ”劳务合同“,”租赁合同“,”销售合同“,”其他“
        :type FlowType: str
        :param _FlowStatus: 流程状态：
0-创建；
1-签署中；
2-拒签；
3-撤回；
4-签完存档完成；
5-已过期；
6-已销毁
7-签署完成未归档
        :type FlowStatus: int
        :param _CreatedOn: 流程创建时间
        :type CreatedOn: int
        :param _UpdatedOn: 流程完成时间
        :type UpdatedOn: int
        :param _Deadline: 流程截止日期
        :type Deadline: int
        :param _CallbackUrl: 回调地址
        :type CallbackUrl: str
        :param _FlowMessage: 流程中止原因
        :type FlowMessage: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Creator = None
        self._FlowId = None
        self._FlowName = None
        self._FlowDescription = None
        self._FlowType = None
        self._FlowStatus = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Deadline = None
        self._CallbackUrl = None
        self._FlowMessage = None
        self._RequestId = None

    @property
    def Creator(self):
        """流程创建者信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def FlowId(self):
        """流程编号
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        """流程名称
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowDescription(self):
        """流程描述
        :rtype: str
        """
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def FlowType(self):
        """流程的类型: ”劳务合同“,”租赁合同“,”销售合同“,”其他“
        :rtype: str
        """
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def FlowStatus(self):
        """流程状态：
0-创建；
1-签署中；
2-拒签；
3-撤回；
4-签完存档完成；
5-已过期；
6-已销毁
7-签署完成未归档
        :rtype: int
        """
        return self._FlowStatus

    @FlowStatus.setter
    def FlowStatus(self, FlowStatus):
        self._FlowStatus = FlowStatus

    @property
    def CreatedOn(self):
        """流程创建时间
        :rtype: int
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """流程完成时间
        :rtype: int
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Deadline(self):
        """流程截止日期
        :rtype: int
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def CallbackUrl(self):
        """回调地址
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def FlowMessage(self):
        """流程中止原因
        :rtype: str
        """
        return self._FlowMessage

    @FlowMessage.setter
    def FlowMessage(self, FlowMessage):
        self._FlowMessage = FlowMessage

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Creator") is not None:
            self._Creator = Caller()
            self._Creator._deserialize(params.get("Creator"))
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        self._FlowDescription = params.get("FlowDescription")
        self._FlowType = params.get("FlowType")
        self._FlowStatus = params.get("FlowStatus")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Deadline = params.get("Deadline")
        self._CallbackUrl = params.get("CallbackUrl")
        self._FlowMessage = params.get("FlowMessage")
        self._RequestId = params.get("RequestId")


class DescribeSealsRequest(AbstractModel):
    """DescribeSeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _SealIds: 印章ID列表
        :type SealIds: list of str
        :param _UserId: 用户唯一标识
        :type UserId: str
        """
        self._Caller = None
        self._SealIds = None
        self._UserId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def SealIds(self):
        """印章ID列表
        :rtype: list of str
        """
        return self._SealIds

    @SealIds.setter
    def SealIds(self, SealIds):
        self._SealIds = SealIds

    @property
    def UserId(self):
        """用户唯一标识
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._SealIds = params.get("SealIds")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSealsResponse(AbstractModel):
    """DescribeSeals返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Seals: 印章信息
        :type Seals: list of Seal
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Seals = None
        self._RequestId = None

    @property
    def Seals(self):
        """印章信息
        :rtype: list of Seal
        """
        return self._Seals

    @Seals.setter
    def Seals(self, Seals):
        self._Seals = Seals

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Seals") is not None:
            self._Seals = []
            for item in params.get("Seals"):
                obj = Seal()
                obj._deserialize(item)
                self._Seals.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubOrganizationsRequest(AbstractModel):
    """DescribeSubOrganizations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _SubOrganizationIds: 子机构ID数组
        :type SubOrganizationIds: list of str
        """
        self._Caller = None
        self._SubOrganizationIds = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def SubOrganizationIds(self):
        """子机构ID数组
        :rtype: list of str
        """
        return self._SubOrganizationIds

    @SubOrganizationIds.setter
    def SubOrganizationIds(self, SubOrganizationIds):
        self._SubOrganizationIds = SubOrganizationIds


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._SubOrganizationIds = params.get("SubOrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubOrganizationsResponse(AbstractModel):
    """DescribeSubOrganizations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubOrganizationInfos: 子机构信息列表
        :type SubOrganizationInfos: list of SubOrganizationDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubOrganizationInfos = None
        self._RequestId = None

    @property
    def SubOrganizationInfos(self):
        """子机构信息列表
        :rtype: list of SubOrganizationDetail
        """
        return self._SubOrganizationInfos

    @SubOrganizationInfos.setter
    def SubOrganizationInfos(self, SubOrganizationInfos):
        self._SubOrganizationInfos = SubOrganizationInfos

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SubOrganizationInfos") is not None:
            self._SubOrganizationInfos = []
            for item in params.get("SubOrganizationInfos"):
                obj = SubOrganizationDetail()
                obj._deserialize(item)
                self._SubOrganizationInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsersRequest(AbstractModel):
    """DescribeUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _UserIds: UserId列表，最多支持100个UserId
        :type UserIds: list of str
        """
        self._Caller = None
        self._UserIds = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def UserIds(self):
        """UserId列表，最多支持100个UserId
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsersResponse(AbstractModel):
    """DescribeUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 用户信息查询结果
        :type Users: list of UserDescribe
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        """用户信息查询结果
        :rtype: list of UserDescribe
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserDescribe()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyFlowFileRequest(AbstractModel):
    """DestroyFlowFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 流程ID
        :type FlowId: str
        """
        self._Caller = None
        self._FlowId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyFlowFileResponse(AbstractModel):
    """DestroyFlowFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FaceIdPhoto(AbstractModel):
    """此结构体 (FaceIdPhoto) 用于描述慧眼人脸核身照片信息。

    """

    def __init__(self):
        r"""
        :param _Result: 核身结果：
0 - 通过；
1 - 未通过
        :type Result: int
        :param _Description: 核身失败描述
        :type Description: str
        :param _Photo: 照片数据 (base64编码, 一般为JPG或PNG)
        :type Photo: str
        :param _OrderNumber: 订单号 (orderNo)
        :type OrderNumber: str
        """
        self._Result = None
        self._Description = None
        self._Photo = None
        self._OrderNumber = None

    @property
    def Result(self):
        """核身结果：
0 - 通过；
1 - 未通过
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """核身失败描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Photo(self):
        """照片数据 (base64编码, 一般为JPG或PNG)
        :rtype: str
        """
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

    @property
    def OrderNumber(self):
        """订单号 (orderNo)
        :rtype: str
        """
        return self._OrderNumber

    @OrderNumber.setter
    def OrderNumber(self, OrderNumber):
        self._OrderNumber = OrderNumber


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._Photo = params.get("Photo")
        self._OrderNumber = params.get("OrderNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceIdResult(AbstractModel):
    """此结构体 (FaceIdResult) 用于描述慧眼人脸核身结果。

    """

    def __init__(self):
        r"""
        :param _Result: 核身结果：
0 - 通过；
1 - 未通过
        :type Result: int
        :param _Description: 核身失败描述
        :type Description: str
        :param _OrderNumber: 订单号 (orderNo)
        :type OrderNumber: str
        :param _Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _IdCardType: 身份证件类型： 
ID_CARD - 居民身份证
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardType: str
        :param _IdCardNumber: 身份证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardNumber: str
        :param _LiveRate: 活体检测得分 (百分制)
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveRate: int
        :param _Similarity: 人脸检测得分 (百分制)
注意：此字段可能返回 null，表示取不到有效值。
        :type Similarity: float
        :param _OccurredTime: 刷脸时间 (UNIX时间戳)
注意：此字段可能返回 null，表示取不到有效值。
        :type OccurredTime: int
        :param _Photo: 照片数据 (base64编码, 一般为JPG或PNG)
注意：此字段可能返回 null，表示取不到有效值。
        :type Photo: str
        :param _Video: 视频数据 (base64编码, 一般为MP4)
注意：此字段可能返回 null，表示取不到有效值。
        :type Video: str
        """
        self._Result = None
        self._Description = None
        self._OrderNumber = None
        self._Name = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._LiveRate = None
        self._Similarity = None
        self._OccurredTime = None
        self._Photo = None
        self._Video = None

    @property
    def Result(self):
        """核身结果：
0 - 通过；
1 - 未通过
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Description(self):
        """核身失败描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OrderNumber(self):
        """订单号 (orderNo)
        :rtype: str
        """
        return self._OrderNumber

    @OrderNumber.setter
    def OrderNumber(self, OrderNumber):
        self._OrderNumber = OrderNumber

    @property
    def Name(self):
        """姓名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdCardType(self):
        """身份证件类型： 
ID_CARD - 居民身份证
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """身份证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def LiveRate(self):
        """活体检测得分 (百分制)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LiveRate

    @LiveRate.setter
    def LiveRate(self, LiveRate):
        self._LiveRate = LiveRate

    @property
    def Similarity(self):
        """人脸检测得分 (百分制)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def OccurredTime(self):
        """刷脸时间 (UNIX时间戳)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OccurredTime

    @OccurredTime.setter
    def OccurredTime(self, OccurredTime):
        self._OccurredTime = OccurredTime

    @property
    def Photo(self):
        """照片数据 (base64编码, 一般为JPG或PNG)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Photo

    @Photo.setter
    def Photo(self, Photo):
        self._Photo = Photo

    @property
    def Video(self):
        """视频数据 (base64编码, 一般为MP4)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Description = params.get("Description")
        self._OrderNumber = params.get("OrderNumber")
        self._Name = params.get("Name")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._LiveRate = params.get("LiveRate")
        self._Similarity = params.get("Similarity")
        self._OccurredTime = params.get("OccurredTime")
        self._Photo = params.get("Photo")
        self._Video = params.get("Video")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileUrl(AbstractModel):
    """此结构体 (FileUrl) 用于描述下载文件的URL信息。

    """

    def __init__(self):
        r"""
        :param _Url: 下载文件的URL
        :type Url: str
        :param _Option: 下载文件的附加信息
        :type Option: str
        :param _Index: 下载文件所属的资源序号
        :type Index: int
        :param _FlowId: 目录业务下，文件对应的流程
        :type FlowId: str
        """
        self._Url = None
        self._Option = None
        self._Index = None
        self._FlowId = None

    @property
    def Url(self):
        """下载文件的URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Option(self):
        """下载文件的附加信息
        :rtype: str
        """
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def Index(self):
        """下载文件所属的资源序号
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def FlowId(self):
        """目录业务下，文件对应的流程
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Option = params.get("Option")
        self._Index = params.get("Index")
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverInfo(AbstractModel):
    """此结构体 (FlowApproverInfo) 用于描述流程参与者信息。

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _VerifyChannel: 认证方式：
WEIXINAPP - 微信小程序；
FACEID - 慧眼 (默认)；
VERIFYCODE - 验证码；
THIRD - 第三方 (暂不支持)
        :type VerifyChannel: list of str
        :param _ApproveStatus: 签署状态：
0 - 待签署；
1- 已签署；
2 - 拒绝；
3 - 过期未处理；
4 - 流程已撤回,
12-审核中,
13-审核驳回
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveStatus: int
        :param _ApproveMessage: 拒签/签署/审核驳回原因
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMessage: str
        :param _ApproveTime: 签约时间的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveTime: int
        :param _SubOrganizationId: 签署企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubOrganizationId: str
        :param _JumpUrl: 签署完成后跳转的URL
注意：此字段可能返回 null，表示取不到有效值。
        :type JumpUrl: str
        :param _ComponentSeals: 用户签署区ID到印章ID的映射集合
注意：此字段可能返回 null，表示取不到有效值。
        :type ComponentSeals: list of ComponentSeal
        :param _IsFullText: 签署前置条件：是否强制用户全文阅读，即阅读到待签署文档的最后一页。默认FALSE
        :type IsFullText: bool
        :param _PreReadTime: 签署前置条件：强制阅读时长，页面停留时长不足则不允许签署。默认不限制
        :type PreReadTime: int
        :param _Mobile: 签署人手机号，脱敏显示
        :type Mobile: str
        :param _Deadline: 签署链接截止时间，默认签署流程发起后7天失效
        :type Deadline: int
        :param _IsLastApprover: 是否为最后一个签署人, 若为最后一人，则其签署完成后自动归档
        :type IsLastApprover: bool
        :param _SmsTemplate: 短信模板
注意：此字段可能返回 null，表示取不到有效值。
        :type SmsTemplate: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        :param _IdCardNumber: 身份证号，脱敏显示
        :type IdCardNumber: str
        :param _Name: 用户姓名
        :type Name: str
        :param _CanOffLine: 是否支持线下核身
        :type CanOffLine: bool
        :param _IdCardType: 证件号码类型：ID_CARD - 身份证，PASSPORT - 护照，MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证; 暂不支持用于电子签自有平台实名认证，MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证; 暂不支持用于电子签自有平台实名认证，HOUSEHOLD_REGISTER - 户口本; 暂不支持用于电子签自有平台实名认证，TEMP_ID_CARD - 临时居民身份证; 暂不支持用于电子签自有平台实名认证
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardType: str
        :param _CallbackUrl: 签署回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        :param _SignId: 签署任务ID，标识每一次的流程发送
注意：此字段可能返回 null，表示取不到有效值。
        :type SignId: str
        """
        self._UserId = None
        self._VerifyChannel = None
        self._ApproveStatus = None
        self._ApproveMessage = None
        self._ApproveTime = None
        self._SubOrganizationId = None
        self._JumpUrl = None
        self._ComponentSeals = None
        self._IsFullText = None
        self._PreReadTime = None
        self._Mobile = None
        self._Deadline = None
        self._IsLastApprover = None
        self._SmsTemplate = None
        self._IdCardNumber = None
        self._Name = None
        self._CanOffLine = None
        self._IdCardType = None
        self._CallbackUrl = None
        self._SignId = None

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def VerifyChannel(self):
        """认证方式：
WEIXINAPP - 微信小程序；
FACEID - 慧眼 (默认)；
VERIFYCODE - 验证码；
THIRD - 第三方 (暂不支持)
        :rtype: list of str
        """
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def ApproveStatus(self):
        """签署状态：
0 - 待签署；
1- 已签署；
2 - 拒绝；
3 - 过期未处理；
4 - 流程已撤回,
12-审核中,
13-审核驳回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ApproveStatus

    @ApproveStatus.setter
    def ApproveStatus(self, ApproveStatus):
        self._ApproveStatus = ApproveStatus

    @property
    def ApproveMessage(self):
        """拒签/签署/审核驳回原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveMessage

    @ApproveMessage.setter
    def ApproveMessage(self, ApproveMessage):
        self._ApproveMessage = ApproveMessage

    @property
    def ApproveTime(self):
        """签约时间的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ApproveTime

    @ApproveTime.setter
    def ApproveTime(self, ApproveTime):
        self._ApproveTime = ApproveTime

    @property
    def SubOrganizationId(self):
        """签署企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def JumpUrl(self):
        """签署完成后跳转的URL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def ComponentSeals(self):
        """用户签署区ID到印章ID的映射集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ComponentSeal
        """
        return self._ComponentSeals

    @ComponentSeals.setter
    def ComponentSeals(self, ComponentSeals):
        self._ComponentSeals = ComponentSeals

    @property
    def IsFullText(self):
        """签署前置条件：是否强制用户全文阅读，即阅读到待签署文档的最后一页。默认FALSE
        :rtype: bool
        """
        return self._IsFullText

    @IsFullText.setter
    def IsFullText(self, IsFullText):
        self._IsFullText = IsFullText

    @property
    def PreReadTime(self):
        """签署前置条件：强制阅读时长，页面停留时长不足则不允许签署。默认不限制
        :rtype: int
        """
        return self._PreReadTime

    @PreReadTime.setter
    def PreReadTime(self, PreReadTime):
        self._PreReadTime = PreReadTime

    @property
    def Mobile(self):
        """签署人手机号，脱敏显示
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Deadline(self):
        """签署链接截止时间，默认签署流程发起后7天失效
        :rtype: int
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def IsLastApprover(self):
        """是否为最后一个签署人, 若为最后一人，则其签署完成后自动归档
        :rtype: bool
        """
        return self._IsLastApprover

    @IsLastApprover.setter
    def IsLastApprover(self, IsLastApprover):
        self._IsLastApprover = IsLastApprover

    @property
    def SmsTemplate(self):
        """短信模板
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        """
        return self._SmsTemplate

    @SmsTemplate.setter
    def SmsTemplate(self, SmsTemplate):
        self._SmsTemplate = SmsTemplate

    @property
    def IdCardNumber(self):
        """身份证号，脱敏显示
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def Name(self):
        """用户姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CanOffLine(self):
        """是否支持线下核身
        :rtype: bool
        """
        return self._CanOffLine

    @CanOffLine.setter
    def CanOffLine(self, CanOffLine):
        self._CanOffLine = CanOffLine

    @property
    def IdCardType(self):
        """证件号码类型：ID_CARD - 身份证，PASSPORT - 护照，MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证; 暂不支持用于电子签自有平台实名认证，MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证; 暂不支持用于电子签自有平台实名认证，HOUSEHOLD_REGISTER - 户口本; 暂不支持用于电子签自有平台实名认证，TEMP_ID_CARD - 临时居民身份证; 暂不支持用于电子签自有平台实名认证
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def CallbackUrl(self):
        """签署回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SignId(self):
        """签署任务ID，标识每一次的流程发送
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._VerifyChannel = params.get("VerifyChannel")
        self._ApproveStatus = params.get("ApproveStatus")
        self._ApproveMessage = params.get("ApproveMessage")
        self._ApproveTime = params.get("ApproveTime")
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._JumpUrl = params.get("JumpUrl")
        if params.get("ComponentSeals") is not None:
            self._ComponentSeals = []
            for item in params.get("ComponentSeals"):
                obj = ComponentSeal()
                obj._deserialize(item)
                self._ComponentSeals.append(obj)
        self._IsFullText = params.get("IsFullText")
        self._PreReadTime = params.get("PreReadTime")
        self._Mobile = params.get("Mobile")
        self._Deadline = params.get("Deadline")
        self._IsLastApprover = params.get("IsLastApprover")
        if params.get("SmsTemplate") is not None:
            self._SmsTemplate = SmsTemplate()
            self._SmsTemplate._deserialize(params.get("SmsTemplate"))
        self._IdCardNumber = params.get("IdCardNumber")
        self._Name = params.get("Name")
        self._CanOffLine = params.get("CanOffLine")
        self._IdCardType = params.get("IdCardType")
        self._CallbackUrl = params.get("CallbackUrl")
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowFileInfo(AbstractModel):
    """此结构体 (FlowFileInfo) 用于描述流程文档信息。

    """

    def __init__(self):
        r"""
        :param _FileIndex: 文件序号
        :type FileIndex: int
        :param _FileType: 文件类型
        :type FileType: str
        :param _FileMd5: 文件的MD5码
        :type FileMd5: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileSize: 文件大小，单位为Byte
        :type FileSize: int
        :param _CreatedOn: 文件创建时间戳
        :type CreatedOn: int
        :param _Url: 文件的下载地址
        :type Url: str
        """
        self._FileIndex = None
        self._FileType = None
        self._FileMd5 = None
        self._FileName = None
        self._FileSize = None
        self._CreatedOn = None
        self._Url = None

    @property
    def FileIndex(self):
        """文件序号
        :rtype: int
        """
        return self._FileIndex

    @FileIndex.setter
    def FileIndex(self, FileIndex):
        self._FileIndex = FileIndex

    @property
    def FileType(self):
        """文件类型
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileMd5(self):
        """文件的MD5码
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """文件大小，单位为Byte
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def CreatedOn(self):
        """文件创建时间戳
        :rtype: int
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def Url(self):
        """文件的下载地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._FileIndex = params.get("FileIndex")
        self._FileType = params.get("FileType")
        self._FileMd5 = params.get("FileMd5")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._CreatedOn = params.get("CreatedOn")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowInfo(AbstractModel):
    """此结构体 (FlowInfo) 用于描述流程信息。

    """

    def __init__(self):
        r"""
        :param _FlowName: 合同名字
        :type FlowName: str
        :param _Deadline: 签署截止时间戳，超过有效签署时间则该签署流程失败
        :type Deadline: int
        :param _FlowDescription: 合同描述
        :type FlowDescription: str
        :param _FlowType: 合同类型：
1. “劳务”
2. “销售”
3. “租赁”
4. “其他”
        :type FlowType: str
        :param _CallbackUrl: 回调地址
        :type CallbackUrl: str
        :param _UserData: 用户自定义数据
        :type UserData: str
        """
        self._FlowName = None
        self._Deadline = None
        self._FlowDescription = None
        self._FlowType = None
        self._CallbackUrl = None
        self._UserData = None

    @property
    def FlowName(self):
        """合同名字
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def Deadline(self):
        """签署截止时间戳，超过有效签署时间则该签署流程失败
        :rtype: int
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def FlowDescription(self):
        """合同描述
        :rtype: str
        """
        return self._FlowDescription

    @FlowDescription.setter
    def FlowDescription(self, FlowDescription):
        self._FlowDescription = FlowDescription

    @property
    def FlowType(self):
        """合同类型：
1. “劳务”
2. “销售”
3. “租赁”
4. “其他”
        :rtype: str
        """
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def CallbackUrl(self):
        """回调地址
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def UserData(self):
        """用户自定义数据
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData


    def _deserialize(self, params):
        self._FlowName = params.get("FlowName")
        self._Deadline = params.get("Deadline")
        self._FlowDescription = params.get("FlowDescription")
        self._FlowType = params.get("FlowType")
        self._CallbackUrl = params.get("CallbackUrl")
        self._UserData = params.get("UserData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateOrganizationSealRequest(AbstractModel):
    """GenerateOrganizationSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _SealType: 印章类型：
OFFICIAL-公章
SPECIAL_FINANCIAL-财务专用章
CONTRACT-合同专用章
LEGAL_REPRESENTATIVE-法定代表人章
SPECIAL_NATIONWIDE_INVOICE-发票专用章
OTHER-其他
        :type SealType: str
        :param _SourceIp: 请求生成企业印章的客户端Ip
        :type SourceIp: str
        :param _SealName: 电子印章名称
        :type SealName: str
        :param _SealHorizontalText: 企业印章横向文字，最多可填8个汉字（可不填，默认为"电子签名专用章"）
        :type SealHorizontalText: str
        :param _IsDefault: 是否是默认印章 true：是，false：否
        :type IsDefault: bool
        """
        self._Caller = None
        self._SealType = None
        self._SourceIp = None
        self._SealName = None
        self._SealHorizontalText = None
        self._IsDefault = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def SealType(self):
        """印章类型：
OFFICIAL-公章
SPECIAL_FINANCIAL-财务专用章
CONTRACT-合同专用章
LEGAL_REPRESENTATIVE-法定代表人章
SPECIAL_NATIONWIDE_INVOICE-发票专用章
OTHER-其他
        :rtype: str
        """
        return self._SealType

    @SealType.setter
    def SealType(self, SealType):
        self._SealType = SealType

    @property
    def SourceIp(self):
        """请求生成企业印章的客户端Ip
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def SealName(self):
        """电子印章名称
        :rtype: str
        """
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def SealHorizontalText(self):
        """企业印章横向文字，最多可填8个汉字（可不填，默认为"电子签名专用章"）
        :rtype: str
        """
        return self._SealHorizontalText

    @SealHorizontalText.setter
    def SealHorizontalText(self, SealHorizontalText):
        self._SealHorizontalText = SealHorizontalText

    @property
    def IsDefault(self):
        """是否是默认印章 true：是，false：否
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._SealType = params.get("SealType")
        self._SourceIp = params.get("SourceIp")
        self._SealName = params.get("SealName")
        self._SealHorizontalText = params.get("SealHorizontalText")
        self._IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateOrganizationSealResponse(AbstractModel):
    """GenerateOrganizationSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealId: 电子印章Id
        :type SealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealId = None
        self._RequestId = None

    @property
    def SealId(self):
        """电子印章Id
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._RequestId = params.get("RequestId")


class GenerateUserSealRequest(AbstractModel):
    """GenerateUserSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _UserId: 用户ID
        :type UserId: str
        :param _SourceIp: 请求生成个人印章的客户端IP
        :type SourceIp: str
        :param _SealName: 电子印章名称
        :type SealName: str
        :param _IsDefault: 是否是默认印章 true：是，false：否
        :type IsDefault: bool
        """
        self._Caller = None
        self._UserId = None
        self._SourceIp = None
        self._SealName = None
        self._IsDefault = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SourceIp(self):
        """请求生成个人印章的客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def SealName(self):
        """电子印章名称
        :rtype: str
        """
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def IsDefault(self):
        """是否是默认印章 true：是，false：否
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._UserId = params.get("UserId")
        self._SourceIp = params.get("SourceIp")
        self._SealName = params.get("SealName")
        self._IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateUserSealResponse(AbstractModel):
    """GenerateUserSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealId: 电子印章Id
        :type SealId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealId = None
        self._RequestId = None

    @property
    def SealId(self):
        """电子印章Id
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._RequestId = params.get("RequestId")


class ModifyOrganizationDefaultSealRequest(AbstractModel):
    """ModifyOrganizationDefaultSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _SealId: 重新指定的默认印章ID
        :type SealId: str
        :param _SourceIp: 请求重新指定企业默认印章的客户端IP
        :type SourceIp: str
        """
        self._Caller = None
        self._SealId = None
        self._SourceIp = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def SealId(self):
        """重新指定的默认印章ID
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SourceIp(self):
        """请求重新指定企业默认印章的客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._SealId = params.get("SealId")
        self._SourceIp = params.get("SourceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrganizationDefaultSealResponse(AbstractModel):
    """ModifyOrganizationDefaultSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySealRequest(AbstractModel):
    """ModifySeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _SourceIp: 请求更新印章的客户端IP
        :type SourceIp: str
        :param _SealId: 电子印章ID。若为空，则修改个人/机构的默认印章。
        :type SealId: str
        :param _SealName: 电子印章名称
        :type SealName: str
        :param _Image: 印章图片，base64编码（与FileId参数二选一，同时传入参数时优先使用Image参数）
        :type Image: str
        :param _FileId: 印章图片文件ID（与Image参数二选一，同时传入参数时优先使用Image参数）
        :type FileId: str
        :param _UserId: 需要更新印章的用户ID
        :type UserId: str
        """
        self._Caller = None
        self._SourceIp = None
        self._SealId = None
        self._SealName = None
        self._Image = None
        self._FileId = None
        self._UserId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def SourceIp(self):
        """请求更新印章的客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def SealId(self):
        """电子印章ID。若为空，则修改个人/机构的默认印章。
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SealName(self):
        """电子印章名称
        :rtype: str
        """
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def Image(self):
        """印章图片，base64编码（与FileId参数二选一，同时传入参数时优先使用Image参数）
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def FileId(self):
        """印章图片文件ID（与Image参数二选一，同时传入参数时优先使用Image参数）
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def UserId(self):
        """需要更新印章的用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._SourceIp = params.get("SourceIp")
        self._SealId = params.get("SealId")
        self._SealName = params.get("SealName")
        self._Image = params.get("Image")
        self._FileId = params.get("FileId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySealResponse(AbstractModel):
    """ModifySeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubOrganizationInfoRequest(AbstractModel):
    """ModifySubOrganizationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息，该接口 SubOrganizationId 字段与 OpenId 字段二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _OpenId: 机构在第三方的唯一标识，32位定长字符串，与 Caller 中 SubOrgnizationId 二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :type OpenId: str
        :param _Name: 机构名称全称，修改后机构状态将变为未实名，需要调用实名接口重新实名。
        :type Name: str
        :param _OrganizationType: 机构类型可选值：
1. ENTERPRISE - 企业；
2. INDIVIDUALBIZ - 个体工商户；
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :type OrganizationType: str
        :param _BizLicenseFile: 机构证件照片文件，base64编码。支持jpg，jpeg，png格式；如果传值，则重新上传文件后，机构状态将变为未实名，需要调用实名接口重新实名。
        :type BizLicenseFile: str
        :param _BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param _LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param _LegalIdCardType: 机构法人/经营者证件类型，可选值：ID_CARD - 居民身份证。OrganizationType 为 ENTERPRISE、INDIVIDUALBIZ 时，此项必填，其他情况选填。
        :type LegalIdCardType: str
        :param _LegalIdCardNumber: 机构法人/经营者证件号码。OrganizationType 为 ENTERPRISE、INDIVIDUALBIZ 时，此项必填，其他情况选填
        :type LegalIdCardNumber: str
        :param _LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param _ContactName: 组织联系人姓名
        :type ContactName: str
        :param _ContactAddress: 企业联系地址
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        :param _Email: 机构电子邮箱
        :type Email: str
        """
        self._Caller = None
        self._OpenId = None
        self._Name = None
        self._OrganizationType = None
        self._BizLicenseFile = None
        self._BizLicenseFileName = None
        self._LegalName = None
        self._LegalIdCardType = None
        self._LegalIdCardNumber = None
        self._LegalMobile = None
        self._ContactName = None
        self._ContactAddress = None
        self._Email = None

    @property
    def Caller(self):
        """调用方信息，该接口 SubOrganizationId 字段与 OpenId 字段二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def OpenId(self):
        """机构在第三方的唯一标识，32位定长字符串，与 Caller 中 SubOrgnizationId 二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Name(self):
        """机构名称全称，修改后机构状态将变为未实名，需要调用实名接口重新实名。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OrganizationType(self):
        """机构类型可选值：
1. ENTERPRISE - 企业；
2. INDIVIDUALBIZ - 个体工商户；
3. PUBLICINSTITUTION - 政府/事业单位
4. OTHERS - 其他组织
        :rtype: str
        """
        return self._OrganizationType

    @OrganizationType.setter
    def OrganizationType(self, OrganizationType):
        self._OrganizationType = OrganizationType

    @property
    def BizLicenseFile(self):
        """机构证件照片文件，base64编码。支持jpg，jpeg，png格式；如果传值，则重新上传文件后，机构状态将变为未实名，需要调用实名接口重新实名。
        :rtype: str
        """
        return self._BizLicenseFile

    @BizLicenseFile.setter
    def BizLicenseFile(self, BizLicenseFile):
        self._BizLicenseFile = BizLicenseFile

    @property
    def BizLicenseFileName(self):
        """机构证件照片文件名
        :rtype: str
        """
        return self._BizLicenseFileName

    @BizLicenseFileName.setter
    def BizLicenseFileName(self, BizLicenseFileName):
        self._BizLicenseFileName = BizLicenseFileName

    @property
    def LegalName(self):
        """机构法人/经营者姓名
        :rtype: str
        """
        return self._LegalName

    @LegalName.setter
    def LegalName(self, LegalName):
        self._LegalName = LegalName

    @property
    def LegalIdCardType(self):
        """机构法人/经营者证件类型，可选值：ID_CARD - 居民身份证。OrganizationType 为 ENTERPRISE、INDIVIDUALBIZ 时，此项必填，其他情况选填。
        :rtype: str
        """
        return self._LegalIdCardType

    @LegalIdCardType.setter
    def LegalIdCardType(self, LegalIdCardType):
        self._LegalIdCardType = LegalIdCardType

    @property
    def LegalIdCardNumber(self):
        """机构法人/经营者证件号码。OrganizationType 为 ENTERPRISE、INDIVIDUALBIZ 时，此项必填，其他情况选填
        :rtype: str
        """
        return self._LegalIdCardNumber

    @LegalIdCardNumber.setter
    def LegalIdCardNumber(self, LegalIdCardNumber):
        self._LegalIdCardNumber = LegalIdCardNumber

    @property
    def LegalMobile(self):
        """机构法人/经营者/联系人手机号码
        :rtype: str
        """
        return self._LegalMobile

    @LegalMobile.setter
    def LegalMobile(self, LegalMobile):
        self._LegalMobile = LegalMobile

    @property
    def ContactName(self):
        """组织联系人姓名
        :rtype: str
        """
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def ContactAddress(self):
        """企业联系地址
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Address`
        """
        return self._ContactAddress

    @ContactAddress.setter
    def ContactAddress(self, ContactAddress):
        self._ContactAddress = ContactAddress

    @property
    def Email(self):
        """机构电子邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._OpenId = params.get("OpenId")
        self._Name = params.get("Name")
        self._OrganizationType = params.get("OrganizationType")
        self._BizLicenseFile = params.get("BizLicenseFile")
        self._BizLicenseFileName = params.get("BizLicenseFileName")
        self._LegalName = params.get("LegalName")
        self._LegalIdCardType = params.get("LegalIdCardType")
        self._LegalIdCardNumber = params.get("LegalIdCardNumber")
        self._LegalMobile = params.get("LegalMobile")
        self._ContactName = params.get("ContactName")
        if params.get("ContactAddress") is not None:
            self._ContactAddress = Address()
            self._ContactAddress._deserialize(params.get("ContactAddress"))
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubOrganizationInfoResponse(AbstractModel):
    """ModifySubOrganizationInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubOrganizationId: 子机构ID
        :type SubOrganizationId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubOrganizationId = None
        self._RequestId = None

    @property
    def SubOrganizationId(self):
        """子机构ID
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._RequestId = params.get("RequestId")


class ModifyUserDefaultSealRequest(AbstractModel):
    """ModifyUserDefaultSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _UserId: 用户唯一标识，需要重新指定默认印章的用户ID
        :type UserId: str
        :param _SealId: 重新指定的默认印章ID
        :type SealId: str
        :param _SourceIp: 请求重新指定个人默认印章的客户端IP
        :type SourceIp: str
        """
        self._Caller = None
        self._UserId = None
        self._SealId = None
        self._SourceIp = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def UserId(self):
        """用户唯一标识，需要重新指定默认印章的用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SealId(self):
        """重新指定的默认印章ID
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SourceIp(self):
        """请求重新指定个人默认印章的客户端IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._UserId = params.get("UserId")
        self._SealId = params.get("SealId")
        self._SourceIp = params.get("SourceIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserDefaultSealResponse(AbstractModel):
    """ModifyUserDefaultSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _OpenId: 第三方平台用户唯一标识; OpenId 和 UserId 二选一填写, 两个都不为空则优先使用UserId
        :type OpenId: str
        :param _UserId: 腾讯电子签平台用户唯一标识; OpenId 和 UserId 二选一填写, 两个都不为空则优先使用UserId
        :type UserId: str
        :param _Mobile: 用户手机号码，不要求唯一
        :type Mobile: str
        :param _Email: 用户邮箱，不要求唯一
        :type Email: str
        :param _Name: 用户姓名
        :type Name: str
        """
        self._Caller = None
        self._OpenId = None
        self._UserId = None
        self._Mobile = None
        self._Email = None
        self._Name = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def OpenId(self):
        """第三方平台用户唯一标识; OpenId 和 UserId 二选一填写, 两个都不为空则优先使用UserId
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def UserId(self):
        """腾讯电子签平台用户唯一标识; OpenId 和 UserId 二选一填写, 两个都不为空则优先使用UserId
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Mobile(self):
        """用户手机号码，不要求唯一
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def Email(self):
        """用户邮箱，不要求唯一
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Name(self):
        """用户姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._OpenId = params.get("OpenId")
        self._UserId = params.get("UserId")
        self._Mobile = params.get("Mobile")
        self._Email = params.get("Email")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    """ModifyUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 腾讯电子签平台用户唯一标识
        :type UserId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        """腾讯电子签平台用户唯一标识
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class RejectFlowRequest(AbstractModel):
    """RejectFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 流程编号
        :type FlowId: str
        :param _VerifyResult: 意愿确认票据。
1. VerifyChannel 为 WEIXINAPP，使用响应的VerifyResult；
2. VerifyChannel 为 FACEID时，使用OrderNo；
3. VerifyChannel 为 VERIFYCODE，使用短信验证码
4. VerifyChannel 为 NONE，传空值
（注：普通情况下，VerifyResult不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyResult: str
        :param _VerifyChannel: 意愿确认渠道：
1. WEIXINAPP - 微信小程序
2. FACEID - 慧眼 (默认) 
3. VERIFYCODE - 验证码
4. THIRD - 第三方 (暂不支持)
5. NONE - 无需电子签系统验证
（注：普通情况下，VerifyChannel不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyChannel: str
        :param _SourceIp: 客户端来源IP
        :type SourceIp: str
        :param _RejectMessage: 拒签原因
        :type RejectMessage: str
        :param _SignId: 签署参与者编号
        :type SignId: str
        """
        self._Caller = None
        self._FlowId = None
        self._VerifyResult = None
        self._VerifyChannel = None
        self._SourceIp = None
        self._RejectMessage = None
        self._SignId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """流程编号
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def VerifyResult(self):
        """意愿确认票据。
1. VerifyChannel 为 WEIXINAPP，使用响应的VerifyResult；
2. VerifyChannel 为 FACEID时，使用OrderNo；
3. VerifyChannel 为 VERIFYCODE，使用短信验证码
4. VerifyChannel 为 NONE，传空值
（注：普通情况下，VerifyResult不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :rtype: str
        """
        return self._VerifyResult

    @VerifyResult.setter
    def VerifyResult(self, VerifyResult):
        self._VerifyResult = VerifyResult

    @property
    def VerifyChannel(self):
        """意愿确认渠道：
1. WEIXINAPP - 微信小程序
2. FACEID - 慧眼 (默认) 
3. VERIFYCODE - 验证码
4. THIRD - 第三方 (暂不支持)
5. NONE - 无需电子签系统验证
（注：普通情况下，VerifyChannel不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :rtype: str
        """
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def SourceIp(self):
        """客户端来源IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def RejectMessage(self):
        """拒签原因
        :rtype: str
        """
        return self._RejectMessage

    @RejectMessage.setter
    def RejectMessage(self, RejectMessage):
        self._RejectMessage = RejectMessage

    @property
    def SignId(self):
        """签署参与者编号
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        self._VerifyResult = params.get("VerifyResult")
        self._VerifyChannel = params.get("VerifyChannel")
        self._SourceIp = params.get("SourceIp")
        self._RejectMessage = params.get("RejectMessage")
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectFlowResponse(AbstractModel):
    """RejectFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Seal(AbstractModel):
    """此结构体 (Seal) 用于描述电子印章的信息。

    """

    def __init__(self):
        r"""
        :param _SealId: 电子印章ID
        :type SealId: str
        :param _SealName: 电子印章名称
        :type SealName: str
        :param _SealType: 电子印章类型
        :type SealType: str
        :param _SealSource: 电子印章来源：
CREATE - 通过图片上传
GENERATE - 通过文字生成
        :type SealSource: str
        :param _Creator: 电子印章创建者
        :type Creator: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _CreatedOn: 电子印章创建时间戳
        :type CreatedOn: int
        :param _UserId: 电子印章所有人
        :type UserId: str
        :param _FileUrl: 电子印章URL
        :type FileUrl: :class:`tencentcloud.essbasic.v20201222.models.FileUrl`
        :param _DefaultSeal: 是否为默认印章，false-非默认，true-默认
        :type DefaultSeal: bool
        """
        self._SealId = None
        self._SealName = None
        self._SealType = None
        self._SealSource = None
        self._Creator = None
        self._CreatedOn = None
        self._UserId = None
        self._FileUrl = None
        self._DefaultSeal = None

    @property
    def SealId(self):
        """电子印章ID
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SealName(self):
        """电子印章名称
        :rtype: str
        """
        return self._SealName

    @SealName.setter
    def SealName(self, SealName):
        self._SealName = SealName

    @property
    def SealType(self):
        """电子印章类型
        :rtype: str
        """
        return self._SealType

    @SealType.setter
    def SealType(self, SealType):
        self._SealType = SealType

    @property
    def SealSource(self):
        """电子印章来源：
CREATE - 通过图片上传
GENERATE - 通过文字生成
        :rtype: str
        """
        return self._SealSource

    @SealSource.setter
    def SealSource(self, SealSource):
        self._SealSource = SealSource

    @property
    def Creator(self):
        """电子印章创建者
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedOn(self):
        """电子印章创建时间戳
        :rtype: int
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UserId(self):
        """电子印章所有人
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def FileUrl(self):
        """电子印章URL
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.FileUrl`
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def DefaultSeal(self):
        """是否为默认印章，false-非默认，true-默认
        :rtype: bool
        """
        return self._DefaultSeal

    @DefaultSeal.setter
    def DefaultSeal(self, DefaultSeal):
        self._DefaultSeal = DefaultSeal


    def _deserialize(self, params):
        self._SealId = params.get("SealId")
        self._SealName = params.get("SealName")
        self._SealType = params.get("SealType")
        self._SealSource = params.get("SealSource")
        if params.get("Creator") is not None:
            self._Creator = Caller()
            self._Creator._deserialize(params.get("Creator"))
        self._CreatedOn = params.get("CreatedOn")
        self._UserId = params.get("UserId")
        if params.get("FileUrl") is not None:
            self._FileUrl = FileUrl()
            self._FileUrl._deserialize(params.get("FileUrl"))
        self._DefaultSeal = params.get("DefaultSeal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendFlowRequest(AbstractModel):
    """SendFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 需要推送合同的流程ID
        :type FlowId: str
        :param _UserId: 签署人用户ID
        :type UserId: str
        :param _SignComponents: 签署控件信息 (支持添加多个控件)
        :type SignComponents: list of Component
        :param _Mobile: 签署人手机号 (如果选择短信验证码签署，则此字段必填)
        :type Mobile: str
        :param _SubOrganizationId: 签署人对应的子机构ID，个人签署者此字段不填
        :type SubOrganizationId: str
        :param _VerifyChannel: 签名后校验方式：
1. WEIXINAPP - 微信小程序；
2. FACEID - 慧眼 (默认) ；
3. VERIFYCODE - 验证码；
4. NONE - 无。此选项为白名单参数，暂不支持公开调用。如需开通权限，请通过客户经理或邮件至e-contract@tencent.com与我们联系；
5. THIRD - 第三方 (暂不支持)
        :type VerifyChannel: list of str
        :param _Deadline: 签署链接失效截止时间，默认为7天
        :type Deadline: int
        :param _IsLastApprover: 是否为最后一个签署人。若为最后一人，本次签署完成以后自动归档。
        :type IsLastApprover: bool
        :param _JumpUrl: 签署完成后，前端跳转的URL
        :type JumpUrl: str
        :param _SmsTemplate: 短信模板。默认使用腾讯电子签官方短信模板，如有自定义需求，请通过客户经理或邮件至e-contract@tencent.com与我们联系。
        :type SmsTemplate: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        :param _IsFullText: 签署前置条件：是否要全文阅读，默认否
        :type IsFullText: bool
        :param _PreReadTime: 签署前置条件：强制用户阅读待签署文件时长，默认不限制
        :type PreReadTime: int
        :param _CanOffLine: 当前参与者是否支持线下核身,默认为不支持
        :type CanOffLine: bool
        :param _CallbackUrl: 签署任务的回调地址
        :type CallbackUrl: str
        """
        self._Caller = None
        self._FlowId = None
        self._UserId = None
        self._SignComponents = None
        self._Mobile = None
        self._SubOrganizationId = None
        self._VerifyChannel = None
        self._Deadline = None
        self._IsLastApprover = None
        self._JumpUrl = None
        self._SmsTemplate = None
        self._IsFullText = None
        self._PreReadTime = None
        self._CanOffLine = None
        self._CallbackUrl = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """需要推送合同的流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def UserId(self):
        """签署人用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SignComponents(self):
        """签署控件信息 (支持添加多个控件)
        :rtype: list of Component
        """
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def Mobile(self):
        """签署人手机号 (如果选择短信验证码签署，则此字段必填)
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def SubOrganizationId(self):
        """签署人对应的子机构ID，个人签署者此字段不填
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def VerifyChannel(self):
        """签名后校验方式：
1. WEIXINAPP - 微信小程序；
2. FACEID - 慧眼 (默认) ；
3. VERIFYCODE - 验证码；
4. NONE - 无。此选项为白名单参数，暂不支持公开调用。如需开通权限，请通过客户经理或邮件至e-contract@tencent.com与我们联系；
5. THIRD - 第三方 (暂不支持)
        :rtype: list of str
        """
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def Deadline(self):
        """签署链接失效截止时间，默认为7天
        :rtype: int
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def IsLastApprover(self):
        """是否为最后一个签署人。若为最后一人，本次签署完成以后自动归档。
        :rtype: bool
        """
        return self._IsLastApprover

    @IsLastApprover.setter
    def IsLastApprover(self, IsLastApprover):
        self._IsLastApprover = IsLastApprover

    @property
    def JumpUrl(self):
        """签署完成后，前端跳转的URL
        :rtype: str
        """
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def SmsTemplate(self):
        """短信模板。默认使用腾讯电子签官方短信模板，如有自定义需求，请通过客户经理或邮件至e-contract@tencent.com与我们联系。
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        """
        return self._SmsTemplate

    @SmsTemplate.setter
    def SmsTemplate(self, SmsTemplate):
        self._SmsTemplate = SmsTemplate

    @property
    def IsFullText(self):
        """签署前置条件：是否要全文阅读，默认否
        :rtype: bool
        """
        return self._IsFullText

    @IsFullText.setter
    def IsFullText(self, IsFullText):
        self._IsFullText = IsFullText

    @property
    def PreReadTime(self):
        """签署前置条件：强制用户阅读待签署文件时长，默认不限制
        :rtype: int
        """
        return self._PreReadTime

    @PreReadTime.setter
    def PreReadTime(self, PreReadTime):
        self._PreReadTime = PreReadTime

    @property
    def CanOffLine(self):
        """当前参与者是否支持线下核身,默认为不支持
        :rtype: bool
        """
        return self._CanOffLine

    @CanOffLine.setter
    def CanOffLine(self, CanOffLine):
        self._CanOffLine = CanOffLine

    @property
    def CallbackUrl(self):
        """签署任务的回调地址
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        self._UserId = params.get("UserId")
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._Mobile = params.get("Mobile")
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._VerifyChannel = params.get("VerifyChannel")
        self._Deadline = params.get("Deadline")
        self._IsLastApprover = params.get("IsLastApprover")
        self._JumpUrl = params.get("JumpUrl")
        if params.get("SmsTemplate") is not None:
            self._SmsTemplate = SmsTemplate()
            self._SmsTemplate._deserialize(params.get("SmsTemplate"))
        self._IsFullText = params.get("IsFullText")
        self._PreReadTime = params.get("PreReadTime")
        self._CanOffLine = params.get("CanOffLine")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendFlowResponse(AbstractModel):
    """SendFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignId: 签署任务ID，标识每一次的流程发送
        :type SignId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignId = None
        self._RequestId = None

    @property
    def SignId(self):
        """签署任务ID，标识每一次的流程发送
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._RequestId = params.get("RequestId")


class SendFlowUrlRequest(AbstractModel):
    """SendFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 需要推送合同的流程ID
        :type FlowId: str
        :param _UserId: 签署人ID
        :type UserId: str
        :param _SignComponents: 签署控件信息 (支持添加多个控件)
        :type SignComponents: list of Component
        :param _Mobile: 签署人手机号 (如果选择短信验证码签署，则此字段必填)
        :type Mobile: str
        :param _SubOrganizationId: 签署人对应的子机构ID，个人签署者此字段不填
        :type SubOrganizationId: str
        :param _VerifyChannel: 签名后校验方式：
1. WEIXINAPP - 微信小程序；
2. FACEID - 慧眼 (默认) ；
3. VERIFYCODE - 验证码；
4. NONE - 无。此选项为白名单参数，暂不支持公开调用。如需开通权限，请通过客户经理或邮件至e-contract@tencent.com与我们联系；
5. THIRD - 第三方 (暂不支持)
6. OFFLINE - 线下人工审核
        :type VerifyChannel: list of str
        :param _Deadline: 签署链接失效截止时间，默认为7天
        :type Deadline: int
        :param _IsLastApprover: 是否为最后一个签署人。若为最后一人，本次签署完成以后自动归档
        :type IsLastApprover: bool
        :param _JumpUrl: 签署完成后，前端跳转的url
        :type JumpUrl: str
        :param _SmsTemplate: 短信模板
默认使用腾讯电子签官方短信模板，如有自定义需求，请通过客户经理或邮件至e-contract@tencent.com与我们联系。
        :type SmsTemplate: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        :param _IsFullText: 签署前置条件：是否要全文阅读，默认否
        :type IsFullText: bool
        :param _PreReadTime: 签署前置条件：强制用户阅读待签署文件时长，默认不限制
        :type PreReadTime: int
        :param _CanOffLine: 当前参与者是否支持线下核身,默认为不支持
        :type CanOffLine: bool
        :param _CallbackUrl: 签署任务的回调地址
        :type CallbackUrl: str
        """
        self._Caller = None
        self._FlowId = None
        self._UserId = None
        self._SignComponents = None
        self._Mobile = None
        self._SubOrganizationId = None
        self._VerifyChannel = None
        self._Deadline = None
        self._IsLastApprover = None
        self._JumpUrl = None
        self._SmsTemplate = None
        self._IsFullText = None
        self._PreReadTime = None
        self._CanOffLine = None
        self._CallbackUrl = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """需要推送合同的流程ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def UserId(self):
        """签署人ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SignComponents(self):
        """签署控件信息 (支持添加多个控件)
        :rtype: list of Component
        """
        return self._SignComponents

    @SignComponents.setter
    def SignComponents(self, SignComponents):
        self._SignComponents = SignComponents

    @property
    def Mobile(self):
        """签署人手机号 (如果选择短信验证码签署，则此字段必填)
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def SubOrganizationId(self):
        """签署人对应的子机构ID，个人签署者此字段不填
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def VerifyChannel(self):
        """签名后校验方式：
1. WEIXINAPP - 微信小程序；
2. FACEID - 慧眼 (默认) ；
3. VERIFYCODE - 验证码；
4. NONE - 无。此选项为白名单参数，暂不支持公开调用。如需开通权限，请通过客户经理或邮件至e-contract@tencent.com与我们联系；
5. THIRD - 第三方 (暂不支持)
6. OFFLINE - 线下人工审核
        :rtype: list of str
        """
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def Deadline(self):
        """签署链接失效截止时间，默认为7天
        :rtype: int
        """
        return self._Deadline

    @Deadline.setter
    def Deadline(self, Deadline):
        self._Deadline = Deadline

    @property
    def IsLastApprover(self):
        """是否为最后一个签署人。若为最后一人，本次签署完成以后自动归档
        :rtype: bool
        """
        return self._IsLastApprover

    @IsLastApprover.setter
    def IsLastApprover(self, IsLastApprover):
        self._IsLastApprover = IsLastApprover

    @property
    def JumpUrl(self):
        """签署完成后，前端跳转的url
        :rtype: str
        """
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def SmsTemplate(self):
        """短信模板
默认使用腾讯电子签官方短信模板，如有自定义需求，请通过客户经理或邮件至e-contract@tencent.com与我们联系。
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.SmsTemplate`
        """
        return self._SmsTemplate

    @SmsTemplate.setter
    def SmsTemplate(self, SmsTemplate):
        self._SmsTemplate = SmsTemplate

    @property
    def IsFullText(self):
        """签署前置条件：是否要全文阅读，默认否
        :rtype: bool
        """
        return self._IsFullText

    @IsFullText.setter
    def IsFullText(self, IsFullText):
        self._IsFullText = IsFullText

    @property
    def PreReadTime(self):
        """签署前置条件：强制用户阅读待签署文件时长，默认不限制
        :rtype: int
        """
        return self._PreReadTime

    @PreReadTime.setter
    def PreReadTime(self, PreReadTime):
        self._PreReadTime = PreReadTime

    @property
    def CanOffLine(self):
        """当前参与者是否支持线下核身,默认为不支持
        :rtype: bool
        """
        return self._CanOffLine

    @CanOffLine.setter
    def CanOffLine(self, CanOffLine):
        self._CanOffLine = CanOffLine

    @property
    def CallbackUrl(self):
        """签署任务的回调地址
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        self._UserId = params.get("UserId")
        if params.get("SignComponents") is not None:
            self._SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self._SignComponents.append(obj)
        self._Mobile = params.get("Mobile")
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._VerifyChannel = params.get("VerifyChannel")
        self._Deadline = params.get("Deadline")
        self._IsLastApprover = params.get("IsLastApprover")
        self._JumpUrl = params.get("JumpUrl")
        if params.get("SmsTemplate") is not None:
            self._SmsTemplate = SmsTemplate()
            self._SmsTemplate._deserialize(params.get("SmsTemplate"))
        self._IsFullText = params.get("IsFullText")
        self._PreReadTime = params.get("PreReadTime")
        self._CanOffLine = params.get("CanOffLine")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendFlowUrlResponse(AbstractModel):
    """SendFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignId: 签署任务ID，标识每一次的流程发送
        :type SignId: str
        :param _SignUrl: 签署链接
        :type SignUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignId = None
        self._SignUrl = None
        self._RequestId = None

    @property
    def SignId(self):
        """签署任务ID，标识每一次的流程发送
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def SignUrl(self):
        """签署链接
        :rtype: str
        """
        return self._SignUrl

    @SignUrl.setter
    def SignUrl(self, SignUrl):
        self._SignUrl = SignUrl

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._SignUrl = params.get("SignUrl")
        self._RequestId = params.get("RequestId")


class SendSignInnerVerifyCodeRequest(AbstractModel):
    """SendSignInnerVerifyCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _Mobile: 手机号
        :type Mobile: str
        :param _VerifyType: 验证码类型，取值(SIGN)
        :type VerifyType: str
        :param _UserId: 用户 id
        :type UserId: str
        :param _VerifyTemplateId: 模板 id
        :type VerifyTemplateId: str
        :param _VerifySign: 签名
        :type VerifySign: str
        :param _FlowId: 流程(目录) id
        :type FlowId: str
        :param _CheckThreeElementResult: 三要素检测结果
        :type CheckThreeElementResult: int
        """
        self._Caller = None
        self._Mobile = None
        self._VerifyType = None
        self._UserId = None
        self._VerifyTemplateId = None
        self._VerifySign = None
        self._FlowId = None
        self._CheckThreeElementResult = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def Mobile(self):
        """手机号
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def VerifyType(self):
        """验证码类型，取值(SIGN)
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def UserId(self):
        """用户 id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def VerifyTemplateId(self):
        """模板 id
        :rtype: str
        """
        return self._VerifyTemplateId

    @VerifyTemplateId.setter
    def VerifyTemplateId(self, VerifyTemplateId):
        self._VerifyTemplateId = VerifyTemplateId

    @property
    def VerifySign(self):
        """签名
        :rtype: str
        """
        return self._VerifySign

    @VerifySign.setter
    def VerifySign(self, VerifySign):
        self._VerifySign = VerifySign

    @property
    def FlowId(self):
        """流程(目录) id
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def CheckThreeElementResult(self):
        """三要素检测结果
        :rtype: int
        """
        return self._CheckThreeElementResult

    @CheckThreeElementResult.setter
    def CheckThreeElementResult(self, CheckThreeElementResult):
        self._CheckThreeElementResult = CheckThreeElementResult


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._Mobile = params.get("Mobile")
        self._VerifyType = params.get("VerifyType")
        self._UserId = params.get("UserId")
        self._VerifyTemplateId = params.get("VerifyTemplateId")
        self._VerifySign = params.get("VerifySign")
        self._FlowId = params.get("FlowId")
        self._CheckThreeElementResult = params.get("CheckThreeElementResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSignInnerVerifyCodeResponse(AbstractModel):
    """SendSignInnerVerifyCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: true: 验证码正确，false: 验证码错误
        :type Result: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """true: 验证码正确，false: 验证码错误
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class SignFlowRequest(AbstractModel):
    """SignFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _FlowId: 流程编号
        :type FlowId: str
        :param _VerifyResult: 意愿确认票据。
1. VerifyChannel 为 WEIXINAPP，使用响应的VerifyResult；
2. VerifyChannel 为 FACEID时，使用OrderNo；
3. VerifyChannel 为 VERIFYCODE，使用短信验证码
4. VerifyChannel 为 NONE，传空值
（注：普通情况下，VerifyResult不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyResult: str
        :param _VerifyChannel: 意愿确认渠道：
1. WEIXINAPP - 微信小程序
2. FACEID - 慧眼 (默认) 
3. VERIFYCODE - 验证码
4. THIRD - 第三方 (暂不支持)
5. NONE - 无需电子签系统验证
（注：普通情况下，VerifyChannel不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :type VerifyChannel: str
        :param _SourceIp: 客户端来源IP
        :type SourceIp: str
        :param _SignSeals: 签署内容
        :type SignSeals: list of SignSeal
        :param _ApproveMessage: 签署备注
        :type ApproveMessage: str
        :param _SignId: 签署参与者编号
        :type SignId: str
        """
        self._Caller = None
        self._FlowId = None
        self._VerifyResult = None
        self._VerifyChannel = None
        self._SourceIp = None
        self._SignSeals = None
        self._ApproveMessage = None
        self._SignId = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def FlowId(self):
        """流程编号
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def VerifyResult(self):
        """意愿确认票据。
1. VerifyChannel 为 WEIXINAPP，使用响应的VerifyResult；
2. VerifyChannel 为 FACEID时，使用OrderNo；
3. VerifyChannel 为 VERIFYCODE，使用短信验证码
4. VerifyChannel 为 NONE，传空值
（注：普通情况下，VerifyResult不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :rtype: str
        """
        return self._VerifyResult

    @VerifyResult.setter
    def VerifyResult(self, VerifyResult):
        self._VerifyResult = VerifyResult

    @property
    def VerifyChannel(self):
        """意愿确认渠道：
1. WEIXINAPP - 微信小程序
2. FACEID - 慧眼 (默认) 
3. VERIFYCODE - 验证码
4. THIRD - 第三方 (暂不支持)
5. NONE - 无需电子签系统验证
（注：普通情况下，VerifyChannel不能为None，如您不希望腾讯电子签对用户签署意愿做校验，请提前与客户经理或邮件至e-contract@tencent.com与我们联系）
        :rtype: str
        """
        return self._VerifyChannel

    @VerifyChannel.setter
    def VerifyChannel(self, VerifyChannel):
        self._VerifyChannel = VerifyChannel

    @property
    def SourceIp(self):
        """客户端来源IP
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def SignSeals(self):
        """签署内容
        :rtype: list of SignSeal
        """
        return self._SignSeals

    @SignSeals.setter
    def SignSeals(self, SignSeals):
        self._SignSeals = SignSeals

    @property
    def ApproveMessage(self):
        """签署备注
        :rtype: str
        """
        return self._ApproveMessage

    @ApproveMessage.setter
    def ApproveMessage(self, ApproveMessage):
        self._ApproveMessage = ApproveMessage

    @property
    def SignId(self):
        """签署参与者编号
        :rtype: str
        """
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._FlowId = params.get("FlowId")
        self._VerifyResult = params.get("VerifyResult")
        self._VerifyChannel = params.get("VerifyChannel")
        self._SourceIp = params.get("SourceIp")
        if params.get("SignSeals") is not None:
            self._SignSeals = []
            for item in params.get("SignSeals"):
                obj = SignSeal()
                obj._deserialize(item)
                self._SignSeals.append(obj)
        self._ApproveMessage = params.get("ApproveMessage")
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignFlowResponse(AbstractModel):
    """SignFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 签署任务状态。签署成功 - SUCCESS、提交审核 - REVIEW
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """签署任务状态。签署成功 - SUCCESS、提交审核 - REVIEW
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SignSeal(AbstractModel):
    """此结构体 (SignSeal) 用于描述签名/印章信息。

    """

    def __init__(self):
        r"""
        :param _ComponentId: 签署控件ID
        :type ComponentId: str
        :param _SignType: 签署印章类型:
SIGN_SIGNATURE - 签名
SIGN_SEAL - 印章
SIGN_DATE - 日期
SIGN_IMAGE - 图片
        :type SignType: str
        :param _FileIndex: 合同文件ID
        :type FileIndex: int
        :param _SealId: 印章ID，仅当 SignType 为 SIGN_SEAL 时必填
        :type SealId: str
        :param _SealContent: 签名内容，仅当 SignType 为SIGN_SIGNATURE或SIGN_IMAGE 时必填，base64编码
        :type SealContent: str
        """
        self._ComponentId = None
        self._SignType = None
        self._FileIndex = None
        self._SealId = None
        self._SealContent = None

    @property
    def ComponentId(self):
        """签署控件ID
        :rtype: str
        """
        return self._ComponentId

    @ComponentId.setter
    def ComponentId(self, ComponentId):
        self._ComponentId = ComponentId

    @property
    def SignType(self):
        """签署印章类型:
SIGN_SIGNATURE - 签名
SIGN_SEAL - 印章
SIGN_DATE - 日期
SIGN_IMAGE - 图片
        :rtype: str
        """
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def FileIndex(self):
        """合同文件ID
        :rtype: int
        """
        return self._FileIndex

    @FileIndex.setter
    def FileIndex(self, FileIndex):
        self._FileIndex = FileIndex

    @property
    def SealId(self):
        """印章ID，仅当 SignType 为 SIGN_SEAL 时必填
        :rtype: str
        """
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def SealContent(self):
        """签名内容，仅当 SignType 为SIGN_SIGNATURE或SIGN_IMAGE 时必填，base64编码
        :rtype: str
        """
        return self._SealContent

    @SealContent.setter
    def SealContent(self, SealContent):
        self._SealContent = SealContent


    def _deserialize(self, params):
        self._ComponentId = params.get("ComponentId")
        self._SignType = params.get("SignType")
        self._FileIndex = params.get("FileIndex")
        self._SealId = params.get("SealId")
        self._SealContent = params.get("SealContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsTemplate(AbstractModel):
    """此结构体 (SmsTemplate) 用于描述短信模板。

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板ID，必须填写已审核通过的模板ID。模板ID可登录短信控制台查看。
        :type TemplateId: str
        :param _Sign: 短信签名内容，使用UTF-8编码，必须填写已审核通过的签名，签名信息可登录短信控制台查看。
        :type Sign: str
        """
        self._TemplateId = None
        self._Sign = None

    @property
    def TemplateId(self):
        """模板ID，必须填写已审核通过的模板ID。模板ID可登录短信控制台查看。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Sign(self):
        """短信签名内容，使用UTF-8编码，必须填写已审核通过的签名，签名信息可登录短信控制台查看。
        :rtype: str
        """
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Sign = params.get("Sign")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubOrganizationDetail(AbstractModel):
    """此结构体 (SubOrganizationDetail) 用于描述子机构或子企业的详情信息。

    """

    def __init__(self):
        r"""
        :param _Id: 组织ID
        :type Id: str
        :param _Name: 机构名称全称
        :type Name: str
        :param _Email: 机构电子邮箱
        :type Email: str
        :param _IdCardType: 机构证件号码类型
        :type IdCardType: str
        :param _IdCardNumber: 机构证件号码
        :type IdCardNumber: str
        :param _OrganizationType: 机构类型
        :type OrganizationType: str
        :param _IdCardFileType: 机构证件文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardFileType: str
        :param _BizLicenseFile: 机构证件照片文件，base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type BizLicenseFile: str
        :param _BizLicenseFileName: 机构证件照片文件名
        :type BizLicenseFileName: str
        :param _LegalName: 机构法人/经营者姓名
        :type LegalName: str
        :param _LegalIdCardType: 机构法人/经营者证件类型
        :type LegalIdCardType: str
        :param _LegalIdCardNumber: 机构法人/经营者证件号码
        :type LegalIdCardNumber: str
        :param _LegalMobile: 机构法人/经营者/联系人手机号码
        :type LegalMobile: str
        :param _ContactName: 组织联系人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactName: str
        :param _VerifyStatus: 机构实名状态
        :type VerifyStatus: str
        :param _VerifiedOn: 机构通过实名时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifiedOn: int
        :param _CreatedOn: 机构创建时间
        :type CreatedOn: int
        :param _UpdatedOn: 机构更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedOn: int
        :param _VerifyClientIp: 实名认证的客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyClientIp: str
        :param _VerifyServerIp: 实名认证的服务器IP
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyServerIp: str
        :param _ContactAddress: 企业联系地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactAddress: :class:`tencentcloud.essbasic.v20201222.models.Address`
        """
        self._Id = None
        self._Name = None
        self._Email = None
        self._IdCardType = None
        self._IdCardNumber = None
        self._OrganizationType = None
        self._IdCardFileType = None
        self._BizLicenseFile = None
        self._BizLicenseFileName = None
        self._LegalName = None
        self._LegalIdCardType = None
        self._LegalIdCardNumber = None
        self._LegalMobile = None
        self._ContactName = None
        self._VerifyStatus = None
        self._VerifiedOn = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._VerifyClientIp = None
        self._VerifyServerIp = None
        self._ContactAddress = None

    @property
    def Id(self):
        """组织ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """机构名称全称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Email(self):
        """机构电子邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def IdCardType(self):
        """机构证件号码类型
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """机构证件号码
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def OrganizationType(self):
        """机构类型
        :rtype: str
        """
        return self._OrganizationType

    @OrganizationType.setter
    def OrganizationType(self, OrganizationType):
        self._OrganizationType = OrganizationType

    @property
    def IdCardFileType(self):
        """机构证件文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdCardFileType

    @IdCardFileType.setter
    def IdCardFileType(self, IdCardFileType):
        self._IdCardFileType = IdCardFileType

    @property
    def BizLicenseFile(self):
        """机构证件照片文件，base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BizLicenseFile

    @BizLicenseFile.setter
    def BizLicenseFile(self, BizLicenseFile):
        self._BizLicenseFile = BizLicenseFile

    @property
    def BizLicenseFileName(self):
        """机构证件照片文件名
        :rtype: str
        """
        return self._BizLicenseFileName

    @BizLicenseFileName.setter
    def BizLicenseFileName(self, BizLicenseFileName):
        self._BizLicenseFileName = BizLicenseFileName

    @property
    def LegalName(self):
        """机构法人/经营者姓名
        :rtype: str
        """
        return self._LegalName

    @LegalName.setter
    def LegalName(self, LegalName):
        self._LegalName = LegalName

    @property
    def LegalIdCardType(self):
        """机构法人/经营者证件类型
        :rtype: str
        """
        return self._LegalIdCardType

    @LegalIdCardType.setter
    def LegalIdCardType(self, LegalIdCardType):
        self._LegalIdCardType = LegalIdCardType

    @property
    def LegalIdCardNumber(self):
        """机构法人/经营者证件号码
        :rtype: str
        """
        return self._LegalIdCardNumber

    @LegalIdCardNumber.setter
    def LegalIdCardNumber(self, LegalIdCardNumber):
        self._LegalIdCardNumber = LegalIdCardNumber

    @property
    def LegalMobile(self):
        """机构法人/经营者/联系人手机号码
        :rtype: str
        """
        return self._LegalMobile

    @LegalMobile.setter
    def LegalMobile(self, LegalMobile):
        self._LegalMobile = LegalMobile

    @property
    def ContactName(self):
        """组织联系人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def VerifyStatus(self):
        """机构实名状态
        :rtype: str
        """
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def VerifiedOn(self):
        """机构通过实名时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VerifiedOn

    @VerifiedOn.setter
    def VerifiedOn(self, VerifiedOn):
        self._VerifiedOn = VerifiedOn

    @property
    def CreatedOn(self):
        """机构创建时间
        :rtype: int
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        """机构更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def VerifyClientIp(self):
        """实名认证的客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyClientIp

    @VerifyClientIp.setter
    def VerifyClientIp(self, VerifyClientIp):
        self._VerifyClientIp = VerifyClientIp

    @property
    def VerifyServerIp(self):
        """实名认证的服务器IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyServerIp

    @VerifyServerIp.setter
    def VerifyServerIp(self, VerifyServerIp):
        self._VerifyServerIp = VerifyServerIp

    @property
    def ContactAddress(self):
        """企业联系地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Address`
        """
        return self._ContactAddress

    @ContactAddress.setter
    def ContactAddress(self, ContactAddress):
        self._ContactAddress = ContactAddress


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Email = params.get("Email")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        self._OrganizationType = params.get("OrganizationType")
        self._IdCardFileType = params.get("IdCardFileType")
        self._BizLicenseFile = params.get("BizLicenseFile")
        self._BizLicenseFileName = params.get("BizLicenseFileName")
        self._LegalName = params.get("LegalName")
        self._LegalIdCardType = params.get("LegalIdCardType")
        self._LegalIdCardNumber = params.get("LegalIdCardNumber")
        self._LegalMobile = params.get("LegalMobile")
        self._ContactName = params.get("ContactName")
        self._VerifyStatus = params.get("VerifyStatus")
        self._VerifiedOn = params.get("VerifiedOn")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._VerifyClientIp = params.get("VerifyClientIp")
        self._VerifyServerIp = params.get("VerifyServerIp")
        if params.get("ContactAddress") is not None:
            self._ContactAddress = Address()
            self._ContactAddress._deserialize(params.get("ContactAddress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFile(AbstractModel):
    """此结构体 (UploadFile) 用于描述多文件上传的文件信息。

    """

    def __init__(self):
        r"""
        :param _FileBody: Base64编码后的文件内容
        :type FileBody: str
        :param _FileName: 文件名
        :type FileName: str
        """
        self._FileBody = None
        self._FileName = None

    @property
    def FileBody(self):
        """Base64编码后的文件内容
        :rtype: str
        """
        return self._FileBody

    @FileBody.setter
    def FileBody(self, FileBody):
        self._FileBody = FileBody

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._FileBody = params.get("FileBody")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesRequest(AbstractModel):
    """UploadFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _BusinessType: 文件对应业务类型，用于区分文件存储路径：
1. TEMPLATE - 模版； 文件类型：.pdf/.html
2. DOCUMENT - 签署过程及签署后的合同文档 文件类型：.pdf/.html
3. FLOW - 签署过程 文件类型：.pdf/.html
4. SEAL - 印章； 文件类型：.jpg/.jpeg/.png
5. BUSINESSLICENSE - 营业执照 文件类型：.jpg/.jpeg/.png
6. IDCARD - 身份证 文件类型：.jpg/.jpeg/.png
        :type BusinessType: str
        :param _FileInfos: 上传文件内容数组，最多支持20个文件
        :type FileInfos: list of UploadFile
        :param _FileUrls: 上传文件链接数组，最多支持20个URL
        :type FileUrls: list of str
        :param _CoverRect: 是否将pdf灰色矩阵置白
true--是，处理置白
false--否，不处理
        :type CoverRect: bool
        :param _FileType: 特殊文件类型需要指定文件类型：
HTML-- .html文件
        :type FileType: str
        :param _CustomIds: 用户自定义ID数组，与上传文件一一对应
        :type CustomIds: list of str
        """
        self._Caller = None
        self._BusinessType = None
        self._FileInfos = None
        self._FileUrls = None
        self._CoverRect = None
        self._FileType = None
        self._CustomIds = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def BusinessType(self):
        """文件对应业务类型，用于区分文件存储路径：
1. TEMPLATE - 模版； 文件类型：.pdf/.html
2. DOCUMENT - 签署过程及签署后的合同文档 文件类型：.pdf/.html
3. FLOW - 签署过程 文件类型：.pdf/.html
4. SEAL - 印章； 文件类型：.jpg/.jpeg/.png
5. BUSINESSLICENSE - 营业执照 文件类型：.jpg/.jpeg/.png
6. IDCARD - 身份证 文件类型：.jpg/.jpeg/.png
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def FileInfos(self):
        """上传文件内容数组，最多支持20个文件
        :rtype: list of UploadFile
        """
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def FileUrls(self):
        """上传文件链接数组，最多支持20个URL
        :rtype: list of str
        """
        return self._FileUrls

    @FileUrls.setter
    def FileUrls(self, FileUrls):
        self._FileUrls = FileUrls

    @property
    def CoverRect(self):
        """是否将pdf灰色矩阵置白
true--是，处理置白
false--否，不处理
        :rtype: bool
        """
        return self._CoverRect

    @CoverRect.setter
    def CoverRect(self, CoverRect):
        self._CoverRect = CoverRect

    @property
    def FileType(self):
        """特殊文件类型需要指定文件类型：
HTML-- .html文件
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CustomIds(self):
        """用户自定义ID数组，与上传文件一一对应
        :rtype: list of str
        """
        return self._CustomIds

    @CustomIds.setter
    def CustomIds(self, CustomIds):
        self._CustomIds = CustomIds


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._BusinessType = params.get("BusinessType")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = UploadFile()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        self._FileUrls = params.get("FileUrls")
        self._CoverRect = params.get("CoverRect")
        self._FileType = params.get("FileType")
        self._CustomIds = params.get("CustomIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesResponse(AbstractModel):
    """UploadFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileIds: 文件id数组
        :type FileIds: list of str
        :param _TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileIds = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FileIds(self):
        """文件id数组
        :rtype: list of str
        """
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def TotalCount(self):
        """上传成功文件数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileIds = params.get("FileIds")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class UserDescribe(AbstractModel):
    """此结构体 (UserDescribe) 用于描述个人帐号查询结果。

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _Mobile: 手机号，隐藏中间4位数字，用*代替
        :type Mobile: str
        :param _CreatedOn: 注册时间点 (UNIX时间戳)
        :type CreatedOn: int
        :param _VerifyStatus: 实名认证状态：
0 - 未实名；
1 - 通过实名
        :type VerifyStatus: int
        :param _Name: 真实姓名
        :type Name: str
        :param _VerifiedOn: 实名认证通过时间 (UNIX时间戳)
        :type VerifiedOn: int
        :param _IdCardType: 身份证件类型; 
ID_CARD - 居民身份证；
PASSPORT - 护照；
MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证；
MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证；
HOUSEHOLD_REGISTER - 户口本；
TEMP_ID_CARD - 临时居民身份证
        :type IdCardType: str
        :param _IdCardNumber: 身份证件号码 (脱敏)
        :type IdCardNumber: str
        """
        self._UserId = None
        self._Mobile = None
        self._CreatedOn = None
        self._VerifyStatus = None
        self._Name = None
        self._VerifiedOn = None
        self._IdCardType = None
        self._IdCardNumber = None

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Mobile(self):
        """手机号，隐藏中间4位数字，用*代替
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def CreatedOn(self):
        """注册时间点 (UNIX时间戳)
        :rtype: int
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def VerifyStatus(self):
        """实名认证状态：
0 - 未实名；
1 - 通过实名
        :rtype: int
        """
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def Name(self):
        """真实姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VerifiedOn(self):
        """实名认证通过时间 (UNIX时间戳)
        :rtype: int
        """
        return self._VerifiedOn

    @VerifiedOn.setter
    def VerifiedOn(self, VerifiedOn):
        self._VerifiedOn = VerifiedOn

    @property
    def IdCardType(self):
        """身份证件类型; 
ID_CARD - 居民身份证；
PASSPORT - 护照；
MAINLAND_TRAVEL_PERMIT_FOR_HONGKONG_AND_MACAO_RESIDENTS - 港澳居民来往内地通行证；
MAINLAND_TRAVEL_PERMIT_FOR_TAIWAN_RESIDENTS - 台湾居民来往大陆通行证；
HOUSEHOLD_REGISTER - 户口本；
TEMP_ID_CARD - 临时居民身份证
        :rtype: str
        """
        return self._IdCardType

    @IdCardType.setter
    def IdCardType(self, IdCardType):
        self._IdCardType = IdCardType

    @property
    def IdCardNumber(self):
        """身份证件号码 (脱敏)
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Mobile = params.get("Mobile")
        self._CreatedOn = params.get("CreatedOn")
        self._VerifyStatus = params.get("VerifyStatus")
        self._Name = params.get("Name")
        self._VerifiedOn = params.get("VerifiedOn")
        self._IdCardType = params.get("IdCardType")
        self._IdCardNumber = params.get("IdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySubOrganizationRequest(AbstractModel):
    """VerifySubOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息，该接口SubOrganizationId必填
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _OpenId: 机构在第三方的唯一标识，32位定长字符串，与 Caller 中 SubOrgnizationId 二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :type OpenId: str
        """
        self._Caller = None
        self._OpenId = None

    @property
    def Caller(self):
        """调用方信息，该接口SubOrganizationId必填
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def OpenId(self):
        """机构在第三方的唯一标识，32位定长字符串，与 Caller 中 SubOrgnizationId 二者至少需要传入一个，全部传入时则使用 SubOrganizationId 信息
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._OpenId = params.get("OpenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySubOrganizationResponse(AbstractModel):
    """VerifySubOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubOrganizationId: 子机构ID
        :type SubOrganizationId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubOrganizationId = None
        self._RequestId = None

    @property
    def SubOrganizationId(self):
        """子机构ID
        :rtype: str
        """
        return self._SubOrganizationId

    @SubOrganizationId.setter
    def SubOrganizationId(self, SubOrganizationId):
        self._SubOrganizationId = SubOrganizationId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubOrganizationId = params.get("SubOrganizationId")
        self._RequestId = params.get("RequestId")


class VerifyUserRequest(AbstractModel):
    """VerifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Caller: 调用方信息
        :type Caller: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        :param _UserId: 电子签平台用户ID
        :type UserId: str
        :param _CertificateRequired: 是否需要下发个人长效证书，默认为false
注：如您有下发个人长效证书需求，请提前邮件至e-contract@oa.com进行申请。
        :type CertificateRequired: bool
        """
        self._Caller = None
        self._UserId = None
        self._CertificateRequired = None

    @property
    def Caller(self):
        """调用方信息
        :rtype: :class:`tencentcloud.essbasic.v20201222.models.Caller`
        """
        return self._Caller

    @Caller.setter
    def Caller(self, Caller):
        self._Caller = Caller

    @property
    def UserId(self):
        """电子签平台用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CertificateRequired(self):
        """是否需要下发个人长效证书，默认为false
注：如您有下发个人长效证书需求，请提前邮件至e-contract@oa.com进行申请。
        :rtype: bool
        """
        return self._CertificateRequired

    @CertificateRequired.setter
    def CertificateRequired(self, CertificateRequired):
        self._CertificateRequired = CertificateRequired


    def _deserialize(self, params):
        if params.get("Caller") is not None:
            self._Caller = Caller()
            self._Caller._deserialize(params.get("Caller"))
        self._UserId = params.get("UserId")
        self._CertificateRequired = params.get("CertificateRequired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyUserResponse(AbstractModel):
    """VerifyUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 电子签平台用户ID
        :type UserId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        """电子签平台用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")