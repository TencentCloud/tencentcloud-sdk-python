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
from tencentcloud.billing.v20180709 import models


class BillingClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'billing.tencentcloudapi.com'
    _service = 'billing'


    def CreateAllocationRule(self, request):
        """创建公摊规则

        :param request: Request instance for CreateAllocationRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateAllocationRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateAllocationRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllocationRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllocationRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAllocationTag(self, request):
        """批量设置分账标签

        :param request: Request instance for CreateAllocationTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateAllocationTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateAllocationTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllocationTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllocationTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAllocationUnit(self, request):
        """创建分账单元

        :param request: Request instance for CreateAllocationUnit.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateAllocationUnitRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateAllocationUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllocationUnit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllocationUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGatherRule(self, request):
        """创建归集规则

        :param request: Request instance for CreateGatherRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateGatherRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateGatherRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGatherRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGatherRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllocationRule(self, request):
        """公摊规则删除接口

        :param request: Request instance for DeleteAllocationRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllocationRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllocationRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllocationTag(self, request):
        """批量取消设置分账标签

        :param request: Request instance for DeleteAllocationTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllocationTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllocationTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllocationUnit(self, request):
        """删除分账单元

        :param request: Request instance for DeleteAllocationUnit.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationUnitRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllocationUnit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllocationUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGatherRule(self, request):
        """删除归集规则

        :param request: Request instance for DeleteGatherRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteGatherRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteGatherRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGatherRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGatherRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountBalance(self, request):
        """获取云账户余额信息。

        :param request: Request instance for DescribeAccountBalance.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAccountBalanceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountBalance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocateConditions(self, request):
        """查询资源目录筛选条件

        :param request: Request instance for DescribeAllocateConditions.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocateConditionsRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocateConditionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocateConditions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocateConditionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationBillConditions(self, request):
        """查询分账账单筛选条件

        :param request: Request instance for DescribeAllocationBillConditions.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationBillConditionsRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationBillConditionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationBillConditions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationBillConditionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationBillDetail(self, request):
        """查询分账账单明细

        :param request: Request instance for DescribeAllocationBillDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationBillDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationBillDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationBillDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationBillDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationMonthOverview(self, request):
        """查询分账账单月概览

        :param request: Request instance for DescribeAllocationMonthOverview.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationMonthOverviewRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationMonthOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationMonthOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationMonthOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationOverview(self, request):
        """查询分账账单日概览

        :param request: Request instance for DescribeAllocationOverview.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationOverviewRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationRuleDetail(self, request):
        """查询公摊规则详情

        :param request: Request instance for DescribeAllocationRuleDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationRuleSummary(self, request):
        """查询所有公摊规则概览

        :param request: Request instance for DescribeAllocationRuleSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationRuleSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationRuleSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationSummaryByBusiness(self, request):
        """查询分账账单按产品汇总

        :param request: Request instance for DescribeAllocationSummaryByBusiness.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationSummaryByBusinessRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationSummaryByBusinessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationSummaryByBusiness", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationSummaryByBusinessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationSummaryByItem(self, request):
        """查询分账账单按组件汇总

        :param request: Request instance for DescribeAllocationSummaryByItem.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationSummaryByItemRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationSummaryByItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationSummaryByItem", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationSummaryByItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationSummaryByResource(self, request):
        """查询分账账单按资源汇总

        :param request: Request instance for DescribeAllocationSummaryByResource.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationSummaryByResourceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationSummaryByResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationSummaryByResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationSummaryByResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationTree(self, request):
        """查询分账目录树

        :param request: Request instance for DescribeAllocationTree.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationTreeRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationTrendByMonth(self, request):
        """查询分账账单费用趋势

        :param request: Request instance for DescribeAllocationTrendByMonth.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationTrendByMonthRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationTrendByMonthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationTrendByMonth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationTrendByMonthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationUnitDetail(self, request):
        """查询分账单元详情

        :param request: Request instance for DescribeAllocationUnitDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationUnitDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationUnitDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationUnitDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationUnitDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillAdjustInfo(self, request):
        """可以通过API获取当前UIN是否有调账，客户可以更快地主动地获取调账情况。

        :param request: Request instance for DescribeBillAdjustInfo.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillAdjustInfoRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillAdjustInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillAdjustInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillAdjustInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDetail(self, request):
        """获取账单明细数据。
        注意事项：
        1.在请求接口时，由于网络不稳定或其它异常，可能会导致请求失败。如果您遇到这种情况，我们建议您在接口请求失败时，手动发起重试操作，这样可以更好地确保您的接口请求能够成功执行。
        2.对于账单明细数据量级很大（例如每月账单明细量级超过20w）的客户，通过 API 调用账单数据效率较低，建议您开通账单数据存储功能，通过存储桶中获取账单文件进行分析。[账单存储至COS桶](https://cloud.tencent.com/document/product/555/61275)

        :param request: Request instance for DescribeBillDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDetailForOrganization(self, request):
        """成员账号获取管理账号代付账单（费用明细）。
        注意事项：在请求接口时，由于网络不稳定或其它异常，可能会导致请求失败。如果您遇到这种情况，我们建议您在接口请求失败时，手动发起重试操作，这样可以更好地确保您的接口请求能够成功执行。

        :param request: Request instance for DescribeBillDetailForOrganization.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailForOrganizationRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailForOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDetailForOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDetailForOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDownloadUrl(self, request):
        """该接口支持通过传参，获取L0-PDF、L1-汇总、L2-资源、L3-明细、账单包、五类账单文件下载链接

        :param request: Request instance for DescribeBillDownloadUrl.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDownloadUrlRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillList(self, request):
        """获取收支明细列表，支持翻页和参数过滤

        :param request: Request instance for DescribeBillList.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillListRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillResourceSummary(self, request):
        """获取账单资源汇总数据

        :param request: Request instance for DescribeBillResourceSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillResourceSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillResourceSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillResourceSummaryForOrganization(self, request):
        """成员账号获取管理账号代付账单（按资源汇总）

        :param request: Request instance for DescribeBillResourceSummaryForOrganization.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryForOrganizationRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryForOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillResourceSummaryForOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillResourceSummaryForOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummary(self, request):
        """该接口支持通过传参，按照产品、项目、地域、计费模式和标签五个维度获取账单费用明细。

        :param request: Request instance for DescribeBillSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByPayMode(self, request):
        """获取按计费模式汇总费用分布

        :param request: Request instance for DescribeBillSummaryByPayMode.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByPayMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByPayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByProduct(self, request):
        """获取产品汇总费用分布

        :param request: Request instance for DescribeBillSummaryByProduct.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByProject(self, request):
        """获取按项目汇总费用分布

        :param request: Request instance for DescribeBillSummaryByProject.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByRegion(self, request):
        """获取按地域汇总费用分布

        :param request: Request instance for DescribeBillSummaryByRegion.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByTag(self, request):
        """获取按标签汇总费用分布

        :param request: Request instance for DescribeBillSummaryByTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByTag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryForOrganization(self, request):
        """该接口支持通过传参，按照产品、项目、地域、计费模式和标签五个维度获取账单费用明细。

        :param request: Request instance for DescribeBillSummaryForOrganization.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryForOrganizationRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryForOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryForOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryForOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostDetail(self, request):
        """查询消耗明细

        注意事项：
        1. 对于消耗明细数据量级很大（例如每月消耗明细量级超过100w）的客户，通过 API 调用明细数据会有超时风险，建议您开通消耗账单数据存储功能，通过存储桶中获取账单文件进行分析。[账单存储至COS桶](https://cloud.tencent.com/document/product/555/61275)

        :param request: Request instance for DescribeCostDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostExplorerSummary(self, request):
        """查看成本分析明细

        :param request: Request instance for DescribeCostExplorerSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostExplorerSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostExplorerSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostExplorerSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostExplorerSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByProduct(self, request):
        """获取按产品汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByProduct.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProductRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByProject(self, request):
        """获取按项目汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByProject.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProjectRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByRegion(self, request):
        """获取按地域汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByRegion.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByResource(self, request):
        """获取按资源汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByResource.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByResourceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDealsByCond(self, request):
        """查询订单

        :param request: Request instance for DescribeDealsByCond.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDealsByCondRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDealsByCondResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDealsByCond", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDealsByCondResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDosageCosDetailByDate(self, request):
        """获取COS产品用量明细

        :param request: Request instance for DescribeDosageCosDetailByDate.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDosageCosDetailByDateRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDosageCosDetailByDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDosageCosDetailByDate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDosageCosDetailByDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDosageDetailByDate(self, request):
        """按日期获取产品用量明细

        :param request: Request instance for DescribeDosageDetailByDate.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDosageDetailByDateRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDosageDetailByDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDosageDetailByDate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDosageDetailByDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDosageDetailList(self, request):
        """获取已接入标准用量明细模板产品的用量明细数据，目前已接入并支持查询的产品包括：云联络中心、实时音视频、实时音视频、智能媒资托管、CODING DevOps、全球IP应用加速

        :param request: Request instance for DescribeDosageDetailList.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDosageDetailListRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDosageDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDosageDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDosageDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatherResource(self, request):
        """查询分账账单资源归集汇总

        :param request: Request instance for DescribeGatherResource.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeGatherResourceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeGatherResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatherResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatherResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatherRuleDetail(self, request):
        """查询归集规则详情

        :param request: Request instance for DescribeGatherRuleDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeGatherRuleDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeGatherRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatherRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatherRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSavingPlanResourceInfo(self, request):
        """查询节省计划详情

        :param request: Request instance for DescribeSavingPlanResourceInfo.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeSavingPlanResourceInfoRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeSavingPlanResourceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSavingPlanResourceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSavingPlanResourceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagList(self, request):
        """获取分账标签

        :param request: Request instance for DescribeTagList.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeTagListRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeTagListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVoucherInfo(self, request):
        """获取代金券相关信息

        :param request: Request instance for DescribeVoucherInfo.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherInfoRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVoucherInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVoucherInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVoucherUsageDetails(self, request):
        """获取代金券使用记录

        :param request: Request instance for DescribeVoucherUsageDetails.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherUsageDetailsRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherUsageDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVoucherUsageDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVoucherUsageDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllocationRule(self, request):
        """编辑公摊规则

        :param request: Request instance for ModifyAllocationRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllocationRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllocationRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllocationUnit(self, request):
        """修改分账单元信息

        :param request: Request instance for ModifyAllocationUnit.
        :type request: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationUnitRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllocationUnit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllocationUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGatherRule(self, request):
        """编辑归集规则

        :param request: Request instance for ModifyGatherRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.ModifyGatherRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.ModifyGatherRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGatherRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGatherRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PayDeals(self, request):
        """支付订单

        :param request: Request instance for PayDeals.
        :type request: :class:`tencentcloud.billing.v20180709.models.PayDealsRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.PayDealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PayDeals", params, headers=headers)
            response = json.loads(body)
            model = models.PayDealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))