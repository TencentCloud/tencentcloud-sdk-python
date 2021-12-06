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
            body = self.call("AddContract", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddContractResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("AddMerchant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddMerchantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("AddShop", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddShopResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ApplyApplicationMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyApplicationMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ApplyOutwardOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyOutwardOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ApplyPayerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyPayerInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ApplyReWithdrawal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyReWithdrawalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ApplyTrade", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyTradeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ApplyWithdrawal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyWithdrawalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("BindAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("BindAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("BindRelateAccReUnionPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRelateAccReUnionPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("BindRelateAcctSmallAmount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRelateAcctSmallAmountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("BindRelateAcctUnionPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRelateAcctUnionPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CheckAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CheckAmount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAmountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CloseOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ConfirmOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ConfirmOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ContractOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ContractOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateAgentTaxPaymentInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAgentTaxPaymentInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateAnchor", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAnchorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateBatchPayment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBatchPaymentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateCustAcctId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustAcctIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateExternalAnchor", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateExternalAnchorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateInvoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInvoiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateInvoiceV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInvoiceV2Response()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateMerchant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMerchantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreatePayMerchant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePayMerchantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateRedInvoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRedInvoiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateRedInvoiceV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRedInvoiceV2Response()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSinglePay(self, request):
        """银企直连-单笔支付接口

        :param request: Request instance for CreateSinglePay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.CreateSinglePayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.CreateSinglePayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSinglePay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSinglePayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateSinglePayment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSinglePaymentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateTransferBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTransferBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeduceQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeduceQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeleteAgentTaxPaymentInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAgentTaxPaymentInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeleteAgentTaxPaymentInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAgentTaxPaymentInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeChargeDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeChargeDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeOrderStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrderStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DistributeAccreditQuery", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeAccreditQueryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DistributeAccreditTlinx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeAccreditTlinxResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DistributeAddReceiver", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeAddReceiverResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DistributeApply", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeApplyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DistributeCancel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeCancelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DistributeQuery", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeQueryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DistributeQueryReceiver(self, request):
        """云支付-T查询已添加分账接收方接口

        :param request: Request instance for DistributeQueryReceiver.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.DistributeQueryReceiverRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.DistributeQueryReceiverResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DistributeQueryReceiver", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeQueryReceiverResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DistributeRemoveReceiver", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DistributeRemoveReceiverResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DownloadBill", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadBillResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DownloadOrgFile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadOrgFileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DownloadReconciliationUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadReconciliationUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ExecuteMemberTransaction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExecuteMemberTransactionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigrateOrderRefund(self, request):
        """山姆聚合支付项目-存量订单退款接口。可以通过本接口将支付款全部或部分退还给付款方，在收到用户退款请求并且验证成功之后，按照退款规则将支付款按原路退回到支付帐号。

        :param request: Request instance for MigrateOrderRefund.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.MigrateOrderRefundRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.MigrateOrderRefundResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MigrateOrderRefund", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigrateOrderRefundResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("MigrateOrderRefundQuery", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigrateOrderRefundQueryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyAgentTaxPaymentInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAgentTaxPaymentInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyBindedAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBindedAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyMerchant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMerchantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyMntMbrBindRelateAcctBankCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMntMbrBindRelateAcctBankCodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryAcctBinding", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAcctBindingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryAcctInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAcctInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryAcctInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAcctInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryAgentStatements", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAgentStatementsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryAgentTaxPaymentBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAgentTaxPaymentBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryAnchorContractInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAnchorContractInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryApplicationMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryApplicationMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryAssignment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAssignmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryBankClear", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBankClearResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryBankTransactionDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBankTransactionDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryBankWithdrawCashDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBankWithdrawCashDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryBatchPaymentResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBatchPaymentResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryBillDownloadURL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBillDownloadURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryCityCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCityCodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryCommonTransferRecharge", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCommonTransferRechargeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryContract", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryContractResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryContractPayFee", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryContractPayFeeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryContractPayWayList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryContractPayWayListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryContractRelateShop", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryContractRelateShopResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryCustAcctIdBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCustAcctIdBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryDownloadBillURL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryDownloadBillURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryExchangeRate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryExchangeRateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryInvoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryInvoiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryInvoiceV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryInvoiceV2Response()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMaliciousRegistration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMaliciousRegistrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMemberBind", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMemberBindResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMemberTransaction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMemberTransactionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMerchant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMerchantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMerchantBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMerchantBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMerchantClassification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMerchantClassificationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMerchantInfoForManagement", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMerchantInfoForManagementResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMerchantOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMerchantOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryMerchantPayWayList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMerchantPayWayListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryOrderStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryOrderStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryOutwardOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryOutwardOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryPayerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryPayerInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryReconciliationDocument", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryReconciliationDocumentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryRefund", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryRefundResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryShopOpenId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryShopOpenIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuerySinglePay(self, request):
        """银企直连-单笔支付状态查询接口

        :param request: Request instance for QuerySinglePay.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.QuerySinglePayRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.QuerySinglePayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QuerySinglePay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuerySinglePayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QuerySinglePaymentResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuerySinglePaymentResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QuerySingleTransactionStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuerySingleTransactionStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QuerySmallAmountTransfer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuerySmallAmountTransferResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryTrade", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryTradeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryTransferBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryTransferBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryTransferDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryTransferDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("QueryTransferResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryTransferResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RechargeByThirdPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RechargeByThirdPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RechargeMemberThirdPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RechargeMemberThirdPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("Refund", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RefundResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RefundMemberTransaction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RefundMemberTransactionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RefundOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RefundOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RefundTlinxOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RefundTlinxOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RegisterBehavior", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterBehaviorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RegisterBill", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterBillResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RegisterBillSupportWithdraw", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterBillSupportWithdrawResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RevResigterBillSupportWithdraw", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevResigterBillSupportWithdrawResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ReviseMbrProperty", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReviseMbrPropertyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RevokeMemberRechargeThirdPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevokeMemberRechargeThirdPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("RevokeRechargeByThirdPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevokeRechargeByThirdPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("SyncContractData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncContractDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("TerminateContract", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateContractResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("TransferSinglePay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransferSinglePayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UnBindAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UnbindRelateAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindRelateAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UnifiedOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnifiedOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UnifiedTlinxOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnifiedTlinxOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UploadExternalAnchorInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadExternalAnchorInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UploadFile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadFileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UploadOrgFile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadOrgFileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UploadTaxList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadTaxListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("UploadTaxPayment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadTaxPaymentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ViewContract", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ViewContractResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ViewMerchant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ViewMerchantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ViewShop", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ViewShopResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("WithdrawCashMembership", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WithdrawCashMembershipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)