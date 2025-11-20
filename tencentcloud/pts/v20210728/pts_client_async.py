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
from tencentcloud.pts.v20210728 import models
from typing import Dict


class PtsClient(AbstractClient):
    _apiVersion = '2021-07-28'
    _endpoint = 'pts.tencentcloudapi.com'
    _service = 'pts'

    async def AbortCronJobs(
            self,
            request: models.AbortCronJobsRequest,
            opts: Dict = None,
    ) -> models.AbortCronJobsResponse:
        """
        停止定时任务
        """
        
        kwargs = {}
        kwargs["action"] = "AbortCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AbortJob(
            self,
            request: models.AbortJobRequest,
            opts: Dict = None,
    ) -> models.AbortJobResponse:
        """
        停止任务
        """
        
        kwargs = {}
        kwargs["action"] = "AbortJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustJobSpeed(
            self,
            request: models.AdjustJobSpeedRequest,
            opts: Dict = None,
    ) -> models.AdjustJobSpeedResponse:
        """
        调整任务的目标RPS
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustJobSpeed"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustJobSpeedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyScenario(
            self,
            request: models.CopyScenarioRequest,
            opts: Dict = None,
    ) -> models.CopyScenarioResponse:
        """
        复制场景
        """
        
        kwargs = {}
        kwargs["action"] = "CopyScenario"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyScenarioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlertChannel(
            self,
            request: models.CreateAlertChannelRequest,
            opts: Dict = None,
    ) -> models.CreateAlertChannelResponse:
        """
        创建告警通知接收组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlertChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlertChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCronJob(
            self,
            request: models.CreateCronJobRequest,
            opts: Dict = None,
    ) -> models.CreateCronJobResponse:
        """
        创建定时任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCronJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCronJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        创建环境
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFile(
            self,
            request: models.CreateFileRequest,
            opts: Dict = None,
    ) -> models.CreateFileResponse:
        """
        创建文件
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        创建项目
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScenario(
            self,
            request: models.CreateScenarioRequest,
            opts: Dict = None,
    ) -> models.CreateScenarioResponse:
        """
        创建场景
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScenario"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScenarioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlertChannel(
            self,
            request: models.DeleteAlertChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteAlertChannelResponse:
        """
        删除告警通知接收组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlertChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlertChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCronJobs(
            self,
            request: models.DeleteCronJobsRequest,
            opts: Dict = None,
    ) -> models.DeleteCronJobsResponse:
        """
        删除定时任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironments(
            self,
            request: models.DeleteEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentsResponse:
        """
        删除环境
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFiles(
            self,
            request: models.DeleteFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteFilesResponse:
        """
        删除文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJobs(
            self,
            request: models.DeleteJobsRequest,
            opts: Dict = None,
    ) -> models.DeleteJobsResponse:
        """
        删除任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjects(
            self,
            request: models.DeleteProjectsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectsResponse:
        """
        删除项目
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScenarios(
            self,
            request: models.DeleteScenariosRequest,
            opts: Dict = None,
    ) -> models.DeleteScenariosResponse:
        """
        删除场景
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScenarios"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScenariosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertChannels(
            self,
            request: models.DescribeAlertChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertChannelsResponse:
        """
        查询告警通知接收组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertRecords(
            self,
            request: models.DescribeAlertRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertRecordsResponse:
        """
        返回告警历史项的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableMetrics(
            self,
            request: models.DescribeAvailableMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableMetricsResponse:
        """
        查询系统支持的指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckSummary(
            self,
            request: models.DescribeCheckSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckSummaryResponse:
        """
        查询检查点汇总信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCronJobs(
            self,
            request: models.DescribeCronJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeCronJobsResponse:
        """
        列出定时任务，非必填数组为空就默认全选
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        查看环境列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeErrorSummary(
            self,
            request: models.DescribeErrorSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeErrorSummaryResponse:
        """
        查询错误详情汇总信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeErrorSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeErrorSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFiles(
            self,
            request: models.DescribeFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeFilesResponse:
        """
        查询文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        查询任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLabelValues(
            self,
            request: models.DescribeLabelValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeLabelValuesResponse:
        """
        查询标签内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLabelValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLabelValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricLabelWithValues(
            self,
            request: models.DescribeMetricLabelWithValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricLabelWithValuesResponse:
        """
        查询指标所有的label及values值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricLabelWithValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricLabelWithValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNormalLogs(
            self,
            request: models.DescribeNormalLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeNormalLogsResponse:
        """
        压测过程日志包括引擎输出日志及用户输出日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNormalLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNormalLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        查询项目列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        查询地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRequestSummary(
            self,
            request: models.DescribeRequestSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeRequestSummaryResponse:
        """
        查询请求汇总信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRequestSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRequestSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleBatchQuery(
            self,
            request: models.DescribeSampleBatchQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleBatchQueryResponse:
        """
        批量查询指标，返回固定时间点指标内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleBatchQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleBatchQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleLogs(
            self,
            request: models.DescribeSampleLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleLogsResponse:
        """
        查询采样日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleMatrixBatchQuery(
            self,
            request: models.DescribeSampleMatrixBatchQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleMatrixBatchQueryResponse:
        """
        批量查询指标矩阵
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleMatrixBatchQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleMatrixBatchQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleMatrixQuery(
            self,
            request: models.DescribeSampleMatrixQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleMatrixQueryResponse:
        """
        查询指标矩阵
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleMatrixQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleMatrixQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSampleQuery(
            self,
            request: models.DescribeSampleQueryRequest,
            opts: Dict = None,
    ) -> models.DescribeSampleQueryResponse:
        """
        查询指标，返回固定时间点指标内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSampleQuery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSampleQueryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenarioWithJobs(
            self,
            request: models.DescribeScenarioWithJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeScenarioWithJobsResponse:
        """
        查询场景配置并附带已经执行的任务内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenarioWithJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenarioWithJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScenarios(
            self,
            request: models.DescribeScenariosRequest,
            opts: Dict = None,
    ) -> models.DescribeScenariosResponse:
        """
        查询场景列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScenarios"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScenariosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateTmpKey(
            self,
            request: models.GenerateTmpKeyRequest,
            opts: Dict = None,
    ) -> models.GenerateTmpKeyResponse:
        """
        生成临时COS凭证
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateTmpKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateTmpKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartCronJobs(
            self,
            request: models.RestartCronJobsRequest,
            opts: Dict = None,
    ) -> models.RestartCronJobsResponse:
        """
        重启状态为已中止的定时任务
        """
        
        kwargs = {}
        kwargs["action"] = "RestartCronJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartCronJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartJob(
            self,
            request: models.StartJobRequest,
            opts: Dict = None,
    ) -> models.StartJobResponse:
        """
        创建并启动任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCronJob(
            self,
            request: models.UpdateCronJobRequest,
            opts: Dict = None,
    ) -> models.UpdateCronJobResponse:
        """
        更新定时任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCronJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCronJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEnvironment(
            self,
            request: models.UpdateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.UpdateEnvironmentResponse:
        """
        更新环境
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFileScenarioRelation(
            self,
            request: models.UpdateFileScenarioRelationRequest,
            opts: Dict = None,
    ) -> models.UpdateFileScenarioRelationResponse:
        """
        更新关联文件场景
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFileScenarioRelation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFileScenarioRelationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateJob(
            self,
            request: models.UpdateJobRequest,
            opts: Dict = None,
    ) -> models.UpdateJobResponse:
        """
        更新任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProject(
            self,
            request: models.UpdateProjectRequest,
            opts: Dict = None,
    ) -> models.UpdateProjectResponse:
        """
        更新项目
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateScenario(
            self,
            request: models.UpdateScenarioRequest,
            opts: Dict = None,
    ) -> models.UpdateScenarioResponse:
        """
        更新场景
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateScenario"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateScenarioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)