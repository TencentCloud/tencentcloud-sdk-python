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
from tencentcloud.trp.v20210515 import models


class TrpClient(AbstractClient):
    _apiVersion = '2021-05-15'
    _endpoint = 'trp.tencentcloudapi.com'
    _service = 'trp'


    def AuthorizedTransfer(self, request):
        """接收客户侧的用户已授权的号码。

        :param request: Request instance for AuthorizedTransfer.
        :type request: :class:`tencentcloud.trp.v20210515.models.AuthorizedTransferRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.AuthorizedTransferResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthorizedTransfer", params, headers=headers)
            response = json.loads(body)
            model = models.AuthorizedTransferResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateChainBatch(self, request):
        """批量上链接口

        :param request: Request instance for CreateChainBatch.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateChainBatchRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateChainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodeBatch(self, request):
        """新增批次

        :param request: Request instance for CreateCodeBatch.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateCodeBatchRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateCodeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodeBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCodePack(self, request):
        """生成普通码包

        :param request: Request instance for CreateCodePack.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateCodePackRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateCodePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodePack", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCodePackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCorporationOrder(self, request):
        """以订单方式新建企业信息/配额信息

        :param request: Request instance for CreateCorporationOrder.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateCorporationOrderRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateCorporationOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCorporationOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCorporationOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomPack(self, request):
        """生成自定义码包

        :param request: Request instance for CreateCustomPack.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateCustomPackRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateCustomPackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomPack", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomPackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomRule(self, request):
        """新建自定义码规则

        :param request: Request instance for CreateCustomRule.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateCustomRuleRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMerchant(self, request):
        """新建商户

        :param request: Request instance for CreateMerchant.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateMerchantRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateMerchantResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProduct(self, request):
        """新建商品

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProduct", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTraceChain(self, request):
        """上链溯源信息

        :param request: Request instance for CreateTraceChain.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateTraceChainRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateTraceChainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceChain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTraceChainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTraceCodes(self, request):
        """批量绑定指定批次并激活二维码，只支持平台发的码，且只会激活没有使用过的码

        :param request: Request instance for CreateTraceCodes.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateTraceCodesRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateTraceCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceCodes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTraceCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTraceCodesAsync(self, request):
        """异步导入激活码包，如果是第三方码包，需要域名跟配置的匹配

        :param request: Request instance for CreateTraceCodesAsync.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateTraceCodesAsyncRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateTraceCodesAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceCodesAsync", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTraceCodesAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTraceData(self, request):
        """新增溯源信息

        :param request: Request instance for CreateTraceData.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateTraceDataRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateTraceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceData", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTraceDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCodeBatch(self, request):
        """删除批次

        :param request: Request instance for DeleteCodeBatch.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteCodeBatchRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteCodeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeBatch", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCodeBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMerchant(self, request):
        """删除商户

        :param request: Request instance for DeleteMerchant.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteMerchantRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMerchant", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMerchantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProduct(self, request):
        """删除商品，如果商品被使用，则不可删除

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTraceData(self, request):
        """删除溯源信息，如果已经上链则不可删除

        :param request: Request instance for DeleteTraceData.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteTraceDataRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteTraceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTraceData", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTraceDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentCorps(self, request):
        """查询渠道企业列表

        :param request: Request instance for DescribeAgentCorps.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeAgentCorpsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeAgentCorpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentCorps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentCorpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeBatchById(self, request):
        """查询批次信息

        :param request: Request instance for DescribeCodeBatchById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeBatchById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeBatchByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeBatches(self, request):
        """查询批次列表

        :param request: Request instance for DescribeCodeBatches.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchesRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeBatches", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeBatchesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodeBatchs(self, request):
        """查询批次列表

        旧版接口已经弃用，新业务请使用新版的接口 DescribeCodeBatches

        :param request: Request instance for DescribeCodeBatchs.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeBatchs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodeBatchsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodePackStatus(self, request):
        """查询码包状态

        :param request: Request instance for DescribeCodePackStatus.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodePackStatusRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodePackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodePackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodePackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodePackUrl(self, request):
        """查询码包地址

        :param request: Request instance for DescribeCodePackUrl.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodePackUrlRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodePackUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodePackUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodePackUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodePacks(self, request):
        """查询码包列表

        :param request: Request instance for DescribeCodePacks.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodePacksRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodePacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodePacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCodesByPack(self, request):
        """查询码包的二维码列表，上限 3 万

        :param request: Request instance for DescribeCodesByPack.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodesByPackRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodesByPackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodesByPack", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCodesByPackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCorpQuotas(self, request):
        """查询渠道商下属企业额度使用情况

        :param request: Request instance for DescribeCorpQuotas.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCorpQuotasRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCorpQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCorpQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCorpQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRuleById(self, request):
        """查自定义码规则

        :param request: Request instance for DescribeCustomRuleById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCustomRuleByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCustomRuleByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRuleById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRuleByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRules(self, request):
        """查自定义码规则列表

        :param request: Request instance for DescribeCustomRules.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCustomRulesRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCustomRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobFileUrl(self, request):
        """获取异步任务的输出地址

        :param request: Request instance for DescribeJobFileUrl.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeJobFileUrlRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeJobFileUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobFileUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobFileUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMerchantById(self, request):
        """查询商户信息

        :param request: Request instance for DescribeMerchantById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMerchantById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMerchantByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMerchants(self, request):
        """查询商户列表

        :param request: Request instance for DescribeMerchants.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMerchants", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMerchantsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlanQRCodeScanRecords(self, request):
        """查询安心计划二维码扫码记录

        :param request: Request instance for DescribePlanQRCodeScanRecords.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribePlanQRCodeScanRecordsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribePlanQRCodeScanRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlanQRCodeScanRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlanQRCodeScanRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlanQRCodes(self, request):
        """查询安心计划二维码列表

        :param request: Request instance for DescribePlanQRCodes.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribePlanQRCodesRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribePlanQRCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlanQRCodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlanQRCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductById(self, request):
        """查询商品信息

        :param request: Request instance for DescribeProductById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeProductByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeProductByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProducts(self, request):
        """查询商品列表

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProducts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRawScanLogs(self, request):
        """支持增量查询扫码日志，通常提供给数据同步使用，调用时需要指定从哪一行开始查询数据

        :param request: Request instance for DescribeRawScanLogs.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeRawScanLogsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeRawScanLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRawScanLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRawScanLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanLogs(self, request):
        """查询扫码日志明细

        :param request: Request instance for DescribeScanLogs.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeScanLogsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeScanLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanStats(self, request):
        """查询扫码的统计信息列表，支持按照商户ID，产品ID，批次ID，安心码筛选，筛选条件至少有一个
        没有被扫过的不会返回

        :param request: Request instance for DescribeScanStats.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeScanStatsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeScanStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTmpToken(self, request):
        """查询临时Token，主要用于上传接口

        :param request: Request instance for DescribeTmpToken.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTmpTokenRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTmpTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTmpToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTmpTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTraceCodeById(self, request):
        """查询二维码信息

        :param request: Request instance for DescribeTraceCodeById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodeByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodeByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceCodeById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTraceCodeByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTraceCodes(self, request):
        """查询二维码列表

        :param request: Request instance for DescribeTraceCodes.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodesRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceCodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTraceCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTraceDataById(self, request):
        """查询溯源ID查溯源信息，通常溯源信息跟生产批次绑定，即一个批次的所有溯源信息都是一样的

        :param request: Request instance for DescribeTraceDataById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTraceDataByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTraceDataByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceDataById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTraceDataByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTraceDataList(self, request):
        """查询溯源信息，通常溯源信息跟生产批次绑定，即一个批次的所有溯源信息都是一样的

        :param request: Request instance for DescribeTraceDataList.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTraceDataListRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTraceDataListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceDataList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTraceDataListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EffectFeedback(self, request):
        """接收客户反馈的各环节数据

        :param request: Request instance for EffectFeedback.
        :type request: :class:`tencentcloud.trp.v20210515.models.EffectFeedbackRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.EffectFeedbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EffectFeedback", params, headers=headers)
            response = json.loads(body)
            model = models.EffectFeedbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCodeBatch(self, request):
        """修改批次

        :param request: Request instance for ModifyCodeBatch.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyCodeBatchRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyCodeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCodeBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCodeBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomRule(self, request):
        """修改自定义码规则

        :param request: Request instance for ModifyCustomRule.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyCustomRuleRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomRuleStatus(self, request):
        """更新自定义码规则状态

        :param request: Request instance for ModifyCustomRuleStatus.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyCustomRuleStatusRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyCustomRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMerchant(self, request):
        """编辑商户

        :param request: Request instance for ModifyMerchant.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyMerchantRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyMerchantResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProduct(self, request):
        """编辑商品

        :param request: Request instance for ModifyProduct.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyProductRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProduct", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTraceCode(self, request):
        """冻结或者激活二维码，所属的批次的冻结状态优先级大于单个二维码的状态，即如果批次是冻结的，那么该批次下二维码的状态都是冻结的

        :param request: Request instance for ModifyTraceCode.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyTraceCodeRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyTraceCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTraceCode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTraceCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTraceCodeUnlink(self, request):
        """解绑溯源码和批次的关系，让溯源码重置为未关联的状态，以便关联其他批次
        注意：溯源码必须属于指定的批次才会解绑

        :param request: Request instance for ModifyTraceCodeUnlink.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyTraceCodeUnlinkRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyTraceCodeUnlinkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTraceCodeUnlink", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTraceCodeUnlinkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTraceData(self, request):
        """修改溯源信息

        :param request: Request instance for ModifyTraceData.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTraceData", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTraceDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTraceDataRanks(self, request):
        """修改溯源信息的排序

        :param request: Request instance for ModifyTraceDataRanks.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataRanksRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataRanksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTraceDataRanks", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTraceDataRanksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportBatchCallbackStatus(self, request):
        """接收离线筛选包回执，用于效果统计和分析。

        :param request: Request instance for ReportBatchCallbackStatus.
        :type request: :class:`tencentcloud.trp.v20210515.models.ReportBatchCallbackStatusRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ReportBatchCallbackStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportBatchCallbackStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ReportBatchCallbackStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))