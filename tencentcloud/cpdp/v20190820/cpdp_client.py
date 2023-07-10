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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cpdp.v20190820 import models


class CpdpClient(AbstractClient):
    _apiVersion = '2019-08-20'
    _endpoint = 'cpdp.tencentcloudapi.com'
    _service = 'cpdp'


    def AddContract(self, request):
        """云支付-添加合同接口

        :param request: Request instance for AddContract.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.AddContractRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.AddContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddContract", params, headers=headers)
            response = json.loads(body)
            model = models.AddContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddFlexFundingAccount(self, request):
        """灵云V2-绑定收款用户资金账号信息

        :param request: Request instance for AddFlexFundingAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.AddFlexFundingAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.AddFlexFundingAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddFlexFundingAccount", params, headers=headers)
            response = json.loads(body)
            model = models.AddFlexFundingAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddFlexIdInfo(self, request):
        """灵云V2-补充证件信息

        :param request: Request instance for AddFlexIdInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.AddFlexIdInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.AddFlexIdInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddFlexIdInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddFlexIdInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddFlexPhoneNo(self, request):
        """灵云V2-补充手机号信息

        :param request: Request instance for AddFlexPhoneNo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.AddFlexPhoneNoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.AddFlexPhoneNoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddFlexPhoneNo", params, headers=headers)
            response = json.loads(body)
            model = models.AddFlexPhoneNoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddMerchant(self, request):
        """云支付-添加商户接口

        :param request: Request instance for AddMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.AddMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.AddMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.AddMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddShop(self, request):
        """云支付-添加门店接口

        :param request: Request instance for AddShop.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.AddShopRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.AddShopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddShop", params, headers=headers)
            response = json.loads(body)
            model = models.AddShopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyApplicationMaterial(self, request):
        """跨境-提交申报材料。申报材料的主体是付款人，需要提前调用【跨境-付款人申请】接口提交付款人信息且审核通过后调用。

        :param request: Request instance for ApplyApplicationMaterial.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyApplicationMaterialRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyApplicationMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyApplicationMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyApplicationMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyFlexPayment(self, request):
        """灵云V2-付款

        :param request: Request instance for ApplyFlexPayment.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexPaymentRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexPaymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyFlexPayment", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyFlexPaymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyFlexSettlement(self, request):
        """灵云V2-结算

        :param request: Request instance for ApplyFlexSettlement.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexSettlementRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexSettlementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyFlexSettlement", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyFlexSettlementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyFlexWechatPreAuth(self, request):
        """微工卡开通预核身接口

        :param request: Request instance for ApplyFlexWechatPreAuth.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexWechatPreAuthRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexWechatPreAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyFlexWechatPreAuth", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyFlexWechatPreAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyOpenBankOrderDetailReceipt(self, request):
        """云企付-申请单笔交易回单

        :param request: Request instance for ApplyOpenBankOrderDetailReceipt.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyOpenBankOrderDetailReceiptRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyOpenBankOrderDetailReceiptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyOpenBankOrderDetailReceipt", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyOpenBankOrderDetailReceiptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyOpenBankSettleOrder(self, request):
        """云企付-结算申请接口

        :param request: Request instance for ApplyOpenBankSettleOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyOpenBankSettleOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyOpenBankSettleOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyOpenBankSettleOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyOpenBankSettleOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyOpenBankSubMerchantSignOnline(self, request):
        """子商户在线签约

        :param request: Request instance for ApplyOpenBankSubMerchantSignOnline.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyOpenBankSubMerchantSignOnlineRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyOpenBankSubMerchantSignOnlineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyOpenBankSubMerchantSignOnline", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyOpenBankSubMerchantSignOnlineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyOutwardOrder(self, request):
        """跨境-汇出指令申请。通过该接口可将对接方账户中的人民币余额汇兑成外币，再汇出至指定银行账户。

        :param request: Request instance for ApplyOutwardOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyOutwardOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyOutwardOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyPayerInfo(self, request):
        """跨境-付款人申请。通过该接口提交付款人信息并进行 kyc 审核。

        :param request: Request instance for ApplyPayerInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyPayerInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyPayerInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyReWithdrawal(self, request):
        """正常结算提现失败情况下，发起重新提现的请求接口

        :param request: Request instance for ApplyReWithdrawal.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyReWithdrawalRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyReWithdrawalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyReWithdrawal", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyReWithdrawalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyReconciliationFile(self, request):
        """聚鑫-申请对账文件

        :param request: Request instance for ApplyReconciliationFile.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyReconciliationFileRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyReconciliationFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyReconciliationFile", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyReconciliationFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyTrade(self, request):
        """跨境-提交贸易材料。通过提交贸易材料接口可为对接方累计贸易额度，在额度范围内可发起汇兑汇出交易。

        :param request: Request instance for ApplyTrade.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyTrade", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyTradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyWithdrawal(self, request):
        """商户提现

        :param request: Request instance for ApplyWithdrawal.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ApplyWithdrawalRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ApplyWithdrawalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyWithdrawal", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyWithdrawalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindAccount(self, request):
        """灵云-绑定账号

        :param request: Request instance for BindAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.BindAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.BindAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAccount", params, headers=headers)
            response = json.loads(body)
            model = models.BindAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindAcct(self, request):
        """商户绑定提现银行卡，每个商户只能绑定一张提现银行卡

        :param request: Request instance for BindAcct.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.BindAcctRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.BindAcctResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAcct", params, headers=headers)
            response = json.loads(body)
            model = models.BindAcctResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindOpenBankExternalSubMerchantBankAccount(self, request):
        """云企付-子商户银行卡绑定

        :param request: Request instance for BindOpenBankExternalSubMerchantBankAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.BindOpenBankExternalSubMerchantBankAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.BindOpenBankExternalSubMerchantBankAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindOpenBankExternalSubMerchantBankAccount", params, headers=headers)
            response = json.loads(body)
            model = models.BindOpenBankExternalSubMerchantBankAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindOpenBankProfitSharePayee(self, request):
        """云企付-绑定分账收款方

        :param request: Request instance for BindOpenBankProfitSharePayee.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.BindOpenBankProfitSharePayeeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.BindOpenBankProfitSharePayeeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindOpenBankProfitSharePayee", params, headers=headers)
            response = json.loads(body)
            model = models.BindOpenBankProfitSharePayeeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindRelateAccReUnionPay(self, request):
        """会员绑定提现账户-回填银联鉴权短信码。用于会员填写动态验证码后，发往银行进行验证，验证成功则完成绑定。

        :param request: Request instance for BindRelateAccReUnionPay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.BindRelateAccReUnionPayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.BindRelateAccReUnionPayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindRelateAccReUnionPay", params, headers=headers)
            response = json.loads(body)
            model = models.BindRelateAccReUnionPayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindRelateAcctSmallAmount(self, request):
        """会员绑定提现账户-小额鉴权。会员申请绑定提现账户，绑定后从会员子账户中提现到绑定账户。
        转账鉴权有两种形式：往账鉴权和来账鉴权。
        往账鉴权：该接口发起成功后，银行会向提现账户转入小于等于0.5元的随机金额，并短信通知客户查看，客户查看后，需将收到的金额大小，在电商平台页面上回填，并通知银行。银行验证通过后，完成提现账户绑定。
        来账鉴权：该接口发起成功后，银行以短信通知客户查看，客户查看后，需通过待绑定的账户往市场的监管账户转入短信上指定的金额。银行检索到该笔指定金额的来账是源自待绑定账户，则绑定成功。平安银行的账户，即BankType送1时，大小额行号和超级网银号都不用送。

        :param request: Request instance for BindRelateAcctSmallAmount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.BindRelateAcctSmallAmountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.BindRelateAcctSmallAmountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindRelateAcctSmallAmount", params, headers=headers)
            response = json.loads(body)
            model = models.BindRelateAcctSmallAmountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindRelateAcctUnionPay(self, request):
        """会员绑定提现账户-银联鉴权。用于会员申请绑定提现账户，申请后银行前往银联验证卡信息：姓名、证件、卡号、银行预留手机是否相符，相符则发送给会员手机动态验证码并返回成功，不相符则返回失败。
        平台接收到银行返回成功后，进入输入动态验证码的页面，有效期120秒，若120秒未输入，客户可点击重新发送动态验证码，这个步骤重新调用该接口即可。
        平安银行的账户，大小额行号和超级网银号都不用送。
        超级网银号：单笔转账金额不超过5万，不限制笔数，只用选XX银行，不用具体到支行，可实时知道对方是否收款成功。
        大小额联行号：单笔转账可超过5万，需具体到支行，不能实时知道对方是否收款成功。金额超过5万的，在工作日的8点30-17点间才会成功。

        :param request: Request instance for BindRelateAcctUnionPay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.BindRelateAcctUnionPayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.BindRelateAcctUnionPayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindRelateAcctUnionPay", params, headers=headers)
            response = json.loads(body)
            model = models.BindRelateAcctUnionPayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckAcct(self, request):
        """商户绑定提现银行卡的验证接口

        :param request: Request instance for CheckAcct.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CheckAcctRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CheckAcctResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAcct", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAcctResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckAmount(self, request):
        """验证鉴权金额。此接口可受理BindRelateAcctSmallAmount接口发起的转账金额（往账鉴权方式）的验证处理。若所回填的验证金额验证通过，则会绑定原申请中的银行账户作为提现账户。通过此接口也可以查得BindRelateAcctSmallAmount接口发起的来账鉴权方式的申请的当前状态。

        :param request: Request instance for CheckAmount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CheckAmountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CheckAmountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAmount", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAmountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseCloudOrder(self, request):
        """通过此接口关闭此前已创建的订单。关闭后，用户将无法继续付款，仅能关闭创建后未支付的订单。

        :param request: Request instance for CloseCloudOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CloseCloudOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CloseCloudOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseCloudOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CloseCloudOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseOpenBankPaymentOrder(self, request):
        """云企付-关闭订单

        :param request: Request instance for CloseOpenBankPaymentOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CloseOpenBankPaymentOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CloseOpenBankPaymentOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseOpenBankPaymentOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CloseOpenBankPaymentOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseOrder(self, request):
        """通过此接口关闭此前已创建的订单，关闭后，用户将无法继续付款。仅能关闭创建后未支付的订单

        :param request: Request instance for CloseOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CloseOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CloseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CloseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ConfirmOrder(self, request):
        """云鉴-消费订单确认接口

        :param request: Request instance for ConfirmOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ConfirmOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ConfirmOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ContractOrder(self, request):
        """应用需要先带上签约信息调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。

        :param request: Request instance for ContractOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ContractOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ContractOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ContractOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ContractOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAcct(self, request):
        """子商户入驻聚鑫平台

        :param request: Request instance for CreateAcct.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateAcctRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateAcctResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcct", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAcctResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAgentTaxPaymentInfos(self, request):
        """直播平台-代理商完税信息录入

        :param request: Request instance for CreateAgentTaxPaymentInfos.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateAgentTaxPaymentInfosRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateAgentTaxPaymentInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentTaxPaymentInfos", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentTaxPaymentInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAnchor(self, request):
        """直播平台-主播入驻

        :param request: Request instance for CreateAnchor.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateAnchorRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateAnchorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAnchor", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAnchorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBatchPayment(self, request):
        """灵云-批量主播转账接口

        :param request: Request instance for CreateBatchPayment.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateBatchPaymentRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateBatchPaymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBatchPayment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBatchPaymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCloudSubMerchant(self, request):
        """创建子商户

        :param request: Request instance for CreateCloudSubMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateCloudSubMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateCloudSubMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudSubMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudSubMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCustAcctId(self, request):
        """会员子账户开立。会员在银行注册，并开立会员子账户，交易网会员代码即会员在平台端系统的会员编号。
        平台需保存银行返回的子账户账号，后续交易接口都会用到。会员属性字段为预留扩展字段，当前必须送默认值。

        :param request: Request instance for CreateCustAcctId.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateCustAcctIdRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateCustAcctIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustAcctId", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustAcctIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateExternalAnchor(self, request):
        """灵云-主播入驻

        :param request: Request instance for CreateExternalAnchor.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateExternalAnchorRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateExternalAnchorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExternalAnchor", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExternalAnchorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFlexPayee(self, request):
        """灵云V2-收款用户开立

        :param request: Request instance for CreateFlexPayee.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateFlexPayeeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateFlexPayeeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlexPayee", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlexPayeeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInvoice(self, request):
        """智慧零售-发票开具

        :param request: Request instance for CreateInvoice.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInvoice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInvoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInvoiceV2(self, request):
        """智慧零售-发票开具V2

        :param request: Request instance for CreateInvoiceV2.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceV2Request`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInvoiceV2", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInvoiceV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMerchant(self, request):
        """智慧零售-商户注册

        :param request: Request instance for CreateMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankAggregatedSubMerchantRegistration(self, request):
        """云企付-子商户进件V2

        :param request: Request instance for CreateOpenBankAggregatedSubMerchantRegistration.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankAggregatedSubMerchantRegistrationRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankAggregatedSubMerchantRegistrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankAggregatedSubMerchantRegistration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankAggregatedSubMerchantRegistrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankExternalSubMerchantAccountBook(self, request):
        """第三方子商户电子记账本创建接口

        :param request: Request instance for CreateOpenBankExternalSubMerchantAccountBook.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankExternalSubMerchantAccountBookRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankExternalSubMerchantAccountBookResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankExternalSubMerchantAccountBook", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankExternalSubMerchantAccountBookResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankExternalSubMerchantRegistration(self, request):
        """云企付-子商户进件

        :param request: Request instance for CreateOpenBankExternalSubMerchantRegistration.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankExternalSubMerchantRegistrationRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankExternalSubMerchantRegistrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankExternalSubMerchantRegistration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankExternalSubMerchantRegistrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankGlobalPaymentOrder(self, request):
        """云企付-跨境支付下单

        :param request: Request instance for CreateOpenBankGlobalPaymentOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankGlobalPaymentOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankGlobalPaymentOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankGlobalPaymentOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankGlobalPaymentOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankMerchant(self, request):
        """云企付-创建商户

        :param request: Request instance for CreateOpenBankMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankPaymentOrder(self, request):
        """云企付-创建支付订单。支持B2B网关支付，B2C转账下单。

        :param request: Request instance for CreateOpenBankPaymentOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankPaymentOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankPaymentOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankPaymentOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankPaymentOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankRechargeOrder(self, request):
        """云企付-创建充值订单

        :param request: Request instance for CreateOpenBankRechargeOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankRechargeOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankRechargeOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankRechargeOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankRechargeOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankSubMerchantRateConfigure(self, request):
        """云企付-子商户费率配置

        :param request: Request instance for CreateOpenBankSubMerchantRateConfigure.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankSubMerchantRateConfigureRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankSubMerchantRateConfigureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankSubMerchantRateConfigure", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankSubMerchantRateConfigureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankUnifiedOrder(self, request):
        """云企付-聚合下单

        :param request: Request instance for CreateOpenBankUnifiedOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankUnifiedOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankUnifiedOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankUnifiedOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankUnifiedOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOpenBankVerificationOrder(self, request):
        """云企付-创建核销申请，适用于针对支付订单维度的确认收货，解冻等业务场景。目前支持的渠道有TENPAY下的EBANK_PAYMENT付款方式创建支付订单时，选择担保支付下单的订单进行解冻。

        :param request: Request instance for CreateOpenBankVerificationOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankVerificationOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankVerificationOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpenBankVerificationOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpenBankVerificationOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOrder(self, request):
        """云鉴-消费订单发起的接口

        :param request: Request instance for CreateOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePayMerchant(self, request):
        """商户新增的接口

        :param request: Request instance for CreatePayMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreatePayMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreatePayMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePayMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePayMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePayRollPreOrder(self, request):
        """务工卡-核身预下单

        :param request: Request instance for CreatePayRollPreOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreatePayRollPreOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreatePayRollPreOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePayRollPreOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePayRollPreOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePayRollPreOrderWithAuth(self, request):
        """务工卡-核身预下单带授权

        :param request: Request instance for CreatePayRollPreOrderWithAuth.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreatePayRollPreOrderWithAuthRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreatePayRollPreOrderWithAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePayRollPreOrderWithAuth", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePayRollPreOrderWithAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePayRollToken(self, request):
        """务工卡-生成授权令牌

        :param request: Request instance for CreatePayRollToken.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreatePayRollTokenRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreatePayRollTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePayRollToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePayRollTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRedInvoice(self, request):
        """智慧零售-发票红冲

        :param request: Request instance for CreateRedInvoice.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRedInvoice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRedInvoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRedInvoiceV2(self, request):
        """智慧零售-发票红冲V2

        :param request: Request instance for CreateRedInvoiceV2.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceV2Request`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRedInvoiceV2", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRedInvoiceV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSinglePayment(self, request):
        """灵云-单笔主播转账接口

        :param request: Request instance for CreateSinglePayment.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateSinglePaymentRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateSinglePaymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSinglePayment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSinglePaymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTransferBatch(self, request):
        """微信商户发起批量转账

        :param request: Request instance for CreateTransferBatch.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateTransferBatchRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateTransferBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTransferBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTransferBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeduceQuota(self, request):
        """直播平台-扣减额度

        :param request: Request instance for DeduceQuota.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DeduceQuotaRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DeduceQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeduceQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DeduceQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAgentTaxPaymentInfo(self, request):
        """直播平台-删除代理商完税信息

        :param request: Request instance for DeleteAgentTaxPaymentInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DeleteAgentTaxPaymentInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DeleteAgentTaxPaymentInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgentTaxPaymentInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentTaxPaymentInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAgentTaxPaymentInfos(self, request):
        """直播平台-删除代理商完税信息

        :param request: Request instance for DeleteAgentTaxPaymentInfos.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DeleteAgentTaxPaymentInfosRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DeleteAgentTaxPaymentInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAgentTaxPaymentInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAgentTaxPaymentInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChargeDetail(self, request):
        """查询充值明细接口

        :param request: Request instance for DescribeChargeDetail.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DescribeChargeDetailRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DescribeChargeDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChargeDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChargeDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrderStatus(self, request):
        """查询单笔订单交易状态

        :param request: Request instance for DescribeOrderStatus.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DescribeOrderStatusRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DescribeOrderStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrderStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrderStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeAccreditQuery(self, request):
        """云支付-分账授权申请查询接口

        :param request: Request instance for DistributeAccreditQuery.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeAccreditQueryRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeAccreditQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeAccreditQuery", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeAccreditQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeAccreditTlinx(self, request):
        """云支付-分账授权申请接口

        :param request: Request instance for DistributeAccreditTlinx.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeAccreditTlinxRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeAccreditTlinxResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeAccreditTlinx", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeAccreditTlinxResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeAddReceiver(self, request):
        """云支付-分账添加分账接收方接口

        :param request: Request instance for DistributeAddReceiver.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeAddReceiverRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeAddReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeAddReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeAddReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeApply(self, request):
        """云支付-分账请求接口

        :param request: Request instance for DistributeApply.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeApplyRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeApply", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeCancel(self, request):
        """云支付-分账撤销接口

        :param request: Request instance for DistributeCancel.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeCancelRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeCancelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeCancel", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeCancelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeQuery(self, request):
        """云支付-分账结果查询接口

        :param request: Request instance for DistributeQuery.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeQueryRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeQuery", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeQueryReceiver(self, request):
        """云支付-查询已添加分账接收方接口

        :param request: Request instance for DistributeQueryReceiver.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeQueryReceiverRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeQueryReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeQueryReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeQueryReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeRemoveReceiver(self, request):
        """云支付-分账解除分账接收方接口

        :param request: Request instance for DistributeRemoveReceiver.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeRemoveReceiverRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeRemoveReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeRemoveReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeRemoveReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadBill(self, request):
        """账单下载接口，根据本接口返回的URL地址，在D+1日下载对账单。注意，本接口返回的URL地址有时效，请尽快下载。URL超时时效后，请重新调用本接口再次获取。

        :param request: Request instance for DownloadBill.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DownloadBillRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DownloadBillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadBill", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadBillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadOrgFile(self, request):
        """云支付-下载机构文件接口

        :param request: Request instance for DownloadOrgFile.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DownloadOrgFileRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DownloadOrgFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadOrgFile", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadOrgFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadReconciliationUrl(self, request):
        """获取对账中心账单下载地址的接口

        :param request: Request instance for DownloadReconciliationUrl.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DownloadReconciliationUrlRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DownloadReconciliationUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadReconciliationUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadReconciliationUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExecuteMemberTransaction(self, request):
        """会员间交易接口

        :param request: Request instance for ExecuteMemberTransaction.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ExecuteMemberTransactionRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ExecuteMemberTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteMemberTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteMemberTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FreezeFlexBalance(self, request):
        """灵云V2-冻结余额

        :param request: Request instance for FreezeFlexBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.FreezeFlexBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.FreezeFlexBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeFlexBalance", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeFlexBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetBillDownloadUrl(self, request):
        """调用该接口返回对账单下载地址，对账单下载URL通过GET方式访问，返回zip包，解压后为csv格式文件。文件首行如下：
        订单号,订单归属日期,机构编号,订单描述,交易类型,订单状态,支付场景,原始金额,折扣金额,实际交易金额,支付渠道优惠金额,抹零金额,币种,下单时间,付款成功时间,商户编号,门店编号,付款方式编号,付款方式名称,商户手续费T1,商户扣率,是否信用卡交易,原始订单号,用户账号,外部订单号,订单备注

        :param request: Request instance for GetBillDownloadUrl.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.GetBillDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.GetBillDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBillDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GetBillDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDistributeBillDownloadUrl(self, request):
        """调用该接口返回对账单下载地址，对账单下载URL通过GET方式访问，返回zip包，解压后为csv格式文件。文件首行如下：
        商户号,订单号,支付订单号,分账订单总金额,分账详情（通过|分割每笔明细：商户号1#分账金额1|商户号2#分账金额2）,交易手续费承担方商户号,交易手续费,发起时间,分账状态,结算日期,非交易主体分账金额,商户退款订单号,商户分账单号

        :param request: Request instance for GetDistributeBillDownloadUrl.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.GetDistributeBillDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.GetDistributeBillDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDistributeBillDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GetDistributeBillDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPayRollAuth(self, request):
        """务工卡-查询授权关系

        :param request: Request instance for GetPayRollAuth.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.GetPayRollAuthRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.GetPayRollAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPayRollAuth", params, headers=headers)
            response = json.loads(body)
            model = models.GetPayRollAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPayRollAuthList(self, request):
        """务工卡-查询核身记录

        :param request: Request instance for GetPayRollAuthList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.GetPayRollAuthListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.GetPayRollAuthListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPayRollAuthList", params, headers=headers)
            response = json.loads(body)
            model = models.GetPayRollAuthListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPayRollAuthResult(self, request):
        """务工卡-获取核身结果

        :param request: Request instance for GetPayRollAuthResult.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.GetPayRollAuthResultRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.GetPayRollAuthResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPayRollAuthResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetPayRollAuthResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigrateOrderRefund(self, request):
        """山姆聚合支付项目-存量订单退款接口。可以通过本接口将支付款全部或部分退还给付款方，在收到用户退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付账号。

        :param request: Request instance for MigrateOrderRefund.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.MigrateOrderRefundRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.MigrateOrderRefundResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateOrderRefund", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateOrderRefundResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigrateOrderRefundQuery(self, request):
        """提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时。

        :param request: Request instance for MigrateOrderRefundQuery.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.MigrateOrderRefundQueryRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.MigrateOrderRefundQueryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateOrderRefundQuery", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateOrderRefundQueryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAgentTaxPaymentInfo(self, request):
        """直播平台-修改代理商完税信息

        :param request: Request instance for ModifyAgentTaxPaymentInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ModifyAgentTaxPaymentInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ModifyAgentTaxPaymentInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAgentTaxPaymentInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAgentTaxPaymentInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBindedAccount(self, request):
        """灵云-重新绑定账号

        :param request: Request instance for ModifyBindedAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ModifyBindedAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ModifyBindedAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBindedAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBindedAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyFlexFundingAccount(self, request):
        """灵云V2-修改收款用户资金账号信息

        :param request: Request instance for ModifyFlexFundingAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ModifyFlexFundingAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ModifyFlexFundingAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFlexFundingAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFlexFundingAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyFlexPayeeAccountRightStatus(self, request):
        """灵云V2-收款用户账户权益状态修改

        :param request: Request instance for ModifyFlexPayeeAccountRightStatus.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ModifyFlexPayeeAccountRightStatusRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ModifyFlexPayeeAccountRightStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFlexPayeeAccountRightStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFlexPayeeAccountRightStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMerchant(self, request):
        """云鉴-商户信息修改的接口

        :param request: Request instance for ModifyMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ModifyMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ModifyMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMntMbrBindRelateAcctBankCode(self, request):
        """维护会员绑定提现账户联行号。此接口可以支持市场修改会员的提现账户的开户行信息，具体包括开户行行名、开户行的银行联行号（大小额联行号）和超级网银行号。

        :param request: Request instance for ModifyMntMbrBindRelateAcctBankCode.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ModifyMntMbrBindRelateAcctBankCodeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ModifyMntMbrBindRelateAcctBankCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMntMbrBindRelateAcctBankCode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMntMbrBindRelateAcctBankCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAcctBinding(self, request):
        """聚鑫-查询子账户绑定银行卡

        :param request: Request instance for QueryAcctBinding.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryAcctBindingRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryAcctBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAcctBinding", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAcctBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAcctInfo(self, request):
        """聚鑫-开户信息查询

        :param request: Request instance for QueryAcctInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryAcctInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryAcctInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAcctInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAcctInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAcctInfoList(self, request):
        """聚鑫-开户信息列表查询, 查询某一段时间的开户信息

        :param request: Request instance for QueryAcctInfoList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryAcctInfoListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryAcctInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAcctInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAcctInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAgentStatements(self, request):
        """直播平台-查询代理商结算单链接

        :param request: Request instance for QueryAgentStatements.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryAgentStatementsRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryAgentStatementsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAgentStatements", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAgentStatementsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAgentTaxPaymentBatch(self, request):
        """直播平台-查询批次信息

        :param request: Request instance for QueryAgentTaxPaymentBatch.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryAgentTaxPaymentBatchRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryAgentTaxPaymentBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAgentTaxPaymentBatch", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAgentTaxPaymentBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAnchorContractInfo(self, request):
        """直播平台-查询主播签约信息

        :param request: Request instance for QueryAnchorContractInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryAnchorContractInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryAnchorContractInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAnchorContractInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAnchorContractInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryApplicationMaterial(self, request):
        """跨境-成功申报材料查询。查询成功入库的申报材料。

        :param request: Request instance for QueryApplicationMaterial.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryApplicationMaterialRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryApplicationMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryApplicationMaterial", params, headers=headers)
            response = json.loads(body)
            model = models.QueryApplicationMaterialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAssignment(self, request):
        """直播平台-查询分配关系

        :param request: Request instance for QueryAssignment.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryAssignmentRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryAssignmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryAssignment", params, headers=headers)
            response = json.loads(body)
            model = models.QueryAssignmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBalance(self, request):
        """子商户余额查询

        :param request: Request instance for QueryBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBankClear(self, request):
        """查询银行在途清算结果。查询时间段内交易网的在途清算结果。

        :param request: Request instance for QueryBankClear.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryBankClearRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryBankClearResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBankClear", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBankClearResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBankTransactionDetails(self, request):
        """查询银行时间段内交易明细。查询时间段的会员成功交易。

        :param request: Request instance for QueryBankTransactionDetails.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryBankTransactionDetailsRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryBankTransactionDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBankTransactionDetails", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBankTransactionDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBankWithdrawCashDetails(self, request):
        """查询银行时间段内清分提现明细。查询银行时间段内清分提现明细接口：若为“见证+收单退款”“见证+收单充值”记录时备注Note为“见证+收单充值,订单号”“见证+收单退款,订单号”，此接口可以查到T0/T1的充值明细和退款记录。查询标志：充值记录仍用3清分选项查询，退款记录同提现用2选项查询。

        :param request: Request instance for QueryBankWithdrawCashDetails.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryBankWithdrawCashDetailsRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryBankWithdrawCashDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBankWithdrawCashDetails", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBankWithdrawCashDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBatchPaymentResult(self, request):
        """灵云-批量转账结果查询

        :param request: Request instance for QueryBatchPaymentResult.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryBatchPaymentResultRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryBatchPaymentResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBatchPaymentResult", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBatchPaymentResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBillDownloadURL(self, request):
        """获取单笔代发转账对账单下载URL

        :param request: Request instance for QueryBillDownloadURL.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryBillDownloadURLRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryBillDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBillDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBillDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCityCode(self, request):
        """云支付-查询城市编码接口

        :param request: Request instance for QueryCityCode.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryCityCodeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryCityCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCityCode", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCityCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCloudChannelData(self, request):
        """发起支付等渠道操作后，可以调用该接口查询渠道的数据。

        :param request: Request instance for QueryCloudChannelData.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryCloudChannelDataRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryCloudChannelDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCloudChannelData", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCloudChannelDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCloudOrder(self, request):
        """根据订单号或用户ID，查询支付订单状态。

        :param request: Request instance for QueryCloudOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryCloudOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryCloudOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCloudOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCloudOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCloudRefundOrder(self, request):
        """提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时，用微信零钱支付的退款约20分钟内到账，银行卡支付的退款约3个工作日后到账。

        :param request: Request instance for QueryCloudRefundOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryCloudRefundOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryCloudRefundOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCloudRefundOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCloudRefundOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCommonTransferRecharge(self, request):
        """查询普通转账充值明细。接口用于查询会员主动转账进资金汇总账户的明细情况。若会员使用绑定账号转入，则直接入账到会员子账户。若未使用绑定账号转入，则系统无法自动清分到对应子账户，则转入挂账子账户由平台自行清分。若是 “见证+收单充值”T0充值记录时备注Note为“见证+收单充值,订单号” 此接口可以查到T0到账的“见证+收单充值”充值记录。

        :param request: Request instance for QueryCommonTransferRecharge.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryCommonTransferRechargeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryCommonTransferRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCommonTransferRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCommonTransferRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCompanyTitle(self, request):
        """智慧零售-查询公司抬头

        :param request: Request instance for QueryCompanyTitle.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryCompanyTitleRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryCompanyTitleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCompanyTitle", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCompanyTitleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryContract(self, request):
        """通过此接口查询签约数据

        :param request: Request instance for QueryContract.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryContractRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryContract", params, headers=headers)
            response = json.loads(body)
            model = models.QueryContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryContractPayFee(self, request):
        """云支付-查询支付方式费率及自定义表单项接口

        :param request: Request instance for QueryContractPayFee.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryContractPayFeeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryContractPayFeeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryContractPayFee", params, headers=headers)
            response = json.loads(body)
            model = models.QueryContractPayFeeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryContractPayWayList(self, request):
        """云支付-查询合同支付方式列表接口

        :param request: Request instance for QueryContractPayWayList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryContractPayWayListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryContractPayWayListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryContractPayWayList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryContractPayWayListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryContractRelateShop(self, request):
        """云支付-查询合同可关联门店接口

        :param request: Request instance for QueryContractRelateShop.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryContractRelateShopRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryContractRelateShopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryContractRelateShop", params, headers=headers)
            response = json.loads(body)
            model = models.QueryContractRelateShopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCustAcctIdBalance(self, request):
        """查询银行子账户余额。查询会员子账户以及平台的功能子账户的余额。

        :param request: Request instance for QueryCustAcctIdBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryCustAcctIdBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryCustAcctIdBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCustAcctIdBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCustAcctIdBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryDownloadBillURL(self, request):
        """云鉴-查询对账单下载地址的接口

        :param request: Request instance for QueryDownloadBillURL.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryDownloadBillURLRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryDownloadBillURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDownloadBillURL", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDownloadBillURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryExceedingInfo(self, request):
        """灵云-查询超额信息

        :param request: Request instance for QueryExceedingInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryExceedingInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryExceedingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryExceedingInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryExceedingInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryExchangeRate(self, request):
        """跨境-查询汇率

        :param request: Request instance for QueryExchangeRate.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryExchangeRateRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryExchangeRateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryExchangeRate", params, headers=headers)
            response = json.loads(body)
            model = models.QueryExchangeRateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFinancialDataUrl(self, request):
        """财税-查询金融数据文件下载链接

        :param request: Request instance for QueryFinancialDataUrl.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFinancialDataUrlRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFinancialDataUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFinancialDataUrl", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFinancialDataUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexAmountBeforeTax(self, request):
        """灵云V2-查询税前金额

        :param request: Request instance for QueryFlexAmountBeforeTax.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexAmountBeforeTaxRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexAmountBeforeTaxResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexAmountBeforeTax", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexAmountBeforeTaxResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexBillDownloadUrl(self, request):
        """灵云V2-查询对账单文件下载链接

        :param request: Request instance for QueryFlexBillDownloadUrl.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexBillDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexBillDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexBillDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexBillDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexFreezeOrderList(self, request):
        """灵云V2-查询冻结订单列表

        :param request: Request instance for QueryFlexFreezeOrderList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexFreezeOrderListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexFreezeOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexFreezeOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexFreezeOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexOrderSummaryList(self, request):
        """灵云V2-订单汇总列表查询

        :param request: Request instance for QueryFlexOrderSummaryList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexOrderSummaryListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexOrderSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexOrderSummaryList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexOrderSummaryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexPayeeAccountBalance(self, request):
        """灵云V2-收款用户账户余额查询

        :param request: Request instance for QueryFlexPayeeAccountBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeAccountBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexPayeeAccountBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexPayeeAccountBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexPayeeAccountInfo(self, request):
        """灵云V2-收款用户账户信息查询

        :param request: Request instance for QueryFlexPayeeAccountInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeAccountInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeAccountInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexPayeeAccountInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexPayeeAccountInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexPayeeAccountList(self, request):
        """灵云V2-收款用户账户列表查询

        :param request: Request instance for QueryFlexPayeeAccountList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeAccountListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeAccountListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexPayeeAccountList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexPayeeAccountListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexPayeeInfo(self, request):
        """灵云V2-收款用户信息查询

        :param request: Request instance for QueryFlexPayeeInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPayeeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexPayeeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexPayeeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexPaymentOrderList(self, request):
        """灵云V2-查询付款订单列表

        :param request: Request instance for QueryFlexPaymentOrderList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPaymentOrderListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPaymentOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexPaymentOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexPaymentOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexPaymentOrderStatus(self, request):
        """灵云V2-查询付款订单状态

        :param request: Request instance for QueryFlexPaymentOrderStatus.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPaymentOrderStatusRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPaymentOrderStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexPaymentOrderStatus", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexPaymentOrderStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexPlatformAccountBalance(self, request):
        """灵云V2-平台账户余额查询

        :param request: Request instance for QueryFlexPlatformAccountBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPlatformAccountBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexPlatformAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexPlatformAccountBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexPlatformAccountBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexServiceProviderAccountBalance(self, request):
        """灵云V2-查询服务商账户余额

        :param request: Request instance for QueryFlexServiceProviderAccountBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexServiceProviderAccountBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexServiceProviderAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexServiceProviderAccountBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexServiceProviderAccountBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexSettlementOrderList(self, request):
        """灵云V2-查询结算订单列表

        :param request: Request instance for QueryFlexSettlementOrderList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexSettlementOrderListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexSettlementOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexSettlementOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexSettlementOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFlexWechatAuthResult(self, request):
        """查询微工卡核身结果

        :param request: Request instance for QueryFlexWechatAuthResult.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexWechatAuthResultRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFlexWechatAuthResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFlexWechatAuthResult", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFlexWechatAuthResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryFundsTransactionDetails(self, request):
        """聚鑫-查询会员资金交易信息列表

        :param request: Request instance for QueryFundsTransactionDetails.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryFundsTransactionDetailsRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryFundsTransactionDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFundsTransactionDetails", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFundsTransactionDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryInvoice(self, request):
        """智慧零售-发票查询

        :param request: Request instance for QueryInvoice.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryInvoice", params, headers=headers)
            response = json.loads(body)
            model = models.QueryInvoiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryInvoiceV2(self, request):
        """智慧零售-发票查询V2

        :param request: Request instance for QueryInvoiceV2.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceV2Request`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryInvoiceV2", params, headers=headers)
            response = json.loads(body)
            model = models.QueryInvoiceV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMaliciousRegistration(self, request):
        """商户恶意注册接口

        :param request: Request instance for QueryMaliciousRegistration.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMaliciousRegistrationRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMaliciousRegistrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMaliciousRegistration", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMaliciousRegistrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMemberBind(self, request):
        """会员绑定信息查询。查询标志为“单个会员”的情况下，返回该会员的有效的绑定账户信息。
        查询标志为“全部会员”的情况下，返回市场下的全部的有效的绑定账户信息。查询标志为“单个会员的证件信息”的情况下，返回市场下的指定的会员的留存在电商见证宝系统的证件信息。

        :param request: Request instance for QueryMemberBind.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMemberBindRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMemberBindResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMemberBind", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMemberBindResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMemberTransaction(self, request):
        """会员间交易-不验证。此接口可以实现会员间的余额的交易，实现资金在会员之间流动。

        :param request: Request instance for QueryMemberTransaction.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMemberTransactionRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMemberTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMemberTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMemberTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMemberTransactionDetails(self, request):
        """聚鑫-查询会员间交易信息列表

        :param request: Request instance for QueryMemberTransactionDetails.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMemberTransactionDetailsRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMemberTransactionDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMemberTransactionDetails", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMemberTransactionDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMerchant(self, request):
        """云鉴-商户信息查询接口

        :param request: Request instance for QueryMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMerchantBalance(self, request):
        """跨境-对接方账户余额查询

        :param request: Request instance for QueryMerchantBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMerchantBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMerchantBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMerchantClassification(self, request):
        """云支付-查询商户分类接口

        :param request: Request instance for QueryMerchantClassification.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantClassificationRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantClassificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMerchantClassification", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMerchantClassificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMerchantInfoForManagement(self, request):
        """智慧零售-查询管理端商户

        :param request: Request instance for QueryMerchantInfoForManagement.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantInfoForManagementRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantInfoForManagementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMerchantInfoForManagement", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMerchantInfoForManagementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMerchantOrder(self, request):
        """云鉴-消费订单查询接口

        :param request: Request instance for QueryMerchantOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMerchantOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMerchantOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMerchantPayWayList(self, request):
        """商户查询已开通的支付方式列表

        :param request: Request instance for QueryMerchantPayWayList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantPayWayListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantPayWayListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMerchantPayWayList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMerchantPayWayListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankBankAccountBalance(self, request):
        """云企付-子商户银行卡余额查询

        :param request: Request instance for QueryOpenBankBankAccountBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBankAccountBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBankAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankBankAccountBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankBankAccountBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankBankBranchList(self, request):
        """云企付-查询联行号

        :param request: Request instance for QueryOpenBankBankBranchList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBankBranchListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBankBranchListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankBankBranchList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankBankBranchListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankBillDataPage(self, request):
        """云企付-分页查询对账单数据

        :param request: Request instance for QueryOpenBankBillDataPage.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBillDataPageRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBillDataPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankBillDataPage", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankBillDataPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankBindExternalSubMerchantBankAccount(self, request):
        """云企付-子商户银行卡绑定结果查询

        :param request: Request instance for QueryOpenBankBindExternalSubMerchantBankAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBindExternalSubMerchantBankAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBindExternalSubMerchantBankAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankBindExternalSubMerchantBankAccount", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankBindExternalSubMerchantBankAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankDailyReceiptDownloadUrl(self, request):
        """云企付-按日期批量查询回单下载地址

        :param request: Request instance for QueryOpenBankDailyReceiptDownloadUrl.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankDailyReceiptDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankDailyReceiptDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankDailyReceiptDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankDailyReceiptDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankDownLoadUrl(self, request):
        """云企付-查询对账单下载地址

        :param request: Request instance for QueryOpenBankDownLoadUrl.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankDownLoadUrlRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankDownLoadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankDownLoadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankDownLoadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankExternalSubAccountBookBalance(self, request):
        """第三方子商户电子记账本余额查询接口

        :param request: Request instance for QueryOpenBankExternalSubAccountBookBalance.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubAccountBookBalanceRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubAccountBookBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankExternalSubAccountBookBalance", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankExternalSubAccountBookBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankExternalSubMerchantBankAccount(self, request):
        """云企付-子商户银行卡列表查询

        :param request: Request instance for QueryOpenBankExternalSubMerchantBankAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubMerchantBankAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubMerchantBankAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankExternalSubMerchantBankAccount", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankExternalSubMerchantBankAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankExternalSubMerchantRegistration(self, request):
        """云企付-子商户进件结果查询

        :param request: Request instance for QueryOpenBankExternalSubMerchantRegistration.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubMerchantRegistrationRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubMerchantRegistrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankExternalSubMerchantRegistration", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankExternalSubMerchantRegistrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankOrderDetailReceiptInfo(self, request):
        """云企付-单笔交易回单申请结果查询

        :param request: Request instance for QueryOpenBankOrderDetailReceiptInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankOrderDetailReceiptInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankOrderDetailReceiptInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankOrderDetailReceiptInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankOrderDetailReceiptInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankPaymentOrder(self, request):
        """云企付-查询订单支付结果

        :param request: Request instance for QueryOpenBankPaymentOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankPaymentOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankPaymentOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankPaymentOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankPaymentOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankProfitSharePayee(self, request):
        """云企付-绑定分账收款方查询

        :param request: Request instance for QueryOpenBankProfitSharePayee.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankProfitSharePayeeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankProfitSharePayeeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankProfitSharePayee", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankProfitSharePayeeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankRefundOrder(self, request):
        """云企付-退款结果查询

        :param request: Request instance for QueryOpenBankRefundOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankRefundOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankRefundOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankRefundOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankRefundOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankSettleOrder(self, request):
        """云企付-结算单查询结果

        :param request: Request instance for QueryOpenBankSettleOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSettleOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSettleOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankSettleOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankSettleOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankSubMerchantCredential(self, request):
        """云企付-子商户资质文件查询

        :param request: Request instance for QueryOpenBankSubMerchantCredential.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantCredentialRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankSubMerchantCredential", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankSubMerchantCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankSubMerchantRateConfigure(self, request):
        """云企付-子商户费率配置结果查询

        :param request: Request instance for QueryOpenBankSubMerchantRateConfigure.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantRateConfigureRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantRateConfigureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankSubMerchantRateConfigure", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankSubMerchantRateConfigureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankSubMerchantSignOnline(self, request):
        """子商户在线签约查询

        :param request: Request instance for QueryOpenBankSubMerchantSignOnline.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantSignOnlineRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantSignOnlineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankSubMerchantSignOnline", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankSubMerchantSignOnlineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankSupportBankList(self, request):
        """云企付-查询支持银行列表

        :param request: Request instance for QueryOpenBankSupportBankList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSupportBankListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSupportBankListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankSupportBankList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankSupportBankListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankUnbindExternalSubMerchantBankAccount(self, request):
        """云企付-子商户银行卡解绑结果查询

        :param request: Request instance for QueryOpenBankUnbindExternalSubMerchantBankAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankUnbindExternalSubMerchantBankAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankUnbindExternalSubMerchantBankAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankUnbindExternalSubMerchantBankAccount", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankUnbindExternalSubMerchantBankAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOpenBankVerificationOrder(self, request):
        """云企付-查询核销订单状态，客户可以使用该接口来查询核销申请的订单状态。目前仅支持TENPAY渠道EBANK_PAYMENT付款方式的担保支付订单查询。

        :param request: Request instance for QueryOpenBankVerificationOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankVerificationOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankVerificationOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOpenBankVerificationOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOpenBankVerificationOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOrder(self, request):
        """根据订单号，或者用户Id，查询支付订单状态

        :param request: Request instance for QueryOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOrderStatus(self, request):
        """云支付-查询订单付款状态

        :param request: Request instance for QueryOrderStatus.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOrderStatusRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOrderStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOrderStatus", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOrderStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOutwardOrder(self, request):
        """跨境-查询汇出结果

        :param request: Request instance for QueryOutwardOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryOutwardOrder", params, headers=headers)
            response = json.loads(body)
            model = models.QueryOutwardOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryPayerInfo(self, request):
        """跨境-付款人查询

        :param request: Request instance for QueryPayerInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryPayerInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryPayerInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryReconciliationDocument(self, request):
        """查询对账文件信息。平台调用该接口获取需下载对账文件的文件名称以及密钥。 平台获取到信息后， 可以再调用OPENAPI的文件下载功能。

        :param request: Request instance for QueryReconciliationDocument.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryReconciliationDocumentRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryReconciliationDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryReconciliationDocument", params, headers=headers)
            response = json.loads(body)
            model = models.QueryReconciliationDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryReconciliationFileApplyInfo(self, request):
        """聚鑫-查询对账文件申请结果

        :param request: Request instance for QueryReconciliationFileApplyInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryReconciliationFileApplyInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryReconciliationFileApplyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryReconciliationFileApplyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryReconciliationFileApplyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryRefund(self, request):
        """提交退款申请后，通过调用该接口查询退款状态。退款可能有一定延时，用微信零钱支付的退款约20分钟内到账，银行卡支付的退款约3个工作日后到账。

        :param request: Request instance for QueryRefund.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryRefundRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryRefundResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryRefund", params, headers=headers)
            response = json.loads(body)
            model = models.QueryRefundResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryShopOpenId(self, request):
        """云支付-获取门店OpenId接口

        :param request: Request instance for QueryShopOpenId.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryShopOpenIdRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryShopOpenIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryShopOpenId", params, headers=headers)
            response = json.loads(body)
            model = models.QueryShopOpenIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuerySinglePaymentResult(self, request):
        """灵云-单笔转账结果查询

        :param request: Request instance for QuerySinglePaymentResult.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QuerySinglePaymentResultRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QuerySinglePaymentResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QuerySinglePaymentResult", params, headers=headers)
            response = json.loads(body)
            model = models.QuerySinglePaymentResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuerySingleTransactionStatus(self, request):
        """查询银行单笔交易状态。查询单笔交易的状态。

        :param request: Request instance for QuerySingleTransactionStatus.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QuerySingleTransactionStatusRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QuerySingleTransactionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QuerySingleTransactionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.QuerySingleTransactionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuerySmallAmountTransfer(self, request):
        """查询小额鉴权转账结果。查询小额往账鉴权的转账状态。

        :param request: Request instance for QuerySmallAmountTransfer.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QuerySmallAmountTransferRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QuerySmallAmountTransferResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QuerySmallAmountTransfer", params, headers=headers)
            response = json.loads(body)
            model = models.QuerySmallAmountTransferResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryTrade(self, request):
        """跨境-贸易材料明细查询。

        :param request: Request instance for QueryTrade.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTrade", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryTransferBatch(self, request):
        """通过商家批次单号或者微信批次号查询批次单

        :param request: Request instance for QueryTransferBatch.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferBatchRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTransferBatch", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTransferBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryTransferDetail(self, request):
        """通过商家或者微信批次明细单号查询明细单

        :param request: Request instance for QueryTransferDetail.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferDetailRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTransferDetail", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTransferDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryTransferResult(self, request):
        """智能代发-单笔代发转账查询接口

        :param request: Request instance for QueryTransferResult.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferResultRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTransferResult", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTransferResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RechargeByThirdPay(self, request):
        """会员在途充值(经第三方支付渠道)接口

        :param request: Request instance for RechargeByThirdPay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RechargeByThirdPayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RechargeByThirdPayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RechargeByThirdPay", params, headers=headers)
            response = json.loads(body)
            model = models.RechargeByThirdPayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RechargeMemberThirdPay(self, request):
        """见证宝-会员在途充值(经第三方支付渠道)

        :param request: Request instance for RechargeMemberThirdPay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RechargeMemberThirdPayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RechargeMemberThirdPayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RechargeMemberThirdPay", params, headers=headers)
            response = json.loads(body)
            model = models.RechargeMemberThirdPayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Refund(self, request):
        """如交易订单需退款，可以通过本接口将支付款全部或部分退还给付款方，聚鑫将在收到退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。最长支持1年的订单退款。在订单包含多个子订单的情况下，如果使用本接口传入OutTradeNo或TransactionId退款，则只支持全单退款；如果需要部分退款，请通过传入子订单的方式来指定部分金额退款。

        :param request: Request instance for Refund.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RefundRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RefundResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Refund", params, headers=headers)
            response = json.loads(body)
            model = models.RefundResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RefundCloudOrder(self, request):
        """如交易订单需退款，可以通过本接口将支付款全部或部分退还给付款方，聚鑫将在收到退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。最长支持1年的订单退款。在订单包含多个子订单的情况下，如果使用本接口传入OutTradeNo或TransactionId退款，则只支持全单退款；如果需要部分退款，请通过传入子订单的方式来指定部分金额退款。

        :param request: Request instance for RefundCloudOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RefundCloudOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RefundCloudOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundCloudOrder", params, headers=headers)
            response = json.loads(body)
            model = models.RefundCloudOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RefundMemberTransaction(self, request):
        """会员间交易退款

        :param request: Request instance for RefundMemberTransaction.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RefundMemberTransactionRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RefundMemberTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundMemberTransaction", params, headers=headers)
            response = json.loads(body)
            model = models.RefundMemberTransactionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RefundOpenBankOrder(self, request):
        """云企付-退款申请

        :param request: Request instance for RefundOpenBankOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RefundOpenBankOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RefundOpenBankOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundOpenBankOrder", params, headers=headers)
            response = json.loads(body)
            model = models.RefundOpenBankOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RefundOrder(self, request):
        """云鉴-消费订单退款的接口

        :param request: Request instance for RefundOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RefundOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RefundOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundOrder", params, headers=headers)
            response = json.loads(body)
            model = models.RefundOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RefundTlinxOrder(self, request):
        """云支付订单退款接口

        :param request: Request instance for RefundTlinxOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RefundTlinxOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RefundTlinxOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundTlinxOrder", params, headers=headers)
            response = json.loads(body)
            model = models.RefundTlinxOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterBehavior(self, request):
        """商户查询是否签约和签约行为上报

        :param request: Request instance for RegisterBehavior.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RegisterBehaviorRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RegisterBehaviorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterBehavior", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterBehaviorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterBill(self, request):
        """登记挂账(支持撤销)

        :param request: Request instance for RegisterBill.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RegisterBillRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RegisterBillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterBill", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterBillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterBillSupportWithdraw(self, request):
        """登记挂账(支持撤销)。此接口可实现把不明来账或自有资金等已登记在挂账子账户下的资金调整到普通会员子账户。即通过申请调用此接口，将会减少挂账子账户的资金，调增指定的普通会员子账户的可提现余额及可用余额。此接口不支持把挂账子账户资金清分到功能子账户。

        :param request: Request instance for RegisterBillSupportWithdraw.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RegisterBillSupportWithdrawRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RegisterBillSupportWithdrawResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterBillSupportWithdraw", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterBillSupportWithdrawResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevResigterBillSupportWithdraw(self, request):
        """登记挂账撤销。此接口可以实现把RegisterBillSupportWithdraw接口完成的登记挂账进行撤销，即调减普通会员子账户的可提现和可用余额，调增挂账子账户的可用余额。

        :param request: Request instance for RevResigterBillSupportWithdraw.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RevResigterBillSupportWithdrawRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RevResigterBillSupportWithdrawResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevResigterBillSupportWithdraw", params, headers=headers)
            response = json.loads(body)
            model = models.RevResigterBillSupportWithdrawResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReviseMbrProperty(self, request):
        """修改会员属性-普通商户子账户。修改会员的会员属性。

        :param request: Request instance for ReviseMbrProperty.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ReviseMbrPropertyRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ReviseMbrPropertyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReviseMbrProperty", params, headers=headers)
            response = json.loads(body)
            model = models.ReviseMbrPropertyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevokeMemberRechargeThirdPay(self, request):
        """撤销会员在途充值(经第三方支付渠道)

        :param request: Request instance for RevokeMemberRechargeThirdPay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RevokeMemberRechargeThirdPayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RevokeMemberRechargeThirdPayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeMemberRechargeThirdPay", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeMemberRechargeThirdPayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevokeRechargeByThirdPay(self, request):
        """撤销会员在途充值(经第三方支付渠道)接口

        :param request: Request instance for RevokeRechargeByThirdPay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RevokeRechargeByThirdPayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RevokeRechargeByThirdPayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeRechargeByThirdPay", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeRechargeByThirdPayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncContractData(self, request):
        """对于存量的签约关系导入或者部分场景下米大师无法收到签约通知的场景，需要由调用方主动将签约状态同步至米大师

        :param request: Request instance for SyncContractData.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.SyncContractDataRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.SyncContractDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncContractData", params, headers=headers)
            response = json.loads(body)
            model = models.SyncContractDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateContract(self, request):
        """通过此接口进行解约

        :param request: Request instance for TerminateContract.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.TerminateContractRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.TerminateContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateContract", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransferSinglePay(self, request):
        """智能代发-单笔代发转账接口

        :param request: Request instance for TransferSinglePay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.TransferSinglePayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.TransferSinglePayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransferSinglePay", params, headers=headers)
            response = json.loads(body)
            model = models.TransferSinglePayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindAcct(self, request):
        """商户解除绑定的提现银行卡

        :param request: Request instance for UnBindAcct.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UnBindAcctRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UnBindAcctResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindAcct", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindAcctResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindOpenBankExternalSubMerchantBankAccount(self, request):
        """云企付-子商户银行卡解绑

        :param request: Request instance for UnbindOpenBankExternalSubMerchantBankAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UnbindOpenBankExternalSubMerchantBankAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UnbindOpenBankExternalSubMerchantBankAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindOpenBankExternalSubMerchantBankAccount", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindOpenBankExternalSubMerchantBankAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindRelateAcct(self, request):
        """会员解绑提现账户。此接口可以支持会员解除名下的绑定账户关系。

        :param request: Request instance for UnbindRelateAcct.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UnbindRelateAcctRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UnbindRelateAcctResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindRelateAcct", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindRelateAcctResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnifiedCloudOrder(self, request):
        """应用需要先调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。

        :param request: Request instance for UnifiedCloudOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UnifiedCloudOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UnifiedCloudOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnifiedCloudOrder", params, headers=headers)
            response = json.loads(body)
            model = models.UnifiedCloudOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnifiedOrder(self, request):
        """应用需要先调用本接口生成支付订单号，并将应答的PayInfo透传给聚鑫SDK，拉起客户端（包括微信公众号/微信小程序/客户端App）支付。

        :param request: Request instance for UnifiedOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UnifiedOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UnifiedOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnifiedOrder", params, headers=headers)
            response = json.loads(body)
            model = models.UnifiedOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnifiedTlinxOrder(self, request):
        """云支付-统一下单接口

        :param request: Request instance for UnifiedTlinxOrder.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UnifiedTlinxOrderRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UnifiedTlinxOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnifiedTlinxOrder", params, headers=headers)
            response = json.loads(body)
            model = models.UnifiedTlinxOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadExternalAnchorInfo(self, request):
        """灵云-上传主播信息

        :param request: Request instance for UploadExternalAnchorInfo.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UploadExternalAnchorInfoRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UploadExternalAnchorInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadExternalAnchorInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UploadExternalAnchorInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadFile(self, request):
        """直播平台-文件上传

        :param request: Request instance for UploadFile.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UploadFileRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UploadFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFile", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadOpenBankSubMerchantCredential(self, request):
        """云企付-子商户资质文件上传

        :param request: Request instance for UploadOpenBankSubMerchantCredential.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UploadOpenBankSubMerchantCredentialRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UploadOpenBankSubMerchantCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadOpenBankSubMerchantCredential", params, headers=headers)
            response = json.loads(body)
            model = models.UploadOpenBankSubMerchantCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadOrgFile(self, request):
        """云支付-上传机构文件接口

        :param request: Request instance for UploadOrgFile.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UploadOrgFileRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UploadOrgFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadOrgFile", params, headers=headers)
            response = json.loads(body)
            model = models.UploadOrgFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadTaxList(self, request):
        """直播平台-上传代理商完税列表

        :param request: Request instance for UploadTaxList.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UploadTaxListRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UploadTaxListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadTaxList", params, headers=headers)
            response = json.loads(body)
            model = models.UploadTaxListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadTaxPayment(self, request):
        """直播平台-上传代理商完税证明

        :param request: Request instance for UploadTaxPayment.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.UploadTaxPaymentRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.UploadTaxPaymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadTaxPayment", params, headers=headers)
            response = json.loads(body)
            model = models.UploadTaxPaymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VerifyOpenBankAccount(self, request):
        """云企付-子商户银行卡打款验证，在接入TENPAY渠道EBANK_PAYMENT付款时，若客户期望接入担保支付，需在接入前先完成，收款商户绑定的银行卡进行打款验证。验证成功后，才可以调用CreateOpenBankPaymentOrder接口进行担保支付下单。

        :param request: Request instance for VerifyOpenBankAccount.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.VerifyOpenBankAccountRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.VerifyOpenBankAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyOpenBankAccount", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyOpenBankAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ViewContract(self, request):
        """云支付-查询合同明细接口

        :param request: Request instance for ViewContract.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ViewContractRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ViewContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ViewContract", params, headers=headers)
            response = json.loads(body)
            model = models.ViewContractResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ViewMerchant(self, request):
        """云支付-查询商户明细接口

        :param request: Request instance for ViewMerchant.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ViewMerchantRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ViewMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ViewMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.ViewMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ViewShop(self, request):
        """云支付-查询门店明细接口

        :param request: Request instance for ViewShop.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.ViewShopRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.ViewShopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ViewShop", params, headers=headers)
            response = json.loads(body)
            model = models.ViewShopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WithdrawCashMembership(self, request):
        """会员提现-不验证。此接口受理会员发起的提现申请。会员子账户的可提现余额、可用余额会减少，市场的资金汇总账户(监管账户)会减少相应的发生金额，提现到会员申请的收款账户。

        :param request: Request instance for WithdrawCashMembership.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.WithdrawCashMembershipRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.WithdrawCashMembershipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WithdrawCashMembership", params, headers=headers)
            response = json.loads(body)
            model = models.WithdrawCashMembershipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)