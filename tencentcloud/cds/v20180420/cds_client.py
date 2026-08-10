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
from tencentcloud.cds.v20180420 import models


class CdsClient(AbstractClient):
    _apiVersion = '2018-04-20'
    _endpoint = 'cds.tencentcloudapi.com'
    _service = 'cds'


    def CreateReportPdf(self, request):
        r"""下载报表PDF

        :param request: Request instance for CreateReportPdf.
        :type request: :class:`tencentcloud.cds.v20180420.models.CreateReportPdfRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.CreateReportPdfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReportPdf", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReportPdfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTimerReport(self, request):
        r"""新建报表任务

        :param request: Request instance for CreateTimerReport.
        :type request: :class:`tencentcloud.cds.v20180420.models.CreateTimerReportRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.CreateTimerReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTimerReport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTimerReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetsList(self, request):
        r"""查询资产列表

        :param request: Request instance for DescribeAssetsList.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeAssetsListRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeAssetsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbauditInstanceType(self, request):
        r"""本接口 (DescribeDbauditInstanceType) 用于查询可售卖的产品规格列表。

        :param request: Request instance for DescribeDbauditInstanceType.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstanceTypeRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstanceTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbauditInstanceType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbauditInstanceTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbauditInstances(self, request):
        r"""本接口 (DescribeDbauditInstances) 用于查询数据安全审计实例列表

        :param request: Request instance for DescribeDbauditInstances.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstancesRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbauditInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbauditInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbauditUsedRegions(self, request):
        r"""本接口 (DescribeDbauditUsedRegions) 用于查询可售卖地域列表。

        :param request: Request instance for DescribeDbauditUsedRegions.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditUsedRegionsRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditUsedRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbauditUsedRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbauditUsedRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportList(self, request):
        r"""查询报表列表

        :param request: Request instance for DescribeReportList.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeReportListRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReportMissionList(self, request):
        r"""查询报表任务列表

        :param request: Request instance for DescribeReportMissionList.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeReportMissionListRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeReportMissionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReportMissionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReportMissionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceDbauditInstance(self, request):
        r"""用于查询数据安全审计产品实例价格

        :param request: Request instance for InquiryPriceDbauditInstance.
        :type request: :class:`tencentcloud.cds.v20180420.models.InquiryPriceDbauditInstanceRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.InquiryPriceDbauditInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceDbauditInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceDbauditInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDbauditInstancesRenewFlag(self, request):
        r"""本接口 (ModifyDbauditInstancesRenewFlag) 用于修改数据安全审计产品实例续费标识

        :param request: Request instance for ModifyDbauditInstancesRenewFlag.
        :type request: :class:`tencentcloud.cds.v20180420.models.ModifyDbauditInstancesRenewFlagRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.ModifyDbauditInstancesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDbauditInstancesRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDbauditInstancesRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))