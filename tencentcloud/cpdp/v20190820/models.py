# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class Acct(AbstractModel):
    """账户信息

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，见证子账户的账号（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctProperty: STRING(10)，见证子账户的属性（可重复。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctProperty: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctName: STRING(150)，见证子账户的名称（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param AcctAvailBal: STRING(20)，见证子账户可用余额（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctAvailBal: str
        :param CashAmt: STRING(20)，见证子账户可提现金额（可重复。开户日期或修改日期）
注意：此字段可能返回 null，表示取不到有效值。
        :type CashAmt: str
        :param MaintenanceDate: STRING(8)，维护日期
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintenanceDate: str
        """
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


class ApplyApplicationMaterialRequest(AbstractModel):
    """ApplyApplicationMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param TradeCode: 贸易编码
        :type TradeCode: str
        :param OriginalDeclareId: 原申报流水号
        :type OriginalDeclareId: str
        :param SourceAmount: 源金额
        :type SourceAmount: int
        :param TargetAmount: 目的金额
        :type TargetAmount: int
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
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


class ApplyApplicationMaterialResponse(AbstractModel):
    """ApplyApplicationMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 提交申报材料结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 第三方指令编号
        :type TransactionId: str
        :param Status: 受理状态
        :type Status: str
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param OriginalDeclareId: 原申报流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalDeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        """
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


class ApplyDeclareResult(AbstractModel):
    """提交申报材料结果

    """

    def __init__(self):
        """
        :param Code: 错误码
        :type Code: str
        :param Data: 提交申报材料数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyDeclareData()
            self.Data._deserialize(params.get("Data"))


class ApplyOutwardOrderData(AbstractModel):
    """汇出指令申请数据

    """

    def __init__(self):
        """
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param Status: 受理状态
        :type Status: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.Status = params.get("Status")


class ApplyOutwardOrderRequest(AbstractModel):
    """ApplyOutwardOrder请求参数结构体

    """

    def __init__(self):
        """
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param PricingCurrency: 定价币种
        :type PricingCurrency: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param PayeeType: 收款人类型
        :type PayeeType: str
        :param PayeeAccount: 收款人账号
        :type PayeeAccount: str
        :param SourceAmount: 源币种金额
        :type SourceAmount: float
        :param TargetAmount: 目的金额
        :type TargetAmount: float
        :param PayeeName: 收款人姓名
        :type PayeeName: str
        :param PayeeAddress: 收款人地址
        :type PayeeAddress: str
        :param PayeeBankAccountType: 收款人银行账号类型
        :type PayeeBankAccountType: str
        :param PayeeCountryCode: 收款人国家或地区编码
        :type PayeeCountryCode: str
        :param PayeeBankName: 收款人开户银行名称
        :type PayeeBankName: str
        :param PayeeBankAddress: 收款人开户银行地址
        :type PayeeBankAddress: str
        :param PayeeBankDistrict: 收款人开户银行所在国家或地区编码
        :type PayeeBankDistrict: str
        :param PayeeBankSwiftCode: 收款银行SwiftCode
        :type PayeeBankSwiftCode: str
        :param PayeeBankType: 收款银行国际编码类型
        :type PayeeBankType: str
        :param PayeeBankCode: 收款银行国际编码
        :type PayeeBankCode: str
        :param ReferenceForBeneficiary: 收款人附言
        :type ReferenceForBeneficiary: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
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


class ApplyOutwardOrderResponse(AbstractModel):
    """ApplyOutwardOrder返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 汇出指令申请
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Data: 汇出指令申请数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderData`
        :param Code: 错误码
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplyOutwardOrderData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")


class ApplyPayerInfoRequest(AbstractModel):
    """ApplyPayerInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayerType: 付款人类型 (个人: INDIVIDUAL, 企业: CORPORATE)
        :type PayerType: str
        :param PayerName: 付款人姓名
        :type PayerName: str
        :param PayerIdType: 付款人证件类型 (身份证: ID_CARD, 统一社会信用代码: UNIFIED_CREDIT_CODE)
        :type PayerIdType: str
        :param PayerIdNo: 付款人证件号
        :type PayerIdNo: str
        :param PayerCountryCode: 付款人常驻国家或地区编码 (见常见问题-国家/地区编码)
        :type PayerCountryCode: str
        :param PayerContactName: 付款人联系人名称
        :type PayerContactName: str
        :param PayerContactNumber: 付款人联系电话 (PayerType=CORPORATE 必填)
        :type PayerContactNumber: str
        :param PayerEmailAddress: 付款人联系邮箱
        :type PayerEmailAddress: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
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


class ApplyPayerInfoResponse(AbstractModel):
    """ApplyPayerInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 付款人申请结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MerchantId: 商户号
        :type MerchantId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        """
        self.MerchantId = None
        self.PayerId = None
        self.Status = None
        self.FailReason = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")


class ApplyPayerinfoResult(AbstractModel):
    """付款人申请结果

    """

    def __init__(self):
        """
        :param Code: 错误码
        :type Code: str
        :param Data: 数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyPayerinfoData()
            self.Data._deserialize(params.get("Data"))


class ApplyReWithdrawalRequest(AbstractModel):
    """ApplyReWithdrawal请求参数结构体

    """

    def __init__(self):
        """
        :param BusinessType: 聚鑫业务类型
        :type BusinessType: int
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param Body: 提现信息
        :type Body: :class:`tencentcloud.cpdp.v20190820.models.WithdrawBill`
        :param MidasAppId: 聚鑫业务ID
        :type MidasAppId: str
        """
        self.BusinessType = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Body = None
        self.MidasAppId = None


    def _deserialize(self, params):
        self.BusinessType = params.get("BusinessType")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        if params.get("Body") is not None:
            self.Body = WithdrawBill()
            self.Body._deserialize(params.get("Body"))
        self.MidasAppId = params.get("MidasAppId")


class ApplyReWithdrawalResponse(AbstractModel):
    """ApplyReWithdrawal返回参数结构体

    """

    def __init__(self):
        """
        :param WithdrawOrderId: 重新提现业务订单号
        :type WithdrawOrderId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param TradeCurrency: 交易币种
        :type TradeCurrency: str
        :param TradeAmount: 交易金额
        :type TradeAmount: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 状态
        :type Status: str
        """
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


class ApplyTradeRequest(AbstractModel):
    """ApplyTrade请求参数结构体

    """

    def __init__(self):
        """
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param TradeOrderId: 贸易材料订单号
        :type TradeOrderId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayeeName: 付款人姓名
        :type PayeeName: str
        :param PayeeCountryCode: 收款人常驻国家或地区编码 (见常见问题)
        :type PayeeCountryCode: str
        :param TradeType: 贸易类型 (GOODS: 商品, SERVICE: 服务)
        :type TradeType: str
        :param TradeTime: 交易时间 (格式: yyyyMMdd)
        :type TradeTime: str
        :param TradeCurrency: 交易币种
        :type TradeCurrency: str
        :param TradeAmount: 交易金额
        :type TradeAmount: float
        :param TradeName: 交易名称 
(TradeType=GOODS时填写物品名称，可填写多个，格式无要求；
TradeType=SERVICE时填写贸易类别，见常见问题-贸易类别)
        :type TradeName: str
        :param TradeCount: 交易数量 (TradeType=GOODS 填写物品数量, TradeType=SERVICE填写服务次数)
        :type TradeCount: int
        :param GoodsCarrier: 货贸承运人 (TradeType=GOODS 必填)
        :type GoodsCarrier: str
        :param ServiceDetail: 服贸交易细节 (TradeType=GOODS 必填, 见常见问题-交易细节)
        :type ServiceDetail: str
        :param ServiceTime: 服贸服务时间 (TradeType=GOODS 必填, 见常见问题-服务时间)
        :type ServiceTime: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
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


class ApplyTradeResponse(AbstractModel):
    """ApplyTrade返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 提交贸易材料结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Code: 错误码
        :type Code: str
        :param Data: 提交贸易材料数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyTradeData()
            self.Data._deserialize(params.get("Data"))


class ApplyWithdrawalRequest(AbstractModel):
    """ApplyWithdrawal请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctName: str
        :param CurrencyType: 币种 RMB
        :type CurrencyType: str
        :param CurrencyUnit: 单位，1：元，2：角，3：分
        :type CurrencyUnit: int
        :param CurrencyAmt: 金额
        :type CurrencyAmt: str
        :param TranWebName: 交易网名称
        :type TranWebName: str
        :param IdType: 会员证件类型
        :type IdType: str
        :param IdCode: 会员证件号码
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type IdCode: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
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


class ApplyWithdrawalResponse(AbstractModel):
    """ApplyWithdrawal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BankCardItem(AbstractModel):
    """绑卡列表

    """

    def __init__(self):
        """
        :param EiconBankBranchId: 超级网银行号
        :type EiconBankBranchId: str
        :param CnapsBranchId: 大小额行号
        :type CnapsBranchId: str
        :param SettleAcctType: 结算账户类型
1 – 本行账户
2 – 他行账户
        :type SettleAcctType: int
        :param SettleAcctName: 结算账户户名
<敏感信息>
        :type SettleAcctName: str
        :param AcctBranchName: 开户行名称
        :type AcctBranchName: str
        :param SettleAcctNo: 用于提现
<敏感信息>
        :type SettleAcctNo: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 验证类型
1 – 小额转账验证
2 – 短信验证
        :type BindType: int
        :param Mobile: 用于短信验证
BindType==2时必填
<敏感信息>
        :type Mobile: str
        :param IdType: 证件类型
        :type IdType: str
        :param IdCode: 证件号码
<敏感信息>
        :type IdCode: str
        """
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


class BindAcctRequest(AbstractModel):
    """BindAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 1 – 小额转账验证
2 – 短信验证
每个结算账户每天只能使用一次小额转账验证
        :type BindType: int
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctName: str
        :param SettleAcctType: 1 – 本行账户
2 – 他行账户
        :type SettleAcctType: int
        :param IdType: 证件类型，见《证件类型》表
        :type IdType: str
        :param IdCode: 证件号码
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type IdCode: str
        :param AcctBranchName: 开户行名称
        :type AcctBranchName: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param Mobile: 用于短信验证
BindType==2时必填
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Mobile: str
        :param CnapsBranchId: 大小额行号，超级网银行号和大小额行号
二选一
        :type CnapsBranchId: str
        :param EiconBankBranchId: 超级网银行号，超级网银行号和大小额行号
二选一
        :type EiconBankBranchId: str
        """
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


class BindAcctResponse(AbstractModel):
    """BindAcct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindRelateAccReUnionPayRequest(AbstractModel):
    """BindRelateAccReUnionPay请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctUnionPay接口中的“会员的待绑定账户的账号”）
        :type MemberAcctNo: str
        :param MessageCheckCode: STRING(20)，短信验证码（即 BindRelateAcctUnionPay接口中的手机所接收到的短信验证码）
        :type MessageCheckCode: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.MessageCheckCode = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.MessageCheckCode = params.get("MessageCheckCode")
        self.ReservedMsg = params.get("ReservedMsg")


class BindRelateAccReUnionPayResponse(AbstractModel):
    """BindRelateAccReUnionPay返回参数结构体

    """

    def __init__(self):
        """
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）
        :type Mobile: str
        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，转账方式（1: 往账鉴权(默认值); 2: 来账鉴权）
        :type ReservedMsg: str
        """
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


class BindRelateAcctSmallAmountResponse(AbstractModel):
    """BindRelateAcctSmallAmount返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域（来账鉴权的方式下，此字段的值为客户需往监管账户转入的金额。在同名子账户绑定的场景下，若返回""VERIFIED""则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）
        :type Mobile: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
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


class BindRelateAcctUnionPayResponse(AbstractModel):
    """BindRelateAcctUnionPay返回参数结构体

    """

    def __init__(self):
        """
        :param ReservedMsg: STRING(1027)，保留域（在同名子账户绑定的场景下，若返回"VERIFIED"则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class CheckAcctRequest(AbstractModel):
    """CheckAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 1：小额鉴权
2：短信校验鉴权
        :type BindType: int
        :param SettleAcctNo: 结算账户账号
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param CheckCode: 短信验证码
BindType==2必填
        :type CheckCode: str
        :param CurrencyType: 币种 RMB
BindType==1必填
        :type CurrencyType: str
        :param CurrencyUnit: 单位
1：元，2：角，3：分
BindType==1必填
        :type CurrencyUnit: int
        :param CurrencyAmt: 金额
BindType==1必填
        :type CurrencyAmt: str
        """
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


class CheckAcctResponse(AbstractModel):
    """CheckAcct返回参数结构体

    """

    def __init__(self):
        """
        :param FrontSeqNo: 前置流水号，请保存
        :type FrontSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param TakeCashAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户的账号”）
        :type TakeCashAcctNo: str
        :param AuthAmt: STRING(20)，鉴权验证金额（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户收到的验证金额。原小额转账鉴权方式为来账鉴权的情况下此字段须赋值为0.00）
        :type AuthAmt: str
        :param Ccy: STRING(3)，币种（默认为RMB）
        :type Ccy: str
        :param ReservedMsg: STRING(1027)，原小额转账方式（1: 往账鉴权，此为默认值; 2: 来账鉴权）
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.TakeCashAcctNo = None
        self.AuthAmt = None
        self.Ccy = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.AuthAmt = params.get("AuthAmt")
        self.Ccy = params.get("Ccy")
        self.ReservedMsg = params.get("ReservedMsg")


class CheckAmountResponse(AbstractModel):
    """CheckAmount返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param SubAcctType: STRING(40)，子账号类型（子帐号类型。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号; 7: 在途; 8: 理财购买子帐号; 9: 理财赎回子帐号; 10: 平台子拥有结算子帐号）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctType: str
        :param ReconcileStatus: STRING(3)，对账状态（0: 成功; 1: 失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReconcileStatus: str
        :param ReconcileReturnMsg: STRING(300)，对账返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReconcileReturnMsg: str
        :param ClearingStatus: STRING(20)，清算状态（0: 成功; 1: 失败; 2: 异常; 3: 待处理）
注意：此字段可能返回 null，表示取不到有效值。
        :type ClearingStatus: str
        :param ClearingReturnMsg: STRING(2)，清算返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClearingReturnMsg: str
        :param TotalAmt: STRING(300)，待清算总金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAmt: str
        """
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


class CloseOrderRequest(AbstractModel):
    """CloseOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param OutTradeNo: 业务订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo
        :type TransactionId: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.TransactionId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")


class CloseOrderResponse(AbstractModel):
    """CloseOrder返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAcctRequest(AbstractModel):
    """CreateAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId
        :type MidasAppId: str
        :param SubMchId: 业务平台的子商户ID，唯一
        :type SubMchId: str
        :param SubMchName: 子商户名称
        :type SubMchName: str
        :param Address: 子商户地址
        :type Address: str
        :param Contact: 子商户联系人
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Contact: str
        :param Mobile: 联系人手机号
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Mobile: str
        :param Email: 邮箱 
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type Email: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param SubMchType: 子商户类型：
个人: personal
企业：enterprise
缺省： enterprise
        :type SubMchType: str
        :param ShortName: 不填则默认子商户名称
        :type ShortName: str
        :param SubMerchantMemberType: 子商户会员类型：
general:普通子账户
merchant:商户子账户
缺省： general
        :type SubMerchantMemberType: str
        """
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


class CreateAcctResponse(AbstractModel):
    """CreateAcct返回参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubAcctNo: 平安银行生成的子商户账户
        :type SubAcctNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.SubAcctNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.RequestId = params.get("RequestId")


class CreateCustAcctIdRequest(AbstractModel):
    """CreateCustAcctId请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionFlag: STRING(2)，功能标志（1: 开户; 3: 销户）
        :type FunctionFlag: str
        :param FundSummaryAcctNo: STRING(50)，资金汇总账号（即收单资金归集入账的账号）
        :type FundSummaryAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（平台端的用户ID，需要保证唯一性，可数字字母混合，如HY_120）
        :type TranNetMemberCode: str
        :param MemberProperty: STRING(10)，会员属性（00-普通子账户(默认); SH-商户子账户）
        :type MemberProperty: str
        :param Mobile: STRING(30)，手机号码
        :type Mobile: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SelfBusiness: String(2)，是否为自营业务（0位非自营，1为自营）
        :type SelfBusiness: bool
        :param ContactName: String(64)，联系人
        :type ContactName: str
        :param SubAcctName: String(64)，子账户名称
        :type SubAcctName: str
        :param SubAcctShortName: String(64)，子账户简称
        :type SubAcctShortName: str
        :param SubAcctType: String(4)，子账户类型（0: 个人子账户; 1: 企业子账户）
        :type SubAcctType: int
        :param UserNickname: STRING(150)，用户昵称
        :type UserNickname: str
        :param Email: STRING(150)，邮箱
        :type Email: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
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


class CreateCustAcctIdResponse(AbstractModel):
    """CreateCustAcctId返回参数结构体

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，见证子账户的账号（平台需要记录下来，后续所有接口交互都会用到）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域（需要开通智能收款，此处返回智能收款账号，正常情况下返回空）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Name: 商品名称
        :type Name: str
        :param TaxCode: 税收商品编码
        :type TaxCode: str
        :param TotalPrice: 不含税商品总价（商品含税价总额/（1+税率））。单位为分
        :type TotalPrice: int
        :param TaxRate: 商品税率
        :type TaxRate: int
        :param TaxAmount: 商品税额（不含税商品总价*税率）。单位为分
        :type TaxAmount: int
        :param TaxType: 税收商品类别
        :type TaxType: str
        :param Models: 商品规格
        :type Models: str
        :param Unit: 商品单位
        :type Unit: str
        :param Total: 商品数量
        :type Total: str
        :param Price: 不含税商品单价
        :type Price: str
        :param Discount: 含税折扣总额。单位为分
        :type Discount: int
        :param PreferentialPolicyFlag: 优惠政策标志。0：不使用优惠政策；1：使用优惠政策。
        :type PreferentialPolicyFlag: str
        :param ZeroTaxFlag: 零税率标识：
空：非零税率；
0：出口零税率；
1：免税；
2：不征税；
3：普通零税率。
        :type ZeroTaxFlag: str
        :param VatSpecialManagement: 增值税特殊管理。PreferentialPolicyFlag字段为1时，必填。目前仅支持5%(3%，2%，1.5%)简易征税、免税、不征税。
        :type VatSpecialManagement: str
        """
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


class CreateInvoiceRequest(AbstractModel):
    """CreateInvoice请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID。0：高灯
        :type InvoicePlatformId: int
        :param TitleType: 抬头类型：1：个人/政府事业单位；2：企业
        :type TitleType: int
        :param BuyerTitle: 购方名称
        :type BuyerTitle: str
        :param OrderId: 业务开票号
        :type OrderId: str
        :param AmountHasTax: 含税总金额（单位为分）
        :type AmountHasTax: int
        :param TaxAmount: 总税额（单位为分）
        :type TaxAmount: int
        :param AmountWithoutTax: 不含税总金额（单位为分）
        :type AmountWithoutTax: int
        :param SellerTaxpayerNum: 销方纳税人识别号
        :type SellerTaxpayerNum: str
        :param SellerName: 销方名称。（不填默认读取商户注册时输入的信息）
        :type SellerName: str
        :param SellerAddress: 销方地址。（不填默认读取商户注册时输入的信息）
        :type SellerAddress: str
        :param SellerPhone: 销方电话。（不填默认读取商户注册时输入的信息）
        :type SellerPhone: str
        :param SellerBankName: 销方银行名称。（不填默认读取商户注册时输入的信息）
        :type SellerBankName: str
        :param SellerBankAccount: 销方银行账号。（不填默认读取商户注册时输入的信息）
        :type SellerBankAccount: str
        :param BuyerTaxpayerNum: 购方纳税人识别号（购方票面信息）,若抬头类型为2时，必传
        :type BuyerTaxpayerNum: str
        :param BuyerAddress: 购方地址。开具专用发票时必填
        :type BuyerAddress: str
        :param BuyerBankName: 购方银行名称。开具专用发票时必填
        :type BuyerBankName: str
        :param BuyerBankAccount: 购方银行账号。开具专用发票时必填
        :type BuyerBankAccount: str
        :param BuyerPhone: 购方电话。开具专用发票时必填
        :type BuyerPhone: str
        :param BuyerEmail: 收票人邮箱。若填入，会收到发票推送邮件
        :type BuyerEmail: str
        :param TakerPhone: 收票人手机号。若填入，会收到发票推送短信
        :type TakerPhone: str
        :param InvoiceType: 开票类型：
1：增值税专用发票；
2：增值税普通发票；
3：增值税电子发票；
4：增值税卷式发票；
5：区块链电子发票。
若该字段不填，或值不为1-5，则认为开具”增值税电子发票”
        :type InvoiceType: int
        :param CallbackUrl: 发票结果回传地址
        :type CallbackUrl: str
        :param Drawer: 开票人姓名。（不填默认读取商户注册时输入的信息）
        :type Drawer: str
        :param Payee: 收款人姓名。（不填默认读取商户注册时输入的信息）
        :type Payee: str
        :param Checker: 复核人姓名。（不填默认读取商户注册时输入的信息）
        :type Checker: str
        :param TerminalCode: 税盘号
        :type TerminalCode: str
        :param LevyMethod: 征收方式。开具差额征税发票时必填2。开具普通征税发票时为空
        :type LevyMethod: str
        :param Deduction: 差额征税扣除额（单位为分）
        :type Deduction: int
        :param Remark: 备注（票面信息）
        :type Remark: str
        :param Items: 项目商品明细
        :type Items: list of CreateInvoiceItem
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        """
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


class CreateInvoiceResponse(AbstractModel):
    """CreateInvoice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 发票开具结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Message: 错误消息
        :type Message: str
        :param Code: 错误码
        :type Code: int
        :param Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResultData`
        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = CreateInvoiceResultData()
            self.Data._deserialize(params.get("Data"))


class CreateInvoiceResultData(AbstractModel):
    """蓝票结果数据

    """

    def __init__(self):
        """
        :param State: 开票状态
        :type State: int
        :param InvoiceId: 发票ID
        :type InvoiceId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        """
        self.State = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")


class CreateMerchantRequest(AbstractModel):
    """CreateMerchant请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID
        :type InvoicePlatformId: int
        :param TaxpayerName: 企业名称
        :type TaxpayerName: str
        :param TaxpayerNum: 销方纳税人识别号
        :type TaxpayerNum: str
        :param LegalPersonName: 注册企业法定代表人名称
        :type LegalPersonName: str
        :param ContactsName: 联系人
        :type ContactsName: str
        :param Phone: 联系人手机号
        :type Phone: str
        :param Address: 不包含省市名称的地址
        :type Address: str
        :param RegionCode: 地区编码
        :type RegionCode: int
        :param CityName: 市（地区）名称
        :type CityName: str
        :param Drawer: 开票人
        :type Drawer: str
        :param TaxRegistrationCertificate: 税务登记证图片（Base64）字符串，需小于 3M
        :type TaxRegistrationCertificate: str
        :param Email: 联系人邮箱地址
        :type Email: str
        :param BusinessMobile: 企业电话
        :type BusinessMobile: str
        :param BankName: 银行名称
        :type BankName: str
        :param BankAccount: 银行账号
        :type BankAccount: str
        :param Reviewer: 复核人
        :type Reviewer: str
        :param Payee: 收款人
        :type Payee: str
        :param RegisterCode: 注册邀请码
        :type RegisterCode: str
        :param State: 不填默认为1，有效状态
0：表示无效；
1:表示有效；
2:表示禁止开蓝票；
3:表示禁止冲红。
        :type State: str
        :param CallbackUrl: 接收推送的消息地址
        :type CallbackUrl: str
        :param Profile: 接入环境。沙箱环境填 sandbox。
        :type Profile: str
        """
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


class CreateMerchantResponse(AbstractModel):
    """CreateMerchant返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 商户注册结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Code: 状态码
        :type Code: int
        :param Message: 响应消息
        :type Message: str
        :param Data: 创建商户结果数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResultData`
        """
        self.Code = None
        self.Message = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Data") is not None:
            self.Data = CreateMerchantResultData()
            self.Data._deserialize(params.get("Data"))


class CreateMerchantResultData(AbstractModel):
    """创建商户结果数据

    """

    def __init__(self):
        """
        :param TaxpayerName: 企业名称
        :type TaxpayerName: str
        :param SerialNo: 请求流水号
        :type SerialNo: str
        :param TaxpayerNum: 纳税号
        :type TaxpayerNum: str
        """
        self.TaxpayerName = None
        self.SerialNo = None
        self.TaxpayerNum = None


    def _deserialize(self, params):
        self.TaxpayerName = params.get("TaxpayerName")
        self.SerialNo = params.get("SerialNo")
        self.TaxpayerNum = params.get("TaxpayerNum")


class CreateRedInvoiceItem(AbstractModel):
    """创建红票明细

    """

    def __init__(self):
        """
        :param OrderId: 订单号
        :type OrderId: str
        :param CallbackUrl: 发票结果回传地址
        :type CallbackUrl: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        :param RedSerialNo: 红字信息表编码
        :type RedSerialNo: str
        """
        self.OrderId = None
        self.CallbackUrl = None
        self.OrderSn = None
        self.RedSerialNo = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.CallbackUrl = params.get("CallbackUrl")
        self.OrderSn = params.get("OrderSn")
        self.RedSerialNo = params.get("RedSerialNo")


class CreateRedInvoiceRequest(AbstractModel):
    """CreateRedInvoice请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID
        :type InvoicePlatformId: int
        :param Invoices: 红冲明细
        :type Invoices: list of CreateRedInvoiceItem
        :param Profile: 接入环境。沙箱环境填 sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.Invoices = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        if params.get("Invoices") is not None:
            self.Invoices = []
            for item in params.get("Invoices"):
                obj = CreateRedInvoiceItem()
                obj._deserialize(item)
                self.Invoices.append(obj)
        self.Profile = params.get("Profile")


class CreateRedInvoiceResponse(AbstractModel):
    """CreateRedInvoice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 红冲结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Message: 错误消息
        :type Message: str
        :param Code: 错误码
        :type Code: int
        :param Data: 红票数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CreateRedInvoiceResultData
        """
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


class CreateRedInvoiceResultData(AbstractModel):
    """红票结果数据

    """

    def __init__(self):
        """
        :param Code: 红冲状态码
        :type Code: int
        :param Message: 红冲状态消息
        :type Message: str
        :param InvoiceId: 发票ID
        :type InvoiceId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        """
        self.Code = None
        self.Message = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")


class DownloadBillRequest(AbstractModel):
    """DownloadBill请求参数结构体

    """

    def __init__(self):
        """
        :param StateDate: 请求下载对账单日期
        :type StateDate: str
        :param MidasAppId: 聚鑫分配的MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的SecretId
        :type MidasSecretId: str
        :param MidasSignature: 使用聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.StateDate = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.StateDate = params.get("StateDate")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class DownloadBillResponse(AbstractModel):
    """DownloadBill返回参数结构体

    """

    def __init__(self):
        """
        :param FileName: 账单文件名
        :type FileName: str
        :param FileMD5: 账单文件的MD5值
        :type FileMD5: str
        :param DownloadUrl: 账单文件的真实下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileName = None
        self.FileMD5 = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileMD5 = params.get("FileMD5")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class FileItem(AbstractModel):
    """对账文件信息

    """

    def __init__(self):
        """
        :param FileName: STRING(256)，文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param RandomPassword: STRING(120)，随机密码
注意：此字段可能返回 null，表示取不到有效值。
        :type RandomPassword: str
        :param FilePath: STRING(512)，文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param DrawCode: STRING(64)，提取码
注意：此字段可能返回 null，表示取不到有效值。
        :type DrawCode: str
        """
        self.FileName = None
        self.RandomPassword = None
        self.FilePath = None
        self.DrawCode = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.RandomPassword = params.get("RandomPassword")
        self.FilePath = params.get("FilePath")
        self.DrawCode = params.get("DrawCode")


class ModifyMntMbrBindRelateAcctBankCodeRequest(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
        :type SubAcctNo: str
        :param MemberBindAcctNo: STRING(50)，会员绑定账号
        :type MemberBindAcctNo: str
        :param AcctOpenBranchName: STRING(150)，开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，大小额行号（CnapsBranchId和EiconBankBranchId两者二选一必填）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，超级网银行号
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberBindAcctNo = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberBindAcctNo = params.get("MemberBindAcctNo")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")


class ModifyMntMbrBindRelateAcctBankCodeResponse(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class QueryAcctBindingRequest(AbstractModel):
    """QueryAcctBinding请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryAcctBindingResponse(AbstractModel):
    """QueryAcctBinding返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总行数
        :type TotalCount: int
        :param BankCardItems: 银行卡信息列表
        :type BankCardItems: list of BankCardItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param QueryAcctBeginTime: 查询开始时间(以开户时间为准)
        :type QueryAcctBeginTime: str
        :param QueryAcctEndTime: 查询结束时间(以开户时间为准)
        :type QueryAcctEndTime: str
        :param PageOffset: 分页号,  起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照开户时间的先后
        :type PageOffset: str
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.QueryAcctBeginTime = None
        self.QueryAcctEndTime = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.QueryAcctBeginTime = params.get("QueryAcctBeginTime")
        self.QueryAcctEndTime = params.get("QueryAcctEndTime")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryAcctInfoListResponse(AbstractModel):
    """QueryAcctInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param ResultCount: 本次交易返回查询结果记录数
        :type ResultCount: int
        :param TotalCount: 符合业务查询条件的记录总数
        :type TotalCount: int
        :param QueryAcctItems: 查询结果项 [object,object]
        :type QueryAcctItems: list of QueryAcctItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId
        :type MidasAppId: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubMchId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryAcctInfoResponse(AbstractModel):
    """QueryAcctInfo返回参数结构体

    """

    def __init__(self):
        """
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubMchName: 子商户名称
        :type SubMchName: str
        :param SubMchType: 子商户类型：
个人: personal
企业：enterprise
缺省： enterprise
        :type SubMchType: str
        :param ShortName: 不填则默认子商户名称
        :type ShortName: str
        :param Address: 子商户地址
        :type Address: str
        :param Contact: 子商户联系人子商户联系人
<敏感信息>
        :type Contact: str
        :param Mobile: 联系人手机号
<敏感信息>
        :type Mobile: str
        :param Email: 邮箱 
<敏感信息>
        :type Email: str
        :param SubMchId: 子商户id
        :type SubMchId: str
        :param SubAcctNo: 子账户
        :type SubAcctNo: str
        :param SubMerchantMemberType: 子商户会员类型：
general:普通子账户
merchant:商户子账户
缺省： general
注意：此字段可能返回 null，表示取不到有效值。
        :type SubMerchantMemberType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
缺省： enterprise
        :type SubMchType: str
        :param SubMchName: 子商户名称
        :type SubMchName: str
        :param SubAcctNo: 子账号号
        :type SubAcctNo: str
        :param ShortName: 不填则默认子商户名称
        :type ShortName: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param Contact: 子商户联系人
<敏感信息>
        :type Contact: str
        :param Address: 子商户地址
        :type Address: str
        :param Mobile: 联系人手机号
<敏感信息>
        :type Mobile: str
        :param Email: 邮箱 
<敏感信息>
        :type Email: str
        :param SubMerchantMemberType: 子商户会员类型：
general:普通子账户
merchant:商户子账户
缺省： general
注意：此字段可能返回 null，表示取不到有效值。
        :type SubMerchantMemberType: str
        """
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


class QueryApplicationMaterialRequest(AbstractModel):
    """QueryApplicationMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.DeclareId = None
        self.Profile = None


    def _deserialize(self, params):
        self.DeclareId = params.get("DeclareId")
        self.Profile = params.get("Profile")


class QueryApplicationMaterialResponse(AbstractModel):
    """QueryApplicationMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 成功申报材料查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param QueryFlag: 2：普通会员子账号
3：功能子账号
        :type QueryFlag: str
        :param PageOffset: 起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后
        :type PageOffset: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.QueryFlag = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.QueryFlag = params.get("QueryFlag")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryBalanceResponse(AbstractModel):
    """QueryBalance返回参数结构体

    """

    def __init__(self):
        """
        :param ResultCount: 本次交易返回查询结果记录数
        :type ResultCount: str
        :param StartRecordOffset: 起始记录号
        :type StartRecordOffset: str
        :param EndFlag: 结束标志
        :type EndFlag: str
        :param TotalCount: 符合业务查询条件的记录总数
        :type TotalCount: str
        :param QueryItems: 查询结果项
        :type QueryItems: list of QueryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 全部; 2: 指定时间段）
        :type FunctionFlag: str
        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param StartDate: STRING(8)，开始日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式: 20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankClearResponse(AbstractModel):
    """QueryBankClear返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数, 一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of ClearItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查询标志（1: 全部; 2: 转出; 3: 转入 ）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param StartDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankTransactionDetailsResponse(AbstractModel):
    """QueryBankTransactionDetails返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransactionItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查询标志（2: 提现; 3: 清分）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param BeginDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type BeginDate: str
        :param EndDate: STRING(8)，结束日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.BeginDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankWithdrawCashDetailsResponse(AbstractModel):
    """QueryBankWithdrawCashDetails返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0:否; 1:是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of WithdrawItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class QueryCommonTransferRechargeRequest(AbstractModel):
    """QueryCommonTransferRecharge请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1为查询当日数据，0查询历史数据）
        :type FunctionFlag: str
        :param StartDate: STRING(8)，开始日期（格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（格式：20190101）
        :type EndDate: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.StartDate = None
        self.EndDate = None
        self.PageNum = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.PageNum = params.get("PageNum")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryCommonTransferRechargeResponse(AbstractModel):
    """QueryCommonTransferRecharge返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransferItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class QueryCustAcctIdBalanceRequest(AbstractModel):
    """QueryCustAcctIdBalance请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查询标志（2: 普通会员子账号; 3: 功能子账号）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2时，子账号必输）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryCustAcctIdBalanceResponse(AbstractModel):
    """QueryCustAcctIdBalance返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param AcctArray: 账户信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctArray: list of Acct
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param OriginalDeclareId: 原申报流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalDeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param SourceAmount: 源金额
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAmount: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param TargetAmount: 目的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAmount: str
        :param TradeCode: 交易编码
        :type TradeCode: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
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


class QueryDeclareResult(AbstractModel):
    """成功申报材料查询结果

    """

    def __init__(self):
        """
        :param Data: 成功申报材料查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareData`
        :param Code: 错误码
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryDeclareData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")


class QueryExchangeRateRequest(AbstractModel):
    """QueryExchangeRate请求参数结构体

    """

    def __init__(self):
        """
        :param SourceCurrency: 源币种 (默认CNY)
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种 (见常见问题-汇出币种)
        :type TargetCurrency: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.Profile = None


    def _deserialize(self, params):
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.Profile = params.get("Profile")


class QueryExchangeRateResponse(AbstractModel):
    """QueryExchangeRate返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询汇率结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryExchangerateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Rate: 汇率
        :type Rate: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param RateTime: 汇率时间
        :type RateTime: str
        :param BaseCurrency: 基准币种
        :type BaseCurrency: str
        """
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


class QueryExchangerateResult(AbstractModel):
    """查询汇率结果

    """

    def __init__(self):
        """
        :param Code: 错误码
        :type Code: str
        :param Data: 查询汇率数据数组
        :type Data: list of QueryExchangerateData
        """
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


class QueryInvoiceRequest(AbstractModel):
    """QueryInvoice请求参数结构体

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 开票平台ID
        :type InvoicePlatformId: int
        :param OrderId: 订单号
        :type OrderId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        :param IsRed: 发票种类：
0：蓝票
1：红票【该字段默认为0， 如果需要查询红票信息，本字段必须传1，否则可能查询不到需要的发票信息】。
        :type IsRed: int
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.OrderSn = None
        self.IsRed = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.OrderSn = params.get("OrderSn")
        self.IsRed = params.get("IsRed")
        self.Profile = params.get("Profile")


class QueryInvoiceResponse(AbstractModel):
    """QueryInvoice返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 发票查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Message: 错误消息
        :type Message: str
        :param Code: 错误码
        :type Code: int
        :param Data: 查询发票数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResultData`
        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryInvoiceResultData()
            self.Data._deserialize(params.get("Data"))


class QueryInvoiceResultData(AbstractModel):
    """查询发票结果数据

    """

    def __init__(self):
        """
        :param OrderId: 订单号
        :type OrderId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        :param Status: 发票状态
        :type Status: int
        :param Message: 开票描述
        :type Message: str
        :param TicketDate: 开票日期
        :type TicketDate: str
        :param TicketSn: 发票号码
        :type TicketSn: str
        :param TicketCode: 发票代码
        :type TicketCode: str
        :param CheckCode: 检验码
        :type CheckCode: str
        :param AmountWithTax: 含税金额(元)
        :type AmountWithTax: str
        :param AmountWithoutTax: 不含税金额(元)
        :type AmountWithoutTax: str
        :param TaxAmount: 税额(元)
        :type TaxAmount: str
        :param IsRedWashed: 是否被红冲
        :type IsRedWashed: int
        :param PdfUrl: pdf地址
        :type PdfUrl: str
        """
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


class QueryItem(AbstractModel):
    """聚鑫商户余额查询输出项

    """

    def __init__(self):
        """
        :param SubAcctNo: 子商户账户
        :type SubAcctNo: str
        :param SubAcctProperty: 子账户属性 
1：普通会员子账号 
2：挂账子账号 
3：手续费子账号 
4：利息子账号
5：平台担保子账号
        :type SubAcctProperty: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param SubAcctName: 子账户名称
        :type SubAcctName: str
        :param AcctAvailBal: 账户可用余额
        :type AcctAvailBal: str
        :param CashAmt: 可提现金额
        :type CashAmt: str
        :param MaintenanceDate: 维护日期 开户日期或修改日期
        :type MaintenanceDate: str
        """
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


class QueryMemberBindRequest(AbstractModel):
    """QueryMemberBind请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查询标志（1: 全部会员; 2: 单个会员; 3: 单个会员的证件信息）
        :type QueryFlag: str
        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2或3时，子账户账号必输）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryMemberBindResponse(AbstractModel):
    """QueryMemberBind返回参数结构体

    """

    def __init__(self):
        """
        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TranItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 下单预支付; 2: 确认并付款; 3: 退款; 6: 直接支付T+1; 9: 直接支付T+0）
        :type FunctionFlag: str
        :param OutSubAcctNo: STRING(50)，转出方的见证子账户的账号（付款方）
        :type OutSubAcctNo: str
        :param OutMemberCode: STRING(32)，转出方的交易网会员代码
        :type OutMemberCode: str
        :param OutSubAcctName: STRING(150)，转出方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）
        :type OutSubAcctName: str
        :param InSubAcctNo: STRING(50)，转入方的见证子账户的账号（收款方）
        :type InSubAcctNo: str
        :param InMemberCode: STRING(32)，转入方的交易网会员代码
        :type InMemberCode: str
        :param InSubAcctName: STRING(150)，转入方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）
        :type InSubAcctName: str
        :param TranAmt: STRING(20)，交易金额
        :type TranAmt: str
        :param TranFee: STRING(20)，交易费用（平台收取交易费用）
        :type TranFee: str
        :param TranType: STRING(20)，交易类型（01: 普通交易）
        :type TranType: str
        :param Ccy: STRING(3)，币种（默认: RMB）
        :type Ccy: str
        :param OrderNo: STRING(50)，订单号（功能标志为1,2,3时必输）
        :type OrderNo: str
        :param OrderContent: STRING(500)，订单内容
        :type OrderContent: str
        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域（若需短信验证码则此项必输短信指令号）
        :type ReservedMsg: str
        :param WebSign: STRING(300)，网银签名（若需短信验证码则此项必输）
        :type WebSign: str
        """
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


class QueryMemberTransactionResponse(AbstractModel):
    """QueryMemberTransaction返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Currency: 余额币种
        :type Currency: str
        :param Balance: 账户余额
        :type Balance: str
        :param MerchantId: 商户ID
        :type MerchantId: str
        """
        self.Currency = None
        self.Balance = None
        self.MerchantId = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Balance = params.get("Balance")
        self.MerchantId = params.get("MerchantId")


class QueryMerchantBalanceRequest(AbstractModel):
    """QueryMerchantBalance请求参数结构体

    """

    def __init__(self):
        """
        :param Currency: 余额币种
        :type Currency: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.Currency = None
        self.Profile = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Profile = params.get("Profile")


class QueryMerchantBalanceResponse(AbstractModel):
    """QueryMerchantBalance返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 对接方账户余额查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Code: 错误码
        :type Code: str
        :param Data: 对接账户余额查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryMerchantBalanceData()
            self.Data._deserialize(params.get("Data"))


class QueryOrderOutOrderList(AbstractModel):
    """查询订单接口的出参，订单列表

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param Amt: 支付金额，单位：分
        :type Amt: int
        :param UserId: 用户Id
        :type UserId: str
        :param CashAmt: 现金支付金额
        :type CashAmt: str
        :param Metadata: 发货标识，由业务在调用聚鑫下单 接口的时候下发
        :type Metadata: str
        :param PayTime: 支付时间unix时间戳
        :type PayTime: str
        :param CouponAmt: 抵扣券金额
        :type CouponAmt: str
        :param OrderTime: 下单时间unix时间戳
        :type OrderTime: str
        :param ProductId: 物品id
        :type ProductId: str
        :param SceneInfo: 高速场景信息
        :type SceneInfo: str
        :param OrderState: 当前订单的订单状态 
0：初始状态，获取聚鑫交易订单成功；  
1：拉起聚鑫支付页面成功，用户未 支付；
2：用户支付成功，正在发货；
3：用户支付成功，发货失败；
4：用户支付成功，发货成功；
5：聚鑫支付页面正在失效中；
6：聚鑫支付页面已经失效；
        :type OrderState: str
        :param Channel: 支付渠道：wechat：微信支付;
qqwallet：QQ钱包;
bank：网银
        :type Channel: str
        :param RefundFlag: 是否曾退款
        :type RefundFlag: str
        :param OutTradeNo: 务支付订单号
        :type OutTradeNo: str
        :param ProductName: 商品名称
        :type ProductName: str
        :param CallBackTime: 支付回调时间，unix时间戳
        :type CallBackTime: str
        :param CurrencyType: ISO 货币代码，CNY
        :type CurrencyType: str
        :param AcctSubAppId: 微校场景账户Id
        :type AcctSubAppId: str
        :param TransactionId: 调用下单接口获取的聚鑫交易订单
        :type TransactionId: str
        :param ChannelOrderId: 聚鑫内部渠道订单号
        :type ChannelOrderId: str
        :param SubOrderList: 调用下单接口传进来的 SubOutTradeNoList
        :type SubOrderList: list of QueryOrderOutSubOrderList
        :param ChannelExternalOrderId: 支付机构订单号
        :type ChannelExternalOrderId: str
        """
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


class QueryOrderOutSubOrderList(AbstractModel):
    """子订单列表

    """

    def __init__(self):
        """
        :param Amt: 子订单支付金额
        :type Amt: int
        :param SubMchIncome: 子订单结算应收金额，单位：分
        :type SubMchIncome: int
        :param Metadata: 发货标识，由业务在调用Midas下单接口的时候下发。
        :type Metadata: str
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param SettleCheck: 核销状态，1表示核销，0表示未核销
        :type SettleCheck: int
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        """
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


class QueryOrderRequest(AbstractModel):
    """QueryOrder请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主 MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param Type: type=by_order根据订单号 查订单；
type=by_user根据用户id 查订单 。
        :type Type: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param Count: 每页返回的记录数。根据用户 号码查询订单列表时需要传。 用于分页展示。Type=by_order时必填
        :type Count: int
        :param Offset: 记录数偏移量，默认从0开 始。根据用户号码查询订单列 表时需要传。用于分页展示。Type=by_order时必填
        :type Offset: int
        :param StartTime: 查询开始时间，Unix时间戳。Type=by_order时必填
        :type StartTime: str
        :param EndTime: 查询结束时间，Unix时间戳。Type=by_order时必填
        :type EndTime: str
        :param OutTradeNo: 业务订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo
        :type TransactionId: str
        """
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


class QueryOrderResponse(AbstractModel):
    """QueryOrder返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 返回订单数
        :type TotalNum: int
        :param OrderList: 查询结果的订单列表
        :type OrderList: list of QueryOrderOutOrderList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param AcctDate: 财务日期
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctDate: str
        :param PricingCurrency: 定价币种
注意：此字段可能返回 null，表示取不到有效值。
        :type PricingCurrency: str
        :param SourceCurrency: 源币种
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCurrency: str
        :param SourceAmount: 源金额
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAmount: str
        :param TargetCurrency: 目的币种
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetCurrency: str
        :param TargetAmount: 目的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAmount: str
        :param FxRate: 汇率
注意：此字段可能返回 null，表示取不到有效值。
        :type FxRate: str
        :param Status: 指令状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param RefundAmount: 退汇金额
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundAmount: str
        :param RefundCurrency: 退汇币种
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundCurrency: str
        """
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


class QueryOutwardOrderRequest(AbstractModel):
    """QueryOutwardOrder请求参数结构体

    """

    def __init__(self):
        """
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.TransactionId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.Profile = params.get("Profile")


class QueryOutwardOrderResponse(AbstractModel):
    """QueryOutwardOrder返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 查询汇出结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Code: 错误码
        :type Code: str
        :param Data: 查询汇出数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryOutwardOrderData()
            self.Data._deserialize(params.get("Data"))


class QueryPayerInfoRequest(AbstractModel):
    """QueryPayerInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.PayerId = None
        self.Profile = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.Profile = params.get("Profile")


class QueryPayerInfoResponse(AbstractModel):
    """QueryPayerInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 付款人查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MerchantId: 商户号
        :type MerchantId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 审核状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param PayerType: 付款人类型
        :type PayerType: str
        :param PayerName: 付款人姓名
        :type PayerName: str
        :param PayerIdType: 付款人证件类型
        :type PayerIdType: str
        :param PayerIdNo: 付款人证件号
        :type PayerIdNo: str
        :param PayerContactNumber: 付款人联系电话
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerContactNumber: str
        :param PayerEmailAddress: 付款人联系邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerEmailAddress: str
        :param PayerCountryCode: 付款人常驻国家或地区编码
        :type PayerCountryCode: str
        :param PayerContactName: 付款人联系名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerContactName: str
        """
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


class QueryPayerinfoResult(AbstractModel):
    """付款人查询结果

    """

    def __init__(self):
        """
        :param Code: 错误码
        :type Code: str
        :param Data: 付款人查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryPayerinfoData()
            self.Data._deserialize(params.get("Data"))


class QueryReconciliationDocumentRequest(AbstractModel):
    """QueryReconciliationDocument请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param FileType: STRING(10)，文件类型（充值文件-CZ; 提现文件-TX; 交易文件-JY; 余额文件-YE; 合约文件-HY）
        :type FileType: str
        :param FileDate: STRING(8)，文件日期（格式：20190101）
        :type FileDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FileType = None
        self.FileDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FileType = params.get("FileType")
        self.FileDate = params.get("FileDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryReconciliationDocumentResponse(AbstractModel):
    """QueryReconciliationDocument返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of FileItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合。
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合。
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryRefundResponse(AbstractModel):
    """QueryRefund返回参数结构体

    """

    def __init__(self):
        """
        :param State: 退款状态码，退款提交成功后返回  1：退款中；  2：退款成功；  3：退款失败。
        :type State: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class QuerySingleTransactionStatusRequest(AbstractModel):
    """QuerySingleTransactionStatus请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（2: 会员间交易; 3: 提现; 4: 充值）
        :type FunctionFlag: str
        :param TranNetSeqNo: STRING(52)，交易网流水号（提现，充值或会员交易请求时的CnsmrSeqNo值）
        :type TranNetSeqNo: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号（未启用）
        :type SubAcctNo: str
        :param TranDate: STRING(8)，交易日期（未启用）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetSeqNo = None
        self.SubAcctNo = None
        self.TranDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetSeqNo = params.get("TranNetSeqNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QuerySingleTransactionStatusResponse(AbstractModel):
    """QuerySingleTransactionStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param BookingFlag: STRING(2)，记账标志（记账标志。1: 登记挂账; 2: 支付; 3: 提现; 4: 清分; 5: 下单预支付; 6: 确认并付款; 7: 退款; 8: 支付到平台; N: 其他）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功; 1: 失败; 2: 待确认; 5: 待处理; 6: 处理中。0和1是终态，2、5、6是中间态，其中2是特指提现后待确认提现是否成功，5是银行收到交易等待处理，6是交易正在处理）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param InSubAcctNo: STRING(50)，转入子账户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，转出子账户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param FailMsg: STRING(300)，失败信息（当提现失败时，返回交易失败原因）
注意：此字段可能返回 null，表示取不到有效值。
        :type FailMsg: str
        :param OldTranFrontSeqNo: STRING(50)，原前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OldTranFrontSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param OldTranSeqNo: STRING(52)，原交易流水号（小额鉴权交易请求时的CnsmrSeqNo值）
        :type OldTranSeqNo: str
        :param TranDate: STRING(8)，交易日期（格式：20190101）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.OldTranSeqNo = None
        self.TranDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.OldTranSeqNo = params.get("OldTranSeqNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QuerySmallAmountTransferResponse(AbstractModel):
    """QuerySmallAmountTransfer返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReturnStatus: STRING(10)，返回状态（0: 成功; 1: 失败; 2: 待确认）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnStatus: str
        :param ReturnMsg: STRING(512)，返回信息（失败返回具体信息）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param TradeOrderId: 贸易材料订单号
        :type TradeOrderId: str
        :param Status: 审核状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayeeName: 收款人姓名
        :type PayeeName: str
        :param PayeeCountryCode: 收款人常驻国家或地区编码
        :type PayeeCountryCode: str
        :param TradeType: 交易类型
        :type TradeType: str
        :param TradeTime: 交易日期
        :type TradeTime: str
        :param TradeCurrency: 交易币种
        :type TradeCurrency: str
        :param TradeAmount: 交易金额
        :type TradeAmount: str
        :param TradeName: 交易名称
        :type TradeName: str
        :param TradeCount: 交易数量
        :type TradeCount: int
        :param GoodsCarrier: 货贸承运人
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsCarrier: str
        :param ServiceDetail: 服贸交易细节
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDetail: str
        :param ServiceTime: 服贸服务时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTime: str
        """
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


class QueryTradeRequest(AbstractModel):
    """QueryTrade请求参数结构体

    """

    def __init__(self):
        """
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.TradeFileId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TradeFileId = params.get("TradeFileId")
        self.Profile = params.get("Profile")


class QueryTradeResponse(AbstractModel):
    """QueryTrade返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 贸易材料明细查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Data: 贸易材料明细查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeData`
        :param Code: 错误码
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryTradeData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")


class RechargeMemberThirdPayRequest(AbstractModel):
    """RechargeMemberThirdPay请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会代码
        :type TranNetMemberCode: str
        :param MemberFillAmt: STRING(20)，会员充值金额
        :type MemberFillAmt: str
        :param Commission: STRING(20)，手续费金额
        :type Commission: str
        :param Ccy: STRING(3)，币种。如RMB
        :type Ccy: str
        :param PayChannelType: STRING(20)，支付渠道类型。
0001-微信
0002-支付宝
0003-京东支付
        :type PayChannelType: str
        :param PayChannelAssignMerNo: STRING(50)，支付渠道所分配的商户号
        :type PayChannelAssignMerNo: str
        :param PayChannelTranSeqNo: STRING(52)，支付渠道交易流水号
        :type PayChannelTranSeqNo: str
        :param EjzbOrderNo: STRING(52)，电商见证宝订单号
        :type EjzbOrderNo: str
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param EjzbOrderContent: STRING(500)，电商见证宝订单内容
        :type EjzbOrderContent: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
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


class RechargeMemberThirdPayResponse(AbstractModel):
    """RechargeMemberThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param MemberSubAcctPreAvailBal: STRING(20)，会员子账户交易前可用余额
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberSubAcctPreAvailBal: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class RefundOutSubOrderRefundList(AbstractModel):
    """退款子订单列表

    """

    def __init__(self):
        """
        :param PlatformRefundAmt: 平台应退金额
        :type PlatformRefundAmt: int
        :param RefundAmt: 子订单退款金额
        :type RefundAmt: int
        :param SubMchRefundAmt: 商家应退金额
        :type SubMchRefundAmt: int
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param SubRefundId: 子退款单号，调用方需要保证 全局唯一性
        :type SubRefundId: str
        """
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


class RefundRequest(AbstractModel):
    """Refund请求参数结构体

    """

    def __init__(self):
        """
        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、 字母、下划线（_）、横杠字 符（-）、点（.）的组合
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param TotalRefundAmt: 退款金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额
        :type TotalRefundAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param OutTradeNo: 商品订单，仅支持数字、字 母、下划线（_）、横杠字符 （-）、点（.）的组合。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo
        :type OutTradeNo: str
        :param MchRefundAmt: 结算应收金额，单位：分
        :type MchRefundAmt: int
        :param TransactionId: 调用下单接口获取的聚鑫交 易订单。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo
        :type TransactionId: str
        :param PlatformRefundAmt: 平台应收金额，单位：分
        :type PlatformRefundAmt: int
        :param SubOrderRefundList: 支持多个子订单批量退款单 个子订单退款支持传 SubOutTradeNo ，也支持传 SubOutTradeNoList ，都传的时候以 SubOutTradeNoList 为准。  如果传了子单退款细节，外 部不需要再传退款金额，平 台应退，商户应退金额，我 们可以直接根据子单退款算出来总和。
        :type SubOrderRefundList: list of RefundOutSubOrderRefundList
        """
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


class RefundResponse(AbstractModel):
    """Refund返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterBillSupportWithdrawRequest(AbstractModel):
    """RegisterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param OrderNo: STRING(50)，订单号
        :type OrderNo: str
        :param SuspendAmt: STRING(20)，挂账金额（包含交易费用）
        :type SuspendAmt: str
        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）
        :type TranFee: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.TranNetMemberCode = None
        self.OrderNo = None
        self.SuspendAmt = None
        self.TranFee = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


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


class RegisterBillSupportWithdrawResponse(AbstractModel):
    """RegisterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param CnsmrSeqNo: String(22)，交易流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class RevRegisterBillSupportWithdrawRequest(AbstractModel):
    """RevRegisterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param OldOrderNo: STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）
        :type OldOrderNo: str
        :param CancelAmt: STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）
        :type CancelAmt: str
        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）
        :type TranFee: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.OldOrderNo = None
        self.CancelAmt = None
        self.TranFee = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


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


class RevRegisterBillSupportWithdrawResponse(AbstractModel):
    """RevRegisterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class RevResigterBillSupportWithdrawRequest(AbstractModel):
    """RevResigterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param OldOrderNo: STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）
        :type OldOrderNo: str
        :param CancelAmt: STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）
        :type CancelAmt: str
        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）
        :type TranFee: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.OldOrderNo = None
        self.CancelAmt = None
        self.TranFee = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


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


class RevResigterBillSupportWithdrawResponse(AbstractModel):
    """RevResigterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
        :type SubAcctNo: str
        :param MemberProperty: STRING(10)，会员属性（00-普通子账号; SH-商户子账户。暂时只支持00-普通子账号改为SH-商户子账户）
        :type MemberProperty: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberProperty = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberProperty = params.get("MemberProperty")
        self.ReservedMsg = params.get("ReservedMsg")


class ReviseMbrPropertyResponse(AbstractModel):
    """ReviseMbrProperty返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param OldFillFrontSeqNo: STRING(52)，原充值的前置流水号
        :type OldFillFrontSeqNo: str
        :param OldFillPayChannelType: STRING(20)，原充值的支付渠道类型
        :type OldFillPayChannelType: str
        :param OldPayChannelTranSeqNo: STRING(52)，原充值的支付渠道交易流水号
        :type OldPayChannelTranSeqNo: str
        :param OldFillEjzbOrderNo: STRING(52)，原充值的电商见证宝订单号
        :type OldFillEjzbOrderNo: str
        :param ApplyCancelMemberAmt: STRING(20)，申请撤销的会员金额
        :type ApplyCancelMemberAmt: str
        :param ApplyCancelCommission: STRING(20)，申请撤销的手续费金额
        :type ApplyCancelCommission: str
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
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


class RevokeMemberRechargeThirdPayResponse(AbstractModel):
    """RevokeMemberRechargeThirdPay返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class TranItem(AbstractModel):
    """交易信息

    """

    def __init__(self):
        """
        :param FundSummaryAcctNo: STRING(50)，资金汇总账号
注意：此字段可能返回 null，表示取不到有效值。
        :type FundSummaryAcctNo: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，会员名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员绑定账户的账号（提现的银行卡）
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员绑定账户的本他行类型（1: 本行; 2: 他行）
注意：此字段可能返回 null，表示取不到有效值。
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员绑定账户的开户行名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，会员绑定账户的开户行的联行号
注意：此字段可能返回 null，表示取不到有效值。
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员绑定账户的开户行的超级网银行号
注意：此字段可能返回 null，表示取不到有效值。
        :type EiconBankBranchId: str
        :param Mobile: STRING(30)，会员的手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
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


class TransactionItem(AbstractModel):
    """交易明细信息

    """

    def __init__(self):
        """
        :param BookingFlag: STRING(2)，记账标志（1: 转出; 2: 转入）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param BookingType: STRING(20)，记账类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingType: str
        :param InSubAcctNo: STRING(50)，转入见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，转出见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param Remark: STRING(300)，备注（返回交易订单号）
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
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


class TransferItem(AbstractModel):
    """转账充值明细信息

    """

    def __init__(self):
        """
        :param InAcctType: STRING(10)，入账类型（02: 会员充值; 03: 资金挂账）
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctType: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranAmt: STRING(20)，入金金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param InAcctNo: STRING(50)，入金账号
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctNo: str
        :param InAcctName: STRING(150)，入金账户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctName: str
        :param Ccy: STRING(3)，币种
注意：此字段可能返回 null，表示取不到有效值。
        :type Ccy: str
        :param AccountingDate: STRING(8)，会计日期（即银行主机记账日期）
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountingDate: str
        :param BankName: STRING(150)，银行名称（付款账户银行名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type BankName: str
        :param Remark: STRING(300)，转账备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        """
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


class UnBindAcctRequest(AbstractModel):
    """UnBindAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见《商户端接口敏感信息加密说明》
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class UnBindAcctResponse(AbstractModel):
    """UnBindAcct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindRelateAcctRequest(AbstractModel):
    """UnbindRelateAcct请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 解绑）
        :type FunctionFlag: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，待解绑的提现账户的账号（提现账号）
        :type MemberAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class UnbindRelateAcctResponse(AbstractModel):
    """UnbindRelateAcct返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param SubMchIncome: 子订单结算应收金额，单位： 分
        :type SubMchIncome: int
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param Amt: 子订单支付金额
        :type Amt: int
        :param Metadata: 发货标识，由业务在调用聚鑫下单接口的 时候下发
        :type Metadata: str
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        """
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


class UnifiedOrderRequest(AbstractModel):
    """UnifiedOrder请求参数结构体

    """

    def __init__(self):
        """
        :param CurrencyType: ISO 货币代码，CNY
        :type CurrencyType: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param OutTradeNo: 支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type OutTradeNo: str
        :param ProductDetail: 商品详情，需要URL编码
        :type ProductDetail: str
        :param ProductId: 商品ID，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type ProductId: str
        :param ProductName: 商品名称，需要URL编码
        :type ProductName: str
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param RealChannel: 银行真实渠道.如:bank_pingan
        :type RealChannel: str
        :param OriginalAmt: 原始金额
        :type OriginalAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param CallbackUrl: Web端回调地址
        :type CallbackUrl: str
        :param Channel: 指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定
        :type Channel: str
        :param Metadata: 透传字段，支付成功回调透传给应用，用于业务透传自定义内容
        :type Metadata: str
        :param Quantity: 购买数量，不传默认为1
        :type Quantity: int
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOrderList: 子订单信息列表，格式：子订单号、子应用ID、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)
注：接入银行或其他支付渠道服务商模式下，必传
        :type SubOrderList: list of UnifiedOrderInSubOrderList
        :param TotalMchIncome: 结算应收金额，单位：分
        :type TotalMchIncome: int
        :param TotalPlatformIncome: 平台应收金额，单位：分
        :type TotalPlatformIncome: int
        :param WxOpenId: 微信公众号/小程序支付时为必选，需要传微信下的openid
        :type WxOpenId: str
        :param WxSubOpenId: 在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一
        :type WxSubOpenId: str
        """
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


class UnifiedOrderResponse(AbstractModel):
    """UnifiedOrder返回参数结构体

    """

    def __init__(self):
        """
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param OutTradeNo: 应用支付订单号
        :type OutTradeNo: str
        :param PayInfo: 支付参数透传给聚鑫SDK（原文透传给SDK即可，不需要解码）
        :type PayInfo: str
        :param TransactionId: 聚鑫的交易订单
        :type TransactionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class WithdrawBill(AbstractModel):
    """聚鑫提现订单内容

    """

    def __init__(self):
        """
        :param WithdrawOrderId: 业务提现订单号
        :type WithdrawOrderId: str
        :param Date: 提现日期
        :type Date: str
        :param PayAmt: 提现金额，单位： 分
        :type PayAmt: str
        :param InSubAppId: 聚鑫分配转入账户appid
        :type InSubAppId: str
        :param OutSubAppId: 聚鑫分配转出账户appid
        :type OutSubAppId: str
        :param CurrencyType: ISO货币代码
        :type CurrencyType: str
        :param MetaData: 透传字段
        :type MetaData: str
        :param ExtendFieldData: 扩展字段
        :type ExtendFieldData: str
        """
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


class WithdrawCashMembershipRequest(AbstractModel):
    """WithdrawCashMembership请求参数结构体

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranWebName: STRING(150)，交易网名称（市场名称）
        :type TranWebName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，会员名称
        :type MemberName: str
        :param TakeCashAcctNo: STRING(50)，提现账号（银行卡）
        :type TakeCashAcctNo: str
        :param OutAmtAcctName: STRING(150)，出金账户名称（银行卡户名）
        :type OutAmtAcctName: str
        :param Ccy: STRING(3)，币种（默认为RMB）
        :type Ccy: str
        :param CashAmt: STRING(20)，可提现金额
        :type CashAmt: str
        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param WebSign: STRING(300)，网银签名
        :type WebSign: str
        """
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


class WithdrawCashMembershipResponse(AbstractModel):
    """WithdrawCashMembership返回参数结构体

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param TransferFee: STRING(20)，转账手续费（固定返回0.00）
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferFee: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param BookingMsg: STRING(200)，记账说明
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingMsg: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctName: STRING(150)，见证子账户的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param Commission: STRING(20)，手续费
注意：此字段可能返回 null，表示取不到有效值。
        :type Commission: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param Remark: STRING(300)，备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
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