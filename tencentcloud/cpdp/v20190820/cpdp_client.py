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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cpdp.v20190820 import models


class CpdpClient(AbstractClient):
    _apiVersion = '2019-08-20'
    _endpoint = 'cpdp.tencentcloudapi.com'


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


    def RevRegisterBillSupportWithdraw(self, request):
        """登记挂账撤销。此接口可以实现把RegisterBillSupportWithdraw接口完成的登记挂账进行撤销，即调减普通会员子账户的可提现和可用余额，调增挂账子账户的可用余额。

        :param request: Request instance for RevRegisterBillSupportWithdraw.
        :type request: :class:`tencentcloud.cpdp.v20190820.models.RevRegisterBillSupportWithdrawRequest`
        :rtype: :class:`tencentcloud.cpdp.v20190820.models.RevRegisterBillSupportWithdrawResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevRegisterBillSupportWithdraw", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevRegisterBillSupportWithdrawResponse()
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