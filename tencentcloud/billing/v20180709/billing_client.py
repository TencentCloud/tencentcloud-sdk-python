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


    def DescribeAccountBalance(self, request):
        """获取云账户余额信息。

        :param request: Request instance for DescribeAccountBalance.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAccountBalanceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountBalanceResponse()
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


    def DescribeBillDetail(self, request):
        """查询账单明细数据

        :param request: Request instance for DescribeBillDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillDetailResponse()
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


    def DescribeBillList(self, request):
        """获取收支明细列表，支持翻页和参数过滤

        :param request: Request instance for DescribeBillList.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillListRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillListResponse()
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


    def DescribeBillResourceSummary(self, request):
        """查询账单资源汇总数据

        :param request: Request instance for DescribeBillResourceSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillResourceSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillResourceSummaryResponse()
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


    def DescribeBillSummaryByPayMode(self, request):
        """获取按付费模式汇总费用分布

        :param request: Request instance for DescribeBillSummaryByPayMode.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByPayMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByPayModeResponse()
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


    def DescribeBillSummaryByProduct(self, request):
        """获取产品汇总费用分布

        :param request: Request instance for DescribeBillSummaryByProduct.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByProductResponse()
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


    def DescribeBillSummaryByProject(self, request):
        """获取按项目汇总费用分布

        :param request: Request instance for DescribeBillSummaryByProject.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByProjectResponse()
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


    def DescribeBillSummaryByRegion(self, request):
        """获取按地域汇总费用分布

        :param request: Request instance for DescribeBillSummaryByRegion.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByRegionResponse()
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


    def DescribeBillSummaryByTag(self, request):
        """获取按标签汇总费用分布

        :param request: Request instance for DescribeBillSummaryByTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByTagResponse()
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


    def DescribeCostDetail(self, request):
        """查询消耗明细

        :param request: Request instance for DescribeCostDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCostDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCostDetailResponse()
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


    def DescribeCostSummaryByProduct(self, request):
        """获取按产品汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByProduct.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProductRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCostSummaryByProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCostSummaryByProductResponse()
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


    def DescribeCostSummaryByProject(self, request):
        """获取按项目汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByProject.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProjectRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCostSummaryByProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCostSummaryByProjectResponse()
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


    def DescribeCostSummaryByRegion(self, request):
        """获取按地域汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByRegion.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCostSummaryByRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCostSummaryByRegionResponse()
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


    def DescribeCostSummaryByResource(self, request):
        """获取按资源汇总消耗详情

        :param request: Request instance for DescribeCostSummaryByResource.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByResourceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByResourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCostSummaryByResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCostSummaryByResourceResponse()
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


    def DescribeDealsByCond(self, request):
        """查询订单

        :param request: Request instance for DescribeDealsByCond.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDealsByCondRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDealsByCondResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDealsByCond", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDealsByCondResponse()
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


    def DescribeDosageCosDetailByDate(self, request):
        """获取COS产品用量明细

        :param request: Request instance for DescribeDosageCosDetailByDate.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDosageCosDetailByDateRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDosageCosDetailByDateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDosageCosDetailByDate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDosageCosDetailByDateResponse()
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


    def DescribeDosageDetailByDate(self, request):
        """按日期获取产品用量明细

        :param request: Request instance for DescribeDosageDetailByDate.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDosageDetailByDateRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDosageDetailByDateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDosageDetailByDate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDosageDetailByDateResponse()
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


    def PayDeals(self, request):
        """支付订单

        :param request: Request instance for PayDeals.
        :type request: :class:`tencentcloud.billing.v20180709.models.PayDealsRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.PayDealsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PayDeals", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PayDealsResponse()
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