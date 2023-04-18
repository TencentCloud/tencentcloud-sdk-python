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
from tencentcloud.rum.v20210622 import models


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.tencentcloudapi.com'
    _service = 'rum'


    def CreateLogExport(self, request):
        """接口请求域名： rum.tencentcloudapi.com 。

        本接口用于创建日志下载任务

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for CreateLogExport.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateLogExportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOfflineLogConfig(self, request):
        """创建离线日志监听，对应用户的离线日志将上报

        :param request: Request instance for CreateOfflineLogConfig.
        :type request: :class:`tencentcloud.rum.v20210622.models.CreateOfflineLogConfigRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.CreateOfflineLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOfflineLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOfflineLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProject(self, request):
        """创建 RUM 应用（归属于某个团队）

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateReleaseFile(self, request):
        """创建对应项目的文件记录

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStarProject(self, request):
        """个人用户添加星标项目

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTawInstance(self, request):
        """创建 RUM 业务系统

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWhitelist(self, request):
        """创建白名单

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteInstance(self, request):
        """删除实例，谨慎操作，不可恢复

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLogExport(self, request):
        """接口请求域名： rum.tencentcloudapi.com 。

        本接口用于删除日志下载任务

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for DeleteLogExport.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteLogExportRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteLogExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteOfflineLogConfig(self, request):
        """删除 rum 离线日志监听 - 对应用户的离线日志将不会上报

        :param request: Request instance for DeleteOfflineLogConfig.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogConfigRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOfflineLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOfflineLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteOfflineLogRecord(self, request):
        """删除对应的离线日志记录

        :param request: Request instance for DeleteOfflineLogRecord.
        :type request: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogRecordRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DeleteOfflineLogRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOfflineLogRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOfflineLogRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteProject(self, request):
        """删除给定的 rum 的项目

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteReleaseFile(self, request):
        """将对应 sourcemap 文件删除

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteStarProject(self, request):
        """删除用户名下的星标项目

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWhitelist(self, request):
        """删除白名单

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAppDimensionMetrics(self, request):
        """用于查询 app 监控多维分析数据

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAppMetricsData(self, request):
        """获取 app 监控指标数据

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAppSingleCaseDetailList(self, request):
        """查询 app 监控个例样本详情列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAppSingleCaseList(self, request):
        """查询 app 监控个例聚合列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeData(self, request):
        """转发monitor查询

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataCustomUrl(self, request):
        """获取DescribeDataCustomUrl信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataEventUrl(self, request):
        """获取DescribeDataEventUrl信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataFetchProject(self, request):
        """获取DescribeDataFetchProject信息。已下线，请使用DescribeDataFetchUrl

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataFetchUrl(self, request):
        """获取DescribeDataFetchUrl信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataFetchUrlInfo(self, request):
        """获取DescribeDataFetchUrlInfo信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataLogUrlInfo(self, request):
        """获取loginfo信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataLogUrlStatistics(self, request):
        """获取LogUrlStatistics信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataPerformancePage(self, request):
        """获取PerformancePage信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataPerformanceProject(self, request):
        """获取PerformanceProject信息

        :param request: Request instance for DescribeDataPerformanceProject.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformanceProjectRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeDataPerformanceProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataPerformanceProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataPerformanceProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataPvUrlInfo(self, request):
        """获取PvUrlInfo信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataPvUrlStatistics(self, request):
        """获取DescribeDataPvUrlStatistics信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataReportCount(self, request):
        """获取项目上报量

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataSetUrlStatistics(self, request):
        """获取DescribeDataSetUrlStatistics信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataStaticProject(self, request):
        """获取DescribeDataStaticProject信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataStaticResource(self, request):
        """获取DescribeDataStaticResource信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataStaticUrl(self, request):
        """获取DescribeDataStaticUrl信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataWebVitalsPage(self, request):
        """获取DescribeDataWebVitalsPage信息，用户核心活动信息
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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeError(self, request):
        """获取首页错误信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogExports(self, request):
        """接口请求域名： rum.tencentcloudapi.com 。

        本接口用于获取日志下载任务列表

        默认接口请求频率限制：20次/秒

        :param request: Request instance for DescribeLogExports.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLogExportsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLogExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogList(self, request):
        """(已下线，请用DescribeRumLogList)

        :param request: Request instance for DescribeLogList.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeLogListRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOfflineLogConfigs(self, request):
        """获取设置的离线日志监听配置 - 返回设置的用户唯一标识

        :param request: Request instance for DescribeOfflineLogConfigs.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogConfigsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineLogConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineLogConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOfflineLogRecords(self, request):
        """获取所有离线日志记录(最多100条)

        :param request: Request instance for DescribeOfflineLogRecords.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogRecordsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineLogRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineLogRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOfflineLogs(self, request):
        """获取对应离线日志

        :param request: Request instance for DescribeOfflineLogs.
        :type request: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogsRequest`
        :rtype: :class:`tencentcloud.rum.v20210622.models.DescribeOfflineLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjectLimits(self, request):
        """获取应用上报抽样信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjects(self, request):
        """获取项目列表（实例创建的团队下的项目列表）

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePvList(self, request):
        """获取项目下的PV列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReleaseFileSign(self, request):
        """获取上传文件存储的临时密钥

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReleaseFiles(self, request):
        """获取应用对应sourcemap文件列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRumGroupLog(self, request):
        """获取项目下的日志聚合信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRumLogExport(self, request):
        """获取项目下的日志列表（实例创建的项目下的日志列表）

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRumLogExports(self, request):
        """获取项目下的日志导出列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRumLogList(self, request):
        """获取项目下的日志列表（实例创建的项目下的日志列表）

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRumStatsLogList(self, request):
        """获取项目下的日志列表，分钟级

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScores(self, request):
        """获取首页分数列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTawAreas(self, request):
        """查询片区信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTawInstances(self, request):
        """查询实例信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUvList(self, request):
        """获取项目下的UV列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWhitelists(self, request):
        """获取白名单列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstance(self, request):
        """修改 RUM 业务系统

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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProject(self, request):
        """修改 RUM 应用信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProjectLimit(self, request):
        """新增修改限流

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
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeInstance(self, request):
        """恢复 RUM 业务系统，恢复后，用户可以正常使用和上报数据

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
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeProject(self, request):
        """恢复应用使用与上报数据

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
                raise TencentCloudSDKException(e.message, e.message)


    def StopInstance(self, request):
        """停止实例

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
                raise TencentCloudSDKException(e.message, e.message)


    def StopProject(self, request):
        """停止项目使用与上报数据

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
                raise TencentCloudSDKException(e.message, e.message)