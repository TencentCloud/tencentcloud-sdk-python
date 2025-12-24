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
from tencentcloud.billing.v20180709 import models
from typing import Dict


class BillingClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'billing.tencentcloudapi.com'
    _service = 'billing'

    async def CreateAllocationRule(
            self,
            request: models.CreateAllocationRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAllocationRuleResponse:
        """
        创建公摊规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllocationRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllocationRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAllocationTag(
            self,
            request: models.CreateAllocationTagRequest,
            opts: Dict = None,
    ) -> models.CreateAllocationTagResponse:
        """
        批量设置分账标签
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllocationTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllocationTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAllocationUnit(
            self,
            request: models.CreateAllocationUnitRequest,
            opts: Dict = None,
    ) -> models.CreateAllocationUnitResponse:
        """
        创建分账单元
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllocationUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllocationUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBudget(
            self,
            request: models.CreateBudgetRequest,
            opts: Dict = None,
    ) -> models.CreateBudgetResponse:
        """
        创建预算信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBudget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBudgetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGatherRule(
            self,
            request: models.CreateGatherRuleRequest,
            opts: Dict = None,
    ) -> models.CreateGatherRuleResponse:
        """
        创建归集规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGatherRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGatherRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllocationRule(
            self,
            request: models.DeleteAllocationRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAllocationRuleResponse:
        """
        公摊规则删除接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllocationRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllocationRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllocationTag(
            self,
            request: models.DeleteAllocationTagRequest,
            opts: Dict = None,
    ) -> models.DeleteAllocationTagResponse:
        """
        批量取消设置分账标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllocationTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllocationTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllocationUnit(
            self,
            request: models.DeleteAllocationUnitRequest,
            opts: Dict = None,
    ) -> models.DeleteAllocationUnitResponse:
        """
        删除分账单元
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllocationUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllocationUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBudget(
            self,
            request: models.DeleteBudgetRequest,
            opts: Dict = None,
    ) -> models.DeleteBudgetResponse:
        """
        依据预算ID删除对应预算项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBudget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBudgetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGatherRule(
            self,
            request: models.DeleteGatherRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteGatherRuleResponse:
        """
        删除归集规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGatherRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGatherRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountBalance(
            self,
            request: models.DescribeAccountBalanceRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountBalanceResponse:
        """
        获取云账户余额信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocateConditions(
            self,
            request: models.DescribeAllocateConditionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocateConditionsResponse:
        """
        查询资源目录筛选条件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocateConditions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocateConditionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationBillConditions(
            self,
            request: models.DescribeAllocationBillConditionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationBillConditionsResponse:
        """
        查询分账账单筛选条件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationBillConditions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationBillConditionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationBillDetail(
            self,
            request: models.DescribeAllocationBillDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationBillDetailResponse:
        """
        查询分账账单明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationBillDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationBillDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationMonthOverview(
            self,
            request: models.DescribeAllocationMonthOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationMonthOverviewResponse:
        """
        查询分账账单月概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationMonthOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationMonthOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationOverview(
            self,
            request: models.DescribeAllocationOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationOverviewResponse:
        """
        查询分账账单日概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationRuleDetail(
            self,
            request: models.DescribeAllocationRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationRuleDetailResponse:
        """
        查询公摊规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationRuleSummary(
            self,
            request: models.DescribeAllocationRuleSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationRuleSummaryResponse:
        """
        查询所有公摊规则概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationRuleSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationRuleSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationSummaryByBusiness(
            self,
            request: models.DescribeAllocationSummaryByBusinessRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationSummaryByBusinessResponse:
        """
        查询分账账单按产品汇总
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationSummaryByBusiness"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationSummaryByBusinessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationSummaryByItem(
            self,
            request: models.DescribeAllocationSummaryByItemRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationSummaryByItemResponse:
        """
        查询分账账单按组件汇总
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationSummaryByItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationSummaryByItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationSummaryByResource(
            self,
            request: models.DescribeAllocationSummaryByResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationSummaryByResourceResponse:
        """
        查询分账账单按资源汇总
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationSummaryByResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationSummaryByResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationTree(
            self,
            request: models.DescribeAllocationTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationTreeResponse:
        """
        查询分账目录树
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationTrendByMonth(
            self,
            request: models.DescribeAllocationTrendByMonthRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationTrendByMonthResponse:
        """
        查询分账账单费用趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationTrendByMonth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationTrendByMonthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationUnitDetail(
            self,
            request: models.DescribeAllocationUnitDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationUnitDetailResponse:
        """
        查询分账单元详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationUnitDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationUnitDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillAdjustInfo(
            self,
            request: models.DescribeBillAdjustInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBillAdjustInfoResponse:
        """
        可以通过API获取当前UIN是否有调账，客户可以更快地主动地获取调账情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillAdjustInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillAdjustInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDetail(
            self,
            request: models.DescribeBillDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDetailResponse:
        """
        获取账单明细数据。
        注意事项：
        1.在请求接口时，由于网络不稳定或其它异常，可能会导致请求失败。如果您遇到这种情况，我们建议您在接口请求失败时，手动发起重试操作，这样可以更好地确保您的接口请求能够成功执行。
        2.对于账单明细数据量级很大（例如每月账单明细量级超过20w）的客户，通过 API 调用账单数据效率较低，建议您开通账单数据存储功能，通过存储桶中获取账单文件进行分析。[账单存储至COS桶](https://cloud.tencent.com/document/product/555/61275)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDetailForOrganization(
            self,
            request: models.DescribeBillDetailForOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDetailForOrganizationResponse:
        """
        成员账号获取管理账号代付账单（费用明细）。
        注意事项：在请求接口时，由于网络不稳定或其它异常，可能会导致请求失败。如果您遇到这种情况，我们建议您在接口请求失败时，手动发起重试操作，这样可以更好地确保您的接口请求能够成功执行。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDetailForOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDetailForOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDownloadUrl(
            self,
            request: models.DescribeBillDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDownloadUrlResponse:
        """
        该接口支持通过传参，获取L0-PDF、L1-汇总、L2-资源、L3-明细、账单包、五类账单文件下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillList(
            self,
            request: models.DescribeBillListRequest,
            opts: Dict = None,
    ) -> models.DescribeBillListResponse:
        """
        获取收支明细列表，支持翻页和参数过滤
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillResourceSummary(
            self,
            request: models.DescribeBillResourceSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeBillResourceSummaryResponse:
        """
        获取账单资源汇总数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillResourceSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillResourceSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillResourceSummaryForOrganization(
            self,
            request: models.DescribeBillResourceSummaryForOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeBillResourceSummaryForOrganizationResponse:
        """
        成员账号获取管理账号代付账单（按资源汇总）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillResourceSummaryForOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillResourceSummaryForOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummary(
            self,
            request: models.DescribeBillSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryResponse:
        """
        该接口支持通过传参，按照产品、项目、地域、计费模式和标签五个维度获取账单费用明细。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByPayMode(
            self,
            request: models.DescribeBillSummaryByPayModeRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByPayModeResponse:
        """
        获取按计费模式汇总费用分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByPayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByPayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByProduct(
            self,
            request: models.DescribeBillSummaryByProductRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByProductResponse:
        """
        获取产品汇总费用分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByProject(
            self,
            request: models.DescribeBillSummaryByProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByProjectResponse:
        """
        获取按项目汇总费用分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByRegion(
            self,
            request: models.DescribeBillSummaryByRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByRegionResponse:
        """
        获取按地域汇总费用分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByTag(
            self,
            request: models.DescribeBillSummaryByTagRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByTagResponse:
        """
        获取按标签汇总费用分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryForOrganization(
            self,
            request: models.DescribeBillSummaryForOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryForOrganizationResponse:
        """
        该接口支持通过传参，按照产品、项目、地域、计费模式和标签五个维度获取账单费用明细。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryForOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryForOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBudget(
            self,
            request: models.DescribeBudgetRequest,
            opts: Dict = None,
    ) -> models.DescribeBudgetResponse:
        """
        获取预算详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBudget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBudgetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBudgetOperationLog(
            self,
            request: models.DescribeBudgetOperationLogRequest,
            opts: Dict = None,
    ) -> models.DescribeBudgetOperationLogResponse:
        """
        查询预算修改记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBudgetOperationLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBudgetOperationLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBudgetRemindRecordList(
            self,
            request: models.DescribeBudgetRemindRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeBudgetRemindRecordListResponse:
        """
        返回预算提醒记录，包括预算周期、检测时间、提醒时间、提醒类型、提醒内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBudgetRemindRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBudgetRemindRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostDetail(
            self,
            request: models.DescribeCostDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCostDetailResponse:
        """
        查询消耗明细

        注意事项：
        1. 对于消耗明细数据量级很大（例如每月消耗明细量级超过100w）的客户，通过 API 调用明细数据会有超时风险，建议您开通消耗账单数据存储功能，通过存储桶中获取账单文件进行分析。[账单存储至COS桶](https://cloud.tencent.com/document/product/555/61275)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostExplorerSummary(
            self,
            request: models.DescribeCostExplorerSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCostExplorerSummaryResponse:
        """
        查看成本分析明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostExplorerSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostExplorerSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByProduct(
            self,
            request: models.DescribeCostSummaryByProductRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByProductResponse:
        """
        获取按产品汇总消耗详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByProject(
            self,
            request: models.DescribeCostSummaryByProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByProjectResponse:
        """
        获取按项目汇总消耗详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByRegion(
            self,
            request: models.DescribeCostSummaryByRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByRegionResponse:
        """
        获取按地域汇总消耗详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByResource(
            self,
            request: models.DescribeCostSummaryByResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByResourceResponse:
        """
        获取按资源汇总消耗详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByTag(
            self,
            request: models.DescribeCostSummaryByTagRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByTagResponse:
        """
        获取按标签汇总消耗详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDealsByCond(
            self,
            request: models.DescribeDealsByCondRequest,
            opts: Dict = None,
    ) -> models.DescribeDealsByCondResponse:
        """
        查询订单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDealsByCond"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDealsByCondResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDosageCosDetailByDate(
            self,
            request: models.DescribeDosageCosDetailByDateRequest,
            opts: Dict = None,
    ) -> models.DescribeDosageCosDetailByDateResponse:
        """
        获取COS产品用量明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDosageCosDetailByDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDosageCosDetailByDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDosageDetailByDate(
            self,
            request: models.DescribeDosageDetailByDateRequest,
            opts: Dict = None,
    ) -> models.DescribeDosageDetailByDateResponse:
        """
        按日期获取产品用量明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDosageDetailByDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDosageDetailByDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDosageDetailList(
            self,
            request: models.DescribeDosageDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeDosageDetailListResponse:
        """
        获取已接入标准用量明细模板产品的用量明细数据，目前已接入并支持查询的产品包括：云联络中心、实时音视频、实时音视频、智能媒资托管、CODING DevOps、全球IP应用加速
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDosageDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDosageDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatherResource(
            self,
            request: models.DescribeGatherResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeGatherResourceResponse:
        """
        查询分账账单资源归集汇总
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatherResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatherResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatherRuleDetail(
            self,
            request: models.DescribeGatherRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeGatherRuleDetailResponse:
        """
        查询归集规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatherRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatherRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSavingPlanResourceInfo(
            self,
            request: models.DescribeSavingPlanResourceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSavingPlanResourceInfoResponse:
        """
        查询节省计划详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSavingPlanResourceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSavingPlanResourceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagList(
            self,
            request: models.DescribeTagListRequest,
            opts: Dict = None,
    ) -> models.DescribeTagListResponse:
        """
        获取分账标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVoucherInfo(
            self,
            request: models.DescribeVoucherInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVoucherInfoResponse:
        """
        获取代金券相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVoucherInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVoucherInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVoucherUsageDetails(
            self,
            request: models.DescribeVoucherUsageDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeVoucherUsageDetailsResponse:
        """
        获取代金券使用记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVoucherUsageDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVoucherUsageDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllocationRule(
            self,
            request: models.ModifyAllocationRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAllocationRuleResponse:
        """
        编辑公摊规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllocationRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllocationRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllocationUnit(
            self,
            request: models.ModifyAllocationUnitRequest,
            opts: Dict = None,
    ) -> models.ModifyAllocationUnitResponse:
        """
        修改分账单元信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllocationUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllocationUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBudget(
            self,
            request: models.ModifyBudgetRequest,
            opts: Dict = None,
    ) -> models.ModifyBudgetResponse:
        """
        更新预算信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBudget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBudgetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatherRule(
            self,
            request: models.ModifyGatherRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyGatherRuleResponse:
        """
        编辑归集规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatherRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatherRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PayDeals(
            self,
            request: models.PayDealsRequest,
            opts: Dict = None,
    ) -> models.PayDealsResponse:
        """
        支付订单
        """
        
        kwargs = {}
        kwargs["action"] = "PayDeals"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PayDealsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)