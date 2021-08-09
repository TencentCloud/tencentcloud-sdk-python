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


class Acct(AbstractModel):
    """账户信息

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，见证子账户的账号（可重复）
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctNo: str\n        :param SubAcctProperty: STRING(10)，见证子账户的属性（可重复。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号）
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctProperty: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码（可重复）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranNetMemberCode: str\n        :param SubAcctName: STRING(150)，见证子账户的名称（可重复）
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctName: str\n        :param AcctAvailBal: STRING(20)，见证子账户可用余额（可重复）
注意：此字段可能返回 null，表示取不到有效值。\n        :type AcctAvailBal: str\n        :param CashAmt: STRING(20)，见证子账户可提现金额（可重复。开户日期或修改日期）
注意：此字段可能返回 null，表示取不到有效值。\n        :type CashAmt: str\n        :param MaintenanceDate: STRING(8)，维护日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaintenanceDate: str\n        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.TranNetMemberCode = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgencyClientInfo(AbstractModel):
    """经办人信息

    """

    def __init__(self):
        """
        :param AgencyClientName: 经办人姓名，存在经办人必输\n        :type AgencyClientName: str\n        :param AgencyClientGlobalType: 经办人证件类型，存在经办人必输\n        :type AgencyClientGlobalType: str\n        :param AgencyClientGlobalId: 经办人证件号，存在经办人必输\n        :type AgencyClientGlobalId: str\n        :param AgencyClientMobile: 经办人手机号，存在经办人必输\n        :type AgencyClientMobile: str\n        """
        self.AgencyClientName = None
        self.AgencyClientGlobalType = None
        self.AgencyClientGlobalId = None
        self.AgencyClientMobile = None


    def _deserialize(self, params):
        self.AgencyClientName = params.get("AgencyClientName")
        self.AgencyClientGlobalType = params.get("AgencyClientGlobalType")
        self.AgencyClientGlobalId = params.get("AgencyClientGlobalId")
        self.AgencyClientMobile = params.get("AgencyClientMobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTaxPayment(AbstractModel):
    """代理商完税证明

    """

    def __init__(self):
        """
        :param AnchorId: 主播银行账号\n        :type AnchorId: str\n        :param AnchorName: 主播姓名\n        :type AnchorName: str\n        :param AnchorIDCard: 主播身份证\n        :type AnchorIDCard: str\n        :param StartTime: 纳税的开始时间，格式yyyy-MM-dd\n        :type StartTime: str\n        :param EndTime: 纳税的结束时间，格式yyyy-MM-dd\n        :type EndTime: str\n        :param Amount: 流水金额。以“分”为单位\n        :type Amount: int\n        :param Tax: 应缴税款。以“分”为单位\n        :type Tax: int\n        """
        self.AnchorId = None
        self.AnchorName = None
        self.AnchorIDCard = None
        self.StartTime = None
        self.EndTime = None
        self.Amount = None
        self.Tax = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.AnchorName = params.get("AnchorName")
        self.AnchorIDCard = params.get("AnchorIDCard")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Amount = params.get("Amount")
        self.Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTaxPaymentBatch(AbstractModel):
    """代理商完税证明批次信息

    """

    def __init__(self):
        """
        :param StatusMsg: 状态消息\n        :type StatusMsg: str\n        :param BatchNum: 批次号\n        :type BatchNum: int\n        :param InfoNum: 录入记录的条数\n        :type InfoNum: int\n        :param RawElectronicCertUrl: 源电子凭证下载地址\n        :type RawElectronicCertUrl: str\n        :param AgentId: 代理商账号\n        :type AgentId: str\n        :param FileName: 文件名\n        :type FileName: str\n        :param StatusCode: 状态码。0表示下载成功\n        :type StatusCode: int\n        :param Channel: 渠道号\n        :type Channel: int\n        :param Type: 0-视同，1-个体工商户\n        :type Type: int\n        """
        self.StatusMsg = None
        self.BatchNum = None
        self.InfoNum = None
        self.RawElectronicCertUrl = None
        self.AgentId = None
        self.FileName = None
        self.StatusCode = None
        self.Channel = None
        self.Type = None


    def _deserialize(self, params):
        self.StatusMsg = params.get("StatusMsg")
        self.BatchNum = params.get("BatchNum")
        self.InfoNum = params.get("InfoNum")
        self.RawElectronicCertUrl = params.get("RawElectronicCertUrl")
        self.AgentId = params.get("AgentId")
        self.FileName = params.get("FileName")
        self.StatusCode = params.get("StatusCode")
        self.Channel = params.get("Channel")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnchorContractInfo(AbstractModel):
    """主播签约信息

    """

    def __init__(self):
        """
        :param AnchorId: 主播ID\n        :type AnchorId: str\n        :param AnchorName: 主播名称\n        :type AnchorName: str\n        :param AgentId: 代理商ID\n        :type AgentId: str\n        :param AgentName: 代理商名称\n        :type AgentName: str\n        :param IdNo: 主播身份证号\n        :type IdNo: str\n        """
        self.AnchorId = None
        self.AnchorName = None
        self.AgentId = None
        self.AgentName = None
        self.IdNo = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.AnchorName = params.get("AnchorName")
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        self.IdNo = params.get("IdNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyApplicationMaterialRequest(AbstractModel):
    """ApplyApplicationMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param TransactionId: 对接方汇出指令编号\n        :type TransactionId: str\n        :param DeclareId: 申报流水号\n        :type DeclareId: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param SourceCurrency: 源币种\n        :type SourceCurrency: str\n        :param TargetCurrency: 目的币种\n        :type TargetCurrency: str\n        :param TradeCode: 贸易编码\n        :type TradeCode: str\n        :param OriginalDeclareId: 原申报流水号\n        :type OriginalDeclareId: str\n        :param SourceAmount: 源金额\n        :type SourceAmount: int\n        :param TargetAmount: 目的金额\n        :type TargetAmount: int\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.TransactionId = None
        self.DeclareId = None
        self.PayerId = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.TradeCode = None
        self.OriginalDeclareId = None
        self.SourceAmount = None
        self.TargetAmount = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.DeclareId = params.get("DeclareId")
        self.PayerId = params.get("PayerId")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TradeCode = params.get("TradeCode")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetAmount = params.get("TargetAmount")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyApplicationMaterialResponse(AbstractModel):
    """ApplyApplicationMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 提交申报材料结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyDeclareResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyDeclareData(AbstractModel):
    """提交申报材料结果

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param TransactionId: 第三方指令编号\n        :type TransactionId: str\n        :param Status: 受理状态\n        :type Status: str\n        :param DeclareId: 申报流水号\n        :type DeclareId: str\n        :param OriginalDeclareId: 原申报流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalDeclareId: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        """
        self.MerchantId = None
        self.TransactionId = None
        self.Status = None
        self.DeclareId = None
        self.OriginalDeclareId = None
        self.PayerId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.Status = params.get("Status")
        self.DeclareId = params.get("DeclareId")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.PayerId = params.get("PayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDeclareResult(AbstractModel):
    """提交申报材料结果

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Data: 提交申报材料数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareData`\n        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyDeclareData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOutwardOrderData(AbstractModel):
    """汇出指令申请数据

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param TransactionId: 对接方汇出指令编号\n        :type TransactionId: str\n        :param Status: 受理状态\n        :type Status: str\n        """
        self.MerchantId = None
        self.TransactionId = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOutwardOrderRequest(AbstractModel):
    """ApplyOutwardOrder请求参数结构体

    """

    def __init__(self):
        """
        :param TransactionId: 对接方汇出指令编号\n        :type TransactionId: str\n        :param PricingCurrency: 定价币种\n        :type PricingCurrency: str\n        :param SourceCurrency: 源币种\n        :type SourceCurrency: str\n        :param TargetCurrency: 目的币种\n        :type TargetCurrency: str\n        :param PayeeType: 收款人类型（银行卡填"BANK_ACCOUNT"）\n        :type PayeeType: str\n        :param PayeeAccount: 收款人账号\n        :type PayeeAccount: str\n        :param SourceAmount: 源币种金额\n        :type SourceAmount: float\n        :param TargetAmount: 目的金额\n        :type TargetAmount: float\n        :param PayeeName: 收款人姓名（PayeeType为"BANK_COUNT"时必填）\n        :type PayeeName: str\n        :param PayeeAddress: 收款人地址（PayeeType为"BANK_COUNT"时必填）\n        :type PayeeAddress: str\n        :param PayeeBankAccountType: 收款人银行账号类型（PayeeType为"BANK_COUNT"时必填）
个人填"INDIVIDUAL"
企业填"CORPORATE"\n        :type PayeeBankAccountType: str\n        :param PayeeCountryCode: 收款人国家或地区编码（PayeeType为"BANK_COUNT"时必填）\n        :type PayeeCountryCode: str\n        :param PayeeBankName: 收款人开户银行名称（PayeeType为"BANK_COUNT"时必填）\n        :type PayeeBankName: str\n        :param PayeeBankAddress: 收款人开户银行地址（PayeeType为"BANK_COUNT"时必填）\n        :type PayeeBankAddress: str\n        :param PayeeBankDistrict: 收款人开户银行所在国家或地区编码（PayeeType为"BANK_COUNT"时必填）\n        :type PayeeBankDistrict: str\n        :param PayeeBankSwiftCode: 收款银行SwiftCode（PayeeType为"BANK_COUNT"时必填）\n        :type PayeeBankSwiftCode: str\n        :param PayeeBankType: 收款银行国际编码类型\n        :type PayeeBankType: str\n        :param PayeeBankCode: 收款银行国际编码\n        :type PayeeBankCode: str\n        :param ReferenceForBeneficiary: 收款人附言\n        :type ReferenceForBeneficiary: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.TransactionId = None
        self.PricingCurrency = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.PayeeType = None
        self.PayeeAccount = None
        self.SourceAmount = None
        self.TargetAmount = None
        self.PayeeName = None
        self.PayeeAddress = None
        self.PayeeBankAccountType = None
        self.PayeeCountryCode = None
        self.PayeeBankName = None
        self.PayeeBankAddress = None
        self.PayeeBankDistrict = None
        self.PayeeBankSwiftCode = None
        self.PayeeBankType = None
        self.PayeeBankCode = None
        self.ReferenceForBeneficiary = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.PricingCurrency = params.get("PricingCurrency")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.PayeeType = params.get("PayeeType")
        self.PayeeAccount = params.get("PayeeAccount")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetAmount = params.get("TargetAmount")
        self.PayeeName = params.get("PayeeName")
        self.PayeeAddress = params.get("PayeeAddress")
        self.PayeeBankAccountType = params.get("PayeeBankAccountType")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.PayeeBankName = params.get("PayeeBankName")
        self.PayeeBankAddress = params.get("PayeeBankAddress")
        self.PayeeBankDistrict = params.get("PayeeBankDistrict")
        self.PayeeBankSwiftCode = params.get("PayeeBankSwiftCode")
        self.PayeeBankType = params.get("PayeeBankType")
        self.PayeeBankCode = params.get("PayeeBankCode")
        self.ReferenceForBeneficiary = params.get("ReferenceForBeneficiary")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOutwardOrderResponse(AbstractModel):
    """ApplyOutwardOrder返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 汇出指令申请\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyOutwardOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyOutwardOrderResult(AbstractModel):
    """汇出指令申请结果

    """

    def __init__(self):
        """
        :param Data: 汇出指令申请数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderData`\n        :param Code: 错误码\n        :type Code: str\n        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplyOutwardOrderData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPayerInfoRequest(AbstractModel):
    """ApplyPayerInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param PayerType: 付款人类型 (个人: INDIVIDUAL, 企业: CORPORATE)\n        :type PayerType: str\n        :param PayerName: 付款人姓名\n        :type PayerName: str\n        :param PayerIdType: 付款人证件类型 (身份证: ID_CARD, 统一社会信用代码: UNIFIED_CREDIT_CODE)\n        :type PayerIdType: str\n        :param PayerIdNo: 付款人证件号\n        :type PayerIdNo: str\n        :param PayerCountryCode: 付款人常驻国家或地区编码 (见常见问题-国家/地区编码)\n        :type PayerCountryCode: str\n        :param PayerContactName: 付款人联系人名称\n        :type PayerContactName: str\n        :param PayerContactNumber: 付款人联系电话\n        :type PayerContactNumber: str\n        :param PayerEmailAddress: 付款人联系邮箱\n        :type PayerEmailAddress: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.PayerId = None
        self.PayerType = None
        self.PayerName = None
        self.PayerIdType = None
        self.PayerIdNo = None
        self.PayerCountryCode = None
        self.PayerContactName = None
        self.PayerContactNumber = None
        self.PayerEmailAddress = None
        self.Profile = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.PayerType = params.get("PayerType")
        self.PayerName = params.get("PayerName")
        self.PayerIdType = params.get("PayerIdType")
        self.PayerIdNo = params.get("PayerIdNo")
        self.PayerCountryCode = params.get("PayerCountryCode")
        self.PayerContactName = params.get("PayerContactName")
        self.PayerContactNumber = params.get("PayerContactNumber")
        self.PayerEmailAddress = params.get("PayerEmailAddress")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPayerInfoResponse(AbstractModel):
    """ApplyPayerInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 付款人申请结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyPayerinfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyPayerinfoData(AbstractModel):
    """付款人申请结果

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param Status: 状态\n        :type Status: str\n        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailReason: str\n        """
        self.MerchantId = None
        self.PayerId = None
        self.Status = None
        self.FailReason = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPayerinfoResult(AbstractModel):
    """付款人申请结果

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Data: 数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoData`\n        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyPayerinfoData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyReWithdrawalRequest(AbstractModel):
    """ApplyReWithdrawal请求参数结构体

    """

    def __init__(self):
        """
        :param BusinessType: 聚鑫业务类型\n        :type BusinessType: int\n        :param MidasSecretId: 由平台客服提供的计费密钥Id\n        :type MidasSecretId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param Body: 提现信息\n        :type Body: :class:`tencentcloud.cpdp.v20190820.models.WithdrawBill`\n        :param MidasAppId: 聚鑫业务ID\n        :type MidasAppId: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.BusinessType = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Body = None
        self.MidasAppId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.BusinessType = params.get("BusinessType")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        if params.get("Body") is not None:
            self.Body = WithdrawBill()
            self.Body._deserialize(params.get("Body"))
        self.MidasAppId = params.get("MidasAppId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyReWithdrawalResponse(AbstractModel):
    """ApplyReWithdrawal返回参数结构体

    """

    def __init__(self):
        """
        :param WithdrawOrderId: 重新提现业务订单号\n        :type WithdrawOrderId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.WithdrawOrderId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        self.RequestId = params.get("RequestId")


class ApplyTradeData(AbstractModel):
    """提交贸易材料结果

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param TradeFileId: 贸易材料流水号\n        :type TradeFileId: str\n        :param TradeCurrency: 交易币种\n        :type TradeCurrency: str\n        :param TradeAmount: 交易金额\n        :type TradeAmount: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param Status: 状态\n        :type Status: str\n        """
        self.MerchantId = None
        self.TradeFileId = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.PayerId = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TradeFileId = params.get("TradeFileId")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTradeRequest(AbstractModel):
    """ApplyTrade请求参数结构体

    """

    def __init__(self):
        """
        :param TradeFileId: 贸易材料流水号\n        :type TradeFileId: str\n        :param TradeOrderId: 贸易材料订单号\n        :type TradeOrderId: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param PayeeName: 收款人姓名\n        :type PayeeName: str\n        :param PayeeCountryCode: 收款人常驻国家或地区编码 (见常见问题)\n        :type PayeeCountryCode: str\n        :param TradeType: 贸易类型 (GOODS: 商品, SERVICE: 服务)\n        :type TradeType: str\n        :param TradeTime: 交易时间 (格式: yyyyMMdd)\n        :type TradeTime: str\n        :param TradeCurrency: 交易币种\n        :type TradeCurrency: str\n        :param TradeAmount: 交易金额\n        :type TradeAmount: float\n        :param TradeName: 交易名称 
(TradeType=GOODS时填写物品名称，可填写多个，格式无要求；
TradeType=SERVICE时填写贸易类别，见常见问题-贸易类别)\n        :type TradeName: str\n        :param TradeCount: 交易数量 (TradeType=GOODS 填写物品数量, TradeType=SERVICE填写服务次数)\n        :type TradeCount: int\n        :param GoodsCarrier: 货贸承运人 (TradeType=GOODS 必填)\n        :type GoodsCarrier: str\n        :param ServiceDetail: 服贸交易细节 (TradeType=GOODS 必填, 见常见问题-交易细节)\n        :type ServiceDetail: str\n        :param ServiceTime: 服贸服务时间 (TradeType=GOODS 必填, 见常见问题-服务时间)\n        :type ServiceTime: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.TradeFileId = None
        self.TradeOrderId = None
        self.PayerId = None
        self.PayeeName = None
        self.PayeeCountryCode = None
        self.TradeType = None
        self.TradeTime = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.TradeName = None
        self.TradeCount = None
        self.GoodsCarrier = None
        self.ServiceDetail = None
        self.ServiceTime = None
        self.Profile = None


    def _deserialize(self, params):
        self.TradeFileId = params.get("TradeFileId")
        self.TradeOrderId = params.get("TradeOrderId")
        self.PayerId = params.get("PayerId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.TradeType = params.get("TradeType")
        self.TradeTime = params.get("TradeTime")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.TradeName = params.get("TradeName")
        self.TradeCount = params.get("TradeCount")
        self.GoodsCarrier = params.get("GoodsCarrier")
        self.ServiceDetail = params.get("ServiceDetail")
        self.ServiceTime = params.get("ServiceTime")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTradeResponse(AbstractModel):
    """ApplyTrade返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 提交贸易材料结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyTradeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyTradeResult(AbstractModel):
    """提交贸易材料结果

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Data: 提交贸易材料数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeData`\n        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyTradeData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyWithdrawalRequest(AbstractModel):
    """ApplyWithdrawal请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SettleAcctNo: 用于提现
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SettleAcctNo: str\n        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SettleAcctName: str\n        :param CurrencyType: 币种 RMB\n        :type CurrencyType: str\n        :param CurrencyUnit: 单位，1：元，2：角，3：分\n        :type CurrencyUnit: int\n        :param CurrencyAmt: 金额\n        :type CurrencyAmt: str\n        :param TranWebName: 交易网名称\n        :type TranWebName: str\n        :param IdType: 会员证件类型\n        :type IdType: str\n        :param IdCode: 会员证件号码
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type IdCode: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param CommissionAmount: 手续费金额\n        :type CommissionAmount: str\n        :param WithdrawOrderId: 提现单号，长度32字节\n        :type WithdrawOrderId: str\n        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None
        self.TranWebName = None
        self.IdType = None
        self.IdCode = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None
        self.CommissionAmount = None
        self.WithdrawOrderId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")
        self.TranWebName = params.get("TranWebName")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.CommissionAmount = params.get("CommissionAmount")
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyWithdrawalResponse(AbstractModel):
    """ApplyWithdrawal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BankCardItem(AbstractModel):
    """绑卡列表

    """

    def __init__(self):
        """
        :param EiconBankBranchId: 超级网银行号\n        :type EiconBankBranchId: str\n        :param CnapsBranchId: 大小额行号\n        :type CnapsBranchId: str\n        :param SettleAcctType: 结算账户类型
1 – 本行账户
2 – 他行账户\n        :type SettleAcctType: int\n        :param SettleAcctName: 结算账户户名
<敏感信息>\n        :type SettleAcctName: str\n        :param AcctBranchName: 开户行名称\n        :type AcctBranchName: str\n        :param SettleAcctNo: 用于提现
<敏感信息>\n        :type SettleAcctNo: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param BindType: 验证类型
1 – 小额转账验证
2 – 短信验证\n        :type BindType: int\n        :param Mobile: 用于短信验证
BindType==2时必填
<敏感信息>\n        :type Mobile: str\n        :param IdType: 证件类型\n        :type IdType: str\n        :param IdCode: 证件号码
<敏感信息>\n        :type IdCode: str\n        """
        self.EiconBankBranchId = None
        self.CnapsBranchId = None
        self.SettleAcctType = None
        self.SettleAcctName = None
        self.AcctBranchName = None
        self.SettleAcctNo = None
        self.SubAppId = None
        self.BindType = None
        self.Mobile = None
        self.IdType = None
        self.IdCode = None


    def _deserialize(self, params):
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.SettleAcctType = params.get("SettleAcctType")
        self.SettleAcctName = params.get("SettleAcctName")
        self.AcctBranchName = params.get("AcctBranchName")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.Mobile = params.get("Mobile")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAcctRequest(AbstractModel):
    """BindAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param BindType: 1 – 小额转账验证
2 – 短信验证
3 - 一分钱转账验证，无需再调CheckAcct验证绑卡
4 - 银行四要素验证，无需再调CheckAcct验证绑卡
每个结算账户每天只能使用一次小额转账验证\n        :type BindType: int\n        :param SettleAcctNo: 用于提现
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SettleAcctNo: str\n        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SettleAcctName: str\n        :param SettleAcctType: 1 – 本行账户
2 – 他行账户\n        :type SettleAcctType: int\n        :param IdType: 证件类型，见《证件类型》表\n        :type IdType: str\n        :param IdCode: 证件号码
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type IdCode: str\n        :param AcctBranchName: 开户行名称\n        :type AcctBranchName: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param Mobile: 用于短信验证
BindType==2时必填
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type Mobile: str\n        :param CnapsBranchId: 大小额行号，超级网银行号和大小额行号
二选一\n        :type CnapsBranchId: str\n        :param EiconBankBranchId: 超级网银行号，超级网银行号和大小额行号
二选一\n        :type EiconBankBranchId: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param AgencyClientInfo: 经办人信息\n        :type AgencyClientInfo: :class:`tencentcloud.cpdp.v20190820.models.AgencyClientInfo`\n        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.SettleAcctType = None
        self.IdType = None
        self.IdCode = None
        self.AcctBranchName = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.EncryptType = None
        self.MidasEnvironment = None
        self.AgencyClientInfo = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.SettleAcctType = params.get("SettleAcctType")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.AcctBranchName = params.get("AcctBranchName")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        if params.get("AgencyClientInfo") is not None:
            self.AgencyClientInfo = AgencyClientInfo()
            self.AgencyClientInfo._deserialize(params.get("AgencyClientInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAcctResponse(AbstractModel):
    """BindAcct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindRelateAccReUnionPayRequest(AbstractModel):
    """BindRelateAccReUnionPay请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）\n        :type TranNetMemberCode: str\n        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctUnionPay接口中的“会员的待绑定账户的账号”）\n        :type MemberAcctNo: str\n        :param MessageCheckCode: STRING(20)，短信验证码（即 BindRelateAcctUnionPay接口中的手机所接收到的短信验证码）\n        :type MessageCheckCode: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.MessageCheckCode = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.MessageCheckCode = params.get("MessageCheckCode")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRelateAccReUnionPayResponse(AbstractModel):
    """BindRelateAccReUnionPay返回参数结构体

    """

    def __init__(self):
        """
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class BindRelateAcctSmallAmountRequest(AbstractModel):
    """BindRelateAcctSmallAmount请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）\n        :type TranNetMemberCode: str\n        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）\n        :type MemberName: str\n        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）\n        :type MemberGlobalType: str\n        :param MemberGlobalId: STRING(32)，会员证件号码\n        :type MemberGlobalId: str\n        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）\n        :type MemberAcctNo: str\n        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）\n        :type BankType: str\n        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称\n        :type AcctOpenBranchName: str\n        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）\n        :type Mobile: str\n        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）\n        :type CnapsBranchId: str\n        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）\n        :type EiconBankBranchId: str\n        :param ReservedMsg: STRING(1027)，转账方式（1: 往账鉴权(默认值); 2: 来账鉴权）\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRelateAcctSmallAmountResponse(AbstractModel):
    """BindRelateAcctSmallAmount返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域（来账鉴权的方式下，此字段的值为客户需往监管账户转入的金额。在同名子账户绑定的场景下，若返回""VERIFIED""则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class BindRelateAcctUnionPayRequest(AbstractModel):
    """BindRelateAcctUnionPay请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）\n        :type TranNetMemberCode: str\n        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）\n        :type MemberName: str\n        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）\n        :type MemberGlobalType: str\n        :param MemberGlobalId: STRING(32)，会员证件号码\n        :type MemberGlobalId: str\n        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）\n        :type MemberAcctNo: str\n        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）\n        :type BankType: str\n        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）\n        :type AcctOpenBranchName: str\n        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）\n        :type Mobile: str\n        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）\n        :type CnapsBranchId: str\n        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）\n        :type EiconBankBranchId: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.MrchCode = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRelateAcctUnionPayResponse(AbstractModel):
    """BindRelateAcctUnionPay返回参数结构体

    """

    def __init__(self):
        """
        :param ReservedMsg: STRING(1027)，保留域（在同名子账户绑定的场景下，若返回"VERIFIED"则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class ChannelContractInfo(AbstractModel):
    """米大师内部存放的合约信息

    """

    def __init__(self):
        """
        :param OutContractCode: 外部合约协议号\n        :type OutContractCode: str\n        :param ChannelContractCode: 米大师内部生成的合约协议号\n        :type ChannelContractCode: str\n        """
        self.OutContractCode = None
        self.ChannelContractCode = None


    def _deserialize(self, params):
        self.OutContractCode = params.get("OutContractCode")
        self.ChannelContractCode = params.get("ChannelContractCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelReturnContractInfo(AbstractModel):
    """米大师内部生成的合约信息

    """

    def __init__(self):
        """
        :param ContractStatus: 平台合约状态
协议状态，枚举值：
CONTRACT_STATUS_SIGNED：已签约
CONTRACT_STATUS_TERMINATED：未签约
CONTRACT_STATUS_PENDING：签约进行中\n        :type ContractStatus: str\n        :param ChannelContractInfo: 米大师内部存放的合约信息\n        :type ChannelContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ChannelContractInfo`\n        """
        self.ContractStatus = None
        self.ChannelContractInfo = None


    def _deserialize(self, params):
        self.ContractStatus = params.get("ContractStatus")
        if params.get("ChannelContractInfo") is not None:
            self.ChannelContractInfo = ChannelContractInfo()
            self.ChannelContractInfo._deserialize(params.get("ChannelContractInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAcctRequest(AbstractModel):
    """CheckAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param BindType: 1 – 小额转账验证
2 – 短信验证
每个结算账户每天只能使用一次小额转账验证\n        :type BindType: int\n        :param SettleAcctNo: 结算账户账号
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SettleAcctNo: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param CheckCode: 短信验证码或指令号
BindType==2必填，平安渠道必填\n        :type CheckCode: str\n        :param CurrencyType: 币种 RMB
BindType==1必填\n        :type CurrencyType: str\n        :param CurrencyUnit: 单位
1：元，2：角，3：分
BindType==1必填\n        :type CurrencyUnit: int\n        :param CurrencyAmt: 金额
BindType==1必填\n        :type CurrencyAmt: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CheckCode = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CheckCode = params.get("CheckCode")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAcctResponse(AbstractModel):
    """CheckAcct返回参数结构体

    """

    def __init__(self):
        """
        :param FrontSeqNo: 前置流水号，请保存\n        :type FrontSeqNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.RequestId = params.get("RequestId")


class CheckAmountRequest(AbstractModel):
    """CheckAmount请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）\n        :type TranNetMemberCode: str\n        :param TakeCashAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户的账号”）\n        :type TakeCashAcctNo: str\n        :param AuthAmt: STRING(20)，鉴权验证金额（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户收到的验证金额。原小额转账鉴权方式为来账鉴权的情况下此字段须赋值为0.00）\n        :type AuthAmt: str\n        :param Ccy: STRING(3)，币种（默认为RMB）\n        :type Ccy: str\n        :param ReservedMsg: STRING(1027)，原小额转账方式（1: 往账鉴权，此为默认值; 2: 来账鉴权）\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.TakeCashAcctNo = None
        self.AuthAmt = None
        self.Ccy = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.AuthAmt = params.get("AuthAmt")
        self.Ccy = params.get("Ccy")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAmountResponse(AbstractModel):
    """CheckAmount返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）\n        :type FrontSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class ClearItem(AbstractModel):
    """银行在途清算结果信息

    """

    def __init__(self):
        """
        :param Date: STRING(8)，日期（格式: 20190101）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Date: str\n        :param SubAcctType: STRING(40)，子账号类型（子帐号类型。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号; 7: 在途; 8: 理财购买子帐号; 9: 理财赎回子帐号; 10: 平台子拥有结算子帐号）
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctType: str\n        :param ReconcileStatus: STRING(3)，对账状态（0: 成功; 1: 失败）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReconcileStatus: str\n        :param ReconcileReturnMsg: STRING(300)，对账返回信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReconcileReturnMsg: str\n        :param ClearingStatus: STRING(20)，清算状态（0: 成功; 1: 失败; 2: 异常; 3: 待处理）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClearingStatus: str\n        :param ClearingReturnMsg: STRING(2)，清算返回信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClearingReturnMsg: str\n        :param TotalAmt: STRING(300)，待清算总金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalAmt: str\n        """
        self.Date = None
        self.SubAcctType = None
        self.ReconcileStatus = None
        self.ReconcileReturnMsg = None
        self.ClearingStatus = None
        self.ClearingReturnMsg = None
        self.TotalAmt = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.SubAcctType = params.get("SubAcctType")
        self.ReconcileStatus = params.get("ReconcileStatus")
        self.ReconcileReturnMsg = params.get("ReconcileReturnMsg")
        self.ClearingStatus = params.get("ClearingStatus")
        self.ClearingReturnMsg = params.get("ClearingReturnMsg")
        self.TotalAmt = params.get("TotalAmt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseOrderRequest(AbstractModel):
    """CloseOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合\n        :type UserId: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param OutTradeNo: 业务订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo\n        :type OutTradeNo: str\n        :param TransactionId: 聚鑫订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo\n        :type TransactionId: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.UserId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.TransactionId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseOrderResponse(AbstractModel):
    """CloseOrder返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConfirmOrderRequest(AbstractModel):
    """ConfirmOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 分配给商户的AppId\n        :type MerchantAppId: str\n        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。\n        :type OrderNo: str\n        """
        self.MerchantAppId = None
        self.OrderNo = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmOrderResponse(AbstractModel):
    """ConfirmOrder返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 分配给商户的AppId\n        :type MerchantAppId: str\n        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。\n        :type OrderNo: str\n        :param Status: 订单确认状态。0-确认失败
1-确认成功 
2-可疑状态\n        :type Status: str\n        :param Description: 订单确认状态描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantAppId = None
        self.OrderNo = None
        self.Status = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class ContractInfo(AbstractModel):
    """合约信息

    """

    def __init__(self):
        """
        :param ChannelContractMerchantId: 米大师内部签约商户号\n        :type ChannelContractMerchantId: str\n        :param ChannelContractSubMerchantId: 米大师内部签约子商户号
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChannelContractSubMerchantId: str\n        :param ChannelContractAppId: 米大师内部签约应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChannelContractAppId: str\n        :param ChannelContractSubAppId: 米大师内部签约子应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChannelContractSubAppId: str\n        :param OutContractCode: 业务合约协议号\n        :type OutContractCode: str\n        :param ExternalContractUserInfoList: 第三方渠道用户信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalContractUserInfoList: list of ExternalContractUserInfo\n        :param ContractMethod: 签约方式，如 wechat_app ，使用app方式下的微信签\n        :type ContractMethod: str\n        :param ContractSceneId: 合约场景id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContractSceneId: str\n        :param UserInfo: 用户信息\n        :type UserInfo: :class:`tencentcloud.cpdp.v20190820.models.ContractUserInfo`\n        :param ExternalContractData: 第三方渠道签约数据\n        :type ExternalContractData: str\n        """
        self.ChannelContractMerchantId = None
        self.ChannelContractSubMerchantId = None
        self.ChannelContractAppId = None
        self.ChannelContractSubAppId = None
        self.OutContractCode = None
        self.ExternalContractUserInfoList = None
        self.ContractMethod = None
        self.ContractSceneId = None
        self.UserInfo = None
        self.ExternalContractData = None


    def _deserialize(self, params):
        self.ChannelContractMerchantId = params.get("ChannelContractMerchantId")
        self.ChannelContractSubMerchantId = params.get("ChannelContractSubMerchantId")
        self.ChannelContractAppId = params.get("ChannelContractAppId")
        self.ChannelContractSubAppId = params.get("ChannelContractSubAppId")
        self.OutContractCode = params.get("OutContractCode")
        if params.get("ExternalContractUserInfoList") is not None:
            self.ExternalContractUserInfoList = []
            for item in params.get("ExternalContractUserInfoList"):
                obj = ExternalContractUserInfo()
                obj._deserialize(item)
                self.ExternalContractUserInfoList.append(obj)
        self.ContractMethod = params.get("ContractMethod")
        self.ContractSceneId = params.get("ContractSceneId")
        if params.get("UserInfo") is not None:
            self.UserInfo = ContractUserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.ExternalContractData = params.get("ExternalContractData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractOrderInSubOrder(AbstractModel):
    """支付中签约子订单列表

    """

    def __init__(self):
        """
        :param SubMchIncome: 子订单结算应收金额，单位： 分\n        :type SubMchIncome: int\n        :param PlatformIncome: 子订单平台应收金额，单位：分\n        :type PlatformIncome: int\n        :param ProductDetail: 子订单商品详情\n        :type ProductDetail: str\n        :param ProductName: 子订单商品名称\n        :type ProductName: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SubOutTradeNo: 子订单号\n        :type SubOutTradeNo: str\n        :param Amt: 子订单支付金额\n        :type Amt: int\n        :param OriginalAmt: 子订单原始金额\n        :type OriginalAmt: int\n        :param Metadata: 发货标识，由业务在调用聚鑫下单接口的 时候下发\n        :type Metadata: str\n        """
        self.SubMchIncome = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SubAppId = None
        self.SubOutTradeNo = None
        self.Amt = None
        self.OriginalAmt = None
        self.Metadata = None


    def _deserialize(self, params):
        self.SubMchIncome = params.get("SubMchIncome")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.Amt = params.get("Amt")
        self.OriginalAmt = params.get("OriginalAmt")
        self.Metadata = params.get("Metadata")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractOrderRequest(AbstractModel):
    """ContractOrder请求参数结构体

    """

    def __init__(self):
        """
        :param CurrencyType: ISO 货币代码，CNY\n        :type CurrencyType: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param OutTradeNo: 支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合\n        :type OutTradeNo: str\n        :param ProductDetail: 商品详情，需要URL编码\n        :type ProductDetail: str\n        :param ProductId: 商品ID，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合\n        :type ProductId: str\n        :param ProductName: 商品名称，需要URL编码\n        :type ProductName: str\n        :param TotalAmt: 支付金额，单位： 分\n        :type TotalAmt: int\n        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合\n        :type UserId: str\n        :param RealChannel: 银行真实渠道.如:bank_pingan\n        :type RealChannel: str\n        :param OriginalAmt: 原始金额\n        :type OriginalAmt: int\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param ContractNotifyUrl: 签约通知地址\n        :type ContractNotifyUrl: str\n        :param CallbackUrl: Web端回调地址\n        :type CallbackUrl: str\n        :param Channel: 指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定\n        :type Channel: str\n        :param Metadata: 透传字段，支付成功回调透传给应用，用于业务透传自定义内容\n        :type Metadata: str\n        :param Quantity: 购买数量，不传默认为1\n        :type Quantity: int\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SubOrderList: 子订单信息列表，格式：子订单号、子应用ID、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)
注：接入银行或其他支付渠道服务商模式下，必传\n        :type SubOrderList: list of ContractOrderInSubOrder\n        :param TotalMchIncome: 结算应收金额，单位：分\n        :type TotalMchIncome: int\n        :param TotalPlatformIncome: 平台应收金额，单位：分\n        :type TotalPlatformIncome: int\n        :param WxOpenId: 微信公众号/小程序支付时为必选，需要传微信下的openid\n        :type WxOpenId: str\n        :param WxSubOpenId: 在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一\n        :type WxSubOpenId: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param WxAppId: 微信商户应用ID\n        :type WxAppId: str\n        :param WxSubAppId: 微信商户子应用ID\n        :type WxSubAppId: str\n        :param PaymentNotifyUrl: 支付通知地址\n        :type PaymentNotifyUrl: str\n        :param ContractSceneId: 传入调用方在Midas注册签约信息时获得的ContractSceneId。若未在Midas注册签约信息，则传入ExternalContractData。注意：ContractSceneId与ExternalContractData必须二选一传入其中一个\n        :type ContractSceneId: str\n        :param ExternalContractData: 需要按照各个渠道的扩展签约信息规范组装好该字段。若未在Midas注册签约信息，则传入该字段。注意：ContractSceneId与ExternalContractData必须二选一传入其中一个\n        :type ExternalContractData: str\n        :param OutContractCode: 外部签约协议号，唯一标记一个签约关系。仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合\n        :type OutContractCode: str\n        :param AttachData: 透传给第三方渠道的附加数据\n        :type AttachData: str\n        :param ContractDisplayName: 展示用的签约用户名称，若不传入时，默认取UserId\n        :type ContractDisplayName: str\n        """
        self.CurrencyType = None
        self.MidasAppId = None
        self.OutTradeNo = None
        self.ProductDetail = None
        self.ProductId = None
        self.ProductName = None
        self.TotalAmt = None
        self.UserId = None
        self.RealChannel = None
        self.OriginalAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.ContractNotifyUrl = None
        self.CallbackUrl = None
        self.Channel = None
        self.Metadata = None
        self.Quantity = None
        self.SubAppId = None
        self.SubOrderList = None
        self.TotalMchIncome = None
        self.TotalPlatformIncome = None
        self.WxOpenId = None
        self.WxSubOpenId = None
        self.MidasEnvironment = None
        self.WxAppId = None
        self.WxSubAppId = None
        self.PaymentNotifyUrl = None
        self.ContractSceneId = None
        self.ExternalContractData = None
        self.OutContractCode = None
        self.AttachData = None
        self.ContractDisplayName = None


    def _deserialize(self, params):
        self.CurrencyType = params.get("CurrencyType")
        self.MidasAppId = params.get("MidasAppId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.TotalAmt = params.get("TotalAmt")
        self.UserId = params.get("UserId")
        self.RealChannel = params.get("RealChannel")
        self.OriginalAmt = params.get("OriginalAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.ContractNotifyUrl = params.get("ContractNotifyUrl")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Channel = params.get("Channel")
        self.Metadata = params.get("Metadata")
        self.Quantity = params.get("Quantity")
        self.SubAppId = params.get("SubAppId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = ContractOrderInSubOrder()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.TotalMchIncome = params.get("TotalMchIncome")
        self.TotalPlatformIncome = params.get("TotalPlatformIncome")
        self.WxOpenId = params.get("WxOpenId")
        self.WxSubOpenId = params.get("WxSubOpenId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.WxAppId = params.get("WxAppId")
        self.WxSubAppId = params.get("WxSubAppId")
        self.PaymentNotifyUrl = params.get("PaymentNotifyUrl")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ExternalContractData = params.get("ExternalContractData")
        self.OutContractCode = params.get("OutContractCode")
        self.AttachData = params.get("AttachData")
        self.ContractDisplayName = params.get("ContractDisplayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractOrderResponse(AbstractModel):
    """ContractOrder返回参数结构体

    """

    def __init__(self):
        """
        :param TotalAmt: 支付金额，单位： 分\n        :type TotalAmt: int\n        :param OutTradeNo: 应用支付订单号\n        :type OutTradeNo: str\n        :param PayInfo: 支付参数透传给聚鑫SDK（原文透传给SDK即可，不需要解码）\n        :type PayInfo: str\n        :param TransactionId: 聚鑫的交易订单号\n        :type TransactionId: str\n        :param OutContractCode: 外部签约协议号\n        :type OutContractCode: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalAmt = None
        self.OutTradeNo = None
        self.PayInfo = None
        self.TransactionId = None
        self.OutContractCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAmt = params.get("TotalAmt")
        self.OutTradeNo = params.get("OutTradeNo")
        self.PayInfo = params.get("PayInfo")
        self.TransactionId = params.get("TransactionId")
        self.OutContractCode = params.get("OutContractCode")
        self.RequestId = params.get("RequestId")


class ContractSyncInfo(AbstractModel):
    """签约同步信息

    """

    def __init__(self):
        """
        :param ExternalReturnContractInfo: 第三方渠道合约信息\n        :type ExternalReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ExternalReturnContractInfo`\n        :param ExternalContractUserInfo: 第三方渠道用户信息\n        :type ExternalContractUserInfo: list of ExternalContractUserInfo\n        :param ContractMethod: 签约方式，枚举值，
<br/>CONTRACT_METHOD_WECHAT_INVALID: 无效
CONTRACT_METHOD_WECHAT_APP: 微信APP
CONTRACT_METHOD_WECHAT_PUBLIC: 微信公众号
CONTRACT_METHOD_WECHAT_MINIPROGRAM: 微信小程序
CONTRACT_METHOD_WECHAT_H5: 微信H5\n        :type ContractMethod: str\n        :param ContractSceneId: 在米大师侧分配的场景id\n        :type ContractSceneId: str\n        :param ExternalReturnContractData: 调用方从第三方渠道查询到的签约数据，由各个渠道定义\n        :type ExternalReturnContractData: str\n        """
        self.ExternalReturnContractInfo = None
        self.ExternalContractUserInfo = None
        self.ContractMethod = None
        self.ContractSceneId = None
        self.ExternalReturnContractData = None


    def _deserialize(self, params):
        if params.get("ExternalReturnContractInfo") is not None:
            self.ExternalReturnContractInfo = ExternalReturnContractInfo()
            self.ExternalReturnContractInfo._deserialize(params.get("ExternalReturnContractInfo"))
        if params.get("ExternalContractUserInfo") is not None:
            self.ExternalContractUserInfo = []
            for item in params.get("ExternalContractUserInfo"):
                obj = ExternalContractUserInfo()
                obj._deserialize(item)
                self.ExternalContractUserInfo.append(obj)
        self.ContractMethod = params.get("ContractMethod")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ExternalReturnContractData = params.get("ExternalReturnContractData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractUserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        """
        :param UserType: USER_ID: 用户ID
ANONYMOUS: 匿名类型用户ID\n        :type UserType: str\n        :param UserId: 用户类型\n        :type UserId: str\n        """
        self.UserType = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserType = params.get("UserType")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcctRequest(AbstractModel):
    """CreateAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId\n        :type MidasAppId: str\n        :param SubMchId: 业务平台的子商户ID，唯一\n        :type SubMchId: str\n        :param SubMchName: 子商户名称\n        :type SubMchName: str\n        :param Address: 子商户地址\n        :type Address: str\n        :param Contact: 子商户联系人
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type Contact: str\n        :param Mobile: 联系人手机号
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type Mobile: str\n        :param Email: 邮箱 
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type Email: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param SubMchType: 子商户类型：
个人: personal
企业: enterprise
个体工商户: individual
缺省: enterprise\n        :type SubMchType: str\n        :param ShortName: 不填则默认子商户名称\n        :type ShortName: str\n        :param SubMerchantMemberType: 子商户会员类型：
general: 普通子账户
merchant: 商户子账户
缺省: general\n        :type SubMerchantMemberType: str\n        :param SubMerchantKey: 子商户密钥
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SubMerchantKey: str\n        :param SubMerchantPrivateKey: 子商户私钥
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SubMerchantPrivateKey: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param SubAcctNo: 银行生成的子商户账户，已开户的场景需要录入\n        :type SubAcctNo: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param SubMerchantStoreName: 店铺名称
企业、个体工商户必输\n        :type SubMerchantStoreName: str\n        :param OrganizationInfo: 公司信息\n        :type OrganizationInfo: :class:`tencentcloud.cpdp.v20190820.models.OrganizationInfo`\n        """
        self.MidasAppId = None
        self.SubMchId = None
        self.SubMchName = None
        self.Address = None
        self.Contact = None
        self.Mobile = None
        self.Email = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.SubMchType = None
        self.ShortName = None
        self.SubMerchantMemberType = None
        self.SubMerchantKey = None
        self.SubMerchantPrivateKey = None
        self.EncryptType = None
        self.SubAcctNo = None
        self.MidasEnvironment = None
        self.SubMerchantStoreName = None
        self.OrganizationInfo = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.SubMchName = params.get("SubMchName")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.SubMchType = params.get("SubMchType")
        self.ShortName = params.get("ShortName")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")
        self.SubMerchantKey = params.get("SubMerchantKey")
        self.SubMerchantPrivateKey = params.get("SubMerchantPrivateKey")
        self.EncryptType = params.get("EncryptType")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.SubMerchantStoreName = params.get("SubMerchantStoreName")
        if params.get("OrganizationInfo") is not None:
            self.OrganizationInfo = OrganizationInfo()
            self.OrganizationInfo._deserialize(params.get("OrganizationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcctResponse(AbstractModel):
    """CreateAcct返回参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SubAcctNo: 银行生成的子商户账户\n        :type SubAcctNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SubAppId = None
        self.SubAcctNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.RequestId = params.get("RequestId")


class CreateAgentTaxPaymentInfosRequest(AbstractModel):
    """CreateAgentTaxPaymentInfos请求参数结构体

    """

    def __init__(self):
        """
        :param AgentId: 代理商ID\n        :type AgentId: str\n        :param Channel: 平台渠道\n        :type Channel: int\n        :param Type: 类型。0-视同，1-个体工商户\n        :type Type: int\n        :param RawElectronicCertUrl: 源电子凭证下载地址\n        :type RawElectronicCertUrl: str\n        :param FileName: 文件名\n        :type FileName: str\n        :param AgentTaxPaymentInfos: 完税信息\n        :type AgentTaxPaymentInfos: list of AgentTaxPayment\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.AgentId = None
        self.Channel = None
        self.Type = None
        self.RawElectronicCertUrl = None
        self.FileName = None
        self.AgentTaxPaymentInfos = None
        self.Profile = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.Channel = params.get("Channel")
        self.Type = params.get("Type")
        self.RawElectronicCertUrl = params.get("RawElectronicCertUrl")
        self.FileName = params.get("FileName")
        if params.get("AgentTaxPaymentInfos") is not None:
            self.AgentTaxPaymentInfos = []
            for item in params.get("AgentTaxPaymentInfos"):
                obj = AgentTaxPayment()
                obj._deserialize(item)
                self.AgentTaxPaymentInfos.append(obj)
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentTaxPaymentInfosResponse(AbstractModel):
    """CreateAgentTaxPaymentInfos返回参数结构体

    """

    def __init__(self):
        """
        :param AgentTaxPaymentBatch: 代理商完税证明批次信息\n        :type AgentTaxPaymentBatch: :class:`tencentcloud.cpdp.v20190820.models.AgentTaxPaymentBatch`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentTaxPaymentBatch = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentTaxPaymentBatch") is not None:
            self.AgentTaxPaymentBatch = AgentTaxPaymentBatch()
            self.AgentTaxPaymentBatch._deserialize(params.get("AgentTaxPaymentBatch"))
        self.RequestId = params.get("RequestId")


class CreateCustAcctIdRequest(AbstractModel):
    """CreateCustAcctId请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionFlag: STRING(2)，功能标志（1: 开户; 3: 销户）\n        :type FunctionFlag: str\n        :param FundSummaryAcctNo: STRING(50)，资金汇总账号（即收单资金归集入账的账号）\n        :type FundSummaryAcctNo: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码（平台端的用户ID，需要保证唯一性，可数字字母混合，如HY_120）\n        :type TranNetMemberCode: str\n        :param MemberProperty: STRING(10)，会员属性（00-普通子账户(默认); SH-商户子账户）\n        :type MemberProperty: str\n        :param Mobile: STRING(30)，手机号码\n        :type Mobile: str\n        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param SelfBusiness: String(2)，是否为自营业务（0位非自营，1为自营）\n        :type SelfBusiness: bool\n        :param ContactName: String(64)，联系人\n        :type ContactName: str\n        :param SubAcctName: String(64)，子账户名称\n        :type SubAcctName: str\n        :param SubAcctShortName: String(64)，子账户简称\n        :type SubAcctShortName: str\n        :param SubAcctType: String(4)，子账户类型（0: 个人子账户; 1: 企业子账户）\n        :type SubAcctType: int\n        :param UserNickname: STRING(150)，用户昵称\n        :type UserNickname: str\n        :param Email: STRING(150)，邮箱\n        :type Email: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.FunctionFlag = None
        self.FundSummaryAcctNo = None
        self.TranNetMemberCode = None
        self.MemberProperty = None
        self.Mobile = None
        self.MrchCode = None
        self.SelfBusiness = None
        self.ContactName = None
        self.SubAcctName = None
        self.SubAcctShortName = None
        self.SubAcctType = None
        self.UserNickname = None
        self.Email = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.FunctionFlag = params.get("FunctionFlag")
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberProperty = params.get("MemberProperty")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.SelfBusiness = params.get("SelfBusiness")
        self.ContactName = params.get("ContactName")
        self.SubAcctName = params.get("SubAcctName")
        self.SubAcctShortName = params.get("SubAcctShortName")
        self.SubAcctType = params.get("SubAcctType")
        self.UserNickname = params.get("UserNickname")
        self.Email = params.get("Email")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustAcctIdResponse(AbstractModel):
    """CreateCustAcctId返回参数结构体

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，见证子账户的账号（平台需要记录下来，后续所有接口交互都会用到）
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctNo: str\n        :param ReservedMsg: STRING(1027)，保留域（需要开通智能收款，此处返回智能收款账号，正常情况下返回空）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class CreateInvoiceItem(AbstractModel):
    """发票开具明细

    """

    def __init__(self):
        """
        :param Name: 商品名称\n        :type Name: str\n        :param TaxCode: 税收商品编码\n        :type TaxCode: str\n        :param TotalPrice: 不含税商品总价（商品含税价总额/（1+税率））。InvoicePlatformId 为1时，该金额为含税总金额。单位为分。\n        :type TotalPrice: int\n        :param TaxRate: 商品税率\n        :type TaxRate: int\n        :param TaxAmount: 商品税额（不含税商品总价*税率）。单位为分\n        :type TaxAmount: int\n        :param TaxType: 税收商品类别\n        :type TaxType: str\n        :param Models: 商品规格\n        :type Models: str\n        :param Unit: 商品单位\n        :type Unit: str\n        :param Total: 商品数量\n        :type Total: str\n        :param Price: 不含税商品单价。InvoicePlatformId 为1时，该金额为含税单价。\n        :type Price: str\n        :param Discount: 含税折扣总额。单位为分\n        :type Discount: int\n        :param PreferentialPolicyFlag: 优惠政策标志。0：不使用优惠政策；1：使用优惠政策。\n        :type PreferentialPolicyFlag: str\n        :param ZeroTaxFlag: 零税率标识：
空：非零税率；
0：出口零税率；
1：免税；
2：不征税；
3：普通零税率。\n        :type ZeroTaxFlag: str\n        :param VatSpecialManagement: 增值税特殊管理。PreferentialPolicyFlag字段为1时，必填。目前仅支持5%(3%，2%，1.5%)简易征税、免税、不征税。\n        :type VatSpecialManagement: str\n        """
        self.Name = None
        self.TaxCode = None
        self.TotalPrice = None
        self.TaxRate = None
        self.TaxAmount = None
        self.TaxType = None
        self.Models = None
        self.Unit = None
        self.Total = None
        self.Price = None
        self.Discount = None
        self.PreferentialPolicyFlag = None
        self.ZeroTaxFlag = None
        self.VatSpecialManagement = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TaxCode = params.get("TaxCode")
        self.TotalPrice = params.get("TotalPrice")
        self.TaxRate = params.get("TaxRate")
        self.TaxAmount = params.get("TaxAmount")
        self.TaxType = params.get("TaxType")
        self.Models = params.get("Models")
        self.Unit = params.get("Unit")
        self.Total = params.get("Total")
        self.Price = params.get("Price")
        self.Discount = params.get("Discount")
        self.PreferentialPolicyFlag = params.get("PreferentialPolicyFlag")
        self.ZeroTaxFlag = params.get("ZeroTaxFlag")
        self.VatSpecialManagement = params.get("VatSpecialManagement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceRequest(AbstractModel):
    """CreateInvoice请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID。0：高灯，1：票易通\n        :type InvoicePlatformId: int\n        :param TitleType: 抬头类型：1：个人/政府事业单位；2：企业\n        :type TitleType: int\n        :param BuyerTitle: 购方名称\n        :type BuyerTitle: str\n        :param OrderId: 业务开票号\n        :type OrderId: str\n        :param AmountHasTax: 含税总金额（单位为分）\n        :type AmountHasTax: int\n        :param TaxAmount: 总税额（单位为分）\n        :type TaxAmount: int\n        :param AmountWithoutTax: 不含税总金额（单位为分）。InvoicePlatformId 为1时，传默认值-1\n        :type AmountWithoutTax: int\n        :param SellerTaxpayerNum: 销方纳税人识别号\n        :type SellerTaxpayerNum: str\n        :param SellerName: 销方名称。（不填默认读取商户注册时输入的信息）\n        :type SellerName: str\n        :param SellerAddress: 销方地址。（不填默认读取商户注册时输入的信息）\n        :type SellerAddress: str\n        :param SellerPhone: 销方电话。（不填默认读取商户注册时输入的信息）\n        :type SellerPhone: str\n        :param SellerBankName: 销方银行名称。（不填默认读取商户注册时输入的信息）\n        :type SellerBankName: str\n        :param SellerBankAccount: 销方银行账号。（不填默认读取商户注册时输入的信息）\n        :type SellerBankAccount: str\n        :param BuyerTaxpayerNum: 购方纳税人识别号（购方票面信息）,若抬头类型为2时，必传\n        :type BuyerTaxpayerNum: str\n        :param BuyerAddress: 购方地址。开具专用发票时必填\n        :type BuyerAddress: str\n        :param BuyerBankName: 购方银行名称。开具专用发票时必填\n        :type BuyerBankName: str\n        :param BuyerBankAccount: 购方银行账号。开具专用发票时必填\n        :type BuyerBankAccount: str\n        :param BuyerPhone: 购方电话。开具专用发票时必填\n        :type BuyerPhone: str\n        :param BuyerEmail: 收票人邮箱。若填入，会收到发票推送邮件\n        :type BuyerEmail: str\n        :param TakerPhone: 收票人手机号。若填入，会收到发票推送短信\n        :type TakerPhone: str\n        :param InvoiceType: 开票类型：
1：增值税专用发票；
2：增值税普通发票；
3：增值税电子发票；
4：增值税卷式发票；
5：区块链电子发票。
若该字段不填，或值不为1-5，则认为开具”增值税电子发票”\n        :type InvoiceType: int\n        :param CallbackUrl: 发票结果回传地址\n        :type CallbackUrl: str\n        :param Drawer: 开票人姓名。（不填默认读取商户注册时输入的信息）\n        :type Drawer: str\n        :param Payee: 收款人姓名。（不填默认读取商户注册时输入的信息）\n        :type Payee: str\n        :param Checker: 复核人姓名。（不填默认读取商户注册时输入的信息）\n        :type Checker: str\n        :param TerminalCode: 税盘号\n        :type TerminalCode: str\n        :param LevyMethod: 征收方式。开具差额征税发票时必填2。开具普通征税发票时为空\n        :type LevyMethod: str\n        :param Deduction: 差额征税扣除额（单位为分）\n        :type Deduction: int\n        :param Remark: 备注（票面信息）\n        :type Remark: str\n        :param Items: 项目商品明细\n        :type Items: list of CreateInvoiceItem\n        :param Profile: 接入环境。沙箱环境填sandbox。\n        :type Profile: str\n        :param UndoPart: 撤销部分商品。0-不撤销，1-撤销\n        :type UndoPart: int\n        :param OrderDate: 订单下单时间（格式 YYYYMMDD）\n        :type OrderDate: str\n        :param Discount: 订单级别折扣（单位为分）\n        :type Discount: int\n        :param StoreNo: 门店编码\n        :type StoreNo: str\n        :param InvoiceChannel: 开票渠道。0：APP渠道，1：线下渠道，2：小程序渠道。不填默认为APP渠道\n        :type InvoiceChannel: int\n        """
        self.InvoicePlatformId = None
        self.TitleType = None
        self.BuyerTitle = None
        self.OrderId = None
        self.AmountHasTax = None
        self.TaxAmount = None
        self.AmountWithoutTax = None
        self.SellerTaxpayerNum = None
        self.SellerName = None
        self.SellerAddress = None
        self.SellerPhone = None
        self.SellerBankName = None
        self.SellerBankAccount = None
        self.BuyerTaxpayerNum = None
        self.BuyerAddress = None
        self.BuyerBankName = None
        self.BuyerBankAccount = None
        self.BuyerPhone = None
        self.BuyerEmail = None
        self.TakerPhone = None
        self.InvoiceType = None
        self.CallbackUrl = None
        self.Drawer = None
        self.Payee = None
        self.Checker = None
        self.TerminalCode = None
        self.LevyMethod = None
        self.Deduction = None
        self.Remark = None
        self.Items = None
        self.Profile = None
        self.UndoPart = None
        self.OrderDate = None
        self.Discount = None
        self.StoreNo = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TitleType = params.get("TitleType")
        self.BuyerTitle = params.get("BuyerTitle")
        self.OrderId = params.get("OrderId")
        self.AmountHasTax = params.get("AmountHasTax")
        self.TaxAmount = params.get("TaxAmount")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        self.SellerName = params.get("SellerName")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerPhone = params.get("SellerPhone")
        self.SellerBankName = params.get("SellerBankName")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.BuyerTaxpayerNum = params.get("BuyerTaxpayerNum")
        self.BuyerAddress = params.get("BuyerAddress")
        self.BuyerBankName = params.get("BuyerBankName")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.BuyerPhone = params.get("BuyerPhone")
        self.BuyerEmail = params.get("BuyerEmail")
        self.TakerPhone = params.get("TakerPhone")
        self.InvoiceType = params.get("InvoiceType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Drawer = params.get("Drawer")
        self.Payee = params.get("Payee")
        self.Checker = params.get("Checker")
        self.TerminalCode = params.get("TerminalCode")
        self.LevyMethod = params.get("LevyMethod")
        self.Deduction = params.get("Deduction")
        self.Remark = params.get("Remark")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CreateInvoiceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Profile = params.get("Profile")
        self.UndoPart = params.get("UndoPart")
        self.OrderDate = params.get("OrderDate")
        self.Discount = params.get("Discount")
        self.StoreNo = params.get("StoreNo")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceResponse(AbstractModel):
    """CreateInvoice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 发票开具结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateInvoiceResult(AbstractModel):
    """发票结果

    """

    def __init__(self):
        """
        :param Message: 错误消息\n        :type Message: str\n        :param Code: 错误码\n        :type Code: int\n        :param Data: 数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResultData`\n        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = CreateInvoiceResultData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceResultData(AbstractModel):
    """蓝票结果数据

    """

    def __init__(self):
        """
        :param State: 开票状态\n        :type State: int\n        :param InvoiceId: 发票ID\n        :type InvoiceId: str\n        :param OrderSn: 业务开票号\n        :type OrderSn: str\n        """
        self.State = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceResultV2(AbstractModel):
    """发票结果V2

    """

    def __init__(self):
        """
        :param InvoiceId: 发票ID\n        :type InvoiceId: str\n        """
        self.InvoiceId = None


    def _deserialize(self, params):
        self.InvoiceId = params.get("InvoiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceV2Request(AbstractModel):
    """CreateInvoiceV2请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID。0：高灯，1：票易通\n        :type InvoicePlatformId: int\n        :param TitleType: 抬头类型：1：个人/政府事业单位；2：企业\n        :type TitleType: int\n        :param BuyerTitle: 购方名称\n        :type BuyerTitle: str\n        :param OrderId: 业务开票号\n        :type OrderId: str\n        :param AmountHasTax: 含税总金额（单位为分）\n        :type AmountHasTax: int\n        :param TaxAmount: 总税额（单位为分）\n        :type TaxAmount: int\n        :param AmountWithoutTax: 不含税总金额（单位为分）。InvoicePlatformId 为1时，传默认值-1\n        :type AmountWithoutTax: int\n        :param SellerTaxpayerNum: 销方纳税人识别号\n        :type SellerTaxpayerNum: str\n        :param SellerName: 销方名称。（不填默认读取商户注册时输入的信息）\n        :type SellerName: str\n        :param SellerAddress: 销方地址。（不填默认读取商户注册时输入的信息）\n        :type SellerAddress: str\n        :param SellerPhone: 销方电话。（不填默认读取商户注册时输入的信息）\n        :type SellerPhone: str\n        :param SellerBankName: 销方银行名称。（不填默认读取商户注册时输入的信息）\n        :type SellerBankName: str\n        :param SellerBankAccount: 销方银行账号。（不填默认读取商户注册时输入的信息）\n        :type SellerBankAccount: str\n        :param BuyerTaxpayerNum: 购方纳税人识别号（购方票面信息）,若抬头类型为2时，必传\n        :type BuyerTaxpayerNum: str\n        :param BuyerAddress: 购方地址。开具专用发票时必填\n        :type BuyerAddress: str\n        :param BuyerBankName: 购方银行名称。开具专用发票时必填\n        :type BuyerBankName: str\n        :param BuyerBankAccount: 购方银行账号。开具专用发票时必填\n        :type BuyerBankAccount: str\n        :param BuyerPhone: 购方电话。开具专用发票时必填\n        :type BuyerPhone: str\n        :param BuyerEmail: 收票人邮箱。若填入，会收到发票推送邮件\n        :type BuyerEmail: str\n        :param TakerPhone: 收票人手机号。若填入，会收到发票推送短信\n        :type TakerPhone: str\n        :param InvoiceType: 开票类型：
1：增值税专用发票；
2：增值税普通发票；
3：增值税电子发票；
4：增值税卷式发票；
5：区块链电子发票。
若该字段不填，或值不为1-5，则认为开具”增值税电子发票”\n        :type InvoiceType: int\n        :param CallbackUrl: 发票结果回传地址\n        :type CallbackUrl: str\n        :param Drawer: 开票人姓名。（不填默认读取商户注册时输入的信息）\n        :type Drawer: str\n        :param Payee: 收款人姓名。（不填默认读取商户注册时输入的信息）\n        :type Payee: str\n        :param Checker: 复核人姓名。（不填默认读取商户注册时输入的信息）\n        :type Checker: str\n        :param TerminalCode: 税盘号\n        :type TerminalCode: str\n        :param LevyMethod: 征收方式。开具差额征税发票时必填2。开具普通征税发票时为空\n        :type LevyMethod: str\n        :param Deduction: 差额征税扣除额（单位为分）\n        :type Deduction: int\n        :param Remark: 备注（票面信息）\n        :type Remark: str\n        :param Items: 项目商品明细\n        :type Items: list of CreateInvoiceItem\n        :param Profile: 接入环境。沙箱环境填sandbox。\n        :type Profile: str\n        :param UndoPart: 撤销部分商品。0-不撤销，1-撤销\n        :type UndoPart: int\n        :param OrderDate: 订单下单时间（格式 YYYYMMDD）\n        :type OrderDate: str\n        :param Discount: 订单级别折扣（单位为分）\n        :type Discount: int\n        :param StoreNo: 门店编码\n        :type StoreNo: str\n        :param InvoiceChannel: 开票渠道。0：APP渠道，1：线下渠道，2：小程序渠道。不填默认为APP渠道\n        :type InvoiceChannel: int\n        """
        self.InvoicePlatformId = None
        self.TitleType = None
        self.BuyerTitle = None
        self.OrderId = None
        self.AmountHasTax = None
        self.TaxAmount = None
        self.AmountWithoutTax = None
        self.SellerTaxpayerNum = None
        self.SellerName = None
        self.SellerAddress = None
        self.SellerPhone = None
        self.SellerBankName = None
        self.SellerBankAccount = None
        self.BuyerTaxpayerNum = None
        self.BuyerAddress = None
        self.BuyerBankName = None
        self.BuyerBankAccount = None
        self.BuyerPhone = None
        self.BuyerEmail = None
        self.TakerPhone = None
        self.InvoiceType = None
        self.CallbackUrl = None
        self.Drawer = None
        self.Payee = None
        self.Checker = None
        self.TerminalCode = None
        self.LevyMethod = None
        self.Deduction = None
        self.Remark = None
        self.Items = None
        self.Profile = None
        self.UndoPart = None
        self.OrderDate = None
        self.Discount = None
        self.StoreNo = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TitleType = params.get("TitleType")
        self.BuyerTitle = params.get("BuyerTitle")
        self.OrderId = params.get("OrderId")
        self.AmountHasTax = params.get("AmountHasTax")
        self.TaxAmount = params.get("TaxAmount")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        self.SellerName = params.get("SellerName")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerPhone = params.get("SellerPhone")
        self.SellerBankName = params.get("SellerBankName")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.BuyerTaxpayerNum = params.get("BuyerTaxpayerNum")
        self.BuyerAddress = params.get("BuyerAddress")
        self.BuyerBankName = params.get("BuyerBankName")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.BuyerPhone = params.get("BuyerPhone")
        self.BuyerEmail = params.get("BuyerEmail")
        self.TakerPhone = params.get("TakerPhone")
        self.InvoiceType = params.get("InvoiceType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Drawer = params.get("Drawer")
        self.Payee = params.get("Payee")
        self.Checker = params.get("Checker")
        self.TerminalCode = params.get("TerminalCode")
        self.LevyMethod = params.get("LevyMethod")
        self.Deduction = params.get("Deduction")
        self.Remark = params.get("Remark")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CreateInvoiceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Profile = params.get("Profile")
        self.UndoPart = params.get("UndoPart")
        self.OrderDate = params.get("OrderDate")
        self.Discount = params.get("Discount")
        self.StoreNo = params.get("StoreNo")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceV2Response(AbstractModel):
    """CreateInvoiceV2返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 发票开具结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResultV2`\n        :param ErrCode: 错误码\n        :type ErrCode: str\n        :param ErrMessage: 错误消息\n        :type ErrMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.ErrCode = None
        self.ErrMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInvoiceResultV2()
            self.Result._deserialize(params.get("Result"))
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.RequestId = params.get("RequestId")


class CreateMerchantRequest(AbstractModel):
    """CreateMerchant请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID\n        :type InvoicePlatformId: int\n        :param TaxpayerName: 企业名称\n        :type TaxpayerName: str\n        :param TaxpayerNum: 销方纳税人识别号\n        :type TaxpayerNum: str\n        :param LegalPersonName: 注册企业法定代表人名称\n        :type LegalPersonName: str\n        :param ContactsName: 联系人\n        :type ContactsName: str\n        :param Phone: 联系人手机号\n        :type Phone: str\n        :param Address: 不包含省市名称的地址\n        :type Address: str\n        :param RegionCode: 地区编码\n        :type RegionCode: int\n        :param CityName: 市（地区）名称\n        :type CityName: str\n        :param Drawer: 开票人\n        :type Drawer: str\n        :param TaxRegistrationCertificate: 税务登记证图片（Base64）字符串，需小于 3M\n        :type TaxRegistrationCertificate: str\n        :param Email: 联系人邮箱地址\n        :type Email: str\n        :param BusinessMobile: 企业电话\n        :type BusinessMobile: str\n        :param BankName: 银行名称\n        :type BankName: str\n        :param BankAccount: 银行账号\n        :type BankAccount: str\n        :param Reviewer: 复核人\n        :type Reviewer: str\n        :param Payee: 收款人\n        :type Payee: str\n        :param RegisterCode: 注册邀请码\n        :type RegisterCode: str\n        :param State: 不填默认为1，有效状态
0：表示无效；
1:表示有效；
2:表示禁止开蓝票；
3:表示禁止冲红。\n        :type State: str\n        :param CallbackUrl: 接收推送的消息地址\n        :type CallbackUrl: str\n        :param Profile: 接入环境。沙箱环境填 sandbox。\n        :type Profile: str\n        """
        self.InvoicePlatformId = None
        self.TaxpayerName = None
        self.TaxpayerNum = None
        self.LegalPersonName = None
        self.ContactsName = None
        self.Phone = None
        self.Address = None
        self.RegionCode = None
        self.CityName = None
        self.Drawer = None
        self.TaxRegistrationCertificate = None
        self.Email = None
        self.BusinessMobile = None
        self.BankName = None
        self.BankAccount = None
        self.Reviewer = None
        self.Payee = None
        self.RegisterCode = None
        self.State = None
        self.CallbackUrl = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TaxpayerName = params.get("TaxpayerName")
        self.TaxpayerNum = params.get("TaxpayerNum")
        self.LegalPersonName = params.get("LegalPersonName")
        self.ContactsName = params.get("ContactsName")
        self.Phone = params.get("Phone")
        self.Address = params.get("Address")
        self.RegionCode = params.get("RegionCode")
        self.CityName = params.get("CityName")
        self.Drawer = params.get("Drawer")
        self.TaxRegistrationCertificate = params.get("TaxRegistrationCertificate")
        self.Email = params.get("Email")
        self.BusinessMobile = params.get("BusinessMobile")
        self.BankName = params.get("BankName")
        self.BankAccount = params.get("BankAccount")
        self.Reviewer = params.get("Reviewer")
        self.Payee = params.get("Payee")
        self.RegisterCode = params.get("RegisterCode")
        self.State = params.get("State")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMerchantResponse(AbstractModel):
    """CreateMerchant返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 商户注册结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateMerchantResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateMerchantResult(AbstractModel):
    """创建商户结果

    """

    def __init__(self):
        """
        :param Code: 状态码\n        :type Code: int\n        :param Message: 响应消息\n        :type Message: str\n        :param Data: 创建商户结果数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResultData`\n        """
        self.Code = None
        self.Message = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Data") is not None:
            self.Data = CreateMerchantResultData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMerchantResultData(AbstractModel):
    """创建商户结果数据

    """

    def __init__(self):
        """
        :param TaxpayerName: 企业名称\n        :type TaxpayerName: str\n        :param SerialNo: 请求流水号\n        :type SerialNo: str\n        :param TaxpayerNum: 纳税号\n        :type TaxpayerNum: str\n        """
        self.TaxpayerName = None
        self.SerialNo = None
        self.TaxpayerNum = None


    def _deserialize(self, params):
        self.TaxpayerName = params.get("TaxpayerName")
        self.SerialNo = params.get("SerialNo")
        self.TaxpayerNum = params.get("TaxpayerNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderRequest(AbstractModel):
    """CreateOrder请求参数结构体

    """

    def __init__(self):
        """
        :param ChannelCode: 渠道编号。ZSB2B：招商银行B2B。\n        :type ChannelCode: str\n        :param MerchantAppId: 进件成功后返给商户方的 AppId。\n        :type MerchantAppId: str\n        :param Amount: 交易金额。单位：元\n        :type Amount: str\n        :param TraceNo: 商户流水号。商户唯一订单号由字母或数字组成。\n        :type TraceNo: str\n        :param NotifyUrl: 通知地址。商户接收交易结果的通知地址。\n        :type NotifyUrl: str\n        :param ReturnUrl: 返回地址。支付成功后，页面将跳 转返回到商户的该地址。\n        :type ReturnUrl: str\n        """
        self.ChannelCode = None
        self.MerchantAppId = None
        self.Amount = None
        self.TraceNo = None
        self.NotifyUrl = None
        self.ReturnUrl = None


    def _deserialize(self, params):
        self.ChannelCode = params.get("ChannelCode")
        self.MerchantAppId = params.get("MerchantAppId")
        self.Amount = params.get("Amount")
        self.TraceNo = params.get("TraceNo")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ReturnUrl = params.get("ReturnUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderResponse(AbstractModel):
    """CreateOrder返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 进件成功后返给商户方的AppId。\n        :type MerchantAppId: str\n        :param TraceNo: 商户流水号，商户唯一订单号由字母或数字组成。\n        :type TraceNo: str\n        :param OrderNo: 平台流水号，若下单成功则返回。\n        :type OrderNo: str\n        :param PayUrl: 支付页面跳转地址，若下单成功则返回。\n        :type PayUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantAppId = None
        self.TraceNo = None
        self.OrderNo = None
        self.PayUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.TraceNo = params.get("TraceNo")
        self.OrderNo = params.get("OrderNo")
        self.PayUrl = params.get("PayUrl")
        self.RequestId = params.get("RequestId")


class CreatePayMerchantRequest(AbstractModel):
    """CreatePayMerchant请求参数结构体

    """

    def __init__(self):
        """
        :param PlatformCode: 平台编号\n        :type PlatformCode: str\n        :param ChannelMerchantNo: 渠道方收款商户编号，由渠道方(银行)提 供。\n        :type ChannelMerchantNo: str\n        :param ChannelCheckFlag: 是否需要向渠道进行 商户信息验证 1:验证
0:不验证\n        :type ChannelCheckFlag: str\n        :param MerchantName: 收款商户名称\n        :type MerchantName: str\n        :param BusinessPayFlag: 是否开通 B2B 支付 1:开通 0:不开通 缺省:1\n        :type BusinessPayFlag: str\n        """
        self.PlatformCode = None
        self.ChannelMerchantNo = None
        self.ChannelCheckFlag = None
        self.MerchantName = None
        self.BusinessPayFlag = None


    def _deserialize(self, params):
        self.PlatformCode = params.get("PlatformCode")
        self.ChannelMerchantNo = params.get("ChannelMerchantNo")
        self.ChannelCheckFlag = params.get("ChannelCheckFlag")
        self.MerchantName = params.get("MerchantName")
        self.BusinessPayFlag = params.get("BusinessPayFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayMerchantResponse(AbstractModel):
    """CreatePayMerchant返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 分配给商户的 AppId。该 AppId 为后续各项 交易的商户标识。\n        :type MerchantAppId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.RequestId = params.get("RequestId")


class CreateRedInvoiceItem(AbstractModel):
    """创建红票明细

    """

    def __init__(self):
        """
        :param OrderId: 订单号\n        :type OrderId: str\n        :param CallbackUrl: 发票结果回传地址\n        :type CallbackUrl: str\n        :param OrderSn: 业务开票号\n        :type OrderSn: str\n        :param RedSerialNo: 红字信息表编码\n        :type RedSerialNo: str\n        :param StoreNo: 门店编号\n        :type StoreNo: str\n        """
        self.OrderId = None
        self.CallbackUrl = None
        self.OrderSn = None
        self.RedSerialNo = None
        self.StoreNo = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.CallbackUrl = params.get("CallbackUrl")
        self.OrderSn = params.get("OrderSn")
        self.RedSerialNo = params.get("RedSerialNo")
        self.StoreNo = params.get("StoreNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceRequest(AbstractModel):
    """CreateRedInvoice请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID\n        :type InvoicePlatformId: int\n        :param Invoices: 红冲明细\n        :type Invoices: list of CreateRedInvoiceItem\n        :param Profile: 接入环境。沙箱环境填 sandbox。\n        :type Profile: str\n        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道\n        :type InvoiceChannel: int\n        """
        self.InvoicePlatformId = None
        self.Invoices = None
        self.Profile = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        if params.get("Invoices") is not None:
            self.Invoices = []
            for item in params.get("Invoices"):
                obj = CreateRedInvoiceItem()
                obj._deserialize(item)
                self.Invoices.append(obj)
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceResponse(AbstractModel):
    """CreateRedInvoice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 红冲结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateRedInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateRedInvoiceResult(AbstractModel):
    """红票结果

    """

    def __init__(self):
        """
        :param Message: 错误消息\n        :type Message: str\n        :param Code: 错误码\n        :type Code: int\n        :param Data: 红票数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of CreateRedInvoiceResultData\n        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CreateRedInvoiceResultData()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceResultData(AbstractModel):
    """红票结果数据

    """

    def __init__(self):
        """
        :param Code: 红冲状态码\n        :type Code: int\n        :param Message: 红冲状态消息\n        :type Message: str\n        :param InvoiceId: 发票ID\n        :type InvoiceId: str\n        :param OrderSn: 业务开票号\n        :type OrderSn: str\n        """
        self.Code = None
        self.Message = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceResultV2(AbstractModel):
    """红票结果V2

    """

    def __init__(self):
        """
        :param InvoiceId: 红票ID\n        :type InvoiceId: str\n        """
        self.InvoiceId = None


    def _deserialize(self, params):
        self.InvoiceId = params.get("InvoiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceV2Request(AbstractModel):
    """CreateRedInvoiceV2请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID\n        :type InvoicePlatformId: int\n        :param OrderId: 订单号\n        :type OrderId: str\n        :param Profile: 接入环境。沙箱环境填 sandbox。\n        :type Profile: str\n        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道\n        :type InvoiceChannel: int\n        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.Profile = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceV2Response(AbstractModel):
    """CreateRedInvoiceV2返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 红冲结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceResultV2`\n        :param ErrCode: 错误码\n        :type ErrCode: str\n        :param ErrMessage: 错误消息\n        :type ErrMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.ErrCode = None
        self.ErrMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateRedInvoiceResultV2()
            self.Result._deserialize(params.get("Result"))
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.RequestId = params.get("RequestId")


class CreateSinglePayRequest(AbstractModel):
    """CreateSinglePay请求参数结构体

    """

    def __init__(self):
        """
        :param SerialNumber: 业务流水号，历史唯一\n        :type SerialNumber: str\n        :param PayAccountNumber: 付方账户号\n        :type PayAccountNumber: str\n        :param PayAccountName: 付方账户名称\n        :type PayAccountName: str\n        :param Amount: 金额\n        :type Amount: int\n        :param RecvAccountNumber: 收方账户号\n        :type RecvAccountNumber: str\n        :param RecvAccountName: 收方账户名称\n        :type RecvAccountName: str\n        :param PayBankCnaps: 付方账户CNAPS号\n        :type PayBankCnaps: str\n        :param PayBankType: 付方账户银行大类，PayBankCnaps为空时必传（见常见问题-银企直连银行类型）\n        :type PayBankType: str\n        :param PayBankProvince: 付方账户银行所在省，PayBankCnaps为空时必传（见常见问题-银企直连省份枚举信息）\n        :type PayBankProvince: str\n        :param PayBankCity: 付方账户银行所在地区，PayBankCnaps为空时必传（见常见问题-银企直连城市枚举信息）\n        :type PayBankCity: str\n        :param RecvBankCnaps: 收方账户CNAPS号\n        :type RecvBankCnaps: str\n        :param RecvBankType: 收方账户银行大类，RecvBankCnaps为空时必传（见常见问题-银企直连银行类型）\n        :type RecvBankType: str\n        :param RecvBankProvince: 收方账户银行所在省，RecvBankCnaps为空时必传（见常见问题-银企直连省份枚举信息）\n        :type RecvBankProvince: str\n        :param RecvBankCity: 收方账户银行所在地区，RecvBankCnaps为空时必传（见常见问题-银企直连城市枚举信息）\n        :type RecvBankCity: str\n        :param RecvCertType: 收款方证件类型（见常见问题-银企直连证件类型枚举信息）\n        :type RecvCertType: str\n        :param RecvCertNo: 收款方证件号码\n        :type RecvCertNo: str\n        :param Summary: 摘要信息\n        :type Summary: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.SerialNumber = None
        self.PayAccountNumber = None
        self.PayAccountName = None
        self.Amount = None
        self.RecvAccountNumber = None
        self.RecvAccountName = None
        self.PayBankCnaps = None
        self.PayBankType = None
        self.PayBankProvince = None
        self.PayBankCity = None
        self.RecvBankCnaps = None
        self.RecvBankType = None
        self.RecvBankProvince = None
        self.RecvBankCity = None
        self.RecvCertType = None
        self.RecvCertNo = None
        self.Summary = None
        self.Profile = None


    def _deserialize(self, params):
        self.SerialNumber = params.get("SerialNumber")
        self.PayAccountNumber = params.get("PayAccountNumber")
        self.PayAccountName = params.get("PayAccountName")
        self.Amount = params.get("Amount")
        self.RecvAccountNumber = params.get("RecvAccountNumber")
        self.RecvAccountName = params.get("RecvAccountName")
        self.PayBankCnaps = params.get("PayBankCnaps")
        self.PayBankType = params.get("PayBankType")
        self.PayBankProvince = params.get("PayBankProvince")
        self.PayBankCity = params.get("PayBankCity")
        self.RecvBankCnaps = params.get("RecvBankCnaps")
        self.RecvBankType = params.get("RecvBankType")
        self.RecvBankProvince = params.get("RecvBankProvince")
        self.RecvBankCity = params.get("RecvBankCity")
        self.RecvCertType = params.get("RecvCertType")
        self.RecvCertNo = params.get("RecvCertNo")
        self.Summary = params.get("Summary")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSinglePayResponse(AbstractModel):
    """CreateSinglePay返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateSinglePayResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateSinglePayResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateSinglePayResult(AbstractModel):
    """银企直连-单笔支付响应结果

    """

    def __init__(self):
        """
        :param HandleStatus: 受理状态（S：处理成功；F：处理失败）\n        :type HandleStatus: str\n        :param HandleMsg: 受理状态描述\n        :type HandleMsg: str\n        :param SerialNo: 业务流水号，历史唯一
注意：此字段可能返回 null，表示取不到有效值。\n        :type SerialNo: str\n        :param BankSerialNo: 银行指令流水
注意：此字段可能返回 null，表示取不到有效值。\n        :type BankSerialNo: str\n        :param PayStatus: 付款状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayStatus: str\n        :param BankRetCode: 银行原始返回码
注意：此字段可能返回 null，表示取不到有效值。\n        :type BankRetCode: str\n        :param BankRetMsg: 银行原始返回
注意：此字段可能返回 null，表示取不到有效值。\n        :type BankRetMsg: str\n        """
        self.HandleStatus = None
        self.HandleMsg = None
        self.SerialNo = None
        self.BankSerialNo = None
        self.PayStatus = None
        self.BankRetCode = None
        self.BankRetMsg = None


    def _deserialize(self, params):
        self.HandleStatus = params.get("HandleStatus")
        self.HandleMsg = params.get("HandleMsg")
        self.SerialNo = params.get("SerialNo")
        self.BankSerialNo = params.get("BankSerialNo")
        self.PayStatus = params.get("PayStatus")
        self.BankRetCode = params.get("BankRetCode")
        self.BankRetMsg = params.get("BankRetMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTransferBatchRequest(AbstractModel):
    """CreateTransferBatch请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号。
示例值：129284394\n        :type MerchantId: str\n        :param TransferDetails: 转账明细列表。
发起批量转账的明细列表，最多三千笔\n        :type TransferDetails: list of TransferDetailRequest\n        :param MerchantAppId: 直连商户appId。
即商户号绑定的appid。
示例值：wxf636efh567hg4356\n        :type MerchantAppId: str\n        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013\n        :type MerchantBatchNo: str\n        :param BatchName: 批次名称。
批量转账的名称。
示例值：2019年1月深圳分部报销单\n        :type BatchName: str\n        :param BatchRemark: 转账说明。
UTF8编码，最多32个字符。
示例值：2019年深圳分部报销单\n        :type BatchRemark: str\n        :param TotalAmount: 转账总金额。
转账金额，单位为分。
示例值：4000000\n        :type TotalAmount: int\n        :param TotalNum: 转账总笔数。
一个转账批次最多允许发起三千笔转账。
示例值：200\n        :type TotalNum: int\n        :param Profile: 环境名。
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type Profile: str\n        """
        self.MerchantId = None
        self.TransferDetails = None
        self.MerchantAppId = None
        self.MerchantBatchNo = None
        self.BatchName = None
        self.BatchRemark = None
        self.TotalAmount = None
        self.TotalNum = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        if params.get("TransferDetails") is not None:
            self.TransferDetails = []
            for item in params.get("TransferDetails"):
                obj = TransferDetailRequest()
                obj._deserialize(item)
                self.TransferDetails.append(obj)
        self.MerchantAppId = params.get("MerchantAppId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchName = params.get("BatchName")
        self.BatchRemark = params.get("BatchRemark")
        self.TotalAmount = params.get("TotalAmount")
        self.TotalNum = params.get("TotalNum")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTransferBatchResponse(AbstractModel):
    """CreateTransferBatch返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013\n        :type MerchantBatchNo: str\n        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
示例值：1030000071100999991182020050700019480001\n        :type BatchId: str\n        :param CreateTime: 批次受理成功时返回，遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00\n        :type CreateTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantBatchNo = None
        self.BatchId = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DeleteAgentTaxPaymentInfoRequest(AbstractModel):
    """DeleteAgentTaxPaymentInfo请求参数结构体

    """

    def __init__(self):
        """
        :param BatchNum: 批次号\n        :type BatchNum: int\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.BatchNum = None
        self.Profile = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentTaxPaymentInfoResponse(AbstractModel):
    """DeleteAgentTaxPaymentInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAgentTaxPaymentInfosRequest(AbstractModel):
    """DeleteAgentTaxPaymentInfos请求参数结构体

    """

    def __init__(self):
        """
        :param BatchNum: 批次号\n        :type BatchNum: int\n        """
        self.BatchNum = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentTaxPaymentInfosResponse(AbstractModel):
    """DeleteAgentTaxPaymentInfos返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeChargeDetailRequest(AbstractModel):
    """DescribeChargeDetail请求参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型\n        :type RequestType: str\n        :param MerchantCode: 商户号\n        :type MerchantCode: str\n        :param PayChannel: 支付渠道\n        :type PayChannel: str\n        :param PayChannelSubId: 子渠道\n        :type PayChannelSubId: int\n        :param OrderId: 原始交易订单号或者流水号\n        :type OrderId: str\n        :param BankAccountNumber: 父账户账号，资金汇总账号\n        :type BankAccountNumber: str\n        :param AcquiringChannelType: 收单渠道类型\n        :type AcquiringChannelType: str\n        :param PlatformShortNumber: 平台短号(银行分配)\n        :type PlatformShortNumber: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param TransSequenceNumber: 交易流水号\n        :type TransSequenceNumber: str\n        :param MidasEnvironment: Midas环境参数\n        :type MidasEnvironment: str\n        :param ReservedMessage: 保留域\n        :type ReservedMessage: str\n        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.AcquiringChannelType = None
        self.PlatformShortNumber = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.MidasEnvironment = None
        self.ReservedMessage = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.AcquiringChannelType = params.get("AcquiringChannelType")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChargeDetailResponse(AbstractModel):
    """DescribeChargeDetail返回参数结构体

    """

    def __init__(self):
        """
        :param OrderStatus: 交易状态 （0：成功，1：失败，2：异常,3:冲正，5：待处理）\n        :type OrderStatus: str\n        :param OrderAmount: 交易金额\n        :type OrderAmount: str\n        :param CommissionAmount: 佣金费\n        :type CommissionAmount: str\n        :param PayMode: 支付方式  0-冻结支付 1-普通支付\n        :type PayMode: str\n        :param OrderDate: 交易日期\n        :type OrderDate: str\n        :param OrderTime: 交易时间\n        :type OrderTime: str\n        :param OrderActualInSubAccountName: 订单实际转入见证子账户的名称\n        :type OrderActualInSubAccountName: str\n        :param OrderActualInSubAccountNumber: 订单实际转入见证子账户的帐号\n        :type OrderActualInSubAccountNumber: str\n        :param OrderInSubAccountName: 订单实际转入见证子账户的帐号\n        :type OrderInSubAccountName: str\n        :param OrderInSubAccountNumber: 订单转入见证子账户的帐号\n        :type OrderInSubAccountNumber: str\n        :param FrontSequenceNumber: 银行流水号\n        :type FrontSequenceNumber: str\n        :param FailMessage: 当充值失败时，返回交易失败原因\n        :type FailMessage: str\n        :param RequestType: 请求类型\n        :type RequestType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OrderStatus = None
        self.OrderAmount = None
        self.CommissionAmount = None
        self.PayMode = None
        self.OrderDate = None
        self.OrderTime = None
        self.OrderActualInSubAccountName = None
        self.OrderActualInSubAccountNumber = None
        self.OrderInSubAccountName = None
        self.OrderInSubAccountNumber = None
        self.FrontSequenceNumber = None
        self.FailMessage = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderStatus = params.get("OrderStatus")
        self.OrderAmount = params.get("OrderAmount")
        self.CommissionAmount = params.get("CommissionAmount")
        self.PayMode = params.get("PayMode")
        self.OrderDate = params.get("OrderDate")
        self.OrderTime = params.get("OrderTime")
        self.OrderActualInSubAccountName = params.get("OrderActualInSubAccountName")
        self.OrderActualInSubAccountNumber = params.get("OrderActualInSubAccountNumber")
        self.OrderInSubAccountName = params.get("OrderInSubAccountName")
        self.OrderInSubAccountNumber = params.get("OrderInSubAccountNumber")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.FailMessage = params.get("FailMessage")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class DescribeOrderStatusRequest(AbstractModel):
    """DescribeOrderStatus请求参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型，此接口固定填：QueryOrderStatusReq\n        :type RequestType: str\n        :param MerchantCode: 商户号\n        :type MerchantCode: str\n        :param PayChannel: 支付渠道\n        :type PayChannel: str\n        :param PayChannelSubId: 子渠道\n        :type PayChannelSubId: int\n        :param OrderId: 交易订单号或流水号，提现，充值或会员交易请求时的CnsmrSeqNo值\n        :type OrderId: str\n        :param BankAccountNumber: 父账户账号，资金汇总账号\n        :type BankAccountNumber: str\n        :param PlatformShortNumber: 平台短号(银行分配)\n        :type PlatformShortNumber: str\n        :param QueryType: 功能标志 0：会员间交易 1：提现 2：充值\n        :type QueryType: str\n        :param TransSequenceNumber: 银行流水号\n        :type TransSequenceNumber: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasEnvironment: Midas环境参数\n        :type MidasEnvironment: str\n        :param ReservedMessage: 保留字段\n        :type ReservedMessage: str\n        :param BankSubAccountNumber: 子账户账号 暂未使用\n        :type BankSubAccountNumber: str\n        :param TransDate: 交易日期 暂未使用\n        :type TransDate: str\n        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.PlatformShortNumber = None
        self.QueryType = None
        self.TransSequenceNumber = None
        self.MidasSignature = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasEnvironment = None
        self.ReservedMessage = None
        self.BankSubAccountNumber = None
        self.TransDate = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.QueryType = params.get("QueryType")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        self.BankSubAccountNumber = params.get("BankSubAccountNumber")
        self.TransDate = params.get("TransDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrderStatusResponse(AbstractModel):
    """DescribeOrderStatus返回参数结构体

    """

    def __init__(self):
        """
        :param OrderStatus: 交易状态 （0：成功，1：失败，2：待确认, 5：待处理，6：处理中）\n        :type OrderStatus: str\n        :param OrderAmount: 交易金额\n        :type OrderAmount: str\n        :param OrderDate: 交易日期\n        :type OrderDate: str\n        :param OrderTime: 交易时间\n        :type OrderTime: str\n        :param OutSubAccountNumber: 转出子账户账号\n        :type OutSubAccountNumber: str\n        :param InSubAccountNumber: 转入子账户账号\n        :type InSubAccountNumber: str\n        :param BookingFlag: 记账标志（1：登记挂账 2：支付 3：提现 4：清分5:下单预支付 6：确认并付款 7：退款 8：支付到平台 N:其他）\n        :type BookingFlag: str\n        :param FailMessage: 当交易失败时，返回交易失败原因\n        :type FailMessage: str\n        :param RequestType: 请求类型\n        :type RequestType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OrderStatus = None
        self.OrderAmount = None
        self.OrderDate = None
        self.OrderTime = None
        self.OutSubAccountNumber = None
        self.InSubAccountNumber = None
        self.BookingFlag = None
        self.FailMessage = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderStatus = params.get("OrderStatus")
        self.OrderAmount = params.get("OrderAmount")
        self.OrderDate = params.get("OrderDate")
        self.OrderTime = params.get("OrderTime")
        self.OutSubAccountNumber = params.get("OutSubAccountNumber")
        self.InSubAccountNumber = params.get("InSubAccountNumber")
        self.BookingFlag = params.get("BookingFlag")
        self.FailMessage = params.get("FailMessage")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class DownloadBillRequest(AbstractModel):
    """DownloadBill请求参数结构体

    """

    def __init__(self):
        """
        :param StateDate: 请求下载对账单日期\n        :type StateDate: str\n        :param MidasAppId: 聚鑫分配的MidasAppId\n        :type MidasAppId: str\n        :param MidasSecretId: 聚鑫分配的SecretId\n        :type MidasSecretId: str\n        :param MidasSignature: 使用聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.StateDate = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.StateDate = params.get("StateDate")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadBillResponse(AbstractModel):
    """DownloadBill返回参数结构体

    """

    def __init__(self):
        """
        :param FileName: 账单文件名\n        :type FileName: str\n        :param FileMD5: 账单文件的MD5值\n        :type FileMD5: str\n        :param DownloadUrl: 账单文件的真实下载地址\n        :type DownloadUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FileName = None
        self.FileMD5 = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileMD5 = params.get("FileMD5")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExecuteMemberTransactionRequest(AbstractModel):
    """ExecuteMemberTransaction请求参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型此接口固定填：MemberTransactionReq\n        :type RequestType: str\n        :param MerchantCode: 银行注册商户号\n        :type MerchantCode: str\n        :param PayChannel: 支付渠道\n        :type PayChannel: str\n        :param PayChannelSubId: 子渠道\n        :type PayChannelSubId: int\n        :param OutTransNetMemberCode: 转出交易网会员代码\n        :type OutTransNetMemberCode: str\n        :param OutSubAccountName: 转出见证子账户的户名\n        :type OutSubAccountName: str\n        :param InSubAccountName: 转入见证子账户的户名\n        :type InSubAccountName: str\n        :param OutSubAccountNumber: 转出子账户账号\n        :type OutSubAccountNumber: str\n        :param InSubAccountNumber: 转入子账户账号\n        :type InSubAccountNumber: str\n        :param BankAccountNumber: 父账户账号，资金汇总账号\n        :type BankAccountNumber: str\n        :param CurrencyUnit: 货币单位 单位，1：元，2：角，3：分\n        :type CurrencyUnit: str\n        :param CurrencyType: 币种\n        :type CurrencyType: str\n        :param CurrencyAmount: 交易金额\n        :type CurrencyAmount: str\n        :param OrderId: 订单号\n        :type OrderId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param TransSequenceNumber: 交易流水号 
生成方式：用户短号+日期（6位）+ 随机编号（10位）例如：F088722005120904930798
短号：F08872  日期： 200512   随机编号：0904930798\n        :type TransSequenceNumber: str\n        :param InTransNetMemberCode: 转入交易网会员代码\n        :type InTransNetMemberCode: str\n        :param MidasEnvironment: Midas环境标识 release 现网环境 sandbox 沙箱环境
development 开发环境\n        :type MidasEnvironment: str\n        :param PlatformShortNumber: 平台短号(银行分配)\n        :type PlatformShortNumber: str\n        :param TransType: 1：下单预支付 
2：确认并付款
3：退款
6：直接支付T+1
9：直接支付T+0\n        :type TransType: str\n        :param TransFee: 交易手续费\n        :type TransFee: str\n        :param ReservedMessage: 保留域\n        :type ReservedMessage: str\n        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OutTransNetMemberCode = None
        self.OutSubAccountName = None
        self.InSubAccountName = None
        self.OutSubAccountNumber = None
        self.InSubAccountNumber = None
        self.BankAccountNumber = None
        self.CurrencyUnit = None
        self.CurrencyType = None
        self.CurrencyAmount = None
        self.OrderId = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.InTransNetMemberCode = None
        self.MidasEnvironment = None
        self.PlatformShortNumber = None
        self.TransType = None
        self.TransFee = None
        self.ReservedMessage = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OutTransNetMemberCode = params.get("OutTransNetMemberCode")
        self.OutSubAccountName = params.get("OutSubAccountName")
        self.InSubAccountName = params.get("InSubAccountName")
        self.OutSubAccountNumber = params.get("OutSubAccountNumber")
        self.InSubAccountNumber = params.get("InSubAccountNumber")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.OrderId = params.get("OrderId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.InTransNetMemberCode = params.get("InTransNetMemberCode")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.TransType = params.get("TransType")
        self.TransFee = params.get("TransFee")
        self.ReservedMessage = params.get("ReservedMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteMemberTransactionResponse(AbstractModel):
    """ExecuteMemberTransaction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型\n        :type RequestType: str\n        :param FrontSequenceNumber: 银行流水号\n        :type FrontSequenceNumber: str\n        :param ReservedMessage: 保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestType = None
        self.FrontSequenceNumber = None
        self.ReservedMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.ReservedMessage = params.get("ReservedMessage")
        self.RequestId = params.get("RequestId")


class ExternalContractUserInfo(AbstractModel):
    """第三方渠道用户信息

    """

    def __init__(self):
        """
        :param ExternalUserType: 第三方用户类型，例如:  WX_OPENID, WX_SUB_OPENID,WX_PAYER_OPENID\n        :type ExternalUserType: str\n        :param ExternalUserId: 第三方用户ID\n        :type ExternalUserId: str\n        """
        self.ExternalUserType = None
        self.ExternalUserId = None


    def _deserialize(self, params):
        self.ExternalUserType = params.get("ExternalUserType")
        self.ExternalUserId = params.get("ExternalUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalReturnContractInfo(AbstractModel):
    """第三方渠道合约信息

    """

    def __init__(self):
        """
        :param ExternalReturnAgreementId: 第三方渠道协议id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnAgreementId: str\n        :param ExternalReturnContractEffectiveTimestamp: 第三方渠道协议生效时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractEffectiveTimestamp: str\n        :param ExternalReturnContractTerminationTimestamp: 第三方渠道协议解约时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractTerminationTimestamp: str\n        :param ExternalReturnContractStatus: 平台合约状态
协议状态，枚举值：
CONTRACT_STATUS_SIGNED：已签约
CONTRACT_STATUS_TERMINATED：未签约
CONTRACT_STATUS_PENDING：签约进行中
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractStatus: str\n        :param ExternalReturnRequestId: 第三方渠道请求序列号
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnRequestId: str\n        :param ExternalReturnContractSignedTimestamp: 第三方渠道协议签署时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractSignedTimestamp: str\n        :param ExternalReturnContractExpiredTimestamp: 第三方渠道协议到期时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractExpiredTimestamp: str\n        :param ExternalReturnContractData: 第三方渠道返回的合约数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractData: str\n        :param ExternalReturnContractTerminationRemark: 第三方渠道解约备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractTerminationRemark: str\n        :param ExternalReturnContractTerminationMode: 第三方渠道协议解约方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnContractTerminationMode: str\n        """
        self.ExternalReturnAgreementId = None
        self.ExternalReturnContractEffectiveTimestamp = None
        self.ExternalReturnContractTerminationTimestamp = None
        self.ExternalReturnContractStatus = None
        self.ExternalReturnRequestId = None
        self.ExternalReturnContractSignedTimestamp = None
        self.ExternalReturnContractExpiredTimestamp = None
        self.ExternalReturnContractData = None
        self.ExternalReturnContractTerminationRemark = None
        self.ExternalReturnContractTerminationMode = None


    def _deserialize(self, params):
        self.ExternalReturnAgreementId = params.get("ExternalReturnAgreementId")
        self.ExternalReturnContractEffectiveTimestamp = params.get("ExternalReturnContractEffectiveTimestamp")
        self.ExternalReturnContractTerminationTimestamp = params.get("ExternalReturnContractTerminationTimestamp")
        self.ExternalReturnContractStatus = params.get("ExternalReturnContractStatus")
        self.ExternalReturnRequestId = params.get("ExternalReturnRequestId")
        self.ExternalReturnContractSignedTimestamp = params.get("ExternalReturnContractSignedTimestamp")
        self.ExternalReturnContractExpiredTimestamp = params.get("ExternalReturnContractExpiredTimestamp")
        self.ExternalReturnContractData = params.get("ExternalReturnContractData")
        self.ExternalReturnContractTerminationRemark = params.get("ExternalReturnContractTerminationRemark")
        self.ExternalReturnContractTerminationMode = params.get("ExternalReturnContractTerminationMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileItem(AbstractModel):
    """对账文件信息

    """

    def __init__(self):
        """
        :param FileName: STRING(256)，文件名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileName: str\n        :param RandomPassword: STRING(120)，随机密码
注意：此字段可能返回 null，表示取不到有效值。\n        :type RandomPassword: str\n        :param FilePath: STRING(512)，文件路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilePath: str\n        :param DrawCode: STRING(64)，提取码
注意：此字段可能返回 null，表示取不到有效值。\n        :type DrawCode: str\n        """
        self.FileName = None
        self.RandomPassword = None
        self.FilePath = None
        self.DrawCode = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.RandomPassword = params.get("RandomPassword")
        self.FilePath = params.get("FilePath")
        self.DrawCode = params.get("DrawCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MerchantManagementList(AbstractModel):
    """商户查询管理端列表

    """

    def __init__(self):
        """
        :param TaxpayerName: 企业名称。\n        :type TaxpayerName: str\n        :param TaxpayerNum: 纳税人识别号(税号)	。\n        :type TaxpayerNum: str\n        :param SerialNo: 请求流水号。\n        :type SerialNo: str\n        :param InvoicePlatformId: 开票系统ID\n        :type InvoicePlatformId: int\n        """
        self.TaxpayerName = None
        self.TaxpayerNum = None
        self.SerialNo = None
        self.InvoicePlatformId = None


    def _deserialize(self, params):
        self.TaxpayerName = params.get("TaxpayerName")
        self.TaxpayerNum = params.get("TaxpayerNum")
        self.SerialNo = params.get("SerialNo")
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MerchantManagementResult(AbstractModel):
    """商户管理端结果

    """

    def __init__(self):
        """
        :param Total: 总数。\n        :type Total: int\n        :param List: 商户列表。\n        :type List: list of MerchantManagementList\n        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = MerchantManagementList()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOrderRefundQueryRequest(AbstractModel):
    """MigrateOrderRefundQuery请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param PayChannel: 支付渠道，ALIPAY对应支付宝渠道；UNIONPAY对应银联渠道\n        :type PayChannel: str\n        :param RefundOrderId: 退款订单号，最长64位，仅支持数字、 字母\n        :type RefundOrderId: str\n        :param TradeSerialNo: 退款流水号\n        :type TradeSerialNo: str\n        :param Profile: 接入环境。沙箱环境填 sandbox。\n        :type Profile: str\n        """
        self.MerchantId = None
        self.PayChannel = None
        self.RefundOrderId = None
        self.TradeSerialNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayChannel = params.get("PayChannel")
        self.RefundOrderId = params.get("RefundOrderId")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOrderRefundQueryResponse(AbstractModel):
    """MigrateOrderRefundQuery返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 请求成功状态\n        :type IsSuccess: bool\n        :param TradeSerialNo: 交易流水号\n        :type TradeSerialNo: str\n        :param TradeMsg: 交易备注\n        :type TradeMsg: str\n        :param TradeStatus: 交易状态：0=交易待处理；1=交易处理中；2=交易处理成功；3=交易失败；4=状态未知\n        :type TradeStatus: int\n        :param ThirdChannelOrderId: 第三方支付机构支付交易号
注意：此字段可能返回 null，表示取不到有效值。\n        :type ThirdChannelOrderId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IsSuccess = None
        self.TradeSerialNo = None
        self.TradeMsg = None
        self.TradeStatus = None
        self.ThirdChannelOrderId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.TradeMsg = params.get("TradeMsg")
        self.TradeStatus = params.get("TradeStatus")
        self.ThirdChannelOrderId = params.get("ThirdChannelOrderId")
        self.RequestId = params.get("RequestId")


class MigrateOrderRefundRequest(AbstractModel):
    """MigrateOrderRefund请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户代码\n        :type MerchantId: str\n        :param PayChannel: 支付渠道，ALIPAY对应支付宝渠道；UNIONPAY对应银联渠道\n        :type PayChannel: str\n        :param PayOrderId: 正向支付商户订单号\n        :type PayOrderId: str\n        :param RefundOrderId: 退款订单号，最长64位，仅支持数字、 字母\n        :type RefundOrderId: str\n        :param RefundAmt: 退款金额，单位：分。备注：改字段必须大于0 和小于10000000000的整数。\n        :type RefundAmt: int\n        :param ThirdChannelOrderId: 第三方支付机构支付交易号\n        :type ThirdChannelOrderId: str\n        :param PayAmt: 原始支付金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额\n        :type PayAmt: int\n        :param Profile: 接入环境。沙箱环境填 sandbox。\n        :type Profile: str\n        :param RefundReason: 退款原因\n        :type RefundReason: str\n        """
        self.MerchantId = None
        self.PayChannel = None
        self.PayOrderId = None
        self.RefundOrderId = None
        self.RefundAmt = None
        self.ThirdChannelOrderId = None
        self.PayAmt = None
        self.Profile = None
        self.RefundReason = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayChannel = params.get("PayChannel")
        self.PayOrderId = params.get("PayOrderId")
        self.RefundOrderId = params.get("RefundOrderId")
        self.RefundAmt = params.get("RefundAmt")
        self.ThirdChannelOrderId = params.get("ThirdChannelOrderId")
        self.PayAmt = params.get("PayAmt")
        self.Profile = params.get("Profile")
        self.RefundReason = params.get("RefundReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOrderRefundResponse(AbstractModel):
    """MigrateOrderRefund返回参数结构体

    """

    def __init__(self):
        """
        :param IsSuccess: 请求成功状态\n        :type IsSuccess: bool\n        :param TradeSerialNo: 退款流水号\n        :type TradeSerialNo: str\n        :param TradeMsg: 交易备注\n        :type TradeMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IsSuccess = None
        self.TradeSerialNo = None
        self.TradeMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.TradeMsg = params.get("TradeMsg")
        self.RequestId = params.get("RequestId")


class ModifyAgentTaxPaymentInfoRequest(AbstractModel):
    """ModifyAgentTaxPaymentInfo请求参数结构体

    """

    def __init__(self):
        """
        :param BatchNum: 批次号\n        :type BatchNum: int\n        :param RawElectronicCertUrl: 新源电子凭证地址\n        :type RawElectronicCertUrl: str\n        :param FileName: 新的文件名\n        :type FileName: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.BatchNum = None
        self.RawElectronicCertUrl = None
        self.FileName = None
        self.Profile = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        self.RawElectronicCertUrl = params.get("RawElectronicCertUrl")
        self.FileName = params.get("FileName")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentTaxPaymentInfoResponse(AbstractModel):
    """ModifyAgentTaxPaymentInfo返回参数结构体

    """

    def __init__(self):
        """
        :param AgentTaxPaymentBatch: 代理商完税证明批次信息\n        :type AgentTaxPaymentBatch: :class:`tencentcloud.cpdp.v20190820.models.AgentTaxPaymentBatch`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentTaxPaymentBatch = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentTaxPaymentBatch") is not None:
            self.AgentTaxPaymentBatch = AgentTaxPaymentBatch()
            self.AgentTaxPaymentBatch._deserialize(params.get("AgentTaxPaymentBatch"))
        self.RequestId = params.get("RequestId")


class ModifyMerchantRequest(AbstractModel):
    """ModifyMerchant请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 进件成功后返给商户的AppId\n        :type MerchantAppId: str\n        :param MerchantName: 收款商户名称\n        :type MerchantName: str\n        :param BusinessPayFlag: B2B 支付标志。是否开通 B2B支付， 1:开通 0:不开通。\n        :type BusinessPayFlag: str\n        """
        self.MerchantAppId = None
        self.MerchantName = None
        self.BusinessPayFlag = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.MerchantName = params.get("MerchantName")
        self.BusinessPayFlag = params.get("BusinessPayFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMerchantResponse(AbstractModel):
    """ModifyMerchant返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMntMbrBindRelateAcctBankCodeRequest(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param SubAcctNo: STRING(50)，见证子账户的账号\n        :type SubAcctNo: str\n        :param MemberBindAcctNo: STRING(50)，会员绑定账号\n        :type MemberBindAcctNo: str\n        :param AcctOpenBranchName: STRING(150)，开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）\n        :type AcctOpenBranchName: str\n        :param CnapsBranchId: STRING(20)，大小额行号（CnapsBranchId和EiconBankBranchId两者二选一必填）\n        :type CnapsBranchId: str\n        :param EiconBankBranchId: STRING(20)，超级网银行号\n        :type EiconBankBranchId: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberBindAcctNo = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberBindAcctNo = params.get("MemberBindAcctNo")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMntMbrBindRelateAcctBankCodeResponse(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class Order(AbstractModel):
    """线下查票-订单信息

    """

    def __init__(self):
        """
        :param AmountHasTax: 含税金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type AmountHasTax: float\n        :param Discount: 优惠金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type Discount: float\n        :param SellerName: 销方名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SellerName: str\n        :param InvoiceType: 发票类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvoiceType: int\n        :param Name: 默认“”
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Amount: 支付金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type Amount: float\n        :param OrderDate: 下单日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrderDate: str\n        :param OrderId: 订单号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrderId: str\n        :param StoreNo: 门店号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StoreNo: str\n        :param Items: 明细
注意：此字段可能返回 null，表示取不到有效值。\n        :type Items: list of OrderItem\n        """
        self.AmountHasTax = None
        self.Discount = None
        self.SellerName = None
        self.InvoiceType = None
        self.Name = None
        self.Amount = None
        self.OrderDate = None
        self.OrderId = None
        self.StoreNo = None
        self.Items = None


    def _deserialize(self, params):
        self.AmountHasTax = params.get("AmountHasTax")
        self.Discount = params.get("Discount")
        self.SellerName = params.get("SellerName")
        self.InvoiceType = params.get("InvoiceType")
        self.Name = params.get("Name")
        self.Amount = params.get("Amount")
        self.OrderDate = params.get("OrderDate")
        self.OrderId = params.get("OrderId")
        self.StoreNo = params.get("StoreNo")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrderItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderItem(AbstractModel):
    """线下查票-订单明细

    """

    def __init__(self):
        """
        :param AmountHasTax: 明细金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type AmountHasTax: float\n        :param Discount: 优惠金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type Discount: float\n        :param Name: 商品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Models: 型号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Models: str\n        :param Total: 数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param Unit: 数量单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Unit: str\n        :param Status: 默认“0”
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param Price: 单价
注意：此字段可能返回 null，表示取不到有效值。\n        :type Price: float\n        :param TaxCode: 商品编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaxCode: str\n        """
        self.AmountHasTax = None
        self.Discount = None
        self.Name = None
        self.Models = None
        self.Total = None
        self.Unit = None
        self.Status = None
        self.Price = None
        self.TaxCode = None


    def _deserialize(self, params):
        self.AmountHasTax = params.get("AmountHasTax")
        self.Discount = params.get("Discount")
        self.Name = params.get("Name")
        self.Models = params.get("Models")
        self.Total = params.get("Total")
        self.Unit = params.get("Unit")
        self.Status = params.get("Status")
        self.Price = params.get("Price")
        self.TaxCode = params.get("TaxCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationInfo(AbstractModel):
    """公司信息

    """

    def __init__(self):
        """
        :param OrganizationName: 公司名称，个体工商户必输\n        :type OrganizationName: str\n        :param OrganizationType: 公司证件类型，个体工商户必输，证件类型仅支持73\n        :type OrganizationType: str\n        :param OrganizationCode: 公司证件号码，个体工商户必输\n        :type OrganizationCode: str\n        :param LegalPersonName: 法人名称，如果SubMchName不是法人，需要另外送入法人信息（企业必输）
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type LegalPersonName: str\n        :param LegalPersonIdType: 法人证件类型，如果SubMchName不是法人，需要另外送入法人信息（企业必输）\n        :type LegalPersonIdType: str\n        :param LegalPersonIdCode: 法人证件号码，如果SubMchName不是法人，需要另外送入法人信息（企业必输）
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type LegalPersonIdCode: str\n        """
        self.OrganizationName = None
        self.OrganizationType = None
        self.OrganizationCode = None
        self.LegalPersonName = None
        self.LegalPersonIdType = None
        self.LegalPersonIdCode = None


    def _deserialize(self, params):
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationType = params.get("OrganizationType")
        self.OrganizationCode = params.get("OrganizationCode")
        self.LegalPersonName = params.get("LegalPersonName")
        self.LegalPersonIdType = params.get("LegalPersonIdType")
        self.LegalPersonIdCode = params.get("LegalPersonIdCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctBindingRequest(AbstractModel):
    """QueryAcctBinding请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param MidasSecretId: 由平台客服提供的计费密钥Id\n        :type MidasSecretId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.SubAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctBindingResponse(AbstractModel):
    """QueryAcctBinding返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总行数\n        :type TotalCount: int\n        :param BankCardItems: 银行卡信息列表\n        :type BankCardItems: list of BankCardItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.BankCardItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BankCardItems") is not None:
            self.BankCardItems = []
            for item in params.get("BankCardItems"):
                obj = BankCardItem()
                obj._deserialize(item)
                self.BankCardItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryAcctInfoListRequest(AbstractModel):
    """QueryAcctInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param QueryAcctBeginTime: 查询开始时间(以开户时间为准)\n        :type QueryAcctBeginTime: str\n        :param QueryAcctEndTime: 查询结束时间(以开户时间为准)\n        :type QueryAcctEndTime: str\n        :param PageOffset: 分页号,  起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照开户时间的先后\n        :type PageOffset: str\n        :param MidasSecretId: 由平台客服提供的计费密钥Id\n        :type MidasSecretId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.QueryAcctBeginTime = None
        self.QueryAcctEndTime = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.QueryAcctBeginTime = params.get("QueryAcctBeginTime")
        self.QueryAcctEndTime = params.get("QueryAcctEndTime")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctInfoListResponse(AbstractModel):
    """QueryAcctInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param ResultCount: 本次交易返回查询结果记录数\n        :type ResultCount: int\n        :param TotalCount: 符合业务查询条件的记录总数\n        :type TotalCount: int\n        :param QueryAcctItems: 查询结果项 [object,object]\n        :type QueryAcctItems: list of QueryAcctItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultCount = None
        self.TotalCount = None
        self.QueryAcctItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.TotalCount = params.get("TotalCount")
        if params.get("QueryAcctItems") is not None:
            self.QueryAcctItems = []
            for item in params.get("QueryAcctItems"):
                obj = QueryAcctItem()
                obj._deserialize(item)
                self.QueryAcctItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryAcctInfoRequest(AbstractModel):
    """QueryAcctInfo请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId\n        :type MidasAppId: str\n        :param SubMchId: 业务平台的子商户Id，唯一\n        :type SubMchId: str\n        :param MidasSecretId: 由平台客服提供的计费密钥Id\n        :type MidasSecretId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.SubMchId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctInfoResponse(AbstractModel):
    """QueryAcctInfo返回参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SubMchName: 子商户名称\n        :type SubMchName: str\n        :param SubMchType: 子商户类型：
个人: personal
企业：enterprise
缺省： enterprise\n        :type SubMchType: str\n        :param ShortName: 不填则默认子商户名称\n        :type ShortName: str\n        :param Address: 子商户地址\n        :type Address: str\n        :param Contact: 子商户联系人子商户联系人
<敏感信息>\n        :type Contact: str\n        :param Mobile: 联系人手机号
<敏感信息>\n        :type Mobile: str\n        :param Email: 邮箱 
<敏感信息>\n        :type Email: str\n        :param SubMchId: 子商户id\n        :type SubMchId: str\n        :param SubAcctNo: 子账户\n        :type SubAcctNo: str\n        :param SubMerchantMemberType: 子商户会员类型：
general:普通子账户
merchant:商户子账户
缺省： general
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubMerchantMemberType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SubAppId = None
        self.SubMchName = None
        self.SubMchType = None
        self.ShortName = None
        self.Address = None
        self.Contact = None
        self.Mobile = None
        self.Email = None
        self.SubMchId = None
        self.SubAcctNo = None
        self.SubMerchantMemberType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubMchName = params.get("SubMchName")
        self.SubMchType = params.get("SubMchType")
        self.ShortName = params.get("ShortName")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SubMchId = params.get("SubMchId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")
        self.RequestId = params.get("RequestId")


class QueryAcctItem(AbstractModel):
    """查询账户列表接口

    """

    def __init__(self):
        """
        :param SubMchType: 子商户类型：
个人: personal
企业：enterprise
缺省： enterprise\n        :type SubMchType: str\n        :param SubMchName: 子商户名称\n        :type SubMchName: str\n        :param SubAcctNo: 子账号号\n        :type SubAcctNo: str\n        :param ShortName: 不填则默认子商户名称\n        :type ShortName: str\n        :param SubMchId: 业务平台的子商户Id，唯一\n        :type SubMchId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param Contact: 子商户联系人
<敏感信息>\n        :type Contact: str\n        :param Address: 子商户地址\n        :type Address: str\n        :param Mobile: 联系人手机号
<敏感信息>\n        :type Mobile: str\n        :param Email: 邮箱 
<敏感信息>\n        :type Email: str\n        :param SubMerchantMemberType: 子商户会员类型：
general:普通子账户
merchant:商户子账户
缺省： general
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubMerchantMemberType: str\n        """
        self.SubMchType = None
        self.SubMchName = None
        self.SubAcctNo = None
        self.ShortName = None
        self.SubMchId = None
        self.SubAppId = None
        self.Contact = None
        self.Address = None
        self.Mobile = None
        self.Email = None
        self.SubMerchantMemberType = None


    def _deserialize(self, params):
        self.SubMchType = params.get("SubMchType")
        self.SubMchName = params.get("SubMchName")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ShortName = params.get("ShortName")
        self.SubMchId = params.get("SubMchId")
        self.SubAppId = params.get("SubAppId")
        self.Contact = params.get("Contact")
        self.Address = params.get("Address")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAgentStatementsRequest(AbstractModel):
    """QueryAgentStatements请求参数结构体

    """

    def __init__(self):
        """
        :param Date: 结算单日期，月结算单填每月1日\n        :type Date: str\n        :param Type: 日结算单:daily
月结算单:monthly\n        :type Type: str\n        """
        self.Date = None
        self.Type = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAgentStatementsResponse(AbstractModel):
    """QueryAgentStatements返回参数结构体

    """

    def __init__(self):
        """
        :param FileUrl: 文件下载链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.RequestId = params.get("RequestId")


class QueryAgentTaxPaymentBatchRequest(AbstractModel):
    """QueryAgentTaxPaymentBatch请求参数结构体

    """

    def __init__(self):
        """
        :param BatchNum: 批次号\n        :type BatchNum: int\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.BatchNum = None
        self.Profile = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAgentTaxPaymentBatchResponse(AbstractModel):
    """QueryAgentTaxPaymentBatch返回参数结构体

    """

    def __init__(self):
        """
        :param AgentTaxPaymentBatch: 代理商完税证明批次信息\n        :type AgentTaxPaymentBatch: :class:`tencentcloud.cpdp.v20190820.models.AgentTaxPaymentBatch`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AgentTaxPaymentBatch = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentTaxPaymentBatch") is not None:
            self.AgentTaxPaymentBatch = AgentTaxPaymentBatch()
            self.AgentTaxPaymentBatch._deserialize(params.get("AgentTaxPaymentBatch"))
        self.RequestId = params.get("RequestId")


class QueryAnchorContractInfoRequest(AbstractModel):
    """QueryAnchorContractInfo请求参数结构体

    """

    def __init__(self):
        """
        :param BeginTime: 起始时间，格式为yyyy-MM-dd\n        :type BeginTime: str\n        :param EndTime: 起始时间，格式为yyyy-MM-dd\n        :type EndTime: str\n        """
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAnchorContractInfoResponse(AbstractModel):
    """QueryAnchorContractInfo返回参数结构体

    """

    def __init__(self):
        """
        :param AnchorContractInfoList: 签约主播数据\n        :type AnchorContractInfoList: list of AnchorContractInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AnchorContractInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AnchorContractInfoList") is not None:
            self.AnchorContractInfoList = []
            for item in params.get("AnchorContractInfoList"):
                obj = AnchorContractInfo()
                obj._deserialize(item)
                self.AnchorContractInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryApplicationMaterialRequest(AbstractModel):
    """QueryApplicationMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param DeclareId: 申报流水号\n        :type DeclareId: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.DeclareId = None
        self.Profile = None


    def _deserialize(self, params):
        self.DeclareId = params.get("DeclareId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryApplicationMaterialResponse(AbstractModel):
    """QueryApplicationMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功申报材料查询结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryDeclareResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryBalanceRequest(AbstractModel):
    """QueryBalance请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param QueryFlag: 2：普通会员子账号
3：功能子账号\n        :type QueryFlag: str\n        :param PageOffset: 起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后\n        :type PageOffset: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.SubAppId = None
        self.QueryFlag = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.QueryFlag = params.get("QueryFlag")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBalanceResponse(AbstractModel):
    """QueryBalance返回参数结构体

    """

    def __init__(self):
        """
        :param ResultCount: 本次交易返回查询结果记录数\n        :type ResultCount: str\n        :param StartRecordOffset: 起始记录号\n        :type StartRecordOffset: str\n        :param EndFlag: 结束标志\n        :type EndFlag: str\n        :param TotalCount: 符合业务查询条件的记录总数\n        :type TotalCount: str\n        :param QueryItems: 查询结果项\n        :type QueryItems: list of QueryItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultCount = None
        self.StartRecordOffset = None
        self.EndFlag = None
        self.TotalCount = None
        self.QueryItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.StartRecordOffset = params.get("StartRecordOffset")
        self.EndFlag = params.get("EndFlag")
        self.TotalCount = params.get("TotalCount")
        if params.get("QueryItems") is not None:
            self.QueryItems = []
            for item in params.get("QueryItems"):
                obj = QueryItem()
                obj._deserialize(item)
                self.QueryItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryBankClearRequest(AbstractModel):
    """QueryBankClear请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param FunctionFlag: STRING(2)，功能标志（1: 全部; 2: 指定时间段）\n        :type FunctionFlag: str\n        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）\n        :type PageNum: str\n        :param StartDate: STRING(8)，开始日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式: 20190101）\n        :type StartDate: str\n        :param EndDate: STRING(8)，终止日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式：20190101）\n        :type EndDate: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBankClearResponse(AbstractModel):
    """QueryBankClear返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultNum: str\n        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartRecordNo: str\n        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndFlag: str\n        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数, 一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalNum: str\n        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranItemArray: list of ClearItem\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = ClearItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankTransactionDetailsRequest(AbstractModel):
    """QueryBankTransactionDetails请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）\n        :type FunctionFlag: str\n        :param SubAcctNo: STRING(50)，见证子帐户的帐号\n        :type SubAcctNo: str\n        :param QueryFlag: STRING(4)，查询标志（1: 全部; 2: 转出; 3: 转入 ）\n        :type QueryFlag: str\n        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）\n        :type PageNum: str\n        :param StartDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）\n        :type StartDate: str\n        :param EndDate: STRING(8)，终止日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）\n        :type EndDate: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBankTransactionDetailsResponse(AbstractModel):
    """QueryBankTransactionDetails返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultNum: str\n        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartRecordNo: str\n        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndFlag: str\n        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalNum: str\n        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranItemArray: list of TransactionItem\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransactionItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankWithdrawCashDetailsRequest(AbstractModel):
    """QueryBankWithdrawCashDetails请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）\n        :type FunctionFlag: str\n        :param SubAcctNo: STRING(50)，见证子帐户的帐号\n        :type SubAcctNo: str\n        :param QueryFlag: STRING(4)，查询标志（2: 提现; 3: 清分）\n        :type QueryFlag: str\n        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）\n        :type PageNum: str\n        :param BeginDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）\n        :type BeginDate: str\n        :param EndDate: STRING(8)，结束日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）\n        :type EndDate: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.BeginDate = None
        self.EndDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBankWithdrawCashDetailsResponse(AbstractModel):
    """QueryBankWithdrawCashDetails返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultNum: str\n        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartRecordNo: str\n        :param EndFlag: STRING(2)，结束标志（0:否; 1:是）
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndFlag: str\n        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalNum: str\n        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranItemArray: list of WithdrawItem\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = WithdrawItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBillDownloadURLData(AbstractModel):
    """智能代发-单笔代发转账对账单返回数据

    """

    def __init__(self):
        """
        :param BillDownloadURL: 统一对账单下载链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type BillDownloadURL: str\n        :param OriginalBillDownloadURL: 渠道原始对账单下载链接
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalBillDownloadURL: str\n        """
        self.BillDownloadURL = None
        self.OriginalBillDownloadURL = None


    def _deserialize(self, params):
        self.BillDownloadURL = params.get("BillDownloadURL")
        self.OriginalBillDownloadURL = params.get("OriginalBillDownloadURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBillDownloadURLRequest(AbstractModel):
    """QueryBillDownloadURL请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param TransferType: 代发类型：
1、 微信企业付款 
2、 支付宝转账 
3、 平安银企直联代发转账\n        :type TransferType: int\n        :param BillDate: 账单日期，格式yyyy-MM-dd\n        :type BillDate: str\n        """
        self.MerchantId = None
        self.TransferType = None
        self.BillDate = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransferType = params.get("TransferType")
        self.BillDate = params.get("BillDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBillDownloadURLResponse(AbstractModel):
    """QueryBillDownloadURL返回参数结构体

    """

    def __init__(self):
        """
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功\n        :type ErrCode: str\n        :param ErrMessage: 响应消息\n        :type ErrMessage: str\n        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryBillDownloadURLData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryBillDownloadURLData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryCommonTransferRechargeRequest(AbstractModel):
    """QueryCommonTransferRecharge请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param FunctionFlag: STRING(2)，功能标志（1为查询当日数据，0查询历史数据）\n        :type FunctionFlag: str\n        :param StartDate: STRING(8)，开始日期（格式：20190101）\n        :type StartDate: str\n        :param EndDate: STRING(8)，终止日期（格式：20190101）\n        :type EndDate: str\n        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）\n        :type PageNum: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.StartDate = None
        self.EndDate = None
        self.PageNum = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.PageNum = params.get("PageNum")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCommonTransferRechargeResponse(AbstractModel):
    """QueryCommonTransferRecharge返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultNum: str\n        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartRecordNo: str\n        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndFlag: str\n        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalNum: str\n        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranItemArray: list of TransferItem\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransferItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryContractRequest(AbstractModel):
    """QueryContract请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合\n        :type UserId: str\n        :param Channel: 指定渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定\n        :type Channel: str\n        :param ContractQueryMode: 枚举值：
CONTRACT_QUERY_MODE_BY_OUT_CONTRACT_CODE：按 OutContractCode + ContractSceneId 查询
CONTRACT_QUERY_MODE_BY_CHANNEL_CONTRACT_CODE：按ChannelContractCode查询\n        :type ContractQueryMode: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param OutContractCode: 业务签约合同协议号 当 ContractQueryMode=CONTRACT_QUERY_MODE_BY_OUT_CONTRACT_CODE 时 ，必填\n        :type OutContractCode: str\n        :param ContractSceneId: 签约场景ID，当 ContractQueryMode=CONTRACT_QUERY_MODE_BY_OUT_CONTRACT_CODE 时 必填，在米大师侧托管后生成\n        :type ContractSceneId: str\n        :param ChannelContractCode: 米大师生成的协议号 ，当 ContractQueryMode=CONTRACT_QUERY_MODE_BY_CHANNEL_CONTRACT_CODE 时必填\n        :type ChannelContractCode: str\n        :param ExternalContractData: 第三方渠道合约数据，为json字符串，与特定渠道有关\n        :type ExternalContractData: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param UserType: USER_ID: 用户ID
ANONYMOUS: 匿名类型 USER_ID
默认值为 USER_ID\n        :type UserType: str\n        :param MigrateMode: 签约代扣穿透查询存量数据迁移模式\n        :type MigrateMode: str\n        :param ContractMethod: 签约方式\n        :type ContractMethod: str\n        """
        self.MidasAppId = None
        self.UserId = None
        self.Channel = None
        self.ContractQueryMode = None
        self.MidasSignature = None
        self.MidasSecretId = None
        self.SubAppId = None
        self.OutContractCode = None
        self.ContractSceneId = None
        self.ChannelContractCode = None
        self.ExternalContractData = None
        self.MidasEnvironment = None
        self.UserType = None
        self.MigrateMode = None
        self.ContractMethod = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.ContractQueryMode = params.get("ContractQueryMode")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasSecretId = params.get("MidasSecretId")
        self.SubAppId = params.get("SubAppId")
        self.OutContractCode = params.get("OutContractCode")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ChannelContractCode = params.get("ChannelContractCode")
        self.ExternalContractData = params.get("ExternalContractData")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.UserType = params.get("UserType")
        self.MigrateMode = params.get("MigrateMode")
        self.ContractMethod = params.get("ContractMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryContractResponse(AbstractModel):
    """QueryContract返回参数结构体

    """

    def __init__(self):
        """
        :param ContractData: 签约数据\n        :type ContractData: :class:`tencentcloud.cpdp.v20190820.models.ResponseQueryContract`\n        :param Msg: 请求处理信息\n        :type Msg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ContractData = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContractData") is not None:
            self.ContractData = ResponseQueryContract()
            self.ContractData._deserialize(params.get("ContractData"))
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class QueryCustAcctIdBalanceRequest(AbstractModel):
    """QueryCustAcctIdBalance请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param QueryFlag: STRING(4)，查询标志（2: 普通会员子账号; 3: 功能子账号）\n        :type QueryFlag: str\n        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）\n        :type PageNum: str\n        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2时，子账号必输）\n        :type SubAcctNo: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustAcctIdBalanceResponse(AbstractModel):
    """QueryCustAcctIdBalance返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultNum: str\n        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartRecordNo: str\n        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndFlag: str\n        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalNum: str\n        :param AcctArray: 账户信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type AcctArray: list of Acct\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.AcctArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("AcctArray") is not None:
            self.AcctArray = []
            for item in params.get("AcctArray"):
                obj = Acct()
                obj._deserialize(item)
                self.AcctArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryDeclareData(AbstractModel):
    """成功申报材料查询数据

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param TransactionId: 对接方汇出指令编号\n        :type TransactionId: str\n        :param DeclareId: 申报流水号\n        :type DeclareId: str\n        :param OriginalDeclareId: 原申报流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalDeclareId: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param SourceCurrency: 源币种\n        :type SourceCurrency: str\n        :param SourceAmount: 源金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type SourceAmount: str\n        :param TargetCurrency: 目的币种\n        :type TargetCurrency: str\n        :param TargetAmount: 目的金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TargetAmount: str\n        :param TradeCode: 交易编码\n        :type TradeCode: str\n        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
        self.MerchantId = None
        self.TransactionId = None
        self.DeclareId = None
        self.OriginalDeclareId = None
        self.PayerId = None
        self.SourceCurrency = None
        self.SourceAmount = None
        self.TargetCurrency = None
        self.TargetAmount = None
        self.TradeCode = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.DeclareId = params.get("DeclareId")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.PayerId = params.get("PayerId")
        self.SourceCurrency = params.get("SourceCurrency")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TargetAmount = params.get("TargetAmount")
        self.TradeCode = params.get("TradeCode")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDeclareResult(AbstractModel):
    """成功申报材料查询结果

    """

    def __init__(self):
        """
        :param Data: 成功申报材料查询数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareData`\n        :param Code: 错误码\n        :type Code: str\n        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryDeclareData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExchangeRateRequest(AbstractModel):
    """QueryExchangeRate请求参数结构体

    """

    def __init__(self):
        """
        :param SourceCurrency: 源币种 (默认CNY)\n        :type SourceCurrency: str\n        :param TargetCurrency: 目的币种 (见常见问题-汇出币种)\n        :type TargetCurrency: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.Profile = None


    def _deserialize(self, params):
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExchangeRateResponse(AbstractModel):
    """QueryExchangeRate返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询汇率结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryExchangerateResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryExchangerateResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryExchangerateData(AbstractModel):
    """查询汇率数据

    """

    def __init__(self):
        """
        :param Rate: 汇率\n        :type Rate: str\n        :param SourceCurrency: 源币种\n        :type SourceCurrency: str\n        :param TargetCurrency: 目的币种\n        :type TargetCurrency: str\n        :param RateTime: 汇率时间\n        :type RateTime: str\n        :param BaseCurrency: 基准币种\n        :type BaseCurrency: str\n        """
        self.Rate = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.RateTime = None
        self.BaseCurrency = None


    def _deserialize(self, params):
        self.Rate = params.get("Rate")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.RateTime = params.get("RateTime")
        self.BaseCurrency = params.get("BaseCurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExchangerateResult(AbstractModel):
    """查询汇率结果

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Data: 查询汇率数据数组\n        :type Data: list of QueryExchangerateData\n        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryExchangerateData()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceRequest(AbstractModel):
    """QueryInvoice请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID\n        :type InvoicePlatformId: int\n        :param OrderId: 订单号\n        :type OrderId: str\n        :param OrderSn: 业务开票号\n        :type OrderSn: str\n        :param IsRed: 发票种类：
0：蓝票
1：红票【该字段默认为0， 如果需要查询红票信息，本字段必须传1，否则可能查询不到需要的发票信息】。\n        :type IsRed: int\n        :param Profile: 接入环境。沙箱环境填sandbox。\n        :type Profile: str\n        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道\n        :type InvoiceChannel: int\n        :param SellerTaxpayerNum: 当渠道为线下渠道时，必填\n        :type SellerTaxpayerNum: str\n        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.OrderSn = None
        self.IsRed = None
        self.Profile = None
        self.InvoiceChannel = None
        self.SellerTaxpayerNum = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.OrderSn = params.get("OrderSn")
        self.IsRed = params.get("IsRed")
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceResponse(AbstractModel):
    """QueryInvoice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 发票查询结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryInvoiceResult(AbstractModel):
    """查询发票结果

    """

    def __init__(self):
        """
        :param Message: 错误消息\n        :type Message: str\n        :param Code: 错误码\n        :type Code: int\n        :param Data: 查询发票数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResultData`\n        :param Order: 订单数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Order: :class:`tencentcloud.cpdp.v20190820.models.Order`\n        """
        self.Message = None
        self.Code = None
        self.Data = None
        self.Order = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryInvoiceResultData()
            self.Data._deserialize(params.get("Data"))
        if params.get("Order") is not None:
            self.Order = Order()
            self.Order._deserialize(params.get("Order"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceResultData(AbstractModel):
    """查询发票结果数据

    """

    def __init__(self):
        """
        :param OrderId: 订单号\n        :type OrderId: str\n        :param OrderSn: 业务开票号\n        :type OrderSn: str\n        :param Status: 发票状态\n        :type Status: int\n        :param Message: 开票描述\n        :type Message: str\n        :param TicketDate: 开票日期\n        :type TicketDate: str\n        :param TicketSn: 发票号码\n        :type TicketSn: str\n        :param TicketCode: 发票代码\n        :type TicketCode: str\n        :param CheckCode: 检验码\n        :type CheckCode: str\n        :param AmountWithTax: 含税金额(元)\n        :type AmountWithTax: str\n        :param AmountWithoutTax: 不含税金额(元)\n        :type AmountWithoutTax: str\n        :param TaxAmount: 税额(元)\n        :type TaxAmount: str\n        :param IsRedWashed: 是否被红冲\n        :type IsRedWashed: int\n        :param PdfUrl: pdf地址\n        :type PdfUrl: str\n        """
        self.OrderId = None
        self.OrderSn = None
        self.Status = None
        self.Message = None
        self.TicketDate = None
        self.TicketSn = None
        self.TicketCode = None
        self.CheckCode = None
        self.AmountWithTax = None
        self.AmountWithoutTax = None
        self.TaxAmount = None
        self.IsRedWashed = None
        self.PdfUrl = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.OrderSn = params.get("OrderSn")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.TicketDate = params.get("TicketDate")
        self.TicketSn = params.get("TicketSn")
        self.TicketCode = params.get("TicketCode")
        self.CheckCode = params.get("CheckCode")
        self.AmountWithTax = params.get("AmountWithTax")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.TaxAmount = params.get("TaxAmount")
        self.IsRedWashed = params.get("IsRedWashed")
        self.PdfUrl = params.get("PdfUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceV2Request(AbstractModel):
    """QueryInvoiceV2请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID\n        :type InvoicePlatformId: int\n        :param OrderId: 订单号\n        :type OrderId: str\n        :param IsRed: 发票种类：
0：蓝票
1：红票【该字段默认为0， 如果需要查询红票信息，本字段必须传1，否则可能查询不到需要的发票信息】。\n        :type IsRed: int\n        :param Profile: 接入环境。沙箱环境填sandbox。\n        :type Profile: str\n        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道\n        :type InvoiceChannel: int\n        :param SellerTaxpayerNum: 当渠道为线下渠道时，必填\n        :type SellerTaxpayerNum: str\n        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.IsRed = None
        self.Profile = None
        self.InvoiceChannel = None
        self.SellerTaxpayerNum = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.IsRed = params.get("IsRed")
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceV2Response(AbstractModel):
    """QueryInvoiceV2返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 发票查询结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResultData`\n        :param ErrCode: 错误码\n        :type ErrCode: str\n        :param ErrMessage: 错误消息\n        :type ErrMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.ErrCode = None
        self.ErrMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryInvoiceResultData()
            self.Result._deserialize(params.get("Result"))
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.RequestId = params.get("RequestId")


class QueryItem(AbstractModel):
    """聚鑫商户余额查询输出项

    """

    def __init__(self):
        """
        :param SubAcctNo: 子商户账户\n        :type SubAcctNo: str\n        :param SubAcctProperty: 子账户属性 
1：普通会员子账号 
2：挂账子账号 
3：手续费子账号 
4：利息子账号
5：平台担保子账号\n        :type SubAcctProperty: str\n        :param SubMchId: 业务平台的子商户Id，唯一\n        :type SubMchId: str\n        :param SubAcctName: 子账户名称\n        :type SubAcctName: str\n        :param AcctAvailBal: 账户可用余额\n        :type AcctAvailBal: str\n        :param CashAmt: 可提现金额\n        :type CashAmt: str\n        :param MaintenanceDate: 维护日期 开户日期或修改日期\n        :type MaintenanceDate: str\n        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.SubMchId = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.SubMchId = params.get("SubMchId")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemberBindRequest(AbstractModel):
    """QueryMemberBind请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param QueryFlag: STRING(4)，查询标志（1: 全部会员; 2: 单个会员; 3: 单个会员的证件信息）\n        :type QueryFlag: str\n        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）\n        :type PageNum: str\n        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2或3时，子账户账号必输）\n        :type SubAcctNo: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemberBindResponse(AbstractModel):
    """QueryMemberBind返回参数结构体

    """

    def __init__(self):
        """
        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultNum: str\n        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartRecordNo: str\n        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndFlag: str\n        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalNum: str\n        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranItemArray: list of TranItem\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TranItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class QueryMemberTransactionRequest(AbstractModel):
    """QueryMemberTransaction请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param FunctionFlag: STRING(2)，功能标志（1: 下单预支付; 2: 确认并付款; 3: 退款; 6: 直接支付T+1; 9: 直接支付T+0）\n        :type FunctionFlag: str\n        :param OutSubAcctNo: STRING(50)，转出方的见证子账户的账号（付款方）\n        :type OutSubAcctNo: str\n        :param OutMemberCode: STRING(32)，转出方的交易网会员代码\n        :type OutMemberCode: str\n        :param OutSubAcctName: STRING(150)，转出方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）\n        :type OutSubAcctName: str\n        :param InSubAcctNo: STRING(50)，转入方的见证子账户的账号（收款方）\n        :type InSubAcctNo: str\n        :param InMemberCode: STRING(32)，转入方的交易网会员代码\n        :type InMemberCode: str\n        :param InSubAcctName: STRING(150)，转入方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）\n        :type InSubAcctName: str\n        :param TranAmt: STRING(20)，交易金额\n        :type TranAmt: str\n        :param TranFee: STRING(20)，交易费用（平台收取交易费用）\n        :type TranFee: str\n        :param TranType: STRING(20)，交易类型（01: 普通交易）\n        :type TranType: str\n        :param Ccy: STRING(3)，币种（默认: RMB）\n        :type Ccy: str\n        :param OrderNo: STRING(50)，订单号（功能标志为1,2,3时必输）\n        :type OrderNo: str\n        :param OrderContent: STRING(500)，订单内容\n        :type OrderContent: str\n        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）\n        :type Remark: str\n        :param ReservedMsg: STRING(1027)，保留域（若需短信验证码则此项必输短信指令号）\n        :type ReservedMsg: str\n        :param WebSign: STRING(300)，网银签名（若需短信验证码则此项必输）\n        :type WebSign: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.OutSubAcctNo = None
        self.OutMemberCode = None
        self.OutSubAcctName = None
        self.InSubAcctNo = None
        self.InMemberCode = None
        self.InSubAcctName = None
        self.TranAmt = None
        self.TranFee = None
        self.TranType = None
        self.Ccy = None
        self.OrderNo = None
        self.OrderContent = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.OutMemberCode = params.get("OutMemberCode")
        self.OutSubAcctName = params.get("OutSubAcctName")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.InMemberCode = params.get("InMemberCode")
        self.InSubAcctName = params.get("InSubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.TranFee = params.get("TranFee")
        self.TranType = params.get("TranType")
        self.Ccy = params.get("Ccy")
        self.OrderNo = params.get("OrderNo")
        self.OrderContent = params.get("OrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemberTransactionResponse(AbstractModel):
    """QueryMemberTransaction返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryMerchantBalanceData(AbstractModel):
    """对接账户余额查询数据

    """

    def __init__(self):
        """
        :param Currency: 余额币种\n        :type Currency: str\n        :param Balance: 账户余额\n        :type Balance: str\n        :param MerchantId: 商户ID\n        :type MerchantId: str\n        """
        self.Currency = None
        self.Balance = None
        self.MerchantId = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Balance = params.get("Balance")
        self.MerchantId = params.get("MerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantBalanceRequest(AbstractModel):
    """QueryMerchantBalance请求参数结构体

    """

    def __init__(self):
        """
        :param Currency: 余额币种\n        :type Currency: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.Currency = None
        self.Profile = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantBalanceResponse(AbstractModel):
    """QueryMerchantBalance返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 对接方账户余额查询结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryMerchantBalanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryMerchantBalanceResult(AbstractModel):
    """对接账户余额查询结果

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Data: 对接账户余额查询数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceData`\n        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryMerchantBalanceData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantInfoForManagementRequest(AbstractModel):
    """QueryMerchantInfoForManagement请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID\n        :type InvoicePlatformId: int\n        :param Offset: 页码\n        :type Offset: int\n        :param Limit: 页大小\n        :type Limit: int\n        :param Profile: 接入环境。沙箱环境填sandbox。\n        :type Profile: str\n        """
        self.InvoicePlatformId = None
        self.Offset = None
        self.Limit = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantInfoForManagementResponse(AbstractModel):
    """QueryMerchantInfoForManagement返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 商户结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.MerchantManagementResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = MerchantManagementResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryMerchantOrderRequest(AbstractModel):
    """QueryMerchantOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 进件成功后返给商户方的AppId。\n        :type MerchantAppId: str\n        :param OrderNo: 平台流水号。平台唯一订单号。\n        :type OrderNo: str\n        """
        self.MerchantAppId = None
        self.OrderNo = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantOrderResponse(AbstractModel):
    """QueryMerchantOrder返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 进件成功后返给商户方的AppId。\n        :type MerchantAppId: str\n        :param OrderNo: 平台流水号。平台唯一订单号。\n        :type OrderNo: str\n        :param Status: 订单支付状态。0-下单失败 1-下单成功未支付 2-支付成功 3-支付失败 4-退款中 5-退款成功 6-退款失败 7-待付款 8-待确认。\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantAppId = None
        self.OrderNo = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class QueryMerchantRequest(AbstractModel):
    """QueryMerchant请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 进件成功后返给商户方的 AppId\n        :type MerchantAppId: str\n        """
        self.MerchantAppId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantResponse(AbstractModel):
    """QueryMerchant返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 分配给商户的 AppId，该 AppId 为后续各项 交易的商户标识。\n        :type MerchantAppId: str\n        :param MerchantName: 收款商户名称。\n        :type MerchantName: str\n        :param BusinessPayFlag: B2B 支付标志。是否开通 B2B 支付， 1:开通 0:不开通。\n        :type BusinessPayFlag: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantAppId = None
        self.MerchantName = None
        self.BusinessPayFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.MerchantName = params.get("MerchantName")
        self.BusinessPayFlag = params.get("BusinessPayFlag")
        self.RequestId = params.get("RequestId")


class QueryOrderOutOrderList(AbstractModel):
    """查询订单接口的出参，订单列表

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param Amt: 支付金额，单位：分\n        :type Amt: int\n        :param UserId: 用户Id\n        :type UserId: str\n        :param CashAmt: 现金支付金额\n        :type CashAmt: str\n        :param Metadata: 发货标识，由业务在调用聚鑫下单 接口的时候下发\n        :type Metadata: str\n        :param PayTime: 支付时间unix时间戳\n        :type PayTime: str\n        :param CouponAmt: 抵扣券金额\n        :type CouponAmt: str\n        :param OrderTime: 下单时间unix时间戳\n        :type OrderTime: str\n        :param ProductId: 物品id\n        :type ProductId: str\n        :param SceneInfo: 高速场景信息\n        :type SceneInfo: str\n        :param OrderState: 当前订单的订单状态 
0：初始状态，获取聚鑫交易订单成功；  
1：拉起聚鑫支付页面成功，用户未 支付；
2：用户支付成功，正在发货；
3：用户支付成功，发货失败；
4：用户支付成功，发货成功；
5：聚鑫支付页面正在失效中；
6：聚鑫支付页面已经失效；\n        :type OrderState: str\n        :param Channel: 支付渠道：wechat：微信支付;
qqwallet：QQ钱包;
bank：网银\n        :type Channel: str\n        :param RefundFlag: 是否曾退款\n        :type RefundFlag: str\n        :param OutTradeNo: 务支付订单号\n        :type OutTradeNo: str\n        :param ProductName: 商品名称\n        :type ProductName: str\n        :param CallBackTime: 支付回调时间，unix时间戳\n        :type CallBackTime: str\n        :param CurrencyType: ISO 货币代码，CNY\n        :type CurrencyType: str\n        :param AcctSubAppId: 微校场景账户Id\n        :type AcctSubAppId: str\n        :param TransactionId: 调用下单接口获取的聚鑫交易订单\n        :type TransactionId: str\n        :param ChannelOrderId: 聚鑫内部渠道订单号\n        :type ChannelOrderId: str\n        :param SubOrderList: 调用下单接口传进来的 SubOutTradeNoList\n        :type SubOrderList: list of QueryOrderOutSubOrderList\n        :param ChannelExternalOrderId: 支付机构订单号\n        :type ChannelExternalOrderId: str\n        """
        self.MidasAppId = None
        self.Amt = None
        self.UserId = None
        self.CashAmt = None
        self.Metadata = None
        self.PayTime = None
        self.CouponAmt = None
        self.OrderTime = None
        self.ProductId = None
        self.SceneInfo = None
        self.OrderState = None
        self.Channel = None
        self.RefundFlag = None
        self.OutTradeNo = None
        self.ProductName = None
        self.CallBackTime = None
        self.CurrencyType = None
        self.AcctSubAppId = None
        self.TransactionId = None
        self.ChannelOrderId = None
        self.SubOrderList = None
        self.ChannelExternalOrderId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.Amt = params.get("Amt")
        self.UserId = params.get("UserId")
        self.CashAmt = params.get("CashAmt")
        self.Metadata = params.get("Metadata")
        self.PayTime = params.get("PayTime")
        self.CouponAmt = params.get("CouponAmt")
        self.OrderTime = params.get("OrderTime")
        self.ProductId = params.get("ProductId")
        self.SceneInfo = params.get("SceneInfo")
        self.OrderState = params.get("OrderState")
        self.Channel = params.get("Channel")
        self.RefundFlag = params.get("RefundFlag")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductName = params.get("ProductName")
        self.CallBackTime = params.get("CallBackTime")
        self.CurrencyType = params.get("CurrencyType")
        self.AcctSubAppId = params.get("AcctSubAppId")
        self.TransactionId = params.get("TransactionId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = QueryOrderOutSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.ChannelExternalOrderId = params.get("ChannelExternalOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderOutSubOrderList(AbstractModel):
    """子订单列表

    """

    def __init__(self):
        """
        :param Amt: 子订单支付金额\n        :type Amt: int\n        :param SubMchIncome: 子订单结算应收金额，单位：分\n        :type SubMchIncome: int\n        :param Metadata: 发货标识，由业务在调用Midas下单接口的时候下发。\n        :type Metadata: str\n        :param OriginalAmt: 子订单原始金额\n        :type OriginalAmt: int\n        :param PlatformIncome: 子订单平台应收金额，单位：分\n        :type PlatformIncome: int\n        :param ProductDetail: 子订单商品详情\n        :type ProductDetail: str\n        :param ProductName: 子订单商品名称\n        :type ProductName: str\n        :param SettleCheck: 核销状态，1表示核销，0表示未核销\n        :type SettleCheck: int\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SubOutTradeNo: 子订单号\n        :type SubOutTradeNo: str\n        """
        self.Amt = None
        self.SubMchIncome = None
        self.Metadata = None
        self.OriginalAmt = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SettleCheck = None
        self.SubAppId = None
        self.SubOutTradeNo = None


    def _deserialize(self, params):
        self.Amt = params.get("Amt")
        self.SubMchIncome = params.get("SubMchIncome")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SettleCheck = params.get("SettleCheck")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderRequest(AbstractModel):
    """QueryOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主 MidasAppId\n        :type MidasAppId: str\n        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合\n        :type UserId: str\n        :param Type: type=by_order根据订单号 查订单；
type=by_user根据用户id 查订单 。\n        :type Type: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param Count: 每页返回的记录数。根据用户 号码查询订单列表时需要传。 用于分页展示。Type=by_order时必填\n        :type Count: int\n        :param Offset: 记录数偏移量，默认从0开 始。根据用户号码查询订单列 表时需要传。用于分页展示。Type=by_order时必填\n        :type Offset: int\n        :param StartTime: 查询开始时间，Unix时间戳。Type=by_order时必填\n        :type StartTime: str\n        :param EndTime: 查询结束时间，Unix时间戳。Type=by_order时必填\n        :type EndTime: str\n        :param OutTradeNo: 业务订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo\n        :type OutTradeNo: str\n        :param TransactionId: 聚鑫订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo\n        :type TransactionId: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.UserId = None
        self.Type = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Count = None
        self.Offset = None
        self.StartTime = None
        self.EndTime = None
        self.OutTradeNo = None
        self.TransactionId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Type = params.get("Type")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Count = params.get("Count")
        self.Offset = params.get("Offset")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderResponse(AbstractModel):
    """QueryOrder返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 返回订单数\n        :type TotalNum: int\n        :param OrderList: 查询结果的订单列表\n        :type OrderList: list of QueryOrderOutOrderList\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalNum = None
        self.OrderList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("OrderList") is not None:
            self.OrderList = []
            for item in params.get("OrderList"):
                obj = QueryOrderOutOrderList()
                obj._deserialize(item)
                self.OrderList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryOutwardOrderData(AbstractModel):
    """查询汇出数据

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param TransactionId: 对接方汇出指令编号\n        :type TransactionId: str\n        :param AcctDate: 财务日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type AcctDate: str\n        :param PricingCurrency: 定价币种
注意：此字段可能返回 null，表示取不到有效值。\n        :type PricingCurrency: str\n        :param SourceCurrency: 源币种
注意：此字段可能返回 null，表示取不到有效值。\n        :type SourceCurrency: str\n        :param SourceAmount: 源金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type SourceAmount: str\n        :param TargetCurrency: 目的币种
注意：此字段可能返回 null，表示取不到有效值。\n        :type TargetCurrency: str\n        :param TargetAmount: 目的金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TargetAmount: str\n        :param FxRate: 汇率
注意：此字段可能返回 null，表示取不到有效值。\n        :type FxRate: str\n        :param Status: 指令状态\n        :type Status: str\n        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailReason: str\n        :param RefundAmount: 退汇金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type RefundAmount: str\n        :param RefundCurrency: 退汇币种
注意：此字段可能返回 null，表示取不到有效值。\n        :type RefundCurrency: str\n        """
        self.MerchantId = None
        self.TransactionId = None
        self.AcctDate = None
        self.PricingCurrency = None
        self.SourceCurrency = None
        self.SourceAmount = None
        self.TargetCurrency = None
        self.TargetAmount = None
        self.FxRate = None
        self.Status = None
        self.FailReason = None
        self.RefundAmount = None
        self.RefundCurrency = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.AcctDate = params.get("AcctDate")
        self.PricingCurrency = params.get("PricingCurrency")
        self.SourceCurrency = params.get("SourceCurrency")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TargetAmount = params.get("TargetAmount")
        self.FxRate = params.get("FxRate")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.RefundAmount = params.get("RefundAmount")
        self.RefundCurrency = params.get("RefundCurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOutwardOrderRequest(AbstractModel):
    """QueryOutwardOrder请求参数结构体

    """

    def __init__(self):
        """
        :param TransactionId: 对接方汇出指令编号\n        :type TransactionId: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.TransactionId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOutwardOrderResponse(AbstractModel):
    """QueryOutwardOrder返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询汇出结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryOutwardOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOutwardOrderResult(AbstractModel):
    """查询汇出结果

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Data: 查询汇出数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderData`\n        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryOutwardOrderData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPayerInfoRequest(AbstractModel):
    """QueryPayerInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.PayerId = None
        self.Profile = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPayerInfoResponse(AbstractModel):
    """QueryPayerInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 付款人查询结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryPayerinfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryPayerinfoData(AbstractModel):
    """付款人查询数据

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param Status: 审核状态\n        :type Status: str\n        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailReason: str\n        :param PayerType: 付款人类型\n        :type PayerType: str\n        :param PayerName: 付款人姓名\n        :type PayerName: str\n        :param PayerIdType: 付款人证件类型\n        :type PayerIdType: str\n        :param PayerIdNo: 付款人证件号\n        :type PayerIdNo: str\n        :param PayerContactNumber: 付款人联系电话
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayerContactNumber: str\n        :param PayerEmailAddress: 付款人联系邮箱
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayerEmailAddress: str\n        :param PayerCountryCode: 付款人常驻国家或地区编码\n        :type PayerCountryCode: str\n        :param PayerContactName: 付款人联系名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayerContactName: str\n        """
        self.MerchantId = None
        self.PayerId = None
        self.Status = None
        self.FailReason = None
        self.PayerType = None
        self.PayerName = None
        self.PayerIdType = None
        self.PayerIdNo = None
        self.PayerContactNumber = None
        self.PayerEmailAddress = None
        self.PayerCountryCode = None
        self.PayerContactName = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.PayerType = params.get("PayerType")
        self.PayerName = params.get("PayerName")
        self.PayerIdType = params.get("PayerIdType")
        self.PayerIdNo = params.get("PayerIdNo")
        self.PayerContactNumber = params.get("PayerContactNumber")
        self.PayerEmailAddress = params.get("PayerEmailAddress")
        self.PayerCountryCode = params.get("PayerCountryCode")
        self.PayerContactName = params.get("PayerContactName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPayerinfoResult(AbstractModel):
    """付款人查询结果

    """

    def __init__(self):
        """
        :param Code: 错误码\n        :type Code: str\n        :param Data: 付款人查询数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoData`\n        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryPayerinfoData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryReconciliationDocumentRequest(AbstractModel):
    """QueryReconciliationDocument请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号\n        :type MrchCode: str\n        :param FileType: STRING(10)，文件类型（充值文件-CZ; 提现文件-TX; 交易文件-JY; 余额文件-YE; 合约文件-HY）\n        :type FileType: str\n        :param FileDate: STRING(8)，文件日期（格式：20190101）\n        :type FileDate: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FileType = None
        self.FileDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FileType = params.get("FileType")
        self.FileDate = params.get("FileDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryReconciliationDocumentResponse(AbstractModel):
    """QueryReconciliationDocument返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultNum: str\n        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranItemArray: list of FileItem\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = FileItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryRefundRequest(AbstractModel):
    """QueryRefund请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合。\n        :type UserId: str\n        :param RefundId: 退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合。\n        :type RefundId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRefundResponse(AbstractModel):
    """QueryRefund返回参数结构体

    """

    def __init__(self):
        """
        :param State: 退款状态码，退款提交成功后返回  1：退款中；  2：退款成功；  3：退款失败。\n        :type State: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class QuerySinglePayItem(AbstractModel):
    """银企直连-查询单笔支付状态条目

    """

    def __init__(self):
        """
        :param PayStatus: 付款状态（S：支付成功；P：支付处理中；F：支付失败）
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayStatus: str\n        :param PlatformMsg: 平台信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlatformMsg: str\n        :param BankRetCode: 银行原始返回码
注意：此字段可能返回 null，表示取不到有效值。\n        :type BankRetCode: str\n        :param BankRetMsg: 银行原始返回
注意：此字段可能返回 null，表示取不到有效值。\n        :type BankRetMsg: str\n        """
        self.PayStatus = None
        self.PlatformMsg = None
        self.BankRetCode = None
        self.BankRetMsg = None


    def _deserialize(self, params):
        self.PayStatus = params.get("PayStatus")
        self.PlatformMsg = params.get("PlatformMsg")
        self.BankRetCode = params.get("BankRetCode")
        self.BankRetMsg = params.get("BankRetMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePayRequest(AbstractModel):
    """QuerySinglePay请求参数结构体

    """

    def __init__(self):
        """
        :param SerialNumber: 业务流水号\n        :type SerialNumber: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.SerialNumber = None
        self.Profile = None


    def _deserialize(self, params):
        self.SerialNumber = params.get("SerialNumber")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePayResponse(AbstractModel):
    """QuerySinglePay返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 返回结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QuerySinglePayResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QuerySinglePayResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QuerySinglePayResult(AbstractModel):
    """银企直连-查询单笔支付状态结果

    """

    def __init__(self):
        """
        :param HandleStatus: 受理状态（S：处理成功；F：处理失败）\n        :type HandleStatus: str\n        :param HandleMsg: 受理状态描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type HandleMsg: str\n        :param SerialNo: 业务流水号\n        :type SerialNo: str\n        :param Items: 支付明细
注意：此字段可能返回 null，表示取不到有效值。\n        :type Items: list of QuerySinglePayItem\n        """
        self.HandleStatus = None
        self.HandleMsg = None
        self.SerialNo = None
        self.Items = None


    def _deserialize(self, params):
        self.HandleStatus = params.get("HandleStatus")
        self.HandleMsg = params.get("HandleMsg")
        self.SerialNo = params.get("SerialNo")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = QuerySinglePayItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySingleTransactionStatusRequest(AbstractModel):
    """QuerySingleTransactionStatus请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param FunctionFlag: STRING(2)，功能标志（2: 会员间交易; 3: 提现; 4: 充值）\n        :type FunctionFlag: str\n        :param TranNetSeqNo: STRING(52)，交易网流水号（提现，充值或会员交易请求时的CnsmrSeqNo值）\n        :type TranNetSeqNo: str\n        :param SubAcctNo: STRING(50)，见证子帐户的帐号（未启用）\n        :type SubAcctNo: str\n        :param TranDate: STRING(8)，交易日期（未启用）\n        :type TranDate: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetSeqNo = None
        self.SubAcctNo = None
        self.TranDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetSeqNo = params.get("TranNetSeqNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySingleTransactionStatusResponse(AbstractModel):
    """QuerySingleTransactionStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param BookingFlag: STRING(2)，记账标志（记账标志。1: 登记挂账; 2: 支付; 3: 提现; 4: 清分; 5: 下单预支付; 6: 确认并付款; 7: 退款; 8: 支付到平台; N: 其他）
注意：此字段可能返回 null，表示取不到有效值。\n        :type BookingFlag: str\n        :param TranStatus: STRING(32)，交易状态（0: 成功; 1: 失败; 2: 待确认; 5: 待处理; 6: 处理中。0和1是终态，2、5、6是中间态，其中2是特指提现后待确认提现是否成功，5是银行收到交易等待处理，6是交易正在处理）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranStatus: str\n        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranAmt: str\n        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranDate: str\n        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranTime: str\n        :param InSubAcctNo: STRING(50)，转入子账户账号
注意：此字段可能返回 null，表示取不到有效值。\n        :type InSubAcctNo: str\n        :param OutSubAcctNo: STRING(50)，转出子账户账号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutSubAcctNo: str\n        :param FailMsg: STRING(300)，失败信息（当提现失败时，返回交易失败原因）
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailMsg: str\n        :param OldTranFrontSeqNo: STRING(50)，原前置流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OldTranFrontSeqNo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.FailMsg = None
        self.OldTranFrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.FailMsg = params.get("FailMsg")
        self.OldTranFrontSeqNo = params.get("OldTranFrontSeqNo")
        self.RequestId = params.get("RequestId")


class QuerySmallAmountTransferRequest(AbstractModel):
    """QuerySmallAmountTransfer请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param OldTranSeqNo: STRING(52)，原交易流水号（小额鉴权交易请求时的CnsmrSeqNo值）\n        :type OldTranSeqNo: str\n        :param TranDate: STRING(8)，交易日期（格式：20190101）\n        :type TranDate: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.OldTranSeqNo = None
        self.TranDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.OldTranSeqNo = params.get("OldTranSeqNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySmallAmountTransferResponse(AbstractModel):
    """QuerySmallAmountTransfer返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ReturnStatus: STRING(10)，返回状态（0: 成功; 1: 失败; 2: 待确认）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReturnStatus: str\n        :param ReturnMsg: STRING(512)，返回信息（失败返回具体信息）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReturnMsg: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReturnStatus = None
        self.ReturnMsg = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReturnStatus = params.get("ReturnStatus")
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryTradeData(AbstractModel):
    """贸易材料明细查询数据

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param TradeFileId: 贸易材料流水号\n        :type TradeFileId: str\n        :param TradeOrderId: 贸易材料订单号\n        :type TradeOrderId: str\n        :param Status: 审核状态\n        :type Status: str\n        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailReason: str\n        :param PayerId: 付款人ID\n        :type PayerId: str\n        :param PayeeName: 收款人姓名\n        :type PayeeName: str\n        :param PayeeCountryCode: 收款人常驻国家或地区编码\n        :type PayeeCountryCode: str\n        :param TradeType: 交易类型\n        :type TradeType: str\n        :param TradeTime: 交易日期\n        :type TradeTime: str\n        :param TradeCurrency: 交易币种\n        :type TradeCurrency: str\n        :param TradeAmount: 交易金额\n        :type TradeAmount: str\n        :param TradeName: 交易名称\n        :type TradeName: str\n        :param TradeCount: 交易数量\n        :type TradeCount: int\n        :param GoodsCarrier: 货贸承运人
注意：此字段可能返回 null，表示取不到有效值。\n        :type GoodsCarrier: str\n        :param ServiceDetail: 服贸交易细节
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceDetail: str\n        :param ServiceTime: 服贸服务时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceTime: str\n        """
        self.MerchantId = None
        self.TradeFileId = None
        self.TradeOrderId = None
        self.Status = None
        self.FailReason = None
        self.PayerId = None
        self.PayeeName = None
        self.PayeeCountryCode = None
        self.TradeType = None
        self.TradeTime = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.TradeName = None
        self.TradeCount = None
        self.GoodsCarrier = None
        self.ServiceDetail = None
        self.ServiceTime = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TradeFileId = params.get("TradeFileId")
        self.TradeOrderId = params.get("TradeOrderId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.PayerId = params.get("PayerId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.TradeType = params.get("TradeType")
        self.TradeTime = params.get("TradeTime")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.TradeName = params.get("TradeName")
        self.TradeCount = params.get("TradeCount")
        self.GoodsCarrier = params.get("GoodsCarrier")
        self.ServiceDetail = params.get("ServiceDetail")
        self.ServiceTime = params.get("ServiceTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTradeRequest(AbstractModel):
    """QueryTrade请求参数结构体

    """

    def __init__(self):
        """
        :param TradeFileId: 贸易材料流水号\n        :type TradeFileId: str\n        :param Profile: 接入环境。沙箱环境填sandbox\n        :type Profile: str\n        """
        self.TradeFileId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TradeFileId = params.get("TradeFileId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTradeResponse(AbstractModel):
    """QueryTrade返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 贸易材料明细查询结果\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryTradeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryTradeResult(AbstractModel):
    """贸易材料明细查询结果

    """

    def __init__(self):
        """
        :param Data: 贸易材料明细查询数据\n        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeData`\n        :param Code: 错误码\n        :type Code: str\n        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryTradeData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferBatchRequest(AbstractModel):
    """QueryTransferBatch请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号。
示例值：129284394\n        :type MerchantId: str\n        :param NeedQueryDetail: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480101\n        :type NeedQueryDetail: bool\n        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013\n        :type MerchantBatchNo: str\n        :param BatchId: 是否查询账单明细。
true-是；
false-否，默认否。
商户可选择是否查询指定状态的转账明细单，当转账批次单状态为“FINISHED”（已完成）时，才会返回满足条件的转账明细单。
示例值：true\n        :type BatchId: str\n        :param Profile: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type Profile: str\n        :param Offset: 请求资源起始位置。
从0开始，默认值为0。
示例值：20\n        :type Offset: int\n        :param Limit: 最大资源条数。
该次请求可返回的最大资源（转账明细单）条数，最小20条，最大100条，不传则默认20条。不足20条按实际条数返回
示例值：20\n        :type Limit: int\n        :param DetailStatus: 明细状态。
ALL：全部，需要同时查询转账成功喝失败的明细单；
SUCCESS：转账成功，只查询成功的明细单；
FAIL：转账失败，只查询转账失败的明细单。
示例值：FAIL\n        :type DetailStatus: str\n        """
        self.MerchantId = None
        self.NeedQueryDetail = None
        self.MerchantBatchNo = None
        self.BatchId = None
        self.Profile = None
        self.Offset = None
        self.Limit = None
        self.DetailStatus = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.NeedQueryDetail = params.get("NeedQueryDetail")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.Profile = params.get("Profile")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DetailStatus = params.get("DetailStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferBatchResponse(AbstractModel):
    """QueryTransferBatch返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号。
示例值：19300009329\n        :type MerchantId: str\n        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013\n        :type MerchantBatchNo: str\n        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
示例值：1030000071100999991182020050700019480001\n        :type BatchId: str\n        :param MerchantAppId: 直连商户appId。
商户号绑定的appid。
示例值：wxf636efh567hg4356\n        :type MerchantAppId: str\n        :param BatchStatus: 批次状态。
ACCEPTED:已受理，批次已受理成功，若发起批量转账的30分钟后，转账批次单仍处于该状态，可能原因是商户账户余额不足等。商户可查询账户资金流水，若该笔转账批次单的扣款已经发生，则表示批次已经进入转账中，请再次查单确认；
PROCESSING:转账中，已开始处理批次内的转账明细单；
FINISHED:已完成，批次内的所有转账明细单都已处理完成；
CLOSED:已关闭，可查询具体的批次关闭原因确认；
示例值：ACCEPTED\n        :type BatchStatus: str\n        :param CloseReason: 批次关闭原因。
如果批次单状态为“CLOSED”（已关闭），则有关闭原因；
MERCHANT_REVOCATION：商户主动撤销；
OVERDUE_CLOSE：系统超时关闭。
示例值：OVERDUE_CLOSE
注意：此字段可能返回 null，表示取不到有效值。\n        :type CloseReason: str\n        :param TotalAmount: 转账总金额。
转账金额，单位为分。
示例值：4000000\n        :type TotalAmount: int\n        :param TotalNum: 转账总笔数。
一个转账批次最多允许发起三千笔转账。
示例值：200\n        :type TotalNum: int\n        :param CreateTime: 批次受理成功时返回，遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 批次最近一次更新时间，遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param SuccessAmount: 转账成功金额。
转账成功的金额，单位为分，可能随时变化。
示例值：4000000
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessAmount: int\n        :param SuccessNum: 转账成功的笔数。
可能随时变化。
示例值：200
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessNum: int\n        :param FailAmount: 转账失败金额。
转账失败的金额，单位为分，可能随时变化。
示例值：4000000
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailAmount: int\n        :param FailNum: 转账失败笔数。
可能随时变化。
示例值：200
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailNum: int\n        :param TransferDetails: 转账明细列表。
返回明细详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferDetails: list of TransferDetailResponse\n        :param BatchType: 批次类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchType: str\n        :param BatchName: 批次名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchName: str\n        :param BatchRemark: 批次标注。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchRemark: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantId = None
        self.MerchantBatchNo = None
        self.BatchId = None
        self.MerchantAppId = None
        self.BatchStatus = None
        self.CloseReason = None
        self.TotalAmount = None
        self.TotalNum = None
        self.CreateTime = None
        self.UpdateTime = None
        self.SuccessAmount = None
        self.SuccessNum = None
        self.FailAmount = None
        self.FailNum = None
        self.TransferDetails = None
        self.BatchType = None
        self.BatchName = None
        self.BatchRemark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.MerchantAppId = params.get("MerchantAppId")
        self.BatchStatus = params.get("BatchStatus")
        self.CloseReason = params.get("CloseReason")
        self.TotalAmount = params.get("TotalAmount")
        self.TotalNum = params.get("TotalNum")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.SuccessAmount = params.get("SuccessAmount")
        self.SuccessNum = params.get("SuccessNum")
        self.FailAmount = params.get("FailAmount")
        self.FailNum = params.get("FailNum")
        if params.get("TransferDetails") is not None:
            self.TransferDetails = []
            for item in params.get("TransferDetails"):
                obj = TransferDetailResponse()
                obj._deserialize(item)
                self.TransferDetails.append(obj)
        self.BatchType = params.get("BatchType")
        self.BatchName = params.get("BatchName")
        self.BatchRemark = params.get("BatchRemark")
        self.RequestId = params.get("RequestId")


class QueryTransferDetailRequest(AbstractModel):
    """QueryTransferDetail请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号。
示例值：129284394\n        :type MerchantId: str\n        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013\n        :type MerchantBatchNo: str\n        :param MerchantDetailNo: 商家明细单号。
商户系统内部的商家明细单号
示例值：plfk2020042013\n        :type MerchantDetailNo: str\n        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
商家单号（包含批次号和明细单号）和微信单号（包含批次号和明细单号）二者必填其一。
示例值：1030000071100999991182020050700019480001\n        :type BatchId: str\n        :param DetailId: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480001\n        :type DetailId: str\n        :param Profile: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type Profile: str\n        """
        self.MerchantId = None
        self.MerchantBatchNo = None
        self.MerchantDetailNo = None
        self.BatchId = None
        self.DetailId = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.BatchId = params.get("BatchId")
        self.DetailId = params.get("DetailId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferDetailResponse(AbstractModel):
    """QueryTransferDetail返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号。
示例值：19300009329\n        :type MerchantId: str\n        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013\n        :type MerchantBatchNo: str\n        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
示例值：1030000071100999991182020050700019480001\n        :type BatchId: str\n        :param MerchantDetailNo: 商家明细单号。
商户系统内部的商家明细单号
示例值：plfk2020042013\n        :type MerchantDetailNo: str\n        :param DetailId: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480001\n        :type DetailId: str\n        :param DetailStatus: 明细状态。
PROCESSING：转账中，正在处理，结果未明；
SUCCESS：转账成功；
FAIL：转账失败，需要确认失败原因以后，再决定是否重新发起地该笔明细的转账。
示例值：SUCCESS\n        :type DetailStatus: str\n        :param TransferAmount: 转账金额。
单位为分。
示例值：200\n        :type TransferAmount: int\n        :param FailReason: 失败原因。
如果转账失败则有失败原因
ACCOUNT_FROZEN：账户冻结
REAL_NAME_CHECK_FAIL：用户未实名
NAME_NOT_CORRECT：用户姓名校验失败
OPENID_INVALID：Openid校验失败
TRANSFER_QUOTA_EXCEED：超过用户单笔收款额度
DAY_RECEIVED_QUOTA_EXCEED：超过用户单日收款额度
MONTH_RECEIVED_QUOTA_EXCEED：超过用户单月收款额度
DAY_RECEIVED_COUNT_EXCEED：超过用户单日收款次数
PRODUCT_AUTH_CHECK_FAIL：产品权限校验失败
OVERDUE_CLOSE：转账关闭
ID_CARD_NOT_CORRECT：用户身份证校验失败
ACCOUNT_NOT_EXIST：用户账户不存在
TRANSFER_RISK：转账存在风险
示例值：ACCOUNT_FROZEN
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailReason: str\n        :param InitiateTime: 转账发起时间。
遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。\n        :type InitiateTime: str\n        :param UpdateTime: 转账更新时间。
遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param UserName: 用户名。
示例值：张三
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserName: str\n        :param TransferRemark: 转账备注。
单条转账备注（微信用户会收到该备注）。UTF8编码，最多32字符。
示例值：2020年4月报销
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferRemark: str\n        :param MerchantAppId: 商家绑定公众号APPID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MerchantAppId: str\n        :param OpenId: 用户openId。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OpenId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantId = None
        self.MerchantBatchNo = None
        self.BatchId = None
        self.MerchantDetailNo = None
        self.DetailId = None
        self.DetailStatus = None
        self.TransferAmount = None
        self.FailReason = None
        self.InitiateTime = None
        self.UpdateTime = None
        self.UserName = None
        self.TransferRemark = None
        self.MerchantAppId = None
        self.OpenId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.DetailId = params.get("DetailId")
        self.DetailStatus = params.get("DetailStatus")
        self.TransferAmount = params.get("TransferAmount")
        self.FailReason = params.get("FailReason")
        self.InitiateTime = params.get("InitiateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.UserName = params.get("UserName")
        self.TransferRemark = params.get("TransferRemark")
        self.MerchantAppId = params.get("MerchantAppId")
        self.OpenId = params.get("OpenId")
        self.RequestId = params.get("RequestId")


class QueryTransferResultData(AbstractModel):
    """智能代发-单笔代发转账查询接口返回内容

    """

    def __init__(self):
        """
        :param TradeSerialNo: 平台交易流水号\n        :type TradeSerialNo: str\n        :param OrderId: 订单号\n        :type OrderId: str\n        :param TradeStatus: 交易状态。
0 处理中  
1 提交成功 
2 交易成功 
3 交易失败 
4 未知渠道异常 
99 未知系统异常\n        :type TradeStatus: int\n        :param Remark: 业务备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        """
        self.TradeSerialNo = None
        self.OrderId = None
        self.TradeStatus = None
        self.Remark = None


    def _deserialize(self, params):
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.OrderId = params.get("OrderId")
        self.TradeStatus = params.get("TradeStatus")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferResultRequest(AbstractModel):
    """QueryTransferResult请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param MerchantAppId: 申请商户号的appid或者商户号绑定的appid\n        :type MerchantAppId: str\n        :param TransferType: 1、 微信企业付款 
2、 支付宝转账 
3、 平安银企直联代发转账\n        :type TransferType: int\n        :param TradeSerialNo: 交易流水流水号（与 OrderId 不能同时为空）\n        :type TradeSerialNo: str\n        :param OrderId: 订单号（与 TradeSerialNo 不能同时为空）\n        :type OrderId: str\n        :param Profile: 接入环境。沙箱环境填sandbox。\n        :type Profile: str\n        """
        self.MerchantId = None
        self.MerchantAppId = None
        self.TransferType = None
        self.TradeSerialNo = None
        self.OrderId = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantAppId = params.get("MerchantAppId")
        self.TransferType = params.get("TransferType")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.OrderId = params.get("OrderId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferResultResponse(AbstractModel):
    """QueryTransferResult返回参数结构体

    """

    def __init__(self):
        """
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功\n        :type ErrCode: str\n        :param ErrMessage: 响应消息\n        :type ErrMessage: str\n        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferResultData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryTransferResultData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class RechargeByThirdPayRequest(AbstractModel):
    """RechargeByThirdPay请求参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型 此接口固定填：MemberRechargeThirdPayReq\n        :type RequestType: str\n        :param MerchantCode: 商户号\n        :type MerchantCode: str\n        :param PayChannel: 支付渠道\n        :type PayChannel: str\n        :param PayChannelSubId: 子渠道\n        :type PayChannelSubId: int\n        :param OrderId: 交易订单号\n        :type OrderId: str\n        :param BankAccountNumber: 父账户账号，资金汇总账号\n        :type BankAccountNumber: str\n        :param PlatformShortNumber: 平台短号(银行分配)\n        :type PlatformShortNumber: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param TransSequenceNumber: 交易流水号\n        :type TransSequenceNumber: str\n        :param BankSubAccountNumber: 子账户账号\n        :type BankSubAccountNumber: str\n        :param TransFee: 交易手续费，以元为单位\n        :type TransFee: str\n        :param ThirdPayChannel: 第三方支付渠道类型 0001-微信 0002-支付宝 0003-京东支付\n        :type ThirdPayChannel: str\n        :param ThirdPayChannelMerchantCode: 第三方渠道商户号\n        :type ThirdPayChannelMerchantCode: str\n        :param ThirdPayChannelOrderId: 第三方渠道订单号或流水号\n        :type ThirdPayChannelOrderId: str\n        :param CurrencyAmount: 交易金额\n        :type CurrencyAmount: str\n        :param CurrencyUnit: 单位，1：元，2：角，3：分\n        :type CurrencyUnit: str\n        :param CurrencyType: 币种\n        :type CurrencyType: str\n        :param TransNetMemberCode: 交易网会员代码\n        :type TransNetMemberCode: str\n        :param MidasEnvironment: midas环境参数\n        :type MidasEnvironment: str\n        :param ReservedMessage: 保留域\n        :type ReservedMessage: str\n        :param Remark: 备注\n        :type Remark: str\n        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.PlatformShortNumber = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.BankSubAccountNumber = None
        self.TransFee = None
        self.ThirdPayChannel = None
        self.ThirdPayChannelMerchantCode = None
        self.ThirdPayChannelOrderId = None
        self.CurrencyAmount = None
        self.CurrencyUnit = None
        self.CurrencyType = None
        self.TransNetMemberCode = None
        self.MidasEnvironment = None
        self.ReservedMessage = None
        self.Remark = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.BankSubAccountNumber = params.get("BankSubAccountNumber")
        self.TransFee = params.get("TransFee")
        self.ThirdPayChannel = params.get("ThirdPayChannel")
        self.ThirdPayChannelMerchantCode = params.get("ThirdPayChannelMerchantCode")
        self.ThirdPayChannelOrderId = params.get("ThirdPayChannelOrderId")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyType = params.get("CurrencyType")
        self.TransNetMemberCode = params.get("TransNetMemberCode")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeByThirdPayResponse(AbstractModel):
    """RechargeByThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param ReservedMessage: 保留字段
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMessage: str\n        :param FrontSequenceNumber: 银行流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSequenceNumber: str\n        :param RequestType: 请求类型\n        :type RequestType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReservedMessage = None
        self.FrontSequenceNumber = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMessage = params.get("ReservedMessage")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class RechargeMemberThirdPayRequest(AbstractModel):
    """RechargeMemberThirdPay请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会代码\n        :type TranNetMemberCode: str\n        :param MemberFillAmt: STRING(20)，会员充值金额\n        :type MemberFillAmt: str\n        :param Commission: STRING(20)，手续费金额\n        :type Commission: str\n        :param Ccy: STRING(3)，币种。如RMB\n        :type Ccy: str\n        :param PayChannelType: STRING(20)，支付渠道类型。
0001-微信
0002-支付宝
0003-京东支付\n        :type PayChannelType: str\n        :param PayChannelAssignMerNo: STRING(50)，支付渠道所分配的商户号\n        :type PayChannelAssignMerNo: str\n        :param PayChannelTranSeqNo: STRING(52)，支付渠道交易流水号\n        :type PayChannelTranSeqNo: str\n        :param EjzbOrderNo: STRING(52)，电商见证宝订单号\n        :type EjzbOrderNo: str\n        :param MrchCode: String(22)，商户号\n        :type MrchCode: str\n        :param EjzbOrderContent: STRING(500)，电商见证宝订单内容\n        :type EjzbOrderContent: str\n        :param Remark: STRING(300)，备注\n        :type Remark: str\n        :param ReservedMsgOne: STRING(300)，保留域1\n        :type ReservedMsgOne: str\n        :param ReservedMsgTwo: STRING(300)，保留域2\n        :type ReservedMsgTwo: str\n        :param ReservedMsgThree: STRING(300)，保留域3\n        :type ReservedMsgThree: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.TranNetMemberCode = None
        self.MemberFillAmt = None
        self.Commission = None
        self.Ccy = None
        self.PayChannelType = None
        self.PayChannelAssignMerNo = None
        self.PayChannelTranSeqNo = None
        self.EjzbOrderNo = None
        self.MrchCode = None
        self.EjzbOrderContent = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberFillAmt = params.get("MemberFillAmt")
        self.Commission = params.get("Commission")
        self.Ccy = params.get("Ccy")
        self.PayChannelType = params.get("PayChannelType")
        self.PayChannelAssignMerNo = params.get("PayChannelAssignMerNo")
        self.PayChannelTranSeqNo = params.get("PayChannelTranSeqNo")
        self.EjzbOrderNo = params.get("EjzbOrderNo")
        self.MrchCode = params.get("MrchCode")
        self.EjzbOrderContent = params.get("EjzbOrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeMemberThirdPayResponse(AbstractModel):
    """RechargeMemberThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param MemberSubAcctPreAvailBal: STRING(20)，会员子账户交易前可用余额
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemberSubAcctPreAvailBal: str\n        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsgOne: str\n        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsgTwo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.MemberSubAcctPreAvailBal = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.MemberSubAcctPreAvailBal = params.get("MemberSubAcctPreAvailBal")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class RefundMemberTransactionRequest(AbstractModel):
    """RefundMemberTransaction请求参数结构体

    """

    def __init__(self):
        """
        :param OutSubAccountName: 转出见证子账户的户名\n        :type OutSubAccountName: str\n        :param InSubAccountName: 转入见证子账户的户名\n        :type InSubAccountName: str\n        :param PayChannelSubId: 子渠道\n        :type PayChannelSubId: int\n        :param OutSubAccountNumber: 转出见证子账户账号\n        :type OutSubAccountNumber: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param InSubAccountNumber: 转入见证子账户账号\n        :type InSubAccountNumber: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param BankAccountNumber: 父账户账号，资金汇总账号\n        :type BankAccountNumber: str\n        :param OldTransSequenceNumber: 原老订单流水号\n        :type OldTransSequenceNumber: str\n        :param MerchantCode: 银行注册商户号\n        :type MerchantCode: str\n        :param RequestType: 请求类型，固定为MemberTransactionRefundReq\n        :type RequestType: str\n        :param CurrencyAmount: 交易金额\n        :type CurrencyAmount: str\n        :param TransSequenceNumber: 交易流水号\n        :type TransSequenceNumber: str\n        :param PayChannel: 渠道\n        :type PayChannel: str\n        :param OldOrderId: 原订单号\n        :type OldOrderId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param OrderId: 订单号\n        :type OrderId: str\n        :param MidasEnvironment: Midas环境标识 release 现网环境 sandbox 沙箱环境
development 开发环境\n        :type MidasEnvironment: str\n        :param OutTransNetMemberCode: 转出子账户交易网会员代码\n        :type OutTransNetMemberCode: str\n        :param InTransNetMemberCode: 转入子账户交易网会员代码\n        :type InTransNetMemberCode: str\n        :param ReservedMessage: 保留域\n        :type ReservedMessage: str\n        :param PlatformShortNumber: 平台短号(银行分配)\n        :type PlatformShortNumber: str\n        :param TransType: 0-登记挂账，1-撤销挂账\n        :type TransType: str\n        :param TransFee: 交易手续费\n        :type TransFee: str\n        """
        self.OutSubAccountName = None
        self.InSubAccountName = None
        self.PayChannelSubId = None
        self.OutSubAccountNumber = None
        self.MidasSignature = None
        self.InSubAccountNumber = None
        self.MidasSecretId = None
        self.BankAccountNumber = None
        self.OldTransSequenceNumber = None
        self.MerchantCode = None
        self.RequestType = None
        self.CurrencyAmount = None
        self.TransSequenceNumber = None
        self.PayChannel = None
        self.OldOrderId = None
        self.MidasAppId = None
        self.OrderId = None
        self.MidasEnvironment = None
        self.OutTransNetMemberCode = None
        self.InTransNetMemberCode = None
        self.ReservedMessage = None
        self.PlatformShortNumber = None
        self.TransType = None
        self.TransFee = None


    def _deserialize(self, params):
        self.OutSubAccountName = params.get("OutSubAccountName")
        self.InSubAccountName = params.get("InSubAccountName")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OutSubAccountNumber = params.get("OutSubAccountNumber")
        self.MidasSignature = params.get("MidasSignature")
        self.InSubAccountNumber = params.get("InSubAccountNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.OldTransSequenceNumber = params.get("OldTransSequenceNumber")
        self.MerchantCode = params.get("MerchantCode")
        self.RequestType = params.get("RequestType")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.PayChannel = params.get("PayChannel")
        self.OldOrderId = params.get("OldOrderId")
        self.MidasAppId = params.get("MidasAppId")
        self.OrderId = params.get("OrderId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.OutTransNetMemberCode = params.get("OutTransNetMemberCode")
        self.InTransNetMemberCode = params.get("InTransNetMemberCode")
        self.ReservedMessage = params.get("ReservedMessage")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.TransType = params.get("TransType")
        self.TransFee = params.get("TransFee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundMemberTransactionResponse(AbstractModel):
    """RefundMemberTransaction返回参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型\n        :type RequestType: str\n        :param FrontSequenceNumber: 银行流水号\n        :type FrontSequenceNumber: str\n        :param ReservedMessage: 保留域\n        :type ReservedMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestType = None
        self.FrontSequenceNumber = None
        self.ReservedMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.ReservedMessage = params.get("ReservedMessage")
        self.RequestId = params.get("RequestId")


class RefundOrderRequest(AbstractModel):
    """RefundOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 进件成功后返给商户方的AppId\n        :type MerchantAppId: str\n        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。\n        :type OrderNo: str\n        """
        self.MerchantAppId = None
        self.OrderNo = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundOrderResponse(AbstractModel):
    """RefundOrder返回参数结构体

    """

    def __init__(self):
        """
        :param MerchantAppId: 进件成功后返给商户方的AppId\n        :type MerchantAppId: str\n        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。\n        :type OrderNo: str\n        :param Status: 订单退款状态。0-退款失败
1-退款成功 
2-可疑状态\n        :type Status: str\n        :param Description: 订单退款状态描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MerchantAppId = None
        self.OrderNo = None
        self.Status = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class RefundOutSubOrderRefundList(AbstractModel):
    """退款子订单列表

    """

    def __init__(self):
        """
        :param PlatformRefundAmt: 平台应退金额\n        :type PlatformRefundAmt: int\n        :param RefundAmt: 子订单退款金额\n        :type RefundAmt: int\n        :param SubMchRefundAmt: 商家应退金额\n        :type SubMchRefundAmt: int\n        :param SubOutTradeNo: 子订单号\n        :type SubOutTradeNo: str\n        :param SubRefundId: 子退款单号，调用方需要保证 全局唯一性\n        :type SubRefundId: str\n        """
        self.PlatformRefundAmt = None
        self.RefundAmt = None
        self.SubMchRefundAmt = None
        self.SubOutTradeNo = None
        self.SubRefundId = None


    def _deserialize(self, params):
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        self.RefundAmt = params.get("RefundAmt")
        self.SubMchRefundAmt = params.get("SubMchRefundAmt")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubRefundId = params.get("SubRefundId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundRequest(AbstractModel):
    """Refund请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合\n        :type UserId: str\n        :param RefundId: 退款订单号，仅支持数字、 字母、下划线（_）、横杠字 符（-）、点（.）的组合\n        :type RefundId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param TotalRefundAmt: 退款金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额\n        :type TotalRefundAmt: int\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param OutTradeNo: 商品订单，仅支持数字、字 母、下划线（_）、横杠字符 （-）、点（.）的组合。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo\n        :type OutTradeNo: str\n        :param MchRefundAmt: 结算应收金额，单位：分\n        :type MchRefundAmt: int\n        :param TransactionId: 调用下单接口获取的聚鑫交 易订单。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo\n        :type TransactionId: str\n        :param PlatformRefundAmt: 平台应收金额，单位：分\n        :type PlatformRefundAmt: int\n        :param SubOrderRefundList: 支持多个子订单批量退款单 个子订单退款支持传 SubOutTradeNo ，也支持传 SubOutTradeNoList ，都传的时候以 SubOutTradeNoList 为准。  如果传了子单退款细节，外 部不需要再传退款金额，平 台应退，商户应退金额，我 们可以直接根据子单退款算出来总和。\n        :type SubOrderRefundList: list of RefundOutSubOrderRefundList\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.TotalRefundAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.MchRefundAmt = None
        self.TransactionId = None
        self.PlatformRefundAmt = None
        self.SubOrderRefundList = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.TotalRefundAmt = params.get("TotalRefundAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.MchRefundAmt = params.get("MchRefundAmt")
        self.TransactionId = params.get("TransactionId")
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        if params.get("SubOrderRefundList") is not None:
            self.SubOrderRefundList = []
            for item in params.get("SubOrderRefundList"):
                obj = RefundOutSubOrderRefundList()
                obj._deserialize(item)
                self.SubOrderRefundList.append(obj)
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundResponse(AbstractModel):
    """Refund返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterBehaviorRequest(AbstractModel):
    """RegisterBehavior请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param FunctionFlag: 功能标志
1：登记行为记录信息
2：查询补录信息\n        :type FunctionFlag: int\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param OperationClickTime: 操作点击时间
yyyyMMddHHmmss
功能标志FunctionFlag=1时必输\n        :type OperationClickTime: str\n        :param IpAddress: IP地址
功能标志FunctionFlag=1时必输\n        :type IpAddress: str\n        :param MacAddress: MAC地址
功能标志FunctionFlag=1时必输\n        :type MacAddress: str\n        :param SignChannel: 签约渠道
1:  App
2:  平台H5网页
3：公众号
4：小程序
功能标志FunctionFlag=1时必输\n        :type SignChannel: int\n        """
        self.MidasAppId = None
        self.SubAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.FunctionFlag = None
        self.MidasEnvironment = None
        self.OperationClickTime = None
        self.IpAddress = None
        self.MacAddress = None
        self.SignChannel = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.FunctionFlag = params.get("FunctionFlag")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.OperationClickTime = params.get("OperationClickTime")
        self.IpAddress = params.get("IpAddress")
        self.MacAddress = params.get("MacAddress")
        self.SignChannel = params.get("SignChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterBehaviorResponse(AbstractModel):
    """RegisterBehavior返回参数结构体

    """

    def __init__(self):
        """
        :param ReplenishSuccessFlag: 补录是否成功标志
功能标志为2时存在。
S：成功
F：失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReplenishSuccessFlag: str\n        :param RegisterInfo: 签约信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegisterInfo: :class:`tencentcloud.cpdp.v20190820.models.RegisterInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReplenishSuccessFlag = None
        self.RegisterInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplenishSuccessFlag = params.get("ReplenishSuccessFlag")
        if params.get("RegisterInfo") is not None:
            self.RegisterInfo = RegisterInfo()
            self.RegisterInfo._deserialize(params.get("RegisterInfo"))
        self.RequestId = params.get("RequestId")


class RegisterBillRequest(AbstractModel):
    """RegisterBill请求参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型此接口固定填：RegBillSupportWithdrawReq\n        :type RequestType: str\n        :param MerchantCode: 商户号\n        :type MerchantCode: str\n        :param PayChannel: 支付渠道\n        :type PayChannel: str\n        :param PayChannelSubId: 子渠道\n        :type PayChannelSubId: int\n        :param OrderId: 交易订单号\n        :type OrderId: str\n        :param BankAccountNo: 父账户账号，资金汇总账号\n        :type BankAccountNo: str\n        :param PlatformShortNo: 平台短号(银行分配)\n        :type PlatformShortNo: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param TransSeqNo: 交易流水号\n        :type TransSeqNo: str\n        :param TranFee: 暂未使用，默认传0.0\n        :type TranFee: str\n        :param OrderAmt: 挂账金额，以元为单位\n        :type OrderAmt: str\n        :param BankSubAccountNo: 子账户账号\n        :type BankSubAccountNo: str\n        :param TranNetMemberCode: 交易网会员代码\n        :type TranNetMemberCode: str\n        :param TranType: 0,登记挂账，1，撤销挂账\n        :type TranType: str\n        :param ReservedMessage: 保留域\n        :type ReservedMessage: str\n        :param Remark: 备注\n        :type Remark: str\n        :param MidasEnvironment: Midas环境参数\n        :type MidasEnvironment: str\n        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNo = None
        self.PlatformShortNo = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSeqNo = None
        self.TranFee = None
        self.OrderAmt = None
        self.BankSubAccountNo = None
        self.TranNetMemberCode = None
        self.TranType = None
        self.ReservedMessage = None
        self.Remark = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNo = params.get("BankAccountNo")
        self.PlatformShortNo = params.get("PlatformShortNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSeqNo = params.get("TransSeqNo")
        self.TranFee = params.get("TranFee")
        self.OrderAmt = params.get("OrderAmt")
        self.BankSubAccountNo = params.get("BankSubAccountNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.TranType = params.get("TranType")
        self.ReservedMessage = params.get("ReservedMessage")
        self.Remark = params.get("Remark")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterBillResponse(AbstractModel):
    """RegisterBill返回参数结构体

    """

    def __init__(self):
        """
        :param FrontSeqNo: 银行流水号\n        :type FrontSeqNo: str\n        :param ReservedMessage: 保留字段\n        :type ReservedMessage: str\n        :param RequestType: 请求类型\n        :type RequestType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FrontSeqNo = None
        self.ReservedMessage = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMessage = params.get("ReservedMessage")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class RegisterBillSupportWithdrawRequest(AbstractModel):
    """RegisterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会员代码\n        :type TranNetMemberCode: str\n        :param OrderNo: STRING(50)，订单号\n        :type OrderNo: str\n        :param SuspendAmt: STRING(20)，挂账金额（包含交易费用）\n        :type SuspendAmt: str\n        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）\n        :type TranFee: str\n        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param Remark: STRING(300)，备注\n        :type Remark: str\n        :param ReservedMsgOne: STRING(300)，保留域1\n        :type ReservedMsgOne: str\n        :param ReservedMsgTwo: STRING(300)，保留域2\n        :type ReservedMsgTwo: str\n        :param ReservedMsgThree: STRING(300)，保留域3\n        :type ReservedMsgThree: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.TranNetMemberCode = None
        self.OrderNo = None
        self.SuspendAmt = None
        self.TranFee = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OrderNo = params.get("OrderNo")
        self.SuspendAmt = params.get("SuspendAmt")
        self.TranFee = params.get("TranFee")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterBillSupportWithdrawResponse(AbstractModel):
    """RegisterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param CnsmrSeqNo: String(22)，交易流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type CnsmrSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.FrontSeqNo = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RegisterInfo(AbstractModel):
    """签约信息

    """

    def __init__(self):
        """
        :param LegalPersonIdCode: 法人证件号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type LegalPersonIdCode: str\n        :param LegalPersonIdType: 法人证件类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type LegalPersonIdType: str\n        :param LegalPersonName: 法人名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type LegalPersonName: str\n        :param OrganizationCode: 公司证件号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationCode: str\n        :param OrganizationName: 公司名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationName: str\n        :param OrganizationType: 公司证件类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationType: str\n        """
        self.LegalPersonIdCode = None
        self.LegalPersonIdType = None
        self.LegalPersonName = None
        self.OrganizationCode = None
        self.OrganizationName = None
        self.OrganizationType = None


    def _deserialize(self, params):
        self.LegalPersonIdCode = params.get("LegalPersonIdCode")
        self.LegalPersonIdType = params.get("LegalPersonIdType")
        self.LegalPersonName = params.get("LegalPersonName")
        self.OrganizationCode = params.get("OrganizationCode")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationType = params.get("OrganizationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseQueryContract(AbstractModel):
    """签约数据

    """

    def __init__(self):
        """
        :param ExternalReturnCode: 第三方渠道错误码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnCode: str\n        :param ExternalReturnMessage: 第三方渠道错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnMessage: str\n        :param ExternalReturnData: 第三方渠道返回的原始数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnData: str\n        :param ChannelMerchantId: 米大师内部商户号\n        :type ChannelMerchantId: str\n        :param ChannelSubMerchantId: 米大师内部子商户号
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChannelSubMerchantId: str\n        :param ChannelAppId: 米大师内部应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChannelAppId: str\n        :param ChannelSubAppId: 米大师内部子应用ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChannelSubAppId: str\n        :param ChannelName: 渠道名称\n        :type ChannelName: str\n        :param ReturnContractInfo: 返回的合约信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ReturnContractInfo`\n        :param NotifyUrl: 签约通知地址\n        :type NotifyUrl: str\n        """
        self.ExternalReturnCode = None
        self.ExternalReturnMessage = None
        self.ExternalReturnData = None
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelAppId = None
        self.ChannelSubAppId = None
        self.ChannelName = None
        self.ReturnContractInfo = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.ExternalReturnCode = params.get("ExternalReturnCode")
        self.ExternalReturnMessage = params.get("ExternalReturnMessage")
        self.ExternalReturnData = params.get("ExternalReturnData")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelAppId = params.get("ChannelAppId")
        self.ChannelSubAppId = params.get("ChannelSubAppId")
        self.ChannelName = params.get("ChannelName")
        if params.get("ReturnContractInfo") is not None:
            self.ReturnContractInfo = ReturnContractInfo()
            self.ReturnContractInfo._deserialize(params.get("ReturnContractInfo"))
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseTerminateContract(AbstractModel):
    """解约数据

    """

    def __init__(self):
        """
        :param ExternalReturnCode: 第三方渠道错误码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnCode: str\n        :param ExternalReturnMessage: 第三方渠道错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnMessage: str\n        :param ExternalReturnData: 第三方渠道返回的原始数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalReturnData: str\n        """
        self.ExternalReturnCode = None
        self.ExternalReturnMessage = None
        self.ExternalReturnData = None


    def _deserialize(self, params):
        self.ExternalReturnCode = params.get("ExternalReturnCode")
        self.ExternalReturnMessage = params.get("ExternalReturnMessage")
        self.ExternalReturnData = params.get("ExternalReturnData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReturnContractInfo(AbstractModel):
    """返回的合约信息

    """

    def __init__(self):
        """
        :param ContractInfo: 合约信息\n        :type ContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ContractInfo`\n        :param ChannelReturnContractInfo: 米大师内部生成的合约信息\n        :type ChannelReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ChannelReturnContractInfo`\n        :param ExternalReturnContractInfo: 第三方渠道合约信息\n        :type ExternalReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ExternalReturnContractInfo`\n        """
        self.ContractInfo = None
        self.ChannelReturnContractInfo = None
        self.ExternalReturnContractInfo = None


    def _deserialize(self, params):
        if params.get("ContractInfo") is not None:
            self.ContractInfo = ContractInfo()
            self.ContractInfo._deserialize(params.get("ContractInfo"))
        if params.get("ChannelReturnContractInfo") is not None:
            self.ChannelReturnContractInfo = ChannelReturnContractInfo()
            self.ChannelReturnContractInfo._deserialize(params.get("ChannelReturnContractInfo"))
        if params.get("ExternalReturnContractInfo") is not None:
            self.ExternalReturnContractInfo = ExternalReturnContractInfo()
            self.ExternalReturnContractInfo._deserialize(params.get("ExternalReturnContractInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevResigterBillSupportWithdrawRequest(AbstractModel):
    """RevResigterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码\n        :type TranNetMemberCode: str\n        :param OldOrderNo: STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）\n        :type OldOrderNo: str\n        :param CancelAmt: STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）\n        :type CancelAmt: str\n        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）\n        :type TranFee: str\n        :param Remark: STRING(300)，备注\n        :type Remark: str\n        :param ReservedMsgOne: STRING(300)，保留域1\n        :type ReservedMsgOne: str\n        :param ReservedMsgTwo: STRING(300)，保留域2\n        :type ReservedMsgTwo: str\n        :param ReservedMsgThree: STRING(300)，保留域3\n        :type ReservedMsgThree: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.OldOrderNo = None
        self.CancelAmt = None
        self.TranFee = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OldOrderNo = params.get("OldOrderNo")
        self.CancelAmt = params.get("CancelAmt")
        self.TranFee = params.get("TranFee")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevResigterBillSupportWithdrawResponse(AbstractModel):
    """RevResigterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class ReviseMbrPropertyRequest(AbstractModel):
    """ReviseMbrProperty请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param SubAcctNo: STRING(50)，见证子账户的账号\n        :type SubAcctNo: str\n        :param MemberProperty: STRING(10)，会员属性（00-普通子账号; SH-商户子账户。暂时只支持00-普通子账号改为SH-商户子账户）\n        :type MemberProperty: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberProperty = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberProperty = params.get("MemberProperty")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReviseMbrPropertyResponse(AbstractModel):
    """ReviseMbrProperty返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RevokeMemberRechargeThirdPayRequest(AbstractModel):
    """RevokeMemberRechargeThirdPay请求参数结构体

    """

    def __init__(self):
        """
        :param OldFillFrontSeqNo: STRING(52)，原充值的前置流水号\n        :type OldFillFrontSeqNo: str\n        :param OldFillPayChannelType: STRING(20)，原充值的支付渠道类型\n        :type OldFillPayChannelType: str\n        :param OldPayChannelTranSeqNo: STRING(52)，原充值的支付渠道交易流水号\n        :type OldPayChannelTranSeqNo: str\n        :param OldFillEjzbOrderNo: STRING(52)，原充值的电商见证宝订单号\n        :type OldFillEjzbOrderNo: str\n        :param ApplyCancelMemberAmt: STRING(20)，申请撤销的会员金额\n        :type ApplyCancelMemberAmt: str\n        :param ApplyCancelCommission: STRING(20)，申请撤销的手续费金额\n        :type ApplyCancelCommission: str\n        :param MrchCode: String(22)，商户号\n        :type MrchCode: str\n        :param Remark: STRING(300)，备注\n        :type Remark: str\n        :param ReservedMsgOne: STRING(300)，保留域1\n        :type ReservedMsgOne: str\n        :param ReservedMsgTwo: STRING(300)，保留域2\n        :type ReservedMsgTwo: str\n        :param ReservedMsgThree: STRING(300)，保留域3\n        :type ReservedMsgThree: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.OldFillFrontSeqNo = None
        self.OldFillPayChannelType = None
        self.OldPayChannelTranSeqNo = None
        self.OldFillEjzbOrderNo = None
        self.ApplyCancelMemberAmt = None
        self.ApplyCancelCommission = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.OldFillFrontSeqNo = params.get("OldFillFrontSeqNo")
        self.OldFillPayChannelType = params.get("OldFillPayChannelType")
        self.OldPayChannelTranSeqNo = params.get("OldPayChannelTranSeqNo")
        self.OldFillEjzbOrderNo = params.get("OldFillEjzbOrderNo")
        self.ApplyCancelMemberAmt = params.get("ApplyCancelMemberAmt")
        self.ApplyCancelCommission = params.get("ApplyCancelCommission")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeMemberRechargeThirdPayResponse(AbstractModel):
    """RevokeMemberRechargeThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsgOne: str\n        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsgTwo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class RevokeRechargeByThirdPayRequest(AbstractModel):
    """RevokeRechargeByThirdPay请求参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型此接口固定填：RevokeMemberRechargeThirdPayReq\n        :type RequestType: str\n        :param MerchantCode: 商户号\n        :type MerchantCode: str\n        :param PayChannel: 支付渠道\n        :type PayChannel: str\n        :param PayChannelSubId: 子渠道\n        :type PayChannelSubId: int\n        :param OrderId: 原始充值交易订单号\n        :type OrderId: str\n        :param BankAccountNumber: 父账户账号，资金汇总账号\n        :type BankAccountNumber: str\n        :param PlatformShortNumber: 平台短号(银行分配)\n        :type PlatformShortNumber: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param MidasSignature: 计费签名\n        :type MidasSignature: str\n        :param TransSequenceNumber: 交易流水号\n        :type TransSequenceNumber: str\n        :param TransFee: 申请撤销的手续费金额,以元为单位\n        :type TransFee: str\n        :param ThirdPayChannel: 第三方支付渠道类型 0001-微信 0002-支付宝 0003-京东支付\n        :type ThirdPayChannel: str\n        :param ThirdPayChannelOrderId: 第三方渠道订单号或流水号\n        :type ThirdPayChannelOrderId: str\n        :param OldFrontSequenceNumber: 充值接口银行返回的流水号(FrontSeqNo)\n        :type OldFrontSequenceNumber: str\n        :param CurrencyAmount: 申请撤销的金额\n        :type CurrencyAmount: str\n        :param CurrencyUnit: 单位，1：元，2：角，3：分 目前固定填1\n        :type CurrencyUnit: str\n        :param CurrencyType: 币种 目前固定填RMB\n        :type CurrencyType: str\n        :param MidasEnvironment: Midas环境标识\n        :type MidasEnvironment: str\n        :param ReservedMessage: 保留域\n        :type ReservedMessage: str\n        :param Remark: 备注\n        :type Remark: str\n        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.PlatformShortNumber = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.TransFee = None
        self.ThirdPayChannel = None
        self.ThirdPayChannelOrderId = None
        self.OldFrontSequenceNumber = None
        self.CurrencyAmount = None
        self.CurrencyUnit = None
        self.CurrencyType = None
        self.MidasEnvironment = None
        self.ReservedMessage = None
        self.Remark = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.TransFee = params.get("TransFee")
        self.ThirdPayChannel = params.get("ThirdPayChannel")
        self.ThirdPayChannelOrderId = params.get("ThirdPayChannelOrderId")
        self.OldFrontSequenceNumber = params.get("OldFrontSequenceNumber")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyType = params.get("CurrencyType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeRechargeByThirdPayResponse(AbstractModel):
    """RevokeRechargeByThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param RequestType: 请求类型\n        :type RequestType: str\n        :param ReservedMessage: 保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMessage: str\n        :param FrontSequenceNumber: 银行流水号\n        :type FrontSequenceNumber: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestType = None
        self.ReservedMessage = None
        self.FrontSequenceNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.ReservedMessage = params.get("ReservedMessage")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    """场景信息

    """

    def __init__(self):
        """
        :param LocaleCode: 语言代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type LocaleCode: str\n        :param RegionCode: 地区代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionCode: str\n        :param UserClientIp: 用户IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserClientIp: str\n        """
        self.LocaleCode = None
        self.RegionCode = None
        self.UserClientIp = None


    def _deserialize(self, params):
        self.LocaleCode = params.get("LocaleCode")
        self.RegionCode = params.get("RegionCode")
        self.UserClientIp = params.get("UserClientIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncContractDataRequest(AbstractModel):
    """SyncContractData请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合\n        :type UserId: str\n        :param Channel: 签约使用的渠道\n        :type Channel: str\n        :param OutContractCode: 业务签约合同协议号\n        :type OutContractCode: str\n        :param ContractStatus: 签约状态，枚举值
CONTRACT_STATUS_INVALID=无效状态
CONTRACT_STATUS_SIGNED=已签约
CONTRACT_STATUS_TERMINATED=已解约
CONTRACT_STATUS_PENDING=签约进行中\n        :type ContractStatus: str\n        :param ContractSyncInfo: 签约同步信息\n        :type ContractSyncInfo: :class:`tencentcloud.cpdp.v20190820.models.ContractSyncInfo`\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param UserType: 用户类型，枚举值
USER_ID: 用户ID
ANONYMOUS: 匿名类型 USER_ID
默认值为 USER_ID\n        :type UserType: str\n        :param SceneInfo: 场景信息\n        :type SceneInfo: :class:`tencentcloud.cpdp.v20190820.models.SceneInfo`\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.UserId = None
        self.Channel = None
        self.OutContractCode = None
        self.ContractStatus = None
        self.ContractSyncInfo = None
        self.MidasSignature = None
        self.MidasSecretId = None
        self.SubAppId = None
        self.UserType = None
        self.SceneInfo = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.OutContractCode = params.get("OutContractCode")
        self.ContractStatus = params.get("ContractStatus")
        if params.get("ContractSyncInfo") is not None:
            self.ContractSyncInfo = ContractSyncInfo()
            self.ContractSyncInfo._deserialize(params.get("ContractSyncInfo"))
        self.MidasSignature = params.get("MidasSignature")
        self.MidasSecretId = params.get("MidasSecretId")
        self.SubAppId = params.get("SubAppId")
        self.UserType = params.get("UserType")
        if params.get("SceneInfo") is not None:
            self.SceneInfo = SceneInfo()
            self.SceneInfo._deserialize(params.get("SceneInfo"))
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncContractDataResponse(AbstractModel):
    """SyncContractData返回参数结构体

    """

    def __init__(self):
        """
        :param Msg: 请求处理信息\n        :type Msg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class TerminateContractRequest(AbstractModel):
    """TerminateContract请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合\n        :type UserId: str\n        :param Channel: 指定渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定\n        :type Channel: str\n        :param TerminateMode: 枚举值：
CONTRACT_TERMINATION_MODE_BY_OUT_CONTRACT_CODE: 按OutContractCode+ContractSceneId解约
CONTRACT_TERMINATION_MODE_BY_CHANNEL_CONTRACT_CODE：按ChannelContractCode解约\n        :type TerminateMode: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param OutContractCode: 业务签约合同协议号 当TerminateMode=CONTRACT_TERMINATION_MODE_BY_OUT_CONTRACT_CODE 时 必填\n        :type OutContractCode: str\n        :param ContractSceneId: 签约场景ID，当 TerminateMode=CONTRACT_TERMINATION_MODE_BY_OUT_CONTRACT_CODE 时 必填，在米大师侧托管后生成\n        :type ContractSceneId: str\n        :param ChannelContractCode: 米大师生成的协议号 当 TerminateMode=CONTRACT_TERMINATION_MODE_BY_CHANNEL_CONTRACT_CODE 时 必填\n        :type ChannelContractCode: str\n        :param ExternalContractData: 第三方渠道合约数据，json字符串，与特定渠道有关\n        :type ExternalContractData: str\n        :param TerminationReason: 终止合约原因\n        :type TerminationReason: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param UserType: USER_ID: 用户ID
ANONYMOUS: 匿名类型 USER_ID
默认值为 USER_ID\n        :type UserType: str\n        :param ContractMethod: 签约方式\n        :type ContractMethod: str\n        :param MigrateMode: 签约代扣穿透查询存量数据迁移模式\n        :type MigrateMode: str\n        """
        self.MidasAppId = None
        self.UserId = None
        self.Channel = None
        self.TerminateMode = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.SubAppId = None
        self.OutContractCode = None
        self.ContractSceneId = None
        self.ChannelContractCode = None
        self.ExternalContractData = None
        self.TerminationReason = None
        self.MidasEnvironment = None
        self.UserType = None
        self.ContractMethod = None
        self.MigrateMode = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.TerminateMode = params.get("TerminateMode")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.SubAppId = params.get("SubAppId")
        self.OutContractCode = params.get("OutContractCode")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ChannelContractCode = params.get("ChannelContractCode")
        self.ExternalContractData = params.get("ExternalContractData")
        self.TerminationReason = params.get("TerminationReason")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.UserType = params.get("UserType")
        self.ContractMethod = params.get("ContractMethod")
        self.MigrateMode = params.get("MigrateMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateContractResponse(AbstractModel):
    """TerminateContract返回参数结构体

    """

    def __init__(self):
        """
        :param ContractTerminateData: 解约数据\n        :type ContractTerminateData: :class:`tencentcloud.cpdp.v20190820.models.ResponseTerminateContract`\n        :param Msg: 请求处理信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ContractTerminateData = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContractTerminateData") is not None:
            self.ContractTerminateData = ResponseTerminateContract()
            self.ContractTerminateData._deserialize(params.get("ContractTerminateData"))
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class TranItem(AbstractModel):
    """交易信息

    """

    def __init__(self):
        """
        :param FundSummaryAcctNo: STRING(50)，资金汇总账号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FundSummaryAcctNo: str\n        :param SubAcctNo: STRING(50)，见证子账户的账号
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctNo: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranNetMemberCode: str\n        :param MemberName: STRING(150)，会员名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemberName: str\n        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemberGlobalType: str\n        :param MemberGlobalId: STRING(32)，会员证件号码
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemberGlobalId: str\n        :param MemberAcctNo: STRING(50)，会员绑定账户的账号（提现的银行卡）
注意：此字段可能返回 null，表示取不到有效值。\n        :type MemberAcctNo: str\n        :param BankType: STRING(10)，会员绑定账户的本他行类型（1: 本行; 2: 他行）
注意：此字段可能返回 null，表示取不到有效值。\n        :type BankType: str\n        :param AcctOpenBranchName: STRING(150)，会员绑定账户的开户行名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type AcctOpenBranchName: str\n        :param CnapsBranchId: STRING(20)，会员绑定账户的开户行的联行号
注意：此字段可能返回 null，表示取不到有效值。\n        :type CnapsBranchId: str\n        :param EiconBankBranchId: STRING(20)，会员绑定账户的开户行的超级网银行号
注意：此字段可能返回 null，表示取不到有效值。\n        :type EiconBankBranchId: str\n        :param Mobile: STRING(30)，会员的手机号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mobile: str\n        """
        self.FundSummaryAcctNo = None
        self.SubAcctNo = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.Mobile = None


    def _deserialize(self, params):
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionItem(AbstractModel):
    """交易明细信息

    """

    def __init__(self):
        """
        :param BookingFlag: STRING(2)，记账标志（1: 转出; 2: 转入）
注意：此字段可能返回 null，表示取不到有效值。\n        :type BookingFlag: str\n        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranStatus: str\n        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranAmt: str\n        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranDate: str\n        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranTime: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param BookingType: STRING(20)，记账类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。\n        :type BookingType: str\n        :param InSubAcctNo: STRING(50)，转入见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。\n        :type InSubAcctNo: str\n        :param OutSubAcctNo: STRING(50)，转出见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutSubAcctNo: str\n        :param Remark: STRING(300)，备注（返回交易订单号）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        """
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.BookingType = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.BookingType = params.get("BookingType")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferDetailRequest(AbstractModel):
    """批量转账明细实体

    """

    def __init__(self):
        """
        :param MerchantDetailNo: 商家明细单号。
商户系统内部区分转账批次单下不同转账明细单的唯一标识，要求此参数只能由数字、大小写字母组成。
示例值：x23zy545Bd5436\n        :type MerchantDetailNo: str\n        :param TransferAmount: 转账金额。
转账金额单位为分。
示例值：200000\n        :type TransferAmount: int\n        :param TransferRemark: 转账备注。
单条转账备注（微信用户会收到该备注）。UTF8编码，最多32字符。
示例值：2020年4月报销\n        :type TransferRemark: str\n        :param OpenId: 用户在直连商户下的唯一标识。
示例值：o-MYE42l80oelYMDE34nYD456Xoy\n        :type OpenId: str\n        :param UserName: 收款用户姓名。
收款方姓名。
示例值：张三\n        :type UserName: str\n        """
        self.MerchantDetailNo = None
        self.TransferAmount = None
        self.TransferRemark = None
        self.OpenId = None
        self.UserName = None


    def _deserialize(self, params):
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.TransferAmount = params.get("TransferAmount")
        self.TransferRemark = params.get("TransferRemark")
        self.OpenId = params.get("OpenId")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferDetailResponse(AbstractModel):
    """批量转账查询返回批次明细实体

    """

    def __init__(self):
        """
        :param MerchantDetailNo: 商家明细单号。
商户系统内部的商家明细单号
示例值：plfk2020042013\n        :type MerchantDetailNo: str\n        :param DetailId: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480001\n        :type DetailId: str\n        :param DetailStatus: 明细状态。
PROCESSING：转账中，正在处理，结果未明；
SUCCESS：转账成功；
FAIL：转账失败，需要确认失败原因以后，再决定是否重新发起地该笔明细的转账。
示例值：SUCCESS\n        :type DetailStatus: str\n        """
        self.MerchantDetailNo = None
        self.DetailId = None
        self.DetailStatus = None


    def _deserialize(self, params):
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.DetailId = params.get("DetailId")
        self.DetailStatus = params.get("DetailStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferItem(AbstractModel):
    """转账充值明细信息

    """

    def __init__(self):
        """
        :param InAcctType: STRING(10)，入账类型（02: 会员充值; 03: 资金挂账）
注意：此字段可能返回 null，表示取不到有效值。\n        :type InAcctType: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranNetMemberCode: str\n        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctNo: str\n        :param TranAmt: STRING(20)，入金金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranAmt: str\n        :param InAcctNo: STRING(50)，入金账号
注意：此字段可能返回 null，表示取不到有效值。\n        :type InAcctNo: str\n        :param InAcctName: STRING(150)，入金账户名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InAcctName: str\n        :param Ccy: STRING(3)，币种
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ccy: str\n        :param AccountingDate: STRING(8)，会计日期（即银行主机记账日期）
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccountingDate: str\n        :param BankName: STRING(150)，银行名称（付款账户银行名称）
注意：此字段可能返回 null，表示取不到有效值。\n        :type BankName: str\n        :param Remark: STRING(300)，转账备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        """
        self.InAcctType = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.TranAmt = None
        self.InAcctNo = None
        self.InAcctName = None
        self.Ccy = None
        self.AccountingDate = None
        self.BankName = None
        self.Remark = None
        self.FrontSeqNo = None


    def _deserialize(self, params):
        self.InAcctType = params.get("InAcctType")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranAmt = params.get("TranAmt")
        self.InAcctNo = params.get("InAcctNo")
        self.InAcctName = params.get("InAcctName")
        self.Ccy = params.get("Ccy")
        self.AccountingDate = params.get("AccountingDate")
        self.BankName = params.get("BankName")
        self.Remark = params.get("Remark")
        self.FrontSeqNo = params.get("FrontSeqNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferSinglePayData(AbstractModel):
    """智能代发-单笔代发转账接口返回数据

    """

    def __init__(self):
        """
        :param TradeSerialNo: 平台交易流水号，唯一\n        :type TradeSerialNo: str\n        """
        self.TradeSerialNo = None


    def _deserialize(self, params):
        self.TradeSerialNo = params.get("TradeSerialNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferSinglePayRequest(AbstractModel):
    """TransferSinglePay请求参数结构体

    """

    def __init__(self):
        """
        :param MerchantId: 商户号\n        :type MerchantId: str\n        :param MerchantAppId: 微信申请商户号的appid或者商户号绑定的appid
支付宝、平安填入MerchantId\n        :type MerchantAppId: str\n        :param TransferType: 1、 微信企业付款 
2、 支付宝转账 
3、 平安银企直联代发转账\n        :type TransferType: int\n        :param OrderId: 订单流水号，唯一，不能包含特殊字符，长度最大限制64位，推荐使用字母，数字组合，"_","-"组合\n        :type OrderId: str\n        :param TransferAmount: 转账金额，单位分\n        :type TransferAmount: int\n        :param PayeeId: 收款方标识。
微信为open_id；
支付宝为会员alipay_user_id;
平安为收款方银行账号\n        :type PayeeId: str\n        :param PayeeName: 收款方姓名。支付宝可选；微信，平安模式下必传\n        :type PayeeName: str\n        :param PayeeExtends: 收款方附加信息，平安接入使用。需要以JSON格式提供以下字段：
PayeeBankName：收款人开户行名称
 CcyCode：货币类型（RMB-人民币）
 UnionFlag：行内跨行标志（1：行内转账，0：跨行转账）。\n        :type PayeeExtends: str\n        :param ReqReserved: 请求预留字段，原样透传返回\n        :type ReqReserved: str\n        :param Remark: 业务备注\n        :type Remark: str\n        :param NotifyUrl: 转账结果回调通知URL。若不填，则不进行回调。\n        :type NotifyUrl: str\n        :param Profile: 接入环境。沙箱环境填sandbox。\n        :type Profile: str\n        """
        self.MerchantId = None
        self.MerchantAppId = None
        self.TransferType = None
        self.OrderId = None
        self.TransferAmount = None
        self.PayeeId = None
        self.PayeeName = None
        self.PayeeExtends = None
        self.ReqReserved = None
        self.Remark = None
        self.NotifyUrl = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantAppId = params.get("MerchantAppId")
        self.TransferType = params.get("TransferType")
        self.OrderId = params.get("OrderId")
        self.TransferAmount = params.get("TransferAmount")
        self.PayeeId = params.get("PayeeId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeExtends = params.get("PayeeExtends")
        self.ReqReserved = params.get("ReqReserved")
        self.Remark = params.get("Remark")
        self.NotifyUrl = params.get("NotifyUrl")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferSinglePayResponse(AbstractModel):
    """TransferSinglePay返回参数结构体

    """

    def __init__(self):
        """
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功\n        :type ErrCode: str\n        :param ErrMessage: 响应消息\n        :type ErrMessage: str\n        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.cpdp.v20190820.models.TransferSinglePayData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = TransferSinglePayData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UnBindAcctRequest(AbstractModel):
    """UnBindAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SettleAcctNo: 用于提现
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>\n        :type SettleAcctNo: str\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA\n        :type EncryptType: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindAcctResponse(AbstractModel):
    """UnBindAcct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindRelateAcctRequest(AbstractModel):
    """UnbindRelateAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param FunctionFlag: STRING(2)，功能标志（1: 解绑）\n        :type FunctionFlag: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）\n        :type TranNetMemberCode: str\n        :param MemberAcctNo: STRING(50)，待解绑的提现账户的账号（提现账号）\n        :type MemberAcctNo: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindRelateAcctResponse(AbstractModel):
    """UnbindRelateAcct返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class UnifiedOrderInSubOrderList(AbstractModel):
    """子订单列表

    """

    def __init__(self):
        """
        :param SubMchIncome: 子订单结算应收金额，单位： 分\n        :type SubMchIncome: int\n        :param PlatformIncome: 子订单平台应收金额，单位：分\n        :type PlatformIncome: int\n        :param ProductDetail: 子订单商品详情\n        :type ProductDetail: str\n        :param ProductName: 子订单商品名称\n        :type ProductName: str\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SubOutTradeNo: 子订单号\n        :type SubOutTradeNo: str\n        :param Amt: 子订单支付金额\n        :type Amt: int\n        :param Metadata: 发货标识，由业务在调用聚鑫下单接口的 时候下发\n        :type Metadata: str\n        :param OriginalAmt: 子订单原始金额\n        :type OriginalAmt: int\n        """
        self.SubMchIncome = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SubAppId = None
        self.SubOutTradeNo = None
        self.Amt = None
        self.Metadata = None
        self.OriginalAmt = None


    def _deserialize(self, params):
        self.SubMchIncome = params.get("SubMchIncome")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.Amt = params.get("Amt")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnifiedOrderRequest(AbstractModel):
    """UnifiedOrder请求参数结构体

    """

    def __init__(self):
        """
        :param CurrencyType: ISO 货币代码，CNY\n        :type CurrencyType: str\n        :param MidasAppId: 聚鑫分配的支付主MidasAppId\n        :type MidasAppId: str\n        :param OutTradeNo: 支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合\n        :type OutTradeNo: str\n        :param ProductDetail: 商品详情，需要URL编码\n        :type ProductDetail: str\n        :param ProductId: 商品ID，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合\n        :type ProductId: str\n        :param ProductName: 商品名称，需要URL编码\n        :type ProductName: str\n        :param TotalAmt: 支付金额，单位： 分\n        :type TotalAmt: int\n        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合\n        :type UserId: str\n        :param RealChannel: 银行真实渠道.如:bank_pingan\n        :type RealChannel: str\n        :param OriginalAmt: 原始金额\n        :type OriginalAmt: int\n        :param MidasSecretId: 聚鑫分配的安全ID\n        :type MidasSecretId: str\n        :param MidasSignature: 按照聚鑫安全密钥计算的签名\n        :type MidasSignature: str\n        :param CallbackUrl: Web端回调地址\n        :type CallbackUrl: str\n        :param Channel: 指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定\n        :type Channel: str\n        :param Metadata: 透传字段，支付成功回调透传给应用，用于业务透传自定义内容\n        :type Metadata: str\n        :param Quantity: 购买数量，不传默认为1\n        :type Quantity: int\n        :param SubAppId: 聚鑫计费SubAppId，代表子商户\n        :type SubAppId: str\n        :param SubOrderList: 子订单信息列表，格式：子订单号、子应用ID、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)
注：接入银行或其他支付渠道服务商模式下，必传\n        :type SubOrderList: list of UnifiedOrderInSubOrderList\n        :param TotalMchIncome: 结算应收金额，单位：分\n        :type TotalMchIncome: int\n        :param TotalPlatformIncome: 平台应收金额，单位：分\n        :type TotalPlatformIncome: int\n        :param WxOpenId: 微信公众号/小程序支付时为必选，需要传微信下的openid\n        :type WxOpenId: str\n        :param WxSubOpenId: 在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一\n        :type WxSubOpenId: str\n        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release\n        :type MidasEnvironment: str\n        :param WxAppId: 微信商户应用ID\n        :type WxAppId: str\n        :param WxSubAppId: 微信商户子应用ID\n        :type WxSubAppId: str\n        :param PaymentNotifyUrl: 支付通知地址\n        :type PaymentNotifyUrl: str\n        """
        self.CurrencyType = None
        self.MidasAppId = None
        self.OutTradeNo = None
        self.ProductDetail = None
        self.ProductId = None
        self.ProductName = None
        self.TotalAmt = None
        self.UserId = None
        self.RealChannel = None
        self.OriginalAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CallbackUrl = None
        self.Channel = None
        self.Metadata = None
        self.Quantity = None
        self.SubAppId = None
        self.SubOrderList = None
        self.TotalMchIncome = None
        self.TotalPlatformIncome = None
        self.WxOpenId = None
        self.WxSubOpenId = None
        self.MidasEnvironment = None
        self.WxAppId = None
        self.WxSubAppId = None
        self.PaymentNotifyUrl = None


    def _deserialize(self, params):
        self.CurrencyType = params.get("CurrencyType")
        self.MidasAppId = params.get("MidasAppId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.TotalAmt = params.get("TotalAmt")
        self.UserId = params.get("UserId")
        self.RealChannel = params.get("RealChannel")
        self.OriginalAmt = params.get("OriginalAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Channel = params.get("Channel")
        self.Metadata = params.get("Metadata")
        self.Quantity = params.get("Quantity")
        self.SubAppId = params.get("SubAppId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = UnifiedOrderInSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.TotalMchIncome = params.get("TotalMchIncome")
        self.TotalPlatformIncome = params.get("TotalPlatformIncome")
        self.WxOpenId = params.get("WxOpenId")
        self.WxSubOpenId = params.get("WxSubOpenId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.WxAppId = params.get("WxAppId")
        self.WxSubAppId = params.get("WxSubAppId")
        self.PaymentNotifyUrl = params.get("PaymentNotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnifiedOrderResponse(AbstractModel):
    """UnifiedOrder返回参数结构体

    """

    def __init__(self):
        """
        :param TotalAmt: 支付金额，单位： 分\n        :type TotalAmt: int\n        :param OutTradeNo: 应用支付订单号\n        :type OutTradeNo: str\n        :param PayInfo: 支付参数透传给聚鑫SDK（原文透传给SDK即可，不需要解码）\n        :type PayInfo: str\n        :param TransactionId: 聚鑫的交易订单\n        :type TransactionId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalAmt = None
        self.OutTradeNo = None
        self.PayInfo = None
        self.TransactionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAmt = params.get("TotalAmt")
        self.OutTradeNo = params.get("OutTradeNo")
        self.PayInfo = params.get("PayInfo")
        self.TransactionId = params.get("TransactionId")
        self.RequestId = params.get("RequestId")


class UploadTaxListRequest(AbstractModel):
    """UploadTaxList请求参数结构体

    """

    def __init__(self):
        """
        :param Channel: 平台渠道\n        :type Channel: int\n        :param BeginMonth: 起始月份，YYYY-MM\n        :type BeginMonth: str\n        :param EndMonth: 结束月份。如果只上传一个月，结束月份等于起始月份\n        :type EndMonth: str\n        :param FileUrl: 完税列表下载地址\n        :type FileUrl: str\n        """
        self.Channel = None
        self.BeginMonth = None
        self.EndMonth = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")
        self.BeginMonth = params.get("BeginMonth")
        self.EndMonth = params.get("EndMonth")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadTaxListResponse(AbstractModel):
    """UploadTaxList返回参数结构体

    """

    def __init__(self):
        """
        :param TaxId: 完税ID\n        :type TaxId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaxId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaxId = params.get("TaxId")
        self.RequestId = params.get("RequestId")


class UploadTaxPaymentRequest(AbstractModel):
    """UploadTaxPayment请求参数结构体

    """

    def __init__(self):
        """
        :param Channel: 平台渠道\n        :type Channel: int\n        :param TaxId: 完税ID\n        :type TaxId: str\n        :param FileUrl: 完税列表下载地址\n        :type FileUrl: str\n        """
        self.Channel = None
        self.TaxId = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")
        self.TaxId = params.get("TaxId")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadTaxPaymentResponse(AbstractModel):
    """UploadTaxPayment返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WithdrawBill(AbstractModel):
    """聚鑫提现订单内容

    """

    def __init__(self):
        """
        :param WithdrawOrderId: 业务提现订单号\n        :type WithdrawOrderId: str\n        :param Date: 提现日期\n        :type Date: str\n        :param PayAmt: 提现金额，单位： 分\n        :type PayAmt: str\n        :param InSubAppId: 聚鑫分配转入账户appid\n        :type InSubAppId: str\n        :param OutSubAppId: 聚鑫分配转出账户appid\n        :type OutSubAppId: str\n        :param CurrencyType: ISO货币代码\n        :type CurrencyType: str\n        :param MetaData: 透传字段\n        :type MetaData: str\n        :param ExtendFieldData: 扩展字段\n        :type ExtendFieldData: str\n        """
        self.WithdrawOrderId = None
        self.Date = None
        self.PayAmt = None
        self.InSubAppId = None
        self.OutSubAppId = None
        self.CurrencyType = None
        self.MetaData = None
        self.ExtendFieldData = None


    def _deserialize(self, params):
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        self.Date = params.get("Date")
        self.PayAmt = params.get("PayAmt")
        self.InSubAppId = params.get("InSubAppId")
        self.OutSubAppId = params.get("OutSubAppId")
        self.CurrencyType = params.get("CurrencyType")
        self.MetaData = params.get("MetaData")
        self.ExtendFieldData = params.get("ExtendFieldData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawCashMembershipRequest(AbstractModel):
    """WithdrawCashMembership请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）\n        :type MrchCode: str\n        :param TranWebName: STRING(150)，交易网名称（市场名称）\n        :type TranWebName: str\n        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）\n        :type MemberGlobalType: str\n        :param MemberGlobalId: STRING(32)，会员证件号码\n        :type MemberGlobalId: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码\n        :type TranNetMemberCode: str\n        :param MemberName: STRING(150)，会员名称\n        :type MemberName: str\n        :param TakeCashAcctNo: STRING(50)，提现账号（银行卡）\n        :type TakeCashAcctNo: str\n        :param OutAmtAcctName: STRING(150)，出金账户名称（银行卡户名）\n        :type OutAmtAcctName: str\n        :param Ccy: STRING(3)，币种（默认为RMB）\n        :type Ccy: str\n        :param CashAmt: STRING(20)，可提现金额\n        :type CashAmt: str\n        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）\n        :type Remark: str\n        :param ReservedMsg: STRING(1027)，保留域\n        :type ReservedMsg: str\n        :param WebSign: STRING(300)，网银签名\n        :type WebSign: str\n        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"\n        :type Profile: str\n        """
        self.MrchCode = None
        self.TranWebName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.TakeCashAcctNo = None
        self.OutAmtAcctName = None
        self.Ccy = None
        self.CashAmt = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranWebName = params.get("TranWebName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.OutAmtAcctName = params.get("OutAmtAcctName")
        self.Ccy = params.get("Ccy")
        self.CashAmt = params.get("CashAmt")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawCashMembershipResponse(AbstractModel):
    """WithdrawCashMembership返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码\n        :type TxnReturnCode: str\n        :param TxnReturnMsg: String(100)，返回信息\n        :type TxnReturnMsg: str\n        :param CnsmrSeqNo: String(22)，交易流水号\n        :type CnsmrSeqNo: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param TransferFee: STRING(20)，转账手续费（固定返回0.00）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransferFee: str\n        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReservedMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.TransferFee = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.TransferFee = params.get("TransferFee")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class WithdrawItem(AbstractModel):
    """清分提现明细信息

    """

    def __init__(self):
        """
        :param BookingFlag: STRING(2)，记账标志（01: 提现; 02: 清分 ）
注意：此字段可能返回 null，表示取不到有效值。\n        :type BookingFlag: str\n        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranStatus: str\n        :param BookingMsg: STRING(200)，记账说明
注意：此字段可能返回 null，表示取不到有效值。\n        :type BookingMsg: str\n        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranNetMemberCode: str\n        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctNo: str\n        :param SubAcctName: STRING(150)，见证子账户的名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubAcctName: str\n        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranAmt: str\n        :param Commission: STRING(20)，手续费
注意：此字段可能返回 null，表示取不到有效值。\n        :type Commission: str\n        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranDate: str\n        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranTime: str\n        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrontSeqNo: str\n        :param Remark: STRING(300)，备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        """
        self.BookingFlag = None
        self.TranStatus = None
        self.BookingMsg = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.SubAcctName = None
        self.TranAmt = None
        self.Commission = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.BookingMsg = params.get("BookingMsg")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctName = params.get("SubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.Commission = params.get("Commission")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        