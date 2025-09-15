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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.svp.v20240125 import models


class SvpClient(AbstractClient):
    _apiVersion = '2024-01-25'
    _endpoint = 'svp.tencentcloudapi.com'
    _service = 'svp'


    def CreateSavingPlanOrder(self, request):
        r"""创建节省计划订单

        :param request: Request instance for CreateSavingPlanOrder.
        :type request: :class:`tencentcloud.svp.v20240125.models.CreateSavingPlanOrderRequest`
        :rtype: :class:`tencentcloud.svp.v20240125.models.CreateSavingPlanOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSavingPlanOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSavingPlanOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSavingPlanCoverage(self, request):
        r"""查询当前用户节省计划覆盖率明细数据，如无特别说明，金额单位均为元（国内站）或者美元（国际站）。

        :param request: Request instance for DescribeSavingPlanCoverage.
        :type request: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanCoverageRequest`
        :rtype: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanCoverageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSavingPlanCoverage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSavingPlanCoverageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSavingPlanDeduct(self, request):
        r"""查询节省计划抵扣明细

        :param request: Request instance for DescribeSavingPlanDeduct.
        :type request: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanDeductRequest`
        :rtype: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanDeductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSavingPlanDeduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSavingPlanDeductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSavingPlanOverview(self, request):
        r"""查用当前用户明细节省计划总览查询时段内的使用情况

        :param request: Request instance for DescribeSavingPlanOverview.
        :type request: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanOverviewRequest`
        :rtype: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSavingPlanOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSavingPlanOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSavingPlanUsage(self, request):
        r"""查用当前用户明细节省计划查询时段内的使用情况

        :param request: Request instance for DescribeSavingPlanUsage.
        :type request: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanUsageRequest`
        :rtype: :class:`tencentcloud.svp.v20240125.models.DescribeSavingPlanUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSavingPlanUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSavingPlanUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))