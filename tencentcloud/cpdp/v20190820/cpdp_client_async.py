# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.cpdp.v20190820 import models
from typing import Dict


class CpdpClient(AbstractClient):
    _apiVersion = '2019-08-20'
    _endpoint = 'cpdp.tencentcloudapi.com'
    _service = 'cpdp'

    async def AddContract(
            self,
            request: models.AddContractRequest,
            opts: Dict = None,
    ) -> models.AddContractResponse:
        """
        云支付-添加合同接口
        """
        
        kwargs = {}
        kwargs["action"] = "AddContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddFlexFundingAccount(
            self,
            request: models.AddFlexFundingAccountRequest,
            opts: Dict = None,
    ) -> models.AddFlexFundingAccountResponse:
        """
        灵云V2-绑定收款用户资金账号信息
        """
        
        kwargs = {}
        kwargs["action"] = "AddFlexFundingAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddFlexFundingAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddFlexIdInfo(
            self,
            request: models.AddFlexIdInfoRequest,
            opts: Dict = None,
    ) -> models.AddFlexIdInfoResponse:
        """
        灵云V2-补充证件信息
        """
        
        kwargs = {}
        kwargs["action"] = "AddFlexIdInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddFlexIdInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddFlexPhoneNo(
            self,
            request: models.AddFlexPhoneNoRequest,
            opts: Dict = None,
    ) -> models.AddFlexPhoneNoResponse:
        """
        灵云V2-补充手机号信息
        """
        
        kwargs = {}
        kwargs["action"] = "AddFlexPhoneNo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddFlexPhoneNoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddMerchant(
            self,
            request: models.AddMerchantRequest,
            opts: Dict = None,
    ) -> models.AddMerchantResponse:
        """
        云支付-添加商户接口
        """
        
        kwargs = {}
        kwargs["action"] = "AddMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddShop(
            self,
            request: models.AddShopRequest,
            opts: Dict = None,
    ) -> models.AddShopResponse:
        """
        云支付-添加门店接口
        """
        
        kwargs = {}
        kwargs["action"] = "AddShop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddShopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyApplicationMaterial(
            self,
            request: models.ApplyApplicationMaterialRequest,
            opts: Dict = None,
    ) -> models.ApplyApplicationMaterialResponse:
        """
        跨境-提交申报材料。申报材料的主体是付款人，需要提前调用【跨境-付款人申请】接口提交付款人信息且审核通过后调用。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyApplicationMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyApplicationMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyFlexPayment(
            self,
            request: models.ApplyFlexPaymentRequest,
            opts: Dict = None,
    ) -> models.ApplyFlexPaymentResponse:
        """
        灵云V2-付款
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyFlexPayment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyFlexPaymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyFlexSettlement(
            self,
            request: models.ApplyFlexSettlementRequest,
            opts: Dict = None,
    ) -> models.ApplyFlexSettlementResponse:
        """
        灵云V2-结算
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyFlexSettlement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyFlexSettlementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyFlexWechatPreAuth(
            self,
            request: models.ApplyFlexWechatPreAuthRequest,
            opts: Dict = None,
    ) -> models.ApplyFlexWechatPreAuthResponse:
        """
        微工卡开通预核身接口
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyFlexWechatPreAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyFlexWechatPreAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyOpenBankOrderDetailReceipt(
            self,
            request: models.ApplyOpenBankOrderDetailReceiptRequest,
            opts: Dict = None,
    ) -> models.ApplyOpenBankOrderDetailReceiptResponse:
        """
        云企付-申请单笔交易回单
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyOpenBankOrderDetailReceipt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyOpenBankOrderDetailReceiptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyOpenBankSettleOrder(
            self,
            request: models.ApplyOpenBankSettleOrderRequest,
            opts: Dict = None,
    ) -> models.ApplyOpenBankSettleOrderResponse:
        """
        云企付-结算申请接口
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyOpenBankSettleOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyOpenBankSettleOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyOpenBankSubMerchantSignOnline(
            self,
            request: models.ApplyOpenBankSubMerchantSignOnlineRequest,
            opts: Dict = None,
    ) -> models.ApplyOpenBankSubMerchantSignOnlineResponse:
        """
        子商户在线签约
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyOpenBankSubMerchantSignOnline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyOpenBankSubMerchantSignOnlineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyOutwardOrder(
            self,
            request: models.ApplyOutwardOrderRequest,
            opts: Dict = None,
    ) -> models.ApplyOutwardOrderResponse:
        """
        跨境-汇出指令申请。通过该接口可将对接方账户中的人民币余额汇兑成外币，再汇出至指定银行账户。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyOutwardOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyOutwardOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyPayerInfo(
            self,
            request: models.ApplyPayerInfoRequest,
            opts: Dict = None,
    ) -> models.ApplyPayerInfoResponse:
        """
        跨境-付款人申请。通过该接口提交付款人信息并进行 kyc 审核。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyPayerInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyPayerInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyReWithdrawal(
            self,
            request: models.ApplyReWithdrawalRequest,
            opts: Dict = None,
    ) -> models.ApplyReWithdrawalResponse:
        """
        正常结算提现失败情况下，发起重新提现的请求接口
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyReWithdrawal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyReWithdrawalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyReconciliationFile(
            self,
            request: models.ApplyReconciliationFileRequest,
            opts: Dict = None,
    ) -> models.ApplyReconciliationFileResponse:
        """
        聚鑫-申请对账文件
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyReconciliationFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyReconciliationFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyTrade(
            self,
            request: models.ApplyTradeRequest,
            opts: Dict = None,
    ) -> models.ApplyTradeResponse:
        """
        跨境-提交贸易材料。通过提交贸易材料接口可为对接方累计贸易额度，在额度范围内可发起汇兑汇出交易。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyTrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyTradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyWithdrawal(
            self,
            request: models.ApplyWithdrawalRequest,
            opts: Dict = None,
    ) -> models.ApplyWithdrawalResponse:
        """
        商户提现
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyWithdrawal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyWithdrawalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindAccount(
            self,
            request: models.BindAccountRequest,
            opts: Dict = None,
    ) -> models.BindAccountResponse:
        """
        灵云-绑定账号
        """
        
        kwargs = {}
        kwargs["action"] = "BindAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindAcct(
            self,
            request: models.BindAcctRequest,
            opts: Dict = None,
    ) -> models.BindAcctResponse:
        """
        商户绑定提现银行卡，每个商户只能绑定一张提现银行卡
        """
        
        kwargs = {}
        kwargs["action"] = "BindAcct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAcctResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindOpenBankExternalSubMerchantBankAccount(
            self,
            request: models.BindOpenBankExternalSubMerchantBankAccountRequest,
            opts: Dict = None,
    ) -> models.BindOpenBankExternalSubMerchantBankAccountResponse:
        """
        云企付-子商户银行卡绑定
        """
        
        kwargs = {}
        kwargs["action"] = "BindOpenBankExternalSubMerchantBankAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindOpenBankExternalSubMerchantBankAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindOpenBankProfitSharePayee(
            self,
            request: models.BindOpenBankProfitSharePayeeRequest,
            opts: Dict = None,
    ) -> models.BindOpenBankProfitSharePayeeResponse:
        """
        云企付-绑定分账收款方
        """
        
        kwargs = {}
        kwargs["action"] = "BindOpenBankProfitSharePayee"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindOpenBankProfitSharePayeeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindRelateAccReUnionPay(
            self,
            request: models.BindRelateAccReUnionPayRequest,
            opts: Dict = None,
    ) -> models.BindRelateAccReUnionPayResponse:
        """
        会员绑定提现账户-回填银联鉴权短信码。用于会员填写动态验证码后，发往银行进行验证，验证成功则完成绑定。
        """
        
        kwargs = {}
        kwargs["action"] = "BindRelateAccReUnionPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindRelateAccReUnionPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindRelateAcctSmallAmount(
            self,
            request: models.BindRelateAcctSmallAmountRequest,
            opts: Dict = None,
    ) -> models.BindRelateAcctSmallAmountResponse:
        """
        会员绑定提现账户-小额鉴权。会员申请绑定提现账户，绑定后从会员子账户中提现到绑定账户。
        转账鉴权有两种形式：往账鉴权和来账鉴权。
        往账鉴权：该接口发起成功后，银行会向提现账户转入小于等于0.5元的随机金额，并短信通知客户查看，客户查看后，需将收到的金额大小，在电商平台页面上回填，并通知银行。银行验证通过后，完成提现账户绑定。
        来账鉴权：该接口发起成功后，银行以短信通知客户查看，客户查看后，需通过待绑定的账户往市场的监管账户转入短信上指定的金额。银行检索到该笔指定金额的来账是源自待绑定账户，则绑定成功。平安银行的账户，即BankType送1时，大小额行号和超级网银号都不用送。
        """
        
        kwargs = {}
        kwargs["action"] = "BindRelateAcctSmallAmount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindRelateAcctSmallAmountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindRelateAcctUnionPay(
            self,
            request: models.BindRelateAcctUnionPayRequest,
            opts: Dict = None,
    ) -> models.BindRelateAcctUnionPayResponse:
        """
        会员绑定提现账户-银联鉴权。用于会员申请绑定提现账户，申请后银行前往银联验证卡信息：姓名、证件、卡号、银行预留手机是否相符，相符则发送给会员手机动态验证码并返回成功，不相符则返回失败。
        平台接收到银行返回成功后，进入输入动态验证码的页面，有效期120秒，若120秒未输入，客户可点击重新发送动态验证码，这个步骤重新调用该接口即可。
        平安银行的账户，大小额行号和超级网银号都不用送。
        超级网银号：单笔转账金额不超过5万，不限制笔数，只用选XX银行，不用具体到支行，可实时知道对方是否收款成功。
        大小额联行号：单笔转账可超过5万，需具体到支行，不能实时知道对方是否收款成功。金额超过5万的，在工作日的8点30-17点间才会成功。
        """
        
        kwargs = {}
        kwargs["action"] = "BindRelateAcctUnionPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindRelateAcctUnionPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAcct(
            self,
            request: models.CheckAcctRequest,
            opts: Dict = None,
    ) -> models.CheckAcctResponse:
        """
        商户绑定提现银行卡的验证接口
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAcct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAcctResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAmount(
            self,
            request: models.CheckAmountRequest,
            opts: Dict = None,
    ) -> models.CheckAmountResponse:
        """
        验证鉴权金额。此接口可受理BindRelateAcctSmallAmount接口发起的转账金额（往账鉴权方式）的验证处理。若所回填的验证金额验证通过，则会绑定原申请中的银行账户作为提现账户。通过此接口也可以查得BindRelateAcctSmallAmount接口发起的来账鉴权方式的申请的当前状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAmount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAmountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseCloudOrder(
            self,
            request: models.CloseCloudOrderRequest,
            opts: Dict = None,
    ) -> models.CloseCloudOrderResponse:
        """
        通过此接口关闭此前已创建的订单。关闭后，用户将无法继续付款，仅能关闭创建后未支付的订单。
        """
        
        kwargs = {}
        kwargs["action"] = "CloseCloudOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseCloudOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseOpenBankPaymentOrder(
            self,
            request: models.CloseOpenBankPaymentOrderRequest,
            opts: Dict = None,
    ) -> models.CloseOpenBankPaymentOrderResponse:
        """
        云企付-关闭订单
        """
        
        kwargs = {}
        kwargs["action"] = "CloseOpenBankPaymentOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseOpenBankPaymentOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseOrder(
            self,
            request: models.CloseOrderRequest,
            opts: Dict = None,
    ) -> models.CloseOrderResponse:
        """
        通过此接口关闭此前已创建的订单，关闭后，用户将无法继续付款。仅能关闭创建后未支付的订单
        """
        
        kwargs = {}
        kwargs["action"] = "CloseOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmOrder(
            self,
            request: models.ConfirmOrderRequest,
            opts: Dict = None,
    ) -> models.ConfirmOrderResponse:
        """
        云鉴-消费订单确认接口
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ContractOrder(
            self,
            request: models.ContractOrderRequest,
            opts: Dict = None,
    ) -> models.ContractOrderResponse:
        """
        应用需要先带上签约信息调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。
        """
        
        kwargs = {}
        kwargs["action"] = "ContractOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ContractOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAcct(
            self,
            request: models.CreateAcctRequest,
            opts: Dict = None,
    ) -> models.CreateAcctResponse:
        """
        子商户入驻聚鑫平台
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAcct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAcctResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentTaxPaymentInfos(
            self,
            request: models.CreateAgentTaxPaymentInfosRequest,
            opts: Dict = None,
    ) -> models.CreateAgentTaxPaymentInfosResponse:
        """
        直播平台-代理商完税信息录入
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentTaxPaymentInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentTaxPaymentInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAnchor(
            self,
            request: models.CreateAnchorRequest,
            opts: Dict = None,
    ) -> models.CreateAnchorResponse:
        """
        直播平台-主播入驻
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAnchor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAnchorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBatchPayment(
            self,
            request: models.CreateBatchPaymentRequest,
            opts: Dict = None,
    ) -> models.CreateBatchPaymentResponse:
        """
        灵云-批量主播转账接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBatchPayment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBatchPaymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudSubMerchant(
            self,
            request: models.CreateCloudSubMerchantRequest,
            opts: Dict = None,
    ) -> models.CreateCloudSubMerchantResponse:
        """
        创建子商户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudSubMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudSubMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustAcctId(
            self,
            request: models.CreateCustAcctIdRequest,
            opts: Dict = None,
    ) -> models.CreateCustAcctIdResponse:
        """
        会员子账户开立。会员在银行注册，并开立会员子账户，交易网会员代码即会员在平台端系统的会员编号。
        平台需保存银行返回的子账户账号，后续交易接口都会用到。会员属性字段为预留扩展字段，当前必须送默认值。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustAcctId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustAcctIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExternalAnchor(
            self,
            request: models.CreateExternalAnchorRequest,
            opts: Dict = None,
    ) -> models.CreateExternalAnchorResponse:
        """
        灵云-主播入驻
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExternalAnchor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExternalAnchorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFlexPayee(
            self,
            request: models.CreateFlexPayeeRequest,
            opts: Dict = None,
    ) -> models.CreateFlexPayeeResponse:
        """
        灵云V2-收款用户开立
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlexPayee"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlexPayeeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInvoice(
            self,
            request: models.CreateInvoiceRequest,
            opts: Dict = None,
    ) -> models.CreateInvoiceResponse:
        """
        智慧零售-发票开具
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInvoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInvoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInvoiceV2(
            self,
            request: models.CreateInvoiceV2Request,
            opts: Dict = None,
    ) -> models.CreateInvoiceV2Response:
        """
        智慧零售-发票开具V2
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInvoiceV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInvoiceV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMerchant(
            self,
            request: models.CreateMerchantRequest,
            opts: Dict = None,
    ) -> models.CreateMerchantResponse:
        """
        智慧零售-商户注册
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankAggregatedSubMerchantRegistration(
            self,
            request: models.CreateOpenBankAggregatedSubMerchantRegistrationRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankAggregatedSubMerchantRegistrationResponse:
        """
        云企付-子商户进件V2
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankAggregatedSubMerchantRegistration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankAggregatedSubMerchantRegistrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankExternalSubMerchantAccountBook(
            self,
            request: models.CreateOpenBankExternalSubMerchantAccountBookRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankExternalSubMerchantAccountBookResponse:
        """
        第三方子商户电子记账本创建接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankExternalSubMerchantAccountBook"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankExternalSubMerchantAccountBookResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankExternalSubMerchantRegistration(
            self,
            request: models.CreateOpenBankExternalSubMerchantRegistrationRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankExternalSubMerchantRegistrationResponse:
        """
        云企付-子商户进件
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankExternalSubMerchantRegistration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankExternalSubMerchantRegistrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankGlobalPaymentOrder(
            self,
            request: models.CreateOpenBankGlobalPaymentOrderRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankGlobalPaymentOrderResponse:
        """
        云企付-跨境支付下单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankGlobalPaymentOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankGlobalPaymentOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankMerchant(
            self,
            request: models.CreateOpenBankMerchantRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankMerchantResponse:
        """
        云企付-创建商户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankPaymentOrder(
            self,
            request: models.CreateOpenBankPaymentOrderRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankPaymentOrderResponse:
        """
        云企付-创建支付订单。支持B2B网关支付，B2C转账下单。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankPaymentOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankPaymentOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankRechargeOrder(
            self,
            request: models.CreateOpenBankRechargeOrderRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankRechargeOrderResponse:
        """
        云企付-创建充值订单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankRechargeOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankRechargeOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankSubMerchantRateConfigure(
            self,
            request: models.CreateOpenBankSubMerchantRateConfigureRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankSubMerchantRateConfigureResponse:
        """
        云企付-子商户费率配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankSubMerchantRateConfigure"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankSubMerchantRateConfigureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankUnifiedOrder(
            self,
            request: models.CreateOpenBankUnifiedOrderRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankUnifiedOrderResponse:
        """
        云企付-聚合下单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankUnifiedOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankUnifiedOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpenBankVerificationOrder(
            self,
            request: models.CreateOpenBankVerificationOrderRequest,
            opts: Dict = None,
    ) -> models.CreateOpenBankVerificationOrderResponse:
        """
        云企付-创建核销申请，适用于针对支付订单维度的确认收货，解冻等业务场景。目前支持的渠道有TENPAY下的EBANK_PAYMENT付款方式创建支付订单时，选择担保支付下单的订单进行解冻。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpenBankVerificationOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpenBankVerificationOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrder(
            self,
            request: models.CreateOrderRequest,
            opts: Dict = None,
    ) -> models.CreateOrderResponse:
        """
        云鉴-消费订单发起的接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePayMerchant(
            self,
            request: models.CreatePayMerchantRequest,
            opts: Dict = None,
    ) -> models.CreatePayMerchantResponse:
        """
        商户新增的接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePayMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePayMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePayRollPreOrder(
            self,
            request: models.CreatePayRollPreOrderRequest,
            opts: Dict = None,
    ) -> models.CreatePayRollPreOrderResponse:
        """
        务工卡-核身预下单
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePayRollPreOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePayRollPreOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePayRollPreOrderWithAuth(
            self,
            request: models.CreatePayRollPreOrderWithAuthRequest,
            opts: Dict = None,
    ) -> models.CreatePayRollPreOrderWithAuthResponse:
        """
        务工卡-核身预下单带授权
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePayRollPreOrderWithAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePayRollPreOrderWithAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePayRollToken(
            self,
            request: models.CreatePayRollTokenRequest,
            opts: Dict = None,
    ) -> models.CreatePayRollTokenResponse:
        """
        务工卡-生成授权令牌
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePayRollToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePayRollTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRedInvoice(
            self,
            request: models.CreateRedInvoiceRequest,
            opts: Dict = None,
    ) -> models.CreateRedInvoiceResponse:
        """
        智慧零售-发票红冲
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRedInvoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRedInvoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRedInvoiceV2(
            self,
            request: models.CreateRedInvoiceV2Request,
            opts: Dict = None,
    ) -> models.CreateRedInvoiceV2Response:
        """
        智慧零售-发票红冲V2
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRedInvoiceV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRedInvoiceV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSinglePayment(
            self,
            request: models.CreateSinglePaymentRequest,
            opts: Dict = None,
    ) -> models.CreateSinglePaymentResponse:
        """
        灵云-单笔主播转账接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSinglePayment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSinglePaymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTransferBatch(
            self,
            request: models.CreateTransferBatchRequest,
            opts: Dict = None,
    ) -> models.CreateTransferBatchResponse:
        """
        微信商户发起批量转账
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTransferBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTransferBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeduceQuota(
            self,
            request: models.DeduceQuotaRequest,
            opts: Dict = None,
    ) -> models.DeduceQuotaResponse:
        """
        直播平台-扣减额度
        """
        
        kwargs = {}
        kwargs["action"] = "DeduceQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeduceQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgentTaxPaymentInfo(
            self,
            request: models.DeleteAgentTaxPaymentInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentTaxPaymentInfoResponse:
        """
        直播平台-删除代理商完税信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgentTaxPaymentInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentTaxPaymentInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgentTaxPaymentInfos(
            self,
            request: models.DeleteAgentTaxPaymentInfosRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentTaxPaymentInfosResponse:
        """
        直播平台-删除代理商完税信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgentTaxPaymentInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentTaxPaymentInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChargeDetail(
            self,
            request: models.DescribeChargeDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeChargeDetailResponse:
        """
        查询充值明细接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChargeDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChargeDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrderStatus(
            self,
            request: models.DescribeOrderStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeOrderStatusResponse:
        """
        查询单笔订单交易状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrderStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrderStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeAccreditQuery(
            self,
            request: models.DistributeAccreditQueryRequest,
            opts: Dict = None,
    ) -> models.DistributeAccreditQueryResponse:
        """
        云支付-分账授权申请查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeAccreditQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeAccreditQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeAccreditTlinx(
            self,
            request: models.DistributeAccreditTlinxRequest,
            opts: Dict = None,
    ) -> models.DistributeAccreditTlinxResponse:
        """
        云支付-分账授权申请接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeAccreditTlinx"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeAccreditTlinxResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeAddReceiver(
            self,
            request: models.DistributeAddReceiverRequest,
            opts: Dict = None,
    ) -> models.DistributeAddReceiverResponse:
        """
        云支付-分账添加分账接收方接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeAddReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeAddReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeApply(
            self,
            request: models.DistributeApplyRequest,
            opts: Dict = None,
    ) -> models.DistributeApplyResponse:
        """
        云支付-分账请求接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeCancel(
            self,
            request: models.DistributeCancelRequest,
            opts: Dict = None,
    ) -> models.DistributeCancelResponse:
        """
        云支付-分账撤销接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeCancel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeCancelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeQuery(
            self,
            request: models.DistributeQueryRequest,
            opts: Dict = None,
    ) -> models.DistributeQueryResponse:
        """
        云支付-分账结果查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeQueryReceiver(
            self,
            request: models.DistributeQueryReceiverRequest,
            opts: Dict = None,
    ) -> models.DistributeQueryReceiverResponse:
        """
        云支付-查询已添加分账接收方接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeQueryReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeQueryReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeRemoveReceiver(
            self,
            request: models.DistributeRemoveReceiverRequest,
            opts: Dict = None,
    ) -> models.DistributeRemoveReceiverResponse:
        """
        云支付-分账解除分账接收方接口
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeRemoveReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeRemoveReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadBill(
            self,
            request: models.DownloadBillRequest,
            opts: Dict = None,
    ) -> models.DownloadBillResponse:
        """
        账单下载接口，根据本接口返回的URL地址，在D+1日下载对账单。注意，本接口返回的URL地址有时效，请尽快下载。URL超时时效后，请重新调用本接口再次获取。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadBill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadBillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadOrgFile(
            self,
            request: models.DownloadOrgFileRequest,
            opts: Dict = None,
    ) -> models.DownloadOrgFileResponse:
        """
        云支付-下载机构文件接口
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadOrgFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadOrgFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadReconciliationUrl(
            self,
            request: models.DownloadReconciliationUrlRequest,
            opts: Dict = None,
    ) -> models.DownloadReconciliationUrlResponse:
        """
        获取对账中心账单下载地址的接口
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadReconciliationUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadReconciliationUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteMemberTransaction(
            self,
            request: models.ExecuteMemberTransactionRequest,
            opts: Dict = None,
    ) -> models.ExecuteMemberTransactionResponse:
        """
        会员间交易接口
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteMemberTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteMemberTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreezeFlexBalance(
            self,
            request: models.FreezeFlexBalanceRequest,
            opts: Dict = None,
    ) -> models.FreezeFlexBalanceResponse:
        """
        灵云V2-冻结余额
        """
        
        kwargs = {}
        kwargs["action"] = "FreezeFlexBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreezeFlexBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetBillDownloadUrl(
            self,
            request: models.GetBillDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.GetBillDownloadUrlResponse:
        """
        调用该接口返回对账单下载地址，对账单下载URL通过GET方式访问，返回zip包，解压后为csv格式文件。文件首行如下：
        订单号,订单归属日期,机构编号,订单描述,交易类型,订单状态,支付场景,原始金额,折扣金额,实际交易金额,支付渠道优惠金额,抹零金额,币种,下单时间,付款成功时间,商户编号,门店编号,付款方式编号,付款方式名称,商户手续费T1,商户扣率,是否信用卡交易,原始订单号,用户账号,外部订单号,订单备注
        """
        
        kwargs = {}
        kwargs["action"] = "GetBillDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetBillDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDistributeBillDownloadUrl(
            self,
            request: models.GetDistributeBillDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.GetDistributeBillDownloadUrlResponse:
        """
        调用该接口返回对账单下载地址，对账单下载URL通过GET方式访问，返回zip包，解压后为csv格式文件。文件首行如下：
        商户号,订单号,支付订单号,分账订单总金额,分账详情（通过|分割每笔明细：商户号1#分账金额1|商户号2#分账金额2）,交易手续费承担方商户号,交易手续费,发起时间,分账状态,结算日期,非交易主体分账金额,商户退款订单号,商户分账单号
        """
        
        kwargs = {}
        kwargs["action"] = "GetDistributeBillDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDistributeBillDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPayRollAuth(
            self,
            request: models.GetPayRollAuthRequest,
            opts: Dict = None,
    ) -> models.GetPayRollAuthResponse:
        """
        务工卡-查询授权关系
        """
        
        kwargs = {}
        kwargs["action"] = "GetPayRollAuth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPayRollAuthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPayRollAuthList(
            self,
            request: models.GetPayRollAuthListRequest,
            opts: Dict = None,
    ) -> models.GetPayRollAuthListResponse:
        """
        务工卡-查询核身记录
        """
        
        kwargs = {}
        kwargs["action"] = "GetPayRollAuthList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPayRollAuthListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPayRollAuthResult(
            self,
            request: models.GetPayRollAuthResultRequest,
            opts: Dict = None,
    ) -> models.GetPayRollAuthResultResponse:
        """
        务工卡-获取核身结果
        """
        
        kwargs = {}
        kwargs["action"] = "GetPayRollAuthResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPayRollAuthResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateOrderRefund(
            self,
            request: models.MigrateOrderRefundRequest,
            opts: Dict = None,
    ) -> models.MigrateOrderRefundResponse:
        """
        山姆聚合支付项目-存量订单退款接口。可以通过本接口将支付款全部或部分退还给付款方，在收到用户退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付账号。
        """
        
        kwargs = {}
        kwargs["action"] = "MigrateOrderRefund"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigrateOrderRefundResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateOrderRefundQuery(
            self,
            request: models.MigrateOrderRefundQueryRequest,
            opts: Dict = None,
    ) -> models.MigrateOrderRefundQueryResponse:
        """
        提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时。
        """
        
        kwargs = {}
        kwargs["action"] = "MigrateOrderRefundQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigrateOrderRefundQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentTaxPaymentInfo(
            self,
            request: models.ModifyAgentTaxPaymentInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentTaxPaymentInfoResponse:
        """
        直播平台-修改代理商完税信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentTaxPaymentInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentTaxPaymentInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBindedAccount(
            self,
            request: models.ModifyBindedAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyBindedAccountResponse:
        """
        灵云-重新绑定账号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBindedAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBindedAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFlexFundingAccount(
            self,
            request: models.ModifyFlexFundingAccountRequest,
            opts: Dict = None,
    ) -> models.ModifyFlexFundingAccountResponse:
        """
        灵云V2-修改收款用户资金账号信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFlexFundingAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFlexFundingAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFlexPayeeAccountRightStatus(
            self,
            request: models.ModifyFlexPayeeAccountRightStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyFlexPayeeAccountRightStatusResponse:
        """
        灵云V2-收款用户账户权益状态修改
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFlexPayeeAccountRightStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFlexPayeeAccountRightStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMerchant(
            self,
            request: models.ModifyMerchantRequest,
            opts: Dict = None,
    ) -> models.ModifyMerchantResponse:
        """
        云鉴-商户信息修改的接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMntMbrBindRelateAcctBankCode(
            self,
            request: models.ModifyMntMbrBindRelateAcctBankCodeRequest,
            opts: Dict = None,
    ) -> models.ModifyMntMbrBindRelateAcctBankCodeResponse:
        """
        维护会员绑定提现账户联行号。此接口可以支持市场修改会员的提现账户的开户行信息，具体包括开户行行名、开户行的银行联行号（大小额联行号）和超级网银行号。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMntMbrBindRelateAcctBankCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMntMbrBindRelateAcctBankCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAcctBinding(
            self,
            request: models.QueryAcctBindingRequest,
            opts: Dict = None,
    ) -> models.QueryAcctBindingResponse:
        """
        聚鑫-查询子账户绑定银行卡
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAcctBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAcctBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAcctInfo(
            self,
            request: models.QueryAcctInfoRequest,
            opts: Dict = None,
    ) -> models.QueryAcctInfoResponse:
        """
        聚鑫-开户信息查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAcctInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAcctInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAcctInfoList(
            self,
            request: models.QueryAcctInfoListRequest,
            opts: Dict = None,
    ) -> models.QueryAcctInfoListResponse:
        """
        聚鑫-开户信息列表查询, 查询某一段时间的开户信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAcctInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAcctInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAgentStatements(
            self,
            request: models.QueryAgentStatementsRequest,
            opts: Dict = None,
    ) -> models.QueryAgentStatementsResponse:
        """
        直播平台-查询代理商结算单链接
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAgentStatements"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAgentStatementsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAgentTaxPaymentBatch(
            self,
            request: models.QueryAgentTaxPaymentBatchRequest,
            opts: Dict = None,
    ) -> models.QueryAgentTaxPaymentBatchResponse:
        """
        直播平台-查询批次信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAgentTaxPaymentBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAgentTaxPaymentBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAnchorContractInfo(
            self,
            request: models.QueryAnchorContractInfoRequest,
            opts: Dict = None,
    ) -> models.QueryAnchorContractInfoResponse:
        """
        直播平台-查询主播签约信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAnchorContractInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAnchorContractInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryApplicationMaterial(
            self,
            request: models.QueryApplicationMaterialRequest,
            opts: Dict = None,
    ) -> models.QueryApplicationMaterialResponse:
        """
        跨境-成功申报材料查询。查询成功入库的申报材料。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryApplicationMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryApplicationMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryAssignment(
            self,
            request: models.QueryAssignmentRequest,
            opts: Dict = None,
    ) -> models.QueryAssignmentResponse:
        """
        直播平台-查询分配关系
        """
        
        kwargs = {}
        kwargs["action"] = "QueryAssignment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryAssignmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryBalance(
            self,
            request: models.QueryBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryBalanceResponse:
        """
        子商户余额查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryBankClear(
            self,
            request: models.QueryBankClearRequest,
            opts: Dict = None,
    ) -> models.QueryBankClearResponse:
        """
        查询银行在途清算结果。查询时间段内交易网的在途清算结果。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryBankClear"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryBankClearResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryBankTransactionDetails(
            self,
            request: models.QueryBankTransactionDetailsRequest,
            opts: Dict = None,
    ) -> models.QueryBankTransactionDetailsResponse:
        """
        查询银行时间段内交易明细。查询时间段的会员成功交易。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryBankTransactionDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryBankTransactionDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryBankWithdrawCashDetails(
            self,
            request: models.QueryBankWithdrawCashDetailsRequest,
            opts: Dict = None,
    ) -> models.QueryBankWithdrawCashDetailsResponse:
        """
        查询银行时间段内清分提现明细。查询银行时间段内清分提现明细接口：若为“见证+收单退款”“见证+收单充值”记录时备注Note为“见证+收单充值,订单号”“见证+收单退款,订单号”，此接口可以查到T0/T1的充值明细和退款记录。查询标志：充值记录仍用3清分选项查询，退款记录同提现用2选项查询。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryBankWithdrawCashDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryBankWithdrawCashDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryBatchPaymentResult(
            self,
            request: models.QueryBatchPaymentResultRequest,
            opts: Dict = None,
    ) -> models.QueryBatchPaymentResultResponse:
        """
        灵云-批量转账结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryBatchPaymentResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryBatchPaymentResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryBillDownloadURL(
            self,
            request: models.QueryBillDownloadURLRequest,
            opts: Dict = None,
    ) -> models.QueryBillDownloadURLResponse:
        """
        获取单笔代发转账对账单下载URL
        """
        
        kwargs = {}
        kwargs["action"] = "QueryBillDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryBillDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCityCode(
            self,
            request: models.QueryCityCodeRequest,
            opts: Dict = None,
    ) -> models.QueryCityCodeResponse:
        """
        云支付-查询城市编码接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCityCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCityCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCloudChannelData(
            self,
            request: models.QueryCloudChannelDataRequest,
            opts: Dict = None,
    ) -> models.QueryCloudChannelDataResponse:
        """
        发起支付等渠道操作后，可以调用该接口查询渠道的数据。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCloudChannelData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCloudChannelDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCloudOrder(
            self,
            request: models.QueryCloudOrderRequest,
            opts: Dict = None,
    ) -> models.QueryCloudOrderResponse:
        """
        根据订单号或用户ID，查询支付订单状态。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCloudOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCloudOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCloudRefundOrder(
            self,
            request: models.QueryCloudRefundOrderRequest,
            opts: Dict = None,
    ) -> models.QueryCloudRefundOrderResponse:
        """
        提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时，用微信零钱支付的退款约20分钟内到账，银行卡支付的退款约3个工作日后到账。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCloudRefundOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCloudRefundOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCommonTransferRecharge(
            self,
            request: models.QueryCommonTransferRechargeRequest,
            opts: Dict = None,
    ) -> models.QueryCommonTransferRechargeResponse:
        """
        查询普通转账充值明细。接口用于查询会员主动转账进资金汇总账户的明细情况。若会员使用绑定账号转入，则直接入账到会员子账户。若未使用绑定账号转入，则系统无法自动清分到对应子账户，则转入挂账子账户由平台自行清分。若是 “见证+收单充值”T0充值记录时备注Note为“见证+收单充值,订单号” 此接口可以查到T0到账的“见证+收单充值”充值记录。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCommonTransferRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCommonTransferRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCompanyTitle(
            self,
            request: models.QueryCompanyTitleRequest,
            opts: Dict = None,
    ) -> models.QueryCompanyTitleResponse:
        """
        智慧零售-查询公司抬头
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCompanyTitle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCompanyTitleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryContract(
            self,
            request: models.QueryContractRequest,
            opts: Dict = None,
    ) -> models.QueryContractResponse:
        """
        通过此接口查询签约数据
        """
        
        kwargs = {}
        kwargs["action"] = "QueryContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryContractPayFee(
            self,
            request: models.QueryContractPayFeeRequest,
            opts: Dict = None,
    ) -> models.QueryContractPayFeeResponse:
        """
        云支付-查询支付方式费率及自定义表单项接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryContractPayFee"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryContractPayFeeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryContractPayWayList(
            self,
            request: models.QueryContractPayWayListRequest,
            opts: Dict = None,
    ) -> models.QueryContractPayWayListResponse:
        """
        云支付-查询合同支付方式列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryContractPayWayList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryContractPayWayListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryContractRelateShop(
            self,
            request: models.QueryContractRelateShopRequest,
            opts: Dict = None,
    ) -> models.QueryContractRelateShopResponse:
        """
        云支付-查询合同可关联门店接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryContractRelateShop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryContractRelateShopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCustAcctIdBalance(
            self,
            request: models.QueryCustAcctIdBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryCustAcctIdBalanceResponse:
        """
        查询银行子账户余额。查询会员子账户以及平台的功能子账户的余额。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCustAcctIdBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCustAcctIdBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryDownloadBillURL(
            self,
            request: models.QueryDownloadBillURLRequest,
            opts: Dict = None,
    ) -> models.QueryDownloadBillURLResponse:
        """
        云鉴-查询对账单下载地址的接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryDownloadBillURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryDownloadBillURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryExceedingInfo(
            self,
            request: models.QueryExceedingInfoRequest,
            opts: Dict = None,
    ) -> models.QueryExceedingInfoResponse:
        """
        灵云-查询超额信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryExceedingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryExceedingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryExchangeRate(
            self,
            request: models.QueryExchangeRateRequest,
            opts: Dict = None,
    ) -> models.QueryExchangeRateResponse:
        """
        跨境-查询汇率
        """
        
        kwargs = {}
        kwargs["action"] = "QueryExchangeRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryExchangeRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFinancialDataUrl(
            self,
            request: models.QueryFinancialDataUrlRequest,
            opts: Dict = None,
    ) -> models.QueryFinancialDataUrlResponse:
        """
        财税-查询金融数据文件下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFinancialDataUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFinancialDataUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexAmountBeforeTax(
            self,
            request: models.QueryFlexAmountBeforeTaxRequest,
            opts: Dict = None,
    ) -> models.QueryFlexAmountBeforeTaxResponse:
        """
        灵云V2-查询税前金额
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexAmountBeforeTax"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexAmountBeforeTaxResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexBillDownloadUrl(
            self,
            request: models.QueryFlexBillDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.QueryFlexBillDownloadUrlResponse:
        """
        灵云V2-查询对账单文件下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexBillDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexBillDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexFreezeOrderList(
            self,
            request: models.QueryFlexFreezeOrderListRequest,
            opts: Dict = None,
    ) -> models.QueryFlexFreezeOrderListResponse:
        """
        灵云V2-查询冻结订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexFreezeOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexFreezeOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexOrderSummaryList(
            self,
            request: models.QueryFlexOrderSummaryListRequest,
            opts: Dict = None,
    ) -> models.QueryFlexOrderSummaryListResponse:
        """
        灵云V2-订单汇总列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexOrderSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexOrderSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexPayeeAccountBalance(
            self,
            request: models.QueryFlexPayeeAccountBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryFlexPayeeAccountBalanceResponse:
        """
        灵云V2-收款用户账户余额查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexPayeeAccountBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexPayeeAccountBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexPayeeAccountInfo(
            self,
            request: models.QueryFlexPayeeAccountInfoRequest,
            opts: Dict = None,
    ) -> models.QueryFlexPayeeAccountInfoResponse:
        """
        灵云V2-收款用户账户信息查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexPayeeAccountInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexPayeeAccountInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexPayeeAccountList(
            self,
            request: models.QueryFlexPayeeAccountListRequest,
            opts: Dict = None,
    ) -> models.QueryFlexPayeeAccountListResponse:
        """
        灵云V2-收款用户账户列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexPayeeAccountList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexPayeeAccountListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexPayeeInfo(
            self,
            request: models.QueryFlexPayeeInfoRequest,
            opts: Dict = None,
    ) -> models.QueryFlexPayeeInfoResponse:
        """
        灵云V2-收款用户信息查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexPayeeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexPayeeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexPaymentOrderList(
            self,
            request: models.QueryFlexPaymentOrderListRequest,
            opts: Dict = None,
    ) -> models.QueryFlexPaymentOrderListResponse:
        """
        灵云V2-查询付款订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexPaymentOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexPaymentOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexPaymentOrderStatus(
            self,
            request: models.QueryFlexPaymentOrderStatusRequest,
            opts: Dict = None,
    ) -> models.QueryFlexPaymentOrderStatusResponse:
        """
        灵云V2-查询付款订单状态
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexPaymentOrderStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexPaymentOrderStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexPlatformAccountBalance(
            self,
            request: models.QueryFlexPlatformAccountBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryFlexPlatformAccountBalanceResponse:
        """
        灵云V2-平台账户余额查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexPlatformAccountBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexPlatformAccountBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexServiceProviderAccountBalance(
            self,
            request: models.QueryFlexServiceProviderAccountBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryFlexServiceProviderAccountBalanceResponse:
        """
        灵云V2-查询服务商账户余额
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexServiceProviderAccountBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexServiceProviderAccountBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexSettlementOrderList(
            self,
            request: models.QueryFlexSettlementOrderListRequest,
            opts: Dict = None,
    ) -> models.QueryFlexSettlementOrderListResponse:
        """
        灵云V2-查询结算订单列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexSettlementOrderList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexSettlementOrderListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFlexWechatAuthResult(
            self,
            request: models.QueryFlexWechatAuthResultRequest,
            opts: Dict = None,
    ) -> models.QueryFlexWechatAuthResultResponse:
        """
        查询微工卡核身结果
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFlexWechatAuthResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFlexWechatAuthResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFundsTransactionDetails(
            self,
            request: models.QueryFundsTransactionDetailsRequest,
            opts: Dict = None,
    ) -> models.QueryFundsTransactionDetailsResponse:
        """
        聚鑫-查询会员资金交易信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFundsTransactionDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFundsTransactionDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryInvoice(
            self,
            request: models.QueryInvoiceRequest,
            opts: Dict = None,
    ) -> models.QueryInvoiceResponse:
        """
        智慧零售-发票查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryInvoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryInvoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryInvoiceV2(
            self,
            request: models.QueryInvoiceV2Request,
            opts: Dict = None,
    ) -> models.QueryInvoiceV2Response:
        """
        智慧零售-发票查询V2
        """
        
        kwargs = {}
        kwargs["action"] = "QueryInvoiceV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryInvoiceV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMaliciousRegistration(
            self,
            request: models.QueryMaliciousRegistrationRequest,
            opts: Dict = None,
    ) -> models.QueryMaliciousRegistrationResponse:
        """
        商户恶意注册接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMaliciousRegistration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMaliciousRegistrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMemberBind(
            self,
            request: models.QueryMemberBindRequest,
            opts: Dict = None,
    ) -> models.QueryMemberBindResponse:
        """
        会员绑定信息查询。查询标志为“单个会员”的情况下，返回该会员的有效的绑定账户信息。
        查询标志为“全部会员”的情况下，返回市场下的全部的有效的绑定账户信息。查询标志为“单个会员的证件信息”的情况下，返回市场下的指定的会员的留存在电商见证宝系统的证件信息。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMemberBind"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMemberBindResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMemberTransaction(
            self,
            request: models.QueryMemberTransactionRequest,
            opts: Dict = None,
    ) -> models.QueryMemberTransactionResponse:
        """
        会员间交易-不验证。此接口可以实现会员间的余额的交易，实现资金在会员之间流动。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMemberTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMemberTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMemberTransactionDetails(
            self,
            request: models.QueryMemberTransactionDetailsRequest,
            opts: Dict = None,
    ) -> models.QueryMemberTransactionDetailsResponse:
        """
        聚鑫-查询会员间交易信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMemberTransactionDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMemberTransactionDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMerchant(
            self,
            request: models.QueryMerchantRequest,
            opts: Dict = None,
    ) -> models.QueryMerchantResponse:
        """
        云鉴-商户信息查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMerchantBalance(
            self,
            request: models.QueryMerchantBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryMerchantBalanceResponse:
        """
        跨境-对接方账户余额查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMerchantBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMerchantBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMerchantClassification(
            self,
            request: models.QueryMerchantClassificationRequest,
            opts: Dict = None,
    ) -> models.QueryMerchantClassificationResponse:
        """
        云支付-查询商户分类接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMerchantClassification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMerchantClassificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMerchantInfoForManagement(
            self,
            request: models.QueryMerchantInfoForManagementRequest,
            opts: Dict = None,
    ) -> models.QueryMerchantInfoForManagementResponse:
        """
        智慧零售-查询管理端商户
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMerchantInfoForManagement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMerchantInfoForManagementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMerchantOrder(
            self,
            request: models.QueryMerchantOrderRequest,
            opts: Dict = None,
    ) -> models.QueryMerchantOrderResponse:
        """
        云鉴-消费订单查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMerchantOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMerchantOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMerchantPayWayList(
            self,
            request: models.QueryMerchantPayWayListRequest,
            opts: Dict = None,
    ) -> models.QueryMerchantPayWayListResponse:
        """
        商户查询已开通的支付方式列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMerchantPayWayList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMerchantPayWayListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankBankAccountBalance(
            self,
            request: models.QueryOpenBankBankAccountBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankBankAccountBalanceResponse:
        """
        云企付-子商户银行卡余额查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankBankAccountBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankBankAccountBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankBankBranchList(
            self,
            request: models.QueryOpenBankBankBranchListRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankBankBranchListResponse:
        """
        云企付-查询联行号
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankBankBranchList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankBankBranchListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankBillDataPage(
            self,
            request: models.QueryOpenBankBillDataPageRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankBillDataPageResponse:
        """
        云企付-分页查询对账单数据
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankBillDataPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankBillDataPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankBindExternalSubMerchantBankAccount(
            self,
            request: models.QueryOpenBankBindExternalSubMerchantBankAccountRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankBindExternalSubMerchantBankAccountResponse:
        """
        云企付-子商户银行卡绑定结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankBindExternalSubMerchantBankAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankBindExternalSubMerchantBankAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankDailyReceiptDownloadUrl(
            self,
            request: models.QueryOpenBankDailyReceiptDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankDailyReceiptDownloadUrlResponse:
        """
        云企付-按日期批量查询回单下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankDailyReceiptDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankDailyReceiptDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankDownLoadUrl(
            self,
            request: models.QueryOpenBankDownLoadUrlRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankDownLoadUrlResponse:
        """
        云企付-查询对账单下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankDownLoadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankDownLoadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankExternalSubAccountBookBalance(
            self,
            request: models.QueryOpenBankExternalSubAccountBookBalanceRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankExternalSubAccountBookBalanceResponse:
        """
        第三方子商户电子记账本余额查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankExternalSubAccountBookBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankExternalSubAccountBookBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankExternalSubMerchantBankAccount(
            self,
            request: models.QueryOpenBankExternalSubMerchantBankAccountRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankExternalSubMerchantBankAccountResponse:
        """
        云企付-子商户银行卡列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankExternalSubMerchantBankAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankExternalSubMerchantBankAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankExternalSubMerchantRegistration(
            self,
            request: models.QueryOpenBankExternalSubMerchantRegistrationRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankExternalSubMerchantRegistrationResponse:
        """
        云企付-子商户进件结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankExternalSubMerchantRegistration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankExternalSubMerchantRegistrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankOrderDetailReceiptInfo(
            self,
            request: models.QueryOpenBankOrderDetailReceiptInfoRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankOrderDetailReceiptInfoResponse:
        """
        云企付-单笔交易回单申请结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankOrderDetailReceiptInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankOrderDetailReceiptInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankPaymentOrder(
            self,
            request: models.QueryOpenBankPaymentOrderRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankPaymentOrderResponse:
        """
        云企付-查询订单支付结果
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankPaymentOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankPaymentOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankProfitSharePayee(
            self,
            request: models.QueryOpenBankProfitSharePayeeRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankProfitSharePayeeResponse:
        """
        云企付-绑定分账收款方查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankProfitSharePayee"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankProfitSharePayeeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankRefundOrder(
            self,
            request: models.QueryOpenBankRefundOrderRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankRefundOrderResponse:
        """
        云企付-退款结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankRefundOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankRefundOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankSettleOrder(
            self,
            request: models.QueryOpenBankSettleOrderRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankSettleOrderResponse:
        """
        云企付-结算单查询结果
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankSettleOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankSettleOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankSubMerchantCredential(
            self,
            request: models.QueryOpenBankSubMerchantCredentialRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankSubMerchantCredentialResponse:
        """
        云企付-子商户资质文件查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankSubMerchantCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankSubMerchantCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankSubMerchantRateConfigure(
            self,
            request: models.QueryOpenBankSubMerchantRateConfigureRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankSubMerchantRateConfigureResponse:
        """
        云企付-子商户费率配置结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankSubMerchantRateConfigure"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankSubMerchantRateConfigureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankSubMerchantSignOnline(
            self,
            request: models.QueryOpenBankSubMerchantSignOnlineRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankSubMerchantSignOnlineResponse:
        """
        子商户在线签约查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankSubMerchantSignOnline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankSubMerchantSignOnlineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankSupportBankList(
            self,
            request: models.QueryOpenBankSupportBankListRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankSupportBankListResponse:
        """
        云企付-查询支持银行列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankSupportBankList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankSupportBankListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankUnbindExternalSubMerchantBankAccount(
            self,
            request: models.QueryOpenBankUnbindExternalSubMerchantBankAccountRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankUnbindExternalSubMerchantBankAccountResponse:
        """
        云企付-子商户银行卡解绑结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankUnbindExternalSubMerchantBankAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankUnbindExternalSubMerchantBankAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOpenBankVerificationOrder(
            self,
            request: models.QueryOpenBankVerificationOrderRequest,
            opts: Dict = None,
    ) -> models.QueryOpenBankVerificationOrderResponse:
        """
        云企付-查询核销订单状态，客户可以使用该接口来查询核销申请的订单状态。目前仅支持TENPAY渠道EBANK_PAYMENT付款方式的担保支付订单查询。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOpenBankVerificationOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOpenBankVerificationOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOrder(
            self,
            request: models.QueryOrderRequest,
            opts: Dict = None,
    ) -> models.QueryOrderResponse:
        """
        根据订单号，或者用户Id，查询支付订单状态
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOrderStatus(
            self,
            request: models.QueryOrderStatusRequest,
            opts: Dict = None,
    ) -> models.QueryOrderStatusResponse:
        """
        云支付-查询订单付款状态
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOrderStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOrderStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryOutwardOrder(
            self,
            request: models.QueryOutwardOrderRequest,
            opts: Dict = None,
    ) -> models.QueryOutwardOrderResponse:
        """
        跨境-查询汇出结果
        """
        
        kwargs = {}
        kwargs["action"] = "QueryOutwardOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryOutwardOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryPayerInfo(
            self,
            request: models.QueryPayerInfoRequest,
            opts: Dict = None,
    ) -> models.QueryPayerInfoResponse:
        """
        跨境-付款人查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryPayerInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryPayerInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryReconciliationDocument(
            self,
            request: models.QueryReconciliationDocumentRequest,
            opts: Dict = None,
    ) -> models.QueryReconciliationDocumentResponse:
        """
        查询对账文件信息。平台调用该接口获取需下载对账文件的文件名称以及密钥。 平台获取到信息后， 可以再调用OPENAPI的文件下载功能。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryReconciliationDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryReconciliationDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryReconciliationFileApplyInfo(
            self,
            request: models.QueryReconciliationFileApplyInfoRequest,
            opts: Dict = None,
    ) -> models.QueryReconciliationFileApplyInfoResponse:
        """
        聚鑫-查询对账文件申请结果
        """
        
        kwargs = {}
        kwargs["action"] = "QueryReconciliationFileApplyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryReconciliationFileApplyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryRefund(
            self,
            request: models.QueryRefundRequest,
            opts: Dict = None,
    ) -> models.QueryRefundResponse:
        """
        提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时，用微信零钱支付的退款约20分钟内到账，银行卡支付的退款约3个工作日后到账。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryRefund"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryRefundResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryShopOpenId(
            self,
            request: models.QueryShopOpenIdRequest,
            opts: Dict = None,
    ) -> models.QueryShopOpenIdResponse:
        """
        云支付-获取门店OpenId接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryShopOpenId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryShopOpenIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuerySinglePaymentResult(
            self,
            request: models.QuerySinglePaymentResultRequest,
            opts: Dict = None,
    ) -> models.QuerySinglePaymentResultResponse:
        """
        灵云-单笔转账结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QuerySinglePaymentResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuerySinglePaymentResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuerySingleTransactionStatus(
            self,
            request: models.QuerySingleTransactionStatusRequest,
            opts: Dict = None,
    ) -> models.QuerySingleTransactionStatusResponse:
        """
        查询银行单笔交易状态。查询单笔交易的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "QuerySingleTransactionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuerySingleTransactionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuerySmallAmountTransfer(
            self,
            request: models.QuerySmallAmountTransferRequest,
            opts: Dict = None,
    ) -> models.QuerySmallAmountTransferResponse:
        """
        查询小额鉴权转账结果。查询小额往账鉴权的转账状态。
        """
        
        kwargs = {}
        kwargs["action"] = "QuerySmallAmountTransfer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuerySmallAmountTransferResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTrade(
            self,
            request: models.QueryTradeRequest,
            opts: Dict = None,
    ) -> models.QueryTradeResponse:
        """
        跨境-贸易材料明细查询。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTransferBatch(
            self,
            request: models.QueryTransferBatchRequest,
            opts: Dict = None,
    ) -> models.QueryTransferBatchResponse:
        """
        通过商家批次单号或者微信批次号查询批次单
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTransferBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTransferBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTransferDetail(
            self,
            request: models.QueryTransferDetailRequest,
            opts: Dict = None,
    ) -> models.QueryTransferDetailResponse:
        """
        通过商家或者微信批次明细单号查询明细单
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTransferDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTransferDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTransferResult(
            self,
            request: models.QueryTransferResultRequest,
            opts: Dict = None,
    ) -> models.QueryTransferResultResponse:
        """
        智能代发-单笔代发转账查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTransferResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTransferResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RechargeByThirdPay(
            self,
            request: models.RechargeByThirdPayRequest,
            opts: Dict = None,
    ) -> models.RechargeByThirdPayResponse:
        """
        会员在途充值(经第三方支付渠道)接口
        """
        
        kwargs = {}
        kwargs["action"] = "RechargeByThirdPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RechargeByThirdPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RechargeMemberThirdPay(
            self,
            request: models.RechargeMemberThirdPayRequest,
            opts: Dict = None,
    ) -> models.RechargeMemberThirdPayResponse:
        """
        见证宝-会员在途充值(经第三方支付渠道)
        """
        
        kwargs = {}
        kwargs["action"] = "RechargeMemberThirdPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RechargeMemberThirdPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Refund(
            self,
            request: models.RefundRequest,
            opts: Dict = None,
    ) -> models.RefundResponse:
        """
        如交易订单需退款，可以通过本接口将支付款全部或部分退还给付款方，聚鑫将在收到退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。最长支持1年的订单退款。在订单包含多个子订单的情况下，如果使用本接口传入OutTradeNo或TransactionId退款，则只支持全单退款；如果需要部分退款，请通过传入子订单的方式来指定部分金额退款。
        """
        
        kwargs = {}
        kwargs["action"] = "Refund"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundCloudOrder(
            self,
            request: models.RefundCloudOrderRequest,
            opts: Dict = None,
    ) -> models.RefundCloudOrderResponse:
        """
        如交易订单需退款，可以通过本接口将支付款全部或部分退还给付款方，聚鑫将在收到退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。最长支持1年的订单退款。在订单包含多个子订单的情况下，如果使用本接口传入OutTradeNo或TransactionId退款，则只支持全单退款；如果需要部分退款，请通过传入子订单的方式来指定部分金额退款。
        """
        
        kwargs = {}
        kwargs["action"] = "RefundCloudOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundCloudOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundMemberTransaction(
            self,
            request: models.RefundMemberTransactionRequest,
            opts: Dict = None,
    ) -> models.RefundMemberTransactionResponse:
        """
        会员间交易退款
        """
        
        kwargs = {}
        kwargs["action"] = "RefundMemberTransaction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundMemberTransactionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundOpenBankOrder(
            self,
            request: models.RefundOpenBankOrderRequest,
            opts: Dict = None,
    ) -> models.RefundOpenBankOrderResponse:
        """
        云企付-退款申请
        """
        
        kwargs = {}
        kwargs["action"] = "RefundOpenBankOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundOpenBankOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundOrder(
            self,
            request: models.RefundOrderRequest,
            opts: Dict = None,
    ) -> models.RefundOrderResponse:
        """
        云鉴-消费订单退款的接口
        """
        
        kwargs = {}
        kwargs["action"] = "RefundOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefundTlinxOrder(
            self,
            request: models.RefundTlinxOrderRequest,
            opts: Dict = None,
    ) -> models.RefundTlinxOrderResponse:
        """
        云支付订单退款接口
        """
        
        kwargs = {}
        kwargs["action"] = "RefundTlinxOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefundTlinxOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterBehavior(
            self,
            request: models.RegisterBehaviorRequest,
            opts: Dict = None,
    ) -> models.RegisterBehaviorResponse:
        """
        商户查询是否签约和签约行为上报
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterBehavior"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterBehaviorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterBill(
            self,
            request: models.RegisterBillRequest,
            opts: Dict = None,
    ) -> models.RegisterBillResponse:
        """
        登记挂账(支持撤销)
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterBill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterBillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterBillSupportWithdraw(
            self,
            request: models.RegisterBillSupportWithdrawRequest,
            opts: Dict = None,
    ) -> models.RegisterBillSupportWithdrawResponse:
        """
        登记挂账(支持撤销)。此接口可实现把不明来账或自有资金等已登记在挂账子账户下的资金调整到普通会员子账户。即通过申请调用此接口，将会减少挂账子账户的资金，调增指定的普通会员子账户的可提现余额及可用余额。此接口不支持把挂账子账户资金清分到功能子账户。
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterBillSupportWithdraw"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterBillSupportWithdrawResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReviseMbrProperty(
            self,
            request: models.ReviseMbrPropertyRequest,
            opts: Dict = None,
    ) -> models.ReviseMbrPropertyResponse:
        """
        修改会员属性-普通商户子账户。修改会员的会员属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ReviseMbrProperty"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReviseMbrPropertyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeMemberRechargeThirdPay(
            self,
            request: models.RevokeMemberRechargeThirdPayRequest,
            opts: Dict = None,
    ) -> models.RevokeMemberRechargeThirdPayResponse:
        """
        撤销会员在途充值(经第三方支付渠道)
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeMemberRechargeThirdPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeMemberRechargeThirdPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeRechargeByThirdPay(
            self,
            request: models.RevokeRechargeByThirdPayRequest,
            opts: Dict = None,
    ) -> models.RevokeRechargeByThirdPayResponse:
        """
        撤销会员在途充值(经第三方支付渠道)接口
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeRechargeByThirdPay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeRechargeByThirdPayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncContractData(
            self,
            request: models.SyncContractDataRequest,
            opts: Dict = None,
    ) -> models.SyncContractDataResponse:
        """
        对于存量的签约关系导入或者部分场景下米大师无法收到签约通知的场景，需要由调用方主动将签约状态同步至米大师
        """
        
        kwargs = {}
        kwargs["action"] = "SyncContractData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncContractDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateContract(
            self,
            request: models.TerminateContractRequest,
            opts: Dict = None,
    ) -> models.TerminateContractResponse:
        """
        通过此接口进行解约
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferSinglePay(
            self,
            request: models.TransferSinglePayRequest,
            opts: Dict = None,
    ) -> models.TransferSinglePayResponse:
        """
        智能代发-单笔代发转账接口
        """
        
        kwargs = {}
        kwargs["action"] = "TransferSinglePay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferSinglePayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindAcct(
            self,
            request: models.UnBindAcctRequest,
            opts: Dict = None,
    ) -> models.UnBindAcctResponse:
        """
        商户解除绑定的提现银行卡
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindAcct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindAcctResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindOpenBankExternalSubMerchantBankAccount(
            self,
            request: models.UnbindOpenBankExternalSubMerchantBankAccountRequest,
            opts: Dict = None,
    ) -> models.UnbindOpenBankExternalSubMerchantBankAccountResponse:
        """
        云企付-子商户银行卡解绑
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindOpenBankExternalSubMerchantBankAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindOpenBankExternalSubMerchantBankAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindRelateAcct(
            self,
            request: models.UnbindRelateAcctRequest,
            opts: Dict = None,
    ) -> models.UnbindRelateAcctResponse:
        """
        会员解绑提现账户。此接口可以支持会员解除名下的绑定账户关系。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindRelateAcct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindRelateAcctResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnifiedCloudOrder(
            self,
            request: models.UnifiedCloudOrderRequest,
            opts: Dict = None,
    ) -> models.UnifiedCloudOrderResponse:
        """
        应用需要先调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。
        """
        
        kwargs = {}
        kwargs["action"] = "UnifiedCloudOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnifiedCloudOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnifiedOrder(
            self,
            request: models.UnifiedOrderRequest,
            opts: Dict = None,
    ) -> models.UnifiedOrderResponse:
        """
        应用需要先调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。
        """
        
        kwargs = {}
        kwargs["action"] = "UnifiedOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnifiedOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnifiedTlinxOrder(
            self,
            request: models.UnifiedTlinxOrderRequest,
            opts: Dict = None,
    ) -> models.UnifiedTlinxOrderResponse:
        """
        云支付-统一下单接口
        """
        
        kwargs = {}
        kwargs["action"] = "UnifiedTlinxOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnifiedTlinxOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadExternalAnchorInfo(
            self,
            request: models.UploadExternalAnchorInfoRequest,
            opts: Dict = None,
    ) -> models.UploadExternalAnchorInfoResponse:
        """
        灵云-上传主播信息
        """
        
        kwargs = {}
        kwargs["action"] = "UploadExternalAnchorInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadExternalAnchorInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFile(
            self,
            request: models.UploadFileRequest,
            opts: Dict = None,
    ) -> models.UploadFileResponse:
        """
        直播平台-文件上传
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadOpenBankSubMerchantCredential(
            self,
            request: models.UploadOpenBankSubMerchantCredentialRequest,
            opts: Dict = None,
    ) -> models.UploadOpenBankSubMerchantCredentialResponse:
        """
        云企付-子商户资质文件上传
        """
        
        kwargs = {}
        kwargs["action"] = "UploadOpenBankSubMerchantCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadOpenBankSubMerchantCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadOrgFile(
            self,
            request: models.UploadOrgFileRequest,
            opts: Dict = None,
    ) -> models.UploadOrgFileResponse:
        """
        云支付-上传机构文件接口
        """
        
        kwargs = {}
        kwargs["action"] = "UploadOrgFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadOrgFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadTaxList(
            self,
            request: models.UploadTaxListRequest,
            opts: Dict = None,
    ) -> models.UploadTaxListResponse:
        """
        直播平台-上传代理商完税列表
        """
        
        kwargs = {}
        kwargs["action"] = "UploadTaxList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadTaxListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadTaxPayment(
            self,
            request: models.UploadTaxPaymentRequest,
            opts: Dict = None,
    ) -> models.UploadTaxPaymentResponse:
        """
        直播平台-上传代理商完税证明
        """
        
        kwargs = {}
        kwargs["action"] = "UploadTaxPayment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadTaxPaymentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyOpenBankAccount(
            self,
            request: models.VerifyOpenBankAccountRequest,
            opts: Dict = None,
    ) -> models.VerifyOpenBankAccountResponse:
        """
        云企付-子商户银行卡打款验证，在接入TENPAY渠道EBANK_PAYMENT付款时，若客户期望接入担保支付，需在接入前先完成，收款商户绑定的银行卡进行打款验证。验证成功后，才可以调用CreateOpenBankPaymentOrder接口进行担保支付下单。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyOpenBankAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyOpenBankAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ViewContract(
            self,
            request: models.ViewContractRequest,
            opts: Dict = None,
    ) -> models.ViewContractResponse:
        """
        云支付-查询合同明细接口
        """
        
        kwargs = {}
        kwargs["action"] = "ViewContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ViewContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ViewMerchant(
            self,
            request: models.ViewMerchantRequest,
            opts: Dict = None,
    ) -> models.ViewMerchantResponse:
        """
        云支付-查询商户明细接口
        """
        
        kwargs = {}
        kwargs["action"] = "ViewMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ViewMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ViewShop(
            self,
            request: models.ViewShopRequest,
            opts: Dict = None,
    ) -> models.ViewShopResponse:
        """
        云支付-查询门店明细接口
        """
        
        kwargs = {}
        kwargs["action"] = "ViewShop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ViewShopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def WithdrawCashMembership(
            self,
            request: models.WithdrawCashMembershipRequest,
            opts: Dict = None,
    ) -> models.WithdrawCashMembershipResponse:
        """
        会员提现-不验证。此接口受理会员发起的提现申请。会员子账户的可提现余额、可用余额会减少，市场的资金汇总账户(监管账户)会减少相应的发生金额，提现到会员申请的收款账户。
        """
        
        kwargs = {}
        kwargs["action"] = "WithdrawCashMembership"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.WithdrawCashMembershipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)