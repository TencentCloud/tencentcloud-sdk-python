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
from tencentcloud.rum.v20210622 import models
from typing import Dict


class RumClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'rum.tencentcloudapi.com'
    _service = 'rum'

    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        创建 RUM 应用（归属于某个团队）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReleaseFile(
            self,
            request: models.CreateReleaseFileRequest,
            opts: Dict = None,
    ) -> models.CreateReleaseFileResponse:
        """
        创建对应项目的文件记录
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReleaseFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReleaseFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStarProject(
            self,
            request: models.CreateStarProjectRequest,
            opts: Dict = None,
    ) -> models.CreateStarProjectResponse:
        """
        个人用户添加星标项目
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStarProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStarProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTawInstance(
            self,
            request: models.CreateTawInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateTawInstanceResponse:
        """
        创建 RUM 业务系统
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTawInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTawInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWhitelist(
            self,
            request: models.CreateWhitelistRequest,
            opts: Dict = None,
    ) -> models.CreateWhitelistResponse:
        """
        创建白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        删除实例，谨慎操作，不可恢复
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProject(
            self,
            request: models.DeleteProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectResponse:
        """
        删除给定的 rum 的项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReleaseFile(
            self,
            request: models.DeleteReleaseFileRequest,
            opts: Dict = None,
    ) -> models.DeleteReleaseFileResponse:
        """
        将对应 sourcemap 文件删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReleaseFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReleaseFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStarProject(
            self,
            request: models.DeleteStarProjectRequest,
            opts: Dict = None,
    ) -> models.DeleteStarProjectResponse:
        """
        删除用户名下的星标项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStarProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStarProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWhitelist(
            self,
            request: models.DeleteWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteWhitelistResponse:
        """
        删除白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppDimensionMetrics(
            self,
            request: models.DescribeAppDimensionMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeAppDimensionMetricsResponse:
        """
        用于查询 app 监控多维分析数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppDimensionMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppDimensionMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppMetricsData(
            self,
            request: models.DescribeAppMetricsDataRequest,
            opts: Dict = None,
    ) -> models.DescribeAppMetricsDataResponse:
        """
        获取 app 监控指标数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppMetricsData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppMetricsDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppSingleCaseDetailList(
            self,
            request: models.DescribeAppSingleCaseDetailListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppSingleCaseDetailListResponse:
        """
        查询 app 监控个例样本详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppSingleCaseDetailList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppSingleCaseDetailListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppSingleCaseList(
            self,
            request: models.DescribeAppSingleCaseListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppSingleCaseListResponse:
        """
        查询 app 监控个例聚合列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppSingleCaseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppSingleCaseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeData(
            self,
            request: models.DescribeDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDataResponse:
        """
        转发monitor查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataCustomUrl(
            self,
            request: models.DescribeDataCustomUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataCustomUrlResponse:
        """
        获取DescribeDataCustomUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataCustomUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataCustomUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEventUrl(
            self,
            request: models.DescribeDataEventUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEventUrlResponse:
        """
        获取DescribeDataEventUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEventUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEventUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchProject(
            self,
            request: models.DescribeDataFetchProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchProjectResponse:
        """
        获取DescribeDataFetchProject信息。已下线，请使用DescribeDataFetchUrl
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchUrl(
            self,
            request: models.DescribeDataFetchUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchUrlResponse:
        """
        获取DescribeDataFetchUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFetchUrlInfo(
            self,
            request: models.DescribeDataFetchUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFetchUrlInfoResponse:
        """
        获取DescribeDataFetchUrlInfo信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFetchUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFetchUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataLogUrlInfo(
            self,
            request: models.DescribeDataLogUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataLogUrlInfoResponse:
        """
        获取loginfo信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataLogUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataLogUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataLogUrlStatistics(
            self,
            request: models.DescribeDataLogUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataLogUrlStatisticsResponse:
        """
        获取LogUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataLogUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataLogUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPerformancePage(
            self,
            request: models.DescribeDataPerformancePageRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPerformancePageResponse:
        """
        获取PerformancePage信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPerformancePage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPerformancePageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPvUrlInfo(
            self,
            request: models.DescribeDataPvUrlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPvUrlInfoResponse:
        """
        获取PvUrlInfo信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPvUrlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPvUrlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataPvUrlStatistics(
            self,
            request: models.DescribeDataPvUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataPvUrlStatisticsResponse:
        """
        获取DescribeDataPvUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataPvUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataPvUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataReportCount(
            self,
            request: models.DescribeDataReportCountRequest,
            opts: Dict = None,
    ) -> models.DescribeDataReportCountResponse:
        """
        获取项目上报量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataReportCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataReportCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSetUrlStatistics(
            self,
            request: models.DescribeDataSetUrlStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSetUrlStatisticsResponse:
        """
        获取DescribeDataSetUrlStatistics信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSetUrlStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSetUrlStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticProject(
            self,
            request: models.DescribeDataStaticProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticProjectResponse:
        """
        获取DescribeDataStaticProject信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticResource(
            self,
            request: models.DescribeDataStaticResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticResourceResponse:
        """
        获取DescribeDataStaticResource信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataStaticUrl(
            self,
            request: models.DescribeDataStaticUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDataStaticUrlResponse:
        """
        获取DescribeDataStaticUrl信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataStaticUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataStaticUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataWebVitalsPage(
            self,
            request: models.DescribeDataWebVitalsPageRequest,
            opts: Dict = None,
    ) -> models.DescribeDataWebVitalsPageResponse:
        """
        获取DescribeDataWebVitalsPage信息，用户核心活动信息
        页面加载性能之Web Vitals。性能关键点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataWebVitalsPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataWebVitalsPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeError(
            self,
            request: models.DescribeErrorRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorResponse:
        """
        获取首页错误信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeError"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectLimits(
            self,
            request: models.DescribeProjectLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectLimitsResponse:
        """
        获取应用上报抽样信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        获取项目列表（实例创建的团队下的项目列表）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePvList(
            self,
            request: models.DescribePvListRequest,
            opts: Dict = None,
    ) -> models.DescribePvListResponse:
        """
        获取项目下的PV列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseFileSign(
            self,
            request: models.DescribeReleaseFileSignRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseFileSignResponse:
        """
        获取上传文件存储的临时密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseFileSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseFileSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseFiles(
            self,
            request: models.DescribeReleaseFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseFilesResponse:
        """
        获取应用对应sourcemap文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumGroupLog(
            self,
            request: models.DescribeRumGroupLogRequest,
            opts: Dict = None,
    ) -> models.DescribeRumGroupLogResponse:
        """
        获取项目下的日志聚合信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumGroupLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumGroupLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExport(
            self,
            request: models.DescribeRumLogExportRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportResponse:
        """
        获取项目下的日志列表（实例创建的项目下的日志列表）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogExports(
            self,
            request: models.DescribeRumLogExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogExportsResponse:
        """
        获取项目下的日志导出列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumLogList(
            self,
            request: models.DescribeRumLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeRumLogListResponse:
        """
        获取项目下的日志列表（实例创建的项目下的日志列表）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRumStatsLogList(
            self,
            request: models.DescribeRumStatsLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeRumStatsLogListResponse:
        """
        获取项目下的日志列表，分钟级
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRumStatsLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRumStatsLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScores(
            self,
            request: models.DescribeScoresRequest,
            opts: Dict = None,
    ) -> models.DescribeScoresResponse:
        """
        获取首页分数列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScores"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScoresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTawAreas(
            self,
            request: models.DescribeTawAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeTawAreasResponse:
        """
        查询片区信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTawAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTawAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTawInstances(
            self,
            request: models.DescribeTawInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeTawInstancesResponse:
        """
        查询实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTawInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTawInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUvList(
            self,
            request: models.DescribeUvListRequest,
            opts: Dict = None,
    ) -> models.DescribeUvListResponse:
        """
        获取项目下的UV列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhitelists(
            self,
            request: models.DescribeWhitelistsRequest,
            opts: Dict = None,
    ) -> models.DescribeWhitelistsResponse:
        """
        获取白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhitelists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhitelistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        修改 RUM 业务系统
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        修改 RUM 应用信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProjectLimit(
            self,
            request: models.ModifyProjectLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectLimitResponse:
        """
        新增修改限流
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProjectLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeInstance(
            self,
            request: models.ResumeInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeInstanceResponse:
        """
        恢复 RUM 业务系统，恢复后，用户可以正常使用和上报数据
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeProject(
            self,
            request: models.ResumeProjectRequest,
            opts: Dict = None,
    ) -> models.ResumeProjectResponse:
        """
        恢复应用使用与上报数据
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstance(
            self,
            request: models.StopInstanceRequest,
            opts: Dict = None,
    ) -> models.StopInstanceResponse:
        """
        停止实例
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopProject(
            self,
            request: models.StopProjectRequest,
            opts: Dict = None,
    ) -> models.StopProjectResponse:
        """
        停止项目使用与上报数据
        """
        
        kwargs = {}
        kwargs["action"] = "StopProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)