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
from tencentcloud.trp.v20210515 import models
from typing import Dict


class TrpClient(AbstractClient):
    _apiVersion = '2021-05-15'
    _endpoint = 'trp.tencentcloudapi.com'
    _service = 'trp'

    async def AuthorizedTransfer(
            self,
            request: models.AuthorizedTransferRequest,
            opts: Dict = None,
    ) -> models.AuthorizedTransferResponse:
        """
        接收客户侧的用户已授权的号码。
        """
        
        kwargs = {}
        kwargs["action"] = "AuthorizedTransfer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuthorizedTransferResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateChainBatch(
            self,
            request: models.CreateChainBatchRequest,
            opts: Dict = None,
    ) -> models.CreateChainBatchResponse:
        """
        批量上链接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateChainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateChainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCodeBatch(
            self,
            request: models.CreateCodeBatchRequest,
            opts: Dict = None,
    ) -> models.CreateCodeBatchResponse:
        """
        新增批次
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCodePack(
            self,
            request: models.CreateCodePackRequest,
            opts: Dict = None,
    ) -> models.CreateCodePackResponse:
        """
        生成普通码包
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCorporationOrder(
            self,
            request: models.CreateCorporationOrderRequest,
            opts: Dict = None,
    ) -> models.CreateCorporationOrderResponse:
        """
        以订单方式新建企业信息/配额信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCorporationOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCorporationOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomPack(
            self,
            request: models.CreateCustomPackRequest,
            opts: Dict = None,
    ) -> models.CreateCustomPackResponse:
        """
        生成自定义码包
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomPack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomPackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomRule(
            self,
            request: models.CreateCustomRuleRequest,
            opts: Dict = None,
    ) -> models.CreateCustomRuleResponse:
        """
        新建自定义码规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMerchant(
            self,
            request: models.CreateMerchantRequest,
            opts: Dict = None,
    ) -> models.CreateMerchantResponse:
        """
        新建商户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProduct(
            self,
            request: models.CreateProductRequest,
            opts: Dict = None,
    ) -> models.CreateProductResponse:
        """
        新建商品
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTraceChain(
            self,
            request: models.CreateTraceChainRequest,
            opts: Dict = None,
    ) -> models.CreateTraceChainResponse:
        """
        上链溯源信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTraceChain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTraceChainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTraceCodes(
            self,
            request: models.CreateTraceCodesRequest,
            opts: Dict = None,
    ) -> models.CreateTraceCodesResponse:
        """
        批量绑定指定批次并激活二维码，只支持平台发的码，且只会激活没有使用过的码
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTraceCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTraceCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTraceCodesAsync(
            self,
            request: models.CreateTraceCodesAsyncRequest,
            opts: Dict = None,
    ) -> models.CreateTraceCodesAsyncResponse:
        """
        异步导入激活码包，如果是第三方码包，需要域名跟配置的匹配
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTraceCodesAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTraceCodesAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTraceData(
            self,
            request: models.CreateTraceDataRequest,
            opts: Dict = None,
    ) -> models.CreateTraceDataResponse:
        """
        新增溯源信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTraceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTraceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCodeBatch(
            self,
            request: models.DeleteCodeBatchRequest,
            opts: Dict = None,
    ) -> models.DeleteCodeBatchResponse:
        """
        删除批次
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodeBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodeBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMerchant(
            self,
            request: models.DeleteMerchantRequest,
            opts: Dict = None,
    ) -> models.DeleteMerchantResponse:
        """
        删除商户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProduct(
            self,
            request: models.DeleteProductRequest,
            opts: Dict = None,
    ) -> models.DeleteProductResponse:
        """
        删除商品，如果商品被使用，则不可删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTraceData(
            self,
            request: models.DeleteTraceDataRequest,
            opts: Dict = None,
    ) -> models.DeleteTraceDataResponse:
        """
        删除溯源信息，如果已经上链则不可删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTraceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTraceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentCorps(
            self,
            request: models.DescribeAgentCorpsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentCorpsResponse:
        """
        查询渠道企业列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentCorps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentCorpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodeBatchById(
            self,
            request: models.DescribeCodeBatchByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeCodeBatchByIdResponse:
        """
        查询批次信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodeBatchById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodeBatchByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodeBatches(
            self,
            request: models.DescribeCodeBatchesRequest,
            opts: Dict = None,
    ) -> models.DescribeCodeBatchesResponse:
        """
        查询批次列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodeBatches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodeBatchesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodeBatchs(
            self,
            request: models.DescribeCodeBatchsRequest,
            opts: Dict = None,
    ) -> models.DescribeCodeBatchsResponse:
        """
        查询批次列表

        旧版接口已经弃用，新业务请使用新版的接口 DescribeCodeBatches
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodeBatchs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodeBatchsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodePackStatus(
            self,
            request: models.DescribeCodePackStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCodePackStatusResponse:
        """
        查询码包状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodePackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodePackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodePackUrl(
            self,
            request: models.DescribeCodePackUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeCodePackUrlResponse:
        """
        查询码包地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodePackUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodePackUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodePacks(
            self,
            request: models.DescribeCodePacksRequest,
            opts: Dict = None,
    ) -> models.DescribeCodePacksResponse:
        """
        查询码包列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodesByPack(
            self,
            request: models.DescribeCodesByPackRequest,
            opts: Dict = None,
    ) -> models.DescribeCodesByPackResponse:
        """
        查询码包的二维码列表，上限 3 万
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodesByPack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodesByPackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCorpQuotas(
            self,
            request: models.DescribeCorpQuotasRequest,
            opts: Dict = None,
    ) -> models.DescribeCorpQuotasResponse:
        """
        查询渠道商下属企业额度使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCorpQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCorpQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRuleById(
            self,
            request: models.DescribeCustomRuleByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRuleByIdResponse:
        """
        查自定义码规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRuleById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRuleByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomRules(
            self,
            request: models.DescribeCustomRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomRulesResponse:
        """
        查自定义码规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobFileUrl(
            self,
            request: models.DescribeJobFileUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeJobFileUrlResponse:
        """
        获取异步任务的输出地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobFileUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobFileUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMerchantById(
            self,
            request: models.DescribeMerchantByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeMerchantByIdResponse:
        """
        查询商户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMerchantById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMerchantByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMerchants(
            self,
            request: models.DescribeMerchantsRequest,
            opts: Dict = None,
    ) -> models.DescribeMerchantsResponse:
        """
        查询商户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMerchants"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMerchantsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlanQRCodeScanRecords(
            self,
            request: models.DescribePlanQRCodeScanRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribePlanQRCodeScanRecordsResponse:
        """
        查询安心计划二维码扫码记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlanQRCodeScanRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlanQRCodeScanRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlanQRCodes(
            self,
            request: models.DescribePlanQRCodesRequest,
            opts: Dict = None,
    ) -> models.DescribePlanQRCodesResponse:
        """
        查询安心计划二维码列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlanQRCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlanQRCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductById(
            self,
            request: models.DescribeProductByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeProductByIdResponse:
        """
        查询商品信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProducts(
            self,
            request: models.DescribeProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeProductsResponse:
        """
        查询商品列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRawScanLogs(
            self,
            request: models.DescribeRawScanLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeRawScanLogsResponse:
        """
        支持增量查询扫码日志，通常提供给数据同步使用，调用时需要指定从哪一行开始查询数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRawScanLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRawScanLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanLogs(
            self,
            request: models.DescribeScanLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeScanLogsResponse:
        """
        查询扫码日志明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanStats(
            self,
            request: models.DescribeScanStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeScanStatsResponse:
        """
        查询扫码的统计信息列表，支持按照商户ID，产品ID，批次ID，安心码筛选，筛选条件至少有一个
        没有被扫过的不会返回
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTmpToken(
            self,
            request: models.DescribeTmpTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeTmpTokenResponse:
        """
        查询临时Token，主要用于上传接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTmpToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTmpTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTraceCodeById(
            self,
            request: models.DescribeTraceCodeByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeTraceCodeByIdResponse:
        """
        查询二维码信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTraceCodeById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTraceCodeByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTraceCodes(
            self,
            request: models.DescribeTraceCodesRequest,
            opts: Dict = None,
    ) -> models.DescribeTraceCodesResponse:
        """
        查询二维码列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTraceCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTraceCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTraceDataById(
            self,
            request: models.DescribeTraceDataByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeTraceDataByIdResponse:
        """
        查询溯源ID查溯源信息，通常溯源信息跟生产批次绑定，即一个批次的所有溯源信息都是一样的
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTraceDataById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTraceDataByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTraceDataList(
            self,
            request: models.DescribeTraceDataListRequest,
            opts: Dict = None,
    ) -> models.DescribeTraceDataListResponse:
        """
        查询溯源信息，通常溯源信息跟生产批次绑定，即一个批次的所有溯源信息都是一样的
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTraceDataList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTraceDataListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EffectFeedback(
            self,
            request: models.EffectFeedbackRequest,
            opts: Dict = None,
    ) -> models.EffectFeedbackResponse:
        """
        接收客户反馈的各环节数据
        """
        
        kwargs = {}
        kwargs["action"] = "EffectFeedback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EffectFeedbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCodeBatch(
            self,
            request: models.ModifyCodeBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyCodeBatchResponse:
        """
        修改批次
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCodeBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCodeBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomRule(
            self,
            request: models.ModifyCustomRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomRuleResponse:
        """
        修改自定义码规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomRuleStatus(
            self,
            request: models.ModifyCustomRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomRuleStatusResponse:
        """
        更新自定义码规则状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMerchant(
            self,
            request: models.ModifyMerchantRequest,
            opts: Dict = None,
    ) -> models.ModifyMerchantResponse:
        """
        编辑商户
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMerchant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMerchantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProduct(
            self,
            request: models.ModifyProductRequest,
            opts: Dict = None,
    ) -> models.ModifyProductResponse:
        """
        编辑商品
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTraceCode(
            self,
            request: models.ModifyTraceCodeRequest,
            opts: Dict = None,
    ) -> models.ModifyTraceCodeResponse:
        """
        冻结或者激活二维码，所属的批次的冻结状态优先级大于单个二维码的状态，即如果批次是冻结的，那么该批次下二维码的状态都是冻结的
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTraceCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTraceCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTraceCodeUnlink(
            self,
            request: models.ModifyTraceCodeUnlinkRequest,
            opts: Dict = None,
    ) -> models.ModifyTraceCodeUnlinkResponse:
        """
        解绑溯源码和批次的关系，让溯源码重置为未关联的状态，以便关联其他批次
        注意：溯源码必须属于指定的批次才会解绑
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTraceCodeUnlink"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTraceCodeUnlinkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTraceData(
            self,
            request: models.ModifyTraceDataRequest,
            opts: Dict = None,
    ) -> models.ModifyTraceDataResponse:
        """
        修改溯源信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTraceData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTraceDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTraceDataRanks(
            self,
            request: models.ModifyTraceDataRanksRequest,
            opts: Dict = None,
    ) -> models.ModifyTraceDataRanksResponse:
        """
        修改溯源信息的排序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTraceDataRanks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTraceDataRanksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportBatchCallbackStatus(
            self,
            request: models.ReportBatchCallbackStatusRequest,
            opts: Dict = None,
    ) -> models.ReportBatchCallbackStatusResponse:
        """
        接收离线筛选包回执，用于效果统计和分析。
        """
        
        kwargs = {}
        kwargs["action"] = "ReportBatchCallbackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportBatchCallbackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)