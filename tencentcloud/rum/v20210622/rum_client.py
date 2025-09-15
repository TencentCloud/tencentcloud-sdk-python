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
from tencentcloud.rum.v20210622 import models


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.tencentcloudapi.com'
    _service = 'rum'


    def CreateProject(self, request):
        r"""创建 RUM 应用（归属于某个团队）

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReleaseFile(self, request):
        r"""创建对应项目的文件记录

        :param request: Request instance for CreateReleaseFile.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateReleaseFileRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateReleaseFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReleaseFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReleaseFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStarProject(self, request):
        r"""个人用户添加星标项目

        :param request: Request instance for CreateStarProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateStarProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateStarProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStarProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStarProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTawInstance(self, request):
        r"""创建 RUM 业务系统

        :param request: Request instance for CreateTawInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateTawInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateTawInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTawInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTawInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWhitelist(self, request):
        r"""创建白名单

        :param request: Request instance for CreateWhitelist.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateWhitelistRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        r"""删除实例，谨慎操作，不可恢复

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProject(self, request):
        r"""删除给定的 rum 的项目

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReleaseFile(self, request):
        r"""将对应 sourcemap 文件删除

        :param request: Request instance for DeleteReleaseFile.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteReleaseFileRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteReleaseFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReleaseFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReleaseFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStarProject(self, request):
        r"""删除用户名下的星标项目

        :param request: Request instance for DeleteStarProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteStarProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteStarProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStarProject", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStarProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWhitelist(self, request):
        r"""删除白名单

        :param request: Request instance for DeleteWhitelist.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteWhitelistRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppDimensionMetrics(self, request):
        r"""用于查询 app 监控多维分析数据

        :param request: Request instance for DescribeAppDimensionMetrics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppDimensionMetricsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppDimensionMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppDimensionMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppDimensionMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppMetricsData(self, request):
        r"""获取 app 监控指标数据

        :param request: Request instance for DescribeAppMetricsData.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppMetricsDataRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppMetricsDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppMetricsData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppMetricsDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppSingleCaseDetailList(self, request):
        r"""查询 app 监控个例样本详情列表

        :param request: Request instance for DescribeAppSingleCaseDetailList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseDetailListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppSingleCaseDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppSingleCaseDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppSingleCaseList(self, request):
        r"""查询 app 监控个例聚合列表

        :param request: Request instance for DescribeAppSingleCaseList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeAppSingleCaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppSingleCaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppSingleCaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeData(self, request):
        r"""转发monitor查询

        :param request: Request instance for DescribeData.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataCustomUrl(self, request):
        r"""获取DescribeDataCustomUrl信息

        :param request: Request instance for DescribeDataCustomUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataCustomUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataCustomUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataCustomUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEventUrl(self, request):
        r"""获取DescribeDataEventUrl信息

        :param request: Request instance for DescribeDataEventUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataEventUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEventUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEventUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFetchProject(self, request):
        r"""获取DescribeDataFetchProject信息。已下线，请使用DescribeDataFetchUrl

        :param request: Request instance for DescribeDataFetchProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFetchProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFetchUrl(self, request):
        r"""获取DescribeDataFetchUrl信息

        :param request: Request instance for DescribeDataFetchUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFetchUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataFetchUrlInfo(self, request):
        r"""获取DescribeDataFetchUrlInfo信息

        :param request: Request instance for DescribeDataFetchUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataFetchUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataFetchUrlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataFetchUrlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataLogUrlInfo(self, request):
        r"""获取loginfo信息

        :param request: Request instance for DescribeDataLogUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataLogUrlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataLogUrlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataLogUrlStatistics(self, request):
        r"""获取LogUrlStatistics信息

        :param request: Request instance for DescribeDataLogUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataLogUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataLogUrlStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataLogUrlStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPerformancePage(self, request):
        r"""获取PerformancePage信息

        :param request: Request instance for DescribeDataPerformancePage.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformancePageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPerformancePage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPerformancePageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPvUrlInfo(self, request):
        r"""获取PvUrlInfo信息

        :param request: Request instance for DescribeDataPvUrlInfo.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlInfoRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPvUrlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPvUrlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataPvUrlStatistics(self, request):
        r"""获取DescribeDataPvUrlStatistics信息

        :param request: Request instance for DescribeDataPvUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPvUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPvUrlStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPvUrlStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataReportCount(self, request):
        r"""获取项目上报量

        :param request: Request instance for DescribeDataReportCount.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataReportCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataReportCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataReportCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSetUrlStatistics(self, request):
        r"""获取DescribeDataSetUrlStatistics信息

        :param request: Request instance for DescribeDataSetUrlStatistics.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataSetUrlStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSetUrlStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSetUrlStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticProject(self, request):
        r"""获取DescribeDataStaticProject信息

        :param request: Request instance for DescribeDataStaticProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticResource(self, request):
        r"""获取DescribeDataStaticResource信息

        :param request: Request instance for DescribeDataStaticResource.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataStaticUrl(self, request):
        r"""获取DescribeDataStaticUrl信息

        :param request: Request instance for DescribeDataStaticUrl.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataStaticUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataStaticUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataStaticUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataWebVitalsPage(self, request):
        r"""获取DescribeDataWebVitalsPage信息，用户核心活动信息
        页面加载性能之Web Vitals。性能关键点

        :param request: Request instance for DescribeDataWebVitalsPage.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataWebVitalsPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataWebVitalsPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataWebVitalsPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeError(self, request):
        r"""获取首页错误信息

        :param request: Request instance for DescribeError.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeErrorRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeErrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeError", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeErrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectLimits(self, request):
        r"""获取应用上报抽样信息

        :param request: Request instance for DescribeProjectLimits.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeProjectLimitsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeProjectLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        r"""获取项目列表（实例创建的团队下的项目列表）

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePvList(self, request):
        r"""获取项目下的PV列表

        :param request: Request instance for DescribePvList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribePvListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribePvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseFileSign(self, request):
        r"""获取上传文件存储的临时密钥

        :param request: Request instance for DescribeReleaseFileSign.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFileSignRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFileSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseFileSign", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseFileSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseFiles(self, request):
        r"""获取应用对应sourcemap文件列表

        :param request: Request instance for DescribeReleaseFiles.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFilesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeReleaseFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumGroupLog(self, request):
        r"""获取项目下的日志聚合信息

        :param request: Request instance for DescribeRumGroupLog.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumGroupLogRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumGroupLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumGroupLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumGroupLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogExport(self, request):
        r"""获取项目下的日志列表（实例创建的项目下的日志列表）

        :param request: Request instance for DescribeRumLogExport.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogExports(self, request):
        r"""获取项目下的日志导出列表

        :param request: Request instance for DescribeRumLogExports.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumLogList(self, request):
        r"""获取项目下的日志列表（实例创建的项目下的日志列表）

        :param request: Request instance for DescribeRumLogList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRumStatsLogList(self, request):
        r"""获取项目下的日志列表，分钟级

        :param request: Request instance for DescribeRumStatsLogList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeRumStatsLogListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeRumStatsLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRumStatsLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRumStatsLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScores(self, request):
        r"""获取首页分数列表

        :param request: Request instance for DescribeScores.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeScoresRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeScoresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScores", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScoresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTawAreas(self, request):
        r"""查询片区信息

        :param request: Request instance for DescribeTawAreas.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTawAreasRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTawAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTawAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTawAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTawInstances(self, request):
        r"""查询实例信息

        :param request: Request instance for DescribeTawInstances.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeTawInstancesRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeTawInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTawInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTawInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUvList(self, request):
        r"""获取项目下的UV列表

        :param request: Request instance for DescribeUvList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeUvListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeUvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhitelists(self, request):
        r"""获取白名单列表

        :param request: Request instance for DescribeWhitelists.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeWhitelistsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeWhitelistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhitelists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhitelistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        r"""修改 RUM 业务系统

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProject(self, request):
        r"""修改 RUM 应用信息

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProjectLimit(self, request):
        r"""新增修改限流

        :param request: Request instance for ModifyProjectLimit.
        :type request: :class:`tencentcloud.rum.v20210622.models.ModifyProjectLimitRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ModifyProjectLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProjectLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProjectLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeInstance(self, request):
        r"""恢复 RUM 业务系统，恢复后，用户可以正常使用和上报数据

        :param request: Request instance for ResumeInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.ResumeInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ResumeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeProject(self, request):
        r"""恢复应用使用与上报数据

        :param request: Request instance for ResumeProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.ResumeProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.ResumeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeProject", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInstance(self, request):
        r"""停止实例

        :param request: Request instance for StopInstance.
        :type request: :class:`tencentcloud.rum.v20210622.models.StopInstanceRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.StopInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopProject(self, request):
        r"""停止项目使用与上报数据

        :param request: Request instance for StopProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.StopProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.StopProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopProject", params, headers=headers)
            response = json.loads(body)
            model = models.StopProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))